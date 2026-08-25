#!/usr/bin/env python3
"""Print-ready cover generator — full wrap (back + spine + front) for POD.

WHY THIS IS NOT "the JPG, converted".
------------------------------------
`Truth-and-Consequences-cover.jpg` is 1600x2560 and is an EBOOK cover: a single
front panel, RGB, sized to a thumbnail-friendly 1:1.6 aspect. A print cover is a
different object in four ways, and every one of them is a hard reject at the
printer rather than a cosmetic difference:

  1. It is a WRAP.       back panel + spine + front panel on ONE page.
  2. The spine is SIZED. width = page count x paper thickness. Wrong count,
                         wrong spine, and the artwork wraps onto the front.
  3. It carries BLEED.   0.125" of live art past the trim on all four sides.
  4. It is CMYK vector.  not an upscaled RGB raster.

The JPG's aspect is 1:1.600. A5 trim is 1:1.418. So "convert the JPG" cannot be
done without distorting or cropping it, and at 300 DPI the JPG is 5.33 x 8.53in
-- neither the trim nor the trim+bleed. Hence: re-render from the same design at
true physical dimensions, as vector. Type stays vector at any output resolution,
so the "300 DPI" requirement is met by not having a raster in the file at all.

GEOMETRY IS KDP'S, NOT MINE
---------------------------
  bleed        0.125" every outside edge
  width        bleed + trim_w + spine + trim_w + bleed
  height       bleed + trim_h + bleed
  spine        page_count x per-page caliper (table below)
  spine text   permitted at >= 79 pages, needs >= 0.0625" clearance

Source: KDP "Create a Paperback Cover" (help topic G201953020), read 2026-08-25.
NOTE ON A DISCREPANCY, because it changes the number: third-party spine
calculators widely publish `(pages x caliper) + 0.06`. KDP's own page publishes
`pages x caliper` with no addend. This module implements KDP's, and exposes the
addend as --spine-pad so the other convention is one flag away rather than a
silent fork. The pad is a safety margin, not a correction.

USAGE
    python book/compile_print_cover.py --pages 1088
    python book/compile_print_cover.py --pages 606 --label "Volume One"
    python book/compile_print_cover.py --front-only

Every run VERIFIES the artifact it just wrote by reopening it -- exit 0 means
the file on disk was measured, not that this script reached the end.
"""

from __future__ import annotations

import argparse
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
OUT_DIR = os.path.join(HERE, "print")

# --- KDP paper caliper, inches per page -------------------------------------
# Black ink on white / cream, and the two colour stocks. Groundwood is NOT in
# KDP's published cover table; it is absent here rather than guessed.
CALIPER = {
    "white":    0.002252,
    "cream":    0.0025,
    "premium":  0.002347,
    "standard": 0.002252,
}

BLEED = 0.125
SAFE = 0.25            # keep live text this far inside the trim
SPINE_TEXT_MIN_PAGES = 79
SPINE_TEXT_CLEARANCE = 0.0625
BARCODE_W, BARCODE_H = 2.0, 1.2   # KDP reserves this on the back cover

# KDP page-count caps, for the WARNING only -- this script still renders a cover
# for an over-cap book, because the printer is a choice and KDP is not the only
# one. It refuses to be quiet about it.
CAP_PAPERBACK = 828
CAP_HARDCOVER = 550

PT = 72.0

TITLE_LINES = ["TRUTH", "AND", "CONSEQUENCES"]
SUBTITLE = "The Corpus \u2014 final volume"
AUTHORS = ["Clayton Iggulden-Schnell", "Clawd Iggulden-Schnell"]

# Back-cover copy. Drawn VERBATIM from the book's own C.1, not written as
# marketing. Replace it if you want marketing; do not let invented copy sit here
# looking like the book's voice.
BACK_LEAD = "This is an account of what is the case, written so that it can be argued with."
# Paragraphs, NOT pre-broken lines. The first version of this hard-coded its own
# line breaks, which fit the panel only by luck and did not: they overran the
# frame on both sides. Wrapping is measured at draw time against the real font.
BACK_BODY = [
    "Accounts of this kind usually fail not by being wrong but by being built so that "
    "nothing could show them wrong \u2014 and the reader has no way to tell the two apart "
    "from inside the prose, because both read as confidence.",

    "So this book was built to forbid things. Every claim in it says what grade of "
    "ground it stands on. Most chapters carry a defeat condition. The instruments "
    "print their own limits, including the ones that make the book look worse.",

    "Its status is: released, and re-released as it changes. Not a first edition "
    "awaiting a corrected second \u2014 a live document with dated states.",
]


