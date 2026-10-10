# Repair brief — Book 6, Movement 4 (one consolidated same-author repair)

**Sources.** All three ran on Sol (codex), fresh context:
- `review-editorial.md` (editorial);
- `review-cold.md` (cold read);
- `source-tracking.md` (side-by-side source-distance read).

**Verdicts.**
- **Editorial:** repair one progression-count error, reconcile one calendar entry, then close. The movement succeeds at its intended work, and the following all pass:
  - the Reader Standard;
  - protected wording;
  - the source-reuse gate;
  - canon boundaries, including Seln, the cache and the Velmere letter;
  - the formula ranges.
- **Cold:** three non-structural priorities.
- **Source distance:** **FAIL, 85 tracked passages**, down from M3's 136. The stricter method worked where you rebuilt with your own mechanics: **ch24 and ch26 have 0**. The tracking concentrates in ch22 (28) and ch27 (26), with smaller clusters in ch21 (12), ch25 (13) and ch23 (6).

The current text is frozen in `pre-repair/`. Repair by reading, never by script.

## Coordinator rulings on your flags

1. **The meet date: ACCEPTED as day 71** (the hall postponement for river repairs, eight days; the false quarter). The M4 chain stands: day-68 council, day-71 meet, the 23-day sealed-letter interval, the day-75 sitting and day-76 gate. I correct the M3 ledger's day-63 entry at the M4 close; the M3 page stays true as written. Make sure every M4 interval agrees with day 71.
2. **The escort order:** ACCEPTED. The six-word heading *In the matter of Caelen Hesk-ward.* makes 81 words read aloud (#44); the order's text is verbatim and protected.
3. **The hearing-provision plant for Karis's M8 closing:** ACCEPTED. Keep it light.
4. **Seln and the cache:** both reviewers confirm the boundary holds (not told; the cache's content never stated; the letter sealed). Keep it exactly so.
5. **Lira's 27 into the meet record under the hall's seal:** ACCEPTED, in the #38 bands. It may stand on her file for the advancement evaluation.
6. **Progression vocabulary density:** noted, not a must-fix. Let the P1 redraft thin it where it is restated.

## Priority 1 — Source distance (must fix)

The method that produced 0 in ch24 and ch26 is the method to use: build the scene from your own mechanics and a way in that the source does not have.

1. **REDRAFT ch22 and ch27 WHOLE.**
   - Work from EVENT-LIST.md, the packet and BOOK_MAP only.
   - **Do not reopen the source chapters at all for these two.** You have read them, and that memory is what keeps the order.
   - Choose a new first scene-moment and a new internal order for each scene. Choose a different carrier for each beat where you can: object, Log, dialogue or silence.
   - Keep every protected and packet line: *Prepare both roads*; *I'm not leaving the room while the text still works*; *It was the night we asked*; the Anchor query; the faceless-layer line; the closing schedule line; and the rest.
   - Keep every planned event, plus Seln's cutaway at the same altitude: he is not told, and the cache's content is never stated.
2. **RE-COMPOSE the tabled passages in ch21, ch23 and ch25**, passage by passage. The keys are in `source-tracking.md`.
   - Start each passage from a different link.
   - Drop or invert one link, or let one happen off-page and arrive only as its consequence.
   - Never synonym-swap, never split sentences.
3. Leave ch24 and ch26 as they are, apart from P2's narrow fixes.

## Priority 2 — Continuity and reader (must fix)

1. **ch24:117–139 and 157–161: Lira's burst ledger** (editorial).
   - The crossways-board attack is called a burst. Two escapes are then numbered fourth and fifth, the text says she has spent five, and the next attempt is called sixth.
   - Make the launch at 117–119 an ordinary push or drive, or make the smallest other change, so that she has spent exactly five before E4.
   - Recheck every ordinal, Brom's count, Rooke's bill, and "borrowed against tomorrow".
   - Do not shorten the fight.
2. **ch23, from the departure through the host-provision explanation** (cold read). Compress the duplicated reminders: prior rulings, travel context, meet procedure and program rationale.
   - Keep the colors, Rooke's reason for a permanent meet record, Lira's fear of being "a good loss", and what is needed to understand the exhibition.
   - Some of this may fall away naturally in the P1 re-composition.
3. **ch26–27: the fourth rider is solved too many times** (cold read). Trim one layer of restatement, most naturally the counsel's immediate post-departure explanation, so the physical evidence carries the inference.
   - Keep the staged observation, the gate confrontation, the chalk reconstruction, and the explicit blanks around the Anchor's reach, rate and price.
   - ch27's part of this goes into the P1 redraft.
4. **The paper/ground/floor/receipt metaphor, movement-wide** (cold read). Thin the echoes after the new meaning has landed.
   - Keep Lira's "It's not ground. It's a floor", the paired papers at the rail, Jent's answer about evidence, and Seln's still hands.
   - Fix ch26's same-speaker quotation seam at "So you get one question out of this, and you get it once."

## After repair

1. From editions/monroe-1.3, run `bash tools/ed.sh gates book-06-the-compacts-hand 4` and `bash tools/ed.sh overlap book-06-the-compacts-hand 4`. Targets: gates 0; overlap 0 unprotected.
2. From the worktree root, run `bash editions/monroe-1.3/tools/sweep_probe.sh book-06-the-compacts-hand 4 4`.
3. Hold the length near 32,700 words. Do not pad.
4. Append "## Repair r1" to AUTHOR-REPORT.md, covering:
   - ch22 and ch27: the new way into each scene;
   - ch21, ch23 and ch25: the re-composed keys, each with its old chain and new chain;
   - the P2 fixes;
   - anything you declined, and why.
5. No git.
