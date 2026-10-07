#!/usr/bin/env python3
"""Publish one Local Breeze Director's Cut audition to fractured-path (main, Git LFS).

usage: fp_publish.py BOOK N
Writes audio/<EDITION_ID>/local-breeze-directors-cut/chapter-NN.mp3 (64 kbps mono) and the
chapter's separate render entry in audio/manifest.json,
commits ONLY those two paths (other people's uncommitted files are left alone), pushes main.
Labeled exactly as the Meridian Breeze renders are (owner decision #34).
"""
import datetime, hashlib, json, subprocess, sys, time
from pathlib import Path

REPO = Path("/Users/drive/fractured-path")
RUN = Path("/Users/drive/.local/share/monroe-tts/fractured-directors-run")
ED = Path(__file__).resolve().parents[1]
BOOKS = {"book-01-the-shattered": ("fractured-path-monroe-1.3-book-01", "The Shattered (Monroe 1.3 edition)", 60)}


def git(*a, check=True):
    return subprocess.run(["git", *a], cwd=REPO, check=check, capture_output=True, text=True)


def main():
    book, n = sys.argv[1], int(sys.argv[2])
    eid, etitle, total = BOOKS[book]
    d = RUN / f"{book}-ch{n:02d}"
    wav = d / f"{d.name}.breeze-directed.wav"
    src = (ED / book / "manuscript" / f"chapter-{n:02d}.md").read_bytes()
    title = src.decode().splitlines()[0].lstrip("# ").strip()
    rel = f"audio/{eid}/local-breeze-directors-cut/chapter-{n:02d}.mp3"
    mp3 = REPO / rel
    mp3.parent.mkdir(parents=True, exist_ok=True)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(wav), "-ac", "1", "-c:a", "libmp3lame", "-b:a", "64k",
                    str(mp3)], check=True)
    data = mp3.read_bytes()
    dur = float(subprocess.check_output(["ffprobe", "-v", "error", "-show_entries", "format=duration",
                                         "-of", "csv=p=0", str(mp3)]))
    render = {
        "render": "local-breeze-directors-cut-audition",
        "engine": "Local Breeze TTS 2 8-bit MLX (mlx-community/Breeze-TTS-2-mlx-8bit)",
        "voice": "Original Calder clone · Local Breeze Director's Cut",
        "methodId": "breeze-tts2-original-calder-local-directors-cut",
        "finishState": "objective-qa-and-owner-listening-pending",
        "file": rel, "bytes": len(data), "durationSec": round(dur, 2), "sha256": hashlib.sha256(data).hexdigest(),
        "sourceSha256": hashlib.sha256(src).hexdigest(),
        "url": f"https://media.githubusercontent.com/media/adobetoby-maker/fractured-path/main/{rel}",
        "note": ("Listening audition · research/non-commercial licence · objective QA and owner listening pending. "
                 "Standalone square-bracket directions were parsed into the following segment's instruct field and "
                 "were never sent as spoken text. This audition is not production-approved or Finished.")}
    for attempt in range(1, 7):
        git("pull", "--ff-only", "-q", "origin", "main")
        manp = REPO / "audio/manifest.json"
        m = json.loads(manp.read_text())
        b = next((x for x in m["books"] if x["id"] == eid), None)
        if b is None:
            b = {"id": eid, "title": etitle, "edition": "monroe-1.3", "totalChapters": total, "renderedChapters": 0,
                 "chapters": []}
            m["books"].append(b)
        ch = next((c for c in b["chapters"] if c["number"] == n), None)
        if ch is None:
            ch = {"number": n, "title": title,
                  "manuscript": f"books/fractured-path-monroe-1.3/book-01/manuscript/chapter-{n:02d}.md", "renders": []}
            b["chapters"].append(ch); b["chapters"].sort(key=lambda c: c["number"])
        ch["title"] = title
        ch["renders"] = [render] + [
            r for r in ch["renders"] if r["render"] != "local-breeze-directors-cut-audition"
        ]
        b["renderedChapters"] = sum(1 for c in b["chapters"] if c["renders"])
        m["generated"] = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
        manp.write_text(json.dumps(m, indent=2, ensure_ascii=False) + "\n")
        git("add", rel, "audio/manifest.json")
        git("commit", "-q", "-m", f"Add {etitle} chapter {n} Local Breeze Director's Cut audition\n\n"
            "Listening audition only; objective QA and owner listening remain pending.\n\n"
            "Breeze licence is research/non-commercial.", "--", rel, "audio/manifest.json")
        p = git("push", "origin", "main", check=False)
        if p.returncode == 0:
            (d / "published").write_text(f"{datetime.datetime.now().isoformat()} {render['sha256']}\n")
            print(f"published {eid} chapter {n} ({dur/60:.1f} min, {len(data)/1e6:.1f} MB) on attempt {attempt}")
            return
        print(f"push rejected (attempt {attempt}): {p.stderr[-200:]}")
        git("reset", "--soft", "HEAD~1"); git("restore", "--staged", rel, "audio/manifest.json")
        git("checkout", "--", "audio/manifest.json")
        time.sleep(10 * attempt)
    sys.exit(3)


if __name__ == "__main__":
    main()
