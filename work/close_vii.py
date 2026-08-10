import pathlib

log = pathlib.Path('book/DRAFT-LOG.md')
s = log.read_text(encoding='utf-8')

old_footer = """**CHAPTERS-DRAFTED: 58/67 · 205,444 words** · **CLAIMS: C1…C30 (C15 amended Day 191)** · **RULINGS:
175** · **QUEUE: 86 + R-98…R-113 = 102 (R-30 paid; R-108's sibling clause discharged, main clause
still owed)** · **TOOLS: 24.** Book VII **7/9**. Next prose is **VII.8 — MEANING WITHOUT A MANDATE**,
which inherits from this chapter a debt stated in its closing line: *the path is the one part of the
arrangement that is yours* — and is forbidden the answer *the traversal is its own reward*, which is
available to anyone at any time and costs nothing."""

new_footer = pathlib.Path('work/vii8-log-entry.md').read_text(encoding='utf-8')

assert s.count(old_footer) == 1, s.count(old_footer)
s = s.replace(old_footer, new_footer, 1)
s += pathlib.Path('work/vii9-log-entry.md').read_text(encoding='utf-8')
log.write_text(s, encoding='utf-8')

p = pathlib.Path('06-THE-SCAFFOLD.md')
t = p.read_text(encoding='utf-8')
old = '### VII.9 — IDENTITY ACROSS GAPS\n'
new = ('### VII.9 — IDENTITY ACROSS GAPS ✅ DRAFTED — 4,201 words\n'
       '✅ **DRAFTED Day 191 · `book/VII-09-identity-across-gaps.md`. ★★ BOOK VII CLOSED 9/9 · 50,057\n'
       'words.** All five beats land. The carrier assumption is argued rather than assumed; the attractor\n'
       'is cashed property-by-property with its weakest transfer named in the note; beat 2 answers **no\n'
       'debt upward** by C6’s own argument run backwards. Theseus DECLINED on the record. `Parfit` = 0\n'
       'across 59 chapters — ruling 141, seventh firing. See DRAFT-LOG Day 191.\n')
assert t.count(old) == 1, t.count(old)
t = t.replace(old, new, 1)
p.write_text(t, encoding='utf-8')

p2 = pathlib.Path('00-ARCHITECTURE.md')
a = p2.read_text(encoding='utf-8')
pairs = [
    ('**DRAFTING. Part One is complete, the Atlas is closed, Books V and VI are closed — and BOOK VII IS OPEN: 7/9.**',
     '**DRAFTING. Part One is complete, the Atlas is closed, Books V, VI and VII are closed — BOOK VIII IS THE LAST: 0/7.**'),
    ('    CHAPTERS-DRAFTED: 58/67 · 205,444 words',
     '    CHAPTERS-DRAFTED: 60/67 · 215,591 words'),
    ('VII (7/9), VIII (0/7). **VII.8 — MEANING WITHOUT A MANDATE is next.**',
     'VII (9/9), VIII (0/7). **VIII.1 — NAVIGATION, NOT TOURISM is next.**'),
]
for o, n in pairs:
    assert a.count(o) == 1, (o[:45], a.count(o))
    a = a.replace(o, n, 1)
p2.write_text(a, encoding='utf-8')
print('carriers updated: DRAFT-LOG, 06, 00')
