#!/usr/bin/env python3
"""Render one chapter of The Shattered in Jason Keiller's voice.

Different engine path from the Boundary books, and the difference matters.
Those go through higgsfield's MCP, which exposes no request stitching -- every
chunk comes back as a fresh roll of the delivery register, so that pipeline has
to measure each chunk and pull it back to the chapter median afterwards
(assemble_fixed.py). Here we call ElevenLabs directly, which accepts
previous_request_ids, so the engine carries prosody across the seam itself.
Correcting drift after the fact is strictly worse than not creating it.

No EQ or pitch chain. The Boundary chain (highpass 85, notch 140, +0.5st) exists
to fix a specific low-frequency throb in Holden's delivery. Keiller is a
different voice and chapters 1-3 shipped clean; applying someone else's
correction would be an unforced error.

  python3 render_chapter.py <n>          # renders + assembles chapter n (book 1)
  python3 render_chapter.py <n> --dry    # chunk only, no API calls
  python3 render_chapter.py <n> --book book-02-iron-circuit   # target a different book
"""
import hashlib, json, os, re, ssl, subprocess, sys, time, urllib.error, urllib.request

VOICE = "powBJzjz7VpBtyzNZUJy"          # Jason Keiller - Audience Pleaser
MODEL = "eleven_multilingual_v2"
SEED  = 20260827
MAX_CHARS = 1800     # measured on the Boundary books: reads tighter than 4000
                     # with half the >=0.8s pauses, and the extra seam is
                     # inaudible -- doubly so here, where stitching hides it
BITRATE = 64         # one mono voice; 128 buys nothing but radio time
STITCH = 3           # ElevenLabs accepts at most 3 previous_request_ids
SR = 44100

# QUOTA POLICY (author decision, 2026-08-30): do NOT probe the balance before
# rendering. Just start. Chunk failures are clean (no partial chapters are ever
# assembled), so running dry mid-book costs nothing but a resume later. The
# "oversized-probe" trick is banned: it reads the balance for free ONLY when
# quota is low enough to reject it -- with healthy quota it renders the filler
# and charges for it. If balance visibility is ever needed, fix the key scope
# (user_read) instead of burning renders to ask.

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BOOK = "book-01-the-shattered"
if "--book" in sys.argv:
    BOOK = sys.argv[sys.argv.index("--book") + 1]
BOOK_AUDIO_DIR = {
    "book-01-the-shattered": "book-01-the-shattered",
    "book-02-iron-circuit": "book-02-iron-circuit",
}.get(BOOK, BOOK)
CHAPTERS = os.path.join(ROOT, f"books/{BOOK}/chapters")
OUT = os.path.join(ROOT, f"audio/{BOOK_AUDIO_DIR}")
WORK = "/tmp/fp_render"

# Two baselines, because the method changed mid-book.
#   8,791 w/hr -- chapters 1-3, rendered WITHOUT request stitching. Stable to
#     within 0.5% across the three.
#   9,836 w/hr -- chapters 4-6, stitched. Measured 9994 / 9815 / 9700.
# The ~12% gap is the stitching itself: an unstitched chunk cold-starts with a
# settling cadence, a stitched one continues a sentence it can already hear.
# The gate compares against the stitched figure because everything from ch4 on
# is stitched. A chapter far off THIS is the dropped-text signal.
WPH = 9836


def chunk(text):
    """Split on paragraph boundaries only. A mid-paragraph split puts a hard
    stop where the prose has none, and that seam is audible even with stitching."""
    out, cur = [], ""
    for p in (p.strip() for p in text.split("\n\n")):
        if not p:
            continue
        cand = (cur + "\n\n" + p).strip()
        if len(cand) > MAX_CHARS and cur:
            out.append(cur); cur = p
        else:
            cur = cand
    if cur:
        out.append(cur)
    return out


def prep(n):
    path = os.path.join(CHAPTERS, f"chapter-{n:02d}.md")
    t = open(path).read()
    t = re.sub(r"^#\s*Chapter\s*(\d+)\s*[—–:-]?\s*(.*)$",
               lambda m: f"Chapter {int(m.group(1))}. {m.group(2).strip()}.", t,
               count=1, flags=re.M)
    t = re.sub(r"^#{1,6}\s*", "", t, flags=re.M)          # strip heading marks
    t = re.sub(r"(\*\*|\*|`|_)", "", t)                   # strip emphasis marks
    t = re.sub(r"(?m)^\s*[-–—]{3,}\s*$", "", t)           # rules
    # Every chapter file ends with an authoring line like
    #   *End of Chapter 4 — approximately 4,460 words*
    # Chapter 1's shipped audio ends on real prose, so the original pipeline
    # dropped it. Stripping emphasis marks (above) turns it into ordinary text,
    # and it WILL be narrated -- caught in the ch4 pilot, where the take ended
    # "End of chapter 4. Approximately 4,160 words."
    t = re.sub(r"(?im)^\s*end of chapter\b.*$", "", t)
    t = re.sub(r"(?im)^\s*\(?word count[:\s].*$", "", t)
    t = re.sub(r"\n{3,}", "\n\n", t).strip()
    return t, chunk(t)


