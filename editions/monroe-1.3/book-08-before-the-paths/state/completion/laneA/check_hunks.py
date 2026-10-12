#!/usr/bin/env python3
"""Lane A helper (read-only): every changed hunk vs pre-lanes, checked against protected lines.
For each changed baseline line: is it a flagged protected line, or within 2 file lines (one paragraph) of one?
Also: does any changed line differ inside quotation marks or inside *italics*?"""
import difflib, re, sys
from pathlib import Path
book = Path("editions/monroe-1.3/book-08-before-the-paths")
prot = {}
for l in (book/"state/completion/laneA/protected-lines.txt").read_text(encoding="utf-8").splitlines():
    f, rest = l.split(":", 1); n = int(rest.split("\t")[0]); prot.setdefault(f, {})[n] = rest.split("\t")[1]
Q = re.compile(r'"[^"]*"|“[^”]*”'); IT = re.compile(r"\*[^*]+\*")
tot = 0; bad = 0
for c in range(1, 31):
    f = f"chapter-{c:02d}.md"
    a = (book/"state/completion/pre-lanes"/f).read_text(encoding="utf-8").splitlines()
    b = (book/"manuscript"/f).read_text(encoding="utf-8").splitlines()
    sm = difflib.SequenceMatcher(None, a, b, autojunk=False)
    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        if tag == "equal": continue
        tot += 1
        lines = list(range(i1+1, max(i2, i1+1)+1))
        flags = []
        for n in lines:
            for d in (-2, -1, 0, 1, 2):
                if (n+d) in prot.get(f, {}): flags.append(f"{'ON' if d==0 else 'near'} {n+d}:{prot[f][n+d]}")
        old = "\n".join(a[i1:i2]); new = "\n".join(b[j1:j2])
        qchg = Q.findall(old) != Q.findall(new)
        ichg = IT.findall(old) != IT.findall(new)
        status = "OK" if not flags and not qchg and not ichg else "CHECK"
        if status != "OK": bad += 1
        print(f"{f}:{i1+1}-{i2} [{tag}] {status} {'; '.join(flags)} {'QUOTED-TEXT-CHANGED' if qchg else ''} {'ITALIC-CHANGED' if ichg else ''}")
print(f"hunks={tot} needing-a-look={bad}")
