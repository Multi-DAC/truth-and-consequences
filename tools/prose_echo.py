#!/usr/bin/env python3
"""prose_echo.py — ruling 90's instrument. Truth and Consequences, Day 187.

WHY THIS EXISTS, and it is the third confession in this file family.

`beat_sweep.py` compares PLANS to PLANS. `prose_beat_sweep.py` was written because that left a
blind region — a future chapter's beat against a shipped paragraph — and it closed exactly that
one. Its own docstring asks the right question of every gauge here: *what has the project
acquired since this was written that it still cannot see?*

Asked of the pair, the answer is embarrassing and was sitting in plain sight for twenty chapters.
**Nothing in this toolkit compares SHIPPED PROSE to SHIPPED PROSE.**

  beat_sweep         plan   <-> plan     ✅
  prose_beat_sweep   plan   <-> prose    ✅
  (nothing)          prose  <-> prose    ← twenty chapters, ~50,000 words, unmeasured

It was found the way these always are: by eye, late, on a day a chapter shipped. III.6's credit
paragraph closed with *"by working cognitive scientists with an experimental programme
underneath."* III.4 had already shipped *"That is co-constitution, stated by working cognitive
scientists, with an experimental programme under it."* Same credential, same ancestor, two
chapters apart — and **every gauge in this repo passed the file clean**, because a beat is not
involved anywhere in that pair. Both sides are prose. Neither tool admits that corpus.

★★ THE STANDING LESSON, and it is the same one one level up again: **a gauge built to close a
blind region defines a new one at its own edge.** The pair above was not negligence; it was two
instruments each doing exactly its job, with the union of their coverage silently mistaken for
coverage. Ask of any SET of gauges, not just of each: what does no member of the set admit?

WHAT IT CHECKS — TWO ARMS, and the second exists because the first's floor failed calibration on
the day it was written. Headings are stripped: `# BOOK III — THE GAME` is in six files and is
not an echo.

  ARM 1 · ** ECHO **      a shared n-gram (default 6) carrying at least 4 non-stopword tokens.
  ARM 2 · ** SENTENCE **  a whole sentence, normalised, present in two chapters — at ANY content
                          density. This arm is not a refinement of the first; it catches a class
                          the first is blind to by construction.

⚠ THE CALIBRATION FAILURE THAT PRODUCED ARM 2, recorded because a floor chosen by feel is a
claim like any other. The fixture pair is **"Error does not need a territory."** — an entire
sentence, verbatim, in two chapters across a book boundary, and about as distinctive as prose
gets. ARM 1 dropped it: six words, of which *does*, *not* and *a* are stopwords, leaving three
content tokens under a floor of four. Lowering the floor to three surfaced it and took the
book-wide count from 72 to 213, most of it house phrasing. **The floor was not wrong and the
fixture was not wrong. The DISCRIMINATOR was the wrong shape** — a 6-gram spanning a clause
boundary and a 6-gram that is an entire sentence are not the same object, and a content-word
count cannot see the difference. Sentence-hood is the missing feature, so it is measured
directly instead of being approximated by density.

  [q] flag     the hit falls inside a block quotation in at least one chapter. Usually the same
               SOURCE quoted twice, which is a different event from the same AUTHORIAL sentence
               written twice — and is the `beat_sweep` named-opponent question in another dress.

A HIT IS A QUESTION, NEVER A VERDICT. The exemption table below carries the answered ones with
the reason on the same line. Per beat_sweep's doctrine, **an exemption is only ever a specific
PAIR plus a specific gram — never a chapter, never a phrase on its own.** An exemption that
absorbs a class is how a gauge stops measuring.

CALIBRATION, and it is the only reason to trust a clean run:

    python tools/prose_echo.py --selftest

must surface **II.5 ~ III.6 / "error does not need a territory"**. That pair is real, adjudicated
and KEPT — II.5 states the shape of the answer and hands it forward; III.6 is where it is cashed,
and the returning sentence is the reader's signpost that this is the promised answer. A detector
that cannot see a pair we have decided to keep cannot be trusted about one we would want to cut.
"""

import argparse
import collections
import glob
import os
import re
import subprocess
import sys

N = 6
MIN_CONTENT = 4

STOP = set("""
a an the and or but of to in on at by for with from as is are was were be been being it its this
that these those there here not no nor so than then too very can could may might must shall should
will would do does did done has have had having if when while what which who whom whose how why
one two i you he she they we us them him her his their our your my me
""".split())

