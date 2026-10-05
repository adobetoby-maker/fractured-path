#!/usr/bin/env python3
"""Build word-locked Eleven v4 Director's Cut artifacts for frozen Monroe 1.3 books."""

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
EDITION = "Eleven v4 Director's Cut"

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
}

SCENE_RULES = [
    (
        re.compile(r"\b(registry|warden|compact|statute|clause|file|record|ledger|petition|hearing|provision|office|form|notation)\b", re.I),
        "[Dry, precise narration; keep the institutional language clear and the pressure understated]",
    ),
    (
        re.compile(r"\b(fight|bout|strike|stance|guard|blade|floor|yard|drill|spar|exchange|hit|fell|blood)\b", re.I),
        "[Taut, spatially clear narration; controlled urgency, never rushed]",
    ),
    (
        re.compile(r"\b(fragment|arbiter|notice|shattered|unbound|wind|pressure|compression|ember|iron|tide|path)\b", re.I),
        "[Focused, lucid narration; give the system detail and the character's inference equal weight]",
    ),
    (
        re.compile(r"\b(hesk|lira|brom|karis|grandfather|letter|home|family|friend|smile|laughed|laugh)\b", re.I),
        "[Warm, intimate narration; hold the feeling lightly and let the relationship carry it]",
    ),
    (
        re.compile(r"\b(road|gate|market|district|hill|room|bench|archive|school|greyvane|ardenmere)\b", re.I),
        "[Steady, observant narration; let place, distance, and social position register]",
    ),
]


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha256_file(path: Path) -> str:
    return sha256_bytes(path.read_bytes())


def git_value(root: Path, *args: str) -> str:
    return subprocess.check_output(["git", *args], cwd=root, text=True).strip()


def clean_spoken_markdown(text: str) -> str:
    """Remove presentation-only Markdown while preserving spoken words and punctuation."""
    text = re.sub(r"(?m)^#{1,6}\s+", "", text)
    text = re.sub(r"(?<!\\)[*_`]", "", text)
    text = text.replace(r"\*", "*").replace(r"\_", "_").replace(r"\`", "`")
    # LitRPG UI brackets are visual punctuation, but Eleven v4 reserves square brackets
    # for audio direction. Remove only the brackets so names such as SHATTERED and
    # Rooted Stance remain word-for-word identical and are spoken instead of swallowed.
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
    movement = movement_for(number, config["movement_ranges"])
    return config["movement_tags"][movement]


def scene_tag(scene: str, number: int, scene_index: int, scene_count: int, config: dict) -> str:
    sample = " ".join(scene.split())[:1200]
    for pattern, tag in SCENE_RULES:
        if pattern.search(sample):
            return tag
    if scene_index == scene_count - 1:
        if number >= config["chapter_count"] - 2:
            return "[Quietly reflective narration; let the final realization settle without announcing it]"
        return "[Measured narration; allow the scene to resolve before moving on]"
    return chapter_opening_tag(number, config)


def paragraphize(scene: str) -> list[str]:
    return [part.strip() for part in re.split(r"\n\s*\n", scene) if part.strip()]


def build_directed_chapter(number: int, title: str, scenes: list[str], config: dict) -> tuple[str, list[dict[str, str]]]:
    opening = chapter_opening_tag(number, config)
    blocks: list[str] = [title, "", opening, ""]
    epub_blocks: list[dict[str, str]] = [{"type": "direction", "text": opening}]
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
    rendered = []
    for block in blocks:
        cls = "direction" if block["type"] == "direction" else "prose"
        rendered.append(f'      <p class="{cls}">{html.escape(block["text"])}</p>')
    body = "\n".join(rendered)
    return f'''<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" lang="en" xml:lang="en">
  <head>
    <meta charset="utf-8" />
    <title>{html.escape(title)}</title>
    <link rel="stylesheet" type="text/css" href="../styles/book.css" />
  </head>
  <body>
    <section class="chapter">
      <h1>{html.escape(title)}</h1>
{body}
    </section>
  </body>
</html>
'''


