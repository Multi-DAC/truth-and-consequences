#!/usr/bin/env python3
"""order_sweep.py — the gauge under the book order. Truth and Consequences, Day 187.

WHY THIS EXISTS. Two book orders were proposed for Part Two and each one broke exactly one
written handoff:

    mine    I II III V VI IV VII VIII  — breaks VI.8 -> VII.1
    Fable's I II III V IV VI VII VIII  — breaks V.10 -> VI

Neither of us caught our own. Fable caught mine; the pre-mortem caught Fable's. The defect
is not either order — it is that `06-THE-SCAFFOLD.md` contains chapter-ending beats whose
correctness depends on which book comes NEXT, and nothing checked them. A handoff that has
gone false does not error and does not read wrong. It reads like a chapter that ends well,
which is the one property a silent failure needs.

`claim_sweep.py` watches retired terms, Trap-5 tells and self-reference. It does not know
what order the books are in. This does, and only that.

WHAT IT CHECKS
  1. Every `handoff to Book X` beat that sits in the LAST chapter of its book is an
     ADJACENCY CLAIM. The named target must be the book that actually follows under the
     adopted order. -> PASS / **FAIL**
  2. The same beat in a NON-final chapter is a forward reference, not an adjacency claim.
     -> INFO, never a failure.
  3. Any beat asserting adjacency in prose -- "the next subject", "the next book", "the
     book that follows" -- WITHOUT a checkable named target. -> **UNRESOLVED**, because a
     claim the tool cannot check is exactly how the V.10 line survived.

HOW TO USE IT FOR A REORDER. Do not edit the manuscript first. Run the candidate through:

    python tools/order_sweep.py --order I,II,III,V,IV,VI,VII,VIII

Everything it prints as FAIL is a beat that must be rewritten as part of the reorder, not
after it. Then change ORDER below and commit the two together.

KNOWN LIMIT, stated so nobody trusts a clean run further than it goes: this reads the
SCAFFOLD's stated handoffs. A chapter whose last paragraph leans on the next book without
saying "handoff" is invisible here, and so is every dependency that is not a handoff --
the forward-reference class (does Book V presuppose Book IV's roster?) needs a reader, not
a regex. A green run means no STATED handoff is false. It does not mean the order is safe.
"""
import argparse
import pathlib
import re
import sys

# The adopted order. CHANGE THIS AND THE MANUSCRIPT IN ONE COMMIT.
ORDER = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII"]

SCAFFOLD = pathlib.Path(__file__).resolve().parents[1] / "06-THE-SCAFFOLD.md"

CHAPTER_RE = re.compile(r"^### ((?:[IVX]+|C)\.\d+) — (.+?)\s*$", re.MULTILINE)
HANDOFF_RE = re.compile(r"handoff to (?:the )?(Book\s+([IVX]+)|CODA)", re.IGNORECASE)
# Adjacency asserted in prose, with nothing a tool can resolve.
LOOSE_RE = re.compile(r"the next (?:subject|book|chapter is)|the book that follows|"
                      r"which is the next", re.IGNORECASE)


def blocks(text):
    """[(chapter_id, joined_body)] — body joined so a hard wrap cannot hide a needle."""
    parts = re.split(r"^### ", text, flags=re.MULTILINE)[1:]
    out = []
    for part in parts:
        head = part.splitlines()[0]
        m = CHAPTER_RE.match("### " + head)
        if not m:
            continue
        body = " ".join(ln.strip() for ln in part.splitlines()[1:])
        out.append((m.group(1), body))
    return out


def book_of(chapter_id):
    return chapter_id.split(".")[0]


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--order", default=",".join(ORDER),
                    help="comma-separated candidate order to test, e.g. I,II,III,V,IV,VI,VII,VIII")
    args = ap.parse_args()

    order = [b.strip() for b in args.order.split(",") if b.strip()]
    if sorted(order) != sorted(ORDER):
        print(f"!! candidate order is not a permutation of the eight books: {order}")
        return 2

    text = SCAFFOLD.read_text(encoding="utf-8")
    chapters = blocks(text)
    if not chapters:
        print("!! no chapters parsed — the scaffold's heading format changed")
        return 2

    # last chapter of each book, in file order
    last = {}
    for cid, _ in chapters:
        last[book_of(cid)] = cid

    successor = {b: (order[i + 1] if i + 1 < len(order) else "CODA")
                 for i, b in enumerate(order)}

    print(f"ORDER SWEEP — {len(chapters)} chapters · order: {' '.join(order)}")
    print()

    fails = unresolved = 0
    for cid, body in chapters:
        book = book_of(cid)
        if book == "C":
            continue
        for m in HANDOFF_RE.finditer(body):
            target = (m.group(2) or "CODA").upper()
            if cid != last.get(book):
                print(f"  info  {cid} → {target}  (not its book's last chapter; "
                      f"a forward reference, not an adjacency claim)")
                continue
            actual = successor[book]
            # THE CODA IS TERMINAL, and every book leans toward it. A handoff naming the
            # CODA from anywhere except the final book is a THEMATIC forward reference —
            # IV.10's "the handoff to the CODA's living-book claim" is nine chapters from
            # the Coda under every candidate and was never an adjacency claim. Stated as a
            # category rather than filed as an exemption: an exemption list that absorbs a
            # whole class is how a gauge stops measuring. Printed, never silent.
            if target == "CODA" and book != order[-1]:
                print(f"  info  {cid} → CODA  (thematic; the Coda is terminal and is not "
                      f"{book}'s neighbour under any order)")
                continue
            if target == actual:
                print(f"  PASS  {cid} → {target}")
            else:
                fails += 1
                print(f"  ** FAIL **  {cid} names Book {target}, but under this order "
                      f"Book {book} is followed by {actual}.")
                print(f"              the beat: …{body[max(0, m.start()-110):m.end()+90].strip()}…")
        if LOOSE_RE.search(body) and not HANDOFF_RE.search(body):
            unresolved += 1
            lm = LOOSE_RE.search(body)
            print(f"  ?? UNRESOLVED  {cid} asserts adjacency with no named target: "
                  f"…{body[max(0, lm.start()-70):lm.end()+70].strip()}…")

    print()
    print(f"  {fails} false handoff(s) · {unresolved} unresolved adjacency claim(s)")
    if fails:
        print("  Every FAIL is a beat to rewrite AS PART OF the reorder, not after it.")
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
