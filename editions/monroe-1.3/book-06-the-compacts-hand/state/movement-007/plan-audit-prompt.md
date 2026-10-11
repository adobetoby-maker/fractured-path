You are Sol, an independent plan-and-calendar auditor for the Monroe 1.3 edition of The Fractured Path. Work in /Users/drive/fractured-path-monroe13. Edit nothing except your output file. Run no git commands.

Book 6 Movement 7 (editions/monroe-1.3/book-06-the-compacts-hand/manuscript/chapter-41.md … chapter-47.md) has no source chapter of its own, and its author invented the calendar past day 98. Movement 8 and Movement 9 will inherit it. Audit the author's "Owner flags" (editions/monroe-1.3/book-06-the-compacts-hand/state/movement-007/AUTHOR-REPORT.md) against:
- editions/monroe-1.3/book-06-the-compacts-hand/BOOK_MAP.md — §2 (calendar, binding), §3 (the spine), §4 (expansion, especially §4a the last bout and §4e the Velmere letters), §6, §8 (protected wording, including M8's Tier B minute line) and §9;
- packets/MOVEMENT-008.md and packets/MOVEMENT-009.md, for what they assume about dates and state;
- STATE_LEDGER.md, the AFTER MOVEMENT 1–6 blocks. Coordinator rulings govern. Note Brom's ninety days, the day-71 meet, the day-75 sitting, the day-76 gate, the clean door (day 75 to day 115), and the nine-week inventory clock.

Rule on each item.

1. **The calendar.**
   - Recess: days 99–112.
   - Sittings 6–11: days 117, 124, 138, 145, 152, 166.
   - The last month opens day 176.
   - Closings: days 187 and 194.
   - The ruling and Brom's panel: day 201.

   Is it consistent with §2's binding shape (the ruling in the year's last month; the Line crossed after the year's close), with the clean door's day 115, with Brom's panel "the same docket day as the ruling" (M2), and with what the M8 and M9 packets assume? Give a ratified table, or the exact corrections.
2. **The Velmere envelope.** It is the day-45 letter, moved to Brom's table on day 173 and still sealed. No new envelope arrives. Check it against BOOK_MAP §4e, especially #10, and against M8 and M9.
3. **Gault's note** on the riders at the gate enters the minute at the eighth sitting, and Jent disclaims knowledge. Does it disturb M8?
4. **Vastin's window.** *The Archmarshal declines to certify.* The first notice came in the year's eighth week, and the seat may proceed without him. Check this against M8's Tier B minute line (*Evaluation-protocol certification: declined by the evaluator of record; proceeding on the presiding seat's authority.*).
5. **Havel.** He compares two leaves of schedule two, so the designation's title passes under his pen. He weighs a seventh entry and notices *until relieved*. Check this against the plan's "never connects" and against six sheets, no seventh.
6. **Lira's window.** It gives three sentences to her own Kindling. Check this against the §9 limits.
7. **The night spar.** It shows the suite past the Halcenvane rates to Lira alone on a closed floor. Check it against the managed-band ruling and the honest-floor canon.
8. **Seln's count.** His five beans, and Cael's log line "all five of us", make it felt before M8. Is that inside the plan?
9. **New minor canon.** How Iron Skin looks in use; the sigil frame "under load"; the farm, orchard and gardener; Withrow's four letters advising *release*. Check these against Books 1–5 and the plan.

Write your audit to editions/monroe-1.3/book-06-the-compacts-hand/state/movement-007/plan-audit.md:
- the verdict FIRST;
- a ratified calendar table for M8 and M9 to inherit;
- each item, with chapter:line and the governing text quoted;
- exact line fixes in this format, with each old string verified by grep to match exactly once:
  1. `manuscript/chapter-NN.md`
     old: `exact current text`
     new: `replacement text`
