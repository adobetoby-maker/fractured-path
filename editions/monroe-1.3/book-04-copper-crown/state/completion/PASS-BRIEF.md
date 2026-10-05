# Book 4 — completion pass, Step 3: same-author texture pass (from the whole-arc read)

**Source.** `whole-arc-read.md` (Claude Fable, a straight read of ch1–62), §§3, 4, 8 and 9, with the counts in
`whole-arc-notes.md`. The book holds as one arc:
- the day-anchored calendar chains cleanly;
- every standing and tally agrees with the page;
- knowledge boundaries hold;
- "unbound" and "decision point" each appear once;
- C7 is framed as belief;
- #35 is verified;
- the Reader Standard is met.

**Already applied by the coordinator (do not redo):**
- the read's 68 line fixes (§8), including:
  - the baseline as the SECOND month throughout (ch43, ch49, ch54–55);
  - English weekday names fixed at ch7 and ch12;
  - "half-metre" settled as the book's yard measure;
  - the seams listed in §1;
- one more: ch55 "the cold runs had given up at the baseline".

Re-read each in context and smooth any join.

The pass runs in two lanes. Each edits only its own chapters.

## Both lanes — Priority 1: thin the simile, pause and number repertoire (§3)
- **Similes.** Cap the explanatory "the way a X does Y" (283) and "as if / as though" (176) TOGETHER at three per
  chapter, and never two on one gesture.
- **Fillers.** Cut "exactly" (208), "for a long moment" and the other measured pauses (194), and "without a word" where
  the sentence stands without them.
- **"Did not look up"** belongs to Prynn and Bracken again.
- **"He wrote it that night".** Vary or drop the frame around the Log. Keep every entry.
- **The stake and the corner.** Explain them once, in lane B. Do not re-explain them in every chapter after.
- **"Eleven" (228).** Take it out wherever it is not canon, so the elevens that matter ring.
  - **Lane A** removes: eleven instruments, eleven Paths, eleven swings, eleven feet, Nyle's eleven wins.
  - **Lane B** removes: the porters' eleven minutes, the eleven thumbnail marks, the eleven crosses, eleven years of
    indexes, the eleven provision files, "eleven more chairs", "Lira has done it eleven times", and the supersession
    clerk's eleven minutes.
  - **KEEP:**
    - carrel eleven;
    - eleven weeks;
    - eleven seconds;
    - eleven questions;
    - eleven days;
    - Ilsev's eleven minutes and eleven months;
    - Lira's eleven bouts unbeaten;
    - "eleven of twelve";
    - "subsection eleven";
    - Gault's protected "in eleven years";
    - the delegation's eleven names;
    - any eleven inside a protected line or pattern.
- **The first instance of each figure stays.** Rewrite the rest in the character's own register, or cut them.
- **Length.** Expect to lose 2,000–3,000 words across the book.

## Lane A — chapters 1–31
- Priority 1, as above.
- **Priority 2: the M3 counting study.**
  - ch15: tell the second and third failed maps in a sentence each; keep the fourth and fifth.
  - ch17: let the retelling to the three stop at the overlay.
  - ch18: cut the fatigue page's restatement of the ch17 plan.
  - Together these lose 600–800 words. Add or remove no scene breaks.
- **Seams (Priority 3).** Reread for:
  - ch9–10: the ladder book;
  - ch14, ch28, ch30: Seln's hands (four hands and the cipher; a round cover hand);
  - ch30–31: Lira's hip calendar;
  - ch23: rule two.

## Lane B — chapters 32–62
- Priority 1, as above. The stake and corner explanation lives here, once.
- **Priority 2.**
  - ch49: lose about 500 words. Fold Cael's first recess into Ilsev's section and Havel's logging into his own
    window, so the finding is reached in six sections, not eight.
  - ch47: lose about 300 words. The Ilsev window's four-volume anecdote becomes a sentence.
  - ch45: add ONE line of Cael's own stake before the Vastin window.
  - No scene breaks added or removed; no cutaway cut.
  - Keep the ch49 Cael beat between the windows (from M7 repair) and mark four exactly where it is.
- **Seams (Priority 3).** Reread for:
  - ch34: rule two;
  - ch48, ch58, ch62: Seln's hands;
  - ch51–52, ch56: Lira's certificate;
  - ch54–55: the baseline month.

## Both lanes
**Method.** By reading, in place, never by script.

**Protect.**
- Every protected line (BOOK_MAP §9/§10, `protected-patterns.txt`).
- Every notice.
- Every bout's exchanges and landing beats: Edran, Mire, Fiske ×2, the pin, Tarn, Merrick, the Copper final.
- The evaluation's six trials and their figures; the interview's questions.
- Every tally, count, day and date, and every line Book 5 will quote.
- C7 framing; "decision point" once; unbound once.
- Gwen and Abbot stay as they are (owner-pending placeholders).
- No English weekday names, no season words, no month order (#35).

**Count.** Count each target before and after with grep, within your range, and report both.

**After.**
- `ed.sh overlap book-04-copper-crown N` stays at 0 unprotected for every movement in range.
- `ed.sh gates` stays at 0.
- `tools/sweep_probe.sh book-04-copper-crown F L` does not rise.
- Run `formula_metrics.py` on your range. Hold the mean ≥ 13.3, ≥40w ≤ 4.5%, and 850–1,050 words per scene.
- Write `LANE-A-REPORT.md` or `LANE-B-REPORT.md` here.
- No git commands of any kind.
