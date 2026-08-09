#!/usr/bin/env python3
"""
ENDNOTE DEBT  —  Truth and Consequences.  Rebuilt Day 190 under R-71.

Ruling 9 (Day 186, Clayton), in full:

    "Book I: nothing. Everywhere after: the name lives in the sentence; the
     source lives in an endnote. Per-chapter, numbered, at the back of the book."

We obey the first half on every page. Books II-V have never executed the second.
This gauge measures the second half, per chapter, and prints the debt.

WHAT THE FIRST VERSION GOT WRONG  (R-71, and it is the reason for this rewrite)
------------------------------------------------------------------------------
v1 matched attributive names AGAINST A CURATED ROSTER and counted only the ones
the roster already knew. That is a ROSTER-MEMBERSHIP TEST wearing an ATTRIBUTION
detector's clothes, and it fails in the worst available direction:

    a chapter citing five famous rostered names it never opened reports well;
    a chapter that went and found the actual scholarship on its own subject
    reports `sources 0 -- no attributive name found`.

It did not merely under-count the behaviour the retrofit exists to produce. It
PENALISED it, hardest in exactly the chapters whose receipts matter most --
because a rostered name is one a reader can check unaided and a new one is not.
Live proof: VI.4 cites eight authors in eight full notes and v1 printed
`sources 3  --  Augustine, Barfield, Plato`, of whom TWO ARE NOT ITS SOURCES.

THE ROSTER IS GONE. Names are extracted from the prose.

WHAT IT COUNTS NOW
------------------
The file is split at the notes block, because the two halves do different jobs:

PROSE       everything before the first `[^n]:` definition or NOTES heading.
            Attribution happens here. Each sentence is read for names in
            attributive position -- possessive ("Gibson's affordances"), or
            adjacent to an attribution verb ("Searle argues"), or after
            "according to / per / following".

NOTES       the block itself. This is where receipts live, and a receipt is
            counted only if IT NAMES SOMEBODY -- not as a bare marker. v1
            counted `[^3]` at the call site AND at the definition AND the
            NOTES heading, so VI.4's eight notes scored 18 and the coverage
            line read 600%. A marker is not a receipt. A note naming a source
            is.

Three exclusions, applied per sentence, each of them a rule about SCOPE rather
than about a list of people:

CROSS-REF   a name preceded IN ITS OWN SENTENCE by a pointer to another part of
            this book ("VI.2 took what Julian Jaynes's evidence could bear").
            The receipt for that source lives where the source was first used.
            A back-reference does not owe a fresh note.
SUBORDINATE a name preceded in its sentence by another attributive name
            ("Havelock's observation is that Plato's hostility..."). The outer
            subject is the source; names inside its complement are its SUBJECT
            MATTER. Plato is what Havelock is talking about, not an authority
            this chapter is leaning on.
COMMON NOUN a candidate whose lowercase form appears twice or more as a
            standalone word in the same chapter. "Print did not bring fixity"
            is not a citation of somebody called Print. This test is MEASURED
            against the text rather than hand-listed, so it needs no upkeep.

A name is a SOURCE if it stands as the governing subject in AT LEAST ONE
sentence. Being subordinate somewhere does not demote it -- VI.4 says "VI.4 now
takes McGilchrist's conclusion" (cross-ref shape) and also gives McGilchrist a
governing sentence of his own, and he is correctly a source.

WHAT THIS GAUGE STILL CANNOT DO, PRINTED EVERY RUN
--------------------------------------------------
It cannot tell an authority from a historical actor. VI.4 attributes actions to
Ambrose, who is the subject of the chapter's opening scene and not a cited
scholar. He surfaces as an uncovered source and a reader has to say so. That is
reported as a LIMIT, not hidden: every exclusion class is printed with counts,
so a wrong exclusion is visible instead of silent. R-66's finding, applied
here: report BLINDNESS, never ABSENCE.

Usage:  python tools/endnote_debt.py [--sites] [--chapter VI-04] [--limits]
"""

