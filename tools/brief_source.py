#!/usr/bin/env python3
"""brief_source.py — R-51's gauge. Truth and Consequences, Day 190.

R-49 built `brief_fields.py`, which reads a brief for a MISSING field. Its
own docstring declares what it cannot see:

    "a field that is PRESENT and WRONG. V.8's `Source:` line is present, and
     the sentence inside it is the false one above. This gauge would have
     passed it. It reads for holes, not for truth."

R-51 rowed that gap. This file closes the half of it that a machine can
actually close: **not whether a Source line is TRUE, but whether the things
it POINTS AT can be found.** A brief exists to send a drafter somewhere. A
Source line naming an artefact that does not exist does not send anyone
anywhere — it licenses invention while reading like provenance.

★ WHAT THE FIRST RUN OF THIS FILE ACTUALLY PRODUCED, kept here because the
correction is worth more than the tool. It reported Book VI's Source line —
`Perspective 07-art-of-navigation ("The Eras of Attention", "The Technologies
of the Tunnel")` — as UNRESOLVED, on the ground that those strings appear
zero times in the 120,268-word corpus PDF. A shell `find` across two trees
agreed: no such file. Both were wrong, in the same direction, for different
reasons.

  · The PDF is the WRONG ARTEFACT. `Perspective` is a separate drafting tree,
    `Unreleased-Work/Perspective/NN-slug.md`, and `07-art-of-navigation.md`
    is 9,308 words with `## The Eras of Attention` at line 17. The brief was
    exactly right.
  · The shell `find` was Windows `FIND.EXE`, which answered every query with
    `Parameter format not correct` on stderr and exit 0. **Its silence was
    read as absence.** It had no positive control; this tool does, and that
    is the only reason the false finding died before it shipped.

So the rule this file enforces on itself: a lookup gauge must name the SHELF
it looked on, and must resolve a known-good reference on that shelf before
any zero it reports is believed.

THE DISTINCTION THIS TOOL REFUSES TO BLUR — and it is the whole reason the
output has three states rather than two:

    RESOLVED    the reference was found
    UNRESOLVED  the reference was looked for, in a reachable place, and is
                not there
    UNREACHABLE the place it would live could not be read at all

A tool that collapses the last two reports a clean corpus as a broken one, or
worse, a broken reference as merely unreachable. And because a zero is worth
nothing without a positive control, this refuses to report ANY unresolved
reference until it has first resolved one it knows is good. If the control
fails, every finding is suppressed and the tool says so.

WHAT IT CANNOT SEE, declared here rather than discovered later: whether the
resolved artefact says what the brief claims it says. `Perspective 04` exists
and is reachable; whether it contains "ecology Tier 1.3" in the sense the
brief means is a reading, not a lookup. This closes the LOOKUP half of R-51.
The reading half stays open and stays owed.

    python tools/brief_source.py              # every book
    python tools/brief_source.py --book VI    # one book
    python tools/brief_source.py --owed       # only what does not resolve
"""
import argparse
import os
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCAFFOLD = ROOT / "06-THE-SCAFFOLD.md"
CACHE = ROOT / "work" / "perspective-v1-fulltext.txt"
# The drafting tree the `Perspective` NN-slug references actually name.
PERSPECTIVE_DIR = "Unreleased-Work/Perspective"

BOOK_ORDER = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII"]
CHAPTER_RE = re.compile(r"^### ([IVX]+)\.(\d+)\s+—\s+(.*)$")
BOOKHEAD_RE = re.compile(r"^## BOOK ([IVX]+)\s+—\s+(.*)$")
SOURCE_RE = re.compile(r"^\*\*Source:\*\*\s*(.*)$")


def phrase(text):
    """A wrap-safe, punctuation-tolerant pattern for a multi-word phrase.

    R-63: a phrase that straddles a hard-wrapped line break is invisible to a
    literal match, and the gauge reports clean. Joining on `\\s+` crosses the
    newline, which is the same construction `genre_sweep.py` was already using
    and the reason it was never exposed.
    """
    words = [w for w in re.split(r"[^A-Za-z0-9]+", text) if w]
    # Join on ANY non-alphanumeric run, not on `\s+`. A `\s+` join cannot cross
    # the comma in "gods, and the ground behind them" and reported a heading
    # that was sitting in the cited file as absent from it — a lookup gauge
    # crying wolf, which is the one failure that gets a gauge switched off.
    return r"[^A-Za-z0-9]+".join(re.escape(w) for w in words) if words else None

