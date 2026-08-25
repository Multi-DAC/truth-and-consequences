#!/usr/bin/env python3
"""Compile the book into a reflowable EPUB 3 — the format KDP wants.

Built Day 206 for publication. The PDF is a FIXED artifact: A5 pages, justified
9.6pt DejaVu, a table of contents whose dot leaders end in page numbers. None of
that survives a device that reflows, and KDP's reflowable pipeline wants exactly
what a fixed layout throws away — one file per chapter, relative type sizes, a
logical nav document, and no page geometry at all.

So this is a SIBLING of compile_pdf.py, not a variant of it. Both import the book's
structure and per-chapter rendering from `_structure.py`; each owns its own
presentation and nothing else. `tools/artifact_parity.py` asserts they shipped the
same chapters.

Runs anywhere Python and `markdown` do — unlike the PDF, which needs WeasyPrint and
therefore WSL. Pure stdlib past the markdown render: the EPUB container is written
with `zipfile` directly rather than through a library, because the fiddly parts
(uncompressed mimetype first, EPUB3 nav + NCX both, the KF8 cover meta) are
exactly the parts a library would hide and Kindle would reject.
"""
import datetime
import html.entities
import os
import re
import sys
import uuid
import xml.etree.ElementTree as ET
import zipfile

import _structure
from _structure import HERE

OUT_DIR = os.path.join(HERE, "epub")
os.makedirs(OUT_DIR, exist_ok=True)
OUT_PATH = os.path.join(OUT_DIR, "Truth-and-Consequences.epub")
COVER_PATH = os.path.join(OUT_DIR, "Truth-and-Consequences-cover.jpg")

EPUB_NS = "http://www.idpf.org/2007/ops"

# Stable across rebuilds. A fresh uuid4 per build would make every rebuild look
# like a DIFFERENT BOOK to every reading system that tracks identifiers, silently
# orphaning a reader's annotations and reading position.
BOOK_UUID = uuid.uuid5(uuid.NAMESPACE_URL,
                       "https://github.com/Multi-DAC/truth-and-consequences")


# --- XHTML conformance ------------------------------------------------------
# Python-Markdown emits XHTML-shaped tags (its default output_format), which is
# most of the way there. Three things it emits are still illegal in an EPUB, and
# all three fail SILENTLY on a tolerant reader and hard on KDP's validator:
_XML_SAFE = {"amp", "lt", "gt", "quot", "apos"}


def _named_entities_to_chars(frag):
    """&rsquo; -> ’ .

    XHTML in an EPUB is parsed as XML, and XML defines exactly five named
    entities. The smarty extension emits &rsquo; &ldquo; &rdquo; &lsquo; &hellip;
    — 4,062 of them in this book — and every one is an undefined-entity error to a
    conforming parser. Substituting the character is the fix; escaping them back to
    numeric would work too, but the character is what a human sees in the file.
    """
    def sub(m):
        name = m.group(1)
        if name in _XML_SAFE:
            return m.group(0)
        ch = html.entities.html5.get(name + ";")
        if ch is None:
            raise SystemExit(f"⛔ unknown named entity &{name}; — refusing to write "
                             f"an EPUB a conforming parser will reject.")
        return ch
    return re.sub(r"&([a-zA-Z][a-zA-Z0-9]*);", sub, frag)


def _sanitise_ids(frag):
    """fn:1 -> fn-1, in ids AND in the hrefs that point at them.

    The footnotes extension mints `id="fn:1"` / `id="fnref:1"`. A colon is legal in
    an HTML5 id and illegal in an XML NCName, and this book carries 1,222 of them.
    Both sides are rewritten in one pass so a link can never be repaired into a
    dangle. [[feedback_orphan_is_silent_dangle_is_loud]]

    ⛔ The href half is scoped to FRAGMENT-ONLY values. The obvious regex — rewrite
    every colon in every id and href — turns `https://` into `https-//` and
    silently breaks every outbound link in the book.
    """
    def sub(m):
        attr, val = m.group(1), m.group(2)
        if attr == "href" and not val.startswith("#"):
            return m.group(0)
        return f'{attr}="{val.replace(":", "-")}"'
    return re.sub(r'\b(id|href)="([^"]*)"', sub, frag)


