#!/usr/bin/env python3
"""
RELEASE GATES — the six conditions that block upload, and the two that are RUN rather than read.

WHY THIS IS ITS OWN FILE AS OF DAY 195 NIGHT. The gate list used to live inside `queue_state.py`,
which was a 6,391-line-queue analyser that happened to also check gates. When Clayton retired that
queue, the analyser's subject became an ARCHIVE — and a gate that reads archived text is a defect
this project has already paid for once: a release condition blocked on a passage that had been
retired, because the retirement was honoured in one pass and not the other.

⛔ **SO THE RULE IS EXPLICIT AND MECHANICAL: NOTHING IN THIS FILE READS THE ARCHIVE.** The gate
table is read from the LIVE queue; the measured gates run their own tools against the LIVE book.
`queue_state.py` still exists and is now archive-only by construction.

TWO KINDS OF GATE, AND THE DIFFERENCE IS THE WHOLE POINT.

  DECLARED   a human wrote "discharged" in the table. That is a claim, and this file reports it as
             a claim. It is not evidence and is not upgraded by being repeated.
  MEASURED   a tool is executed and its EXIT CODE is the verdict. `self_citation_gate.py` returns
             2 when its own positive control fails, and that is reported as UNKNOWN — never folded
             into either answer, because a zero from a detector that has stopped detecting is the
             exact failure the whole family exists to prevent.

  usage:  python tools/release_gates.py
  exit:   0 = every gate met · 1 = a gate is open · 2 = a gate's own control failed (UNKNOWN)
"""

import os
import re
import sys
import subprocess

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
QUEUE = os.path.join(ROOT, "book", "docs", "REVISION-QUEUE.md")
ARCHIVE_DIR = os.path.join(ROOT, "book", "docs", "archive")

# gate row id -> tool whose exit code IS the verdict. Everything else is DECLARED.
# The value is an ARGV TAIL, not just a filename, because R-240's verdict lives behind
# a flag: `bibliography.py` with no argument REWRITES the page, which would make the
# gate pass by doing the work rather than by finding it done. A gate that repairs its
# own subject is not a gate. [[feedback_instrument_fix_vs_relaxation]]
MEASURED = {
    "R-238": ["self_citation_gate.py"],
    # R-240, added Day 205 under R2-074. `bibliography.py` had NO CALLER anywhere in
    # the repo for ten days, so the works-cited page shipped current only when someone
    # remembered. It drifted TWICE IN ONE DAY: once before R2-053 regenerated it, and
    # again within hours, when the Book-VIII repairs made one more citation parseable
    # and nothing said so. `book/compile_pdf.py` now regenerates before it renders;
    # this gate is the second hand, and it is the one that fires without a build.
    # [[feedback_delegated_step_has_no_trigger]]
    "R-240": ["bibliography.py", "--check"],
}


def read_gate_table():
    """The `| n | gate | R-nnn | state |` rows out of the live queue's gate table."""
    rows = []
    for line in open(QUEUE, encoding="utf-8").read().split("\n"):
        m = re.match(r"^\|\s*(\d+)\s*\|\s*(.*?)\s*\|\s*\*?\*?(R-\d+)\*?\*?\s*\|\s*(.*?)\s*\|\s*$",
                     line)
        if m:
            rows.append((int(m.group(1)), m.group(2), m.group(3), m.group(4)))
    return rows


def run_tool(argv):
    if isinstance(argv, str):           # tolerate the single-name form
        argv = [argv]
    p = subprocess.run([sys.executable, os.path.join(ROOT, "tools", argv[0])] + argv[1:],
                       capture_output=True, text=True, encoding="utf-8", errors="replace")
    return p.returncode


def main():
    # ⚠ POSITIVE CONTROL ON THE SOURCE, NOT ON THE LOGIC. The one way this file can lie
    # quietly is by reading the wrong queue — the retired one still contains every gate
    # row, so pointing at it would produce a perfectly plausible green over dead text.
    # Assert the live path and assert it is NOT inside the archive directory.
    if not os.path.exists(QUEUE):
        print(f"⛔ no live queue at {QUEUE}")
        return 2
    if os.path.abspath(QUEUE).startswith(os.path.abspath(ARCHIVE_DIR)):
        print("⛔ the gate table resolved INTO the archive. Refusing to report.")
        return 2
    print(f"RELEASE GATES — read from {os.path.relpath(QUEUE, ROOT)}")
    print(f"  (archive at {os.path.relpath(ARCHIVE_DIR, ROOT)} is NOT read by this file)\n")

    rows = read_gate_table()
    if not rows:
        print("⛔ no gate table found in the live queue. Refusing to report a green over")
        print("   an absent table — an empty result and a met condition are different things.")
        return 2

    open_gates, unknown = 0, 0
    for num, gate, rid, state in rows:
        if rid in MEASURED:
            rc = run_tool(MEASURED[rid])
            label = " ".join(MEASURED[rid])
            if rc == 0:
                verdict = f"✅ MET      — {label} exit 0, RUN not read"
            elif rc == 2:
                verdict = f"❓ UNKNOWN  — {label} control failed; verdict withheld"
                unknown += 1
            else:
                verdict = f"⛔ OPEN     — {label} exit {rc}"
                open_gates += 1
        elif "discharged" in state or "met" in state.lower():
            verdict = "◻ DECLARED — a human wrote this; it is a claim, not evidence"
        else:
            verdict = "⛔ OPEN"
            open_gates += 1
        print(f"  {num}. {rid:<7s} {verdict}")
        print(f"     {gate}")

    print()
    if unknown:
        print(f"VERDICT WITHHELD — {unknown} gate(s) could not be measured.")
        return 2
    if open_gates:
        print(f"⛔ {open_gates} gate(s) OPEN — upload is blocked.")
        return 1
    print("✅ every gate met or declared. ⚠ DECLARED is not MEASURED: only the rows marked")
    print("   RUN not read were checked against the book tonight. The rest are on the record")
    print("   of whoever wrote them.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
