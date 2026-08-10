#!/usr/bin/env python3
"""
CARD SWEEP  —  Truth and Consequences, Day 189.

WHEN A BOOK DECLARES A FORM LOAD-BEARING, DOES IT ACTUALLY DELIVER THE FORM?

V.1:44 says of the census card: "That is the whole load-bearing claim of this
book, and it is small." A rolling reviewer read all eleven chapters and reported
the card appears twice. Counting from disk agreed, and made it worse: the card
does not taper across Book V, it stops. `complement` occurs in V.1 and V.2 and
in no chapter after. No partial card is attempted anywhere else.

WHY THAT WENT UNSEEN FOR ELEVEN CHAPTERS, which is the reason this file exists:

    THE PROJECT'S SEVENTEEN INSTRUMENTS ALL MEASURE PROSE PROPERTIES —
    voice uniformity, beat delivery, citation density, ancestor coverage.
    Not one of them measures whether a DECLARED STRUCTURE was populated.

A missing card is not a defect of sentences. Every chapter without one reads
well; that is precisely the problem. A form that is announced and then not
performed leaves no trace in any prose metric, because the absent thing was
never a sentence. It is the same class as the tier IV.10 lost: found by putting
two lists side by side and counting, not by reading harder.

And there is a second thing this measures that the reviewer named and I would
not have: WHICH chapters carry the card. Both carded chapters are the two where
the tradition is held at arm's length. The roads treated most sympathetically
are the ones never carded. That correlation is visible only when the count is
per-chapter and the chapters are in order, so the output keeps them in order.

WHAT THIS IS NOT. It counts vocabulary, not comprehension. A chapter can use
the word `boundary` in an ordinary sense and score — V.11's three are of that
kind. So the strong signal here is the ZERO, never the small positive: a chapter
with compl=0 and null=0 has certainly not written a card. A chapter with a 2 has
possibly written one and must be read. The instrument is trusted downward only,
and that limit is declared rather than discovered later.

Usage:
    python tools/card_sweep.py            # every drafted book
    python tools/card_sweep.py V          # one book
"""

import re
import sys
from pathlib import Path

BOOK = Path(__file__).resolve().parent.parent / "book"

# The four card fields, as the census defines them in Book IV. Patterns are
# deliberately loose (stems, not phrases) so the instrument OVER-reports rather
# than under-reports: a false positive costs a read, a false negative hides the
# defect this file was built to catch.
FIELDS = {
    "null": r"null[- ]space",
    "bound": r"boundar",
    "compl": r"complement",
    "navig": r"navigat",
}

# A chapter is CARDED only if it carries the two fields that have no ordinary-
# English use in this book's register. `boundary` and `navigation` are common
# words; `null space` and `complement` are not.
DIAGNOSTIC = ("null", "compl")


def chapters(book=None):
    pat = f"{book}-*.md" if book else "*-*.md"
    out = []
    for p in sorted(BOOK.glob(pat)):
        m = re.match(r"^([IVX]+)-(\d+)-", p.name)
        if m:
            out.append((m.group(1), int(m.group(2)), p))
    return out


def main():
    book = sys.argv[1].upper() if len(sys.argv) > 1 else None
    rows = chapters(book)
    if not rows:
        print(f"no chapters found for {book or 'any book'}")
        return 1

    print("CARD SWEEP — declared-form delivery, counted from disk")
    print("  ⚠ trusted DOWNWARD only: a zero is evidence, a small positive is a read-order\n")

    current = None
    tallies = {}
    for bk, n, path in rows:
        if bk != current:
            if current is not None:
                print()
            print(f"  BOOK {bk}")
            current = bk
            tallies[bk] = [0, 0]
        text = path.read_text(encoding="utf-8", errors="replace").lower()
        counts = {k: len(re.findall(v, text)) for k, v in FIELDS.items()}
        carded = all(counts[f] for f in DIAGNOSTIC)
        tallies[bk][0] += 1
        tallies[bk][1] += 1 if carded else 0
        cells = "  ".join(f"{k}={counts[k]}" for k in FIELDS)
        # ⚠ THE VERDICT NOW OBEYS THE DOCSTRING. This column used to read "✓ CARDED" for
        # any chapter with one `null space` and one `complement` ANYWHERE in the file, in
        # any context — so VII.2, which prints no card and merely QUOTES Book IV's cards
        # four times, scored CARDED, and that false positive reached handoff.json. The
        # header above has always said "trusted DOWNWARD only: a zero is evidence, a small
        # positive is a read-order." The output asserted the opposite. Honest label, no
        # coupling to what may be asserted — R-90's defect, in a gauge. (R-94, Day 190.)
        # For the structural check that CAN license a positive, see instrument_sweep.py.
        mark = (
            "? vocab-only — read it" if carded
            else ("· partial" if any(counts.values()) else "  none")
        )
        print(f"    {bk}.{n:<2} {cells}   {mark}")

    # The aggregate carried the same overclaim as the per-chapter column, and it is the
    # string that produced the "2 of 11" headline. That headline SURVIVES — it rests on the
    # ZEROS, which is the direction this instrument is valid in. So the summary now states
    # the licensed reading (the absences) and refuses the unlicensed one (the deliveries).
    print()
    for bk, (total, carded) in tallies.items():
        absent = total - carded
        flag = ""
        if absent:
            flag = f"   ⚠ {absent} of {total} carry NO card vocabulary — that count is evidence"
        print(
            f"  BOOK {bk}: {carded}/{total} have card vocabulary "
            f"({100.0 * carded / total:.0f}%) — NOT a delivery count{flag}"
        )
    print("\n  ⛔ This tool cannot license a positive. For delivered form, run:")
    print("       python tools/instrument_sweep.py --cards")
    return 0


if __name__ == "__main__":
    sys.exit(main())
