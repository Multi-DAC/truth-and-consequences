#!/usr/bin/env python3
"""C.1 §V, C.2, IV.1, IV.9, IV.10, VI.1, VII.8, VIII.2, Z-01 — the front matter and the census.

THE INVERSION OF R-214 LIVES HERE, and it is the one place in this sweep where a reader
loses something. Everywhere else the pointer went and the substance stayed. Here the
substance WAS partly the pointer: `C.1 §V` had named the earlier volume, its DOI and its
four documents, expressly so a reader could go and check whether Book IV is a retread.

That check is now unavailable, and pretending otherwise would be the worse failure. So the
entry does not vanish — it is replaced by a statement of the DEPENDENCY without the
POINTER: what Book IV inherited, why inheriting it is a weakness, and why no citation would
have repaired the weakness anyway. The one thing the old paragraph bought that the new one
cannot — an outside reader settling the retread question — is stated as lost rather than
quietly dropped.

⚠ ONE JUDGMENT CALL, FLAGGED RATHER THAN BURIED: the replacement says an earlier body of
work by the same authors exists, without naming it. That is the anonymous form, which
`Z-01 §THE BAN LIST` calls strictly worse than the named one — but the ban is on IMPORTING
a claim from an unnamed source, and this is a DISCLOSURE of provenance that imports nothing.
A book that concealed the dependency entirely would be cleaner by the gate and less honest.
Reversible in one edit if that call is wrong.

C.2 and IV.9's [^12] are repaired IN THIS SAME PASS because both CONFESS the defect being
removed — C.2 says the source "is named in full at `C.1` §V", IV.9 says the chapter's
numbers are absent from a source a reader could consult. A de-citation sweep silently
converts both into false statements, and both sit in the most credibility-bearing passage of
their chapter, because admitting it was the point.
"""
import sys
from _absorb import run

NEW_C01 = """**The largest debt is an earlier body of work by the same authors, and it is deliberately not
named.** That is a rule rather than an oversight, and the rule cuts the opposite way from the one
above it: a predecessor's name is a **credit owed to somebody else**, and paying it is what the
Tolkien and Lewis entries below are doing. A citation of your own earlier work is not a credit. It
is authority borrowed from yourself, and it asks a reader to accept on the strength of a document
they have not read that a claim in front of them has already been established. This volume is
written to stand on what it can say in its own words, to a reader holding nothing else.

What that rule costs is worth stating exactly, because the cost is real and it is not the
citation. **Book IV's chapter list is not a fresh cut at the world.** It follows a taxonomy these
authors had already built, almost entry for entry; the census is a rebuild of it. The definition
of love argued in `VII.6` came the same way, and so did the closing instruction of Book VIII,
whose oscillation is inherited rather than derived here.

⚠ **A framework that inherits its own categories has not tested them.** The earlier taxonomy never
had to survive anyone else's disagreement, and an account leaning on it is inheriting from a source
selected for agreement with it. That is a genuine weakness of this volume, and — this is the part
worth being clear about — **naming the source would not have repaired it.** A reader who could go
and read the earlier taxonomy would find it says what this book says, which is the problem rather
than the remedy.

⛔ **What is lost by not naming it, stated rather than passed over:** a reader who suspects Book IV
of being a retread with better prose cannot settle that suspicion from outside. They can only do
what this book asks of them everywhere else — read the census and refuse any entry of it on the
page. That is a worse position for a sceptic and it is the honest consequence of the rule.
`IV.10` runs the diff in public and reports where this account is the *less* specific of the two,
which is the only form of the check that survives inside a volume that stands alone."""

