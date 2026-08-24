#!/usr/bin/env python3
"""Second pass: the 21 process-ID sites the patterned pass left. Exact strings, hand-written.

Each entry is (file, old, new). An exact-string edit that does not match is an ERROR here,
not a no-op — a silent miss is how a strip pass reports done and leaves the token on the page.
"""
import pathlib
import sys

BOOK = pathlib.Path(__file__).resolve().parent.parent / "book"

EDITS = [
    ("IV-03-the-living-non-human.md",
     "which is the whole of what R-2 is.",
     "which is the whole of what this note is."),

    ("IV-07-the-non-physical.md",
     "reads, and filed with R-144's trigger: the scan before\nthis volume ships.",
     "reads."),

    ("IV-09-the-archetypal.md",
     "**Filed twice before it was fixed — R-108, `SWEEP-001` row 1, and again\nhere**",
     "**Filed twice before it was fixed — once upstream in a sweep, and again\nhere**"),

    ("IV-09-the-archetypal.md",
     "Full\nmeasurement: `review/SCAN-002-day191-iv9-source-audit.md`;. Checked line by line",
     "Checked line by line"),

    ("IV-10-what-the-census-cannot-see.md",
     "Checked against\ndisk: `06-THE-SCAFFOLD.md`:154 records the renumber (*\"name at V.10 (was V.9 — ruling 125)\"*), and\n**`book/V-09-the-road-being-walked-now.md` exists and is drafted**",
     "Checked: the\nrenumber is on the record, and **V.9 exists and carries the entry**"),

    ("IV-10-what-the-census-cannot-see.md",
     "and the reason R-148 must\nsweep the planning files and not only the prose.",
     "and the reason the sweep must\nreach the planning material and not only the prose."),

    ("V-03-the-scholastics-and-the-god-without-a-face.md",
     "but after R-161,",
     "but after the repair,"),

    ("V-06-the-room-that-was-never-emptied.md",
     "[^3]: ⛔ **R-184. The chapter inherits",
     "[^3]: ⛔ **The chapter inherits"),

    ("V-06-the-room-that-was-never-emptied.md",
     "That is the R-190 condition sitting inside a clean row.",
     "That is the same condition sitting inside a clean row."),

    ("V-06-the-room-that-was-never-emptied.md",
     "[^14]: ⛔ **R-183. The chapter coins",
     "[^14]: ⛔ **The chapter coins"),

    ("V-07-magic-operative.md",
     "R-176's sweep of all thirty V.x→V.1 reaches",
     "The sweep of all thirty V.x→V.1 reaches"),

    ("V-07-magic-operative.md",
     "which credited V.1 with a thesis V.1 does not contain (R-189).",
     "which credited V.1 with a thesis V.1 does not contain."),

    ("V-08-travel.md",
     "and the two are being deliberately rhymed. R-191 is the\nfiled instance",
     "and the two are being deliberately rhymed. This is the\nfiled instance"),

    ("V-08-travel.md",
     "Same shape as IV.8's translator finding (R-187).",
     "Same shape as IV.8's translator finding."),

    ("V-08-travel.md",
     "⛔ **The caution is that R-189\nfound V.6 crediting",
     "⛔ **The caution is that an earlier pass\nfound V.6 crediting"),

    ("V-11-what-the-old-roads-knew.md",
     "⛔ **AND THE VERDICT ON R-208\n WAS WRONG AS FILED.**",
     "⛔ **AND THE VERDICT ON THAT PREDICTION\n    WAS WRONG AS FILED.**"),

    ("VI-01-different-worlds-not-different-opinions.md",
     "which is a distinction ruling 9 asks for and which the gauge that found this gap cannot itself make.",
     "which is a distinction the gauge that found this gap cannot itself make."),

    ("VI-04-print-and-the-interior.md",
     "Measured on Day 190 under the\nscope declared at R-67 — `.md` files, `archive/` and `_superseded/` excluded, across 2,550 research\nfiles —",
     "Measured on Day 190 under the\ndeclared scope —"),

    ("VI-05-electric.md",
     "**a wider scope than R-67's declared 2,550**",
     "**a wider scope than the one declared earlier**"),

    ("VI-05-electric.md",
     "should not be quoted as R-67-scoped:",
     "should not be quoted against it:"),

    ("VII-03-the-floor.md",
     "Filed Day 195 as R-216 by the ghost audit:",
     "Filed Day 195 by the ghost audit:"),

    ("VIII-05-the-second-arrow.md",
     "its central term was banned by ruling 109 on the",
     "its central term was banned on the"),
]

failed = []
for fname, old, new in EDITS:
    path = BOOK / fname
    text = path.read_text(encoding="utf-8")
    if old not in text:
        failed.append((fname, old[:70]))
        continue
    if text.count(old) > 1:
        failed.append((fname, f"AMBIGUOUS ({text.count(old)}x): {old[:60]}"))
        continue
    path.write_text(text.replace(old, new), encoding="utf-8")

print(f"{len(EDITS) - len(failed)}/{len(EDITS)} applied.")
for fname, snippet in failed:
    print(f"  ⛔ NO MATCH  {fname}  {snippet!r}")
sys.exit(1 if failed else 0)
