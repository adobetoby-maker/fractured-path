#!/usr/bin/env python3
"""Read-only verification that Lane A's edits (manuscript ch1-30 vs state/completion/pre-lanes) lie outside protected text.
Reads only edition files: pre-lanes, manuscript, protected-patterns.txt, BOOK_MAP.md. Never opens books/ or v3-runs/."""
import re, difflib, pathlib, collections
B = pathlib.Path("/Users/drive/fractured-path-monroe13/editions/monroe-1.3/book-07-void-roads")
pre = lambda c: (B / "state/completion/pre-lanes" / f"chapter-{c:02d}.md").read_text(encoding="utf-8")
cur = lambda c: (B / "manuscript" / f"chapter-{c:02d}.md").read_text(encoding="utf-8")
norm = lambda s: " ".join(re.findall(r"[a-z0-9]+(?:['’][a-z0-9]+)*", s.lower().replace("’", "'")))
ok = True
def check(name, cond, detail=""):
    global ok
    ok &= bool(cond)
    print(("PASS  " if cond else "FAIL  ") + name + (("  " + detail) if detail else ""))

A = {c: pre(c) for c in range(1, 31)}; Z = {c: cur(c) for c in range(1, 31)}
allA = norm("\n".join(A[c] for c in range(1, 31))); allZ = norm("\n".join(Z[c] for c in range(1, 31)))

# 1. protected-patterns.txt: every pattern matches the same number of times before and after (lane text)
pats = [l.strip() for l in (B / "protected-patterns.txt").read_text(encoding="utf-8").splitlines() if l.strip() and not l.startswith("#")]
bad = []; hits = 0
for p in pats:
    r = re.compile(p)
    a, z = len(r.findall(allA)), len(r.findall(allZ))
    hits += a > 0
    if a != z: bad.append((p[:50], a, z))
check(f"protected-patterns.txt: {len(pats)} patterns, {hits} occur in ch1-30, identical match counts before/after", not bad, str(bad))

# 2. every italic segment (*...*: logs, letters, slips, ledger lines, documents, quoted words) identical as a multiset, per chapter
bad = []; nseg = 0
for c in range(1, 31):
    ia = collections.Counter(re.findall(r"\*[^*\n]+\*", A[c])); iz = collections.Counter(re.findall(r"\*[^*\n]+\*", Z[c]))
    nseg += sum(ia.values())
    if ia != iz: bad.append((c, list((ia - iz).items())[:3], list((iz - ia).items())[:3]))
check(f"italic segments (logs/letters/slips/documents): {nseg} segments, multiset identical per chapter", not bad, str(bad))

# 3. every 'Deployment since the Line' line identical, in order
da = [(c, m) for c in range(1, 31) for m in re.findall(r"Deployment since the Line: [a-z-]+", A[c])]
dz = [(c, m) for c in range(1, 31) for m in re.findall(r"Deployment since the Line: [a-z-]+", Z[c])]
check(f"'Deployment since the Line' lines: {len(da)} lines, identical in order", da == dz)

# 4. spoken dialogue: the sequence of words inside double quotes is identical per chapter (quote boundaries may merge)
bad = []; nq = 0
for c in range(1, 31):
    qa = norm(" ".join(re.findall(r"\"([^\"]*)\"", A[c]))); qz = norm(" ".join(re.findall(r"\"([^\"]*)\"", Z[c])))
    nq += len(qa.split())
    if qa != qz:
        sm = difflib.SequenceMatcher(None, qa.split(), qz.split(), autojunk=False)
        bad.append((c, [(" ".join(qa.split()[i1:i2]), " ".join(qz.split()[j1:j2])) for t, i1, i2, j1, j2 in sm.get_opcodes() if t != "equal"][:3]))
check(f"dialogue: {nq} spoken words, word sequence identical per chapter", not bad, str(bad))
qcount = [(c, A[c].count('"'), Z[c].count('"')) for c in range(1, 31) if A[c].count('"') != Z[c].count('"')]
print(f"      quote-mark count changed in chapters (merged speech where a hand beat was cut): {qcount}")

# 5. BOOK_MAP section 10: every protected unit that stood in the baseline lane text still stands, same number of times
bm = (B / "BOOK_MAP.md").read_text(encoding="utf-8")
sec = bm[bm.index("## 10. Protected wording"):bm.index("## 11.")]
units = set()
for m in re.finditer(r"\*([^*\n]{12,})\*|\"([^\"\n]{12,})\"", sec):
    u = norm(m.group(1) or m.group(2))
    for piece in re.split(r"\s*…\s*|\s+/\s+", (m.group(1) or m.group(2))):
        pn = norm(piece)
        if len(pn.split()) >= 4: units.add(pn)
