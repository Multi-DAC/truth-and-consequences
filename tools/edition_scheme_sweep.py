#!/usr/bin/env python3
"""
EDITION / SCHEME SWEEP  —  Truth and Consequences.  Day 190.  R-108's sibling sweep, given a hand.

WHY THIS EXISTS.

R-108 (Day 190 night) found this in `IV-09-the-archetypal.md`:

    the chapter says  "Go and read II, 7, 5"      <- Massuet's division, via Jung
    the chapter says  "as Harvey prints it"        <- Harvey divides the same book differently
    Harvey prints that passage at LIB. II. vi. 3.

Both halves are true. The pair sends a reader to a chapter that does not contain the quotation.

    THE GENERAL FORM: an EDITION and a CITATION-SCHEME are two different facts, and prose that
    names one while numbering by the other reads as a single correct citation.

The row closed with a clause nobody could act on -- "check the same pair everywhere the book cites
a critical edition by a standard-scheme number" -- which is a sweep with no instrument, i.e. a
stamp. This is the instrument. It does not adjudicate; it ENUMERATES THE POPULATION so a human
adjudicates a list of eight instead of re-reading fifty-six chapters.

WHAT IT DOES, EXACTLY. Three passes, deliberately built from the GENERAL FORM and not from the
Irenaeus instance -- a grep derived from the defect just found returns its own reflection, not its
siblings.

    pass 1  EDITION-NAMINGS   "as X prints", "X's text/edition/translation", series sigla
                              (ANF, SBE, Loeb, PG/PL, Diels-Kranz, Stephanus, Bekker, ...)
    pass 2  LOCI              numeric  (roman-dotted, arabic-dotted, colon-form, folio)
                              AND scheme-word (Gate, Ennead, Question/Article, Nikaya, Logion...)
                              <- pass 2b exists because pass 2a MISSED `Gate III, chapter 4`
                                 on its first run. The numeric sweep could not see a locus whose
                                 scheme is spelled in words. Found by hand, mid-run, and the fix
                                 is here rather than in a note.
    pass 3  COVERAGE BOUND    every italicised work-title, and how many carry a locus at all.

THE LIMIT LINE, and it is the whole point of pass 3.

    This sweep can only inspect a citation that EXISTS. On Day 190 it reports 8 exposed loci
    against 368 distinct cited works, because Books II-V carry ZERO endnotes across 37 chapters
    and cite their sources by name with no locus and no apparatus. The edition-sensitive material
    in this volume -- Irenaeus, the Brahma Sutra, Nefesh HaChayim, the Zohar, Plotinus, Sankara --
    is concentrated in exactly the region with nothing to check.

    So a CLEAN RESULT HERE IS A FALSE NEGATIVE BY CONSTRUCTION. The endnote retrofit (R-2) will
    not merely reveal this population; it will CREATE it, roughly ninety citations at once. This
    sweep is therefore not a run-once-and-close: it is a mandatory step INSIDE R-2, re-run after
    each book's notes are written. The row says so; this docstring says so; the output says so.

Usage:  python tools/edition_scheme_sweep.py [--full]
Exit 0 always -- this is a census, not a pass/fail gauge. It has no idea which pairs are wrong.
"""

import re
import sys
import pathlib
import collections

ROOT = pathlib.Path(__file__).resolve().parents[1]
BOOK = ROOT / "book"
CHAPTER = re.compile(r"^(I|II|III|IV|V|VI|VII|VIII)-\d\d-")
BOOKS = {"I": 6, "II": 8, "III": 8, "IV": 10, "V": 11, "VI": 8, "VII": 9, "VIII": 7}

EDITION_SIGLA = re.compile(
    r"\b(ANF|NPNF|SBE|Loeb|Migne|PG|PL|Diels[- ]Kranz|Diels|Laks|Stephanus|Bekker|Akademie|"
    r"Harvey|Massuet|Thibaut|Vire[sś]var|Nag Hammadi|Vilna|Mantua|Fl[üu]gel|Vulgate|Septuagint|"
    r"LXX|Masoretic|KJV|RSV|NRSV|Douay|Sacred Books of the East|Ante-Nicene|Collected Works|"
    r"Standard Edition|Pritzker|Soncino|Steinsaltz|Dombart|Kalb|CCSL|CSEL|PTS)\b"
)
EDITION_PHRASE = re.compile(
    r"((?:as|the way) [A-Z][a-zÀ-ÿ]+ (?:prints|has|renders|gives|translates|sets)|"
    r"[A-Z][a-zÀ-ÿ]+'s (?:text|edition|Latin|Greek|Hebrew|translation|rendering|numbering|"
    r"division|recension|version)|(?:edited|translated|trans\.|ed\.) by [A-Z][a-zÀ-ÿ]+|"
    r"the [A-Z][a-zÀ-ÿ]+ (?:edition|recension|text))"
)
LOCUS_NUM = re.compile(r"\b[IVXLC]{1,6}[.,]\s?\d+(?:[.,]\s?\d+)?\b")
LOCUS_WORD = re.compile(
    r"\b(Gate|Sha'?ar|Tractate|Ennead|Treatise|Logion|Aphorism|Sutta|S[uū]tra|K[āa]ṇḍa|"
    r"Adhy[āa]ya|P[āa]da|Vagga|Nik[āa]ya|Canto|Question|Article|Surah|Sura|Psalm|Daf|Folio|"
    r"Codex|Homily|Mishnah|Gemara)\b[\s,]*(?:[IVXLC]+|\d+)?"
)
TITLE = re.compile(r"\*([A-ZĀŚṢ][^*\n]{3,60})\*")
TITLE_LOCUS = re.compile(r"\b([IVXLC]{1,6}[.,]\s?\d|\d{1,4}[:.]\d|q\.\s?\d|Gate|Ennead|chapter\s+\d|ch\.\s?\d)")
# a modern journal is volume:issue -- a scheme with no edition ambiguity. Matched by SHAPE
# (a serial name ending in a discipline word) as well as by a name list, because the first
# version of this line listed six journals and let `Personality and Social Psychology
# Bulletin` through on its opening word.
JOURNALISH = re.compile(
    r"^(Journal|Science|Nature|No[uû]s|Philosophical Review|Psychological|Inquiry|Annals|"
    r"Cognition|Slate)\b|\b(Journal|Review|Bulletin|Quarterly|Studies|Proceedings|"
    r"Psychology|Psychologist|Sciences?)$"
)
# `*Buffered* is used at III.4` -- an italicised TERM being discussed, not a work being cited.
TERM_NOT_WORK = re.compile(r"^\s*(is|was|are|were|means?|here|itself|does|has)\b")


