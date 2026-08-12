#!/usr/bin/env python3
"""
APPARATUS ROT  —  Truth and Consequences, Day 192.  The retrofit's own exhaust, given a gauge.

WHY THIS EXISTS, and the confession is that I found it by accident while auditing something else.

VII.7 [^9] says Plotinus and tzimtzum run to *"eighteen occurrences across V.1, V.3, V.6, V.9 and
V.10."*  The chapter roster is EXACTLY right — those five and no others — which is the signature of
somebody who really did run the count.  At the commit the note was written against, the total was
17.  Today it is 25.  Nothing changed in VII.7.  V.1 gained seven Plotinus mentions and V.3 gained
one, and the note went quietly false while sitting inside the mechanism this book uses to be right.

That is the whole defect class:

    THE APPARATUS IS THE BOOK'S FRESHNESS MECHANISM AND THE APPARATUS HAS NO GAUGE.

A note is written against a snapshot.  It cites `I.3:46-49`.  It says a term appears `zero times in
V.1`.  Both were measured, both were true, and both are hostages to the next edit of a DIFFERENT
file.  The note does not error.  It does not read wrong.  It reads like scholarship — which is the
one property a silent failure needs, and the fifth time this project has written that sentence.

It matters NOW rather than eventually, because Clayton's sequence is: finish the endnote retrofit,
then carapace, THEN THE ACTUAL REVISION PASS.  The revision pass is the event that moves every line
in the book at once.  Every locator the retrofit is currently writing — and it is writing ten to
fifteen per chapter, one chapter a session — comes due on that day, silently, all together.
The retrofit is manufacturing this defect faster than anything is detecting it.

WHAT IT CHECKS.  Two kinds of claim, of very different strength.  Do not read them as one number.

  LOCATOR   `CH:LINE` or `CH:LINE-LINE` appearing inside a note.
            STRONG when the note also quotes a span near the locator: the quote is searched for in
            the cited chapter (whitespace-normalised, so the book's hard wrapping does not matter)
            and its true start line is compared to the claim.  A quote that is found at the wrong
            line is DRIFTED.  A quote that is not found at all is MISSING — the more serious of
            the two, because it means the span was reworded or deleted, not merely moved.
            WEAK when there is no adjacent quote: all that can be checked is that the chapter
            exists and is long enough to have the line.  Reported separately and never summed
            with the strong rows.

  COUNT     `zero times in CH`, `appears N times`, `N occurrences`, where a term and a scope are
            both recoverable from the sentence.  Re-derived against disk.

LIMIT — read this before quoting the number.  This gauge finds claims by PATTERN, so its
denominator is the claims it can parse, not the claims that exist.  A note that says "a few pages
later" or "the section above" is unmeasurable and is counted in UNPARSED, which is printed on
purpose: an apparatus can rot in prose that names no number at all, and this instrument is blind to
exactly that.  UNPARSED going up is not good news.  It also cannot see a locator that is wrong in a
way the text still satisfies — if two chapters carry near-twin sentences (I.3:60 and I.6:7 do), a
quote search can confirm the wrong one.  Locator rows are evidence, not proof.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

BOOK = Path(__file__).resolve().parent.parent / "book"

CH_RE = re.compile(r"^(?P<book>[IVX]+)-(?P<num>\d+)-")
# A locator: V.6:258  ·  I.3:46-49  ·  I.3:46–49 (en dash)  ·  VII.10:7
LOCATOR_RE = re.compile(r"\b(?P<ch>[IVX]+\.\d+):(?P<a>\d+)(?:\s*[-–—]\s*(?P<b>\d+))?\b")
# A quoted span: *"..."* or "..." or *'...'*  — the book uses all three in notes.
QUOTE_RE = re.compile(r"[*_]*[\"“](?P<q>[^\"”]{12,400})[\"”][*_]*")
NOTE_RE = re.compile(r"^\[\^(?P<n>\d+)\]:", re.M)
# ⛔ Day 192. This gauge audited ONE chapter of sixty from its first run to this fix.
# The loop said `if "## NOTES" not in text: continue` — a literal, case-sensitive
# match. Exactly one chapter in the book writes the heading that way (V.6). Twenty-five
# write `## Notes`; thirty-four carry an apparatus under no heading at all. So every
# number this tool ever printed — "10 locators checked, 0 failing", "UNANCHORED: 4" —
# was V.6's, and was read as the book's. It never once printed a zero, which is why
# nothing caught it: a plausible non-zero result reads as coverage.
NOTES_HEAD_RE = re.compile(r"^#{1,4}[ \t]*(?:NOTES?|ENDNOTES?)[ \t]*$", re.I | re.M)


def notes_block(text: str) -> str | None:
    """The apparatus, however the chapter happens to announce it.

    Falls back to the first note DEFINITION when there is no heading, because
    thirty-four chapters have none. NOTE_RE requires the `[^n]:` colon and a line
    start, so a `[^3]` reference in prose cannot open the block by mistake."""
    head = NOTES_HEAD_RE.search(text)
    if head:
        return text[head.end():]
    first = NOTE_RE.search(text)
    return text[first.start():] if first else None

WORDNUM = {
    "zero": 0, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6,
    "seven": 7, "eight": 8, "nine": 9, "ten": 10, "eleven": 11, "twelve": 12,
    "thirteen": 13, "fourteen": 14, "fifteen": 15, "sixteen": 16, "seventeen": 17,
    "eighteen": 18, "nineteen": 19, "twenty": 20,
}
# "`travel` ... appear ZERO times in V.1"  /  "`summit` appears five times"
COUNT_RE = re.compile(
    r"[`*]+(?P<term>[A-Za-z][A-Za-z '’\-]{1,40}?)[`*]+[^.]{0,80}?"
    r"\b(?:appears?|occurs?|stands?|runs?)\b[^.]{0,40}?"
    r"\b(?P<num>zero|one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|"
    r"thirteen|fourteen|fifteen|sixteen|seventeen|eighteen|nineteen|twenty|\d+)\b"
    r"\s*times?\b(?:[^.]{0,40}?\bin\s+(?P<scope>[IVX]+\.\d+))?",
    re.I,
)


def norm(s: str) -> str:
    """Collapse whitespace AND drop emphasis markers.

    The book hard-wraps, so a quoted span crosses lines — that half was here from
    the start. The other half was not, and it produced six false ⛔ MISSINGs the
    moment this gauge could see more than one chapter: III.6:207 reads
    `**The seed takes an edit the way it took the installation** — by repetition`,
    V.7 [^5] quotes it without the bold, and a raw substring test says the span is
    absent from a chapter that contains it word for word.

    ⛔ This is R-63, and the repair already existed in a sibling tool: endnote_debt's
    scan carries an explicit `[*_]*` for exactly this reason, with a comment naming
    the family. The lesson is not 'strip asterisks' — it is that a known defect class
    fixed in one prose gauge does not propagate to the next one written."""
    return re.sub(r"\s+", " ", re.sub(r"[*_`]", "", s)).strip()


class Chapter:
    """Prose only. The apparatus is deliberately NOT searchable.

    R-175's defect, which this gauge reproduced on its first run: a note quotes the span it is
    ruling on, so searching the whole file finds the quote inside the note itself and certifies
    the note against its own text. The first build of this tool reported a V.6 locator as
    DRIFTED to V.6:470 — a line in V.6's own apparatus. A gauge whose corpus includes the thing
    it is auditing is measuring its own exhaust.
    """

    def __init__(self, path: Path):
        self.path = path
        full = path.read_text(encoding="utf-8")
        self.total_lines = len(full.splitlines())
        # ⛔ Day 192: this line ALSO read `full.split("## NOTES", 1)[0]`. In 59 of the 60
        # chapters that carry an apparatus the literal is absent, so split() returned the
        # whole file and `self.prose` INCLUDED THE NOTES — silently defeating the single
        # guard this class exists to be, as its own docstring above describes. The same
        # wrong literal in two places, the second one disarming the first.
        head = NOTES_HEAD_RE.search(full)
        first = NOTE_RE.search(full)
        cut = head.start() if head else (first.start() if first else len(full))
        self.prose = full[:cut]
        self.lines = self.prose.splitlines()
        # Two indexes. PROSE is what a chapter's own notes are checked against — a note that
        # quotes the span it rules on must not be allowed to certify itself. FULL is what
        # OTHER chapters' notes are checked against, because a note citing IV.8's apparatus is
        # citing an independent artifact, and refusing to resolve it would report a correct
        # cross-reference as MISSING. The hazard is self-reference, not apparatus-reference.
        self.norm, self.idx2line = self._index(self.lines)
        self.norm_full, self.idx2line_full = self._index(full.splitlines())

    @staticmethod
    def _index(lines: list[str]) -> tuple[str, list[int]]:
        buf, idx = [], []
        for lineno, line in enumerate(lines, 1):
            # ⛔ Day 192: this read `re.sub(r"\s+", " ", line).strip()` — norm()'s body,
            # copied. So fixing norm() to drop emphasis markers fixed the NEEDLE and left
            # the HAYSTACK bolded, and every span quoted from a bolded source still read
            # MISSING. Third instance tonight of one shape: the repair lands in one place
            # and the path that matters holds its own copy. Call the function.
            piece = norm(line)
            if not piece:
                continue
            if buf:
                buf.append(" ")
                idx.append(lineno)
            for _ in piece:
                idx.append(lineno)
            buf.append(piece)
        return "".join(buf), idx

    def find_line(self, quote: str, include_notes: bool = False) -> int | None:
        """Line of the quote's first character, or None.

        include_notes=False (a chapter checking itself) searches prose only.
        include_notes=True (another chapter citing this one) searches the whole file.

        Elided quotes are the norm in this apparatus — a note writes
        `"The Fullness is not less for having a vantage in it…"` and the ellipsis is the
        note's, not the book's. Match each fragment in order instead of the literal string;
        without this the gauge reports MISSING on correctly-cited spans, which is the failure
        mode that gets an instrument switched off.
        """
        src = self.norm_full if include_notes else self.norm
        idx = self.idx2line_full if include_notes else self.idx2line
        hay = src.replace("’", "'").replace("‘", "'")
        frags = [norm(f).replace("’", "'").replace("‘", "'")
                 for f in re.split(r"…|\.\.\.", quote)]
        frags = [f for f in frags if len(f) >= 8]
        if not frags:
            return None
        first, cursor = None, 0
        for f in frags:
            i = hay.find(f, cursor)
            if i < 0:
                return None
            if first is None:
                first = i
            cursor = i + len(f)
        return idx[first] if first < len(idx) else None

    def count(self, term: str) -> tuple[int, int]:
        """(whole-word, substring). They differ exactly where a claim is fragile.

        R-183 asserted `travel` appears zero times in V.1. Whole-word: true. Substring: 2 —
        V.1 carries "traveller" and "Travellers", and the second is the term V.1 parts from.
        The finding survives and gets sharper; the EVIDENCE SENTENCE did not survive as written.
        A gauge that reports only one of these numbers hides that.
        """
        esc = re.escape(term)
        word = len(re.findall(rf"\b{esc}\b", self.norm, re.I))
        sub = len(re.findall(esc, self.norm, re.I))
        return word, sub


def load_chapters() -> dict[str, Chapter]:
    out: dict[str, Chapter] = {}
    for p in sorted(BOOK.glob("*.md")):
        m = CH_RE.match(p.name)
        if not m:
            continue
        key = f"{m.group('book')}.{int(m.group('num'))}"
        out[key] = Chapter(p)
    return out


def split_notes(text: str) -> list[tuple[int, str]]:
    """Return [(note_number, body)] for a chapter's apparatus."""
    hits = list(NOTE_RE.finditer(text))
    notes = []
    for i, m in enumerate(hits):
        end = hits[i + 1].start() if i + 1 < len(hits) else len(text)
        notes.append((int(m.group("n")), text[m.end():end]))
    return notes


