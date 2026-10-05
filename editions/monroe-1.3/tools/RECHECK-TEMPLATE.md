# Recheck / close checks for every movement (coordinator standard, 2026-10-04)

Every movement closes only after a recheck (Sol by default) that has read the FULL current movement and covers:

1. **Brief items.** Each one RESOLVED, PARTIAL or NOT, with quoted evidence (diff vs `pre-repair/`).
2. **Continuity.** Against BOOK_MAP, STATE_LEDGER rulings, the previous movement and later-book canon. Covers calendar, counts, knowledge boundaries, protected lines (exact; first where mapped) and reserved truths.
3. **Formula.** `formula_metrics.py` reproduced. Overlap 0 unprotected. Gates 0. `sweep_probe.sh` totals.
4. **Reader clarity.** Speaker attribution, referents, the 13-year-old lens, and the Reader Standard.
5. **Listening proof.** For every changed region and every chapter of the movement, check:
   - balanced quotes and italics;
   - `---` spacing;
   - numerals and abbreviations the narrator would misvoice;
   - homographs and ear collisions;
   - broken joins.
6. **Output.** A verdict (CLOSE / CLOSE WITH LINE FIXES / SECOND REPAIR), then exact line fixes in the `N. \`manuscript/chapter-NN.md\` / old: / new:` format, each verified to match once.

On CLOSE, the coordinator:
- applies the fixes;
- appends the STATE_LEDGER "After Movement N" block and its CLOSED note;
- records AUTHORSHIP (actual model) and the RUN-LEDGER line;
- commits and pushes;
- publishes the movement's chapters to the PWA edition (text only; bump totalChapters).
