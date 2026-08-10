#!/usr/bin/env python3
"""pointer_title_check.py — R-115, filed Day 190, written Day 191.

THE DEFECT IT EXISTS FOR. Three pointer errors were found in three days, all by
re-reading, none by any instrument in this repo:

  - VII.8's brief pointed at a chapter for a treatment that was not in it.
  - VIII.1's brief said `Watts`, returning from **I.6**. `Watts` occurs ZERO
    times in I.6; he is in III.2. A drafter following the brief would have
    written a false internal cross-reference into shipped prose.
  - VIII.3's source row said "The Seven Navigation Classes" where the source
    says eight.

`brief_fields` reads for HOLES and says so in its own footer: a `Source:` line
that is present and FALSE passes it. `card_sweep` counts vocabulary.
`order_sweep` is book-level and cannot see a chapter-level pointer. So the
class had no gauge, and was being caught by luck with good note-taking — which
is the thing this manuscript has a standing order against.

WHAT IT CHECKS. Two arms, both cheap, both able to fail on their own:

  ARM A — POINTER vs TITLE. Any `IV.7 — SOME TITLE` construction anywhere in
  the manuscript is checked against the canonical title for IV.7. Catches a
  pointer that names a real chapter and misdescribes it.

  ARM B — CLAIM-OF-PRESENCE vs TEXT. A brief line of the form
  `**Watts**, returning from **I.6**` asserts that a name occurs in a chapter.
  Every bolded proper noun within a window of a chapter pointer is grepped
  against that chapter's actual file. Catches the VIII.1 error exactly.

⛔ WHAT IT CANNOT SEE, and this is not a caveat, it is half the class:
  - A pointer at an EXTERNAL source (`Guide §4.1`, `Doctrine §13.4`). The
    R-116 error — "Seven" where the source says eight — lives here. Checking
    it means reading a file outside this repo, which this tool deliberately
    does not do, because a gauge with an off-tree dependency fails silently
    the day the tree moves. R-116's class is STILL UNGAUGED. Say so.
  - A pointer that is CORRECT about the title and WRONG about the content.
    Arm B narrows this to named entities and no further.
  - Prose that describes a chapter without naming it.
"""

from __future__ import annotations
import re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BOOK = ROOT / "book"

ROMAN = r"(?:I{1,3}|IV|V|VI{1,3}|IX|X)"
POINTER = re.compile(rf"\b({ROMAN})\.(\d{{1,2}})\b")
# `### VII.8 — MEANING WITHOUT A MANDATE ✅ DRAFTED — 6,146 words`
HEADING = re.compile(
    rf"^#{{2,3}}\s+({ROMAN})\.(\d{{1,2}})\s*[—-]\s*(.+?)\s*$", re.M)
# `IV.7 — THE NON-PHYSICAL` used inline, title in the manuscript's shouting case
INLINE_TITLED = re.compile(
    rf"\*{{0,2}}({ROMAN})\.(\d{{1,2}})\*{{0,2}}\s*[—-]{{1,2}}\s*\*{{0,2}}([A-Z][A-Z ,'’\-]{{6,}})")
BOLD_NAME = re.compile(r"\*\*([A-Z][a-zA-Zàéèêöü’'\-]{2,})\*\*")
# Arm B's window. See the note at its call site: LINE scope produced 7/7 false
# positives on the first cold run, all of them two unrelated assertions sharing
# a row. The manuscript's own separator is the middot.
CLAUSE = re.compile(r"·|\||(?<=[.!?])\s+(?=[A-Z★⚠⛔])")
# Case-insensitive on purpose: the manuscript SHOUTS its absence claims
# (`occurs ZERO times in I.6`), and a case-sensitive guard let the very note
# that documents a fixed pointer error fire as a standing false alarm — which
# is how a gauge becomes a warning nobody reads.
ASSERTS_ABSENCE = re.compile(
    r"=\s*\*{0,2}0\b|\b(?:also|and|is|are|remains?)\s+\*{0,2}0\b"
    r"|occurs?\s+(?:zero|0)\s+times|\bzero times\b", re.I)

