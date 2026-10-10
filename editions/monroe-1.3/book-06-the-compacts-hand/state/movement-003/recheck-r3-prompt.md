You are Sol, the independent recheck seat for the Monroe 1.3 edition of The Fractured Path, Book 6 "The Compact's Hand", Movement 3 (chapters 14–20), after the narrow same-author repair r3. Work in /Users/drive/fractured-path-monroe13. Files are under editions/monroe-1.3/book-06-the-compacts-hand/.

Your r2 recheck (state/movement-003/recheck-r2.md) left 10 STILL TRACKING units: 14:19, 14:139, 14:169, 17:230, 18:55, 19:191, 19:213, 20:193, 20:195, 20:293. The "## Repair r3" section of state/movement-003/AUTHOR-REPORT.md says how each source chain was broken.

1. For each of the 10 units, read the current text side by side with its source sentence (books/book-06-the-compacts-hand/chapters/chapter-05.md … chapter-08.md) and decide RESOLVED or STILL TRACKING. Use the r2 standard: the source's internal chain must not survive under new words.
2. Check the seams around each changed unit:
   - no dangling pronoun or reference;
   - no fact that later text still depends on has been removed. In particular, check whether anything in ch20 or later relies on the dropped couriers or "four towns by tonight", on the eighteen months in 19:191, or on the old assessor in 14:169;
   - quotes and italics are balanced.
3. Confirm nothing that r1–r2 protected has regressed:
   - the sealed Velmere letter in Brom's left pocket;
   - Seln not told;
   - the two hearing orientation beats;
   - the town count in ch15;
   - the ch19 Hesk three-line answer;
   - protected lines verbatim.
4. Rerun the checks:
   - from editions/monroe-1.3: `bash tools/ed.sh gates book-06-the-compacts-hand 3` and `bash tools/ed.sh overlap book-06-the-compacts-hand 3`;
   - from the root: `bash editions/monroe-1.3/tools/sweep_probe.sh book-06-the-compacts-hand 3 3`.

Write state/movement-003/recheck-r3.md:
- verdict FIRST: CLOSE / CLOSE WITH LINE FIXES / FURTHER REPAIR (with counts);
- then findings;
- then exact line fixes in this format, with each old string verified by grep to match once:
  1. `manuscript/chapter-NN.md`
     old: `exact current text`
     new: `replacement text`

Do not edit any manuscript file. Run no git commands.
