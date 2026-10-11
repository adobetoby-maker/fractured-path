# Repair brief — Book 6, Movement 8 (one bounded same-author repair)

**Sources.** All on Sol (gpt-5.6-sol), fresh context:
- `review-editorial.md`
- `review-cold.md`
- `source-tracking.md`
- `plan-audit.md`

**Verdicts.**
- **Story and continuity:** pass.
- **Source distance:** only 2 tracked passages.
- **Plan audit:** close after one bounded repair covering protected text and the hand-off. It ratifies:
  - the calendar;
  - the ruling's outcome and "close of the present academic year";
  - the council and bout on day 202;
  - Cael's win, two touches to one;
  - Ephram's right shoulder;
  - the Blade notice and the fragment count;
  - the four call days;
  - Ilsev's six minutes as a return (Bracken's fourteen holds);
  - the "evaluator of record" gloss;
  - Seln's "twice more" (the count remains two);
  - Brom's panel and the sealed envelope;
  - the length. Retain the scenes.

## ALREADY APPLIED BY THE COORDINATOR — do not undo; smooth the joins

The plan audit ruled that BOOK_MAP §8 protects the FULL referenced Tier B units, not only the short phrases the map quotes. Its nine exact fixes are applied and the restored text is now in protected-patterns.txt:

1. **ch51, the ruling.** It is now the protected ruling paragraph: one paragraph, with "the close of the present academic year" for "term's end". Your five numbered heads are gone. Two references to "the second head" (ch51, ch53) now point at "the finding that the respondent institution was compliant throughout" and "what the ruling says of the respondent institution".
2. **ch54, "Both. Enter both."** It now means the bout is entered under BOTH FIGHTERS' NAMES in the house's permanent column. It no longer means in two books.
3. **ch54, the boards ritual.** Rooke's clerk chalks the result while both fighters stand at the board. The loser-chalks custom and the blank rule above Ephram's name are out.
4. **ch54, Ephram's "Still glad." speech and the ninth's Log entry.** Both are restored whole (*Nine. Taken in earnest from a friend…*).
5. **ch53, Lira.** She has ONE morning left before the key goes back, not five drill days.

Read ch51, ch53 and ch54 around each of these and fix any join. Look for a pronoun, a callback or a count that still assumes the removed version: "five heads", "the second head", the chalk in Ephram's hand, the blank line, "two books", "five days".

## Must fix

1. **Seams around the restored text** (above).
   - Cael's reactions to the ruling were written against five numbered heads. Make them answer the single paragraph.
   - The same goes for the board scene and the Log scene in ch54.
   - Keep the ruling scene's stillness, the board-and-ladder intimacy, and Cael's moral accounting of the unpriced shoulder.
2. **ch49, after the protected certification line, through Gault writing in his book; ch50, Ilsev's return** (editorial). "Evaluator of record" is used in close succession for the certifying office and for Gault.
   - Outside the protected line, call the Archmarshal's office "the certifying office" throughout.
   - Reserve the unqualified "evaluator of record" for Gault.
   - One or two noun-level changes only. No added explanation.
   - Keep the five-word absence on the form, the four pens stopping, and Gault's quiet decision.
3. **The two tracked passages** (`source-tracking.md`). Do not open the source.
   - **49:83** ("In all that record these sections have never once been turned…", near-verbatim): re-compose it in your own words and order.
   - **54:154** ("He read it through twice…"): break the chain of reading the last field twice, then every entry adversarial, then the machine's grammar bending.
4. **ch49, Karis's close** (cold), from "That was an honest answer, and it is the whole of this case" through "The seat is asked to order a test in order to obtain a failure."
   - Remove or merge ONE recap of the known-result proposition, or shorten the bridge between the four indicators and the fourteenth-chapter argument.
   - Keep the legal spine, the wool-scale analogy, Jent's honest agreement, and the silent omission of the true argument.
5. **Explanatory echoes** (cold): ch50 after the girl leaves the north-road station; ch51 Havel after pinning the return and tying his six sheets; ch51 Seln after examining the ruling.
   - Cut only sentences that restate the image just shown.
   - Keep each scene whole, including Seln's "the hand".
6. **ch51, the opening** (cold): add one orienting phrase that ties Havel to the records table and the junior chair at once. No history.

## Length (#45)

The movement is now about 40,900 words after the coordinator's fixes, under the 42,000 cap. Retain the scenes. Do not pad, and do not cut development.

## After

1. From editions/monroe-1.3, run:
   - `bash tools/ed.sh gates book-06-the-compacts-hand 8` — target 0;
   - `bash tools/ed.sh overlap book-06-the-compacts-hand 8` — target 0 unprotected.
2. From the root, run `bash editions/monroe-1.3/tools/sweep_probe.sh book-06-the-compacts-hand 8 8`.
3. Append "## Repair r1" to AUTHOR-REPORT.md and correct your ledger lines for the ruling, the boards ritual, "Both", and Lira's one morning.
4. No git.
