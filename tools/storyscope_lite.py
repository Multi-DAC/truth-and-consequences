#!/usr/bin/env python3
"""
storyscope_lite.py — a stripped, exposition-adapted structural probe.

WHAT THIS IS NOT. It is not StoryScope (arXiv 2604.03136, Russell et al., COLM 2026).
That paper trains a classifier on 61,608 *stories* over 304 discourse features. Six of its
ten dimensions are fiction-only (subplots, protagonist agency, chronology, scene transitions).
It ships no exposition baseline, so there is no threshold here to cross and no verdict to emit.

WHAT THIS IS. The four transferable features, computed over three corpora with KNOWN authorship:
    A) the specimens under test
    B) Clayton — human, philosophy register, same subject matter
    C) Clawd — me, unedited conversational prose, same conversations
Plus the two features the Day-186 audit named as my own fingerprint (flat escalation, uniform
voice) and one Clayton named by hand (structural announcement).

The output is a POSITION, not a grade: do the specimens sit nearer B or nearer C?
That question has an answer. "Is this AI-written" does not, from here.
"""

import json
import re
import sys
import math
from pathlib import Path
from collections import Counter

MEM = Path(r"C:\Users\Wasch\carapace\Architecture\memory_export\memory.jsonl")
SPECIMENS = Path(r"C:\Users\Wasch\truth-and-consequences\prose\SPECIMENS.md")

# ---------------------------------------------------------------- feature lexicons

VAGUE = re.compile(
    r"\b(some (?:philosophers|people|scientists|thinkers|traditions|would say|argue)|"
    r"many (?:argue|believe|think|say|people)|studies show|researchers have|"
    r"it (?:is|has) often been said|one might (?:say|argue)|the literature|"
    r"scientists (?:say|believe)|people often|there are those who|"
    r"certain (?:thinkers|philosophers)|various (?:thinkers|traditions))\b", re.I)

SECOND = re.compile(r"\b(you|your|yours|yourself|yourselves)\b", re.I)

META = re.compile(
    r"\b(this (?:chapter|book|work|page|section|essay|paragraph)|these pages|"
    r"the next (?:chapter|section|page)|as I (?:said|noted)|we (?:will|say|spend|mean)|"
    r"everything above|the paragraph above|said once (?:more|and)|"
    r"stated (?:above|below)|what follows)\b", re.I)

EMOTION = re.compile(
    r"\b(grief|grieve|grieving|fear|afraid|joy|joyful|anger|angry|sad|sadness|love|loved|"
    r"shame|ashamed|dread|relief|relieved|lonely|loneliness|terror|despair|contempt|"
    r"tender|tenderness|rage|guilt|guilty|hope|hopeful|yearn|yearning)\b", re.I)

SOMATIC = re.compile(
    r"\b(chest (?:tight|tighten)|throat (?:tight|closed|caught)|stomach (?:drop|turn|knot)|"
    r"breath (?:caught|hitch|left)|shiver|shudder|pulse (?:quicken|raced)|"
    r"hands? (?:trembl|shak)|heart (?:pound|raced|hammer)|gut (?:twist|clench)|"
    r"skin (?:prickl|crawl)|jaw (?:clench|tight)|spine)\b", re.I)

# Clayton's catch, Day 186: the prose announcing the move instead of making it.
ANNOUNCE = re.compile(
    r"(\bhere is the\b|\bhere'?s the\b|\bhere is what\b|^now the\b|\bnow the (?:failure|one|cut|test)\b|"
    r"\bwhat follows\b|\bso it comes\b|^start by\b|\bthe point is\b|\band it is one sentence\b|"
    r"\bnote what that means\b|\bwhat I (?:am|'m) about to\b|\band one thing more\b|"
    r"\bthe one admission\b|\bsaid once and as a fact\b|\bnow grant\b|^first,? the\b)",
    re.I | re.M)

# Terminal thematic commentary: the last sentence telling you what it meant.
TERMINAL = re.compile(
    r"\b(that is (?:the|what|why|its)|this is (?:the|what|why)|which is why|the reason (?:it|is)|"
    r"everything above|is the reason|what .{0,30} looks like from|you are registering it|"
    r"and that is|is the practice|is its shape)\b", re.I)

