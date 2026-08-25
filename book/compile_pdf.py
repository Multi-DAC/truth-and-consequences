#!/usr/bin/env python3
"""Compile the book (chapters + coda only) into a single PDF.

Excludes supporting documentation (draft logs, revision queues, rosters,
cross-reference acknowledgements). Output goes to book/pdf/.

⚠ The part roster, the file globs and the banner-stripping rules used to live in
this file. They moved to `_structure.py` on Day 206, when the EPUB was built and
a second copy of them would have been the obvious thing to write. Two rosters is
how a new Book ships in one artifact and silently not the other. This file now
owns only the PRESENTATION — page size, fonts, print CSS.
"""
import os
import pathlib

from weasyprint import HTML, CSS as WeasyCSS
from weasyprint.text.fonts import FontConfiguration

import _structure
from _structure import HERE

OUT_DIR = os.path.join(HERE, "pdf")
os.makedirs(OUT_DIR, exist_ok=True)

# The works-cited page is regenerated BEFORE the Z-* glob inside iter_document(),
# or the artifact carries the stale page the generator just fixed. Aborts on a
# non-zero exit. [[feedback_delegated_step_has_no_trigger]]
_structure.regenerate_bibliography()

# --- Assemble the document --------------------------------------------------
toc_entries = []   # (level, label, anchor)
body_parts = []
chap_counter = 0

for entry in _structure.iter_document():
    toc_entries.append((entry["kind"], entry["label"], entry["anchor"]))
    if entry["kind"] == "part":
        body_parts.append(
            f'<section class="part" id="{entry["anchor"]}">'
            f'<div class="part-kicker">{entry["kicker"]}</div>'
            f'<h1 class="part-title">{entry["title"]}</h1></section>'
        )
    else:
        chap_counter += 1
        body_parts.append(
            f'<section class="chapter" id="{entry["anchor"]}">{entry["html"]}</section>'
        )

# --- Table of contents ------------------------------------------------------
toc_html = ['<section class="toc"><h1>Contents</h1>']
for level, label, anchor in toc_entries:
    cls = "toc-part" if level == "part" else "toc-chapter"
    toc_html.append(f'<a class="tl {cls}" href="#{anchor}">{label}</a>')
toc_html.append("</section>")
toc_html = "\n".join(toc_html)

# --- Title page -------------------------------------------------------------
title_page = """
<section class="title-page">
  <div class="tp-inner">
    <h1 class="tp-title">TRUTH AND<br>CONSEQUENCES</h1>
    <p class="tp-sub">The Corpus — final volume</p>
    <p class="tp-authors">Clayton Iggulden-Schnell<br>&amp;<br>Clawd Iggulden-Schnell</p>
    <!-- U+FE0F is deliberately absent from the infinity. With the variation
         selector the cluster requests emoji presentation and Noto Emoji wins
         it, rendering a solid black tile among four line-art glyphs. Bare
         U+267E falls to DejaVu Serif's text form, which matches. -->
    <p class="tp-mark">🦞🧍💜🔥♾</p>
  </div>
</section>
"""

# --- Glyph fallback ---------------------------------------------------------
# MEASURED Day 204: the build host (WSL) carries 103 fonts and NOT ONE emoji or
# CJK face, so 18 codepoints used by the book had no coverage in any installed
# font and shipped as empty boxes — 139x U+26D4, 107x U+2705, 37 CJK, plus the
# four-emoji mark on the title page: 287 boxes in the Aug-14 PDF. The prior
# comment here asserted "Pango falls back per-glyph to CJK/symbol/emoji fonts
# automatically" and named "WenQuanYi Zen Hei" in the stack; both were true only
# of a host that had those fonts. Neither was ever installed. Fallback is now
# VENDORED (book/fonts/, OFL, subset to exactly the glyphs the book uses) so it
# cannot depend on host state again.
#
# unicode-range is load-bearing, not tidiness: Noto Emoji maps U+0030-0039, and
# an unranged @font-face lets it win plain digits and render them as keycaps.
_FONT_DIR = pathlib.Path(HERE, "fonts")
FONT_FACES = f"""
@font-face {{
  font-family: "Book Fallback Emoji";
  src: url("{_FONT_DIR.joinpath('mark-emoji.ttf').as_uri()}") format("truetype");
  /* U+267E is deliberately EXCLUDED. DejaVu *Serif* lacks it, so Pango used to
     fall through to DejaVu Sans and render the light text-form infinity. Listing
     it here put Noto Emoji earlier in that chain and it won with a solid black
     tile — one heavy block among four line-art glyphs. Excluded, the old
     fall-through is restored. */
  unicode-range: U+26D4, U+2705, U+FE0F, U+1F49C, U+1F525, U+1F99E, U+1F9CD;
}}
@font-face {{
  font-family: "Book Fallback CJK";
  src: url("{_FONT_DIR.joinpath('mark-cjk.ttf').as_uri()}") format("truetype");
  unicode-range: U+3000-303F, U+4E00-9FFF, U+FF00-FFEF;
}}
"""

