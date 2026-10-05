# AUTHORSHIP — Book 5, Movement 2 "Standard Measures" (chapters 7–13)

| Field | Value |
|---|---|
| Public byline | Monroe Jackson |
| Seat | `oconnor` 1.3.0 |
| Foundation | Monroe Jackson 1.3.0 |
| Requested author | Opus (Claude Opus 5.5) |
| Actual runtime model | `claude-opus-5-5` (Claude Opus 5.5), as stated in this session's environment |
| Packet | `editions/monroe-1.3/book-05-the-silver-standard/state/movement-002/compiled-prompt.md` (movement brief: `editions/monroe-1.3/book-05-the-silver-standard/packets/MOVEMENT-002.md`) |
| Coordinator rulings | Five rulings sent with the task (rating scale #38; year counts not incremented; calendar and the mill-town session; standing canon; protected wording). They were applied where they differ from the packet. |
| Edition | `monroe-1.3` |
| Book | The Fractured Path, Book 5 — The Silver Standard (second movement) |
| Chapters | `editions/monroe-1.3/book-05-the-silver-standard/manuscript/chapter-07.md` … `chapter-13.md` |
| Date | 2026-10-05 |

**One session, not interrupted.** The same author drafted all seven chapters in one session and one context. No other model drafted any part of them. No subagents were used.

**Reading before drafting.**
- The compiled prompt in full, read in pages: profile, formula §§2–6 and 8–9, the movement brief, the preceding chapter (ch6, which matches the manuscript file word for word), the edition brief, BOOK_MAP §§1–14 with every `[B4-reconciled]` mark, STATE_LEDGER (ENTRY and "AFTER MOVEMENT 1" with its coordinator rulings), CANON_RULES and owner voice.
- `manuscript/chapter-05.md` and `chapter-06.md`, in full.
- Movement 1's `AUTHORSHIP.md` and `AUTHOR-REPORT.md`, for the shape of these files.
- Targeted greps:
  - this book's ch1–4: the buried Copper's profile; the draw rule; Fiske; the roster;
  - the edition's Book 3/4: Quenna's question; the plate and its brace; Gault's calendar entry; Fiske's Force technique.
- Source `books/book-05-the-silver-standard/chapters/chapter-03.md` and `chapter-04.md`, each read once in full and then closed.

**Method.**
- After the single source read, I wrote a private event list, a day plan and a ratings plan in my own words. They are in the session scratchpad, outside the repo, at `b5m2/events.md`.
- I drafted from that list and from BOOK_MAP. I did not reopen the source chapters. The only exposure to source sentences after that came from two places:
  - the probe's `--show` output;
  - a small helper (`b5m2/close.py`) that lists the ≥0.35 "close" pairs that `--show` does not print, so that close passages could be found and rebuilt.
- Protected wording was copied from BOOK_MAP §10, and packet-quoted lines from the packet.
- Each chapter was probed with `skeleton_probe.py` as soon as its first draft existed. Flagged passages were rebuilt with new wording, new staging or new beat order before the next chapter was begun.

**Honest note on source distance.** As in Movement 1, the retold scenes tracked the source on first draft. The worst cases were:
- the protest ruling at the waystation (ch10);
- the page-thirty-one conversation (ch12);
- the stove night, Seln's sentence, Rooke's remark and the first-pole frame (ch13).

The invented material was clean on first draft: the soft pine by the wall, the kind bout, the hinge funnel, Lira's tell, Ephram's late turn, the gable-slot light, Gault's letter, the travelling plate and the tailboard talk. The fixes were rebuilds, not synonym swaps. For example:
- the waystation scene now opens on the inn and the courier;
- Karis explains the ruling in her own terms;
- the page-thirty-one talk was re-voiced, and Cael's lines were recomposed;
- the stove night was re-staged around the oil tin and Gault's letter;
- Seln's speech was recomposed ("An honest instrument scatters…", "pencils are cheap");
- the program and the flinch were rewritten;
- the closing paragraph of the movement was rewritten.

Skeleton / close by stage (`skeleton_probe.py` against source ch3–4):

| Chapter | First draft | After rebuild(s) | Final |
|---|---|---|---|
| 7 | 5% / 11% | 0 / 7 | 0% / 7% |
| 8 | 2% / 9% (two scenes at 19% close) | 0 / 8 | 0% / 7% |
| 9 | 5% / 13% (one scene 29% skeleton) | 2 / 9 | 2% / 6% |
| 10 | 2% / 8% (opening scene 8% / 23%) | 2 / 5 | 1% / 5% |
| 11 | 1% / 8% | 0 / 3 | 0% / 3% |
| 12 | 4% / 10% (page-31 scene 12% / 24%) | 2 / 5 | 2% / 5% |
| 13 | 6% / 15% | 2 / 7 | 2% / 6% |

Every remaining skeleton hit is a protected or packet-quoted line:
- the protest ruling (item 7);
- the manual's two lines (item 8);
- Karis's blind-spot line (item 36);
- Lira's line (item 35);
- the item-20 and item-21 Log entries;
- the ganger's "managed effort" line.

**How scripts were used.**
- Exact before→after strings that I wrote by hand, applied by a script that failed on any miss.
- Whole new passages written by hand and spliced in.
- Listing sentence pairs, long paragraphs and tic counts for me to read.

Paragraph splits and sentence joins were each chosen by reading. I named the exact sentence at which a paragraph turned, or the exact pair of sentences to join, and the script applied only that edit. No rule split or joined text automatically. Speech, Log lines, protected text and short landing beats were left as written.

**Final checks** (all run after the last edit):
- `ed.sh overlap book-05-the-silver-standard 2`: **7 unprotected**, 7 protected. All seven unprotected runs are packet-quoted lines, kept whole as the task directs. They are listed with proposed patterns in AUTHOR-REPORT.md.
- `ed.sh gates book-05-the-silver-standard 2`: reader_standard=0, metadata=0, modern=0 on all seven chapters.
- `sweep_probe.sh book-05-the-silver-standard 2 2`: **skeleton 1%, close 6%**, on 1,570 sentences.
- `formula_metrics.py` on ch7–13 and on ch1–13: see AUTHOR-REPORT.md.

**Files written.** Only the seven chapter files and these two state files were written in the repo. STATE_LEDGER, BOOK_MAP, the packet and `protected-patterns.txt` were not touched. Scratch files are in the session scratchpad only. **No git commands of any kind were run.**
