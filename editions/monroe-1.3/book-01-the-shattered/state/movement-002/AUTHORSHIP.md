# AUTHORSHIP — Movement 2 (chapters 7–13)

| Field | Value |
|---|---|
| Public byline | Monroe Jackson |
| Seat | `oconnor` 1.3.0 |
| Foundation | Monroe Jackson 1.3.0 |
| Requested author | Opus (Claude Opus 5.5) |
| Actual runtime model | `claude-opus-5-5` (Claude Opus 5.5), as stated in this session's environment |
| Packet | `editions/monroe-1.3/book-01-the-shattered/state/movement-002/compiled-prompt.md` (movement brief: `editions/monroe-1.3/book-01-the-shattered/packets/MOVEMENT-002.md`) |
| Edition | `monroe-1.3` |
| Book | The Fractured Path, Book 1 — The Shattered |
| Chapters | `editions/monroe-1.3/book-01-the-shattered/manuscript/chapter-07.md` … `chapter-13.md` |
| Date | 2026-10-01 |

All seven chapters were written forward in one run by the model above, without
scoring or editing between chapters. After the full movement existed, the author made
only these changes: (1) the coordinator's source-reuse pass — every run of ten or more
words shared with the source edition rewritten in new words (events unchanged), until
`tools/source_overlap.py` reported zero unprotected runs; (2) name/canon repairs (two
invented names removed — Garrik's wife and a sanctioned-season town; Cael's name kept
out of Vell's ledger to protect the Book 1 ending); (3) small calendar and Reader
Standard fixes (two lines implying swearing, one forward-flash aside). No formula-driven
rewriting has been done; measured drift is reported in AUTHOR-REPORT.md.
