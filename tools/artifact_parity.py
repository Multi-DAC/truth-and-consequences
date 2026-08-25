#!/usr/bin/env python3
"""Do the two shipped artifacts carry the same book, and is either one stale?

WHY THIS EXISTS. On Day 206 the release gates read 48/48 with seven green checks
beside a PDF that was thirteen hours older than the prose in it. Every gate in
this repo audits the MANUSCRIPT; not one had ever looked at the ARTIFACT. Then a
second artifact was added — the reflowable EPUB for KDP — which doubles the
surface: now a chapter can ship in one and not the other, and the manuscript gates
stay green either way because from where they stand nothing is wrong.

So this asks the ARTIFACTS what they shipped. Not the compilers, not the roster
they were built from — the finished files, opened and read. A gauge that asks the
generator whether it generated the thing is asking the wrong witness.
[[feedback_artifact_states_its_own_roster]]

Three checks:
  1. ROSTER    the EPUB's spine covers exactly the chapters `_structure` enumerates
  2. FIDELITY  every chapter in the EPUB matches the manuscript word for word,
               and every chapter title is findable in the PDF's text layer
  3. FRESH     each artifact is downstream of the newest prose commit

⚠ Check 2 had a tolerance band when it was first written — a 0.5% word-count
comparison between the two artifacts — and it fired at 1.25% on its first run.
The temptation was to widen the band. The gap turned out to be entirely in the
INSTRUMENT: 1,094 page-number lines and 126 hyphenated line-breaks that pypdf
reports as words, against an EPUB that has neither. Comparing two artifacts
through two different readers can only ever be done to a tolerance, and a
tolerance is a place to hide. So the comparison changed anchors instead: the EPUB
is checked against the MANUSCRIPT, exactly, zero tolerance — and the PDF, which
can only be read back through a lossy text layer, is asked the one question that
layer can answer honestly. [[feedback_instrument_fix_vs_relaxation]]

Exit 0 = all three pass. Non-zero = the count of failures. Prints every reading,
pass or fail, because a gauge that only speaks when it is unhappy trains you to
read silence as health. [[feedback_gauge_can_only_render_its_good_news]]

  python tools/artifact_parity.py
"""
import html as _html
import os
import re
import subprocess
import sys
import zipfile

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BOOK = os.path.join(REPO, "book")
PDF = os.path.join(BOOK, "pdf", "Truth-and-Consequences.pdf")
EPUB = os.path.join(BOOK, "epub", "Truth-and-Consequences.epub")

sys.path.insert(0, BOOK)

# The one string the EPUB adds that the manuscript did not write. Subtracted by
# name so the fidelity check below can stay at zero tolerance; if the compiler
# ever generates a second such string and forgets to declare it here, the check
# fires, which is the correct direction to fail in.
GENERATED_CHROME = ['<h3 class="notes-heading">Notes</h3>']


def git(*args):
    return subprocess.run(["git", "-C", REPO, *args], capture_output=True,
                          text=True, encoding="utf-8", errors="replace").stdout.strip()


def epub_roster():
    """The chapter anchors the EPUB actually ships, read out of its own spine.

    Reading the spine rather than listing the zip is deliberate: a file can sit in
    an EPUB container, manifested and unreferenced, and no reader will ever open
    it. Present is not the same as reachable.
    """
    with zipfile.ZipFile(EPUB) as z:
        opf = z.read("OEBPS/content.opf").decode("utf-8")
        hrefs = dict(re.findall(r'<item id="([^"]+)" href="([^"]+)"', opf))
        order = re.findall(r'<itemref idref="([^"]+)"', opf)
    out = []
    for iid in order:
        href = hrefs.get(iid, "")
        stem = os.path.splitext(os.path.basename(href))[0]
        if stem.startswith("ch-"):
            out.append(stem)
    return out


def words(markup):
    """Visible words in a fragment of markup, tags and entities resolved."""
    return _html.unescape(re.sub(r"<[^>]+>", " ", markup)).split()


def epub_chapter_words(z, anchor):
    x = z.read(f"OEBPS/text/{anchor}.xhtml").decode("utf-8")
    body = re.search(r"<body[^>]*>(.*)</body>", x, re.S).group(1)
    for chrome in GENERATED_CHROME:
        body = body.replace(chrome, " ")
    return len(words(body))


def pdf_text():
    """The PDF's text layer, normalised toward the shape a comparison can use.

    ⚠ Everything undone here is a defect of the READER, not of the book:
      · page numbers  — 1,094 footer lines pypdf reports as words
      · U+2010 breaks — WeasyPrint hyphenates justified prose at line ends
      · f-ligatures   — pypdf drops them, so "suffering" reads "suering"
                        [[reference_pypdf_ligature_extraction_miss]]
      · kerned runs   — "IV.1" comes back as "IV .1", which is why whitespace is
                        removed entirely rather than merely collapsed
    The ligature sequences are deleted from BOTH sides of every comparison, never
    from one, so the normalisation cannot manufacture a match it did not earn.
    """
    from pypdf import PdfReader
    r = PdfReader(PDF)
    raw = "\n".join(p.extract_text() or "" for p in r.pages)
    raw = re.sub(r"(\w)[-‐]\n(\w)", r"\1\2", raw)
    raw = "\n".join(ln for ln in raw.split("\n")
                    if not re.fullmatch(r"\s*\d+\s*", ln))
    return raw, len(r.pages)


def fold(s):
    """Whitespace-free, ligature-free key for presence testing."""
    s = re.sub(r"\s+", "", s)
    for lig in ("ffi", "ffl", "ff", "fi", "fl"):
        s = s.replace(lig, "")
    return s