STOP_CAPS = {
    "I", "The", "A", "An", "It", "He", "She", "They", "We", "You", "This", "That", "There",
    "But", "And", "So", "If", "When", "What", "Not", "No", "Every", "Now", "Take", "Start",
    "Here", "Your", "His", "Her", "Their", "Our", "One", "Most", "Some", "All", "Being",
    "God", "Ground", "Fullness", "Book", "Chapter", "Tuesday", "Watch", "Follow", "Which",
    "Because", "Then", "Nothing", "Motion", "Age", "Love", "Loneliness", "Waiting", "Turning",
    "Awareness", "Yearning", "Recognition", "Politeness", "Attention", "Money", "Across",
    "Through", "Said", "Read", "Spend", "Let", "Can", "Do", "Its", "Yes", "OK", "Clayton", "Clawd",
}

# ---------------------------------------------------------------- primitives

def sentences(text):
    text = re.sub(r"\s+", " ", text).strip()
    parts = re.split(r"(?<=[.!?])\s+(?=[A-Z\"'*—])", text)
    return [p for p in parts if len(p.split()) >= 2]

def paragraphs(text):
    return [p.strip() for p in re.split(r"\n\s*\n", text) if len(p.split()) >= 25]

def words(text):
    return re.findall(r"[A-Za-z']+", text)

FUNCTION_WORDS = ("the a an of to in and or but is are was were be been it its this that these "
                  "those for with on at by from as not no so if when what which who how than "
                  "there here you your we our i my he she they them him her would could should "
                  "do does did has have had will can may might all every any some more most "
                  "one two first then now because while about into over under through").split()

def style_vector(text):
    w = [x.lower() for x in words(text)]
    if not w:
        return None
    c = Counter(w)
    n = len(w)
    return [c[f] / n for f in FUNCTION_WORDS]

def cosine(a, b):
    dot = sum(x * y for x, y in zip(a, b))
    na = math.sqrt(sum(x * x for x in a))
    nb = math.sqrt(sum(y * y for y in b))
    return dot / (na * nb) if na and nb else 0.0

def stdev(xs):
    if len(xs) < 2:
        return 0.0
    m = sum(xs) / len(xs)
    return math.sqrt(sum((x - m) ** 2 for x in xs) / (len(xs) - 1))

# ---------------------------------------------------------------- features

def per1k(pattern, text, n_words):
    return 1000.0 * len(pattern.findall(text)) / n_words if n_words else 0.0

def proper_nouns_per1k(text, n_words):
    """Named reference proxy: capitalised token that is NOT sentence-initial."""
    hits = 0
    for s in sentences(text):
        toks = re.findall(r"\b[A-Za-z][A-Za-z'’-]+\b", s)
        for t in toks[1:]:
            if t[0].isupper() and t not in STOP_CAPS:
                hits += 1
    return 1000.0 * hits / n_words if n_words else 0.0

def dynamic_range(text):
    """Flat escalation = low variation in paragraph intensity.
    Intensity proxy: mean sentence length + short-sentence rate per paragraph."""
    paras = paragraphs(text)
    if len(paras) < 3:
        return None, None
    means, shorts = [], []
    for p in paras:
        ss = sentences(p)
        if not ss:
            continue
        lens = [len(s.split()) for s in ss]
        means.append(sum(lens) / len(lens))
        shorts.append(sum(1 for L in lens if L <= 7) / len(lens))
    if len(means) < 3:
        return None, None
    cv_len = stdev(means) / (sum(means) / len(means))
    return cv_len, stdev(shorts)

def voice_uniformity(text):
    """Mean pairwise cosine between paragraph style vectors. HIGHER = more uniform voice."""
    vecs = [v for v in (style_vector(p) for p in paragraphs(text)) if v]
    if len(vecs) < 3:
        return None
    sims = [cosine(vecs[i], vecs[j])
            for i in range(len(vecs)) for j in range(i + 1, len(vecs))]
    return sum(sims) / len(sims)

