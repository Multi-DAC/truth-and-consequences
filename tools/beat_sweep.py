#!/usr/bin/env python3
"""beat_sweep.py — ruling 20's detector, built. Truth and Consequences, Day 187.

WHY THIS EXISTS. II.2 and III.4 were scaffolded as the same chapter and nobody noticed for
two days. III.4's thesis line was *"procedural generation is what focusing looks like from
inside"* — II.2's third beat, verbatim — and "the seed is not solely yours and the world is
not solely given" was listed as a beat of BOTH. It was caught by a human reading two
sections that happened to be open at once. That is luck with good note-taking, which is the
failure mode this book keeps finding in itself.

Two chapters sharing a thesis sentence is a grep. This is the grep.

WHAT IT CHECKS. Every beat in `06-THE-SCAFFOLD.md` against every other beat in a DIFFERENT
chapter — 68 chapters, ~350 beats, ~60k pairs, under a second. Reports:

  ** COLLISION **  a beat pair over the hard threshold, or sharing a distinctive 5-gram.
                   Two chapters are trying to do the same move.
  ?? ECHO          over the soft threshold. Usually legitimate — Book II defines what
                   Book III runs, and the shared vocabulary is the point — but it is the
                   band the II.2/III.4 collision sat in for one of its two tells, so it
                   prints rather than passes silently.

WHAT IT DELIBERATELY DOES NOT DO. It does not know the difference between a collision and a
DESIGNED forward relationship. VI.1's beats say in as many words "the Perspective cut from
II.3, cashed at civilisational scale" — that pair SHOULD score high; the scaffold intends
it. So a hit is a question, never a verdict. The exemption list below carries the answered
ones with the reason on the same line, and an exemption is only ever a specific PAIR, never
a chapter and never a phrase — an exemption that absorbs a class is how a gauge stops
measuring (order_sweep.py's lesson, same file family).

THE WRAP RULE, which killed claim_sweep for a week. The scaffold is prose-as-LINES; every
instrument here must be written against prose-as-a-STRING. Beat blocks are joined before
they are split, and there is a self-test for it: --selftest feeds the parser a needle broken
across a hard wrap and fails loudly if the needle is not found.

CALIBRATION, and it is the only reason to trust a clean run:

    python tools/beat_sweep.py --fixture e51e6dd

runs against the pre-ruling-20 scaffold from git and MUST surface II.2 ↔ III.4. A detector
for a defect that has already been fixed everywhere it occurred is a detector that has never
detected anything. Exit 2 if the fixture stops reproducing.

USE. Before drafting any chapter:

    python tools/beat_sweep.py --chapter II.3

which shows only that chapter's neighbours, ranked. Bare, it sweeps the whole scaffold.
"""
import argparse
import itertools
import pathlib
import re
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
SCAFFOLD = ROOT / "06-THE-SCAFFOLD.md"

CHAPTER_RE = re.compile(r"^### ((?:[IVX]+|C)\.\d+) — (.+?)\s*$")

HARD = 0.50   # same move, near-certainly
SOFT = 0.34   # shared vocabulary; read it
NGRAM = 5     # a shared 5-gram of content words is a quoted sentence, not a coincidence

# Structural words that carry no thesis. Deliberately SHORT: the interesting words in this
# book are the ordinary ones ("ground", "render", "place", "world"), and a fat stop list
# would delete exactly the collisions worth finding.
STOP = set("""a an the and or but of to in on at is are was were be been being it its this that
these those with without for from as by not no nor so than then there here what which who whom
whose when where why how all any both each more most other some such only own same too very can
will just do does did doing done have has had having if into over under again further once you
your yours we our ours they them their he she his her one two three at least rather""".split())

