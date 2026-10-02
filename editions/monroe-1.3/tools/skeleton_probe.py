#!/usr/bin/env python3
"""Sentence-level source-distance probe (catches paraphrase the n-word overlap gate cannot see).

Method (the Fable reviewers' align.py, made a tool): every manuscript sentence of >= 8 tokens is
matched to its best source sentence by difflib ordered-token ratio, prefiltered by token-set
Jaccard >= 0.15. Ratio >= 0.50 = kept skeleton; >= 0.35 = close paraphrase. Reported per chapter
and per scene (scenes split on '---' lines) as a share of sentences.
Baselines: event-list drafting (B1 M8) 0-1% per chapter, close ~11%; reviewers' clean band 2-13%;
anything above ~15% in a scene is tracked prose. Use --show to list the matched pairs.

usage: skeleton_probe.py [--show] --source SRC_CH.md [SRC_CH.md ...] -- MS_CH.md [MS_CH.md ...]
"""
import re, sys, difflib
from pathlib import Path

TOK = re.compile(r"[a-z0-9]+(?:['’][a-z0-9]+)*")
SPLIT = re.compile(r"(?<=[.!?…])[\"'”’*)]*\s+")


def toks(s):
    return TOK.findall(s.lower().replace("’", "'"))


def sentences(text):
    text = re.sub(r"^#.*$", "", text, flags=re.M)
    out = []
    for para in re.split(r"\n\s*\n", text):
        para = " ".join(para.split())
        if not para or para == "---":
            continue
        for s in SPLIT.split(para):
            t = toks(s)
            if len(t) >= 8:
                out.append((s, t))
    return out


def main(argv):
    show = argv[:1] == ["--show"]
    if show:
        argv = argv[1:]
    if "--" not in argv or argv[0] != "--source":
        sys.exit(__doc__)
    i = argv.index("--")
    src_files, ms_files = argv[1:i], argv[i + 1:]
    src = []
    for f in src_files:
        src += sentences(Path(f).read_text(encoding="utf-8"))
    src_sets = [set(t) for _, t in src]
    tot = [0, 0, 0]
    for f in ms_files:
        text = Path(f).read_text(encoding="utf-8")
        scenes = re.split(r"\n\s*---\s*\n", text)
        ch = [0, 0, 0]
        rows, rows_show = [], []
        for n, sc in enumerate(scenes, 1):
            k = [0, 0, 0]
            for s, t in sentences(sc):
                ts = set(t)
                best, bs = 0.0, ""
                for (sx, st), ss in zip(src, src_sets):
                    j = len(ts & ss) / len(ts | ss)
                    if j < 0.15:
                        continue
                    r = difflib.SequenceMatcher(None, t, st, autojunk=False).ratio()
                    if r > best:
                        best, bs = r, sx
                if show and best >= 0.50:
                    rows_show.append((n, best, s, bs))
                k[0] += 1
                k[1] += best >= 0.50
                k[2] += best >= 0.35
            rows.append((n, k))
            ch = [a + b for a, b in zip(ch, k)]
        tot = [a + b for a, b in zip(tot, ch)]
        pct = lambda k, i: 100 * k[i] / k[0] if k[0] else 0
        print(f"{Path(f).name}\tsentences={ch[0]}\tskeleton={pct(ch,1):.0f}%\tclose={pct(ch,2):.0f}%")
        for n, k in rows:
            flag = "  <-- over 15%" if pct(k, 1) > 15 and k[0] >= 10 else ""
            print(f"  scene {n}\tn={k[0]}\tskeleton={pct(k,1):.0f}%\tclose={pct(k,2):.0f}%{flag}")
        for n, r, s, bs in rows_show:
            print(f"    [s{n} {r:.2f}] MS: {s}\n              SRC: {bs}")
    if tot[0]:
        print(f"TOTAL\tsentences={tot[0]}\tskeleton={100*tot[1]/tot[0]:.0f}%\tclose={100*tot[2]/tot[0]:.0f}%")


if __name__ == "__main__":
    main(sys.argv[1:])
