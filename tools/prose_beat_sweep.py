#!/usr/bin/env python3
"""prose_beat_sweep.py — ruling 33's instrument. Truth and Consequences, Day 187.

WHY THIS EXISTS, and it is a confession about the tool next door.

`beat_sweep.py` compares every beat in `06-THE-SCAFFOLD.md` against every other beat. It was
written when the scaffold was 68 chapters of plan and nothing was drafted, and on that corpus
it is complete. It is no longer that corpus. Fourteen chapters are PROSE now, and a beat in
`06` is not what those chapters contain — it is what they were once going to contain.

The day II.8 was drafted, `beat_sweep --chapter II.8` returned **0 collisions, 0 echoes**, and
it was wrong. I.6's shipped prose had already performed all four of the denials II.8's beats
planned — *"there is no leaving… there is no wall"* · *"nothing is under repair"* — and the
pair became visible only when a human wrote a ruling that put the two sentences in one file.
A collision between DRAFTED PROSE and a FUTURE CHAPTER'S BEATS is invisible to that tool **by
construction**, and the blind region grows by one chapter every time one ships.

★★ THE STANDING LESSON, and it is why this file exists rather than a patch to that one:
**A GAUGE BUILT WHEN NOTHING WAS DRAFTED COMPARES PLANS TO PLANS FOREVER.** The corpus an
instrument admits is smaller than the corpus that can collide. Ask of every gauge here: *what
has the project acquired since this was written that it still cannot see?*

WHAT IT CHECKS. Every beat of every UNDRAFTED chapter against every paragraph of every DRAFTED
chapter. The question is not "do two plans overlap" but the one that actually costs a reader:
**has this move already been PERFORMED on the page?**

  ** SPENT **   the beat's distinctive vocabulary is already in a shipped paragraph, or a
                content 5-gram is shared outright. The move has been made. Drafting the
                chapter as planned writes it twice, and the SECOND one reads as the weaker,
                because the reader met the idea first somewhere else.
  ?? TRACE      over the soft bar. Usually legitimate — Book II defines what Book III runs —
                but it is the band ruling 33's own case sat in, so it prints.

DIRECTION MATTERS AND THE METRIC IS ASYMMETRIC ON PURPOSE. `beat_sweep` uses a Jaccard because
both sides are beats and comparable in size. Here one side is a fifteen-word plan and the other
is a ninety-word paragraph; a Jaccard would score every true hit near zero, since the paragraph
carries four-fifths of the words alone. The right question is CONTAINMENT — *what fraction of
what this beat plans to say is already on the page?* — and containment is exactly the metric
`beat_sweep` was right to refuse for its own job and is right for this one.

WHAT IT DELIBERATELY DOES NOT DO. It does not know a spent move from a DESIGNED reprise. II.4
repeats I.4 out loud and says so — *"has already been said once, in a book that was not
permitted to argue"* — and that is the book working. So a hit is a question, never a verdict.
The exemption table is `beat_sweep`'s, imported rather than copied: an adjudication lives in
ONE place or it rots in the second (ruling 31, ruling 36 — a rule stated in one place and
implemented in one of the two that need it).

CALIBRATION, and it is the only reason to trust a clean run:

    python tools/prose_beat_sweep.py --fixture a65139f

runs against the repository as it stood the morning II.8 was still a PLAN and I.6 was already
PROSE, with exemptions off, and MUST surface I.6 ~ II.8. That is the one case this instrument
exists for and the one case the tool next door could not see. Exit 2 if it stops reproducing.

THE WRAP RULE, which has now cost this project three separate findings. `06` is prose-as-lines
and so is `book/`; every needle here is joined into a STRING before it is split. `--selftest`
feeds both parsers a needle broken across a hard wrap and fails loudly.

USE. Before drafting any chapter:

    python tools/prose_beat_sweep.py --chapter III.1

which shows only what that chapter's beats would be repeating. Bare, it sweeps everything.
"""
import argparse
import pathlib
import re
import subprocess
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from beat_sweep import (EXEMPT, chapters, beats, words, grams, selftest as beat_selftest)

ROOT = pathlib.Path(__file__).resolve().parents[1]
SCAFFOLD = ROOT / "06-THE-SCAFFOLD.md"
BOOK = ROOT / "book"

