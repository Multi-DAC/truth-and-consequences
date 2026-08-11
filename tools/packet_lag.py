#!/usr/bin/env python3
"""
PACKET LAG  —  Truth and Consequences, Day 191.

WHEN AN OUTSIDE READ COMES BACK, "ALREADY KNEW THAT" IS A CLAIM ABOUT A CLOCK,
AND I HAVE BEEN SETTLING IT FROM MEMORY WHILE THE CLOCK SAT ON DISK.

`PACKET-003` opens with **State: `fd37971`**. Every packet since has declared the
commit it was cut from. That field is the whole apparatus for deciding whether a
reviewer's finding is REDUNDANT (the row was already in the queue they were handed)
or LAG (I filed the row *after* they started, so they could not possibly have seen
it, and their finding is INDEPENDENT CORROBORATION). Nothing has ever read it.

WHAT THAT COST, MEASURED, ON THE READ THAT PROMPTED THIS FILE. The whole-volume
outside read was adjudicated in `11ad140` at **16:05:54** on Day 191. Its packet
header says "Most of its findings are re-reports" and enumerates seven. Their
filing commits:

    R-3     7158635   2026-08-07            genuinely prior
    R-120   560287b   2026-08-10  earlier same day
    R-124   560287b   2026-08-10  earlier same day
    R-127   9a6bd30   2026-08-10  15:38:13   —  27 minutes before
    R-128   9a6bd30   2026-08-10  15:38:13   —  27 minutes before
    R-132   9290458   2026-08-10  15:51:24   —  14 minutes before

Nobody reading sixty-seven chapters was handed a queue containing rows filed
fourteen minutes earlier. Three of the seven were structurally unknowable to that
reader and were logged as duplicates of my own work anyway. The headline read
"4 of 11 novel"; decomposed against the clock it is closer to 9 of 11, and the
error ran in the direction where I already knew.

⚠ THE FAILURE IS NOT GENEROSITY, IT IS A SIGN CONVENTION. Simultaneous independent
derivation is the STRONGEST corroboration available — this queue says so itself
about R-128/R-129 ("one witness, twice", weighted down for exactly this reason).
Applied to two readers converging inside one hour, the same rule got run backwards:
concurrency was scored as the reviewer FOLLOWING me, when the timestamps prove they
could not have. A rule that discounts a correlated witness must first establish
that the correlation had a channel.

FOUR LIMITS, stated because a clean run here must not imply the read was good:

 1. IT CLASSIFIES TIMING, NOT MERIT. A row filed before the snapshot may still be a
    finding the reviewer reached independently; git cannot see that. LAG is proof of
    independence; REDUNDANT is only ABSENCE of proof, never evidence of copying.
 2. IT NEEDS THE MAPPING. Which R-row a reviewer's finding corresponds to is a
    judgement I make by hand. This file audits the clock, not the correspondence.
 3. A PACKET WITH NO DECLARED STATE IS UNKNOWABLE, AND SAYS SO. It is not scored
    as clean. `--strict` exits nonzero on any such packet, because the whole point
    is that a missing snapshot destroys the statistic rather than degrading it.
 4. FIRST-APPEARANCE IS `git log -S` ON THE QUEUE FILE ONLY. A row discussed in a
    log entry or a chapter before it was filed will date from its queue filing.
    That is the intended semantics — the queue is what a packet ships.

Usage:
    python tools/packet_lag.py --state fd37971 R-3 R-120 R-127 R-132 R-136
    python tools/packet_lag.py --packet review/PACKET-003-day190-book-VI.md R-3 R-136
    python tools/packet_lag.py --selftest        two known answers, opposite signs
"""
import re
import sys
import pathlib
import subprocess

HERE = pathlib.Path(__file__).resolve().parent
REPO = HERE.parent
QUEUE = "book/REVISION-QUEUE.md"

STATE = re.compile(r"State:\s*`([0-9a-f]{7,40})`")
ROW = re.compile(r"^R-\d+$")


def git(*args):
    r = subprocess.run(["git", "-C", str(REPO), *args],
                       capture_output=True, text=True, errors="replace")
    return r.returncode, r.stdout.strip()