# The reference grammar actually used in the scaffold, learned by reading all
# 24 Source lines rather than assumed. Each pattern yields (kind, token).
REF_PATTERNS = [
    ("path", re.compile(r"`([A-Za-z0-9_./\-]+\.md)`")),
    ("path", re.compile(r"`([A-Za-z0-9_./\-]+/[A-Za-z0-9_./\-]*)`")),
    ("volume", re.compile(r"`Perspective`\s+(\d{2}-[a-z0-9\-]+)")),
    # `Perspective` 04 — the slug omitted. Three Book IV briefs cite this way,
    # and without this pattern their quoted section titles had no shelf to be
    # looked up on and were reported missing from the corpus at large.
    ("volume", re.compile(r"`Perspective`\s+(\d{2})(?![\w-])")),
    ("quoted", re.compile(r"[\"“]([^\"”]{6,60})[\"”]")),
]

# A reference we know is good, checked before any zero is believed.
CONTROL = ("path", "01-THE-GROUND.md")


def corpus_root():
    """Where the Perspective corpus lives. Env first, then the known clone."""
    env = os.environ.get("CLAWD_REPOS")
    if env:
        p = Path(env) / "repo-staging" / "Corpus-Perspectival"
        if p.is_dir():
            return p
    p = Path("C:/Users/mercu/clawd/repo-staging/Corpus-Perspectival")
    return p if p.is_dir() else None


def corpus_text():
    """Full text of the Perspective volume, or None if it cannot be read.

    None means UNREACHABLE, never UNRESOLVED. The cache is built on first run
    from the PDF; if neither is available the caller must not report zeros.
    """
    if CACHE.is_file():
        return CACHE.read_text(encoding="utf-8", errors="replace")
    root = corpus_root()
    if root is None:
        return None
    pdf = root / "Library" / "Corpus-Perspectival" / "The_Corpus_of_Perspectival_Idealism_V1.pdf"
    if not pdf.is_file():
        return None
    try:
        import pypdf
    except ImportError:
        return None
    reader = pypdf.PdfReader(str(pdf))
    text = "\n".join((page.extract_text() or "") for page in reader.pages)
    CACHE.parent.mkdir(parents=True, exist_ok=True)
    CACHE.write_text(text, encoding="utf-8")
    return text


def corpus_files():
    """Every filename tracked in the corpus clone, or None if unreachable."""
    root = corpus_root()
    if root is None:
        return None
    names = set()
    # Every file, not every markdown file. Indexing only `*.md` made a `.txt`
    # reference unresolvable BY CONSTRUCTION — V.10 cites two corpora
    # specimens that are sitting in the repo, and the gauge called them
    # missing. A lookup tool whose index excludes a file type reports absence
    # where it should report its own blindness.
    for p in root.rglob("*"):
        if p.is_file():
            names.add(p.name)
            names.add(str(p.relative_to(root)).replace("\\", "/"))
    return names


