#!/usr/bin/env python3
"""
BEAT BAN SWEEP — screen `06`'s beat lines against `05`'s ban list.

★ THIS TOOL EXISTS BECAUSE RULING 126 NAMED ITS OWN ABSENCE AND NOBODY BUILT IT.

Ruling 126, Day 188, verbatim: *"A BEAT LINE WRITTEN IN A BANNED WORD CAN NEVER
SCORE."* IV.1's beat 1 read *"mapped as far as an atlas can map its own
blindness"* — and `map` is banned by `05` §3b for our own instrument, the one
word Book IV may not use for the thing it is. The beat was therefore
**undeliverable without breaching the lexicon**: a permanent MISS that reads
exactly like a drafting failure. The drafter would have spent the session trying
to hit a target the lexicon forbids, and every gauge would have agreed with them.

The ruling then wrote down the hole in plain sight:

    ⚠ No gauge screens beat lines against the ban list — `claim_sweep` does not
      read `06`'s beats as prose. Book IV checked by hand and clean apart from
      beat 1; Books V–VIII unchecked, left open rather than claimed closed.

That is the household's signature defect with the trigger missing rather than
broken: **correct content, correctly filed, and nothing calls it.** It sat for a
day, and it sat pointing directly at the book about to be drafted.

WHY IT IS NOT A NEW SCOPE IN `claim_sweep`
------------------------------------------
The cheap version — add `06` to a scope — was tried on paper and refused. `06`
is 2,900 lines and most of them are RULINGS, which discuss banned terms
constantly and correctly; that is what a ruling about a banned term looks like.
Sweeping the file would bury a real beat breach under a hundred legitimate
mentions, and a gauge nobody can read is a gauge nobody runs. **The unit is the
beat line, not the file** — so this tool extracts beats with the same parser the
drafting gauges use (`beat_sweep.beats`, fixed Day 189) and hands ONLY those to
`claim_sweep`'s rule engine.

⚠ THE REUSE IS DELIBERATE AND SO IS ITS ONE COST. Beats are written to scratch
files named `V-02-beats.md` so that `claim_sweep`'s filename-keyed scopes
(`book-after-one`, `chapters-not-II-01`) resolve the way they would for real
prose. That means **no exemption in `claim_sweep.EXEMPTIONS` can fire here** —
they are keyed to real chapter paths. Correct for now (a beat has earned no
exemptions) and PRINTED on every run, because a suppression nobody can see is
one nobody audits, and the inverse — an exemption silently unavailable — would
make a beat look dirtier than it is.

POSITIVE CONTROL, AND THE RUN REFUSES WITHOUT IT
------------------------------------------------
A clean sweep from a screen that is not wired in is indistinguishable from a
clean scaffold — `claim_sweep`'s own lesson, one level up. So before any verdict
this tool plants ruling 126's ACTUAL defect (IV.1 beat 1's `map`) into a
synthetic beat and requires the screen to catch it. If the control misses, no
verdict is printed. A zero needs a positive control of the same shape.

    python tools/beat_ban_sweep.py               # all books
    python tools/beat_ban_sweep.py --book V      # one book
    python tools/beat_ban_sweep.py --control     # the control only
"""

import argparse
import re
import shutil
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import beat_sweep  # noqa: E402
import claim_sweep  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
SCAFFOLD = ROOT / "06-THE-SCAFFOLD.md"
BOOKS = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII"]

# Ruling 108's mark: drafter-voice clauses are wrapped in guillemets and stripped
# before the words are taken. A screen that read them would flag an instruction
# to the drafter as though it were a sentence owed to the page — which is the
# exact confusion ruling 108 was made to end.
GUILLEMETS = re.compile(r"«[^»]*»")

ROMAN = re.compile(r"^(I|II|III|IV|V|VI|VII|VIII)\.(\d+)$")


def beat_lines(book_filter=None):
    """Every beat in `06`, as (chapter_id, kind, index, text), drafter-voice stripped."""
    text = SCAFFOLD.read_text(encoding="utf-8")
    out = []
    for ch_id, _title, body in beat_sweep.chapters(text):
        m = ROMAN.match(ch_id)
        if not m:
            continue
        book = m.group(1)
        if book_filter and book != book_filter:
            continue
        for i, (kind, t) in enumerate(beat_sweep.beats(body), 1):
            stripped = GUILLEMETS.sub(" ", t)
            out.append((ch_id, book, kind, i, stripped, t))
    return out