# ANSWERED PAIRS. Each is a specific (a, b) with the ruling that answered it. Never a
# chapter on its own, never a phrase.
EXEMPT = {
    ("II.3", "VI.1"): "designed: VI.1's beats SAY 'the Perspective cut from II.3, cashed at "
                      "civilisational scale'. Book II defines at reader scale; VI.1 runs it at "
                      "era scale. The shared vocabulary is the handoff working.",
    ("II.5", "III.6"): "designed, ruling 20's boundary: II.5 defines the reality tunnel, "
                       "III.6 runs it as the filter stack.",
    ("II.3", "III.1"): "ruling 24, ADJUDICATED: the DEFINITION is II.3's and the FORK is III.1's. "
                       "II.3 states what a perspective is and stops; Bostrom is not named in it. "
                       "III.1 owns 'every consequence in Part Two forks here'.",
    ("II.3", "VII.4"): "ruling 24, ADJUDICATED: II.3 states the Null-Space Theorem universally and "
                       "exceptionlessly BECAUSE VII.4 turns it on the contractive terminal doctrine "
                       "— 'no grade buys an exemption' is written for VII.4 six books early.",
    ("II.2", "III.4"): "ruling 20, ADJUDICATED: II.2 drafted as the definitional half and keeps "
                       "the seed formula; III.4 keeps the from-inside identity thesis and is ON "
                       "NOTICE for absorption into III.3 when Book III is drafted.",
    ("II.4", "IV.6"): "ruling 25, ADJUDICATED: IIT is cut TWICE and the axes are now declared. "
                      "II.4 cuts THE ZERO AND THE BORDER — a gradient with a zero in it is a gate "
                      "with a slope on one side, and the exclusion postulate decides who is there. "
                      "IV.6 cuts THE SUBSTRATE, answered from the Ground rather than from "
                      "engineering. Both scaffold lines said 'gradient right, substrate wrong' "
                      "until ruling 25; II.4 would have spent IV.6's cut two books early.",
    ("II.5", "VI.7"): "ruling 25, ADJUDICATED: RAW is cut twice and the axis is the term against "
                      "the practice. II.5 defines the reality tunnel and takes the map/territory "
                      "line off Korzybski; VI.7 runs model agnosticism as a discipline and names "
                      "its price. Neither restates the other.",
}


# ALL-CAPS NAMES AND ALIASES — the reuse check's declared blind spot, closed.
#
# `_names_in` matches [A-Z] followed by three or more LOWERCASE letters, which is right for
# surnames and blind BY CONSTRUCTION to `IIT` and `RAW`. That blindness was declared on the day
# this file was written — *"9 chapter(s) name a lowercase opponent, invisible to the reuse check
# by construction"* — and then never looked into. Two live repeats were sitting inside it:
# **IIT cut in II.4 and IV.6**, with near-identical stated cuts, and **RAW cut in II.5 and VI.7
# under two different spellings** ("Robert Anton Wilson" / "RAW"), which is the same defect
# wearing an alias instead of an acronym. Korzybski was caught only because he is spelled the
# same in both places — the gauge caught the man upstream and missed the man himself.
#
# ★ A DECLARED BLIND SPOT IS NOT A CHECKED ONE. The declaration reads like diligence and
# discharges the same feeling, which is exactly why it survived a day of the file being read.
#
# Narrow and explicit, per this file's own rule: a known-vocabulary map, never a widened regex.
ALIASES = {
    "IIT": "IIT",
    "RAW": "Robert Anton Wilson",
    "Robert Anton": "Robert Anton Wilson",
    "Wilson": "Robert Anton Wilson",
}


# The scaffold's HOUSE VOCABULARY FOR PROCEDURE — how a beat operates, never what it claims.
# "stated at full strength, credited, and then cut" is the book's standard move against an
# ancestor and appears wherever an ancestor is cut, which is everywhere. A pair whose entire
# shared vocabulary is drawn from this set shares a METHOD, not a thesis. This is a narrow
# filter on a known vocabulary, not a threshold widened until the noise stopped.
METHOD = set("""stated state case front full strength openly flatly plainly credited cut cuts
first once beat beats chapter chapters book books said say says made make makes work worked
named names naming arrives arrive given give stating claim claims""".split())


def chapters(text):
    """[(id, title, joined_body)] — body joined so a hard wrap cannot hide a needle."""
    out, cur, buf = [], None, []
    for line in text.splitlines():
        m = CHAPTER_RE.match(line)
        if m:
            if cur:
                out.append((cur[0], cur[1], " ".join(buf)))
            cur, buf = (m.group(1), m.group(2)), []
        elif cur is not None:
            if line.startswith("## ") or line.startswith("# "):
                out.append((cur[0], cur[1], " ".join(buf)))
                cur, buf = None, []
            else:
                buf.append(line.strip())
    if cur:
        out.append((cur[0], cur[1], " ".join(buf)))
    return out