import re
import sys
import pathlib
from collections import Counter, defaultdict

ROOT = pathlib.Path(__file__).resolve().parents[1]
BOOK = ROOT / "book"

CHAPTER_RE = re.compile(r"^(?P<book>I{1,3}|IV|V|VI{1,3})-(?P<n>\d\d)-")
BOOK_ORDER = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII"]

# Book I takes no apparatus, by ruling 9. Not a debt; the design.
EXEMPT_BOOKS = {"I"}

# Attribution verbs, built from stems so the participle and progressive forms are
# not lost. v1 listed finite forms only, so "Augustine is recording his own..."
# scored zero in the chapter that OPENS with Augustine. "not" is written out
# explicitly rather than stemmed from "note" -- a bare "not" would match
# "Augustine was not amazed" and turn every negation into a citation.
_STEMS = [
    "argu", "writ", "call", "nam", "show", "coin", "observ", "claim", "describ",
    "report", "propos", "remark", "ask", "answer", "term", "phras", "record",
    "demonstrat", "trac", "conclud", "insist", "deni", "distinguish", "quot",
]
_IRREG = (r"notes?|noted|noting|wrote|written|says?|said|holds?|held|put it|"
          r"puts it|found|thought|showed|shown|tells?|told|meant")
ATTRIB_VERB = "(?:" + "|".join(s + r"(?:e?s|ed|ing)?" for s in _STEMS) + \
              "|" + _IRREG + ")"
# an auxiliary or adverb may sit between the name and the verb
AUX = r"(?:\s+(?:is|was|are|were|has|had|also|then|later|here|elsewhere|already|"
AUX += r"never|often|again|now|thus|therefore|indeed|himself|herself))?"
NAME_TOK = r"[A-Z][a-zA-ZÀ-ſĀ-ſ.'’-]+(?:\s+[A-Z][a-zA-ZÀ-ſ.'’-]+){0,2}"

# Capitalized words that open sentences or are book furniture. These are STRIPPED
# from the front of a multi-token match ("On Eisenstein's account" -> Eisenstein),
# not used to reject the match outright -- v1 rejected and lost the name with it.
OPENERS = {
    "The", "And", "It", "This", "That", "What", "If", "But", "A", "An", "In",
    "So", "Then", "You", "He", "She", "They", "We", "There", "Not", "No",
    "Now", "One", "Two", "Three", "Four", "Which", "When", "Where", "Every",
    "Nothing", "Anything", "Something", "Whatever", "Both", "Here", "As",
    "First", "Second", "Third", "These", "Those", "Take", "Start", "To", "Is",
    "How", "Whether", "Without", "End", "Any", "Nobody", "Already", "Our",
    "Book", "Books", "Chapter", "Because", "Suppose", "Consider", "Call",
    "Say", "Let", "Once", "Still", "Even", "Only", "Yet", "For", "At", "By",
    "On", "Of", "With", "From", "Their", "Its", "His", "Her", "Everything",
    "Everybody", "Somebody", "Neither", "Either", "Each", "Most", "Much",
    "Many", "Some", "All", "Nor", "Or", "Before", "After", "Until", "While",
    "Since", "Though", "Although", "Unless", "Whereas", "Given", "Read",
}

# a pointer to another part of this book: VI.2 / IV.11 / Book III / Books I-III
CHAPTER_PTR = re.compile(
    r"\b(?:I{1,3}|IV|VI{1,3}|VII|VIII|V)\.\d+\b"
    r"|\bBooks?\s+(?:I{1,3}|IV|VI{1,3}|VII|VIII|V)\b"
    r"|\bBooks?\s+[IVX]+[–—-][IVX]+\b"
)

NOTE_DEF = re.compile(r"^\[\^([^\]]+)\]:\s*(.*)$", re.M)
NOTES_HEAD = re.compile(r"^#{1,4}\s*(?:NOTES?|ENDNOTES?)\b", re.I | re.M)
SENT_SPLIT = re.compile(r"(?<=[.!?])\s+(?=[A-Z“\"*★⚠—])")


