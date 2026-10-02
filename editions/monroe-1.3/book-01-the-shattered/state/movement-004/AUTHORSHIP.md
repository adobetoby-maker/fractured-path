# AUTHORSHIP — Movement 4 (chapters 21–27)

| Field | Value |
|---|---|
| Public byline | Monroe Jackson |
| Seat | `oconnor` 1.3.0 |
| Foundation | Monroe Jackson 1.3.0 |
| Requested author | Opus (Claude Opus 5.5) |
| Actual runtime model | `claude-opus-5-5` (Claude Opus 5.5), as stated in this session's environment |
| Packet | `editions/monroe-1.3/book-01-the-shattered/state/movement-004/compiled-prompt.md` (movement brief: `editions/monroe-1.3/book-01-the-shattered/packets/MOVEMENT-004.md`) |
| Edition | `monroe-1.3` |
| Book | The Fractured Path, Book 1 — The Shattered |
| Chapters | `editions/monroe-1.3/book-01-the-shattered/manuscript/chapter-21.md` … `chapter-27.md` |
| Date | 2026-10-01 |

All seven chapters were written forward in one run by the model above, with no scoring or
measuring between chapters. During the run the author corrected only blocking slips as they
were noticed:
- ch 21: the calendar ("five weeks… in Ardenmere" became the thirty-sixth day since Weaver's Row,
  a month in Ardenmere; the Unranked edge has no gate);
- ch 22: Lira's arithmetic line, so that it carries "the district's one new variable" with the
  right interval;
- ch 23: an invented name for Dessa's Fenrow opponent was removed (he is "the Fenrow Iron");
- ch 26: the cart page is quoted as ch 9 wrote it, and "Red Cap" was taken out of Lira's mouth.

After the full movement existed, the author made:
1. the source-reuse pass. `ed.sh overlap` found 31 unprotected runs, in chs 25–26. All were
   rewritten by reading, events unchanged, and it now reports zero.
2. one addition of about 500 words to ch 27 (the old man's "Four… You went the long side"),
   to bring the movement nearer its budget. It was overlap-checked afterward.
3. a few small fixes on reading ("nine days ago"; a bread duplication in ch 27; Renn's hold).

The formula metrics were run once, after all of this. No formula-driven rewriting was done.
