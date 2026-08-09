#!/usr/bin/env python3
"""
GENRE SWEEP  —  Truth and Consequences, Day 189.  R-19's third item, the one with a gauge.

WHAT R-19 ASKED FOR, IN ITS OWN WORDS:

  "a genre-name sweep — list the counterparts the work is positioned against and
   count each once, rather than finding them one zero at a time."

Three zeros of the same shape had been found by tripping over them: `video game` = 0
(Day 185), `Alan Watts` = 0 (Day 185), `Wilber` = 0 (Day 189, V.9), and then a fourth
while the row was still open — `Otto` = 0 in the chapter whose title beat is *the
numinous*, a 1917 coinage the project had used unattributed since IV.8. R-19's own
verdict on that: "the procedure exists, has been run twice, and only ever runs when a
count happens to be taken. Three instances is a search running on who we already
respect."

★ SO THE SEED LIST HERE IS DELIBERATELY NOT DERIVED FROM THIS PROJECT'S DOCUMENTS.

`ancestor_gap.py` seeds from `03`'s bold cells and `ancestor_sweep.TERMS` — names
somebody here already nominated — and says so as its known limit: "A figure who is in
neither `03` nor `ancestor_sweep.TERMS` is invisible here no matter how load-bearing."
That is precisely the class R-19 is about. This file's roster is hand-authored from the
OUTSIDE: for each position the work takes, who else in the world owns that position,
whether or not anyone here has ever written the name down.

⚠ THE LIMIT, AND IT IS THE WHOLE HONEST BOUNDARY OF THIS FILE. The roster is authored,
so it cannot certify its own completeness, and it never will be able to. A counterpart
absent from the table below is exactly as invisible as it was before this file existed.
What the gauge buys is narrower and real: the zeros now arrive ALL AT ONCE, in a list,
with the position each name owns written next to it — instead of one per chapter, on the
night that chapter happens to need them. It converts a discovery mode into a work list.

⚠ AND THE SECOND LIMIT, which is the one that will bite: PRESENCE IS NOT ENGAGEMENT.
A name that appears once in a list of names counts 1 here and owes just as much as a
zero. The gauge reads for the string, and a string is not a reading.

RELATION = what this book does with the position, authored at the same time as the row
so that no row is a bare name:
    RIVAL    same object, different answer, and the answer is live
    GENRE    the same KIND of book; a reader who has met it arrives expecting this one
    FAILURE  their failure is what one of our guards is for  (Wilber is the type case)
    COUNTER  the standing argument AGAINST a move this book makes
    SOURCE   an owner of a doctrine the book uses

COLUMNS: prose = drafted chapters in book/ · plan = 00-07 + review/ · corp = the research
corpus, via ancestor_sweep's contract (files containing the string, case-insensitive).
"""
import io, re, sys, pathlib, contextlib, argparse

HERE = pathlib.Path(__file__).resolve().parent
REPO = HERE.parent
CHAPTER = re.compile(r"^[IVX]+-\d\d-.*\.md$")