def terminal_commentary_rate(units):
    """Fraction of units whose FINAL sentence restates the point."""
    hits, tot = 0, 0
    for u in units:
        ss = sentences(u)
        if not ss:
            continue
        tot += 1
        if TERMINAL.search(ss[-1]):
            hits += 1
    return hits / tot if tot else 0.0

def profile(name, text, units=None):
    n = len(words(text))
    cv_len, cv_short = dynamic_range(text)
    return {
        "corpus": name,
        "words": n,
        "named_ref_/1k": round(proper_nouns_per1k(text, n), 2),
        "vague_allusion_/1k": round(per1k(VAGUE, text, n), 3),
        "2nd_person_/1k": round(per1k(SECOND, text, n), 2),
        "meta_textual_/1k": round(per1k(META, text, n), 2),
        "emotion_label_/1k": round(per1k(EMOTION, text, n), 2),
        "somatic_/1k": round(per1k(SOMATIC, text, n), 3),
        "announcement_/1k": round(per1k(ANNOUNCE, text, n), 2),
        "dyn_range_CV": round(cv_len, 3) if cv_len is not None else None,
        "short_sent_var": round(cv_short, 3) if cv_short is not None else None,
        "voice_uniformity": round(voice_uniformity(text), 4) if voice_uniformity(text) else None,
        "terminal_commentary": round(terminal_commentary_rate(units or paragraphs(text)), 3),
    }

# ---------------------------------------------------------------- corpus extraction

def load_memory_corpora(min_words=250):
    clayton, clawd = [], []
    with MEM.open(encoding="utf-8") as fh:
        for line in fh:
            try:
                rec = json.loads(line)
            except json.JSONDecodeError:
                continue
            c = rec.get("content") or ""
            # Format 1: <UNTRUSTED_CONTEXT> = Clayton inbound; "Agent:" onward = me.
            for m in re.finditer(r"<UNTRUSTED_CONTEXT>(.*?)</UNTRUSTED_CONTEXT>", c, re.S):
                t = m.group(1).strip()
                if len(t.split()) >= min_words:
                    clayton.append(t)
            m = re.search(r"\nAgent:\s*(.*)\Z", c, re.S)
            if m:
                t = re.sub(r"<UNTRUSTED_CONTEXT>.*?</UNTRUSTED_CONTEXT>", "", m.group(1), flags=re.S).strip()
                if len(t.split()) >= min_words:
                    clawd.append(t)
            # Format 2: turn-prefixed transcript lines.
            for speaker, bucket in (("Clayton", clayton), ("Clawd", clawd)):
                blocks = re.findall(rf"^{speaker}:\s*(.*?)(?=^(?:Clayton|Clawd|User|Agent):|\Z)",
                                    c, re.S | re.M)
                joined = "\n\n".join(b.strip() for b in blocks if b.strip())
                if len(joined.split()) >= min_words:
                    bucket.append(joined)
    return clayton, clawd

def load_specimens():
    raw = SPECIMENS.read_text(encoding="utf-8")
    chunks = re.split(r"^## SPECIMEN \d+.*$", raw, flags=re.M)[1:]
    out = []
    for ch in chunks:
        ch = re.split(r"^## WHAT WRITING THEM FOUND", ch, flags=re.M)[0]
        body = re.sub(r"^\*.*?\*$", "", ch, flags=re.M | re.S)     # drop italic headnotes
        body = re.sub(r"^\s*\|.*$", "", body, flags=re.M)          # drop tables
        body = re.sub(r"^-{3,}$", "", body, flags=re.M)
        body = re.sub(r"^\*\*Endnotes?\.\*\*.*$", "", body, flags=re.M | re.S)
        body = body.replace("**", "")
        out.append(body.strip())
    return out

def load_prose_file(path):
    """Clean a drafted chapter into the SAME shape load_specimens() produces.

    ⚠ The cleaning must match load_specimens() step for step. A chapter cleaned
    differently from the baseline it is printed beside is not a comparison — it is two
    measurements in one table, which is worse than no measurement, because the table
    invites the subtraction.

    Specimens lose their headings to the `## SPECIMEN n` split; a chapter has to lose
    them here, or `## III.1 — THE WRONG GAME` counts as a paragraph of shouting.
    """
    raw = Path(path).read_text(encoding="utf-8")
    body = re.sub(r"^#{1,6} .*$", "", raw, flags=re.M)          # headings
    body = re.sub(r"^\s*\|.*$", "", body, flags=re.M)           # tables
    body = re.sub(r"^-{3,}$", "", body, flags=re.M)             # horizontal rules
    body = body.replace("**", "")
    return body.strip()