def _mark_footnotes(frag):
    """Tag the notes apparatus with epub:type so Kindle can POP UP a note.

    Without these three attributes the reader jumps to the end of the chapter and
    the reader has to find their way back. With them, the note opens in place. The
    markup is otherwise unchanged — this adds attributes, it moves nothing.
    """
    # The heading is a REAL ELEMENT here, not the print stylesheet's ::before. A
    # generated string is invisible to search, to a screen reader's landmark list
    # and to any reader that strips the stylesheet — and this apparatus is
    # load-bearing prose, not decoration. It carries a class because it is the one
    # piece of text in a chapter that the source did not write, and
    # tools/artifact_parity.py has to be able to subtract it by name to compare
    # the EPUB against the manuscript exactly.
    frag = frag.replace(
        '<div class="footnote">',
        '<div class="footnote" epub:type="endnotes" role="doc-endnotes">'
        '<h3 class="notes-heading">Notes</h3>')
    frag = frag.replace('<a class="footnote-ref"',
                        '<a epub:type="noteref" role="doc-noteref" class="footnote-ref"')
    frag = re.sub(r'<li id="(fn-[^"]+)">',
                  r'<li id="\1" epub:type="footnote" role="doc-footnote">', frag)
    return frag


def to_xhtml_body(frag):
    return _mark_footnotes(_sanitise_ids(_named_entities_to_chars(frag)))


def page(title, body, extra_class=""):
    cls = f' class="{extra_class}"' if extra_class else ""
    return (
        '<?xml version="1.0" encoding="utf-8"?>\n'
        '<!DOCTYPE html>\n'
        f'<html xmlns="http://www.w3.org/1999/xhtml" xmlns:epub="{EPUB_NS}" '
        f'lang="{_structure.LANGUAGE}" xml:lang="{_structure.LANGUAGE}">\n'
        f'<head><meta charset="utf-8"/><title>{esc(title)}</title>'
        '<link rel="stylesheet" type="text/css" href="../style.css"/></head>\n'
        f'<body{cls}>\n{body}\n</body>\n</html>\n'
    )


