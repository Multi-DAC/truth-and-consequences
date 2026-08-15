#!/usr/bin/env python3
"""
SELF-CITATION GATE — Truth and Consequences, Day 195. Clayton's release condition, given a grep.

WHY THIS EXISTS, AND IT IS THE WORST PROVENANCE ANY TOOL IN THIS TREE HAS.

The standard is Clayton's and it is old: **the volume stands on its own.** Past work of ours may
be USED — its arguments, its taxonomy, its sentences — but never NAMED and never POINTED AT. If
it is worth invoking it is written in here, in full. `Z-01 §THE BAN LIST` already legislates it,
in almost those words, and had done so before this file existed.

And on Day 195 the project spent an afternoon moving the book in the *opposite* direction. Queue
row **R-214** said the source was "never named"; it was paid by NAMING it — a full bibliographic
entry at `C.1 §V`, the DOI, the four document titles, and forty-two endnote pointers left standing
and now legible. Every step of that was careful, sourced, and self-critical. It was also a direct
violation of a rule written down in this same book, and nothing objected, because the rule lived
in a glossary and the row lived in front of me.

**That is the whole reason this file exists rather than a paragraph of policy.** A standard with
no instrument loses to any queue row that contradicts it, every time, on the day the row is
worked. The row is concrete and present; the standard is prose in another file. Give the standard
a gauge and the asymmetry reverses.

WHAT IT CHECKS — three families, and they are of different strengths. Do not read them as one.

  NAMED       an explicit pointer to one of our prior works: the short titles the endnotes use
              (`Perspective` + Doctrine / Guide / Atlas / Ecology / numbered document), the full
              title, the DOI, or the standalone capital-C `Corpus` used as a proper noun for it.
              ⚠ THE FIRST DRAFT OF THIS RULE WAS WRONG AND THE FIRST RUN SAID SO. `Corpus` is an
              ordinary Latin word for a body of texts, and a book with an ancestors file uses it
              that way: `Corpus Hermeticum` (II.6), `Corpus Dionysiacum` (V.1), `Corpus Christi`
              (V.2) are three OTHER PEOPLE'S corpora and three false positives. They are excluded
              by the following word, not by a line number, so the exclusion keeps working when
              the lines move.

  ANONYMOUS   the unnamed self-reference — *as we argued elsewhere*, *in our earlier work*, *we
              have shown*, *our previous volume*. Z-01 calls this **strictly worse** than the
              named form and it is right: it points a reader at something they cannot look up.
              Weakest family and the most prone to false hits, since "we have shown" is also how
              a book refers to ITSELF. Reported separately, never merged into the headline.

  DANGLING    a live cross-reference to a passage this gate's own repairs deleted — e.g. "cited
              in full at `C.1` §V" after `C.1 §V`'s entry is gone. This family is here because a
              de-citation sweep MANUFACTURES it: the repair is what breaks these, so the tool
              that drives the repair has to be the one that sees them.

THE EXCLUSION, AND WHY IT IS NARROW. `Z-01 §THE BAN LIST` must QUOTE the banned forms in order to
ban them, and `C-02` may describe the rule. An exclusion honoured in one pass and not another is a
defect this project has already paid for, so there is exactly ONE exclusion mechanism here — the
`<!-- self-citation-gate: quoting-the-ban -->` marker — it applies to every family, and every
suppression it performs is PRINTED. A suppression you cannot see is a gate lying quietly.

POSITIVE CONTROL. `--selftest` runs the detector over synthetic text containing one instance of
each family plus all three historical corpora. It must return 3 hits and 3 clean. A zero from this
gate means nothing unless the selftest passes in the same run, so `main()` runs it EVERY time and
refuses to print a verdict if it fails. The failure this guards against is not subtle and it is
the one that actually happens: a regex edited until the book looks clean.

WHAT IT CANNOT DO. It cannot see an ABSORBED debt, which is the point — absorption is the desired
end state and is invisible by construction. So a green here does NOT mean the book is honest about
what it inherited; it means the book no longer points. Those are different claims and only the
second one is measured.

  usage:  python tools/self_citation_gate.py [--verbose] [--selftest]
  exit:   0 = clean, 1 = violations, 2 = the gate's own control failed
"""

