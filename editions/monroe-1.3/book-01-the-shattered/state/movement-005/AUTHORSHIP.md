# AUTHORSHIP — Movement 5 (chapters 28–33)

| Field | Value |
|---|---|
| Public byline | Monroe Jackson |
| Seat | `oconnor` 1.3.0 |
| Foundation | Monroe Jackson 1.3.0 |
| Requested author | Opus (Claude Opus 5.5) |
| Actual runtime model | `claude-opus-5-5` (Claude Opus 5.5), as stated in this session's environment |
| Packet | `editions/monroe-1.3/book-01-the-shattered/state/movement-005/compiled-prompt.md` (movement brief: `editions/monroe-1.3/book-01-the-shattered/packets/MOVEMENT-005.md`) |
| Edition | `monroe-1.3` |
| Book | The Fractured Path, Book 1 — The Shattered |
| Chapters | `editions/monroe-1.3/book-01-the-shattered/manuscript/chapter-28.md` … `chapter-33.md` |
| Date | 2026-10-01 → 2026-10-02 (across a restart) |

**Restart.** The run was cut off by a session rate limit after chapter 28 was complete and
chapter 29 stopped at Vell's "Begin when you're ready" (5,011 words, the bout not yet begun).
On the coordinator's instruction the same author and model resumed in the same session
context: the end of chapter 29 was re-checked, the chapter was continued from that exact
point (nothing already on disk was rewritten), and chapters 30–33 were written forward. The
original plan had opened chapter 30 with the bout; because chapter 29 was to be finished,
the bout went into chapter 29, which is why it is the longest chapter.

All six chapters were written forward with no scoring or measuring between chapters. During
the run the author corrected one blocking slip as noticed:
- ch 28: Coss had "served" the Statute 14 notice twice on adults; a notice for a Kindling
  result cannot have been served on adults, so it became "he knew the form, though he had
  never had cause to serve one".

After all six chapters existed, the author made:
1. the source-reuse pass. `ed.sh overlap book-01-the-shattered 5` found 12 unprotected runs
   (chs 28, 30, 32). All were rewritten by reading, events unchanged. It now reports zero
   unprotected runs (2 protected runs, allowed).
2. one run of `tools/formula_metrics.py` on the six chapters. No formula-driven rewriting was
   done.