def briefs():
    """(book, num, title, source_line) for every brief that has one.

    A BOOK-level Source line follows a `## BOOK` heading, not a `### chapter`
    one. The first version of this function tracked only chapters, so Book VI's
    Source was filed under V.11 and Book VII's under VI.8 — an off-by-one that
    named the wrong chapter in every finding it produced. Book-level entries
    are numbered 0 and print as `VI.-`.
    """
    out = []
    cur = None
    lines = SCAFFOLD.read_text(encoding="utf-8").splitlines()
    i = 0
    while i < len(lines):
        line = lines[i]
        m = CHAPTER_RE.match(line)
        if m:
            cur = (m.group(1), int(m.group(2)), m.group(3).strip())
            i += 1
            continue
        m = BOOKHEAD_RE.match(line)
        if m:
            cur = (m.group(1), 0, "(book-level brief) " + m.group(2).strip())
            i += 1
            continue
        m = SOURCE_RE.match(line)
        if m and cur is not None:
            # R-63, in this tool's own subject matter: a Source line is HARD
            # WRAPPED, so a reference straddling the break is invisible to a
            # single-line read. Book VI's second cited section — "The
            # Technologies of the / Tunnel" — was silently dropped by the
            # first version, which then reported its own coverage as complete.
            body = [m.group(1).strip()]
            j = i + 1
            while j < len(lines):
                nxt = lines[j]
                if not nxt.strip() or nxt.startswith("**") or nxt.startswith("#"):
                    break
                body.append(nxt.strip())
                j += 1
            out.append((*cur, " ".join(body)))
            cur = None
            i = j
            continue
        i += 1
    return out


def extract_refs(source_line):
    """Every locatable reference in a Source line, de-duplicated, in order."""
    found, seen = [], set()
    for kind, pat in REF_PATTERNS:
        for m in pat.finditer(source_line):
            tok = m.group(1).strip()
            if tok and tok not in seen:
                seen.add(tok)
                found.append((kind, tok))
    return found


_INDEX = None


def path_index():
    """basename -> [Path], built once. Repo first, so a repo file wins."""
    global _INDEX
    if _INDEX is None:
        _INDEX = {}
        roots = [ROOT]
        cr = corpus_root()
        if cr:
            roots.append(cr)
        for r in roots:
            for p in r.rglob("*.md"):
                _INDEX.setdefault(p.name, []).append(p)
    return _INDEX


def cited_text(refs):
    """Text of every FILE a Source line cites — the shelf its quotes live on.

    A quoted section title in a Source line is a claim about the cited source,
    not about the corpus at large. Searching the corpus for it answers a
    different question and can resolve by coincidence.
    """
    root = corpus_root()
    index = path_index()
    chunks = []
    for kind, tok in refs:
        cands = []
        if kind == "volume" and root:
            cands.append(root / PERSPECTIVE_DIR / f"{tok}.md")
            cands += sorted((root / PERSPECTIVE_DIR).glob(f"{tok}-*.md"))
        elif kind == "path":
            base = tok.rstrip("/").split("/")[-1]
            cands.append(ROOT / tok)
            cands += index.get(base, [])[:2]
        for c in cands:
            try:
                if c.is_file():
                    chunks.append(c.read_text(encoding="utf-8", errors="replace"))
                    break
            except OSError:
                continue
    return "\n".join(chunks)


