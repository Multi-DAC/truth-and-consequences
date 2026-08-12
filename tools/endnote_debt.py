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

# Books the R-2 retrofit pass has actually been RUN over. This is a DECLARATION,
# not a measurement, and it is here because the tool could not tell the two zeros
# apart: II.4 extracts 0 sources and carries 0 notes because the pass ran and the
# chapter needed nothing, while IV.1 extracts 0 sources and carries 0 notes
# because nobody has ever looked. Both printed "(none -- chapter is square)".
# Five chapter rows in an untouched book read as CLEAN. Undeclared is not square;
# it is unmeasured, and it now says so. The declaration is itself checked below
# against notes on disk, so a book listed here that carries no apparatus raises an
# alarm rather than quietly vouching for itself.
RETROFITTED_BOOKS = {"II", "III", "IV", "V", "VI", "VII", "VIII"}
# V added Day 192 — 11/11 chapters carry apparatus (163 notes), which CLOSES THE RETROFIT:
# every book II–VIII now carries one. V.11 was the last chapter and the only one owed at
# the time (6 names), and it went to 0 with 29 notes. Its one residual, `East`, was the
# R-203 class predicted in advance — "The East asked the count question" is a region, the
# same defect as V.9's "Hampshire" being half of New Hampshire.
#
# ⛔ AND THE WHOLE-BOOK RESIDUAL WAS HAND-CHECKED THE SAME NIGHT, all thirteen, one at a
# time against their own evidence sentences, because the alternative is a filter written
# by the party it exonerates. Not one is an uncited source:
#   Certification  II.7:50   sentence-initial common noun
#   Plenitude      III.3:196 sentence-initial common noun, and the book's OWN term
#   Claus/Scotland/Western/Father/Islamicist  -- the five recorded above for IV, unchanged
#   Religious      V.4:31    sentence-initial adjective
#   Western        VI.3:28   adjectival
#   Gold, Moon     VI.3:36   metals and planets in the correspondence scheme -- objects
#   Enlightenment  VII.8:336 a period, not a person
#   Clayton        VII.8:389 "Clayton's amendment" -- the book's editor, named on purpose
# 13/13 in classes the LIMIT block below already declares. THE NUMBER IS NOT ZERO AND IS
# NOT BEING MADE ZERO: no threshold moved, no name was excluded, the rows still print.
# What changed is that each has been READ. [[feedback_never_relax_the_gauge_that_caught_you]]
# IV added Day 192, on the stated condition ("add it when the book closes") and NOT on
# a clean owed-count. 10/10 chapters carry apparatus (74 notes) and R-110's mandatory
# edition sweep has run. The five names still printed as owed were hand-checked one at
# a time against their own evidence sentences rather than waved through as artifact:
#   Claus    IV.7:515  Santa Claus -- the chapter's worked EXAMPLE ENTITY, not a source
#   Scotland IV.7:404  "the Findhorn community in Scotland" -- toponym
#   Western  IV.7:91   "the Western record" -- adjectival
#   Father   IV.9:260  "a Church Father's testimony" -- common noun; the actual
#                      Ante-Nicene Fathers citation IS receipted at IV.9:569
#   Islamicist IV.10   Corbin, receipted at IV.7 [^8]/[^9], cross-referenced IV.10 [^8]
# Five for five fall in classes this file's own LIMIT block declares. Recorded here
# because a declaration entered by the party it exonerates needs its working shown.

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
# NOTE_DEF captures ONE LINE. Every receipt in this book is wrapped to ~80
# columns, so a name paid on the second line of a note was invisible to
# scan_notes and the chapter reported it as an unpaid source. Found Day 190 at
# VII.2, where Kant is credited on line 2 of [^17] and the chapter still read
# `⚠ Kant`. This splitter takes the WHOLE body of each note. It widens the
# window, so it also widens the tool's standing LIMIT (it cannot tell a cited
# authority from a name that merely appears) by however long the note is.
NOTE_SPLIT = re.compile(r"^\[\^[^\]]+\]:", re.M)
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