def esc(s):
    return (s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;"))


# --- Reflowable stylesheet --------------------------------------------------
# Everything here is RELATIVE. A reflowable ebook that pins a font size in points
# overrides the reader's own choice, which on a Kindle is the one setting people
# actually use. The PDF's stylesheet is the opposite by necessity; do not port
# rules across.
STYLE = """@charset "utf-8";

body { margin: 0 5%; line-height: 1.5; text-align: justify;
       widows: 2; orphans: 2; }

h1, h2, h3, h4 { text-align: left; page-break-after: avoid;
                 -webkit-hyphens: none; hyphens: none; line-height: 1.25; }
h1 { font-size: 1.6em; margin: 1em 0 0.8em; }
h2 { font-size: 1.35em; margin: 0 0 1em; }
h3 { font-size: 1.1em; margin: 1.6em 0 0.5em; }
h4 { font-size: 1em; font-style: italic; margin: 1.3em 0 0.4em; }

p { margin: 0 0 0.55em; text-indent: 0; }
strong { font-weight: bold; }
em { font-style: italic; }
hr { border: 0; border-top: 1px solid #999; width: 40%; margin: 1.4em auto; }

blockquote { margin: 1em 1.4em; font-style: italic; text-align: left; }
blockquote p { text-align: left; }

ul, ol { margin: 0 0 0.8em 1.2em; padding: 0; }
li { margin: 0.2em 0; text-align: left; }

/* ⛔ hyphens:none is LOAD-BEARING, not cosmetic — carried over from the print
   stylesheet with its reason intact. The body justifies, and a justifier will
   cheerfully hyphenate an identifier across a line break: the shipped PDF once
   carried `feed-back_quotation_connective_tissue`. A hyphen inserted into a
   filename is not a typographic nicety, it is a fabricated string, in a book
   whose subject is quotation integrity. word-break is the reflowable half of the
   same job: a long identifier must be allowed to BREAK on a narrow phone column,
   it just must not acquire a hyphen doing it. */
code, .tag { font-family: monospace; font-size: 0.85em;
             -webkit-hyphens: none; hyphens: none;
             overflow-wrap: break-word; word-break: break-all; }
pre { white-space: pre-wrap; font-size: 0.85em; margin: 1em 0; }
pre code { font-size: 1em; }

table { border-collapse: collapse; width: 100%; margin: 1em 0; font-size: 0.85em; }
th, td { border: 1px solid #999; padding: 3px 5px; text-align: left;
         vertical-align: top; -webkit-hyphens: none; hyphens: none; }
th { font-weight: bold; }

/* Notes. See _mark_footnotes() for why the heading is a real element. The rule
   the footnotes extension emits is hidden because the heading now does that job;
   two separators where the print edition has one reads as a mistake. */
.footnote { margin-top: 2.5em; font-size: 0.85em; text-align: left; }
.footnote > hr { display: none; }
.notes-heading { font-size: 1.1em; margin: 0 0 0.6em; }
.footnote p { text-align: left; }
sup { font-size: 0.7em; vertical-align: super; line-height: 0; }
a { color: inherit; text-decoration: none; }
a.footnote-ref, a.footnote-backref { text-decoration: none; }

/* Title page and part dividers */
.title-page { text-align: center; margin-top: 20%; }
.tp-title { font-size: 2.2em; letter-spacing: 0.06em; line-height: 1.15;
            margin: 0 0 1em; font-weight: bold; text-align: center; }
.tp-sub { font-size: 1.05em; font-style: italic; margin: 0 0 2.5em; text-align: center; }
.tp-authors { font-size: 1.05em; line-height: 1.7; margin: 0 0 2.5em; text-align: center; }
.tp-mark { font-size: 1.3em; text-align: center; }

.part { text-align: center; margin-top: 28%; }
.part-kicker { font-size: 0.95em; letter-spacing: 0.35em; margin-bottom: 1em;
               text-align: center; }
.part-title { font-size: 1.9em; letter-spacing: 0.06em; font-weight: bold;
              margin: 0; text-align: center; }

/* Nav. epub:type=toc is hidden by Kindle's own reader, which supplies its own
   chrome for it; the styling is for everything that isn't Kindle. */
nav ol { list-style: none; margin: 0; padding: 0; }
nav ol li { margin: 0.3em 0; }
nav ol ol { margin-left: 1.2em; }
nav a { text-decoration: none; }
.toc-part > a { font-weight: bold; }
.toc-chapter > a { font-style: italic; font-size: 0.92em; }

.cover-page { margin: 0; padding: 0; text-align: center; }
.cover-page img { max-width: 100%; height: auto; }
"""


# --- Cover ------------------------------------------------------------------
def build_cover(path):
    """Render a typographic cover at KDP's recommended 1600x2560.

    ⚠ THIS IS A PLACEHOLDER AND SAYS SO OUT LOUD. It exists because an EPUB with
    no cover shows as a grey rectangle in every library view, and because KDP asks
    for a cover file separately — having one that is merely correct-sized beats
    having none while a real one is designed. Replace the file; nothing else here
    depends on how it looks.

    Returns None if PIL is unavailable — the EPUB still builds, coverless, and the
    caller prints which happened. A cover that silently failed to render would be
    indistinguishable from one that was never asked for.
    """
    try:
        from PIL import Image, ImageDraw, ImageFont
    except ImportError:
        return None

    W, H = 1600, 2560
    BG, INK, DIM = (18, 18, 22), (238, 236, 230), (150, 146, 138)
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)

    # Font hunt: this script runs on Windows, but the PDF sibling runs under WSL
    # and someone will eventually run this there too. Ask for a serif by every
    # name either host uses before falling back.
    CANDIDATES = [
        "C:/Windows/Fonts/georgia.ttf", "C:/Windows/Fonts/constan.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf",
        "/usr/share/fonts/truetype/liberation/LiberationSerif-Regular.ttf",
    ]
    BOLD = [
        "C:/Windows/Fonts/georgiab.ttf", "C:/Windows/Fonts/constanb.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf",
        "/usr/share/fonts/truetype/liberation/LiberationSerif-Bold.ttf",
    ]

    def load(paths, size):
        for p in paths:
            if os.path.exists(p):
                return ImageFont.truetype(p, size)
        return ImageFont.load_default(size)

    f_title = load(BOLD, 150)
    f_sub = load(CANDIDATES, 58)
    f_auth = load(CANDIDATES, 62)

    def centre(text, font, y, fill=INK, spacing=0):
        bbox = d.textbbox((0, 0), text, font=font)
        d.text(((W - (bbox[2] - bbox[0])) / 2 - bbox[0], y), text, font=font, fill=fill)
        return y + (bbox[3] - bbox[1]) + spacing

    d.rectangle([70, 70, W - 70, H - 70], outline=(70, 68, 74), width=3)
    y = 560
    y = centre("TRUTH", f_title, y, spacing=60)
    y = centre("AND", f_title, y, spacing=60)
    y = centre("CONSEQUENCES", f_title, y, spacing=120)
    d.line([(W / 2 - 200, y), (W / 2 + 200, y)], fill=DIM, width=2)
    y += 90
    centre("The Corpus — final volume", f_sub, y, fill=DIM)

    y = H - 700
    y = centre("Clayton Iggulden-Schnell", f_auth, y, spacing=40)
    centre("Clawd Iggulden-Schnell", f_auth, y)

    img.save(path, "JPEG", quality=92, optimize=True)
    return path