import re
import sys
import glob
import os

BOOK = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "book")

MARKER = "self-citation-gate: quoting-the-ban"

# Other people's corpora. Excluded by the word that FOLLOWS "Corpus", so the
# exclusion survives every renumber and reflow. Extend by adding a word, never
# by adding a line number.
FOREIGN_CORPORA = {"hermeticum", "dionysiacum", "christi", "iuris", "callosum"}

NAMED = [
    (r"`Perspective`", "short-title tag used by the endnotes"),
    (r"\bThe Corpus of Perspectival Idealism\b", "full title"),
    (r"\bCorpus of Perspectival\b", "full title, partial"),
    (r"10\.5281/zenodo\.\d+", "the deposit DOI"),
    (r"\*\*(?:Doctrine|Guide|Atlas|Ecology)\s*(?:§|#|\d)", "document + section pointer"),
    (r"\b[Tt]he (?:Doctrine|Null Space Atlas|Navigational Guide|Ecology)\b", "document by name"),
    (r"\bCorpus-Perspectival\b", "the drafting tree"),
    (r"\bUnreleased-Work/Perspective\b", "the drafting tree"),
    # Added AFTER the first repair pass, on finding two forms the first draft of
    # this list could not see: the backticked document numbers the apparatus also
    # used (`03`, `05`, `06`), and the bare capitalised document name without the
    # `Perspective` tag in front of it. Both are pointers. ⚠ Widening a detector
    # after a clean-up is only legitimate in this direction — it can add findings,
    # never remove one — and the count it produced is reported rather than folded
    # into the original total.
    (r"`0[1-9]`\s*§", "backticked document number + section"),
    # ⚠ SENTENCE-INITIAL WAS INVISIBLE. These two entries were written lowercase-only
    # and `scan_text` matches NAMED case-SENSITIVELY, so `The Guide's own statement of
    # what a being is` — an explicit pointer opening a section of VIII.1 — did not
    # register, on every run this gate has ever made. It is the SAME defect the
    # declared-gap counter had already been caught with and repaired for, one screen
    # further down this file, and the repair was not carried up here.
    # [[feedback_repair_scoped_to_named_cause]]
    # The determiner is widened, NOT the document name: `the atlas` lowercase is this
    # book's own Book IV and must never match. Measured at the time of the fix:
    # 0 occurrences of any capitalised form remain, so this adds no findings today —
    # it closes the hole for the next reflow.
    (r"\b[Tt]he (?:Guide|Atlas|Doctrine)\b(?!\s*(?:says nothing|to))", "document by bare name"),
]

ANONYMOUS = [
    r"\bas we (?:argued|showed|said|established) elsewhere\b",
    r"\bin our (?:earlier|previous|prior) (?:work|volume|book|document)\b",
    r"\bour (?:earlier|previous|prior) (?:work|volume|book)\b",
    r"\belsewhere we (?:have )?(?:argued|shown|established)\b",
    r"\bthe (?:earlier|previous|companion) volume\b",
]

DANGLING = [
    (r"(?:cited |citation )?(?:in full )?at `C\.1` §V", "points at C.1 §V's source entry"),
    (r"full citation at `C\.1` §V", "points at C.1 §V's source entry"),
]


def corpus_is_ours(line, idx):
    """`Corpus` at position idx — ours, or somebody else's body of texts?"""
    tail = line[idx + len("Corpus"):].lstrip()
    nxt = re.match(r"[A-Za-z]+", tail)
    if nxt and nxt.group().lower() in FOREIGN_CORPORA:
        return False
    return True


