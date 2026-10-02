# Book 1 — completion pass, same-author texture pass (from the whole-arc read)

Source: `whole-arc-read.md` (Fable 5.1, a straight read of ch1–60), §§3, 4, 7 and 9, with counts in
`whole-arc-notes.md`.

**Verdict.** The book holds as one book. The calendar, the counts, the knowledge boundaries, the
protected lines, the plants and the Reader Standard all hold. The coordinator has already applied
the read's 32 line fixes. They include:
- the season lines (ch53 Hesk's palm in the autumn; ch6 the hawthorn);
- "there are provisions" restored to the roof;
- the workshop bench;
- Lira's eleven tries in one afternoon;
- five day-counts;
- three protected-line repairs.

Do not redo them. Re-read ch36, 38, 39, 42, 43 and 45 for sense where they touched "second
morning" and "eleven tries".

The pass is split into two lanes. Each lane edits only its own chapters.

## Lane 1 — chapters 1–30

- **Priority 1, texture (your share).** Thin, by reading:
  - the generic "the way …" similes — about a third of them. Keep the instrument similes (rig, lever, needle, coin) and cut the generic "the way a man / you / it does".
  - "found that he" / "he found that" — about half.
  - the duration pads "for a long time / for a while / for some time / a long moment" — about half.
  - "did not look up" for Vell and Torvin. Keep Yeni's and the mender's.
  - the §3 named repeats, down to the instances §3 says to keep.
- **Priority 3, attribution.**
  - Scenes: ch10 s3 (the rules) and ch27 s1 (the supper).
  - Drop the tag wherever the paragraph already makes the speaker clear.
- **Rhythm.** Join clipped runs in ch26 s4 into sentences of 15–30 words.

## Lane 2 — chapters 31–60

- **Priority 1, texture (your share).**
  - Same targets as Lane 1, hardest in M6–M7 (ch34–47), where the "the way …" similes run at 23–26 per 10k.
  - Take the duration pads in M9 (ch54–60) first.
- **Priority 2, compress the investigative fortnight.** Net about 1,500 words out.
  - Cut points: ch41 s3–s5, ch42 s1–s2, ch43 s1–s2 and s4–s5.
  - Fold the four same-note back-page entries into two.
  - Let one Kestrel morning stand for both.
  - Run ch43's three-name hunt in one movement, not three visits.
  - Join ch43's clipped runs (mean 11.65).
- **Priority 2, un-rhyme ch48 s5.** Keep Halden, the bone knife and "begin at the beginning". Cut the recap of ch31's method so the chapter's weight falls on section one at two in the morning.
- **Priority 3, attribution.**
  - Scenes: ch44 s3 and ch52 s2 (the suppers), ch46 s1, ch56 s3, and ch59 s1–s3.
  - Drop the tag wherever the paragraph makes the speaker clear.

## Both lanes

**Method.** Work by reading, in place, never by script.

**Protect:**
- every protected line (BOOK_MAP §7, `protected-patterns.txt`);
- every bout's exchanges and landing beats;
- every fact, count and date;
- every line a later chapter quotes.

**After:**
- `ed.sh overlap` must stay at 0 unprotected for every movement in your range.
- `ed.sh gates` must stay at 0.
- The skeleton probe (`tools/sweep_probe.sh`) must not rise.
- Run `formula_metrics.py` on your range.
- Write `LANE-1-REPORT.md` or `LANE-2-REPORT.md` with the before/after counts for each texture target, the metrics, and a changelist.
- Run no git commands.