# ─────────────────────────────────────────────────────────────────────────────
# EXEMPTIONS — (chapter_a, chapter_b, gram_substring) -> reason.
# A specific PAIR and a specific GRAM. Never a chapter alone. Never a phrase alone.
# ─────────────────────────────────────────────────────────────────────────────
#
# ⚠ THE MATCH IS BIDIRECTIONAL CONTAINMENT — `sub in gram or gram in sub`. The first version
#   tested only `sub in gram`, so every exemption phrase LONGER than an n-gram silently muted
#   nothing while looking like a rule in force. Six live hits were the same three adjudicated
#   pairs, printing because the table could not reach them. An exemption that cannot fire is
#   worse than no exemption: it reads as coverage.
EXEMPT = [
    ("II.5", "III.6", "error does not need a territory",
     "★ ADJUDICATED AND KEPT, ruling 90. II.5 STATES the shape and hands it forward explicitly "
     "('the answer is Book III's'); III.6 CASHES it with the argument under it. The returning "
     "sentence is the signpost that this is the promised answer, which is ruling 33's structure "
     "used deliberately rather than stumbled into — I.6 performs, II.8 names."),
    ("II.5", "III.6", "a reality tunnel is a persistent render filter three words",
     "II.5's definition, quoted at the top of the chapter that runs it. A chapter of mechanics "
     "that did not restate its own definition would be starting from nowhere."),
    ("II.5", "III.6", "a repetition that outlived its occasion",
     "II.5's criterion, cited by III.6 at the two sites that depend on it (installation, and the "
     "edit). The criterion is not re-derived; ruling 90 checked that the derivation is absent."),
    ("II.5", "III.6", "a relation between two structures",
     "II.5's Korzybski clause, cited rather than re-argued — III.6 says 'this was settled where "
     "the map was retired' and does not name him a second time. beat_sweep already reserves the "
     "second Korzybski cut for VI.7."),
    ("II.5", "III.6", "if a render cannot be wrong about the ground how is",
     "The handed-forward HOLE, quoted so the reader recognises the question being answered. "
     "Ruling 86 puts the cash site on the record; VI.1 gets the civilisational form."),
    ("I.5", "III.6", "certainties of the people standing nearest",
     "★ DESIGNED. I.5 accretes the five mythically and never names them; III.6 re-cuts one image "
     "into mechanics. Book I plants, Book III runs — the macro-structure, working."),
    ("III.4", "III.6", "francisco varela evan thompson and eleanor rosch",
     "A name. Rule 5 requires the ancestor named in both chapters; the axis is declared in `06` "
     "(III.4 cuts them, III.6 credits them whole)."),
    ("IV.1", "IV.3", "fourth line of our own card",
     "★ ADJUDICATED AND KEPT, Day 188. Not a restatement — a CONTRADICTION of the original, which "
     "is the strongest form of use. IV.1 applies the fourth line to the atlas itself and rules the "
     "boundary UNFINDABLE ('we do not know where, and the not-knowing is structural'). IV.3 returns "
     "the identical phrase to say that in this one chapter it CAN be walked up to, because the "
     "entries answer — and that it stops being visible again at IV.5. The phrase is the signpost "
     "that the same line is being read a second time to a different value; deleting it would hide "
     "the fact that the two chapters disagree on purpose. Contrast the pair repaired the same day: "
     "IV.2~IV.3's 'because at the mineral grade nothing' was a PARAPHRASE of the previous chapter's "
     "own observation, which reads as fresh and is not, and was cut rather than exempted."),
    ("II.6", "IV.5", "all four coheres and keeps cohering",
     "★ ADJUDICATED AND KEPT, Day 188. IV.5 does not assert that a company is a being — it RUNS "
     "II.6's four conditions on one, announced ('Book II gave four conditions... Run them.'). The "
     "rule has to be quoted at the site where it is cashed or the test is being applied from "
     "memory. Signposted, not smuggled — which is the line the IV.2~IV.3 cut above was on the "
     "wrong side of."),
    ("II.6", "IV.5", "own expectations did not already contain",
     "II.6's definition of MEASUREMENT, cited in the sentence that applies it to revenue and a "
     "regulator's letter. A condition restated in the drafter's own words would be a different "
     "condition, silently."),
    ("II.6", "IV.5", "levels had dissolved into one another",
     "★ DESIGNED PARALLEL, and the punchline is the point: II.6's body-with-no-levels is 'a "
     "slurry', IV.5's company-with-no-levels is 'a room of people shouting'. Same frame, same "
     "test, different material, different landing — the structure the whole section announces. "
     "⚠ The verbatim SENTENCE this pair originally carried ('the settling at one level has to be "
     "compatible with the settling at the others') was REWORDED, not exempted: arm 2 caught it and "
     "a whole borrowed sentence is not a citation, it is the drafter reaching for the nearest "
     "phrasing. The gram survives because the frame is deliberate; the sentence did not."),
    ("II.7", "IV.5", "made of something the reader already",
     "Ruling 30's criterion, quoted in the act of being applied a second time — the `egregore` "
     "refusal (ruling 109) is made on identical grounds to the `superposition` ban, and IV.5 says "
     "so on the page. A test reapplied without its own words is a new test wearing the old one's "
     "authority."),
    ("II.3", "IV.5", "the practices are book viii s",
     "The standing forward-reference formula, deliberately fixed. II.3 hands the practices "
     "forward in these words; IV.5 hands them forward in the same words. A recurring promise "
     "kept in one phrasing is a refrain the reader can recognise — varying it would make two "
     "promises out of one."),
]