# Bolded words that are structural vocabulary, not people or works.
NOT_A_NAME = {
    "DRAFTED", "AMENDED", "Beats", "Source", "Named", "Establishes", "Depends",
    "Complement", "Boundary", "Whose", "Mechanism", "Navigational", "Book",
    "Corrected", "Promoted", "Filed", "The", "And", "But", "This", "That",
    "Both", "Every", "Not", "It", "Its", "One", "Two", "Three", "Four", "Five",
    "Seven", "Eight", "Nine", "Ten", "Class", "Part", "Guide", "Doctrine",
    "Method", "Ruling", "Beat", "Card", "Register", "Queue", "Tool", "Day",
    "PER", "BRIEF", "AND", "THE", "FOUND", "THIRD", "SECOND",
    "Thesis", "Beat", "Trap", "Opponent", "Instrument", "Claim", "Note",
}

# ADJUDICATED EXEMPTIONS. Anchored to CONTENT, never to a line number — a line
# number rots on the next insertion and takes the exemption's meaning with it.
# Each carries its reason, and the count is printed whether or not it is zero,
# because an exemption list that hides is a second null space.
EXEMPT: list[tuple[str, str]] = [
    ("VIII.1's `Named:` line reads",
     "the note that DOCUMENTS the corrected Watts/I.6 error, quoting the defective "
     "pointer verbatim so a reader can see what was wrong. A true positive on a "
     "quotation. Removing the quote would remove the record."),
]


def norm(s: str) -> str:
    """Compare titles by their letters only — markers, word counts and
    decoration are not part of the identity of a title."""
    s = re.split(r"✅|⚠|⛔|★", s)[0]
    s = re.sub(r"\*+", "", s)
    s = re.sub(r"\(.*?\)", "", s)
    s = re.sub(r"[^A-Za-z ]", " ", s)
    return " ".join(s.upper().split())


def canonical_titles() -> dict[tuple[str, int], str]:
    """From the scaffold's own headings, and from the chapter files, which are
    the two places a title is written down. A disagreement between them is
    itself reported."""
    titles: dict[tuple[str, int], str] = {}
    scaffold = (ROOT / "06-THE-SCAFFOLD.md").read_text(encoding="utf-8", errors="replace")
    for bk, n, title in HEADING.findall(scaffold):
        titles[(bk, int(n))] = norm(title)
    for f in sorted(BOOK.glob("*.md")):
        head = f.read_text(encoding="utf-8", errors="replace")[:400]
        m = HEADING.search(head)
        if not m:
            continue
        key = (m.group(1), int(m.group(2)))
        t = norm(m.group(3))
        if key in titles and titles[key] != t:
            print(f"  ⚠ TITLE DISAGREEMENT {key[0]}.{key[1]}: "
                  f"scaffold {titles[key]!r} vs chapter file {t!r}")
        titles.setdefault(key, t)
    return titles


def chapter_files() -> dict[tuple[str, int], Path]:
    out: dict[tuple[str, int], Path] = {}
    for f in sorted(BOOK.glob("*.md")):
        m = re.match(rf"^({ROMAN})-(\d{{2}})-", f.name)
        if m:
            out[(m.group(1), int(m.group(2)))] = f
    return out


def scan_targets() -> list[Path]:
    return [p for p in sorted(ROOT.glob("*.md"))] + \
           [p for p in sorted(BOOK.glob("*.md"))
            if p.name not in {"DRAFT-LOG.md", "REVISION-QUEUE.md"}]


