# RESULT — Specimen 1-C, scored against PREDICTION-1C.md

*Day 186, ~15:30. Run: `python tools/storyscope_pair.py`. Predictions were filed and committed
before the gauge saw 1-C.*

## Scorecard against the pre-registration

| # | Prediction | Result | |
|---|---|---|---|
| 1 | whole-chapter voice_uniformity within ±0.010 of 1-B's 0.5610 | **0.5563** (−0.005) | ✅ |
| 2 | announcement_/1k unchanged from 1-B (3.14) | **3.17** (denominator only) | ✅ |
| 3 | terminal_commentary stays 0.00 | **0.00** | ✅ |
| 4 | paragraph-local: cutting the "I" reverts toward S1, mean gain ≥ +0.010 | **−0.0289, sign reversed** | ❌ |
| 5 | coverage reported, VOID below 70% | 88.3% both — no VOID triggered | ✅ |

## The finding: my claim is withdrawn

**"Neither intrusion can be cut without the paragraph going back to sounding like the
original" is unsupported, and the only measurement with power points the other way.**

The flinch paragraph (n=65w, the sole adequately-powered arm) moved *away* from Specimen 1
when the narrator was removed: cos 0.7472 → 0.7183. The confession arm gained +0.0715 but is
19 words long, was flagged under-floor before the run, and a function-word vector at that
length is noise. It is excluded, at any weight.

**Clayton read this off the page in one line and was right. I built a ruler and was wrong.**

## The correction that matters more than the verdict

1-B's announcement rate doubled against Specimen 1 (1.61 → 3.14/1k). Yesterday I called that
"the cost of speaking voice" and framed it as a trade. **Wrong attribution.** The lexicon dump
names the actual culprits:

    S1  : ['the one admission']
    1-B : ['what follows', 'Now the']
    1-C : ['what follows', 'Now the']   ← identical with the narrator gone

Neither hit is the narrator's. Both are *structural*: a thesis sentence ("…is what follows
from it") and a paragraph that announces its own arrival ("Now the confession…"). Speaking
voice did not raise the announcement rate. **Two removable constructions did**, and they
survive the narrator's removal untouched — which is why removing the "I" bought nothing back.
Open craft item, not a register problem.

## What did carry the spokenness

Second person survives at 14.29/1k against Specimen 1's 8.05. Terminal commentary stays at
zero. Eight paragraphs are short beats. **Imperative + second person + short beat carry
address; a speaker is not required to have a listener.** That is the Silmarillion's own
arrangement, and Specimen 1 already had the device before 1-B replaced it with a person: *"the
one admission the telling owes"*, *"it is said once more, flatly."* A telling can owe things
without being someone.

## A defect in the instrument, found by the instrument

The first run printed **"MEAN GAIN = +0.0213 → claim SURVIVES."** That verdict was produced
entirely by the 19-word noise arm outvoting the 65-word arm in an unweighted mean of two.
A gauge emitting a clean verdict it has no power to emit — Day 186's recurring law, committed
by the tool written that morning to catch it. `storyscope_pair.py` now gates arms by n,
excludes under-floor arms from the verdict rather than down-weighting them, and returns
INDETERMINATE when powered arms disagree in sign.

**Had I not fixed it, the tool would have told me I was right.**

## Open, and Clayton's

The gauge cannot rule on whether 1-C still *sounds* spoken. Nothing here can. That is a human
read on the prose, and it is the only remaining question in the register/narrator ruling.
