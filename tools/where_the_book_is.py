#!/usr/bin/env python3
"""
WHERE THE BOOK IS  —  Truth and Consequences, Day 188.

THE ONE NUMBER EVERY PLANNING DECISION RESTS ON, AND THE ONLY ONE WITH NO GAUGE.

This directory holds twelve instruments. Every one of them measures PROSE:
voice uniformity, terminal commentary, beat delivery, ancestor coverage, claim
density, reviewer gaps. They are good instruments and several of them have
caught real defects that no amount of reading would have found.

Not one of them answers "how much of the book exists."

That is not the cheapness law — chapter count is the CHEAPEST measurement in the
entire project, `ls book/ | wc -l`, one line, no calibration, no false positives.
It is a sharper thing and it needs its own name:

    INSTRUMENTS GO WHERE INSTRUMENTS ARE INTERESTING.

Voice uniformity is a hard, absorbing, genuinely novel measurement problem and I
built a tool for it. Counting files is not a problem at all, so it never presented
as work, so it stayed in prose — carried by documents, written by hand, at the end
of long sessions, by someone who had just finished a chapter and was tired.

WHAT IT FOUND ON ITS FIRST RUN, which is why it exists:

    FOUR CARRIERS, FOUR DIFFERENT NUMBERS, NOT ONE OF THEM RIGHT.

    disk (ground truth)      : 32 chapters, 96,274 words
    Architecture/handoff.json: 41   ❌ over  by 9  — the live continuity carrier
    book/DRAFT-LOG.md        : 29   ❌ under by 3  — stopped carrying it after IV.7
    06-THE-SCAFFOLD.md       : 16   ❌ under by 16 — ✅ marks stopped mid-Book-III

    ...and every one of them says the denominator is 68 where the scaffold
    itself lists 67. Even the constant had drifted.

The handoff is the one SessionStart prints as the ACTIVE TASK. Every breath of
Day 188 opened by reading that the book was 41/68 — 60% — when it was 32/67, 48%.
The scaffold, which is the document you consult to decide WHAT TO WRITE NEXT,
says 16 chapters are unwritten that are sitting finished on disk beside it.

No comparison among them could have caught this. They diverge in BOTH directions
from a truth none of them consults, so agreement was never available as a signal.
A consistency check between two stamps is not a gauge. All four were true once.
That is what a stamp is.

THE COUNTS ROT TOO, AND HARDER THAN THE COUNT OF COUNTS. Calibrating against the
scaffold's own hand-written per-chapter numbers — a positive control with sixteen
known answers — IV.6 and IV.7 reproduce EXACTLY (delta 0, same pipeline, marked
the same day), Book I sits ~2% low, and then:

    II.7  scaffold 2,560   measured 3,094   +534  (+20.9%)
    II.8  scaffold 1,967   measured 2,377   +410  (+20.8%)

Those two were revised after being marked and the mark never moved. Anyone sizing
Book VII against Book II's "measured" length is a fifth short in its last two
chapters. The zero-delta pair is what makes this readable: without a control that
HITS, +534 is indistinguishable from a broken tool.

⚠ IT IS ALSO WHAT SAVED THIS FILE FROM ITS OWN CORRECTION. v1's raw count put
II.7 at 3,145; I saw it move, called it vandalism against curated numbers, and
reverted. The revert was RIGHT and the reasoning was WRONG — 3,145 is genuinely
uncalibrated, but the honest number is 3,094, so the thing I was protecting was
stale by 534 words and I was protecting it because it looked hand-made. Had the
crude count happened to land near 2,560 I would have shipped an uncalibrated
measure with a clean conscience. Only the control said which measure to trust.
A correction reflex that fires on MOVEMENT rather than on a known answer is not
discipline; it is conservatism with good posture.

⚠ AND THE DRAFT-LOG LINE ABOVE IS A CORRECTION TO THIS DOCSTRING'S FIRST DRAFT,
which read "32 ✅ correct — it counts as it writes." I wrote that from the naive
last-match parse, believed it, and shipped it into the file. The denominator
filter below — written to fix a false positive AGAINST the log — turned out to
exonerate nothing: the log had simply stopped emitting the global count three
chapters before the book closed. The tool refuted its own author's summary of
the tool's own first run, inside ten minutes. Left in rather than smoothed over,
because a docstring that hides having been wrong is the fifth stamp.

WHAT THIS TOOL CANNOT DO, stated plainly so the next reader does not overtrust it:

  · It counts FILES, not finished chapters. A file containing one paragraph and a
    TODO scores identically to IV.7. There is no quality claim here whatsoever —
    that is what the other twelve tools are for, and this one must not be read as
    if it borrowed their authority.
  · The scaffold's own chapter list is itself a hand-written plan. If a chapter is
    scaffolded under the wrong number, or two share one, this reports the plan's
    error as fact. It gauges the CARRIERS against disk; it cannot gauge the plan
    against intent.
  · It is a LOW-DEMAND instrument. It will be right for weeks and then matter once.
    Wire it into the drafting loop or it will rot exactly as its subjects did.

Exit code is 1 when any carrier disagrees with disk, so this cannot go quietly
green in a pipeline.

    python tools/where_the_book_is.py [--brief]
"""

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from storyscope_lite import load_prose_file, words  # noqa: E402

