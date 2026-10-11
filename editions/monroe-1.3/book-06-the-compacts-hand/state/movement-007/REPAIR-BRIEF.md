# Repair brief — Book 6, Movement 7 (one bounded same-author repair)

**Sources.** All on Sol (gpt-5.6-sol), fresh context:
- `review-editorial.md`
- `review-cold.md`
- `source-tracking.md`
- `plan-audit.md`

**Verdicts.**

| Read | Verdict |
|---|---|
| Editorial | Close with line fixes, plus one bounded cadence pass. "Structurally sound, canon-faithful, emotionally effective." |
| Cold | Three local priorities. |
| Source distance | **0 genuine tracked passages.** |
| Plan audit | **RATIFIED AS WRITTEN, no manuscript line fix.** |

The plan audit confirms that these are all inside the plan:
- your calendar past day 98;
- the day-45 Velmere envelope on Brom's table;
- Gault's gate leaf;
- Havel's six-sheet stop;
- Lira's window;
- the private spar;
- Seln's five;
- the minor canon.

Text is frozen in `pre-repair/`. Repair by reading, never by script.

## Coordinator rulings on your flags

All eleven are ACCEPTED. Two need recording:
1. **Calendar: RATIFIED.** The full table is in `plan-audit.md` and goes into the ledger. It runs:
   - recess, days 99–112;
   - sittings 6–11 on days 117, 124, 138, 145, 152 and 166;
   - the last month opens day 176;
   - closings on days 187 and 194;
   - ruling and Brom's panel on day 201.

   For M8 and M9 the coordinator chooses the audit's preferred finish: council and last bout on day 202, M9 entry on day 203, year close on day 207.
2. **The Velmere envelope:** the day-45 letter, on Brom's table from day 173, still sealed. RATIFIED.

## Must fix

1. **ch41:61 against ch41:89, forty versus forty-one resident enrollees.** Anchor the count to Bracken's FORTY-ONE.
2. **ch42:103 against ch42:111–131, five door approaches promised and four performed.** Anchor to the FOUR actual trainees. Recheck the immediate paragraphs.
3. **ch41, the opening through the reading-room argument** (cold read). Add or adjust two or three brief orientation beats and no more:
   - around "Six now";
   - Cael's reason for remaining;
   - what the proceeding can concretely do to him.

   Do not recap M6 or explain the hidden discovery. Keep the deniable routes, the empty hill and the sparse Log entry restrained.
4. **ch44, Havel** (cold read), from "Havel had the two leaves under his hands" through the inn-room review.
   - Either compress the receipt mechanics, or give ONE clearer statement of what he hoped the designation would prove and why the proper registry entry defeats that hope.
   - Keep his viewpoint, the withheld disclosure, six sheets and no seventh, and *until relieved*.
5. **ch47, from the Log sequence through the final window** (cold read). The thesis that correct entries can be true, costly and weightless is restated in several adjacent forms.
   - Compress one or two reflective paragraphs.
   - Favour the concrete inventory: "three boxes… two under a bed… a carter's book… five beans".
   - End on "Next: Ostrand" and the changing of the coats.

## Cadence (editorial; bounded)

Apply this only in the expository bridge passages of ch41, ch44, ch46 and ch47.
- Join only adjacent statements that form one thought, into clear 20–35-word constructions.
- Protect every short spoken line and every landing beat.
- Exclude dialogue and every developed action or learning sequence. That covers Lira's fights, the night spar and the road-craft.
- Do not chase the SD.
- Keep the ≥40-word share at or under 4.5%.

## Length (#45)

M7 is at about 103% of budget, which is right. These fixes should not shrink it materially. No padding.

## After

1. From editions/monroe-1.3, run `bash tools/ed.sh gates book-06-the-compacts-hand 7` (target 0) and `bash tools/ed.sh overlap book-06-the-compacts-hand 7` (target 0 unprotected).
2. From the root, run `bash editions/monroe-1.3/tools/sweep_probe.sh book-06-the-compacts-hand 7 7`. It works now.
3. Append "## Repair r1" to AUTHOR-REPORT.md.
4. No git.
