# AUTHORSHIP — Book 6, Movement 4 "Within the System" (chapters 21–27)

| Field | Value |
|---|---|
| Public byline | Monroe Jackson |
| Seat | `oconnor` 1.3.0 |
| Foundation | Monroe Jackson 1.3.0 |
| Requested author | Opus (Claude Opus 5.5) |
| Actual runtime model | `claude-opus-5-5` (Claude Opus 5.5), as stated in this session's environment. Run as a delegated agent session launched by the coordinator. |
| Packet | `editions/monroe-1.3/book-06-the-compacts-hand/state/movement-004/compiled-prompt.md` (movement brief: `packets/MOVEMENT-004.md`, with its `[B5-reconciled 2026-10-05]` and `[B5-reconciled 2026-10-06]` marks) |
| Coordinator rulings applied | STATE_LEDGER "AFTER MOVEMENT 1–3" blocks and their coordinator rulings; the 2026-10-10 Seln correction; the task's standing rulings (season-blind #42; feet and yards; Halcenvane weekdays; first pole / "two renewals on paper" #43; *Caelen Hesk-ward* in instruments #44; Hesk's clock; lane bill; the read at Gold; the managed band; Iron Rank One the foot; Jent procurator of record, counsel not face; "the house's counsel" at first mention per chapter; Seln not told about Shadow; the day-45 Velmere letter sealed in Brom's left pocket; placeholders unused, no new names). The coordinator's mid-run message (M3 CLOSED after r3) was applied after a re-read of ch20 and the closed M3 ledger block — see AUTHOR-REPORT owner flag 1 (the road meet's day). |
| Edition | `monroe-1.3` |
| Book | The Fractured Path, Book 6 — The Compact's Hand (fourth movement) |
| Chapters | `editions/monroe-1.3/book-06-the-compacts-hand/manuscript/chapter-21.md` … `chapter-27.md` |
| Date | 2026-10-10 |

**One session.** One author drafted all seven chapters in one session and one context. No other model drafted any part of them; no subagents were used. No git command was run. Nothing outside the seven manuscript chapters and this movement's state folder was edited (a probe helper script lived in the session scratchpad, outside the repository). `protected-patterns.txt` was not touched.

**Reading before drafting.** The compiled prompt in full (profile; formula §§2–6, 8–9; the M4 packet; ch20; the edition brief; BOOK_MAP §§1–13; STATE_LEDGER with AFTER M1–M3; CANON_RULES; owner voice). M3's AUTHORSHIP, AUTHOR-REPORT and EVENT-LIST head (for shape and method). Manuscript ch19 in full and targeted greps of ch1–20 (the lodge, the covered walk, the Stone, Jent's "Advocate", the door log, the road-meet card, Pellin). Targeted reads of the edition's Book 5 for the confluence (ch20–23: two days north of Ostrand; the hall at the tongue's point; the innkeeper's framed ruling; the exhibition provision's format, ch7) and Ternhall's anchors (ch34, ch46). Source `books/book-06-the-compacts-hand/chapters/chapter-09.md`–`chapter-11.md`, read **once**, for events. After the coordinator's message: ch20 re-read in full from disk and the closed AFTER MOVEMENT 3 block.

**Method.** After the single source read I wrote `EVENT-LIST.md` in my own words, closed the source, and drafted every chapter from the event list, the packet and BOOK_MAP. After each chapter I ran `skeleton_probe.py` against source ch9–11 and a helper that lists every pair at ≥0.40, and did a side-by-side self-check of the flagged passages against the source; tracked passages were rebuilt from the event list (new entry points, new devices, reordered beats), not by synonym swaps or sentence splits. The source was reopened only (a) for those post-chapter checks and (b) once by `grep` to confirm the escort order's Tier B text character for character. All edits were composed by hand and applied as exact-string replacements; scene breaks were merged by hand where two scenes were continuous.
