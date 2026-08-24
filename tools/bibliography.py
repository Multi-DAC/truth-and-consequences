#!/usr/bin/env python3
"""Generate the works-cited list from the endnotes, and PRINT ITS OWN RECALL GAP.

WHY THIS IS A TOOL AND NOT A HAND-KEPT PAGE.  A bibliography typed once is a
stamp: it is accurate on the day it is typed and it rots at exactly the rate
the notes are repaired, without changing appearance.  This book spends a
volume arguing that a gauge which fails on its own beats a mark that
remembers, and its own back matter is not exempt.  Re-run this and the page
is current; do not hand-edit `book/Z-02-works-cited.md`.

⛔ THE LIMIT, PRINTED INTO THE ARTIFACT ITSELF RATHER THAN LEFT IN THIS
DOCSTRING.  The extractor is deliberately STRICT: it takes only what it can
parse with confidence, and it COUNTS the note blocks that plainly carry a
citation (a four-digit year) and yielded nothing.  That count is the recall
gap, and it goes on the page.  A works-cited list that silently dropped a
third of its sources would be the exact object this book exists to diagnose --
a partial result wearing the authority of a complete one.

usage:  python tools/bibliography.py [--check]
        --check  exits 1 if the generated page differs from the one on disk
"""
from __future__ import annotations

import collections
import os
import re
import sys
import glob
import unicodedata

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
BOOK = os.path.join(ROOT, "book")
OUT = os.path.join(BOOK, "Z-02-works-cited.md")

NOTE_BLOCK = re.compile(r"^\[\^[^\]]+\]:(.*?)(?=^\[\^|\Z)", re.S | re.M)
YEAR = re.compile(r"\b(1[4-9]\d\d|20[0-2]\d)\b")

# A citation, strictly: an italicised title, optionally preceded by an author
# phrase, followed within a short window by a parenthetical carrying a year.
# Anything that does not match this shape is NOT guessed at -- it is counted.
CITE = re.compile(
    r"(?P<author>(?:[A-ZÉÖÜÅ][\w.'’\-]+(?:,? (?:and |& )?)?){1,4}(?:[A-ZÉÖÜÅ][\w.'’\-]+)?)?"
    r"\s*\*(?P<title>[^*\n]{4,110}?)\*"
    r"[^.(\n]{0,60}?"
    r"\((?P<imprint>[^()]{0,110}?(?P<year>1[4-9]\d\d|20[0-2]\d)[^()]{0,20}?)\)"
)

# Fragments that mean the italics were emphasis, not a title.
NOT_A_TITLE = re.compile(
    r"[.;:!?]\s|\bthe\b.*\bis\b|^\W|\b(?:and|but|because|which|that|this|it|we|our|its)\b",
    re.I,
)
SENTENCEY = re.compile(r"\b(?:is|are|was|were|does|do|has|have|not|never|would|should)\b", re.I)


def tidy(s: str) -> str:
    s = unicodedata.normalize("NFC", " ".join(s.split()))
    return s.strip(" ,;:—-")


# A locus is not a title. These are the shapes that survived the first pass and
# were caught by reading the generated page rather than by the filter -- kept as
# named cases so a later reader can see what the strictness is actually for.
LOCUS = re.compile(r"^(?:Gate|Book|Chapter|Chap\.|Part|Vol\.?|Volume|Canto|Lecture)\b", re.I)
TRUNCATED = re.compile(r"[,;]\s*[\"“”']?$|^[\"“”']?\s*[a-z]")

