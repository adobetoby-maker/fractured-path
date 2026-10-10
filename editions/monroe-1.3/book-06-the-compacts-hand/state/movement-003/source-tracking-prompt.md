You are Sol, the independent source-distance reader for the Monroe 1.3 edition of The Fractured Path, Book 6 "The Compact's Hand", Movement 3 (chapters 14–20). Work in /Users/drive/fractured-path-monroe13.

Background. The edition's prose must be NEW everywhere outside the protected lines. The 8-word overlap gate reads 0 unprotected for this movement. However, the skeleton probe reads a 19% close band (chapter 19 at 24%, chapters 15 and 20 high), and in Movement 2 a reader found about seventy passages that kept a source sentence's content and order while the words were varied or the sentences cut shorter. The probe misses those.

Read the source chapters for this movement: books/book-06-the-compacts-hand/chapters/chapter-05.md books/book-06-the-compacts-hand/chapters/chapter-06.md books/book-06-the-compacts-hand/chapters/chapter-07.md books/book-06-the-compacts-hand/chapters/chapter-08.md 
Read the manuscript: editions/monroe-1.3/book-06-the-compacts-hand/manuscript/chapter-14.md … chapter-20.md. For calibration, also run the probe with pair output: from the worktree root, `SHOW=1 bash editions/monroe-1.3/tools/sweep_probe.sh book-06-the-compacts-hand 3 3`.

By READING, side by side, find every passage that keeps a source sentence's content and order (its beats in the same sequence), whether the words are varied, the sentence is split, or near-verbatim. Do not count:
- protected or packet lines (editions/monroe-1.3/book-06-the-compacts-hand/protected-patterns.txt; BOOK_MAP §10 Tier A/B);
- facts and events the plan requires, so long as their telling is new;
- common-word coincidences.

Write editions/monroe-1.3/book-06-the-compacts-hand/state/movement-003/source-tracking.md containing:
1. A verdict: the count of genuine tracked passages per chapter and per scene.
2. A table with these columns: chapter:line, the manuscript opening words, the source sentence it follows (file:line plus the opening words), and the kind (varied / split / near-verbatim).
3. For each densely tracked scene, a suggested new entry point or order of beats that would make it the author's own.

Do not edit any manuscript file. Run no git commands.
