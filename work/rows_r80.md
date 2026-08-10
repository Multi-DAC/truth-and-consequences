
---

**FILED — R-80: THE CORPUS-SUPPORT SCRIPT'S ROOT NO LONGER EXISTS, AND ITS FAILURE MODE IS ITS OWN
HEADLINE FINDING.** `work/vi5_corpus.py` carries a hardcoded `ROOT` under `C:\Users\Wasch\` for the
quarry archive. **That path does not resolve on this machine** — the live clone with the matching
git history sits under `CLAWD_REPOS`. `os.walk` over a nonexistent directory raises nothing and
yields nothing, so the script runs to completion, reports `scanned 0 files`, and prints **0 against
every term in its list.**
★★ **The defect is not the dead path. It is that the failure is shaped exactly like the result.**
This instrument's contribution to VI.4, VI.5, VI.6 and VI.7 has each time been *a name at zero where
the vocabulary is everywhere* — so a broken run does not look broken. It looks like the strongest
finding the tool has ever produced, arriving in the chapter that most wants one. The `scanned 0
files` line is printed, and it is one line above forty lines of zeros that are far more interesting
to read.
✅ **Caught on the VI.8 run, and only because the term list happened to carry words that could not
honestly be absent** — *paradigm*, *modernity*, *the present*, *dated*. Those are the positive
control, and they were in the list by accident of drafting, not by design.
⚠ **The four prior chapters' counts are NOT retracted.** They were non-zero, which means they were
measured against a live tree; a dead root cannot produce a 23. **What is not known is which tree**,
and whether it is the same one VI.8 measured (3,069 `.md`/`.txt` files against VI.7's reported
2,586 — a gap that may be scope, may be growth, and has not been resolved).
**Repair, three parts, and the first two are cheap:** (a) the script **exits non-zero and loudly** if
`scanned == 0`, or if any member of a declared control list returns 0 — a null with no positive
control is not a result; (b) `ROOT` resolves from `CLAWD_REPOS` rather than a user path, so it
survives a machine change; (c) the tool is promoted out of `work/` into `tools/` with the rest of the
gauges, and the corpus root and file count are **printed into the log entry that cites it**, so a
later reader can tell which tree a count came from. ⚠ (c) is what makes the VI.4–VI.7 ambiguity
un-repeatable; without it, (a) and (b) fix the future and leave the record unreadable.
**TRIGGER: before the next chapter that runs a corpus-support screen — which is VII.1.**
medium — the instrument is cheap to fix and its failures are indistinguishable from its findings
