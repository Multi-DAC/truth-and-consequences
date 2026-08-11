#!/usr/bin/env python3
"""placement_sweep.py — where and when does the book say each person was?

R-152 found `Aquinas, in Paris in the twelve-sixties` and was scoped to the chapter it was
found in. R-158 found the same sentence in two more chapters, one of them a recap that
propagates it forward. This is the population grep that R-158 owed: not "find the defect
I already found", but "find every place/date attribution and show me the ones that
disagree with each other."

A PROVENANCE ERROR IS THE SIGNATURE DEFECT OF THIS BOOK'S SOURCE HANDLING. The doctrine is
right and the address is wrong, and the address is what makes a sentence feel researched.
IV.9's Irenaeus, V.2's Aquinas, and whatever this prints.

WHAT IT MEASURES: for every person named in a chapter, the place-tokens and date-tokens
inside a window around each mention. Then it groups by person across chapters and flags
anyone placed in two different cities, or dated to two different years.

WHAT IT CANNOT DO, and both matter:
  * A DIVERGENCE IS NOT AN ERROR. A person can legitimately be in Paris in one decade and
    Rome in another; a life has more than one address. This flags a QUESTION, and the
    answer is external to the book.
  * AGREEMENT IS NOT CORRECTNESS. Three chapters saying "Paris" agree with each other and
    were all wrong until an hour ago. A name with one consistent placement is UNCHECKED,
    not clean — the tool cannot see outside the corpus.
    [[feedback_correlated_witness_needs_a_channel]]
  * The gazetteer is a fixed list. A place not on it is invisible, and the list was built
    by reading this corpus, so it encodes the corpus as it was.
    [[feedback_denylist_encodes_the_corpus_as_it_was]]
  * A SENTENCE NAMING SEVERAL PEOPLE CROSS-ATTRIBUTES ALL OF THEM. V.3's recap —
    "Aquinas in Rome, Eckhart preaching in Cologne and Maimonides ruling in Cairo" — puts
    every one of the three men in all three cities as far as this tool can tell. Those
    rows are noise and must be read, not counted. Fixing it needs a parser, not a
    proximity rule, and a bad parser would fail silently where this fails loudly.

USAGE
    python tools/placement_sweep.py            # Book V (default)
    python tools/placement_sweep.py IV V       # named books
    python tools/placement_sweep.py --all
"""

from __future__ import annotations

import re
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BOOK = ROOT / "book"
# A placement claim is a CLAUSE, not a character window. The first draft of this tool
# windowed ±140 chars and reported Aquinas in Andalusia, Damascus, Girona and Provence —
# all of them places belonging to the *next sentence* in V.1's list of six. The fix is not
# a tighter threshold; it is the right reporting unit. Scope to the sentence containing the
# name, then require the place to sit within PROXIMITY characters of it.
PROXIMITY = 60

PLACES = [
    "Paris", "Rome", "Cologne", "Cairo", "Safed", "the Galilee", "Volozhin", "Liadi",
    "Lithuania", "Provence", "Girona", "Andalusia", "Damascus", "Baghdad", "Athos",
    "the Rhineland", "Alexandria", "Alexandrian", "Edinburgh", "Long Island", "Brooklyn",
    "Virginia", "Connecticut", "Siberia", "New Hampshire", "Mount Rainier", "the Vatican",
    "England", "Erfurt", "Strasbourg", "Naples", "Orvieto", "Spain", "Córdoba", "Cordoba",
    "Fustat", "Toledo", "Oxford", "Cambridge", "Geneva", "Basel", "Constantinople",
    "Athens", "Alexandria", "Safed", "Vilna", "Prague", "Amsterdam",
]

DECADES = ("tens|twenties|thirties|forties|fifties|sixties|seventies|eighties|nineties")
ORDINALS = ("first|second|third|fourth|fifth|sixth|seventh|eighth|ninth|tenth|eleventh|"
            "twelfth|thirteenth|fourteenth|fifteenth|sixteenth|seventeenth|eighteenth|"
            "nineteenth|twentieth|twenty-first")
DATE_RES = [
    re.compile(r"\b1[0-9]{3}\b"),
    re.compile(r"\b(?:ten|eleven|twelve|thirteen|fourteen|fifteen|sixteen|seventeen|"
               r"eighteen|nineteen)-" + DECADES + r"\b", re.I),
    re.compile(r"\b(?:" + ORDINALS + r") century\b", re.I),
    re.compile(r"\baround \d{3,4}\b", re.I),
]

