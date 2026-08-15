#!/usr/bin/env python3
"""_absorb.py — the R-214 inversion harness. Day 195.

Applies the self-citation absorptions as EXACT anchored replacements, each of which
must match exactly once. A miss is a hard failure, never a silent no-op — the whole
class of defect this book keeps finding is an edit that reported success and did
nothing. Line endings are read and restored per file (this tree is CRLF; an LF
anchor against a CRLF file misses silently, which is a filed reference defect).

Not a general tool. Delete after the sweep, or keep as the receipt for it.
"""
import io
import os
import sys

ROOT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "book")


def apply(fname, pairs):
    path = os.path.join(ROOT, fname)
    raw = open(path, "rb").read()
    crlf = b"\r\n" in raw
    text = raw.decode("utf-8").replace("\r\n", "\n")
    for old, new in pairs:
        n = text.count(old)
        if n != 1:
            print(f"  [X] {fname}: anchor matched {n} times, expected 1")
            print(f"      {old[:120]!r}")
            return False
        text = text.replace(old, new)
    out = text.replace("\n", "\r\n") if crlf else text
    open(path, "wb").write(out.encode("utf-8"))
    print(f"  [ok] {fname}: {len(pairs)} absorption(s) applied")
    return True


def run(batch):
    ok = True
    for fname, pairs in batch:
        ok = apply(fname, pairs) and ok
    return 0 if ok else 1
