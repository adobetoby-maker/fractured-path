# Repair brief — Book 4, Movement 9 (one consolidated same-author repair; the book's last)

**Sources.** `review-editorial.md` and `review-cold.md`, both from Claude Fable, fresh context, on the review seat.
The cold read saw the manuscript only.

**Verdict.** Both reviewers would pick up Book 5. They point to three priced promises: the compulsion clause,
"Continue observation", and Ephram's floor time. The strongest beats are:
- Vastin's struck sentence, and "answered it smaller" (ch59);
- the corridor timetable (ch58);
- Lira's "They caught up" (ch60).

The editorial verified the ending against BOOK_MAP §1, the Book 5 hand-off and every coordinator ruling, line by
line. All of it holds:
- every protected line is verbatim;
- the gates are clean (no weekdays, seasons or oaths; no "unbound"; no new names);
- source reuse is 0 unprotected;
- the formula is in range.

Pre-repair text is frozen in `pre-repair/`. Repair in reading order, in place, by reading — never by script.

## Coordinator rulings on your flags (all ACCEPTED)
1. **"Since the pin"** replaces the map's "since midwinter". Season words are out under #35. BOOK_MAP §10 is amended to
   "since the pin".
2. **Vell's letter** says "five short sentences", with no word count.
3. **The Fiske page.** "A page that's all footwork… not a line about her. Fix that." is accepted.
4. **The law range** (carrel eleven) is accepted.
5. **The last unit session** on the Third-day, with six of nine attending, is accepted.
6. **Vastin strikes the line at the close** and writes the amendment that night. Accepted.
7. **C7 framing** is accepted. P3 below closes the one line that slips.
8. **The new-month dates** with no month named are accepted.
9. **Withrow's four-line finding and Vastin's letter to Bracken** in your own wording are accepted.
10. **Withrow's sentence** ends at "qualifying season". The Book 5 reconciliation will follow it.
11. **Gwen** stays as the placeholder.

## Priority 1 — The compilation's return date (editorial: HIGH; closed M7 governs)
ch58 has the delegation return the wing's six-filing compilation by the afternoon paper on the 24th, "held for
eleven days". ch59 has Vastin still holding it under pink tape that evening.

Closed M7 already settled this:
- Vastin sent it back on the 13th (ch45);
- Cael watched the case come home unmarked at the wing's counter on the 14th (ch48);
- Havel's ledger logs the return (ch49).

Keep M7 as the record:
- **ch58.** Re-set Seln's four minutes with the eyes and the thumb to the 14th, at the copying table after the list
  clerk had gone and the counter was clear. ch48 only shows the case's face being read at the counter, so the thumb
  check is open.
- **The 24th.** The afternoon paper brings the delegation's CLOSING DOCKET for the requisition: the signed return slip
  that discharges the loan and attests no extract or copy was retained. The first master's chalked rule and "one of
  three. probably the third." still land.
- **Dates.** Amend "waited since the twelfth" and the cipher page's "The date the file came back" to the 14th.
- **ch59.** Change "He let the pink tape lie" to a memory of having sent the filings back on the second morning.
- **Keep whole:** the thumb on the corners; the pin-hole "a fraction rounder"; "as clean as a sheet still in the
  ream".

## Priority 2 — Calendar and counts (editorial)
1. **The baseline month.** The baseline is the forty-eighth day (ch12), which is the SECOND month. Change "first month"
   to "second month" at ch57 (the one that disagrees with "second month" in the same scene) and at ch62 (the
   inventory). The M8 and ch43/ch49 uses go to the book-level sweep for one ruling. Do not touch them now.
2. **ch58, "since the day my key was cut".** Seln arrived about four weeks after the key was cut. Make it "since the day
   he first opened that book", or similar.
3. **ch62, "Three years now" / "Three years and not a Tide practitioner"** for the same Book 2 events that l.35 calls
   "two years ago". Make them two years, or make an inclusive count explicit once.
4. **ch60, the satchel's "three hundred sheets"** fuses with the 311-sheet enrollment file and the season sheets. Drop
   the number ("the season's sheets behind them in his numbered order").
5. **ch61, the frame "had been rebuilt"**, while ch62's notch is still to be fitted. Make it "is being rebuilt".

## Priority 3 — The ending ends once; clarity; C7 (both)
- **The wall (cold).** After Karis's "Noted.", three codas stack: Seln's exit, "The bluff held. The stamp was real.",
  and the barge horn.
  - "The bluff held. The stamp was real." is the packet's close. Make it the LAST beat.
  - Fold Seln's exit in before the closing exchange, or cut it. Its sixty-feet-down-the-wall image already sits
    earlier.
  - Move the barge horn earlier, or cut it.
  - The closing exchange stays exactly as set.
- **ch62 l.128 (C7).** "One note in one file, in a hand that signs its whole name" is stated as something Cael holds.
  Hedge it by a phrase ("in a hand I'd wager signs its whole name"), so belief and knowledge stay distinct.
- **The posting-house (cold).** Anchor the backward time jump into Vastin's evening with a phrase that says when.
  Give Vastin's role one phrase at first naming ("the Archmarshal, Vastin…"), so a listener who missed M7 knows him.
- **ch62 vs ch59 (cold; verify).** Cael's "single look across the brass" sits against Vastin's stated not-looking. If
  they conflict, make Cael's line his reading of a glance he cannot be sure of, or align the two.
- **To taste.** Thin "said" tags where the speaker is already clear (ch58 ll.143–207; ch60 ll.199–209). Let one of
  ch59's two "forty years" go.

**Length.** Finish within 28,500–31,000 words.

## After the repair
Run:
- `ed.sh overlap book-04-copper-crown 9` (0 unprotected);
- `ed.sh gates`;
- `sweep_probe.sh book-04-copper-crown 9 9` (≤ 5% skeleton, ≤ 13% close);
- `formula_metrics.py` on the six chapters.

Append "## Repair r1" to AUTHOR-REPORT.md with:
- the changelist, by chapter;
- before/after metrics;
- the day table, if anything moved.

Edit only ch57–62 and AUTHOR-REPORT.md. Run NO git commands of any kind.
