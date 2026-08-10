import os, re
ROOT = r"C:\Users\Wasch\Corpus-Perspectival"
NAMES = ["Mannheim","sociology of knowledge","Ideology and Utopia","free-floating",
         "freischwebende","relationism","situated knowledge","standpoint",
         "bias blind spot","Pronin","introspection illusion","Lee Ross",
         "reflexivity","self-refuting","self-refutation","tu quoque",
         "blind spot","my own bias","own blind spot","null space",
         "the tunnel you are in","filter stack","reality tunnel","Gebser",
         "Charles Taylor","immanent frame","disenchantment","episteme","Foucault",
         "Kuhn","paradigm","incommensurab","Barfield","Ong","McLuhan",
         "confirmation bias","naive realism","Geertz","Bourdieu","habitus",
         "the present","our era","this era","modernity"]
counts = {n:0 for n in NAMES}
files = 0
for dp, dn, fn in os.walk(ROOT):
    dn[:] = [d for d in dn if d not in ('.git','node_modules','__pycache__','.venv')]
    for f in fn:
        if not f.lower().endswith(('.md','.txt')): continue
        p = os.path.join(dp,f)
        try: t = open(p, encoding='utf-8', errors='ignore').read()
        except Exception: continue
        files += 1
        for n in NAMES:
            if re.search(re.escape(n), t, re.I): counts[n] += 1
print(f"scanned {files} files under {ROOT}")
for n in NAMES:
    print(f"  {counts[n]:5d}  {n}")
