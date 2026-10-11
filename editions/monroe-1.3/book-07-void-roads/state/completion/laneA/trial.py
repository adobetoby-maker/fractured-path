#!/usr/bin/env python3
"""Read-only on the manuscript. Writes a TRIAL COPY of one chapter into laneA/tmp with one string swapped,
then runs the official skeleton probe on the copy and prints per-scene counts beside the baseline's.
usage: trial.py CH 'CURRENT' 'TRIAL'
"""
import sys, subprocess, pathlib, re
root = pathlib.Path("/Users/drive/fractured-path-monroe13")
B = root / "editions/monroe-1.3/book-07-void-roads"
L = B / "state/completion/laneA"
ch = int(sys.argv[1]); cur, new = sys.argv[2], sys.argv[3]
m = 1 if ch <= 7 else 2 if ch <= 14 else 3 if ch <= 22 else 4
t = (B / "manuscript" / f"chapter-{ch:02d}.md").read_text(encoding="utf-8")
assert t.count(cur) == 1, f"current string occurs {t.count(cur)} times"
tmp = L / "tmp" / f"chapter-{ch:02d}.md"
tmp.write_text(t.replace(cur, new), encoding="utf-8")
src = (L / f"src-m{m}.paths").read_text().split()
def scenes(path):
    out = subprocess.run(["python3", str(root / "editions/monroe-1.3/tools/skeleton_probe.py"), "--source", *src, "--", str(path)],
                         capture_output=True, text=True, cwd=root).stdout
    res = []
    for line in out.splitlines():
        mm = re.match(r"\s+scene (\d+)\s+n=(\d+)\s+skeleton=(\d+)%\s+close=(\d+)%", line)
        if mm:
            n = int(mm.group(2)); res.append((n, round(int(mm.group(3)) * n / 100), round(int(mm.group(4)) * n / 100)))
    return res
base = scenes(B / "state/completion/pre-lanes" / f"chapter-{ch:02d}.md")
tr = scenes(tmp)
flag = [f"s{i+1}:{b}->{a}" for i, (b, a) in enumerate(zip(base, tr)) if a[1] > b[1] or a[2] > b[2]]
print(f"ch{ch} trial: rises = {flag if flag else 'NONE'}")
