#!/usr/bin/env python3
"""Lane B read-only helper. Never reads the source edition.
usage:
  protected.py list  DIR 31 60      -> per chapter, the lines holding protected wording (BOOK_MAP section 10 runs >= MIN tokens, or a protected-patterns.txt match, or italic/document lines)
  protected.py check OLD_DIR NEW_DIR 31 60 -> every protected run in OLD must stand unchanged in NEW; every changed line is listed with a flag if it held protected or italic text
"""
import re, sys, difflib
from pathlib import Path
ED = Path('/Users/drive/fractured-path-monroe13/editions/monroe-1.3')
B = ED / 'book-07-void-roads'
TOK = re.compile(r"[a-z0-9]+(?:['’][a-z0-9]+)*")
def toks(t): return TOK.findall(t.lower().replace("’", "'"))
MIN = 6
maplines = (B / 'BOOK_MAP.md').read_text(encoding='utf-8').splitlines()
s = next(i for i, l in enumerate(maplines) if l.startswith('## 10.'))
e = next(i for i, l in enumerate(maplines) if l.startswith('## 11.'))
ptoks = toks("\n".join(maplines[s:e]))
grams = set(tuple(ptoks[i:i+MIN]) for i in range(len(ptoks)-MIN+1))
allow = [re.compile(l.strip()) for l in (B/'protected-patterns.txt').read_text(encoding='utf-8').splitlines() if l.strip() and not l.lstrip().startswith('#')]

def runs(line):
    t = toks(line); out = []; i = 0
    while i <= len(t)-MIN:
        if tuple(t[i:i+MIN]) in grams:
            j = i+MIN
            while j < len(t) and tuple(t[j-MIN+1:j+1]) in grams: j += 1
            out.append(" ".join(t[i:j])); i = j
        else: i += 1
    return out
def allowhits(line):
    n = " ".join(toks(line)); return [r.pattern for r in allow if r.search(n)]
def italic(line): return bool(re.search(r"\*[^*\s][^*]*\*", line)) or line.lstrip().startswith(('>', '```'))

def chapter(d, c): return (Path(d)/f'chapter-{c:02d}.md').read_text(encoding='utf-8').splitlines()

mode = sys.argv[1]
if mode == 'list':
    d, lo, hi = sys.argv[2], int(sys.argv[3]), int(sys.argv[4])
    for c in range(lo, hi+1):
        print(f'== ch{c}')
        incode = False
        for n, line in enumerate(chapter(d, c), 1):
            if line.strip().startswith('```'): incode = not incode; print(f'  {n}: CODE FENCE'); continue
            if incode: print(f'  {n}: CODE'); continue
            r = runs(line); a = allowhits(line); it = italic(line)
            if r or a or it:
                tag = ('MAP ' if r else '') + ('PAT ' if a else '') + ('ITAL ' if it else '')
                longest = max(r, key=len) if r else ''
                print(f'  {n}: {tag}| {len(longest.split())}w {longest[:70]}')
elif mode == 'check':
    old, new, lo, hi = sys.argv[2], sys.argv[3], int(sys.argv[4]), int(sys.argv[5])
    bad = 0; changed = 0
    for c in range(lo, hi+1):
        o = chapter(old, c); n = chapter(new, c)
        ntext = " ".join(toks("\n".join(n)))
        # 1. every protected run in the old file still stands in the new file
        for ln, line in enumerate(o, 1):
            for r in runs(line):
                if r not in ntext:
                    bad += 1; print(f'ch{c}:{ln} PROTECTED RUN LOST: {r[:100]}')
        # 2. allow patterns: same number of hits old and new
        otext = " ".join(toks("\n".join(o)))
        for r in allow:
            if len(r.findall(otext)) != len(r.findall(ntext)):
                bad += 1; print(f'ch{c} PATTERN COUNT CHANGED: {r.pattern[:80]}')
        # 3. changed lines
        sm = difflib.SequenceMatcher(None, o, n, autojunk=False)
        for tag, i1, i2, j1, j2 in sm.get_opcodes():
            if tag == 'equal': continue
            for k in range(i1, i2):
                changed += 1
                line = o[k]; r = runs(line); a = allowhits(line); it = italic(line)
                if r or a or it:
                    # the protected run(s) of this line must be present verbatim in the replacement lines
                    repl = " ".join(toks("\n".join(n[j1:j2])))
                    lost = [x for x in r if x not in repl]
                    al = [p for p in a if not re.search(p, repl)]
                    # italic spans must be byte-identical in the replacement
                    spans = re.findall(r"\*[^*]+\*", line); newraw = "\n".join(n[j1:j2])
                    sl = [x for x in spans if x not in newraw]
                    status = 'OK(protected text intact)' if not (lost or al or sl) else 'VIOLATION'
                    if status == 'VIOLATION': bad += 1
                    print(f'ch{c}:{k+1} changed line holds protected/italic text -> {status} {lost[:1]} {al[:1]} {sl[:1]}')
    print(f'# changed old lines: {changed}; violations: {bad}')
