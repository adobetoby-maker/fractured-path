#!/usr/bin/env python3
"""Lane B helper: exact skeleton / close counts per chapter, baseline vs manuscript, using the
edition tool's own functions (tools/skeleton_probe.py). Prints MANUSCRIPT sentences only (never a
source sentence) where a sentence that is new or changed in the manuscript sits at >= 0.35."""
import sys, re, difflib, subprocess
from pathlib import Path
sys.path.insert(0, "editions/monroe-1.3/tools")
import skeleton_probe as sp
BOOK = "book-08-before-the-paths"
E = Path("editions/monroe-1.3") / BOOK
RANGES = {5: (31, 33), 6: (34, 40), 7: (41, 46), 8: (47, 53), 9: (54, 60)}

def best(t, src, sets):
    ts = set(t); b = 0.0
    for (sx, st), ss in zip(src, sets):
        if len(ts & ss) / len(ts | ss) < 0.15:
            continue
        r = difflib.SequenceMatcher(None, t, st, autojunk=False).ratio()
        if r > b: b = r
    return b

for m, (lo, hi) in RANGES.items():
    out = subprocess.run([sys.executable, "editions/monroe-1.3/tools/probe_sources.py",
                          str(E / "packets" / f"MOVEMENT-{m:03d}.md"), BOOK], capture_output=True, text=True).stdout.split()
    src = []
    for f in out:
        src += sp.sentences(Path(f).read_text(encoding="utf-8"))
    sets = [set(t) for _, t in src]
    for c in range(lo, hi + 1):
        old = sp.sentences((E / "state/completion/pre-lanes" / f"chapter-{c:02d}.md").read_text(encoding="utf-8"))
        new = sp.sentences((E / "manuscript" / f"chapter-{c:02d}.md").read_text(encoding="utf-8"))
        oldset = {s for s, _ in old}
        ro = [best(t, src, sets) for _, t in old]
        rn = [(s, best(t, src, sets)) for s, t in new]
        line = (f"ch{c} sentences {len(old)}->{len(new)}  skeleton(>=0.50) {sum(r>=0.5 for r in ro)}->{sum(r>=0.5 for _,r in rn)}"
                f"  close(>=0.35) {sum(r>=0.35 for r in ro)}->{sum(r>=0.35 for _,r in rn)}")
        print(line)
        for s, r in rn:
            if s not in oldset and r >= 0.35:
                print(f"    changed sentence at {r:.2f}: {s[:110]}")