# The prose heading a drafted chapter carries. Read from the FILE'S CONTENT, not its name:
# a filename is a label somebody typed once and a heading is what the chapter says it is.
# They are cross-checked, and a disagreement prints — see `drafted()`.
PROSE_HEAD = re.compile(r"^##\s+((?:[IVX]+|C)\.\d+)\s+—")
FILE_ID = re.compile(r"^((?:[IVX]+|C))-0*(\d+)-")

HARD = 0.72   # nearly everything this beat plans to say is already on the page
SOFT = 0.55   # shared vocabulary at a level worth a human's eye
NGRAM = 5     # a shared content 5-gram is a quoted sentence, not a coincidence

# The floor below which containment means nothing. A four-content-word beat can hit 1.00 on
# any paragraph in the book by accident; the ratio needs a denominator with something in it.
# ⚠ This is an ADMISSION GATE, which is where a gauge's design case goes to die (the standing
# note, learned when beat_sweep's floor of 4 excluded the three-content-word beat its own
# docstring named as the case that mattered). So the short beats are not dropped silently —
# they are routed to the exact-phrase discriminator, which is the correct treatment for a
# beat that IS a phrase, and the count of them prints every run.
MIN_BEAT = 6


def paragraphs(text):
    """[(n, joined)] — prose split at blank lines, each block joined so a hard wrap cannot
    hide a needle. Headings and rules are not paragraphs; a block quote is."""
    out, buf, start = [], [], 0
    for i, line in enumerate(text.splitlines(), 1):
        s = line.strip()
        if not s:
            if buf:
                out.append((start, " ".join(buf)))
                buf = []
            continue
        if s.startswith("#") or set(s) <= set("-*_ "):
            if buf:
                out.append((start, " ".join(buf)))
                buf = []
            continue
        if not buf:
            start = i
        buf.append(s.lstrip("> "))
    if buf:
        out.append((start, " ".join(buf)))
    return out


def drafted(read):
    """{chapter_id: [(line, paragraph)]} for every chapter that is PROSE.

    `read` is a callable so the fixture path can pull the same files out of git — the
    calibration must read a past state of the tree, and a tool that can only read `now` can
    never be shown to have detected anything."""
    out = {}
    for name, text in read():
        head = None
        for line in text.splitlines():
            m = PROSE_HEAD.match(line)
            if m:
                head = m.group(1)
                break
        fm = FILE_ID.match(name)
        fid = f"{fm.group(1)}.{int(fm.group(2))}" if fm else None
        if head and fid and head != fid:
            # A gauge that silently prefers one of two disagreeing sources has picked a side
            # without telling anyone. Say it, then trust the heading — the file says what it is.
            print(f"  ⚠ {name}: filename says {fid}, heading says {head} — trusting the heading")
        cid = head or fid
        if not cid:
            print(f"  ⚠ {name}: no chapter id in heading or filename — NOT SWEPT")
            continue
        out[cid] = paragraphs(text)
    return out


def contain(beat_w, para_w):
    """What fraction of the beat's distinct content words are already in this paragraph.

    Asymmetric by design. NOT idf-weighted, and that is a decision rather than an omission:
    the interesting words in this book are the ordinary ones — ground, render, place, world,
    focus — and any rarity weighting deletes exactly the vocabulary a repeat is made of.
    House vocabulary is filtered downstream instead, where it can be read and argued with."""
    sb = set(beat_w)
    if not sb:
        return 0.0
    return len(sb & set(para_w)) / len(sb)


# The book's HOUSE VOCABULARY, measured rather than guessed: a content word carried by two
# thirds of the drafted chapters is not evidence that a move has been made. This is computed
# at run time from the drafted corpus, not hand-listed, so it cannot rot — but the threshold
# and the cap are choices and they print with the run.
HOUSE_DF = 0.66
HOUSE_CAP = 60


def house(dr):
    df = {}
    for cid, paras in dr.items():
        seen = set()
        for _, p in paras:
            seen |= set(words(p))
        for w in seen:
            df[w] = df.get(w, 0) + 1
    n = max(1, len(dr))
    common = sorted((w for w, c in df.items() if c / n >= HOUSE_DF),
                    key=lambda w: -df[w])[:HOUSE_CAP]
    return set(common), df


