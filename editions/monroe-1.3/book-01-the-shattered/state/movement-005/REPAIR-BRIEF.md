# Repair brief — Book 1, Movement 5 (one consolidated same-author repair)

Sources: `review-editorial.md` and `review-cold.md` (both Claude Fable 5.1, fresh context; the
cold read is manuscript-only). Both would keep reading; opening on a stranger reading Cael's file
orients a new reader at once; the Lira–Brenna bout is the strongest stretch and the desk leg the
best plant-and-payoff. No canon violation; Reader Standard clean; protected lines verbatim;
overlap 0; all nine coordinator notes met; the ch29 restart seam reads as one scene. Pre-repair
text is frozen in `pre-repair/`. Repair in reading order, in place, by reading — never by script.

**Rulings on your flags:** the Coss cutaway is earned in content but ~900 words over and should
come down (Priority 2); Lira's bout and Brenna are earned — do not shorten; the Movement 6 plant
works; all the new canon is approved; Vell learning "Hesk-ward" is right; the Halvern/Halden
handling is enough.

**Coordinator ruling:** Lira's "in the life before the academy… I've read Compact paper" (ch32,
near L65) nudges an item BOOK_MAP holds OPEN. Soften it so it says nothing new about her life
before the academy (she can know Compact paper from the academy, or simply know it).

**Protect:** every exchange of the Lira–Brenna bout and its aftermath; the Coss recognition beat
at Torvin's supper; the archive hypothesis read aloud like a load calculation; the desk leg;
"make myself expensive"; every protected line.

## Priority 1 — Counted time and clarity

- ch29 (near L325, L371): "three weeks" since Cael's Brenna bout is about five and a half (day
  15 → day ~53). Make it "five weeks" or the true count.
- ch30 (near L181): "four nights ago" is three. ch31 (near L87): "forty hours left" is in the
  mid-thirties. ch33 (near L207): "four days of weather" is three. Also the cold read's "second
  afternoon" (its line 753) — check against the movement's own day count.
- ch29 (near L299) re-describes Brenna's shield in ch15's words — cut it to a clause.
- Clarity: "wrote it on the wall by the pump"; the flashback tense the cold read cites (its line
  363); gloss "the four" where it first appears in this movement.

## Priority 2 — Say it once; bring Coss to ~6.2k

- Coss's cutaway: trim 500–800 words from ch28's second-day district survey (things the reader
  already has through Cael) and cut the doorstep lesson taught twice (ch28 / ch30) to one.
- Ch32: cut Coss's explanation of how unusual the objection is and his closing aphorism and
  counsel — the respect is already shown across his three readings, and a man who refuses to
  speculate should not speculate aloud.
- Ch33 tells one quarter-hour four times (wall, Log, letter, report): cut the front-of-Log entry
  to two lines and the letter's route-through-the-index paragraph to its result, so the "make
  myself expensive" plan arrives sooner.

## Priority 3 — Rhythm, by reading

Words per scene are 643 (range 850–1,050) and the ≥40-word share 5.3% (range 2.5–4.5%). Join
about ten scene breaks — mainly ch29's exchange-by-exchange cuts inside the bout (a bout is one
contest; keep every exchange), plus the openers of ch28, 30, 31 and 32 — aiming for 34–35 scenes.
Split about twenty of the longest Coss and archive sentences at a real turn of thought (the
editorial review lists them). Do not touch dialogue, the bout's beats or the short-sentence share.

**Length.** Finish within 27,500–30,000 words.

## After the repair

Run `editions/monroe-1.3/tools/ed.sh overlap book-01-the-shattered 5` (must stay 0 unprotected)
and `python3 editions/monroe-1.3/tools/formula_metrics.py` on the six chapters, then append "##
Repair r1" to `AUTHOR-REPORT.md` (before/after metrics, overlap summary, the softened Lira line,
changelist by chapter). Edit only the six chapter files and AUTHOR-REPORT.md.