def chapters():
    return sorted(p for p in BOOK.glob("*.md") if CHAPTER.match(p.name))


def is_internal(tok):
    m = re.match(r"^([IVX]+)[.,]\s?(\d+)$", tok)
    return bool(m and m.group(1) in BOOKS and int(m.group(2)) <= BOOKS[m.group(1)])


def main():
    full = "--full" in sys.argv
    files = chapters()
    editions, loci, works, exposed = [], [], collections.Counter(), []

    for p in files:
        lines = p.read_text(encoding="utf-8", errors="replace").splitlines()
        for i, ln in enumerate(lines, 1):
            for m in list(EDITION_SIGLA.finditer(ln)) + list(EDITION_PHRASE.finditer(ln)):
                editions.append((p.name, i, m.group(0).strip(), ln.strip()))
            for m in LOCUS_NUM.finditer(ln):
                if not is_internal(m.group(0)):
                    loci.append((p.name, i, m.group(0), ln.strip()))
            for m in LOCUS_WORD.finditer(ln):
                if re.search(r"\d|[IVXLC]{1,6}$", m.group(0)) or re.match(r"\s*\d", ln[m.end():m.end() + 4]):
                    loci.append((p.name, i, m.group(0).strip(), ln.strip()))
            for m in TITLE.finditer(ln):
                t = m.group(1).strip()
                if t.endswith((".", ",")) or len(t.split()) > 9:
                    continue
                works[t] += 1
                tail = ln[m.end():]
                if JOURNALISH.search(t) or TERM_NOT_WORK.match(tail):
                    continue
                # SENTENCE-scoped, not 70-char-scoped. `The *Brahma Sūtra* takes the second horn
                # in four words — *lokavat tu līlākaivalyam*, II.1.33` puts 58 characters and a
                # second italic between the title and its locus; the first version of this pass
                # missed it, and knew it only because pass 2 caught the same line independently.
                # NB: the internal-pointer filter is deliberately NOT applied here. A locus
                # standing after a named external work is external by construction, and
                # `Confessions VI.3` / `Adversus haereses II, 7` / `De Rerum Natura III, 832`
                # all look exactly like this book's own chapter pointers. Applying it dropped
                # four of the five real hits and left a result that looked cleaner.
                sentence = re.split(r"(?<=[.!?])\s+(?=[A-Z(])", tail)[0]
                hit = TITLE_LOCUS.search(sentence)
                if hit:
                    exposed.append((t, p.name, i, sentence.strip()[:78]))

    print(f"EDITION / SCHEME SWEEP — {len(files)} drafted chapters, {ROOT.name}\n")
    print(f"pass 1  EDITION-NAMINGS : {len(editions)}")
    if full:
        for f, i, g, ln in editions:
            print(f"          {f}:{i}  [{g}]")
    print(f"pass 2  EXTERNAL LOCI   : {len(loci)}   (internal chapter pointers excluded)")
    if full:
        for f, i, g, ln in loci:
            print(f"          {f}:{i}  [{g}]  {ln[:110]}")

    print(f"\npass 3  EXPOSED PAIRS   : {len(exposed)}   <- a named work AND a classical/scriptural locus")
    for t, f, i, tail in sorted(exposed):
        print(f"          {f}:{i:<5d} {t}  ->  {tail[:78]}")

    n_titles = len(works)
    print(f"\nCOVERAGE BOUND: {len(exposed)} exposed / {n_titles} distinct cited works "
          f"({100.0 * len(exposed) / max(n_titles, 1):.1f}%).")
    print("  ⚠ LIMIT — this sweep can only inspect a citation that EXISTS. Books II–V carry no")
    print("    endnotes; they name sources without loci, so their edition-sensitive material is")
    print("    INVISIBLE HERE, not clean. A low number above is a statement about the apparatus,")
    print("    NOT about the citations. RE-RUN INSIDE R-2, after each book's notes are written.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