def split_prose_notes(text):
    """Prose is everything before the apparatus. Attribution lives in one half,
    receipts in the other, and reading them as one text is how v1 scored a
    chapter's own bibliography as evidence of its prose."""
    cuts = []
    m = NOTE_DEF.search(text)
    if m:
        cuts.append(m.start())
    m = NOTES_HEAD.search(text)
    if m:
        cuts.append(m.start())
    if not cuts:
        return text, ""
    cut = min(cuts)
    return text[:cut], text[cut:]


def strip_furniture(text):
    """Headings and code fences carry no prose attribution."""
    text = re.sub(r"^```.*?^```", "", text, flags=re.M | re.S)
    text = re.sub(r"^#.*$", "", text, flags=re.M)
    return text


def clean_name(raw):
    """Strip leading sentence-openers; return (display, surname) or None.

    The trailing-possessive strip is load-bearing. NAME_TOK admits an apostrophe
    (O'Brien, Sohravardī's transliterations), so "Everett's" is swallowed WHOLE
    into the match and keys the source as `Everett's` -- which then never matches
    `Everett` in the notes, and the chapter reports an uncovered source it has
    actually paid for."""
    toks = [t for t in raw.replace("’", "'").split() if t]
    while toks and toks[0].strip(".,;:'") in OPENERS:
        toks.pop(0)
    if not toks:
        return None
    toks = [re.sub(r"'s$", "", t) for t in toks]
    surname = toks[-1].strip(".,;:'")
    if len(surname) < 3 or surname in OPENERS or surname.isupper():
        return None
    return " ".join(toks).strip(".,;:'"), surname


def common_noun_counts(prose):
    """Lowercase standalone-word frequencies. A capitalized token whose lowercase
    twin is ordinary vocabulary in this very chapter is not a person. Measured,
    not curated -- so it stays true as the book grows."""
    return Counter(re.findall(r"\b[a-z][a-z'-]{2,}\b", prose))


def scan_prose(prose, corpus_lower=None):
    """Return (sources, crossrefs, subordinates, commons, sites).

    sources: {surname: display} for names governing at least one sentence."""
    flat = strip_furniture(prose)
    lower = common_noun_counts(flat)
    corpus_lower = corpus_lower or Counter()
    flat = re.sub(r"\s+", " ", flat.replace("\n", " "))

    # NOTE the `[*_]*` after the possessive. Without it, "Taylor's *buffered* self"
    # does not match -- the markdown emphasis marker sits where the scan expects a
    # lowercase letter, and the source vanishes. Same family as R-63: a prose gauge
    # blind to the markup the prose is written in.
    patterns = [
        rf"\b({NAME_TOK})(?:’s|'s)\s+[*_]*[a-z]",                    # Gibson's affordances
        rf"\b({NAME_TOK})(?:’s|'s)?{AUX}\s+(?:{ATTRIB_VERB})\b",     # Searle argues
        rf"(?:according to|per|following)\s+({NAME_TOK})\b",
    ]

    sources, crossrefs, subordinates, commons = {}, Counter(), Counter(), Counter()
    sites = defaultdict(list)

    for sent in SENT_SPLIT.split(flat):
        hits = []
        for pat in patterns:
            for m in re.finditer(pat, sent):
                cn = clean_name(m.group(1))
                if not cn:
                    continue
                display, surname = cn
                # TWO SCALES, because one chapter is a small sample. "Western",
                # "Faith", "Ground" survive a chapter-local test and are plainly
                # not authors; across 47 chapters their lowercase twins are
                # everywhere. Still measured against the text, still no curated
                # list to maintain -- just a corpus the size of the book.
                if lower[surname.lower()] >= 2 or corpus_lower[surname.lower()] >= 8:
                    commons[surname] += 1
                    continue
                hits.append((m.start(1), display, surname))
        if not hits:
            continue
        hits.sort()
        ptrs = [m.start() for m in CHAPTER_PTR.finditer(sent)]
        seen_earlier = set()
        for pos, display, surname in hits:
            if any(p < pos for p in ptrs):
                crossrefs[surname] += 1
            elif seen_earlier:
                subordinates[surname] += 1
            else:
                prev = sources.get(surname, "")
                if len(display) > len(prev):
                    sources[surname] = display
                sites[surname].append(sent.strip()[:150])
            seen_earlier.add(surname)

    return sources, crossrefs, subordinates, commons, sites


