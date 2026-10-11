You are the whole-arc reader for Book 6, "The Compact's Hand", in the Monroe 1.3 edition of The Fractured Path. You sit the independent review seat with fresh context. This is Step 2 of the book-completion pass: the first time anyone reads the sixty chapters straight through as one book.

**Do not modify any manuscript file.** Working directory: /Users/drive/fractured-path-monroe13. Run no git commands of any kind, not even read-only ones. Do not open anything under books/ (the source edition) except where section 10 below tells you to.

## The model to follow
Read Book 5's read first and match its structure, depth and judgement:
- editions/monroe-1.3/book-05-the-silver-standard/state/completion/whole-arc-read.md

## Read before the manuscript
Under editions/monroe-1.3/:
- EDITION_BRIEF.md (voice, O'Connor controls, Reader Standard: a 13-year-old reader).
- OWNER-DECISIONS.md, all of it. For this book especially #33, #35–#46. Owner-pending placeholders (Bede, Maud, Gwen, Abbot) are not findings.
- book-06-the-compacts-hand/BOOK_MAP.md (§3–§4 plan, §6 calendar, §8 protected text, §9 reserved truths).
- book-06-the-compacts-hand/STATE_LEDGER.md, all nine AFTER MOVEMENT blocks. They hold the coordinator rulings. A ruling there is settled; report text that contradicts a ruling, not the ruling.
- book-06-the-compacts-hand/protected-patterns.txt. Never propose a change to a protected run.
- book-06-the-compacts-hand/state/completion/COMPLETION-PLAN.md.
- The last two chapters of Book 5 (book-05-the-silver-standard/manuscript/chapter-59.md, chapter-60.md) for the entry seam, and book-07-void-roads/BOOK_MAP.md §3 first movement for the exit seam.

## Then read
book-06-the-compacts-hand/manuscript/chapter-01.md through chapter-60.md, in order, every word. Keep running notes in state/completion/whole-arc-notes.md as you go.

## Check, across movements (not inside one movement; those were reviewed already)
1. **Continuity.**
   - The calendar: every day number, "days since", interval and deadline against BOOK_MAP §6 and the ratified table in the ledger's AFTER MOVEMENT 7 block (ruling and Brom's panel day 201; council and last bout day 202; M9 entry day 203; year close day 207; the Line after). The book is season-blind: no season names, no month order, no English weekday names (#42).
   - Counts and figures: the lane bill (ten / ten / twelve; a bill, not a flag); renewals ("two renewals on paper" everywhere except the protected first pole, which reads "a stamp renewed four times" in ch7 and ch60); Anchor distances (about 10 / 12 / 14 feet); nine fragments with the anomaly uncounted; the clean door (day 75 to 115); "twice more" standing at two; Hesk's clock losing time.
   - Titles and offices: Gault is the evaluator of record; "the certifying office" is the Archmarshal's office; the challenge addresses Caelen Hesk-ward (#44).
   - Quotations: every line quoted back later against its first occurrence, word for word.
   - Names, pronouns, ranks, ages, sides of the body, who owns what, where each person is.
   - Seams: Book 5 ch60 into ch1; ch60 into Book 7's plan (the shelf is the second camp past the Line and the first fire).
2. **Knowledge boundaries.** Who knows what, when. In particular: Seln learns why Shadow is sealed in the M6 chapters, not before; Shadow is sealed "while its use can be seen by anyone who could carry the seeing west"; the Kindling mechanics (the Arbiter wakes; the brass plate; the corrections function failing safe); the Velmere day-45 envelope stays sealed on Brom's table; nothing in §9 reserved truths is spent early.
3. **Book-wide repetition.** The worst ten: images, gestures, sentence moves, tics and tag habits that recur across movements until a reader notices. Give counts and chapter:line examples.
4. **Arc and pacing.** Does the book's argument (work within the system / the system is the hand) build and turn where the plan says? Where does it sag or rush? Movements 5–9 were written fuller by owner ruling (#45): say where the fullness earns its length and where it reads as padding.
5. **Protected lines** (BOOK_MAP §8 and the Tier B units): all present, each once, each where mapped, character for character.
6. **Reader Standard.** Anything a 13-year-old could not follow in one pass, or should not read.
7. **Rhythm outliers.** Chapters whose sentence length or scene length sits far from the book's norm (use tools/formula_metrics.py if useful).
8. **Line fixes.** Exact, minimal, each old string verified with grep to match exactly once in its file:

   ```
   N. `manuscript/chapter-NN.md`
      old: `...`
      new: `...`
   ```
   Use `\n` for a line break inside a fix. Never inside a protected run.
9. **Three cross-movement priorities** for one same-author texture pass in two lanes (ch1–30, ch31–60). Each must be specific enough to brief: what to find, how many, what to do instead, what to leave alone.
10. **Close to source.** Movements 1–4 were drafted before the no-source method and were repaired heavily. Run `bash editions/monroe-1.3/tools/sweep_probe.sh book-06-the-compacts-hand 1 9` (and `SHOW=1` for any chapter at 5% skeleton or more) and, for those movements only, open the source chapters the probe names to judge any passage that still reads as source-shaped: same content in the same order, reworded. Exclude protected text and packet-required beats. List chapter:line, the source file:line, and the kind (varied / split / near-verbatim).

## Write
state/completion/whole-arc-read.md with a verdict and sections 1–10 as above, and your notes file. Nothing else. Be exact: chapter:line for every claim. Where the book holds, say so in a line and move on.