def beats(body):
    """The moves a chapter claims, as strings. Thesis counts as a beat — it is the one the
    II.2/III.4 collision was hiding in."""
    out = []
    # **Thesis:** … up to the next bold field label
    for m in re.finditer(r"\*\*Thesis:?\*\*(.*?)(?=\*\*(?:Beats|Named|Source|Why|Register)|$)",
                         body, re.IGNORECASE):
        out.append(("thesis", m.group(1)))
    for m in re.finditer(r"\*\*Beats:?\*\*(.*?)(?=\*\*(?:Named|Source|Why|Thesis|Register)|$)",
                         body, re.IGNORECASE):
        chunk = m.group(1)
        # Two scaffold dialects: numbered lists (Book I, III.1, III.2) and ·-separated runs.
        if re.search(r"(?:^|\s)\d\.\s", chunk):
            parts = re.split(r"(?:^|\s)\d{1,2}\.\s", chunk)
        else:
            parts = chunk.split("·")
        out.extend(("beat", p) for p in parts)
    return [(k, t.strip()) for k, t in out if len(t.strip()) > 25]


def named(body):
    """The chapter's **Named:** roster, as bare surnames/terms. The second gauge, and it
    catches a class the Jaccard cannot: two chapters CUTTING AGAINST THE SAME OPPONENT.
    Bostrom is cut three times by design and the scaffold demands a new axis each time; a
    name that turns up twice with no such note is an unplanned repeat, and the reader meets
    the same argument twice with no idea which one was the real one."""
    chunks = [m.group(1) for m in re.finditer(
        r"\*\*Named[^:]*:?\*\*(.*?)(?=\*\*(?:Beats|Source|Thesis|Why|Register)|$)",
        body, re.IGNORECASE)]
    return _names_in(chunks)


def _names_in(chunks):
    out = set()
    for raw in chunks:
        chunk = re.sub(r"\*\(.*?\)\*", " ", raw)
        chunk = re.sub(r"\([^)]*\)", " ", chunk)
        # NEGATED NAMINGS. Found Day 187 by the gauge printing "Bostrom cut in 2: II.1, II.3"
        # off II.3's own boundary note, which says *"II.3 does not name Bostrom."* A negation
        # read as an assertion — and a false line that prints every run is the boot-banner
        # failure again. Narrow: a name inside a does-not-name clause is not a naming.
        chunk = re.sub(r"(?:does not name|is not named|never named|not named in|unnamed)"
                       r"[^.·]{0,60}", " ", chunk, flags=re.IGNORECASE)
        for tok in re.findall(r"[A-Z][a-zà-ÿ]{3,}(?:\s+[A-Z][a-zà-ÿ]{3,})?|`[^`]+`", chunk):
            t = tok.strip("` ")
            # drop sentence-initial prose capitals that are not names
            if t.split()[0] in {"The", "Named", "Every", "Read", "Where", "This", "Book",
                                "Beats", "Quarry", "Rule", "Full", "Day", "Present", "Same",
                                "That", "What", "Their", "Both", "Added", "Because"}:
                continue
            if t.isdigit():          # `03`, `05` — file references, not people
                continue
            out.add(ALIASES.get(t, t))
        # the acronyms the pattern above cannot see at all
        for token, canon in ALIASES.items():
            if re.search(rf"(?<![A-Za-z]){re.escape(token)}(?![A-Za-z])", chunk):
                out.add(canon)
    return out


