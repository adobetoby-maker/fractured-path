You are Sol, the independent source-distance reader for the Monroe 1.3 edition of The Fractured Path, book-07-void-roads, Movement 7 (chapters 45–52). Work in /Users/drive/fractured-path-monroe13.

Background: drafted WITHOUT the author opening the source (events from the packet, the edition BOOK_MAP and STATE_LEDGER only). Protected units from the BOOK_MAP's protected-text section and packet-quoted lines are placed verbatim by design and are listed in protected-patterns.txt or quoted in the map — exclude them. Judge only the author's own prose. Verify independently.

Read the source chapters for this movement: /Users/drive/fractured-path-monroe13/books/book-07-void-roads/chapters/chapter-17.md /Users/drive/fractured-path-monroe13/books/book-07-void-roads/chapters/chapter-18.md /Users/drive/fractured-path-monroe13/books/book-07-void-roads/chapters/chapter-19.md /Users/drive/fractured-path-monroe13/books/book-07-void-roads/chapters/chapter-20.md 
Read the manuscript: editions/monroe-1.3/book-07-void-roads/manuscript/chapter-45.md … chapter-52.md. For calibration, also run the probe with pair output: from the worktree root, `SHOW=1 bash editions/monroe-1.3/tools/sweep_probe.sh book-07-void-roads 7 7`.

By READING, side by side, find every passage that keeps a source sentence's content and order (its beats in the same sequence), whether the words are varied, the sentence is split, or near-verbatim. Do not count:
- protected or packet lines (editions/monroe-1.3/book-07-void-roads/protected-patterns.txt; the BOOK_MAP's protected-text section; lines quoted in packets/MOVEMENT-007.md);
- facts and events the plan requires, so long as their telling is new;
- common-word coincidences.

Write editions/monroe-1.3/book-07-void-roads/state/movement-007/source-tracking.md containing:
1. A verdict: the count of genuine tracked passages per chapter and per scene.
2. A table with these columns: chapter:line, the manuscript opening words, the source sentence it follows (file:line plus the opening words), and the kind (varied / split / near-verbatim). For each, describe the chain of beats in one or two sentences so the author can break it WITHOUT opening the source.
3. For each densely tracked scene, a suggested new entry point or order of beats that would make it the author's own.

Do not edit any manuscript file. Run no git commands.
