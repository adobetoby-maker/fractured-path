#!/usr/bin/env python3
"""Lane A helper (read-only): list manuscript lines that carry protected wording.
A line is flagged when it shares a run of >= N tokens with BOOK_MAP section 10,
or matches a regex in protected-patterns.txt (on normalised tokens).
usage: protected_lines.py DIR [N]   -> prints 'chapter-XX.md:LINE<TAB>why<TAB>text'
"""
import re, sys
from pathlib import Path
TOK = re.compile(r"[a-z0-9]+(?:['’][a-z0-9]+)*")
def toks(t): return TOK.findall(t.lower().replace("’", "'"))
book = Path("editions/monroe-1.3/book-08-before-the-paths")
d = Path(sys.argv[1]); N = int(sys.argv[2]) if len(sys.argv) > 2 else 6
bm = book.joinpath("BOOK_MAP.md").read_text(encoding="utf-8").splitlines()
s = next(i for i, l in enumerate(bm) if l.startswith("## 10."))
e = next(i for i, l in enumerate(bm) if l.startswith("## 11."))
grams = set()
for l in bm[s:e]:
    t = toks(l)
    for i in range(len(t) - N + 1): grams.add(tuple(t[i:i+N]))
pats = [re.compile(l.strip()) for l in book.joinpath("protected-patterns.txt").read_text(encoding="utf-8").splitlines() if l.strip() and not l.startswith("#")]
for c in range(1, 31):
    p = d / f"chapter-{c:02d}.md"
    for n, line in enumerate(p.read_text(encoding="utf-8").splitlines(), 1):
        t = toks(line)
        if not t: continue
        why = []
        if any(tuple(t[i:i+N]) in grams for i in range(len(t) - N + 1)): why.append("map")
        norm = " ".join(t).replace("'", "'")
        if any(rx.search(norm) for rx in pats): why.append("pattern")
        if line.lstrip().startswith(("*", ">", "_")) : why.append("italic/doc")
        if why: print(f"{p.name}:{n}\t{'+'.join(why)}\t{line[:110]}")
