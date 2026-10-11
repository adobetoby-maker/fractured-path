You are Sol, the independent source-distance reader for the Monroe 1.3 edition of The Fractured Path, Book 6 "The Compact's Hand", Movement 5 (chapters 28–34). Work in /Users/drive/fractured-path-monroe13.

Background: the 8-word overlap gate reads 0 unprotected and the probe 1% skeleton / 10% close. This movement was drafted WITHOUT the author ever opening the source chapters (events from the packet and BOOK_MAP spine only) — the first movement drafted that way. M3 and M4 first drafts had 136 and 85 tracked passages. The author notes ch33 scenes 1–3 and ch32 scene 1 probe 15–19% close and asks that a reader with the source look there. Verify independently.

Read the source chapters for this movement: books/book-06-the-compacts-hand/chapters/chapter-12.md books/book-06-the-compacts-hand/chapters/chapter-13.md books/book-06-the-compacts-hand/chapters/chapter-14.md 
Read the manuscript: editions/monroe-1.3/book-06-the-compacts-hand/manuscript/chapter-28.md … chapter-34.md. For calibration, also run the probe with pair output: from the worktree root, `SHOW=1 bash editions/monroe-1.3/tools/sweep_probe.sh book-06-the-compacts-hand 5 5`.

By READING, side by side, find every passage that keeps a source sentence's content and order (its beats in the same sequence), whether the words are varied, the sentence is split, or near-verbatim. Do not count:
- protected or packet lines (editions/monroe-1.3/book-06-the-compacts-hand/protected-patterns.txt; BOOK_MAP §10 Tier A/B);
- facts and events the plan requires, so long as their telling is new;
- common-word coincidences.

Write editions/monroe-1.3/book-06-the-compacts-hand/state/movement-005/source-tracking.md containing:
1. A verdict: the count of genuine tracked passages per chapter and per scene.
2. A table with these columns: chapter:line, the manuscript opening words, the source sentence it follows (file:line plus the opening words), and the kind (varied / split / near-verbatim).
3. For each densely tracked scene, a suggested new entry point or order of beats that would make it the author's own.

Do not edit any manuscript file. Run no git commands.
