You are the line-and-listening proofreader for Book 4 "Copper Crown" of the Monroe 1.3 edition of The
Fractured Path (Claude Fable, review seat, fresh context). This is Step 4 of the book-completion pass, the last
check before the text is locked and hash-bound. Later it is rendered to audio by a single narrator voice, one
segment per paragraph, with `---` breaks read as long pauses.

**Do not modify any manuscript file.** Working directory: /Users/drive/fractured-path-monroe13. Run no git
commands.

## The models to follow
Book 1's and Book 3's proofs. Read both first and match their structure and judgement:
- editions/monroe-1.3/book-01-the-shattered/state/completion/listening-proof.md
- editions/monroe-1.3/book-03-no-path-given/state/completion/listening-proof.md

## Read
- editions/monroe-1.3/book-04-copper-crown/state/completion/COMPLETION-PLAN.md, whole-arc-read.md (§8 fixes are
  already applied), LANE-A-REPORT.md and LANE-B-REPORT.md (texture lanes).
- editions/monroe-1.3/EDITION_BRIEF.md: the audio and Reader Standard sections.
- editions/monroe-1.3/OWNER-DECISIONS.md:
  - #33: Cael = KAYL and Lira = LEER-a are owner-confirmed;
  - #11: Gwen and Abbot are owner-pending placeholders, not findings;
  - #35: no month order and no season names;
  - Halcenvane weekdays are First-day … Seventh-day.
- editions/monroe-1.3/book-04-copper-crown/BOOK_MAP.md §9 and §10 (protected lines) and book-04-copper-crown/protected-patterns.txt. Never change one.
- editions/monroe-1.3/audio/fpaudio.py, to see how code blocks and italics are flattened for the narrator.

## Proof every chapter
Proof manuscript/chapter-01.md through chapter-62.md (about 290,000 words) under
editions/monroe-1.3/book-04-copper-crown/. Keep running notes in state/completion/listening-notes.md.

Check for:

1. **Quotation marks.**
   - Unbalanced or mismatched quotes, including multi-paragraph speeches.
   - Speech whose speaker a listener cannot tell, especially in the three-person suppers (Cael/Lira/Brom), the
     bouts, the cookshop, and Quenna's approach.

2. **Ear collisions.**
   - Names that sound alike in one scene: Gault/Gwen, Fiske/Fisk-, Seln/Selm-, Karis/Kestrel, Havel/Halvern,
     Ilsev, Vastin, Withrow, Bracken/Brom, Rooke, Ephram, Merrick, Tarn, Jask, Jessup, Nyle, Edran, Prynn.
   - Homographs a narrator could misread (lead, wound, close, read, tear).
   - A bare "as" that could be heard as "while", after the lanes' conversions.

3. **Formatting the narrator meets.**
   - The FRAGMENT ACQUIRED notices and code blocks.
   - `[SHATTERED]` in documents: brackets are never voiced. The spoken "Shattered" is plain.
   - Italic Log and grey-notebook entries, Karis's columns, the minute, the charter and notice texts.
   - Numerals and tallies (standings like 6/0, bout scores, trial figures, day counts, d-numbers).
   - Abbreviations, stray markdown, `---` spacing (a blank line before and after).

4. **Typos and broken joins** left by the lanes: a mid-clause end, a lower-case start, doubled words, a dangling
   comparison where a simile was cut.

5. **Paragraphs over about 700 characters.** List these only.

## Write
Write state/completion/listening-proof.md and your notes file. Nothing else.

listening-proof.md must contain:
- a verdict;
- findings by category;
- exact line fixes, in this format, each old string verified with grep to match exactly once (use `\n` for a line
  break inside a fix):
  N. `manuscript/chapter-NN.md`
     old: `...`
     new: `...`
- a pronunciation lexicon table for the Book 2 names and terms, carrying forward Book 1's and Book 3's entries for
  shared names.

Never change a protected line.
