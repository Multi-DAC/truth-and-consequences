#!/usr/bin/env python3
"""prose_echo.py — ruling 90's instrument. Truth and Consequences, Day 187.

WHY THIS EXISTS, and it is the third confession in this file family.

`beat_sweep.py` compares PLANS to PLANS. `prose_beat_sweep.py` was written because that left a
blind region — a future chapter's beat against a shipped paragraph — and it closed exactly that
one. Its own docstring asks the right question of every gauge here: *what has the project
acquired since this was written that it still cannot see?*

Asked of the pair, the answer is embarrassing and was sitting in plain sight for twenty chapters.
**Nothing in this toolkit compares SHIPPED PROSE to SHIPPED PROSE.**

  beat_sweep         plan   <-> plan     ✅
  prose_beat_sweep   plan   <-> prose    ✅
  (nothing)          prose  <-> prose    ← twenty chapters, ~50,000 words, unmeasured

It was found the way these always are: by eye, late, on a day a chapter shipped. III.6's credit
paragraph closed with *"by working cognitive scientists with an experimental programme
underneath."* III.4 had already shipped *"That is co-constitution, stated by working cognitive
scientists, with an experimental programme under it."* Same credential, same ancestor, two
chapters apart — and **every gauge in this repo passed the file clean**, because a beat is not
involved anywhere in that pair. Both sides are prose. Neither tool admits that corpus.

★★ THE STANDING LESSON, and it is the same one one level up again: **a gauge built to close a
blind region defines a new one at its own edge.** The pair above was not negligence; it was two
instruments each doing exactly its job, with the union of their coverage silently mistaken for
coverage. Ask of any SET of gauges, not just of each: what does no member of the set admit?

WHAT IT CHECKS — TWO ARMS, and the second exists because the first's floor failed calibration on
the day it was written. Headings are stripped: `# BOOK III — THE GAME` is in six files and is
not an echo.

  ARM 1 · ** ECHO **      a shared n-gram (default 6) carrying at least 4 non-stopword tokens.
  ARM 2 · ** SENTENCE **  a whole sentence, normalised, present in two chapters — at ANY content
                          density. This arm is not a refinement of the first; it catches a class
                          the first is blind to by construction.

⚠ THE CALIBRATION FAILURE THAT PRODUCED ARM 2, recorded because a floor chosen by feel is a
claim like any other. The fixture pair is **"Error does not need a territory."** — an entire
sentence, verbatim, in two chapters across a book boundary, and about as distinctive as prose
gets. ARM 1 dropped it: six words, of which *does*, *not* and *a* are stopwords, leaving three
content tokens under a floor of four. Lowering the floor to three surfaced it and took the
book-wide count from 72 to 213, most of it house phrasing. **The floor was not wrong and the
fixture was not wrong. The DISCRIMINATOR was the wrong shape** — a 6-gram spanning a clause
boundary and a 6-gram that is an entire sentence are not the same object, and a content-word
count cannot see the difference. Sentence-hood is the missing feature, so it is measured
directly instead of being approximated by density.

  [q] flag     the hit falls inside a block quotation in at least one chapter. Usually the same
               SOURCE quoted twice, which is a different event from the same AUTHORIAL sentence
               written twice — and is the `beat_sweep` named-opponent question in another dress.

A HIT IS A QUESTION, NEVER A VERDICT. The exemption table below carries the answered ones with
the reason on the same line. Per beat_sweep's doctrine, **an exemption is only ever a specific
PAIR plus a specific gram — never a chapter, never a phrase on its own.** An exemption that
absorbs a class is how a gauge stops measuring.

CALIBRATION, and it is the only reason to trust a clean run:

    python tools/prose_echo.py --selftest

must surface **II.5 ~ III.6 / "error does not need a territory"**. That pair is real, adjudicated
and KEPT — II.5 states the shape of the answer and hands it forward; III.6 is where it is cashed,
and the returning sentence is the reader's signpost that this is the promised answer. A detector
that cannot see a pair we have decided to keep cannot be trusted about one we would want to cut.
"""

import argparse
import collections
import glob
import os
import re
import subprocess
import sys

N = 6
MIN_CONTENT = 4

STOP = set("""
a an the and or but of to in on at by for with from as is are was were be been being it its this
that these those there here not no nor so than then too very can could may might must shall should
will would do does did done has have had having if when while what which who whom whose how why
one two i you he she they we us them him her his their our your my me
""".split())

