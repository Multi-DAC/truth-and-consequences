#!/usr/bin/env python3
"""
COMPLEMENT REFERENT CHECK  —  Truth and Consequences, Day 195.  R-136 part 3.

DOES THE FIELD NAMED `Complement` CONTAIN A COMPLEMENT?

The defect this exists for: at VI.4 the card collapsed SEES into COMPLEMENTS and
the merged field kept the COMPLEMENTS name while reporting what the position
itself renders superbly. 18 of the 43 cards that carry the field ran under the
inverted sense from there to the end of the draft, including the card in VIII.2,
the chapter that proves you may not certify your own residual. The register in
08-THE-INSTRUMENTS did not merely miss it — it ruled the inverted form into
v3-canon as a FIXED STRING and required thirteen further cards to comply.

⛔ WHY THIS IS NOT A STRING MATCH, WHICH IS THE WHOLE DESIGN PROBLEM.

`Complement: what it renders superbly` and `Complement: the performance
traditions that never conceded the record was the archive` are the same shape.
Both name a noun phrase. The difference is whether the noun phrase denotes THIS
position or ANOTHER one, and no lexical rule separates them: "the live event" is
inverted at VI.5 and would be a perfectly good complement on a card about print.
Every regex that appeared to work during drafting worked by matching the four
glosses that happened to be in use.

So this instrument does not judge sense. IT FORCES A HUMAN RULING ON EVERY CARD
AND THEN NOTICES WHEN A RULED CARD CHANGES UNDERNEATH THE RULING. Three failure
states, all loud:

  UNRULED   a card carrying the field has no entry in the registry — a new card,
            or one this file has never been shown. Not a pass.
  STALE     the field body no longer hashes to what was ruled on. The ruling
            described text that is gone; it is withdrawn, not carried forward.
  SELF      a standing ruling that the field names its own subject. The defect.

★ AND IT REPORTS ITS OWN COVERAGE, because a green that covers 18 of 43 cards
and does not say so is the thing this project keeps getting caught by. The 25
v1-sense cards are OUTWARD (they name another position) and are deliberately
NOT graded here for REACHABILITY — IV.1 now demands a complement that can be
gone to, several v1 cards answer with an existence claim ("Anything with a
second dimension"), and grading them needs a read of each field body rather than
a line. They are carried as `unreached: reachability ungraded` and printed as
owed work every run. A worklist that prints is worth more than a verdict that
flatters.

Usage:
    python tools/complement_referent.py            # check; non-zero on any failure
    python tools/complement_referent.py --list     # every card, its ruling, its hash
    python tools/complement_referent.py --hashes   # emit current hashes (for re-ruling)
"""

import hashlib
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BOOK = ROOT / "book"
REGISTRY = Path(__file__).resolve().parent / "complement_rulings.json"

# Every dialect the label has worn across four card versions. The card format
# drifted four times and each drift renamed the label; an extractor that knows
# only v3-canon would report the v1 cards as absent, which is the exact shape of
# the error this file exists to catch.
LABEL = re.compile(
    r"^[>\s]*(?:\*{0,3}|_{0,3})"
    r"(?P<label>COMPLEMENTS?|Complements?|Its complement)"
    r"(?:\s*[—-][^:]*)?"
    r"(?:\*{0,3}|_{0,3})\s*:",
)

# ⚠ THE BODY MUST STOP AT THE NEXT FIELD, NOT THE NEXT BLANK LINE. In the v1
# blockquote cards every field is one line of a single unbroken quote, so a
# blank-line terminator swallowed BOUNDARY and NAVIGATIONAL IMPLICATION into the
# hash — and a ruling on the complement would then have gone STALE the first time
# anybody edited an unrelated line four fields down. An instrument that cries
# wolf on every edit is switched off, which is a slower way of having none.
# Caught by reading the emitted hashes before writing a single ruling against
# them, which is the only moment it was cheap to catch.
NEXT_FIELD = re.compile(
    r"^[>\s]*(?:\*{0,3}|_{0,3})"
    r"(SEES|NULL SPACE|BOUNDARY|NAVIGATIONAL IMPLICATION|SHAPE|WHERE IT SHOWS|"
    r"WHAT IT IS NOT|COMPLEMENTS?|Complements?|Renders|Null space|Its null space|"
    r"Boundary|Its boundary|Mechanism|Navigational implication|Whose|Era|"
    r"What it renders|Its complement|What would make this wrong)"
    r"[^:]{0,60}?(?:\*{0,3}|_{0,3})\s*:",
)


