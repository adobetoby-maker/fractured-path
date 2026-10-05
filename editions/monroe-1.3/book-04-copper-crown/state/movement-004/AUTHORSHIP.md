# AUTHORSHIP — Book 4, Movement 4 "The Line" (chapters 22–29)

| Field | Value |
|---|---|
| Public byline | Monroe Jackson |
| Seat | `oconnor` 1.3.0 |
| Foundation | Monroe Jackson 1.3.0 |
| Requested author | Opus (Claude Opus 5.5) |
| Actual runtime model | `claude-opus-5-5` (Claude Opus 5.5), as stated in this session's environment |
| Packet | `editions/monroe-1.3/book-04-copper-crown/state/movement-004/compiled-prompt.md` (movement brief: `editions/monroe-1.3/book-04-copper-crown/packets/MOVEMENT-004.md`) |
| Edition | `monroe-1.3` |
| Book | The Fractured Path, Book 4 — Copper Crown |
| Chapters | `editions/monroe-1.3/book-04-copper-crown/manuscript/chapter-22.md` … `chapter-29.md` |
| Date | 2026-10-05 |

One session. No other author drafted any chapter. Movement 3 was in recheck during the run, and no coordinator correction arrived.

**Reading before drafting.**
- The compiled prompt in full (1,515 lines, read in pages). That covered the profile, the formula §§2–6 and 8–9, the movement brief, the preceding chapter (ch 21), the edition brief (event-list method, 8-word gate, working ranges), BOOK_MAP §§1–14, and STATE_LEDGER with the "After Movement 1–3" blocks and their coordinator rulings. It also covered CANON_RULES and the owner voice.
- Movement 3 in full: `manuscript/chapter-15.md` … `chapter-21.md`, plus `state/movement-003/AUTHORSHIP.md`, `AUTHOR-REPORT.md` and `REPAIR-BRIEF.md`, for the shape of these files and the rulings.
- `editions/monroe-1.3/OWNER-DECISIONS.md`: #7 Bracken *he*; #9 "since his Kindling"; #11 Abbot pending, so the placeholder was used.
- Source `books/book-04-copper-crown/chapters/chapter-09.md`, `chapter-10.md` and `chapter-11.md`, read once each in full and then closed. They were not reopened while drafting or rebuilding. Afterward only the probes' matched-pair output was read.
- Targeted greps of the edition for continuity:
  - Book 3 ch25–36: the whitewashed room, twenty-two sessions, the match, *Acquisition: directed*, and Karis's "I want it to be me".
  - Book 4 ch9: Fiske's first meeting with Lira and the "minute and a half".
  - Book 4 ch10, ch12 and ch13: the Ash instructor is a stooped woman of about sixty; Compression "nobody had ever seen"; the plate trial.
  - Book 1: Shield Path panes.

**Method.** After the single source read, the author wrote a private event list in its own words (session scratchpad, outside the repo, `m4-events.md`). Drafting worked from that list, the map and Movement 3. The list carried its own calendar, entry points and inventions, among them:
- Karis's biscuit tin of notes, and her six days of not adding pieces.
- The minute's rules.
- The imagined bout Cael cannot lose (the method's failure, re-found).
- The wash-house sandbag rig.
- The Log read at breakfast, as the procedure in action.
- The Mire round answering the Iron girls' M3 question.
- Stopping the counting as a standing decision ("no leaning").
- The creaking third stair in Lira's window.
- The Shield fifth-year's breath.
- Bracken's top-line half-sheet, and Lira choosing the fifteenth.
- Rooke's Socratic bench.
- The dropped book, the Ash instructor's check, and Rooke's "You went toward it".
- The nine-dot map of hall three.
- Seln's imagined young auditor.
- Karis's box and her watcher log.
- Jask turning his dial to the wall.
- The bout told through the evasion sequence Lira teaches Fiske in the first exchange.
- The night at Brom's post.

**Honest note on source distance.** The brief's warning held again, and more strongly than in Movement 3 for the source's most vivid passages. Several first drafts tracked the source's sentence order from memory with the page closed. The probe was run after every chapter. Skeleton / close, by stage:

| Chapter | First draft | After rebuild | Final | Action |
|---|---|---|---|---|
| 22 | 15% / 36% | 4% / 21% | 2% / 15% | Rebuilt whole: new staging (Brom from the taking-apart, Karis's columns as *Greyvane / here*), the voices moved to ch 23 |
| 23 | 20% / 38% | 4% / 23% | 1% / 12% | Rebuilt whole. Brom argues from his own floor; Cael reads the Greyvane entry aloud; the night becomes an imagined bout he cannot lose; the drill gets its own physics (hammer and bell) |
| 24 | 8% / 25% | 2% / 21% | 1% / 11% | Rewritten fuller; the Log lines recomposed; the light scene re-entered |
| 25 | 5% / 21% | — | 0% / 13% | Lines recomposed; the half-sheet and Lira's decision added |
| 26 | 8% / 23% | 2% / 16% | 2% / 15% | Rooke's bench rebuilt as a Socratic exchange with different reasons |
| 27 | 14% / 41% | 5% / 26% | 0% / 13% | Rebuilt whole: the dropped book as entry, new physics language (a cart on a hill; a wave off a seawall), a different procedure, the night as a drawn map |
| 28 | 14% / 32% (Seln scenes 33% / 25%) | 2% / 19% | 1% / 13% | Seln window rebuilt around his imagined young auditor |
| 29 | 40% / 54% | 7% / 24% | 1% / 11% | Rebuilt whole: the bout is told through the sequence Lira teaches Fiske; Karis's four lines; Fiske's speech re-contented (the form and the pen); the night moved to Brom's post; the Log in a new form |

Every rebuild was written by hand from the event list. Scripts only listed flagged sentences and applied the author's exact before→after strings, and they failed on any miss.

The rhythm joins (about 105, listed in AUTHOR-REPORT.md) were each chosen by reading, at a point where the thought continues. They were applied the same way, with exact strings.

**Scratchpad note.** Helpers were kept under unique names (`m4b4_*`) in the session scratchpad, following Movement 3's warning that the scratchpad is shared. Among them was a rough sentence counter, calibrated against Movement 3's published metrics: it reads 13.84 on ch 15–21, against formula_metrics' 13.86. It was used for drafting hygiene in place of repeated formula_metrics runs.

**Final checks.**
- `ed.sh overlap book-04-copper-crown 4`: 0 unprotected, 12 protected.
- `ed.sh gates`: reader_standard=0, metadata=0, modern=0 on all eight chapters.
- `sweep_probe.sh book-04-copper-crown 4 4`: skeleton 1%, close 13%. Every chapter is at or under 2% / 15%.
- `formula_metrics.py`: run once, on the eight chapters, after the rhythm joins. A light terminology pass afterward added about 300 words; it was recounted with the calibrated rough counter, not a second metrics run. See AUTHOR-REPORT.md.

In the repo, only the eight chapter files and these two state files were written. Scratchpad notes stayed outside it. No git commands were run. STATE_LEDGER was not edited; the end-state for it is in AUTHOR-REPORT.md.
