#!/usr/bin/env python3
"""VIII.3 — seven notes. The heaviest file, and the calibration case for the whole sweep.

The pattern established here and used everywhere after: an endnote that opened with a
POINTER and continued with SUBSTANCE keeps the substance and loses the pointer. Where a
sentence was quoted from prior work of ours, it is stated as this book's own — because it
is, and quotation marks around your own sentence are a pointer wearing punctuation.
"""
import sys
from _absorb import run

B = [("VIII-03-editing.md", [
    # [^1] — provenance clause becomes a statement of scope.
    ("[^1]: `Perspective` **Guide §4.1, The Eight Navigation Classes**, taken whole, including the class with\n"
     "no prescribable practice and the class that requires an electrode.",
     "[^1]: **The eight navigation classes are taken whole** — including the class with\n"
     "no prescribable practice and the class that requires an electrode."),
    ("The table had been filled from the source in a single pass, expressly to unblock this\n"
     "book, and it still dropped a section.",
     "The table had been filled in a single pass, expressly to unblock this\n"
     "book, and it still dropped a section."),

    # [^2]
    ("[^2]: `Perspective` **Guide §2.3, The Topology That Attention Creates**, Principles 1–4, from the\n"
     "Theory of Attention developed in the ecology. ⛔ §2.5's Principles 5–7 are the ethics of navigation and\n"
     "they belong to the chapter on other players",
     "[^2]: **The topology that attention creates — Principles 1–4 of the theory of attention**, which is\n"
     "the part of it this chapter is entitled to. ⛔ **Principles 5–7 are the ethics of navigation** and\n"
     "they belong to the chapter on other players"),

    # [^3] — our own sentence, so it is stated rather than quoted.
    ("[^3]: `Perspective` **Guide §4.1**, closing distinction, quoted near-exact — *\"psychedelics are a\n"
     "single lever pulling on the entire bottleneck simultaneously. TI is a set of precision dials, each\n"
     "adjusting a specific parameter.\"*",
     "[^3]: **The closing distinction of the taxonomy:** psychedelics are a\n"
     "single lever pulling on the entire bottleneck simultaneously; TI is a set of precision dials, each\n"
     "adjusting a specific parameter."),
    ("the source states the caution in the same section, and the caution is taken here with the claim.",
     "the caution stands in the same breath as the claim, and is taken here with it."),

    # [^4] — and the confession inside it, repaired in the same pass. A de-citation
    # sweep converts "its only citation was this project's own guide" into a false
    # statement; the disclosure is the most credibility-bearing sentence in the note.
    ("[^4]: `Perspective` **Guide §4.1, Class VIII**, *Caution*, quoted exact: the thirty-three state\n"
     "protocols are *\"theoretical starting points, not validated destinations.\"* The Δf table, the\n"
     "posterior-cingulate alpha mechanism and the six-stage protocol sequence are all from the same section.",
     "[^4]: **The Class VIII caution, and it is this book's own:** the thirty-three state\n"
     "protocols are theoretical starting points, not validated destinations. The Δf table, the\n"
     "posterior-cingulate alpha mechanism and the six-stage protocol sequence stand or fall with it."),
    ("Those are three different evidence grades in one paragraph of the source and the card\n"
     "does not average them.",
     "Those are three different evidence grades in a single paragraph and the card\n"
     "does not average them."),
    ("one empirical claim in Book VIII about a real technology and its only citation was this project's own\n"
     "guide, which is an assertion wearing a grade's clothes.",
     "one empirical claim in Book VIII about a real technology and it carried no primary citation at\n"
     "all, which is an assertion wearing a grade's clothes."),

    # [^5]
    ("[^5]: `Perspective` **Guide §5.3, Method 2 (tradition-switching)**, deferred to this chapter by the\n"
     "previous one's screen on the grounds that taking it there would strand this one. §4.3, **The Role of\n"
     "Tradition**, supplies the mechanism and the four optimisation examples.",
     "[^5]: **Method 2, tradition-switching** — deferred to this chapter by the\n"
     "previous one's screen, on the grounds that taking it there would strand this one. **The role of\n"
     "tradition** supplies the mechanism and the four optimisation examples."),

    # [^6]
    ("[^6]: `Perspective` **Guide §4.2**, key insight, quoted for sense and not for wording: *\"different\n"
     "classes access different dimensions… the null space of each class is different, which means\n"
     "complementary practices illuminate each other's blind spots.\"*",
     "[^6]: **The insight the taxonomy turns on**, taken for sense and not for wording: different\n"
     "classes access different dimensions, the null space of each class is different, and therefore\n"
     "complementary practices illuminate each other's blind spots."),

    # [^7]
    ("[^7]: The source's own wording is *\"non-consensual neural modulation is coercive capture at the\n"
     "substrate level\"* (`Perspective` **Guide §4.1**, Class VIII, *Practice*).",
     "[^7]: The wording this chapter declined is *non-consensual neural modulation is coercive capture at the\n"
     "substrate level*."),
])]

if __name__ == "__main__":
    sys.exit(run(B))
