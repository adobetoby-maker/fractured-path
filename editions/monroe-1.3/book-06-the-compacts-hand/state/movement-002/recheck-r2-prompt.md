You are Sol, the independent recheck seat for the Monroe 1.3 edition of The Fractured Path, Book 6 "The Compact's Hand", Movement 2 (chapters 8–13), after the same-author repair r2. Work in /Users/drive/fractured-path-monroe13. Files are under editions/monroe-1.3/book-06-the-compacts-hand/.

Read first:
- state/movement-002/recheck-r1.md, the previous recheck. Its "### Priority 2: PARTIAL" section tables the 18 passages that still kept a source sentence's content and order, with their source sentences.
- state/movement-002/REPAIR-BRIEF-r2.md.
- state/movement-002/AUTHOR-REPORT.md, the "## Repair r2" section.
- state/movement-002/EVENT-LIST.md.
- The source chapters for this movement, books/book-06-the-compacts-hand/chapters/chapter-03.md and chapter-04.md under the worktree root. Locate them with find if the path differs.

Then:
1. Diff manuscript/chapter-08.md … chapter-13.md against state/movement-002/pre-repair-r2/.
2. For each of the 18 passages, decide RESOLVED or STILL TRACKING. Quote the new text and the source sentence side by side. Re-composition means a new entry point and a new order of beats; synonym-swapped or chopped-up source sentences do not count.
3. Spot-check the rest of the changed text for any new source-tracking.
4. Check that the r2 changes broke nothing the r1 recheck verified:
   - continuity against Books 4–5;
   - the lane measure and the ch12 trial;
   - protected and packet lines verbatim (see protected-patterns.txt and BOOK_MAP §10);
   - knowledge boundaries: no falsification, [UNBOUND], maker or Tide, and Seln not told why Shadow is sealed;
   - no dangling pronoun or reference; quotes and italics balanced.
5. Rerun from editions/monroe-1.3: `bash tools/ed.sh gates book-06-the-compacts-hand 2` and `bash tools/ed.sh overlap book-06-the-compacts-hand 2`. Rerun from the worktree root: `bash editions/monroe-1.3/tools/sweep_probe.sh book-06-the-compacts-hand 2 2`.

Write state/movement-002/recheck-r2.md with the verdict FIRST (CLOSE / CLOSE WITH LINE FIXES / THIRD REPAIR, with scope), then your findings, then exact line fixes in exactly this format. Verify each old string with grep to match exactly once:
1. `manuscript/chapter-NN.md`
   old: `exact current text`
   new: `replacement text`

Do not edit any manuscript file. Run no git commands.