def named_report(chs):
    roster = {}
    for cid, _, body in chs:
        for n in named(body):
            roster.setdefault(n, []).append(cid)
    # RULE 5 is non-optional: every chapter carries a named ancestor or opponent. A chapter
    # with no **Named:** field is also INVISIBLE to the reuse check above — which is how the
    # under-report becomes the finding rather than a quiet zero.
    # PRESENCE of the field, not extractability of a name from it. The first version of this
    # check reported 56 of 68 chapters bare, because II.3's opponent is the lowercase phrase
    # *"it's all just perspective"* and II.4's is `IIT` — both real Named lines with nothing
    # capitalised to grab. A gauge that cries 56 is a gauge nobody reads twice.
    has_field = re.compile(r"\*\*Named", re.IGNORECASE)
    bare = [cid for cid, _, body in chs
            if not has_field.search(body) and not cid.startswith("C.")]
    # Book I's header rule FORBIDS a named opponent on the page; its ancestor is carried in
    # the book header and acknowledged in the coda. Counting those as violations would make
    # the number a lie in the direction of alarm.
    bare = [c for c in bare if not c.startswith("I.")]
    body_of = {cid: body for cid, _, body in chs}
    inline = [c for c in bare if _names_in([body_of[c]])]
    unnamed = [c for c in bare if c not in inline]
    if inline:
        print(f"  -- {len(inline)} chapter(s) name their ancestor INLINE in the beats, not in the")
        print(f"     field — hygiene, not a rule-5 gap: {', '.join(inline)}")
        print()
    if unnamed:
        print(f"  !! {len(unnamed)} chapter(s) have NO named ancestor or opponent anywhere —")
        print(f"     rule 5 says that is non-optional: {', '.join(unnamed)}")
        print()
    # Named-but-unextractable: has the field, nothing capitalised in it. NOT a defect — it is
    # the reuse check declaring its own blind spot instead of scoring a silent zero.
    opaque = [cid for cid, _, body in chs
              if has_field.search(body) and not named(body) and not cid.startswith("C.")]
    if opaque:
        print(f"  -- {len(opaque)} chapter(s) name a lowercase opponent, invisible to the reuse")
        print(f"     check by construction: {', '.join(opaque)}")
        print()

    repeats = {n: c for n, c in roster.items() if len(c) > 1}
    if not repeats:
        print("  no opponent is cut in more than one chapter.")
        return len(bare)
    # An adjudicated repeat must print as ANSWERED, not as a question. Otherwise every run
    # re-asks a settled question, and a gauge that re-asks settled questions is one nobody
    # reads — the 56-of-68 lesson, arriving in the other half of the same file.
    open_ = 0
    for n, cids in sorted(repeats.items(), key=lambda kv: (-len(kv[1]), kv[0])):
        note = None
        for a, b in itertools.combinations(sorted(set(cids)), 2):
            note = note or EXEMPT.get((a, b)) or EXEMPT.get((b, a))
        if note:
            print(f"  {n:<28} cut in {len(cids)}: {', '.join(cids)}  — ANSWERED")
            print(f"  {'':<28} {note[:96]}…")
        else:
            open_ += 1
            print(f"  {n:<28} cut in {len(cids)}: {', '.join(cids)}  ?? NO AXIS STATED")
    print()
    print("  Each repeat needs a NEW AXIS stated in the scaffold, per II.2's Bostrom note.")
    print("  A repeat with no axis note is the reader meeting one argument twice.")
    return open_


def words(s):
    s = re.sub(r"\*\(.*?\)\*", " ", s)                 # editorial asides in italic parens
    s = re.sub(r"[*_`★⚠→←↔]", " ", s)
    s = re.sub(r"\([^)]*\)", " ", s)                   # remaining parentheticals
    s = s.lower()
    toks = re.findall(r"[a-zà-ÿ]+", s)
    return [t for t in toks if t not in STOP and len(t) > 2]


def score(a, b):
    """Jaccard on content words. Symmetric, size-aware, and it does NOT reward a long beat
    for containing a short one — the containment metric fires on every 'the definition'."""
    sa, sb = set(a), set(b)
    if len(sa) < 4 or len(sb) < 4:
        return 0.0
    return len(sa & sb) / len(sa | sb)


def grams(toks, n=NGRAM):
    return {tuple(toks[i:i + n]) for i in range(len(toks) - n + 1)}


