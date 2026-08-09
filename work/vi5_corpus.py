import os, re
ROOT = r"C:\Users\Wasch\Corpus-Perspectival"
NAMES = ["McLuhan","Marshall McLuhan","global village","Tim Wu","attention economy",
         "Herbert Simon","War of the Worlds","Orson Welles","Cantril","penny press",
         "broadcast","radio","television","Postman","Neil Postman","Amusing Ourselves",
         "Benedict Anderson","imagined communities","simultaneity","Innis","Harold Innis",
         "attention merchants","Debord","spectacle","Baudrillard","Carey","James Carey"]
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