# A person is worth sweeping only if the book attributes something to them. The list is
# the NAMED band of the roster, persons only — texts and traditions do not have addresses.
PERSONS = [
    "Plotinus", "Proclus", "Dionysius", "Meister Eckhart", "Eckhart", "Thomas Aquinas",
    "Aquinas", "Ibn Arabi", "Augustine", "Maimonides", "Tillich", "Śaṅkara", "Nāgārjuna",
    "Fazang", "Francis Cook", "Isaac Luria", "Chaim Vital", "Shneur Zalman",
    "Vilna Gaon", "Chaim of Volozhin", "Leonard Moskowitz", "Austin Osman Spare", "Spare",
    "Peter Carroll", "Crowley", "Dee", "Edward Kelley", "Jung", "Michael Harner", "Harner",
    "Mircea Eliade", "Robert Monroe", "Kenneth Arnold", "Heinrich Suso", "William James",
    "Walt Whitman", "Emerson", "Nicholas of Cusa", "Cusanus", "Rudolf Otto", "Guénon",
    "Ken Wilber", "Aldous Huxley", "Frithjof Schuon", "W. T. Stace", "Huston Smith",
    "Coomaraswamy", "Agostino Steuco", "Steven Katz", "Robert Forman", "Richard Dawkins",
    "Christopher Hitchens", "Sam Harris", "Daniel Dennett",
]
# Sweep the longest form first so "Eckhart" does not eat "Meister Eckhart".
PERSONS.sort(key=len, reverse=True)


def normalise(text: str) -> str:
    text = text.replace("*", "").replace("_", "")
    text = re.sub(r"(?m)^\s*>+\s?", "", text)
    return re.sub(r"\s+", " ", text)


SENT_RE = re.compile(r"(?<=[.!?])\s+")


def sentence_spans(hay: str) -> list[tuple[int, int]]:
    spans, start = [], 0
    for m in SENT_RE.finditer(hay):
        spans.append((start, m.start()))
        start = m.end()
    spans.append((start, len(hay)))
    return spans


def near(hay: str, sent: tuple[int, int], name_at: tuple[int, int],
         needles: list[str] | list[re.Pattern]) -> set[str]:
    """Tokens inside the name's own sentence and within PROXIMITY chars of the name."""
    s, e = sent
    lo, hi = name_at
    out: set[str] = set()
    for needle in needles:
        finder = (re.finditer(re.escape(needle), hay[s:e]) if isinstance(needle, str)
                  else needle.finditer(hay[s:e]))
        for m in finder:
            at = s + m.start()
            if at + len(m.group(0)) < lo - PROXIMITY or at > hi + PROXIMITY:
                continue
            out.add(m.group(0) if not isinstance(needle, str) else needle)
    return out


def main() -> int:
    argv = [a for a in sys.argv[1:] if not a.startswith("--")]
    books = argv or (["I", "II", "III", "IV", "V", "VI", "VII", "VIII"]
                     if "--all" in sys.argv else ["V"])

    files: list[Path] = []
    for b in books:
        files += sorted(BOOK.glob(f"{b}-*.md"))
    if not files:
        print(f"⛔ no chapters found for {books}")
        return 2

    # person -> place -> [chapter:line-ish context]
    placed: dict[str, dict[str, list[str]]] = defaultdict(lambda: defaultdict(list))
    dated: dict[str, dict[str, list[str]]] = defaultdict(lambda: defaultdict(list))
    mentions = 0

    for path in files:
        hay = normalise(path.read_text(encoding="utf-8"))
        spans = sentence_spans(hay)
        claimed: list[tuple[int, int]] = []
        for person in PERSONS:
            for m in re.finditer(re.escape(person), hay):
                if any(s <= m.start() < e for s, e in claimed):
                    continue          # already counted under a longer form
                claimed.append((m.start(), m.end()))
                mentions += 1
                sent = next((sp for sp in spans if sp[0] <= m.start() < sp[1]),
                            (m.start(), m.end()))
                key = person.split()[-1] if " " in person else person
                ctx = hay[sent[0]:sent[1]].strip()
                for pl in near(hay, sent, (m.start(), m.end()), PLACES):
                    placed[key][pl].append(f"{path.stem}: {ctx[:150]}")
                for dt in near(hay, sent, (m.start(), m.end()), DATE_RES):
                    dated[key][dt.lower()].append(f"{path.stem}: {ctx[:150]}")

    print(f"PLACEMENT SWEEP — books {', '.join(books)} · {len(files)} chapters · "
          f"{mentions} person-mentions · place/date must share the name's SENTENCE "
          f"and sit within ±{PROXIMITY} chars of it.")

    def report(title: str, table: dict[str, dict[str, list[str]]], show_ctx: bool) -> int:
        hits = {k: v for k, v in table.items() if len(v) > 1}
        print(f"\n=== {title} — {len(hits)} name(s) with more than one ===")
        for name in sorted(hits):
            print(f"\n  {name}:")
            for val, ctxs in sorted(table[name].items()):
                chapters = sorted({c.split(':')[0] for c in ctxs})
                print(f"    · {val:<16} {', '.join(chapters)}")
                if show_ctx:
                    for c in ctxs[:2]:
                        print(f"        {c}")
        return len(hits)

    n_pl = report("PLACES", placed, show_ctx=True)
    n_dt = report("DATES", dated, show_ctx=False)

    print("\n" + "-" * 72)
    print("A divergence is a QUESTION, not a finding: a life has more than one address.")
    print("AND AGREEMENT IS NOT CORRECTNESS — three chapters said 'Aquinas in Paris' and")
    print("agreed with each other while all three were wrong. A single consistent")
    print("placement is UNCHECKED, not clean. This tool cannot see outside the corpus.")
    return 1 if (n_pl or n_dt) else 0


if __name__ == "__main__":
    raise SystemExit(main())