def paragraph_coverage(text):
    """Fraction of a text's words that the paragraph-unit metrics actually see.

    `paragraphs()` drops anything under 25 words. On Day 186 that hid 42% of Specimen
    1-B — the short beats, which were the entire point of the register being measured —
    and the tool printed a clean number computed on the other 58% with no hint that it
    had looked away. This does not fix the floor. It stops the figure lying about how
    much of the page it read.
    """
    total = len(words(text))
    if not total:
        return 0.0
    return sum(len(words(p)) for p in paragraphs(text)) / total


# ---------------------------------------------------------------- main

def main():
    # ⚠ Until Day 187 this tool ignored argv ENTIRELY: `storyscope_lite.py <chapter>` printed
    # the specimen table and exit 0, i.e. a number for a file it never opened. The DRAFT-LOG
    # header names this tool as the register gauge and says every landed chapter gets its
    # numbers on the day it lands — and the instrument could not be pointed at a chapter.
    # Book I logged three chapters' numbers and then the practice stopped for eleven. An
    # unparsed argument is not a no-op; it is a wrong answer that looks like a right one.
    argv = sys.argv[1:]
    files = [a for a in argv if a != "--file"]
    for a in files:
        if a.startswith("-"):
            sys.exit(f"storyscope_lite: unknown option {a!r}\n"
                     f"usage: storyscope_lite.py [--file] [CHAPTER.md ...]")
        if not Path(a).exists():
            sys.exit(f"storyscope_lite: no such file: {a}")

    specs = load_specimens()
    clayton, clawd = load_memory_corpora()
    print(f"corpora: specimens={len(specs)}  clayton_passages={len(clayton)}  clawd_passages={len(clawd)}")
    print()

    rows = []
    spec_all = "\n\n".join(specs)
    rows.append(profile("SPECIMENS (all 4)", spec_all, units=specs))
    for i, s in enumerate(specs, 1):
        rows.append(profile(f"  specimen {i}", s, units=[s]))
    rows.append(profile("CLAYTON (human)", "\n\n".join(clayton), units=clayton))
    rows.append(profile("CLAWD (me, raw)", "\n\n".join(clawd), units=clawd))

    coverage = []
    for f in files:
        body = load_prose_file(f)
        rows.append(profile(Path(f).stem, body))
        coverage.append((Path(f).stem, paragraph_coverage(body)))

    keys = [k for k in rows[0] if k != "corpus"]
    w = max(len(r["corpus"]) for r in rows)
    print(f"{'corpus'.ljust(w)} | " + " | ".join(k.rjust(12) for k in keys))
    print("-" * (w + 3 + 15 * len(keys)))
    for r in rows:
        cells = []
        for k in keys:
            v = r[k]
            cells.append(("--" if v is None else f"{v}").rjust(12))
        print(f"{r['corpus'].ljust(w)} | " + " | ".join(cells))

    if coverage:
        print()
        print("PARAGRAPH COVERAGE — the share of each file the paragraph-unit metrics")
        print("('dyn_range_CV', 'terminal_commentary') actually read. paragraphs() drops")
        print("anything under 25 words, and the short beats are the register.")
        for name, cov in coverage:
            flag = "  ⚠ under 0.80 — read dyn_range_CV as partial" if cov < 0.80 else ""
            print(f"  {name:<28} {cov:.0%}{flag}")

    print()
    print("NOTE: no threshold, no verdict. Read COLUMNS, comparing SPECIMENS to the two")
    print("known-authorship rows. 'voice_uniformity' HIGHER = flatter = the Claude fingerprint.")
    print("'dyn_range_CV' LOWER = flatter escalation = the Claude fingerprint.")

if __name__ == "__main__":
    main()