def scan_text(text, name="<text>"):
    """Returns (hits, suppressed). A hit is (line_no, family, why, line)."""
    hits, suppressed = [], []
    # The marker heads a PARAGRAPH and covers it to the next blank line, rather
    # than sitting inline on each offending line. Two reasons, and the second is
    # the load-bearing one: an inline HTML comment inside a sentence is a
    # rendering hazard in the PDF path, and a per-line marker has to be re-applied
    # every time the prose reflows — which is how an exclusion ends up honoured in
    # one pass and not the next.
    paragraph_excluded = False
    in_apparatus = os.path.basename(name).startswith(APPARATUS)
    for n, line in enumerate(text.split("\n"), 1):
        if not line.strip():
            paragraph_excluded = False
        if MARKER in line:
            paragraph_excluded = True
        excluded = paragraph_excluded
        found = []
        for pat, why in NAMED:
            if re.search(pat, line):
                found.append(("NAMED", why))
        for m in re.finditer(r"\bCorpus\b", line):
            if corpus_is_ours(line, m.start()):
                found.append(("NAMED", "bare `Corpus` as a proper noun for our volume"))
                break
        for pat in ANONYMOUS:
            if re.search(pat, line, re.I):
                found.append(("ANONYMOUS", "unnamed self-reference"))
        for pat, why in DANGLING:
            if re.search(pat, line):
                found.append(("DANGLING", why))
        # RESIDUE — the bare anonymous reference. Two patterns of DIFFERENT scope,
        # because they have different ambiguity: `our source` is unambiguous anywhere
        # in the book, while a bare `the source` means somebody ELSE'S text in most of
        # it (Enoch, the Tibetan material, Mariotte) and only means us inside the
        # chapters whose apparatus was quarried from prior work of ours.
        if SELF_SOURCE_ANY.search(line):
            found.append(("RESIDUE", "anonymous self-reference: `our source`"))
        if in_apparatus and SELF_SOURCE_SCOPED.search(line):
            found.append(("RESIDUE", "anonymous self-reference: bare `the source`, "
                                     "inside an apparatus chapter"))
        # ⚠ THE UNIT IS A LINE THAT POINTS, NOT A REGEX MATCH, and the positive
        # control is what established that. Two DANGLING patterns describing the
        # same pointer made one sentence read as two violations; the first
        # selftest run returned 5 for 3 planted and refused to give a verdict.
        # Collapse per (line, family), keeping every reason, so the headline
        # number is a count of PLACES TO REPAIR — which is the only number a
        # human can act on or check by hand.
        for fam in dict.fromkeys(f for f, _ in found):
            why = "; ".join(dict.fromkeys(w for f, w in found if f == fam))
            rec = (n, fam, why, line.strip()[:160])
            (suppressed if excluded else hits).append(rec)
    return hits, suppressed


SELFTEST = """
The book cites `Perspective` **Guide §4.1** for the eight classes.
As we argued elsewhere, the ground is not addressable.
IV.9 gives the full citation at `C.1` §V and leaves it there.
Ficino's dating of the Corpus Hermeticum was wrong by twelve centuries.
The Corpus Dionysiacum is late fifth century at the earliest.
The office for Corpus Christi was commissioned by Urban IV in 1264.
"""