# ⚠ THIS IMPORT IS THE SECOND CORRECTION THIS FILE OWES ITS OWN FIRST DRAFT.
# v1 counted with `len(text.split())`, which is raw `wc -w`: it eats headings,
# table rows, horizontal rules and `**` as words. Run against the scaffold's
# existing hand-written counts it inflated II.7 from 2,560 to 3,145 (+23%) and
# II.8 from 1,967 to 2,429, and I very nearly committed those over the real ones
# — a gauge REPLACING calibrated numbers with uncalibrated ones while reporting
# itself as the cure for stamp-rot. Day 188's own lesson, verbatim: before
# measuring a property of a project that has tools/, look in tools/ — a gauge
# for that property makes an ad-hoc count not a second opinion but a worse one.
# `load_prose_file` + `words` are what every other instrument here uses.

ROOT = Path(__file__).resolve().parent.parent
BOOK = ROOT / "book"
SCAFFOLD = ROOT / "06-THE-SCAFFOLD.md"
DRAFT_LOG = BOOK / "DRAFT-LOG.md"
HANDOFF = Path("C:/Users/Wasch/carapace/Architecture/handoff/handoff.json")
WORKING_MEMORY = Path("C:/Users/Wasch/carapace/memory/working_memory.json")

# ★ ADDED DAY 189 (R-22), AND THE OMISSION IS THE POINT.
# This tool was built to end carrier rot and it excluded the STALEST CARRIER IN
# THE REPO. `00`'s STATUS block sat at "Day 185 — planning phase, no prose
# drafting until the map is done" for four days and thirty-two chapters, in the
# document that presents itself as what the project is doing. Nothing here was
# looking at it, so nothing could fail on it.
# ⚠ And note WHICH failure this closes and which it does not. A carrier slot
# catches a stale NUMBER. What was actually dangerous in `00` was a stale
# INSTRUCTION — and no gauge in this repo reads instructions. Adding `00` here
# means the next number rots loudly; it does NOT mean the next standing order
# will. Do not read a green run as "`00` is current."
ARCHITECTURE = ROOT / "00-ARCHITECTURE.md"

# ★ Day 189, R-13. The claims register's HEADING carries a range (`C1…C30`), and a heading that
# carries a range is a stamp. It has already cost a reviewer once: the Day-188 halfway letter
# reported `07` as "C1–C23, unchanged since Day 186" while the file ran to C26 and said so in its
# own title — the reader was not looking at the current file and nothing told either party.
# Counted here rather than trusted, because this is the file that exists to stop claims drifting.
REGISTER = ROOT / "07-THE-CLAIMS-REGISTER.md"
CLAIM_HEAD = re.compile(r"^###\s+\*{0,2}C(\d+)\b", re.MULTILINE)


def register_claims():
    """(declared, counted) from 07, or None if the file is absent."""
    if not REGISTER.exists():
        return None
    text = REGISTER.read_text(encoding="utf-8", errors="replace")
    m = re.search(r"CLAIMS-REGISTERED:\s*(\d+)", text)
    nums = {int(n) for n in CLAIM_HEAD.findall(text)}
    return (int(m.group(1)) if m else None), (max(nums) if nums else 0), len(nums)

BOOKS = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII"]
CHAPTER_FILE = re.compile(r"^(I|II|III|IV|V|VI|VII|VIII)-(\d{2})-.+\.md$")
SCAFFOLD_HEAD = re.compile(r"^###\s+(I|II|III|IV|V|VI|VII|VIII)\.(\d+)\s*[—-]")