def fields():
    """Yield (chapter, line_no, label, body_hash, first_line) for every complement field."""
    out = []
    for path in sorted(BOOK.glob("*-*.md")):
        lines = path.read_text(encoding="utf-8", errors="replace").splitlines()
        for i, line in enumerate(lines):
            m = LABEL.match(line)
            if not m:
                continue
            # The body runs to the first blank line — in blockquote cards a bare
            # ">" counts as blank. CRLF is stripped by splitlines(); whitespace is
            # collapsed so a reflow does not read as a rewrite.
            body = [line]
            for nxt in lines[i + 1:]:
                if not nxt.strip() or nxt.strip() == ">":
                    break
                if NEXT_FIELD.match(nxt):
                    break
                body.append(nxt)
            norm = re.sub(r"\s+", " ", " ".join(body).replace(">", " ")).strip()
            h = hashlib.sha1(norm.encode("utf-8")).hexdigest()[:12]
            out.append((path.name, i + 1, m.group("label"), h, norm[:100]))
    return out


def main() -> int:
    found = fields()
    reg = json.loads(REGISTRY.read_text(encoding="utf-8")) if REGISTRY.exists() else {}
    rulings = reg.get("rulings", {})

    if "--hashes" in sys.argv:
        for chap, ln, _, h, head in found:
            print(f"{chap}:{ln}\t{h}\t{head}")
        return 0

    unruled, stale, self_ref, outward, ungraded = [], [], [], [], []
    for chap, ln, _, h, head in found:
        key = f"{chap}:{ln}"
        # A card that moved down the file is not a new card. Match on hash first,
        # then on chapter — a ruling keyed only to a line number would go STALE
        # every time a paragraph was inserted above it, and an instrument that
        # cries wolf on every edit gets switched off, which is a slower way of
        # having no instrument at all.
        r = rulings.get(key)
        if r is None:
            r = next(
                (v for k, v in rulings.items()
                 if k.split(":")[0] == chap and v.get("hash") == h),
                None,
            )
        if r is None:
            by_chapter = [v for k, v in rulings.items() if k.split(":")[0] == chap]
            (stale if by_chapter else unruled).append((key, h, head))
            continue
        if r.get("hash") != h:
            stale.append((key, h, head))
            continue
        verdict = r.get("verdict")
        if verdict == "SELF":
            self_ref.append((key, r.get("note", "")))
        elif verdict == "REFUSED":
            outward.append(key)
        else:
            outward.append(key)
            # ⚠ THREE VALUES, NOT A BOOLEAN. `reachable: false` would mean both
            # "graded, and the reader cannot get to it" (VI.6, a finding the card
            # states outright) and "nobody has looked" (the v1 backlog). Those are
            # opposite epistemic states and a boolean prints them as one number —
            # which is the collapse this whole instrument exists because of.
            if r.get("reach", "ungraded") == "ungraded":
                ungraded.append(key)

    total = len(found)
    print("COMPLEMENT REFERENT — does the field named Complement contain one?")
    print(f"  cards carrying the field, from disk: {total}")
    print(f"  ruled OUTWARD (names another position): {len(outward)}")
    print(f"  ruled SELF (names its own subject): {len(self_ref)}")
    print(f"  UNRULED: {len(unruled)}   STALE: {len(stale)}")
    print(f"  ⚠ reachability UNGRADED: {len(ungraded)} of {len(outward)} outward cards"
          f" — owed work, not a pass\n")

    for key, note in self_ref:
        print(f"  ⛔ SELF     {key}  {note}")
    for key, h, head in stale:
        print(f"  ⚠ STALE    {key}  hash now {h}\n              {head}")
        print("              the ruling described text that no longer exists; re-rule it")
    for key, h, head in unruled:
        print(f"  ⚠ UNRULED  {key}  hash {h}\n              {head}")
        print("              no human has ruled on this field; add it to "
              "tools/complement_rulings.json")

    if ungraded:
        print(f"\n  ungraded for reachability ({len(ungraded)}): "
              + ", ".join(sorted(ungraded)))
        print("  IV.1 requires a complement that can be gone to. These name another")
        print("  position and have not been read for whether the reader could reach it.")

    if "--list" in sys.argv:
        print()
        for chap, ln, label, h, head in found:
            key = f"{chap}:{ln}"
            r = rulings.get(key) or next(
                (v for k, v in rulings.items()
                 if k.split(":")[0] == chap and v.get("hash") == h), {})
            v = r.get("verdict", "—")
            print(f"  {key:<58} {v:<8} {r.get('reach', 'ungraded'):<11} {h}")

    bad = len(self_ref) + len(stale) + len(unruled)
    if bad:
        print(f"\n⛔ {bad} card(s) fail. This is a gate on the instrument, not a style note.")
        return 1
    print("✅ every card carrying the field has a standing human ruling, and every")
    print("   ruling still describes the text on the page.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
