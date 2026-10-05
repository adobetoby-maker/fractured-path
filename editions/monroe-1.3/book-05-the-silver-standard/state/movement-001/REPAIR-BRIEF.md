# Repair brief — Book 5, Movement 1 (one consolidated same-author repair)

**Sources.** `review-editorial.md` and `review-cold.md`, both from Claude Fable, fresh context, on the review seat.
The cold read saw the manuscript only.

**Verdict.** Both reviewers would continue without hesitation. The movement does its job: Cael lands on a
continental roster through other people's honest paperwork. The Standard is taught through Rooke's yellow card and
a mock bout that Cael wins while out-rating lower. Chapters 5–6 find the book's real antagonist: an honest instrument
pointed at a boy who has already decided to manage it.

The editorial verified the Book 4 seam and the ENTRY state line by line. All of these pass:
- six fragments plus the anomaly;
- two public capabilities;
- Pressure flat, right shoulder;
- Lira Iron R1, Ephram Iron R6;
- Seln at the copying table;
- watchers two and two;
- Bracken "he";
- Vastin with no age and "forty years";
- no seasons, no English weekdays, no new names;
- every protected line verbatim, and overlap 0 unprotected.

Pre-repair text is frozen in `pre-repair/`. Repair in reading order, in place, by reading — never by script.

## Coordinator rulings on your flags
1. **"A note for the cold term."** ACCEPTED under #35.
2. **The rating scale.** ACCEPTED in architecture, with the ceiling fixed by **OWNER-DECISIONS #38** (default in force):
   - Each judge gives execution, control and effect marks on a scale that runs PAST ten, to fifteen; ten is par.
   - Five judges mark; the high and low totals are struck and the middle three averaged.
   - A rating can run to forty-five, and par is thirty.
   - Bands: Copper 12–17; Iron 18–21; strong Iron to Silver-touched 22–27; Silver 28–34, with par at thirty in its
     heart; Gold 35 and above.
   - Bronze: Rooke places it across the top of the 22–27 band, and the tournament does not bracket it.
   - Every worked figure already on the page stands, because each is below par.
3. **Teaching fellows** (the fourteen Silver and one Gold not fielded): ACCEPTED.
4. **Vastin's room left unlocated, and the routing slip's two initials:** ACCEPTED. This opens a new thread, which
   the coordinator will carry in the ledger. Do not resolve it.
5. **Hesk's reply, and the buried Copper Rank Four as "she":** ACCEPTED.
6. **The year counts.** Book 5 ch1 is about twelve weeks after Book 4 ch62. Do NOT increment the year counts yet.
   Restore Book 4's figures:
   - the landing beat is "three years";
   - Compression unseen is "two years";
   - the anomaly is "two years running".

   The protected log item 21's "three years" (BOOK_MAP §10) stays as written. It is read as dating from Ardenmere
   (#37 O3).

## Priority 1 — The scale on the page (editorial)
- In ch5 (¶149, ¶175, ¶179), use two or three sentences so the scale runs past ten, par is thirty, and Silver is
  centred on thirty with Gold above. Set the band table to #38, with Rooke's one-line aside placing Bronze.
- In ch6 ¶226, check that "thirty, twenty-eight, twenty-two" still reads true on the new scale; change the numbers
  only if they no longer do.
- Keep: Rooke's yellow card, Karis striking the marks aloud, the ch6 cards read as words, and "a boy who was not
  there".

## Priority 2 — Count slips and the silence's arithmetic (editorial)
1. **ch5 ¶131.** "Nine days" becomes "Thirteen days". The response went down on d12, and the card came up on d25.
2. **ch4, the silence.** Add one sentence: the fourteenth day is crossed off, nothing is sent back down, and Bracken
   does not resubmit. The memorandum's fourteen-day deadline must not pass unremarked.
3. **ch4 ¶101.** Bracken, "two years" becomes "in a year".
4. **ch4 ¶135.** "Forty years before you were born" becomes "forty years ago, before you were born". Reword at most
   one other of ch4's four "forty years".
5. **ch1 ¶207.** Seln's line "on the tenth line" becomes "the last line", or reorder the list.

## Priority 3 — Opening, say-it-once and read-aloud (cold; editorial)
- **The opening (cold).** Open on the oak, and cut ch1's first recess recap and the six-line "adjacent" capability
  inventory to what a stranger can hear. Keep the facts the ENTRY state needs; a newcomer should have footing within
  the first page.
- **ch4 (cold).** The four-page argument is summarised twice in a row (about ¶93–99). Keep one. Tighten Vastin's
  pages two and three.
- **Read-aloud:**
  - ch1: Ephram's duplicated beat (¶235/237).
  - ch3 ¶17: Rooke and Lira share one paragraph. Split it.
  - ch3: the "She says:" misattribution (¶253–259).
  - ch6: the missing section rule (¶221–224). It needs a blank line before and after.
  - ch6 ¶248: recompose the charter sentence so it agrees with ch4's placement of the clause and the provision. The
    charter is open in its oldest part, the founding articles, which are older than the schedule where Karis found
    the provision and older than the clause, "before the registry's last standardization".
  - Earth idioms: ch6 "turn on a sixpence" and ch2 "like a hymn sheet". Swap both.
- **Optional.** Join a few clipped narrative runs in ch3's frames (never the speech) to lift ch3 toward the mean
  floor.

**Length.** Finish within 29,500–32,000 words.

## After the repair
Run:
- `ed.sh overlap book-05-the-silver-standard 1` (0 unprotected);
- `ed.sh gates`;
- `sweep_probe.sh book-05-the-silver-standard 1 1` (≤ 5% skeleton, ≤ 13% close);
- `formula_metrics.py` on the six chapters (sentence mean ≥ 13.2).

Append "## Repair r1" to AUTHOR-REPORT.md with:
- the band table as set;
- before/after metrics;
- the changelist, by chapter.

Edit only ch1–6 and AUTHOR-REPORT.md. Run NO git commands of any kind.