# ─────────────────────────────────────────────────────────────────────────────
# EXEMPTIONS — (chapter_a, chapter_b, gram_substring) -> reason.
# A specific PAIR and a specific GRAM. Never a chapter alone. Never a phrase alone.
# ─────────────────────────────────────────────────────────────────────────────
#
# ⚠ THE MATCH IS BIDIRECTIONAL CONTAINMENT — `sub in gram or gram in sub`. The first version
#   tested only `sub in gram`, so every exemption phrase LONGER than an n-gram silently muted
#   nothing while looking like a rule in force. Six live hits were the same three adjudicated
#   pairs, printing because the table could not reach them. An exemption that cannot fire is
#   worse than no exemption: it reads as coverage.
EXEMPT = [
    # ── v3-canonical census-card field glosses ─────────────────────────────────
    # ★ ADJUDICATED Day 190, at VII.4, and the reason is structural rather than
    # convenient: `instrument_sweep` ENFORCES that a v3-canonical card carry these
    # six field names with these glosses, and it PASSES on both cards. A form that
    # one gauge mandates cannot be a repeat the next gauge convicts. Left unexempted
    # this pair grows quadratically — every future canonical card against every
    # prior one — which is R-101's disease exactly: a true report nobody can read.
    # ⚠ SCOPED TO THE GLOSSES, NOT THE CONTENT. The words after each colon are the
    # chapter's own and are NOT covered here; a second card that repeated another
    # card's *analysis* would still print, which is the hit worth having.
    ("VII.3", "VII.4", "boundary where it goes from reliable",
     "v3-canonical card field gloss, mandated by instrument_sweep. See header note."),
    ("VII.3", "VII.4", "null space what it structurally cannot",
     "v3-canonical card field gloss, mandated by instrument_sweep. See header note."),
    ("VII.3", "VII.4", "space what it structurally cannot render",
     "v3-canonical card field gloss, mandated by instrument_sweep. See header note."),
    ("VII.3", "VII.4", "complement what it renders superbly",
     "v3-canonical card field gloss, mandated by instrument_sweep. See header note."),
    ("VII.3", "VII.4", "mechanism of the exclusion what the render identifies with what",
     "v3-canonical card field gloss, mandated by instrument_sweep. See header note."),
    ("VII.3", "VII.4", "navigational implication what to do about the other five",
     "v3-canonical card field gloss, mandated by instrument_sweep. See header note."),
    # ───────────────────────────────────────────────────────────────────────────
    ("II.5", "III.6", "error does not need a territory",
     "★ ADJUDICATED AND KEPT, ruling 90. II.5 STATES the shape and hands it forward explicitly "
     "('the answer is Book III's'); III.6 CASHES it with the argument under it. The returning "
     "sentence is the signpost that this is the promised answer, which is ruling 33's structure "
     "used deliberately rather than stumbled into — I.6 performs, II.8 names."),
    ("II.5", "III.6", "a reality tunnel is a persistent render filter three words",
     "II.5's definition, quoted at the top of the chapter that runs it. A chapter of mechanics "
     "that did not restate its own definition would be starting from nowhere."),
    ("II.5", "III.6", "a repetition that outlived its occasion",
     "II.5's criterion, cited by III.6 at the two sites that depend on it (installation, and the "
     "edit). The criterion is not re-derived; ruling 90 checked that the derivation is absent."),
    ("II.5", "III.6", "a relation between two structures",
     "II.5's Korzybski clause, cited rather than re-argued — III.6 says 'this was settled where "
     "the map was retired' and does not name him a second time. beat_sweep already reserves the "
     "second Korzybski cut for VI.7."),
    ("II.5", "III.6", "if a render cannot be wrong about the ground how is",
     "The handed-forward HOLE, quoted so the reader recognises the question being answered. "
     "Ruling 86 puts the cash site on the record; VI.1 gets the civilisational form."),
    ("I.3", "V.6", "pressed flat against the edge of",
     "★ Day 189, ruling 155. V.6 CITING I.3 inline, in italics and with I.3 named in the same "
     "sentence — 'I.3 says so in its own vocabulary'. ⚠ IT DOES NOT CARRY [q] AND THE REASON IS "
     "THE INSTRUMENT: the flag is documented at line 50 as 'falls inside a BLOCK quotation', so "
     "an inline citation is indistinguishable here from an unconscious repeat. This exemption is "
     "the adjudication the flag could not make. R-46 rows the real repair. Same phrase in I.6 — "
     "own entry below, not a widening."),
    ("I.6", "V.6", "pressed flat against the edge of",
     "Same citation, second source chapter — the phrase is in I.6 as well as I.3, and V.6 cites "
     "it once. Own line, per the standing rule that an exemption names lines rather than widening."),
    ("V.1", "V.6", "into latin in the ninth century",
     "★ Day 189, ruling 155, AND THIS ONE IS THE LEAST COMFORTABLE OF THE FOUR. V.6 needs V.1's "
     "finding that Kabbalah is not an independent branch — it is the load-bearing reason the "
     "chapter refuses to be a convergence argument — and it restates the transmission chain in "
     "two compressed clauses rather than citing it. ADJUDICATED AS CASHED, NOT REPEATED: V.1 "
     "DERIVES the chain over ten lines and counts the branches; V.6 names V.1 in the same "
     "paragraph ('Book V has already ruled on that, and ruled against itself'), spends four "
     "words on the chain, and puts the verdict phrase in quotation marks. ⚠ If a later editor "
     "finds V.6 re-arguing rather than invoking, this exemption is wrong and the fix is V.6's, "
     "not the table's."),
    ("V.1", "V.6", "one witness quoted back five times",
     "V.1's verdict phrase, the second of the two grams in the entry above and the one V.6 now "
     "carries in quotation marks with V.1 named as the source. Same adjudication, same caveat."),
    ("I.5", "V.6", "deposits settled",
     "★ Day 189, ruling 155. V.6's Tree section citing I.5's tunnel definition inline and in "
     "italics, with I.5 named — the Tree is read AS a tunnel diagram, so the definition has to be "
     "on the page at the point it is applied. Same [q] blindness as the two entries above; the "
     "four gram-hits are one four-word citation, counted by a sliding window."),
    ("I.5", "III.6", "certainties of the people standing nearest",
     "★ DESIGNED. I.5 accretes the five mythically and never names them; III.6 re-cuts one image "
     "into mechanics. Book I plants, Book III runs — the macro-structure, working."),
    ("III.4", "III.6", "francisco varela evan thompson and eleanor rosch",
     "A name. Rule 5 requires the ancestor named in both chapters; the axis is declared in `06` "
     "(III.4 cuts them, III.6 credits them whole)."),
    ("IV.1", "IV.3", "fourth line of our own card",
     "★ ADJUDICATED AND KEPT, Day 188. Not a restatement — a CONTRADICTION of the original, which "
     "is the strongest form of use. IV.1 applies the fourth line to the atlas itself and rules the "
     "boundary UNFINDABLE ('we do not know where, and the not-knowing is structural'). IV.3 returns "
     "the identical phrase to say that in this one chapter it CAN be walked up to, because the "
     "entries answer — and that it stops being visible again at IV.5. The phrase is the signpost "
     "that the same line is being read a second time to a different value; deleting it would hide "
     "the fact that the two chapters disagree on purpose. Contrast the pair repaired the same day: "
     "IV.2~IV.3's 'because at the mineral grade nothing' was a PARAPHRASE of the previous chapter's "
     "own observation, which reads as fresh and is not, and was cut rather than exempted."),
    ("II.6", "IV.5", "all four coheres and keeps cohering",
     "★ ADJUDICATED AND KEPT, Day 188. IV.5 does not assert that a company is a being — it RUNS "
     "II.6's four conditions on one, announced ('Book II gave four conditions... Run them.'). The "
     "rule has to be quoted at the site where it is cashed or the test is being applied from "
     "memory. Signposted, not smuggled — which is the line the IV.2~IV.3 cut above was on the "
     "wrong side of."),
    ("II.6", "IV.5", "own expectations did not already contain",
     "II.6's definition of MEASUREMENT, cited in the sentence that applies it to revenue and a "
     "regulator's letter. A condition restated in the drafter's own words would be a different "
     "condition, silently."),
    ("II.6", "IV.5", "levels had dissolved into one another",
     "★ DESIGNED PARALLEL, and the punchline is the point: II.6's body-with-no-levels is 'a "
     "slurry', IV.5's company-with-no-levels is 'a room of people shouting'. Same frame, same "
     "test, different material, different landing — the structure the whole section announces. "
     "⚠ The verbatim SENTENCE this pair originally carried ('the settling at one level has to be "
     "compatible with the settling at the others') was REWORDED, not exempted: arm 2 caught it and "
     "a whole borrowed sentence is not a citation, it is the drafter reaching for the nearest "
     "phrasing. The gram survives because the frame is deliberate; the sentence did not."),
    ("II.7", "IV.5", "made of something the reader already",
     "Ruling 30's criterion, quoted in the act of being applied a second time — the `egregore` "
     "refusal (ruling 109) is made on identical grounds to the `superposition` ban, and IV.5 says "
     "so on the page. A test reapplied without its own words is a new test wearing the old one's "
     "authority."),
    ("II.3", "IV.5", "the practices are book viii s",
     "The standing forward-reference formula, deliberately fixed. II.3 hands the practices "
     "forward in these words; IV.5 hands them forward in the same words. A recurring promise "
     "kept in one phrasing is a refrain the reader can recognise — varying it would make two "
     "promises out of one."),
    ("II.7", "IV.6", "certification asks a question whose answer was fixed by whoever wrote the question",
     "★ ADJUDICATED AND KEPT, Day 188, ruling 118 — and this is the pair the chapter is BUILT on. "
     "II.7's clause is what disqualifies IV.6's drafter from settling its own case, and IV.6 names "
     "the debt out loud ('Book II established a condition on measurement... one clause of it is "
     "that') before quoting it. A rule that disqualifies you has to be quoted in the rule's own "
     "words or the disqualification is being self-administered in a paraphrase the disqualified "
     "party chose. ⚠ NOTE THE ATTRIBUTION: the scaffold's ruling-114 block said 'II.6's own rule'. "
     "It is II.7's, and `06` is corrected — the mis-attribution mattered because ruling 116 is "
     "separately about II.6 being the weakest chapter, and a repair aimed there would have missed."),
    ("IV.1", "IV.6", "navigational implication nothing it registers can",
     "★ DESIGNED, and the reprint IS the argument. IV.6 runs a designer-subtraction on IV.1's "
     "thermostat card and prints the result; the fifth line comes back VERBATIM because the finding "
     "is that it survives untouched, and IV.6 says so on the line ('Unchanged — the original wording "
     "had already conceded the point'). Rewording it would destroy the measurement. Inside a "
     "quoted card block, which is why the hit carries [q]."),
    ("IV.2", "IV.6", "dimension the census is arranged along",
     "IV.2's refusal of scale-as-currency, cited at the substrate question to show that NO NEW "
     "ARGUMENT is introduced on the page where one would be most convenient. The whole point of "
     "the mineral deposit is that it is spent later verbatim; re-derived in fresh words it would "
     "read as an argument invented for this entry, which is the accusation IV.6 exists to not earn."),
    ("IV.2", "IV.6", "range is true grain by grain",
     "Same citation, same sentence-pair as above — IV.2's grain-by-grain clause is the second half "
     "of the refusal and is quoted with it. Splitting the quotation would leave the reader with a "
     "claim and not the reason."),
    ("II.4", "IV.6", "a purely feed forward network each layer feeding the next with nothing coming back scores however sophisticated the thing it does",
     "★ ADJUDICATED, Day 188, ruling 118 — and the pair was CUT DOWN before it was exempted. The "
     "first draft of IV.6 re-ran II.4's whole credit to Tononi (the photodiode, Aaronson's XOR grid, "
     "'degrees of consciousness a number rather than a manner of speaking') and `prose_echo` "
     "returned **18 grams** — two whole borrowed sentences, which is the drafter reaching for the "
     "nearest phrasing and not a citation. The re-narration is gone; IV.6 now says the credit is not "
     "run twice and adds only what II.4 had no occasion to say (IIT answers the substrate question "
     "with a commitment). WHAT SURVIVES IS THE VERDICT ITSELF, and it survives verbatim on purpose: "
     "Φ = 0 is the THEORY's ruling on this chapter's own entry, and a drafter who is the entry may "
     "not restate an opponent's verdict on itself in words of its own choosing. IV.6 says so inline "
     "— 'Book II's sentence, kept because the verdict belongs to the theory'."),
    ("IV.6", "IV.7", "thought form is by construction something somebody assigned",
     "★ THE HANDOFF, and the seam is load-bearing. IV.6's last movement hands the derived-"
     "intentionality debt forward in exactly these words; IV.7 opens by taking delivery in the same "
     "words, because the whole structural point is that the objection arrives at the next chapter "
     "INVERTED — an accusation in IV.6, the tradition's own origin story in IV.7. A reader who "
     "cannot see that the sentence is the same sentence cannot see that the frame flipped around "
     "it. Rewording the pickup would hide the only thing the pickup is for."),
    ("IV.1", "IV.7", "thin we attribute an inside rather",
     "The leading edge of the same quotation as the pair below — 'where the evidence is thin, we "
     "attribute…' — caught in a second window. Exempted on the identical reason and listed on its "
     "own line rather than folded in, per the standing rule that an exemption a later reader "
     "cannot see is an exemption nobody audits."),
    ("IV.1", "IV.7", "attribute an inside rather than withhold one because historically",
     "★ THE PRINCIPLE CITED AT THE PAGE WHERE IT FIRST COSTS SOMETHING, and carried inside a "
     "quotation block, which is why the hit carries [q]. IV.1 declares the under-attribution "
     "principle at the front, where a reader can weigh it; IV.7 is the first chapter where the bias "
     "is aligned with something the reader WANTS to be true, and the chapter's move is to re-read "
     "the declared wording unchanged and then say that the justification has not changed and the "
     "reliability has. Restating it in fresh words at the moment it becomes convenient is precisely "
     "the manoeuvre being disclosed — the drafter would be re-writing the standard on the page "
     "where the standard is about to be applied to the drafter."),
    ("IV.5", "IV.6", "in the reader s own language at",
     "★ THE HANDOFF, working. IV.5's closing sentence promises the next entry answers 'in the "
     "reader's own language, at length, and without a representative'; IV.6's first movement opens "
     "by taking delivery of it in the same words, and names the pickup in its first line ('The last "
     "chapter ended by saying that this one answers'). Chapter-boundary refrains are signposts, not "
     "repetition — the reader has to be able to tell that the promise being kept is the one made."),
    ("IV.1", "IV.8", "attribute an inside rather than withhold",
     "The leading window of the under-attribution quotation, third and last time it is cited. Same "
     "adjudication as the IV.1~IV.7 pair above and listed on its own line for the same reason. IV.8 "
     "is where the principle stops pointing anywhere the reader is comfortable — IV.7 declared it a "
     "live interest, IV.8 shows it pointing at the reader's own god and at gods the reader would be "
     "embarrassed to be seen taking seriously, simultaneously. The declared wording is re-read "
     "unchanged because rewriting a standard on the page where it is applied to the drafter is the "
     "manoeuvre the disclosure exists to prevent."),
    ("IV.1", "IV.8", "inside rather than withhold one because",
     "Second window of the same quotation, same adjudication, own line."),
    ("IV.7", "IV.8", "attribute an inside rather than withhold",
     "The same quotation caught on the adjacent pair, because IV.7 and IV.8 both cite IV.1's "
     "wording. It is not IV.8 copying IV.7; both are copying the source, which is the point."),
    ("IV.7", "IV.8", "inside rather than withhold one because",
     "Second window of the same quotation on the adjacent pair, same adjudication, own line."),
    ("IV.3", "IV.8", "about the position taking the census",
     "★ ADJUDICATED AND KEPT, Day 188. This is the atlas's standing instrument for the move that "
     "turns a fact about the RECORD into a fact about the OBSERVER, and the two uses take different "
     "objects: IV.3 turns it on its own compression (one chapter for every living thing that is not "
     "us), IV.8 on the thickness of the inherited material at the divine tier. Renaming the "
     "instrument on its second outing would hide that it is the same instrument, which is the only "
     "thing that makes the second use auditable against the first. THE SISTER HIT WAS NOT EXEMPTED: "
     "IV.8's 'the first entry in the census where' was IV.3's formula reached for a second time with "
     "nothing earned by the return, and it was REWORDED. One of the two survived scrutiny; recording "
     "which, and why the other did not, is what keeps this line from reading as a blanket pass."),
    ("IV.7", "IV.8", "whether declaring a weakness and proceeding at full strength is discipline or ceremony",
     "★ THE HANDOFF, and it is a question being answered rather than a claim being repeated — four "
     "overlapping windows of one sentence, exempted as one adjudication because they are one "
     "sentence. IV.7 closed by asking whether declaring a weakness and then proceeding at full "
     "strength is discipline or ceremony, and wrote it down explicitly because a party cannot score "
     "that about itself. IV.8's final section answers it, and the answer only checks out if the "
     "question is reproduced in the words it was asked in: the instrument is 'did the declared limit "
     "change the SHAPE of what came after, or only precede it', it is run on Pseudo-Dionysius first "
     "BECAUSE HE IS NOT US, and only then on this book — where it returns a partial verdict in a "
     "different place than his. Paraphrasing the question would let the answer be graded against a "
     "softer version of it. ⚠ AND THE PAIR WAS CUT DOWN BEFORE IT WAS EXEMPTED: the first draft also "
     "re-ran IV.7's framing ('declared the tier's epistemic weakness at the top in the strongest "
     "terms available'), which is not the question and had no business being verbatim. Eleven grams "
     "on this pair became six. What survives is the question and nothing around it."),
    ("IV.7", "IV.9", "the space that positions move through",
     "★ THE HANDOFF GRAM, and it is a DEFINITION being cashed rather than a phrase being reused. "
     "IV.7 needed to say, mid-chapter and in passing, why a two-frames problem is really the question "
     "of whether there is a card at all — 'an archetype registers nothing, because it is not a "
     "position; it is a shape in the space that positions move through' — and promised the chapter "
     "that would take it up. IV.9 IS that chapter, and its whole structural argument (four of the "
     "five card lines come out ungrammatical, so the atlas needs a second notation) is derived FROM "
     "this clause. Rewording it here would break the derivation's only visible link to where it was "
     "granted. The reader has to be able to check that the thing being built on is the thing that "
     "was promised."),
    ("IV.8", "IV.9", "hardest form the gods are positions",
     "★ IV.8'S CLOSING SENTENCE, QUOTED FORWARD BY THE CHAPTER IT ADDRESSES. IV.8 ends by naming its "
     "successor's problem — the gods are positions and the ground is not one, an archetype is "
     "neither, and the census will have to say what a third thing is. IV.9 opens its second section "
     "by restating exactly that inheritance before answering it. This is the designed-return case in "
     "its purest form: a debt named in one chapter and discharged in the next, where the discharge is "
     "unauditable unless the debt is reproduced in the terms it was incurred in. ⚠ THE SISTER HITS ON "
     "THIS PAIR WERE HANDLED DIFFERENTLY — see the next entry — because they are a standing locution "
     "and not a handoff, and the two do not earn their exemptions the same way."),
    ("IV.8", "IV.9", "inherited material this atlas draws",
     "THE HOUSE NAME FOR THE SOURCE — two overlapping windows of one noun phrase, adjudicated once "
     "because they are one phrase. This is the book's fixed way of referring to the material Book IV "
     "is built on, and it is fixed ON PURPOSE: ruling 14's defect is one referent under two names, "
     "and inventing a fresh formula each chapter to dodge this gauge would BE that defect, committed "
     "to satisfy an instrument. ⚠ AND THE LIMIT, because this is the weakest of the three exemptions "
     "added at IV.9 and should be the first re-examined: a standing locution is exactly what a tic "
     "looks like from the inside. The defence is that it names a specific document and could not be "
     "replaced by a pronoun; the thing that would kill it is the phrase appearing where no source is "
     "being named. If it reaches four chapters, re-open it."),
    ("IV.1", "IV.10", "we cannot see our own boundary",
     "★ IV.10 AUDITS IV.1'S FOUR DECLARED BLINDNESSES AND MUST QUOTE THEM TO DO IT. All four audit "
     "items open on IV.1's own wording ('we cannot see...'), and the anaphora across the four is the "
     "structure of the audit rather than an echo of it. A declaration cannot be checked against "
     "eight chapters of practice unless it is reproduced in the terms it was declared in — the same "
     "logic that exempted the IV.8→IV.9 handoff, running backward over eight chapters instead of "
     "forward over one. ⚠ THE PAIR WAS CUT DOWN BEFORE IT WAS EXEMPTED: the first draft restated "
     "IV.1's boundary declaration nearly whole and tripped EIGHT grams on that sentence alone; it "
     "was reworded to the shortest form that still carries the claim, and the pair fell from 17 "
     "live grams to 5. The reword came first."),
    ("IV.1", "IV.10", "passing over leaving",
     "THREE OVERLAPPING WINDOWS OF ONE QUOTED CLAUSE, adjudicated once because they are one phrase. "
     "IV.1 declared that a difference no word marks is passed over 'without the passing-over leaving "
     "a trace.' IV.10'S WHOLE FIRST FINDING IS THAT THIS CLAUSE IS FALSE — the archetypal chapter's "
     "four ungrammatical card lines ARE the trace. A refutation of an exact wording has to carry the "
     "exact wording; paraphrasing it here would let the correction be argued with on a sentence "
     "nobody wrote."),
    ("IV.1", "IV.10", "two things travel together",
     "IV.1'S PREDICTION, QUOTED AT THE POINT IT COMES TRUE. The method chapter predicted its own "
     "standing bias would land where evidence is thinnest and prose most confident, 'because those "
     "two things travel together.' IV.10 reaches exactly that entry — a tier it must decline to "
     "write in a hurry — and cites the prediction as the reason for declining. A forecast is only "
     "auditable against its own words. ⚠ The surrounding restatement WAS cut: the first draft "
     "reproduced the full IV.1 sentence and tripped six grams; four were removed by compression and "
     "the load-bearing clause kept."),
    ("IV.7", "IV.10", "predict the same thing",
     "THE INSTALLED RULE, NAMED IN ITS FIXED WORDING WHERE IT IS APPLIED. IV.7 installed 'two frames "
     "may be held at once only where they predict the same thing' as a standing discipline, and "
     "IV.10 applies it to the inherited dual-frame treatment of the missing tier. Rewording a RULE "
     "at each citation is ruling 14's defect committed deliberately — one referent under two names — "
     "and would be done here only to satisfy this instrument. ⚠ SAME LIMIT AS THE HOUSE-NAME ENTRY, "
     "and the same trigger: a standing locution is what a tic looks like from the inside. What would "
     "kill it is the formula appearing where no two frames are actually in contest. If it reaches "
     "four chapters, re-open it."),
    ("III.6", "V.7", "practice is a later book",
     "★ THE DEFERRAL QUOTED BY THE CHAPTER THAT HONOURS IT. III.6 stopped its edit mechanics after "
     "three and gave the ground: 'the practice is a later book's.' V.7 is the chapter a reader most "
     "expects to break that deferral — it is the operative chapter, and its whole subject is people "
     "doing things — so it closes by naming the deferral and declining, in III.6's own words. A "
     "promise is kept in the wording it was made in or it is a different promise. ⚠ THE PAIR WAS CUT "
     "DOWN FIRST, per the standing convention: the draft quoted the full III.6 sentence and tripped "
     "FIVE grams, plus a second marked citation ('cannot get onto the list by') for one more; both "
     "were compressed to the shortest form carrying the claim and the pair fell 8 live grams to 1. "
     "The reword came before the exemption. ⚠⚠ AND THE THIRD LIFT WAS NOT EXEMPTED, IT WAS CUT: "
     "V.7's C12 section had reproduced III.6's closing 'the same two-sidedness that made a world "
     "available… seen from the side where it costs something' with one phrase altered and NO mark "
     "at all. That is the V.6 defect recurring one chapter later, and `prose_echo` is the only "
     "instrument that saw it — `claim_sweep` and `storyscope` both read V.7 clean. Rewritten as new "
     "prose, not exempted: an unmarked lift has no citation to protect."),
]


