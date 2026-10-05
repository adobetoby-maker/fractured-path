#!/usr/bin/env python3
"""Publish accepted Monroe 1.3 chapters (text only) to the reader app (boundary-universe).

usage:
  pwa_publish.py K N [--complete]                       update edition book-0K to chapters 1..N
  pwa_publish.py K N --new --title T --cover C --house H --series-index X --after-const CONST \
                 --synopsis S --description D [--complete]   create the edition entry first
Copies editions/monroe-1.3/<book>/manuscript/chapter-01..N.md byte-for-byte to
public/manuscripts/books/fractured-path-monroe-1.3/book-0K/manuscript/, regenerates the edition's
manuscript-index block from each chapter's H1, sets totalChapters = N and the subtitle's
"· in progress" flag (dropped with --complete). Does not build, commit or push.
"""
import argparse, json, re, shutil
from pathlib import Path

ED = Path(__file__).resolve().parents[1]
APP = Path("/Users/drive/boundary-universe")
BOOKS = {1: "book-01-the-shattered", 2: "book-02-iron-circuit", 3: "book-03-no-path-given", 4: "book-04-copper-crown",
         5: "book-05-the-silver-standard", 6: "book-06-the-compacts-hand", 7: "book-07-void-roads", 8: "book-08-before-the-paths"}
def js(x):
    return json.dumps(x, ensure_ascii=False)

WORDS = {1: "ONE", 2: "TWO", 3: "THREE", 4: "FOUR", 5: "FIVE", 6: "SIX", 7: "SEVEN", 8: "EIGHT"}

ap = argparse.ArgumentParser()
ap.add_argument("k", type=int); ap.add_argument("n", type=int)
ap.add_argument("--complete", action="store_true"); ap.add_argument("--new", action="store_true")
for f in ("title", "cover", "house", "series-index", "after-const", "synopsis", "description"):
    ap.add_argument("--" + f)
a = ap.parse_args()
k, n = a.k, a.n
eid = f"fractured-path-monroe-1.3-book-{k:02d}"
const = f"FRACTURED_MONROE_BOOK_{WORDS[k]}_ID"
src = ED / BOOKS[k] / "manuscript"
dst = APP / f"public/manuscripts/books/fractured-path-monroe-1.3/book-{k:02d}/manuscript"
dst.mkdir(parents=True, exist_ok=True)

# 1. texts
titles = []
for c in range(1, n + 1):
    f = src / f"chapter-{c:02d}.md"
    shutil.copyfile(f, dst / f.name)
    h1 = f.read_text().splitlines()[0].lstrip("# ").strip()
    titles.append(re.sub(r"^Chapter\s+\d+\s*[—–-]\s*", "", h1))
for extra in sorted(dst.glob("chapter-*.md")):  # never leave unaccepted chapters published
    if int(extra.stem.split("-")[1]) > n:
        extra.unlink()

# 2. manuscript index
mi = APP / "src/lib/manuscript-index.ts"
t = mi.read_text()
entries = "".join(f'    {{\n      number: {i},\n      title: {titles[i-1]!r},\n      path: "books/fractured-path-monroe-1.3/book-{k:02d}/manuscript/chapter-{i:02d}.md",\n    }},\n'
                  .replace("title: '", 'title: "').replace("',\n      path", '",\n      path') for i in range(1, n + 1))
block = f'  "{eid}": [\n{entries}  ],\n'
m = re.search(rf'  "{re.escape(eid)}": \[\n.*?\n  \],\n', t, re.S)
if m:
    t = t[:m.start()] + block + t[m.end():]
else:
    prev = max(j for j in range(1, 9) if j != k and f'"fractured-path-monroe-1.3-book-{j:02d}": [' in t and j < k)
    pm = re.search(rf'  "fractured-path-monroe-1.3-book-{prev:02d}": \[\n.*?\n  \],\n', t, re.S)
    t = t[:pm.end()] + block + t[pm.end():]
mi.write_text(t)

# 3. catalog
cat = APP / "src/lib/catalog.ts"
t = cat.read_text()
if a.new and f"export const {const}" not in t:
    prevc = max(j for j in range(1, k) if f"FRACTURED_MONROE_BOOK_{WORDS[j]}_ID = " in t)
    line = re.search(rf'export const FRACTURED_MONROE_BOOK_{WORDS[prevc]}_ID = "[^"]+";\n', t)
    t = t[:line.end()] + f'export const {const} = "{eid}";\n' + t[line.end():]
    anchor = re.search(rf"\n  \{{\n    id: {a.after_const},\n.*?\n  \}},\n", t, re.S)
    sub = f"The Fractured Path · Book {k} · Monroe 1.3 edition" + ("" if a.complete else " · in progress")
    entry = (f"  {{\n    id: {const},\n    seriesIndex: {a.series_index},\n    series: \"The Fractured Path\",\n"
             f"    title: {js(a.title)},\n    subtitle: \"{sub}\",\n    cover: \"{a.cover}\",\n    house: {js(a.house)},\n"
             f"    totalChapters: {n},\n    synopsis:\n      {js(a.synopsis)},\n    description:\n      {js(a.description)},\n  }},\n")
    t = t[:anchor.end()] + entry + t[anchor.end():]
em = re.search(rf"\n  \{{\n    id: {const},\n.*?\n  \}},\n", t, re.S)
blk = em.group(0)
blk2 = re.sub(r"totalChapters: \d+,", f"totalChapters: {n},", blk)
blk2 = re.sub(r'(subtitle: "[^"]*?)( · in progress)?"', lambda mm: mm.group(1) + ("" if a.complete else " · in progress") + '"', blk2)
t = t.replace(blk, blk2)
cat.write_text(t)
print(f"{eid}: {n} chapters copied; index regenerated; catalog totalChapters={n} {'complete' if a.complete else 'in progress'}")
