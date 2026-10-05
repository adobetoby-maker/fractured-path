# AUTHORSHIP — Book 4, Movement 9 "Null Report" (chapters 57–62)

| Field | Value |
|---|---|
| Public byline | Monroe Jackson |
| Seat | `oconnor` 1.3.0 |
| Foundation | Monroe Jackson 1.3.0 |
| Requested author | Opus (Claude Opus 5.5) |
| Actual runtime model | `claude-opus-5-5` (Claude Opus 5.5), as stated in this session's environment |
| Packet | `editions/monroe-1.3/book-04-copper-crown/state/movement-009/compiled-prompt.md` (movement brief: `editions/monroe-1.3/book-04-copper-crown/packets/MOVEMENT-009.md`) |
| Edition | `monroe-1.3` |
| Book | The Fractured Path, Book 4 — Copper Crown (final movement) |
| Chapters | `editions/monroe-1.3/book-04-copper-crown/manuscript/chapter-57.md` … `chapter-62.md` |
| Date | 2026-10-05 |

One session. No other author drafted any chapter. The coordinator's five rulings in the task message governed wherever they differed from the packet.

**Reading before drafting.**
- The compiled prompt in full (2,219 lines, read in pages): profile, formula §§2–6 and 8–9, the movement brief, the preceding chapter (ch56, printed in the prompt), the edition brief, BOOK_MAP §§1–14, STATE_LEDGER through "After Movement 8" with its coordinator rulings, CANON_RULES and the owner voice.
- Movement 8's last two chapters in full: `chapter-55.md` (read directly) and `chapter-56.md` (as printed in the prompt).
- `state/movement-008/AUTHORSHIP.md` and `AUTHOR-REPORT.md` for the shape of these two files; `protected-patterns.txt`.
- Targeted continuity reads in the edition: ch30 (Seln's room, cipher, the two cases, the harbour-dues key), ch31–32/35–36/38/40 (the unit: the map store, Third-days at the sixth bell, nine signed, Gwen), ch5/7/11 (carrel eleven on the law range's third floor; the wall behind the second quadrangle), ch12/25/51 (Lira's Fenmark Kindling), ch14/40 (Ephram's two public positions), ch29 (Fiske's Path; Cael's existing Fiske page), ch38 (Rooke under the north arch), ch44/46/49 (Havel: the plan of the yard, the pear, the inch, the four entries), ch45 (Vastin's habits, mentor, the bad month), ch48 (the weighbeam).
- Source `books/book-04-copper-crown/chapters/chapter-22.md` (from "The delegation left"), `chapter-23.md`, `chapter-24.md`, each read once in full and then closed; `books/book-05-the-silver-standard/chapters/chapter-01.md` scanned only for the hand-off facts.

**Method.** After the single source read I wrote a private event list and day table in my own words (session scratchpad, outside the repo: `m9b4/events.md`) and drafted from it and BOOK_MAP. Protected wording was copied from BOOK_MAP only. I probed each chapter with `skeleton_probe.py` as soon as its first draft existed and rebuilt the flagged scenes before starting the next chapter, using a close-band lister of my own (the probe's method, listing pairs from 0.35).

**Honest note on source distance.** As in Movement 8, the first drafts tracked the source from memory wherever the packet's events were dense; the cutaways and the set-piece speeches were worst, exactly as the coordinator warned. The fixes were rebuilds with new staging, not word swaps:
- ch57: the Ilsev scene rebuilt round a question she asks him first ("Now tell me what it was *about*"); the departure Log rebuilt round "count the rooms" and the audit image.
- ch58: Seln's window split into two scenes (the return felt for with the thumb, the old master's chalked rule; then the quarterly); the council rebuilt round Karis reading her corridor page and Cael reading back Karis's marbled watcher log line by line.
- ch59: the whole Vastin window rebuilt: the notebook deliberately set face down until the record has had its chance; the clerk's added three words and the missing shoes; the struck line (stroke at the close, consistent with ch55; amendment that night); three concrete cases of "giving it more"; the three readings staged as two scraps written and burned and a third never written.
- ch60–62: Lira's station window written from the inside (the bench, the porter's chalk, the empty weighbeam bracket, three runs of the sequence); the anteroom recomposed; ch61's Ephram, Withrow and charter scenes rebuilt (Ephram calls Cael down to the oak; Withrow reads the finding's four lines aloud; Karis slides her notebook down the table); ch62's inventory recast as a priced ledger and the wall recomposed.

Skeleton / close by stage:

| Chapter | First draft | After rebuild(s) | Final |
|---|---|---|---|
| 57 | 11% / 31% | 1 / 17 | 1% / 5% |
| 58 | 27% / 56% | 9 / 38 → 2 / 21 | 3% / 8% |
| 59 | 22% / 45% | 10 / 30 → 3 / 21 | 3% / 8% |
| 60 | 11% / 29% | 1 / 11 | 1% / 10% |
| 61 | 29% / 53% | 7 / 33 → 3 / 24 | 3% / 9% |
| 62 | 34% / 55% | 11 / 38 → 4 / 30 | 4% / 11% |

The remaining skeleton hits are protected or packet-quoted lines (the quarterly's four lines, Vastin's notebook lines, the certification, the clause, the letters, the closing exchange) and the twelve packet lines kept whole under ruling 5.

Scripts were used only to apply exact before→after strings that I wrote by hand (each failing on any miss), to splice whole rebuilt scenes I had written into place, to list sentences and close pairs, and to count words per scene. Every join, split and rewording was chosen by reading. Speech, Log lines, protected text and short landing beats were left as speech.

**Scratchpad.** The event list, close-band lister and scene-count helper are in the session scratchpad under `m9b4/`. Nothing from them was written into the repo.

**Final checks** (all run after the last edit):
- `ed.sh overlap book-04-copper-crown 9`: **12 unprotected** (every one a packet-quoted line kept whole under ruling 5; listed with proposed patterns in AUTHOR-REPORT.md), 20 protected.
- `ed.sh gates book-04-copper-crown 9`: reader_standard=0, metadata=0, modern=0 on all six chapters.
- `sweep_probe.sh book-04-copper-crown 9 9`: **skeleton 2%, close 8%** on 1,268 sentences.
- `formula_metrics.py` on ch57–62: see AUTHOR-REPORT.md.

Only the six chapter files and these two state files were written in the repo. One read-only `git status --porcelain` slipped into the last check command by mistake, against the instruction to run no git commands; its output was discarded and nothing was staged, committed or changed. No other git command was run. STATE_LEDGER and protected-patterns.txt were not edited; the book-end state is in AUTHOR-REPORT.md.