def newest_prose_commit():
    """Unix time of the last commit touching a book chapter, and whether any
    chapter is dirty in the working tree.

    Chapter files only — `book/pdf/` and `book/epub/` are excluded by construction
    (they are not *.md), so a rebuild can never vouch for its own freshness. That
    self-vouching is the exact shape the Day-206 note warned about.
    """
    ts = git("log", "-1", "--format=%ct", "--", "book/*.md")
    dirty = [ln for ln in git("status", "--porcelain", "--", "book/*.md").splitlines() if ln.strip()]
    return int(ts) if ts else 0, dirty


def artifact_commit_time(relpath):
    ts = git("log", "-1", "--format=%ct", "--", relpath)
    return int(ts) if ts else None


def main():
    fails = []

    for path, label in ((PDF, "PDF"), (EPUB, "EPUB")):
        if not os.path.exists(path):
            print(f"⛔ {label} MISSING: {path}")
            fails.append(f"{label} missing")
    if fails:
        print(f"\n{len(fails)} FAIL — cannot compare artifacts that are not there.")
        return len(fails)

    import _structure
    expected = [_structure.anchor_for(f) for f in _structure.roster()]
    shipped = epub_roster()

    print("1. ROSTER — the EPUB's spine against the book's structure")
    missing = [a for a in expected if a not in shipped]
    extra = [a for a in shipped if a not in expected]
    print(f"     structure enumerates : {len(expected)} chapters")
    print(f"     EPUB spine carries   : {len(shipped)} chapters")
    if missing or extra:
        for a in missing:
            print(f"     ⛔ IN THE BOOK, NOT IN THE EPUB: {a}")
        for a in extra:
            print(f"     ⛔ IN THE EPUB, NOT IN THE BOOK: {a}")
        fails.append("roster")
    elif shipped != expected:
        print("     ⛔ same chapters, DIFFERENT READING ORDER")
        fails.append("roster order")
    else:
        print("     ✅ exact match, same order")

    print("\n2. FIDELITY — does each artifact carry the manuscript")
    md = _structure._markdown()
    total = 0
    off = []
    with zipfile.ZipFile(EPUB) as z:
        for f in _structure.roster():
            src = len(words(_structure.render_chapter(md, os.path.join(BOOK, f))))
            got = epub_chapter_words(z, _structure.anchor_for(f))
            total += src
            if src != got:
                off.append((f, src, got))
    if off:
        for f, src, got in off[:10]:
            print(f"     ⛔ {f}: manuscript {src:,} words, EPUB {got:,} ({got-src:+,})")
        print(f"     ⛔ {len(off)} of {len(_structure.roster())} chapters differ from source")
        fails.append("epub fidelity")
    else:
        print(f"     ✅ EPUB {len(_structure.roster())}/{len(_structure.roster())} chapters "
              f"word-exact against the manuscript ({total:,} words, zero tolerance)")

    # The PDF gets a weaker question because a text layer can only answer a weaker
    # question. It is NOT the same standard, and this line says so rather than
    # letting a second green tick imply it was. [[feedback_compression_that_keeps_truth]]
    ptext, pages = pdf_text()
    folded = fold(ptext)
    absent = [f for f in _structure.roster()
              if fold(_structure.chapter_title(os.path.join(BOOK, f))) not in folded]
    if absent:
        for f in absent[:10]:
            print(f"     ⛔ title not in the PDF's text layer: {f}")
        fails.append("pdf coverage")
    else:
        print(f"     ✅ PDF  {len(_structure.roster())}/{len(_structure.roster())} chapter "
              f"titles present in the text layer, {pages:,} pages "
              f"(presence, not word-exactness — see the module docstring)")

    print("\n3. FRESH — each artifact downstream of the newest prose")
    prose_ts, dirty = newest_prose_commit()
    import datetime

    def stamp(ts):
        return datetime.datetime.fromtimestamp(ts).strftime("%Y-%m-%d %H:%M")
    print(f"     newest prose commit  : {stamp(prose_ts)}")
    for path, label in ((PDF, "PDF"), (EPUB, "EPUB")):
        rel = os.path.relpath(path, REPO).replace("\\", "/")
        ats = artifact_commit_time(rel)
        if ats is None:
            print(f"     ⛔ {label:<4} NEVER COMMITTED — it exists on this disk and nowhere else")
            fails.append(f"{label} uncommitted")
            continue
        lag = (prose_ts - ats) / 3600
        if ats < prose_ts:
            print(f"     ⛔ {label:<4} committed {stamp(ats)} — {lag:.1f}h STALE against the prose")
            fails.append(f"{label} stale")
        else:
            print(f"     ✅ {label:<4} committed {stamp(ats)}")
    if dirty:
        # Not a failure. Uncommitted prose means the comparison above was against
        # the last COMMIT, and the disk has moved past it — the artifacts may be
        # fine and simply cannot be judged yet. Saying so beats a green tick that
        # quietly answered a question nobody asked.
        print(f"     ⚠ {len(dirty)} chapter file(s) modified and uncommitted — the "
              f"freshness reading above is against HEAD, not against your disk:")
        for ln in dirty[:5]:
            print(f"        {ln}")

    print()
    if fails:
        print(f"⛔ {len(fails)} FAIL: {', '.join(fails)}")
    else:
        print("✅ 3/3 — both artifacts carry the same book and both are current.")
    return len(fails)


if __name__ == "__main__":
    sys.exit(main())