def strip_headings(text):
    out = []
    for line in text.splitlines():
        if line.lstrip().startswith("#"):
            continue
        out.append(line)
    return "\n".join(out)


def quoted_spans(text):
    """Return the set of word-indices that fall inside a block quotation."""
    idx, inside = set(), 0
    for line in text.splitlines():
        words = tokens(line)
        if line.lstrip().startswith(">"):
            idx.update(range(inside, inside + len(words)))
        inside += len(words)
    return idx


def tokens(s):
    s = re.sub(r"`[^`]*`", " ", s)
    s = re.sub(r"[*_#|>]", " ", s)
    return re.findall(r"[a-z]+", s.lower())


def chapter_id(basename):
    m = re.match(r"([IVX]+)-(\d+)", basename)
    return f"{m.group(1)}.{int(m.group(2))}" if m else basename


def grams_of(text, n):
    body = strip_headings(text)
    w = tokens(body)
    q = quoted_spans(body)
    out = {}
    for i in range(len(w) - n + 1):
        g = " ".join(w[i:i + n])
        if sum(1 for x in w[i:i + n] if x not in STOP) < MIN_CONTENT:
            continue
        out.setdefault(g, False)
        if any(j in q for j in range(i, i + n)):
            out[g] = True
    return out


def exemption_for(a, b, gram):
    for ea, eb, sub, reason in EXEMPT:
        if {a, b} == {ea, eb} and (sub in gram or gram in sub):
            return reason
    return None


