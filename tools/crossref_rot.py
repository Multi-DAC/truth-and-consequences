#!/usr/bin/env python3
"""crossref_rot.py — R-148. An endnote that corrects a claim does not correct the claim's readers.

WHY THIS EXISTS. The endnote retrofit annotates IN PLACE by design: the drafted body stays
standing and the correction goes in a note forty lines below it. That is the right call —
silently rewriting drafted prose destroys the record of what was believed when. The cost is
structural and scales with success: every corrected claim becomes a live trap for any chapter
that CITES it, and every gauge in this tree (`endnote_debt.py`, `instrument_sweep.py`,
`edition_scheme_sweep.py`, `pointer_sweep.py`) looks WITHIN a chapter. Nothing looked across.

The instance that filed the row: IV.10 says *"the previous chapter caught the same notation
handing back two confident numbers."* IV.9's body says exactly that. IV.9's **[^12] withdrew
it** — the Promethean entry carries no `Dimensional profile:` line, so *"scored maximal"* has
no cell behind it. IV.10 was drafted from a body that was accurate when written and is now
superseded by matter printed below it. Nobody looked, because there was nowhere to look.

WHAT THE TEST ACTUALLY IS, AND WHY IT IS A RECEIPT RATHER THAN A GUESS. Lexical overlap
between a citation and a note is a similarity score, and a similarity score would have to be
tuned — which means it would be tuned until it agreed with me. The real signal is temporal and
it is already recorded in git:

    the citing line was last touched BEFORE the corrective note landed
        => the citation was written against an uncorrected body.

That is nearly the definition of the defect, and `git blame` settles it per line. IV.10:270 is
2026-08-07; IV.9's [^12] is 2026-08-10. Three days, and no instrument between them until now.
Lexical overlap survives here ONLY as a RANKING within the flagged set — never as a gate.
Gating on overlap is precision eating recall, which is a defect already on file.

WHAT IT CANNOT DO. It cannot adjudicate. A flagged pair is not an error; it is a pair a human
has to read. It locates. That is enough — the failure in the IV.10 case was not bad judgement,
it was that nobody looked.

SEARCH SURFACE, NAMED OUT LOUD. `book/*.md` is not 67 chapters. It also holds `DRAFT-LOG.md`
(2052 dotted refs) and `REVISION-QUEUE.md` (922) — prose ABOUT chapters, which is
indistinguishable by grep from prose that IS one, and which would outnumber the real corpus
twenty to one. Both are excluded by name and the exclusion is PRINTED, not assumed.

WRAPPING. The prose is hard-wrapped at ~95 columns, so a sentence is not a line. Every match
here runs against JOINED PARAGRAPHS. A line-scoped grep over wrapped prose returns nulls that
are not evidence — that is R-37, and it has been rebuilt by accident once already.

USAGE
    python tools/crossref_rot.py                 # tier 1 + tier 2, plus inventory
    python tools/crossref_rot.py --all           # every reference, including tier 3
    python tools/crossref_rot.py --refs          # extraction census only (what it can see)
    python tools/crossref_rot.py IV              # citing chapters in one book
    python tools/crossref_rot.py --ack-template  # emit ack lines for the current tier-1 set

EXIT CODE: 1 if the POSITIVE CONTROL fails (the gauge is broken and its zero means nothing),
or if any tier-1 pair is unacknowledged in `book/CROSSREF-ACK.md`. A reviewed pair is silenced
by its key; editing the citing paragraph changes the key and reopens it, which is correct — a
repair deserves a re-read. Otherwise 0.
"""

from __future__ import annotations

import argparse
import hashlib
import re
import subprocess
import sys
from collections import Counter, defaultdict
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
BOOK = REPO / "book"
ACK_FILE = BOOK / "CROSSREF-ACK.md"

# Prose ABOUT the chapters. Excluded by name, and the exclusion is reported.
NOT_CHAPTERS = {"DRAFT-LOG.md", "REVISION-QUEUE.md", "CROSSREF-ACK.md"}

BOOK_ORDER = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "C"]
CHAPTER_FILE = re.compile(r"^(I{1,3}|IV|VI{0,3}|V|VIII|C)-(\d{2})-(.+)\.md$")

# The pair this gauge was built from. If it stops catching this, its silence is worthless.
CONTROL = {
    "citing": "IV.10",
    "target": "IV.9",
    "note": "12",
    "phrase": "two confident numbers",
}