# ---------------------------------------------------------------------------
# NON-PERSON CLASSES — added Day 191, after a full enumeration of all 153
# extracted names against their evidence sentences.
#
# WHY THIS EXISTS. The frequency test above catches a capitalized token whose
# LOWERCASE twin is ordinary vocabulary. It cannot catch a token the book
# ALWAYS capitalizes -- `Western`, `Certification`, `Plenitude`, `Relativism`,
# `East` -- because there is no lowercase twin to count. Those came through as
# sources and the debt figure carried them.
#
# THE MEASUREMENT, Day 191, over all 153: 41 were not citable persons = 26.8%.
# ⛔ AND THE POINT THAT MATTERS: the LIMIT line this file has printed every run
# since it was written declares ONLY the scene-actor class -- 8 of 41. **The
# disclaimer covered a fifth of its own artifact and read like it covered all
# of it.** A stated limit is not the same as a measured one.
#
# WHAT THE RULES BELOW ACTUALLY REACH, measured after implementing them and NOT
# as estimated before: 14 of the 41. The first draft of this comment claimed 33
# and that was a prediction written next to the code that would falsify it.
# The residual is 27 of a 139 denominator -- STILL 19.4% artifact. The number
# got better and did not get clean, and it must not be quoted as clean.
#
# ⚠ CONFLICT OF INTEREST, DECLARED. This patch was written by the drafter who
# owes the debt it reduces, on the day he wanted the number smaller. So the
# rules below are deliberately narrower than the audit supports: only classes
# decidable by a rule that mentions no name from this book. Toponyms
# (`Scotland`, `Toledo`, `New Hampshire`), objects (`Gold`, `Moon`, `Mercury`)
# and scene actors are LEFT IN THE DEBT and reported as a residual, because
# excluding them needs a gazetteer or a judgement, and a judgement made by the
# interested party is not a gauge. When in doubt the name stays as debt.
#
# ⛔ AND THE ERROR RUNS BOTH WAYS -- do not read this as "the number was too
# big". V.5 extracts `Ding` and `Yan Hui`, who are characters in Zhuangzi, and
# does NOT extract Zhuangzi, who is the source. III.3 extracts three Borges
# characters. The gauge over-counts characters and under-counts the author they
# belong to, which is a worse failure than inflation and is NOT fixed here.
NONPERSON = defaultdict(Counter)   # class -> {name: hits}, accumulated across the run
CALENDAR = {
    "January", "February", "March", "April", "May", "June", "July", "August",
    "September", "October", "November", "December", "Monday", "Tuesday",
    "Wednesday", "Thursday", "Friday", "Saturday", "Sunday",
}
# Tradition / adherent / adjectival morphology. A single token ending this way
# names a school, not a member of one. Kept to single tokens on purpose: "Eric
# Havelock" must never be tested by its second word.
TRADITION_SUFFIX = re.compile(r"^[A-ZÀ-ſ][\w’'-]*?(ism|isms|ist|ists|ian|ians|ic|ics)$")
# A source whose name is another source's name plus an institution word is that
# source's organisation, not a second authority. `Monroe Institute` under
# `Monroe`; `Aristotelian Society` under the citation that names it.
INSTITUTION_WORD = re.compile(
    r"\b(Institute|Society|Foundation|University|College|Press|Group|Trust|Association)$")


GIVEN_NAMED = set()   # surnames ever seen preceded by a given name, book-wide
_GIVEN_PAIR = re.compile(r"\b([A-Z][a-zà-ſ]{2,})\s+([A-Z][\wÀ-ſ’'-]+)\b")


