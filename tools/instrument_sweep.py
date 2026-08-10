#!/usr/bin/env python3
"""instrument_sweep.py — the mechanical half of 08-THE-INSTRUMENTS.md.

WHY THIS EXISTS. `07-THE-CLAIMS-REGISTER.md` holds what the book ASSERTS and ships with
`claim_sweep.py`. Nothing held what the book MEASURES WITH, and that single absence was the
structural cause of five rows (R-54, R-86, R-87, R-88, R-89, R-90). R-91 ruled one register
rather than four bespoke gauges, because four gauges is the disease performed in the repair.

WHAT THE PREVIOUS GAUGE DID WRONG, since this file is its replacement and not its friend.
`card_sweep.py` decides a chapter performed the book's central form like this:

    carded = all(counts[f] for f in DIAGNOSTIC)        # DIAGNOSTIC = ("null", "compl")

Threshold one, anywhere in the file, any context, no mention/use filter. So VII.2 — which
prints no card and merely QUOTES Book IV's cards four times — scored `✓ CARDED`, and that
false positive reached `handoff.json` as "VII.1 and VII.2 are already carding." Its docstring
declares the limit correctly ("trusted DOWNWARD only, a zero is evidence") and then the output
column prints a verdict the method cannot license. That is R-90's defect — honest label, no
coupling to what may be asserted — occurring in a gauge instead of a grade note.

HOW THIS ONE DIFFERS: IT IS STRUCTURAL, NOT LEXICAL. It looks for card FIELD LABELS in the
three renders the register records, and requires MIN_FIELDS distinct labels inside a WINDOW of
lines. A chapter citing another chapter's null space scores zero, because a citation is one
label in running prose and never three in a block. The output reports the VERSION matched, so
an undeclared form change is visible the day it lands rather than five chapters later.

WHAT THIS IS NOT. It cannot tell a good card from a bad one, and it cannot read. It catches an
undeclared FORM, an ordinal printed without a use-log, and a corpus count printed after the
suspension. A determined author defeats it trivially. Seatbelt, not proof.

USAGE
    python tools/instrument_sweep.py              # everything
    python tools/instrument_sweep.py --cards       # card form/version table only
    python tools/instrument_sweep.py --bindings    # forward bindings only
    python tools/instrument_sweep.py VI            # one book

EXIT CODE: 1 if the register slot disagrees with the headings, or any forward binding is
breached, else 0. An UNDECLARED historical form is reported and does NOT fail the build —
v1/v2/v3 are recorded-not-repaired by ruling, and a gauge that fails on known history is a
gauge that gets switched off within a week.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
BOOK = REPO / "book"
REGISTER = REPO / "08-THE-INSTRUMENTS.md"

# The chapter from which the v3-canonical form, the ordinal ban and the corpus-count
# suspension all bind. Declared in 08-THE-INSTRUMENTS.md; changing it here changes nothing.
BINDS_FROM = ("VII", 3)

# ---------------------------------------------------------------------------
# Card field labels, per recorded version. Each entry: (field, compiled pattern).
# Patterns anchor on the LABEL, not on the vocabulary, which is the whole point.
# ---------------------------------------------------------------------------
VERSIONS = {
    "v1": [
        ("sees", r"\*\*SEES:?\*\*"),
        ("null", r"\*\*NULL SPACE:?\*\*"),
        ("compl", r"\*\*COMPLEMENTS:?\*\*"),
        ("bound", r"\*\*BOUNDARY:?\*\*"),
        ("navig", r"\*\*NAVIGATIONAL IMPLICATION:?\*\*"),
    ],
    # IV.9's fork — found by this tool on the day the register was written, and the reason
    # the register's "Book IV never moved" claim had to be withdrawn. A contour, not an
    # entity: four of v1's five fields are absent and `What would make this wrong` is a
    # field that occurs nowhere else in the book.
    "v1b": [
        ("shape", r"\*\*SHAPE:?\*\*"),
        ("where", r"\*\*WHERE IT SHOWS:?\*\*"),
        ("isnot", r"\*\*WHAT IT IS NOT:?\*\*"),
        ("navig", r"\*\*NAVIGATIONAL IMPLICATION:?\*\*"),
        ("wrong", r"\*\*What would make this wrong:?\*\*"),
    ],
    "v2": [
        ("whose", r"\*\*(?:Whose|Era):\*\*"),
        ("compl", r"\*\*Complement[^*]{0,60}?:?\*\*"),
        ("null", r"\*\*Null space:?\*\*"),
        # `Mechanism of the exclusion` (VI.4) OR the shortened `Mechanism` (VI.5+). Both
        # matched so the field is SEEN; which one is reported by --mech-label below,
        # because the shortening is itself the defect and a gauge that folds them together
        # is the gauge that missed it.
        ("mech", r"\*\*Mechanism(?: of the exclusion)?:?\*\*"),
        ("navig", r"\*\*Navigational implication:?\*\*"),
    ],
    "v3": [
        ("compl", r"\*What it renders superbly[^*]{0,80}?\*"),
        ("null", r"\*Its null space:\*"),
        ("bound", r"\*Its boundary:\*"),
        ("mech", r"\*Mechanism:\*"),
        ("navig", r"\*Navigational implication[^*]{0,80}?:\*"),
    ],
}

# v3-canonical: the ruled form. Labels are FIXED STRINGS — the clause-carrying labels of
# VI.7/VI.8 are precisely what made the card uncheckable, so the canonical form forbids them.
CANONICAL = [
    ("whose", r"\*\*(?:Whose|Era):\*\*"),
    ("compl", r"\*\*Complement:\*\*"),
    ("null", r"\*\*Null space:\*\*"),
    ("bound", r"\*\*Boundary:\*\*"),
    ("mech", r"\*\*Mechanism of the exclusion:\*\*"),
    ("navig", r"\*\*Navigational implication:\*\*"),
]

MIN_FIELDS = 3      # distinct labels required to call it a card
WINDOW = 40         # ...within this many lines

ORDINAL = re.compile(
    r"\b(?:second|third|fourth|fifth|sixth|seventh|eighth)\s+time\s+in\s+this\s+book\b", re.I
)
# A corpus count as EVIDENCE. ⚠ THE FIRST VERSION OF THIS PATTERN CAUGHT NONE OF THE THREE
# COUNTS IT WAS WRITTEN FOR. It required the number ADJACENT to a file word, and the real
# prose does not oblige: VI.4 prints "across 2,550 research documents" (the `.md` is twenty
# words upstream), VI.7 prints "over 2,586 live files" (a word intervenes). A gauge whose
# pattern is fitted to the example rather than the class — and it PASSED, vacuously, because
# no bound chapter exists yet. A null with no positive control. So: any thousands-separated
# figure in bound book prose is a corpus count until a human says otherwise. Book prose has
# almost no other use for one, and a false positive here costs a glance.
# ⚠ AND "any thousands-separated figure" was too broad in turn: it fired on VI.6:365,
# `N = 4,965 completing both surveys` — a cited paper's SAMPLE SIZE, which I4 below
# explicitly LICENSES at abstract-only grade. A gauge that flags every correctly-sourced
# trial is a gauge switched off inside a week, which is the real failure mode of a checker.
# So the discriminator is what a corpus count actually IS: a count of THIS PROJECT'S FILES.
# Number and file-word on the same line. Catches all three true positives, drops the N.
#   ⛔ DECLARED LIMIT: this cannot catch VI.6's real defect, which is a denominator
#   REFERENCED without a figure ("the same corpus", two candidates, no number). A count
#   that prints no number is invisible here. That half of R-87 stays human-found.
CORPUS_COUNT = re.compile(
    r"\b\d{1,3},\d{3}\b(?=.*(?:\.md|\.txt|files|documents|essays|corpus|archive))"
    r"|(?:\.md|\.txt|files|documents|essays|corpus|archive).*?\b\d{1,3},\d{3}\b",
    re.I,
)
# Talking ABOUT the ban is not breaching it — but ⚠ THE FIRST VERSION OF THIS FILTER
# SUPPRESSED A TRUE POSITIVE. It listed `licen[cs]`, `register`, `instrument`, `ban`,
# `forbid` — every one of them a word this book argues in ordinary prose. VI.7:125 ("C30 is
# licensed here explicitly, for the fourth time in this book") was silently dropped for
# containing "licensed". The mention/use problem, overcorrected into suppression, in the
# gauge whose whole subject is instruments that overclaim. Bound chapters are book prose and
# carry no queue apparatus, so this can be narrow — it exists only so a footnote QUOTING a
# rule, or this register's own text, does not trip.
# ⚠ AND `R-\d+` HAD TO COME OUT TOO, third pass. The book's own grade notes cite row
# numbers — VI.4:433 "the scope declared at R-67", VI.5:347 "a wider scope than R-67's
# declared 2,550" — so an R-number is a mark of CAREFUL PROSE here, not of apparatus. It was
# suppressing the two loudest corpus counts in the book. Every iteration of this filter has
# failed in the same direction: toward silence. Recorded because the direction is the finding.
META = re.compile(
    r"⛔|08-THE-INSTRUMENTS|does not license|may not print|SUSPENDED|rhetoric wearing",
    re.I,
)


def chapters(book: str | None = None):
    pat = f"{book}-*.md" if book else "*-*.md"
    out = []
    for p in sorted(BOOK.glob(pat)):
        m = re.match(r"^([IVX]+)-(\d+)-", p.name)
        if m:
            out.append((m.group(1), int(m.group(2)), p))
    return out


ROMAN = {"I": 1, "II": 2, "III": 3, "IV": 4, "V": 5, "VI": 6, "VII": 7, "VIII": 8, "IX": 9}


def at_or_after(bk: str, n: int, ref: tuple[str, int]) -> bool:
    a, b = ROMAN.get(bk, 0), ROMAN.get(ref[0], 0)
    return a > b or (a == b and n >= ref[1])


def detect_cards(lines: list[str]) -> list[tuple[str, list[str], int]]:
    """Every card block in the file, as (version, fields, line_no), in document order.

    ⚠ THE FIRST-OCCURRENCE BUG, kept as a comment because it is the same class as
    everything else in this register. The first version of this function recorded only the
    FIRST hit per field and then windowed. So IV.6 — which defines `**SEES**` in running
    prose at L120 and then prints THREE cards from L173 — anchored `sees` at L120, put it
    40+ lines from the card, and reported 4 fields and one card. A gauge that silently
    loses instances of the thing it measures. Fixed by collecting ALL hits and sliding.
    """
    out: list[tuple[str, list[str], int]] = []
    for name, fields in list(VERSIONS.items()) + [("v3-canon", CANONICAL)]:
        hits: list[tuple[int, str]] = []
        for i, line in enumerate(lines):
            for field, pat in fields:
                if re.search(pat, line):
                    hits.append((i, field))
        if len({f for _, f in hits}) < MIN_FIELDS:
            continue
        used = -1
        for idx, (start, _) in enumerate(hits):
            if start <= used:
                continue
            near = {f for i, f in hits if start <= i < start + WINDOW}
            if len(near) >= MIN_FIELDS:
                out.append((name, sorted(near), start + 1))
                used = start + WINDOW - 1
    # A block can match two versions (v2 is a subset of v3-canon's vocabulary in places);
    # keep the richest match per line region, preferring the more specific version.
    out.sort(key=lambda t: (t[2], -len(t[1])))
    kept: list[tuple[str, list[str], int]] = []
    for ver, f, at in out:
        if kept and at - kept[-1][2] < WINDOW and ver != kept[-1][0]:
            if len(f) <= len(kept[-1][1]):
                continue
            kept[-1] = (ver, f, at)
            continue
        kept.append((ver, f, at))
    return kept


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("book", nargs="?", default=None)
    ap.add_argument("--cards", action="store_true")
    ap.add_argument("--bindings", action="store_true")
    args = ap.parse_args()
    all_sections = not (args.cards or args.bindings)
    fail = 0

    print("INSTRUMENT SWEEP — 08-THE-INSTRUMENTS.md, counted from disk")
    print("  structural: card FIELD LABELS in a block, not vocabulary anywhere in the file\n")

    # ---- the slot, same discipline as 07 ------------------------------------
    if all_sections:
        text = REGISTER.read_text(encoding="utf-8", errors="replace")
        m = re.search(r"INSTRUMENTS-REGISTERED:\s*(\d+)", text)
        declared = int(m.group(1)) if m else None
        actual = len(re.findall(r"^## I\d+ ", text, re.M))
        ok = declared == actual
        print(f"  SLOT   declared {declared} · headings {actual}   {'✓' if ok else '✗ ROTTED'}")
        if not ok:
            fail = 1
        print()

    rows = chapters(args.book)
    if not rows:
        print(f"no chapters found for {args.book or 'any book'}")
        return 1

    # ---- card form and version ---------------------------------------------
    if all_sections or args.cards:
        print("  CARD — form and version per chapter")
        current, seen_versions = None, {}
        for bk, n, path in rows:
            if bk != current:
                print(f"\n    BOOK {bk}")
                current = bk
            lines = path.read_text(encoding="utf-8", errors="replace").splitlines()
            cards = detect_cards(lines)
            if not cards:
                print(f"      {bk}.{n:<2} — no card")
                continue
            body = "\n".join(lines)
            for ci, (ver, fields, at) in enumerate(cards):
                seen_versions.setdefault(ver, []).append(f"{bk}.{n}")
                note = ""
                if at_or_after(bk, n, BINDS_FROM) and ver != "v3-canon":
                    note = "   ✗ BREACH — binds to v3-canonical"
                    fail = 1
                # The Mechanism label, reported separately: the collapse of the full name to
                # `Mechanism:` at VI.5 is the defect, and folding the two together is exactly
                # how it went unseen for four chapters and an outside read.
                if "mech" in fields:
                    if re.search(r"Mechanism of the exclusion:?\*", body):
                        note += "   mech=FULL"
                    else:
                        note += "   ⚠ mech=SHORT"
                        if at_or_after(bk, n, BINDS_FROM):
                            note += " ✗ BREACH"
                            fail = 1
                tag = f"{bk}.{n}" if ci == 0 else ""
                print(
                    f"      {tag:<6} {ver:<9} {len(fields)} fields @L{at:<4} "
                    f"[{' '.join(fields)}]{note}"
                )
            if len(cards) > 1:
                print(f"             ↑ {len(cards)} cards in this chapter")
        # CARDS, not chapters. The two are not the same number — IV.3 and IV.7 print four
        # each — and calling cards "chapters" here would be the exact unit slippage that
        # put three different denominators behind R-91's own population table.
        print("\n    versions in use — CARDS, and the chapters they fall in:")
        for v, chs in seen_versions.items():
            uniq = sorted(set(chs), key=chs.index)
            print(f"      {v:<9} {len(chs):>2} card(s) in {len(uniq):>2} chapter(s)   {', '.join(uniq)}")
        print(f"      {'TOTAL':<9} {sum(len(c) for c in seen_versions.values()):>2} card(s)")
        if len(seen_versions) > 1:
            print(
                f"    ⚠ {len(seen_versions)} forms live. v1/v2/v3 are RECORDED-NOT-REPAIRED "
                "by ruling; only a breach at/after "
                f"{BINDS_FROM[0]}.{BINDS_FROM[1]} fails."
            )
        print()

    # ---- forward bindings ---------------------------------------------------
    if all_sections or args.bindings:
        print(f"  FORWARD BINDINGS — enforced from {BINDS_FROM[0]}.{BINDS_FROM[1]}")
        breaches = 0
        for bk, n, path in rows:
            if not at_or_after(bk, n, BINDS_FROM):
                continue
            for i, line in enumerate(path.read_text(encoding="utf-8", errors="replace").splitlines(), 1):
                if META.search(line):
                    continue
                if ORDINAL.search(line):
                    print(f"      ✗ {bk}.{n}:{i}  ORDINAL without a use-log (I2 is v0)")
                    breaches += 1
                if CORPUS_COUNT.search(line):
                    print(f"      ✗ {bk}.{n}:{i}  CORPUS COUNT on the page (I3 SUSPENDED)")
                    breaches += 1
        if breaches:
            fail = 1
        else:
            print("      ✓ no ordinal and no corpus count in bound chapters")
        print()

    print("  ✗ FAIL" if fail else "  ✓ PASS")
    return fail


if __name__ == "__main__":
    sys.exit(main())
