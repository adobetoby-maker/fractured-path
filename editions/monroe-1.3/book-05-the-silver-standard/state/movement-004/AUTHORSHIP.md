# AUTHORSHIP — Book 5, Movement 4 "Qualified" (chapters 20–26)

| Field | Value |
|---|---|
| Public byline | Monroe Jackson |
| Seat | `oconnor` 1.3.0 |
| Foundation | Monroe Jackson 1.3.0 |
| Requested author | Opus (Claude Opus 5.5) |
| Actual runtime model | `claude-opus-5-5` (Claude Opus 5.5), as stated in this session's environment. Run as a delegated agent session launched by the coordinator. |
| Packet | `editions/monroe-1.3/book-05-the-silver-standard/state/movement-004/compiled-prompt.md` (movement brief: `editions/monroe-1.3/book-05-the-silver-standard/packets/MOVEMENT-004.md`, with the coordinator's #39 note at its head) |
| Coordinator rulings | Seven rulings sent with the task (#39 one Iron draw and formats; #38 per-axis ratings and per-day bursts; year counts not incremented; Ember contact only and the caravan captain as renewal-and-tax only, RIGHT forearm, RIGHT shoulder private, LEFT seam healed at entry; the Vastin/Havel/Seln/Karis limits; world rules; protected wording). Applied where they differ from the packet. |
| Edition | `monroe-1.3` |
| Book | The Fractured Path, Book 5 — The Silver Standard (fourth movement; opens the book's middle third) |
| Chapters | `editions/monroe-1.3/book-05-the-silver-standard/manuscript/chapter-20.md` … `chapter-26.md` |
| Date | 2026-10-05 |

**One session.** One author drafted all seven chapters in one session and one context. No other model drafted any part of them, and no subagents were used.

**Reading before drafting.**
- The compiled prompt, read in full in pages: the profile and formula §§2–6, 8–9; the movement brief; the preceding chapter (ch19); the edition brief; BOOK_MAP §§1–14 with every `[B4-reconciled]` mark; STATE_LEDGER ENTRY and AFTER MOVEMENTS 1–3 with their coordinator rulings; CANON_RULES and owner voice.
- `manuscript/chapter-18.md` in full (ch19 was read in full inside the compiled prompt).
- Movement 3's `AUTHORSHIP.md` and `AUTHOR-REPORT.md`, for the shape of these files; `packets/MOVEMENT-005.md` for the seam at the end of this movement (the road's first week, Withrow and Bracken catching up, the trial rules read at Norhold, Vastin's seat-twelve beat reserved for M5).
- Targeted greps of this edition: Book 4 for Havel's notebook (ch44, ch49: cardboard cover, ninety pages, four entries, the one rule-break line; the pear; the ache in the web of the thumb), Shield panes ("breath, plant, pane", B4 ch43) and the public/paper split of the five capabilities (B4 ch43: two public, Ember a thin exhibit at the back of the Greyvane transcript); this book's ch5 (Vastin's room, pigeons, routing slip, "forty years"), ch1 and ch6 (the reserves), ch8 and ch12 (Shields renewing), and the circle's tells.
- Source `books/book-05-the-silver-standard/chapters/chapter-07.md` read once in full, and `chapter-13.md` read once in full for its caravan-captain reference and the Silver weave this movement must not pre-empt. Both were then closed.

**Method.**
- After the single source read I wrote a private event list, a day calendar, and a ratings and bursts plan in my own words. They are in the session scratchpad, outside the repo (`b5m4/events.md`).
- I drafted from that list and BOOK_MAP and did not reopen the source chapters. My only later exposure to source sentences was through the probe's `--show` output and a small helper (`b5m4/close.py`) that lists the ≥0.35 pairs so that close passages could be found and rebuilt.
- Protected wording was copied from BOOK_MAP §10; packet-quoted lines from the packet and the coordinator's rulings.
- Each chapter was probed as soon as its first draft existed, and flagged passages were rebuilt before the next chapter was begun.

**Per-chapter probe (skeleton / close), first draft → final.**

| Chapter | First draft | Rebuilt | Final |
|---|---|---|---|
| 20 | 1% / 5% | the qualifying Log rebuilt for the 8-word gate (its list of arrivals had followed the source's shape) | 0% / 4% |
| 21 | 0% / 5% | — (one 8-word run, "it was the right answer and it cost", recomposed) | 0% / 5% |
| 22 | 0% / 4% | — | 0% / 4% |
| 23 | 2% / 8% | the barge-master's channel image, his two-handed handshake, the convenor's seniority order, Withrow's inventory of her table, the observation-notebook line and the "patient/careful" Log lines rebuilt | 1% / 7% |
| 24 | 2% / 14% | the Vastin cutaway's entry, the office-above paragraph, the three-readings beat, the three answers, the clerk, the files' placing, the query's three items, the toast-keeper line and the chalk line rebuilt | 0% / 10% |
| 25 | 0% / 5% | — | 0% / 4% |
| 26 | 0% / 4% | — | 0% / 4% |

Every remaining skeleton hit is a protected or packet-quoted line (the steward's report, the strata Log line, Withrow's sentence).

**How scripts were used.** Exact before→after strings that I wrote by hand, applied by a script that failed on any miss; whole new passages written by hand and spliced in; listing long paragraphs, scene sizes, close pairs and tic counts for me to read. Every paragraph break was chosen by reading: I named the sentence at which each paragraph turned, and the script applied only that break (`b5m4/brk.py`). No rule split or joined text automatically. Speech, Log lines and protected text were left whole.

**Final checks** (all run after the last edit):
- `ed.sh overlap book-05-the-silver-standard 4`: **4 unprotected**, 3 protected. All four unprotected runs are packet-quoted lines kept whole as ruling 7 directs (listed with proposed patterns in AUTHOR-REPORT.md). Every other shared run was rebuilt.
- `ed.sh gates book-05-the-silver-standard 4`: reader_standard=0, metadata=0, modern=0 on all seven chapters.
- `sweep_probe.sh book-05-the-silver-standard 4 4`: **skeleton 0%, close 5%**, on 1,577 sentences.
- `formula_metrics.py` on ch20–26 and on ch1–26: see AUTHOR-REPORT.md.

**Files written.** Only the seven chapter files and these two state files were written in the repo. STATE_LEDGER, BOOK_MAP, the packets and `protected-patterns.txt` were not touched. Scratch files are in the session scratchpad only. **No git commands of any kind were run.**
