#!/usr/bin/env python3
"""VII.8, VIII.1, VIII.2."""
import sys
from _absorb import run

B = [
("VII-08-meaning-without-a-mandate.md", [
    ("[^1]: Source: `Perspective` **Doctrine §13.1 The Journey of Return** — *\"The ultimate goal, or telos,\n"
     "is to overcome the very limitations that define its individuality and return to a state of integrated\n"
     "unity with its source.\"* ⚠ **The source contradicts this at §13.4** — *\"The culmination is not a\n"
     "terminal state of static reintegration\"* — and says there that it is refining the traditional\n"
     "teleological account. It is; and §13.1's thesis sentence and section heading stand unrepaired. The\n"
     "manuscript has been quoting the half it agrees with.",
     "[^1]: **The journey of return, in the formulation this chapter refuses:** the ultimate goal, or telos,\n"
     "is to overcome the very limitations that define individuality and return to a state of integrated\n"
     "unity with the ground. ⚠ **A second and incompatible formulation stands beside it** — *the culmination\n"
     "is not a terminal state of static reintegration* — and that one is explicitly refining the traditional\n"
     "teleological account. It is; and the first sentence has gone on standing unrepaired. The\n"
     "manuscript had been using the half it agrees with."),
    ("stronger than the source's (the Promethean impulse is eternal, so the oscillation never terminates),",
     "stronger than the received one (the Promethean impulse is eternal, so the oscillation never terminates),"),

    ("[^2]: `Perspective` **Doctrine §13.4 Culmination: The Ongoing Oscillation**, quoted exact.",
     "[^2]: **The culmination is the ongoing oscillation and not a terminal state** — stated in the body\n"
     "exactly as it stands here."),

    ("[^4]: `Perspective` **Doctrine §12.2 Resolving the Mystic-Existentialist Debate**, quoted exact. ★\n"
     "§12.1's Theorem 16 (the Fundamental Oscillation) and its *\"Do be do be do\"* formulation are **VIII.7's**\n"
     "and are pointed at rather than spent here; this chapter needs only §12.2's verdict on which half of\n"
     "the existentialist survives.",
     "[^4]: **The resolution of the mystic–existentialist debate**, taken as stated. ★\n"
     "Theorem 16 (the Fundamental Oscillation) and its *do be do be do* formulation are **VIII.7's**\n"
     "and are pointed at rather than spent here; this chapter needs only the verdict on which half of\n"
     "the existentialist survives."),

    ("[^5]: `Perspective` **Atlas #61, Existential Philosophy of Suffering (Kierkegaard, Heidegger,\n"
     "Frankl, Weil)**, NULL SPACE, first entry, quoted exact. ★★ **This is the source's own census card\n"
     "diagnosing the exact defect this chapter's central argument turns on, and no chapter of this\n"
     "manuscript has cited it before now.**",
     "[^5]: **The census card for the existential philosophy of suffering — Kierkegaard, Heidegger,\n"
     "Frankl, Weil — NULL SPACE, first entry.** ★★ **The card diagnoses the exact defect\n"
     "this chapter's central argument turns on, and no chapter of this\n"
     "manuscript had used it before now.**"),
    ("it reaches this chapter **inside the Atlas card's own quoted sentence, not from a reading of Sartre.** "
     "That is the honest provenance and it is the reason he is not argued with here: the card is citing him "
     "as an instance of existentialism's individualist default, this chapter takes the card's diagnosis, and "
     "**a name that arrives through a quotation is owed the note that says so.**",
     "it reaches this chapter **inside the census card's own sentence, not from a reading of Sartre.** "
     "That is the honest provenance and it is the reason he is not argued with here: the card cites him "
     "as an instance of existentialism's individualist default, this chapter takes the card's diagnosis, and "
     "**a name that arrives through a quotation is owed the note that says so.**"),

    ("[^11]: `Perspective` **Atlas**, universal null spaces, the entry on **Meaning**, quoted exact apart\n"
     "from the bracketed substitution of the framework's name. This is C16's positive half in the source's\n"
     "own words and it is the only place in the source where it is stated as a claim about what meaning\n"
     "*is* rather than as a consequence of the telos.",
     "[^11]: **The universal null spaces, the entry on Meaning** — taken entire apart\n"
     "from the bracketed substitution of the framework's name. This is C16's positive half, and it is the\n"
     "only place the claim is made about what meaning\n"
     "*is* rather than about what follows from the telos."),
]),

("VIII-01-navigation-not-tourism.md", [
    ("[^2]: `Perspective` **Doctrine §13.1** (*\"the ultimate goal, or telos, is to overcome the very\n"
     "limitations that define its individuality and return to a state of integrated unity with its\n"
     "source\"*) against **§13.4** (*\"The culmination is not a terminal state of static reintegration\"*).\n"
     "The source knows it is amending — §13.4 says it *\"refines the traditional teleological account\"* —\n"
     "and leaves §13.1's thesis sentence and its section heading standing.",
     "[^2]: **The telos in its two incompatible statements:** *the ultimate goal is to overcome the very\n"
     "limitations that define individuality and return to a state of integrated unity with the\n"
     "ground*, against *the culmination is not a terminal state of static reintegration*.\n"
     "The second is knowingly amending — it *refines the traditional teleological account* —\n"
     "and the first has been left standing beside it, thesis sentence and heading both."),

    ("[^4]: `Perspective` **Guide §1.3 Navigation as Identity**, quoted exact. The refutation is VII.9's",
     "[^4]: **Navigation as identity**, in the form this book inherited it. The refutation is VII.9's"),
]),

("VIII-02-reading-your-own-filter-stack.md", [
    ("[^3]: The Observational Null Space Theorem, established in Book II and applied throughout Book IV;\n"
     "`Perspective` **Guide §5.1**, quoted exact for the patterning claim — *\"your null space is not\n"
     "random… your blind spots are patterned. They are predictable. They can be mapped, even though they\n"
     "cannot be directly observed.\"*",
     "[^3]: The Observational Null Space Theorem, established in Book II and applied throughout Book IV,\n"
     "together with the patterning claim it licenses: **your null space is not\n"
     "random. Your blind spots are patterned, they are predictable, and they can be mapped, even though they\n"
     "cannot be directly observed.**"),

    ("[^4]: `Perspective` **Guide §5.3, Method 3**, quoted exact and refused. ⛔ The refusal is narrow and\n"
     "should not be read wider than it is: §5.3's Methods 1 and 2 stand entirely, §5.2's four symptoms are\n"
     "correct and are in fact this chapter's instrument, and §5.4's four responses — acknowledge, develop\n"
     "sensitivity to indirect signals, build alliances, accept irreducible mystery — are all sound. What\n"
     "fails is one image and the operation it licenses. ★ And the finding runs in the source's favour twice:\n"
     "the residual instrument this chapter substitutes was **already in §5.2**, one subsection earlier,\n"
     "described as symptoms rather than as a method, so the correction is a promotion rather than an import.",
     "[^4]: **Method 3, taken as stated and refused.** ⛔ The refusal is narrow and\n"
     "should not be read wider than it is: Methods 1 and 2 stand entirely, the four symptoms are\n"
     "correct and are in fact this chapter's instrument, and the four responses — acknowledge, develop\n"
     "sensitivity to indirect signals, build alliances, accept irreducible mystery — are all sound. What\n"
     "fails is one image and the operation it licenses. ★ And the finding runs in the inherited account's favour twice:\n"
     "the residual instrument this chapter substitutes was **already among the symptoms**, one step earlier,\n"
     "described as symptoms rather than as a method, so the correction is a promotion rather than an import."),
]),
]

if __name__ == "__main__":
    sys.exit(run(B))
