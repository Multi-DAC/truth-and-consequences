#!/usr/bin/env python3
"""
HIDDEN-ANCESTOR SWEEP  —  Truth and Consequences, Day 185.

Clayton, Day 185: "There may be many hidden ancestral doctrines we do not
identify, and we should. It will lend us credibility."

INVERSE of 03-THE-ANCESTORS.md's sweep. That one asked: which names we say are
thin? This one asks: which DOCTRINES DO WE HOLD WHOSE OWNER WE NEVER NAME?

COUNTING CONTRACT (standing rule, Day 185 — every count states these):
  ROOT      : C:/Users/mercu/clawd/repo-staging/Corpus-Perspectival
  GLOB      : **/*.md , recursive
  CASE      : case-INSENSITIVE substring match on file text
  ARCHIVES  : reported BOTH ways. "excl" drops any path containing a segment
              matching _superseded / archive / archived / .git / node_modules.
  UNIT      : FILES containing the string (not occurrences).
  KNOWN LIMIT: a grep for a NAME is not a grep for an IDEA. A zero here is
              evidence of an unnamed ancestor; a nonzero is NOT evidence the
              doctrine is engaged.

MEASURED, Day 186 — run this file, never a shell one-liner. Two `python -c`
one-liners reported "archive dirs holding md: 0" (i.e. that they do not exist).
There are 151 files in them. Shell quoting corrupted the regex on the way in and
the corrupted version FAILED SILENTLY, returning a clean plausible zero. This
file, with identical logic, was correct. A one-liner that mis-escapes does not
error -- it agrees with you.

FALSE POSITIVES CONFIRMED BY READING THE HITS (do not re-trust these numbers):
  lusory        12 raw ->  0 real  (all "iLLUSORY")
  lila           1 raw ->  0 real  (the Lunar Laser Interferometer)
  magic circle   6 raw ->  0 real IN THE PLAY SENSE (all Western-esoteric)
  The Grasshopper 2 raw -> 0 real  (a grasshopper analogy in an argument)
  affordance     8 raw ->  0 real in Gibson's technical sense (loose usage)
  Ubuntu       114 raw -> 60 non-OS files (WSL/install/distro filter)
  Wheeler       10 raw -> mostly Misner-Thorne-Wheeler, the GR textbook
  Hartshorne    11 raw -> every sampled hit is "Whitehead/Hartshorne" in a LIST
Precedent, Day 185: `Watts` 8 raw -> 0 real (all electrical: kilowatts).
"""
import os, sys, re

ROOT = r"C:/Users/mercu/clawd/repo-staging/Corpus-Perspectival"
SKIP = re.compile(r"(^|[\\/])(_superseded|archive|archived|\.git|node_modules)([\\/]|$)", re.I)

