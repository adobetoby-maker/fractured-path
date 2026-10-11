You are the line-and-listening proofreader for Book 6, "The Compact's Hand", in the Monroe 1.3 edition of The Fractured Path. You sit the independent review seat with fresh context.

This is Step 4 of the book-completion pass and the last check before the text is locked and hash-bound. Later the book will be rendered to audio by a single narrator voice, one segment per paragraph, with each `---` break read as a long pause.

**Do not modify any manuscript file.** Working directory: /Users/drive/fractured-path-monroe13. Run no git commands of any kind, not even read-only ones.

## The models to follow
Read Book 4's and Book 5's proofs first, and match their structure and judgement:
- editions/monroe-1.3/book-04-copper-crown/state/completion/listening-proof.md
- editions/monroe-1.3/book-05-the-silver-standard/state/completion/listening-proof.md

## Read
- In editions/monroe-1.3/book-06-the-compacts-hand/state/completion/:
  - COMPLETION-PLAN.md;
  - whole-arc-read.md (it proposed no line fixes; its one protected-line question was ruled in OWNER-DECISIONS #47);
  - LANE-RULINGS.md (the coordinator's rulings on both lanes);
  - PASS-BRIEF.md;
  - LANE-A-REPORT.md and LANE-B-REPORT.md (the two texture lanes, both applied).
- editions/monroe-1.3/EDITION_BRIEF.md: the audio and Reader Standard sections.
- editions/monroe-1.3/OWNER-DECISIONS.md:
  - #33: Cael = KAYL and Lira = LEER-a are owner-confirmed;
  - #3 and #11: Bede, Maud, Gwen and Abbot are owner-pending placeholders, not findings;
  - #35–#46: no season names, no month order, no English weekday names (Halcenvane weekdays are First-day … Seventh-day); measures in feet and yards; the #38 ratings, the #39 formats and the #41 calendar.
- editions/monroe-1.3/book-06-the-compacts-hand/BOOK_MAP.md §8 (protected lines) and book-06-the-compacts-hand/protected-patterns.txt. Never change a protected line or a FRAGMENT ACQUIRED notice.
- editions/monroe-1.3/audio/fpaudio.py, to see how code blocks and italics are flattened for the narrator.

## Proof every chapter
Proof manuscript/chapter-01.md through chapter-60.md (about 290,000 words) under editions/monroe-1.3/book-06-the-compacts-hand/. Keep running notes in state/completion/listening-notes.md.

Check for these five things.

1. **Quotation marks.**
   - Unbalanced or mismatched quotes, including multi-paragraph speeches.
   - Speech whose speaker a listener cannot tell. Look hardest at:
     - the councils (Cael, Lira, Brom, Karis, Ephram, Daeva, Seln);
     - the counsel's readings of the challenge and the panel and ruling scenes, where quoted instrument text sits inside speech;
     - the Kindling chapters, where the Arbiter, the plate and people all speak;
     - the road chapters past the Line (ch55–60);
     - any two-speaker run where the texture lanes and repairs cut tags.

2. **Ear collisions.**
   - Names that sound alike in one scene: Gault/Gwen; Seln/Selm-; Hesk/Hesk-ward; Velmere/Vell; Ostrand; Karis/Kestrel; Havel/Halvern; Ilsev; Vastin; Withrow; Bracken/Brom; Rooke; Ephram; Umber; Daeva; Zerin; Marek; Ivenne; Hesk; Quenna; Vell; Fiske; Reydan; Auremont; Ternhall; Rhagen; Norhold; Halcenvane.
   - Homographs a narrator could misread: lead, wound, close, read, tear, live, wind (the Wind Path against the wind).
   - Any bare "as" that could be heard as "while".

3. **Formatting the narrator meets.**
   - The FRAGMENT ACQUIRED notice and the first stability warning.
   - Registry forms, gallery sheets and broadsides.
   - Italic Log and notebook entries, Karis's columns, the minute, the charter and notice texts.
   - Numerals and tallies: scores, flags, ratings, figures, T-numbers, day counts.
   - Abbreviations, stray markdown, and `---` spacing (a blank line before and after).

4. **Typos and broken joins** left by the lanes and repairs. The two texture lanes cut about 3,130 words, most of them declared pauses, silences and small gestures, so read every place where a speech now runs straight into the next action. The Lane A author asked for a second ear at ch13:217–219 (Seln's "they write it down" now runs straight to the residence door) and ch18:97 (two declared silences over the post are gone). Read ch60 closely: the coordinator-directed fix that moves Seln's case under the canvas, Seln awake at the fire, and the purse line. Read ch49 around the certification minute (#47). Look for: a mid-clause end, a lower-case start, doubled words, a dangling comparison where a simile was cut, a number changed in one place but not its echo.

5. **Paragraphs over about 700 characters.** List these only.

## Write
Write state/completion/listening-proof.md and your notes file. Nothing else.

listening-proof.md must contain:
- a verdict;
- findings by category;
- exact line fixes, in the format below, each old string verified with grep to match exactly once. Use `\n` for a line break inside a fix.

  ```
  N. `manuscript/chapter-NN.md`
     old: `...`
     new: `...`
  ```
- a pronunciation lexicon table for the Book 6 names and terms, carrying forward the Book 1, 3, 4 and 5 entries for shared names.

Never change a protected line.
