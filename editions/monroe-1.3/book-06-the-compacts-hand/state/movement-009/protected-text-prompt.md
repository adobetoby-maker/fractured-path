You are Sol, the independent protected-wording and plan auditor for the Monroe 1.3 edition of The Fractured Path. Work in /Users/drive/fractured-path-monroe13. Edit nothing except your output file. Run no git commands.

Book 6 Movement 9 (editions/monroe-1.3/book-06-the-compacts-hand/manuscript/chapter-55.md … chapter-60.md) is the book's final movement. Its author drafted WITHOUT opening the source. Wherever BOOK_MAP §8 protects a Tier A/B unit but quotes only a fragment of it, the author left a marker line of the form `[[TIER-B: <unit> — coordinator to supply protected text]]`. There are six markers; find them with grep for `[[TIER`.

Your job has three parts.

**A. Supply the protected text.** For each marker:
1. Locate the unit's full protected wording in the source edition: books/book-06-the-compacts-hand/chapters/chapter-21.md … chapter-24.md. The Book 7 hand-off sentence, if one is needed, is in books/book-07-void-roads/chapters/chapter-01.md.
2. Give an exact fix that replaces the marker line with the full protected text. Format it the way the surrounding manuscript formats such text (italics, a block, or dialogue).
3. Change ONLY what the edition's standing rulings require. Flag every such change explicitly.
   - Season-blind: no season, month or English weekday words.
   - Feet and yards, not metres.
   - Year counts: "since his Kindling" in place of an incremented count.
   - "Two renewals on paper".
   - The registry name *Caelen Hesk-ward* in instruments.
   - Nine fragments.
   - The ratified calendar: day 203 entry; day 207 year close; the Line after it.
   - The edition's names and pronouns.
4. If the two sentences around the marker need a small join change to fit the restored text, give that as a separate fix. The author notes two:
   - the reply to Daeva is called "short" in the next sentence;
   - the personnel query is framed as the house's question to the district office.

**B. Rule on four author flags.**
1. **The closing inventory.** The packet lists it as protected, but §8 gives no text, and the author composed it in the form of ch34's (nine lines and the blank). Does protected source wording exist for it? If yes, supply the fix. If no, ratify the author's version.
2. **The last line of the book.** The Book 7 BOOK_MAP quotes a source sentence that is not in §8 or the packet, and the author wrote their own. What does §1 (the ending, binding) and the Book 7 seam require? Supply a fix if the protected line must be used.
3. **Attributions chosen without the source.**
   - "Nobody's watching." is given to Brom.
   - In the closing exchange, Lira has "Let them escalate…" and Brom has "And better roads."
   - "Both promises ride east with me." is Cael to Lira.

   Check each against the protected wording and the plan. Give fixes where they are wrong.
4. **Calendar.** The Line is crossed on the fifth road day. The first night past it is fireless under the cart. The shelf is the first fire, on the evening of the second day past the Line. Book 7's map calls the shelf "the first camp beyond the Line". Ratify, or give the correction: which side should change, B6 M9 or the B7 plan?

**C. Check the new canon** against BOOK_MAP §9, Book 7's plan, and the Book 9 reservations (search editions/monroe-1.3 and universe/ for them):
- the last Arbiter station, unstaffed four years, its stamp in the waystation keeper's drawer;
- a second Denvash visit, in one clause;
- Seln burning his nineteen bundles of duplicates;
- the file's new line arriving on an unsigned slip of advice;
- the Book 9 plant: a sigil cut in an older, foreign stone the station was built round.

Write your findings to editions/monroe-1.3/book-06-the-compacts-hand/state/movement-009/protected-text.md, in this order:
1. The verdict FIRST.
2. Each item, with the governing text quoted (file:line).
3. Exact fixes, each old string verified with grep to match exactly once (use fixed-string, multi-line matching where needed). Use this format:

N. `manuscript/chapter-NN.md`

   old:

   ```text
   exact current text
   ```

   new:

   ```text
   replacement text
   ```
