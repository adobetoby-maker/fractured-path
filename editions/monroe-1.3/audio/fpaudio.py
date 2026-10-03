#!/usr/bin/env python3
"""Fractured Path (Monroe 1.3 edition) -> Breeze direction tracks.

Same conventions as the Meridian run (meridian-run/*/build.py, verify.py): one segment per paragraph
(split at sentences over 700 chars), per-segment instruct starting with a pace cue, directed pauses
(330 cut-in, 450 breath, 600 thought, 850 reset, 1200 landing/chapter end, 1500 scene break).

usage:
  fpaudio.py segment BOOK CH        -> RUN/<BOOK>-chNN/raw_segs.json (+ chapter.md snapshot)
  fpaudio.py build   BOOK CH        -> direction.json from spec.json (written by the director)
  fpaudio.py verify  BOOK CH        -> word-lock and format checks; writes direction.ready on pass
  fpaudio.py status  BOOK           -> per-chapter state
The director (an LLM seat) writes RUN/<BOOK>-chNN/spec.json:
  {"summary": "...", "speakers": {"Lira": "same narrator, ... for Lira; ..."},
   "assign": {"s012": "Lira", ...},                 # unlisted segments are the narrator
   "over":   {"s001": ["SLOW", "base narrator, ..."], ...},   # pace tier + colour, overrides the speaker base
   "pause":  {"s014": 850, ...}, "cut": ["s051"], "note": {"s003": "..."}}
"""
import json, math, re, sys
from pathlib import Path

ED = Path(__file__).resolve().parents[1]
RUN = Path("/Users/drive/.local/share/monroe-tts/fractured-run")
PACE = {"SLOW": "Slow, about 120 words per minute, ", "BASE": "Unhurried, about 130 words per minute, ",
        "EASY": "Easy, about 140 words per minute, "}
NARRATOR = "base narrator: low and restrained; plain, close and understated."
LIM = 700


def chdir(book, ch):
    return RUN / f"{book}-ch{int(ch):02d}"


def source(book, ch):
    return ED / book / "manuscript" / f"chapter-{int(ch):02d}.md"


def blocks(raw):
    """Paragraph blocks with headings removed, code fences flattened, '*' stripped. '---' kept as marker."""
    raw = re.sub(r"^```[^\n]*\n(.*?)^```\s*$", lambda m: "\n".join(
        l.strip().rstrip(".") + "." for l in m.group(1).splitlines() if l.strip()) + "\n",
        raw, flags=re.S | re.M)
    out = []
    for b in re.split(r"\n\s*\n", raw):
        b = b.strip()
        if not b or b.startswith("#"):
            continue
        out.append("---" if b == "---" else " ".join(b.replace("*", "").split()))
    return out


def tokens(text):
    return text.split()


def split_long(t):
    if len(t) <= LIM:
        return [t]
    parts = re.split(r'(?<=[.!?…])\s+|(?<=[.!?…]["”’])\s+', t)
    target = len(t) / math.ceil(len(t) / LIM)
    out, cur = [], ""
    for p in parts:
        if cur and (len(cur) + 1 + len(p) > LIM or len(cur) >= target):
            out.append(cur); cur = p
        else:
            cur = f"{cur} {p}" if cur else p
    if cur:
        out.append(cur)
    return out


def segment(book, ch):
    src = source(book, ch).read_text()
    d = chdir(book, ch); d.mkdir(parents=True, exist_ok=True)
    (d / "chapter.md").write_text(src)
    segs = []
    for b in blocks(src):
        if b == "---":
            segs[-1]["brk"] = True
            continue
        for piece in split_long(b):
            segs.append({"text": piece, "brk": False})
    for i, s in enumerate(segs):
        s["id"] = f"s{i + 1:03d}"
    (d / "raw_segs.json").write_text(json.dumps(segs, indent=1, ensure_ascii=False))
    title = re.match(r"#\s*(.+)", src.splitlines()[0]).group(1).strip()
    print(f"{d.name}: {len(segs)} segments, max {max(len(s['text']) for s in segs)} chars, title {title!r}")


