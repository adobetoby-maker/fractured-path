#!/usr/bin/env python3
"""Prepare word-locked Breeze tracks from the marked Local Director's Cut.

Standalone square-bracket direction paragraphs are metadata: each becomes the
``instruct`` value of the next spoken segment and is never included in ``text``.
The marked prose is checked against the canonical manuscript before a ready
marker is written.

usage: prepare_breeze_directors.py BOOK [CHAPTER ...]
"""

from __future__ import annotations

import hashlib
import json
import math
import re
import sys
from pathlib import Path


EDITION = Path(__file__).resolve().parents[1]
RUN = Path("/Users/drive/.local/share/monroe-tts/fractured-directors-run")
LIMIT = 700
BASE_INSTRUCT = (
    "Original Calder: grounded, restrained Australian-English narration at native pace; "
    "speak only the supplied prose."
)
BOOKS = {
    "book-01-the-shattered": "eleven-v4-directors-cut",
    "book-03-no-path-given": "eleven-v4-directors-cut",
}


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def clean_markdown(raw: str) -> str:
    text = raw.replace("\r\n", "\n").replace("\r", "\n")
    text = re.sub(r"\A---\n.*?\n---\n", "", text, flags=re.S)
    text = re.sub(r"\n---\s*\n(?:\*?End of Chapter.*)?\Z", "", text, flags=re.I | re.S)
    text = re.sub(r"^#{1,6}\s+", "", text, flags=re.M)
    text = re.sub(r"^\s*(?:---+|\*\*\*+|___+)\s*$", "", text, flags=re.M)
    text = text.replace("```", "")
    text = re.sub(r"!\[([^]]*)\]\([^)]+\)", r"\1", text)
    text = re.sub(r"\[([^]]+)\]\([^)]+\)", r"\1", text)
    # The published narration packages intentionally remove only the visual
    # square-bracket shell around LitRPG/system copy so those canonical words
    # are spoken.  Normalize that approved presentation change for word-lock.
    text = re.sub(r"\[([^\[\]\n]+)\]", r"\1", text)
    # A few manuscripts italicize only a plural suffix (for example
    # ``gone*s*``), so emphasis markers may be surrounded by word characters.
    text = text.replace("*", "")
    text = re.sub(r"(?<!\w)_{1,3}|_{1,3}(?!\w)", "", text)
    text = re.sub(r"^\s*>\s?", "", text, flags=re.M)
    text = re.sub(r"^\s*[-+*]\s+", "", text, flags=re.M)
    return re.sub(r"\s+", " ", text).strip()


def split_long(text: str) -> list[str]:
    if len(text) <= LIMIT:
        return [text]
    parts = re.split(r'(?<=[.!?…])\s+|(?<=[.!?…]["”’])\s+', text)
    target = len(text) / math.ceil(len(text) / LIMIT)
    groups: list[str] = []
    current = ""
    for part in parts:
        candidate = f"{current} {part}".strip()
        if current and len(candidate) > max(LIMIT, target * 1.25):
            groups.append(current)
            current = part
        else:
            current = candidate
    if current:
        groups.append(current)
    return groups


def parse_marked(raw: str) -> tuple[list[dict], str]:
    blocks = [block.strip() for block in re.split(r"\n\s*\n", raw) if block.strip()]
    segments: list[dict] = []
    pending_direction: str | None = None
    pending_scene_reset = False
    spoken_blocks: list[str] = []
    for block in blocks:
        direction = re.fullmatch(r"\[([^\n\[\]]+)\]", block)
        if direction:
            pending_direction = direction.group(1).strip()
            pending_scene_reset = True
            if segments:
                segments[-1]["pauseAfterMs"] = 2700
            continue
        prose = " ".join(block.split())
        spoken_blocks.append(prose)
        pieces = split_long(prose)
        for position, piece in enumerate(pieces):
            item = {
                "id": f"s{len(segments) + 1:03d}",
                "speaker": "narrator",
                "text": piece,
                "instruct": BASE_INSTRUCT,
                "pauseAfterMs": 2100 if position + 1 == len(pieces) else 1550,
            }
            if position == 0 and pending_direction:
                item["instruct"] = (
                    f"Original Calder at native pace. {pending_direction}. "
                    "Do not speak this direction; speak only the supplied prose."
                )
                item["directionSource"] = pending_direction
                pending_direction = None
                pending_scene_reset = False
            segments.append(item)
    if pending_direction or pending_scene_reset:
        raise ValueError("marked chapter ends with an unattached direction")
    if not segments:
        raise ValueError("marked chapter contains no spoken prose")
    segments[-1]["pauseAfterMs"] = 2700
    return segments, "\n\n".join(spoken_blocks)


def prepare(book: str, chapter: int) -> Path:
    if book not in BOOKS:
        raise ValueError(f"unsupported book: {book}")
    root = EDITION / book
    marked = root / "editions" / BOOKS[book] / "chapters" / f"chapter-{chapter:02d}.txt"
    source = root / "manuscript" / f"chapter-{chapter:02d}.md"
    if not marked.is_file() or not source.is_file():
        raise FileNotFoundError(f"missing source package for {book} chapter {chapter}")
    segments, spoken = parse_marked(marked.read_text(encoding="utf-8"))
    if clean_markdown(spoken) != clean_markdown(source.read_text(encoding="utf-8")):
        raise ValueError(f"word lock failed for {book} chapter {chapter}")

    directory = RUN / f"{book}-ch{chapter:02d}"
    directory.mkdir(parents=True, exist_ok=True)
    track = {
        "schemaVersion": 1,
        "book": book,
        "chapter": chapter,
        "edition": "Local Breeze Director's Cut audition",
        "engine": "mlx-community/Breeze-TTS-2-mlx-8bit",
        "voice": "Original Calder clone",
        "source": str(source),
        "sourceSha256": digest(source),
        "directorSource": str(marked),
        "directorSourceSha256": digest(marked),
        "directionPolicy": "standalone bracket line attaches to next segment and is never spoken",
        "segments": segments,
    }
    temporary = directory / "direction.json.tmp"
    temporary.write_text(json.dumps(track, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    temporary.replace(directory / "direction.json")
    (directory / "chapter.directed.txt").write_text(marked.read_text(encoding="utf-8"), encoding="utf-8")
    (directory / "direction.ready").write_text(
        json.dumps(
            {
                "sourceSha256": track["sourceSha256"],
                "directorSourceSha256": track["directorSourceSha256"],
                "segmentCount": len(segments),
                "directionCount": sum("directionSource" in item for item in segments),
            },
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )
    return directory


def main() -> int:
    if len(sys.argv) < 2:
        raise SystemExit("usage: prepare_breeze_directors.py BOOK [CHAPTER ...]")
    book = sys.argv[1]
    chapters = [int(value) for value in sys.argv[2:]]
    if not chapters:
        chapters = sorted(
            int(path.stem.split("-")[-1])
            for path in (EDITION / book / "editions" / BOOKS[book] / "chapters").glob("chapter-*.txt")
        )
    for chapter in chapters:
        directory = prepare(book, chapter)
        print(directory)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
