# AUTHORSHIP — Book 2, Movement 1 "Rated" (chapters 1–8)

| Field | Value |
|---|---|
| Public byline | Monroe Jackson |
| Seat | `oconnor` 1.3.0 |
| Foundation | Monroe Jackson 1.3.0 |
| Requested author | Opus (Claude Opus 5.5) |
| Actual runtime model | `claude-opus-5-5` (Claude Opus 5.5), as stated in this session's environment |
| Packet | `editions/monroe-1.3/book-02-iron-circuit/state/movement-001/compiled-prompt.md` (movement brief: `editions/monroe-1.3/book-02-iron-circuit/packets/MOVEMENT-001.md`) |
| Edition | `monroe-1.3` |
| Book | The Fractured Path, Book 2 — Iron Circuit |
| Chapters | `editions/monroe-1.3/book-02-iron-circuit/manuscript/chapter-01.md` … `chapter-08.md` |
| Date | 2026-10-02 |

One session, not interrupted. No chapter was drafted by anyone else.

**Reading before drafting.**
- The compiled prompt in full (1,524 lines, paged): profile, formula sections 2–6 and 8–9, the packet with both sets of coordinator notes, the edition brief (event-list method, 8-word gate, working ranges), BOOK_MAP §§1–12, this book's STATE_LEDGER entry state, CANON_RULES, owner voice.
- Source `books/book-02-iron-circuit/chapters/chapter-01.md`–`chapter-04.md`, once each, then closed.
- This edition's Book 1 `chapter-57.md`–`chapter-60.md` in full; Book 1 `STATE_LEDGER.md` "After Movement 9 — BOOK 1 ENDING" with its coordinator rulings; greps of the Book 1 ledger and manuscript for the venue (Cinder House; no Ironyard, no Dace in Book 1), the notices' exact text and arrival, the step's Book 1 costs, the Pressure's acquisition (ch 47), the trough, Dessa's results, Joren's declaration, the fruit woman.
- `universe/UNIVERSE_BIBLE.md` (Path system, tiers, ranks, declarations, fragment notices).
- `editions/monroe-1.3/book-01-the-shattered/state/movement-009/AUTHORSHIP.md` and `AUTHOR-REPORT.md`, for the shape of these files.

**Method.** After the single source read, the author wrote a private event list in its own words in the scratchpad (outside the repo): calendar, the venue bridge, who wants what, and per-chapter beats with its own trial sequence (soft knees / short burst / breath / lean / burst-toward / second burst — not the source's order), its own sweep route and vantage, its own dispute shape (the complainant's own witness; Vell calls one witness aloud), its own seam discovery (Cael finds *to the left* in his own Power Log; the unasked Darrow step found going right in the old Log). It drafted from that list with the source closed.

**Honest note on source distance.** The method was not enough by itself for chapter 2. The first draft of the archive tour, Dace's board and the status scene tracked the source from memory (the probe, run early against all four source chapters, read ch 2 scene 3 at 19% and scene 4 at 12%, with matched sentences on the bindings, the Bronze chain example, "too early, not too late", Dace's debt/wrist/capacity list, Stedd vs the visiting Silver, and the closing systems/keepers line). Chapter 2 scenes 2–5 were thrown away and rewritten in full with new devices: the pine board of fixed points, Cael's own line as the one-link example, the red rule and *t.f.*, the quiet body as "bargaining with the floor", Dace's rings/dots/stitches, Stedd walking to the table to say "Fair", the two heads turning at the door. Smaller tracked sentences in ch 1, 4, 5, 6, 7 and 8 (Lira's "does it bother you" phrasing, "the towns", the crouch, "said it flatly", the rule's phrasing, the Power Log's "rather stay incomplete", the fingerprint run) were recomposed by hand after early probes and overlap runs.

**Drafting.** Eight chapters, written forward in order by the same author. No formula tool was run between chapters. Blocking slips fixed as noticed: two invented names removed (a witness renamed to Book 1's Dessa; a wrist-wrapped fighter made "the Stone woman from the tannery lanes"); Dessa's record corrected to two wins; a street name ("Lantern Row", "Tanners' Lane") removed; the Joren declaration moved to the Denvash notebook where Book 1 keeps it; the notice count ("three times in his life"); the seam/update day count made consistent across ch 7–8; Hesk's "forty years" removed; a Lira "I like him" changed so as not to pre-spend the Brom protected exchange.

**After all eight existed.**
1. `ed.sh overlap book-02-iron-circuit 1`: hits recomposed in context across several runs. Final: **0 unprotected, 6 protected**.
2. `ed.sh gates book-02-iron-circuit 1`: reader_standard=0, metadata=0, modern=0 on all eight.
3. `sweep_probe.sh book-02-iron-circuit 1 1` (packet-parsed sources ch 1 and ch 4): **0% skeleton** total; also run by hand against all four source chapters: **0% skeleton** total (no chapter above 1%).
4. `formula_metrics.py` once on the eight chapters. No formula-driven rewriting. A handful of sentences changed after that one run (a timeline fix in ch 7–8, a place name in ch 3, one letter-history line in ch 8); the metrics were not re-run.

Only the eight chapter files and these two state files were written (plus a scratchpad event list outside the repo). No git commands were run.
