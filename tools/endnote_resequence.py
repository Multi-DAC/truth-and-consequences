#!/usr/bin/env python3
"""
Resequence a chapter's endnotes so DEFINITION order matches BODY order. R2-072's repair hand.

WHY A TOOL AND NOT ELEVEN EDITS. `compile_pdf.py` numbers notes by definition order, so a body
that references 1·2·4·3 prints a superscript 4 two pages before a superscript 3. `endnote_order.py`
prices the defect; this pays it. Eleven chapters, 89 notes, one of them a ten-note resequence
(VII.4, `3·2·9·10·7·4·5·1·6·8`) — hand-swapping that is how you get ten right and the eleventh
silently wrong, which is the failure this whole checklist exists to stop.

⚠ THE HAZARD THE GAUGE CANNOT SEE, and the reason this file has a footer concept.
`endnote_order.py` reads BODY PROSE ONLY — everything above the first `[^n]:` line — because a
marker inside a note is a note citing a note, not something a reader meets in sequence. That rule
is right for measuring and blind for repairing. Two chapters (IV.6, VI.6) close with an unnumbered
*On the grade of the sources above* footer that sits AFTER the last definition and cites notes by
number: "[^1] is two-digitisation-grade", "Liu et al. [^8]". Those references are invisible to the
gauge, so a renumber that ignores them still reports a clean 0 inversions while the footer now
points a reader at the wrong source. Worse, a naive "split the tail on definition lines and sort"
carries the footer along inside whichever note happens to be defined last and files it into the
middle of the notes.

So: markers are remapped EVERYWHERE in the file; the footer is cut at its `---`, held out of the
sort, and pinned back at the end.

WHAT IT WILL NOT DO. It refuses any chapter with a note defined but never cited, a marker with no
definition, a non-numeric label, or a duplicate definition — because in each of those cases
"body appearance order" does not define a total order and the right answer is a human's. All 11
targets were swept clean of these before this was written; the guard is for the twelfth.

POST-CONDITIONS, asserted per file, not reported (assertions fail loudly; reports get skimmed):
  1. the body's marker sequence is exactly 1..N ascending
  2. every note block's text is byte-identical apart from its own label
  3. the body is byte-identical apart from markers
  4. the footer, if any, survives verbatim apart from markers
  5. the multiset of note bodies is preserved — nothing dropped, nothing duplicated

Dry-run by default. `--apply` writes. Exit 0 if every requested chapter is already in order or was
repaired; 1 if any was refused.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

BOOK = Path(__file__).resolve().parent.parent / "book"
DEF_LINE = re.compile(r"^\[\^([^\]]+)\]:")
REF = re.compile(r"\[\^([^\]]+)\]")
RULE = re.compile(r"^---\s*$")


class Refused(Exception):
    pass


def unit_of(path: Path) -> str:
    parts = path.stem.split("-", 2)
    return "-".join(parts[:2]) if len(parts) >= 2 else path.stem


def split_file(text: str):
    """head (body prose) | list of (label, block_text) | footer.

    The footer is the trailing `---`-delimited section of the LAST note block, if one is there.
    Anywhere else a `---` is part of a note and stays with it.
    """
    lines = text.split("\n")
    def_idx = [i for i, l in enumerate(lines) if DEF_LINE.match(l)]
    if not def_idx:
        raise Refused("no endnote definitions")

    head = lines[: def_idx[0]]
    bounds = def_idx + [len(lines)]
    blocks = []
    for k, start in enumerate(def_idx):
        blocks.append((DEF_LINE.match(lines[start]).group(1),
                       lines[start:bounds[k + 1]]))

    footer = []
    last_label, last_lines = blocks[-1]
    rules = [i for i, l in enumerate(last_lines) if RULE.match(l)]
    if rules:
        cut = rules[0]
        footer = last_lines[cut:]
        blocks[-1] = (last_label, last_lines[:cut])
    return head, blocks, footer


def body_order(head, labels: list[str]) -> list[str]:
    known, seen, order = set(labels), set(), []
    for m in REF.finditer("\n".join(head)):
        name = m.group(1)
        if name in known and name not in seen:
            seen.add(name)
            order.append(name)
    return order


def remap(text: str, mapping: dict[str, str]) -> str:
    """Simultaneous rename. Two passes through a sentinel so 1->2 and 2->1 cannot collide."""
    def to_sentinel(m):
        name = m.group(1)
        return f"[^\x00{mapping[name]}\x00]" if name in mapping else m.group(0)
    return REF.sub(to_sentinel, text).replace("[^\x00", "[^").replace("\x00]", "]")


def resequence(path: Path):
    """-> (changed, note) ; raises Refused."""
    text = path.read_text(encoding="utf-8")
    head, blocks, footer = split_file(text)
    labels = [lab for lab, _ in blocks]

    if len(labels) != len(set(labels)):
        raise Refused("duplicate note definitions")
    bad = [l for l in labels if not l.isdigit()]
    if bad:
        raise Refused(f"non-numeric labels {bad}")
    referenced = {m.group(1) for m in REF.finditer(text)}
    dangling = sorted(referenced - set(labels))
    if dangling:
        raise Refused(f"markers with no definition: {dangling}")

    order = body_order(head, labels)
    uncited = [l for l in labels if l not in order]
    if uncited:
        raise Refused(f"defined but never cited in body: {uncited} "
                      "— body order does not rank them; rule by hand")

    mapping = {old: str(i + 1) for i, old in enumerate(order)}
    if all(old == new for old, new in mapping.items()):
        return False, "already in order"

    new_head = remap("\n".join(head), mapping).split("\n")
    new_footer = remap("\n".join(footer), mapping).split("\n") if footer else []
    new_blocks = []
    for lab, block in blocks:
        body = remap("\n".join(block[1:]), mapping).split("\n") if len(block) > 1 else []
        first = f"[^{mapping[lab]}]:" + remap(block[0][len(f"[^{lab}]:"):], mapping)
        new_blocks.append((int(mapping[lab]), [first] + body))
    new_blocks.sort(key=lambda t: t[0])

    out = "\n".join(new_head + [l for _, b in new_blocks for l in b] + new_footer)

    # --- post-conditions -------------------------------------------------
    v_head, v_blocks, v_footer = split_file(out)
    v_labels = [lab for lab, _ in v_blocks]
    assert v_labels == [str(i + 1) for i in range(len(labels))], \
        f"{path.name}: definitions not 1..N: {v_labels}"
    assert body_order(v_head, v_labels) == v_labels, \
        f"{path.name}: body order still not ascending"

    strip = lambda ls: REF.sub("[^]", "\n".join(ls))
    assert strip(v_head) == strip(head), f"{path.name}: body text changed beyond markers"
    assert strip(v_footer) == strip(footer), f"{path.name}: footer changed beyond markers"
    before = sorted(strip(b[1:]) for _, b in blocks)
    after = sorted(strip(b[1:]) for _, b in v_blocks)
    assert before == after, f"{path.name}: note bodies not preserved"
    assert len(REF.sub("[^]", out)) == len(REF.sub("[^]", text)), \
        f"{path.name}: length changed beyond markers"

    moved = sum(1 for old, new in mapping.items() if old != new)
    return out, f"{len(labels)} notes, {moved} renumbered"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("units", nargs="*", help="e.g. III-08 VII-04 (default: every chapter)")
    ap.add_argument("--apply", action="store_true")
    args = ap.parse_args()

    wanted = set(args.units)
    refused = changed = 0
    for path in sorted(BOOK.glob("*.md")):
        unit = unit_of(path)
        if wanted and unit not in wanted:
            continue
        try:
            result = resequence(path)
        except Refused as e:
            if wanted:
                print(f"  REFUSED  {unit}: {e}")
                refused += 1
            continue
        out, note = result
        if out is False:
            if wanted:
                print(f"  ok       {unit}: {note}")
            continue
        changed += 1
        if args.apply:
            path.write_text(out, encoding="utf-8")
            print(f"  WRITTEN  {unit}: {note}")
        else:
            print(f"  would    {unit}: {note}")

    print(f"\n{changed} chapter(s) {'repaired' if args.apply else 'to repair'}, {refused} refused")
    if not args.apply and changed:
        print("dry run — pass --apply to write")
    return 1 if refused else 0


if __name__ == "__main__":
    sys.exit(main())
