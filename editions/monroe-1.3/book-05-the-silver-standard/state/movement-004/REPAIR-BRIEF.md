# Repair brief — Book 5, Movement 4 (one consolidated same-author repair)

**Sources.** `review-editorial.md` and `review-cold.md`, both from Claude Fable, fresh context, on the review seat.
The cold read saw the manuscript only.

**Verdict.** This is a strong, close-to-clean movement, and both readers want to go to Norhold. Among the best pages
in the edition:
- the circular at the waystation;
- the builder bout;
- the barge-master's bed;
- Gault's fourth;
- Ephram's "North.";
- the chapter 24 lamps.

The editorial checked the movement against the rulings, and all of these pass:
- #38 figures;
- one Iron draw with sound bracket arithmetic;
- bursts per day;
- Ember on contact only;
- Pressure on the RIGHT shoulder, and the RIGHT forearm;
- Compression unseen and Shadow at zero;
- the year counts;
- the limits on Vastin, Havel and Karis;
- no leaks of seasons, weekdays or new names;
- protected wording verbatim, and overlap 0 unprotected.

All three cutaways are identifiable. Vastin's is the movement's best non-fighting prose.

Pre-repair text is frozen in `pre-repair/`. Repair in reading order, in place, by reading — never by script.

## Coordinator rulings on your flags (OWNER-DECISIONS #40 new)
1. **Builder as the semifinal, and Lira over Ephram in the final:** ACCEPTED. It is the only order that works.
2. **Shared third with no bout for third:** ACCEPTED as regional custom.
3. **Withrow's nine words:** ACCEPTED.
4. **Ember shown publicly (#40):** from M4 on, three capabilities have been SHOWN ON PUBLIC FLOORS: Wind, the Iron read,
   and Ember at its documented two-contact rate. The record of five is unchanged. Your inventory line "the record holds
   two of them public… shown a third at its documented rate" stands.
5. **The Shield mechanics** (panes, breath-plant-pane, oldest-first renewal): ACCEPTED as new canon. P3 softens the one
   absolute so that M7's weave can deny rhythm, order and the plant while keeping layers and ageing.
6. **Gault's "bout for third" (#40):** Norhold has no individual third-place bouts; its third place is the team trial.
   Make Gault's continental fourth "fourth on the figures", or similar, and remove the bout for third.

## Priority 1 — Two count defects (editorial)
1. **The barge-master's second touch (ch23, ll.111–127)** lands with no exchange break, so the bout reads as two
   touches inside one exchange. Add 15–30 words between l.113 and l.115:
   - Cael walks his circle with the forearm against his side;
   - the steward calls the fourth;
   - the barge-master plants "somewhere new".

   Keep "late in the exchange" once the exchange exists. Nothing else in the bout moves.
2. **The first confluence day.** All four Iron quarterfinals finish by noon, yet later scenes contradict that. Do NOT
   move the quarterfinals; make four or five line edits instead:
   - Lira arrives "between her bouts" becomes "after her bouts".
   - At dusk, replace the Iron quarterfinal "still running" with the main hall's lamps over the clerk chalking
     tomorrow's card to empty benches.
   - Lira watches the builder's two bouts that day, not "three": she sits "in the back row until the hall emptied,
     drawing his two bouts on her knee". Next morning she says, "I watched both of his yesterday, and then I watched
     them again in my head till the lamp went out."
   - Make "both boys who fought him today" agree.

## Priority 2 — Say it once (cold)
- **ch25, the Shield-reserve section.** It re-teaches a lesson already taught twice. Compress it by roughly a third:
  - fold the restatement paragraphs ("It was an honest clock and a slow one…" and "The numbers had changed. The plant
    had not…");
  - move the one new development, the reserve making his plant *smaller*, earlier, so the section ends on a problem
    not yet solved;
  - keep the reserve's "That's not fair" exchange as a scene;
  - keep "I think Shield is solved".
- **ch26, the inventory Log.** Reduce it to the lines that carry new weight: Ember "two a round on the Shield reserve
  since… a habit kept only in public is a costume", and "Six. The record holds two of them public… The doctrine
  holds". Let Seln's section be where the two-a-round observation reaches the reader. That is roughly 150–250 words
  out. Do not touch Seln.

## Priority 3 — Line and canon phrasing (both)
- **ch25 l.279.** "a declaration needed the floor under it" is stated as a law, but ch22 already shows it isn't one,
  and M7's weave must deny it. Make it the reserve's limit: "the reserve had never been taught to set a pane without
  the floor under it, and perhaps nobody at Iron had".
- **ch26 l.105 and l.129.** "on a meet record" becomes "a seat's report" or "the confluence seat's report". Meet
  records are figure-only.
- **ch26 l.101.** The right shoulder has not been asked for anything "since the recess" becomes "since the mill town's
  plate".
- **ch23, "four were in the band above it" (cold).** This inverts the book's own scale. Make it "below it", or add the
  half-clause that makes the band scale legible.
- **The two other cold-read snags.** One needs a section rule or a named Cael. The other is the region-sends-three
  passage: keep Karis's four sums and her pencil laid "very straight", and cut the explanatory clauses to "the region
  would send three north, and there was no longer a way through".
- **Gault's fourth.** Per ruling 6.
- **To taste.** Thin "said" tags where the speaker is already clear (about 74 per 10k against roughly 41).

**Length.** Finish within 32,500–34,500 words.

## After the repair
Run:
- `ed.sh overlap book-05-the-silver-standard 4` (0 unprotected);
- `ed.sh gates`;
- `sweep_probe.sh book-05-the-silver-standard 4 4` (≤ 5% skeleton, ≤ 13% close);
- `formula_metrics.py` on the seven chapters.

Hold the ≥40-word share at 2.5% or above. You are at the floor, so do not split long sentences further.

Append "## Repair r1" to AUTHOR-REPORT.md with:
- the confluence day's bout schedule;
- before/after metrics;
- the changelist, by chapter.

Edit only ch20–26 and AUTHOR-REPORT.md. Run NO git commands of any kind.
