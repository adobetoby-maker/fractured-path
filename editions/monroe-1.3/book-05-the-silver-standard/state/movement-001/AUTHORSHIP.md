# AUTHORSHIP — Book 5, Movement 1 "Roster" (chapters 1–6)

| Field | Value |
|---|---|
| Public byline | Monroe Jackson |
| Seat | `oconnor` 1.3.0 |
| Foundation | Monroe Jackson 1.3.0 |
| Requested author | Opus (Claude Opus 5.5) |
| Actual runtime model | `claude-opus-5-5` (Claude Opus 5.5), as stated in this session's environment |
| Packet | `editions/monroe-1.3/book-05-the-silver-standard/state/movement-001/compiled-prompt.md` (movement brief: `editions/monroe-1.3/book-05-the-silver-standard/packets/MOVEMENT-001.md`) |
| Edition | `monroe-1.3` |
| Book | The Fractured Path, Book 5 — The Silver Standard (first movement) |
| Chapters | `editions/monroe-1.3/book-05-the-silver-standard/manuscript/chapter-01.md` … `chapter-06.md` |
| Date | 2026-10-05 |

**Interrupted and resumed.** The run hit a session limit after ch01 and ch02 had been drafted, probed and rebuilt. The coordinator sent a resume message once the limit reset. On resumption I confirmed both chapters were complete (ch02 ends on the protected Log entry, item 19), re-ran ch02's probe (3% / 14%, passing) and did a sentence-length repair on it. I then drafted ch03–06 in the same session and context, under the same per-chapter probe discipline. The same author wrote all six chapters. No other model drafted any part of them.

**Reading before drafting.**
- The compiled prompt in full (1,492 lines, read in pages): profile, formula §§2–6 and 8–9, the movement brief, the preceding chapter (B4 ch62, printed in the prompt), the edition brief, BOOK_MAP §§1–14 with every `[B4-reconciled]` mark, the STATE_LEDGER ENTRY block, CANON_RULES and owner voice.
- `book-04-copper-crown/STATE_LEDGER.md`: the coordinator rulings under "After Movement 8" and "After Movement 9 — BOOK END", plus the author end-states beneath them.
- The closed Book 4 ending, `manuscript/chapter-57.md` … `chapter-62.md`, in full.
- `OWNER-DECISIONS.md` (all of it, including #7–#11, #16–#18 and #35–#37) and `state/B4-RECONCILIATION-APPLIED.md`.
- `universe/UNIVERSE_BIBLE.md`: the Path system, tiers, Arbiter and fragment notices.
- Book 4 `state/movement-009/AUTHORSHIP.md` and `AUTHOR-REPORT.md`, for the shape of these two files.
- Targeted greps in the edition's Book 4 for: *Hold. First.*; drifts and the thumbnail chair; Ephram in ch8 (Iron Rank Six; the fourteen Silvers and one Gold); and Withrow's office.
- Source `books/book-05-the-silver-standard/chapters/chapter-01.md` and `chapter-02.md`, each read once in full and then closed.

**Method.**
- After the single source read, I wrote a private event list and day plan in my own words. It is in the session scratchpad, outside the repo, at `b5m1/events.md`.
- I drafted from that list and from BOOK_MAP. The source chapters were never reopened. The only exposure to source sentences after that was the probe's `--show` output, which lists matched pairs so that flagged passages can be rebuilt.
- Protected wording was copied from BOOK_MAP §10 and packet-quoted lines from the packet.
- Each chapter was probed with `skeleton_probe.py` as soon as its first draft existed. Flagged scenes were rebuilt with new staging and a new beat order before the next chapter was begun.

**Honest note on source distance.** As in Book 4, the first drafts tracked the source wherever I retold one of its own scenes. The worst cases were the convocation (ch1), the bluff road and counter (ch2), Lira's argument on the wall (ch4), and the map room and log (ch5). Everything I invented was clean on first draft: the dawn session, the learning fight, the broom on the hearthrug, the Ephram sessions, Hesk's reply, the mock exhibition and Rooke's rating card. The fixes were rebuilds, not word swaps:
- **ch1, convocation:** rebuilt round Withrow's "three numbers" (five, four, eighteen).
- **ch2, the bluff road:** rebuilt as Karis making Cael play the regional registrar ("Find me the step").
- **ch2, the counter:** now opens on the new buff form.
- **ch4, the wall:** Lira's argument rebuilt round "Who signed it?" and Karis's card, with Brom's pencil line under it.
- **ch5, map room:** rebuilt round Rooke's own yellow rating card from his cycle, on which he lost the bout and was rated two points above the winner.
- **ch5, log:** the card log rebuilt, and the honest-want entry rebuilt round Cael ruling a grid on the back of that card.

Skeleton / close by stage (`skeleton_probe.py` against source ch1–2):

| Chapter | First draft | After rebuild(s) | Final |
|---|---|---|---|
| 1 | 10% / 25% | 3 / 13 → 1 / 12 | 1% / 10% |
| 2 | 16% / 27% | 3 / 14 | 3% / 11% |
| 3 | 8% / 20% | 2 / 13 | 2% / 12% |
| 4 | 8% / 24% | 1 / 12 | 1% / 11% |
| 5 | 19% / 33% | 3 / 16 → 2 / 15 | 3% / 13% |
| 6 | 3% / 9% | 1 / 6 | 0% / 6% |

Every remaining skeleton hit is a protected or packet-quoted line: the certification, the memorandum's item, the exhibition provision, the advisory, the card line, the item-19 Log entry, Karis's roster sentence, and Seln's counter line.

**How scripts were used.** Scripts did three jobs only:
- Applying exact before→after strings that I wrote by hand. Each one failed on any miss.
- Splicing whole rebuilt scenes, written by hand in the scratchpad, into place.
- Listing sentences of 40 or more words, and counting words per scene.

Every split, join and rewording was chosen by reading. Speech, Log lines, protected text and short landing beats were left as speech. After the drafting I did one hand pass for tics, taking out explanatory "the way a X…" similes, surplus "as if" and "as though", and surplus "exactly".

**Scratchpad.** The event list, the long-sentence lister and the rebuilt-scene source files are in the session scratchpad under `b5m1/`. Nothing from them was written into the repo except the chapter text itself.

**Final checks** (all run after the last edit):
- `ed.sh overlap book-05-the-silver-standard 1`: **1 unprotected**, 13 protected. The one unprotected run is the packet-quoted Bracken line "A trap catches you moving. A mirror just stands there.", kept whole. A pattern for it is proposed in AUTHOR-REPORT.md.
- `ed.sh gates book-05-the-silver-standard 1`: reader_standard=0, metadata=0, modern=0 on all six chapters.
- `sweep_probe.sh book-05-the-silver-standard 1 1`: **skeleton 2%, close 10%**, on 1,280 sentences.
- `formula_metrics.py` on ch1–6: see AUTHOR-REPORT.md.

**Files written.** Only the six chapter files and these two state files were written in the repo. The `manuscript/` folder already existed. STATE_LEDGER, BOOK_MAP and `protected-patterns.txt` were not touched; Book 5 has no `protected-patterns.txt` yet. **No git commands of any kind were run.**