# ---------------------------------------------------------------------------
# A note is CORRECTIVE when it takes something back. ⛔ is the tree's own marker
# for that and carries the most weight; the lexicon catches the ones that withdraw
# without reaching for the glyph. Both are reported with their class, so a reader
# can see WHICH signal fired rather than trusting a merged verdict.
STOP_GLYPH = "⛔"  # ⛔

CORRECTIVE_LEXICON = [
    r"not in the source",
    r"NOT PRESENT",
    r"does not (?:exist|contain|survive|appear|say)",
    r"no (?:cell|assignment|such|publication|journal|volume|DOI) ",
    r"withdraw(?:n|s|al)?\b",
    r"retract(?:ed|s|ion)?\b",
    r"supersede[ds]?\b",
    r"misattribut",
    r"cannot be verified",
    r"is (?:wrong|false|incorrect)\b",
    r"has no .{0,24}behind it",
    r"never (?:built|ran|run|published)",
    r"\bunreachable\b",
    r"invented",
]
CORRECTIVE_RE = re.compile("|".join(CORRECTIVE_LEXICON), re.I)

RELATIVE_BACK = re.compile(
    r"\bthe (?:previous|preceding|last|foregoing|prior) chapter\b", re.I)
RELATIVE_FWD = re.compile(
    r"\bthe (?:next|following) chapter\b", re.I)
DOTTED = re.compile(r"\b(I{1,3}|IV|VI{0,3}|V|VIII)\.(\d{1,2})\b")
DESCRIPTIVE = re.compile(r"\bthe ([a-z][a-z\-']{3,})(?:\s+[a-z\-']+)?\s+chapter\b", re.I)

TITLE_STOPWORDS = {
    "the", "and", "not", "what", "why", "how", "that", "this", "with", "from",
    "for", "its", "it", "is", "was", "are", "one", "two", "many", "own", "you",
    "your", "cannot", "there", "when", "where", "who", "whom", "being", "been",
    "a", "an", "of", "in", "on", "at", "to", "by", "or", "but", "as", "if",
    "chapter", "book", "first", "second", "third", "last", "next", "previous",
}

WORD = re.compile(r"[a-z][a-z\-']{4,}")


# ---------------------------------------------------------------------------
# Registry


class Chapter:
    def __init__(self, path: Path, book: str, num: int, slug: str):
        self.path = path
        self.book = book
        self.num = num
        self.slug = slug
        self.cid = f"{book}.{num}"
        self.raw = path.read_text(encoding="utf-8")
        self.title = self._title()
        self.body, self.notes_text, self.notes_offset = self._split()
        self.notes = self._parse_notes()
        self.order = 0  # filled by build_registry

    def _title(self) -> str:
        m = re.search(r"^##\s+\S+\s+[—-]\s+(.+)$", self.raw, re.M)
        return m.group(1).strip() if m else self.slug.replace("-", " ")

    def _split(self):
        """Body is everything before the first note DEFINITION at column 0."""
        m = re.search(r"^\[\^\d+\]:", self.raw, re.M)
        if not m:
            return self.raw, "", len(self.raw)
        return self.raw[: m.start()], self.raw[m.start():], m.start()

    def _parse_notes(self):
        """{n: {'text', 'scope', 'corrective', 'why', 'defline'}}

        SCOPE is the body span the marker annotates: from the previous marker to
        this one. That span, not just the note text, is what a citing chapter is
        actually citing — the note is the correction, the scope is the claim.
        """
        out = {}
        marks = [(mm.group(1), mm.start()) for mm in re.finditer(r"\[\^(\d+)\]", self.body)]
        mark_at = {n: pos for n, pos in marks}
        defs = list(re.finditer(r"^\[\^(\d+)\]:[ ]?", self.notes_text, re.M))
        for i, dm in enumerate(defs):
            n = dm.group(1)
            end = defs[i + 1].start() if i + 1 < len(defs) else len(self.notes_text)
            text = self.notes_text[dm.end(): end].strip()
            pos = mark_at.get(n)
            if pos is None:
                scope = ""
            else:
                earlier = [p for _, p in marks if p < pos]
                scope = self.body[(max(earlier) if earlier else 0): pos]
            glyph = STOP_GLYPH in text
            lex = CORRECTIVE_RE.search(text)
            out[n] = {
                "text": text,
                "scope": scope,
                "corrective": bool(glyph or lex),
                "why": "STOP" if glyph else (f"lex:{lex.group(0)[:22]}" if lex else ""),
                "defline": self.raw[: self.notes_offset + dm.start()].count("\n") + 1,
            }
        return out