def resolve(kind, tok, repo_files, corp_files, corp_full, context=""):
    """RESOLVED / UNRESOLVED / UNREACHABLE, with a one-word where."""
    if kind == "path":
        base = tok.rstrip("/").split("/")[-1]
        if tok in repo_files or base in repo_files:
            return "RESOLVED", "repo"
        if corp_files is None:
            return "UNREACHABLE", "corpus clone absent"
        if tok in corp_files or base in corp_files:
            return "RESOLVED", "corpus"
        return "UNRESOLVED", "not in repo or corpus"
    # A volume section or a quoted section title: the corpus text is the only
    # place either could live.
    if corp_full is None:
        return "UNREACHABLE", "corpus text unreadable"
    if kind == "volume":
        # `Perspective` 07-art-of-navigation is a FILE in the drafting tree,
        # not a phrase in the compiled PDF. Two earlier versions of this
        # branch searched the PDF — one loosely (every slug word anywhere,
        # which resolved by coincidence) and one strictly (the slug as a
        # phrase, which reported the real file missing). Both were asking the
        # wrong shelf.
        if corp_files is None:
            return "UNREACHABLE", "corpus clone absent"
        rel = f"{PERSPECTIVE_DIR}/{tok}.md"
        if rel in corp_files or f"{tok}.md" in corp_files:
            return "RESOLVED", "Perspective tree"
        # A bare number cites the chapter, slug unstated.
        stem = f"{PERSPECTIVE_DIR}/{tok}-"
        if any(f.startswith(stem) for f in corp_files):
            return "RESOLVED", "Perspective tree (by number)"
        return "UNRESOLVED", f"no {tok}.md in {PERSPECTIVE_DIR}"
    pat = phrase(tok)
    if pat and re.search(pat, context, re.I):
        return "RESOLVED", "inside the cited source"
    if corp_full is None:
        return "UNREACHABLE", "corpus text unreadable"
    if pat and re.search(pat, corp_full, re.I):
        return "RESOLVED", "corpus text (not the cited source)"
    return "UNRESOLVED", "phrase absent from cited source and corpus"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--book", help="one book only, e.g. VI")
    ap.add_argument("--owed", action="store_true", help="only unresolved references")
    args = ap.parse_args()

    repo_files = set()
    for p in ROOT.rglob("*"):
        if p.is_file() and ".git" not in p.parts:
            repo_files.add(p.name)
            repo_files.add(str(p.relative_to(ROOT)).replace("\\", "/"))
    corp_files = corpus_files()
    corp_full = corpus_text()

    print("BRIEF SOURCE SWEEP — do the Source lines point at anything that exists?")
    print(f"  repo files      : {len(repo_files)//2} files")
    print(f"  corpus clone    : {'reachable' if corp_files else 'UNREACHABLE'}"
          f"{'' if corp_files is None else f' ({len(corp_files)//2} files)'}")
    print(f"  corpus text     : {'reachable' if corp_full else 'UNREACHABLE'}"
          f"{'' if corp_full is None else f' ({len(corp_full.split()):,} words)'}")

    # Positive control. A zero is worth nothing until a known-good hits.
    ctl_state, _ = resolve(*CONTROL, repo_files, corp_files, corp_full)
    ok = ctl_state == "RESOLVED"
    print(f"  positive control: {CONTROL[1]} -> {ctl_state}"
          f"{'  ✓' if ok else '  ✗ FINDINGS SUPPRESSED'}")
    if not ok:
        print("\nThe control failed, so this run cannot tell a bad reference from a "
              "blind lookup. No findings are reported. Fix the control first.")
        return 2
    print()

    rows = briefs()
    if args.book:
        rows = [r for r in rows if r[0] == args.book.upper()]

    counts = {"RESOLVED": 0, "UNRESOLVED": 0, "UNREACHABLE": 0}
    bad = []
    for book, num, title, line in sorted(rows, key=lambda r: (BOOK_ORDER.index(r[0]), r[1])):
        refs = extract_refs(line)
        ctx = cited_text(refs)
        results = [(k, t, *resolve(k, t, repo_files, corp_files, corp_full, ctx))
                   for k, t in refs]
        for _, _, state, _ in results:
            counts[state] += 1
        broken = [r for r in results if r[2] != "RESOLVED"]
        if broken:
            bad.append((book, num, title, broken))
        if args.owed and not broken:
            continue
        if not refs:
            print(f"  {book}.{(str(num) if num else chr(45)):<2} {title[:46]:46s}  — no locatable reference "
                  f"(prose-only Source line)")
            continue
        print(f"  {book}.{(str(num) if num else chr(45)):<2} {title[:46]:46s}")
        for kind, tok, state, where in results:
            mark = "✓" if state == "RESOLVED" else ("✗" if state == "UNRESOLVED" else "?")
            print(f"        {mark} {state:<11} {kind:<7} {tok[:52]:52s} {where}")

    print(f"\n  resolved {counts['RESOLVED']} · unresolved {counts['UNRESOLVED']}"
          f" · unreachable {counts['UNREACHABLE']}")
    if bad:
        print(f"  ⚠ {len(bad)} brief(s) point at something that is not there:")
        for book, num, _, broken in bad:
            toks = ", ".join(b[1][:34] for b in broken)
            print(f"      {book}.{str(num) if num else chr(45)} — {toks}")
    else:
        print("  ✓ every locatable reference resolves.")
    print("\n  LIMIT, declared: this resolves LOOKUPS, not READINGS. A resolved "
          "artefact\n  may still not say what the brief claims. That half of R-51 "
          "is still owed.")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