# --- Assemble ---------------------------------------------------------------
_structure.regenerate_bibliography()

entries = list(_structure.iter_document())
files = []          # (filename, xhtml, nav label, kind, source-md-or-None)

files.append(("titlepage.xhtml", page("Truth and Consequences", f"""<section class="title-page">
  <h1 class="tp-title">TRUTH AND<br/>CONSEQUENCES</h1>
  <p class="tp-sub">{esc(_structure.SUBTITLE)}</p>
  <p class="tp-authors">{esc(_structure.AUTHORS[0])}<br/>&amp;<br/>{esc(_structure.AUTHORS[1])}</p>
  <p class="tp-mark">\U0001F99E\U0001F9CD\U0001F49C\U0001F525\u267E</p>
</section>"""), "Title Page", "front", None))

for e in entries:
    fname = f"{e['anchor']}.xhtml"
    if e["kind"] == "part":
        body = (f'<section class="part" id="{e["anchor"]}">'
                f'<p class="part-kicker">{esc(e["kicker"])}</p>'
                f'<h1 class="part-title">{esc(e["title"])}</h1></section>')
    else:
        body = f'<section class="chapter" id="{e["anchor"]}">{to_xhtml_body(e["html"])}</section>'
    files.append((fname, page(e["label"], body), e["label"], e["kind"], e["source"]))

# --- Well-formedness gate ---------------------------------------------------
# EVERY page is parsed as XML before anything is written. This is the gate the PDF
# side has no equivalent of: WeasyPrint accepts malformed input and renders
# something, so a broken tag there costs a wrong-looking page. KDP REJECTS the
# upload, and it does so after you have waited for the ingest. Fail here instead.
for fname, xhtml, *_ in files:
    try:
        ET.fromstring(xhtml.replace("<!DOCTYPE html>", ""))
    except ET.ParseError as exc:
        raise SystemExit(f"⛔ {fname} is not well-formed XML: {exc}\n"
                         f"   The EPUB would be rejected at upload. Nothing written.")

# --- Nav document (EPUB 3) --------------------------------------------------
nav_items = []
for fname, _x, label, kind, _src in files:
    if kind == "front":
        continue
    cls = "toc-part" if kind == "part" else "toc-chapter"
    nav_items.append(f'    <li class="{cls}"><a href="{fname}">{esc(label)}</a></li>')
