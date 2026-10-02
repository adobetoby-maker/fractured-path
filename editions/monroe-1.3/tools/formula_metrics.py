#!/usr/bin/env python3
"""Reproducible formula metrics for the Monroe 1.3 / O'Connor 1.3 edition.

Measures what FORMULA_REVIEW.md asks for that can be counted without judgment.
POV share and development beats need a reader and are NOT measured here.

usage: formula_metrics.py CHAPTER.md [CHAPTER.md ...] [--json]

Method (publish with every report so runs compare):
- Text: markdown H1 line and lines that are only '---' / '***' / '* * *' are
  stripped; '*' and '_' emphasis markers removed; fenced code blocks (system
  notices) excluded from sentence/readability stats but counted as words.
- Paragraph: a non-empty line separated by blank lines (one paragraph per line
  in this repo). Dialogue lines count as paragraphs.
- Scene break: a line that is exactly '---', '***', '* * *' or '#'. Chapter
  boundaries are not counted as scene breaks.
- Sentence: split on [.!?] followed by whitespace + an opening quote/capital,
  or end of paragraph; ellipses and common abbreviations (Mr. Mrs. Dr. St.)
  are protected. Em-dash interruptions do not end a sentence.
- Syllables: vowel-group heuristic with silent-e and -le adjustments; proper
  nouns are estimated the same way (they can bias Flesch slightly).
- Flesch Reading Ease = 206.835 - 1.015*(words/sentences) - 84.6*(syll/words)
- Flesch-Kincaid grade = 0.39*(words/sentences) + 11.8*(syll/words) - 15.59
Targets (research/ironprince-craft-formula.md §2, §3, §8): sentence mean 14.6,
median 11; paragraph median ~18 / mean ~26.8 (ASR proxy, directional);
~950 words per scene, ~8.7 scene breaks per 10k words (ASR proxy, directional);
Flesch RE 72.3, FK grade 6.8.
"""
import json, re, statistics, sys
from pathlib import Path

BREAK = re.compile(r"^\s*(---|\*\*\*|\* \* \*|#)\s*$")
ABBR = re.compile(r"\b(Mr|Mrs|Ms|Dr|St|Mt)\.")
SPLIT = re.compile(r"(?<=[.!?])[\"'”’)]*\s+(?=[\"'“‘(]?[A-Z0-9])")


def syllables(word: str) -> int:
    w = re.sub(r"[^a-z]", "", word.lower())
    if not w:
        return 0
    if len(w) <= 3:
        return 1
    w = re.sub(r"(?:[^laeiouy]es|ed|[^laeiouy]e)$", "", w)
    w = re.sub(r"^y", "", w)
    groups = re.findall(r"[aeiouy]{1,2}", w)
    n = len(groups)
    if word.lower().endswith("le") and len(word) > 2 and word.lower()[-3] not in "aeiouy":
        n += 1
    return max(1, n)


def words_of(text: str):
    return re.findall(r"[A-Za-z0-9][A-Za-z0-9'’\-]*", text)


def analyse(paths):
    paras, sentences, total_words, breaks, fenced_words = [], [], 0, 0, 0
    syll = 0
    for p in paths:
        in_fence = False
        for raw in Path(p).read_text(encoding="utf-8").splitlines():
            line = raw.rstrip()
            if line.strip().startswith("```"):
                in_fence = not in_fence
                continue
            if in_fence:
                fenced_words += len(words_of(line))
                continue
            if not line.strip() or line.lstrip().startswith("# ") and not BREAK.match(line):
                continue
            if BREAK.match(line):
                breaks += 1
                continue
            text = re.sub(r"[*_]", "", line).strip()
            ws = words_of(text)
            if not ws:
                continue
            paras.append(len(ws))
            total_words += len(ws)
            syll += sum(syllables(w) for w in ws)
            protected = ABBR.sub(lambda m: m.group(1) + "<DOT>", text).replace("...", "<ELL>").replace("…", "<ELL>")
            for s in SPLIT.split(protected):
                n = len(words_of(s))
                if n:
                    sentences.append(n)
    total_all = total_words + fenced_words
    sc = len(sentences) or 1
    wps = total_words / sc
    spw = syll / (total_words or 1)
    scenes = breaks + len(paths)
    return {
        "chapters": len(paths),
        "words_total": total_all,
        "words_prose": total_words,
        "words_in_system_notices": fenced_words,
        "sentences": len(sentences),
        "sentence_mean": round(statistics.fmean(sentences), 2) if sentences else None,
        "sentence_median": statistics.median(sentences) if sentences else None,
        "sentence_sd_pop": round(statistics.pstdev(sentences), 2) if sentences else None,
        "share_le5_words": round(sum(1 for s in sentences if s <= 5) / sc, 3),
        "share_ge40_words": round(sum(1 for s in sentences if s >= 40) / sc, 3),
        "paragraphs": len(paras),
        "paragraph_mean": round(statistics.fmean(paras), 2) if paras else None,
        "paragraph_median": statistics.median(paras) if paras else None,
        "scene_breaks_marked": breaks,
        "scene_breaks_per_10k": round(breaks / (total_all or 1) * 10000, 2),
        "words_per_scene": round(total_all / scenes, 1),
        "flesch_reading_ease": round(206.835 - 1.015 * wps - 84.6 * spw, 1),
        "flesch_kincaid_grade": round(0.39 * wps + 11.8 * spw - 15.59, 2),
        "method": "editions/monroe-1.3/tools/formula_metrics.py (see module docstring)",
        "targets": {"sentence_mean": 14.6, "sentence_median": 11, "paragraph_median_asr": 18,
                    "paragraph_mean_asr": 26.8, "words_per_scene_asr": 950,
                    "scene_breaks_per_10k_asr": 8.7, "flesch_reading_ease": 72.3,
                    "flesch_kincaid_grade": 6.8},
    }


if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if a != "--json"]
    if not args:
        sys.exit(__doc__)
    r = analyse(args)
    if "--json" in sys.argv:
        print(json.dumps(r, indent=2))
    else:
        for k, v in r.items():
            if k != "targets":
                t = r["targets"].get(k.replace("words_per_scene", "words_per_scene_asr"))
                print(f"{k:28} {v}" + (f"   (target {t})" if t is not None else ""))
