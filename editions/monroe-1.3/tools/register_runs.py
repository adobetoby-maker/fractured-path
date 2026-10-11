#!/usr/bin/env python3
"""Register unprotected overlap runs as protected patterns ONLY when the run is quoted in the movement packet
or the BOOK_MAP (i.e. a plan-quoted line kept whole). Anything else is reported and left for the author.
usage (from the worktree root): register_runs.py BOOK N LABEL"""
import re, subprocess, sys
from pathlib import Path
book, n, label = sys.argv[1], int(sys.argv[2]), sys.argv[3]
E = Path("editions/monroe-1.3"); B = E / book
def norm(s): return re.sub(r"\s+", " ", re.sub(r"[^a-z0-9' ]+", " ", s.lower().replace("’", "'"))).strip()
plan = norm((B / f"packets/MOVEMENT-{n:03d}.md").read_text() + " " + (B / "BOOK_MAP.md").read_text())
out = subprocess.run(["bash", str(E / "tools/ed.sh"), "overlap", book, str(n)], capture_output=True, text=True).stdout
add, rest = [], []
for line in out.splitlines():
    p = line.split("\t")
    if len(p) == 4 and p[0].startswith("chapter-"):
        run = norm(p[3])
        (add if run in plan else rest).append((p[0], run))
if add:
    with open(B / "protected-patterns.txt", "a") as f:
        f.write(f"# {label} — plan-quoted lines (kept whole)\n")
        for _, r in add: f.write(r.replace("'", ".?") + "\n")
for c, r in add: print("registered:", c, "|", r)
for c, r in rest: print("NOT IN PLAN (author to recompose or audit to rule):", c, "|", r)
print(f"{len(add)} registered, {len(rest)} left")
