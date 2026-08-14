#!/usr/bin/env python3
"""
QUEUE STATE  —  Truth and Consequences, Day 195.

THE FILE THAT ANSWERS "WHAT DOES THIS BOOK OWE?" COULD NOT ANSWER IT.

REVISION-QUEUE.md opens by declaring itself the authority on what is outstanding
and when it comes due. It is 5,596 lines and it is hand-kept, and asked the flat
question it exists to answer, it required a human to read all of it.

Its own Day-195 tail filed this gauge as "the next thing to build" and then did
not build it, on the correct grounds that the consolidation Clayton asked for
should not be swallowed by a tooling detour. This is that thing, built the next
morning, because a release gate that cannot be checked is a wish.

WHAT IT FOUND ON ITS FIRST RUN — the reason it is not a formatting exercise:

    R-2 IS DEAD AS A FINDING AND ALIVE AS A CLOCK.

    R-2 says "Endnotes. There are none. Zero markers and zero files exist
    across twenty-one chapters -- not one receipt." Measured against the
    shipped files: 531 note definitions across 62 of 69 chapters.

    That is the easy half. The hard half is that TWENTY-THREE other rows
    carry a trigger that names R-2 -- "TRIGGER: R-2, Book VII."
    R-2 was not only the largest debt in the book, it was the SCHEDULER.

    So the endnote pass ran, book by book, and every one of those triggers
    FIRED -- silently, with nothing watching, because the row that would
    have announced the firing was the row describing a world where the
    pass had not started. Those 23 rows are not pending. They are OVERDUE,
    and they have been overdue for days.

    Striking R-2 as "premise falsified" without moving its dependents is
    how you turn 23 tracked debts into 23 untracked ones in a single edit.
    That is the failure this project has a name for: a mechanism with no
    trigger, which is what a trigger pointing at a dead row becomes.

    AND R-2 IS NOT THE ONLY DEAD GATE. Three PAID rows -- R-69 (2),
    R-71 (2), R-13 (1) -- carry five more dangling clauses between them.
    Those did not need a falsification to strand their dependents; being
    PAID was enough. 28 dangling clauses in total.

HOW MANY OF THIS TOOL'S OWN NUMBERS WERE WRONG BEFORE THE CONTROL RAN: three.

    It printed 23, then 20, then 24, then 23 -- and only the last is
    trustworthy, because only the last survived a positive control that
    re-homed one real trigger and watched the total fall to 22 and come
    back. The three wrong counts came from (1) a line-scoped regex over
    HARD-WRAPPED prose, (2) this file's own row about the triggers being
    counted as triggers, and (3) a fixed-width window bleeding into the
    next row. Each looked exactly as authoritative as the right one.

    THE CONTROL IS THE ONLY REASON ANY OF THAT SURFACED. A gauge whose
    alarm you have never watched MOVE is a gauge you have not tested --
    and the first control written here was itself void: it edited a string
    that did not exist, asserted nothing, and "passed."

WHAT IT DOES

    * enumerates every R-nnn in the file, with the line it first appears on
    * splits them: OPEN table (the part anyone actually reads) vs prose-only
    * reads dispositions from the file's own idioms -- ~~**R-n**~~ = paid,
      "CLOSED -- R-n", "PREMISE FALSIFIED"
    * resolves TRIGGER clauses that name another row, and reports any whose
      gate row is discharged: those are FIRED-UNOBSERVED
    * checks the release gate: the named ship-condition rows, and whether
      each is still open

LIMIT -- stated because this tool's whole subject is unverifiable bookkeeping:

    IT READS DECLARATIONS, NOT THE BOOK. A row marked paid by a sentence
    that has since rotted reads paid here. A row whose finding was falsified
    by the world -- exactly R-2 -- reads OPEN until a human writes the
    falsification down. This gauge makes the queue's SHAPE checkable. It
    cannot make the queue TRUE, and the day it appears to is the day it has
    started lying in a new way.

    It also cannot see a debt that was never rowed. The queue's own header
    says it: an item absent from this list is unrecorded, not discharged.

usage:  python tools/queue_state.py [--gate] [--triggers] [--verbose]
"""