def audit(chapters: dict[str, Chapter], only: str | None):
    strong, weak, counts, unparsed, unanchored = [], [], [], [], []

    for key, ch in chapters.items():
        if only and key != only:
            continue
        text = ch.path.read_text(encoding="utf-8")
        block = notes_block(text)
        if block is None:
            continue
        for n, body in split_notes(block):
            where = f"{key} [^{n}]"

            locs = list(LOCATOR_RE.finditer(body))
            quotes = list(QUOTE_RE.finditer(body))
            # Assign each quote to its NEAREST locator by character distance, then check a
            # locator only against the quotes that chose it. The first build paired
            # "the quote after, else before", which in a note carrying three locators and
            # three quotes hands I.5's span to I.3's locator and reports three false MISSINGs.
            # ...and a quote further than ADOPT_WINDOW from every locator is UNANCHORED, not
            # adopted by the nearest one. Without the cap, V.6 [^11] — which cites IV.8:498 and
            # then quotes V.6's own line 43 four sentences later with no locator — reported the
            # V.6 span MISSING FROM IV.8. A false positive in a rot gauge is worse than a miss:
            # it is the row that gets the tool switched off.
            ADOPT_WINDOW = 220
            owned: dict[int, list[str]] = {i: [] for i in range(len(locs))}
            for qm in quotes:
                if not locs:
                    break
                qmid = (qm.start() + qm.end()) // 2
                nearest = min(range(len(locs)),
                              key=lambda i: abs(((locs[i].start() + locs[i].end()) // 2) - qmid))
                lmid = (locs[nearest].start() + locs[nearest].end()) // 2
                if abs(lmid - qmid) > ADOPT_WINDOW:
                    unanchored.append((where, norm(qm.group("q"))[:60]))
                    continue
                owned[nearest].append(qm.group("q"))

            for i, lm in enumerate(locs):
                tgt, a = lm.group("ch"), int(lm.group("a"))
                b = int(lm.group("b")) if lm.group("b") else a
                target = chapters.get(tgt)
                if target is None:
                    strong.append((where, tgt, a, "DEAD", "no such chapter"))
                    continue
                cands = owned.get(i) or []
                if not cands:
                    ok = b <= target.total_lines
                    weak.append((where, tgt, a, "OK" if ok else "PAST-EOF",
                                 f"chapter has {target.total_lines} lines"))
                    continue
                best = None
                for q in cands:
                    found = target.find_line(q, include_notes=(tgt != key))
                    if found is None:
                        scope_word = "own prose" if tgt == key else "text"
                        cand = ("MISSING", f'span not in {tgt} {scope_word}: "{norm(q)[:52]}…"', 2)
                    elif not (a - 2 <= found <= b + 2):
                        cand = ("DRIFTED", f"span is at {tgt}:{found}, note says {a}", 1)
                    else:
                        cand = ("CONFIRMED", f"span at {tgt}:{found}", 0)
                    if best is None or cand[2] < best[2]:
                        best = cand
                strong.append((where, tgt, a, best[0], best[1]))

            for cm in COUNT_RE.finditer(body):
                term = cm.group("term").strip()
                raw = cm.group("num").lower()
                claimed = WORDNUM.get(raw, None)
                if claimed is None:
                    try:
                        claimed = int(raw)
                    except ValueError:
                        continue
                scope = cm.group("scope")
                if not scope or scope not in chapters:
                    unparsed.append((where, f'"{term}" x{claimed} — no resolvable scope'))
                    continue
                word, sub = chapters[scope].count(term)
                if word == claimed and sub == claimed:
                    verdict = "CONFIRMED"
                elif word == claimed:
                    verdict = "STEM"      # true as a word, false as a stem — sharpen the sentence
                else:
                    verdict = "DRIFTED"
                counts.append((where, scope, term, claimed, word, sub, verdict))

    return strong, weak, counts, unparsed, unanchored


def main() -> int:
    ap = argparse.ArgumentParser(description="Re-derive the apparatus's own numeric claims.")
    ap.add_argument("--chapter", help="limit to one chapter, e.g. V.6")
    ap.add_argument("--all", action="store_true", help="print CONFIRMED rows too, not just failures")
    args = ap.parse_args()

    chapters = load_chapters()
    strong, weak, counts, unparsed, unanchored = audit(chapters, args.chapter)

    print("APPARATUS ROT — the notes' own locators and counts, re-derived from disk")
    print(f"  {BOOK}   ({len(chapters)} chapters loaded)\n")

    bad = [r for r in strong if r[3] != "CONFIRMED"]
    print(f"  LOCATORS (strong — quote-anchored): {len(strong)} checked, {len(bad)} failing")
    for where, tgt, a, verdict, why in (strong if args.all else bad):
        mark = "  ✓" if verdict == "CONFIRMED" else "  ⛔"
        print(f"{mark} {where:<16} {verdict:<10} {why}")
    if not bad:
        print("     (none failing)")

    weakbad = [r for r in weak if r[3] != "OK"]
    print(f"\n  LOCATORS (weak — no quote to anchor): {len(weak)} seen, {len(weakbad)} past EOF")
    for where, tgt, a, verdict, why in (weak if args.all else weakbad):
        mark = "  ·" if verdict == "OK" else "  ⛔"
        print(f"{mark} {where:<16} {tgt}:{a:<6} {verdict:<9} {why}")
    print("     ⚠ these are NOT evidence the locator is right — only that the line exists.")

    cbad = [r for r in counts if r[6] != "CONFIRMED"]
    print(f"\n  COUNT CLAIMS: {len(counts)} checked, {len(cbad)} needing attention")
    for where, scope, term, claimed, word, sub, verdict in (counts if args.all else cbad):
        mark = {"CONFIRMED": "  ✓", "STEM": "  ⚠", "DRIFTED": "  ⛔"}[verdict]
        print(f"{mark} {where:<16} \"{term}\" in {scope}: note says {claimed}, "
              f"disk says {word} whole-word / {sub} as a stem  [{verdict}]")
    if not cbad:
        print("     (none failing)")
    print("     ⚠ STEM = the claim is true of the word and false of the root. Not a")
    print("       refutation — an evidence sentence that needs one more clause.")

    print(f"\n  UNANCHORED QUOTES: {len(unanchored)} — quoted spans with no locator beside them.")
    for where, q in unanchored[:8]:
        print(f'     · {where:<16} "{q}…"')
    if len(unanchored) > 8:
        print(f"     … and {len(unanchored) - 8} more")
    print("     ⚠ NOT CHECKED, and printed rather than dropped. A quote with no CH:LINE")
    print("       next to it cannot be re-derived, and adopting it to the nearest locator")
    print("       invents failures — that cost this gauge a false ⛔ against IV.8 on its")
    print("       second run. Give a span a locator and it stays checkable. This number")
    print("       is the apparatus's uncheckable fraction; it should fall, not hold.")

    print(f"\n  UNPARSED: {len(unparsed)} numeric claims this gauge could not resolve.")
    for where, why in unparsed[:12]:
        print(f"     · {where:<16} {why}")
    if len(unparsed) > 12:
        print(f"     … and {len(unparsed) - 12} more")
    print("     ⚠ UNPARSED GOING UP IS NOT GOOD NEWS. It is the part of the apparatus")
    print("       that rots where this instrument cannot see — prose locators, 'a few")
    print("       pages later', counts with no named scope. Read it as coverage debt.")

    return 1 if (bad or weakbad or cbad) else 0


if __name__ == "__main__":
    sys.exit(main())
