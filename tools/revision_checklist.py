#!/usr/bin/env python3
"""
Read the D204 revision checklist and report what is open, what is done, and — with --verify —
whether a ticked box is actually true of the manuscript.

WHY THIS EXISTS. The checklist it reads was promoted from a read whose headline number ("41
proposed moves") was a count of arrow GLYPHS, not of proposals. Every tally in this project that
was carried in prose has been wrong at least once. So the file carries the rows and this reads the
count off it; nothing types a total.

THE ONE NON-OBVIOUS THING: matching is done on the PARAGRAPH-UNWRAPPED source. The manuscript is
hard-wrapped at ~95 columns, so a phrase can straddle a newline and a line-scoped grep will report
it ABSENT when it is present. Six of the first eighteen anchors written into the checklist came
back MISS for that reason and every one of them was there. That is R2-075's defect, in the tool
that was built to audit R2-075.

WHAT THIS CANNOT DO, stated because a green here is narrower than it looks:
  * `ruling:` and `manual:` rows are NOT machine-decidable and are never auto-verified. They are
    reported in their own bucket. A run with 20 manual rows ticked has verified NOTHING about them.
  * An `absent:` check going green means the defect STRING is gone. It does not mean the
    replacement is right, or that the surrounding sentence still parses.
  * It reads the markdown, not the PDF. A row can be true of the source and false of the book —
    which is exactly how the "standing note above" repair was filed wrongly and withdrawn.

USAGE
  python tools/revision_checklist.py                 counts + the open list
  python tools/revision_checklist.py --verify        run every machine check; flag divergence
  python tools/revision_checklist.py --group C       one group
  python tools/revision_checklist.py --open          open rows only, terse
"""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
CHECKLIST = REPO / "book" / "docs" / "REVISION-CHECKLIST-D204.md"
BOOK = REPO / "book"

ROW_RE = re.compile(r"^- \[( |x|X)\] \*\*(R2-\d+)\*\*(.*)$")
SUB_RE = re.compile(r"^\s+- \[( |x|X)\] (.*)$")
GROUP_RE = re.compile(r"^## ([A-H]) — (.*)$")
CHECK_RE = re.compile(r"`✓`\s*(\w+):(.*)$")
TABLE_RE = re.compile(r"^\| \*\*([A-H])\*\* — [^|]*\|\s*(\d+)\s*\|")
TOTAL_RE = re.compile(r"^\| \*\*total\*\* \| \*\*(\d+)\*\* \|")


def unwrap(text: str) -> str:
    """Join single newlines inside a paragraph. Blank lines stay blank."""
    return re.sub(r"[ \t]*\n[ \t]*", " ", text)


def chapter_text(prefix: str) -> str | None:
    """Unwrapped text of every book file whose basename starts with `prefix`."""
    hits = sorted(BOOK.glob(f"{prefix}*.md"))
    if not hits:
        return None
    return "\n\n".join(unwrap(p.read_text(encoding="utf-8")) for p in hits)


class Row:
    def __init__(self, rid, done, group, headline):
        self.id = rid
        self.done = done
        self.group = group
        self.headline = headline
        self.check_kind = None
        self.check_arg = None
        self.subs = []          # list of (done, label)

    @property
    def machine(self):
        return self.check_kind in ("absent", "present", "cmd", "cmdabsent", "cmdpresent")

    def verify(self):
        """-> (verdict, detail). verdict in PASS / FAIL / SKIP / ERROR."""
        if not self.machine:
            return "SKIP", f"{self.check_kind} — not machine-decidable"
        if self.check_kind in ("absent", "present"):
            prefix, _, needle = self.check_arg.partition(":")
            text = chapter_text(prefix.strip())
            if text is None:
                return "ERROR", f"no book file matching {prefix.strip()}*"
            n = text.count(needle.strip())
            if self.check_kind == "absent":
                return ("PASS", "string gone") if n == 0 else ("FAIL", f"still present ×{n}")
            return ("PASS", f"present ×{n}") if n else ("FAIL", "not found")

        # cmd kinds. `cmd:` trusts the exit code; use it ONLY where a nonzero genuinely means the
        # row is unsatisfied. Most sweeps in tools/ exit 0 on a successful RUN regardless of what
        # they found, which made three rows read green while wide open on this gauge's first pass.
        # `cmdabsent:NEEDLE::COMMAND` is the honest form for those: the row is done when the
        # tool stops printing the thing.
        needle = None
        if self.check_kind in ("cmdabsent", "cmdpresent"):
            needle, _, cmd = self.check_arg.partition("::")
            needle = needle.strip()
        else:
            cmd = self.check_arg
        try:
            r = subprocess.run(
                cmd.strip(), shell=True, cwd=REPO,
                capture_output=True, text=True, timeout=180,
            )
        except subprocess.TimeoutExpired:
            return "ERROR", "timed out"
        out = (r.stdout or "") + (r.stderr or "")
        if needle is not None:
            n = out.count(needle)
            if self.check_kind == "cmdabsent":
                return ("PASS", f"tool no longer prints {needle!r}") if n == 0 \
                    else ("FAIL", f"tool still prints {needle!r} ×{n}")
            return ("PASS", f"tool prints {needle!r} ×{n}") if n else ("FAIL", f"{needle!r} not printed")
        tail = out.strip().splitlines()
        return ("PASS" if r.returncode == 0 else "FAIL",
                f"exit {r.returncode}" + (f" — {tail[-1][:90]}" if tail else ""))


