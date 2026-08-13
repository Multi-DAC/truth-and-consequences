#!/usr/bin/env python3
"""roster_verify.py — check that every NAMED entry in BOOK-V-ROSTER.md is really in the prose.

WHY THIS EXISTS. The Day-192 roster rebuild (R-157) is a hand-built list. A hand-built
list is a hypothesis; this is the gauge that can refute it. It answers exactly one
question: does the string appear in the chapter at all?

WHAT IT DOES NOT DO — read this before quoting it.
  * It cannot tell you a name is MISSING FROM the roster. It only checks the entries
    that are there. A name the readers and I both walked past is invisible to it, and
    that is the failure mode R-157 was filed on. This gauge does not close R-157's
    class; it closes only "the roster asserts a name the chapter does not contain."
  * It does not check the BAND. A name can be present and mis-banded (SOURCE that is
    really a MENTION). Banding is a judgement and this tool has none.
  * A hit is not a citation. Presence of the token says nothing about whether the
    chapter leans on it.

THE ONE REAL TRICK. Book chapters are hard-wrapped, so a two-word name is routinely
split across a newline. A line-scoped grep returns 0 on a name that is plainly there —
this happened on Day 192 with "Dao De Jing" and nearly refuted a correct reader. So the
chapter text is whitespace-collapsed to a single line before matching, and markdown
emphasis is stripped, because "*Zhuangzi*" and "Zhuangzi" are the same name.

USAGE
    python tools/roster_verify.py                 # check, print, exit 1 on any miss
    python tools/roster_verify.py --show-hits     # also print the matched context
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ROSTER = ROOT / "book" / "docs" / "BOOK-V-ROSTER.md"
BOOK = ROOT / "book"

SECTION_RE = re.compile(r"^###\s+V\.(\d+)\b")
BAND_RE = re.compile(r"^-\s+\*\*(NAMED|UNNAMED|INTERNAL|ACTOR|MENTION)\*\*:\s*(.*)$")
AS_RE = re.compile(r'\(as\s+"([^"]+)"\)')


def normalise(text: str) -> str:
    """Collapse to one line and drop markdown emphasis, so a wrapped name still matches.

    Blockquote markers are stripped at line-start for the same reason as the wrap itself.
    Found the hard way on this tool's FIRST run: "The Hebrew prophets" sits inside a card
    and wraps as `The Hebrew\n> prophets`, so collapsing whitespace alone yields
    "The Hebrew > prophets" and the name reads as absent. I had diagnosed the hard wrap,
    built the fix for the hard wrap, and left its sibling artefact standing in the very
    tool written to catch it. [[feedback_repair_scoped_to_named_cause]]
    """
    text = text.replace("*", "").replace("_", "")
    text = re.sub(r"(?m)^\s*>+\s?", "", text)
    return re.sub(r"\s+", " ", text)


def chapter_path(num: str) -> Path | None:
    hits = sorted(BOOK.glob(f"V-{int(num):02d}-*.md"))
    return hits[0] if hits else None


def entry_probe(entry: str) -> tuple[str, str]:
    """Return (display, search-string) for one roster entry.

    `Michael Harner (as "Harner")` searches for the form the prose actually uses.
    Otherwise a trailing parenthetical is decoration and is dropped from the probe.
    """
    display = entry.strip()
    m = AS_RE.search(display)
    if m:
        return display, normalise(m.group(1))
    probe = re.sub(r"\s*\([^)]*\)\s*$", "", display)
    probe = probe.replace("⚑", "").strip()
    return display, normalise(probe)


def main() -> int:
    show_hits = "--show-hits" in sys.argv
    if not ROSTER.exists():
        print(f"⛔ no roster at {ROSTER}")
        return 2

    current: str | None = None
    text_cache: dict[str, str] = {}
    checked = missing = 0
    misses: list[tuple[str, str]] = []
    soft: list[tuple[str, str]] = []

    for raw in ROSTER.read_text(encoding="utf-8").splitlines():
        sec = SECTION_RE.match(raw)
        if sec:
            current = sec.group(1)
            continue
        band = BAND_RE.match(raw.strip())
        if not band or current is None:
            continue
        if band.group(1) not in ("NAMED", "FORMULA"):
            continue
        bandname = band.group(1)

        if current not in text_cache:
            path = chapter_path(current)
            if path is None:
                print(f"⛔ V.{current}: no chapter file on disk")
                return 2
            text_cache[current] = normalise(path.read_text(encoding="utf-8"))
        hay = text_cache[current]

        for entry in band.group(2).split("·"):
            if not entry.strip():
                continue
            display, probe = entry_probe(entry)
            if not probe:
                continue
            checked += 1
            if probe in hay:
                if show_hits:
                    i = hay.index(probe)
                    print(f"  V.{current}  ✓ {bandname[0]} {display}\n        …{hay[max(0, i - 60):i + len(probe) + 60]}…")
            elif probe.lower() in hay.lower():
                # Present but cased differently. Not a miss, but worth saying out loud:
                # the roster should quote the prose, and a case slip can hide a real
                # difference between a tradition-name and an ordinary word.
                soft.append((f"V.{current}", display))
            else:
                missing += 1
                misses.append((f"V.{current}", f"[{bandname}] {display}"))

    print(f"ROSTER VERIFY — {checked} NAMED/FORMULA entries checked against the prose, "
          f"whitespace-collapsed (a wrapped name still matches).")
    if soft:
        print(f"\n⚠ {len(soft)} present but cased differently from the roster — "
              f"quote the prose's own casing:")
        for chap, display in soft:
            print(f"   {chap:6s} {display}")
    if misses:
        print(f"\n⛔ {missing} entr{'y' if missing == 1 else 'ies'} NOT FOUND in the chapter:")
        for chap, display in misses:
            print(f"   {chap:6s} {display}")
        print("\nA miss is one of: the name is not in that chapter, the roster spells it "
              "differently from the prose (use `Name (as \"prose form\")`), or the chapter changed.")
        return 1

    print("✓ every NAMED entry is present in its chapter.")
    print("  LIMIT: this cannot see a name MISSING FROM the roster — the R-157 defect. "
          "Presence is not a citation and the band is not checked.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
