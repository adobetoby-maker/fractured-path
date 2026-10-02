#!/usr/bin/env python3
"""Find runs of N+ consecutive words an edition chapter shares with the source edition.

usage: source_overlap.py --book BOOKDIR [--min 10] EDITION_CHAPTER.md [...]
  BOOKDIR is the current-edition book directory (books/<book>), whose chapters/*.md
  are the source. Protected wording listed in the edition BOOK_MAP is reported
  separately (allowed), not as reuse.

Method: lower-case word tokens (letters, digits, apostrophes), punctuation and
markdown ignored. Every maximal shared run of >= --min tokens is reported once,
with its length, location (edition paragraph number) and the text. A run that lies
inside any line of the BOOK_MAP is classed PROTECTED. Reported as text so a repair
author can find and rewrite it.
"""
import argparse, re, sys
from pathlib import Path

TOK = re.compile(r"[a-z0-9]+(?:['’][a-z0-9]+)*")


def toks(text):
    return TOK.findall(text.lower().replace("’", "'"))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--book", required=True, type=Path)
    ap.add_argument("--map", type=Path, help="edition BOOK_MAP.md (protected wording)")
    ap.add_argument("--min", type=int, default=10)
    ap.add_argument("--allow", type=Path, help="file of regexes (one per line, # comments); a run matching any is PROTECTED")
    ap.add_argument("chapters", nargs="+", type=Path)
    a = ap.parse_args()
    n = a.min
    src = []
    for p in sorted((a.book / "chapters").glob("chapter-*.md")):
        src += toks(p.read_text(encoding="utf-8"))
    grams = {}
    for i in range(len(src) - n + 1):
        grams.setdefault(tuple(src[i:i + n]), i)
    protected = " ".join(toks(a.map.read_text(encoding="utf-8"))) if a.map and a.map.exists() else ""
    allow = []
    if a.allow and a.allow.exists():
        allow = [re.compile(l.strip()) for l in a.allow.read_text(encoding="utf-8").splitlines()
                 if l.strip() and not l.lstrip().startswith("#")]
    total = prot = 0
    for ch in a.chapters:
        paras = [l for l in ch.read_text(encoding="utf-8").splitlines() if l.strip()]
        for pi, para in enumerate(paras, 1):
            t = toks(para)
            i = 0
            while i <= len(t) - n:
                if tuple(t[i:i + n]) in grams:
                    j = i + n
                    while j < len(t) and tuple(t[j - n + 1:j + 1]) in grams:
                        j += 1
                    run = " ".join(t[i:j])
                    kind = "PROTECTED" if (protected and run in protected) or any(r.search(run) for r in allow) else "REUSE"
                    if kind == "REUSE":
                        total += 1
                        print(f"{ch.name}\tpara {pi}\t{j - i}w\t{run}")
                    else:
                        prot += 1
                    i = j
                else:
                    i += 1
    print(f"# summary: {total} unprotected shared runs of >= {n} words; {prot} protected runs (allowed)", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
