#!/usr/bin/env python3
"""Apply a Sol report's "Exact line fixes" to a book's manuscript.
usage: apply_fixes.py BOOK_DIR REPORT.md [--dry]
Understands   N. `manuscript/chapter-NN.md`\n   old: `...`\n   new: `...`   (inline backticks, \\n = line break)
and fenced variants (old:/new: followed by a ``` block). Each old string must match exactly once; otherwise
the fix is skipped and reported. Never guesses."""
import re, sys
from pathlib import Path
book, report = Path(sys.argv[1]), Path(sys.argv[2]); dry = "--dry" in sys.argv
t = report.read_text()
m = re.search(r"^## .*[Ll]ine fixes.*$", t, re.M)
t = t[m.start():] if m else t
items = re.split(r"(?m)^\s*(\d+)\.\s+`(manuscript/chapter-\d+\.md)`\s*$", t)
ok = bad = 0
def grab(body, key):
    f = re.search(rf"(?ms)^\s*{key}:\s*\n\s*```[a-z]*\n(.*?)\n\s*```", body)
    if f: return f.group(1)
    i = re.search(rf"(?ms)^\s*{key}:\s*`(.*?)`\s*$", body)
    return i.group(1).replace("\\n", "\n") if i else None
for k in range(1, len(items), 3):
    n, path, body = items[k], items[k+1], items[k+2]
    old, new = grab(body, "old"), grab(body, "new")
    f = book / path
    if old is None or new is None or not f.exists():
        print(f"{n}. {path}: UNPARSED"); bad += 1; continue
    s = f.read_text(); c = s.count(old)
    if c != 1:
        print(f"{n}. {path}: SKIPPED (old matches {c}x): {old[:70]!r}"); bad += 1; continue
    if not dry: f.write_text(s.replace(old, new))
    print(f"{n}. {path}: applied"); ok += 1
print(f"applied {ok}, not applied {bad}")
