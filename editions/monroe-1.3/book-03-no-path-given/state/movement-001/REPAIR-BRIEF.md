# Repair brief — Book 3, Movement 1 (one consolidated same-author repair)

Sources: `review-editorial.md` (Fable 5.1, fresh-context editorial pass with canon and
measured formula) and `review-cold.md` (Fable 5.1, manuscript-only simulated cold read),
plus `source-overlap.tsv` (tools/source_overlap.py). Both reviewers would keep reading. No
canon violation, no Reader Standard violation; every protected line is verbatim. The
pre-repair edition is frozen in `pre-repair/`. Repair in reading order, in place.

**Protect, untouched or only lightly joined:** the Ch4 Wray session; Brom's drill against
Hobb; D1; the Ch7 "He chose. He chose nothing" beat; the Oona exchange and "Where's
shattered?"; Naveth's ledger; every protected line (P6, P7, Wray's D1 record, Naveth's two
anchors, the Tide line, the Compression notice).

**Coordinator rulings.** Oona, Hobb and Gerda stay as drafted (owner decision #12 pending;
one find-and-replace will apply the owner's choice). Hobb learning his name only in Ch8 is
fine.

## Priority 1 — New prose and a continuity sweep (line-level)

- **Source reuse.** `source-overlap.tsv` lists 37 runs of ten or more words shared with the
  current edition that BOOK_MAP does not protect (longest: Ch6 para 148, 26 words; Ch6 para 19,
  24 words; Ch3 para 92, 21 words). Rewrite each in your own words, events unchanged. Then
  re-run `editions/monroe-1.3/tools/ed.sh overlap book-03-no-path-given 1` until only
  protected wording remains.
- **Reveal pacing (Ch6).** Cael must not already hold the idea that each fragment "arrived
  after he had watched someone use their Path… under real stakes." The STATE_LEDGER has him
  believing fragments arrive like weather; BOOK_MAP §10 reserves the hypothesis for Karis in
  Movement 3. Rewrite the line to his weather belief.
- **Continuity.** Brom's injured side (the reviewers found it flipping between chapters —
  make it one side everywhere, the side the majority of mentions use); "three days ago" for
  the day-one strike (it is four); the sixth bell vs floors closing; Ch5's scene order vs
  "the night before"; the dropped-word sentence the cold read cites (Ch5, near line 1178 of
  the compiled prompt); Prynn's "thirty years" against the sixty-year anchor; rank read "by
  his tag" when tags carry only a crest; Ch6 naming Edran and "the girls on the stair" before
  the reader meets either or the stair event happens. Cut the ten restatements of "a year and
  a half" to the two or three that do work.

## Priority 2 — Give the outside threat a face, and spend the room on story

- **The outside reader.** "Someone will read this form properly" is stated twice and never
  given a face or a date, so Ch2–5 run on craft alone. Add one concrete trace of that reader
  (a returned query slip, a clerk's countersignature, a date on the provision — something
  physical, within canon and without naming Coss), and let the Ch3 calendar line start a clock.
- **Lira's standings bout** has 626 words in the ring against an allowance of ~1,800;
  exchanges three and four are summarized. Put them on the page.
- **Ch8's second week** is told; show the part of it that matters.
- **Room for it:** fold the registry-history lecture into the taxonomy block; trim the
  duplicated bell recitation; convert four or five italic log entries that only restate the
  scene into action or a line of summary (keep every entry that turns rather than restates);
  cap "a door shutting in another room" at three uses and "not one ounce" at one.

## Priority 3 — Rhythm and scene economy

Measured: sentence mean 9.66 (target 14.6; Ch1–3 ~8.3, Ch4–8 ~11.5), ≤5-word share 38.6%
(~28%), ≥40-word 1.1% (3.3%), 68 scene breaks at ~480 words per scene (~950), ~100 tags per
10k (~41), "the way a…" seven times in Ch7. Apply the edition brief's "Rhythm calibration":
join clipped runs that are one thought into well-built sentences; three to five deliberate
forty-plus-word sentences per chapter; merge scene breaks toward one every ~950 words (about
half of them); drop tags where the speaker is clear; keep paragraphs short. Keep the short
beats that land.

**Length.** Budget ~37,000. Finish within 35,000–39,000 words. Never pad; use what you
free for Priority 2.

## After the repair

Re-run `python3 editions/monroe-1.3/tools/formula_metrics.py` on the eight chapters and the
overlap check, and append "## Repair r1" to `AUTHOR-REPORT.md` with before/after metrics,
the final overlap summary, and a changelist by chapter. Edit only the eight chapter files and
AUTHOR-REPORT.md.
