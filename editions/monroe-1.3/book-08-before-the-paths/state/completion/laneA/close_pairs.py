#!/usr/bin/env python3
"""Lane A helper: for every sentence changed by the pass, the probe ratio before -> after (manuscript text only; no source text printed)."""
import re, sys, difflib, subprocess
from pathlib import Path
T = Path("editions/monroe-1.3/tools"); book = Path("editions/monroe-1.3/book-08-before-the-paths")
sys.path.insert(0, str(T))
import skeleton_probe as sp
MOV = {1: range(1, 7), 2: range(7, 13), 3: range(13, 20), 4: range(20, 27), 5: range(27, 31)}
def best(t, src, src_sets):
    ts = set(t); b = 0.0
    for (sx, st), ss in zip(src, src_sets):
        if len(ts & ss) / len(ts | ss) < 0.15: continue
        r = difflib.SequenceMatcher(None, t, st, autojunk=False).ratio()
        if r > b: b = r
    return b
def sents(path):
    return [s for s, t in [(s, sp.toks(s)) for para in re.split(r"\n\s*\n", re.sub(r"^#.*$", "", path.read_text(encoding="utf-8"), flags=re.M)) for s in sp.SPLIT.split(" ".join(para.split())) if para.strip() and para.strip() != "---"]]
for m, chs in MOV.items():
    srcf = subprocess.run([sys.executable, str(T/"probe_sources.py"), str(book/f"packets/MOVEMENT-{m:03d}.md"), book.name], capture_output=True, text=True).stdout.split()
    src = []
    for f in srcf: src += sp.sentences(Path(f).read_text(encoding="utf-8"))
    src_sets = [set(t) for _, t in src]
    for c in chs:
        f = f"chapter-{c:02d}.md"
        a = sents(book/"state/completion/pre-lanes"/f); b = sents(book/"manuscript"/f)
        for tag, i1, i2, j1, j2 in difflib.SequenceMatcher(None, a, b, autojunk=False).get_opcodes():
            if tag == "equal": continue
            ra = [(best(sp.toks(s), src, src_sets) if len(sp.toks(s)) >= 8 else None) for s in a[i1:i2]]
            rb = [(best(sp.toks(s), src, src_sets) if len(sp.toks(s)) >= 8 else None) for s in b[j1:j2]]
            fa = " / ".join("short" if r is None else f"{r:.2f}" for r in ra) or "-"
            fb = " / ".join("short" if r is None else f"{r:.2f}" for r in rb) or "-"
            mx_a = max([r for r in ra if r is not None] or [0]); mx_b = max([r for r in rb if r is not None] or [0])
            flag = "  <-- crosses 0.35" if mx_b >= .35 > mx_a else ("  <-- crosses 0.50" if mx_b >= .5 > mx_a else ("  (up)" if mx_b > mx_a + 1e-9 else ""))
            print(f"{c:02d}  {fa:>20} -> {fb:<14}{flag}  | {' '.join(b[j1:j2])[:90]}")
