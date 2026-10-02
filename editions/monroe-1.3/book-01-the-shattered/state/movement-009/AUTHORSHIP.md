# AUTHORSHIP — Movement 9 (chapters 54–60)

| Field | Value |
|---|---|
| Public byline | Monroe Jackson |
| Seat | `oconnor` 1.3.0 |
| Foundation | Monroe Jackson 1.3.0 |
| Requested author | Opus (Claude Opus 5.5) |
| Actual runtime model | `claude-opus-5-5` (Claude Opus 5.5), as stated in this session's environment |
| Packet | `editions/monroe-1.3/book-01-the-shattered/state/movement-009/compiled-prompt.md` (movement brief: `editions/monroe-1.3/book-01-the-shattered/packets/MOVEMENT-009.md`) |
| Edition | `monroe-1.3` |
| Book | The Fractured Path, Book 1 — The Shattered |
| Chapters | `editions/monroe-1.3/book-01-the-shattered/manuscript/chapter-54.md` … `chapter-60.md` |
| Date | 2026-10-02 |

**Interruption.** The session was stopped once by a rate limit after all seven chapters had been written and ch 58 had been recomposed (see below), before the checks were run. The coordinator resumed the same author with a message. On resuming, the author confirmed on disk that ch 58's recomposition was complete (the whole chapter had been rewritten in one write; the probe had already read it at 1%) and that ch 60 was complete. It then ran the overlap, gates, probe and metrics and wrote these two files. No chapter was drafted by anyone else.

**Reading before drafting.**
- The compiled prompt in full (2,506 lines, paged): edition brief (incl. the event-list method note, the 8-word gate, working ranges), BOOK_MAP §§1–11, STATE_LEDGER through "After Movement 8" and its coordinator rulings, CANON_RULES, the packet and every coordinator note.
- Source `books/book-01-the-shattered/chapters/chapter-21.md`–`chapter-24.md` and `books/book-02-iron-circuit/chapter-01.md`, once each.
- This edition: ch 52 and ch 53 in full (ch 53 via the compiled prompt); ch 46 (the Feryn bout: Vell's call formulas, the yard) and parts of ch 47 (Feryn's open account), ch 45, ch 51 (old man's number calls, Log entry format), ch 11 and ch 24 (Iron Path as rendered), ch 50 (Vell's table); greps for Yeni, Marrow, the board, Torvin's "yard door".
- A grep of Book 2 for its market watcher, so as to give the stranger nothing of his (Book 2's is a man who sits beside Cael and speaks; this one is sexless in the text, stands at a distance and says nothing).
- `state/movement-008/AUTHORSHIP.md` and `AUTHOR-REPORT.md`, for the shape of these files.

**Method.** After the source read, the author wrote a private event list in its own words (calendar, Darrow's stance geometry, the strike count to the crossing, the cost-at-the-wrong-moment, per-chapter beats) in the scratchpad and drafted from it with the source closed.

**Honest note on source distance.** Drafting from the list did not by itself keep two retold scenes clear. Re-reading its own draft of ch 57 (the yard and exchanges 1–2) and ch 58 (exchanges 3–4, the call, "What are you?", Lira after, the notice), the author found it had reproduced many of the source's beats and sentence shapes from memory (the counting exchange with Lira, "say it back", the measured-you exchange, the futility paragraph, the clarity-and-arithmetic paragraph, the reversal paragraph, the yard's walk home, the notice reaction). Both chapters were thrown away and rewritten in full from the event list with new entry points and images: the board with *HESK-WARD*; Darrow paying at the gate; the empty *Ruling* line; Hesk's bench load-test; the reading-room floor over the river; Darrow leaning on a gate; the market-gate carts; the trough's returning rings; the old man's standing; the ladder rung; the latch; Vell's dry pump; the stake at the edge of a marsh. Smaller source-shaped sentences in ch 54–56 were recomposed after an early probe. The probe figures below are on the final text.

**Drafting.** Seven chapters, written forward in order by the same author. No formula tool was run between chapters. Blocking slips fixed as noticed: Cael's signature goes on Darrow's carter's slip, not into Vell's book (so the book names him first after the bout); Lira's healer threat no longer points at Denvash's Merchant Row; the crossing-strike count was made a running count (2 + 5 + 2 + 1 = ten); Hesk's letter no longer repeats Lira's exact phrasing; Coss no longer "never said she was wrong" about a roof talk he did not hear.

**After all seven existed.**
1. `ed.sh overlap book-01-the-shattered 9`: 5 unprotected runs, each recomposed in context. Final: **0 unprotected, 8 protected**.
2. `ed.sh gates book-01-the-shattered 9`: reader_standard=0, metadata=0, modern=0 on all seven.
3. `skeleton_probe.py` (source ch 21–24): total **1% skeleton**; ch 60 scene 3 was 17%, all protected log lines, and was brought to 14% by not printing the boundary line a second time as he rereads it.
4. `formula_metrics.py` once on the seven chapters. No formula-driven rewriting.

Only the seven chapter files and these two state files were written (plus a scratchpad event list outside the repo). No git commands were run.