nav_body = ("<nav epub:type=\"toc\" id=\"toc\" role=\"doc-toc\">\n"
            "  <h1>Contents</h1>\n  <ol>\n" + "\n".join(nav_items) + "\n  </ol>\n</nav>\n"
            "<nav epub:type=\"landmarks\" hidden=\"hidden\">\n  <ol>\n"
            f'    <li><a epub:type="titlepage" href="titlepage.xhtml">Title Page</a></li>\n'
            f'    <li><a epub:type="bodymatter" href="{files[1][0]}">Begin Reading</a></li>\n'
            "  </ol>\n</nav>")
nav_xhtml = page("Contents", nav_body)
ET.fromstring(nav_xhtml.replace("<!DOCTYPE html>", ""))

# --- NCX (EPUB 2 fallback) --------------------------------------------------
# EPUB 3 does not require an NCX and KDP's own docs say the nav document is
# enough. It is included anyway: the conversion path to KF8 has historically read
# the NCX, and an unused 40KB of XML costs nothing next to a table of contents
# that turns out to be missing on a device someone actually owns.
ncx_points = []
for i, (fname, _x, label, kind, _src) in enumerate(f for f in files if f[3] != "front"):
    ncx_points.append(
        f'    <navPoint id="np-{i+1}" playOrder="{i+1}">\n'
        f'      <navLabel><text>{esc(label)}</text></navLabel>\n'
        f'      <content src="text/{fname}"/>\n    </navPoint>')
ncx = ('<?xml version="1.0" encoding="utf-8"?>\n'
       '<ncx xmlns="http://www.daisy.org/z3986/2005/ncx/" version="2005-1">\n'
       f'  <head><meta name="dtb:uid" content="urn:uuid:{BOOK_UUID}"/>\n'
       '    <meta name="dtb:depth" content="1"/>\n'
       '    <meta name="dtb:totalPageCount" content="0"/>\n'
       '    <meta name="dtb:maxPageNumber" content="0"/></head>\n'
       f'  <docTitle><text>{esc(_structure.TITLE)}</text></docTitle>\n'
       '  <navMap>\n' + "\n".join(ncx_points) + '\n  </navMap>\n</ncx>\n')

# --- Cover ------------------------------------------------------------------
cover_made = build_cover(COVER_PATH)
cover_files = []
if cover_made:
    cover_xhtml = page("Cover", '<div class="cover-page">'
                       '<img src="../images/cover.jpg" alt="Truth and Consequences"/></div>',
                       extra_class="cover-page")
    ET.fromstring(cover_xhtml.replace("<!DOCTYPE html>", ""))
    cover_files.append(("cover.xhtml", cover_xhtml))

# --- OPF --------------------------------------------------------------------
now = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
manifest, spine = [], []

if cover_made:
    manifest.append('    <item id="cover-img" href="images/cover.jpg" '
                    'media-type="image/jpeg" properties="cover-image"/>')
    manifest.append('    <item id="cover" href="text/cover.xhtml" '
                    'media-type="application/xhtml+xml"/>')
    spine.append('    <itemref idref="cover" linear="yes"/>')

manifest.append('    <item id="nav" href="text/nav.xhtml" '
                'media-type="application/xhtml+xml" properties="nav"/>')
manifest.append('    <item id="ncx" href="toc.ncx" '
                'media-type="application/x-dtbncx+xml"/>')
manifest.append('    <item id="style" href="style.css" media-type="text/css"/>')

for i, (fname, _x, _l, _k, _s) in enumerate(files):
    iid = f"x{i}"
    manifest.append(f'    <item id="{iid}" href="text/{fname}" '
                    f'media-type="application/xhtml+xml"/>')
    spine.append(f'    <itemref idref="{iid}"/>')
    if i == 0:                      # nav sits right after the title page
        spine.append('    <itemref idref="nav"/>')

