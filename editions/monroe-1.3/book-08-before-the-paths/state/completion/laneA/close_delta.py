#!/usr/bin/env python3
"""Lane A helper: same method as tools/skeleton_probe.py, but prints ONLY manuscript-side text.
For each chapter 1-30: counts (sentences, skeleton>=0.50, close>=0.35) for pre-lanes and for the manuscript,
and lists manuscript sentences that are newly at or over a threshold after the pass. No source text is printed."""
import re, sys, difflib, subprocess
from pathlib import Path
T = Path("editions/monroe-1.3/tools"); book = Path("editions/monroe-1.3/book-08-before-the-paths")
sys.path.insert(0, str(T))
import skeleton_probe as sp
MOV = {1: range(1, 7), 2: range(7, 13), 3: range(13, 20), 4: range(20, 27), 5: range(27, 31)}
def score(path, src, src_sets):
    out = {}
    for s, t in sp.sentences(path.read_text(encoding="utf-8").replace("\n---\n", "\n\n")):
        ts = set(t); best = 0.0
        for (sx, st), ss in zip(src, src_sets):
            if len(ts & ss) / len(ts | ss) < 0.15: continue
            r = difflib.SequenceMatcher(None, t, st, autojunk=False).ratio()
            if r > best: best = r
        out[s] = best
    return out
for m, chs in MOV.items():
    srcf = subprocess.run([sys.executable, str(T/"probe_sources.py"), str(book/f"packets/MOVEMENT-{m:03d}.md"), book.name], capture_output=True, text=True).stdout.split()
    src = []
    for f in srcf: src += sp.sentences(Path(f).read_text(encoding="utf-8"))
    src_sets = [set(t) for _, t in src]
    for c in chs:
        f = f"chapter-{c:02d}.md"
        a = score(book/"state/completion/pre-lanes"/f, src, src_sets); b = score(book/"manuscript"/f, src, src_sets)
        ca = (len(a), sum(v >= .5 for v in a.values()), sum(v >= .35 for v in a.values()))
        cb = (len(b), sum(v >= .5 for v in b.values()), sum(v >= .35 for v in b.values()))
        flag = "" if (cb[1] <= ca[1] and cb[2] <= ca[2]) else "  <-- RISE"
        print(f"{f}  before n/skel/close={ca}  after={cb}{flag}")
        for s, v in b.items():
            if v >= .35 and a.get(s, 0) < .35 and s not in a:
                print(f"     new>=0.35 ({v:.2f}): {s[:160]}")
