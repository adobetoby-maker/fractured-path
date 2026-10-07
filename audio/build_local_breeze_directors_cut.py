#!/usr/bin/env python3
"""Build deterministic, word-locked Local Breeze Director's Cut packages."""

from __future__ import annotations

import argparse
import hashlib
import html
import json
import re
import subprocess
import zipfile
from datetime import datetime, timezone
from pathlib import Path


AUTHOR = "Monroe Jackson"
EDITION = "Local Breeze Director's Cut"
# Keep the original public filenames and directory for compatibility with already
# published links. The manifest and README identify the actual local-only use.
COMPATIBILITY_STEM = "Eleven-v4-Directors-Cut"

BOOKS = {
    "book-01-the-shattered": {
        "title": "The Shattered",
        "chapter_count": 60,
        "movement_ranges": [(1, 6), (7, 13), (14, 20), (21, 27), (28, 33), (34, 40), (41, 47), (48, 53), (54, 60)],
        "movement_tags": [
            "[Quiet, observant narration; keep the domestic warmth and approaching dread restrained]",
            "[Wary, grounded narration; let the unfamiliar district open a detail at a time]",
            "[Focused, analytical narration; make every lesson and useful loss legible]",
            "[Measured, quietly confident narration; let competence arrive without swagger]",
            "[Dry, precise narration; hold institutional pressure beneath the ordinary details]",
            "[Patient, methodical narration; give training, failure, and discovery room to accumulate]",
            "[Taut, clear narration; sharpen the danger without rushing the thinking]",
            "[Restrained, watchful narration; keep the evaluation pressure close and human]",
            "[Building, spatially clear narration; earn the public confrontation and let its consequences land]",
        ],
    },
    "book-03-no-path-given": {
        "title": "No Path Given",
        "chapter_count": 61,
        "movement_ranges": [(1, 8), (9, 16), (17, 23), (24, 31), (32, 39), (40, 46), (47, 53), (54, 61)],
        "movement_tags": [
            "[Quiet, precise narration; restrained institutional pressure and careful new beginnings]",
            "[Curious, analytical narration; keep consent, records, and trust sharply distinct]",
            "[Measured, public-facing narration; let each challenge expose character as well as skill]",
            "[Patient, lucid narration; make repeated failure feel cumulative rather than repetitive]",
            "[Taut, spatially clear narration; build the directed match without sacrificing comprehension]",
            "[Dry, controlled narration; let legal pressure tighten through exact language]",
            "[Hushed, deliberate narration; treat the documents war with the focus of a duel]",
            "[Firm, lucid narration; carry the hearing with conviction, then let the daylight settle]",
        ],
    },
    "book-04-copper-crown": {
        "title": "Copper Crown",
        "chapter_count": 62,
        "movement_ranges": [(1, 7), (8, 14), (15, 21), (22, 29), (30, 37), (38, 44), (45, 50), (51, 56), (57, 62)],
        "movement_tags": [
            "[Quiet, exact narration; let consequence and new responsibility settle before momentum returns]",
            "[Observant, controlled narration; keep status, leverage, and friendship legible beneath the travel]",
            "[Focused, analytical narration; make each tactical choice feel earned rather than announced]",
            "[Measured, public-facing narration; hold the spectacle at a human scale]",
            "[Patient, strategic narration; let alliances and costs accumulate without melodrama]",
            "[Dry, precise narration; sharpen the institutional pressure through exact detail]",
            "[Taut, spatially clear narration; keep danger readable and thought moving under pressure]",
            "[Restrained, intimate narration; give loyalty and doubt room to register]",
            "[Building, lucid narration; earn the crown's weight and let the final consequences land]",
        ],
    },
    "book-05-the-silver-standard": {
        "title": "The Silver Standard",
        "chapter_count": 60,
        "movement_ranges": [(1, 6), (7, 13), (14, 19), (20, 26), (27, 32), (33, 39), (40, 46), (47, 53), (54, 60)],
        "movement_tags": [
            "[Quiet, purposeful narration; carry the earlier cost into the new campaign without recapping it]",
            "[Observant, public-facing narration; let reputation alter each room before anyone speaks]",
            "[Focused, analytical narration; keep the standard, the system, and the human stakes distinct]",
            "[Measured, competitive narration; make pressure cumulative and every adjustment legible]",
            "[Patient, strategic narration; allow trust and rivalry to change by degrees]",
            "[Dry, precise narration; let institutional language reveal the trap without overplaying it]",
            "[Taut, spatially clear narration; keep the contest fast in consequence, not in delivery]",
            "[Restrained, intimate narration; hold fear and loyalty close to the characters]",
            "[Firm, lucid narration; build through the final standard and let the aftermath breathe]",
        ],
    },
}