def make_epub(
    path: Path,
    book_id: str,
    title: str,
    chapters: list[dict],
    cover: Path | None,
    modified: str,
) -> None:
    identifier = f"urn:uuid:{book_id}-eleven-v4-directors-cut"
    nav_items = "\n".join(
        f'          <li><a href="text/chapter-{chapter["number"]:02d}.xhtml">{html.escape(chapter["title"])}</a></li>'
        for chapter in chapters
    )
    manifest_items = [
        '<item id="nav" href="nav.xhtml" media-type="application/xhtml+xml" properties="nav"/>',
        '<item id="css" href="styles/book.css" media-type="text/css"/>',
    ]
    spine_items = []
    if cover:
        manifest_items.append('<item id="cover" href="images/cover.jpg" media-type="image/jpeg" properties="cover-image"/>')
    for chapter in chapters:
        number = chapter["number"]
        manifest_items.append(
            f'<item id="chapter-{number:02d}" href="text/chapter-{number:02d}.xhtml" media-type="application/xhtml+xml"/>'
        )
        spine_items.append(f'<itemref idref="chapter-{number:02d}"/>')
    opf = f'''<?xml version="1.0" encoding="utf-8"?>
<package xmlns="http://www.idpf.org/2007/opf" version="3.0" unique-identifier="book-id">
  <metadata xmlns:dc="http://purl.org/dc/elements/1.1/">
    <dc:identifier id="book-id">{identifier}</dc:identifier>
    <dc:title>{html.escape(title)} — {EDITION}</dc:title>
    <dc:creator>{AUTHOR}</dc:creator>
    <dc:language>en</dc:language>
    <meta property="dcterms:modified">{modified}</meta>
  </metadata>
  <manifest>
    {"\n    ".join(manifest_items)}
  </manifest>
  <spine>
    {"\n    ".join(spine_items)}
  </spine>
</package>
'''
    nav = f'''<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:epub="http://www.idpf.org/2007/ops" lang="en">
  <head><meta charset="utf-8"/><title>Contents</title></head>
  <body><nav epub:type="toc"><h1>Contents</h1><ol>
{nav_items}
  </ol></nav></body>
</html>
'''
    container = '''<?xml version="1.0" encoding="UTF-8"?>
<container version="1.0" xmlns="urn:oasis:names:tc:opendocument:xmlns:container">
  <rootfiles><rootfile full-path="EPUB/content.opf" media-type="application/oebps-package+xml"/></rootfiles>
</container>
'''
    css = '''body { font-family: serif; line-height: 1.5; margin: 5%; }
h1 { page-break-before: always; text-align: center; margin: 2em 0; }
p { margin: 0 0 0.9em; }
.direction { font-family: sans-serif; font-style: italic; color: #555; margin: 1.5em 0 0.8em; }
'''
    zip_timestamp = datetime.strptime(modified, "%Y-%m-%dT%H:%M:%SZ").timetuple()[:6]

    def write_entry(archive: zipfile.ZipFile, name: str, data: str | bytes, *, stored: bool = False) -> None:
        info = zipfile.ZipInfo(name, date_time=zip_timestamp)
        info.compress_type = zipfile.ZIP_STORED if stored else zipfile.ZIP_DEFLATED
        info.external_attr = 0o644 << 16
        archive.writestr(info, data)

    with zipfile.ZipFile(path, "w") as archive:
        write_entry(archive, "mimetype", "application/epub+zip", stored=True)
        write_entry(archive, "META-INF/container.xml", container)
        write_entry(archive, "EPUB/content.opf", opf)
        write_entry(archive, "EPUB/nav.xhtml", nav)
        write_entry(archive, "EPUB/styles/book.css", css)
        if cover:
            write_entry(archive, "EPUB/images/cover.jpg", cover.read_bytes())
        for chapter in chapters:
            write_entry(
                archive,
                f'EPUB/text/chapter-{chapter["number"]:02d}.xhtml',
                xhtml_document(chapter["title"], chapter["blocks"]),
            )