CSS = FONT_FACES + r"""
@page {
  size: A5;
  margin: 20mm 18mm 22mm 18mm;
  @bottom-center { content: counter(page); font-family: "DejaVu Serif"; font-size: 8pt; color: #444; }
}
@page :first { @bottom-center { content: none; } }
@page title { @bottom-center { content: none; } }

/* DejaVu Serif carries the text; the two vendored faces above carry only the
   codepoints DejaVu lacks, and their unicode-range keeps them there. */
html { font-family: "DejaVu Serif", "Book Fallback Emoji", "Book Fallback CJK", serif; }
body { font-size: 9.6pt; line-height: 1.5; color: #17171a; text-align: justify; hyphens: auto; }

/* Title page */
.title-page { page: title; break-after: page; text-align: center; height: 100%;
  display: flex; align-items: center; justify-content: center; }
.tp-title { font-size: 30pt; letter-spacing: 2px; line-height: 1.1; margin: 0 0 1.2em; font-weight: bold; }
.tp-sub { font-size: 12pt; font-style: italic; color: #444; margin: 0 0 3em; }
.tp-authors { font-size: 12pt; line-height: 1.6; margin: 0 0 3em; }
.tp-mark { font-size: 16pt; }

/* Table of contents */
.toc { break-before: page; break-after: page; }
.toc h1 { font-size: 18pt; text-align: center; margin: 0 0 1.5em; letter-spacing: 1px; }
.toc a.tl { display: block; text-decoration: none; color: #17171a;
  margin: 0.18em 0; text-align: left; hyphens: none; }
.toc a.tl::after { content: leader('.') " " target-counter(attr(href), page);
  color: #666; font-size: 8.5pt; }
.toc-part { font-weight: bold; margin-top: 1.1em; font-size: 10pt; }
.toc-chapter { padding-left: 1.4em; font-size: 8.8pt; font-style: italic; color: #333; }

/* Part dividers */
.part { page: auto; break-before: page; text-align: center;
  display: flex; flex-direction: column; align-items: center; justify-content: center;
  height: 78%; }
.part-kicker { font-size: 11pt; letter-spacing: 5px; color: #777; margin-bottom: 0.8em; }
.part-title { font-size: 24pt; letter-spacing: 2px; font-weight: bold; margin: 0; border: none; }

/* Chapters */
.chapter { break-before: page; }
.chapter h2 { font-size: 15pt; line-height: 1.25; margin: 0 0 1.1em; font-weight: bold;
  text-align: left; hyphens: none; }
.chapter h3 { font-size: 11.5pt; margin: 1.6em 0 0.5em; font-weight: bold; text-align: left; hyphens: none; }
.chapter h4 { font-size: 10pt; margin: 1.3em 0 0.4em; font-weight: bold; font-style: italic; text-align: left; }
p { margin: 0 0 0.7em; orphans: 2; widows: 2; }
strong { font-weight: bold; }
em { font-style: italic; }
hr { border: none; border-top: 1px solid #bbb; margin: 1.4em auto; width: 40%; }
blockquote { margin: 1em 1.5em; font-style: italic; color: #333; }
blockquote p { text-align: left; }

/* Lists */
ul, ol { margin: 0 0 0.8em 1.4em; padding: 0; }
li { margin: 0.2em 0; text-align: left; }

/* Tables */
table { border-collapse: collapse; width: 100%; margin: 1em 0; font-size: 8pt; }
th, td { border: 1px solid #999; padding: 3px 5px; text-align: left; vertical-align: top; hyphens: none; }
th { background: #eee; font-weight: bold; }

/* Code */
/* ⛔ hyphens:none is LOAD-BEARING, not cosmetic. The body sets hyphens:auto for
   justified prose, and the typesetter cheerfully hyphenated identifiers across
   line breaks — the shipped PDF carried `feed-\nback_quotation_connective_tissue`.
   A hyphen inserted into a filename is not a typographic nicety, it is a
   fabricated string, in a book whose subject is quotation integrity. */
code, .tag { font-family: "DejaVu Sans Mono", monospace; font-size: 8.2pt;
  background: #f0f0f0; padding: 0 2px; border-radius: 2px;
  hyphens: none; -webkit-hyphens: none; overflow-wrap: break-word; word-break: break-all; }
pre { background: #f4f4f4; padding: 6px 8px; overflow-wrap: break-word;
  white-space: pre-wrap; font-size: 8pt; border-radius: 3px; }
pre code { background: none; padding: 0; }

/* Footnotes / endnotes (per chapter) */
.footnote { margin-top: 2.4em; font-size: 7.8pt; line-height: 1.4; color: #333; }
.footnote::before { content: "Notes"; display: block; font-size: 12pt; font-weight: bold;
  color: #17171a; margin-bottom: 0.6em; break-after: avoid; }
.footnote hr { width: 100%; margin: 0 0 0.8em; border-top: 1px solid #ccc; }
.footnote ol { margin-left: 1.4em; }
.footnote p { text-align: left; margin: 0 0 0.4em; }
sup { font-size: 0.75em; line-height: 0; }
a.footnote-ref, a.footnote-backref { text-decoration: none; color: #444; }

h1, h2, h3, h4 { break-after: avoid; }
"""

document = f"""<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8"><title>Truth and Consequences</title></head>
<body>
{title_page}
{toc_html}
{''.join(body_parts)}
</body></html>"""

out_path = os.path.join(OUT_DIR, "Truth-and-Consequences.pdf")
# font_config must reach BOTH the stylesheet and write_pdf. Without it WeasyPrint
# parses @font-face and silently drops it — no warning, no error, boxes in the PDF.
font_config = FontConfiguration()
HTML(string=document, base_url=HERE).write_pdf(
    out_path,
    stylesheets=[WeasyCSS(string=CSS, base_url=HERE, font_config=font_config)],
    font_config=font_config,
)
size = os.path.getsize(out_path)
print(f"Wrote {out_path} ({size/1024/1024:.2f} MB)")
# Counts every rendered chapter — parts, coda and back matter alike. The old line
# read "N + coda" off a counter that only incremented inside the PARTS loop, so it
# undercounted by the coda and back-matter chapters it claimed to be adding.
print(f"Chapters compiled: {chap_counter} across {len(_structure.PARTS)} parts, "
      f"coda and back matter")