def main() -> int:
    titles = canonical_titles()
    files = chapter_files()
    print(f"POINTER/TITLE CHECK — {len(titles)} canonical titles · "
          f"{len(files)} chapter files on disk\n")

    arm_a: list[str] = []
    arm_b: list[str] = []
    dangling: list[str] = []
    exempted: list[str] = []

    for path in scan_targets():
        rel = path.relative_to(ROOT).as_posix()
        text = path.read_text(encoding="utf-8", errors="replace")
        lines = text.splitlines()

        for i, line in enumerate(lines, 1):
            if line.lstrip().startswith("#"):
                continue  # a heading IS the canonical statement, not a pointer at one

            # ARM A — a pointer that carries a title with it.
            # ⚠ NARROWED Day 191, first run: the loose form flagged ten hits and all
            # ten were a caps EMPHASIS run being read as a title ("III.6 — ADOPTED
            # WHOLE"). The narrowing is principled rather than cosmetic — require the
            # claimed string to BE some chapter's real title, then check it is THIS
            # chapter's. That is exactly the dangerous form: a pointer paired with a
            # plausible title belonging to a different chapter. It gives up the
            # typo'd-title case, which is stated in the LIMIT.
            known = set(titles.values())
            for bk, n, claimed in INLINE_TITLED.findall(line):
                key = (bk, int(n))
                if key not in titles:
                    dangling.append(f"{rel}:{i}  {bk}.{n} — no such chapter")
                    continue
                want, got = titles[key], norm(claimed)
                if not (want and got) or got not in known:
                    continue
                if not (got.startswith(want) or want.startswith(got)):
                    arm_a.append(f"{rel}:{i}  {bk}.{n} called {got!r}, canonically {want!r}")

            # ARM B — a bolded name in the same line as a pointer asserts presence.
            # ⚠ Two exclusions, both principled, both recorded because a filter that
            # quietly eats true positives reads as a cleaner list (LC: filter
            # precision eats recall). (1) A line ASSERTING ABSENCE — `Dunning` = 0,
            # `Watts` occurs zero times — is stating the tool's own finding and
            # agreeing with it; flagging it inverts the claim. (2) An ALL-CAPS bolded
            # token is this manuscript's emphasis marker, not a person: every real
            # name in the register is Capitalised, never SHOUTED.
            # ⚠⚠ AND THE THIRD NARROWING, WHICH IS A DEFECT I BUILT AND THEN FOUND IN
            # MY OWN TOOL ON ITS FIRST COLD RUN. Arm B was LINE-scoped, and every one
            # of its seven surviving hits was a line-scope artifact: this manuscript's
            # briefs pack many independent assertions onto one line separated by `·`,
            # so `…5, all in VII.2… · ★ **Darwall** —` reads as "Darwall is in VII.2"
            # when the two clauses have nothing to do with each other. That is R-37
            # EXACTLY — `claim_sweep`'s licence guard is line-scoped and has been on
            # the queue for days — rebuilt from scratch in a new tool by someone who
            # had read the R-37 row. A defect you have filed is not a defect you have
            # stopped making. Arm B is now CLAUSE-scoped.
            hit_exempt = next((r for a, r in EXEMPT if a in line), None)
            if hit_exempt:
                exempted.append(f"{rel}:{i}  — {hit_exempt}")
                continue

            for seg in CLAUSE.split(line):
                if ASSERTS_ABSENCE.search(seg):
                    continue
                ptrs = POINTER.findall(seg)
                if not ptrs:
                    continue
                names = [n for n in BOLD_NAME.findall(seg)
                         if n not in NOT_A_NAME and not n.isupper()]
                if not names:
                    continue
                for bk, n in ptrs:
                    key = (bk, int(n))
                    f = files.get(key)
                    if f is None:
                        if key not in titles:
                            dangling.append(f"{rel}:{i}  {bk}.{n} — no such chapter")
                        continue
                    body = f.read_text(encoding="utf-8", errors="replace")
                    for name in names:
                        if re.search(rf"\b{re.escape(name)}\b", body):
                            continue
                        arm_b.append(
                            f"{rel}:{i}  claims `{name}` at {bk}.{n} "
                            f"({f.name}) — {name} occurs 0 times there")

    def report(title: str, rows: list[str]) -> None:
        print(f"  {title}: {len(rows)}")
        for r in dict.fromkeys(rows):
            print(f"    ✗ {r}")
        print()

    report("ARM A — pointer names a title that is not that chapter's", arm_a)
    report("ARM B — pointer claims a name is in a chapter that lacks it", arm_b)
    report("DANGLING — pointer at a chapter that does not exist", dangling)
    print(f"  EXEMPTED — adjudicated, with reasons, not hidden: {len(exempted)}")
    for r in dict.fromkeys(exempted):
        print(f"    · {r}")
    print()

    print("  ⛔ LIMIT — READ THIS BEFORE TREATING A ZERO AS A CLEAN BILL.")
    print("     This tool checks pointers INTO THIS MANUSCRIPT only. A pointer at an")
    print("     external source — `Guide §4.1`, `Doctrine §13.4` — is invisible to it,")
    print("     and that is where R-116 lived: a source row that said SEVEN navigation")
    print("     classes where the Guide says eight. THAT CLASS IS STILL UNGAUGED and is")
    print("     still being caught by re-reading. Arm B narrows content errors to named")
    print("     entities and no further: a brief may point at the right chapter, name a")
    print("     person who is genuinely in it, and still be wrong about what it says.")
    bad = len(arm_a) + len(arm_b) + len(dangling)
    print(f"\n  {'⛔ ' + str(bad) + ' pointer defect(s)' if bad else '✓ PASS'}")
    return 1 if bad else 0


