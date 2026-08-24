#!/usr/bin/env python3
"""Third pass: file and tool pointers. D205, Clayton's second ruling —
"strip references to outside files and works of our own... The book should stand
as it is without external files."

Same discipline as the ID pass: the POINTER goes, the CLAIM stays. "measured by
`tools/instrument_sweep.py`, not recalled" becomes "measured, not recalled" — the
reader learns the same thing about the number and is not sent to a file they
cannot open.

A no-match is an error, not a no-op.
"""
import pathlib
import sys

BOOK = pathlib.Path(__file__).resolve().parent.parent / "book"

EDITS = [
    ("C-01-what-this-is.md",
     " ⚠ At the time of this printing `Sex, Ecology,\nSpirituality` is still absent from `03-THE-ANCESTORS.md`, which is a filed and unpaid item — the\nparagraph above discharges the coda half of it and not the other.",
     ""),

    ("C-01-what-this-is.md",
     "quoted from `00-ARCHITECTURE.md`'s replacement table",
     "quoted from the replacement table"),

    ("C-02-why-it-is-not-finished.md",
     "The 18-of-44 figure is measured by `tools/instrument_sweep.py`, not recalled:",
     "The 18-of-44 figure is measured, not recalled:"),

    ("IV-01-the-census-and-its-method.md",
     "**Neither text\nis in this repository.** `null-space-atlas.md` is, and its figure was counted rather than recalled,\nwhich is how the error in the prose was found.",
     "The figure was counted rather than recalled,\nwhich is how the error in the prose was found."),

    ("IV-09-the-archetypal.md",
     "**Go to the out-list.** `00-ARCHITECTURE.md:61` carries `archetypes-as-genetic` with",
     "**Go to the out-list.** It carries the entry with"),

    ("IV-09-the-archetypal.md",
     "1857) as held locally at `corpora/tmp/sanctiirenaeiepi01unse.txt`. The English is exact against the",
     "1857). The English is exact against the"),

    ("IV-10-what-the-census-cannot-see.md",
     "★★ **AND THE PLAN HAD IT RIGHT.** `06-THE-SCAFFOLD.md`:1601–1602 renders the clause as",
     "★★ **AND THE PLAN HAD IT RIGHT.** The plan renders the clause as"),

    ("IV-10-what-the-census-cannot-see.md",
     "`tools/brief_source.py`:71 names a drafting tree, **which is\nnot on this machine.**",
     "The drafting record names a source tree **which is\nnot available here.**"),

    ("IV-10-what-the-census-cannot-see.md",
     "⛔ **AND THIS ONE DID ENTER AT PLANNING.** `06-THE-SCAFFOLD.md`:1604–1606 carries the sentence in",
     "⛔ **AND THIS ONE DID ENTER AT PLANNING.** The plan carries the sentence in"),

    ("IV-10-what-the-census-cannot-see.md",
     "`06-THE-SCAFFOLD.md`\ncontains no sasquatch, no bars and no *\"three of five\"* anywhere in IV.10's beats; what it carries is\nthe **count** (*\"the third instance of IV.9's filled-table finding\"*, `06`:1620 — see [^11]).",
     "The plan\ncontains no sasquatch, no bars and no *\"three of five\"* anywhere in IV.10's beats; what it carries is\nthe **count** (*\"the third instance of IV.9's filled-table finding\"* — see [^11]).",),

    ("IV-10-what-the-census-cannot-see.md",
     "⚠ **The count entered at planning.** `06-THE-SCAFFOLD.md`:1620 already reads",
     "⚠ **The count entered at planning.** The plan already reads"),

    ("V-01-what-a-tradition-is.md",
     "**The same false placement\n    stood in three chapters and they agreed with each other**, which is why `tools/placement_sweep.py`\n    exists and why a consistent placement in this book should be read as unchecked rather than clean.",
     "**The same false placement\n    stood in three chapters and they agreed with each other**, which is why a consistent placement in\n    this book should be read as unchecked rather than clean."),

    ("V-04-the-atheism-that-was-right-about-the-wrong-thing.md",
     "That cluster was found by\n`tools/crossref_rot.py --all` and **not by `crossref_rot.py`** — see [^11] — which is the finding",
     "That cluster was found by\nthe widened sweep and **not by the default one** — see [^11] — which is the finding"),

    ("V-04-the-atheism-that-was-right-about-the-wrong-thing.md",
     "This pair *is* tier 1 in\n    `crossref_rot.py` — `V.4>V.1:5ee32b3c`, cited 2026-08-09, four corrective notes landed in V.1 two\n    days later. It was **never printed**: the tool caps its default view at 20 of 99 rows",
     "This pair *is* tier 1 in\n    the sweep — cited 2026-08-09, four corrective notes landed in V.1 two\n    days later. It was **never printed**: the default view caps at 20 of 99 rows"),

    ("V-05-the-east-one-ground-many-localisations.md",
     "This is precisely what `tools/placement_sweep.py` was built for after V.1 [^3]: *a",
     "This is precisely the rule set after V.1 [^3]: *a"),

    ("V-06-the-room-that-was-never-emptied.md",
     "it is\n    why `tools/apparatus_rot.py` exists as of tonight.",
     "it is\n    why the apparatus is swept on its own as of tonight."),

    ("V-06-the-room-that-was-never-emptied.md",
     "⚠ **The stem clause is not mine — `tools/apparatus_rot.py` produced it, five minutes after being",
     "⚠ **The stem clause is not mine — the apparatus sweep produced it, five minutes after being"),

    ("V-08-travel.md",
     "`endnote_debt.py` scores this chapter's owed sources as *Eliade, Monroe* and does not\n    list Harner — he is dropped **silently**, appearing in none of the tool's printed exclusion\n    classes. Cause, read off `scan_prose`:",
     "The debt sweep scores this chapter's owed sources as *Eliade, Monroe* and does not\n    list Harner — he is dropped **silently**, appearing in none of its printed exclusion\n    classes. The cause:"),

    ("V-09-the-road-being-walked-now.md",
     "    same\"* (`07-THE-CLAIMS-REGISTER.md`:1121). C29 withdrew IV.1's induction on exactly this ground —",
     "    same\"*. C29 withdrew IV.1's induction on exactly this ground —"),

    ("VI-08-the-tunnel-you-are-in.md",
     "[^10]: The room is `palace/southeast/mirror.md` in that archive, described in its own index as",
     "[^10]: The room is described in its own index as"),

    ("Z-02-works-cited.md",
     "*Generated from the endnotes by `tools/bibliography.py`. Do not hand-edit this page — re-run the tool. A bibliography typed once is a stamp; it rots at exactly the rate the notes are repaired and does not change appearance while it rots, which is the object this book spends a volume diagnosing. The back matter is not exempt from the argument.*",
     "<!-- MAINTAINER, NOT PRINTED: generated from the endnotes; do not hand-edit this page,\n     re-run the generator. A bibliography typed once is a stamp; it rots at exactly the rate\n     the notes are repaired and does not change appearance while it rots, which is the object\n     this book spends a volume diagnosing. The back matter is not exempt from the argument. -->"),
]

failed = []
for fname, old, new in EDITS:
    path = BOOK / fname
    text = path.read_text(encoding="utf-8")
    n = text.count(old)
    if n != 1:
        failed.append((fname, n, old[:70]))
        continue
    path.write_text(text.replace(old, new), encoding="utf-8")

print(f"{len(EDITS) - len(failed)}/{len(EDITS)} applied.")
for fname, n, snippet in failed:
    print(f"  ⛔ {n} MATCHES  {fname}  {snippet!r}")
sys.exit(1 if failed else 0)