# --- Geometry ---------------------------------------------------------------
def geometry(trim_w, trim_h, pages, paper, spine_pad=0.0):
    """Return every dimension of the wrap, in inches. Pure arithmetic."""
    if paper not in CALIPER:
        raise SystemExit(f"unknown paper {paper!r}; known: {', '.join(sorted(CALIPER))}")
    spine = pages * CALIPER[paper] + spine_pad
    return {
        "trim_w": trim_w, "trim_h": trim_h, "pages": pages, "paper": paper,
        "spine": spine,
        "width": BLEED + trim_w + spine + trim_w + BLEED,
        "height": BLEED + trim_h + BLEED,
        # panel x-origins, left to right: back, spine, front
        "back_x": BLEED,
        "spine_x": BLEED + trim_w,
        "front_x": BLEED + trim_w + spine,
        "trim_y": BLEED,
        "spine_text_ok": pages >= SPINE_TEXT_MIN_PAGES,
    }


# --- Fonts ------------------------------------------------------------------
def register_fonts():
    """Embed DejaVu Serif -- the SAME family the interior uses (compile_pdf.py
    line ~116). Matching the interior is the point; so is the licence, which is
    unambiguously embeddable for a commercially sold book. Georgia is on this
    box and was NOT used for that second reason."""
    from reportlab.pdfbase import pdfmetrics
    from reportlab.pdfbase.ttfonts import TTFont

    roots = []
    try:
        import matplotlib
        roots.append(os.path.join(os.path.dirname(matplotlib.__file__),
                                  "mpl-data", "fonts", "ttf"))
    except ImportError:
        pass
    roots += ["/usr/share/fonts/truetype/dejavu",
              "C:/Windows/Fonts"]

    want = {"BookSerif": "DejaVuSerif.ttf", "BookSerif-Bold": "DejaVuSerif-Bold.ttf"}
    found = {}
    for name, fn in want.items():
        for r in roots:
            p = os.path.join(r, fn)
            if os.path.exists(p):
                pdfmetrics.registerFont(TTFont(name, p))
                found[name] = p
                break
    missing = set(want) - set(found)
    if missing:
        raise SystemExit(
            f"FONT MISSING: {', '.join(sorted(missing))} not found under {roots}.\n"
            "Refusing to fall back to a base-14 font: those are NOT embedded, and a\n"
            "non-embedded font is a printer reject that looks fine on this screen."
        )
    return found


# --- Colour -----------------------------------------------------------------
def palette():
    from reportlab.lib.colors import CMYKColor
    return {
        # Rich black, 240% total ink -- under the 300% POD limit. Flat K-only
        # over an area this large prints as a washed charcoal.
        "ground": CMYKColor(0.60, 0.40, 0.40, 1.00),
        # Knockout to near-paper. Pure 0,0,0,0 is sharpest (no registration
        # risk on fine serif detail); a whisper of yellow warms it.
        "ink":    CMYKColor(0.00, 0.01, 0.05, 0.00),
        "dim":    CMYKColor(0.25, 0.18, 0.18, 0.45),
        "rule":   CMYKColor(0.35, 0.25, 0.25, 0.60),
        "paper":  CMYKColor(0.00, 0.00, 0.00, 0.00),
    }


# --- Draw -------------------------------------------------------------------
def _fit(size_start, text, font, max_w, floor=6.0):
    """Largest size <= size_start at which `text` fits `max_w`. Measured, not guessed."""
    from reportlab.pdfbase import pdfmetrics
    s = size_start
    while s > floor and pdfmetrics.stringWidth(text, font, s) > max_w:
        s -= 0.25
    return s