SCENE_RULES = [
    (re.compile(r"\b(registry|warden|compact|statute|clause|file|record|ledger|petition|hearing|provision|office|form|notation)\b", re.I),
     "[Dry, precise narration; keep the institutional language clear and the pressure understated]"),
    (re.compile(r"\b(fight|bout|strike|stance|guard|blade|floor|yard|drill|spar|exchange|hit|fell|blood)\b", re.I),
     "[Taut, spatially clear narration; controlled urgency, never rushed]"),
    (re.compile(r"\b(fragment|arbiter|notice|shattered|unbound|wind|pressure|compression|ember|iron|tide|path)\b", re.I),
     "[Focused, lucid narration; give the system detail and the character's inference equal weight]"),
    (re.compile(r"\b(hesk|lira|brom|karis|grandfather|letter|home|family|friend|smile|laughed|laugh)\b", re.I),
     "[Warm, intimate narration; hold the feeling lightly and let the relationship carry it]"),
    (re.compile(r"\b(road|gate|market|district|hill|room|bench|archive|school|greyvane|ardenmere)\b", re.I),
     "[Steady, observant narration; let place, distance, and social position register]"),
]


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha256_file(path: Path) -> str:
    return sha256_bytes(path.read_bytes())


def git_value(root: Path, *args: str) -> str:
    return subprocess.check_output(["git", *args], cwd=root, text=True).strip()


def clean_spoken_markdown(text: str) -> str:
    """Remove presentation-only Markdown while preserving every spoken token."""
    text = re.sub(r"(?m)^#{1,6}\s+", "", text)
    text = re.sub(r"(?<!\\)[*_`]", "", text)
    text = text.replace(r"\*", "*").replace(r"\_", "_").replace(r"\`", "`")
    # Square brackets are visual LitRPG punctuation in canonical prose. Breeze
    # reserves standalone bracket lines for instructions, so preserve the words
    # but remove only the visual brackets.
    return re.sub(r"\[([^\[\]\n]+)\]", r"\1", text)


def spoken_tokens(text: str) -> list[str]:
    return re.findall(r"[\w’'-]+", text.casefold(), flags=re.UNICODE)


def parse_chapter(source: str) -> tuple[str, list[str]]:
    lines = source.replace("\r\n", "\n").splitlines()
    if not lines or not lines[0].startswith("# "):
        raise ValueError("Chapter is missing its level-one title")
    title = clean_spoken_markdown(lines[0][2:].strip())
    body = "\n".join(lines[1:]).strip()
    scenes = [clean_spoken_markdown(part.strip()) for part in re.split(r"(?m)^---\s*$", body)]
    scenes = [scene for scene in scenes if scene]
    if not scenes:
        raise ValueError(f"{title} has no prose")
    return title, scenes


def movement_for(number: int, ranges: list[tuple[int, int]]) -> int:
    for index, (start, end) in enumerate(ranges):
        if start <= number <= end:
            return index
    raise ValueError(f"Chapter {number} is outside the configured movement ranges")