def build_registry():
    chapters, skipped = {}, []
    for p in sorted(BOOK.glob("*.md")):
        if p.name in NOT_CHAPTERS:
            skipped.append(p.name)
            continue
        m = CHAPTER_FILE.match(p.name)
        if not m:
            skipped.append(p.name)
            continue
        book, num, slug = m.group(1), int(m.group(2)), m.group(3)
        ch = Chapter(p, book, num, slug)
        chapters[ch.cid] = ch
    ordered = sorted(chapters.values(), key=lambda c: (BOOK_ORDER.index(c.book), c.num))
    for i, c in enumerate(ordered):
        c.order = i
    return chapters, ordered, skipped


# ---------------------------------------------------------------------------
# git blame — the whole temporal test rests on this


def blame_dates(path: Path):
    """line-number -> 'YYYY-MM-DD'. Uncommitted lines map to None (UNMEASURED,
    never silently treated as fresh)."""
    try:
        out = subprocess.run(
            ["git", "blame", "--porcelain", "--", str(path.relative_to(REPO))],
            cwd=REPO, capture_output=True, text=True, encoding="utf-8",
            errors="replace", check=True).stdout
    except (subprocess.CalledProcessError, FileNotFoundError):
        return {}
    dates, commit_time, cur = {}, {}, None
    import datetime as _dt
    for line in out.splitlines():
        m = re.match(r"^([0-9a-f]{40}) \d+ (\d+)", line)
        if m:
            cur, lineno = m.group(1), int(m.group(2))
            if cur in commit_time:
                dates[lineno] = commit_time[cur]
            else:
                dates[lineno] = None
                pending = lineno
            continue
        if line.startswith("author-time ") and cur:
            ts = int(line.split()[1])
            d = _dt.datetime.fromtimestamp(ts).strftime("%Y-%m-%d")
            commit_time[cur] = d
            if cur.startswith("0" * 40):
                commit_time[cur] = None
            dates[pending] = commit_time[cur]
    return dates


# ---------------------------------------------------------------------------
# Paragraphs — wrapped prose is joined before anything is matched against it


def paragraphs(body: str, start_line: int = 1):
    """[(text_joined, first_line, last_line)]"""
    out, buf, first = [], [], None
    lineno = start_line - 1
    for raw in body.split("\n"):
        lineno += 1
        if raw.strip():
            if first is None:
                first = lineno
            buf.append(raw.strip())
        elif buf:
            out.append((" ".join(buf), first, lineno - 1))
            buf, first = [], None
    if buf:
        out.append((" ".join(buf), first, lineno))
    return out


# ---------------------------------------------------------------------------
# Reference extraction


def descriptive_index(ordered):
    """distinctive title token -> cid, only where the token is UNIQUE."""
    hits = defaultdict(set)
    for c in ordered:
        for tok in re.findall(r"[a-z][a-z\-']+", c.title.lower()):
            if tok in TITLE_STOPWORDS or len(tok) < 5:
                continue
            hits[tok].add(c.cid)
    unique = {t: next(iter(v)) for t, v in hits.items() if len(v) == 1}
    ambiguous = {t: sorted(v) for t, v in hits.items() if len(v) > 1}
    return unique, ambiguous


def extract_refs(ch, chapters, ordered, desc_index):
    """[(target_cid, kind, line, para_text)] — self-references dropped."""
    refs = []
    body_paras = paragraphs(ch.body, 1)
    note_start_line = ch.raw[: ch.notes_offset].count("\n") + 1
    note_paras = paragraphs(ch.notes_text, note_start_line) if ch.notes_text else []
    for text, first, last in body_paras + note_paras:
        seen = set()

        def add(cid, kind):
            if cid and cid != ch.cid and (cid, kind) not in seen and cid in chapters:
                seen.add((cid, kind))
                refs.append((cid, kind, first, text))

        for bk, n in DOTTED.findall(text):
            add(f"{bk}.{int(n)}", "dotted")
        if RELATIVE_BACK.search(text) and ch.order > 0:
            add(ordered[ch.order - 1].cid, "prev")
        if RELATIVE_FWD.search(text) and ch.order < len(ordered) - 1:
            add(ordered[ch.order + 1].cid, "next")
        for tok in DESCRIPTIVE.findall(text):
            add(desc_index.get(tok.lower()), "descriptive")
    return refs