def sweep(scaffold_text, dr, focus=None, exempt=True):
    chs = chapters(scaffold_text)
    if not chs:
        print("!! no chapters parsed — the scaffold's heading format changed")
        return None
    hv, _ = house(dr)
    undrafted = [(cid, title, body) for cid, title, body in chs if cid not in dr]

    hits, short = [], 0
    for cid, _, body in undrafted:
        if focus and focus != cid:
            continue
        for kind, text in beats(body):
            bw = words(text)
            distinct = [w for w in bw if w not in hv]
            bg = grams(bw, NGRAM)
            if len(set(distinct)) < MIN_BEAT:
                short += 1
                distinct = None            # phrase-only: reachable by 5-gram, not by ratio
            for pcid, paras in dr.items():
                if focus and focus not in (cid, pcid):
                    continue
                best = (0.0, None, None)
                shared = set()
                for ln, p in paras:
                    pw = words(p)
                    g = bg & grams(pw, NGRAM)
                    if g:
                        shared |= g
                        best = max(best, (1.0, ln, p), key=lambda t: t[0])
                    if distinct:
                        c = contain(distinct, pw)
                        if c > best[0]:
                            best = (c, ln, p)
                if best[0] >= SOFT or shared:
                    hits.append((max(best[0], HARD if shared else best[0]), best[0], shared,
                                 cid, kind, text, pcid, best[1], best[2]))
    hits.sort(key=lambda h: -h[0])
    return chs, undrafted, hits, short, hv


def report(chs, dr, undrafted, hits, short, hv, exempt=True, quiet=False):
    spent = traces = exempted = 0
    for rank, c, shared, cid, kind, text, pcid, ln, para in hits:
        note = EXEMPT.get(tuple(sorted((cid, pcid)))) if exempt else None
        if note:
            exempted += 1
            if not quiet:
                print(f"  --    {pcid} prose ~ {cid} {kind}   {c:.2f}  EXEMPT — {note[:88]}…")
            continue
        if rank >= HARD:
            spent += 1
            print(f"  ** SPENT **   {cid} ({kind}) is already performed in {pcid}"
                  f"   containment {c:.2f}"
                  + (f" · shared {NGRAM}-gram: \"{' '.join(next(iter(shared)))}\"" if shared else ""))
        else:
            traces += 1
            print(f"  ?? TRACE      {cid} ({kind}) ~ {pcid}   containment {c:.2f}")
        print(f"        PLAN  {cid}: {text[:150].strip()}")
        print(f"        PROSE {pcid}:{ln}: {para[:170].strip()}")
    print()
    print(f"  {len(dr)} drafted chapter(s) · {sum(len(p) for p in dr.values())} paragraphs · "
          f"{len(undrafted)} undrafted · {spent} spent · {traces} trace(s) · {exempted} exempt")
    print(f"  {short} beat(s) below the {MIN_BEAT}-distinct-word floor — NOT dropped: reachable")
    print(f"  by the {NGRAM}-gram discriminator only, which is what a beat that IS a phrase needs.")
    print(f"  house vocabulary discounted, measured at df ≥ {HOUSE_DF:.2f}: {len(hv)} word(s)"
          + (f" — {', '.join(sorted(hv)[:12])}…" if hv else ""))
    if spent:
        print()
        print("  SPENT is a QUESTION, not a verdict: the chapter may still be RIGHT to return")
        print("  to the move — II.4 repeats I.4 deliberately and SAYS SO on the page, and that")
        print("  is the strongest seam in the work. What it may not do is return SILENTLY.")
        print("  Answer it in `06` — cut the beat, or flag the reprise out loud — and add the")
        print("  PAIR to beat_sweep.EXEMPT with the ruling. Do not raise the threshold.")
    return spent


