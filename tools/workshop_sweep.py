#!/usr/bin/env python3
"""
WORKSHOP SWEEP — Truth and Consequences, Day 205. Clayton's ruling, given a gauge.

WHY THIS EXISTS.

Day 205, Clayton ruled on four checklist rows at once: *"let's strip the workshop. It's a book,
not a demonstration of book writing."* and *"let's strip references to outside files and works
of our own. No need for our archive to be available, including that of the work shopping and
writing of this book. The book should stand as it is without external files."*

That is one standard covering four censuses that were taken separately, by four different
instruments, on four different days (R2-032, R2-033, R2-035, R2-036). Each census was a
number in a checklist row. A number in a row is a MEASUREMENT and it rots: the row says 54
and the source says something else, because the row counted printed PDF pages and the source
is markdown. So this file re-derives all four from disk, on demand, and is the thing that gets
to say the work is finished. The checklist rows do not get to say it.

WHAT IT COUNTS — four classes, and they are NOT disjoint. Do not add them.

  SLUG      `[[a_lesson_slug]]` — a memory-store filename. compile_pdf.py strips the brackets,
            so on the page it arrives looking like a term of art the reader missed.
  PROCID    `ruling 177`, `R-144` — process-row IDs from a queue no reader has. Not in the
            glossary, not in the works-cited. Reads as a scholarly cross-reference apparatus
            pointing at a body of rulings that does not exist.
  FILEREF   a pointer to a file in this project or on this disk: apparatus filenames (`05`,
            `07-THE-CLAIMS-REGISTER.md`), tool names (`compile_pdf.py`), absolute paths.
  DRAFTING  the book narrating its own construction: `Filed with`, `the generator`, drafted-
            chapter counts, audit lines pasted into prose, notes-to-a-maintainer.

  ARCHIVE   (fifth, added for the second ruling) — counts and claims about OUR corpus that a
            reader cannot obtain: "search it for maybe logic and you get eleven files".
            VI.8 already rules these off the page in its own prose; VI.7 prints eleven of them.

⚠ WHAT IT CANNOT DO. This is a PATTERN gauge, so it finds tokens, not intentions. A sentence
that narrates the drafting process in ordinary English with no marker word is invisible here.
A green run means "no marked workshop residue"; it does not mean "the book stops talking about
its own making." Only a read settles that, and the D204 read is the one on record.

Positive control below plants one of each class in synthetic text and requires all five caught.
"""

import re
import sys
import pathlib

BOOK = pathlib.Path(__file__).resolve().parent.parent / "book"

# ── the five detectors ────────────────────────────────────────────────────────
# Each is (name, compiled regex, note). Order is the report order.

# ⚠ The hyphen alternative is not decoration. The first version of this pattern was
# `[a-z0-9_]` only, it printed ✅ SLUG 0, and IV.6 was carrying two tags written with
# HYPHENS and no `feedback_` prefix at lines 477 and 495. The read notes had said so
# on D204 — "some slugs are hyphenated rather than feedback_-prefixed" — and the gauge
# was built from the common shape rather than from the census. A green that came from
# a narrowed pattern reads exactly like a green that came from clean text.
SLUG = re.compile(r"\[\[[a-z0-9][a-z0-9_-]{4,}\]\]")

PROCID = re.compile(r"\b(?:[Rr]uling\s+\d+|R-\d+)\b")

FILEREF = re.compile(
    r"""(?x)
      \b[\w\-]+\.(?:py|md|json|txt|tex|sty|yaml|toml|db|sqlite3?)\b   # any filename with a code/doc extension
    | \b[A-Z]:[\\/][\w\\/.\-]+                                        # absolute Windows path
    | (?<![\w/])/(?:c|mnt|home|Users)/[\w/.\-]+                       # absolute posix path
    | \b\d{2}-[A-Z][A-Z\-]{3,}\b                                      # apparatus files: 07-THE-CLAIMS-REGISTER
    | `0\d`                                                           # the SAME files by bare number: `05`, `07`
    | \bplanning\s+(?:document|file|apparatus)s?\b                    # the drafting tree, unnamed
    | \bthe\s+scaffold\b
    """
)
# ⚠ The last three alternatives were added AFTER the first FILEREF pass printed a green.
# The pattern required a file extension or the NN-CAPS form, and the book refers to the same
# apparatus files 31 more times as bare backticked numbers — `05`'s ruling, `07` C27, "the
# scaffold", "our own planning file". Found by reading the DRAFTING residue, not by this
# gauge. A pattern built from the loudest form of a thing certifies the quiet form clean.

DRAFTING = re.compile(
    r"""(?xi)
      \bfiled\s+(?:with|as|under)\s+(?:R-|ruling|the\s+queue)         # "Filed with R-143"
    | \b(?:the\s+)?revision\s+queue\b
    | \bthe\s+generator\b
    | \b(?:sixty|fifty|forty|seventy)-\w+\s+drafted\s+chapters?\b
    | \bdrafted\s+chapters?\b
    | \bnamed_cause\b
    | \bthis\s+(?:chapter|book|volume)'?s?\s+own\s+(?:draft|drafting)\b
    | \b(?:a\s+)?note\s+to\s+(?:the\s+)?maintainer\b
    | \bstanding\s+note\b
    """
)

