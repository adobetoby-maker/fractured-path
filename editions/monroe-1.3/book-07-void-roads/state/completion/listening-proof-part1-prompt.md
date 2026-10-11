You are the line-and-listening proofreader for Book 7, "Void Roads", in the Monroe 1.3 edition of The Fractured Path. You sit the independent review seat with fresh context.

This is Step 4 of the book-completion pass and the last check before the text is locked and hash-bound. Later the book will be rendered to audio by a single narrator voice, one segment per paragraph, with each `---` break read as a long pause.

**Do not modify any manuscript file.** Working directory: /Users/drive/fractured-path-monroe13. Run no git commands of any kind, not even read-only ones.

## The models to follow
Read Book 5's and Book 6's proofs first, and match their structure and judgement:
- editions/monroe-1.3/book-05-the-silver-standard/state/completion/listening-proof.md
- editions/monroe-1.3/book-06-the-compacts-hand/state/completion/listening-proof.md

## Read
- In editions/monroe-1.3/book-07-void-roads/state/completion/:
  - COMPLETION-PLAN.md;
  - whole-arc-read.md (PASS — RATIFY; it proposed no line fixes);
  - PASS-BRIEF.md;
  - LANE-A-REPORT.md and LANE-B-REPORT.md (the two texture lanes, both applied; each lists joins for a second ear);
  - LANE-RULINGS.md (the coordinator's rulings, including two cuts restored in ch55 and ch56).
- editions/monroe-1.3/EDITION_BRIEF.md: the audio and Reader Standard sections.
- editions/monroe-1.3/OWNER-DECISIONS.md:
  - #33: Cael = KAYL and Lira = LEER-a are owner-confirmed;
  - #42, #48: no season names, no month names or order, no English weekday names; feet, yards, paces, cords; generic "season" and "month" are allowed;
  - #49, #50, #51: three sets of protected lines stand word for word by default ("mine" / "Path" in Cael's quiet-ground log entries; "Six years I've wanted a face"; "Tomorrow makes three"). They are not findings.
- editions/monroe-1.3/book-07-void-roads/BOOK_MAP.md §10 (protected lines) and book-07-void-roads/protected-patterns.txt. Never change a protected line, a log entry, the FRAGMENT ACQUIRED notice, the inventory or the closing.
- editions/monroe-1.3/audio/fpaudio.py, to see how code blocks and italics are flattened for the narrator.

## Proof every chapter
Proof manuscript/chapter-01.md through chapter-15.md ONLY (about 76,000 words; three other proofreaders have the other chapters) under editions/monroe-1.3/book-07-void-roads/. Keep running notes in state/completion/listening-notes-part1.md.

Check for these five things.

1. **Quotation marks.**
   - Unbalanced or mismatched quotes, including multi-paragraph speeches.
   - Speech whose speaker a listener cannot tell. Look hardest at:
     - the councils of five or six (Cael, Lira, Brom, Karis, Seln, Oryn), above all the loft (ch36) and the contract council (ch46);
     - the board at Lowmarch, where Pike reads lines aloud and people answer from the meadow;
     - the fights (the ford ch10–11; the Ring ch31–32; the trap ch49–51; the Hall ch54), where orders are called;
     - Oryn at work, where she speaks to a patient, to herself and to the room;
     - the unnamed people (the steading's woman, the bowman, the carter and his wife, the ford-keeper, the six on the rim, Teague's crew): a listener must always know which unnamed speaker this is;
     - the twelve speech joins Lane B lists where a stage beat was removed between two halves of one speech, and Lane A's eleven joins.

2. **Ear collisions.**
   - Names that sound alike in one scene: Oryn / Ostrand / Oxhollow; Karis / Cael; Seln / Selm-; Teague; Pike; Lowmarch / Millrace; Thornwater; the Fallow / the Hall; Hesk; Vell; Ephram; Brom / the bowman; Lira / Line.
   - Homographs a narrator could misread: lead, wound, close, read (the Iron read; she read him; he had read), tear, live, wind (the Wind Path against the wind), bow (the crossbow against to bow), row, minute.
   - Any bare "as" that could be heard as "while".

3. **Formatting the narrator meets.**
   - The FRAGMENT ACQUIRED notice (ch37) and any bracketed in-world form ([UNBOUND], ch42).
   - Cael's log entries in italics, above all the repeated "Deployment since the Line: …" line and the night logs that list uses and bills; Pike's ledger lines and slips (all-caps HOLD); Karis's leaves, tallies and sheet numbers; letters (Hesk, Vell, Ephram, Oryn); the covenant leaf.
   - Numerals and tallies: days past the Line, marks, lines on the wall, paces, yards and cords, stake numbers, sheet counts, counts in a fight. Arabic numerals in narration are a finding unless they are a visible mark.
   - Abbreviations, stray markdown, and `---` spacing (a blank line before and after).

4. **Typos and broken joins** left by the lanes, the repairs and the audits' line fixes. The two texture lanes cut about 2,800 words, mostly retrospective glosses ("That was…", "as he had…"), counted pauses and generic stage business, so read every place where a sentence now ends sooner or a speech runs straight on. Every movement also took exact line fixes from Sol's audits that restored protected units inside the author's prose: read each restored unit's lead-in and follow-on (ch13 the gate; ch20 "Cold"; ch25 Pike to the book; ch29 Lira's clock; ch31, ch34 and ch37 Oryn; ch38 "the colour of the wall"; ch44 "North in the morning"; ch45–49 and ch52; ch54 "Walls"; ch55 "Twice"; ch58 the fork). Read ch47–48 closely (the boy's wrist refused; "May I read you?" granted) and ch58 (the fourth site approached and not touched). Look for: a mid-clause end, a lower-case start, doubled words, a pronoun whose noun was cut, a dangling comparison, a number changed in one place but not its echo (the deployment count runs none → one → thirteen → twenty-three → twenty-seven).

5. **Paragraphs over about 700 characters.** List these only.

## Write
Write state/completion/listening-proof-part1.md and your notes file. Nothing else.

listening-proof-part1.md must contain:
- a verdict;
- findings by category;
- exact line fixes, in the format below, each old string verified with grep to match exactly once. Use `\n` for a line break inside a fix.

  ```
  N. `manuscript/chapter-NN.md`
     old: `...`
     new: `...`
  ```
- a pronunciation lexicon table for the Book 7 names and terms (Oryn, Teague, Pike, Lowmarch, Thornwater, Oxhollow, Millrace, the Fallow, stillhound, shale-back, the Quieting, and the rest), carrying forward the earlier books' entries for shared names.
- In every proposed line fix, do not introduce a run of eight or more words that also stands in the source (the overlap gate is run after fixes are applied).

Never change a protected line.

## COVERAGE — binding (a previous run of this proof was rejected because it did not read the text)
- Your range is chapters 1–15. Read EVERY chapter in your range in full, in order, by printing the whole file (for example `cat -n` on one chapter at a time). Scripts and greps may SUPPLEMENT the reading (quote balance, paragraph lengths, numerals); they never replace it. Do not sample, skim or summarise from reports.
- As evidence of reading, your notes file must give, for every chapter: the chapter's title; the number of scenes; and for EVERY scene the first six words and the last six words exactly as they stand, followed by your listening notes for that scene (speaker attribution, joins, numerals, anything a narrator would stumble on) or the single word "clean".
- For restored protected units and lane joins that fall in your range (listed in the prompt above and in LANE-A-REPORT.md / LANE-B-REPORT.md), quote the sentence before and the sentence after each, and rule the join sound or give a fix.
- The pronunciation lexicon in your part lists only names and terms that occur in your range.
- If you run short of room, STOP and say exactly which chapters you did not read. Never claim a chapter you did not read in full.