# ────────────────────────────────────────────────────────────────────────────────
# THE SEMANTIC ARM — and it exists because the lexical arm above FAILED its own
# calibration, on the first run, on the one case it was written for.
#
# Ruling 33's case is II.8's beat *"the Return defined against escape, salvation, and exit"*
# sitting on top of I.6's shipped *"There is no leaving… There is no wall… Nothing is under
# repair."* Those two sentences perform the same act and **share not one content word**. Every
# discriminator above — containment, 5-gram, trigram — is a gauge whose unit is the WORD, and
# the standing note already says what that costs:
#
#   ★★ A DUPLICATE OF **FUNCTION** IS INVISIBLE TO A GAUGE WHOSE UNIT IS THE WORD (ruling 32).
#
# The correct response was NOT to lower the thresholds until the pair appeared. A threshold
# retreat would have bought the calibration at the price of the instrument. It needed a second
# eye that measures MEANING, so the lexical arm keeps its bars and stays honest about what it
# cannot see.
#
# ⚠⚠ AND THE RAW COSINE IS NOT THE MEASUREMENT — NOR IS A Z-SCORE. Both were built here and
# both failed, and the failures are worth more than the fix.
#
# bge-m3 is anisotropic: two unrelated texts sit near 0.50 by the model's own geometry —
# measured at 0.497 on this machine, with a control confirming it is a property of the model
# and not of any corpus. So a "similarity of 0.63" is not a finding; it is a number with the
# model's offset baked into it.
#
# The obvious correction was a z against each beat's own spread over the drafted book. That is
# a matched null and it is still WRONG, for a reason that took a measurement to see: with 390
# paragraphs, the MAXIMUM of 390 draws sits about three standard deviations above the mean **by
# arithmetic**. Every beat has a best match, so `z(best) ≥ 3` selects nearly every beat. The
# first run returned 143 hits, which is the same thing as returning none.
#
# ★★ A NULL FOR THE MEAN IS NOT A NULL FOR THE MAXIMUM. The statistic under test was an
# extreme, and it was being scored against a null built for a typical value.
#
# What the direct measurement showed, and what the instrument is now built on: for ruling 33's
# own beat — *"the Return defined against escape, salvation, and exit"* — I.6's *"Not by leaving
# it. There is no leaving…"* ranks **3rd of 390 paragraphs**, at cosine 0.489, under a top match
# of 0.498. The top six span 0.021. In SCORE the pair is invisible and always will be. In RANK
# it is in the top 0.8% of the drafted book.
#
# Mutual rank was tried next — reciprocal nearest neighbours, which is offset-immune because it
# never reads the number, only the ordering. It returned THIRTY pairs at mutual rank 1/1, most
# of them plainly unrelated (*"State Bostrom's argument at full strength"* against II.2's *"Not
# a part of it being the case"*). That is not a bug either. **A mutual-nearest-neighbour set is
# a MATCHING, not a rarity test**: pair 186 beats with 302 paragraphs by any similarity at all
# and a few dozen reciprocal pairs fall out of the structure of the graph, carrying no evidence.
#
# ★★★ SO THE ARM DOES NOT RETURN A VERDICT, AND THAT IS THE FINDING RATHER THAN A RETREAT.
#
# The direct measurement is unambiguous about why. Ruling 33's beat is six words of abstract
# nouns; its embedding barely carries anything, and its top six matches across the whole drafted
# book span 0.021 of cosine. There is no statistic over this model that separates the true pair
# from the flat noise beneath it, because the separation is not present in the data. Any
# threshold that made the calibration pass would have been fitted to one known answer — a
# detector tuned on its own fixture, which detects nothing it was not already told.
#
# What the measurement DOES support is retrieval. I.6's paragraph ranks **3rd of 390** for that
# beat: invisible as a score, top 0.8% as an ordering. So the semantic arm is a PRE-DRAFT
# READING BRIEF — for each beat of the chapter about to be written, the handful of already-
# shipped paragraphs nearest to it, printed to be READ. No verdict, no threshold, no bucket.
# It narrows 390 paragraphs to a page, and the reader adjudicates. That is exactly the
# procedure that caught ruling 33 by hand, with the search cost taken off the human.
#
# The honest statement of what this buys: it would have caught ruling 33 the morning of, and it
# cannot promise to catch the next one. An instrument that says so is worth more than one that
# reports a clean run it has not earned.
_EMBED_HOME = pathlib.Path(r"C:\Users\Wasch\carapace\Architecture")

BRIEF_N = 5      # shipped paragraphs shown per beat


