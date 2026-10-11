#!/usr/bin/env python3
"""Read-only: print word-level differences between pre-lanes and manuscript for chapters 1-30."""
import difflib, pathlib, sys
root = pathlib.Path("/Users/drive/fractured-path-monroe13/editions/monroe-1.3/book-07-void-roads")
n = 0
for ch in range(1, 31):
    a = (root / "state/completion/pre-lanes" / f"chapter-{ch:02d}.md").read_text(encoding="utf-8")
    b = (root / "manuscript" / f"chapter-{ch:02d}.md").read_text(encoding="utf-8")
    aw, bw = a.split(" "), b.split(" ")
    # line numbers in the baseline for each word index
    sm = difflib.SequenceMatcher(None, aw, bw, autojunk=False)
    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        if tag == "equal":
            continue
        n += 1
        line = a[: len(" ".join(aw[:i1]))].count("\n") + 1
        ctx = " ".join(aw[max(0, i1 - 4):i1])
        old = " ".join(aw[i1:i2]).replace("\n", "\\n")
        new = " ".join(bw[j1:j2]).replace("\n", "\\n")
        print(f"{n}\tch{ch}:{line}\t…{ctx} [-{old}-] {{+{new}+}}")