SENT_MIN_WORDS = 5


def sentences(text):
    """Normalised sentences, with a flag for block-quoted ones.

    ⚠ THE WRAP RULE, which is beat_sweep's and applies here with teeth: this manuscript is
    hard-wrapped at ~100 columns, so almost every sentence spans two or three LINES. Splitting
    per line finds nothing and reports clean. Paragraphs are joined into one string before any
    sentence boundary is looked for, and --selftest feeds the parser a needle broken across a
    hard wrap.
    """
    body = strip_headings(text)
    out = []
    for para in re.split(r"\n\s*\n", body):
        if not para.strip():
            continue
        q = any(ln.lstrip().startswith(">") for ln in para.splitlines())
        joined = " ".join(ln.strip().lstrip(">").strip() for ln in para.splitlines())
        for raw in re.split(r"(?<=[.!?])\s+", joined):
            w = tokens(raw)
            if len(w) >= SENT_MIN_WORDS:
                out.append((" ".join(w), q))
    return out


def load(root):
    files = {}
    for p in sorted(glob.glob(os.path.join(root, "*.md"))):
        base = os.path.basename(p)
        if "DRAFT-LOG" in base:
            continue
        files[chapter_id(base)] = open(p, encoding="utf-8").read()
    return files


def run(files, n, only=None, quiet=False):
    gr = {cid: grams_of(txt, n) for cid, txt in files.items()}
    sn = {cid: dict(sentences(txt)) for cid, txt in files.items()}
    ids = sorted(gr, key=lambda s: [int(x) if x.isdigit() else x
                                    for x in re.split(r"[.\-]", s)])
    live, sent, muted = collections.defaultdict(list), collections.defaultdict(list), 0
    for i, a in enumerate(ids):
        for b in ids[i + 1:]:
            if only and only not in (a, b):
                continue
            for g in sorted(set(gr[a]) & set(gr[b])):
                if exemption_for(a, b, g):
                    muted += 1
                    continue
                live[(a, b)].append((g, gr[a][g] or gr[b][g]))
            for s in sorted(set(sn[a]) & set(sn[b])):
                if exemption_for(a, b, s):
                    muted += 1
                    continue
                sent[(a, b)].append((s, sn[a][s] or sn[b][s]))

    print(f"PROSE ECHO — {len(files)} drafted chapter(s) · arm 1: {n}-grams, "
          f"≥{MIN_CONTENT} content words · arm 2: whole sentences, ≥{SENT_MIN_WORDS} words"
          + (f" · chapter {only}" if only else ""))
    print()
    total = 0
    for (a, b), hits in sorted(sent.items()):
        print(f"  ** SENTENCE **  {a} ~ {b}   ({len(hits)})")
        for s, q in hits:
            print(f"       {'[q] ' if q else '    '}{s[:110]}")
        total += len(hits)
        print()
    for (a, b), hits in sorted(live.items()):
        print(f"  ** ECHO **  {a} ~ {b}   ({len(hits)})")
        for g, q in hits:
            print(f"       {'[q] ' if q else '    '}{g}")
        total += len(hits)
        print()
    if not total:
        print("  no unexempted echoes.\n")
    print(f"  {total} live hit(s) · {muted} exempted · {len(EXEMPT)} rule(s) in the table")
    if not quiet:
        print()
        print("  A hit is a QUESTION. Designed returns (a definition cited where it is cashed,")
        print("  a Book I image re-cut in Book III) score identically to a sentence written")
        print("  twice by someone who forgot. Adjudicate, then exempt the PAIR AND THE GRAM —")
        print("  never the chapter, never the phrase alone.")
        print("  ⚠ AND THE LIMIT: this reads WORDS. A move performed twice in different")
        print("    vocabulary is invisible here by construction — which is the exact defect")
        print("    prose_beat_sweep was built for, on the other corpus. Neither tool covers it")
        print("    prose-to-prose. That region is still open.")
    return total