from __future__ import annotations

import re
import sys
from collections import Counter
from pathlib import Path

QUEUE = Path(__file__).resolve().parent.parent / "book" / "docs" / "REVISION-QUEUE.md"

# The rows named as the publication gate (Day 195 ruling). Everything else in
# the queue is a maintenance backlog and explicitly does NOT block release.
RELEASE_GATE = ["R-212", "R-228", "R-216", "R-222", "R-234"]

ROW_RE = re.compile(r"\bR-(\d+)(\([a-z]\))?\b")
OPEN_TABLE_ROW = re.compile(r"^\|\s*(~~)?\*\*(R-[\w()]+)\*\*")


def load() -> list[str]:
    if not QUEUE.exists():
        sys.exit(f"queue not found: {QUEUE}")
    return QUEUE.read_text(encoding="utf-8").split("\n")


def open_table_bounds(lines: list[str]) -> tuple[int, int]:
    """The OPEN table runs from the '## OPEN' heading to the next '---' after it."""
    start = next(i for i, l in enumerate(lines) if l.strip() == "## OPEN")
    for i in range(start + 3, len(lines)):
        if lines[i].strip() == "---":
            return start, i
    return start, len(lines)


def analyse(lines: list[str]) -> dict:
    text = "\n".join(lines)
    lo, hi = open_table_bounds(lines)

    first_line: dict[str, int] = {}
    for i, l in enumerate(lines, 1):
        for m in ROW_RE.finditer(l):
            rid = "R-" + m.group(1)
            first_line.setdefault(rid, i)

    in_open_table: set[str] = set()
    for l in lines[lo:hi]:
        m = OPEN_TABLE_ROW.match(l)
        if m:
            in_open_table.add(re.sub(r"\([a-z]\)", "", m.group(2)))

    # Same declaration-site rule as falsified, for the same reason.
    paid: set[str] = set()
    for l in lines:
        m = re.match(r"\|\s*~~\*\*(R-\d+)[\w()]*\*\*~~(.{0,120})", l)
        if m and not re.search(r"PREMISE FALSIFIED|WITHDRAWN|SUPERSEDED", m.group(2)):
            paid.add(m.group(1))
        m2 = re.match(r"\**CLOSED\s*[-—]+\s*(R-\d+)", l.strip())
        if m2:
            paid.add(m2.group(1))

    # ⚠ A DISPOSITION MUST BE READ AT A DECLARATION SITE, NOT BY PROXIMITY.
    # First version of this matched "PREMISE FALSIFIED" within 120 chars of any
    # R-nnn anywhere in 5,700 lines. R-234 — the row whose entire subject is
    # R-2's falsification, and which is a RELEASE GATE — therefore reported
    # itself DISCHARGED, while the same run printed the 23 dangling triggers
    # that prove it is not. The gauge rendered its own good news and the alarm
    # branch was the broken one. A row is falsified only where it is STRUCK:
    # ~~**R-n**~~ and the verdict on the SAME LINE, which is a declaration.
    # ...and the site is the VERDICT IMMEDIATELY AFTER the strikethrough, not
    # the whole line. These table lines run 400+ chars; scanning all of one
    # made R-58 ("PAID Day 189 night") read FALSIFIED off a word buried deep in
    # its body prose. Bound the window to the declaration itself.
    falsified: set[str] = set()
    for l in lines:
        m = re.match(r"\|\s*~~\*\*(R-\d+)[\w()]*\*\*~~(.{0,120})", l)
        if m and re.search(r"PREMISE FALSIFIED|WITHDRAWN|SUPERSEDED", m.group(2)):
            falsified.add(m.group(1))

    # Trigger dependencies: a TRIGGER clause naming some other row.
    #
    # ⚠ TWO WAYS THIS MISCOUNTED, BOTH FOUND BY A POSITIVE CONTROL THAT
    # RE-HOMED ONE TRIGGER AND WATCHED THE TOTAL NOT MOVE:
    #  (1) `TRIGGER` without a colon matched the PROSE "23 TRIGGER CLAUSES IN
    #      THIS FILE NAME R-2 AS THEIR GATE" — a sentence about triggers
    #      counted as a trigger. Require the colon.
    #  (2) R-234 QUOTES the clauses it describes, so writing the row that
    #      reports the count ADDED to the count. The act of recording
    #      invalidated the record. Quoted examples are `*"TRIGGER: …"*` —
    #      skip any clause opening inside a quotation.
    # Both are the same shape: a gauge that cannot tell its subject from a
    # description of its subject. [[feedback_recording_act_invalidates_record]]
    #  (3) AND THE ONE THAT MATTERED MOST: this file is HARD-WRAPPED prose at
    #      ~100 columns, and the clause regex was LINE-SCOPED (`[^\n]`). Every
    #      trigger whose gate name fell past a line break was invisible — the
    #      clause was truncated at the newline before the `R-2` was reached.
    #      Both of the first two counts this tool printed (23, then 20) were
    #      UNDERCOUNTS produced this way, and the positive control is what
    #      exposed it: re-homing a trigger moved nothing, because the string I
    #      thought I was editing did not exist on one line.
    #      Scan a whitespace-flattened copy. [[feedback_line_scoped_grep_over_wrapped_prose]]
    flat = re.sub(r"\s+", " ", text)
    triggers: list[tuple[str, str, str]] = []  # (dependent, gate, clause)
    for m in re.finditer(r"TRIGGER(?:S)?(?::|\s+FOR\b).{0,240}", flat):
        if flat[max(0, m.start() - 2) : m.start()] == '*"':
            continue  # quoted example, not a live trigger
        # (4) …and the window has to STOP AT THE ROW BOUNDARY. A flat 240 chars
        # bleeds into the next row's heading, so R-234's own trigger ("★ RELEASE
        # GATE 5 — before upload") inherited an R-2 from the row below it and
        # reported itself as its own dependent. Cut at the first `---`, `**FILED`
        # or `## ` — the file's own row separators.
        # (5) TWO MORE SEPARATORS, Day 195, and this is an INSTRUMENT FIX AND NOT
        #     A RELAXATION — the distinction is the whole of it, so here is the
        #     fixture where the two differ. `### R-nn` (a new row heading) and
        #     `✅ **R-nn — DISCHARGED` (a discharge declaration) both END a row
        #     as surely as `---` does, and the window was reading past them into
        #     the NEXT row's identifier. Three clauses whose own text is live
        #     ("before VI.4 is drafted", "with R-67's second half") were being
        #     reported as orphaned by their neighbours' names. Narrowing the
        #     window to the clause's true extent REMOVES FALSE POSITIVES ONLY;
        #     a relaxation would have been widening the ignore-list or dropping
        #     PAID gates from the check, and neither is done here. Positive
        #     control run the same minute: a trigger deliberately re-pointed at
        #     a PAID row is still caught after the fix.
        #     [[feedback_instrument_fix_vs_relaxation]] · [[feedback_zero_needs_a_positive_control]]
        clause = re.split(r"\s---\s|\*\*FILED|\s## |\s### |✅ \*\*R-\d+ — ", m.group(0))[0]
        gates = {"R-" + g for g in re.findall(r"\bR-(\d+)\b", clause)}
        if not gates:
            continue
        # attribute the clause to the row whose section it sits in
        head = text.rfind("R-", 0, m.start() - 1)
        owner = None
        seg = flat[max(0, m.start() - 3000) : m.start()]
        owners = re.findall(r"(?:FILED|CLOSED|^##)\s*[-—]*\s*(R-\d+)", seg, re.M)
        if owners:
            owner = owners[-1]
        for g in gates:
            if g != owner:
                triggers.append((owner or "?", g, clause.strip()))

    return {
        "first_line": first_line,
        "open_table": in_open_table,
        "paid": paid,
        "falsified": falsified,
        "triggers": triggers,
        "bounds": (lo + 1, hi + 1),
    }