present = [u for u in units if u in allA]
bad = [(u[:60], allA.count(u), allZ.count(u)) for u in present if allA.count(u) != allZ.count(u)]
check(f"BOOK_MAP §10: {len(units)} quoted/italic units, {len(present)} stand in ch1-30 at baseline, all stand unchanged after", not bad, str(bad))

# 6. every changed hunk lies outside protected runs, by POSITION: token indices covered by any §10 unit or pattern match
#    in the baseline chapter must not be deleted/replaced, and nothing may be inserted strictly inside such a run
TOKRE = re.compile(r"[a-z0-9]+(?:['’][a-z0-9]+)*")
def tk(s): return TOKRE.findall(s.lower().replace("’", "'"))
bad = []; nh = 0; nprot = 0
for c in range(1, 31):
    ta, tz = tk(A[c]), tk(Z[c]); ja = " ".join(ta)
    starts = [0]
    for w in ta: starts.append(starts[-1] + len(w) + 1)   # char offset of each token in ja
    import bisect
    covered = set()
    def cover(m0, m1):
        i0 = bisect.bisect_right(starts, m0) - 1; i1 = bisect.bisect_left(starts, m1)
        covered.update(range(i0, i1))
    for u in present:
        for m in re.finditer(r"(?<![a-z0-9'])" + re.escape(u) + r"(?![a-z0-9'])", ja): cover(m.start(), m.end())
    for pat in pats:
        for m in re.finditer(pat, ja): cover(m.start(), m.end())
    nprot += len(covered)
    for t, i1, i2, j1, j2 in difflib.SequenceMatcher(None, ta, tz, autojunk=False).get_opcodes():
        if t == "equal": continue
        nh += 1
        hit = [i for i in range(i1, i2) if i in covered]
        inside = (i1 == i2 and (i1 - 1) in covered and i1 in covered)
        if hit or inside: bad.append((c, " ".join(ta[max(0, i1 - 3):i2 + 3])[:90]))
check(f"changed hunks: {nh} token-level hunks; {nprot} protected tokens in ch1-30; no hunk deletes, replaces or splits a protected run", not bad, str(bad))

# 7. numbers: digits in removed vs inserted text
print("      number words/digits inside removed text (back-references cut with their callback; no primary statement changed):")
NUM = r"\b(one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|thirteen|fourteen|fifteen|sixteen|twenty|thirty|forty|fifty|sixty|seventy|eighty|ninety|hundred|thousand|first|second|third|fourth|fifth|ninth|tenth|[a-z]+-(?:first|second|third|fourth|fifth|sixth|seventh|eighth|ninth)|\d+)\b"
for c in range(1, 31):
    aw, zw = A[c].split(" "), Z[c].split(" ")
    for t, i1, i2, j1, j2 in difflib.SequenceMatcher(None, aw, zw, autojunk=False).get_opcodes():
        if t == "equal": continue
        ra, rz = re.findall(NUM, " ".join(aw[i1:i2]).lower()), re.findall(NUM, " ".join(zw[j1:j2]).lower())
        if ra != rz: print(f"        ch{c}: removed {ra} inserted {rz}  ::  {' '.join(aw[i1:i2])[:90]!r}")

# 8. inserted text: banned content
ins = []
for c in range(1, 31):
    aw, zw = A[c].split(" "), Z[c].split(" ")
    for t, i1, i2, j1, j2 in difflib.SequenceMatcher(None, aw, zw, autojunk=False).get_opcodes():
        if t != "equal" and j2 > j1: ins.append((c, " ".join(zw[j1:j2])))
txt = " ".join(s for _, s in ins).lower()
banned = re.findall(r"\b(spring|summer|autumn|winter|fall|january|february|march|april|may|june|july|august|september|october|november|december|monday|tuesday|wednesday|thursday|friday|saturday|sunday|met(?:er|re)s?|kilomet\w+|centimet\w+|inch(?:es)?|miles?|his path)\b", txt)
check(f"inserted text ({sum(len(s.split()) for _, s in ins)} words in {len(ins)} hunks): no season/month/weekday, no metric unit, no 'his Path'", not banned, str(banned))
caps = sorted({w.strip('.,;:"*') for _, s in ins for w in s.replace("\n", " ").split()[0:] if re.match(r"[A-Z][a-z]+", w.strip('.,;:"*'))})
print("      capitalised words in inserted text (check for new names):", caps)
print("\nOVERALL:", "PASS" if ok else "FAIL")