def scan_notes(notes_block):
    """Return (n_notes, named_in_notes). A note counts only if it names somebody:
    a bare marker is not a receipt."""
    named = set()
    n = 0
    for m in NOTE_DEF.finditer(notes_block):
        body = m.group(2)
        toks = re.findall(r"\b[A-Z][a-zA-ZÀ-ſ'’-]{2,}\b", body)
        real = [t for t in toks if t not in OPENERS]
        if real:
            n += 1
            named.update(real)
    return n, named


def chapter_files():
    return sorted(
        (p for p in BOOK.glob("*.md") if CHAPTER_RE.match(p.name)),
        key=lambda p: (BOOK_ORDER.index(CHAPTER_RE.match(p.name)["book"]),
                       int(CHAPTER_RE.match(p.name)["n"])),
    )


def book_totals():
    """(sources, covered, notes) across Books II onward.

    THE PUBLIC ENTRY POINT, and it exists because of how this rewrite nearly went
    wrong: `where_the_book_is` reached into v1's internals (`find_sites`,
    `count_receipts`), both of which this file deleted, inside a `try/except` that
    would have printed 'gauge unavailable' every run instead of failing. The one
    instrument every planning decision consults would have gone quiet politely.
    Consumers get a function; internals are free to change."""
    files = chapter_files()
    corpus = Counter()
    parsed = []
    for p in files:
        prose, notes_block = split_prose_notes(p.read_text(encoding="utf-8"))
        corpus += common_noun_counts(strip_furniture(prose))
        parsed.append((p, prose, notes_block))

    src = cov = notes = 0
    for p, prose, notes_block in parsed:
        if CHAPTER_RE.match(p.name)["book"] in EXEMPT_BOOKS:
            continue
        sources, cross, _sub, _c, _s = scan_prose(prose, corpus)
        n_notes, named = scan_notes(notes_block)
        for surname in list(cross):
            if surname in named and surname not in sources:
                sources[surname] = surname
        src += len(sources)
        cov += sum(1 for s in sources if s in named)
        notes += n_notes
    return src, cov, notes


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

    # Built from every chapter INCLUDING Book I -- the common-word test wants the
    # largest honest sample of this book's ordinary vocabulary, and Book I's
    # exemption is about apparatus, not about English.
    corpus_lower = Counter()
    for p in files:
        corpus_lower += common_noun_counts(
            strip_furniture(split_prose_notes(p.read_text(encoding="utf-8"))[0]))

    per_book = defaultdict(lambda: [0, 0, 0, 0])   # sources, covered, notes, chapters
    rows = []
    all_cross, all_sub, all_common = Counter(), Counter(), Counter()
    all_source_names = set()
    total_src = total_cov = total_notes = 0

    for p in files:
        m = CHAPTER_RE.match(p.name)
        bk, n = m["book"], int(m["n"])
        if only and not p.name.upper().startswith(only):
            continue
        text = p.read_text(encoding="utf-8")
        prose, notes_block = split_prose_notes(text)
        sources, cross, sub, common, sites = scan_prose(prose, corpus_lower)
        n_notes, named = scan_notes(notes_block)

        # A CROSS-REF THIS CHAPTER WROTE A NOTE FOR IS NOT A CROSS-REF.
        # The cross-ref rule guesses where a receipt lives; a note in this
        # chapter's own apparatus ANSWERS that, so the note wins. VI.4 says
        # "Book VI has been circling since VI.3: Taylor's *buffered* self" and
        # then pays Taylor a full note at [^4] -- the chapter is claiming him.
        # Deliberately NOT extended to subordinates: a name inside another
        # author's argument can reach the notes as part of a TITLE (Havelock,
        # "Preface to Plato") without ever being this chapter's authority.
        for surname in list(cross):
            if surname in named and surname not in sources:
                sources[surname] = surname
                sites[surname].append("(cross-ref promoted: this chapter wrote it a note)")
                del cross[surname]

        all_cross += cross
        all_sub += sub
        all_common += common
        all_source_names.update(sources)

        covered = sorted(s for s in sources if s in named)
        uncovered = sorted(s for s in sources if s not in named)
        exempt = bk in EXEMPT_BOOKS
        rows.append((f"{bk}.{n}", p.name, sources, covered, uncovered,
                     n_notes, exempt, sites))
        if not exempt:
            total_src += len(sources)
            total_cov += len(covered)
            total_notes += n_notes
        e = per_book[bk]
        e[0] += len(sources)
        e[1] += len(covered)
        e[2] += n_notes
        e[3] += 1

    print("ENDNOTE DEBT — ruling 9 obeyed in its first half, measured in its second")
    print(f"  {BOOK}   (names EXTRACTED from prose; no roster — R-71)\n")
    print("  CH      sources  notes  covered   owed a receipt")
    for tag, fname, sources, covered, uncovered, n_notes, exempt, _ in rows:
        if exempt:
            print(f"  {tag:<7} {len(sources):>5}  {n_notes:>5}      —    "
                  f"exempt (Book I takes no apparatus, ruling 9)")
            continue
        flag = "  " if not uncovered else " ⚠"
        who = ", ".join(uncovered) if uncovered else "(none — chapter is square)"
        print(f"  {tag:<7} {len(sources):>5}  {n_notes:>5}  {len(covered):>7}{flag} {who[:60]}")

    print()
    for bk in BOOK_ORDER:
        if bk not in per_book:
            continue
        s, c, nt, ch = per_book[bk]
        tail = "   exempt" if bk in EXEMPT_BOOKS else f"   owed {s - c:>3}"
        print(f"  Book {bk:<5} {ch:>2} ch   sources {s:>3}   notes {nt:>3}   covered {c:>3}{tail}")

    print()
    pct = (100 * total_cov / total_src) if total_src else 0
    print(f"  ★ SOURCES WITH A RECEIPT (Books II onward):  {total_cov} / {total_src}"
          f"   ·   {pct:.0f}%   ·   DEBT {total_src - total_cov} notes owed")
    print(f"    notes actually written: {total_notes}"
          "   (a marker is not a receipt; a note that names somebody is)")

    print("\n  WHAT THIS RUN EXCLUDED — printed so a wrong exclusion is visible:")
    print("    (names counted as a source SOMEWHERE are dropped from these lines —"
          " a name\n     subordinate in one sentence and governing in another is"
          " not an exclusion)")

    def _lost(counter):
        return Counter({k: v for k, v in counter.items() if k not in all_source_names})

    for label, counter in (("cross-refs to other chapters", _lost(all_cross)),
                           ("subordinate to another name ", _lost(all_sub)),
                           ("common nouns (lowercase ≥2) ", _lost(all_common))):
        names = ", ".join(w for w, _ in counter.most_common(8))
        print(f"    {label} : {sum(counter.values()):>4}  {names}")
    print("    LIMIT: this cannot tell a cited authority from a historical actor.")
    print("           A name in the scene rather than the bibliography reads as debt.")

    if show_sites:
        print("\n  SITES — the worklist, one line per source:")
        for tag, fname, sources, covered, uncovered, n_notes, exempt, sites in rows:
            if exempt or not sources:
                continue
            print(f"\n  [{tag}] {fname}")
            for surname, display in sorted(sources.items()):
                mark = "✓" if surname in covered else "⚠"
                ctx = sites[surname][0] if sites[surname] else ""
                print(f"    {mark} {display:<22} … {ctx[:110]}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