def say(text, prev_ids, next_text, dest):
    """One chunk. previous_request_ids is what keeps chunk N+1 sounding like
    chunk N; next_text lets the engine shape the final cadence toward what
    actually follows instead of trailing off into a full stop."""
    body = {"text": text, "model_id": MODEL, "seed": SEED,
            "voice_settings": {"stability": 0.5, "similarity_boost": 0.75,
                               "style": 0.0, "speed": 1.0}}
    if prev_ids:
        body["previous_request_ids"] = prev_ids[-STITCH:]
    if next_text:
        body["next_text"] = next_text[:400]
    req = urllib.request.Request(
        f"https://api.elevenlabs.io/v1/text-to-speech/{VOICE}?output_format=mp3_44100_128",
        data=json.dumps(body).encode(),
        headers={"xi-api-key": os.environ["ELEVEN_API_KEY"],
                 "Content-Type": "application/json"})
    for attempt in range(4):
        try:
            with urllib.request.urlopen(req, context=ssl.create_default_context()) as r:
                open(dest, "wb").write(r.read())
                return r.headers.get("request-id")
        except urllib.error.HTTPError as e:
            if e.code in (429, 500, 502, 503) and attempt < 3:
                time.sleep(5 * (attempt + 1)); continue
            sys.exit(f"  chunk failed HTTP {e.code}: {e.read()[:300]}")


def declick(src, dst):
    """ElevenLabs leaves a ~30ms click on the tail of every take. Reverse, trim
    the head (which is the real tail), fade, reverse back. Done per chunk before
    joining -- a click at a seam is far more audible than one at a chapter end."""
    subprocess.run(["ffmpeg", "-hide_banner", "-loglevel", "error", "-i", src,
                    "-ac", "1", "-ar", str(SR), "-af",
                    "areverse,atrim=start=0.030,asetpts=N/SR/TB,"
                    "afade=t=in:st=0:d=0.060,areverse",
                    "-c:a", "pcm_s16le", dst, "-y"], check=True)


def dur(f):
    return float(subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration",
         "-of", "default=nw=1:nk=1", f], capture_output=True, text=True).stdout)


def main():
    n = int(sys.argv[1]); dry = "--dry" in sys.argv
    text, chunks = prep(n)
    words = len(text.split())
    print(f"  ch{n:02d}: {words:,} words, {len(chunks)} chunks, "
          f"{sum(len(c) for c in chunks):,} chars")
    print(f"  expected ~{words/WPH*60:.1f} min at this narrator's measured rate")
    if dry:
        for i, c in enumerate(chunks, 1):
            print(f"    {i:02d} {len(c):>5}ch  {c[:60].splitlines()[0]}...")
        return

    d = os.path.join(WORK, f"ch{n:02d}"); os.makedirs(d, exist_ok=True)
    ids, wavs = [], []
    for i, c in enumerate(chunks, 1):
        nxt = chunks[i] if i < len(chunks) else None
        raw = os.path.join(d, f"{i:02d}_raw.mp3")
        wav = os.path.join(d, f"{i:02d}.wav")
        rid = say(c, ids, nxt, raw)
        if rid:
            ids.append(rid)
        declick(raw, wav)
        wavs.append(wav)
        print(f"    {i:02d}/{len(chunks)}  {dur(wav):6.1f}s  stitch={len(ids[-STITCH:])}")

    lst = os.path.join(d, "list.txt")
    open(lst, "w").write("".join(f"file '{w}'\n" for w in wavs))
    joined = os.path.join(d, "joined.wav")
    subprocess.run(["ffmpeg", "-v", "error", "-f", "concat", "-safe", "0",
                    "-i", lst, "-c", "copy", joined, "-y"], check=True)
    out = os.path.join(OUT, f"chapter-{n:02d}.mp3")
    subprocess.run(["ffmpeg", "-v", "error", "-i", joined, "-c:a", "libmp3lame",
                    "-b:a", f"{BITRATE}k", out, "-y"], check=True)

    d_s = dur(out); rate = words / (d_s / 3600)
    dev = (rate - WPH) / WPH * 100
    flag = "  <-- OFF BASELINE, check for dropped text" if abs(dev) > 8 else ""
    print(f"\n  wrote {out}")
    print(f"  {os.path.getsize(out)/1e6:.1f} MB  {d_s/60:.1f} min  "
          f"{rate:.0f} w/hr ({dev:+.1f}% vs baseline){flag}")


if __name__ == "__main__":
    main()