def screen(items, label_note=True):
    """Run claim_sweep's rule engine over beat text via chapter-named scratch files."""
    tmpdir = Path(tempfile.mkdtemp(prefix="beatban_"))
    hits, mentions = [], []
    try:
        for ch_id, book, kind, i, stripped, raw in items:
            bk, num = ch_id.split(".")
            f = tmpdir / f"{bk}-{int(num):02d}-beats.md"
            f.write_text(stripped + "\n", encoding="utf-8")
            u, m, _e = claim_sweep.sweep_file(f, is_prose=True)
            for rule_id, _p, _n, line, why in u:
                hits.append((ch_id, kind, i, rule_id, line, why, raw))
            for rule_id, _p, _n, line, why in m:
                mentions.append((ch_id, kind, i, rule_id, line, why))
    finally:
        shutil.rmtree(tmpdir, ignore_errors=True)
    return hits, mentions


def control() -> bool:
    """Plant ruling 126's own defect and require the screen to catch it.

    `map` for our own instrument is `05` §3b. If this does not fire, the screen
    is not wired to the ban list and every clean run below is worthless.
    """
    planted = [("IV.1", "IV", "beat", 1,
                "the census mapped as far as an atlas can map its own blindness",
                "(control)")]
    hits, _ = screen(planted, label_note=False)
    ok = bool(hits)
    print("POSITIVE CONTROL — ruling 126's actual defect, replanted:")
    print("  beat: \"the census mapped as far as an atlas can map its own blindness\"")
    if ok:
        rules = sorted({h[3] for h in hits})
        print(f"  ✓ CAUGHT by {', '.join(rules)} — the screen is wired to the ban list.\n")
    else:
        print("  ✗ MISSED. The screen is NOT reading the ban list.")
        print("    Refusing to report a verdict; a clean run from a dead screen is a lie.\n")
    return ok


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[1])
    ap.add_argument("--book", choices=BOOKS, help="screen one book only")
    ap.add_argument("--control", action="store_true", help="run the positive control only")
    ap.add_argument("--show-mentions", action="store_true")
    args = ap.parse_args()

    print()
    if not control():
        return 2
    if args.control:
        return 0

    items = beat_lines(args.book)
    scope = f"Book {args.book}" if args.book else "all eight books"
    chapters = sorted({i[0] for i in items})
    marked = sum(1 for i in items if "«" in i[5])
    print(f"BEAT BAN SWEEP — {len(items)} beat(s) across {len(chapters)} chapter(s) · {scope}")
    print(f"  drafter-voice «…» marks stripped before screening: {marked} beat(s) carry one")
    print("  ⚠ claim_sweep exemptions CANNOT fire here (they are keyed to real chapter")
    print("    paths); a beat has earned none yet, and this line is so that stays visible.\n")

    hits, mentions = screen(items)

    if hits:
        print(f"!! {len(hits)} BEAT(S) WRITTEN IN A BANNED WORD — undeliverable as written:\n")
        for ch_id, kind, i, rule_id, line, why, raw in hits:
            print(f"  [{rule_id}] {ch_id} {kind} {i}")
            print(f"      {line}")
            print(f"      → {why[:220]}\n")
    else:
        print("  no USE-class hits in any beat line.\n")

    print(f"  {len(mentions)} mention(s) suppressed (the term NAMED, not used).")
    if args.show_mentions:
        for ch_id, kind, i, rule_id, line, _why in mentions:
            print(f"    [{rule_id}] {ch_id} {kind} {i}  {line[:110]}")

    # Coverage prints on every run. A screen that quietly covers less than it
    # claims is the stamp this whole apparatus exists to refuse.
    print("\n  COVERAGE — beats screened per book:")
    for b in BOOKS:
        n = sum(1 for i in items if i[1] == b)
        chs = len({i[0] for i in items if i[1] == b})
        mk = sum(1 for i in items if i[1] == b and "«" in i[5])
        flag = "" if mk or not n else "   ⚠ no drafter-voice marks (ruling 108 unapplied)"
        print(f"    Book {b:<4} {chs:>2} chapter(s)  {n:>3} beat(s)  {mk:>3} marked{flag}")

    return 1 if hits else 0


if __name__ == "__main__":
    raise SystemExit(main())
