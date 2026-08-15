#!/usr/bin/env python3
"""Book VII — VII.6, VII.7, VII.8.

Note the second form being repaired here, which the gate does NOT catch: **"the source."**
Where it means prior work of ours it is the anonymous self-reference Z-01 calls strictly
worse than the named one, and it cannot be gated, because 111 occurrences across the book
are overwhelmingly about OTHER people's texts — Enoch, the Tibetan material, Mariotte.
A regex would flag those and be tuned until it stopped. So these are adjudicated by hand,
in the notes being rewritten anyway, and the gate DECLARES the gap instead of pretending to
cover it.
"""
import sys
from _absorb import run

B = [
("VII-06-love.md", [
    ("[^2]: Source: `Perspective` **06 §6.3 The gift of limitation**, quoted closely — \"Love requires two\n"
     "beings… Without limitation, there is no other. Without an other, there is no love.\"",
     "[^2]: **The gift of limitation, and it is the hinge of the chapter:** love requires two\n"
     "beings. Without limitation there is no other; without an other there is no love."),

    ("[^3]: Source: `Perspective` **03 §3.5 Mutual crystallisation and parasitic dissolution**, taken\n"
     "entire; this chapter is its only housing in the manuscript.",
     "[^3]: **Mutual crystallisation and parasitic dissolution**, taken\n"
     "entire; this chapter is their only housing in the manuscript."),

    ("[^4]: Source: `Perspective` **03 §3.4 Orientations in practice** (E+ / E− / V, and the somatic\n"
     "test). Also first housing. The precedence rule where the somatic and longitudinal readings disagree\n"
     "is this chapter's, not the source's, and follows from the source's own statement that the felt\n"
     "quality of an interaction does not discriminate crystallisation from dissolution.",
     "[^4]: **Orientations in practice** — E+ / E− / V, and the somatic\n"
     "test. Also first housing. The precedence rule where the somatic and longitudinal readings disagree\n"
     "is this chapter's own, and it follows directly from the taxonomy: if the felt\n"
     "quality of an interaction does not discriminate crystallisation from dissolution, the felt reading\n"
     "cannot be the one that decides."),

    ("C18 and C19 each lost a limit\n"
     "to a section boundary the source's argument crossed, C21's scope was narrowed by the same operation,",
     "C18 and C19 each lost a limit\n"
     "to a section boundary the argument crossed, C21's scope was narrowed by the same operation,"),
    ("does not catch this one, because the source\n"
     "gives no signpost at all;",
     "does not catch this one, because there\n"
     "is no signpost at all;"),

    ("The care-and-capture diagnostic is the source's, `Perspective` **03 §3.6**, where it is stated\n"
     "for teaching and coercive control; the grade-difference application is this chapter's extension of\n"
     "it,",
     "The care-and-capture diagnostic is inherited, stated first\n"
     "for teaching and for coercive control; the grade-difference application is this chapter's extension of\n"
     "it,"),
    ("Evan Stark on coercive\n"
     "control, and the Hassan and Lifton material on group capture, are cited in the source at this point\n"
     "and are used in this manuscript at VII.3 and VII.4; they are not re-sourced here.",
     "Evan Stark on coercive\n"
     "control, and the Hassan and Lifton material on group capture, arrive with the diagnostic\n"
     "and are used in this manuscript at VII.3 and VII.4; they are not re-sourced here."),
]),

("VII-07-freedom-when-every-path-already-exists.md", [
    ("[^1]: Source: `Perspective` **05 §5.2** — Theorem 6 (Navigational Freedom) and its gloss, quoted in\n"
     "full.",
     "[^1]: **Theorem 6, Navigational Freedom, and its gloss — taken in\n"
     "full.**"),
    ("The remainder — *and whether that felt direction has phenomenological\n"
     "consequences* — is the source's only move beyond pure report, and cutting it made the source look\n"
     "worse than it is. Caught in the pre-draft screen by reading the source rather than the brief.",
     "The remainder — *and whether that felt direction has phenomenological\n"
     "consequences* — is the theorem's only move beyond pure report, and cutting it made the position look\n"
     "worse than it is. Caught in the pre-draft screen by reading the theorem entire rather than the brief."),

    ("[^2]: `Perspective` **05 §5.2**, Theorem 6, stated: *\"Free will is the capacity of a stream to\n"
     "navigate toward or away from its own coherence. The configuration space provides the possibility\n"
     "landscape; the stream provides the navigational direction. The choice is genuine, and the\n"
     "consequences are phenomenologically real.\"* The reading of this as an exchange of a binary quantity\n"
     "at an instant for a continuous quantity across a life is this chapter's, not the source's; the\n"
     "source does not compare the two measurements and does not appear to notice that it has changed what\n"
     "freedom is measured in.",
     "[^2]: **Theorem 6 in full:** free will is the capacity of a stream to\n"
     "navigate toward or away from its own coherence. The configuration space provides the possibility\n"
     "landscape; the stream provides the navigational direction. The choice is genuine, and the\n"
     "consequences are phenomenologically real. ⚠ **The reading of this as an exchange of a binary quantity\n"
     "at an instant for a continuous quantity across a life is this chapter's own, and is new here.** The\n"
     "theorem as stated does not compare the two measurements, and nothing in it registers that it has\n"
     "changed what freedom is measured in."),

    ("[^3]: `Perspective` **05 §5.2.1**: *\"This mechanism is deeply informed by the existentialist\n"
     "philosophy of Jean-Paul Sartre, particularly his concept of the 'project.'\"* Sartre, *L'Être et le\n"
     "Néant* (1943).",
     "[^3]: **The mechanism is deeply informed by the existentialist philosophy of Jean-Paul Sartre**,\n"
     "and specifically by his concept of the *project*: Sartre, *L'Être et le\n"
     "Néant* (1943)."),
    ("and this is the source's own declared engine for this\n"
     "chapter — cited by name in the section being drafted from, and silent through a whole Book whose\n"
     "subject is traditions.",
     "and this is the chapter's own declared engine —\n"
     "named in the very passage that sets the mechanism up, and silent through a whole Book whose\n"
     "subject is traditions."),

    ("[^4]: `Perspective` **05 §5.2.2**, The Teleology-Existentialism Synthesis: the *what* inherited and\n"
     "teleological (Aristotelian entelechy, §5.1), the *how* self-determined through the Sartrean project.\n"
     "The characterisation of this as the use of Sartre's mechanism against Sartre's conclusion is this\n"
     "chapter's, and is a correction to the source rather than a reading of it. The source presents the\n"
     "synthesis as a reconciliation of two traditions; it is better described as a selective borrowing\n"
     "from one of them, and saying so costs the argument nothing it was entitled to keep.",
     "[^4]: **The teleology–existentialism synthesis:** the *what* inherited and\n"
     "teleological — Aristotelian entelechy — the *how* self-determined through the Sartrean project.\n"
     "⚠ **The characterisation of this as the use of Sartre's mechanism against Sartre's conclusion is this\n"
     "chapter's own, and it is a correction rather than a restatement.** The synthesis presents itself as a\n"
     "reconciliation of two traditions; it is better described as a selective borrowing\n"
     "from one of them, and saying so costs the argument nothing it was entitled to keep."),

    ("Cited by the source at Theorem 6.",
     "Cited at Theorem 6."),

    ("A reader who rejects C26 should read section VI's second point as the source's hedge\n"
     "restated, and should be told so rather than left to discover it.",
     "A reader who rejects C26 should read section VI's second point as a hedge\n"
     "restated, and should be told so rather than left to discover it."),

    ("[^9]: `Perspective` **Guide 06 §6.1 The Price of Being Someone**: *\"To be someone is to not be\n"
     "everything else. To see something is to not see everything else.\"*",
     "[^9]: **The price of being someone:** to be someone is to not be\n"
     "everything else, and to see something is to not see everything else."),
    ("Plotinus and Tzimtzum carry the source's emanation parallel at §4.1 and are **housed in Book\n"
     "V**",
     "Plotinus and Tzimtzum carry the emanation parallel and are **housed in Book\n"
     "V**"),

    ("[^10]: `Perspective` **Guide 06 §6.2 The Dissolution Limit**: *\"The Guide's position: the dissolution\n"
     "limit is real, it is reachable, and it is not the goal.\"* ⚠ **First housing in the manuscript: §6.2\n"
     "had zero occurrences across fifty-seven drafted chapters.** The section also supplies the reading of",
     "[^10]: **The dissolution limit, and the position this book holds: it is real, it is reachable, and\n"
     "it is not the goal.** ⚠ **First housing in the manuscript: the claim\n"
     "had zero occurrences across fifty-seven drafted chapters.** It carries with it the reading of"),
]),
]

if __name__ == "__main__":
    sys.exit(run(B))
