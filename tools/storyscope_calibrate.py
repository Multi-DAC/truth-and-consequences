#!/usr/bin/env python3
"""
storyscope_calibrate.py — the null distribution the Day-186 gauge did not have.

WHY THIS EXISTS. storyscope_lite.py reported voice_uniformity 0.634 for the specimens
against 0.506 for my raw conversation, and I read that as "the crafted prose is flatter
than the throwaway prose." That reading has a hole in it big enough to walk through:

    specimens  = 27 paragraphs, one afternoon, one subject, one register
    clawd raw  = 1656 paragraphs, months, dozens of subjects, every register

voice_uniformity is MEAN PAIRWISE COSINE between paragraph style vectors. It falls
monotonically as you add topical and register diversity to the pool. So a lower number
for the big corpus is the expected behaviour of the metric under a larger, broader
sample — it is not, on its own, evidence about voice at all. The comparison was
unmatched, and an unmatched comparison on a size-sensitive statistic is not a finding.

WHAT THIS DOES. Bootstraps a MATCHED null: draw from each corpus the same number of
paragraphs as the specimens have (27), with the same length profile, and recompute.
Two draw modes, because they answer different questions:

    RANDOM     — paragraphs drawn from anywhere in the corpus. Upper bound on diversity.
    CONTIGUOUS — a single run of consecutive paragraphs from ONE passage. This is the
                 condition the specimens were actually written under, and therefore the
                 only null against which their number means anything.

The output is a PERCENTILE, not a grade: where does 0.634 sit in the distribution of
numbers this metric produces on prose of known authorship at matched size?

Also runs the FORMAT arm. My conversational prose is Telegram markdown — headers, bold,
bullets, tables. Structural heterogeneity mechanically depresses pairwise cosine. The
'prose-only' variant drops every paragraph carrying list/table/header markup and strips
emphasis, to ask whether the low number was measuring voice or measuring markdown.
"""

import random
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import storyscope_lite as S

random.seed(186)                      # Day-186; fixed so the table is reproducible
B = 400                               # bootstrap draws per corpus per mode
CORPORA_DIR = Path(__file__).parent.parent / "corpora"

# ---------------------------------------------------------------- markup handling

MARKUP_LINE = re.compile(r"^\s*(#{1,6}\s|[-*+]\s|\d+\.\s|\||>|```|---)")
EMPHASIS = re.compile(r"(\*\*|__|\*|_|`)")

def is_marked_up(par):
    return any(MARKUP_LINE.match(ln) for ln in par.splitlines())

def strip_emphasis(par):
    return EMPHASIS.sub("", par)

def prose_only(pars):
    """Keep paragraphs that are continuous prose; strip emphasis from what survives."""
    return [strip_emphasis(p) for p in pars if not is_marked_up(p)]

# ---------------------------------------------------------------- matched sampling

def length_matched(pool, target_lens, tol=0.35):
    """For each target paragraph length, pick a pool paragraph within +/-tol of it."""
    by_len = sorted(pool, key=lambda p: len(p.split()))
    lens = [len(p.split()) for p in by_len]
    out = []
    for t in target_lens:
        lo, hi = t * (1 - tol), t * (1 + tol)
        cands = [p for p, L in zip(by_len, lens) if lo <= L <= hi]
        if not cands:                       # fall back to nearest by length
            cands = [min(by_len, key=lambda p: abs(len(p.split()) - t))]
        out.append(random.choice(cands))
    return out

def contiguous_run(passages, k):
    """A run of k consecutive paragraphs from a single passage, as the specimens were."""
    eligible = [S.paragraphs(p) for p in passages]
    eligible = [ps for ps in eligible if len(ps) >= k]
    if not eligible:
        return None
    ps = random.choice(eligible)
    i = random.randrange(0, len(ps) - k + 1)
    return ps[i:i + k]

def uniformity(pars):
    return S.voice_uniformity("\n\n".join(pars))

def dyn_cv(pars):
    return S.dynamic_range("\n\n".join(pars))[0]

def pct(sorted_vals, x):
    """Percentile of x within sorted_vals, 0-100."""
    below = sum(1 for v in sorted_vals if v < x)
    return 100.0 * below / len(sorted_vals) if sorted_vals else float("nan")

def fragility(pars):
    """How much of dyn_range_CV rests on ONE paragraph.

    Day 187. A chapter is ~14 eligible paragraphs; CV over 14 items is a statistic a
    single outlier can carry, and the DRAFT-LOG had been reporting it to three decimals
    with no dispersion beside it. Leave-one-out: `drop` is observed CV minus the LOWEST
    CV any single deletion produces. Large `drop` does not mean the escalation is fake —
    a 65-word sentence is a real prosodic event — it means the number describes one
    paragraph rather than the chapter, and must not be quoted as though it described
    the chapter. Same class of error as the unmatched comparison this file was built to
    fix: a sample-size-sensitive statistic read as a measurement.
    """
    obs = dyn_cv(pars)
    if obs is None or len(pars) < 4:
        return None
    jk = [dyn_cv(pars[:i] + pars[i + 1:]) for i in range(len(pars))]
    jk = [v for v in jk if v is not None]
    if not jk:
        return None
    return {"obs": obs, "jack_min": min(jk), "jack_max": max(jk), "drop": obs - min(jk)}