def selftest(files, n):
    print("SELFTEST — the calibration pair must surface on ARM 2, which exists because it did "
          "not surface on ARM 1\n")
    sn = {cid: dict(sentences(txt)) for cid, txt in files.items()}
    ok = False
    if "II.5" in sn and "III.6" in sn:
        shared = set(sn["II.5"]) & set(sn["III.6"])
        ok = "error does not need a territory" in shared
    print(f"  arm 2 · II.5 ~ III.6 / 'error does not need a territory' : "
          f"{'FOUND — detector live' if ok else 'MISSING — DETECTOR IS BLIND'}")

    gr = grams_of("the quick brown\nfox jumps over the lazy dog and\nkeeps running", n)
    wrap_g = any("brown fox jumps over" in k for k in gr)
    print(f"  arm 1 wrap self-test (needle across a hard wrap)         : "
          f"{'PASS' if wrap_g else 'FAIL'}")

    wrapped_para = ("Some lead-in clause here.\nError does not need a\nterritory. And a "
                    "trailing clause follows it.")
    wrap_s = "error does not need a territory" in dict(sentences(wrapped_para))
    print(f"  arm 2 wrap self-test (sentence broken across two lines)  : "
          f"{'PASS' if wrap_s else 'FAIL'}")
    print()
    return 0 if (ok and wrap_g and wrap_s) else 1


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default="book")
    ap.add_argument("--chapter")
    ap.add_argument("--n", type=int, default=N)
    ap.add_argument("--fixture", metavar="REV",
                    help="run against book/ as of a git revision")
    ap.add_argument("--selftest", action="store_true")
    ap.add_argument("--quiet", action="store_true")
    a = ap.parse_args()

    if a.fixture:
        names = subprocess.run(["git", "ls-tree", "--name-only", f"{a.fixture}:{a.root}"],
                               capture_output=True, text=True, check=True).stdout.split()
        files = {}
        for nm in names:
            if not nm.endswith(".md") or "DRAFT-LOG" in nm:
                continue
            body = subprocess.run(["git", "show", f"{a.fixture}:{a.root}/{nm}"],
                                  capture_output=True, text=True, check=True).stdout
            files[chapter_id(nm)] = body
        print(f"[fixture {a.fixture}]")
    else:
        files = load(a.root)

    if a.selftest:
        sys.exit(selftest(files, a.n))
    run(files, a.n, a.chapter, a.quiet)


if __name__ == "__main__":
    main()