def selftest() -> int:
    """A zero needs a positive control. Rebuild the two errors this tool was
    written for and require it to catch both."""
    ok = True
    titles = canonical_titles()
    files = chapter_files()

    # Control 1 (Arm A): mislabel a real chapter.
    line = "returning from **I.6 — THE GAME THAT IS PLAYING YOU** for the practice half"
    hit = False
    for bk, n, claimed in INLINE_TITLED.findall(line):
        want, got = titles.get((bk, int(n)), ""), norm(claimed)
        if want and got and not (got.startswith(want) or want.startswith(got)):
            hit = True
    print(f"  control 1 (Arm A, wrong title on I.6): {'CAUGHT' if hit else 'MISSED'}")
    ok &= hit

    # Control 2 (Arm B): the actual VIII.1 defect, verbatim from the brief.
    line = "★ **Watts**, returning from **I.6** for the practice half"
    names = [n for n in BOLD_NAME.findall(line) if n not in NOT_A_NAME]
    hit = False
    for bk, n in POINTER.findall(line):
        f = files.get((bk, int(n)))
        if not f:
            continue
        body = f.read_text(encoding="utf-8", errors="replace")
        for name in names:
            if not re.search(rf"\b{re.escape(name)}\b", body):
                hit = True
    print(f"  control 2 (Arm B, Watts absent from I.6): {'CAUGHT' if hit else 'MISSED'}")
    ok &= hit

    # Control 3 (negative): the CORRECTED line must pass.
    line = "★ **Watts**, returning from **III.2** for the practice half"
    names = [n for n in BOLD_NAME.findall(line) if n not in NOT_A_NAME]
    false_pos = False
    for bk, n in POINTER.findall(line):
        f = files.get((bk, int(n)))
        if not f:
            continue
        body = f.read_text(encoding="utf-8", errors="replace")
        for name in names:
            if not re.search(rf"\b{re.escape(name)}\b", body):
                false_pos = True
    print(f"  control 3 (corrected III.2 must pass): {'PASS' if not false_pos else 'FALSE POSITIVE'}")
    ok &= not false_pos

    print(f"\n  {'✓ SELFTEST PASS' if ok else '⛔ SELFTEST FAIL'}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(selftest() if "--selftest" in sys.argv else main())