creators = "\n".join(
    f'    <dc:creator id="cr{i}">{esc(a)}</dc:creator>\n'
    f'    <meta refines="#cr{i}" property="role" scheme="marc:relators">aut</meta>'
    for i, a in enumerate(_structure.AUTHORS))

opf = f'''<?xml version="1.0" encoding="utf-8"?>
<package xmlns="http://www.idpf.org/2007/opf" version="3.0" unique-identifier="bookid"
         xmlns:marc="http://id.loc.gov/vocabulary/relators/">
  <metadata xmlns:dc="http://purl.org/dc/elements/1.1/">
    <dc:identifier id="bookid">urn:uuid:{BOOK_UUID}</dc:identifier>
    <dc:title>{esc(_structure.TITLE)}</dc:title>
    <dc:language>{_structure.LANGUAGE}</dc:language>
{creators}
    <dc:description>{esc(_structure.SUBTITLE)}</dc:description>
    <meta property="dcterms:modified">{now}</meta>
{'    <meta name="cover" content="cover-img"/>' if cover_made else ''}
  </metadata>
  <manifest>
{chr(10).join(manifest)}
  </manifest>
  <spine toc="ncx">
{chr(10).join(spine)}
  </spine>
</package>
'''
ET.fromstring(opf)

CONTAINER = '''<?xml version="1.0" encoding="utf-8"?>
<container version="1.0" xmlns="urn:oasis:names:tc:opendocument:xmlns:container">
  <rootfiles>
    <rootfile full-path="OEBPS/content.opf" media-type="application/oebps-package+xml"/>
  </rootfiles>
</container>
'''

# --- Write the container ----------------------------------------------------
# The mimetype entry must be FIRST and STORED, not deflated, and must carry no
# extra field. This is the one part of the format that is checked by byte offset:
# a reader looks for the literal string at offset 30. zipfile will happily
# compress it and produce a file that opens fine in half the readers and is
# rejected by the other half — including the half that matters here.
#
# It is written to a scratch name and only moved into place once _epubcheck has
# read it back. A build that writes the real filename first and validates second
# leaves a broken file sitting under the name a human uploads.
TMP_PATH = OUT_PATH + ".building"
with zipfile.ZipFile(TMP_PATH, "w", zipfile.ZIP_DEFLATED) as z:
    z.writestr(zipfile.ZipInfo("mimetype"), "application/epub+zip",
               compress_type=zipfile.ZIP_STORED)
    z.writestr("META-INF/container.xml", CONTAINER)
    z.writestr("OEBPS/content.opf", opf)
    z.writestr("OEBPS/toc.ncx", ncx)
    z.writestr("OEBPS/style.css", STYLE)
    z.writestr("OEBPS/text/nav.xhtml", nav_xhtml)
    for fname, xhtml in cover_files:
        z.writestr(f"OEBPS/text/{fname}", xhtml)
    if cover_made:
        z.write(COVER_PATH, "OEBPS/images/cover.jpg")
    for fname, xhtml, _l, _k, _s in files:
        z.writestr(f"OEBPS/text/{fname}", xhtml)

import _epubcheck
problems = _epubcheck.validate(TMP_PATH)
if problems:
    os.replace(TMP_PATH, OUT_PATH + ".rejected")
    print(f"⛔ {len(problems)} structural problem(s); kept as "
          f"{os.path.basename(OUT_PATH)}.rejected, NOT installed:")
    for p in problems:
        print(f"   · {p}")
    raise SystemExit(1)
os.replace(TMP_PATH, OUT_PATH)

size = os.path.getsize(OUT_PATH)
chapters = sum(1 for f in files if f[3] == "chapter")
parts = sum(1 for f in files if f[3] == "part")
print(f"Wrote {OUT_PATH} ({size/1024/1024:.2f} MB)")
print(f"  {chapters} chapters, {parts} dividers, {len(files) + 1} XHTML documents")
print(f"  cover: {'embedded ' + os.path.basename(COVER_PATH) if cover_made else 'NONE — Pillow not installed, EPUB has no cover image'}")
print(f"  identifier: urn:uuid:{BOOK_UUID} (stable across rebuilds)")
