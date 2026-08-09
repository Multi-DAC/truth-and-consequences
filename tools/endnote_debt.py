#!/usr/bin/env python3
"""
ENDNOTE DEBT  —  Truth and Consequences, Day 190.

THE INSTRUMENT RULING 117 ORDERED AND NOBODY BUILT.

Ruling 9 (Day 186, Clayton), in full:

    "Book I: nothing. Everywhere after: the name lives in the sentence; the
     source lives in an endnote. Per-chapter, numbered, at the back of the book."

We obey the first half on every page. We have never once executed the second.

Ruling 117 (Day 188) found that, said the words "a mechanism with no trigger,"
and filed the fix AS A BUILD ORDER, NOT A QUESTION:

    "an endnote register plus a gauge counting named sources against receipts
     per chapter, which will read 0/N on the day it is written -- and that zero
     is the finding, printed by an instrument instead of by a reviewer."

Two days later the gauge did not exist, and the way the debt resurfaced was me
re-grepping the raw fact and reporting it to Clayton AS IF IT WERE NEW. Ruling
117 diagnosed mechanism-without-a-trigger and was itself filed without one: a
build order with no gauge and no due date is a stamp, and stamps rot silently.
That is Drift #287 inside the ruling written to stop it.

So: 0/N, printed every time anyone asks, by something that reads the files.

WHAT IT COUNTS
--------------
NAMED SOURCE   a roster name used ATTRIBUTIVELY -- possessive ("Gibson's
               affordances") or adjacent to an attribution verb ("Searle
               argues"). That is the sentence-shape ruling 9 mandates a
               receipt for. A bare mention in a list is not counted; this
               gauge UNDER-reports on purpose, so its N is a floor.
RECEIPT        a markdown footnote reference [^n], an HTML <sup>, or a
               per-chapter NOTES section. Any of the three counts.

THE ROSTER IS THIS FILE'S BLIND SPOT AND IT SAYS SO.
A curated list cannot certify its own coverage, so every run also prints
CANDIDATES: capitalized tokens in attributive position that the roster does
not know. Growing the roster from that list is the maintenance this instrument
requires. A run with candidates outstanding has NOT measured the whole book.

Usage:  python tools/endnote_debt.py [--sites] [--chapter IV-03]
"""

import re
import sys
import pathlib
from collections import Counter, defaultdict

ROOT = pathlib.Path(__file__).resolve().parents[1]
BOOK = ROOT / "book"

CHAPTER_RE = re.compile(r"^(?P<book>I{1,3}|IV|V|VI{1,3})-(?P<n>\d\d)-")
BOOK_ORDER = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII"]

# Book I takes no apparatus, by ruling 9. It is not a debt; it is the design.
EXEMPT_BOOKS = {"I"}

# ---------------------------------------------------------------- the roster
# Built Day 190 from two independent scans of the 43 drafted chapters:
# possessive-form and attribution-verb-adjacent capitalized tokens. Entries are
# matched on the LAST token (surname) or on the full string, whichever appears.
ROSTER = [
    # philosophy of mind / analytic
    "Searle", "Dennett", "Chalmers", "Nagel", "Kant", "Plato", "Aristotle",
    "Spinoza", "Schopenhauer", "Russell", "Whitehead", "Bergson", "Broad",
    "Husserl", "Heidegger", "Merleau-Ponty", "Wittgenstein", "Korzybski",
    "Bostrom", "Dawkins", "Hitchens", "Tononi", "Giulio Tononi",
    # psychology / perception / biology
    "Gibson", "James", "William James", "Jung", "Uexküll", "Mariotte",
    "Moskowitz", "Leonard Moskowitz", "Harner", "Monroe", "Néel",
    # physics
    "Everett", "Wigner", "Neumann", "von Neumann", "Rovelli", "Bohr",
    # mystical / theological
    "Eckhart", "Suso", "Plotinus", "Proclus", "Dionysius", "Aquinas",
    "Augustine", "Irenaeus", "Valentinus", "Tillich", "Schweitzer",
    "Bruno", "Corbin", "Sohravardī", "Gaon", "Eliade", "Katz",
    "Steven Katz", "Forman", "Robert Forman", "Barfield", "Nishida",
    # play / games
    "Suits", "Bernard Suits", "Carse", "James Carse", "Huizinga", "Caillois",
    # letters / magic / anomalous
    "Borges", "Zhuangzi", "Crowley", "Dee", "Spare", "Blake", "Watts",
    "Alan Watts", "Arnold", "Kenneth Arnold", "Vallée", "Teofilo",
]
ROSTER_LAST = {r.split()[-1]: r for r in ROSTER}

ATTRIB_VERB = (
    r"(?:argues?|argued|writes?|wrote|calls?|called|names?|named|shows?|showed|"
    r"put it|coined|observed?|notes?|noted|says?|said|insisted|claims?|claimed|"
    r"held|holds|describes?|described|reports?|reported|proposed?|distinguishe[sd]|"
    r"remarks?|asks?|answers?|terms?|termed|phrase[sd]?)"
)
NAME_TOK = r"[A-Z][a-zA-ZÀ-ſĀ-ſ-]+(?:\s+[A-Z][a-zA-ZÀ-ſ-]+){0,2}"

# capitalized words that are ordinary English sentence-openers or book furniture
STOP = {
    "The", "And", "It", "This", "That", "What", "If", "But", "A", "An", "In",
    "So", "Then", "You", "He", "She", "They", "We", "There", "Not", "No",
    "Now", "One", "Two", "Three", "Four", "Which", "When", "Where", "Every",
    "Nothing", "Anything", "Something", "Whatever", "Both", "Here", "As",
    "First", "These", "Those", "Take", "Start", "To", "Is", "How", "Whether",
    "Without", "End", "Any", "Nobody", "Already", "Our", "Book", "Ground",
    "God", "Godhead", "Their", "Its", "Everything", "Because", "Suppose",
    "Consider", "Call", "Say", "Let", "Once", "Still", "Even", "Only", "Yet",
    "Grade", "Tier", "Truth", "Play", "Player", "Source", "Focus", "Focusing",
    "Fullness", "Superposition", "Return", "Plenitude", "Relativism",
    "Certification", "Science", "SEES", "Black", "Will",
}

