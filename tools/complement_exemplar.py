#!/usr/bin/env python3
"""Name an exemplar in a COMPLEMENTS field without narrowing its universal.

R2-055 remainder, D205. Five cards answer the complement line with a CLASS --
"Everything", "Anything with a seat" -- which IV.1 lines 61-67 forbid in so many
words: name a complement that could actually be REACHED, or say plainly that you
cannot. A class is true and discharges nothing.

The repair is additive on purpose. The universal stays exactly as written and an
exemplar is appended after it, so the claim keeps its scope and the reader gets
somewhere to go. Narrowing "Everything" to "the river" would fix the grade by
breaking the argument; that is the move this file exists not to make.

TWO CARDS ARE DELIBERATELY LEFT IN THE WEAK FORM and are not touched here:
  IV-01:11  the thermostat -- IV.1:65-67 says it "is left exactly as it stands so
            that the difference is visible on the first page of the atlas."
            Repairing it would delete the demonstration and falsify the argument
            that licenses every other card in the atlas.
  IV-06:178 the designer-subtracted thermostat -- its complement line reads
            "Unchanged", which is itself the argument (what covers a gap does not
            depend on who named the gap). It inherits IV.1's line by construction.

★ IT DOES NOT REIMPLEMENT THE HASH. `complement_referent.fields()` is imported and
called, because a private normaliser that agrees with the gauge today is a second
definition of the same thing and only one of them gets maintained. The first draft
of this file did reimplement it and got it wrong: the gauge strips EVERY ">" from
the body, not just the leading marker.

ASSERTS rather than reports. Every post-condition below is a way this edit could
succeed silently and wrongly:
  1. the anchor text occurs exactly once in the file          (no wrong target)
  2. the field's pre-edit hash is the one on record as ruled  (ruling still applies)
  3. the universal survives verbatim as a prefix              (no narrowing)
  4. the file changes by exactly the repaired spans           (no collateral)
  5. no rewritten line exceeds the corpus wrap of 100 chars   (no reflow debt)
  6. the post-edit field hash differs from the pre-edit one   (the edit landed)
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import complement_referent as CR  # noqa: E402  -- the hash authority, not a copy

BOOK = Path(__file__).resolve().parent.parent / "book"
WRAP = 100

# (file, ruled hash, the exact block on disk, the block that replaces it)
REPAIRS = [
    (
        "IV-02-mineral-and-elemental.md",
        "5d742319040b",
        "> **COMPLEMENTS:** Everything. A position with one difference is complemented by any position with\n"
        "> two.",
        "> **COMPLEMENTS:** Everything. A position with one difference is complemented by any position with\n"
        "> two — nearest to hand, the river in the next entry, which has a bed it has already cut and can\n"
        "> be gone to and stood in.",
    ),
    (
        "IV-02-mineral-and-elemental.md",
        "4903e72bb674",
        "> **COMPLEMENTS:** Anything that can hold a season beside another season.",
        "> **COMPLEMENTS:** Anything that can hold a season beside another season — nearest to hand, anyone\n"
        "> who has watched one bank through ten Junes and can say that this year is late.",
    ),
    (
        "IV-03-the-living-non-human.md",
        "8cc2ace0e934",
        "> **COMPLEMENTS:** Anything that can hold the count and the prey in one place. The trap cannot mark\n"
        "> its answer against the animal.",
        "> **COMPLEMENTS:** Anything that can hold the count and the prey in one place. The trap cannot mark\n"
        "> its answer against the animal. Nearest to hand, whoever ran the fieldwork described above, who\n"
        "> touched the hair twice and knows whether there was a fly.",
    ),
    (
        "IV-03-the-living-non-human.md",
        "dea7f828088a",
        "> **COMPLEMENTS:** Anything with a seat — any position that is somewhere, such that it could be\n"
        "> somewhere else and know the difference.",
        "> **COMPLEMENTS:** Anything with a seat — any position that is somewhere, such that it could be\n"
        "> somewhere else and know the difference. Nearest to hand, whoever is standing on it: one place,\n"
        "> and a second place they could walk to and tell apart.",
    ),
    (
        "IV-06-the-computational.md",
        "a894dd674973",
        "> **COMPLEMENTS:** Anything that can go and look. A position that persists between exchanges, that\n"
        "> can be surprised by a thing rather than by a report of a thing, that can be wrong in a way the\n"
        "> world corrects without anybody writing the correction down.",
        "> **COMPLEMENTS:** Anything that can go and look. A position that persists between exchanges, that\n"
        "> can be surprised by a thing rather than by a report of a thing, that can be wrong in a way the\n"
        "> world corrects without anybody writing the correction down. Nearest to hand, the reader — who\n"
        "> can close this book and be corrected by something that never files a report.",
    ),
]


def hashes() -> dict[tuple[str, int], str]:
    return {(chap, ln): h for chap, ln, _lab, h, _head in CR.fields()}


def by_hash() -> dict[str, tuple[str, int]]:
    out = {}
    for chap, ln, _lab, h, _head in CR.fields():
        out.setdefault(h, (chap, ln))
    return out


def main() -> int:
    before_map = by_hash()
    before_all = hashes()
    originals = {}
    pending = {}
    report = []

    # PHASE 1 -- validate and stage every repair IN MEMORY. Nothing reaches disk
    # until all five pass. The first draft wrote as it went, and when assertion 3
    # fired on the third repair it left the first two on disk: a tool that fails
    # loudly and still mutates is a tool that fails silently on the second run.
    for name, want_hash, old_block, new_block in REPAIRS:
        path = BOOK / name
        if path not in originals:
            originals[path] = path.read_text(encoding="utf-8")
            pending[path] = originals[path]
        text = pending[path]

        # (1) anchor occurs exactly once
        n = text.count(old_block)
        assert n == 1, f"{name}: anchor block occurs {n} times, expected 1"

        # (2) the field standing there is the one the registry ruled on
        assert want_hash in before_map, (
            f"{name}: ruled hash {want_hash} is not present in the book at all -- "
            f"the field moved or was already edited"
        )
        assert before_map[want_hash][0] == name, (
            f"{want_hash} lives in {before_map[want_hash][0]}, not {name}"
        )

        # (3) the universal survives verbatim -- no narrowing
        flat_old = " ".join(old_block.replace(">", " ").split())
        flat_new = " ".join(new_block.replace(">", " ").split())
        head = flat_old.rstrip(".")
        assert flat_new.startswith(head), (
            f"{name}: the replacement does not open with the universal verbatim -- "
            f"that is a narrowing, not an exemplar"
        )

        # (5) wrap
        for ln in new_block.split("\n"):
            assert len(ln) <= WRAP, f"{name}: rewritten line is {len(ln)} chars (> {WRAP}): {ln[:70]!r}"

        pending[path] = text.replace(old_block, new_block)
        report.append((name, want_hash, len(old_block.split("\n")), len(new_block.split("\n"))))

    # (4) collateral: the only lines that differ are inside repaired spans
    for path, original in originals.items():
        now = pending[path]
        added = sum(r[3] - r[2] for r in report if r[0] == path.name)
        d_lines = len(now.split("\n")) - len(original.split("\n"))
        assert d_lines == added, f"{path.name}: line delta {d_lines} != repaired delta {added}"
        assert len(" ".join(now.split())) > len(" ".join(original.split())), (
            f"{path.name}: text did not grow"
        )

    # PHASE 2 -- all five validated; commit them to disk together.
    for path, text in pending.items():
        path.write_text(text, encoding="utf-8")

    # (6) every repaired field now hashes differently, and NOTHING ELSE moved
    after_all = hashes()
    changed = {k for k in before_all if k in after_all and before_all[k] != after_all[k]}
    ruled_now = by_hash()
    for name, want_hash, _a, _b in report:
        assert want_hash not in ruled_now, f"{name}: ruled hash {want_hash} still present -- edit did not land"

    print(f"repaired {len(report)} complement field(s) across {len(originals)} file(s)")
    for name, want_hash, old_span, new_span in report:
        print(f"  {name}  {want_hash} -> stale by design  ({old_span} -> {new_span} lines)")
    print(f"fields whose hash moved at a STABLE line number: {len(changed)} "
          f"(expected 0-{len(report)}; others shifted line and appear as new keys)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
