You are Sol, the independent source-distance reader for the Monroe 1.3 edition of The Fractured Path, Book 6 "The Compact's Hand", Movement 4 (chapters 21–27). Work in /Users/drive/fractured-path-monroe13.

Background: the 8-word overlap gate reads 0 unprotected for this movement and the skeleton probe reads 1% skeleton / 13% close. In Movement 3 a side-by-side read found 136 tracked passages that the probe missed; this movement was drafted under a stricter method (source read once, then closed; per-chapter self-check), and the author reports rebuilding flagged passages in ch22, ch26 and ch27. Verify independently.

Read the source chapters for this movement: books/book-06-the-compacts-hand/chapters/chapter-09.md books/book-06-the-compacts-hand/chapters/chapter-10.md books/book-06-the-compacts-hand/chapters/chapter-11.md 
Read the manuscript: editions/monroe-1.3/book-06-the-compacts-hand/manuscript/chapter-21.md … chapter-27.md. For calibration, also run the probe with pair output: from the worktree root, `SHOW=1 bash editions/monroe-1.3/tools/sweep_probe.sh book-06-the-compacts-hand 4 4`.

By READING, side by side, find every passage that keeps a source sentence's content and order (its beats in the same sequence), whether the words are varied, the sentence is split, or near-verbatim. Do not count:
- protected or packet lines (editions/monroe-1.3/book-06-the-compacts-hand/protected-patterns.txt; BOOK_MAP §10 Tier A/B);
- facts and events the plan requires, so long as their telling is new;
- common-word coincidences.

Write editions/monroe-1.3/book-06-the-compacts-hand/state/movement-004/source-tracking.md containing:
1. A verdict: the count of genuine tracked passages per chapter and per scene.
2. A table with these columns: chapter:line, the manuscript opening words, the source sentence it follows (file:line plus the opening words), and the kind (varied / split / near-verbatim).
3. For each densely tracked scene, a suggested new entry point or order of beats that would make it the author's own.

Do not edit any manuscript file. Run no git commands.
