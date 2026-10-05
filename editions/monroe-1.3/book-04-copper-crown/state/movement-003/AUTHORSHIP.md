# AUTHORSHIP — Book 4, Movement 3 "Counted" (chapters 15–21)

| Field | Value |
|---|---|
| Public byline | Monroe Jackson |
| Seat | `oconnor` 1.3.0 |
| Foundation | Monroe Jackson 1.3.0 |
| Requested author | Opus (Claude Opus 5.5) |
| Actual runtime model | `claude-opus-5-5` (Claude Opus 5.5), as stated in this session's environment |
| Packet | `editions/monroe-1.3/book-04-copper-crown/state/movement-003/compiled-prompt.md` (movement brief: `editions/monroe-1.3/book-04-copper-crown/packets/MOVEMENT-003.md`) |
| Edition | `monroe-1.3` |
| Book | The Fractured Path, Book 4 — Copper Crown |
| Chapters | `editions/monroe-1.3/book-04-copper-crown/manuscript/chapter-15.md` … `chapter-21.md` |
| Date | 2026-10-05 |

One session. No chapter was drafted by anyone else. No coordinator correction arrived during the run (Movement 2 was in recheck; nothing was received).

**Reading before drafting.**
- The compiled prompt in full (1,504 lines, paged): profile, formula §§2–6 and 8–9, the movement brief, the preceding chapter (ch 14), the edition brief (event-list method, 8-word gate, working ranges), BOOK_MAP §§1–14, STATE_LEDGER with "After Movement 1" and "After Movement 2" and their coordinator rulings, CANON_RULES, owner voice.
- Movement 2 in full: `manuscript/chapter-08.md` … `chapter-14.md`; `state/movement-002/AUTHORSHIP.md` and `AUTHOR-REPORT.md` for the shape of these files.
- Source `books/book-04-copper-crown/chapters/chapter-06.md`, `chapter-07.md`, `chapter-08.md`, once each, in full, then closed. They were not reopened while drafting or repairing. Afterward only the probes' matched-pair output was read.
- `editions/monroe-1.3/OWNER-DECISIONS.md` (#7 Bracken *he*; #11 no new names used).
- Greps of Movement 1 and the edition's Books 1–3 for: the glance tally (none existed before this movement), the barge horns (M1 ch5, M2 ch14), the tier census (209 / 138 / 51 / 14 / 1; the Silver sheet covers Bronze and Silver), Havel (Ardenmere assessor, notebook), and Withrow (she).

**Method.** After the single source read, the author wrote a private event list in its own words (session scratchpad, outside the repo). It had its own calendar (days 51–110), entry points and inventions, among them: the stair tally with a control column of the wing's other four staff; four failed maps of the author's own design (clock, paper, company, rooms); the door-glass reflection in the empty east hall; the porter and his lamp paste; Lira's vote price; Brom walking into the wing corner; Seln re-sitting the boy's bench at night; the trade carried forward as the schedule error; the Current first-year at seventy-fourth; Lira reading the season entry upside down; the residence cards at the close.

**Honest note on source distance.** The warning in the brief proved right again. First drafts of several scenes tracked the source's sentence order from memory, with the page closed. The probe was run after every chapter (skeleton / close, first draft):

| Chapter | First draft | Action |
|---|---|---|
| 15 | 8% / 29% | Rebuilt whole; maps redesigned; control column added |
| 16 | 8% / 21% (scene 5: 32% / 53%) | Scene 5 (three grades) rebuilt as a dialogue with Lira |
| 17 | 15% / 38% | Council scenes 2–5 rebuilt: new speaking order (Brom answers Lira; Karis gives the sum), new staging, Lira's price, Karis on the stair |
| 18 | 20% / 45% | Rebuilt whole: Seln's window re-framed (courier, the rotation at the road foot, night visit to the bench); Path theory moved into a Karis dialogue |
| 19 | 10% / 25% | Scenes 3 and 5 rebuilt (receipt; the error read as an exchange) |
| 20 | 14% / 29% | Nyle/Merrick aftermaths rebuilt (the silence through particular faces; Rooke at the bench) |
| 21 | 16% / 37% | Rebuilt whole round the first-year at seventy-fourth and Lira at the door |

Every rebuild was written by hand from the event list. Scripts only listed flagged sentences and applied the author's exact before→after strings; they failed on any miss. The 25 rhythm splits (below) were each chosen by reading, at a point where the thought turns.

**Scratchpad note.** The session scratchpad turned out to be shared with other sessions: a helper file the author wrote there (`close.py`) was overwritten by another session's Book 2 version mid-run. The author recreated its own helpers under unique names (`m3_b4_*.py`). Nothing in the repository was affected.

**Final checks.**
- `ed.sh overlap book-04-copper-crown 3`: 0 unprotected, 8 protected.
- `ed.sh gates`: reader_standard=0, metadata=0, modern=0 on all seven chapters.
- `sweep_probe.sh book-04-copper-crown 3 3`: skeleton 1%, close 13%. The highest scene is ch 21 scene 5 at 7% / 27%, which carries the protected season log and the thought; unprotected it is about 20% close.
- `formula_metrics.py`: run once on the seven chapters (and once, early, on ch 15 alone for calibration). See AUTHOR-REPORT.md.

Only the seven chapter files and these two state files were written in the repo, plus scratchpad notes outside it. No git commands were run. STATE_LEDGER was not edited; the end-state for it is in AUTHOR-REPORT.md.
