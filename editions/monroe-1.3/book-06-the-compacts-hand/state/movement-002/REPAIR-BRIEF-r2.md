# Repair brief r2 — Book 6, Movement 2 (bounded second repair: Priority 2 only)

**Source:** `recheck-r1.md`, from a fresh-context Claude Opus 5.5 seat.

**Verdict:** SECOND REPAIR, limited to Priority 2. Everything else in r1 is RESOLVED.
- **Already resolved:** the ch8 renewal against B4; the lane measure; the ch12 trial (five bursts, Rooke's rule, the contact stamp); Brom's panel; Jent's origin; knowledge boundaries; protected lines; quotes; length.
- **Already applied by the coordinator:** the recheck's nine line fixes.
  - ch8: the Log ends on *wondering*; "By supper" for the annex.
  - ch9: one guild wouldn't let Lira in the door.
  - ch10: who "the five" are.
  - ch11: Withrow's coach morning; "Brom's docket"; the boards ahead of the stamp.
  - ch12: the boards ahead of the stamp.
  - ch13: Havel's looks, which now include the Ardenmere pump step and the third look on the oak (B4 ch54:81).

  Re-read each in context. Do not undo them.

The current text is frozen in `pre-repair-r2/`.

## The one job: re-compose the 18 passages

These 18 passages still keep a source sentence's content and order. They are tabled in `recheck-r1.md` under "### Priority 2: PARTIAL", with the manuscript location and the source sentence for each:

| Chapter | Passages |
|---|---|
| ch10 | the close of Jent's conference; the "Thank you" frame around the compliment; the Log (its last sentence is unchanged from pre-repair) |
| ch11 | most of Withrow's two speeches |
| ch12 | Bracken's "anticipated" lines; Karis's *admit* turn |
| ch13 | the bow; Brom's Havel exchange; Seln's lines in the coach and on the step; the room's layout; Seln's seat; the reading over Cael's shoulder |

**Method.** Same-author, by reading, in place:
1. Close the source.
2. Go back to your EVENT-LIST.md and write each beat afresh, from a new entry point and in a new order where the plan allows.
3. Do not synonym-swap. Do not cut a source sentence into shorter pieces that keep its content and order.

**Keep:**
- every protected and packet line verbatim;
- every fact and ruling the recheck verified;
- the scene shapes and the movement's length, about 28,200 words. Do not pad.

**After:**
1. Run `bash tools/ed.sh gates book-06-the-compacts-hand 2` and `bash tools/ed.sh overlap book-06-the-compacts-hand 2` from editions/monroe-1.3. Targets: gates 0, overlap 0 unprotected.
2. Run `bash editions/monroe-1.3/tools/sweep_probe.sh book-06-the-compacts-hand 2 2` from the worktree root. It must not rise.
3. Append "## Repair r2" to AUTHOR-REPORT.md, listing each of the 18 passages with its old entry point and its new one.
4. No git.
