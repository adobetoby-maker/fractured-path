# AUTHORSHIP — Book 5, Movement 7 "Silver" (chapters 40–46)

| Field | Value |
|---|---|
| Public byline | Monroe Jackson |
| Seat | `oconnor` 1.3.0 |
| Foundation | Monroe Jackson 1.3.0 |
| Requested author | Opus (Claude Opus 5.5) |
| Actual runtime model | `claude-opus-5-5` (Claude Opus 5.5), as stated in this session's environment. Run as a delegated agent session launched by the coordinator. |
| Packet | `editions/monroe-1.3/book-05-the-silver-standard/state/movement-007/compiled-prompt.md` (movement brief: `editions/monroe-1.3/book-05-the-silver-standard/packets/MOVEMENT-007.md`) |
| Coordinator rulings | Sent with the task and applied over the packet: the calendar (#41; BOOK_MAP §6 [M6-redated]): ring complete at dawn T11 and the Shield captain T11; the duelist and Vastin's seat T14 ("thirteen days"); the rest day / birthday T15 with the date left OWNER-pending; the team trial T16; Rooke's "four days … seven" not restated. The exhibitions fought in the ring on the main floor. Lira's LEFT shoulder on half work for a week from T9. Brom continental Copper champion. Ternhall's lattice anchors used as PROVISIONAL house doctrine. Continental format (#39) for bracket arithmetic and the exhibition format for both Silver bouts. No new names, no season, month or English weekday names, no metres, no year increments. Vastin (~1,500) and Seln (~500) cutaways at full weight. One mid-run note: the M6 recheck changed one line in ch39 ("That was for Karis to choose."); nothing drafted here depends on it. |
| Edition | `monroe-1.3` |
| Book | The Fractured Path, Book 5 — The Silver Standard (seventh movement; first movement of the last third) |
| Chapters | `editions/monroe-1.3/book-05-the-silver-standard/manuscript/chapter-40.md` … `chapter-46.md` |
| Date | 2026-10-05 |

**One session.** One author drafted all seven chapters in one session and one context. No other model drafted any part of them, and no subagents were used. No git command of any kind was run. Nothing outside the seven manuscript chapters and this movement's state folder was edited.

**Reading before drafting.**
- The compiled prompt, read in full in pages: profile, formula §§2–6 and 8–9, the movement brief and its coordinator note, the edition brief, BOOK_MAP §§1–14 with every `[B4-reconciled]` and `[M6-redated]` mark, STATE_LEDGER ENTRY and AFTER MOVEMENTS 1–6 with their coordinator rulings, CANON_RULES and the owner voice.
- `manuscript/chapter-39.md` in full (the previous ending).
- Targeted reads and greps of the edition's own manuscript for canon the packet relies on: the two Silver filings and Rooke's council (ch32); the trial rule and *Again.* (ch32); the main floor, its sockets and high windows (ch30); the caravan captain's panes and "breath, plant, pane" (ch21); "I think Shield is solved" (ch25); Vastin's register, room and left hand (ch24, ch29); the Compact row, seat twelve, Ilsev and Havel (ch32, ch38); Daeva's likeness and walk (ch29, ch31); the M1 inventory's wording and year counts (ch1); Bracken's first "quarry stone" (ch28); Quenna at Greyvane (B3/B4); sixteen at Halcenvane (B4 ch37); the fight voice of ch35.
- `OWNER-DECISIONS.md` #38–#41.
- Source `books/book-05-the-silver-standard/chapters/chapter-13.md`, `chapter-14.md`, `chapter-15.md`, read once each for events and people, then closed.

**Method.** After the source read I wrote a private event list and a day-by-day calendar in my scratchpad (not in the repository) and drafted from that list and BOOK_MAP. The source chapters were not reopened while drafting. Each chapter was probed with `skeleton_probe.py` against the three source chapters immediately after its first draft, and with a local copy of the probe set to list pairs down to 0.40, so that close passages could be found and rebuilt. Two chapters' worst scenes were redrafted whole (below).

**Rebuilds after the per-chapter probe (first draft → final, skeleton / close).**
- ch40: 1% / 8%. Clean on first draft. Reworked by hand for rhythm (first draft ran sentence mean 11.2 with 38% short sentences); the short stair scene merged into Rooke's session. Final 2% / 8% (the remaining skeleton line is the packet's "you lose the bout").
- ch41: 3% / 16%. Karis's debrief had followed the source's image (the record as a floor, then a ceiling); rewritten round her "two columns". The midpoint log's middle rebuilt in new words around the protected lines. Final 3% / 13%; the skeleton hits are protected log lines.
- ch42: 0% / 8%. One line rebuilt. Final 0% / 7%.
- ch43: 4% / 11%. The rest-day opening, the date line and the likeness stall had followed the source; rebuilt. Final 1% / 8%.
- ch44: 10% / 28%. The blue-door table had followed the source's order, images and table-registers paragraph. **Redrafted whole** after the Seln cutaway (which was clean and kept): new entry through the proprietor at the door; Lira's sign on the table; Brom's "I look like I'm going to be here a while"; Karis sitting on her hands; Ephram's lock-house; a minute-each storytelling game in place of the source's catalogue of registers; Seln's whistling-clerk story; the post before the parcel; a new book description; a new ending on the quay. Final 2% / 11%.
- ch45: 6% / 20%. The inspection had followed the source's order and lines; **redrafted whole** in a new order (Lira, Karis, Brom, Cael) with new findings. The inventory's frame lines, Rooke's brief lines and Umber's reasoning rebuilt. Final 3% / 11%.
- ch46: 8% / 20%. The trial itself was largely clean, but the aftermath (Rooke's review, Ephram's lead-in, the log frame, Lira at the table) had followed the source; **redrafted whole** with new entry points (Rooke in the tunnel, a five-line review sheet passed round the table, Ephram at the courtyard pump, Lira at the door). Eight stormlane and E1/E2 lines rebuilt. Final 1% / 11%.

All rhythm and length changes were made by reading and by hand (Edit/Write, or exact-string Python replacements I wrote one by one). No script split or joined sentences or paragraphs by rule.