def main() -> None:
    lines = load()
    a = analyse(lines)
    all_rows = set(a["first_line"])
    paid = a["paid"] & all_rows
    fals = a["falsified"] & all_rows
    live = all_rows - paid - fals

    def key(r: str) -> int:
        return int(r.split("-")[1])

    print("QUEUE STATE — book/docs/REVISION-QUEUE.md")
    print(f"  file            : {len(lines)} lines")
    print(f"  OPEN table      : lines {a['bounds'][0]}–{a['bounds'][1]}")
    print()
    print(f"  distinct row IDs: {len(all_rows)}")
    print(f"    declared paid : {len(paid)}")
    print(f"    falsified     : {len(fals)}  {sorted(fals, key=key) or ''}")
    print(f"    LIVE          : {len(live)}")
    print()
    intable = a["open_table"]
    prose_only = sorted(live - intable, key=key)
    print(f"  live rows in the OPEN table : {len(live & intable)}")
    print(f"  live rows in PROSE ONLY     : {len(prose_only)}"
          f"   <-- invisible to anyone reading the table")

    # numbering holes
    nums = sorted(key(r) for r in all_rows)
    holes = [n for n in range(1, max(nums) + 1) if n not in set(nums)]
    print(f"  numbering holes             : {len(holes)}  {holes}")
    print()

    # --- trigger analysis: the point of the tool -------------------------
    fired = [(d, g, c) for (d, g, c) in a["triggers"] if g in paid or g in fals]
    if fired:
        by_gate = Counter(g for _, g, _ in fired)
        print("★ TRIGGERS WHOSE GATE ROW IS NO LONGER LIVE — these have FIRED, "
              "and nothing announced it:")
        for g, n in by_gate.most_common():
            state = "FALSIFIED" if g in fals else "PAID"
            print(f"    gate {g} ({state}) holds {n} dependent trigger clause(s)")
        print("    → these rows are OVERDUE, not pending. Re-home each trigger "
              "before striking its gate.")
    else:
        print("no trigger clause points at a discharged row.")
    print()

    print("RELEASE GATE (Day 195 ruling) — these block upload; nothing else does:")
    for r in RELEASE_GATE:
        # ⚠ GATE 5 IS NOT READ FROM ITS OWN DECLARATION. R-234's test is
        # "zero triggers point at a discharged row" — so it is answered by the
        # measurement above, not by a sentence in the row. A gate whose only
        # evidence is its own prose is satisfiable by writing prose.
        if r == "R-234":
            if fired:
                print(f"    {r:8s} ◻ OPEN   ({len(fired)} trigger clause(s) still "
                      f"point at a dead row — MEASURED, not declared)")
            else:
                print(f"    {r:8s} ✅ met    (0 dangling triggers — measured)")
            continue
        if r not in all_rows:
            print(f"    {r:8s} ❓ NOT PRESENT IN THE FILE")
        elif r in paid or r in fals:
            print(f"    {r:8s} ✅ discharged")
        else:
            loc = a["first_line"][r]
            tbl = "in OPEN table" if r in intable else "PROSE ONLY"
            print(f"    {r:8s} ◻ OPEN   (line {loc}, {tbl})")
    remaining = len(live) - sum(1 for r in RELEASE_GATE if r in live)
    print(f"\n  maintenance backlog, explicitly NOT a publication gate: {remaining} live rows")

    print()
    print("LIMIT: this reads DECLARATIONS, not the book. A row whose finding the")
    print("world has falsified reads OPEN here until a human writes that down —")
    print("which is exactly how R-2 sat at the top of the table for seven days.")

    if "--triggers" in sys.argv:
        print("\n--- every trigger clause naming another row ---")
        for d, g, c in sorted(a["triggers"], key=lambda x: key(x[1])):
            mark = "FIRED" if (g in paid or g in fals) else "     "
            print(f"  [{mark}] {d:7s} waits on {g:7s} :: {c[:120]}")


if __name__ == "__main__":
    main()