def build_book(repo: Path, book_id: str, cover: Path | None) -> dict:
    config = BOOKS[book_id]
    title = config["title"]
    manuscript = repo / "editions" / "monroe-1.3" / book_id / "manuscript"
    output = repo / "editions" / "monroe-1.3" / book_id / "editions" / "eleven-v4-directors-cut"
    chapter_output = output / "chapters"
    chapter_output.mkdir(parents=True, exist_ok=True)

    chapter_records = []
    full_text_parts = [
        f"{title} — {EDITION}",
        AUTHOR,
        "",
        "Prepared for ElevenLabs Audio Editor / Studio long-form upload.",
        "Target model: Eleven v4. Inline audio tags; no SSML.",
        "",
    ]
    total_spoken_words = 0
    total_spoken_characters = 0
    total_upload_characters = 0
    total_tags = 0

    for number in range(1, config["chapter_count"] + 1):
        source_path = manuscript / f"chapter-{number:02d}.md"
        source_bytes = source_path.read_bytes()
        title_line, scenes = parse_chapter(source_bytes.decode("utf-8"))
        directed, blocks = build_directed_chapter(number, title_line, scenes, config)

        canonical_spoken = "\n\n".join(scenes)
        directed_without_title_or_tags = "\n".join(
            line for index, line in enumerate(directed.splitlines())
            if index > 0 and not re.fullmatch(r"\[[^\n]+\]", line.strip())
        )
        canonical_tokens = spoken_tokens(canonical_spoken)
        if canonical_tokens != spoken_tokens(directed_without_title_or_tags):
            raise RuntimeError(f"Word lock failed for {source_path.name}")
        if re.search(r"<(?:speak|break)\b", directed, flags=re.I):
            raise RuntimeError(f"SSML found in {source_path.name}")
        for line in directed.splitlines():
            if "[" in line or "]" in line:
                if not re.fullmatch(r"\[[^\n]+\]", line.strip()):
                    raise RuntimeError(f"Ambiguous square brackets found in {source_path.name}: {line}")

        chapter_path = chapter_output / f"chapter-{number:02d}.txt"
        chapter_path.write_text(directed, encoding="utf-8")
        spoken_word_count = len(canonical_tokens)
        spoken_character_count = len(canonical_spoken)
        tag_count = sum(1 for block in blocks if block["type"] == "direction")
        total_spoken_words += spoken_word_count
        total_spoken_characters += spoken_character_count
        total_upload_characters += len(directed)
        total_tags += tag_count
        full_text_parts.extend([directed.rstrip(), ""])
        chapter_records.append(
            {
                "number": number,
                "title": title_line,
                "source": str(source_path.relative_to(repo)),
                "source_sha256": sha256_bytes(source_bytes),
                "directed_file": str(chapter_path.relative_to(repo)),
                "directed_sha256": sha256_file(chapter_path),
                "spoken_word_count": spoken_word_count,
                "spoken_character_count": spoken_character_count,
                "upload_character_count": len(directed),
                "scene_count": len(scenes),
                "direction_tag_count": tag_count,
                "word_lock": "verified",
                "blocks": blocks,
            }
        )

    stem = re.sub(r"[^A-Za-z0-9]+", "-", title).strip("-")
    full_text_path = output / f"{stem}-Eleven-v4-Directors-Cut.txt"
    full_text_path.write_text("\n".join(full_text_parts).rstrip() + "\n", encoding="utf-8")
    epub_path = output / f"{stem}-Eleven-v4-Directors-Cut.epub"
    if cover and not cover.is_file():
        raise FileNotFoundError(cover)
    canonical_commit = git_value(repo, "rev-parse", "HEAD")
    canonical_commit_time = datetime.fromisoformat(
        git_value(repo, "show", "-s", "--format=%cI", canonical_commit)
    ).astimezone(timezone.utc)
    deterministic_timestamp = canonical_commit_time.strftime("%Y-%m-%dT%H:%M:%SZ")
    make_epub(epub_path, book_id, title, chapter_records, cover, deterministic_timestamp)

    manifest_chapters = [{key: value for key, value in record.items() if key != "blocks"} for record in chapter_records]
    manifest = {
        "schema_version": 1,
        "book_id": book_id,
        "title": title,
        "author": AUTHOR,
        "edition": EDITION,
        "target_model": "eleven_v4",
        "format": "full-book long-form upload",
        "canonical_commit": canonical_commit,
        "generated_at": canonical_commit_time.isoformat(),
        "chapter_count": config["chapter_count"],
        "spoken_word_count": total_spoken_words,
        "spoken_character_count": total_spoken_characters,
        "upload_character_count": total_upload_characters,
        "direction_tag_count": total_tags,
        "word_lock": "verified for all chapters",
        "ssml": False,
        "credit_budget_note": "Use the account's generation estimate as authoritative before spending credits; upload character count is recorded for planning only.",
        "outputs": {
            "epub": {"file": epub_path.name, "sha256": sha256_file(epub_path), "bytes": epub_path.stat().st_size},
            "plain_text": {"file": full_text_path.name, "sha256": sha256_file(full_text_path), "bytes": full_text_path.stat().st_size},
        },
        "chapters": manifest_chapters,
    }
    (output / "manifest.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    (output / "README.md").write_text(
        f"# {title} — {EDITION}\n\n"
        "Word-locked long-form upload package for Eleven v4. Direction is expressed with inline square-bracket audio tags; there is no SSML. "
        "The canonical prose is unchanged, and each chapter's source and directed hashes are recorded in `manifest.json`.\n\n"
        "Upload the full EPUB to ElevenLabs Audio Editor / Studio. Confirm the model, voice, and displayed credit estimate before generating. "
        "Do not treat generated audio as production-finished until it passes objective QA and the owner's full listen.\n",
        encoding="utf-8",
    )
    return {
        "book_id": book_id,
        "output": str(output),
        "chapters": config["chapter_count"],
        "spoken_words": total_spoken_words,
        "spoken_characters": total_spoken_characters,
        "upload_characters": total_upload_characters,
        "direction_tags": total_tags,
        "epub_sha256": manifest["outputs"]["epub"]["sha256"],
        "word_lock": manifest["word_lock"],
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("book_id", choices=sorted(BOOKS))
    parser.add_argument("--repo", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--cover", type=Path)
    args = parser.parse_args()
    result = build_book(args.repo.resolve(), args.book_id, args.cover.resolve() if args.cover else None)
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
