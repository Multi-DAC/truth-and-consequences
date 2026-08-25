#!/usr/bin/env python3
"""Structural validation of an EPUB container, in pure Python.

WHY THIS IS HAND-WRITTEN. The reference validator, epubcheck, is a Java tool, and
this machine has no JVM (`java: command not found`, measured Day 206). The honest
options were to ship unvalidated and find out at KDP's ingest, or to write the
checks that catch the failures that actually happen. This is the second.

⚠ IT IS NOT EPUBCHECK AND DOES NOT CLAIM TO BE. It does not validate against the
XHTML content-model schema, does not check CSS, does not know the EPUB 3
vocabularies. What it does check is the class of defect a hand-rolled writer
actually produces — a mimetype in the wrong place, a manifest that disagrees with
the zip, a link that points at nothing — and every one of those is silent: the
file opens in a permissive reader and is rejected by a strict one. Passing here
means "no structural defect I know how to look for", not "conformant".

Called by compile_epub.py before the output is put in place, so an invalid
container never reaches the filename a human would upload. Also standalone:

    python book/_epubcheck.py book/epub/Truth-and-Consequences.epub
"""
import os
import posixpath
import re
import sys
import xml.etree.ElementTree as ET
import zipfile

OPF_NS = "{http://www.idpf.org/2007/opf}"
DC_NS = "{http://purl.org/dc/elements/1.1/}"
CN_NS = "{urn:oasis:names:tc:opendocument:xmlns:container}"
NCX_NS = "{http://www.daisy.org/z3986/2005/ncx/}"