def parse(path: Path):
    rows, groups, table, total = [], {}, {}, None
    group = None
    cur = None
    for line in path.read_text(encoding="utf-8").splitlines():
        g = GROUP_RE.match(line)
        if g:
            group, cur = g.group(1), None
            groups[group] = g.group(2)
            continue
        t = TABLE_RE.match(line)
        if t:
            table[t.group(1)] = int(t.group(2))
            continue
        tt = TOTAL_RE.match(line)
        if tt:
            total = int(tt.group(1))
            continue
        m = ROW_RE.match(line)
        if m:
            cur = Row(m.group(2), m.group(1).lower() == "x", group, m.group(3).strip(" ·"))
            rows.append(cur)
            continue
        if cur is None:
            continue
        s = SUB_RE.match(line)
        if s:
            cur.subs.append((s.group(1).lower() == "x", s.group(2).strip()))
            continue
        c = CHECK_RE.search(line)
        if c and cur.check_kind is None:
            cur.check_kind, cur.check_arg = c.group(1), c.group(2).strip()
    return rows, groups, table, total


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--verify", action="store_true", help="run every machine check")
    ap.add_argument("--group", help="restrict to one group letter")
    ap.add_argument("--open", action="store_true", help="open rows only, terse")
    args = ap.parse_args()

    if not CHECKLIST.exists():
        sys.exit(f"REFUSED: {CHECKLIST} not found")

    rows, groups, table, total = parse(CHECKLIST)
    if args.group:
        rows = [r for r in rows if r.group == args.group.upper()]

    # --- the control that comes before any count: every row must carry a check ---
    naked = [r for r in rows if r.check_kind is None]
    if naked:
        print("⛔ REFUSED — rows with no `✓` check line. A row no instrument can decide is a row")
        print("   that reads OPEN forever; that is how the 206-row backlog happened the first time.")
        for r in naked:
            print(f"     {r.id}")
        sys.exit(2)

    done = [r for r in rows if r.done]
    print(f"REVISION CHECKLIST — {len(done)}/{len(rows)} rows done")
    print(f"  source: {CHECKLIST.relative_to(REPO)}")

    by_kind = {}
    for r in rows:
        by_kind.setdefault(r.check_kind, []).append(r)
    kinds = " · ".join(f"{k} {len(v)}" for k, v in sorted(by_kind.items()))
    print(f"  checks: {kinds}")
    manual = [r for r in rows if not r.machine]
    print(f"  ⚠ {len(manual)} of {len(rows)} rows are rulings or manual — a green here says "
          f"nothing about them")

    print()
    for letter in sorted({r.group for r in rows if r.group}):
        grp = [r for r in rows if r.group == letter]
        d = sum(1 for r in grp if r.done)
        bar = "█" * d + "·" * (len(grp) - d)
        print(f"  {letter}  {d:>2}/{len(grp):<2} {bar:<14} {groups.get(letter, '')[:52]}")

    subs = [(r, s) for r in rows for s in r.subs]
    if subs:
        sd = sum(1 for _, s in subs if s[0])
        print(f"\n  sub-items (R2-072 chapters): {sd}/{len(subs)} done")

    # --- gauge the file's own summary table ---
    if table and not args.group:
        counted = {}
        for r in rows:
            counted[r.group] = counted.get(r.group, 0) + 1
        bad = [(k, v, counted.get(k, 0)) for k, v in table.items() if counted.get(k, 0) != v]
        if total is not None and total != len(rows):
            bad.append(("total", total, len(rows)))
        if bad:
            print("\n⛔ THE FILE'S OWN SUMMARY TABLE DISAGREES WITH THE FILE.")
            for k, printed, actual in bad:
                print(f"     {k}: printed {printed}, counted {actual}")
            sys.exit(1)
        print("\n  ✅ summary table agrees with the rows (checked, not trusted)")

    if args.open or not args.verify:
        openr = [r for r in rows if not r.done]
        if openr:
            print(f"\nOPEN — {len(openr)}")
            for r in openr:
                head = re.sub(r"\s+", " ", r.headline)[:96]
                print(f"  ☐ {r.id}  {head}")

    if args.verify:
        print("\nVERIFY — machine checks only; manual and ruling rows are reported, not decided")
        divergent = []
        for r in rows:
            verdict, detail = r.verify()
            mark = {"PASS": "✅", "FAIL": "⛔", "SKIP": "·", "ERROR": "⚠"}[verdict]
            print(f"  {mark} {r.id}  {verdict:<5} {detail}")
            if r.machine:
                # a ticked row whose check fails, or an unticked row whose check passes
                if r.done and verdict != "PASS":
                    divergent.append((r, "ticked but the defect is still there"))
                elif not r.done and verdict == "PASS":
                    divergent.append((r, "not ticked but the check is already green"))
        if divergent:
            print(f"\n⛔ DIVERGENCE — {len(divergent)}: the box and the manuscript disagree")
            for r, why in divergent:
                print(f"     {r.id}  {why}")
            sys.exit(1)
        print("\n✅ no divergence between ticked boxes and machine checks")
        print("   (this says nothing about the rulings and manual rows above)")


if __name__ == "__main__":
    main()