def on_disk():
    """Ground truth. The only thing here that is measured rather than remembered."""
    found = {b: set() for b in BOOKS}
    counts = {b: 0 for b in BOOKS}
    for p in sorted(BOOK.glob("*.md")):
        m = CHAPTER_FILE.match(p.name)
        if not m:
            continue
        book, num = m.group(1), int(m.group(2))
        found[book].add(num)
        counts[book] += len(words(load_prose_file(p)))
    return found, counts


def planned():
    """The scaffold's chapter list, and separately its ✅ DRAFTED marks."""
    plan = {b: set() for b in BOOKS}
    marked = {b: set() for b in BOOKS}
    if not SCAFFOLD.exists():
        return plan, marked
    for line in SCAFFOLD.read_text(encoding="utf-8", errors="replace").splitlines():
        m = SCAFFOLD_HEAD.match(line)
        if not m:
            continue
        book, num = m.group(1), int(m.group(2))
        plan[book].add(num)
        if "DRAFTED" in line:
            marked[book].add(num)
    return plan, marked


def carrier_claim(path, label, total_plan):
    """
    Pull a WHOLE-BOOK 'N of M' progress claim out of a prose/JSON carrier.

    ⚠ The denominator filter is not tidiness, it is the fix for this tool's own
    first-run false positive. DRAFT-LOG.md's last 'N of M' is `10 of 10` — Book
    IV's within-book count — and the naive last-match parse reported the log as
    22 chapters wrong when the log is the ONE carrier that has been right all
    along. A progress claim is only global if its denominator is near the global
    plan; anything else is a book-local count and none of this tool's business.
    Slack of 3 because the carriers say 68 where the scaffold lists 67, which is
    a fourth stamp error too small to fail a build over and too real to hard-code.
    """
    if not path.exists():
        return None, f"{label}: MISSING at {path}"
    text = path.read_text(encoding="utf-8", errors="replace")

    # ★ THE DECLARED SLOT WINS, AND IT EXISTS BECAUSE PROSE-SCRAPING FAILED TWICE
    # IN ONE EVENING ON THE SAME MISTAKE. A carrier that CORRECTS a bad number has
    # to quote the bad number, and a correction is written after the thing it
    # corrects — so "last global claim wins" reliably returns THE ERROR from any
    # document honest enough to name it. It read DRAFT-LOG.md as 29 after the
    # correction note, and read the brand-new handoff as 41 minutes after that
    # handoff was rewritten specifically to say 32. No regex distinguishes an
    # asserted number from a quoted one; that is a real limit, not a bug to
    # cleverness away. So carriers now DECLARE:
    #
    #     CHAPTERS-DRAFTED: 32/67
    #
    # Prose stays prose. Numbers a machine must trust get a slot a machine can find.
    slot = re.findall(r"CHAPTERS-DRAFTED:\s*(\d+)\s*/\s*(\d+)", text)
    if slot:
        n, m = slot[-1]
        return (int(n), int(m)), None

    hits = [
        (int(n), int(m))
        for n, m in re.findall(r"(\d+)\s+of\s+(\d+)\s*(?:chapters?)?", text)
        if abs(int(m) - total_plan) <= 3
    ]
    if not hits:
        return None, f"{label}: makes no whole-book progress claim"
    return hits[-1], f"{label}: no CHAPTERS-DRAFTED slot — fell back to scraping prose, which reads corrections as errors"