def chapter_opening_tag(number: int, config: dict) -> str:
    return config["movement_tags"][movement_for(number, config["movement_ranges"])]


def scene_tag(scene: str, number: int, index: int, count: int, config: dict) -> str:
    sample = " ".join(scene.split())[:1200]
    for pattern, tag in SCENE_RULES:
        if pattern.search(sample):
            return tag
    if index == count - 1:
        if number >= config["chapter_count"] - 2:
            return "[Quietly reflective narration; let the final realization settle without announcing it]"
        return "[Measured narration; allow the scene to resolve before moving on]"
    return chapter_opening_tag(number, config)


def paragraphize(scene: str) -> list[str]:
    return [part.strip() for part in re.split(r"\n\s*\n", scene) if part.strip()]


def build_directed_chapter(number: int, title: str, scenes: list[str], config: dict) -> tuple[str, list[dict[str, str]]]:
    opening = chapter_opening_tag(number, config)
    blocks = [title, "", opening, ""]
    epub_blocks = [{"type": "direction", "text": opening}]
    for index, scene in enumerate(scenes):
        if index:
            tag = scene_tag(scene, number, index, len(scenes), config)
            blocks.extend([tag, ""])
            epub_blocks.append({"type": "direction", "text": tag})
        for paragraph in paragraphize(scene):
            blocks.extend([paragraph, ""])
            epub_blocks.append({"type": "prose", "text": paragraph})
    return "\n".join(blocks).rstrip() + "\n", epub_blocks


def xhtml_document(title: str, blocks: list[dict[str, str]]) -> str:
    rendered = "\n".join(
        f'      <p class="{block["type"]}">{html.escape(block["text"])}</p>' for block in blocks
    )
    return f'''<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" lang="en" xml:lang="en">
  <head><meta charset="utf-8" /><title>{html.escape(title)}</title><link rel="stylesheet" type="text/css" href="../styles/book.css" /></head>
  <body><section class="chapter"><h1>{html.escape(title)}</h1>
{rendered}
  </section></body>
</html>
'''


def make_epub(path: Path, book_id: str, title: str, chapters: list[dict], modified: str) -> None:
    nav_items = "\n".join(
        f'          <li><a href="text/chapter-{chapter["number"]:02d}.xhtml">{html.escape(chapter["title"])}</a></li>'
        for chapter in chapters
    )
    manifest_items = [
        '<item id="nav" href="nav.xhtml" media-type="application/xhtml+xml" properties="nav"/>',
        '<item id="css" href="styles/book.css" media-type="text/css"/>',
    ]
    spine_items = []
    for chapter in chapters:
        number = chapter["number"]
        manifest_items.append(f'<item id="chapter-{number:02d}" href="text/chapter-{number:02d}.xhtml" media-type="application/xhtml+xml"/>')
        spine_items.append(f'<itemref idref="chapter-{number:02d}"/>')
    opf = f'''<?xml version="1.0" encoding="utf-8"?>
<package xmlns="http://www.idpf.org/2007/opf" version="3.0" unique-identifier="book-id">
  <metadata xmlns:dc="http://purl.org/dc/elements/1.1/"><dc:identifier id="book-id">urn:uuid:{book_id}-local-breeze-directors-cut</dc:identifier><dc:title>{html.escape(title)} — {EDITION}</dc:title><dc:creator>{AUTHOR}</dc:creator><dc:language>en</dc:language><meta property="dcterms:modified">{modified}</meta></metadata>
  <manifest>{"".join(manifest_items)}</manifest><spine>{"".join(spine_items)}</spine>
</package>
'''
    nav = f'''<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE html><html xmlns="http://www.w3.org/1999/xhtml" xmlns:epub="http://www.idpf.org/2007/ops" lang="en"><head><meta charset="utf-8"/><title>Contents</title></head><body><nav epub:type="toc"><h1>Contents</h1><ol>{nav_items}</ol></nav></body></html>
'''
    container = '''<?xml version="1.0" encoding="UTF-8"?>
<container version="1.0" xmlns="urn:oasis:names:tc:opendocument:xmlns:container"><rootfiles><rootfile full-path="EPUB/content.opf" media-type="application/oebps-package+xml"/></rootfiles></container>
'''
    css = "body{font-family:serif;line-height:1.5;margin:5%}h1{page-break-before:always;text-align:center;margin:2em 0}p{margin:0 0 .9em}.direction{font-family:sans-serif;font-style:italic;color:#555;margin:1.5em 0 .8em}"
    timestamp = datetime.strptime(modified, "%Y-%m-%dT%H:%M:%SZ").timetuple()[:6]

    def write(archive: zipfile.ZipFile, name: str, data: str | bytes, stored: bool = False) -> None:
        info = zipfile.ZipInfo(name, date_time=timestamp)
        info.compress_type = zipfile.ZIP_STORED if stored else zipfile.ZIP_DEFLATED
        info.external_attr = 0o644 << 16
        archive.writestr(info, data)

    with zipfile.ZipFile(path, "w") as archive:
        write(archive, "mimetype", "application/epub+zip", stored=True)
        write(archive, "META-INF/container.xml", container)
        write(archive, "EPUB/content.opf", opf)
        write(archive, "EPUB/nav.xhtml", nav)
        write(archive, "EPUB/styles/book.css", css)
        for chapter in chapters:
            write(archive, f'EPUB/text/chapter-{chapter["number"]:02d}.xhtml', xhtml_document(chapter["title"], chapter["blocks"]))