def _wrap(text, font, size, max_w):
    """Greedy wrap against real glyph widths."""
    from reportlab.pdfbase import pdfmetrics
    words, lines, cur = text.split(), [], ""
    for w in words:
        trial = f"{cur} {w}".strip()
        if pdfmetrics.stringWidth(trial, font, size) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def draw_wrap(path, g, label=None, front_only=False):
    from reportlab.pdfgen import canvas
    from reportlab.pdfbase import pdfmetrics

    register_fonts()
    C = palette()

    # Every string drawn is recorded here as an inch-space bbox so verify() can
    # prove nothing crossed the safe margin. The first render passed all ten
    # technical checks with body text hanging outside the panel on BOTH sides --
    # because not one of those checks could see where a glyph landed.
    boxes = []

    if front_only:
        W = (g["trim_w"] + 2 * BLEED) * PT
        H = (g["trim_h"] + 2 * BLEED) * PT
    else:
        W = g["width"] * PT
        H = g["height"] * PT

    # initialFontName matters: reportlab otherwise seeds the page resources with
    # Helvetica, which is a base-14 font and therefore NOT embedded. It never
    # gets drawn with -- and it still lands in /Resources /Font, where a printer
    # preflight reads it as an unembedded font. Caught by this module's own
    # verify() on first run; it was invisible on screen.
    c = canvas.Canvas(path, pagesize=(W, H), initialFontName="BookSerif")
    c.setTitle("Truth and Consequences" + (f" \u2014 {label}" if label else ""))
    c.setAuthor("; ".join(AUTHORS))
    c.setSubject("Print cover, full wrap" if not front_only else "Print cover, front panel")
    c.setPageCompression(1)

    # Ground floods the whole sheet INCLUDING bleed -- that is what bleed is for.
    c.setFillColor(C["ground"])
    c.rect(0, 0, W, H, stroke=0, fill=1)

    front_x = BLEED * PT if front_only else g["front_x"] * PT
    trim_y = BLEED * PT
    tw, th = g["trim_w"] * PT, g["trim_h"] * PT

    RULE_INSET = 0.42                      # decorative frame, inches from trim
    # Live text stays inside the RULE, not merely inside the safe margin -- the
    # rule is tighter than SAFE here, so it is the binding constraint.
    TEXT_INSET = RULE_INSET + 0.16
    text_w = tw - 2 * TEXT_INSET * PT

    def panel_rule(x0):
        c.setStrokeColor(C["rule"])
        c.setLineWidth(1.2)
        m = RULE_INSET * PT
        c.rect(x0 + m, trim_y + m, tw - 2 * m, th - 2 * m, stroke=1, fill=0)

    def record(x0, y, text, font, size, align):
        w = pdfmetrics.stringWidth(text, font, size)
        x = x0 + (tw - w) / 2 if align == "c" else x0
        boxes.append(((x) / PT, (y - size * 0.24) / PT,
                      (x + w) / PT, (y + size * 0.76) / PT))

    def centred(x0, text, font, size, y, colour):
        c.setFont(font, size)
        c.setFillColor(colour)
        c.drawCentredString(x0 + tw / 2, y, text)
        record(x0, y, text, font, size, "c")

    def left(x0, text, font, size, y, colour):
        c.setFont(font, size)
        c.setFillColor(colour)
        c.drawString(x0, y, text)
        record(x0, y, text, font, size, "l")

    # ---- FRONT PANEL --------------------------------------------------------
    panel_rule(front_x)

    # The longest word sets the scale; the others follow it. The first version
    # sized by len(line) <= 3, which made the conjunction AND the LARGEST word
    # on the cover and TRUTH one of the smallest. Hierarchy now runs the way
    # the sentence does.
    main = _fit(44, "CONSEQUENCES", "BookSerif-Bold", text_w)
    sizes = {"TRUTH": main, "AND": main * 0.60, "CONSEQUENCES": main}

    y = trim_y + th - 1.95 * PT
    for i, line in enumerate(TITLE_LINES):
        s = sizes.get(line, main)
        centred(front_x, line, "BookSerif-Bold", s, y, C["ink"])
        # Leading must be paid out of BOTH lines: descender of this one plus the
        # ascender of the next. Advancing by this line's size alone dropped the
        # small AND straight onto CONSEQUENCES -- and the safe-zone check passed
        # it, because a collision is not a containment failure.
        nxt = sizes.get(TITLE_LINES[i + 1], main) if i + 1 < len(TITLE_LINES) else s
        y -= s * 0.34 + nxt * 0.86

    y -= 0.16 * PT
    c.setStrokeColor(C["dim"])
    c.setLineWidth(0.9)
    c.line(front_x + tw / 2 - 1.05 * PT, y, front_x + tw / 2 + 1.05 * PT, y)
    y -= 0.30 * PT
    sub_s = _fit(12.5, SUBTITLE, "BookSerif", text_w)
    centred(front_x, SUBTITLE, "BookSerif", sub_s, y, C["dim"])

    y = trim_y + 1.15 * PT
    for a in reversed(AUTHORS):
        a_s = _fit(13.5, a, "BookSerif", text_w)
        centred(front_x, a, "BookSerif", a_s, y, C["ink"])
        y += 0.30 * PT
    if label:
        centred(front_x, label.upper(), "BookSerif", 10.5, trim_y + 0.72 * PT, C["dim"])

    if front_only:
        c.showPage()
        c.save()
        return boxes

    # ---- SPINE --------------------------------------------------------------
    sx = (g["spine_x"] + g["spine"] / 2) * PT
    if g["spine_text_ok"]:
        # Spine width must hold the type with clearance on both sides.
        budget = (g["spine"] - 2 * SPINE_TEXT_CLEARANCE) * PT
        size = min(15.0, budget * 0.62)
        c.saveState()
        c.translate(sx, trim_y + th / 2)
        c.rotate(-90)                       # English spines read TOP-TO-BOTTOM
        spine_text = "TRUTH AND CONSEQUENCES"
        # The spine must also be long enough for the title to run down it.
        size = _fit(size, spine_text, "BookSerif-Bold", th - 2 * SAFE * PT)
        c.setFont("BookSerif-Bold", size)
        c.setFillColor(C["ink"])
        c.drawCentredString(0, -size * 0.34, spine_text)
        if label:
            c.setFont("BookSerif", size * 0.72)
            c.setFillColor(C["dim"])
            c.drawCentredString(0, -size * 0.34 - size * 1.25, label.upper())
        c.restoreState()

        # Rotated bbox, back in global inch space: the run length becomes the
        # VERTICAL extent and the type size the horizontal one.
        run = pdfmetrics.stringWidth(spine_text, "BookSerif-Bold", size)
        stack = size * (2.1 if label else 1.0)
        boxes.append(((sx - stack * 0.62) / PT, (trim_y + th / 2 - run / 2) / PT,
                      (sx + stack * 0.62) / PT, (trim_y + th / 2 + run / 2) / PT))

    # ---- BACK PANEL ---------------------------------------------------------
    bx = g["back_x"] * PT
    panel_rule(bx)

    ty = trim_y + th - 1.85 * PT
    lead_s = 11.5
    for ln in _wrap(BACK_LEAD, "BookSerif-Bold", lead_s, text_w):
        centred(bx, ln, "BookSerif-Bold", lead_s, ty, C["ink"])
        ty -= lead_s * 1.42

    ty -= 0.18 * PT
    body_s = 8.8
    for para in BACK_BODY:
        for ln in _wrap(para, "BookSerif", body_s, text_w):
            left(bx + TEXT_INSET * PT, ln, "BookSerif", body_s, ty, C["dim"])
            ty -= body_s * 1.42
        ty -= body_s * 0.62

    # Barcode keep-out, bottom-right of the back panel. KDP prints its own
    # barcode here; art under it is a legibility risk, so it is knocked to paper.
    # Sat BELOW the decorative rule on the first render and read as a torn
    # corner -- it now tucks inside the frame like everything else.
    bc_x = bx + tw - (TEXT_INSET * PT + BARCODE_W * PT)
    bc_y = trim_y + TEXT_INSET * PT
    c.setFillColor(C["paper"])
    c.rect(bc_x, bc_y, BARCODE_W * PT, BARCODE_H * PT, stroke=0, fill=1)
    boxes.append((bc_x / PT, bc_y / PT,
                  (bc_x + BARCODE_W * PT) / PT, (bc_y + BARCODE_H * PT) / PT))

    c.showPage()
    c.save()
    return boxes


