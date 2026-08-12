# -*- coding: utf-8 -*-
import io, sys
P = "book/V-11-what-the-old-roads-knew.md"
t = io.open(P, encoding="utf-8").read()
assert "[^1]" not in t, "chapter already has markers"

PAIRS = [
 ("news. Maimonides and the scholastics", "news.[^1] Maimonides and the scholastics"),
 ("what it is not. \u015aa\u1e45kara says", "what it is not.[^2] \u015aa\u1e45kara says"),
 ("doing with your hands.", "doing with your hands.[^3]"),
 ("first act of the story rather than a fall away from it.", "first act of the story rather than a fall away from it.[^4]"),
 ("**Nine of them, and they cannot all be right, and the disagreement is not decorative.**",
  "**Nine of them, and they cannot all be right, and the disagreement is not decorative.**[^5]"),
 ("V.1 said so in its ninth paragraph", "V.1 said so in its ninth paragraph[^6]"),
 ("Dionysius has a procedure for it. Cusanus has a procedure for it.",
  "Dionysius has a procedure for it. Cusanus has a procedure for it.[^7]"),
 ("and it was normal practice among men with\nfurnaces in the sixteenth century.",
  "and it was normal practice among men with\nfurnaces in the sixteenth century.[^8]"),
 ("audited what walked out of the building.", "audited what walked out of the building.[^9]"),
 ("and the fourth it has still not properly absorbed.", "and the fourth it has still not properly absorbed.[^10]"),
 ("and a question decided in advance. Harner stripped that of its cosmology to see what survived, and\nwhat survived worked.",
  "and a question decided in advance.[^11] Harner stripped that of its cosmology to see what survived, and\nwhat survived worked.[^12]"),
 ("because the desire has to get past the part of you doing the wanting.",
  "because the desire has to get past the part of you doing the wanting.[^13]"),
 ("wanting is not on the list and does not get onto it by being stronger.",
  "wanting is not on the list and does not get onto it by being stronger.[^14]"),
 ("*a hedge weakens a claim; a boundary locates an instrument.*",
  "*a hedge weakens a claim; a boundary locates an instrument.*[^15]"),
 ("they are reading from a lower tier.", "they are reading from a lower tier.[^16]"),
 ("V.9 is where that was\ntested at cost, and IV.6 is where an entry was refused for it.",
  "V.9 is where that was\ntested at cost, and IV.6 is where an entry was refused for it.[^17]"),
 ("in order to refuse each in the breath that wrote it.", "in order to refuse each in the breath that wrote it.[^18]"),
 ("**The report is honest. The instrument selected it.**",
  "**The report is honest. The instrument selected it.**[^19]"),
 ("and only a three-bin sort has anywhere to put it.", "and only a three-bin sort has anywhere to put it.[^20]"),
 ("Guénon and Coomaraswamy stand\nbehind all of them.", "Guénon and Coomaraswamy stand\nbehind all of them.[^21]"),
 ("published *De perenni philosophia* in 1540, arguing that the pagans had anticipated the\nfaith.",
  "published *De perenni philosophia* in 1540, arguing that the pagans had anticipated the\nfaith.[^22]"),
 ("**Steven\nKatz argued in 1978 that there are no unmediated experiences**",
  "**Steven\nKatz argued in 1978 that there are no unmediated experiences**[^23]"),
 ("counter-anthology on pure consciousness in 1990 is the shape of the reply.",
  "counter-anthology on pure consciousness in 1990 is the shape of the reply.[^24]"),
 ("which the framework requires by C27,", "which the framework requires by C27,[^25]"),
 ("the unaddressability, the failure of every name — arrive from",
  "the unaddressability, the failure of every name[^26] — arrive from"),
 ("no shared vocabulary for any\nof it, and they arrive in the same shape.",
  "no shared vocabulary for any\nof it,[^27] and they arrive in the same shape."),
 ("the ox-herder back among the shops, the bodhisattva who will\nnot go through the door.",
  "the ox-herder back among the shops, the bodhisattva who will\nnot go through the door.[^28]"),
 ("Ten roads, then.", "Ten roads, then.[^29]"),
]
for old, new in PAIRS:
    n = t.count(old)
    if n != 1:
        print("FAIL %d occurrences: %r" % (n, old[:60])); sys.exit(1)
    t = t.replace(old, new)
io.open(P, "w", encoding="utf-8").write(t)
print("OK — %d markers placed" % len(PAIRS))