# ⚠ THE RESIDUE DETECTOR GETS ITS OWN KNOWN ANSWER, and it has now been wrong
# THREE times while being quoted as "the part this gate is honest about not
# gating" — which is the most dangerous thing a number can be, because it is read
# as a measured concession rather than as a claim anybody has to stand behind.
#   (1) `\b` holds at a hyphen, so *the source-mapping screens* — a compound noun
#       naming an instrument of THIS book — counted as a reference to a document.
#   (2) The pattern was case-SENSITIVE, so every sentence-initial *The source* was
#       invisible: eighteen of them, a quarter of the real total.
#   (3) And the form it could not see at all: *our source* / *our own source*.
#       Same reference, different determiner, and it is the one form unambiguous
#       enough to gate BOOK-WIDE. Twelve were standing while the counter reported
#       the gap as fully described — two of them in section HEADINGS, which is to
#       say in the table of contents. [[feedback_gauge_can_only_render_its_good_news]]
#
# So it stops being a counter and becomes a family. Hand-counted from the fixture
# BEFORE running it, line by line:
#   L1 sentence-initial `The source`          = 1
#   L2 possessive mid-sentence `the source's` = 1
#   L3 `Our own source`                       = 1
#   L4 `our source's`                         = 1
#   L5 compound noun `the source-mapping`     = 0
#   L6 plural `The sources`                   = 0
#   L7 `any source`                           = 0
#   L8 `a source's`                           = 0
# Expected inside an apparatus chapter: 4.
RESIDUE_FIXTURE = """
The source declines to settle the question, and says so plainly.
That reading is the source's, not this chapter's.
Our own source reaches the same conclusion four subsections later.
The fault is named first in our source's census card.
The specific error the source-mapping screens exist to catch is this one.
The sources disagree about the dating by a full century.
No journal, no volume, no DOI, in any source reachable from here.
The conclusion is the chapter's, not a source's.
"""
RESIDUE_EXPECTED_APPARATUS = 4
# ⚠ AND THE SCOPE GETS A CONTROL OF ITS OWN, built where the two answers DIFFER.
# The same fixture read as a non-apparatus chapter must return 2 — the two `our
# source` lines, gated everywhere — and must NOT return the two bare `the source`
# lines, which outside these chapters mean somebody else's text. If the expected
# numbers were equal, a scope that had quietly stopped applying would pass this
# control unchanged. [[feedback_guard_checked_where_both_answers_agree]]
RESIDUE_EXPECTED_ELSEWHERE = 2


def selftest():
    hits, _ = scan_text(SELFTEST, "<selftest>")
    fams = sorted({f for _, f, _, _ in hits})
    ok = fams == ["ANONYMOUS", "DANGLING", "NAMED"] and len(hits) == 3

    inside, _ = scan_text(RESIDUE_FIXTURE, "IV-10-residue-fixture.md")
    outside, _ = scan_text(RESIDUE_FIXTURE, "II-01-residue-fixture.md")
    n_in = sum(1 for _, f, _, _ in inside if f == "RESIDUE")
    n_out = sum(1 for _, f, _, _ in outside if f == "RESIDUE")
    if n_in != RESIDUE_EXPECTED_APPARATUS:
        ok = False
        hits = list(hits) + [(0, "CONTROL", f"residue detector returned {n_in} inside an "
                              f"apparatus chapter, expected {RESIDUE_EXPECTED_APPARATUS}", "")]
    if n_out != RESIDUE_EXPECTED_ELSEWHERE:
        ok = False
        hits = list(hits) + [(0, "CONTROL", f"residue SCOPE returned {n_out} outside the "
                              f"apparatus, expected {RESIDUE_EXPECTED_ELSEWHERE}", "")]
    return ok, hits, (n_in, n_out)


# Chapters whose apparatus drew on prior work of ours. Inside these, a bare
# "the source" is an anonymous self-reference; everywhere else in the book it
# overwhelmingly means somebody else's text and must not be counted.
# ⚠ THIS TUPLE IS THE WEAKEST PART OF THE GATE, AND IT IS NAMED HERE RATHER THAN
# LEFT TO BE DISCOVERED: it is a hand-drawn scope. A chapter that begins quarrying
# prior work tomorrow falls outside it silently, and nothing in this file notices.
# That is exactly why the `our source` family below is UNSCOPED — it is the form
# that needs no judgment about which chapter it is standing in.
# [[feedback_denylist_encodes_the_corpus_as_it_was]]
APPARATUS = ("C-01", "C-02", "IV-09", "IV-10", "VII-06", "VII-07", "VII-08",
             "VIII-01", "VIII-02", "VIII-03", "VIII-04", "VIII-05", "VIII-06", "VIII-07")

