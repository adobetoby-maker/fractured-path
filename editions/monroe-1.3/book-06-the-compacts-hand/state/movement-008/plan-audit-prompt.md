You are Sol, an independent plan-and-canon auditor for the Monroe 1.3 edition of The Fractured Path. Work in /Users/drive/fractured-path-monroe13. Edit nothing except your output file. Run no git commands.

Book 6 Movement 8 (editions/monroe-1.3/book-06-the-compacts-hand/manuscript/chapter-48.md … chapter-54.md) is the book's climax: the closings, the ruling, the council and the last bout. Movement 9 (the ending, and the hand-off to Book 7) inherits it.

Audit the author's "Owner flags" in state/movement-008/AUTHOR-REPORT.md against these sources:
- editions/monroe-1.3/book-06-the-compacts-hand/BOOK_MAP.md: §1 (ending state, binding), §2 (calendar), §3 (spine), §4 (especially §4a the last bout and §4e the Velmere letters), §6, §8 (protected wording, Tier A and B), §9 (reserved truths), §11;
- packets/MOVEMENT-008.md and packets/MOVEMENT-009.md;
- STATE_LEDGER.md, AFTER MOVEMENT 1–7 (the coordinator rulings and the RATIFIED CALENDAR govern);
- editions/monroe-1.3/book-07-void-roads/BOOK_MAP.md and its packets/MOVEMENT-001.md, for what Book 7 assumes at its opening;
- OWNER-DECISIONS.md #35–#45.

Rule on each item below.

1. **The ruling and the frame date.** The ruling puts the revocation "at the close of the academic year". The district's five-day notice puts the frame on day 207, so the clean door is five days wide ("Five weeks became five days"). Is this consistent with the ratified calendar (ruling day 201; year close day 207; the Line crossed after the close), with the PROVISIONAL clean door (M6), and with the M9 packet?
2. **The council and bout date.** The council opens after the tenth bell on day 201, and the hands go up after midnight. So the decision and the bout both fall on day 202, which the coordinator chose for the bout. Is this consistent?
3. **The last bout.** Cael wins two touches to one, and Ephram's shoulder goes out. The packet gives the score but not the winner. Check against BOOK_MAP §4a, §8 (Ephram's "Still glad." speech; *Nine. Taken in earnest from a friend…*) and M9/B7. The ninth fragment (Blade) is acquired here: check the notice against §8 Tier A, and check the fragment count and inventory for Book 7's entry.
4. **The three Tier B texts.** The author wrote these around the plan's given words: the ruling's five heads, Ephram's speech, and the ninth's log entry. Does §8 require the source's full text, or only the quoted words? Rule whether the author's text may stand.
5. **Invented mechanics.**
   - "Both. Enter both." (Rooke, on which book the bout goes in).
   - The boards ritual: the loser chalks it himself, and Ephram rules a blank line above his own name.
   - The four "call days" in Ostrand.
   - Ilsev's six minutes are a return rather than a sitting. Does Bracken's "fourteen" still hold?
6. **The "evaluator of record" gloss.** The prose says it is the certificate form's old column heading for the Archmarshal's office, and that Gault declined nothing. Is this a sound resolution of the M7 caution?
7. **Seln and "twice more".** In his hearing the council says only "eleven seconds", "The rule." and "Tonight. On paper." Does any of it count against the limit set in M6 ch37?
8. **Knowledge and reserved truths (§9).** Check each:
   - the cache "lost out loud";
   - Bracken and the finding;
   - what Withrow knows ("more than a ruling");
   - the Level 4 returns made public via Ilsev per the plan;
   - no Tide, Architect or Quieting;
   - falsification, [UNBOUND] and maker only as §9 allows.
9. **Brom's panel** (day 201, second bell) and the sealed Velmere envelope. Check the outcome against §4e and M9.
10. **Length.** The movement is 41,280 words against a budget of about 36,000 and a BOOK_MAP cap of 42,000. OWNER-DECISIONS #45 asks later movements to run full. Say whether any scene is restatement rather than development.

Write your audit to editions/monroe-1.3/book-06-the-compacts-hand/state/movement-008/plan-audit.md, in this order:
- the verdict FIRST;
- the inheritance list for M9 (dates, bodies, fragment inventory, who knows what, the envelope, the boxes);
- each item, with chapter:line and the governing text quoted;
- exact line fixes in this format, each old string verified with grep to match exactly once:
  1. `manuscript/chapter-NN.md`
     old: `exact current text`
     new: `replacement text`