# ⚠ NOT a rejection list — a DOUBT list. These shapes pass every structural test
# and are still, on inspection, an author's surname standing where a title goes,
# or a piece of the note's running prose that happened to be italicised beside a
# year. Dropping them silently would improve this page's appearance and conceal a
# real limit of the instrument, so they are MARKED instead.
# [[feedback_partial_delivery_beats_no_gauge]]
# ⛔ THE SINGLE-WORD RULE WAS TRIED AND REMOVED, AND THE REASON IS THE POINT.
# Flagging every one-word title caught the two real author-as-title cases and
# ALSO flagged Aion, Angst, Ethics, Counterfactuals, Inquiry, Elite, Nature,
# Science, Neuron, Noûs and PNAS -- 15 false alarms against 2 catches. A flag
# that is wrong seven times out of nine is not a conservative gauge, it is
# noise, and a reader learns within a page to skip it. The discrimination is
# not mechanically available here, so the miss is DECLARED on the page instead
# of being papered over with an alarm nobody will read.
# [[feedback_filter_precision_eats_recall]] · [[feedback_true_signal_inside_the_noise_band]]
# ⚠ DAY 205: THE DECLARED BLIND SPOT HAD MOVED AND THE DECLARATION HAD NOT.
# Every pattern above this line was written against a specimen that existed on the
# day it was written. The residual the page declares — "a one-word title and a bare
# surname are the same shape" — describes a rule that was REMOVED, and the page has
# been standing behind it since. Regenerating today introduces
# `"January 10, 2013, a review of Koch's" (Cambridge, MA: MIT Press, 2012)`: NINE
# words, so the declared limit does not cover it, and none of the instance patterns
# above reach it either. It would have shipped unflagged, on a page whose header is
# this book's best statement of exactly that mechanism.
# So the additions below name SHAPES rather than specimens — the three ways a span
# announces it is a piece of the note's prose and not a title:
#   · it opens with a date (a title almost never does; a note's citation often does)
#   · it ends in a possessive (`Koch's` — the title belongs to whatever came next)
#   · it carries a reviewing/quoting connective in mid-prose voice
# ⛔ THE ONE-WORD CASE IS STILL NOT CAUGHT AND IS STILL DECLARED, not because it is
# unimportant but because it was measured: flagging every single-word entry caught
# two real cases against fifteen false alarms (`Aion`, `Angst`, `Ethics`, `Nature`).
# The residual is real; what changed is that the page now declares the residual it
# actually has instead of the one a deleted rule used to leave.
MONTHS = "January|February|March|April|May|June|July|August|September|October|November|December"
DOUBTFUL = re.compile(
    r"(?:'s translation)|(?:reprinted in)"        # a fragment of the note's prose
    r"|(?:, onset)|(?:^The \w+ books)"
    r"|(?:\btranslated by\b.*\bin\b)"             # two works merged into one match
    rf"|(?:^(?:{MONTHS})\b)|(?:^\d{{1,2}}\s+(?:{MONTHS})\b)|(?:^(?:19|20)\d{{2}}\b)"
    r"|(?:['’]s$)"                                # ends on a possessive: the title is elsewhere
    r"|(?:\ba review of\b)|(?:\bquoted in\b)|(?:\bcited in\b)|(?:\bas reported\b)",
    re.I,
)


def plausible_title(t: str) -> bool:
    """Reject emphasis-italics. Errs toward REJECTING, so the gap is visible."""
    if len(t) < 4 or len(t) > 110:
        return False
    if SENTENCEY.search(t):
        return False
    if LOCUS.match(t) or TRUNCATED.search(t):
        return False
    if t.count(",") > 3:
        return False
    if not re.match(r"[A-Z\"“'‘(]", t):
        return False
    # A title is mostly capitalised words or a foreign-language phrase.
    words = [w for w in re.findall(r"[A-Za-zÀ-ÿ']+", t) if len(w) > 2]
    if not words:
        return False
    caps = sum(1 for w in words if w[0].isupper())
    return caps / len(words) >= 0.45


def harvest() -> tuple[dict, int, int]:
    entries: dict[tuple[str, str], set[str]] = {}
    blocks_with_year = 0
    blocks_yielding = 0
    for path in sorted(glob.glob(os.path.join(BOOK, "[IVC]*.md"))):
        chap = os.path.basename(path).split("-")[0:2]
        label = ".".join(chap).replace(".0", ".")
        text = open(path, encoding="utf-8").read()
        for block in NOTE_BLOCK.findall(text):
            flat = " ".join(block.split())
            if not YEAR.search(flat):
                continue
            blocks_with_year += 1
            got = False
            for m in CITE.finditer(flat):
                title = tidy(m.group("title"))
                if not plausible_title(title):
                    continue
                author = tidy(m.group("author") or "")
                if author and (len(author) > 60 or SENTENCEY.search(author)):
                    author = ""
                imprint = tidy(m.group("imprint"))
                entries.setdefault((title, imprint), set()).add(label)
                got = True
            if got:
                blocks_yielding += 1
    return entries, blocks_with_year, blocks_yielding


