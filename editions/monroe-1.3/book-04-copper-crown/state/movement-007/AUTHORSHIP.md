# AUTHORSHIP — Book 4, Movement 7 "Archmarshal" (chapters 45–50)

| Field | Value |
|---|---|
| Public byline | Monroe Jackson |
| Seat | `oconnor` 1.3.0 |
| Foundation | Monroe Jackson 1.3.0 |
| Requested author | Opus (Claude Opus 5.5) |
| Actual runtime model | `claude-opus-5-5` (Claude Opus 5.5), as stated in this session's environment |
| Packet | `editions/monroe-1.3/book-04-copper-crown/state/movement-007/compiled-prompt.md` (movement brief: `editions/monroe-1.3/book-04-copper-crown/packets/MOVEMENT-007.md`) |
| Edition | `monroe-1.3` |
| Book | The Fractured Path, Book 4 — Copper Crown |
| Chapters | `editions/monroe-1.3/book-04-copper-crown/manuscript/chapter-45.md` … `chapter-50.md` |
| Date | 2026-10-05 |

One session. No other author drafted any chapter. The coordinator's seven rulings in the task message governed wherever they differed from the packet.

**Reading before drafting.**
- The compiled prompt in full (1,936 lines, read in pages): profile, formula §§2–6 and 8–9, the movement brief, the preceding chapter (ch44), the edition brief, BOOK_MAP §§1–14, STATE_LEDGER through "After Movement 6" with its coordinator rulings, CANON_RULES and the owner voice.
- Movement 6's last two chapters in full (`chapter-43.md`, `chapter-44.md`; ch44 confirmed identical to the prompt's copy), and `state/movement-006/AUTHORSHIP.md` and `AUTHOR-REPORT.md` for the shape of these two files.
- Source `books/book-04-copper-crown/chapters/chapter-17.md` and `chapter-18.md`, each read once in full and then closed. Neither was reopened.
- Edition Book 3 `chapter-51.md` lines 110–230 for the documents' wording (the register entry and the later hand; the three copies read aloud).
- Targeted reads of the edition for continuity, not for prose:
  - B3 ch52 (the first return at Greyvane, the referral up, Havel's third entry);
  - B3 ch47 and B2 ch14–15, ch33 (Havel's first two entries, the cardboard notebook);
  - B3 STATE_LEDGER (hearing calendar: the referral went up on the morning of the first sitting, the day before the ruling, which puts this return about eleven months later);
  - B4 ch2 (Bracken's fifteenth letter and the transitional article plant), ch12 (the demonstration floor), ch28 (resistance posts), ch36 (working-ledger format), ch38–39 and ch42 (the counsel, Withrow's counsel, the file's four decisions, the green tabs, "forty breaths… ninety").

**Method.** After the single source read, I wrote a private event list in my own words (session scratchpad, outside the repo: `m7b4/events.md`) with a day table, each chapter's scenes and entry points, and my own inventions. Drafting worked from that list and BOOK_MAP. Protected wording was copied from BOOK_MAP only. Each chapter was probed with `skeleton_probe.py` immediately after drafting, before the next was begun, and flagged scenes were rebuilt with new staging, not word swaps. I used a small close-band lister of my own (the probe's own method, listing pairs from 0.35) to find tracking sentences.

**Honest note on source distance.** As the coordinator warned, my first drafts tracked the source from memory. It was worst in the chapters closest to the end of source ch18, which I had read last: the charter session, the Ilsev and Havel windows, and the back room and Log. Skeleton / close by stage:

| Chapter | First draft | Rebuild(s) | Final | What changed |
|---|---|---|---|---|
| 45 | 6% / 19% | 0 / 12 → 0 / 10 | 0% / 10% | Vastin enters through the counsel heard through a wall and his brass watch; the record read on the road in three tapes; the counsel at his door ("a kindness dressed up as a procedure"); the fire-watch boy seen from his window. Doors-and-boxes scene restaged as a house round a guest's trunk; the counsel's two rooms taken to Karis in carrel eleven |
| 46 | 5% / 19% | 0 / 9 | 0% / 7% | The Havel note written in three tries, with Lira's capitals and gratitude "settled"; the thresholds worked out with Brom at supper ("You do that"), not in library columns |
| 47 | 7% / 22% | full rebuild → 1 / 10 | 0% / 8% | Brom on the stair the night before; the ledger written on a bearer in the yard behind hall three; Karis brings the question counts from Bracken's clerk; the silent gallery analysed afterward |
| 48 | 17% / 38% | scenes 2–7 rebuilt → 4 / 17 → 1 / 15 | 1% / 14% | Lira's foundry weighbeam for the ruler; the taxonomy rebuilt on how each watcher writes; the sitting seen from the door end; provenance and supersession restaged (the stump, the list) |
| 49 | 14% / 32% | full rebuild → 4 / 18 → 3 / 16 | 3% / 15% | Ilsev takes the return as three witnesses, the colleague who was right a year early, *available: at this clearance*; Havel's courier night and the card; the pen list on the back of the floor sheet; Withrow at the window; the steps |
| 50 | 23% / 50% | rebuild → 5 / 24 → 1 / 15 | 0% / 12% | Bracken in the back room ("the best day a file can have"); the green tabs measured with two fingers; Karis shows the page instead of saying the line; the fire-watch slate; Brom's box; a numbered Log |

The remaining skeleton hits in ch49 are the protected finding, the grounds sentence and the C3 notebook line.

Scripts were used only to apply exact before→after strings that I wrote by hand, each failing on any miss, and to list sentences. About forty rhythm joins were each chosen by reading, in narration only. Speech, Log lines, protected text and short landing beats were left as written.

**Continuity fixes after review:** Karis is barred from the records hall until the fifteenth (not the whole inspection), so she can sit at the table; the schedule was pinned "a week ago" (d170), not four days; "most of a year" for Karis's find; no season tied to Reaping ("for the last two winters"); the taxonomy no longer infers anything from the unmarked case; the bout's arrival placed after the first call so the threshold reasoning fits; the fear on the tier is of the second hour, since the gap lesson comes a day later.

**Scratchpad.** The event list, the close-band lister and the staged scene files are in the session scratchpad under `m7b4/`. Nothing from them was written into the repo. One shell redirect briefly created `/tmp/claude-501-ch48head.md` outside the repo; I deleted it at once. It touched no project file.

**Final checks** (all run after the last edit):
- `ed.sh overlap book-04-copper-crown 7`: **0 unprotected**, 10 protected.
- `ed.sh gates book-04-copper-crown 7`: reader_standard=0, metadata=0, modern=0 on all six chapters.
- `sweep_probe.sh book-04-copper-crown 7 7`: **skeleton 1%, close 12%** on 1,350 sentences.
- `formula_metrics.py` on ch45–50: see AUTHOR-REPORT.md.

Only the six chapter files and these two state files were written in the repo. No git commands were run. STATE_LEDGER was not edited; its end-state is in AUTHOR-REPORT.md.