# ---------------------------------------------------------------------------
# THE ROSTER.  Authored Day 189, from outside the project's own documents.
# (pattern, display, position owned, relation)
# `pattern` is matched on word boundaries, case-insensitively. Where a surname is
# ambiguous in ordinary English (Smith, Wright, Harris, White, Taylor, Kelly) the
# pattern is the full name, which can MISS a bare-surname mention — the right way
# for a work-list to fail.
# ---------------------------------------------------------------------------
ROSTER = [
 # -- THE TOTAL SYSTEM: reads every tradition, ranks them, absorbs objections ----
 ("Wilber",              "Ken Wilber",            "integral theory / AQAL — all traditions as partial views of one tier map", "FAILURE"),
 ("Aurobindo",           "Sri Aurobindo",         "evolutionary involution; a total system with a developmental spine",      "RIVAL"),
 ("Teilhard",            "Teilhard de Chardin",   "the Omega point — cosmic process with a terminus",                        "RIVAL"),
 ("Steiner",             "Rudolf Steiner",        "anthroposophy — total system, tier map, clairvoyant epistemology",        "FAILURE"),
 ("Gebser",              "Jean Gebser",           "structures of consciousness, era by era",                                 "SOURCE"),
 ("Blavatsky",           "H. P. Blavatsky",       "theosophy — the first modern all-traditions synthesis, and its collapse", "FAILURE"),

 # -- THE PERENNIALIST CLAIM: the traditions agree.  V.11's exact subject --------
 ("Perennial Philosophy","Huxley, *The Perennial Philosophy*", "the genre-defining statement that the traditions agree",     "GENRE"),
 ("Huxley",              "Aldous Huxley",         "perennialism, and the mescaline report as evidence for it",               "GENRE"),
 ("Schuon",              "Frithjof Schuon",       "the transcendent unity of religions — esoteric core, exoteric shells",    "RIVAL"),
 ("Guénon",              "René Guénon",           "Traditionalism; modernity as decline from a primordial tradition",        "RIVAL"),
 ("Coomaraswamy",        "A. K. Coomaraswamy",    "the traditional doctrine stated as one doctrine across cultures",         "RIVAL"),
 ("Huston Smith",        "Huston Smith",          "*Forgotten Truth* — the perennial claim for a general readership",        "GENRE"),
 ("Stace",               "W. T. Stace",           "introvertive/extrovertive typology — the convergence claim, formalised",  "RIVAL"),
 ("Underhill",           "Evelyn Underhill",      "*Mysticism* (1911) — the map of the stages, pre-James",                   "SOURCE"),
 ("Otto",                "Rudolf Otto",           "the numinous; mysterium tremendum et fascinans",                          "SOURCE"),
 ("James",               "William James",         "*Varieties* — the anthology that manufactured the impression of unanimity","SOURCE"),

 # -- THE CONSTRUCTIVIST COUNTER: convergence is an artefact of description ------
 ("Katz",                "Steven T. Katz",        "★ there are NO unmediated experiences; the tradition shapes the report",  "COUNTER"),
 ("Proudfoot",           "Wayne Proudfoot",       "religious experience as an attribution, not a datum",                     "COUNTER"),
 ("Forman",              "Robert Forman",         "the pure consciousness event — the counter-counter to Katz",              "RIVAL"),
 ("Jantzen",             "Grace Jantzen",         "'mysticism' as a contested political construction",                       "COUNTER"),
 ("Certeau",             "Michel de Certeau",     "*The Mystic Fable* — mysticism as a historically bounded formation",      "COUNTER"),
 ("McGinn",              "Bernard McGinn",        "the historian's account of Western mysticism as a developing tradition",  "COUNTER"),
 ("Masuzawa",            "Tomoko Masuzawa",       "★ 'world religions' is a nineteenth-century invention",                   "COUNTER"),
 ("Jonathan Z. Smith",   "Jonathan Z. Smith",     "'religion' is the scholar's category, not the natives'",                  "COUNTER"),
 ("Hanegraaff",          "Wouter Hanegraaff",     "esotericism as the academy's rejected knowledge",                         "COUNTER"),
 ("Schmidt",             "Leigh Eric Schmidt",    "*Restless Souls* — 'spirituality' as a datable American invention",       "COUNTER"),
 ("Sharf",               "Robert Sharf",          "the rhetoric of experience — Buddhist 'experience' as a modern import",   "COUNTER"),

 # -- ARCHETYPE / MONOMYTH: convergence read as depth psychology ----------------
 ("Campbell",            "Joseph Campbell",       "the monomyth — one story under all the stories",                          "RIVAL"),
 ("Eliade",              "Mircea Eliade",         "hierophany; the sacred/profane distinction as universal",                 "RIVAL"),
 ("Jung",                "C. G. Jung",            "the collective unconscious as the explanation for convergence",           "RIVAL"),

 # -- THE METAPHYSICS RIVALS: the same object as Books I-III --------------------
 ("Kastrup",             "Bernardo Kastrup",      "analytic idealism — one mind at bottom, dissociated into alters",         "RIVAL"),
 ("Hoffman",             "Donald Hoffman",        "★ interface theory of perception — the render, argued from evolution",    "RIVAL"),
 ("Chalmers",            "David Chalmers",        "*Reality+* — virtual worlds are real worlds; the game frame, done",       "RIVAL"),
 ("Metzinger",           "Thomas Metzinger",      "the self-model; nobody is anybody",                                       "RIVAL"),
 ("Tegmark",             "Max Tegmark",           "★ the mathematical universe — every consistent structure exists",         "RIVAL"),
 ("Goff",                "Philip Goff",           "panpsychism, argued analytically",                                        "RIVAL"),
 ("Strawson",            "Galen Strawson",        "realistic physicalism entails panpsychism",                               "RIVAL"),
 ("Whitehead",           "A. N. Whitehead",       "process — occasions of experience all the way down",                      "RIVAL"),
 ("Schmidhuber",         "Jürgen Schmidhuber",    "the computable universe; all programs run",                               "RIVAL"),
 ("Bostrom",             "Nick Bostrom",          "the simulation argument",                                                 "RIVAL"),
 ("Lewis",               "David Lewis",           "modal realism — all possible worlds are as real as this one",             "RIVAL"),

 # -- THE DISENCHANTMENT HISTORY: Book VI's subject -----------------------------
 ("Charles Taylor",      "Charles Taylor",        "★ *A Secular Age* — the buffered self, the immanent frame",               "RIVAL"),
 ("Weber",               "Max Weber",             "disenchantment as the name for the change",                               "SOURCE"),
 ("Barfield",            "Owen Barfield",         "original participation, and its loss",                                    "SOURCE"),
 ("McLuhan",             "Marshall McLuhan",      "the medium reshapes the sensorium",                                       "SOURCE"),
 ("Ong",                 "Walter Ong",            "orality and literacy — print as a change in interiority",                 "SOURCE"),
 ("Jaynes",              "Julian Jaynes",         "the bicameral mind",                                                      "SOURCE"),
 ("McGilchrist",         "Iain McGilchrist",      "hemispheric attention as the history of Western thought",                 "RIVAL"),

 # -- THE MEANING-CRISIS AND PRACTICE DISCOURSE: `04`'s undrafted opponents -----
 ("Vervaeke",            "John Vervaeke",         "★ the meaning crisis; relevance realisation; the ecology of practices",   "RIVAL"),
 ("Sloterdijk",          "Peter Sloterdijk",      "anthropotechnics — practice as the real content of religion",             "RIVAL"),
 ("Peterson",            "Jordan Peterson",       "*Maps of Meaning* — the popular archetypal total system",                 "GENRE"),
 ("Sam Harris",          "Sam Harris",            "secular contemplative practice without the metaphysics",                  "COUNTER"),
 ("Robert Wright",       "Robert Wright",         "*Why Buddhism Is True* — the naturalised tradition",                       "COUNTER"),

 # -- THE ANOMALOUS AND THE DAIMONIC: V.9's subject -----------------------------
 ("Vallée",              "Jacques Vallée",        "★ the control system; the phenomenon as cultural thermostat",             "SOURCE"),
 ("Harpur",              "Patrick Harpur",        "daimonic reality — the anomalous as neither literal nor imaginary",       "RIVAL"),
 ("Kripal",              "Jeffrey Kripal",        "*Authors of the Impossible* — the impossible as a hermeneutic problem",   "RIVAL"),
 ("Erik Davis",          "Erik Davis",            "*High Weirdness* — the weird as a genre with a history",                  "GENRE"),
 ("Mack",                "John Mack",             "the abduction testimony taken seriously by a psychiatrist",               "SOURCE"),
 ("Strieber",            "Whitley Strieber",      "*Communion* — the single most influential node in the testimony",         "SOURCE"),
 ("Irreducible Mind",    "Kelly, *Irreducible Mind*", "the empirical case against production-model consciousness",           "RIVAL"),
 ("Radin",               "Dean Radin",            "the meta-analytic case for psi",                                          "RIVAL"),
 ("Michael Murphy",      "Michael Murphy",        "*The Future of the Body* — the encyclopaedia of attested capacities",     "GENRE"),

 # -- THE OPERATIVE LINE: V.7's subject -----------------------------------------
 ("Crowley",             "Aleister Crowley",      "magick as an experimental discipline with a written record",              "SOURCE"),
 ("Dion Fortune",        "Dion Fortune",          "the psychologised occult; the ritual as an operation on mind",            "SOURCE"),
 ("Regardie",            "Israel Regardie",       "the Golden Dawn corpus, published and thereby made checkable",            "SOURCE"),
 ("Ramsey Dukes",        "Ramsey Dukes",          "*SSOTBME* — magic as one of four irreducible styles of thought",          "RIVAL"),
 ("Peter Carroll",       "Peter Carroll",         "chaos magic — belief as a tool, held deliberately",                       "RIVAL"),
 ("Gordon White",        "Gordon White",          "the contemporary practitioner's synthesis, historically literate",        "GENRE"),
 ("John Michael Greer",  "John Michael Greer",    "the ecological occult; decline as the frame",                             "GENRE"),
 ("Spare",               "Austin Osman Spare",    "sigilisation — the technique that outlived its author's system",          "SOURCE"),
]