def collapse_key(title: str) -> str:
    """The title as a reader would recognise it: no subtitle, no case, no punctuation.

    ⚠ DAY 205. The page declared three limits and had a fourth. Six works were printed
    TWICE under variant strings — a subtitle present in one and absent in the other,
    `Pa.` against `PA`, a city present or absent — so `N entries` overstated distinct
    works, and it was the one figure on the page carrying no caveat. Two of them differ
    by nothing an eye would catch, which is why this is a function and not a sentence:
    a hand-written *six* would have been correct on the day it was typed and silently
    wrong at the next repair, which is the failure this page exists to argue about.
    """
    t = title.split(":")[0]
    t = re.sub(r"[^a-z0-9 ]", "", t.casefold()).strip()
    t = re.sub(r"^(?:the|a|an) ", "", t)
    return re.sub(r"\s+", " ", t)


def collapses(entries):
    """(one_work, serials) — titles printed more than once, split by a year heuristic.

    Same title, same year: one work under two strings. Same title, different years: a
    PERIODICAL whose name is standing where a volume's title goes — a different defect,
    declared beside this one rather than folded into it. ⛔ The split is a heuristic and
    misfiles at least one known case (a book and a 1993 review of it share a title), so
    the page states the total as well as the split.
    """
    groups = collections.defaultdict(list)
    for (title, imprint), chaps in entries.items():
        groups[collapse_key(title)].append((title, imprint))
    one_work, serials = [], []
    for key, rows in groups.items():
        if len(rows) < 2:
            continue
        years = {tuple(re.findall(r"\b(?:1[5-9]|20)\d{2}\b", imp)) for _, imp in rows}
        (serials if len(years) > 1 else one_work).append((key, rows))
    return one_work, serials