def embedder():
    """`(fn, note)`. The book must not HARD-depend on the body; if the organ is not there the
    arm says so out loud and the run continues. A silent skip would let a lexical-only run
    print the same clean summary as a full one, which is the exoneration-bucket failure with
    a different coat on."""
    try:
        if str(_EMBED_HOME) not in sys.path:
            sys.path.insert(0, str(_EMBED_HOME))
        from tools.embedder import embed_batch, MODEL_NAME
        return embed_batch, MODEL_NAME
    except Exception as e:                                  # noqa: BLE001
        return None, f"{type(e).__name__}: {e}"


def brief(scaffold_text, dr, focus, n=BRIEF_N, show=True):
    """The pre-draft reading brief. Returns [(cid, kind, beat, [(rank, cos, pcid, line, para)])].

    Deliberately NOT a detector — see the block comment above. It ranks and prints; a person
    reads. A `None` return means the arm did not run, and that prints loudly rather than
    passing as a clean sweep."""
    fn, note = embedder()
    if fn is None:
        print(f"  ⚠ READING BRIEF NOT RUN — no embedder ({note}).")
        print("    The word-unit arm above CANNOT see a repeat that shares no vocabulary,")
        print("    which is ruling 33's own case. Treat this run as PARTIAL.")
        return None
    chs = chapters(scaffold_text)
    plan = [(cid, kind, text) for cid, _, body in chs if cid not in dr
            and (not focus or cid == focus)
            for kind, text in beats(body) if len(words(text)) >= 4]
    prose = [(pcid, ln, p) for pcid, paras in dr.items() for ln, p in paras
             if len(words(p)) >= 8]
    if not plan or not prose:
        print("  ⚠ reading brief: nothing to compare.")
        return None
    if show:
        print(f"  {note} · {len(plan)} beat(s) × {len(prose)} shipped paragraph(s)"
              f" · top {n} each, RANKED, no verdict")
    pv = fn([p for _, _, p in prose])
    bv = fn([t for _, _, t in plan])
    out = []
    for (cid, kind, text), v in zip(plan, bv):
        sims = [sum(a * b for a, b in zip(v, w)) for w in pv]
        order = sorted(range(len(sims)), key=lambda i: -sims[i])[:n]
        out.append((cid, kind, text,
                    [(r, sims[i], *prose[i]) for r, i in enumerate(order, 1)]))
    return out


def brief_report(rows, exempt=True, quiet=False):
    if rows is None:
        return 0
    for cid, kind, text, near in rows:
        print(f"\n  {cid} ({kind}): {text[:160].strip()}")
        for r, cos, pcid, ln, p in near:
            note = EXEMPT.get(tuple(sorted((cid, pcid)))) if exempt else None
            tag = "  [pair already adjudicated]" if note else ""
            print(f"    {r}. {pcid}:{ln}  cos {cos:.3f}{tag}")
            print(f"       {p[:180].strip()}")
    print()
    print("  READ THESE. No verdict is offered and none is available: the measurement that")
    print("  built this arm showed no statistic separates a true repeat from the floor —")
    print("  ruling 33's own pair ranks 3rd of 390 at a cosine of 0.489, under a top match")
    print("  of 0.498. RANK is the signal and SCORE is not. The brief narrows the book to a")
    print("  page; the adjudication is a person's, exactly as it was the day it was caught.")
    return 0


DRAFTED_MARK = re.compile(r"^### ((?:[IVX]+|C)\.\d+)\b.*?(✅\s*DRAFTED)?$")
# RULING 81 (Day 187). The marker is not always on the heading line, and reading only the
# heading line is how this arm reported every Book III chapter as unmarked for four chapters
# while `06` carried a ✅ for each of them. Books I and II put the tick INLINE
# (`### II.1 — THE GROUND ✅ DRAFTED — 2,282 words`); Book III put it on its own line
# underneath, because the entries grew long enough that a heading could not hold the word
# count, the filename, the source discipline and the rulings. Nobody decided that; it just
# happened at III.1 and the gauge went on measuring the old place.
#   The fix reads the chapter's whole BLOCK — heading to next `###` — and accepts a line that
# BEGINS with the tick. Anchored, not free: a bare mention of the word DRAFTED inside a beat
# is not a marker, and a marker for a DIFFERENT chapter inside this chapter's block would need
# to open its own line with a ✅ to count, which is a thing the format does not do.
BLOCK_MARK = re.compile(r"^✅\s*\*{0,2}DRAFTED", re.M)