def carrier_words(path, label):
    """
    Pull the WORD-COUNT half of a carrier's progress claim — and it is a separate
    function because for 56 chapters it was a separate, ungauged number sitting
    inside the very sentence this tool certified.

    ★ WHY THIS EXISTS (Day 190, evening). Every carrier writes the two figures
    together — "56/67 · 193,656 words" — and this tool checked the first and
    printed `✓ every carrier agrees with disk`, an unqualified sentence, directly
    beneath a word count nothing had compared to anything. Measured at three
    commits:

        c3464cc  54/67  logged 183,182  disk 183,182   ✓
        b1b9005  55/67  logged 188,754  disk 188,622   ✗ off by +132
        3ca6376  56/67  logged 193,656  disk 193,646   ✗ off by +10

    ⚠ THE FIRST DIAGNOSIS WRITTEN IN THIS DOCSTRING WAS WRONG, AND THE MEASUREMENT
    THAT KILLED IT TOOK FIVE LINES. It said both errors were one accident —
    measure, repair, publish the pre-repair number. Then the per-chapter figures
    were swept against both counting methods:

        VII.2  logged 8,376   prose 8,499   raw 8,690    neither
        VII.3  logged 5,540   prose 5,450   raw 5,568    neither
        VII.4  logged 5,572   prose 5,440   raw 5,572    RAW  ← exact
        VII.5  logged 5,137   prose 5,024   raw 5,137    RAW  ← exact

    TWO causes, not one. VII.4 and VII.5 hit raw `.split()` on the nose: those
    chapters were counted with `wc -w`, which eats headings, `**`, table rows and
    `---` as words — the exact hazard the comment at the top of this file already
    warns about. And 183,182 + 5,572 = 188,754 exactly, so the 132 is not a
    timing slip at all: it is a raw chapter figure ADDED to a gauge-true
    cumulative instead of the gauge being re-run. VII.2 and VII.3 match neither
    count, which IS the timing story — measured, then edited after.

    Four of the last five per-chapter figures are wrong, by two mechanisms, and
    the tidy single-cause story would have been committed as a comment and
    believed. Both mechanisms produce numbers that look exactly as plausible as
    the right one.

    This is the local form of a standing lesson: instruments cluster on what is
    cheap to check. Chapter count is a set of filenames — trivial. Word count
    needs the prose loader, so it went unguarded, and it is the figure that gets
    quoted to Clayton in the first line of every report.

    The slot is an EXTENSION, not a replacement — `CHAPTERS-DRAFTED: 56/67`
    still parses, so no carrier breaks by being old. Carrying no word figure is
    a problem, not a pass: an unaudited number that gets read aloud is exactly
    the state that produced the 132.
    """
    if not path.exists():
        return None, None            # the chapter-count audit already reports MISSING
    text = path.read_text(encoding="utf-8", errors="replace")
    # ⚠ The separator class is deliberately wide, and v1's was not. v1 accepted
    # `· 193,646 words` and nothing else — so it read handoff.json, which had
    # declared `56/67 (193,656w)` all along, as carrying NO word figure. A check
    # that misses the field reports "ungauged" and moves on, which is strictly
    # worse than not checking: the real +10 error was sitting in the one carrier
    # that had done the right thing, and the audit's own narrow regex hid it
    # behind a complaint about the format.
    slot = re.findall(
        r"CHAPTERS-DRAFTED:\s*\d+\s*/\s*\d+\s*[·|,;(\[]?\s*([\d,]+)\s*(?:w\b|words)", text
    )
    if not slot:
        return None, (
            f"{label}: CHAPTERS-DRAFTED carries no word figure — but the carrier "
            f"prints one in prose, so the number that gets quoted is ungauged. "
            f"Extend the slot: `CHAPTERS-DRAFTED: N/M · W words`."
        )
    return int(slot[-1].replace(",", "")), None


def status_prose(disk):
    """
    Audit the PER-BOOK prose in 00-ARCHITECTURE.md — `V (11/11), VI (8/8), VII (5/9)` —
    against disk. The declared slot is one number; this is the sentence a human
    actually reads, and until now nothing checked it.

    ★ This function is the hand for a sentence that had none. 00-ARCHITECTURE.md
    has said, since Day 189: *"A carrier check that reads one field is a
    spellcheck for that field."* It said so because the per-book line had gone
    eight chapters stale two lines under the warning about declared numbers
    rotting. The diagnosis was exactly right, it was written in the file it
    described — and it produced no instrument, so on Day 190 the same file's
    prose was fourteen chapters stale again and the gauge still said everything
    agreed.

    Only Roman-numeral book claims are read, and only where the denominator
    matches that book's planned length, so a chapter-local `(2/3)` in unrelated
    prose is not mistaken for a progress claim.

    ⚠ BACKTICKED SPANS ARE STRIPPED FIRST, and that is not tidiness — it is this
    tool's oldest lesson arriving on schedule. `carrier_claim` above exists
    because prose-scraping reads a CORRECTION as an ERROR: a document honest
    enough to name its own stale number has to quote that number, and the quote
    is written after the thing it corrects, so "last match wins" returns the
    error every time. This function was written on Day 190 and failed on its
    very first run for that reason — it flagged `V (2/11)`, which appears in
    this file only inside the Day-189 note explaining that V (2/11) was wrong.
    The repo's own convention already draws the line: a number being QUOTED goes
    in backticks, a number being ASSERTED does not. So that is the rule here.
    The cost is real and accepted — a live claim written in backticks is
    invisible to this check.
    """
    if not ARCHITECTURE.exists():
        return []
    text = ARCHITECTURE.read_text(encoding="utf-8", errors="replace")
    text = re.sub(r"`[^`]*`", " ", text)          # quoted ≠ asserted; see above
    plan, _marked = planned()
    out = []
    for b, have, want in re.findall(
        r"\b(I|II|III|IV|V|VI|VII|VIII)\s*\((\d+)\s*/\s*(\d+)\)", text
    ):
        have, want = int(have), int(want)
        if want != len(plan.get(b, ())):
            continue                      # not a book-progress claim; leave it alone
        if have != len(disk.get(b, ())):
            out.append(
                f"00-ARCHITECTURE.md prose says Book {b} ({have}/{want}), "
                f"disk says {len(disk.get(b, ()))} — the sentence a human reads, "
                f"stale under a slot that passes"
            )
    return out


