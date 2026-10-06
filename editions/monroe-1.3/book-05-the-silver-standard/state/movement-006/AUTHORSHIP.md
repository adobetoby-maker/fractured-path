# AUTHORSHIP — Book 5, Movement 6 "Three Floors" (chapters 33–39)

| Field | Value |
|---|---|
| Public byline | Monroe Jackson |
| Seat | `oconnor` 1.3.0 |
| Foundation | Monroe Jackson 1.3.0 |
| Requested author | Opus (Claude Opus 5.5) |
| Actual runtime model | `claude-opus-5-5` (Claude Opus 5.5), as stated in this session's environment. Run as a delegated agent session launched by the coordinator. |
| Packet | `editions/monroe-1.3/book-05-the-silver-standard/state/movement-006/compiled-prompt.md` (movement brief: `editions/monroe-1.3/book-05-the-silver-standard/packets/MOVEMENT-006.md`) |
| Coordinator rulings | Seven rulings sent with the task: the continental format (#39) and its arithmetic for every featured bout; ratings #38 and public capabilities #40 (Cael does not fight); sided injuries; canon limits (Zerin's and Marek's Kindling/rank, Karis's improvisation not rehearsed, Brom's review notice-only, the Velmere letter verbatim, B4 notation, the empty chair, no meta reference); world rules (no season names, no month order, feet and yards, house weekdays, year counts not incremented, no new names); protected wording kept whole; companion fights in Cael's POV with the cutaway sizes given. Applied wherever they differ from the packet. |
| Edition | `monroe-1.3` |
| Book | The Fractured Path, Book 5 — The Silver Standard (sixth movement; middle third) |
| Chapters | `editions/monroe-1.3/book-05-the-silver-standard/manuscript/chapter-33.md` … `chapter-39.md` |
| Date | 2026-10-05 |

**One session.** One author drafted all seven chapters in one session and one context. No other model drafted any part of them, and no subagents were used. No git command of any kind was run.

**Reading before drafting.**
- The compiled prompt, read in full in pages: profile, formula §§2–6 and 8–9, the movement brief, the preceding chapter (ch32, embedded), the edition brief, BOOK_MAP §§1–14 with every `[B4-reconciled]` mark, STATE_LEDGER ENTRY and AFTER MOVEMENTS 1–5 with their coordinator rulings, CANON_RULES and the owner voice.
- `manuscript/chapter-31.md` and `chapter-32.md` in full.
- `packets/MOVEMENT-007.md` (read only to check the hand-off calendar; nothing drafted from it).
- Targeted greps of the edition's own manuscript for canon facts the packet relied on: Ivenne and the draw (ch30), Ternhall's lattice and Ember's contact rule (B4 ch11; B5 ch11), the buried fair-day Copper (B5 ch3, ch8), Brom's family (B4 ch37), Zerin's and Marek's extracts (ch19, ch25), the Copper schedule and the ring (ch30, ch32).
- Source `books/book-05-the-silver-standard/chapters/chapter-10.md`, `chapter-11.md`, `chapter-12.md`, read once each for events and people, then closed.

**Method.** After the source read I wrote a private event list and a day-by-day calendar in my scratchpad (not in the repository) and drafted from that list and BOOK_MAP. The source chapters were not reopened while drafting. Each chapter was probed with `skeleton_probe.py` against the three source chapters immediately after its first draft, and with a local copy of the probe set to list pairs down to 0.35 so that close passages could be found and rebuilt.

**Rebuilds after the per-chapter probe (first draft → final, skeleton / close).**
- ch33: 2% / 10% (scene 3 at 22% close, scene 5 at 19%). The Zerin-room dialogue and two images had followed the source. Rewritten whole by hand with new lines and images, plus a rhythm pass. Final 0% / 2%.
- ch34: 15% / 27% (scene 4 at 33% skeleton). The study collapse, the supper, the mirror study, the audit and the stair had followed the source's dialogue. Redrafted whole from beats with new entry points (Karis demonstrating the tells on her feet, Ivenne's paragraph read aloud, Brom's oak story, Ephram's fence image, the kit-bag strap, the stair chart in new terms). Then line rebuilds of the remaining close sentences. Final 2% / 9%; the remaining skeleton lines are packet lines.
- ch35: 1% / 9%. Redrafted for rhythm (first draft ran sentence mean 17); five close lines rebuilt. Final 0% / 6%.
- ch36: 10% / 25% (scenes 5–6 over 15%). The accounting, the boards, Lira's report and the stair had followed the source. Redrafted whole: Rooke's accounting now turns on "the measurement" (how far from Silver), Karis's walk report on "a person, not a building", the stair on new terms. Final 3% / 10%; the remaining skeleton lines are packet lines.
- ch37: 1% / 12%. Seventeen lines rebuilt (the E2 opening, the toll images, the interval, the con's close). Final 0% / 6%.
- ch38: 4% / 12%. Ten lines rebuilt; scenes merged. Final 0% / 7%.
- ch39: 7% / 17%. Withrow's report, the boards and Karis's notebook had followed the source's order and wording. Redrafted whole; Karis's finding rewritten in new words around the packet sentence. Final 2% / 7%.

All rhythm and length changes were made by reading and by hand (Edit/Write or exact-string Python replacements I wrote one by one). No script split or joined sentences or paragraphs by rule.
