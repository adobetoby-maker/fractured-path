# AUTHORSHIP — Book 6, Movement 5 "The Keeper and the Road" (chapters 28–34)

| Field | Value |
|---|---|
| Public byline | Monroe Jackson |
| Seat | `oconnor` 1.3.0 |
| Foundation | Monroe Jackson 1.3.0 |
| Requested author | Opus (Claude Opus 5.5) |
| Actual runtime model | `claude-opus-5-5` (Claude Opus 5.5), as stated in this session's environment. Run as a delegated agent session launched by the coordinator. |
| Packet | `editions/monroe-1.3/book-06-the-compacts-hand/state/movement-005/compiled-prompt.md` (movement brief: `packets/MOVEMENT-005.md`, with its `[B5-reconciled 2026-10-05]` marks) |
| Coordinator rulings applied | STATE_LEDGER "AFTER MOVEMENT 1–4" blocks and their rulings and CLOSED notes; the task's standing rulings (season-blind #42; feet and yards; Halcenvane weekdays; the first pole and "two renewals on paper" #43; *Caelen Hesk-ward* in instruments #44; Hesk's clock loses time; the lane bill ten/ten/twelve, *bill, not flag*; the read at Gold takes the air or the body; the managed band; Iron Rank One the foot; Jent procurator of record, counsel not face; "the house's counsel" at first mention per chapter; the day-71 meet, day-75 sitting, day-76 gate; Seln not told why Shadow was sealed and unaware a sealed thing exists; the day-45 Velmere letter sealed in Brom's left pocket; the anchor's reach, rate and price blank except what the packet and notice give; placeholders unused, no new names) |
| Edition | `monroe-1.3` |
| Book | The Fractured Path, Book 6 — The Compact's Hand (fifth movement) |
| Chapters | `editions/monroe-1.3/book-06-the-compacts-hand/manuscript/chapter-28.md` … `chapter-34.md` |
| Date | 2026-10-10 |

**One session.** One author drafted all seven chapters in one session and one context. No other model drafted any part of them; no subagents were used. No git command was run (not even `git status`). Nothing outside the seven manuscript chapters and this movement's state folder (`EVENT-LIST.md`, `AUTHORSHIP.md`, `AUTHOR-REPORT.md`) was edited. `protected-patterns.txt` was not touched.

**No source chapter was opened.** Per the new binding method, I did not open, read, `cat`, `grep` or `--show` any file under `books/book-06-the-compacts-hand/chapters/` at any point in this session — not before drafting, not during, not after. The packet's "Read before drafting" line was not followed. The only contact with the source was mechanical and blind: `skeleton_probe.py` and `sweep_probe.sh` were run **without `--show`**, so they printed percentages per chapter and per scene and never a source sentence; and `ed.sh overlap` printed only the manuscript side of each shared run. Where a scene probed high, I re-composed it from my own event list without seeing what it matched.

**What I read.** The compiled prompt in full (profile; formula §§2–6, 8–9; the M5 packet; the previous ending ch27 as compiled; the edition brief; BOOK_MAP §§1–13; STATE_LEDGER with AFTER M1–M4; CANON_RULES; owner voice). M4's AUTHORSHIP and AUTHOR-REPORT (for shape). The current manuscript ch27 from disk (it carried recheck line fixes since the compile: Lira's question now written in capitals; Seln's horse question), ch1 opening and suite run, ch13's Havel window, ch22's Seln window, ch24's opening (bout voice), and greps of ch1–27 for geography and recurring details. The edition's Book 5 ch56 (how a reach and a notice are rendered on this edition's page). Book 7's BOOK_MAP and STATE_LEDGER greps for Anchor's later behaviour ("wants doorways"; "can release a laid point from inside"). All of these are edition files, not source chapters.

**Method.** I wrote `EVENT-LIST.md` first, in my own words, choosing each scene's entry and order and inventing every mechanism the packet leaves open (the trip's shape, the cut's geometry, the team, the specialist's craft, the fight's four exchanges, the cascade's grammar, the birthday). I drafted from that list, the packet, BOOK_MAP §§3–4 and §8, and the ledger. Packet and §8 protected lines were taken from the packet/BOOK_MAP text only. After each chapter I ran `formula_metrics.py` and `skeleton_probe.py` (no `--show`); scene breaks were removed at points I chose where two scenes were continuous (a one-line deletion of the `---` marker), rhythm was adjusted by reading and re-composing sentences by hand, and one scene (ch33's naming scene, 30% close) was redrafted whole from the event list. All edits were exact-string replacements composed by hand; no script split or joined sentences.
