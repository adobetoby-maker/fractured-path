# Repair brief r2 — Book 3, Movement 6 (narrow, same author)

Source: `recheck-r1.md` (Claude Fable 5.1). Your r1 rebuild worked where you changed a scene's
shape: skeleton share fell from 23–34% to 5–16% per chapter, and about 12,000 tracked words fell to
about 3,500. What is left is where a packet-fixed speech was re-worded in place. Read §1 ("Scene by
scene" and the summary table) and §5 of the recheck for the quoted pairs and the handles.

**Already applied by the coordinator. Do not redo these:**
- the aide's "Both days";
- Lira's "a sitting coming";
- the charter beat moved from the end of ch43 to after the ch44 breakup paragraph, with Karis no longer sent to the residence wing;
- the digests ("went back … for the rest of");
- Prynn's line attributed with "said Prynn" after the first fragment;
- the double blank lines;
- "This is your enrollment, not mine to trade." restored exactly (now a protected pattern).

The other two altered lines stay as you have them.

## The work — the event-list method, source closed

For each passage, write a private event list from your own manuscript, not from the source. Keep
every event and every quoted or protected line. Then rewrite the passage with a different spine.
Do not reopen source chapters 15–17.

1. **ch44 scene 1, the division of labour (~900 words). Rebuild it whole.** This is the one scene
   the re-touch did not move.
   - Let the claims come out of order and by interruption. Lira comes first: she has been silent and furious.
   - Brom's witness line can be said on the stair.
   - Make the plan on Karis's ruled page, each name written as it is claimed.
   - Replace Cael's "what he needed most" reflection with an act: he writes Lira's hour into the page before his own.
   - The scene still opens into the breakup paragraph and the moved Karis beat. Keep that order.
2. **ch44 scene 4, from "Nothing left open overnight" to "a third way a thing could go unscarred" (~500 words).**
   - The rules become a card he reads and breaks one by one.
   - The "angry with it / studying it" exchange moves, or becomes Prynn's question from the high desk mid-page.
   - The three ages are read off the concordance's columns.
3. **ch45 scene 4, from "Is that a compliment?" to "Fourth shelf, second case" (~510 words).**
   - Cael's true answer comes before the clever one, or Prynn asks with the tea tin in hand and her back half turned.
   - Prynn reads the argument summary off the page; Cael does not say it.
4. **ch46 scene 5, from "It held four." to "It's also the only true one I've got." (~400 words).**
   - Carry the page-as-page handle through: the four as four lines in his hand. The fourth's eleven words are counted, not quoted.
   - "How big it was" becomes a margin note.
5. **Recommended, in the same pass:**
   - **ch43 council:** re-cut Naveth's three speeches and Cael's third-way speech so the points come in a different order. For example, the withdrawal is named before the reason the merits are lost.
   - **ch42 scene 4:** give the three family speeches their own sentence shapes.
   - **ch42 scene 3:** the Quenna stair paragraph.

Keep each passage's length about the same. The movement must stay within 35,500–38,500 words,
with sentence mean ≥13 and words per scene in range.

## After

1. Run `editions/monroe-1.3/tools/ed.sh overlap book-03-no-path-given 6` (must stay 0 unprotected), `ed.sh gates`, and `formula_metrics.py` on the seven chapters.
2. Append "## Repair r2" to `AUTHOR-REPORT.md` with a per-passage event list (one line each), the metrics, and the overlap result.
3. Edit only ch42–46 and AUTHOR-REPORT.md.
4. Run no git commands.
