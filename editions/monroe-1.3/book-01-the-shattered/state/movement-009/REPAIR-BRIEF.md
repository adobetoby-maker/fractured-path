# Repair brief — Book 1, Movement 9 (one consolidated same-author repair)

Sources: `review-editorial.md` and `review-cold.md` (both Claude Fable 5.1, fresh context; the cold
read is manuscript-only). The climax lands "strongly". The fourth exchange pays off three separately
built things: the crossing's evidence-to-ruling trail, the ch56 trough failure, and the old man's
"spend nothing". Darrow going down is legible in one paragraph, and Vell's count and her inability
to write what she saw sell it. The ending lands too. Cael's name begins a line, Hesk says *proud*
before he knows, the stranger and the slip dated "the day after" reopen the plot, and Lira keeps
them in the shrinking grey half. The cold reader would pick up Book 2. The editorial spot-check of
the bout against source ch22–23 found new entry points and new images; the shared beats are spine
only. Your rewrite of ch57–58 held. Reader Standard passes, the audio guard is clean, reserved
truths are kept, overlap is 0 and skeleton 1%. Pre-repair text is frozen in `pre-repair/`. Repair in
reading order, in place, by reading — never by script.

**Rulings on your flags — all accepted:**
- Record 9–7 and eight instances (seven = exchange 3, the step unasked; eight = exchange 4). The trough failure is correctly uncounted.
- Vell names him at the rope and then in the book.
- Coss's senior flag is dated the day after, with no entry, the empty log page, and the key home. Flagged as a Book 6 plant; rank stays OPEN.
- Darrow's autumn and "will want to know" stand as an open offer. They fall in the between-books gap, since Book 2 ch1 is silent; this is flagged for the Book 2 map.
- The Iron Path mechanics stand, reconciled with Book 3 ch8's "evasion-reset vulnerability". The crossing is the reset after each load.
- The concurrent use and its cost stand, and so do the district return, the chalk-board woman (the week-two Stone woman), Feryn's anecdotes and Hesk's proud letter. "Properly" is paid in so many words.
- The stranger stands: sex and features are unstated, unlike Book 2's watcher.

The protected lines (Tier A/B) are exact and first appear where the map says. "What are you?" is
Darrow's and occurs once. Hesk's "being seen" letter is quoted only as Cael reads it, and it matches
ch53 word for word. The length is 8% under budget; that is noted, not a repair item.

**Already applied by the coordinator (do not redo):** editorial line fixes 1–10. Re-read each in context and smooth any join:
- ch55: Lira asks Doss in the morning at the yard door, off his watch.
- ch56: the opening quotation mark on Feryn's tannery confession; "the same night".
- ch57: Cael drew it on the wall, not Feryn.
- ch58: "every one of Cael's nine"; the assessment's months.
- ch60:
  - the pin man's "borrowed" removed from Cael's knowledge — it lives only in Coss's ch28 cutaway;
  - Coss's week counted one way: seven days, "the Monday after" in order, and no "fortnight".

**Protect:**
- every exchange of the Darrow bout and its landing beats: "It had been there first.", "It made a noise like a latch.", "Darrow knelt.";
- every between-exchange break and every short speech line;
- Vell's count;
- Hesk's letter as read, and his *proud* letter;
- the daughter, the empty log page, the stranger, the grey slip;
- the final bench image as the last line;
- every protected line.

## Priority 1 — Remaining counting slips and say-it-once (cold read)

- **"unrated (vouched)" (ch54/57) against "assessed Cu (vouched)" (ch55/58).** Check what the ledger shows after the coordinator's ch58 months fix. Make the card's wording one thing throughout, or say in a clause why it reads differently in each place.
- **The "known things can't be put in a drawer" thesis is stated about seven times.**
  - Keep Hesk's and Vell's phrasings, and the *frightened* beat.
  - Trim Lira's paraphrase on the steps (ch56) and Cael's recap to Coss at the gate.
  - Cut or vary the rest.

## Priority 2 — Shape: merge same-place breaks; shorten the tail

- **Merge same-place scene breaks.** Merge ch57 s3+4, ch58 s5+6, ch59 s1–3 and ch55 s2+3; optionally ch55 s5+6 and ch60 s3+4. That is five to seven removals, bringing words per scene from 807 to about 920–970. Keep every between-exchange break.
- **Shorten the tail so the stranger and the grey slip stand clear.**
  - Cut ch59's market walk to the boys and the bread woman.
  - Compress ch60's register and query-form procedure by about a third.
  - Keep the daughter, the empty log page, and the final bench image as the last line.
- **Thin the tags.** Reporting verbs run about 105 per 10k against about 41. Thin chiefly in ch54 s5, ch56 s3 and s5, and ch59.

## Priority 3 — Join narration (sentence mean 12.34, FK 3.31)

- **Where:** join clipped narration runs that are one thought, in the reflective scenes:
  - ch54 s1;
  - ch55 s1–2;
  - ch56 s2;
  - ch58 s8;
  - ch59 s6;
  - ch60 s2 (Coss, the densest).
- **Long sentences:** let a few earn real length.
- **Leave alone:** the bout, and every speech line.
- **Target:** mean about 13.0–13.3, ≥40-word share no higher than 4.5%.

**Length.** Finish within 32,000–35,000 words. The tail cuts and the joins roughly offset each other. Do not pad.

## After the repair

1. Run:
   - `editions/monroe-1.3/tools/ed.sh overlap book-01-the-shattered 9` — must stay at 0 unprotected;
   - `ed.sh gates`;
   - the skeleton probe, as in your original task — stay at 5% or below;
   - `formula_metrics.py` on the seven chapters.
2. Append "## Repair r1" to `AUTHOR-REPORT.md`, with:
   - before/after metrics;
   - the overlap and probe results;
   - the card-wording decision;
   - the merges made;
   - a changelist by chapter.
3. Edit only the seven chapter files and AUTHOR-REPORT.md. Run no git commands.
