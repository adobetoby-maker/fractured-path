# Repair brief — Book 4, Movement 1 (one consolidated same-author repair)

**Sources and verdict.**
- This brief consolidates two reviews by Sol, the edition's review seat: `review-editorial.md`
  and `review-cold.md`. The cold read saw the manuscript only.
- Both reviewers would continue confidently; keep-reading scores were 8–9.
- The movement pays off the assay-clause search, the Greyvane departure, the Edran rematch and
  the enrollment.
- It ends on four specific diverging pressures: the fixed baseline, Lira's bracket, Brom's
  cohort, and the review flag.
- Source distance is clean (probe 1%; overlap 0), including your rewrites of ch5 and ch7.
- Pre-repair text is frozen in `pre-repair/`. Repair in reading order, in place, by reading —
  never by script.

**Coordinator rulings on your flags:**
- Bracken is "he" (the default in force; owner may override).
- Bracken's letters starting in week 8: accepted.
- **The early plant** (Bracken's fifteenth letter cites the directive's transitional article):
  KEEP, as a plant only. It must not state what Ilsev finds in Ch18.
- Fame line in your own words: accepted. Its new worst rumour (that his family gave him up,
  which Cael corrects) is accepted.
- Lira's ladder registration deferred: accepted.
- The tool bug you reported is fixed.

## Priority 1 — Line fix (editorial)

- `chapter-02.md` l.95: Karis's last spoken sentence is missing its closing quotation mark before
  the scene break. Add it.
- Then run a punctuation and listening check on every join you change.

## Priority 2 — Say it once (cold read and editorial)

**The assay clause** (ch1 from the three repeal locations to the week-fourteen finding; ch2 from
"Bracken's fourth letter…" to the fifteenth letter).
- The proof that the clause was orphaned, not repealed, is restated in several overlapping
  passes.
- Add one firmer transition so ch2 reads as the correspondence track braided inside ch1's
  investigation.
- Trim only duplicated explanation, and give the space to reaction, friction or new information.
- Keep on the page: the nine inquiries, Bracken's independent road, the fifteenth letter and
  counsel's seal.

**The ch4 farewells** (Quenna at the pump, Naveth's notice, Wray on the defensive floor, Prynn at
the gate).
- They repeat one construction: a restrained gesture, then a long explanation of what wasn't said.
- Vary or shorten one or two of the interpretive after-paragraphs, trusting the gesture sooner.
- Keep every farewell and its concrete gift.

**Ch7, Halcenvane's reason for taking Cael.** It is stated three times: Karis's inference,
Withrow's two-column sheet, and Cael's roof/ledger synthesis.
- Keep all three perspectives.
- Compress one explanatory paragraph after Karis's evidence.
- Cut only the most duplicative lines from the final binder reflection.
- The baseline-notice hook must land fast.

## Priority 3 — Rhythm (editorial)

- Current figures: sentence mean 12.67 (range 13–15.5); ≥40-word share 2.1% (range 2.5–4.5%).
- Make a non-scripted, sentence-by-sentence pass, chiefly in the narrative exposition of ch1, 2,
  6 and 7:
  - join adjacent narrative statements that belong to one thought;
  - add a limited number of well-built long sentences.
- Leave the Edran rematch's beats short. Never touch speech.
- Secondary: "that" runs about 126 per 10k. Thin it where easy.

**Length.** Finish within 31,000–33,500 words.

## After the repair

- Run:
  - `ed.sh overlap book-04-copper-crown 1` (must stay 0 unprotected);
  - `ed.sh gates`;
  - `tools/sweep_probe.sh book-04-copper-crown 1 1` (must not rise);
  - `formula_metrics.py` on ch1–7.
- Append "## Repair r1" to `AUTHOR-REPORT.md` (before/after metrics, changelist by chapter).
- Edit only ch1–7 and the report. Run no git commands.