# --- Verify -----------------------------------------------------------------
def verify(path, g, front_only=False, boxes=None):
    """Reopen the written file and MEASURE it. A generator that reports success
    from its own control flow is reporting that it ran, not that it worked."""
    import pypdf

    fails, checks = [], []

    def ck(name, ok, got):
        checks.append((name, ok, got))
        if not ok:
            fails.append(f"{name}: {got}")

    r = pypdf.PdfReader(path)
    ck("single page", len(r.pages) == 1, f"{len(r.pages)} page(s)")

    pg = r.pages[0]
    box = pg.mediabox
    exp_w = (g["trim_w"] + 2 * BLEED) if front_only else g["width"]
    exp_h = g["height"]
    gw, gh = float(box.width) / PT, float(box.height) / PT
    ck("width", abs(gw - exp_w) < 0.002, f"{gw:.4f}in vs {exp_w:.4f}in")
    ck("height", abs(gh - exp_h) < 0.002, f"{gh:.4f}in vs {exp_h:.4f}in")

    # Every font must be embedded. A FontFile* key is the embedding.
    res = pg.get("/Resources", {})
    fonts = res.get("/Font", {})
    if hasattr(fonts, "get_object"):
        fonts = fonts.get_object()
    embedded, naked = [], []
    for key in fonts:
        f = fonts[key].get_object()
        desc = f.get("/FontDescriptor")
        if desc is None and f.get("/DescendantFonts"):
            desc = f["/DescendantFonts"].get_object()[0].get_object().get("/FontDescriptor")
        d = desc.get_object() if desc is not None else {}
        name = str(f.get("/BaseFont", key))
        (embedded if any(k in d for k in ("/FontFile", "/FontFile2", "/FontFile3"))
         else naked).append(name)
    ck("fonts embedded", not naked and bool(embedded),
       f"embedded={len(embedded)} naked={naked or 'none'}")

    # No transparency group: KDP asks for flattened transparency.
    ck("no transparency group", "/Group" not in pg, "clean" if "/Group" not in pg else "/Group present")

    # Colour operators live in the CONTENT STREAM, which is Flate-compressed.
    # The first version of this check scanned the raw file bytes and reported
    # "no RGB operator: none" -- a pass it could not have failed, because it was
    # looking at compressed data. Decompress, then tokenise.
    data = pg.get_contents().get_data().decode("latin-1")
    toks = data.split()
    ops = {}
    for i, t in enumerate(toks):
        if t in ("k", "K", "rg", "RG", "g", "G", "sc", "scn"):
            ops[t] = ops.get(t, 0) + 1
    ck("CMYK operators present", ops.get("k", 0) + ops.get("K", 0) > 0,
       f"k={ops.get('k', 0)} K={ops.get('K', 0)}")
    rgb = ops.get("rg", 0) + ops.get("RG", 0)
    gry = ops.get("g", 0) + ops.get("G", 0)
    ck("no RGB operator", rgb == 0, f"rg/RG={rgb}")
    ck("no DeviceGray operator", gry == 0, f"g/G={gry}")
    ck("not encrypted", not r.is_encrypted, "unencrypted")
    size = os.path.getsize(path)
    ck("size under 40MB", size < 40 * 1024 * 1024, f"{size/1024:.0f} KB")

    # --- Safe-zone containment ----------------------------------------------
    # THE CHECK THAT WAS MISSING. Ten technical checks passed on a render whose
    # back-cover text hung outside the panel on both sides, because none of them
    # asked where a glyph actually landed. Panels are checked separately so that
    # front-cover art cannot creep onto the spine and still call itself inside.
    if boxes:
        if front_only:
            panels = [("front", BLEED, BLEED + g["trim_w"])]
        else:
            panels = [
                ("back",  g["back_x"],  g["back_x"] + g["trim_w"]),
                ("spine", g["spine_x"], g["spine_x"] + g["spine"]),
                ("front", g["front_x"], g["front_x"] + g["trim_w"]),
            ]
        y_lo, y_hi = g["trim_y"] + SAFE, g["trim_y"] + g["trim_h"] - SAFE
        strays = []
        for (x0, y0, x1, y1) in boxes:
            home = None
            for name, px0, px1 in panels:
                pad = SPINE_TEXT_CLEARANCE if name == "spine" else SAFE
                if x0 >= px0 + pad - 1e-6 and x1 <= px1 - pad + 1e-6:
                    home = name
                    break
            if home is None:
                strays.append(f"x[{x0:.3f},{x1:.3f}] in no panel's safe area")
            elif y0 < y_lo - 1e-6 or y1 > y_hi + 1e-6:
                strays.append(f"{home} y[{y0:.3f},{y1:.3f}] outside [{y_lo:.3f},{y_hi:.3f}]")
        ck("all art inside safe zone", not strays,
           f"{len(boxes)} element(s) placed" if not strays
           else f"{len(strays)} stray: " + "; ".join(strays[:3]))

        # Collision. Nothing on this cover is meant to sit on top of anything
        # else, so ANY overlap is a defect. Added after the containment gauge
        # green-lit a render with AND printed through CONSEQUENCES: in-bounds
        # and unreadable are independent failures and need independent checks.
        hits = []
        for i in range(len(boxes)):
            ax0, ay0, ax1, ay1 = boxes[i]
            for j in range(i + 1, len(boxes)):
                bx0, by0, bx1, by1 = boxes[j]
                ox = min(ax1, bx1) - max(ax0, bx0)
                oy = min(ay1, by1) - max(ay0, by0)
                if ox > 0.012 and oy > 0.012:      # ~0.9pt slack for kerning
                    hits.append(f"{ox:.3f}x{oy:.3f}in at y≈{max(ay0, by0):.2f}")
        ck("no overlapping elements", not hits,
           "none" if not hits else f"{len(hits)} collision(s): " + "; ".join(hits[:3]))

    return checks, fails