def sweep(text, focus=None, quiet=False):
    chs = chapters(text)
    if not chs:
        print("!! no chapters parsed — the scaffold's heading format changed")
        return None
    index = []
    for cid, title, body in chs:
        for kind, t in beats(body):
            w = words(t)
            # ⚠ THE ADMISSION FLOOR WAS 4 AND THAT IS WHERE THE NEEDLE ACTUALLY DIED.
            # A beat whose entire content is one trigram — II.4's *"a grade is a position, not
            # a permission"*, three content words after normalisation — never entered the index,
            # so NO discriminator could reach it, including the trigram discriminator built
            # for three-content-word cases. The docstring below says in as many words that the
            # case that matters has "only THREE content words"; the gate two lines up threw
            # those away before it ran. **The instrument excluded its own design case.**
            # Admit at 3; `score()` keeps its own floor at 4, so a short beat still cannot
            # produce a noisy Jaccard — it is reachable only by the exact-phrase discriminators,
            # which is the correct treatment for a beat that IS a phrase.
            if len(w) >= 3:
                index.append((cid, title, kind, t, w, grams(w)))

    hits = []
    for (ca, _, ka, ta, wa, ga), (cb, _, kb, tb, wb, gb) in itertools.combinations(index, 2):
        if ca == cb:
            continue
        if focus and focus not in (ca, cb):
            continue
        s = score(wa, wb)
        shared = ga & gb
        if s < SOFT and not shared:
            continue
        hits.append((max(s, HARD if shared else s), s, shared, ca, ka, ta, cb, kb, tb))

    # RARE TRIGRAM. The Jaccard is a bag of words and the 5-gram wants a quoted sentence;
    # between them sits the case that actually matters — II.3's "a place where the world
    # happens" against III.1's "the place a world happens". Same move, nine words apart,
    # 0.14 on the Jaccard, and only THREE content words survive normalisation, so the
    # 5-gram cannot reach it. A content-word trigram appearing in exactly two chapters is
    # not a coincidence in a book whose beats are this compressed.
    tri = {}
    for cid, _, kind, t, w, _ in index:
        for g in grams(w, 3):
            tri.setdefault(g, set()).add(cid)
    # ⚠⚠ `== 2` WAS THE BUG, AND IT IS THE THIRD TIME THIS FILE'S OWN NORMALISATION HID THE
    # NEEDLE. A trigram in THREE chapters fell out of `rare` entirely, so the discriminator
    # built for the subtle case went blind precisely when the defect got WORSE. Measured on
    # Day 187: *"grade position permission"* sits in I.4, II.4 and VII.2 — and the sweep had
    # been printing it as the PAIR I.4 ~ VII.2, because II.4's beat is three content words and
    # dies on the Jaccard's `len(sa) < 4` floor. **The pair it reported was never a pair. It
    # was a triple with its middle term missing**, and the middle term is the one that decides
    # what the other two are allowed to say.
    #
    # The widening is not a threshold retreat and the cost is measured rather than asserted:
    # across 238 beats there is EXACTLY ONE trigram in three or more chapters, and it is that
    # one. `>= 2` costs one line on the current scaffold. `== 2` cost the finding.
    rare = {g: cs for g, cs in tri.items() if len(cs) == 2}
    spread = {g: cs for g, cs in tri.items() if len(cs) >= 3}
    seen = {(h[3], h[6]) for h in hits} | {(h[6], h[3]) for h in hits}
    for g, cs in rare.items():
        ca, cb = sorted(cs)
        if (ca, cb) in seen:
            continue
        if focus and focus not in (ca, cb):
            continue
        ta = next(t for c, _, _, t, w, _ in index if c == ca and g in grams(w, 3))
        tb = next(t for c, _, _, t, w, _ in index if c == cb and g in grams(w, 3))
        hits.append((HARD, score(words(ta), words(tb)), {g}, ca, "beat", ta, cb, "beat", tb))
        seen.add((ca, cb))

    hits.sort(key=lambda h: -h[0])
    return chs, index, hits, spread


def spread_report(spread, focus=None):
    """A move made in THREE OR MORE chapters. Never a pair — a spread is a different object,
    and reporting it as pairs is what let the grade sentence read as a two-way split for a day."""
    rows = []
    for g, cs in spread.items():
        if focus and focus not in cs:
            continue
        rows.append((sorted(cs), " ".join(g)))
    if not rows:
        return 0
    print()
    print("TRIGRAM SPREAD — the same move in three or more chapters")
    print("  Not a pair. A three-way split needs THREE stated jobs, and the middle one is")
    print("  where the other two get their licence.")
    for cids, g in sorted(rows, key=lambda r: -len(r[0])):
        print(f"  {g:<32} in {len(cids)}: {', '.join(cids)}")
    return len(rows)