# Names known to be in the prose. If one of these reads 0, the gauge is broken, not
# the book. A sweep with no positive control cannot tell a clean result from a dead
# code path — and a sweep whose whole output is zeros needs the control most.
# ★ `Peter Carroll` is here on purpose and is the only one that matters: it is the
# two-word name that is SPLIT ACROSS A HARD WRAP in V.7, so it is a live regression
# test for the defect in `compile_pat`'s docstring. A single-word control cannot
# catch it, which is why the first version passed its controls and lied anyway.
CONTROLS = ["Watts", "Searle", "Uexküll", "Irenaeus", "Peter Carroll"]


def load(paths):
    out = {}
    for p in paths:
        try:
            out[p.name] = p.read_text(encoding="utf-8").lower()
        except OSError:
            pass
    return out


def compile_pat(pattern):
    """⚠ THE WHITESPACE JOIN IS NOT COSMETIC — IT IS THIS FILE'S FIRST BUG, FIXED.

    The first version of this gauge wrote `re.escape(pattern)`, which puts a literal
    single space between the words of a two-word name. The manuscript is hard-wrapped
    at ~98 columns, so `Peter Carroll` sits with `Peter` ending line 117 of V.7 and
    `Carroll` opening line 118 — and the row printed **0 in prose for a man who is
    named, discussed and cut in a drafted chapter.**

    That is R-37's cross-wrap defect, committed inside the gauge built to end
    one-zero-at-a-time discovery, on its first run. And it fails in the worst
    available direction: this file's entire output is a list of zeros, so a FALSE
    zero is indistinguishable from a finding. It was caught by reading V.7 — which
    is the discovery mode the gauge exists to replace.
    """
    return re.compile(r"\b" + r"\s+".join(re.escape(w) for w in pattern.lower().split()) + r"\b")