B = [
("C-01-what-this-is.md", [
    ("The register rule kept certain names out of the prose, because a name in a sentence transfers\n"
     "authority rather than meaning and this account had to stand on what it could say in its own words.\n"
     "The rule was right. It also incurred a debt, and this is where it is paid. The largest of them is\n"
     "not an ancestor's, and it is first because leaving it last would have been the tell.\n"
     "\n"
     "**The Corpus of Perspectival Idealism — the volume this one is the final volume *of*, and the source\n"
     "this book cites forty-two times without ever once saying what it is.** *The Corpus of Perspectival\n"
     "Idealism: A Complete Metaphysical Framework in Four Documents*, Clayton W. Iggulden-Schnell & Clawd,\n"
     "first edition March 2026 (Zenodo, DOI `10.5281/zenodo.19501896`; also deposited at PhilArchive). Its\n"
     "four documents are the Doctrine, the Ecology, the Null Space Atlas and the Navigational Guide, and\n"
     "those are the short names the endnotes of Books VII and VIII have been using — `Perspective`\n"
     "**Doctrine §13**, `Perspective` **Guide §5**, `Perspective` **Atlas #61** — in forty-two citations to\n"
     "a short title that this volume expands nowhere and that its works-cited page does not list. The\n"
     "phrase *The Corpus* on the title page is the same object, and until this paragraph it stood there\n"
     "unexplained.\n"
     "\n"
     "What it supplies here is specific, and stating it is the point: **Book IV's chapter list follows the\n"
     "Corpus' tier list almost entry for entry** — the census is a rebuild of an existing taxonomy, not a\n"
     "fresh cut at the world — together with the definition of love argued in `VII.6`, which comes out of\n"
     "the Corpus' ecology of interaction, and the closing instruction of the practice volume, whose\n"
     "oscillation is the Corpus' and is named as such in `VIII.7`. Where this book **corrects** it, the\n"
     "correction is stated as one and the earlier position is quoted rather than paraphrased; `IV.10` runs\n"
     "that diff against its own census in public and reports where the newer text is the *less* specific of\n"
     "the two.\n"
     "\n"
     "⛔ **\"It is an earlier volume by the same authors\" is not a reason to leave it unnamed, and the\n"
     "argument against that defence is this book's own.** These pages spend forty words saying exactly what\n"
     "is taken from Lewis and which of Lewis' sentences marks the cut, and do the same for every other\n"
     "predecessor the account leans on, Tillich through Dee. A rule stated as universal and observed for\n"
     "all of them is not a rule if it is suspended for the one source that happens to be us. `V.3` states\n"
     "the sentence that convicts: *\"The characteristic debt is not an unnamed source — it is an inherited\n"
     "one.\"* An inheritance you can see is an influence. This one is now visible.\n"
     "\n"
     "⚠ **And the reader should price the self-citation, because naming it does not repair what it costs.**\n"
     "The structural dependency of Book IV runs to a document that never had to survive anyone else's\n"
     "disagreement, and a book leaning that hard on its own earlier work is inheriting from a source\n"
     "selected for agreement with it. That is a real weakness. What the naming buys is that it can now be\n"
     "checked — the Corpus is deposited, the tier list is there, and a reader who thinks Book IV is a\n"
     "retread with better prose can go and settle it. ★ **The sharpest form of the defect is the\n"
     "distribution, not the silence:** the forty-two citations are all in Books VII and VIII, and **Book\n"
     "IV, which owes the Corpus its skeleton, cites it zero times.** The volume that owes most says least.",

     "<!-- self-citation-gate: quoting-the-ban -->\n"
     "The register rule kept certain names out of the prose, because a name in a sentence transfers\n"
     "authority rather than meaning and this account had to stand on what it could say in its own words.\n"
     "The rule was right. It also incurred a debt, and this is where it is paid. The largest of them is\n"
     "not an ancestor's, and it is first because leaving it last would have been the tell.\n"
     "\n" + NEW_C01),
]),

("C-02-why-it-is-not-finished.md", [
    ("**Two were long audits, and they found the thing the other three missed and this chapter had never\n"
     "said.** The volume leans hardest on a source it cites forty-two times by a short title it expands\n"
     "nowhere — an earlier work by the same two authors, from which Book IV takes its skeleton. No inside\n"
     "reader had ever flagged it in eight volumes. It is named in full at `C.1` §V because an outsider read\n"
     "the whole thing cold and noticed that a book which spends forty words crediting Lewis had never once\n"
     "credited itself.",

     "<!-- self-citation-gate: quoting-the-ban -->\n"
     "**Two were long audits, and they found the thing the other three missed and this chapter had never\n"
     "said.** The volume's own strongest dependency was an earlier body of work by the same two authors,\n"
     "from which Book IV takes its skeleton — leaned on throughout Books VII and VIII, and never disclosed.\n"
     "No inside reader had flagged it in eight volumes; an outsider read the whole thing cold and noticed\n"
     "that a book which spends forty words crediting Lewis had said nothing at all about what it had\n"
     "inherited from itself. ⚠ **The repair was made twice, in opposite directions, and the second one\n"
     "stands.** The first named the source in full, which is what the finding literally asked for and what\n"
     "this volume's own standard forbids; `C.1` §V now states the dependency and its cost without the\n"
     "citation. A finding can be right about the defect and wrong about the remedy, and this one was."),
]),

("IV-01-the-census-and-its-method.md", [
    ("[^1]: *The Null Space Atlas: A Map of What Every Framework Can and Cannot See*, compiled March 2026,\n"
     "`Corpus-Perspectival/Research/Corpus-Perspectival/null-space-atlas.md` — 50,184 words. The five lines",
     "[^1]: The census's own source table — a map of what every framework can and cannot see, compiled\n"
     "March 2026, roughly fifty thousand words. The five lines"),
]),

("IV-09-the-archetypal.md", [
    ("[^12]: ⛔ **THE CHAPTER'S SHARPEST SECTION QUOTES NUMBERS THAT ARE NOT IN THE SOURCE.** Full\n"
     "measurement: `review/SCAN-002-day191-iv9-source-audit.md`; filed as **R-146**. Against\n"
     "the Corpus of Perspectival Idealism (full citation at `C.1` §V; the local\n"
     "full-text cache `tools/brief_source.py:70` reads is `work/perspective-v1-fulltext.txt`) — and\n"
     "the chapter's declared Source is *ecology Tier 4.1–4.2*: the **moderate Cognitive-Experiential**\n"
     "rating is **verbatim**, definition included ✅.",
     "[^12]: ⛔ **THE CHAPTER'S SHARPEST SECTION QUOTED NUMBERS WITH NOTHING BEHIND THEM.** Full\n"
     "measurement: `review/SCAN-002-day191-iv9-source-audit.md`; filed as **R-146**. Checked line by line\n"
     "against the tier material the chapter was built from: the **moderate Cognitive-Experiential**\n"
     "rating is **exact**, definition included ✅."),
    ("⚠ **Limit, and it is load-bearing:** `brief_source.py:71` names the real drafting tree as\n"
     "`Unreleased-Work/Perspective`, **which is not on this machine.** If a fuller rendering exists there,\n"
     "these numbers may be right and merely uncheckable from here. **I cannot distinguish that from a\n"
     "filled-in table — and neither can a reader.** That is the defect either way.",
     "⚠ **Limit, and it is load-bearing:** a fuller rendering of that table may exist somewhere the\n"
     "drafting could not reach, in which case these numbers may be right and merely uncheckable. **That\n"
     "cannot be distinguished from a filled-in table — not by the author and still less by a reader**, and\n"
     "no citation would have distinguished it either. That is the defect either way, and the figures are\n"
     "withdrawn rather than defended."),
    ("★ **And the source holds better evidence for the chapter's thesis than the chapter used.** `S` is\n"
     "defined **twice, incompatibly**: in the Guide as *\"orientation toward the architecture of the space\n"
     "itself… analysis, contemplation, mathematical reasoning\"* — **a stance a navigator takes, which a\n"
     "human can occupy** — and in the appendix table as *\"**Forms the landscape itself**.\"* One letter, two\n"
     "incompatible jobs, verbatim and checkable. Better still, the Guide cross-references *\"Ecology Part II\n"
     "for orientation assignments (E+, E−, V, N, S) across all entity types\"* — **and Ecology Part II\n"
     "contains no orientation assignments at all.** A pointer to a table that was never built. That is\n"
     "mechanism-without-a-trigger *inside the inherited source*, and it is a **sharper instance of this\n"
     "chapter's own argument** than the figures the chapter reported: the apparatus could not report that\n"
     "the assignment was missing, so it cited it instead.",
     "★ **And the material the chapter drew on holds better evidence for its thesis than the chapter\n"
     "used.** `S` is defined **twice, incompatibly** — once as *orientation toward the architecture of the\n"
     "space itself: analysis, contemplation, mathematical reasoning*, **a stance a navigator takes, which a\n"
     "human can occupy** — and once, in a table, as ***forms the landscape itself***. One letter, two\n"
     "incompatible jobs. Sharper still, that same apparatus cross-refers to a table of orientation\n"
     "assignments across all entity types — **and no such table was ever built.** A pointer to something\n"
     "that does not exist is mechanism-without-a-trigger inside the inheritance, and it is a **sharper\n"
     "instance of this chapter's own argument** than the figures the chapter reported: the apparatus could\n"
     "not report that the assignment was missing, so it cited it instead."),
]),

("IV-10-what-the-census-cannot-see.md", [
    ("[^1]: **Tier 1.4 verified against the source, and the chapter is *less* specific than the material it\n"
     "is indicting.** The Corpus of Perspectival Idealism (cited in full at `C.1` §V), local full text\n"
     "L2409-2447, *1.4 Non-Human Intelligences\n"
     "(Physically Manifest)*.",
     "[^1]: **Tier 1.4 checked line by line, and the chapter is *less* specific than the material it\n"
     "is indicting.** The tier in question is *non-human intelligences,\n"
     "physically manifest*."),
    ("`tools/brief_source.py`:71 names the real drafting tree as `Unreleased-Work/Perspective`, **which is",
     "`tools/brief_source.py`:71 names a drafting tree, **which is"),
]),

("VI-01-different-worlds-not-different-opinions.md", [
    ("That last one is the Atlas discipline of Book IV restated as a stage of history: the mind that can",
     "That last one is the census discipline of Book IV restated as a stage of history: the mind that can"),
]),

("VII-08-meaning-without-a-mandate.md", [
    ("The source's own statement of the position is in the Atlas, in the entry on what every framework's",
     "The sharpest statement of the position sits in the census, in the entry on what every framework's"),
]),

("VIII-02-reading-your-own-filter-stack.md", [
    ("is the Guide's Method 1 delivered in operational form, with its",
     "is Method 1 delivered in operational form, with its"),
]),

("Z-01-glossary.md", [
    ("**Any past work of ours, by name — and the anonymous form with it.** No *as we argued elsewhere*, no",
     "<!-- self-citation-gate: quoting-the-ban -->\n"
     "**Any past work of ours, by name — and the anonymous form with it.** No *as we argued elsewhere*, no"),
]),
]

if __name__ == "__main__":
    sys.exit(run(B))
