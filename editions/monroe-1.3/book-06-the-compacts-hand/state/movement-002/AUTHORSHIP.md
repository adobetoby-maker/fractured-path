# AUTHORSHIP — Book 6, Movement 2 "Grounds and Standing" (chapters 8–13)

| Field | Value |
|---|---|
| Public byline | Monroe Jackson |
| Seat | `oconnor` 1.3.0 |
| Foundation | Monroe Jackson 1.3.0 |
| Requested author | Opus (Claude Opus 5.5) |
| Actual runtime model | `claude-opus-5-5` (Claude Opus 5.5), as stated in this session's environment. Run as a delegated agent session launched by the coordinator. |
| Packet | `editions/monroe-1.3/book-06-the-compacts-hand/state/movement-002/compiled-prompt.md` (movement brief: `editions/monroe-1.3/book-06-the-compacts-hand/packets/MOVEMENT-002.md`, with its `[B5-reconciled 2026-10-05]` and `[B5-reconciled 2026-10-06]` marks) |
| Coordinator rulings | The STATE_LEDGER "AFTER MOVEMENT 1" block and the task's standing rulings, applied over the packet: season-blind (#42), feet and yards, Halcenvane weekdays only; the first pole and "two renewals on paper" (#43) — no renewal count stated in M2 except the renewals table's three rows (grant + two renewals); formal instruments and registry voices name him *Caelen Hesk-ward* (#44), and the house's answer goes to the same address; people say Cael; Hesk's clock loses time; the new limits (air or body at Gold; ten counts slow, *bill, not flag*; the give as a cup); the managed band as redefined; Iron Rank One the foot of the seeding; Brom's review answering inside the ninety days; "the house's counsel" at first mention per chapter; Jent as the procurator of record ("Jent is counsel, not face"); Seln never told why Shadow was sealed; no placeholder or new name used. Mid-run coordinator messages (M1 CLOSED note) applied: Seln's ch2 plant honoured (ch8); Ostrand kept close at the foot of the bluff (the corrected point 4); the district hall not described as cold. |
| Edition | `monroe-1.3` |
| Book | The Fractured Path, Book 6 — The Compact's Hand (second movement) |
| Chapters | `editions/monroe-1.3/book-06-the-compacts-hand/manuscript/chapter-08.md` … `chapter-13.md` |
| Date | 2026-10-06 |

**One session.** One author drafted all six chapters in one session and one context. No other model drafted any part of them, and no subagents were used. No git command was run. Nothing outside the six manuscript chapters and this movement's state folder was edited. `protected-patterns.txt` was not touched.

**Reading before drafting.**
- The compiled prompt in full (profile, formula §§2–6 and 8–9, the M2 packet, ch7 in full, the edition brief, BOOK_MAP §§1–13, STATE_LEDGER including the AFTER MOVEMENT 1 block and r1 notes, CANON_RULES, owner voice).
- Manuscript ch1–6 in full from disk, for voice and continuity; ch7 inside the prompt; the ledger's "Movement 1 CLOSED" note after the coordinator's message.
- M1's EVENT-LIST, AUTHORSHIP, AUTHOR-REPORT and REPAIR-BRIEF (for method and report shape).
- Targeted greps of edition B1–B5 for Ostrand's geography, Fenmark, Vell's yard and the barn, Prynn, Force Path doctrine, Coss, Umber, Pellin (a woman; the eleven seconds; Kindling at fourteen), *Hesk-ward*, the first renewal before the inspection delegation, and Havel's windows (B5 ch25, ch58: the rotation sheet, the thumb, the sheets between the manuals).
- Source `books/book-06-the-compacts-hand/chapters/chapter-03.md` and `chapter-04.md` in full, and the end of `chapter-02.md`, read once for events.

**Method.** After the source read I wrote `state/movement-002/EVENT-LIST.md` and drafted from it and BOOK_MAP; the source chapters were not reopened. Each chapter was probed with `skeleton_probe.py` against source ch2–4 immediately after its first draft, and every listed pair that was not protected or packet text was rebuilt by hand.

**Rebuilds after the per-chapter probe (first draft → final, skeleton / close).**
- ch8: 2% / 14% → 1% / 9%. Two trivial pairs and the answer's address recomposed; later, five 8–10-word runs flagged by `ed.sh overlap` recomposed.
- ch9: 6% / 23% → 1% / 8%. **The Lira scene at the north wall was redrafted whole** (new entry, Cael telling it backward, the Fenmark slate wiped so the form would be clean, Vell's yard heard from three streets off); Withrow's escort line and the log line recomposed.
- ch10: 9% / 25% → 1% / 14%. The notice's text, the per-seal exchange, Jent's second compliment, the conference's measures, the counsel's coach read and the "appetite" log were recomposed.
- ch11: 8% / 22% → 0% / 12%. Withrow's office scene was recomposed sentence by sentence (the entry text, the column, the price, the transcript, the *choosing* note), with the year's geometry and the coats' log.
- ch12: 4% / 19% → 1% / 12%. The "want" log redrafted; the Force's question, Lira's opening line, the envelopes' framing recomposed.
- ch13: 10% / 25% → 2% / 15%. The frames opener, the room count, Withrow's bow, the coach council, Seln's grades, the session log and the window entry recomposed around the protected lines.

**Formula pass.** Scene breaks were merged where action ran on (ch8, ch9, ch10, ch12, ch13). One paragraph-split experiment was reverted because it raised the median. No script split or joined sentences; every change was an exact-string edit composed by hand.

**Repair r1 (same session, same model `claude-opus-5-5`).** Made from `REPAIR-BRIEF.md` and both reviews.
- EVENT-LIST.md's tracked lines were rewritten first. ch10 and most of ch13 were re-entered whole; the tracked scenes of ch8, ch9, ch11 and ch12 were re-entered or recomposed by hand.
- No subagents were used. Nothing outside the six chapters and this folder was edited.
- One read-only `git status` was run by mistake while checking a failed edit. It changed nothing, and no other git command was run.
- Details are in AUTHOR-REPORT.md under "Repair r1".