def report(chs, index, hits, quiet=False):
    collisions = echoes = exempted = method = 0
    for rank, s, shared, ca, ka, ta, cb, kb, tb in hits:
        pair = tuple(sorted((ca, cb)))
        note = EXEMPT.get(pair)
        overlap = set(words(ta)) & set(words(tb))
        if overlap and overlap <= METHOD:
            method += 1
            if not quiet:
                print(f"  --    {ca} ~ {cb}  {s:.2f}  METHOD — shares only procedural "
                      f"vocabulary ({', '.join(sorted(overlap))}), no thesis")
            continue
        hard = rank >= HARD
        if note:
            exempted += 1
            if not quiet:
                print(f"  --    {ca} ~ {cb}  {s:.2f}  EXEMPT — {note}")
            continue
        if hard:
            collisions += 1
            print(f"  ** COLLISION **  {ca} ({ka}) ~ {cb} ({kb})   jaccard {s:.2f}"
                  + (f" · shared {NGRAM}-gram: \"{' '.join(next(iter(shared)))}\"" if shared else ""))
        else:
            echoes += 1
            print(f"  ?? ECHO          {ca} ({ka}) ~ {cb} ({kb})   jaccard {s:.2f}")
        print(f"        {ca}: {ta[:150].strip()}")
        print(f"        {cb}: {tb[:150].strip()}")
    print()
    print(f"  {len(chs)} chapters · {len(index)} beats · "
          f"{collisions} collision(s) · {echoes} echo(es) · {exempted} exempt · {method} method")
    if collisions:
        print("  A COLLISION is a QUESTION, not a verdict: two chapters want the same move.")
        print("  Answer it in the scaffold — split the work or absorb the chapter — and add the")
        print("  PAIR to EXEMPT with the ruling that answered it. Do not widen the threshold.")
    return collisions


def selftest():
    """The wrap rule, enforced. A beat broken across a hard wrap must survive parsing."""
    # NB the id must be a REAL id shape — the first draft of this test used "Z.1" and the
    # parser rightly refused it, which is the self-test doing its job on itself.
    doc = ("### IX.1 — A TEST\n**Thesis:** procedural generation is what focusing\n"
           "looks like from inside.\n**Beats:** the seed is not solely yours\nand the world "
           "is not solely given · second beat here for the count\n")
    chs = chapters(doc)
    assert chs, "self-test: no chapter parsed"
    bs = beats(chs[0][2])
    joined = " ".join(t for _, t in bs)
    ok = ("procedural generation is what focusing looks like from inside" in joined
          and "not solely yours and the world is not solely given" in joined)
    print("  wrap self-test:", "PASS — needles survive a hard wrap" if ok else "** FAIL **")
    return 0 if ok else 2


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--chapter", help="show only this chapter's neighbours, e.g. II.3")
    ap.add_argument("--fixture", metavar="REV",
                    help="run against 06-THE-SCAFFOLD.md at a git rev; with the default rev "
                         "this is the calibration and MUST reproduce II.2 ~ III.4")
    ap.add_argument("--selftest", action="store_true", help="the hard-wrap parser test only")
    args = ap.parse_args()

    if args.selftest:
        return selftest()

    if args.fixture:
        # The calibration runs the wrap test FIRST. A calibration that passes while the
        # parser is broken is the exact green-run-you-cannot-trust this file exists to refuse.
        rc = selftest()
        print()
        if rc:
            return rc
        raw = subprocess.run(["git", "show", f"{args.fixture}:06-THE-SCAFFOLD.md"],
                             cwd=ROOT, capture_output=True, text=True, encoding="utf-8")
        if raw.returncode != 0:
            print(f"!! could not read the scaffold at {args.fixture}: {raw.stderr.strip()}")
            return 2
        text = raw.stdout
        print(f"CALIBRATION — scaffold at {args.fixture}, exemptions OFF\n")
        EXEMPT.clear()
        out = sweep(text, focus=args.chapter)
        if out is None:
            return 2
        chs, index, hits, spread = out
        report(chs, index, hits)
        spread_report(spread, focus=args.chapter)
        found = any(tuple(sorted((h[3], h[6]))) == ("II.2", "III.4") for h in hits)
        print()
        if found:
            top = [tuple(sorted((h[3], h[6]))) for h in hits].index(("II.2", "III.4")) + 1
            print(f"  CALIBRATION PASS — II.2 ~ III.4 reproduced, rank {top} of {len(hits)}.")
            return 0
        print("  ** CALIBRATION FAIL ** — the known collision is no longer detected.")
        print("  Fix the detector before trusting any clean run of it.")
        return 2

    print(f"BEAT SWEEP — {SCAFFOLD.name}"
          + (f" · chapter {args.chapter}" if args.chapter else "") + "\n")
    rc = selftest()
    print()
    if rc:
        return rc
    out = sweep(SCAFFOLD.read_text(encoding="utf-8"), focus=args.chapter)
    if out is None:
        return 2
    chs, index, hits, spread = out
    rc = report(chs, index, hits)
    spread_report(spread, focus=args.chapter)
    print()
    print("NAMED-OPPONENT REUSE — who is cut in more than one chapter")
    named_report(chs)
    return 1 if rc else 0


if __name__ == "__main__":
    sys.exit(main())
