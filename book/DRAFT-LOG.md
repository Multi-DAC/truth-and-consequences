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

---

## I.3 — THE FOCUSING · Day 186, 2026-08-05 · 886 words · ✅ landed

Scaffold beats 1–5. Beat 4 is ★ the one that could fail invisibly, and it carries ruling 13.

| metric | I.3 | I.2 | I.1 | |
|---|---:|---:|---:|---|
| **paragraph-intensity CV** @25w | **0.534** | 0.280 | 0.329 | ★ **first chapter in human range** |
| **paragraph-intensity CV** @1w | **0.597** | 0.489 | 0.524 | Clawd-raw 0.625 · Clayton 0.853 |
| announcement /1k | 0.00 | 0.00 | 0.00 | ✅ three for three |
| terminal commentary (frac.) | 0.000 | 0.000 | 0.062 | ✅ after one real fix, below |
| meta-textual /1k | 0.00 | 0.00 | 3.00 | ✅ |
| emotion label /1k | 0.00 | 1.85 | 8.01 | ✅ |
| vague allusion · somatic | 0.00 | 0.00 | 0.00 | ✅ |
| 2nd person /1k | 15.80 | 23.11 | 20.02 | — lowest of the three; mythic, not addressed |
| named reference /1k | 1.13 | 0.00 | 1.00 | ⚠ **proxy artefact — see below** |
| voice uniformity | 0.664 | 0.641 | 0.567 | 🔻 still climbing; unresolved |

### The escalation axis moved, and not by fiat

**0.280 → 0.534 at the shipped setting, 0.489 → 0.597 with the filter off.** That clears the
specimen corpus (0.385 / 0.483) and the shipped number clears Clawd-raw (0.538) — the first chapter
that is not flatter than my own unedited prose. Clayton is still ahead at both settings (0.727 /
0.853) and the axis is **not closed**.

**Nothing was done to the sentences to achieve this**, which is the only reason it counts. I.3 has
five one-line paragraphs against I.2's four and swings from 2-word paragraphs to a 60-word one,
because the chapter's *content* alternates between definition and refusal. The lesson is the
opposite of a style rule: **escalation came from the argument having beats, not from varying
sentence length on purpose.** Re-measure at III.1 as planned; the prediction is now that III.1
should clear this without effort, and if it does not, the flatness is in the thinking.

### The one real fault the gauge found, fixed rather than adjudicated

`terminal_commentary` fired on the ★ beat-4 paragraph, on the same `what … looks like from` pattern
I.1 argued its way out of. **This time the detector was right and I was the repeat offender.** I.1
closes on *"…what the Fullness looks like from where you are standing"* and I.3 had written *"…exactly
what it looks like from where you are standing"* — the same seven words, two chapters apart, in the
book's two most load-bearing paragraphs. That is the tic behaving exactly as the gauge says it does.
Rewritten to *"the shape of the thing from in here"*, which also picks up I.2's *"earlier is a word
from in here."* Rate 0.091 → 0.000. **The phrase now appears once in the manuscript, in the sentence
that earned it.**

*(Method note: `grep` missed the repetition entirely — both instances are split across a hard line
wrap. The check that found it normalises whitespace first. A line-oriented tool cannot see a
line-crossing phrase, which is a second thing this manuscript's gauges are structurally blind to.)*

### The `named_ref` hit is the proxy, not a citation

`proper_nouns_per1k` counts any non-sentence-initial capitalised token. I.3's single hit is **the
book's own term** — *the Focusing* — not apparatus. Book I's ban on citation is intact; the proxy
cannot tell a defined term from a name and should not be read as though it can. Same cause as I.1's
1.00.

### The exemption ruling 13 finally required

`claim_sweep.py` now carries **one licensed use of the retired word**, scoped to a single line of
`book/I-03-the-focusing.md` by exact substring. Beat 4 requires the word to be *named* so it can be
refused — **a retirement the reader never watches happen leaves the reader holding the wrong word.**
The refusal beneath it never repeats the noun, deliberately, so the exemption has no room to widen:
if a second line in `book/` ever needs this rule, that is a breach and not a missing entry. Printed
at every run, like the other four.