def first_filing(row):
    """The commit that INTRODUCED this row's token into the queue file.

    `git log -S` reports every commit that changed the token's occurrence count;
    the oldest of those is the filing. Returns (sha, iso-date) or (None, None) —
    a row that never appears is reported, not silently treated as ancient.
    """
    code, out = git("log", "--format=%H %cI", "-S", row, "--", QUEUE)
    if code or not out:
        return None, None
    sha, _, date = out.splitlines()[-1].partition(" ")
    return sha, date.strip()


def classify(row, state):
    sha, date = first_filing(row)
    if sha is None:
        return row, "MISSING", None, "never appears in the queue"
    code, _ = git("merge-base", "--is-ancestor", sha, state)
    if code == 0:
        return row, "REDUNDANT", date, "in the queue the reviewer was handed"
    return row, "LAG", date, "filed after the snapshot — could not have been seen"


def resolve_state(argv):
    if "--state" in argv:
        return argv[argv.index("--state") + 1], "--state"
    if "--packet" in argv:
        p = pathlib.Path(argv[argv.index("--packet") + 1])
        if not p.is_absolute():
            p = REPO / p
        m = STATE.search(p.read_text(encoding="utf-8", errors="ignore"))
        if not m:
            print(f"  ⚠ {p.name} DECLARES NO STATE. Not clean — unknowable.")
            print("    A packet without a snapshot cannot be scored for lag at all;")
            print("    every 're-report' against it is an unfalsifiable claim.")
            sys.exit(2)
        return m.group(1), p.name
    return None, None


def selftest():
    """Two known answers with opposite signs, against PACKET-003's declared state.

    R-3   was filed 2026-08-07, before `fd37971` (Day 190)  -> must be REDUNDANT.
    R-136 was filed 2026-08-10, after  `fd37971`            -> must be LAG.

    A gauge that can only confirm the reading I want is not a gauge. If either of
    these flips, the ancestry logic is inverted and every report is worthless.
    """
    state = "fd37971"
    ok = True
    for row, want in (("R-3", "REDUNDANT"), ("R-136", "LAG")):
        _, got, date, _ = classify(row, state)
        mark = "OK " if got == want else "FAIL"
        if got != want:
            ok = False
        print(f"  [{mark}] {row:<6} expected {want:<9} got {got:<9} (filed {date})")
    print("\n  " + ("both controls hit — ancestry logic sound."
                    if ok else "CONTROL FAILED — do not trust any report from this file."))
    return 0 if ok else 1


def main():
    argv = sys.argv[1:]
    if "--selftest" in argv:
        return selftest()

    state, source = resolve_state(argv)
    rows = [a for a in argv if ROW.match(a)]
    if not state or not rows:
        print(__doc__.strip().splitlines()[-5])
        print("  need a snapshot (--state SHA | --packet FILE) and at least one R-row.")
        return 2

    code, resolved = git("rev-parse", "--short", state)
    if code:
        print(f"  ⚠ snapshot {state!r} is not a commit in this repo.")
        return 2

    results = [classify(r, state) for r in rows]
    lag = [r for r in results if r[1] == "LAG"]
    red = [r for r in results if r[1] == "REDUNDANT"]
    missing = [r for r in results if r[1] == "MISSING"]

    print(f"PACKET LAG — was the reviewer able to see it, or did I file it after they started?")
    print(f"  snapshot  : {resolved}  (from {source})")
    print(f"  rows      : {len(results)}\n")
    for row, verdict, date, why in results:
        print(f"  {verdict:<10} {row:<7} {date or '—':<26} {why}")

    print(f"\n  REDUNDANT {len(red)}  ·  LAG {len(lag)}  ·  MISSING {len(missing)}")
    if lag:
        print(f"\n  ⚠ {len(lag)} finding(s) could NOT have been seen by this reviewer.")
        print("    Those are independent corroboration, not duplication. Do not")
        print("    discount them for agreeing with a row they were never shown.")
    if missing:
        print(f"\n  ⚠ {len(missing)} row(s) never appear in the queue — check the mapping.")
    return 1 if (lag or missing) else 0


if __name__ == "__main__":
    sys.exit(main())
