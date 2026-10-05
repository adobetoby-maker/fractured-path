# AUTHORSHIP — Book 4, Movement 8 "Measured Rooms" (chapters 51–56)

| Field | Value |
|---|---|
| Public byline | Monroe Jackson |
| Seat | `oconnor` 1.3.0 |
| Foundation | Monroe Jackson 1.3.0 |
| Requested author | Opus (Claude Opus 5.5) |
| Actual runtime model | `claude-opus-5-5` (Claude Opus 5.5), as stated in this session's environment |
| Packet | `editions/monroe-1.3/book-04-copper-crown/state/movement-008/compiled-prompt.md` (movement brief: `editions/monroe-1.3/book-04-copper-crown/packets/MOVEMENT-008.md`) |
| Edition | `monroe-1.3` |
| Book | The Fractured Path, Book 4 — Copper Crown |
| Chapters | `editions/monroe-1.3/book-04-copper-crown/manuscript/chapter-51.md` … `chapter-56.md` |
| Date | 2026-10-05 |

One session. No other author drafted any chapter. The coordinator's eight rulings in the task message governed wherever they differed from the packet.

**Reading before drafting.**
- The compiled prompt in full (1,968 lines, read in pages): profile, formula §§2–6 and 8–9, the movement brief, the preceding chapter (ch50), the edition brief, BOOK_MAP §§1–14, STATE_LEDGER through "After Movement 7" with its coordinator rulings, CANON_RULES and the owner voice.
- Movement 7's last two chapters in full (`chapter-49.md`; `chapter-50.md` as printed in the prompt).
- The edition's baseline: `chapter-13.md` in full (day 48, the six trials), and the rules of the room in `chapter-12.md` (Gault's three rules, the eleven pieces of apparatus, the clerk).
- Edition Book 3, `chapter-37.md`, for Quenna's question (found by grep; the line is not quoted in this movement).
- Targeted continuity reads: B4 ch25/ch29 (standings notation, nine and nothing), ch41–43 (the semifinal, the batons, "Sit north", the fourth burst), ch44–48 (Vastin's dress and habits, the clerks), B2 ch14–15 (the pump step, to confirm Lira was not there), B3 ch52/57/60–61 (the concession; Ember's second word, "a letting-go").
- `state/movement-007/AUTHORSHIP.md` and `AUTHOR-REPORT.md` for the shape of these two files.
- Source `books/book-04-copper-crown/chapters/chapter-19.md` … `chapter-22.md` (22 to Gault's last line), each read once in full and then closed. None was reopened for drafting.

**Method.** After the single source read I wrote a private event list in my own words (session scratchpad, outside the repo: `m8b4/events.md`) with the day table, Lira's record arithmetic, the final's scoring, and each chapter's scenes and entry points. I drafted from that list and BOOK_MAP. Protected wording was copied from BOOK_MAP only. I probed each chapter with `skeleton_probe.py` as soon as its first draft existed, rebuilt the flagged scenes before starting the next chapter, and used a close-band lister of my own (the probe's method, listing pairs from 0.35) to find tracking sentences.

**Honest note on source distance.** As the coordinator warned, my first drafts tracked the source from memory, and badly: I had read all four source chapters just before drafting, and the set pieces came out in the source's order and cadence. The per-chapter probe caught every one. The fixes were rebuilds with new staging, not word swaps:
- ch53: the calibration night is now built round the furniture standing in for the wing, with the plate rehearsed first and Lira's thumbnail tally in the chair's wax.
- ch54–55: the evaluation is organised round Cael's gap readings (the clerk, the Mire instructor), the slow vessel's waiting, a four-piece account of the fault second, and the glance tally.
- ch56: the prep became Brom playing the silent Archmarshal; the interview dialogue was recomposed throughout.

After all six chapters existed, one rhythm pass (scene merges, sentence joins and splits) and one close-band pass went over the whole movement by reading. Skeleton / close by stage:

| Chapter | First draft | Rebuild(s) | After rhythm + close pass | Final |
|---|---|---|---|---|
| 51 | 19% / 43% | scenes 3, 6, 7, 8 rebuilt → 4 / 23 → 0 / 16 | 0 / 3 | 0% / 4% |
| 52 | 16% / 42% | scenes 2–7 rebuilt; ceremony moved to Ilsev's eyes → 4 / 27 → 1 / 22 | 1 / 7 | 2% / 9% |
| 53 | 35% / 62% | full rebuild → 9 / 38 → 2 / 21 | 1 / 2 | 1% / 3% |
| 54 | 30% / 61% | full rebuild → 8 / 33 → 1 / 26 | 1 / 6 | 1% / 8% |
| 55 | 23% / 46% | scenes 3, 4, 5, 7 rebuilt (fault in four pieces, glance tally, ledger-form Log) → 8 / 35 → 3 / 31 | 3 / 8 | 3% / 10% |
| 56 | 41% / 62% | scenes 2–5 rebuilt (Brom as the Archmarshal; interview recomposed) → 11 / 40 → 3 / 27 | 3 / 8 | 3% / 8% |

The remaining skeleton hits are protected or coordinator-quoted lines: the slip, subsection eleven, the note's opening line, the keynote, "I came to see whether the record and the practitioner match.", "Like somebody with something in his pocket.", "Because the clerk was standing where I'd have landed.", and the tag-broken packet lines (see the report's owner flags).

Scripts were used only to apply exact before→after strings that I wrote by hand, each failing on any miss; to list sentences; and to splice whole rebuilt scenes I had written into place. Every join, split and rewording was chosen by reading. Speech, Log lines, protected text and short landing beats were left as speech.

**Scratchpad.** The event list, probe helper, close-band lister, shape counter and the staged scene files are in the session scratchpad under `m8b4/`. Nothing from them was written into the repo.

**Final checks** (all run after the last edit):
- `ed.sh overlap book-04-copper-crown 8`: **0 unprotected**, 9 protected.
- `ed.sh gates book-04-copper-crown 8`: reader_standard=0, metadata=0, modern=0 on all six chapters.
- `sweep_probe.sh book-04-copper-crown 8 8`: **skeleton 2%, close 7%** on 1,348 sentences.
- `formula_metrics.py` on ch51–56: see AUTHOR-REPORT.md.

Only the six chapter files and these two state files were written in the repo. No git commands were run. STATE_LEDGER was not edited; its end-state is in AUTHOR-REPORT.md.
