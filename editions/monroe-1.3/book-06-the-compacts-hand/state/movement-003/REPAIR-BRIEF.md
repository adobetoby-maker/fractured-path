# Repair brief — Book 6, Movement 3 (one consolidated same-author repair)

**Sources.** All three ran on Sol (codex), an independent model family, with fresh context:
- `review-editorial.md` (editorial);
- `review-cold.md` (cold read);
- `source-tracking.md` (a dedicated source-distance read).

**Verdict.**
- **Editorial:** a focused repair, then a targeted recheck. Structurally successful, no scene-level rewrite needed.
- **Cold read:** three priorities, all non-structural.
- **Source-distance read:** **FAIL, with 136 genuine tracked passages.** These are passages that keep a source sentence's content and order, through varied words, split sentences, or near-verbatim text.

| Chapter | Tracked passages |
|---|---|
| ch14 | 41 |
| ch15 | 13 |
| ch16 | 13 |
| ch17 | 9 |
| ch18 | 8 |
| ch19 | 20 |
| ch20 | 32 |

The 8-word gate (0) and the probe (19%) both understate this, as they did in M2.

**What every reader verified holds:**
- calendar;
- bodies;
- power limits;
- knowledge and reserved disclosures (Seln not told; the M6 reveal preserved; no falsification, [UNBOUND], Tide or Architect);
- roles, ranks and names;
- Reader Standard;
- every protected line exact.

None of the repair below may disturb those.

The current text is frozen in `pre-repair/`. Repair by reading, never by script.

## Coordinator rulings on your flags

1. **Seln and Shadow:** you were RIGHT. "B6 Ch15" means source Ch15, which is the edition's M6. My instruction was wrong. Seln is not told in M3.
2. **Calendar (petition day 41, refusal day 44, received day 45; sittings days 47 and 54; inventory named day 49):** ACCEPTED.
3. **Daeva's statement set aside at the third sitting:** ACCEPTED.
4. **The Velmere letter: CHANGE IT (editorial, mandatory).** The day-45 letter in ch16 must stay SEALED. Brom pockets it unopened, and the table keeps its agreement not to ask. That letter is the one BOOK_MAP §4e #10 carries unopened to M7. Keep the table's restraint and Brom's visible cost.
5. **New canon: ACCEPTED,** pending the recheck:
   - the gallery over wing three's west door;
   - Rooke shutting the program floor from day 46;
   - a burst spent small to look like a step;
   - the fee office sealing archive requests and querying standing;
   - the gate lodge's road column, kept since "the year of the thieves";
   - the lane's dust casting a shadow under lamps.
6. **Hesk's surveyor's level:** keep it. Nobody draws the lesson aloud.
7. **The added private-floor scene (ch20 opening):** ACCEPTED.

## Priority 1 — Source distance (source-tracking.md; must fix)

The table in `source-tracking.md` gives chapter:line, your opening words, the source sentence each one follows, and its kind. Its last section, "New entry points and beat orders for dense scenes", suggests a way in for each dense scene. Method:

1. **Rewrite the source-shaped lines of `EVENT-LIST.md` first, in your own words.**
2. **REDRAFT WHOLE, from the cleaned event list, with the source closed:**
   - **ch14** (41 passages; the Vastin chapter). Find a different way into each of its five scenes and a different order of beats where the plan allows. Keep every protected line and every planned event, including the two-sentence denial and the folder tab.
   - **ch19** (20 passages; the most continuously tracked chapter). Keep Hesk's protected letter whole.
   - **ch20 scenes 2–6** (the hearing; 32 passages). Keep scene 1, the new private floor, as it is.
3. **RE-COMPOSE BY HAND, passage by passage, in ch15–18** (43 passages). Use a new way into each passage and a new order of beats. Do not swap synonyms or split sentences.

Do not count as tracking, and keep verbatim: protected lines and packet lines.

## Priority 2 — The hearing and the middle (cold read)

These go inside the P1 redraft.

1. **ch20 hearing:** while redrafting, give it two short orientation beats at Cael's level, at the major transitions. Say what has just been conceded and what is still dangerous, phrased as consequences, not definitions. Keep the full hearing and its four-part architecture: Jent's voluntary withdrawal of a false overreach, the steel rule, and the two-paragraph ruling.
2. **ch15 to ch16:** the pamphlet market, the post baskets, the observer log, the fee-office query and the cost column all run in the same delivery rhythm: paper appears, a reader extracts it, Cael concludes. Compress duplicated setup, or leave one implication unglossed until Seln's beans. Do NOT remove the gallery log, the fee-office query, Brom's letter or the cost column.

## Priority 3 — Precision and rhythm

1. **ch15:** "three other towns" against Brom's "other two towns". Settle the number of towns so the arithmetic adds up.
2. **ch20:** "*Valid: held. To proceed: held. Both.*." has a doubled full stop. Fix it.
3. **Rhythm (editorial):** the sentence mean is 13.11 and the median 9. In the explanatory runs, join adjacent clauses that form one thought, and add paragraph turns where the speaker, object or inference changes. Do not chase the SD target, lengthen dialogue, or shorten scenes. Most of this happens naturally in the P1 redraft.

## After repair

1. From editions/monroe-1.3, run:
   - `bash tools/ed.sh gates book-06-the-compacts-hand 3`
   - `bash tools/ed.sh overlap book-06-the-compacts-hand 3`
2. From the worktree root, run `bash editions/monroe-1.3/tools/sweep_probe.sh book-06-the-compacts-hand 3 3`.
3. Targets:
   - gates 0;
   - overlap 0 unprotected;
   - close band well down from 19%.
4. Hold the length near 34,000 words. Do not pad.
5. Append "## Repair r1" to AUTHOR-REPORT.md: each redrafted chapter or scene with its new way in, the count of re-composed passages, and anything you declined, with the reason. Correct your ledger lines (the Velmere letter).
6. Run no git commands.
