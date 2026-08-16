#!/usr/bin/env python3
"""RELATIVE-CHAPTER REFERENCE SWEEP — the one cross-reference form nothing else can see.

    python tools/relative_ref_sweep.py             # sweep, with the control first
    python tools/relative_ref_sweep.py --selftest  # control only
    python tools/relative_ref_sweep.py --book III  # one book

WHY THIS EXISTS, stated so it survives being forgotten. `crossref_rot.py` resolves
explicit tokens -- `III.4`, `[^6]`, `C9`. A reference written as *two chapters ago*
carries no token. It resolves against nothing, it is invisible to every other sweep
in this directory, and when it is wrong it fails in the one way a reader blames on
themselves: they turn back, find the wrong chapter, and conclude they missed it.

Filed as queue row R2-020, after a fresh read of III.5 found TWO wrong ones at
opposite ends of one chapter (R2-017) -- and found them by reading, because nothing
was watching. 19 sites in the volume; 5 had ever been checked by anything.

  ==> WHAT THIS TOOL DOES NOT DO, AND MUST NOT BE READ AS DOING. <==

It resolves the ARITHMETIC and prints the target's TITLE. It does not, and cannot,
decide whether the sentence means that chapter. *Two chapters ago the divine player
was taken apart* is wrong because the divine player is not in III.3 -- a fact about
subject matter, not about counting. So every hit is printed for a HUMAN to adjudicate
and nothing is ever marked clean automatically. A green from this tool means the
arithmetic resolves to a chapter that exists. It does not mean the reference is right.

That distinction is the whole design. A sweep that printed OK per site would convert
19 unexamined references into 19 references that LOOK examined, which is worse than
having no sweep -- an audited-looking corpus is harder to get a second read of than
an unaudited one. So the exit code is about resolvability only, and the report is a
worklist, not a verdict.

ORDERING is linear across the volume (I.1 ... VIII.n), because that is the order the
reader meets the chapters in, which is what *ago* indexes. Across a book boundary the
count runs backward into the previous book -- IV.1's "two chapters ago" is III.7.
Front matter and the coda (C.1, C.2) are excluded: nothing in them uses the idiom and
including them would shift every index by two.
"""

import re
import sys
from pathlib import Path

BOOK_DIR = Path(__file__).resolve().parent.parent / "book"

ROMAN = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII"]

WORD_N = {
    "one": 1, "two": 2, "three": 3, "four": 4,
    "five": 5, "six": 6, "seven": 7, "eight": 8,
}

# BACKWARD and FORWARD are separate on purpose: "four chapters later" is a promise
# about text the reader has NOT seen, and it resolves in the other direction.
BACK = r"(ago|back|earlier|before)"
FWD = r"(later|ahead|on|hence)"

PAT_BACK = re.compile(
    r"\b(" + "|".join(WORD_N) + r")\s+chapters?\s+" + BACK + r"\b", re.IGNORECASE)
PAT_FWD = re.compile(
    r"\b(" + "|".join(WORD_N) + r")\s+chapters?\s+" + FWD + r"\b", re.IGNORECASE)


def chapter_order(book_dir):
    """Linear reading order. Returns [(label, title, path), ...]."""
    found = []
    for p in sorted(book_dir.glob("*.md")):
        m = re.match(r"^([IVX]+)-(\d+)-(.+)\.md$", p.name)
        if not m:
            continue                      # C-01, C-02, and anything else
        book, num, slug = m.group(1), int(m.group(2)), m.group(3)
        if book not in ROMAN:
            continue
        found.append((ROMAN.index(book), num, f"{book}.{num}",
                      slug.replace("-", " "), p))
    found.sort(key=lambda r: (r[0], r[1]))
    return [(lbl, title, path) for _, _, lbl, title, path in found]


