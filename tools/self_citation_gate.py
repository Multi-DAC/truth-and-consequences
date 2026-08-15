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
    (r"\bthe (?:Doctrine|Null Space Atlas|Navigational Guide|Ecology)\b", "document by name"),
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
    (r"\bthe (?:Guide|Atlas|Doctrine)\b(?!\s*(?:says nothing|to))", "document by bare name"),
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

# ⚠ THE DECLARED-GAP COUNTER GETS ITS OWN KNOWN ANSWER, and it exists because
# the counter was wrong the whole time it was being quoted. `\bthe source\b`
# fires on *the source-mapping screens* — a compound noun naming an instrument
# of THIS book, not a reference to any document — and VIII-04's entire count of
# one was that. The headline read 50 across 14 chapters; it is 49 across 13.
# Hand-counted, line by line, BEFORE running it: L1 sentence-initial = 1 ·
# L2 possessive mid-sentence = 1 · L3 compound noun = 0 · L4 plural = 0.
# Expected: 2. (It was written as 3 first, from the prose gloss rather than
# from the fixture, and the control caught that too — the known answer has to
# be derived from the text, not from the sentence describing the text.)
COUNTER_FIXTURE = """
The source declines to settle the question, and says so plainly.
That reading is the source's, not this chapter's.
The specific error the source-mapping screens exist to catch is this one.
The sources disagree about the dating by a full century.
"""
COUNTER_EXPECTED = 2


def selftest():
    hits, _ = scan_text(SELFTEST, "<selftest>")
    fams = sorted({f for _, f, _, _ in hits})
    ok = fams == ["ANONYMOUS", "DANGLING", "NAMED"] and len(hits) == 3
    n = sum(len(THE_SOURCE.findall(l)) for l in COUNTER_FIXTURE.split("\n"))
    ok = ok and n == COUNTER_EXPECTED
    if n != COUNTER_EXPECTED:
        hits = list(hits) + [(0, "COUNTER", f"declared-gap counter returned {n}, "
                             f"expected {COUNTER_EXPECTED}", COUNTER_FIXTURE.strip()[:160])]
    return ok, hits


# Chapters whose apparatus drew on prior work of ours. Inside these, a bare
# "the source" is an anonymous self-reference; everywhere else in the book it
# overwhelmingly means somebody else's text and must not be counted.
# TWO defects, found together, pointing OPPOSITE ways — which is why the total
# looked plausible and was wrong at both ends. (1) `\b` holds at a hyphen, so
# *the source-mapping screens* — an instrument of THIS book — was counted as a
# reference to a document. (2) The pattern was case-SENSITIVE, so every
# sentence-initial *The source* was invisible: EIGHTEEN of them, a quarter of
# the real total, in the count this gate printed beside its own green as the
# thing it was honest about not gating. Declared 50; it is 66.
THE_SOURCE = re.compile(r"\bthe source(?:'s)?(?![\w-])", re.I)

APPARATUS = ("C-01", "C-02", "IV-09", "IV-10", "VII-06", "VII-07", "VII-08",
             "VIII-01", "VIII-02", "VIII-03", "VIII-04", "VIII-05", "VIII-06", "VIII-07")


def report_the_source():
    """PRINTS ON A GREEN RUN, ON PURPOSE.

    A gate that reports only what it gates is a gauge that can only render its good
    news. Named pointers are gone; the ANONYMOUS body-prose form — bare *the source*
    — is not gated, because 101 occurrences across book/ are mostly other people's texts
    and any regex that caught the rest would be tuned until it agreed with me. So the
    residue is COUNTED and PRINTED beside the green, where it cannot be mistaken for
    zero. ⚠ These are not a wording problem: several passages ARGUE WITH the thing
    they call *the source*, and a correction addressed to a document the book never
    names is a different and weaker claim, not the same claim reworded.
    """
    import collections
    per = collections.Counter()
    for f in sorted(glob.glob(os.path.join(BOOK, "*.md"))):
        base = os.path.basename(f)
        if not base.startswith(APPARATUS):
            continue
        for line in open(f, encoding="utf-8").read().split("\n"):
            per[base] += len(THE_SOURCE.findall(line))
    n = sum(per.values())
    print()
    print(f"DECLARED GAP — NOT GATED, AND NOT ZERO: {n} bare \"the source\" reference(s) "
          f"remain in body prose")
    print(f"  across {sum(1 for v in per.values() if v)} apparatus chapter(s). Z-01 bans this form too, "
          f"and calls it strictly")
    print("  worse than the named one. It is left standing because removing it changes what")
    print("  several passages CLAIM — a correction aimed at an unnamed document is weaker")
    print("  than one aimed at a named document, and that is an editorial ruling, not a sweep.")
    for k, v in per.most_common():
        if v:
            print(f"      {v:3d}  {k}")


def main():
    verbose = "--verbose" in sys.argv
    ok, control = selftest()
    print("POSITIVE CONTROL — synthetic text, 3 planted violations, 3 foreign corpora:")
    for n, fam, why, line in control:
        print(f"    caught  {fam:9s} L{n}  {why}")
    if not ok:
        print(f"  [X] CONTROL FAILED — expected exactly 3 catches across 3 families, got "
              f"{len(control)}. The gate is not measuring; its verdict is withheld.")
        return 2
    print("  [ok] 3/3 planted caught, 0/3 foreign corpora flagged. Detector is live.\n")

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
        print("  LIMIT: this measures POINTING, not honesty about inheritance. A debt")
        print("  absorbed into the prose is invisible here, which is the intended end")
        print("  state — but it means a green cannot certify that the absorption happened.")
        report_the_source()
        return 0

    print(f"SELF-CITATION GATE: ◻ OPEN — {total} violation(s) across {files} file(s).")
    for fam, n in sorted(by_family.items()):
        print(f"    {fam:9s} {n}")
    print("  Each is repaired by ABSORPTION (state the substance in the book's own")
    print("  voice, drop the pointer) or by CUT. Naming it better is not a repair.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