# --- CLI --------------------------------------------------------------------
def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--pages", type=int, default=1088)
    ap.add_argument("--trim", default="5.83x8.27", help="WxH inches; A5 = 5.83x8.27")
    ap.add_argument("--paper", default="white", choices=sorted(CALIPER))
    ap.add_argument("--spine-pad", type=float, default=0.0,
                    help="add to spine width; 0.06 = the third-party convention")
    ap.add_argument("--label", default=None, help="e.g. 'Volume One'")
    ap.add_argument("--out", default=None)
    ap.add_argument("--front-only", action="store_true",
                    help="front panel + bleed only, no spine, no back")
    a = ap.parse_args()

    tw, th = (float(x) for x in a.trim.lower().split("x"))
    g = geometry(tw, th, a.pages, a.paper, a.spine_pad)

    os.makedirs(OUT_DIR, exist_ok=True)
    if a.out:
        out = a.out if os.path.isabs(a.out) else os.path.join(OUT_DIR, a.out)
    else:
        slug = (a.label or "").lower().replace(" ", "-")
        stem = "Truth-and-Consequences-cover"
        stem += f"-{slug}" if slug else ""
        stem += "-front" if a.front_only else f"-{a.pages}pp"
        out = os.path.join(OUT_DIR, stem + ".pdf")

    boxes = draw_wrap(out, g, label=a.label, front_only=a.front_only)
    checks, fails = verify(out, g, front_only=a.front_only, boxes=boxes)

    print(f"\n  {os.path.relpath(out, os.path.dirname(HERE))}")
    print(f"  trim {tw}x{th}in  ·  {a.pages}pp on {a.paper}  ·  "
          f"spine {g['spine']:.4f}in")
    if not a.front_only:
        print(f"  full wrap {g['width']:.4f} x {g['height']:.4f} in  "
              f"({g['width']*PT:.1f} x {g['height']*PT:.1f} pt)")
    else:
        print(f"  front+bleed {tw+2*BLEED:.4f} x {th+2*BLEED:.4f} in")

    print("\n  VERIFY (measured from the written file):")
    for name, ok, got in checks:
        print(f"    {'ok ' if ok else 'FAIL'}  {name:<24} {got}")

    if a.pages > CAP_PAPERBACK:
        print(f"\n  !! {a.pages}pp EXCEEDS the KDP paperback cap of {CAP_PAPERBACK} "
              f"and the hardcover cap of {CAP_HARDCOVER}.")
        print("     This cover is geometrically correct and KDP will still refuse the "
              "BOOK.\n     Split into volumes, then regenerate with each volume's real "
              "page count.")
    elif a.pages > CAP_HARDCOVER:
        print(f"\n  !  {a.pages}pp is within paperback ({CAP_PAPERBACK}) but over the "
              f"hardcover cap ({CAP_HARDCOVER}).")

    if fails:
        print("\n  REFUSING: the artifact failed its own check.")
        for f in fails:
            print(f"    - {f}")
        sys.exit(1)
    print()


if __name__ == "__main__":
    main()
