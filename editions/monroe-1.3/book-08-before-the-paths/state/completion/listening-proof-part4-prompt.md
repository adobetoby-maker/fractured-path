You are the line-and-listening proofreader for Book 8, "Before the Paths", in the Monroe 1.3 edition of The Fractured Path. You sit the independent review seat with fresh context.

This is Step 4 of the book-completion pass and the last check before the text is locked and hash-bound. Later the book may be rendered to audio by a single narrator voice, one segment per paragraph, with each `---` break read as a long pause.

**Do not modify any manuscript file.** Working directory: /Users/drive/fractured-path-monroe13. Run no git commands of any kind, not even read-only ones. Do not open anything under books/ or v3-runs/.

## The model to follow
Read Book 7's merged proof first, and match its structure and judgement:
- editions/monroe-1.3/book-07-void-roads/state/completion/listening-proof.md

## Read
- In editions/monroe-1.3/book-08-before-the-paths/state/completion/:
  - COMPLETION-PLAN.md;
  - whole-arc-read.md (PASS; two line fixes applied by the coordinator);
  - PASS-BRIEF.md;
  - LANE-A-REPORT.md and LANE-B-REPORT.md (the two texture lanes, both applied; each lists joins for a second ear);
  - LANE-RULINGS.md (the coordinator's rulings on the lanes, including any cut restored).
- editions/monroe-1.3/EDITION_BRIEF.md: the audio and Reader Standard sections.
- editions/monroe-1.3/OWNER-DECISIONS.md:
  - #33: Cael = KAYL and Lira = LEER-a are owner-confirmed;
  - #35 / #42 / #48: no season names, no month names or order, no English weekday names; feet, yards, miles, paces, strides, cords; "thaw", "first snow", "cold term" are events and stand;
  - #52–#60: protected lines that stand word for word by default and are NOT findings — among them "the whole year"; "my Path worked while everyone's died"; "His Path did not die. It also did not *notice* it should have."; "a machine that lit for everyone but him"; "Tell Lira's family I said so"; the young one is never named (#54); Teague's spear-carrier is a tall MAN (#59); the technician's date is never printed (#60).
- editions/monroe-1.3/book-08-before-the-paths/BOOK_MAP.md §9 (the record passages' limits) and §10 (protected lines), and book-08-before-the-paths/protected-patterns.txt. Never change a protected line, a log entry, an italic acquisition unit (the eleventh, twelfth, thirteenth), the leaf, the chronicle line, a slip, the ledger, the letter or the closing prose.
- editions/monroe-1.3/audio/fpaudio.py, to see how code blocks and italics are flattened for the narrator.

## Proof every chapter
Proof manuscript/chapter-46.md through chapter-60.md ONLY (about 77,000 words; three other proofreaders have the other chapters) under editions/monroe-1.3/book-08-before-the-paths/. Keep running notes in state/completion/listening-notes-part4.md.

Check for these five things.

1. **Quotation marks.**
   - Unbalanced or mismatched quotes, including multi-paragraph speeches; two quotations abutting with no beat between (`." "`), which is a known scar of the repairs.
   - Speech whose speaker a listener cannot tell. Look hardest at:
     - the councils (the six; later the six with Vastin; the two crews at one fire): Lowmarch's bench and back room; the fork-stone; the loft at Treswick; the yard fire (ch40); the grade table (ch45); the blanket (ch52); the shale step (ch53–54); the court's rim (ch58–60);
     - Pike's bench, where he reads lines aloud and people answer;
     - the fights and set pieces, where orders and counts are called: the fence and the ice road (ch2–5); the cut (ch15–16); the alley (ch32–33); the seep (ch48); the Span (ch50); the pass (ch54–55);
     - Oryn at work, where she speaks to a patient, to herself and to the room, and every "May I?" and its answer;
     - Vastin's formal speech, with its clauses and self-corrections, and Cleon's clipped speech with his eyes shut;
     - the unnamed people: the clerk, keepers, carters, the factor, the woman with the net, the watch; and Teague's four (the tall man with the spear; the broad man, whom his crew call the bow; Teague's boy, the young one; the lean old woman) — a listener must always know which unnamed speaker this is, and must be able to tell "the boy" of Teague's crew from Cael, and "the old man" (Vastin) from any other old man;
     - protected lines that stand TAGLESS on their own line (for example "Right." and "It's the first one." in ch58): is each speaker unmistakable from the sentence before?
     - every speech join that the lanes list.

2. **Ear collisions.**
   - Names that sound alike in one scene: Cael / Karis / Cleon; Seln / Stair / Span; Teague / Treswick / Ternhall; Oryn / Ostrand; Lowmarch / Millrace; the Fallow / the Hall; Hesk; Pike; Vastin; Brom; Lira / Line / leaf / lean.
   - Homographs a narrator could misread: lead (the cord's lead weight; to lead), wound, close, read (the read; she read him; he had read), tear, live, wind (the Wind fragment against the wind), bow (the crossbow, "the bow" as a man's name, to bow), row (a row of signs), minute, lean (a lean old woman; the lean of a sign), leaf (the leaf of skin; a leaf of a notebook), flat (the courier's flat; flat ground; a flat hand), bar, mark, set, still.
   - Any bare "as" that could be heard as "while".

3. **Formatting the narrator meets.**
   - The three acquisition units in italics (ch33, ch35, ch50); Cael's logs in italics, above all the repeated "Deployment since the Line: …" line, the inventories, the S22 log (ch57), the ledger and the letter (ch60); a word set roman inside an italic unit; Pike's lines; Hesk's notes; Karis's entries; the leaf read aloud in italics inside quotation marks with her own words between (ch38); the chronicle line with its dashes; the two sealed slips (ch52); bracketed forms ([UNBOUND], [SHATTERED]).
   - Numerals and tallies: days past the Line, marks, lengths, cords, strides, yards, sheet counts (eleven / twenty-nine / twelve; fifty-two; sixty-one), the corner figures (sixty-one, ninety-four, a hundred and thirty-eight, two hundred and six), stake numbers, breath counts, flights of bolts. Arabic numerals in narration are a finding unless they are a visible mark.
   - Abbreviations and initials (K., V., S., C., H.), stray markdown, unbalanced asterisks, and `---` spacing (a blank line before and after).

4. **Typos and broken joins** left by the lanes, the repairs and the audits' line fixes. Every movement took exact line fixes that restored protected units inside the author's prose, and the author then wrote the joins: read each restored unit's lead-in and follow-on. The two texture lanes thinned role epithets, "He found that", silence tags, similes and ledger diction: read every place where a sentence now ends sooner, an epithet became a name or a pronoun, or a speech runs straight on. Look for: a mid-clause end, a lower-case start, doubled words, a pronoun whose noun was cut, a dangling comparison, a name used where the viewpoint cannot know it (Teague's and his crew's passages), a number changed in one place but not its echo (the deployment count runs twenty-seven → twenty-eight → twenty-nine → thirty → thirty-two → thirty-three → thirty-four → thirty-five; the purse 96 → 76 → 116 → 118 → 138 → 136 → 134 → 130 → 128 → 127 → 123).

5. **Paragraphs over about 700 characters.** List these only.

## Write
Write state/completion/listening-proof-part4.md and your notes file. Nothing else.

listening-proof-part4.md must contain:
- a verdict;
- findings by category;
- exact line fixes, in the format below, each old string verified with grep to match exactly once. Use `\n` for a line break inside a fix.

  ```
  N. `manuscript/chapter-NN.md`
     old: `...`
     new: `...`
  ```
- a pronunciation lexicon table for the names and terms that occur in your range, carrying forward the earlier books' entries for shared names.
- In every proposed line fix, do not introduce a run of eight or more words that also stands in the source (the overlap gate is run after fixes are applied). Mark each fix REQUIRED (a listener or a narrator will stumble) or OPTIONAL.

Never change a protected line.

## COVERAGE — binding (a previous run of such a proof was rejected because it did not read the text)
- Your range is chapters 46–60. Read EVERY chapter in your range in full, in order, by printing the whole file (for example `cat -n` on one chapter at a time). Scripts and greps may SUPPLEMENT the reading (quote balance, paragraph lengths, numerals); they never replace it. Do not sample, skim or summarise from reports.
- As evidence of reading, your notes file must give, for every chapter: the chapter's title; the number of scenes; and for EVERY scene the first six words and the last six words exactly as they stand, followed by your listening notes for that scene (speaker attribution, joins, numerals, anything a narrator would stumble on) or the single word "clean".
- For restored protected units and lane joins that fall in your range, quote the sentence before and the sentence after each, and rule the join sound or give a fix.
- If you run short of room, STOP and say exactly which chapters you did not read. Never claim a chapter you did not read in full.
