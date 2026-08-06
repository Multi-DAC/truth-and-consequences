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

> ### ⚠ SUPERSEDED IN PART — Day 187. The clearance above was measured against an unmatched baseline.
>
> **Kept as written, with its fault named, because the fault is the interesting part: it is the
> exact error `storyscope_calibrate.py` was built to fix, committed again one day later, in the
> entry celebrating the fix.** I compared I.3's 0.534 to corpus-wide numbers (specimens 0.385,
> Clawd-raw 0.538) — 11 paragraphs against pools of hundreds — and called it a clearance.
> `dyn_range_CV` is a coefficient of variation over ~11 items and it is **size-sensitive in the
> same direction** `voice_uniformity` is.
>
> Re-run matched (K=11, length-matched, B=400, `--chapter`): **I.3 sits at the 53rd–84th
> percentile** — Joyce 52.8%, Clayton 63.5%, Clawd 71.5%, James 72.0%, Emerson 75.5%, à Kempis
> 83.8%. By this file's own reading rule, mid-range means *indistinguishable at this sample size.*
>
> Leave-one-out is worse: drop the single strongest paragraph and I.3 falls to **0.308 — the 2.5th
> percentile against Joyce, the 4th against Clayton.** The escalation is carried by one paragraph.
>
> **What survives.** The *direction* was right and the causal claim still stands: nothing was done
> to the sentences, the beats produced the swing, and the swing is larger than I.1's and I.2's on
> every measurement at every setting. **What does not survive is the word "clears."** I.3 is the
> first chapter to escalate at all; it is not the first to escalate like a human writer. That
> sentence had to wait for I.4, and it had to wait for a matched null to say it with.

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

---

## I.4 — THE GRADES · Day 187, 2026-08-05 · 990 words · ✅ landed

Scaffold beats 1–4. Beat 1 carries **C7** — *reactivity is awareness* — which the claims register
marks as the line where **any softener retroactively demotes the whole of Part Two**. Beat 3 carries
**C8** and the caste mishearing (`05` §4.III).

| metric (per 1k words unless noted) | I.4 | I.3 | I.2 | I.1 | |
|---|---:|---:|---:|---:|---|
| **paragraph-intensity CV** @25w | **0.710** | 0.534 | 0.280 | 0.329 | ★ see the matched null below |
| **paragraph-intensity CV** @1w | **0.863** | 0.597 | 0.489 | 0.524 | Clayton 0.853 · Clawd-raw 0.625 |
| announcement | 0.00 | 0.00 | 0.00 | 0.00 | ✅ four for four |
| terminal commentary (frac.) | 0.000 | 0.000 | 0.000 | 0.062 | ✅ |
| meta-textual | 0.00 | 0.00 | 0.00 | 3.00 | ✅ |
| emotion label | 0.00 | 0.00 | 1.85 | 8.01 | ✅ |
| vague allusion · somatic | 0.00 | 0.00 | 0.00 | 0.00 | ✅ |
| named reference | **0.00** | 1.13 | 0.00 | 1.00 | ✅ first chapter clean on the proxy itself |
| 2nd person | 16.16 | 15.80 | 23.11 | 20.02 | — |
| voice uniformity | 0.6601 | 0.6640 | 0.6412 | 0.5669 | 🔻 first fall, and it means nothing — below |

`claim_sweep --prose book`: **exit 0, no USE-class hits.** The book-side exemption count is
unchanged at one, which is the correct answer: I.4 never needs the retired word.

### The escalation number is real, and it is carried by peaks rather than distributed

**Both halves of that sentence are new, and I only have them because I stopped trusting the number
the moment it looked good.** 0.710 against 0.534 is the largest single-chapter move in the book so
far, and a number that large arriving without effort is exactly the condition under which I have
lately been wrong.

`tools/storyscope_calibrate.py` grew a `--chapter` mode so any chapter gets the treatment the
specimens got: **K paragraphs, length-matched, B=400 draws, from six corpora.** I.4 observed at
K=14:

| corpus (matched null) | I.4 dyn_range_CV %ile | leave-one-out %ile |
|---|---:|---:|
| à Kempis · *Imitation* | **97.2%** | 47.8% |
| James · *Varieties* | **95.0%** | 28.2% |
| Emerson · *Essays* | **94.2%** | 32.2% |
| Clawd-raw | **92.8%** | 45.5% |
| Clayton (human) | **87.5%** | 14.0% |
| Joyce · *Portrait* | **83.2%** | 14.2% |