def summarise(vals):
    v = sorted(x for x in vals if x is not None)
    if not v:
        return None
    def q(p):
        return v[min(len(v) - 1, int(p * len(v)))]
    return {"n": len(v), "p05": q(.05), "p50": q(.50), "p95": q(.95),
            "mean": sum(v) / len(v), "sorted": v}

# ---------------------------------------------------------------- external corpora

BOILER = re.compile(r"\*\*\*\s*(START|END) OF TH(E|IS) PROJECT GUTENBERG.*?\*\*\*", re.I)

def load_external():
    out = {}
    if not CORPORA_DIR.exists():
        return out
    for f in sorted(CORPORA_DIR.glob("*.txt")):
        raw = f.read_text(encoding="utf-8", errors="replace")
        parts = BOILER.split(raw)
        body = max(parts, key=len) if len(parts) > 1 else raw
        body = re.sub(r"\r\n", "\n", body)
        pars = [p for p in S.paragraphs(body) if len(p.split()) <= 260]
        if len(pars) >= 60:
            out[f.stem] = pars
    return out

# ---------------------------------------------------------------- main

def load_chapter(path):
    """A book chapter as the target, so any chapter gets the specimens' treatment."""
    raw = Path(path).read_text(encoding="utf-8")
    body = re.sub(r"^#.*$", "", raw, flags=re.M)          # drop the two heading lines
    return S.paragraphs(body)


def main():
    argv = sys.argv[1:]
    target_name = "SPECIMENS"
    if argv and argv[0] == "--chapter":
        target_name = Path(argv[1]).stem
        spec_pars = load_chapter(argv[1])
    else:
        specs = S.load_specimens()
        spec_pars = S.paragraphs("\n\n".join(specs))
    K = len(spec_pars)
    target_lens = [len(p.split()) for p in spec_pars]
    spec_u = uniformity(spec_pars)
    spec_d = dyn_cv(spec_pars)

    frag = fragility(spec_pars)
    if frag:
        verdict = ("ROBUST" if frag["drop"] < 0.10 else
                   "FRAGILE — the number describes one paragraph, not the chapter")
        print(f"LEAVE-ONE-OUT on {target_name}: dyn_range_CV={frag['obs']:.3f}  "
              f"jack-min={frag['jack_min']:.3f}  jack-max={frag['jack_max']:.3f}  "
              f"drop={frag['drop']:.3f}  -> {verdict}")
        print()

    clayton, clawd = S.load_memory_corpora()
    clawd_pars = S.paragraphs("\n\n".join(clawd))
    clayton_pars = S.paragraphs("\n\n".join(clayton))

    arms = {
        "CLAWD raw (markdown)": (clawd_pars, clawd),
        "CLAWD prose-only":     (prose_only(clawd_pars), clawd),
        "CLAYTON (human)":      (clayton_pars, clayton),
    }
    for name, pars in load_external().items():
        arms[f"PD · {name}"] = (pars, None)

    print(f"MATCHED NULL — K={K} paragraphs, length-matched to {target_name}, B={B} draws")
    print(f"{target_name} observed:  voice_uniformity={spec_u:.4f}   dyn_range_CV={spec_d:.3f}")
    print()
    hdr = (f"{'corpus':22} | {'mode':10} | {'pool':>6} | {'unif p05':>8} | {'p50':>7} | "
           f"{'p95':>7} | {'spec %ile':>9} | {'dynCV p50':>9} | {'spec %ile':>9}")
    print(hdr); print("-" * len(hdr))

    for name, (pars, passages) in arms.items():
        modes = [("random", None)]
        if passages is not None:
            modes.append(("contiguous", passages))
        for mode, src in modes:
            us, ds = [], []
            for _ in range(B):
                if mode == "random":
                    draw = length_matched(pars, target_lens)
                else:
                    draw = contiguous_run(src, K)
                    if draw is None:
                        break
                us.append(uniformity(draw)); ds.append(dyn_cv(draw))
            su, sd = summarise(us), summarise(ds)
            if not su:
                print(f"{name:22} | {mode:10} | {len(pars):6} |  (no eligible draws)")
                continue
            print(f"{name:22} | {mode:10} | {len(pars):6} | {su['p05']:8.4f} | {su['p50']:7.4f} | "
                  f"{su['p95']:7.4f} | {pct(su['sorted'], spec_u):8.1f}% | "
                  f"{(sd['p50'] if sd else float('nan')):9.3f} | "
                  f"{(pct(sd['sorted'], spec_d) if sd else float('nan')):8.1f}%")

    print()
    print("READ IT THIS WAY. 'spec %ile' is where the specimens' observed number falls in")
    print("that corpus's own matched distribution. 50% = indistinguishable at this sample")
    print("size. Only a number near 95% (uniformity) or near 5% (dyn_range_CV) is evidence")
    print("of the flatness the Day-186 audit claimed. Anything mid-range means the original")
    print("unmatched comparison was reading corpus size, not voice.")

if __name__ == "__main__":
    main()