TERMS = {
 "GROUND — static, complete, non-descript": [
    "Parmenides","nirguna","apophatic","via negativa","Pseudo-Dionysius",
    "Cloud of Unknowing","Meister Eckhart","Eckhart","Godhead","Ungrund",
    "Boehme","Böhme","Schelling","Tillich","ground of being","Plotinus",
    "emanation","block universe","eternalism","McTaggart","Cusanus",
 ],
 "REACTIVITY IS AWARENESS — grades of soul": [
    "Whitehead","prehension","actual occasion","Leibniz","monad",
    "petites perceptions","apperception","Strawson","Philip Goff","panpsychism",
    "Teilhard","Hartshorne","Spinoza","scala naturae","Giordano Bruno",
    "anima mundi","hylozoism","Schweitzer","reverence for life","jiva",
 ],
 "CO-CONSTITUTION — world rendered at the point of contact": [
    "Uexküll","Uexkull","Umwelt","enactivism","enactive","Varela","Maturana",
    "autopoiesis","structural coupling","affordance","Gibson","Merleau-Ponty",
    "transcendental idealism","noumenon","Husserl","intentionality","Bergson",
    "final participation","participatory anthropic","Wheeler","it from bit",
    "Goethe","Whorf","linguistic relativity",
 ],
 "REALITY TUNNEL — the upstream owners": [
    "Korzybski","Idols of the Cave","Francis Bacon","Kuhn","paradigm shift",
    "episteme","Foucault","habitus","Bourdieu","Goffman","frame analysis",
    "social construction","Berger and Luckmann","Ouspensky","Gurdjieff",
    "doors of perception","Maybe Logic",
 ],
 "TELOS — exploration + MUTUAL RECOGNITION": [
    "Hegel","Anerkennung","mutual recognition","master-slave","Fichte",
    "Honneth","Martin Buber","I-Thou","I and Thou","Levinas","alterity",
    "the face of the other","Ubuntu","intersubjectivity",
 ],
 "THE GAME — play as a named doctrine": [
    "Huizinga","Homo Ludens","magic circle","Caillois","Bernard Suits",
    "lusory","The Grasshopper","Carse","Finite and Infinite Games",
    "infinite game","lila","līlā","Eugen Fink","procedural generation",
    "open world","MMORPG","NPC",
 ],
 "MEANING BY TRAVERSAL — the completion of existentialism": [
    "MacIntyre","narrative unity","Ricoeur","John Dewey","Viktor Frankl",
    "logotherapy","Camus","Sartre","Kierkegaard",
 ],
 "COHERENCE PRINCIPLE — the formal ancestors": [
    "Peirce","synechism","tychism","Bohm","implicate order","Friston",
    "free energy principle","predictive processing","Markov blanket",
    "Tononi","integrated information","decoherence","Everett",
 ],
}

def walk():
    for dp, dns, fns in os.walk(ROOT):
        if SKIP.search(dp):
            dns[:] = []
            continue
        for fn in fns:
            if fn.lower().endswith(".md"):
                yield os.path.join(dp, fn)

def walk_all():
    for dp, dns, fns in os.walk(ROOT):
        if re.search(r"[\\/]\.git([\\/]|$)", dp):
            dns[:] = []
            continue
        for fn in fns:
            if fn.lower().endswith(".md"):
                yield os.path.join(dp, fn)

def load(paths):
    out = []
    for p in paths:
        try:
            out.append(open(p, encoding="utf-8", errors="ignore").read().lower())
        except Exception:
            pass
    return out

live = load(list(walk()))
allf = load(list(walk_all()))
print(f"CORPUS: {len(live)} .md files (archives EXCLUDED) / {len(allf)} (archives INCLUDED)")
print(f"ROOT  : {ROOT}\n")

# AD-HOC COUNT, same contract. Added Day 187 while scaffolding II.3, because the alternative
# was a shell one-liner and this file's own docstring records what those do: mis-escape,
# fail silently, and agree with you. A count taken any other way is not comparable to the
# counts already in `03` and `04`, and every number in this book is supposed to be.
#     python tools/ancestor_sweep.py --terms "Protagoras,perspectivism,Ortega y Gasset"
if "--terms" in sys.argv:
    raw = sys.argv[sys.argv.index("--terms") + 1]
    ad_hoc = [t.strip() for t in raw.split(",") if t.strip()]
    print(f"\n=== AD HOC ({len(ad_hoc)} terms) ===")
    rows = [(sum(t.lower() in d for d in live), sum(t.lower() in d for d in allf), t)
            for t in ad_hoc]
    for a, b, t in sorted(rows):
        flag = "  <<< ZERO" if b == 0 else ("  << thin" if b <= 3 else "")
        print(f"  {a:5d} excl / {b:5d} incl   {t}{flag}")
    print("\n  REMINDER: a grep for a NAME is not a grep for an IDEA. A zero is evidence of")
    print("  an unnamed ancestor; a nonzero is NOT evidence the doctrine is engaged.")
    sys.exit(0)

for group, terms in TERMS.items():
    print(f"\n=== {group} ===")
    rows = []
    for t in terms:
        tl = t.lower()
        rows.append((sum(tl in d for d in live), sum(tl in d for d in allf), t))
    for a, b, t in sorted(rows):
        flag = "  <<< ZERO" if b == 0 else ("  << thin" if b <= 3 else "")
        print(f"  {a:5d} excl / {b:5d} incl   {t}{flag}")
