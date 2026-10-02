# Repair brief — Book 3, Movement 3 (one consolidated same-author repair)

Sources: `review-editorial.md` and `review-cold.md` (both Claude Fable 5.1, fresh context;
the cold read is manuscript-only). Both would keep reading — "without hesitation"; the held
beats are Edran's "Don't tell me," the archive's "Tires in the sequence, not the body," and "A
fourth." No canon violation; Reader Standard passes; source reuse 0; protected log verbatim.
Pre-repair text is frozen in `pre-repair/`. Repair in reading order, in place, by reading (no
scripted splitting).

**Rulings on your six flagged items — all kept:** Edran refuses to be told (consistent with
BOOK_MAP §5.4); the exhibition rules frame (three exchanges, a fourth at the petitioner's
request, Wray's "unformed at contact. Glancing", Cael 2, Edran 1) is consistent with the spine
and P10's "Same terms" — it becomes ledger canon; the hypothesis is spoken only, and asking
Lira's leave is right (clause five was hers) — keep "appetite/eat" strictly metaphor; the
Compression "drop" is a practised form of D1's non-use — keep, cost "none found yet"; the Iron
"thickening" is the planned cloth-grade plant — keep; Hesk's mended bench — keep; one Lira
cutaway and Cael ~95% matches BOOK_MAP §7's budget for this movement.

**Coordinator ruling on the calendar:** hold BOOK_MAP §3's anchor — the hypothesis falls in
**week 8** (the nulls bind from week 9), and Lira's reassessment falls in weeks 8–9.

**Protect:** every beat, touch, ruling and line of speech in the exhibition bout; Edran's
"Don't tell me"; the archive's "Tires in the sequence, not the body"; "A fourth"; Hesk's bench
and his "glad of the third"; Lira's shoulders at the calendar; Gerda; the protected log line.

## Priority 1 — Calendar and attribution (phrase-level)

- "three weeks ago" (ch18 near l.151, ch19 near l.173) for a bout fought in week 6, day 1 —
  correct the interval.
- Ch21's session order runs Tuesday → Thursday → Wednesday and drifts the hypothesis into week
  9–10; compress ch21's sessions so the hypothesis lands in week 8 (ch23 already logs "Week
  eight"). Ch23's "a week on the board, two days ago" must agree with the elapsed time.
- Lira's reassessment "nine days off" → about five days, so it lands in weeks 8–9.
- Attributions and small facts: "Hobb had said" is Wray's ch17 line — give it to Wray; Naveth's
  "tonight Quenna will copy" vs Quenna's "copied last night" nine-plus days later — make them
  agree; six vs nine points — one figure; Hesk's "back door" against ch3; whether Lira "saw"
  the half push; the non-use count. (Exact locations in both reviews.)

## Priority 2 — One rule for the Glass structures, and the ch23 codas

- **The bout's bookkeeping (ch18 drills; ch19 near :57, :131–145, :217–225, :281):** state
  once — in the ch18 drills, plainly enough for a listener — how many structures Edran can hold
  at once, how the third is made (cold, with half a mind), and where the gap lives. Then make
  every exchange obey it: which forearm carries which structure must not shift inside exchange
  2 or between exchanges, and exchange 4's innovation must be new under that rule rather than a
  contradiction of it. Clause-level edits only; the fight keeps its length and every beat.
- **Ch23's codas:** eight landings in a row after the wall scene, and the Quenna stair beat
  repeats Naveth's "dullest paragraph" almost word for word. Keep only the codas that add
  something new (Hesk's bench, Lira's shoulders at the calendar, Gerda); cut about 25–40 lines.

## Priority 3 — Rhythm in the six conversational chapters

Ch19 (the bout) meets every primary target — leave its rhythm alone. In ch17, ch18, ch20, ch21,
ch22 and ch23 the three primaries are outside the working ranges (movement: mean 11.91,
≥40-word 1.7%, 742 words per scene; ch20 has seven breaks at 606 words per scene). Join clipped
narration into full sentences, add a few earned long sentences, merge one or two breaks per
chapter, drop redundant tags. Keep all speech. As you pass through the training and archive
scenes, let the progression vocabulary come back where it belongs (it measures ~21 per 10k
against ~65 for this stretch) — terms for what Cael and the others can and cannot do, not
decoration.

**Length.** Budget ~35,000; the draft is 34,208. Finish within 34,000–36,500 — the Priority 2
cuts can be spent on the rhythm work.

## After the repair

Run `editions/monroe-1.3/tools/ed.sh overlap book-03-no-path-given 3` (must stay 0
unprotected) and `python3 editions/monroe-1.3/tools/formula_metrics.py` on the seven chapters,
then append "## Repair r1" to `AUTHOR-REPORT.md` (before/after metrics, overlap summary, the
calendar as it now stands week by week, the Glass rule as now stated, changelist by chapter).
Edit only the seven chapter files and AUTHOR-REPORT.md.