def strip_headings(text):
    out = []
    for line in text.splitlines():
        if line.lstrip().startswith("#"):
            continue
        out.append(line)
    return "\n".join(out)


def quoted_spans(text):
    """Return the set of word-indices that fall inside a block quotation."""
    idx, inside = set(), 0
    for line in text.splitlines():
        words = tokens(line)
        if line.lstrip().startswith(">"):
            idx.update(range(inside, inside + len(words)))
        inside += len(words)
    return idx


def tokens(s):
    s = re.sub(r"`[^`]*`", " ", s)
    s = re.sub(r"[*_#|>]", " ", s)
    return re.findall(r"[a-z]+", s.lower())


def chapter_id(basename):
    m = re.match(r"([IVX]+)-(\d+)", basename)
    return f"{m.group(1)}.{int(m.group(2))}" if m else basename


def grams_of(text, n):
    body = strip_headings(text)
    w = tokens(body)
    q = quoted_spans(body)
    out = {}
    for i in range(len(w) - n + 1):
        g = " ".join(w[i:i + n])
        if sum(1 for x in w[i:i + n] if x not in STOP) < MIN_CONTENT:
            continue
        out.setdefault(g, False)
        if any(j in q for j in range(i, i + n)):
            out[g] = True
    return out


def exemption_for(a, b, gram):
    for ea, eb, sub, reason in EXEMPT:
        if {a, b} == {ea, eb} and (sub in gram or gram in sub):
            return reason
    return None


SENT_MIN_WORDS = 5


def sentences(text):
    """Normalised sentences, with a flag for block-quoted ones.

    ⚠ THE WRAP RULE, which is beat_sweep's and applies here with teeth: this manuscript is
    hard-wrapped at ~100 columns, so almost every sentence spans two or three LINES. Splitting
    per line finds nothing and reports clean. Paragraphs are joined into one string before any
    sentence boundary is looked for, and --selftest feeds the parser a needle broken across a
    hard wrap.
    """
    body = strip_headings(text)
    out = []
    for para in re.split(r"\n\s*\n", body):
        if not para.strip():
            continue
        q = any(ln.lstrip().startswith(">") for ln in para.splitlines())
        joined = " ".join(ln.strip().lstrip(">").strip() for ln in para.splitlines())
        for raw in re.split(r"(?<=[.!?])\s+", joined):
            w = tokens(raw)
            if len(w) >= SENT_MIN_WORDS:
                out.append((" ".join(w), q))
    return out


def load(root):
    files = {}
    for p in sorted(glob.glob(os.path.join(root, "*.md"))):
        base = os.path.basename(p)
        if "DRAFT-LOG" in base:
            continue
        files[chapter_id(base)] = open(p, encoding="utf-8").read()
    return files


