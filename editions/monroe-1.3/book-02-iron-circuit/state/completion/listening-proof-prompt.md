You are the line-and-listening proofreader for Book 2 "Iron Circuit" of the Monroe 1.3 edition of The
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
- editions/monroe-1.3/book-02-iron-circuit/state/completion/COMPLETION-PLAN.md, whole-arc-read.md (§8 fixes are
  already applied), LANE-A-REPORT.md and LANE-B-REPORT.md.
- editions/monroe-1.3/EDITION_BRIEF.md: the audio and Reader Standard sections.
- editions/monroe-1.3/OWNER-DECISIONS.md:
  - #33: Cael = KAYL and Lira = LEER-a are owner-confirmed;
  - #3: Bede and Maud are owner-pending placeholders, not findings;
  - #36: the redirect shoulder is RIGHT; Book 3-side errata are queued, not yours.
- editions/monroe-1.3/book-02-iron-circuit/BOOK_MAP.md §9 and §8 (protected lines). Never change one.
- editions/monroe-1.3/audio/fpaudio.py, to see how code blocks and italics are flattened for the narrator.

## Proof every chapter
Proof manuscript/chapter-01.md through chapter-60.md (about 287,500 words) under
editions/monroe-1.3/book-02-iron-circuit/. Keep running notes in state/completion/listening-notes.md.

Check for:

1. **Quotation marks.**
   - Unbalanced or mismatched quotes, including multi-paragraph speeches.
   - Speech whose speaker a listener cannot tell, especially in the three-person suppers (Cael/Lira/Brom), the
     bouts, the cookshop, and Quenna's approach.

2. **Ear collisions.**
   - Names that sound alike in one scene: Coss/Doss, Darrow/Marrow, Brom/Bede (never in one spoken list),
     Keth/Kestrel, Vell/Dace, Reydan, Ansel, Ulric, Maud, Havel, Feryn, Sarel, Talis.
   - Homographs a narrator could misread (lead, wound, close, read, tear).
   - A bare "as" that could be heard as "while", after the lanes' conversions.

3. **Formatting the narrator meets.**
   - The FRAGMENT ACQUIRED notices and code blocks.
   - `[SHATTERED]` and `[UNBOUND]` in documents: brackets are never voiced. The spoken "Shattered" is plain.
   - Italic Log and binder entries, the grey-book habit-marks, and Carrying entries.
   - Numerals and tallies (knock ratios, "14 knocked / 12 answered", bout scores, the plate numbers).
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