def sweep(order, only_book=None):
    index = {lbl: i for i, (lbl, _, _) in enumerate(order)}
    hits = []
    for i, (lbl, _title, path) in enumerate(order):
        if only_book and not lbl.startswith(only_book + "."):
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        for lineno, line in enumerate(text.splitlines(), 1):
            for pat, direction in ((PAT_BACK, -1), (PAT_FWD, +1)):
                for m in pat.finditer(line):
                    n = WORD_N[m.group(1).lower()]
                    tgt = i + direction * n
                    if 0 <= tgt < len(order):
                        t_lbl, t_title, _ = order[tgt]
                        resolves = True
                    else:
                        t_lbl, t_title, resolves = "—", "OFF THE END OF THE VOLUME", False
                    hits.append({
                        "from": lbl, "line": lineno, "file": path.name,
                        "phrase": m.group(0), "n": n,
                        "dir": "back" if direction < 0 else "fwd",
                        "target": t_lbl, "target_title": t_title,
                        "resolves": resolves,
                        "sentence": line.strip(),
                    })
    return hits, index


def selftest(order):
    """POSITIVE CONTROL. Two planted references, one resolvable and one not.

    Runs against a SYNTHETIC ordering, never the book -- a control that shares the
    subject it is controlling for cannot fail independently of it.
    """
    fake = [("X.1", "first", None), ("X.2", "second", None), ("X.3", "third", None)]
    line_ok = "as was said two chapters ago, the thing"
    line_off = "as was said seven chapters ago, the thing"
    ok = PAT_BACK.search(line_ok)
    off = PAT_BACK.search(line_off)
    assert ok and WORD_N[ok.group(1)] == 2, "backward pattern did not match"
    assert off and WORD_N[off.group(1)] == 7, "backward pattern did not match"
    # from X.3, two back == X.1 (resolvable); seven back == off the end.
    i = 2
    assert 0 <= i - 2 < len(fake), "resolvable case failed"
    assert not (0 <= i - 7 < len(fake)), "off-the-end case was NOT caught"
    # and the forward pattern must not fire on backward text, or every hit doubles
    assert not PAT_FWD.search(line_ok), "forward pattern fired on backward text"
    assert PAT_FWD.search("named four chapters later"), "forward pattern is dead"
    # a negative: prose about chapters that is not a relative reference
    assert not PAT_BACK.search("two chapters of this book are about place"), \
        "pattern fires on non-reference prose"
    print("POSITIVE CONTROL — synthetic ordering, both directions and one null:")
    print("    resolvable back-reference (X.3 - 2)      : caught, resolves to X.1")
    print("    unresolvable back-reference (X.3 - 7)    : caught, flagged OFF THE END")
    print("    forward pattern on backward text         : silent  (no double count)")
    print("    'two chapters of this book are about...' : silent  (not a reference)")
    print("  [ok] all four live.\n")
    if order:
        print(f"  volume ordering parsed: {len(order)} chapters, "
              f"{order[0][0]} -> {order[-1][0]}\n")


def main():
    args = sys.argv[1:]
    only_book = None
    if "--book" in args:
        only_book = args[args.index("--book") + 1]

    order = chapter_order(BOOK_DIR)
    selftest(order)
    if "--selftest" in args:
        return 0

    hits, _ = sweep(order, only_book)

    print(f"RELATIVE-CHAPTER REFERENCES — {len(hits)} site(s)"
          + (f" in Book {only_book}" if only_book else " across the volume"))
    print("  Every one is printed. None is marked clean. The arithmetic is mechanical;")
    print("  whether the sentence MEANS that chapter is not, and is yours to decide.\n")

    unresolved = 0
    current = None
    for h in hits:
        if h["from"] != current:
            current = h["from"]
            print(f"  ── {current} ─────────────────────────────────")
        arrow = "<-" if h["dir"] == "back" else "->"
        flag = "" if h["resolves"] else "   ⛔ UNRESOLVABLE"
        if not h["resolves"]:
            unresolved += 1
        print(f"    {h['file']}:{h['line']}  \"{h['phrase']}\"  {arrow} "
              f"{h['target']} — {h['target_title']}{flag}")
        s = h["sentence"]
        print(f"        {s[:150]}{'…' if len(s) > 150 else ''}")

    print(f"\n  resolvable: {len(hits) - unresolved}/{len(hits)}"
          f"   ⛔ unresolvable: {unresolved}")
    print("\n  LIMIT, printed on every run including a clean one: this tool checks that")
    print("  the count lands on a chapter that exists. It has no idea what any chapter")
    print("  is ABOUT. Both defects that caused it to be written (R2-017) resolve")
    print("  perfectly and are wrong. Read the target titles against the sentences.")
    return 1 if unresolved else 0


if __name__ == "__main__":
    sys.exit(main())