FOOTNOTE_REF = re.compile(r"\[\^[^\]]+\]")
SUP_TAG = re.compile(r"<sup\b", re.I)
NOTES_HEAD = re.compile(r"^#{1,4}\s*(?:NOTES?|ENDNOTES?)\b", re.I | re.M)


def strip_furniture(text):
    """Remove headings and code fences -- neither carries prose attribution."""
    text = re.sub(r"^```.*?^```", "", text, flags=re.M | re.S)
    text = re.sub(r"^#.*$", "", text, flags=re.M)
    return text


def find_sites(text):
    """Return [(name, context)] for roster names in attributive position."""
    flat = strip_furniture(text).replace("\n", " ")
    hits = []
    patterns = [
        rf"\b({NAME_TOK})(?:’s|'s)\s+[a-z]",           # Gibson's affordances
        rf"\b({NAME_TOK})(?:’s|'s)?\s+(?:{ATTRIB_VERB})\b",  # Searle argues
        rf"(?:according to|per|following|after)\s+({NAME_TOK})\b",
    ]
    for pat in patterns:
        for m in re.finditer(pat, flat):
            raw = m.group(1).strip()
            if raw.split()[0] in STOP:
                continue
            key = ROSTER_LAST.get(raw.split()[-1])
            ctx = flat[max(0, m.start() - 60): m.end() + 60]
            ctx = re.sub(r"\s+", " ", ctx).strip()
            hits.append((key or raw, ctx, key is not None))
    return hits


def count_receipts(text):
    return len(FOOTNOTE_REF.findall(text)) + len(SUP_TAG.findall(text)) + \
        (1 if NOTES_HEAD.search(text) else 0)


def main():
    show_sites = "--sites" in sys.argv
    only = None
    if "--chapter" in sys.argv:
        only = sys.argv[sys.argv.index("--chapter") + 1].upper()

    files = sorted(
        (p for p in BOOK.glob("*.md") if CHAPTER_RE.match(p.name)),
        key=lambda p: (BOOK_ORDER.index(CHAPTER_RE.match(p.name)["book"]),
                       int(CHAPTER_RE.match(p.name)["n"])),
    )
    if not files:
        print("no chapters found -- is book/ where it was?")
        return 1

    per_book = defaultdict(lambda: [0, 0, 0])   # sources, receipts, chapters
    candidates = Counter()
    rows = []
    total_src = total_rcp = 0

    for p in files:
        m = CHAPTER_RE.match(p.name)
        bk, n = m["book"], int(m["n"])
        if only and not p.name.upper().startswith(only):
            continue
        text = p.read_text(encoding="utf-8")
        hits = find_sites(text)
        known = [h for h in hits if h[2]]
        for name, _, ok in hits:
            if not ok:
                candidates[name] += 1
        distinct = sorted({h[0] for h in known})
        receipts = count_receipts(text)
        exempt = bk in EXEMPT_BOOKS
        rows.append((f"{bk}.{n}", p.name, distinct, receipts, exempt, known))
        if not exempt:
            total_src += len(distinct)
            total_rcp += receipts
        e = per_book[bk]
        e[0] += len(distinct)
        e[1] += receipts
        e[2] += 1

    print("ENDNOTE DEBT — ruling 9 obeyed in its first half, measured in its second")
    print(f"  {BOOK}\n")
    print("  CH      sources  receipts   who")
    for tag, fname, distinct, receipts, exempt, known in rows:
        if exempt:
            mark = "  —  exempt (Book I takes no apparatus, ruling 9)"
            print(f"  {tag:<7} {len(distinct):>5}  {receipts:>7}   {mark}")
            continue
        flag = "" if receipts >= len(distinct) else "  ⚠"
        who = ", ".join(distinct) if distinct else "(no attributive name found)"
        print(f"  {tag:<7} {len(distinct):>5}  {receipts:>7}{flag}  {who[:72]}")

    print()
    for bk in BOOK_ORDER:
        if bk not in per_book:
            continue
        s, r, c = per_book[bk]
        tail = "  exempt" if bk in EXEMPT_BOOKS else ""
        print(f"  Book {bk:<5} {c:>2} ch   sources {s:>3}   receipts {r:>3}{tail}")

    print()
    print(f"  ★ RECEIPTS / NAMED SOURCES (Books II onward):  {total_rcp} / {total_src}")
    if total_rcp == 0 and total_src:
        print("    That zero is ruling 117's finding, now printed by an instrument.")
    print(f"    Coverage: {(100*total_rcp/total_src if total_src else 0):.0f}%"
          f"   ·   debt: {total_src - total_rcp} notes owed")

    if candidates:
        print(f"\n  CANDIDATES — attributive names the roster does not know ({len(candidates)}):")
        print("    (this gauge has NOT measured the whole book until these are triaged)")
        for w, c in candidates.most_common(25):
            print(f"    {c:>3}  {w}")

    if show_sites:
        print("\n  SITES — the worklist, one line per attribution:")
        for tag, fname, distinct, receipts, exempt, known in rows:
            if exempt or not known:
                continue
            print(f"\n  [{tag}] {fname}")
            seen = set()
            for name, ctx, _ in known:
                if name in seen:
                    continue
                seen.add(name)
                print(f"    {name:<14} … {ctx[:130]}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
