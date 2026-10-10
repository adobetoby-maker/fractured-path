# AUTHORSHIP — Book 6, Movement 3 "The Evaluator and the Public Record" (chapters 14–20)

| Field | Value |
|---|---|
| Public byline | Monroe Jackson |
| Seat | `oconnor` 1.3.0 |
| Foundation | Monroe Jackson 1.3.0 |
| Requested author | Opus (Claude Opus 5.5) |
| Actual runtime model | `claude-opus-5-5` (Claude Opus 5.5), as stated in this session's environment. Run as a delegated agent session launched by the coordinator, after the earlier attempt was blocked by a usage limit before any manuscript output. |
| Packet | `editions/monroe-1.3/book-06-the-compacts-hand/state/movement-003/compiled-prompt.md` (movement brief: `editions/monroe-1.3/book-06-the-compacts-hand/packets/MOVEMENT-003.md`, with its `[B5-reconciled 2026-10-05]` and `[B5-reconciled 2026-10-06]` marks) |
| Coordinator rulings applied | The STATE_LEDGER blocks "AFTER MOVEMENT 1" (closed) and "AFTER MOVEMENT 2" (its coordinator rulings over the author end-state), and the task's standing rulings: season-blind (#42), feet and yards, Halcenvane weekdays; the first pole and "two renewals on paper" (#43) — every renewal count in M3 is "the grant and two renewals on paper"; *Caelen Hesk-ward* in instruments and registry voices (#44: the door log, Vastin's finding header); Hesk's clock not touched; the lane bill measured from the laying (ten counts, *bill, not flag*); at Gold the read takes the air or the body (recalled once, ch18); the managed band (wing three, ch17); Jent as procurator of record and counsel, not face, sender unsaid; "the house's counsel" at first mention in each chapter where she appears (ch15, 17, 18, 19, 20; she does not appear in ch14 or ch16); calendar per AFTER MOVEMENT 2 (first sitting day 40; M3's sittings day 47 and day 54; the nine-week inventory counted from day 8, so its sixth week is days 43–49 and the inventory is named on day 49). |
| Ruling NOT applied (flagged) | "Seln learns why Shadow was sealed in Book 6 Ch15, in this movement." See AUTHOR-REPORT owner flag 1: the plan, Book 5's ledger and the packet all locate this at *source* Ch15 (the cache; edition M6), and the M3 packet calls for nothing; following the packet "for exactly how much he learns" means he learns nothing here. Seln is not told in M3. |
| Edition | `monroe-1.3` |
| Book | The Fractured Path, Book 6 — The Compact's Hand (third movement) |
| Chapters | `editions/monroe-1.3/book-06-the-compacts-hand/manuscript/chapter-14.md` … `chapter-20.md` |
| Date | 2026-10-10 |

**One session.** One author drafted all seven chapters in one session and one context. No other model drafted any part of them, and no subagents were used. No git command was run (not even `git status`). Nothing outside the seven manuscript chapters and this movement's state folder was edited. `protected-patterns.txt` was not touched.

**Reading before drafting.**
- The compiled prompt in full (profile, formula §§2–6 and 8–9, the M3 packet, ch13 in full, the edition brief, BOOK_MAP §§1–13, STATE_LEDGER including AFTER MOVEMENT 1 and AFTER MOVEMENT 2, CANON_RULES, owner voice).
- M2's AUTHORSHIP, AUTHOR-REPORT (for report shape) and the head of its EVENT-LIST (for method).
- Manuscript ch3 (wing three's Shield bout), ch8 and ch11 (the band, the honest floor), and targeted greps of ch1–13 (the lodge-man, the post room, the Stone, the counsel, Withrow's two restrictions and the daughter, the six slips, the column).
- Targeted reads of the edition's Book 4 and Book 5 for canon the movement leans on: Vastin's room (B5 ch5, ch29, ch50 — the court, porter and pigeons, cabinet of shallow drawers, crooked seal-press, three trays, the left hand, two days from Norhold by the post road), the eleven questions and the twelfth (B4 ch59), the convening (B5 ch60 — not known to Cael), Umber's entry (B5 ch57), *Overdue* (B5 ch48), Zerin's "Silver bracket, next cycle" (B5 ch36, ch60), Ilsev's manner (B4/B5), Lira's certification (B4, the Ostrand station), Brom's family (B2/B4: father, sister, grandmother at the head of the table), Karis and Ternhall (B3), Hesk as a maker of measuring instruments (B4/B5).
- Source `books/book-06-the-compacts-hand/chapters/chapter-05.md` … `chapter-08.md`, read once for events.

**Method.** After the source read I wrote `state/movement-003/EVENT-LIST.md` in my own words and drafted each chapter from it and from BOOK_MAP. Each chapter was probed with `skeleton_probe.py` against source ch5–8 immediately after its first draft; every non-protected pair at or above 0.50 was rebuilt, and I also listed and recomposed the 0.40–0.50 band where it carried a source sentence's content and order. All edits were composed by hand and applied as exact-string replacements; no script split or joined sentences mechanically.

**Rebuilds after the per-chapter probe (first draft → final, skeleton / close).**
- ch14: 12% / 36% → 0% / 19%. The denial scene and the candle scene were **redrafted whole** with new entry points (the clerk's tread heard from the window; the letter-book laid beside the denial; the candle brought unasked); the petition, the four-for-four, the two chapter-fourteen files and the daughter's letter were recomposed.
- ch15: 15% / 31% → 3% / 17%. **Redrafted whole**: new opening scene (Lira's dawn drill with the two strangers on the gallery), the assistant's paid-for mistake, Brom's quire arithmetic, Withrow's "form thirty", Ephram's confiscated woodcut, and a new log; the source-tracking log of the first draft was discarded.
- ch16: 4% / 20% → 0% / 16%.
- ch17: 8% / 31% → 0% / 19%. Umber's covering note, Karis's reading of it, the second sitting's timings, the counter scene and the log were **redrafted** with new details (the parcel at the post counter; different exhibits timed; the gallery's knitting and pencil games; "a seat can't set aside a library"; the stove and seasoned oak).
- ch18: 10% / 24% → 3% / 17%. Daeva's statement header, Withrow's and Karis's readings, the letter's filing and Lira's rail speech recomposed; new beats added (the counsel's prediction; Ephram's captain's note; Cael's piece of her Storm).
- ch19: 24% / 50% → 2% / 24%. **Redrafted whole** from the event list with a new structure: entry through the Ternhall keeper's letter ("That's twice"), Seln's beans laid right to left, "walking the fences", Lira's bean, Withrow telling the haulier's story from the flour sack backward with the brown pocket code open.
- ch20: 21% / 46% → 1% / 19%. **Redrafted whole** with new devices (Karis's sealed slip *Both.*; Cael's numbered notes on Jent; Karis's card *TEXT. SHELF. PREAMBLE. NAMES.* and the counsel's quarter-turned rule; Havel eating bread over a handkerchief; Jent and the counsel on the fifth point; the printer's two headlines), and a new opening scene on the honest floor (Lira finds the lane by its dust's lamp-shadow).
- `ed.sh overlap` then listed 25 unprotected 8-word runs across the movement; each sentence was recomposed by hand. Final: **0 unprotected runs**.