ARCHIVE = re.compile(
    r"""(?xi)
      \b(?:search|grep)\s+(?:it|the\s+corpus|the\s+archive)\b
    | \byou\s+get\s+\w+\s+files?\b
    | \b\w+\s+files?\s+in\s+(?:the|our|that)\s+(?:corpus|archive)\b
    | \bthe\s+corpus\s+(?:contains|holds|has)\s+\w+\s+files?\b
    | \bfile\s+count\b
    """
)

CLASSES = [
    ("SLUG", SLUG, "memory-store filenames printing as terms of art"),
    ("PROCID", PROCID, "process-row IDs from a queue no reader has"),
    ("FILEREF", FILEREF, "pointers to files in this project or on this disk"),
    ("DRAFTING", DRAFTING, "the book narrating its own construction"),
    ("ARCHIVE", ARCHIVE, "counts in our corpus a reader cannot obtain"),
]

# Lines carrying this marker are deliberate and exempt. Used by Z-01's ban list,
# which must be able to NAME the thing it bans.
EXEMPT = "<!-- workshop-ok -->"


def scan_text(text, classes=CLASSES):
    """Yield (class_name, lineno, matched_text, line) for every hit."""
    for i, line in enumerate(text.splitlines(), 1):
        if EXEMPT in line:
            continue
        for name, rx, _ in classes:
            for m in rx.finditer(line):
                yield name, i, m.group(0), line.strip()


def scan_book():
    hits = {}
    for path in sorted(BOOK.glob("*.md")):
        text = path.read_text(encoding="utf-8")
        for name, lineno, match, line in scan_text(text):
            hits.setdefault(name, []).append((path.name, lineno, match, line))
    return hits


# ── positive control ──────────────────────────────────────────────────────────

CONTROL = """\
The reader is invited to consider [[feedback_quotation_connective_tissue]] here.
And also [[disclaimer-not-coupled-to-verdict]], which is written the other way.
That was settled by ruling 177 and again at R-144.
See 05 and compile_pdf.py, or C:/Users/Wasch/truth-and-consequences/book.
Filed with R-143 after the sixty-three drafted chapters were counted.
Search it for maybe logic and you get eleven files.
"""

CONTROL_CLEAN = """\
The reader is invited to consider what the connective tissue of a quotation does.
That was settled elsewhere, and the reasoning is set out in the chapter above.
See the chapter on the lexicon, which does the same work in prose.
The point survived the drafting; nothing about the drafting is on this page.
The pattern is common enough that the reader will have met it already.
"""


def control():
    """Plant one of each class; require all five caught and the clean text silent."""
    rows = list(scan_text(CONTROL))
    got = {name for name, *_ in rows}
    want = {name for name, _, _ in CLASSES}
    missed = want - got
    # ⚠ Class-level "caught" is too weak for SLUG: the underscore form alone would
    # light the class green while the hyphen form walked past. Require BOTH.
    slug_n = sum(1 for name, *_ in rows if name == "SLUG")
    if slug_n < 2:
        print(f"    NARROW  SLUG caught {slug_n}/2 planted forms "
              f"(underscore + hyphen) — the pattern is narrower than the corpus.")
        missed = missed | {"SLUG-hyphen"}
    false_pos = [h for h in scan_text(CONTROL_CLEAN)]
    ok = not missed and not false_pos
    print("POSITIVE CONTROL — synthetic text, 5 planted classes, 1 clean foil:")
    for name, _, _ in CLASSES:
        print(f"    {'caught ' if name in got else 'MISSED '} {name}")
    if false_pos:
        for name, ln, match, _ in false_pos:
            print(f"    FALSE POSITIVE  {name}  L{ln}  {match!r}")
    print(f"  [{'ok' if ok else 'BROKEN'}] {len(got)}/5 planted caught, "
          f"{len(false_pos)} false positive(s) on the clean foil.")
    print("  Detector is live.\n" if ok else "  DETECTOR IS NOT LIVE — fix before trusting a green.\n")
    return ok


def main():
    verbose = "-v" in sys.argv or "--verbose" in sys.argv
    if not control():
        return 2

    hits = scan_book()
    total = sum(len(v) for v in hits.values())

    print("WORKSHOP SWEEP — Clayton's D205 ruling, re-derived from disk\n")
    for name, _, note in CLASSES:
        rows = hits.get(name, [])
        files = len({r[0] for r in rows})
        mark = "✅" if not rows else "⛔"
        print(f"  {mark} {name:<9} {len(rows):>4} occurrence(s) in {files} file(s)   — {note}")
        if rows and verbose:
            for fname, lineno, match, line in rows:
                print(f"        {fname}:{lineno}  {match!r}")
                print(f"            {line[:150]}")
        elif rows:
            shown = rows[:6]
            for fname, lineno, match, _ in shown:
                print(f"        {fname}:{lineno}  {match!r}")
            if len(rows) > len(shown):
                print(f"        … and {len(rows) - len(shown)} more (-v for all)")
    print()
    if total == 0:
        print("WORKSHOP SWEEP: ✅ CLEAN — no marked workshop residue in any book file.")
        print("  ⚠ This is a TOKEN gauge. A sentence that narrates the drafting in plain")
        print("    English with no marker word is invisible here. Green ≠ the book has")
        print("    stopped talking about its own making; only a read settles that.")
    else:
        print(f"WORKSHOP SWEEP: ⛔ {total} occurrence(s) across "
              f"{len({r[0] for v in hits.values() for r in v})} file(s).")
    return 0 if total == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
