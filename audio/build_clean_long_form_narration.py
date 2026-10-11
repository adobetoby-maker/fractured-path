#!/usr/bin/env python3
"""Build deterministic, direction-free long-form narration packages."""

from __future__ import annotations

import argparse
import json
import re
from datetime import datetime, timezone
from pathlib import Path

from build_local_breeze_directors_cut import (
    AUTHOR,
    BOOKS,
    canonical_commit_for,
    git_value,
    make_epub,
    paragraphize,
    parse_chapter,
    sha256_bytes,
    sha256_file,
    spoken_tokens,
)


EDITION = "Clean Long-Form Narration Edition"
OUTPUT_DIR = "clean-long-form-narration"
OUTPUT_STEM = "Clean-Long-Form-Narration"


def expected_hashes(book_root: Path) -> dict[str, str]:
    result: dict[str, str] = {}
    for line in (book_root / "HASHES.sha256").read_text(encoding="utf-8").splitlines():
        digest, filename = line.split(maxsplit=1)
        result[filename] = digest
    return result


def build_book(repo: Path, book_id: str) -> dict:
    config = BOOKS[book_id]
    title = config["title"]
    book_root = repo / "editions" / "monroe-1.3" / book_id
    manuscript = book_root / "manuscript"
    output = book_root / "editions" / OUTPUT_DIR
    output.mkdir(parents=True, exist_ok=True)
    bound = expected_hashes(book_root)
    source_hashes: dict[str, str] = {}
    chapters: list[dict] = []
    full_text_parts = [
        f"{title} — {EDITION}",
        AUTHOR,
        "",
        "Prepared for long-form audiobook upload. Direction-free; no SSML.",
        "",
    ]
    totals = {"words": 0, "spoken_characters": 0}

    for number in range(1, config["chapter_count"] + 1):
        filename = f"chapter-{number:02d}.md"
        source_path = manuscript / filename
        source_bytes = source_path.read_bytes()
        source_hash = sha256_bytes(source_bytes)
        if bound.get(filename) != source_hash:
            raise RuntimeError(f"Hash binding failed for {filename}")
        chapter_title, scenes = parse_chapter(source_bytes.decode("utf-8"))
        prose = "\n\n".join(scenes)
        rendered = "\n\n".join(paragraph for scene in scenes for paragraph in paragraphize(scene))
        if spoken_tokens(prose) != spoken_tokens(rendered):
            raise RuntimeError(f"Word lock failed for {filename}")
        if re.search(r"<(?:speak|break)\b", rendered, re.I):
            raise RuntimeError(f"SSML found in {filename}")
        if "[" in rendered or "]" in rendered:
            raise RuntimeError(f"Square brackets remain in {filename}")
        source_hashes[f"chapter-{number:02d}"] = source_hash
        full_text_parts.extend([chapter_title, "", rendered, ""])
        totals["words"] += len(spoken_tokens(prose))
        totals["spoken_characters"] += len(prose)
        chapters.append({
            "number": number,
            "title": chapter_title,
            "blocks": [
                {"type": "prose", "text": paragraph}
                for scene in scenes
                for paragraph in paragraphize(scene)
            ],
        })

    stem = re.sub(r"[^A-Za-z0-9]+", "-", title).strip("-")
    text_path = output / f"{stem}-{OUTPUT_STEM}.txt"
    epub_path = output / f"{stem}-{OUTPUT_STEM}.epub"
    text_path.write_text("\n".join(full_text_parts).rstrip() + "\n", encoding="utf-8")
    clean_text = text_path.read_text(encoding="utf-8")
    if re.search(r"(?m)^\s*\[[^\n]+\]\s*$", clean_text):
        raise RuntimeError("Director direction line found in clean output")
    if re.search(r"<(?:speak|break)\b", clean_text, re.I):
        raise RuntimeError("SSML found in clean output")

    commit = canonical_commit_for(repo, book_id)
    commit_time = datetime.fromisoformat(
        git_value(repo, "show", "-s", "--format=%cI", commit)
    ).astimezone(timezone.utc)
    make_epub(
        epub_path,
        book_id,
        title,
        chapters,
        commit_time.strftime("%Y-%m-%dT%H:%M:%SZ"),
        edition=EDITION,
    )

    local_manifest_path = book_root / "editions" / "eleven-v4-directors-cut" / "manifest.json"
    local_manifest = json.loads(local_manifest_path.read_text(encoding="utf-8"))
    manifest = {
        "schema_version": 2,
        "book_id": book_id,
        "title": title,
        "author": AUTHOR,
        "edition": EDITION,
        "intended_use": "ElevenLabs Audio Editor / Studio and other literal long-form readers",
        "literal_long_form_upload": True,
        "derived_from": {
            "edition": local_manifest["edition"],
            "canonical_commit": commit,
            "epub_sha256": local_manifest["outputs"]["epub"]["sha256"],
            "plain_text_sha256": local_manifest["outputs"]["plain_text"]["sha256"],
        },
        "source_chapter_sha256": source_hashes,
        "chapter_count": config["chapter_count"],
        "spoken_word_count": totals["words"],
        "spoken_character_count": totals["spoken_characters"],
        "input_character_count": len(clean_text),
        "upload_character_count": len(clean_text),
        "direction_tag_count": 0,
        "ssml": False,
        "word_lock": "verified for all chapters",
        "transformation": "Removed presentation-only Markdown and visual LitRPG square brackets while preserving their spoken words; no prose was rewritten and no performance directions or SSML were added.",
        "outputs": {
            "epub": {
                "file": epub_path.name,
                "sha256": sha256_file(epub_path),
                "bytes": epub_path.stat().st_size,
            },
            "plain_text": {
                "file": text_path.name,
                "sha256": sha256_file(text_path),
                "bytes": text_path.stat().st_size,
            },
        },
    }
    (output / "manifest.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    return {
        "book_id": book_id,
        "chapters": config["chapter_count"],
        "spoken_words": totals["words"],
        "upload_characters": len(clean_text),
        "epub_sha256": manifest["outputs"]["epub"]["sha256"],
        "plain_text_sha256": manifest["outputs"]["plain_text"]["sha256"],
        "word_lock": manifest["word_lock"],
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("book_ids", nargs="*", choices=sorted(BOOKS))
    parser.add_argument("--repo", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    books = args.book_ids or list(BOOKS)
    print(json.dumps([build_book(args.repo.resolve(), book_id) for book_id in books], indent=2))


if __name__ == "__main__":
    main()