def build_book(repo: Path, book_id: str) -> dict:
    config = BOOKS[book_id]
    title = config["title"]
    manuscript = repo / "editions" / "monroe-1.3" / book_id / "manuscript"
    output = repo / "editions" / "monroe-1.3" / book_id / "editions" / "eleven-v4-directors-cut"
    chapter_output = output / "chapters"
    chapter_output.mkdir(parents=True, exist_ok=True)
    full_text_parts = [
        f"{title} — {EDITION}", AUTHOR, "",
        "Prepared for local Breeze TTS 2 direction parsing; never upload this marked file to a literal long-form reader.",
        "Standalone square-bracket lines are performance instructions and must not be spoken. No SSML.", "",
    ]
    records = []
    totals = {"words": 0, "spoken_characters": 0, "input_characters": 0, "directions": 0}
    for number in range(1, config["chapter_count"] + 1):
        source_path = manuscript / f"chapter-{number:02d}.md"
        source_bytes = source_path.read_bytes()
        chapter_title, scenes = parse_chapter(source_bytes.decode("utf-8"))
        directed, blocks = build_directed_chapter(number, chapter_title, scenes, config)
        canonical_spoken = "\n\n".join(scenes)
        prose_only = "\n".join(line for index, line in enumerate(directed.splitlines()) if index > 0 and not re.fullmatch(r"\[[^\n]+\]", line.strip()))
        canonical_tokens = spoken_tokens(canonical_spoken)
        if canonical_tokens != spoken_tokens(prose_only):
            raise RuntimeError(f"Word lock failed for {source_path.name}")
        if re.search(r"<(?:speak|break)\b", directed, re.I):
            raise RuntimeError(f"SSML found in {source_path.name}")
        for line in directed.splitlines():
            if ("[" in line or "]" in line) and not re.fullmatch(r"\[[^\n]+\]", line.strip()):
                raise RuntimeError(f"Ambiguous square brackets in {source_path.name}: {line}")
        chapter_path = chapter_output / f"chapter-{number:02d}.txt"
        chapter_path.write_text(directed, encoding="utf-8")
        directions = sum(block["type"] == "direction" for block in blocks)
        totals["words"] += len(canonical_tokens)
        totals["spoken_characters"] += len(canonical_spoken)
        totals["input_characters"] += len(directed)
        totals["directions"] += directions
        full_text_parts.extend([directed.rstrip(), ""])
        records.append({
            "number": number,
            "title": chapter_title,
            "source": str(source_path.relative_to(repo)),
            "source_sha256": sha256_bytes(source_bytes),
            "directed_file": str(chapter_path.relative_to(repo)),
            "directed_sha256": sha256_file(chapter_path),
            "spoken_word_count": len(canonical_tokens),
            "spoken_character_count": len(canonical_spoken),
            "input_character_count": len(directed),
            "scene_count": len(scenes),
            "direction_tag_count": directions,
            "word_lock": "verified",
            "blocks": blocks,
        })
    stem = re.sub(r"[^A-Za-z0-9]+", "-", title).strip("-")
    text_path = output / f"{stem}-{COMPATIBILITY_STEM}.txt"
    epub_path = output / f"{stem}-{COMPATIBILITY_STEM}.epub"
    text_path.write_text("\n".join(full_text_parts).rstrip() + "\n", encoding="utf-8")
    commit = git_value(repo, "rev-parse", "HEAD")
    commit_time = datetime.fromisoformat(git_value(repo, "show", "-s", "--format=%cI", commit)).astimezone(timezone.utc)
    make_epub(epub_path, book_id, title, records, commit_time.strftime("%Y-%m-%dT%H:%M:%SZ"))
    manifest_records = [{key: value for key, value in record.items() if key != "blocks"} for record in records]
    manifest = {
        "schema_version": 2,
        "book_id": book_id,
        "title": title,
        "author": AUTHOR,
        "edition": EDITION,
        "intended_use": "Local Breeze TTS 2 evaluation with direction lines parsed into the subsequent segment's instruct field",
        "literal_long_form_upload": False,
        "direction_words_spoken": False,
        "artifact_compatibility_name": COMPATIBILITY_STEM,
        "canonical_commit": commit,
        "generated_at": commit_time.isoformat(),
        "chapter_count": config["chapter_count"],
        "spoken_word_count": totals["words"],
        "spoken_character_count": totals["spoken_characters"],
        "input_character_count": totals["input_characters"],
        "upload_character_count": totals["input_characters"],
        "direction_tag_count": totals["directions"],
        "word_lock": "verified for all chapters",
        "ssml": False,
        "outputs": {
            "epub": {"file": epub_path.name, "sha256": sha256_file(epub_path), "bytes": epub_path.stat().st_size},
            "plain_text": {"file": text_path.name, "sha256": sha256_file(text_path), "bytes": text_path.stat().st_size},
        },
        "chapters": manifest_records,
    }
    (output / "manifest.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    (output / "README.md").write_text(
        f"# {title} — {EDITION}\n\n"
        "This is the word-locked, marked local Breeze package. Standalone square-bracket lines are performance directions. The Breeze runner must attach each direction to the following segment's `instruct` field and must never send the direction words as spoken text. There is no SSML.\n\n"
        "Do not upload this package to ElevenLabs Studio or any literal long-form reader. Use the separate Clean Long-Form Narration package for those tools. Canonical source and directed-output hashes are recorded in `manifest.json`.\n",
        encoding="utf-8",
    )
    return {
        "book_id": book_id,
        "chapters": config["chapter_count"],
        "spoken_words": totals["words"],
        "input_characters": totals["input_characters"],
        "direction_tags": totals["directions"],
        "epub_sha256": manifest["outputs"]["epub"]["sha256"],
        "word_lock": manifest["word_lock"],
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("book_ids", nargs="*", choices=sorted(BOOKS))
    parser.add_argument("--repo", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    books = args.book_ids or list(BOOKS)
    results = [build_book(args.repo.resolve(), book_id) for book_id in books]
    print(json.dumps(results, indent=2))


if __name__ == "__main__":
    main()
