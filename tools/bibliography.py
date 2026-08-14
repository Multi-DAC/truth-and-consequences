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
DOUBTFUL = re.compile(
    r"(?:'s translation)|(?:reprinted in)"        # a fragment of the note's prose
    r"|(?:, onset)|(?:^The \w+ books)"
    r"|(?:\btranslated by\b.*\bin\b)",            # two works merged into one match
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


def render(entries, blocks_with_year, blocks_yielding) -> str:
    gap = blocks_with_year - blocks_yielding
    pct = (100.0 * blocks_yielding / blocks_with_year) if blocks_with_year else 0.0
    lines = [
        "# BACK MATTER",
        "",
        "## WORKS CITED",
        "",
        "*Generated from the endnotes by `tools/bibliography.py`. Do not hand-edit this page — "
        "re-run the tool. A bibliography typed once is a stamp; it rots at exactly the rate the "
        "notes are repaired and does not change appearance while it rots, which is the object this "
        "book spends a volume diagnosing. The back matter is not exempt from the argument.*",
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
        "appearance and hide a real limit of the instrument. ⛔ **And a miss the instrument cannot "
        "flag without becoming noise: a one-word title and a bare surname are the same shape.** "
        "Flagging every single-word entry caught two real cases and raised fifteen false alarms "
        "against titles like *Aion*, *Angst*, *Ethics* and *Nature*, so the rule was removed and "
        "the residual is declared here instead. Assume one or two entries below are an author "
        "standing where a title goes."
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