CARRIER_SLOT = re.compile(
    r"(CHAPTERS-DRAFTED:\s*)(\d+)(\s*/\s*)(\d+)(\s*[·|,;(\[]?\s*)([\d,]+)(\s*(?:w\b|words))"
)


def sync_carriers(total_disk, total_plan, total_words):
    """Write the measured figures BACK into the four carriers. The hand this file
    spent four hundred lines diagnosing and never grew.

    ★ WHY THIS EXISTS, and it is this tool's own standing lesson turned on itself.
    `--sync` has existed for some time and syncs ONE thing: the scaffold's
    headings. Headings are a set of strings — cheap. The word count needs the
    prose loader, drifts on EVERY edit including the one that adds an endnote,
    and is the figure quoted aloud in the first line of every report. So the
    flag named `--sync` synced the cheap carrier and left the expensive one to be
    retyped by hand, every time, forever. *Instruments cluster on what is cheap
    to check* is written in `carrier_words`'s own docstring, forty lines up, as a
    diagnosis. This is the same sentence with a hand on it.

    ⛔ SCOPE, STATED SO IT IS NOT OVER-READ. This rewrites the numeric fields of
    the `CHAPTERS-DRAFTED:` slot and NOTHING ELSE. It does not touch the per-book
    prose in 00-ARCHITECTURE.md — `status_prose` audits that, and a sentence
    needs judgement to rewrite, not a regex. A carrier can be synced by this and
    still be flagged by that, which is correct and not a contradiction.

    Every rewrite is printed with its before and after, on the same argument the
    exclusion lists are printed on: a wrong write must be legible in the output
    on the first run, not discovered later by a number that disagrees.
    """
    for path, label in ((HANDOFF, "handoff.json"), (DRAFT_LOG, "DRAFT-LOG.md"),
                        (ARCHITECTURE, "00-ARCHITECTURE.md"),
                        (WORKING_MEMORY, "carapace working_memory.json")):
        if not path.exists():
            print(f"  ⚠ {label}: MISSING — not synced")
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        hits = list(CARRIER_SLOT.finditer(text))
        if not hits:
            print(f"  ⚠ {label}: no CHAPTERS-DRAFTED slot to sync — the audit below"
                  f" will say so too")
            continue

        # ⛔ THE LAST SLOT ONLY, and this is not a detail. DRAFT-LOG.md is a LOG:
        # it carries one CHAPTERS-DRAFTED line per entry, and the first version of
        # this function rewrote ALL of them — 60/67 and 66/67 became 67/67 and the
        # drafting history was gone, silently, in a function whose whole purpose is
        # to stop carriers lying. Caught on a COPY, by standing order, before it
        # touched a real file. `carrier_words` reads `slot[-1]`; the writer must
        # target exactly what the reader reads or the two disagree by construction.
        m = hits[-1]
        was = f"{m.group(2)}/{m.group(4)} · {m.group(6)} words"
        now = f"{total_disk}/{total_plan} · {total_words:,} words"
        if was.replace(",", "") == now.replace(",", ""):
            print(f"  · {label}: already agrees with disk")
            continue
        fixed = (f"{m.group(1)}{total_disk}{m.group(3)}{total_plan}"
                 f"{m.group(5)}{total_words:,}{m.group(7)}")
        stale = len(hits) - 1
        tail = f"   ({stale} earlier slot(s) left alone — log history)" if stale else ""
        print(f"  ✎ {label}: {was}  →  {now}{tail}")
        path.write_text(text[:m.start()] + fixed + text[m.end():], encoding="utf-8")


