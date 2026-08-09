#!/usr/bin/env python3
"""brief_fields.py — R-49's gauge. Truth and Consequences, Day 189.

R-49 was opened at V.8 with the right diagnosis and the wrong number. The
diagnosis: *no gauge reads a brief for a MISSING FIELD.* `where_the_book_is`
counts chapters, `claim_sweep` reads prose, `prose_beat_sweep` reads beats —
and a brief with a hole in it announces nothing, because absence has no
needle to grep for.

The number, written in the same breath: *"this brief was the ONLY one in
Book V with no `Source:` line."* Measured here: six Book V briefs have none.
★ The finding correctly identified a missing gauge and then produced,
ungauged, precisely the figure the gauge would have produced. That is why
this file exists rather than another sentence.

Fields are NOT equally owed and the tool says so rather than scoring them
alike:
  Beats  — REQUIRED. A brief with no beats is not a brief.
  Source — REQUIRED once the chapter is drafted or scheduled next; a
           chapter whose material is unstated is one the drafter invents.
  Named  — rule 5 (`02`:79): an argument that does not name its opponents
           reads as declaration. beat_sweep already audits WHO is named and
           whether a name is cut twice; it does not audit the field's
           EXISTENCE, which is the hole this covers.

WHAT THIS CANNOT SEE, stated because a clean run is otherwise read as a
clean book: a field that is PRESENT and WRONG. V.8's `Source:` line is
present, and the sentence inside it is the false one above. This gauge would
have passed it. It reads for holes, not for truth.

    python tools/brief_fields.py            # every book
    python tools/brief_fields.py --book V   # one book
    python tools/brief_fields.py --owed     # only what is missing
"""
import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCAFFOLD = ROOT / "06-THE-SCAFFOLD.md"
BOOK = ROOT / "book"

CHAPTER_RE = re.compile(r"^### ([IVX]+)\.(\d+)\s+—\s+(.*)$")
FIELDS = ("Beats", "Source", "Named")
BOOK_ORDER = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII"]


def drafted_ids():
    """Chapter ids with a file on disk — the same source where_the_book_is uses."""
    out = set()
    for p in BOOK.glob("*.md"):
        m = re.match(r"^([IVX]+)-(\d+)-", p.name)
        if m:
            out.add(f"{m.group(1)}.{int(m.group(2))}")
    return out


def briefs():
    lines = SCAFFOLD.read_text(encoding="utf-8").split("\n")
    heads = [(i, m) for i, l in enumerate(lines) if (m := CHAPTER_RE.match(l))]
    for n, (i, m) in enumerate(heads):
        j = heads[n + 1][0] if n + 1 < len(heads) else len(lines)
        body = "\n".join(lines[i:j])
        yield {
            "id": f"{m.group(1)}.{int(m.group(2))}",
            "book": m.group(1),
            "num": int(m.group(2)),
            "title": m.group(3).split("✅")[0].strip(" *—"),
            "line": i + 1,
            "lines": j - i,
            "has": {f: f"**{f}:**" in body for f in FIELDS},
        }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--book")
    ap.add_argument("--owed", action="store_true")
    args = ap.parse_args()

    drafted = drafted_ids()
    rows = [b for b in briefs() if not args.book or b["book"] == args.book.upper()]
    rows.sort(key=lambda b: (BOOK_ORDER.index(b["book"]), b["num"]))

    print(f"BRIEF FIELD SWEEP — {SCAFFOLD.name} · {len(rows)} brief(s)")
    print("  REQUIRED: Beats (always) · Source (drafted or next) · Named (rule 5)\n")

    missing = {f: [] for f in FIELDS}
    thin = []
    for b in rows:
        gone = [f for f in FIELDS if not b["has"][f]]
        for f in gone:
            missing[f].append(b)
        state = "drafted" if b["id"] in drafted else "planned"
        if gone and b["lines"] <= 15 and state == "planned":
            thin.append(b)
        if args.owed and not gone:
            continue
        mark = "  " if not gone else "!!"
        flags = " ".join(("+" if b["has"][f] else "-") + f[0] for f in FIELDS)
        print(f"  {mark} {b['id']:<7} {flags}  {b['lines']:>3}L  {state:<7} {b['title'][:44]}")

    print()
    for f in FIELDS:
        ids = [b["id"] for b in missing[f]]
        if not ids:
            print(f"  {f:<7} complete across every brief swept.")
            continue
        drafted_gap = [i for i in ids if i in drafted]
        print(f"  {f:<7} MISSING in {len(ids)}: {', '.join(ids)}")
        if drafted_gap:
            print(f"          ↑ {len(drafted_gap)} already DRAFTED — the chapter was written "
                  f"without the field: {', '.join(drafted_gap)}")

    if thin:
        print("\n  ⚠ THIN AND UNDRAFTED — a short brief with holes is the one that costs, because")
        print("    the drafter fills a hole from memory and the memory is the thing being audited:")
        for b in thin:
            print(f"      {b['id']}  {b['lines']} lines, `06`:{b['line']}")

    print("\n  ⚠ This reads for HOLES, not for TRUTH. A `Source:` line that is present and false")
    print("    passes here — R-49's own repair line is exactly that, and it passed. The gauge that")
    print("    checks a field's CONTENT does not exist and is not this one.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