# Gated book-wide: `our source`, `our own source`, `our source's`. There is no
# reading of this phrase in which the possessor is somebody else.
SELF_SOURCE_ANY = re.compile(r"\bour (?:own )?sources?(?:'s|')?(?![\w-])", re.I)
# Gated inside APPARATUS only: the bare definite form. Case-insensitive and
# hyphen-guarded, both of which were repairs. Elsewhere in the book this phrase
# overwhelmingly means Enoch, the Tibetan material or Mariotte.
SELF_SOURCE_SCOPED = re.compile(r"\bthe source(?:'s)?(?![\w-])", re.I)


def report_scope():
    """PRINTS ON A GREEN RUN, ON PURPOSE.

    A gate that reports only what it gates is a gauge that can only render its good
    news. The RESIDUE family is now GATED rather than counted, so this no longer
    prints a number it declines to act on — it prints the two things a green here
    still cannot cover, both of which are real.
    """
    print()
    print("WHAT THE GREEN DOES NOT COVER — two limits, stated because a clean run is")
    print("  otherwise read as a stronger claim than it is:")
    print(f"  1. SCOPE. The bare `the source` family is gated inside {len(APPARATUS)} named apparatus")
    print("     chapters only, because everywhere else the phrase means somebody else's")
    print("     text. The list is hand-drawn. A NEW chapter that quarries prior work is")
    print("     outside it silently. (`our source` is gated book-wide and needs no list.)")
    print("  2. ABSORPTION. This measures POINTING, not honesty about inheritance. A debt")
    print("     absorbed into the prose is invisible here by construction — that is the")
    print("     intended end state, and it means a green cannot certify the absorption")
    print("     happened, only that nothing points.")


def main():
    verbose = "--verbose" in sys.argv
    ok, control, residue = selftest()
    print("POSITIVE CONTROL — synthetic text, 3 planted violations, 3 foreign corpora:")
    for n, fam, why, line in control:
        print(f"    caught  {fam:9s} L{n}  {why}")
    if not ok:
        print(f"  [X] CONTROL FAILED — expected exactly 3 catches across 3 families, got "
              f"{len(control)}. The gate is not measuring; its verdict is withheld.")
        return 2
    print("  [ok] 3/3 planted caught, 0/3 foreign corpora flagged.")
    print(f"  [ok] residue control: {residue[0]}/{RESIDUE_EXPECTED_APPARATUS} caught inside an "
          f"apparatus chapter, {residue[1]}/{RESIDUE_EXPECTED_ELSEWHERE} outside it — the two "
          f"numbers differ, so the scope is doing work rather than passing by agreement.")
    print("  Detector is live.\n")

    if "--selftest" in sys.argv:
        return 0

    total, files, all_sup = 0, 0, 0
    by_family = {}
    for f in sorted(glob.glob(os.path.join(BOOK, "*.md"))):
        text = open(f, encoding="utf-8").read()
        hits, sup = scan_text(text, f)
        all_sup += len(sup)
        if sup and verbose:
            for n, fam, why, line in sup:
                print(f"  suppressed  {os.path.basename(f)}:{n}  {fam}  ({why}) "
                      f"— carries the ban marker")
        if not hits:
            continue
        files += 1
        total += len(hits)
        print(f"  {os.path.basename(f)}  — {len(hits)} violation(s)")
        for n, fam, why, line in hits:
            by_family[fam] = by_family.get(fam, 0) + 1
            print(f"      L{n:<5d} [{fam}] {why}")
            if verbose:
                print(f"              {line}")

    print()
    if total == 0:
        print("SELF-CITATION GATE: ✅ CLEAN — 0 named or anonymous pointers to prior work "
              "of ours, across all book files.")
        print(f"  ({all_sup} suppression(s), all carrying the explicit ban marker.)")
        report_scope()
        return 0

    print(f"SELF-CITATION GATE: ◻ OPEN — {total} violation(s) across {files} file(s).")
    for fam, n in sorted(by_family.items()):
        print(f"    {fam:9s} {n}")
    print("  Each is repaired by ABSORPTION (state the substance in the book's own")
    print("  voice, drop the pointer) or by CUT. Naming it better is not a repair.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