def build(book, ch):
    d = chdir(book, ch)
    segs = json.loads((d / "raw_segs.json").read_text())
    spec = json.loads((d / "spec.json").read_text())
    spk, assign, over = spec.get("speakers", {}), spec.get("assign", {}), spec.get("over", {})
    pause, cut, note = spec.get("pause", {}), set(spec.get("cut", [])), spec.get("note", {})
    ids = {s["id"] for s in segs}
    bad = [k for k in list(assign) + list(over) + list(pause) + list(cut) + list(note) if k not in ids]
    if bad:
        sys.exit(f"spec names unknown segment ids: {bad[:10]}")
    missing = sorted({v for v in assign.values() if v not in spk})
    if missing:
        sys.exit(f"assign uses speakers with no base colour: {missing}")
    title = re.match(r"#\s*(.+)", (d / "chapter.md").read_text().splitlines()[0]).group(1).strip()
    out = []
    for i, s in enumerate(segs):
        sid, who = s["id"], assign.get(s["id"], "narrator")
        if sid in over:
            tier, colour = over[sid]
        else:
            tier, colour = "BASE", (spk[who] if who != "narrator" else NARRATOR)
        if tier not in PACE:
            sys.exit(f"{sid}: unknown pace tier {tier}")
        if s["brk"]:
            p = 1500
        elif i == len(segs) - 1:
            p = 1200
        elif sid in cut:
            p = 330
        else:
            p = int(pause.get(sid, 600))
        seg = {"id": sid, "speaker": who, "text": s["text"], "instruct": PACE[tier] + colour, "pauseAfterMs": p}
        if sid in note:
            seg["note"] = note[sid]
        out.append(seg)
    track = {"chapter": f"{book}/chapter-{int(ch):02d}", "title": title, "engine": "Breeze TTS 2 (MLX)",
             "narrator": "Calder", "coach": "CALDER_DELIVERY_COACH_V1", "edition": "monroe-1.3",
             "lexiconStatus": "apply only owner-confirmed render substitutions",
             "summary": spec.get("summary", ""), "segments": out}
    (d / "direction.json").write_text(json.dumps(track, indent=1, ensure_ascii=False))
    print(f"{d.name}: direction.json {len(out)} segments, {sum(1 for x in out if x['speaker'] != 'narrator')} voiced")


def verify(book, ch):
    d = chdir(book, ch)
    src = source(book, ch).read_text()
    snap = (d / "chapter.md").read_text()
    errs = []
    if src != snap:
        errs.append("manuscript changed since segmentation (re-run segment)")
    A = tokens(" ".join(b for b in blocks(src) if b != "---"))
    tr = json.loads((d / "direction.json").read_text())["segments"]
    B = tokens(" ".join(s["text"] for s in tr))
    if A != B:
        k = next((i for i, (x, y) in enumerate(zip(A, B)) if x != y), min(len(A), len(B)))
        errs.append(f"word-lock FAIL at token {k}: src {A[k:k+6]} vs seg {B[k:k+6]} (src {len(A)}, seg {len(B)})")
    if any(len(s["text"]) > LIM for s in tr):
        errs.append("segment over 700 chars")
    if any("*" in s["text"] for s in tr):
        errs.append("asterisk in a segment")
    if not all(any(s["instruct"].startswith(v) for v in PACE.values()) for s in tr):
        errs.append("instruct without a pace cue")
    long = [s["id"] for s in tr if len(s["instruct"].split()) > 32]
    if long:
        errs.append(f"instruct over 32 words: {long[:5]}")
    nb = sum(1 for b in blocks(src) if b == "---")
    if nb != sum(1 for s in tr if s["pauseAfterMs"] == 1500):
        errs.append("scene-break pause count mismatch")
    ready = d / "direction.ready"
    if errs:
        ready.unlink(missing_ok=True)
        print(f"{d.name}: FAIL\n  " + "\n  ".join(errs)); sys.exit(1)
    ready.write_text(f"words {len(A)} segments {len(tr)}\n")
    mins = len(A) / 130
    print(f"{d.name}: PASS words {len(A)} segments {len(tr)} ~{mins:.0f} min speech")


def status(book):
    for f in sorted(ED.joinpath(book, "manuscript").glob("chapter-*.md")):
        n = int(f.stem.split("-")[1]); d = chdir(book, n)
        st = [x for x in ("raw_segs.json", "spec.json", "direction.json", "direction.ready", "published") if (d / x).exists()]
        print(f"ch{n:02d}", " ".join(st) or "-")


if __name__ == "__main__":
    cmd, book, *rest = sys.argv[1:]
    {"segment": segment, "build": build, "verify": verify}.get(cmd, lambda b, *r: status(b))(book, *rest)
