# AUTHORSHIP — Book 4, Movement 2 "Baseline" (chapters 8–14)

| Field | Value |
|---|---|
| Public byline | Monroe Jackson |
| Seat | `oconnor` 1.3.0 |
| Foundation | Monroe Jackson 1.3.0 |
| Requested author | Opus (Claude Opus 5.5) |
| Actual runtime model | `claude-opus-5-5` (Claude Opus 5.5), as stated in this session's environment |
| Packet | `editions/monroe-1.3/book-04-copper-crown/state/movement-002/compiled-prompt.md` (movement brief: `editions/monroe-1.3/book-04-copper-crown/packets/MOVEMENT-002.md`) |
| Edition | `monroe-1.3` |
| Book | The Fractured Path, Book 4 — Copper Crown |
| Chapters | `editions/monroe-1.3/book-04-copper-crown/manuscript/chapter-08.md` … `chapter-14.md` |
| Date | 2026-10-04 |

One session. No chapter was drafted by anyone else. No coordinator correction arrived during the run.

**Reading before drafting.**
- The compiled prompt in full (1,406 lines, paged): profile, formula §§2–6 and 8–9, the movement brief, the preceding chapter (ch 7), the edition brief (event-list method, 8-word gate, working ranges), BOOK_MAP §§1–14, STATE_LEDGER including "After Movement 1" and its coordinator rulings, CANON_RULES, owner voice.
- Movement 1 in full: `manuscript/chapter-01.md` … `chapter-07.md`, and `state/movement-001/AUTHORSHIP.md` / `AUTHOR-REPORT.md` for the shape of these files.
- Source `books/book-04-copper-crown/chapters/chapter-03.md`, `chapter-04.md`, `chapter-05.md`, once each, in full, then closed. They were not reopened while drafting or repairing; only the probes' matched-pair output was read afterward.
- `editions/monroe-1.3/OWNER-DECISIONS.md` (#7 Bracken *he*; #9 "since his Kindling"; #11 no new names used).
- `universe/UNIVERSE_BIBLE.md` (Path system, tiers, fragment notice format).
- Greps of the edition for: the Ardenmere stop protocol (B2 ch1), Wray's finding on Brom's turn (B3 ch26), the Pressure-adjacent description (B3 ch1/22), Hesk's trade (B1), Feryn, Shadow Path (never charted before), Lattice (no binding definition elsewhere).

**Method.** After the single source read, the author wrote a private event list in its own words (session scratchpad, outside the repo), chapter by chapter, with its own entry points and braid: Brom benched twelve days before his first floor hour; Lira reading out every name before signing; the clerk with no column for Cael; the slate and the Ash instructor's chosen look-away; the porter's account of the key on the nail; the wash-house and the dyed shirts; Karis on clause six; Lira's Fenmark minute and a half; Brom's bread and "Count the half-second"; the stationer's five copies; Seln building the man in an Ostrand posting-house; the TA's fumbled sum seen from Cael's side.

**Honest note on source distance.** The event-list method held for ch 8–11 at first draft but not for the baseline and the Seln window. The first sweep probe, run after all seven chapters existed, read: ch 8 7%, ch 9 12%, ch 10 10%, ch 11 11%, ch 12 18%, ch 13 31%, ch 14 53% (total 21%); `ed.sh overlap` found 163 unprotected 8-word runs. The same failure the coordinator warned about from Movement 1 recurred: ch 13 (the trials and Gault's door) and ch 14 (rumour aside) tracked the source's sentence order from memory with the page closed. Repairs, all by hand and by reading:
- Ch 13 was thrown away and rewritten in full with new composition throughout (new question to open each trial, new images for the read and the plate, Gault's speech rebuilt around the protected line).
- Ch 14 scenes 2–7 were thrown away and rewritten: the Seln window now opens on the officer's protected line and recalls the brief in reverse; the cover is built in a posting-house in present scenes (the ferry tally, the posting-house boy, the staring child who demonstrates the Path's prices); Cael's side is reordered round Karis's card census and shows the TA's manufactured sums mistake.
- Ch 8–12: every matched sentence listed by `skeleton_probe.py --show` was recomposed, and the baseline-doctrine debate, the doctrine log, Gault's three rules, the Lattice rule entry and the five-weeks log were rewritten whole.
- Probes were therefore run several times during repair (not once). `formula_metrics.py` was run once, on the finished chapters, and no rhythm repair followed.

**Final checks.** `ed.sh overlap`: 0 unprotected, 8 protected. `ed.sh gates`: reader_standard=0, metadata=0, modern=0 on all seven. `sweep_probe.sh book-04-copper-crown 2 2`: total 1%; chapters 0–2%; highest scene 9% (ch 14 scene 4, the protected brief and officer exchange).

**Interruption.** Partway through repair the disk filled (ENOSPC, about 116 MB free on the data volume; not caused by this run). Writes failed for a few minutes; no file was damaged (the failed edit never replaced the chapter). The author waited, checked free space read-only in a terminal tab, and resumed when writes succeeded. Nothing was deleted.

Only the seven chapter files and these two state files were written in the repo (plus scratchpad notes outside it). No git commands were run.
