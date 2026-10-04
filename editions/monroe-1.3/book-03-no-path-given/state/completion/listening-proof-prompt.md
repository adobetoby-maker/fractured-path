You are the line-and-listening proofreader for Book 3 "No Path Given" of the Monroe 1.3 edition of The Fractured Path (Sol, via codex). This is Step 3 of the book-completion pass, the last check before every chapter is rendered to audio by Breeze TTS. Breeze uses a single narrator voice, one segment per paragraph, with `---` breaks read as long pauses.

**Do not modify any manuscript file.** Working directory: /Users/drive/fractured-path-monroe13.

## The model to follow

Book 1's identical proof is the model. Read it first and match its structure and judgement:
editions/monroe-1.3/book-01-the-shattered/state/completion/listening-proof.md

## Read

- editions/monroe-1.3/book-03-no-path-given/state/completion/COMPLETION-PLAN.md and the lane reports in that folder.
- editions/monroe-1.3/EDITION_BRIEF.md: the audio and Reader Standard sections.
- editions/monroe-1.3/OWNER-DECISIONS.md. Note #33 (Cael = KAYL, Lira = LEER-a are owner-confirmed) and #29.
- BOOK_MAP.md §9 (protected lines) and protected-patterns.txt.
- editions/monroe-1.3/audio/fpaudio.py, to see how code blocks and italics are flattened for the narrator.

## Proof every chapter

Proof manuscript/chapter-01.md through chapter-61.md (about 288,000 words) under editions/monroe-1.3/book-03-no-path-given/. Keep running notes in state/completion/listening-notes.md.

Check for:
1. **Quotation marks.**
   - Unbalanced or mismatched quotes. A previous scan found odd straight-quote counts in ch21 and ch59; check whether these are legitimate multi-paragraph speeches.
   - Speech whose speaker a listener cannot tell, especially in the hearing (ch54–59) and the multi-voice suppers.
2. **Ear collisions.**
   - Names that sound alike in one scene: Coss/Doss, Karis/Kestrel, Quenna, Havel/Halvern, Prynn, Wray, Yorlan, Naveth, Oona, Brom, Edran, Hobb, Gerda.
   - Homographs a narrator could misread.
   - "as" read as "while", after the texture pass's conversions.
3. **Formatting the narrator meets.**
   - System notices and code blocks.
   - `[SHATTERED]` in documents (brackets never voiced).
   - Italic Log and binder entries, and the deposition's recorder dashes.
   - Numerals: the registry number 41-7843-V, weeks, bells, box counts.
   - Abbreviations (D1, D6, wk, Cu).
   - Stray markdown, and `---` spacing.
4. **Typos and broken joins** left by the lanes (a mid-clause end, a lower-case start, doubled words).
5. **Paragraphs over about 700 characters.** List these only.

## Write

Write state/completion/listening-proof.md, and your notes file. Nothing else. It should contain:
- a verdict;
- findings by category;
- exact line fixes, in this format, each old string verified with grep to match exactly once:
  N. `manuscript/chapter-NN.md`
     old: `...`
     new: `...`
- a pronunciation lexicon table for the Book 3 names and terms. Carry forward Book 1's entries for shared names.

Never change a protected line.