# ---------------------------------------------------------------------------
# Ranking only. Never gating.


def build_df(ordered):
    df = Counter()
    for c in ordered:
        df.update(set(WORD.findall(c.raw.lower())))
    return df


def overlap(citing_text, note, df, ndocs):
    """Shared DISTINCTIVE terms between the citation and (note + its scope)."""
    target = (note["text"] + " " + note["scope"]).lower()
    a = set(WORD.findall(citing_text.lower()))
    b = set(WORD.findall(target))
    shared = [w for w in (a & b) if df.get(w, ndocs) <= max(6, ndocs // 6)]
    shared.sort(key=lambda w: df.get(w, 0))
    return shared


# ---------------------------------------------------------------------------


def pair_key(citing_cid, para_text, target_cid):
    """Keyed on the CITING PARAGRAPH's text, so editing the paragraph reopens the
    pair. That is deliberate: a repair deserves a re-read."""
    h = hashlib.sha1(re.sub(r"\s+", " ", para_text).strip().encode("utf-8")).hexdigest()[:8]
    return f"{citing_cid}>{target_cid}:{h}"


def load_acks():
    if not ACK_FILE.exists():
        return set()
    return set(re.findall(r"^-\s+`([^`]+)`", ACK_FILE.read_text(encoding="utf-8"), re.M))


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("book", nargs="?", help="restrict CITING chapters to one book")
    ap.add_argument("--all", action="store_true", help="print tier 3 as well")
    ap.add_argument("--refs", action="store_true", help="extraction census only")
    ap.add_argument("--ack-template", action="store_true")
    args = ap.parse_args()

    chapters, ordered, skipped = build_registry()
    desc_index, ambiguous = descriptive_index(ordered)
    df = build_df(ordered)
    ndocs = len(ordered)

    print("CROSS-CHAPTER CITATION ROT — R-148 · measured from disk + git blame")
    print(f"  corpus: {len(ordered)} chapters   "
          f"excluded as prose-about-chapters: {', '.join(skipped) or 'none'}")

    corrective = {c.cid: {n: d for n, d in c.notes.items() if d["corrective"]}
                  for c in ordered}
    n_notes = sum(len(c.notes) for c in ordered)
    n_corr = sum(len(v) for v in corrective.values())
    n_stop = sum(1 for c in ordered for d in c.notes.values() if d["why"] == "STOP")
    print(f"  notes: {n_notes} defined · {n_corr} corrective "
          f"({n_stop} by ⛔, {n_corr - n_stop} by lexicon) "
          f"in {sum(1 for v in corrective.values() if v)} chapters")

    cite_pool = [c for c in ordered if not args.book or c.book == args.book.upper()]

    blame_cache = {}
    def dates_for(ch):
        if ch.cid not in blame_cache:
            blame_cache[ch.cid] = blame_dates(ch.path)
        return blame_cache[ch.cid]

    # THE UNIT IS THE CITATION, NOT THE NOTE. Pairing every reference against every
    # corrective note in the chapter it cites is a cross-product: the first cut of this
    # gauge printed 223 tier-1 rows for ~490 references, which is a reading list nobody
    # reads — the same failure as a WARN that prints at every boot. A human reads ONE
    # citation against the notes of ONE chapter. So one row per citation, carrying the
    # notes that landed after it.
    kinds = Counter()
    tier1, tier2, tier3, unmeasured = [], [], [], []

    for ch in cite_pool:
        refs = extract_refs(ch, chapters, ordered, desc_index)
        for cid, kind, line, text in refs:
            kinds[kind] += 1
            tgt = chapters[cid]
            corr = corrective.get(cid, {})
            if not corr:
                continue
            cite_date = dates_for(ch).get(line)
            tgt_dates = dates_for(tgt)
            stale, current, blind = [], [], []
            for n, note in sorted(corr.items(), key=lambda kv: int(kv[0])):
                note_date = tgt_dates.get(note["defline"])
                entry = {
                    "n": n, "why": note["why"], "date": note_date,
                    "shared": overlap(text, note, df, ndocs),
                }
                if cite_date is None or note_date is None:
                    blind.append(entry)
                elif cite_date < note_date:
                    stale.append(entry)
                else:
                    current.append(entry)
            rec = {
                "citing": ch.cid, "line": line, "text": text, "target": cid,
                "kind": kind, "cite_date": cite_date,
                "stale": stale, "current": current, "blind": blind,
                "shared": sorted({w for e in stale for w in e["shared"]},
                                 key=lambda w: df.get(w, 0)),
            }
            if stale:
                (tier1 if any(e["why"] == "STOP" for e in stale) else tier2).append(rec)
            elif blind:
                unmeasured.append(rec)
            else:
                tier3.append(rec)

    if args.refs:
        print(f"\nREFERENCE CENSUS (citing side, self-refs dropped)")
        for k, v in kinds.most_common():
            print(f"  {v:5d}  {k}")
        print(f"  {sum(kinds.values()):5d}  TOTAL")
        print(f"\n  descriptive index: {len(desc_index)} unique title tokens; "
              f"{len(ambiguous)} AMBIGUOUS tokens skipped (not silently dropped):")
        for t, v in sorted(ambiguous.items())[:8]:
            print(f"      {t:<16} -> {', '.join(v)}")
        return 0

    def gap(rec):
        import datetime as _dt
        try:
            a = _dt.date.fromisoformat(rec["cite_date"])
            b = min(_dt.date.fromisoformat(e["date"]) for e in rec["stale"])
            return f"{(b - a).days}d"
        except Exception:
            return "?"

    def show(rec, mark):
        snippet = re.sub(r"\s+", " ", rec["text"])
        m = re.search(r"(?:previous|preceding|next|following) chapter|"
                      + re.escape(rec["target"]), snippet, re.I)
        if m:
            s = max(0, m.start() - 90)
            snippet = ("…" if s else "") + snippet[s: m.end() + 130] + "…"
        else:
            snippet = snippet[:220] + "…"
        notes = " ".join(
            f"[^{e['n']}]{'⛔' if e['why'] == 'STOP' else '⚠'}"
            f"{'*' if e['shared'] else ''}"
            for e in rec["stale"])
        print(f"\n  {mark} {rec['citing']}:{rec['line']} ({rec['kind']}) → {rec['target']}"
              f"   cited {rec['cite_date']} · {len(rec['stale'])} note(s) landed after "
              f"(+{gap(rec)}): {notes}")
        print(f"      \"{snippet}\"")
        if rec["shared"]:
            print(f"      * shared distinctive terms: {', '.join(rec['shared'][:9])}")
        if rec["current"]:
            print(f"      (also {len(rec['current'])} corrective note(s) that predate "
                  f"the citation — those were available to the drafter)")
        print(f"      key: {pair_key(rec['citing'], rec['text'], rec['target'])}")

    # ---- positive control -------------------------------------------------
    hit = [r for r in tier1 + tier2
           if r["citing"] == CONTROL["citing"] and r["target"] == CONTROL["target"]
           and CONTROL["phrase"] in r["text"]
           and any(e["n"] == CONTROL["note"] for e in r["stale"])]
    control_ok = bool(hit)

    acks = load_acks()
    rank = lambda r: (-len(r["shared"]), -len(r["stale"]), r["citing"], r["line"])
    tier1.sort(key=rank)
    tier2.sort(key=rank)
    open1 = [r for r in tier1 if pair_key(r["citing"], r["text"], r["target"]) not in acks]

    if args.ack_template:
        print("\n# paste into book/CROSSREF-ACK.md once the citation has been READ")
        for r in tier1:
            print(f"- `{pair_key(r['citing'], r['text'], r['target'])}` "
                  f"— {r['citing']}:{r['line']} → {r['target']} "
                  f"({len(r['stale'])} note(s)) · verdict: ")
        return 0

    cap1 = None if args.all else 20
    print(f"\nTIER 1 — the citation predates a ⛔ note in the chapter it cites "
          f"({len(tier1)} citations, {len(open1)} unacknowledged)")
    if not tier1:
        print("  none")
    for r in tier1[:cap1]:
        show(r, "✓" if pair_key(r["citing"], r["text"], r["target"]) in acks else "⛔")
    if cap1 and len(tier1) > cap1:
        print(f"\n  … {len(tier1) - cap1} more tier-1 citations not printed. "
              f"--all prints them; nothing was dropped silently.")

    cap2 = None if args.all else 8
    print(f"\nTIER 2 — the citation predates a lexicon-corrective note, no ⛔ "
          f"({len(tier2)} citations)")
    if not tier2:
        print("  none")
    for r in tier2[:cap2]:
        show(r, "⚠")
    if cap2 and len(tier2) > cap2:
        print(f"\n  … {len(tier2) - cap2} more. --all prints them; "
              f"nothing was dropped silently.")

    print(f"\nTIER 3 — every corrective note in the cited chapter predates the citation "
          f"(drafted with the correction available): {len(tier3)}, not flagged")
    if args.all:
        for r in tier3:
            show(r, "·")

    if unmeasured:
        print(f"\n⚠ UNMEASURED — {len(unmeasured)} citation(s) where a blame date is "
              f"missing (uncommitted line, or file outside git). NOT counted as clean:")
        for r in unmeasured[:10]:
            print(f"    {r['citing']}:{r['line']} → {r['target']} "
                  f"(cited {r['cite_date']}, {len(r['blind'])} undated note(s))")

    print(f"\nPOSITIVE CONTROL — {CONTROL['citing']} → {CONTROL['target']} "
          f"[^{CONTROL['note']}] ({CONTROL['phrase']!r})")
    if control_ok:
        r = hit[0]
        nd = next(e["date"] for e in r["stale"] if e["n"] == CONTROL["note"])
        print(f"  PASS — caught as tier {'1' if r in tier1 else '2'} at "
              f"{r['citing']}:{r['line']}: cited {r['cite_date']}, note landed {nd}.")
        print("  A zero above therefore means something. Without this line it would not.")
    else:
        print("  ⛔ FAIL — the gauge no longer catches the pair it was built from.")
        print("  EVERY COUNT ABOVE IS UNINTERPRETABLE, including a zero.")

    print("\nLIMIT — what a clean run does NOT license:")
    print("  · It locates, it cannot adjudicate. A flagged pair may be perfectly fine;")
    print("    an unflagged one may be rotten. The output is a reading list.")
    print("  · Only DOTTED, PREV/NEXT and unique-title DESCRIPTIVE references are seen.")
    print("    A citation phrased 'as we saw earlier' is invisible to it — run --refs to")
    print("    see the census of what it can resolve at all.")
    print("  · The temporal test asks WHEN, never WHAT. A citing line touched after the")
    print("    note landed for an unrelated reason (a typo fix) leaves tier 1 silently.")
    # Measured, not remembered. This line read "Books I and V carry 0 notes" as a
    # hardcoded string; V.1, V.2 and V.3 were retrofitted on Day 192 and the limit went
    # on printing the pre-retrofit corpus. A gauge whose LIMIT block is a literal is a
    # stamp, not a gauge — Drift #287 inside the disclaimer of an instrument built to
    # catch exactly this. Recompute it every run.
    books = []                      # book order = first appearance in `ordered`
    for c in ordered:
        b = c.cid.split(".")[0]
        if b not in books:
            books.append(b)
    fully = [b for b in books
             if not any(corrective.get(c.cid)
                        for c in ordered if c.cid.split(".")[0] == b)]
    if fully:
        label = ", ".join("the CODA" if b == "C" else f"Book {b}" for b in fully)
        print(f"  · No corrective note anywhere in {label}, so no reference INTO")
        print("    them can ever flag. That is an absence of instrument, not an")
        print("    absence of rot.")
    else:
        print("  · Every book now carries at least one corrective note, so no book is")
        print("    structurally invisible to the temporal test. Individual CHAPTERS")
        print("    still are: a reference into an un-retrofitted chapter cannot flag.")
    bare = [c.cid for c in ordered if not corrective.get(c.cid)]
    print(f"    Chapters with no corrective note: {len(bare)}/{len(ordered)}"
          + (f" — {', '.join(bare[:8])}{' …' if len(bare) > 8 else ''}" if bare else ""))
    print("  · ⛔ THE EDGE IS CHAPTER→CHAPTER. A caveat attached to a FIGURE rather than")
    print("    to a chapter has no edge to travel along and is invisible here. V.2 [^6]")
    print("    qualifies *Eckhart*; V.3 restates the same claim more strongly without")
    print("    citing V.2, so nothing flags. R-162. This is the known blind spot and it")
    print("    is not small: the corpus cites people far more often than it cites")
    print("    chapters.")

    if not control_ok:
        return 1
    if open1:
        print(f"\n⛔ {len(open1)} tier-1 pair(s) unacknowledged — "
              f"add keys to {ACK_FILE.relative_to(REPO)} once read.")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