def run(files, n, only=None, quiet=False):
    gr = {cid: grams_of(txt, n) for cid, txt in files.items()}
    sn = {cid: dict(sentences(txt)) for cid, txt in files.items()}
    ids = sorted(gr, key=lambda s: [int(x) if x.isdigit() else x
                                    for x in re.split(r"[.\-]", s)])
    live, sent, muted = collections.defaultdict(list), collections.defaultdict(list), 0
    for i, a in enumerate(ids):
        for b in ids[i + 1:]:
            if only and only not in (a, b):
                continue
            for g in sorted(set(gr[a]) & set(gr[b])):
                if exemption_for(a, b, g):
                    muted += 1
                    continue
                live[(a, b)].append((g, gr[a][g] or gr[b][g]))
            for s in sorted(set(sn[a]) & set(sn[b])):
                if exemption_for(a, b, s):
                    muted += 1
                    continue
                sent[(a, b)].append((s, sn[a][s] or sn[b][s]))

    print(f"PROSE ECHO — {len(files)} drafted chapter(s) · arm 1: {n}-grams, "
          f"≥{MIN_CONTENT} content words · arm 2: whole sentences, ≥{SENT_MIN_WORDS} words"
          + (f" · chapter {only}" if only else ""))
    print()
    total = 0
    for (a, b), hits in sorted(sent.items()):
        print(f"  ** SENTENCE **  {a} ~ {b}   ({len(hits)})")
        for s, q in hits:
            print(f"       {'[q] ' if q else '    '}{s[:110]}")
        total += len(hits)
        print()
    for (a, b), hits in sorted(live.items()):
        print(f"  ** ECHO **  {a} ~ {b}   ({len(hits)})")
        for g, q in hits:
            print(f"       {'[q] ' if q else '    '}{g}")
        total += len(hits)
        print()
    if not total:
        print("  no unexempted echoes.\n")
    print(f"  {total} live hit(s) · {muted} exempted · {len(EXEMPT)} rule(s) in the table")
    if not quiet:
        print()
        print("  A hit is a QUESTION. Designed returns (a definition cited where it is cashed,")
        print("  a Book I image re-cut in Book III) score identically to a sentence written")
        print("  twice by someone who forgot. Adjudicate, then exempt the PAIR AND THE GRAM —")
        print("  never the chapter, never the phrase alone.")
        print("  ⚠ AND THE LIMIT: this reads WORDS. A move performed twice in different")
        print("    vocabulary is invisible here by construction — which is the exact defect")
        print("    prose_beat_sweep was built for, on the other corpus. Neither tool covers it")
        print("    prose-to-prose. That region is still open.")
    return total


def selftest(files, n):
    print("SELFTEST — the calibration pair must surface on ARM 2, which exists because it did "
          "not surface on ARM 1\n")
    sn = {cid: dict(sentences(txt)) for cid, txt in files.items()}
    ok = False
    if "II.5" in sn and "III.6" in sn:
        shared = set(sn["II.5"]) & set(sn["III.6"])
        ok = "error does not need a territory" in shared
    print(f"  arm 2 · II.5 ~ III.6 / 'error does not need a territory' : "
          f"{'FOUND — detector live' if ok else 'MISSING — DETECTOR IS BLIND'}")

    gr = grams_of("the quick brown\nfox jumps over the lazy dog and\nkeeps running", n)
    wrap_g = any("brown fox jumps over" in k for k in gr)
    print(f"  arm 1 wrap self-test (needle across a hard wrap)         : "
          f"{'PASS' if wrap_g else 'FAIL'}")

    wrapped_para = ("Some lead-in clause here.\nError does not need a\nterritory. And a "
                    "trailing clause follows it.")
    wrap_s = "error does not need a territory" in dict(sentences(wrapped_para))
    print(f"  arm 2 wrap self-test (sentence broken across two lines)  : "
          f"{'PASS' if wrap_s else 'FAIL'}")
    print()
    return 0 if (ok and wrap_g and wrap_s) else 1


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default="book")
    ap.add_argument("--chapter")
    ap.add_argument("--n", type=int, default=N)
    ap.add_argument("--fixture", metavar="REV",
                    help="run against book/ as of a git revision")
    ap.add_argument("--selftest", action="store_true")
    ap.add_argument("--quiet", action="store_true")
    a = ap.parse_args()

    if a.fixture:
        names = subprocess.run(["git", "ls-tree", "--name-only", f"{a.fixture}:{a.root}"],
                               capture_output=True, text=True, check=True).stdout.split()
        files = {}
        for nm in names:
            if not nm.endswith(".md") or "DRAFT-LOG" in nm:
                continue
            body = subprocess.run(["git", "show", f"{a.fixture}:{a.root}/{nm}"],
                                  capture_output=True, text=True, check=True).stdout
            files[chapter_id(nm)] = body
        print(f"[fixture {a.fixture}]")
    else:
        files = load(a.root)

    if a.selftest:
        sys.exit(selftest(files, a.n))
    run(files, a.n, a.chapter, a.quiet)


if __name__ == "__main__":
    main()