def render(entries, blocks_with_year, blocks_yielding) -> str:
    gap = blocks_with_year - blocks_yielding
    one_work, serials = collapses(entries)
    dup_extra = sum(len(rows) - 1 for _, rows in one_work)
    ser_extra = sum(len(rows) - 1 for _, rows in serials)
    pct = (100.0 * blocks_yielding / blocks_with_year) if blocks_with_year else 0.0
    lines = [
        "# BACK MATTER",
        "",
        "## WORKS CITED",
        "",
        # ⛔ DAY 205: THIS BLOCK WAS A PRINTED ITALIC LINE NAMING THIS FILE, AND SOMEBODY
        # FIXED THAT BY HAND ON THE PAGE. Clayton's D205 ruling took every file pointer out
        # of the shipped text; the repair was made in `Z-02-works-cited.md`, which is
        # GENERATED, and the generator was not told. The hand-edit survived ten days only
        # because nothing had re-run this tool since Day 195 — the first regeneration
        # reverted it, and the sweep caught the filename back in the book. A ruling applied
        # to the output of a generator and not to the generator is not a ruling, it is a
        # delay. Ported here, where regeneration carries it instead of destroying it.
        "<!-- MAINTAINER, NOT PRINTED: generated from the endnotes; do not hand-edit this page,",
        "     regenerate it. A bibliography typed once is a stamp; it rots at exactly the rate",
        "     the notes are repaired and does not change appearance while it rots, which is the "
        "object",
        "     this book spends a volume diagnosing. The back matter is not exempt from the "
        "argument. -->",
        "",
        f"⚠ **THIS LIST IS INCOMPLETE, AND HERE IS BY HOW MUCH.** Of **{blocks_with_year}** endnotes "
        f"carrying a datable citation, **{blocks_yielding}** ({pct:.0f}%) are parsed into entries "
        f"below and **{gap}** are not. The extractor is deliberately strict and refuses to guess: a "
        "citation given in running prose, split across a clause, or carried by a locus rather than "
        "an imprint is counted here and not rendered. **The endnote is the receipt; this page is an "
        "index to the receipts, and it says which ones it could not reach.** A works-cited list that "
        "silently dropped that share would be a partial result wearing the authority of a complete "
        "one.",
        "",
        f"⚠ **AND THE ENTRY COUNT OVERSTATES DISTINCT WORKS.** **{len(one_work)}** work"
        f"{'' if len(one_work) == 1 else 's'} below "
        f"{'is' if len(one_work) == 1 else 'are'} printed more than once under variant strings — a "
        f"subtitle carried in one citation and not the other, a city present or absent, `Pa.` "
        f"against `PA` — which is **{dup_extra}** entr"
        f"{'y' if dup_extra == 1 else 'ies'} more than there are works. A further **{ser_extra}** "
        f"{'is' if ser_extra == 1 else 'are'} the same name recurring against different years — "
        "mostly a periodical standing where a volume's title goes, which is the residue named "
        "below and not the same defect. ⛔ **That split is decided on the year alone and it "
        "misfiles at least one pair**, a book and a dated review of it, which the rule cannot tell "
        "from two issues of a journal; the total above the split is the figure to trust. "
        "**This paragraph is generated, not typed**, for the reason the header gives: the "
        "figure was correct on the day it was first written and would have gone quietly wrong at "
        "the next repair. The duplicates are left standing rather than merged, because choosing "
        "which imprint is canonical is an editorial ruling and this page does not make those.",
        "",
        "**Where this page and an endnote disagree, the endnote is right.**",
        "",
        "---",
        "",
    ]
    doubted = 0
    body = []
    for (title, imprint), chaps in sorted(entries.items(), key=lambda kv: kv[0][0].lower()):
        where = ", ".join(sorted(chaps))
        flag = ""
        if DOUBTFUL.search(title):
            doubted += 1
            flag = (" ⚠ *(machine-uncertain: this may be an author or a fragment of the note's "
                    "prose rather than a title — check the endnote)*")
        body.append(f"- *{title}* ({imprint}) — {where}{flag}")
    lines.append(
        f"⚠ **{doubted} of the {len(entries)} entries below are marked machine-uncertain.** The "
        "extractor can see that they are structurally citation-shaped and cannot tell whether the "
        "italicised span is a title, an author's surname, or a piece of the note's own prose. "
        "**They are marked rather than dropped**, because dropping them would improve this page's "
        "appearance and hide a real limit of the instrument. The marks are raised by shape, not by "
        "recognition: a span that opens on a date, ends on a possessive, or carries a reviewing "
        "connective is prose from the note rather than a title, whatever the words are. ⛔ **Two "
        "residues survive that, and both are declared rather than fixed.** First, **a one-word "
        "title and a bare surname are the same shape** — flagging every single-word entry caught "
        "two real cases against fifteen false alarms on titles like *Aion*, *Angst*, *Ethics* and "
        "*Nature*, so that rule was removed and this sentence stands in its place. Second, **a "
        "journal's name and a book's are also the same shape**, and at least one periodical is "
        "standing in the list below where a volume should be. Assume two or three entries are an "
        "author or a journal in a title's position. **A declared residue is the honest form of a "
        "limit; the failure this page is guarding against is a residue that used to be declared "
        "and quietly changed.**"
    )
    lines.append("")
    lines.extend(body)
    lines.append("")
    lines.append(f"*{len(entries)} entries, {doubted} machine-uncertain.*")
    return "\n".join(lines) + "\n"


def main() -> int:
    entries, bwy, by_ = harvest()
    page = render(entries, bwy, by_)
    check = "--check" in sys.argv
    if check:
        cur = open(OUT, encoding="utf-8").read() if os.path.exists(OUT) else ""
        if cur != page:
            print("WORKS CITED IS STALE — re-run: python tools/bibliography.py")
            return 1
        print(f"works cited: current ({len(entries)} entries, {bwy - by_} notes unparsed)")
        return 0
    with open(OUT, "w", encoding="utf-8", newline="\n") as f:
        f.write(page)
    print(f"wrote {OUT}")
    print(f"  entries          : {len(entries)}")
    print(f"  notes with a year: {bwy}")
    print(f"  notes yielding   : {by_}")
    print(f"  RECALL GAP       : {bwy - by_}  <- printed into the page, not hidden here")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