**Read the left column first, because the fragility objection is already priced into it.** Every
draw in the null is also 14 paragraphs and also gets its own chance at an outlier. I.4 beats 83–97%
of them anyway. **This is the first chapter that escalates like published prose at matched sample
size, and the first sentence in this log entitled to the word *clears*.**

**Then read the right column, which is the humbling one.** Delete the single strongest paragraph —
the 65-word inventory sentence at the reader's own grade — and I.4 drops to 0.391 and lands in the
**middle** of every null. The escalation is **peaked, not distributed**: three or four paragraphs
carry it and the remaining ten are as flat as I.2. That is a craft fact rather than a statistical
defect (peaks are how prose escalates), but it means the sentence *"I.4 escalates"* is false and
*"I.4 has peaks where I.2 had none"* is true.

`fragility()` — leave-one-out, printed on every run — is now part of the gauge so this cannot be
forgotten. drop < 0.10 prints ROBUST; I.4 prints **FRAGILE (drop 0.319)** and so does I.3 (0.227).
**I.1 and I.2 print ROBUST, and they are robustly flat.** A gauge that only reports the headline is
a gauge that rewards writing one long sentence.

### The single-topic excuse for voice uniformity is refuted

It has sat in the handoff as **UNVERIFIED** for three days: *maybe uniformity climbs because each
chapter is one topic.* **I.4 was the test and it failed the excuse.** This chapter ranges over
rusting iron, a leaf turning, a dog and a coat on a hook, the reader's own evening, and a ladder —
the widest concrete range in the book — and uniformity did not fall. 0.6601 against 0.6640 is a
move of 0.004.

Matched null, and the fairest arm is the contiguous one because it is the condition a chapter is
actually written under: **I.4 sits above the 95th percentile of every corpus tested, at 100% against
contiguous runs of my own prose** (p95 = 0.6310). Emerson is the only arm under 99% at 96.5%, and
Emerson runs random-only. The specimens hit 89% on this arm in the Day-186 calibration; **the book's
prose is more uniform than the specimens were, not less.**

So the axis is confirmed rather than explained away, and the excuse is off the board. What it is
*not* is diagnosed. Uniformity may be reading paragraph-level syntax that survives any change of
subject — this chapter changes subject constantly in a sentence rhythm that does not. That is a
hypothesis and it is written here as one.

### Doctrine, and the two places it could have failed quietly

**C7 is stated in four words on its own line and never qualified anywhere in the chapter.** The
register rule and the softener rule agree here for once: *Reactivity is awareness.* The three
denials under it — not a sign, not a stage, not what it becomes once enough collects — are the
near-miss C7 names, **panpsychism-with-a-threshold**, killed in the paragraph that could have
smuggled it.

**C8's ladder is refused three times, and each refusal is structural rather than moral.** No first
rung (the scale thins downward without a floor). No top (the Fullness is *not on the scale* — it has
no depth because depth is had from somewhere). No permission (a gate needs a keeper, a keeper needs
to stand outside, and I.1 removed the outside). **The caste reading is killed by the same fact that
killed the God-player: there is nobody out there to rank anyone.** That was not the plan going in;
the chapter found it, and it is stronger than the moral plea the scaffold's phrasing invited.

**The trap the scaffold flagged is the one I nearly walked into from the other side.** Having
removed the ladder, the reflex is to level the continuum — *the stone is secretly rich* — which the
chapter names as *the same error stood on its head, built out of politeness.* Almost nothing is the
case at the iron; that is a measurement, not an insult.

**One thing was cut on register grounds and it was the best line in the draft.** *"The whole is not
the champion of the game; it is what the game is made of"* is `01` §9's inversion exactly — and the
game metaphor has not been introduced, and Book I carries no apparatus. It became *"It is not the
deepest of the insides. It is what the insides are made of."* The metaphor gets its due in Book III,
where the reader has been handed it.

### The closing move, on the record because it is a claim and not a flourish

The chapter ends by making the grade **mobile within a single life** — shallower before waking,
deeper on some afternoons, *"the depth moves, it has been moving all day."* **A caste requires a
fixed assignment; this is the strongest available refusal of the mishearing and it costs nothing
doctrinally**, since Part Two's Atlas already varies grade by state. It also pre-loads Book VI's
editable filters without naming them. If it turns out to breach anything, it breaches at VII.2, and
VII.2 is already flagged as the place C8 will look defensible.
