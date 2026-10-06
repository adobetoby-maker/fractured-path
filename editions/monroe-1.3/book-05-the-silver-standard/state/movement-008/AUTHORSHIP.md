# AUTHORSHIP — Book 5, Movement 8 "The Challenge" (chapters 47–53)

| Field | Value |
|---|---|
| Public byline | Monroe Jackson |
| Seat | `oconnor` 1.3.0 |
| Foundation | Monroe Jackson 1.3.0 |
| Requested author | Opus (Claude Opus 5.5) |
| Actual runtime model | `claude-opus-5-5` (Claude Opus 5.5), as stated in this session's environment. Run as a delegated agent session launched by the coordinator. |
| Packet | `editions/monroe-1.3/book-05-the-silver-standard/state/movement-008/compiled-prompt.md` (movement brief: `editions/monroe-1.3/book-05-the-silver-standard/packets/MOVEMENT-008.md`) |
| Coordinator rulings | Sent with the task and applied over the packet: the #41 calendar (T17–T18 the empty board; T19 filing and the board at dusk; T20 convening; T21 third place, then the ring rebuilt at midnight as a NEW build; T22 the ring two days out; T23 the eve). M7 inheritance: Rhagen's semifinal loss in one line ("the ledger counts ground"); the trial format not restated; Rooke's five findings drive third place. Cutaway-heavy by design (Daeva ≈7,000, Vastin ≈2,000, Seln ≈1,000). Daeva Kindled at thirteen, six years since the garden court, seven in the program, never "eleven"; public dossier and trial memory only; no theory of Cael; no English weekday ("Tuesday calibration" rendered as the design session). The council's mechanism spoken only among the four; Seln and Ephram outside; Shadow sealed and Seln never told why. Lira's LEFT shoulder; Brom continental Copper champion; Ternhall's anchors PROVISIONAL; ratings #38; formats #39/#40. No new names, no season/month/English weekday names, no metres, no year increments, the tournament's length in days never stated. Mid-run note received: M7 closed with five line changes; ch46's ending re-read from disk; nothing drafted here depended on the changed lines. |
| Edition | `monroe-1.3` |
| Book | The Fractured Path, Book 5 — The Silver Standard (eighth movement) |
| Chapters | `editions/monroe-1.3/book-05-the-silver-standard/manuscript/chapter-47.md` … `chapter-53.md` |
| Date | 2026-10-05 |

**One session.** One author drafted all seven chapters in one session and one context. No other model drafted any part of them, and no subagents were used. No git command was run. Nothing outside the seven manuscript chapters and this movement's state folder was edited (scratch files lived in the session scratchpad only).

**Reading before drafting.**
- The compiled prompt in full, in pages: profile, formula §§2–6 and 8–9, the movement brief with both coordinator notes, the edition brief, BOOK_MAP §§1–14 with every reconciliation mark, STATE_LEDGER ENTRY and AFTER MOVEMENTS 1–7, CANON_RULES and the owner voice.
- `manuscript/chapter-46.md` in full (inside the compiled prompt, and its ending again from disk after the coordinator's recheck note); `chapter-45.md` in full for voice and the trial's canon.
- Targeted greps of the edition: the guesting-house keeper ("he", ch28/ch42); the back room (ch33/ch41); Ephram and the lock-keeper (ch44); the hired hall; Daeva's earlier appearances (ch29, ch31); Cael's circuit losses (B2); the B4 slip and stove (B4 ch53) and Lira's B4 version of "still be you"; M7's author report for its section layout.
- Source `books/book-05-the-silver-standard/chapters/chapter-16.md` … `chapter-19.md`, read once each for events and people.

**Method.** After the source read I wrote a private event list and a day-by-day calendar in the scratchpad and drafted from it and BOOK_MAP. The source chapters were not reopened while drafting. Each chapter was probed with `skeleton_probe.py` against the four source chapters right after its first draft, and with a local scratch copy of the probe set to list pairs down to 0.40 (and once to 0.36) to find close passages.

**Rebuilds after the per-chapter probe (first draft → final, skeleton / close).**
- ch47: 1% / 9%. Clean. Scene breaks merged (seven to four) for spacing; two sentences lengthened.
- ch48: 9% / 23%. The board at dusk and the back-room council had followed the source's order and images; **both scenes redrafted whole** (a new entry for the board, the ladder and the strip; formation re-seen; Seln moved to the tower porch; the council reordered: Lira's case, Brom, Karis, then Lira's own side last). Final 3% / 14%.
- ch49 (Daeva): 6% / 30% on first draft, with the objection room at 44%. **Redrafted whole**: new entry (the design session on the second morning of the empty board), a new Zerin scene, the dossier moved to the third night, the garden and the ladder recomposed, the risk officer's case moved to the stair before the room, the room rebuilt (the head gives up his own chair; counsel's junior reads the papers aloud; the lead instructor on the stair). A pressure-hour scene and a breakfast scene added. Final 0% / 11%.
- ch50: 6% / 21%. Vastin's clearing of the calendar reordered (the silences first, then the book) with new items; Umber's preface and the healers line rebuilt. Final 2% / 14%.
- ch51: 6% / 17% (aftermath 46%). The aftermath **redrafted whole** (Rooke's sheet with no fighter's name; Marek hands Brom his book). Final 2% / 14%.
- ch52: 14% / 31%. The ring walk had followed the source closely; **redrafted whole** with a new entry (Cael on his knees at the grounding trench; she arrives), a new order (floor figures and the crown first; the trial line at the east break; breaks; the mast; losing; the north side), and new words throughout. The toast's log rebuilt. Final 4% / 17%.
- ch53: 19% / 38% on first draft. **Redrafted whole**: new entry (the Seln cutaway opens the chapter, at the fifth bell); Rooke's padwork rewritten; the models reordered so that both dead models come before Cael's recall, and the recall produces the third; the council reordered (Karis argues the alternative before anything is proposed); the Shadow price and the silence paragraph rewritten; the stove and the log rewritten; the night's sounds new. Final 3% / 18%.

All rhythm, length and wording changes were made by reading and by hand, with exact-string replacements written one by one. No script split or joined sentences or paragraphs by rule; scene merges removed a `---` line only where the action was continuous.