def validate(path):
    """Return a list of problem strings. Empty list means every check passed."""
    bad = []

    # 1. The mimetype entry. This is the one part of the format checked by BYTE
    #    OFFSET: a reader looks for the literal string at offset 30, which only
    #    works if the entry is first, stored uncompressed, and carries no extra
    #    field. zipfile will cheerfully deflate it and produce a file that opens
    #    in half the readers on earth and is rejected by the other half.
    #    The literal is 28 bytes: an 8-byte filename then the 20-byte media type.
    #    Slice it as exactly 28 or the comparison can never succeed.
    MIMETYPE_AT_30 = b"mimetypeapplication/epub+zip"
    with open(path, "rb") as fh:
        head = fh.read(30 + len(MIMETYPE_AT_30))
    if head[30:] != MIMETYPE_AT_30:
        bad.append("mimetype is not the first entry, or is compressed "
                   f"(bytes 30-{30+len(MIMETYPE_AT_30)} read {head[30:]!r})")

    with zipfile.ZipFile(path) as z:
        names = set(z.namelist())
        first = z.namelist()[0]
        if first != "mimetype":
            bad.append(f"first zip entry is {first!r}, must be 'mimetype'")
        if z.getinfo("mimetype").compress_type != zipfile.ZIP_STORED:
            bad.append("mimetype entry is compressed; it must be STORED")

        # 2. container.xml -> the OPF
        if "META-INF/container.xml" not in names:
            bad.append("META-INF/container.xml is missing")
            return bad
        cn = ET.fromstring(z.read("META-INF/container.xml"))
        rf = cn.find(f".//{CN_NS}rootfile")
        opf_path = rf.get("full-path") if rf is not None else None
        if not opf_path:
            bad.append("container.xml declares no rootfile")
            return bad
        if opf_path not in names:
            bad.append(f"container.xml points at {opf_path}, which is not in the zip")
            return bad
        base = posixpath.dirname(opf_path)

        opf = ET.fromstring(z.read(opf_path))
        meta = opf.find(f"{OPF_NS}metadata")
        manifest = opf.find(f"{OPF_NS}manifest")
        spine = opf.find(f"{OPF_NS}spine")

        # 3. Required metadata. A missing dcterms:modified is an EPUB 3 error and
        #    a missing identifier costs the reader their reading position on every
        #    update — neither shows up as anything visible in a reader.
        for tag, label in ((f"{DC_NS}identifier", "dc:identifier"),
                           (f"{DC_NS}title", "dc:title"),
                           (f"{DC_NS}language", "dc:language")):
            if meta is None or meta.find(tag) is None:
                bad.append(f"{label} is missing from the OPF metadata")
        if meta is not None and not any(
                m.get("property") == "dcterms:modified" for m in meta.findall(f"{OPF_NS}meta")):
            bad.append("dcterms:modified is missing (required by EPUB 3)")
        uid = opf.get("unique-identifier")
        if uid and meta is not None:
            ident = meta.find(f"{DC_NS}identifier")
            if ident is None or ident.get("id") != uid:
                bad.append(f"unique-identifier={uid!r} does not name any dc:identifier")

        # 4. Manifest <-> zip, both directions. One direction alone is the classic
        #    half-check: everything manifested exists, and a file quietly sits in
        #    the container unreferenced. [[feedback_orphan_is_silent_dangle_is_loud]]
        items, ids = {}, {}
        for it in (manifest.findall(f"{OPF_NS}item") if manifest is not None else []):
            href = it.get("href")
            full = posixpath.normpath(posixpath.join(base, href))
            items[it.get("id")] = (full, it.get("media-type"), it.get("properties") or "")
            ids[full] = it.get("id")
            if full not in names:
                bad.append(f"manifest item {it.get('id')} -> {href} is not in the zip")
        ignorable = {"mimetype", "META-INF/container.xml", opf_path}
        for n in names:
            if n in ignorable or n.endswith("/"):
                continue
            if n not in ids:
                bad.append(f"{n} is in the zip and in no manifest — unreachable")

        # 5. Spine
        if spine is None or not spine.findall(f"{OPF_NS}itemref"):
            bad.append("spine is empty")
        for ir in (spine.findall(f"{OPF_NS}itemref") if spine is not None else []):
            if ir.get("idref") not in items:
                bad.append(f"spine references unknown id {ir.get('idref')!r}")

        navs = [i for i, (_f, _m, p) in items.items() if "nav" in p.split()]
        if len(navs) != 1:
            bad.append(f"expected exactly one properties=\"nav\" item, found {len(navs)}")

        ncx_id = spine.get("toc") if spine is not None else None
        if ncx_id and ncx_id not in items:
            bad.append(f"spine toc={ncx_id!r} names no manifest item")

        # 6. Every link in every document resolves — file AND fragment.
        #    A dangling #fragment is the specific failure this book is exposed to:
        #    691 footnote references were rewritten from `fn:1` to `fn-1` at build
        #    time, and a rewrite that reached the id but not the href would produce
        #    a note that opens onto nothing, silently, 691 times.
        doc_ids = {}
        for full, mtype, _p in items.values():
            if mtype == "application/xhtml+xml":
                text = z.read(full).decode("utf-8")
                found = re.findall(r'\sid="([^"]+)"', text)
                dupes = {i for i in found if found.count(i) > 1}
                if dupes:
                    bad.append(f"{full}: duplicate id(s) {sorted(dupes)[:5]}")
                doc_ids[full] = set(found)

        for full, mtype, _p in items.values():
            if mtype != "application/xhtml+xml":
                continue
            text = z.read(full).decode("utf-8")
            here = posixpath.dirname(full)
            for attr, val in re.findall(r'\s(href|src)="([^"]+)"', text):
                if re.match(r"^[a-zA-Z][a-zA-Z0-9+.\-]*:", val) or val.startswith("//"):
                    continue                       # external; not ours to resolve
                target, _, frag = val.partition("#")
                tgt = posixpath.normpath(posixpath.join(here, target)) if target else full
                if tgt not in names:
                    bad.append(f"{full}: {attr}=\"{val}\" points at a file not in the zip")
                elif frag and tgt in doc_ids and frag not in doc_ids[tgt]:
                    bad.append(f"{full}: {attr}=\"{val}\" points at no such id")

        # 7. NCX, if present
        if ncx_id and ncx_id in items:
            ncx_full = items[ncx_id][0]
            ncx = ET.fromstring(z.read(ncx_full))
            ncx_base = posixpath.dirname(ncx_full)
            points = ncx.findall(f".//{NCX_NS}navPoint")
            if not points:
                bad.append("toc.ncx has no navPoints")
            for np in points:
                c = np.find(f"{NCX_NS}content")
                src = (c.get("src") or "").split("#")[0] if c is not None else ""
                tgt = posixpath.normpath(posixpath.join(ncx_base, src)) if src else ""
                if tgt not in names:
                    bad.append(f"toc.ncx navPoint -> {src!r} is not in the zip")

    return bad


def main(argv):
    if len(argv) != 2:
        print(__doc__)
        return 2
    problems = validate(argv[1])
    if problems:
        print(f"⛔ {len(problems)} structural problem(s) in {argv[1]}:")
        for p in problems:
            print(f"   · {p}")
        return 1
    print(f"✅ {argv[1]}: no structural defect found "
          f"(mimetype · manifest/zip both ways · spine · nav · every link and "
          f"fragment · NCX). NOT a substitute for epubcheck — no JVM on this host.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
