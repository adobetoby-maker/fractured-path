#!/usr/bin/env python3
"""Print the SOURCE chapter files a movement packet names (for sweep_probe.sh).
Reads the packet's "Read before drafting" / "Source chapters to read first" line and takes only the clause that
names this book's source: "source chapters 5, 6 and 7", "source `books/<b>/chapters/chapter-01.md` through
`chapter-04.md`", "B4 source `chapter-01.md`, `chapter-02.md`", "Source chapters to read first, in full: 1, 2, 3".
Ignores previous-book chapters, "the previous ending …" and manuscript/ paths.
usage: probe_sources.py PACKET BOOK
"""
import re, sys
from pathlib import Path

packet, book = Path(sys.argv[1]), sys.argv[2]
text = packet.read_text()
line = next((l for l in text.splitlines() if re.search(r"read before drafting|source chapters to read first", l, re.I)), "")
m = re.search(r"source chapters to read first[^:]*:([^(\n]*)", line, re.I)
if m:
    nums = [int(x) for x in re.findall(r"\d+", m.group(1))]
else:
    m = re.search(r"\bsource\b(.*)", line, re.I)
    seg = re.split(r";|\.\s|the previous ending", m.group(1), flags=re.I)[0] if m else ""
    seg = re.sub(r"`?manuscript/[^`]*`?", "", seg)
    chs = [int(x) for x in re.findall(r"chapter-(\d+)\.md", seg)]
    if re.search(r"\bthrough\b|–|-to-", seg) and len(chs) >= 2:
        nums = list(range(chs[0], chs[-1] + 1))
    elif chs:
        nums = chs
    else:
        nums = [int(x) for x in re.findall(r"\d+", re.split(r"chapters?", seg, maxsplit=1)[-1])]
root = Path(__file__).resolve().parents[3] / "books" / book / "chapters"
for n in nums:
    print(root / f"chapter-{n:02d}.md")