def status(scaffold_text, dr):
    """`06`'s ✅ DRAFTED markers against what is actually in `book/`.

    Why this is a function and not ten more hand-typed ticks: a `✅ DRAFTED` marker is a
    *"Last Verified"* stamp with a checkmark on it. Somebody asserts it once and it rots in
    silence while the thing it describes moves on — which is exactly what happened. The joint
    read caught the rot and MIS-COUNTED IT, reporting four unmarked chapters when the real
    number was ten, because Book I carries no marker at all and nobody thought to look there.
    A stamp with a gauge behind it is a different object from a stamp.

    ⚠ AND THEN IT ROTTED ITSELF — ruling 81. See BLOCK_MARK above: this function read the
    heading line only, Book III moved the tick to the line below, and the gauge written to
    catch an unmeasured stamp spent four chapters reporting a stamp that was there. The
    lesson is the one it was already carrying, one level down: a gauge is a claim about
    where to look, and that claim rots exactly like the stamp does."""
    marked, missing, phantom = set(), [], []
    lines = scaffold_text.splitlines()
    heads = [(i, m.group(1)) for i, line in enumerate(lines)
             for m in [DRAFTED_MARK.match(line)] if m]
    for n, (i, cid) in enumerate(heads):
        end = heads[n + 1][0] if n + 1 < len(heads) else len(lines)
        block = "\n".join(lines[i:end])
        if "DRAFTED" in lines[i] or BLOCK_MARK.search(block):
            marked.add(cid)
            if cid not in dr:
                phantom.append(cid)
        elif cid in dr:
            missing.append(cid)
    print(f"DRAFT STATUS — `06` markers against book/\n")
    print(f"  {len(dr)} chapter(s) are prose on disk · {len(marked)} marked ✅ in the scaffold")
    if missing:
        print(f"  !! {len(missing)} DRAFTED AND UNMARKED — the scaffold under-reports the work:")
        print(f"     {', '.join(missing)}")
    if phantom:
        # The louder failure of the two and the one with no natural reader: the scaffold
        # claiming prose that does not exist. It cannot happen today; it prints anyway.
        print(f"  !! {len(phantom)} MARKED ✅ WITH NO FILE IN book/ — the scaffold claims prose")
        print(f"     that is not there: {', '.join(phantom)}")
    if not missing and not phantom:
        print("  markers agree with the filesystem.")
    return len(missing) + len(phantom)


def read_disk():
    return [(p.name, p.read_text(encoding="utf-8"))
            for p in sorted(BOOK.glob("*.md")) if p.name != "DRAFT-LOG.md"]


def read_git(rev):
    def _read():
        ls = subprocess.run(["git", "ls-tree", "--name-only", f"{rev}:book"],
                            cwd=ROOT, capture_output=True, text=True, encoding="utf-8")
        if ls.returncode != 0:
            raise SystemExit(f"!! could not list book/ at {rev}: {ls.stderr.strip()}")
        out = []
        for name in ls.stdout.split():
            if not name.endswith(".md") or name == "DRAFT-LOG.md":
                continue
            r = subprocess.run(["git", "show", f"{rev}:book/{name}"],
                               cwd=ROOT, capture_output=True, text=True, encoding="utf-8")
            if r.returncode == 0:
                out.append((name, r.stdout))
        return out
    return _read


