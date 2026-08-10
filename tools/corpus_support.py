#!/usr/bin/env python
"""corpus_support.py — how present is a term in the quarry archive?

Counts FILES containing each term (not occurrences) across the Corpus-Perspectival
tree, so a chapter's brief can say "this vocabulary is everywhere and this name is
at zero" and mean something checkable.

R-80, paid Day 190. The instrument this replaces (`work/vi5_corpus.py`,
`work/vi8_corpus.py`) carried a hardcoded ROOT under C:\\Users\\Wasch\\ that does
not resolve on this machine. os.walk over a nonexistent directory raises nothing
and yields nothing, so it ran to completion and printed 0 against every term.

  The defect was never the dead path. It was that the failure is shaped exactly
  like the result. This tool's contribution to four chapters has each time been
  "a name at zero where the vocabulary is everywhere" — so a broken run does not
  look broken. It looks like the strongest finding the tool has ever produced.

Three repairs, and only the third makes the record readable afterwards:
  (a) a NULL WITH NO POSITIVE CONTROL IS NOT A RESULT. Every run declares controls
      — terms that cannot honestly be absent. scanned == 0, or any control at 0,
      exits non-zero with the zeros suppressed, because forty lines of zeros are
      more interesting to read than the one line above them saying the scan failed.
  (b) ROOT resolves from CLAWD_REPOS, so it survives a machine change.
  (c) the root, the file count and the tree's git HEAD are printed in the header,
      so a later reader can tell WHICH tree a count came from. Without this, (a)
      and (b) fix the future and leave the record unreadable — VI.4 through VI.7's
      counts are non-zero, therefore measured against a live tree, and which tree
      is not recoverable.

Usage:
    corpus_support.py --terms terms.txt --controls "paradigm,modernity"
    corpus_support.py --terms terms.txt          # controls default to CONTROLS
    echo "Nagel\nEpicurus" | corpus_support.py --controls "death,grief"
"""
import argparse
import os
import re
import subprocess
import sys
from pathlib import Path

# (b) — a path relative to a variable the machine sets, not a user directory
# a script remembered once. Falls back script-relative-then-env, never bare.
_REPOS = os.environ.get("CLAWD_REPOS") or r"C:/Users/mercu/clawd"
DEFAULT_ROOT = Path(_REPOS) / "repo-staging" / "Corpus-Perspectival"

# (a) — terms that cannot honestly be absent from this archive. If one of these
# reads 0, the scan is broken, not the corpus. Deliberately generic: a control
# specific to the chapter under screen would go dark for the same reason the
# finding does.
CONTROLS = ["consciousness", "perspective", "Ground", "the focusing"]

SKIP_DIRS = {".git", "node_modules", "__pycache__", ".venv", ".mypy_cache"}


def head(root: Path) -> str:
    """(c) — which tree, at which commit. A count with no HEAD is a count with no address."""
    try:
        out = subprocess.run(
            ["git", "-C", str(root), "log", "-1", "--format=%h %ci"],
            capture_output=True, text=True, timeout=20,
        )
        return out.stdout.strip() or "(no git history)"
    except Exception as e:                                   # noqa: BLE001
        return f"(git unavailable: {e})"


def scan(root: Path, terms):
    counts = {t: 0 for t in terms}
    pats = {t: re.compile(re.escape(t), re.I) for t in terms}
    files = 0
    for dp, dn, fn in os.walk(root):
        dn[:] = [d for d in dn if d not in SKIP_DIRS]
        for f in fn:
            if not f.lower().endswith((".md", ".txt")):
                continue
            try:
                text = Path(dp, f).read_text(encoding="utf-8", errors="ignore")
            except Exception:                                # noqa: BLE001
                continue
            files += 1
            for t in terms:
                if pats[t].search(text):
                    counts[t] += 1
    return files, counts


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--terms", help="file with one term per line; default stdin")
    ap.add_argument("--controls", default=",".join(CONTROLS),
                    help="comma-separated terms that cannot honestly be absent")
    ap.add_argument("--root", default=str(DEFAULT_ROOT))
    args = ap.parse_args()

    root = Path(args.root)
    src = Path(args.terms).read_text(encoding="utf-8") if args.terms else sys.stdin.read()
    terms = [ln.strip() for ln in src.splitlines() if ln.strip() and not ln.startswith("#")]
    controls = [c.strip() for c in args.controls.split(",") if c.strip()]

    # The root check comes BEFORE the walk, because the walk cannot fail.
    if not root.is_dir():
        print(f"⛔ ROOT DOES NOT RESOLVE: {root}", file=sys.stderr)
        print("   os.walk would yield nothing and every count would read 0.", file=sys.stderr)
        print("   That is R-80's failure and it looks exactly like a finding.", file=sys.stderr)
        return 2

    files, counts = scan(root, sorted(set(terms + controls), key=str.lower))

    dead = [c for c in controls if counts.get(c, 0) == 0]
    ok = files > 0 and not dead

    # (c) — the header IS the receipt. Paste it into the log entry that cites the run.
    print(f"CORPUS SUPPORT — {'OK' if ok else 'INVALID'}")
    print(f"  root    : {root}")
    print(f"  HEAD    : {head(root)}")
    print(f"  scanned : {files} .md/.txt files")
    print(f"  controls: {', '.join(f'{c}={counts.get(c, 0)}' for c in controls)}")

    if not ok:
        print("", file=sys.stderr)
        print("⛔ RUN INVALID — counts SUPPRESSED, deliberately.", file=sys.stderr)
        if files == 0:
            print("   scanned 0 files.", file=sys.stderr)
        if dead:
            print(f"   control(s) at zero: {', '.join(dead)}", file=sys.stderr)
        print("   A null with no positive control is not a result. Fix the root", file=sys.stderr)
        print("   or the control list; do not read the zeros below — there are none.", file=sys.stderr)
        return 1

    print()
    for t in terms:
        print(f"  {counts.get(t, 0):5d}  {t}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
