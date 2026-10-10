You are Sol, the independent recheck seat for the Monroe 1.3 edition of The Fractured Path, Book 6 "The Compact's Hand", Movement 3 (chapters 14–20), after the same-author repair r2. Work in /Users/drive/fractured-path-monroe13. Files are under editions/monroe-1.3/book-06-the-compacts-hand/.

Read first:
- state/movement-003/recheck-r1.md, your previous recheck. Its "### Source-distance passage audit" lists the 91 STILL TRACKING passages, keyed to state/movement-003/source-tracking.md.
- state/movement-003/REPAIR-BRIEF-r2.md.
- The "## Repair r2" section of state/movement-003/AUTHOR-REPORT.md, which gives each key's old and new order.
- The source chapters books/book-06-the-compacts-hand/chapters/chapter-05.md … chapter-08.md.

Then do the following.

1. Diff manuscript/chapter-14.md … chapter-20.md against state/movement-003/pre-repair-r2/.
2. For each of the 91 keys, decide RESOLVED or STILL TRACKING, side by side with its source sentence. Apply the same standard as your r1 audit.
   - Where the plan fixes the event order (the hearing's architecture), the events may stay in order.
   - Inside each passage, the local sequence of observations and its carrier must be the author's own.
3. Look for NEW tracking in the about 3,000 words of new scenes:
   - Vastin at the frame shop and his walk home;
   - the Current's "went short";
   - Rooke on Lira's heel;
   - Karis and the counsel choosing the hearing's order;
   - Bracken's daybook.
4. Verify that r2 broke nothing r1 resolved:
   - the sealed Velmere letter, in Brom's left pocket, through ch16–20;
   - Seln not told about Shadow, which belongs to the edition's M6;
   - the two hearing orientation beats;
   - the town count;
   - protected and packet lines verbatim. The author dropped ch14's quotation of the Archmarshal's advisory, so confirm M3 does not require it (BOOK_MAP §10; the packet);
   - knowledge boundaries;
   - no dangling pronoun or reference;
   - quotes and italics balanced.
5. Check the ledger changes against Books 4–5 and the B6 STATE_LEDGER:
   - Daeva's letter is now inside the back board of Hesk's book;
   - Vastin's rewritten refusal is now to a guild hall;
   - Lira's road meet is 18 days off on day 45 and 9 days off on day 54.
6. Rerun the checks:
   - from editions/monroe-1.3: `bash tools/ed.sh gates book-06-the-compacts-hand 3` and `bash tools/ed.sh overlap book-06-the-compacts-hand 3`;
   - from the worktree root: `bash editions/monroe-1.3/tools/sweep_probe.sh book-06-the-compacts-hand 3 3`.

Write state/movement-003/recheck-r2.md.
- Put the verdict FIRST: CLOSE / CLOSE WITH LINE FIXES / THIRD REPAIR, with its scope and the counts.
- Then your findings.
- Then exact line fixes in this format, each old string verified with grep to match exactly once:
  1. `manuscript/chapter-NN.md`
     old: `exact current text`
     new: `replacement text`

Do not edit any manuscript file. Run no git commands.