def selftest():
    """Both parsers, against the wrap. `beats()` is beat_sweep's and already tested there;
    what is untested anywhere else is `paragraphs()`, and it is the new surface."""
    rc = beat_selftest()
    doc = ("# BOOK I — THE STILL\n\n## I.9 — A TEST\n\nNot by leaving it. There is no\n"
           "leaving — leaving wants a direction.\n\n---\n\nNothing is under repair.\n")
    ps = paragraphs(doc)
    joined = " | ".join(p for _, p in ps)
    ok = ("There is no leaving — leaving wants a direction." in joined
          and len(ps) == 2 and "A TEST" not in joined)
    print("  prose self-test:", "PASS — needles survive a hard wrap, headings excluded"
          if ok else f"** FAIL ** — got {ps!r}")
    return rc or (0 if ok else 2)


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--chapter", help="show only this chapter, e.g. III.1")
    ap.add_argument("--fixture", metavar="REV",
                    help="sweep the tree as it stood at a git rev, exemptions OFF. With "
                         "a65139f this is the calibration and MUST reproduce I.6 ~ II.8")
    ap.add_argument("--selftest", action="store_true")
    ap.add_argument("--brief", action="store_true",
                    help="with --chapter: the pre-draft reading brief — the shipped paragraphs "
                         "nearest each beat, ranked, for a person to read. No verdict.")
    ap.add_argument("--status", action="store_true",
                    help="`06`'s ✅ DRAFTED markers against what is actually in book/")
    ap.add_argument("--quiet", action="store_true", help="hide the exempt lines")
    args = ap.parse_args()

    if args.selftest:
        return selftest()

    if args.status:
        return 1 if status(SCAFFOLD.read_text(encoding="utf-8"), drafted(read_disk)) else 0

    rc = selftest()
    print()
    if rc:
        return rc

    if args.fixture:
        raw = subprocess.run(["git", "show", f"{args.fixture}:06-THE-SCAFFOLD.md"],
                             cwd=ROOT, capture_output=True, text=True, encoding="utf-8")
        if raw.returncode != 0:
            print(f"!! could not read the scaffold at {args.fixture}: {raw.stderr.strip()}")
            return 2
        print(f"CALIBRATION — tree at {args.fixture}, exemptions OFF\n")
        dr = drafted(read_git(args.fixture))
        out = sweep(raw.stdout, dr, focus=args.chapter, exempt=False)
        if out is None:
            return 2
        chs, undrafted, hits, short, hv = out
        report(chs, dr, undrafted, hits, short, hv, exempt=False)
        print()
        print("READING BRIEF — II.8, as it stood before it was drafted")
        rows = brief(raw.stdout, dr, focus="II.8", show=True)
        # SHOW THE WORK. A calibration that prints only its own verdict is a green light with
        # nothing behind it — the whole failure this project keeps finding. The page a person
        # would have read that morning prints in full, so the pass can be disagreed with.
        brief_report(rows, exempt=False)
        # THE CALIBRATION, and it is a rank test rather than a hit test, because that is what
        # the measurement supports. I.6's *"Not by leaving it. There is no leaving…"* must be
        # ON THE BRIEF for one of II.8's beats. If it falls off, the brief has stopped putting
        # the thing a person needed to read in front of them, which is its only job.
        found = [(cid, r, cos) for cid, kind, text, near in (rows or [])
                 for r, cos, pcid, ln, p in near if pcid == "I.6"]
        print()
        if found:
            best = min(found, key=lambda f: f[1])
            print(f"  CALIBRATION PASS — I.6's prose appears on II.8's pre-draft brief, "
                  f"{len(found)} time(s), best rank {best[1]} (cos {best[2]:.3f}).")
            print("  That is the whole claim: a person reading this page before drafting II.8")
            print("  would have met I.6's denials. It is NOT a claim that a threshold fired.")
            return 0
        print("  ** CALIBRATION FAIL ** — I.6 is not on II.8's brief at all.")
        print("  This instrument exists to put exactly that paragraph in front of a reader.")
        return 2

    print(f"PROSE→BEAT SWEEP — book/ against {SCAFFOLD.name}"
          + (f" · chapter {args.chapter}" if args.chapter else "") + "\n")
    dr = drafted(read_disk)
    text = SCAFFOLD.read_text(encoding="utf-8")
    out = sweep(text, dr, focus=args.chapter)
    if out is None:
        return 2
    chs, undrafted, hits, short, hv = out
    rc = report(chs, dr, undrafted, hits, short, hv, quiet=args.quiet)
    if args.brief:
        if not args.chapter:
            print("\n  --brief needs --chapter: the brief is a page to read before drafting ONE")
            print("  chapter. Printed for 55, it is the 390 paragraphs again with extra steps.")
            return 2
        print(f"\nREADING BRIEF — {args.chapter}, before drafting")
        brief_report(brief(text, dr, focus=args.chapter), quiet=args.quiet)
    else:
        print("\n  ⚠ THE FUNCTION ARM DID NOT RUN. The sweep above is word-unit only and is")
        print("  blind to a repeat that shares no vocabulary — ruling 33's own case shared")
        print("  none. Before drafting, run:  --chapter <id> --brief")
    return 1 if rc else 0


if __name__ == "__main__":
    sys.exit(main())
