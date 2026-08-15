#!/usr/bin/env python3
"""VIII.4, VIII.5, VIII.6, VIII.7 — the last of the endnote apparatus.

One CUT rather than an absorption, and it is recorded because a cut is the lossy move:
VIII.6 [^6] carried a structural note about a Part heading that does not exist in the cited
document. That note was honest and useful while the citation stood. With the citation gone it
describes nothing a reader can reach, so it goes with it — and the finding it recorded is
re-homed to the draft log rather than deleted.
"""
import sys
from _absorb import run

B = [
("VIII-04-holding-it-open.md", [
    ("[^3]: `Perspective` **Guide §2.3, Principle 2** — attentional scarcity is perspectival: attention is",
     "[^3]: **Principle 2 — attentional scarcity is perspectival:** attention is"),

    ("[^5]: `Perspective` **Guide §2.4**, quoted exact for both halves — *\"Expansion is not always good.\n"
     "Contraction is not always bad\"* — and again for the closing-end failure, *\"the narrow channel feels\n"
     "like the only channel, and the being forgets that the wider landscape exists.\"* ⛔ The opening-end\n"
     "failure is our own completeness result from Book II and is not the source's phrasing. ★ Note what the\n"
     "source does that most practice writing does not: it names the failure mode of the mode it prefers, in\n"
     "the same paragraph, without softening.",
     "[^5]: **Both halves, and they are held together on purpose — expansion is not always good;\n"
     "contraction is not always bad** — together with the closing-end failure: *the narrow channel feels\n"
     "like the only channel, and the being forgets that the wider landscape exists.* ⛔ The opening-end\n"
     "failure is this book's own completeness result from Book II and is a separate sentence. ★ Note what the\n"
     "pair does that most practice writing does not: it names the failure mode of the mode it prefers, in\n"
     "the same breath, without softening."),

    ("[^6]: `05` §3a, the **Coherence** row, quoted for the definition:",
     "[^6]: **The Coherence row, and the definition it fixes:**"),
]),

("VIII-05-the-second-arrow.md", [
    ("[^1]: `Perspective` **Guide §5.4, Being Acted Upon by the Invisible** — the four responses, in the\n"
     "source's own order of depth: acknowledge the limitation · develop sensitivity to indirect signals ·\n"
     "build navigational alliances · accept irreducible mystery. ★ **They are used here for a property the\n"
     "source does not name: every one of them is performable *without a diagnosis*,**",
     "[^1]: **Being acted upon by the invisible — the four responses, in their\n"
     "order of depth:** acknowledge the limitation · develop sensitivity to indirect signals ·\n"
     "build navigational alliances · accept irreducible mystery. ★ **They are used here for a property\n"
     "nobody has named alongside them: every one of them is performable *without a diagnosis*,**"),
    ("⛔ **§5.5, The Invisible Others, is not used**: its central term was banned by ruling 109 on the",
     "⛔ **The companion treatment of the invisible others is not used**: its central term was banned by ruling 109 on the"),

    ("[^2]: `Perspective` **Guide §2.4**, quoted exact — *\"the narrow channel feels like the only channel,\n"
     "and the being forgets that the wider landscape exists.\"* ★ The source records this as a description of\n"
     "a failure mode.",
     "[^2]: **The narrow channel feels like the only channel, and the being forgets that the wider\n"
     "landscape exists.** ★ That is set down as a description of\n"
     "a failure mode."),
    ("⚠ The three questions in this section are the\n"
     "chapter's own and are not in the source;",
     "⚠ The three questions in this section are the\n"
     "chapter's own and are new here;"),
]),

("VIII-06-other-players.md", [
    ("[^1]: `Perspective` **Guide §2.5, Principle 5** — navigational choices have moral weight; the Null\n"
     "Space Theorem guarantees you cannot see everything, and *\"the specific PATTERN of what you see and\n"
     "don't see is your moral character.\"* The examples — the jokes you laugh at, the suffering you notice\n"
     "and the suffering you don't — are the source's.",
     "[^1]: **Principle 5 — navigational choices have moral weight.** The Null\n"
     "Space Theorem guarantees you cannot see everything, and **the specific pattern of what you see and\n"
     "don't see is your moral character.** The examples — the jokes you laugh at, the suffering you notice\n"
     "and the suffering you don't — arrive with the principle."),

    ("[^3]: `Perspective` **Guide §5.4**, the alliance move, whose tell — *\"the discomfort of genuine\n"
     "disagreement is the feeling of having your null space illuminated\"* — was used in the previous chapter\n"
     "for a different job. ★ Its use here is the one the source implies and does not state:",
     "[^3]: **The alliance move**, whose tell — *the discomfort of genuine\n"
     "disagreement is the feeling of having your null space illuminated* — was used in the previous chapter\n"
     "for a different job. ★ Its use here is the one the move implies and never states:"),

    ("[^5]: `Perspective` **Guide §2.5**, which poses the scope question — human faces only, all living\n"
     "beings, possibly artificial systems — and explicitly declines to settle it while noting that the\n"
     "framework implies no *a priori* exclusion.",
     "[^5]: **The scope question, posed and deliberately left open** — human faces only, all living\n"
     "beings, possibly artificial systems — declined rather than settled, with the note that the\n"
     "framework implies no *a priori* exclusion."),

    # CUT: the structural note describes a defect in a pointer that no longer exists.
    ("[^6]: `Perspective` **Guide §8.1, You Are Already Collective** — Mead's *you were a we before you were\n"
     "an I*, and the Ubuntu formulation as ontology rather than aspiration. The three diagnostic questions\n"
     "are the source's, compressed. ⚠ **Structural note on the citation, recorded rather than quietly\n"
     "corrected: the Guide has no `Part VIII`.** Its Part headings stop at Part VI and the 7.x and 8.x\n"
     "sections stand as bare headings underneath none of them. Every section title and every claim cited\n"
     "here is present and exact; what does not exist is the Part heading our own planning table named. It\n"
     "is the same class as this book's other external-pointer defect, and the tool written for pointer\n"
     "errors states in its own limit line that it cannot see this class.",
     "[^6]: **You are already collective** — Mead's *you were a we before you were\n"
     "an I*, and the Ubuntu formulation as ontology rather than aspiration. The three diagnostic questions\n"
     "are compressed from a longer set."),

    ("[^7]: `Perspective` **Guide §8.2**, on Kai Erikson's Buffalo Creek work — *\"a blow to the basic",
     "[^7]: Kai Erikson's Buffalo Creek finding — *\"a blow to the basic"),
    ("The complication about the collective second arrow — that it is fired by\n"
     "multiple agents, often strategically, often for power — is also the source's,",
     "The complication about the collective second arrow — that it is fired by\n"
     "multiple agents, often strategically, often for power — is inherited with it,"),

    ("[^8]: `Perspective` **Guide §8.3**, on Goffman's total institution, and the section's own strongest\n"
     "line",
     "[^8]: **On Goffman's total institution**, and the strongest\n"
     "line in the treatment"),
    ("The five warning signs are the source's, given here with the fifth's structural",
     "The five warning signs are inherited, given here with the fifth's structural"),
    ("⚠ Illich, Weber and Zuboff are all cited in this section of the source and are all\n"
     "spent earlier in this manuscript;",
     "⚠ Illich, Weber and Zuboff arrive with that treatment and are all\n"
     "spent earlier in this manuscript;"),

    ("[^9]: `Perspective` **Guide §2.5, Principle 7**, quoted exact: *\"Levinas says: the Other's face,\n"
     "encountered before thought, constitutes YOU as an ethical subject. The responsibility is asymmetrical\n"
     "— you owe it regardless of reciprocity.\"*",
     "[^9]: **Principle 7, stated:** Levinas says the Other's face,\n"
     "encountered before thought, constitutes *you* as an ethical subject. The responsibility is asymmetrical\n"
     "— you owe it regardless of reciprocity."),
    ("**but the conclusion was\n"
     "already in our own source's ethics section, in a subsection that had not been opened, while Levinas\n"
     "was being spent elsewhere in this manuscript on a different job.**",
     "**but the conclusion was\n"
     "already sitting in the ethics this account inherited, in a part that had never been opened, while Levinas\n"
     "was being spent elsewhere in this manuscript on a different job.**"),
]),

("VIII-07-do-be-do-be-do.md", [
    ("[^1]: `Perspective` **Doctrine §12.1**, quoted exact: *\"Frank Sinatra, via Kurt Vonnegut, via Alfred\n"
     "North Whitehead, compressed this into three syllables: 'Do be do be do.' It is not a lyric. It is an\n"
     "ontological formula.\"* ★ The attribution chain is the source's and is preserved rather than tidied,\n"
     "including its order.",
     "[^1]: **Frank Sinatra, via Kurt Vonnegut, via Alfred\n"
     "North Whitehead, compressed this into three syllables: *Do be do be do*. It is not a lyric. It is an\n"
     "ontological formula.** ★ The attribution chain is inherited and is preserved rather than tidied,\n"
     "including its order."),

    ("[^2]: `Perspective` **Doctrine §12.1, Theorem 16 (The Fundamental Oscillation)**, quoted exact:\n"
     "*\"Consciousness, at every scale,",
     "[^2]: **Theorem 16, the Fundamental Oscillation:**\n"
     "*Consciousness, at every scale,"),
    ("not opposites but complementary phases of a single oscillatory process.\"* The inhale/exhale gloss is\n"
     "also §12.1's, verbatim: *\"Being is the inhale",
     "not opposites but complementary phases of a single oscillatory process.* The inhale/exhale gloss\n"
     "belongs with it: *Being is the inhale"),
    ("Consciousness is the breathing\n"
     "itself.\"* ⚠ **§12.2's adjudication of the mystic/existentialist dispute is NOT re-run here.** It was\n"
     "spent at VII.8, which said in its own endnote that §12.1 was being left for this chapter; the debt goes\n"
     "both directions and is now discharged. §12.2 is used for one thing only — its verdict that the target is",
     "Consciousness is the breathing\n"
     "itself.* ⚠ **The adjudication of the mystic/existentialist dispute is NOT re-run here.** It was\n"
     "spent at VII.8, which said in its own endnote that the theorem was being left for this chapter; the debt goes\n"
     "both directions and is now discharged. That adjudication is used for one thing only — its verdict that the target is"),

    ("[^3]: `Perspective` **Doctrine §12.2**, on the oscillation across scales: *\"within a single moment of\n"
     "consciousness (attention expanding and contracting).\"* ⛔ **Cited here specifically to record where §II's\n"
     "struck pair came from, rather than to use it.** The source's *contracting* is innocent in the source,\n"
     "which has no ethical polarity attached to the word; §13.4 then uses *\"a contracted consciousness\"* for a\n"
     "third distinct thing, one paragraph from the image quoted at the close.",
     "[^3]: **On the oscillation across scales:** *within a single moment of\n"
     "consciousness, attention expanding and contracting.* ⛔ **Recorded here specifically to say where §II's\n"
     "struck pair came from, rather than to use it.** That *contracting* is innocent where it stands —\n"
     "no ethical polarity is attached to the word there — while the same vocabulary elsewhere uses *a contracted\n"
     "consciousness* for a third distinct thing, one paragraph from the image quoted at the close."),
    ("Importing the source's gloss would have knocked the fence",
     "Importing that gloss would have knocked the fence"),

    ("[^4]: `Perspective` **Doctrine §13.4 (Culmination: The Ongoing Oscillation)** — closing sentence quoted\n"
     "exact.",
     "[^4]: **The culmination, the ongoing oscillation — closing sentence taken\n"
     "entire.**"),

    ("[^5]: `Perspective` The Coherence Principle, §VI. **This is the statement VIII.4 deferred to this\n"
     "chapter**, and it is given in this manuscript's own words for a stated reason: the apparatus's canonical\n"
     "wording routes the claim",
     "[^5]: **The Coherence Principle. This is the statement VIII.4 deferred to this\n"
     "chapter**, and it is given in this manuscript's own words for a stated reason: the canonical\n"
     "wording routes the claim"),
]),
]

if __name__ == "__main__":
    sys.exit(run(B))
