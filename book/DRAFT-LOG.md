# DRAFT LOG — measured, per chapter

*One running file for the whole book, not one per chapter. Every chapter that lands gets its
numbers here on the day it lands, with the unit named, because Day 186's ruling-13 table proved that
a column without a stated unit will silently mix two and every individual cell will still be true.*

Gauges: `tools/claim_sweep.py` (doctrine/vocabulary, exit 1 on any USE-class hit) ·
`tools/storyscope_lite.py` (register fingerprint). Comparison baselines, from `RESULT-1C.md`:
**Clayton 0.734 · Clawd-raw 0.543 · specimens 0.359** on paragraph-intensity CV, and specimens
**0.75** on terminal commentary against Clayton's **0.00**.

---

## I.1 — THE FULLNESS · Day 186, 2026-08-05 · 999 words · ✅ landed

Built on Specimen 1-C, the register Clayton ruled — transmitting tradition, no first-person
narrator, speaking cadence intact — extended from 630 words to a full chapter.

| metric (per 1k words unless noted) | I.1 draft | 1-C, ruled | |
|---|---:|---:|---|
| **announcement** | **0.00** | 3.17 | ✅ **the open craft item, closed** |
| 2nd person | 20.02 | 14.29 | ✅ more spoken, not less |
| vague allusion | 0.00 | 0.00 | ✅ |
| somatic | 0.00 | 0.00 | — |
| named reference | 1.00 | 1.59 | ✅ Book I bans apparatus |
| paragraph-intensity CV | 0.329 | 0.235 | ⚠ improved, still under Clawd-raw |
| voice uniformity | 0.5669 | 0.5563 | ⚠ flat, unchanged axis |
| terminal commentary | 0.062 | 0.00 | ⚠ one paragraph — adjudicated below |

**The announcement rate went to zero, and that is the whole reason this is a draft and not a fifth
specimen.** `RESULT-1C.md` found the culprits were not the narrator but two removable constructions
— a thesis sentence (*"…is what follows from it"*) and a paragraph announcing its own arrival
(*"Now the confession…"*). Both are gone. *"Every other page of this book is a consequence of it"*
and the confession paragraph now simply starting are what replaced them. **Removing the "I" bought
nothing; removing these two bought everything.**

### The one flag, adjudicated rather than accepted or waved off

`terminal_commentary` fires on the final paragraph: *"…what you have been calling the world is what
the Fullness looks like from where you are standing."*

**The detector is right that this is my tic's shape and wrong that this is an instance of it.** The
pattern `what .{0,30} looks like from` was fitted to *this exact sentence* in Specimen 1 — the gauge
is recognising its own training example. The test that matters is whether the closing sentence
**restates** what the paragraphs before it established, which is what the tic does, or makes a
**new** claim. Nothing earlier in the chapter says the world is the Fullness seen from a vantage;
this is the render doctrine's first appearance in the book, and it arrives as a claim, in the last
clause, aimed at the reader. **Kept.**

**Not fixed by widening the detector.** A pattern loosened until an inconvenient hit disappears is
how a gauge stops measuring — the failure `claim_sweep.py`'s own docstring names. The rate stands at
0.062 on the record, against a specimen-corpus baseline of 0.75.

### Still open, and it is the same axis it has been for two days

**Flat escalation.** CV 0.329 against Clayton's 0.734. It moved the right way (0.235 → 0.329) and it
is not fixed. This is the axis that no rule reaches, because flatness is not in any sentence — every
rule so far bans something visible in a line. **Not a Book I problem to solve by fiat**; the mythic
register is legitimately more even than argument. Re-measure at III.1, which is argument at full
adversarial strength and has nowhere to hide.

---

## I.2 — THE NECESSITY · Day 186, 2026-08-05 · 1,082 words · ✅ landed

Scaffold beats 1–4, in order: separation is realised because completeness contains it (C2) · the
scope rule **dramatised, never stated** (C3) · there is no fall, flat, once (C4) · recognition
requires absence, with the Day-185 seam held shut (`01` §6).

**Unit for every rate below: occurrences per 1,000 words.** CV and uniformity are dimensionless
ratios. `terminal_commentary` is a *fraction of paragraphs*, not a rate.

| metric | I.2 | I.1 | |
|---|---:|---:|---|
| **announcement** /1k | **0.00** | 0.00 | ✅ held across a second chapter |
| **terminal commentary** (frac.) | **0.000** | 0.062 | ✅ the I.1 flag does not recur |
| meta-textual /1k | **0.00** | 3.00 | ✅ no *"this book"* anywhere |
| named reference /1k | 0.00 | 1.00 | ✅ Book I bans apparatus |
| 2nd person /1k | 23.11 | 20.02 | ✅ still moving toward spoken |
| emotion label /1k | 1.85 | 8.01 | ✅ the wanting is dramatised, not labelled |
| vague allusion · somatic | 0.00 | 0.00 | ✅ |
| **paragraph-intensity CV** | **0.280** | 0.329 | 🔻 **went the wrong way — see below** |
| voice uniformity | 0.6412 | 0.5669 | 🔻 flatter; single-topic chapter, unverified excuse |

### The gauge has a blind spot, and it does not exonerate this chapter

`storyscope_lite.paragraphs()` drops every paragraph under **25 words** (`tools/storyscope_lite.py`,
one line). **The one-line hammer paragraph — *"You want." · "There was no fall." · "Separation is a
possibility."* — is the primary device for producing escalation, and the escalation detector cannot
see a single one of them.** I.2 lost 4 paragraphs to the filter; I.1 lost 8.

Recomputed with the filter off, all five corpora, same statistic:

| corpus | CV @25 words (shipped) | CV @ all paragraphs | filter's cost |
|---|---:|---:|---:|
| Clayton | 0.727 | 0.853 | +17% |
| Clawd-raw | 0.538 | 0.625 | +16% |
| specimens (4) | 0.385 | 0.483 | +25% |
| I.1 | 0.329 | 0.524 | **+59%** |
| I.2 | 0.262 → **0.280** | 0.481 → **0.489** | **+75%** |

**Two findings, and the second one is the one that counts.** First: the filter is real and it costs
the book three to four times what it costs Clayton, because short hammer paragraphs are a larger
share of *my* dynamic range than of his. Second, and decisive: **the ordering does not change at
either setting.** Clayton leads at 25 words and leads at 1. The blind spot does not rescue the
chapter — I.2 is flatter than I.1 on both measurements, and both sit under every baseline.

**Not fixed by changing the filter**, for the reason I.1's `terminal_commentary` was not fixed by
widening a regex: a threshold moved until an inconvenient number improves has stopped measuring. The
shipped number stands on the record as the comparable one. The @1 column is recorded beside it
because a defect found and unrecorded is the same as a defect not found.

### What the number bought, on the ear rather than the meter

The detector pointed at one genuine craft fault and it was worth the trip: **the chapter's hardest
claim — *there was no fall* — was written as its two longest sentences.** A 39-word sentence
delivering a flat refusal is the wrong instrument. Rewritten to four blows (*Nothing broke. Nothing
was expelled. Nothing leaked out of a better condition into this one. Nobody erred.*). CV 0.262 →
0.280, @1 0.481 → 0.489. **Small movement, and the edit was right even if it had moved nothing** —
which is the only defensible reason to make an edit a gauge asked for.

No further tuning. The axis stays open where the handoff put it: **re-measure at III.1.**
