# Run ledger — Fractured Path, Monroe 1.3 edition

Append-only. One line per event. The orchestrator writes this; seats do not.

## Standing decisions (2026-10-01)

- Owner: rewrite the whole series through O'Connor 1.3 on Monroe 1.3; Opus 5.5 author;
  ~300,000 words per book; when complete, render every chapter with Breeze and publish
  as a new edition. Original request named Books 3–7; owner then widened it to the series.
- Edition lives in `editions/monroe-1.3/` on branch `edition/monroe-1.3`, worktree
  `/Users/drive/fractured-path-monroe13`. The current edition (`books/`) is untouched.
- Order: books are planned in parallel (each book's entry and end states are fixed by
  canon, so plans do not depend on rewritten neighbours); drafting runs in two lanes —
  Book 1 (series order) and Book 3 (first book the owner named) — then continues.
- Review seat: Sol via `codex exec` while it has usage, otherwise Claude Fable 5.1 (editorial pass with formula check and canon; cold
  read with manuscript only). Repair: the same Opus author, at most three priorities.
- Names: existing canon names kept; registry collisions left for the owner. New minor
  names are listed per book under "Names pending owner approval".
- Metrics: `tools/formula_metrics.py` (method in its docstring).

## Events

- 2026-10-01 18:15 — edition scaffold, brief, metrics tool, driver (`tools/ed.sh`) written.
- 2026-10-01 18:16 — planners launched (Opus): Books 1, 2, 3, 4.
- 2026-10-01 18:30 — Book 1 plan done (Opus 5.5, `claude-opus-5-5`): 9 movements, 60 chapters, 300k budget; 0 names required ("Ebbe" optional). Source conflicts logged in the planner's report: bible "eleven people died" vs Book 1's four cases (plan follows Book 1); Pellin's gender (Book 1 woman vs Book 6 Ch9 "a man") — owner decision; source Ch5 breaks the Reader Standard once ("Damned if I know") — the edition does not carry it.
- 2026-10-01 18:32 — Book 1 Movement 1 compiled (83 KB; ch 1–6, ~30k) and author launched (Opus). Book 5 planner launched.
- 2026-10-01 18:34 — Book 2 plan done (claude-opus-5-5): 8 movements, 60 chapters, 300k. Names pending: Bede, Maud. Contradiction fixes proposed in its §11. Recorded in OWNER-DECISIONS.md (#3, #4). Book 6 planner launched (told: Pellin per Book 1; five travelers at the B6→B7 seam).
- 2026-10-01 18:38 — Book 4 plan done (claude-opus-5-5): 9 movements, 62 chapters, 300k. Conflicts C1–C12 in its map; C1/C2/C3/C7 and names Gwen/Abbot recorded as OWNER-DECISIONS #7–#11 with interim defaults. Book 7 planner launched.
- 2026-10-01 18:41 — Book 3 plan done (claude-opus-5-5): 8 movements, 61 chapters, ~300k; 21 source conflicts with fixes in its §12 (Wray kept a woman; the older-word chapter's "before Arbiters / 400 years" reined in to Book 6's dating and Book 8's reveal). Names Oona/Hobb/Gerda pending (#12). Book 3 Movement 1 compiled (ch 1–8, ~37k; previous = source Book 2 ch24) and author launched (Opus). Policy: pending names are drafted under the proposed name, not as brackets.
- 2026-10-01 18:47 — Book 1 Movement 1 drafted (claude-opus-5-5): ch 1–6, 29,402 words (tool). Gates clean. Formula drift: sentence mean 8.77 (14.6), ≤5w share 41%, ≥40w 0.3%, FRE 90.5 (72.3), FK 2.82 (6.8), 11.9 breaks/10k (8.7); paragraph median 15 (18) close. New facts pending owner: Joren's declaration [Rooted Stance]; Garrik a widower. Rhythm calibration appended to EDITION_BRIEF (applies to every later compile); same correction sent mid-run to the Book 3 M1 author (after its ch 2). Sol reviews (editorial + cold) launched.
- 2026-10-01 18:49 — Sol (codex, ChatGPT plan) is out of usage until 2026-10-03 12:52 PM; both B1 M1 reviews exited without output. Review seat moved to Claude Fable 5.1 (a different model from the Opus 5.5 author; fresh context; labelled in each review). ed.sh review now compiles only; REVIEW_SEAT=codex restores Sol launching. Fable editorial + cold read launched for B1 M1.
- 2026-10-01 18:50 — Book 5 plan done (claude-opus-5-5): 9 movements, 60 chapters, 300k; no new names; 18 source conflicts in its §12 (C4 "four centuries" early hint and C5 "five people knew both ledgers" leak are cut). C1–C3 recorded as OWNER-DECISIONS #16–#18. Book 8 planner launched.
- 2026-10-01 18:57 — Book 6 plan done (claude-opus-5-5): 9 movements, 60 chapters, 300k. Calendar restructured to one academic year with a new movement 7 and the provisional "clean door" (OWNER-DECISIONS #19). Five travelers kept; Pellin per Book 1. Source is furthest from the formula (sentence mean 19.5, ≥40w 15.3%, paragraph median 49). Cold read for B1 M1 in (Fable): keep-reading yes; priorities = repetitive Hesk/Cael middle (ch3–5), doubled Tuesdays realization, four one-sentence rule gaps.
- 2026-10-01 19:00 — B1 M1 editorial review in (Fable 5.1, fresh context): no verified canon violation; Reader Standard pass; all protected lines exact; formula drift short on every sentence metric; POV 100% Cael (later movements must carry ~14.4% cutaway). Coordinator rulings: Hesk's Ardenmere line is source Ch3:177 → keep; Arbiter must be dark after the word (BOOK_MAP §1); rename the Ch2 reel's "circuit". Pre-repair frozen in state/movement-001/pre-repair/. REPAIR-BRIEF.md written (rhythm gear-change; line-level continuity/rule gaps; say-it-once with the room reused for story, 28.5–31.5k). Same author resumed for repair r1.
- 2026-10-01 19:03 — Book 7 plan done (claude-opus-5-5): 8 movements, 60 chapters, 300k; POV Cael 86.6%; no names; Teague's crew never named (Book 8 kills the young one unnamed); straightedges read true at B7 close (Book 8 Ch1 owns the first error). Conflicts C1–C11 in its §12; C1 (cart/horse/purse) and C2 (mule) recorded as OWNER-DECISIONS #23–#24.
- 2026-10-01 19:08 — Book 3 Movement 1 drafted (claude-opus-5-5): ch 1–8, 36,746 words; gates clean; protected lines in. Metrics: sentence mean 9.66 (ch1–3 ~8.3, ch4–8 ~11.5 after the mid-run correction), ≤5w 38.6%, ≥40w 1.1%, FK 3.39, 482 words/scene (target 950). Author rewrote ~20 sentences in ch1–2 that echoed source wording (source-reuse rule). New beat: Compression wakes in D1 and Cael withholds it (bruised forearm). Day-8 Lira review and Brom evaluation left off-page for M2. Pre-repair frozen. Fable editorial + cold read launched.
- 2026-10-01 19:08 — FIX: ed.sh gates had been exiting silently under pipefail (grep with no match); fixed. Re-run: B1 M1 and B3 M1 both 0 reader-standard / 0 metadata / 0 modern. (B1 M1 was also covered by the author's and reviewer's own greps.)
- 2026-10-01 19:11 — Book 8 plan done (claude-opus-5-5): 9 movements, 60 chapters, 300k; no names; conflicts C1–C14 with working rulings in its §12 (Vastin's age unstated per #17; academy spans anchored to events per #9/#18; follows the Rune notice over the bible's Bronze). ALL EIGHT BOOKS PLANNED: 69 movements, 483 chapters, ~2.4M words.
