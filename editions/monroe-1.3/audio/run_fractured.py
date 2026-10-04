#!/usr/bin/env python3
"""Unattended Fractured Path (Monroe 1.3) Breeze pipeline. Queues BEHIND the Meridian run (another session):
it does not start a render while run_meridian.py or any breeze_render_track.py is alive.
For each chapter with direction.ready and no `published` marker, in chapter order: render (retrying GPU
watchdog crashes), then fp_publish.py. Resumable — segment WAVs are checkpoints.

usage: run_fractured.py BOOK [BOOK ...]
"""
import datetime, subprocess, sys, time
from pathlib import Path

RUN = Path("/Users/drive/.local/share/monroe-tts/fractured-run")
PY = Path("/Users/drive/.local/share/monroe-tts/breeze/venv/bin/python")
RENDER = Path("/Users/drive/.local/share/monroe-tts/meridian-run/breeze_render_track.py")
PUB = Path(__file__).resolve().parent / "fp_publish.py"
LOG = RUN / "pipeline.log"


def log(msg):
    line = f"{datetime.datetime.now():%m-%d %H:%M:%S} {msg}"
    print(line, flush=True)
    with LOG.open("a") as f:
        f.write(line + "\n")


def busy():
    for pat in ("run_meridian.py", "breeze_render_track.py"):
        if subprocess.run(["pgrep", "-f", pat], capture_output=True).returncode == 0:
            return True
    return False


def main(books):
    log(f"runner start: {books}")
    while True:
        todo = [d for b in books for d in sorted(RUN.glob(f"{b}-ch*")) if not (d / "published").exists()]
        if not todo:
            log("all chapters published"); return
        ready = [d for d in todo if (d / "direction.ready").exists()]
        if not ready or busy():
            time.sleep(120); continue
        d = ready[0]
        book, n = d.name.rsplit("-ch", 1)
        wav = d / f"{d.name}.breeze-directed.wav"
        for attempt in range(1, 9):
            if wav.exists():
                break
            log(f"{d.name}: render attempt {attempt}")
            r = subprocess.run([str(PY), str(RENDER), str(d), "directed"], capture_output=True, text=True)
            (d / "render.log").write_text(r.stdout[-4000:] + "\n" + r.stderr[-4000:])
            if r.returncode != 0:
                log(f"{d.name}: render failed rc={r.returncode}; retrying in 90s"); time.sleep(90)
        if not wav.exists():
            log(f"{d.name}: giving up after retries"); (d / "direction.ready").rename(d / "direction.ready.failed")
            continue
        p = subprocess.run([sys.executable, str(PUB), book, n], capture_output=True, text=True)
        log(f"{d.name}: publish rc={p.returncode} {p.stdout.strip()[-200:]} {p.stderr.strip()[-200:]}")
        if p.returncode != 0:
            time.sleep(300)


if __name__ == "__main__":
    main(sys.argv[1:] or ["book-01-the-shattered"])