def count(texts, pattern):
    pat = compile_pat(pattern)
    return sum(1 for t in texts.values() if pat.search(t))


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--no-corpus", action="store_true",
                    help="skip the research corpus (it lives on another tree and is slow)")
    ap.add_argument("--all", action="store_true", help="print every row, not just the gaps")
    args = ap.parse_args()

    prose = load([p for p in sorted((REPO / "book").glob("*.md")) if CHAPTER.match(p.name)])
    plan = load(sorted(REPO.glob("0*.md")) + sorted((REPO / "review").glob("*.md")))

    corp_texts, corp_n, corp_root = None, 0, "(skipped)"
    if not args.no_corpus:
        try:
            sys.path.insert(0, str(HERE))
            with contextlib.redirect_stdout(io.StringIO()):
                import ancestor_sweep as A
            corp_texts = {f"c{i}": t for i, t in enumerate(A.live)}
            corp_n, corp_root = len(A.live), str(A.ROOT)
        except Exception as e:                                  # noqa: BLE001
            corp_root = f"(unreachable: {e})"

    print("GENRE SWEEP — the counterparts this work is positioned against, counted once")
    print(f"  prose : {len(prose)} drafted chapters in book/")
    print(f"  plan  : {len(plan)} planning + review documents")
    print(f"  corp  : {corp_n} research files   {corp_root}")
    print(f"  roster: {len(ROSTER)} names, hand-authored Day 189, NOT derived from this repo\n")

    bad = [c for c in CONTROLS if count(prose, c) == 0]
    if bad:
        print(f"  ⛔ POSITIVE CONTROL FAILED — {', '.join(bad)} read 0 in prose. The path is dead;")
        print("     every zero below is uninterpretable. Fix the gauge before reading the table.\n")
        return 2
    print(f"  ✓ positive control: {', '.join(f'{c}={count(prose, c)}' for c in CONTROLS)}\n")

    rows = []
    for pat, name, position, rel in ROSTER:
        rows.append((count(prose, pat), count(plan, pat),
                     count(corp_texts, pat) if corp_texts else -1, name, position, rel))

    def block(title, sel, note):
        sub = [r for r in rows if sel(r)]
        if not sub:
            return
        sub.sort(key=lambda r: (-r[2], -r[1], r[3]))
        print(f"★ {title}  ({len(sub)})")
        print("  prose  plan  corp  relation  name — the position they own")
        for pr, pl, co, name, position, rel in sub:
            c = "  n/a" if co < 0 else f"{co:5d}"
            print(f"  {pr:5d} {pl:5d} {c}  {rel:8s}  {name} — {position}")
        print(f"  {note}\n")

    block("ABSENT EVERYWHERE — not in the prose, not in the plan",
          lambda r: r[0] == 0 and r[1] == 0,
          "⚠ A name here has never been written down in this project. Wilber was in this\n"
          "  class for 189 days; Otto was in it while IV.8 was using his word.")

    block("IN THE PLAN, NOT ON THE PAGE — nominated and never named to a reader",
          lambda r: r[0] == 0 and r[1] > 0,
          "  This is `ancestor_gap`'s drafting-boundary class, on the genre roster.")

    if args.all:
        block("PRESENT — the string appears; whether it was READ is not a question this asks",
              lambda r: r[0] > 0, "  Presence is not engagement. One mention in a list counts 1.")
    else:
        n = sum(1 for r in rows if r[0] > 0)
        print(f"  ({n} of {len(rows)} appear in at least one drafted chapter — `--all` to list them.\n"
              "   Presence is not engagement: a name in a list of names counts 1 here.)\n")

    print("⚠ THIS ROSTER CANNOT CERTIFY ITS OWN COMPLETENESS AND NEVER WILL.")
    print("  It is authored, so a counterpart nobody thought of is exactly as invisible as")
    print("  before. What changed is that the zeros arrive together, with the position each")
    print("  name owns written beside it, instead of one per chapter on the night it mattered.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
