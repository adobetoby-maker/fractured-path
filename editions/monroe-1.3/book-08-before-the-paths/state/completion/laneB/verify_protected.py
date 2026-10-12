#!/usr/bin/env python3
"""Lane B verification: every changed paragraph of ch31-60 (manuscript vs state/completion/pre-lanes)
is checked for (a) dialogue, (b) italics (logs, letters, documents, acquisition units, fragment voices),
(c) numbers, (d) protected-patterns.txt, (e) BOOK_MAP section 10 quoted wording. Read-only."""
import re, difflib, collections
from pathlib import Path
E = Path("editions/monroe-1.3/book-08-before-the-paths")
OLD, NEW = E / "state/completion/pre-lanes", E / "manuscript"
NUM = re.compile(r"\b(\d+|one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|thirteen|fourteen|fifteen|sixteen|seventeen|eighteen|nineteen|twenty|thirty|forty|fifty|sixty|seventy|eighty|ninety|hundred|thousand|first|second|third|fourth|fifth|sixth|seventh|eighth|ninth|tenth|eleventh|twelfth|thirteenth|half|quarter|twice|thrice|once|dozen|score)\b", re.I)
def norm(s): return re.sub(r"[^a-z0-9 ]+", " ", s.lower().replace("’", "'").replace("'", "")).split()
def dialog(p): return re.findall(r'"[^"]*"?', p)
def italics(p): return re.findall(r"\*[^*]+\*", p)
pats = [l.strip() for l in (E / "protected-patterns.txt").read_text().splitlines() if l.strip() and not l.startswith("#")]
bm = (E / "BOOK_MAP.md").read_text()
sec10 = bm[bm.index("## 10. Protected wording"):bm.index("## 11.")]
quoted = {" ".join(norm(q)) for q in re.findall(r'"([^"]{12,})"', sec10)} | {" ".join(norm(q)) for q in re.findall(r"`([^`]{12,})`", sec10)} | {" ".join(norm(q)) for q in re.findall(r"\*([^*]{12,})\*", sec10)}
quoted = {q for q in quoted if len(q.split()) >= 3}
tot = collections.Counter(); bad = []
allold = alln = ""
for c in range(31, 61):
    o = (OLD / f"chapter-{c}.md").read_text(); n = (NEW / f"chapter-{c}.md").read_text()
    allold += " " + " ".join(norm(o)); alln += " " + " ".join(norm(n))
    op, np_ = o.split("\n"), n.split("\n")
    sm = difflib.SequenceMatcher(None, op, np_, autojunk=False)
    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        if tag == "equal": continue
        tot["hunks"] += 1
        a = "\n".join(op[i1:i2]); b = "\n".join(np_[j1:j2])
        if dialog(a) != dialog(b): bad.append((c, "DIALOGUE CHANGED", a[:90]))
        if italics(a) != italics(b): bad.append((c, "ITALIC CHANGED", a[:90]))
        if [x.lower() for x in NUM.findall(a)] != [x.lower() for x in NUM.findall(b)]: bad.append((c, "NUMBER CHANGED", a[:90] + " || " + str([x for x in NUM.findall(a)]) + " -> " + str([x for x in NUM.findall(b)])))
        an, bn = " ".join(norm(a)), " ".join(norm(b))
        for p in pats:
            if len(re.findall(p, an)) != len(re.findall(p, bn)) : bad.append((c, "PROTECTED PATTERN", p[:60]))
        for q in quoted:
            if an.count(q) != bn.count(q): bad.append((c, "BOOK_MAP s10 WORDING", q[:60]))
    # whole-chapter invariants
    if dialog(o) != dialog(n): bad.append((c, "chapter dialogue list differs", ""))
    if italics(o) != italics(n): bad.append((c, "chapter italics list differs", ""))
    tot["dialogue segments"] += len(dialog(n)); tot["italic spans"] += len(italics(n))
for p in pats:
    a, b = len(re.findall(p, allold)), len(re.findall(p, alln))
    tot["pattern hits before"] += a; tot["pattern hits after"] += b
    if a != b: bad.append(("31-60", "PATTERN COUNT", p[:60]))
qa = sum(allold.count(q) for q in quoted); qb = sum(alln.count(q) for q in quoted)
for q in quoted:
    if allold.count(q) != alln.count(q): bad.append(("31-60", "s10 COUNT", q[:60]))
print(dict(tot)); print("BOOK_MAP s10 quoted strings checked:", len(quoted), "| occurrences in ch31-60 before/after:", qa, qb)
print("protected patterns:", len(pats))
print("PROBLEMS:", len(bad))
for x in bad: print("  ", x)
