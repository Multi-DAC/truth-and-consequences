#!/usr/bin/env python
"""row_promotion_sweep.py — does every R-number that has been FILED actually have a ROW?

Ruling 148 (R-26) made the promotion convention: *an entry that files an owed item must row it
in the same commit, or it is a note.* R-31 exists as the receipt of that convention's first
enforcement — a row opened by number in the DRAFT-LOG and never written into the queue, found
by Clayton reading the file, because **nothing derives this file**.

The receipt was mistaken for the mechanism. The convention failed seven more times after it.

This is the mechanism. It reads every `R-<n>` mentioned anywhere in the project and checks it
against the rows the queue actually carries. It also reports the two integrity defects a
missing-row check alone would not see:

  HOLE      — a number nothing anywhere has ever filed (the series lies about its own size)
  COLLISION — one number carrying two different rows (a citation cannot resolve)

Read-only. Exit code is NOT the deliverable; the lists are.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
QUEUE = ROOT / "book" / "docs" / "REVISION-QUEUE.md"
RX = re.compile(r"\bR-(\d+)\b")
# A row is a table line whose FIRST cell is the number, or a `### R-n` section heading.
# The `(?:\([a-z]\))?` is not decoration: R-24 ships as **R-24(b)** because its (a) half was
# discharged separately, and without it this gauge reports its own most-cited row as missing.
RX_ROW = re.compile(r"^\|\s*~?~?\*\*R-(\d+)(?:\([a-z]\))?\*\*|^###\s+R-(\d+)\b", re.M)


def scan(path: Path) -> set[int]:
    try:
        return {int(m) for m in RX.findall(path.read_text(encoding="utf-8"))}
    except (OSError, UnicodeDecodeError):
        return set()


def main() -> int:
    if not QUEUE.exists():
        print(f"FATAL: no queue at {QUEUE}")
        return 2

    qtext = QUEUE.read_text(encoding="utf-8")
    rows: list[int] = [int(a or b) for a, b in RX_ROW.findall(qtext)]
    rowset = set(rows)

    # every R-number mentioned anywhere in the project, and where
    mentions: dict[int, set[str]] = {}
    for md in sorted(ROOT.rglob("*.md")):
        if ".git" in md.parts:
            continue
        for n in scan(md):
            mentions.setdefault(n, set()).add(str(md.relative_to(ROOT)).replace("\\", "/"))

    if not mentions:
        print("FATAL: no R-numbers found anywhere — the regex or the tree moved.")
        return 2

    # A FILING happens in the log, the scaffold, a packet — somewhere that is not this file.
    # The queue is where a filing gets ROWED. Without this distinction the gauge reports its own
    # footprint: the note recording that R-44 is a hole is itself a mention of R-44 inside the
    # queue, which would read back as "filed but never rowed." An instrument that cannot tell its
    # own writing from the thing it measures will always find work.
    qname = str(QUEUE.relative_to(ROOT)).replace("\\", "/")
    elsewhere = {n for n, where in mentions.items() if where - {qname}}

    high = max(mentions)
    filed = sorted(elsewhere | rowset)

    unrowed = [n for n in filed if n not in rowset]
    holes = [n for n in range(1, high + 1) if n not in filed]
    collisions = sorted({n for n in rows if rows.count(n) > 1})

    print("=" * 78)
    print(f"ROW PROMOTION SWEEP — {QUEUE.relative_to(ROOT)}")
    print("=" * 78)
    print(f"  highest number filed : R-{high}")
    print(f"  rows in the queue    : {len(rowset)}")
    print(f"  numbers filed anywhere: {len(filed)}")
    print()

    if unrowed:
        print(f"[X] {len(unrowed)} FILED BUT NEVER ROWED — ruling 148's defect, live:")
        for n in unrowed:
            where = sorted(mentions[n] - {str(QUEUE.relative_to(ROOT)).replace("\\", "/")})
            print(f"      R-{n:<3} cited in: {', '.join(where) or '(queue only)'}")
        print("      An item absent from the queue is UNRECORDED, NOT DISCHARGED (this file's charter).")
    else:
        print("[ok] every filed R-number has a row.")
    print()

    if holes:
        print(f"[!] {len(holes)} HOLE(S) in the series — nothing anywhere ever filed these:")
        print(f"      {', '.join(f'R-{n}' for n in holes)}")
        print("      A citation of 'R-1...R-{0}' overstates the series by {1}.".format(high, len(holes)))
    else:
        print("[ok] no holes — the series is dense.")
    print()

    if collisions:
        print(f"[X] {len(collisions)} COLLISION(S) — one number, two rows, citations cannot resolve:")
        for n in collisions:
            print(f"      R-{n} appears as a row {rows.count(n)} times")
        print("      Ruling 145 (R-23) precedent: do NOT renumber if live citations resolve by")
        print("      context — write a note at each. A renumber breaks every citation at once.")
    else:
        print("[ok] no collisions.")
    print()

    print("-" * 78)
    print("COVERAGE, STATED, BECAUSE THIS GAUGE CANNOT CERTIFY ITSELF:")
    print("  It matches the literal token R-<n>. A row owed in prose that never took a number")
    print("  is invisible to it — the same limit R-32's keyword grep declared about itself.")
    print("  It checks that a row EXISTS. It cannot check that the row is any good.")
    print("-" * 78)

    return 1 if (unrowed or collisions) else 0


if __name__ == "__main__":
    sys.exit(main())
