#!/usr/bin/env python3
"""Lane B read-only helper: word-level diff of chapters 31-60 against the pre-lanes baseline."""
import difflib, sys
from pathlib import Path
B=Path('/Users/drive/fractured-path-monroe13/editions/monroe-1.3/book-07-void-roads')
lo,hi=int(sys.argv[1]),int(sys.argv[2])
tot=0
for c in range(lo,hi+1):
    o=(B/'state/completion/pre-lanes'/f'chapter-{c:02d}.md').read_text().splitlines()
    n=(B/'manuscript'/f'chapter-{c:02d}.md').read_text().splitlines()
    sm=difflib.SequenceMatcher(None,o,n,autojunk=False)
    for tag,i1,i2,j1,j2 in sm.get_opcodes():
        if tag=='equal': continue
        ow=" ".join(o[i1:i2]).split(); nw=" ".join(n[j1:j2]).split()
        wm=difflib.SequenceMatcher(None,ow,nw,autojunk=False)
        parts=[]
        for t,a1,a2,b1,b2 in wm.get_opcodes():
            if t=='equal':
                seg=ow[a1:a2]
                parts.append(" ".join(seg[-5:]) if len(seg)>10 else " ".join(seg)) if False else None
                ctx=" ".join(seg[:4])+" … "+" ".join(seg[-4:]) if len(seg)>9 else " ".join(seg)
                parts.append(ctx)
            else:
                d=" ".join(ow[a1:a2]); a=" ".join(nw[b1:b2])
                parts.append("[-"+d+"-]" if d else ""); parts.append("{+"+a+"+}" if a else "")
                tot+=1
        print(f"ch{c}:{i1+1}  "+" ".join(p for p in parts if p))
print("# word-level change sites:",tot)
