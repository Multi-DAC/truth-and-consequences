#!/usr/bin/env python3
"""
Which chapters print their endnote markers out of sequence, and by how much.

WHY. `compile_pdf.py` uses Python-Markdown's footnotes extension, which numbers notes by
DEFINITION order in the source, not by APPEARANCE order in the body. So a chapter whose body
references `[^1] [^2] [^4] [^3]` prints a superscript 4 before a superscript 3 — in III.8's case,
two pages before. Found at III.8 on Day 204 and called "the only chapter in 1,076 pages" on the
strength of a set that had not been swept; the volume-wide count is twelve.

The repair per chapter is mechanical — swap the `[^n]:` definitions and the body markers so that
definition order matches reading order — which is exactly the kind of work that gets 11 of 12 done
and then reads as finished. Hence a gauge rather than a list. R2-072.

WHAT IT MEASURES. Body prose only: everything above the first `[^n]:` definition line. A `[^n]`
inside a note definition is a note citing a note and is not what a reader meets in sequence.
`inversions` counts pairs out of order (bubble distance), so it prices the repair rather than only
flagging it: VII.4's `3·2·9·10·7·4·5·1·6·8` is a resequence, VIII.7's `1·2·3·5·4` is one swap.

LIMIT, stated because a green here is narrower than it sounds: this reads the MARKDOWN. It infers
what the PDF will print from the extension's documented numbering rule; it does not rasterise. The
inference has been spot-checked in print at III.8 (note 4 on p.201, note 3 on p.203) and VI.6
(pp.680–690 run 1·2·3·8·4·5·6·7). Reading the source and reporting on the artefact is how a
17-file repair got filed wrongly and withdrawn on Day 204 — so: spot-check before you trust a
chapter this tool has newly added.

Exit 0 when every chapter is in order; 1 while any is not.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

BOOK = Path(__file__).resolve().parent.parent / "book"
DEF_RE = re.compile(r"^\[\^([^\]]+)\]:", re.M)
REF_RE = re.compile(r"\[\^([^\]]+)\]")

# The adjudicated set, as a control on this tool rather than a filter on its output.
#
# ⚠ THE DAY-204 READ NAMED TWELVE AND THE TWELFTH WAS WRONG. `V-06` was on that list and its
# markers are in perfect order — definition order and body order are both 1..15, zero inversions,
# nothing uncited. The read's first sweep returned 13, was corrected to 12, and the answer was 11:
# a second error introduced inside the correction of the first, which is the cheapest place for one
# to hide. This control exists so the next disagreement is loud instead of inherited.
D204 = {"III-08", "IV-06", "V-08", "V-10", "VI-06",
        "VII-03", "VII-04", "VII-05", "VII-06", "VIII-03", "VIII-07"}


def inversions(seq):
    return sum(1 for i in range(len(seq)) for j in range(i + 1, len(seq)) if seq[i] > seq[j])


def analyse(path: Path):
    text = path.read_text(encoding="utf-8")
    first_def = DEF_RE.search(text)
    if not first_def:
        return None
    body = text[: first_def.start()]
    order = [m.group(1) for m in DEF_RE.finditer(text)]           # definition order = printed number
    number = {name: i + 1 for i, name in enumerate(order)}
    seen, seq = set(), []
    for m in REF_RE.finditer(body):
        name = m.group(1)
        if name in number and name not in seen:
            seen.add(name)
            seq.append(number[name])
    uncited = [n for n in order if n not in seen]
    return seq, inversions(seq), len(order), uncited


def main():
    rows, clean = [], 0
    for path in sorted(BOOK.glob("*.md")):
        stem = path.stem.split("-", 2)
        unit = "-".join(stem[:2]) if len(stem) >= 2 else path.stem
        r = analyse(path)
        if r is None:
            continue
        seq, inv, total, uncited = r
        if inv:
            rows.append((unit, seq, inv, total, uncited))
        else:
            clean += 1

    print("ENDNOTE MARKER ORDER — body prose only, inferred from definition order")
    print(f"  units with endnotes: {len(rows) + clean}   in order: {clean}   OUT OF ORDER: {len(rows)}")
    print()
    for unit, seq, inv, total, uncited in sorted(rows, key=lambda r: -r[2]):
        mark = " " if unit in D204 else "  ⚠ NOT IN THE D204 SET — spot-check in print before trusting"
        print(f"  {unit:<9} {inv:>2} inversion(s)  of {total} notes   {'·'.join(map(str, seq))}{mark}")
        if uncited:
            print(f"            ⚠ never cited in body prose: {', '.join(uncited)}")

    found = {u for u, *_ in rows}
    missing = D204 - found
    extra = found - D204
    print()
    if missing or extra:
        print("  ⛔ CONTROL DISAGREES WITH THE DAY-204 READ — one of the two is wrong.")
        if missing:
            print(f"     named in the read, not found here: {', '.join(sorted(missing))}")
        if extra:
            print(f"     found here, not named in the read: {', '.join(sorted(extra))}")
    else:
        print(f"  ✅ control: reproduces the adjudicated set exactly, "
              f"{len(found)} of {len(D204)}, no extras.")

    if rows:
        worst = max(rows, key=lambda r: r[2])
        cheap = min(rows, key=lambda r: r[2])
        print(f"  worst: {worst[0]} ({worst[2]} inversions) · cheapest: {cheap[0]} ({cheap[2]})")
    sys.exit(1 if rows else 0)


if __name__ == "__main__":
    main()
