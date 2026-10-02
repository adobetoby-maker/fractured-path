# Repair brief — Book 1, Movement 7 (one consolidated same-author repair)

Sources: `review-editorial.md` and `review-cold.md` (both Claude Fable 5.1, fresh context; the
cold read is manuscript-only). Both would keep reading "without hesitation". The Feryn bout holds
and is trackable exchange by exchange — each of the four exchanges changes one variable on each
side, cost accrues, and Vell's call is argued from inside Cael's own accounting; the unexplained
third exchange is a strength. No canon or Reader Standard violation; overlap 0; both packet notes
met. Pre-repair text is frozen in `pre-repair/`. Repair in reading order, in place, by reading —
never by script.

**Rulings on your flags — all KEPT, with evidence:** Hesk told the five things including the Wind
notice (source ch16's letter says exactly this; Book 2 ch12 agrees); Vell hearing "[SHATTERED]" at
her table (BOOK_MAP §5 stages it there); instances now six; Lira's row of three and eleven drops;
Corvane as a retired Copper Pressure fighter and her air as contact reasoning (a correct plant —
nothing pre-pays Book 3); the Monday-noon exhibition; Hesk quoting the line verbatim; the new
details (with the Feryn-age fix below).

**Protect:** every exchange of the Feryn bout; the unexplained third exchange; Vell's call and the
consent argument; the keys-and-locks image and "not the Arbiter's kind of nothing"; the Pressure
notice; "What tier are you?" / "[SHATTERED]" / "When you figure it out, I want to know."

## Priority 1 — Protected-line hygiene

- **ch44:** Corvane's "What are you?" is Darrow's Tier A question, word for word (BOOK_MAP §7).
  Nobody may ask it in those words before Darrow. Reword her question so it still keeps Vell's
  hearing of "[SHATTERED]" the first time.
- **ch42:** Cael's copied Wind notice must be the exact three-line Tier A text — no added period,
  not run onto one line — and it is called "four lines" twice; it is three.
- Decide once whether `[SHATTERED]` prints with brackets wherever it is written or read (the
  protected lines print it with brackets), and make it consistent.

## Priority 2 — Numbers and continuity

- **The peak (ch46–47):** Vell's "won two since, four of his six" against "a dozen bouts" against
  the Log's "Fifteenth"; and "assessed, in my hand" against "Against unrated" with no line telling
  them apart. Two or three sentences reconcile them; leave the consent argument untouched.
- Vell's "three weeks" is wrong twice (ch43 → a fortnight; ch46 → five weeks); "the second
  Tuesday" → the last Tuesday; "He did not tell anybody about the step" contradicts ch43 → "anybody
  else"; the ch45 montage steps back a day; "on the second Sunday" (cold read, its line 1551) — make
  it clear.
- **Feryn's ages:** Copper at nineteen against a Bronze evaluation at nineteen; "six or seven
  years" for a man of twenty-four; "sat Bronze panels" reads as if he were an assessor. Make them
  agree.
- The doubled "at Copper 3" (cold read, its line 189).
- **ch42 (cold read):** the duplicated "nothing came" courtyard beat re-reports chapter 41's
  attempt on the same wall with the same simile — cut it to what is new; keep the keys and locks
  and "not the Arbiter's kind of nothing".

## Priority 3 — Rhythm and pause-beats

- Words per scene ~828 (range 850–1,050): merge five or six same-place breaks (ch42 ×1, ch44 ×2,
  ch47 ×3 — the editorial review names them).
- "for a long time" appears 28 times (plus 14 "for a while" and 9 "did not look up") and flattens
  the narration's cadence: keep a few; give the rest a concrete beat or nothing.
- Optionally thin tags in ch44–45 (~113 reporting verbs per 10k).

**Length.** Finish within 34,000–35,500 words.

## After the repair

Run `editions/monroe-1.3/tools/ed.sh overlap book-01-the-shattered 7` (must stay 0 unprotected)
and `python3 editions/monroe-1.3/tools/formula_metrics.py` on the seven chapters, then append "##
Repair r1" to `AUTHOR-REPORT.md` (metrics, overlap summary, Corvane's new question, the bracket
decision, Feryn's ages as now stated, changelist). Edit only the seven chapter files and
AUTHOR-REPORT.md.