def build_given_named(texts):
    """Surnames that appear at least once with a GIVEN NAME in front of them.

    ⛔ THIS GUARD EXISTS BECAUSE THE SUFFIX RULE ATE A REAL SOURCE ON ITS FIRST
    RUN. `McGilchrist` ends in -ist. Iain McGilchrist is VI.4's load-bearing
    citation, and the tradition rule deleted him from the debt silently --
    except that it did not, because this file prints every exclusion BY NAME
    and he was sitting in the list. That is the whole argument for printing
    exclusions rather than counts: the filter's own error was legible in its
    output on the first run.

    The guard's errors run TOWARD KEEPING DEBT: a wrongly-rescued name stays
    owed, which is the safe direction for a gauge its own author wants smaller.
    """
    for t in texts:
        for m in _GIVEN_PAIR.finditer(t):
            first, second = m.group(1), m.group(2)
            if first in OPENERS:
                continue
            GIVEN_NAMED.add(second)


def non_person_class(surname, display):
    """Return the exclusion class for a non-person candidate, or None.

    Rule-decidable only. Mentions no name from this manuscript, so it stays
    true as the book grows -- the design constraint the frequency test was
    written under, kept."""
    if surname in CALENDAR or display in CALENDAR:
        return "calendar"
    if (" " not in surname and TRADITION_SUFFIX.match(surname)
            and surname not in GIVEN_NAMED):
        return "tradition/adjectival"
    if INSTITUTION_WORD.search(display):
        return "institution"
    return None


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
                # TWO SCALES, because one chapter is a small sample. "Faith" and
                # "Ground" survive a chapter-local test and are plainly not
                # authors; across the chapter corpus their lowercase twins are
                # everywhere (15 and 134). Still measured against the text, still
                # no curated list to maintain -- just a corpus the size of the book.
                #
                # ⛔ Day 192: this comment listed "Western" FIRST among the three
                # cases the corpus scale rescues. Measured: `western` lowercase
                # appears ZERO times in the chapter corpus, and `Western` is still
                # owed in IV.7 and VI.3 today. The rule's own lead example is the
                # one it cannot reach -- a word the book capitalizes ALWAYS has no
                # lowercase twin to count, so the frequency test is structurally
                # blind exactly where a word is most consistently used as a title.
                # The comment asserted "everywhere" about a set it never counted.
                # The threshold 8 is likewise an integer chosen once and never
                # gauged, and it sits directly on top of the false-positive
                # cluster: religious 6, plenitude 7, father 5, east 3. NOT lowered
                # here -- a relaxation proposed by the party it exonerates is the
                # move to distrust, and the errors are declared to run toward
                # KEEPING debt. Declared, not filtered.
                if lower[surname.lower()] >= 2 or corpus_lower[surname.lower()] >= 8:
                    commons[surname] += 1
                    continue
                # Day 191: the classes the frequency test structurally cannot
                # see, because the book never lowercases them.
                klass = non_person_class(surname, display)
                if klass:
                    NONPERSON[klass][surname] += 1
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
    a bare marker is not a receipt.

    ⛔ THE POSSESSIVE STRIP BELOW IS THE SAME REPAIR `clean_name` ALREADY
    CARRIES, AND IT WAS MISSING HERE FOR AS LONG AS BOTH HAVE EXISTED.
    clean_name's docstring states the failure exactly -- "'Everett's' is
    swallowed WHOLE into the match and keys the source as `Everett's` -- which
    then never matches `Everett` in the notes, and the chapter reports an
    uncovered source it has actually covered" -- and the fix was applied to the
    PROSE side only. The token class here admits ' and ’, so a note reading
    "Galle's confirmation from Berlin" registered the name `Galle's` and left
    the source `Galle` reading as owed. VIII.2 has named Galle in [^5] the
    whole time.

    THE LESSON, and it is the one this manuscript keeps re-learning: a repair
    scoped to the place the defect was FOUND leaves its siblings standing. The
    two scanners are twenty lines apart in one file and one of them describes,
    in prose, the bug the other one still had. Found Day 191, by a debt figure
    that disagreed with a note anyone could read.
    """
    named = set()
    n = 0
    for body in NOTE_SPLIT.split(notes_block)[1:]:
        toks = re.findall(r"\b[A-Z][a-zA-ZÀ-ſ'’-]{2,}\b", body)
        real = []
        for t in toks:
            if t in OPENERS:
                continue
            real.append(t)
            bare = re.sub(r"(?:’s|'s|’|')$", "", t)
            if bare and bare != t:
                real.append(bare)
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
    flats = []
    for p in files:
        prose, notes_block = split_prose_notes(p.read_text(encoding="utf-8"))
        flat = strip_furniture(prose)
        corpus += common_noun_counts(flat)
        flats.append(flat)
        parsed.append((p, prose, notes_block))
    # ⛔ MECHANISM-WITHOUT-A-TRIGGER, MINE, CAUGHT WITHIN THE HOUR. The given-name
    # guard was built in main() only, so THIS path -- the one every planning
    # decision actually consults, via where_the_book_is -- ran with GIVEN_NAMED
    # empty and re-excluded McGilchrist. The two entry points disagreed by 2
    # sources and nothing errored: 62/139 here, 61/137 there. A guard installed
    # on one caller is not installed.
    build_given_named(flats)

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


def selftest():
    """Positive control for the Day-191 non-person rules AND for the guard.

    A zero is worthless without a control of the same shape: if these rules
    silently stopped firing, the debt would climb back to 153 and read as
    honest work rather than as a broken filter. Each case below is a REAL
    string this book produced."""
    GIVEN_NAMED.clear()
    GIVEN_NAMED.update({"McGilchrist", "Havelock"})
    cases = [
        # (surname, display, expected class)
        ("March",       "March",              "calendar"),
        ("Thursday",    "Thursday",           "calendar"),
        ("Buddhism",    "Buddhism",           "tradition/adjectival"),
        ("Whorfian",    "Whorfian",           "tradition/adjectival"),
        ("Stoics",      "Stoics",             "tradition/adjectival"),
        ("Institute",   "Monroe Institute",   "institution"),
        ("Society",     "Aristotelian Society", "institution"),
        # ⛔ THE ONE THAT MATTERS: a real source whose name ends in -ist.
        ("McGilchrist", "Iain McGilchrist",   None),
        # and plain surnames must be untouched by all three rules
        ("Borges",      "Borges",             None),
        ("Weil",        "Weil",               None),
    ]
    bad = 0
    for surname, display, expected in cases:
        got = non_person_class(surname, display)
        ok = got == expected
        bad += not ok
        print(f"  {'✓' if ok else '✗'} {display:<22} -> {str(got):<22}"
              f" expected {expected}")
    if bad:
        print(f"\n  ✗ {bad} CONTROL(S) FAILED — the exclusion rules are not doing"
              " what this file says they do.")
    else:
        print("\n  ✓ all controls pass — rules fire on the real strings, and the"
              "\n    given-name guard protects the real source that shares their shape.")
    GIVEN_NAMED.clear()
    return 1 if bad else 0


def main():
    if "--selftest" in sys.argv:
        return selftest()
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
    _flats = []
    for p in files:
        flat = strip_furniture(split_prose_notes(p.read_text(encoding="utf-8"))[0])
        corpus_lower += common_noun_counts(flat)
        _flats.append(flat)
    # Must run BEFORE any scan_prose call -- non_person_class reads GIVEN_NAMED.
    build_given_named(_flats)

    # sources, covered, notes, chapters, chapters-carrying-apparatus,
    # chapters that NEED apparatus (see the predicate at the accumulator)
    per_book = defaultdict(lambda: [0, 0, 0, 0, 0, 0])
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
        if n_notes:
            e[4] += 1
        # A chapter NEEDS apparatus if it cites anybody, or already carries notes,
        # or sits in a book nobody has looked at -- in an undeclared book a zero is
        # unmeasured, not square. The middle clause is what keeps II.4 (0 sources,
        # 0 notes, pass ran, needed nothing) out of the denominator: without it the
        # partial arm reported Book II as 7/8 and indicted the one chapter the
        # declaration was written to protect.
        if len(sources) or n_notes or (not exempt and bk not in RETROFITTED_BOOKS):
            e[5] += 1

    print("ENDNOTE DEBT — ruling 9 obeyed in its first half, measured in its second")
    print(f"  {BOOK}   (names EXTRACTED from prose; no roster — R-71)\n")
    print("  CH      sources  notes  covered   owed a receipt")
    for tag, fname, sources, covered, uncovered, n_notes, exempt, _ in rows:
        if exempt:
            print(f"  {tag:<7} {len(sources):>5}  {n_notes:>5}      —    "
                  f"exempt (Book I takes no apparatus, ruling 9)")
            continue
        # MEASURED first, declared only as the tie-breaker. Apparatus on disk is
        # positive proof the pass reached this chapter and needs no declaration;
        # the declaration is only load-bearing for the ambiguous zero (no notes,
        # no sources). Reading it the other way round -- book-level literal first
        # -- printed "an unrun pass" over six chapters of Book IV apparatus I had
        # written forty minutes earlier. R-145.
        unrun = n_notes == 0 and tag.split(".")[0] not in RETROFITTED_BOOKS
        flag = "  " if not uncovered else " ⚠"
        if uncovered:
            who = ", ".join(uncovered)
        elif unrun:
            flag = " ·"
            who = "(NOT RETROFITTED — an unrun pass, not a clean one)"
        else:
            who = "(none — chapter is square)"
        print(f"  {tag:<7} {len(sources):>5}  {n_notes:>5}  {len(covered):>7}{flag} {who[:60]}")

    print()
    for bk in BOOK_ORDER:
        if bk not in per_book:
            continue
        s, c, nt, ch, ch_app, ch_need = per_book[bk]
        if bk in EXEMPT_BOOKS:
            tail = "   exempt"
        elif ch_app == 0:
            tail = f"   owed {s - c:>3}  ⛔ PASS NEVER RUN"
        elif ch_app < ch_need:
            # The state the book-level literal could not express. A part-passed
            # book read as NEVER RUN until Day 191, which is the safe direction
            # and still a wrong number to plan tomorrow's worklist from.
            tail = f"   owed {s - c:>3}  ◐ PASS PARTIAL — {ch_app}/{ch_need} ch carry apparatus"
        else:
            tail = f"   owed {s - c:>3}"
        print(f"  Book {bk:<5} {ch:>2} ch   sources {s:>3}   notes {nt:>3}   covered {c:>3}{tail}")

    # The declaration above is a stamp, so give it a gauge. A book claimed as
    # retrofitted that carries no apparatus at all is the stamp having rotted.
    for bk in BOOK_ORDER:
        e = per_book.get(bk, (0, 0, 0, 0, 0, 0))
        if bk in RETROFITTED_BOOKS and e[2] == 0:
            print(f"\n  ⛔ RETROFITTED_BOOKS claims Book {bk} has been through the R-2 pass, "
                  f"but it carries 0 notes on disk. The declaration is wrong, not the book.")
        # AND THE OTHER DIRECTION, missing until Day 191. The check above only
        # caught a stamp that OVERCLAIMS. A stamp that UNDERCLAIMS -- notes on
        # disk, book not declared -- printed PASS NEVER RUN over real apparatus,
        # and nothing said so. Same asymmetry as the boot banner calling
        # working_memory.json stale on the morning it held the only true copy:
        # a gauge for "this stamp may have rotted" and none for "this
        # rotten-looking thing may be right." Both directions now speak.
        if bk not in RETROFITTED_BOOKS and bk not in EXEMPT_BOOKS and e[2]:
            print(f"\n  ◐ Book {bk} carries {e[2]} notes across {e[4]}/{e[3]} chapters and is NOT in "
                  f"RETROFITTED_BOOKS.\n    The disk is ahead of the declaration — add it when the "
                  f"book closes, not before.")

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

    for klass in sorted(NONPERSON):
        c = _lost(NONPERSON[klass])
        names = ", ".join(w for w, _ in c.most_common(8))
        print(f"    non-person: {klass:<18}: {sum(c.values()):>4}  {names}")

    print("\n  ⛔ THE LIMIT, AND ITS MEASURED SIZE — the second half added Day 191:")
    print("    STATED SINCE v1: this cannot tell a cited authority from a historical")
    print("      actor. A name in the scene rather than the bibliography reads as debt.")
    print("    MEASURED Day 191, by enumerating ALL 153 extracted names against their")
    print("      own evidence sentences: 41 were not citable persons — 26.8%.")
    print("      The stated limit above covers 8 of those 41. ⛔ THE DISCLAIMER WAS")
    print("      TRUE AND COVERED A FIFTH OF ITS OWN ARTIFACT, which reads exactly")
    print("      like covering all of it.")
    print("    ⛔ THE RULES ABOVE REACH 14 OF THE 41 — NOT the 33 first predicted.")
    print("      RESIDUAL ARTIFACT IS ~27 IN A 139 DENOMINATOR = ~19%. The number")
    print("      improved and is NOT clean; do not quote it as clean.")
    print("    STILL IN THE DEBT, deliberately (excluding them needs a gazetteer or a")
    print("      judgement, and the judgement would be made by the party it exonerates):")
    print("      toponyms (Scotland, Toledo, New Hampshire) · objects (Gold, Moon,")
    print("      Mercury) · scene actors (Ambrose, Santa Claus, Clayton) · the")
    print("      Borges/Zhuangzi dialogue characters · and `Islamicist`, which the")
    print("      new given-name guard FALSELY RESCUES from the tradition rule because")
    print("      the prose reads `French Islamicist`. Declared: the guard's errors")
    print("      run toward KEEPING debt, which is the safe direction here.")
    print("    ⛔ AND THE ERROR RUNS BOTH WAYS. V.5 extracts `Ding` and `Yan Hui`,")
    print("      Zhuangzi's characters, and does NOT extract Zhuangzi. III.3 extracts")
    print("      three Borges characters. Over-counting characters while missing the")
    print("      author they belong to is worse than inflation and is NOT fixed here.")
    print("    ⛔ NEW CLASS, measured Day 192 — NOT A MISCLASSIFIED PERSON, NOT A")
    print("      PERSON AT ALL. Six of the standing ⚠ are capitalized COMMON NOUNS:")
    print("      Religious (V.4), Certification (II.7), Plenitude (III.3), Father")
    print("      (IV.9), East (V.11), Western (IV.7, VI.3). The stated limit above")
    print("      names toponyms, objects and scene actors — all of which ARE names")
    print("      of something. This class names nothing. It survives because the")
    print("      lowercase-twin test needs 2 in-chapter or 8 corpus-wide hits and")
    print("      these sit at religious 6 · plenitude 7 · father 5 · east 3 ·")
    print("      certification 1 · western 0. THE THRESHOLD 8 SITS ON TOP OF THE")
    print("      CLUSTER and was never gauged. Deliberately NOT lowered: the party")
    print("      that would benefit is the one proposing it. Declared, not filtered.")
    print("    ⛔ AND `Western` WAS THE COMMENT'S OWN LEAD EXAMPLE of a case the")
    print("      corpus scale rescues. It has ZERO lowercase twins in the chapter")
    print("      corpus and is owed in two chapters right now. A word the book")
    print("      ALWAYS capitalizes has nothing to count, so this test is blind")
    print("      exactly where a common noun is used most consistently as a title.")

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
