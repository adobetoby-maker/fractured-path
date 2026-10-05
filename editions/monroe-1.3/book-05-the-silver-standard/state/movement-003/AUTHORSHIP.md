# AUTHORSHIP — Book 5, Movement 3 "The Scouting Economy" (chapters 14–19)

| Field | Value |
|---|---|
| Public byline | Monroe Jackson |
| Seat | `oconnor` 1.3.0 |
| Foundation | Monroe Jackson 1.3.0 |
| Requested author | Opus (Claude Opus 5.5) |
| Actual runtime model | `claude-opus-5-5` (Claude Opus 5.5), as stated in this session's environment. Run as a delegated agent session launched by the coordinator. |
| Packet | `editions/monroe-1.3/book-05-the-silver-standard/state/movement-003/compiled-prompt.md` (movement brief: `editions/monroe-1.3/book-05-the-silver-standard/packets/MOVEMENT-003.md`) |
| Coordinator rulings | Six rulings sent with the task (year counts not incremented, Lira's line "three years"; #38 scale and #39 formats with per-day bursts; Ember contact only, Pressure's right shoulder, the grappler's LEFT shoulder-seam; Seln's base and silence; world rules; protected wording). Applied where they differ from the packet. |
| Edition | `monroe-1.3` |
| Book | The Fractured Path, Book 5 — The Silver Standard (third movement; closes the book's first third) |
| Chapters | `editions/monroe-1.3/book-05-the-silver-standard/manuscript/chapter-14.md` … `chapter-19.md` |
| Date | 2026-10-05 |

**One session.** One author drafted all six chapters in one session and one context. No other model drafted any part of them, and no subagents were used.

**Reading before drafting.**
- The compiled prompt, read in full in pages:
  - the profile and formula §§2–6, 8–9;
  - the movement brief and the preceding chapter (ch13);
  - the edition brief and BOOK_MAP §§1–14, with every `[B4-reconciled]` mark;
  - STATE_LEDGER ENTRY, AFTER MOVEMENT 1 and AFTER MOVEMENT 2, each with its coordinator rulings;
  - CANON_RULES and owner voice.
- `manuscript/chapter-12.md` and `chapter-13.md`, in full.
- Movement 2's `AUTHORSHIP.md` and `AUTHOR-REPORT.md`, for the shape of these files.
- Targeted greps:
  - the edition's Book 4 for the records-hall reader (ch35: Jessup, the letter box, the wing's two lines), Seln's base (ch27–28 the pin; ch58 *unmarked file. one of three. probably the third.*), Fenmark (B2–B4: the river quarter, "the right foot for the third turn", the green wax, Lira's registry-station morning, "No. I mean it's small"), and Hesk's grandfather register;
  - this book's ch3 (Rooke's Fenmark line) and ch11 (Brom's mill-town Copper);
  - OWNER-DECISIONS #38–#39.
- Source `books/book-05-the-silver-standard/chapters/chapter-05.md` and `chapter-06.md`, each read once in full and then closed.

**Method.**
- After the single source read, I wrote a private event list, a calendar and a ratings and bursts plan in my own words. They are in the session scratchpad, outside the repo, at `b5m3/events.md`.
- I drafted from that list and from BOOK_MAP. I did not reopen the source chapters. My only later exposure to source sentences was through two tools:
  - the probe's `--show` output;
  - a small helper (`b5m3/close.py`) that lists the ≥0.35 pairs, so that close passages could be found and rebuilt.
- Protected wording was copied from BOOK_MAP §10. Packet-quoted lines were copied from the packet and the coordinator's rulings.
- Each chapter was probed as soon as its first draft existed. Flagged passages were rebuilt with new entry points, new beat order and new wording before the next chapter began.

**Honest note on source distance.** The invented material was clean on first draft. That includes:
- the bill at breakfast and the slow-feet drill;
- the counter and Bracken's pouch;
- Karis's open lines and the milestone silence;
- the slate test and Brom in the dark;
- the dossier's provenance line and Lira's fight against the doctrine;
- the alehouse, the stair fingerprint and the paper;
- the heat-shadow and the north flags;
- the grappler and Lira's "There's your bill".

The retold scenes tracked the source on first draft, where the source's own lines are most memorable. These were:
- the grey-wool woman (ch15);
- the dossier at the bench (ch16);
- Seln's reconciliation and "Good." (ch17);
- the board-man and the audit (ch18);
- Hesk's letter, the back steps and the profiles (ch19).

The fixes were rebuilds, not synonym swaps:
- ch17's table speech was re-voiced around "Offices insist. Shops make do.";
- the board-man was re-staged as Lira's performance with new jokes;
- the back steps now open on Zerin's page, and the Fenmark account is told after it;
- Hesk's letter was rewritten around his own trade except for the packet's three phrases;
- Rooke's coaches' speech and the Marek reading were recomposed.

Skeleton / close by stage (`skeleton_probe.py` against source ch5–6):

| Chapter | First draft | After rebuild | Final |
|---|---|---|---|
| 14 | 0% / 4% (after a full rhythm rewrite) | — | 0% / 4% |
| 15 | 4% / 10% (grey-wool scene 8% / 24%) | 1% / 4% | 1% / 3% |
| 16 | 7% / 13% (dossier scene 20% / 27%) | 0% / 6% | 0% / 6% |
| 17 | 10% / 19% (table scenes 19% / 34% and 22% / 50%) | 2% / 6% | 2% / 5% |
| 18 | 4% / 13% (board-man 12% / 28%; audit 11% / 29%) | 0% / 5% | 1% / 6% |
| 19 | 10% / 20% (letter 21% / 36%; back steps 25% / 41%; profiles 17% / 46%) | 2% / 11% | 2% / 9% |

Every remaining skeleton hit is a protected or packet-quoted line.

**How scripts were used.**
- Exact before→after strings that I wrote by hand, applied by a script that failed on any miss.
- Whole new passages written by hand and spliced in.
- Listing long paragraphs, close pairs and tic counts for me to read.

Each paragraph break was chosen by reading. I named the exact sentence at which a paragraph turned, and the script applied only that break. No rule split or joined text automatically. Speech, Log lines and protected text were left whole. One break that fell inside a quotation was reverted by hand.

**Final checks** (all run after the last edit):
- `ed.sh overlap book-05-the-silver-standard 3`: **6 unprotected**, 5 protected. All six unprotected runs are packet-quoted lines, kept whole as the task directs. Proposed patterns are in AUTHOR-REPORT.md. Every other shared run was rebuilt.
- `ed.sh gates book-05-the-silver-standard 3`: reader_standard=0, metadata=0, modern=0 on all six chapters.
- `sweep_probe.sh book-05-the-silver-standard 3 3`: **skeleton 1%, close 6%**, on 1,458 sentences.
- `formula_metrics.py` on ch14–19 and on ch1–19: see AUTHOR-REPORT.md.

**Files written.** Only the six chapter files and these two state files were written in the repo. STATE_LEDGER, BOOK_MAP, the packet and `protected-patterns.txt` were not touched. Scratch files are in the session scratchpad only. **No git commands of any kind were run.**