def sync_scaffold(disk):
    """
    Rewrite 06-THE-SCAFFOLD.md's ✅ marks FROM DISK, so they are derived rather
    than remembered.

    This exists because of Day 188's own lesson: four separate measurements of a
    broken thing produced four memory rows and zero hands, and the reason was
    never poor memory — it was that the repair path returned nothing. A gauge
    that can only complain trains its reader to scroll past it. Word counts are
    re-measured every run; the mark is never trusted, only overwritten.

    It touches ONLY the heading line, and only its trailing status. A heading
    with hand-written prose after the marker keeps that prose — the regex eats
    an existing ✅ clause and nothing else.
    """
    per_file = {}
    for p in BOOK.glob("*.md"):
        m = CHAPTER_FILE.match(p.name)
        if m:
            per_file[(m.group(1), int(m.group(2)))] = len(words(load_prose_file(p)))

    lines = SCAFFOLD.read_text(encoding="utf-8").splitlines(keepends=True)
    changed = 0
    for i, line in enumerate(lines):
        m = SCAFFOLD_HEAD.match(line)
        if not m:
            continue
        key = (m.group(1), int(m.group(2)))
        stripped = re.sub(r"\s*✅\s*DRAFTED.*$", "", line.rstrip("\n")).rstrip()
        want = (
            f"{stripped} ✅ DRAFTED — {per_file[key]:,} words"
            if key in per_file
            else stripped
        )
        if want + "\n" != line:
            lines[i] = want + "\n"
            changed += 1
    SCAFFOLD.write_text("".join(lines), encoding="utf-8")
    print(f"  synced 06-THE-SCAFFOLD.md — {changed} heading(s) rewritten from disk\n")


def main():
    brief = "--brief" in sys.argv
    disk, words = on_disk()
    if "--sync" in sys.argv:
        sync_scaffold(disk)
    plan, marked = planned()
    if "--sync" in sys.argv:
        # AFTER planned(), because sync_scaffold rewrites the file planned() reads
        # and the denominator must come from the post-sync scaffold. BEFORE the
        # audit prints, so the report below is post-sync truth rather than a
        # complaint about a file this same run just repaired.
        sync_carriers(sum(len(v) for v in disk.values()),
                      sum(len(v) for v in plan.values()),
                      sum(words.values()))
        print()

    total_disk = sum(len(v) for v in disk.values())
    total_plan = sum(len(v) for v in plan.values())
    total_marked = sum(len(v) for v in marked.values())
    total_words = sum(words.values())

    print(f"WHERE THE BOOK IS — measured from disk, {BOOK}")
    print(f"  DRAFTED: {total_disk} of {total_plan} chapters · {total_words:,} words\n")

    if not brief:
        for b in BOOKS:
            if not plan[b] and not disk[b]:
                continue
            have, want = len(disk[b]), len(plan[b])
            bar = "█" * have + "·" * max(0, want - have)
            missing = sorted(plan[b] - disk[b])
            extra = sorted(disk[b] - plan[b])
            note = ""
            if missing:
                note += f"  missing {','.join(str(x) for x in missing)}"
            if extra:
                note += f"  ⚠ ON DISK, NOT IN PLAN: {','.join(str(x) for x in extra)}"
            print(f"  Book {b:<4} {have:>2}/{want:<2} {bar:<12} {words[b]:>7,}w{note}")
        print()

    # --- the part that is the point: audit every carrier against disk ---
    problems = []

    if total_marked != total_disk:
        lag = sorted(
            f"{b}.{n}" for b in BOOKS for n in (disk[b] - marked[b])
        )
        problems.append(
            f"06-THE-SCAFFOLD.md ✅ marks say {total_marked}, disk says {total_disk} "
            f"(off by {total_marked - total_disk:+d})\n"
            f"      unmarked but written: {', '.join(lag) if lag else '(none)'}"
        )

    for path, label in (
        (HANDOFF, "handoff.json"),
        (DRAFT_LOG, "DRAFT-LOG.md"),
        (ARCHITECTURE, "00-ARCHITECTURE.md"),  # R-22, Day 189
        # Day 190 evening. Found holding "32/67 — 94,486 words, V-VIII unstarted" —
        # 24 chapters stale, the FOURTH carrier caught with that rot in one sitting.
        # Added the same hour it was found, because the lesson being written up in
        # that same hour was that a diagnosis without a hand changes nothing.
        (WORKING_MEMORY, "carapace working_memory.json"),
    ):
        claim, err = carrier_claim(path, label, total_plan)
        # A missing slot is a warning AND the scraped number still gets checked —
        # v1 returned early on any `err` and so stopped auditing the moment it had
        # something to complain about, which is the failure it was built to catch.
        if err:
            problems.append(err)
        if claim and claim[0] != total_disk:
            problems.append(
                f"{label} claims {claim[0]} of {claim[1]}, disk says {total_disk} "
                f"(off by {claim[0] - total_disk:+d})"
            )

        # The other half of the same sentence — see carrier_words. Exact, no slack:
        # both sides are computed by the same prose loader, so any gap is a stamp
        # taken before the last repair, which is precisely the 132.
        wclaim, werr = carrier_words(path, label)
        if werr:
            problems.append(werr)
        if wclaim is not None and wclaim != total_words:
            problems.append(
                f"{label} claims {wclaim:,} words, disk says {total_words:,} "
                f"(off by {wclaim - total_words:+,d}) — check BOTH known causes: a "
                f"raw `wc -w` count added to a gauge-true cumulative, or a figure "
                f"measured before the last edit. Re-run this tool; do not hand-add."
            )

    problems.extend(status_prose(disk))

    reg = register_claims()
    if reg:
        declared, highest, count = reg
        if declared is None:
            problems.append(
                "07-THE-CLAIMS-REGISTER.md: no CLAIMS-REGISTERED slot — the heading's range "
                "is a stamp with nothing behind it, which is the state that misled a reviewer."
            )
        elif declared != highest:
            problems.append(
                f"07-THE-CLAIMS-REGISTER.md declares {declared}, highest C-heading is C{highest} "
                f"({count} rows). The title and the file disagree."
            )
        elif not brief:
            print(f"  CLAIMS: C1…C{highest} · {count} rows · declared {declared} ✓\n")

    # ---- 08-THE-INSTRUMENTS.md, same discipline, same reason (R-91, Day 190). A register
    # that only its own dedicated tool checks is a register nothing checks, because the tool
    # gets run on the day it is written and then not again. This is the instrument every
    # planning decision already consults, so the slot rides here too.
    instruments = ROOT / "08-THE-INSTRUMENTS.md"
    if instruments.exists():
        itext = instruments.read_text(encoding="utf-8", errors="replace")
        m = re.search(r"INSTRUMENTS-REGISTERED:\s*(\d+)", itext)
        headings = len(re.findall(r"^## I\d+ ", itext, re.M))
        if not m:
            problems.append(
                "08-THE-INSTRUMENTS.md: no INSTRUMENTS-REGISTERED slot — the heading's range "
                "is a stamp with nothing behind it."
            )
        elif int(m.group(1)) != headings:
            problems.append(
                f"08-THE-INSTRUMENTS.md declares {m.group(1)} instruments, "
                f"{headings} I-headings present. The title and the file disagree."
            )
        elif not brief:
            print(f"  INSTRUMENTS: I1…I{headings} · declared {m.group(1)} ✓")
            print("    ⛔ forward bindings live from VII.3 — run tools/instrument_sweep.py\n")

    # ---- ruling 117's trigger. It ordered a gauge; a gauge nobody runs is a
    # stamp. So the one instrument every planning decision already consults
    # carries the ratio, and the debt cannot go quiet again. (R-65, Day 190.)
    if not brief:
        try:
            import endnote_debt as _ed
            src, cov, _notes = _ed.book_totals()
            flag = "  ⚠ ruling 9's second half" if cov < src else "  ✓"
            print(f"  ENDNOTES: {cov}/{src} sources carry a receipt{flag}"
                  f"   (tools/endnote_debt.py — ±, see its LIMIT line)\n")
        except Exception as exc:                      # never block the count
            print(f"  ENDNOTES: gauge unavailable — {exc}\n")

    if problems:
        print("⚠ CARRIERS DISAGREEING WITH DISK — the stamp is not the gauge:")
        for p in problems:
            print(f"   ✗ {p}")
        print(
            "\n   Both directions matter. A carrier that OVER-reports makes the next\n"
            "   breath think there is less left than there is; one that UNDER-reports\n"
            "   sends it to write a chapter that already exists."
        )
        return 1

    print("✓ every carrier agrees with disk.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
