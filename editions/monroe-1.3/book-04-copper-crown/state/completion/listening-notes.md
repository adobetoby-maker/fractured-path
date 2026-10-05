# Book 4 — listening proof, running notes (Claude Fable, review seat, fresh context, 2026-10-05)

Read order: prompt → Book 1, Book 3 and Book 2 listening-proof.md (models; Book 2's listening-notes.md as the model for
this file) → COMPLETION-PLAN, whole-arc-read (§8 applied), LANE-A-REPORT, LANE-B-REPORT → EDITION_BRIEF (audio, Reader
Standard) → OWNER-DECISIONS #11, #33, #35 (+ #7–#10, #37) → BOOK_MAP §9, §10 (+ §11, §13) → protected-patterns.txt →
audio/fpaudio.py → mechanical sweep (script, scratchpad) → chapters 1–62 in order. The prompt's lexicon line says
"Book 2 names and terms"; read as Book 4 (a copy-over from the Book 2 prompt), carrying B1/B2/B3 entries forward.

## Mechanical sweep (script over all 62 files, before the read)
- 62 files, 290,068 words by `wc`. 256 `---` breaks, every one with a blank line before and after. No setext accidents.
- `*` count per paragraph: 0 odd. No `_`, no `**`, no backticks outside the one fence, no headings after line 1, no
  tabs, no trailing spaces, no curly quotes.
- `"` count per paragraph: 12 odd — ch55 ×4 (Gault reads his evaluation note, multi-paragraph), ch56 ×3 (lines 69, 85,
  285), ch61 ×5 (lines 183–197, Withrow's address). All to be checked in place as multi-paragraph speech (open,
  reopen, close).
- Code fences: 1 (ch34 FRAGMENT ACQUIRED, Shadow-adjacent; protected §10). fpaudio flattens each line + ".".
- Brackets: `[SHATTERED]` ch2 line 33 (document: the station's gate list, "the designation in brackets, [SHATTERED],
  as the station had written"); `[unnamed]` in the ch34 notice. No other brackets in the book.
- Lower-case paragraph start: 1 — ch58 line 65 "unmarked file. one of three. probably the third." (Seln's cipher page;
  protected pattern). Deliberate.
- Paragraphs with no terminal punctuation: 9, all end in a colon introducing a Log line, a note or a sign (ch5, 15, 28,
  38, 40, 41, 46 ×2, 49). Fine.
- Doubled words: 7 "had had" (ch18, 23, 33, 42, 49, 59 ×2). All grammatical. No true doubles; no ", ," ".." or
  double-space artefacts anywhere.
- Slashes between words: 1 — ch25 line 79 "*Lira — Wind — Copper 2 — 6/0.*" (the standings board). Candidate fix.
- d-numbers (d144 etc.): none in the manuscript.
- Numerals: "41-7843-V" (ch2, registry number, lexicon); the glance/fame tally in ch15 ("29 of 91", "0 of 7", "9 of 14",
  "5 of 11", "7 of 19", "0 of 31"); ch19 Log "Sixth-day the 80th"; ch22 "shelf-marks 40–60"; ch25 "Copper 2 — 6/0";
  ch36 "a large, plain 0"; ch38 "a large 41"; ch39 "41 pages — tabbed — DO NOT RE-SORT"; ch42 "4 of 4", "311"; ch49
  "Priority Level 4"; the numbered Log lists ch49 (1.–5.), ch50 (1.–4.), ch53 (5.). Check "0" (B1 precedent: nought),
  "80th", "40–60", "6/0" in place.
- Abbreviations: none of Cu/Br/R1/wk/exch/unr/def/opp/equiv/Fri anywhere. Initials only: K. (Karis's notes), L./F.
  (Karis's minute of the Fiske bouts, ch29, ch42), C. (ch23 minute), K.D. (ch34), H. (Hesk ch37), W. (ch48 note),
  B. (ch55 note). Letter-names.
- All-caps (20): [SHATTERED] ch2; COPPER ch6 (porter writes); KILLED, NO SIGNAL ch15; THE CORE MUST BE FREE… ch27
  (protected plate); READ FIRST ch31/ch34; FIELD ASSESSMENT ch32; READ THE NOTICE, CARRY THE LADDER ch35 (Gwen);
  AIMED / NOT ch36; DO NOT RE-SORT ch39; GROWTH / CONTROL / FIVE ch43 (Karis's columns); ON THE NUMBER ch53 ×2, ch54.
  All written signs; renderer sentence case, as B1/B2.
- Spaced em dashes: 17 — inside documents, notes, letters, the notice, the board line, and three protected spoken lines
  (ch7 Withrow, ch29 Fiske, ch56 Vastin). All pauses.
- Name pairs per scene (script): Gault/Gwen together in ch32 s4, ch38 s5, ch58 s3, ch59 s1 (check); Fisk-/Selm-/
  Kestrel/Halvern/Wren absent; Bracken/Brom share 37 scenes (BRACK-en vs BROM; check spoken lists); Havel/Cael 21
  scenes (HAV-el vs KAYL); Jask/Jessup never together (Jessup once, ch35); Merrick/Tarn ch22, 24, 26; Edran/Ephram
  ch14 s2 only; Vell/Velmere never; Wray/Greyvane ch3, 4, 8, 10, 20.
- Homographs (contexts pulled): lead = LEED in every fighting use (lead arm/hand/foot/shoulder/leg/thigh: ch3 ×13, ch9,
  ch19, ch21 ×2, ch24, ch51 ×3, ch52) and as the verb (ch36 "turned to lead the others", ch49 "don't lead to the same
  place"); LED the metal: ch7 "the cost of lead", ch17 "the lead of the window-pane" ×3, ch34 "the lead between the
  panes". wound = WOWND in 11 of 12 (wraps, cords, the gauge, the roll, the bandage, the drum, the scarf); ch51 "a
  fight out of the other one's wound" = WOOND. bow: ch28 "a flat bow" (tape) = BOH; ch36 "a little bow", ch44 "did
  not bow", ch52 "not to bow" = BAU; ch3 "bowed to the table" = BAUD. live = LYV: ch6 "a live thing", "kept live";
  ch27 "a live hazard", "anything live"; ch30 "a live delivery", "A live situation"; ch49 "remains live" (protected
  return); ch60 "stayed live"; LIV elsewhere. lives = LIVZ ch1, ch27, ch57; LYVZ ch13, ch43, ch48. tear ch20 = TAIR
  (the lining); tears ch29 = TEERS. present = PREZ-ent (gift) ch37, ch53; pre-ZENT (verb) ch12 "will present himself";
  adjective elsewhere. refuse: all verb. row: all ROH. wind: the Path and the weather only; no "wind up".
  minute (121): all time-uses. record/records: nouns and verbs clear in context (ch52 "I will record" verb).
- ", as" clauses: 345 listed (ctx.json); read below.
- Paragraphs over 700 flattened chars: 114 (list in the proof).

## Chapter notes
- ch1: clean. Brom's pocket book "*Week three. K. found a word.*" = the letter K. The four-person supper (Karis/Lira/Brom/Cael)
  is tagged line by line. "as steady as a clock" manner. Fix 1–3 lines ("the last week of the winter term", "the months
  since", "three years") sit clean. "Hesk-ward" two words. Fine.
- ch2: "*[SHATTERED]*" inside an italic document, with the narration saying "in brackets" — brackets never voiced, the
  word plain. "41-7843-V" written "digit by digit" (lexicon: four-one, seven-eight-four-three, V). "*K. Dellenmoor*"
  = the letter. "Copper, Rank Two" in words. Supper (four tracks) all tagged. "He assumed," said Cael. Fine.
- ch3: the Edran bout. Wray's calls ("Touch. Edran. One." / "Time. Even." / "Touch. Cael. Exchange and bout, four to
  three.") are flat and clear; the second "Understood, Instructor." untagged = Cael by alternation. "lead arm / lead
  hand / lead shell" = LEED throughout (13 uses). "He bowed to the table" = BAUD. "Third one someday." protected, exact;
  "Someday," said Cael. Lira "as if she were testing whether it was attached" (first instance, kept by lane A). The
  Log entry in italics (six paragraphs) reads as one document. Fine.
- ch4: "Told you it would be soon." exact. Naveth's notice in narration (not italic). Wray's farewell. Prynn's "The shelf
  gap is still there. It'll be there when you're forty." exact. The road log "*Day one. Two. …*" — count cadence; "the
  near hind" fine. "Liar," said Karis. Karis/Brom/Cael in the inn room tagged. Fine.
- ch5: the toll board in italics (list cadence). "the Ost" (OST), Ostrand (OST-rand), Halcenvane (HAL-sen-vayn), "Weighbridge
  Street". The gate clerk reads the four names flat. Bracken (BRACK-en) first met: the enrollment record (§10) exact, three
  italic lines; "It's the first one that's true." exact; "*Ninety-four minutes.*" in words. "Carrel eleven" / "Is eleven a
  good number?" The wall: four, tagged. Log "*Enrolled.* / *Second time the word's been used about me. First time it's
  been accurate.*" … "*I intend to be worth the sentence.*" … "*I'd have paid more.*" exact. Fine.
- ch6: the porter (unnamed) and his shorthand lines in italics; "two hundred and nine", "four hundred and twelve" in words;
  "*COPPER*" written on the board (sentence case at render). Fix 7–8 (oak on bearers) clean. "the gaze stops seeing and
  starts supplying" — Log. Every scene two-person. Fine.
- ch7: the hatch woman (tagged). The eleven rumours (Log). The open session: Rooke's "The provision may be sound…" and
  Withrow's "Minuted." exact. **FIX** — the pinned minute Cael reads: "*Instr. Rooke: the provision may be sound; …*" —
  "Instr." is an abbreviation an engine voices as "instr" or spells; "Instructor Rooke" is the form two paragraphs above.
  → "*Instructor Rooke: …*". "the cost of lead" = LED. Withrow's protected speech ("I read the hearing transcript four
  times…") exact, spaced dash = pause. "Count on both." The assessment notice (italic). The wall at dusk: four, tagged.
  Fine otherwise.
- ch8: Rooke (ROOK, as "book") first on the floor; "Again." / "Enough." Ephram (EF-ram) introduced; "Blade. Iron Rank Six."
  Brom's "I found the wall. It has students." exact; Rooke's wrap text read aloud "in Rooke's flat rhythm" (italics inside
  quotes: a voice reading) exact. "He wound the wrap back on" = WOWND. "I'm *delighted*." Common room: the four plus two
  Iron girls arguing; tagged. Fix 10–11 ("two years") clean. "That night the binder got it plainly." (lane A frame). Fine.
- ch9: Lira reads the list from memory ("Third on the list…"); the clerk's seeding speech; "Sixty-four. And me." The practice
  bout: the instructor's calls ("Touch. Stone. One." / "Wind. Bout, three to one."). The register line "*Lira, Wind, Copper
  Two (transfer), over* — the fourth-year's name — *Stone, Copper Six. Three to one. Practice.*": the dashes bracket an
  authorial aside inside a read document; direct the aside in the narrator's own colour (fpaudio strips the italics, so the
  colour is the only cue). Fiske (FISK) introduced, "a dozen minutes" (lane A). "You're the transfer with the flag." /
  "And you've held it two years." Wash-house: four, tagged; "said Brom, humbly". Fine.
- ch10: the office's half-sheet (italic); "*Present everywhere. Eligible nowhere.*" Fix 14–16 ("every name", "a book of
  names") clean. The Ardenmere terms with Lira: "Stop." and the count "Twenty-eight… Thirty." The Ash instructor (unnamed;
  "the fourth name on Cael's standing list"). "Eleven supervisors, eleven crossovers" (canon). Karis's three terms; "I'm
  eight and nil." Fine.
- ch11: the Lattice instructor (unnamed): "Magistra" (MAJ-iss-tra) / "I don't take the title"; the pupil's count "One, and
  set. Two, and set. Draw. Three, and set." (keep the count rhythm). The porter's "lad". "the instrument he had trusted for
  two years" (fix 17) clean; "half the Paths this hill teaches" (lane A) clean; the season words gone. Brom "wound the
  wrap back up" = WOWND. Wall at dusk: four, tagged; "Four of us, four doors, all real…" exact. Fine.
- ch12: Karis reads the standing rule (italic). The common-room doctrine talk: four, tagged ("Two," said Karis / "Three,"
  said Brom). Fix 23–24 ("Four days." / "If I'd said it then…") clean. Lira's Fenmark: "Copper" / "Rank One" in words;
  "Somebody in this family". Attribution note (not a fix): line 137 "So make him look." opens a new paragraph straight
  after Lira's own paragraph (135); alternation suggests Cael for three words until "She turned her head" resolves it —
  Lira is the only "she" present; keep Lira's colour across both segments. "Count the half-second." Gault (GAWLT),
  "Magister" (MAJ-iss-ter); the apparatus; "Three rules of this room" (Gault's voice, flat). "Understood, Magister." Fine.
- ch13: the baseline. Gault's instructions and the clerk's readings ("Three brass left of the crossing. One forward.
  Interval—" and a number: the cut-off dash closes inside the quote, then narration). "Eleven of twelve" in words.
  "Held, low." Gault's note read aloud (quoted, four sentences) exact; "I don't need to know what you are, Enrollee…"
  exact. Fix 25 ("before term") clean. Seln glimpsed as "a man carrying a stack of forms" (unnamed here). Fine.
- ch14: the board slip (italic, nine words). Ephram's "Greyvane needed him to be real. We don't. I'll wait for the semester
  evaluation." exact; Log "*Fair. Same terms I'd offer.*" exact. POV: Seln from s3 (the windowless room) to s4 (the
  posting-house, the bluff walk) — mark the `---`; "The Compact does not know what he is." / "No," said Seln exact; the
  brief in italics exact. Fix 26–28 (four hands, the round clerk's script) clean; "He was thirty-eight". The sum
  "Seventy—" / "Seventy-two." / "Seventy-six," (three voices, tagged). The residence card "*Seln. Shadow. Bronze.*"; Log
  "*New TA in Gault's office…*" exact — "TA" = the two letters (ch15 decodes it: "A teaching assistant carried paper").
  Seln = SELN (one syllable, as "kiln" with an s). Fine.
- ch15: the fame tally. **FIX** — the binder lines "*TA, assessment office: 0 of 7.*" and "*TA: 0 of 31.*" carry the
  figure 0, which an engine says as "zero"; the book's own word is "nought" (ch36 ×2; B1's fix 10–11 is the precedent)
  → "nought of seven", "nought of thirty-one". The other tally lines (29 of 91; 9 of 14; 5 of 11; 7 of 19) read as
  numbers naturally. **FIX** — the three shorthand lines (ll. 113–117) are joined with middle dots: "*Day sixty-one ·
  second bell · hall three gallery · west end by the turned post · all floor, both doors.*" etc. "·" has no spoken form
  and fpaudio does not strip it; an engine may say "dot" or spell nothing. → spaced em dashes, the book's own shorthand
  separator (ch25's board line). "*KILLED, NO SIGNAL*" caps (sentence case). Lane A's one-sentence maps read clean; the
  fifth map; "Where would I stand?"; the floor trade. Brom "wound a wrap" = WOWND. "as if it owed you money" (first,
  kept). Fine otherwise.
- ch16: the empty east hall; "*He needs a crowd.*" exact. The Shield man ("Again," over his letter). The Power Log entry
  (late read). The lamp; the porter's "Fourth-day" (house weekday); "two for a copper". "*Nobody avoids me that
  consistently by accident. Avoidance at that precision is aim.*" exact. Havel named in Lira's and Cael's talk (HAV-el;
  with Cael KAYL in the same scene, different onsets). "as polite as shopkeepers" (first, kept). Fine.
- ch17: the council (four, door locked; every line tagged or answered). "the lead of the window-pane" ×3 = LED. Brom's "We
  know where their eyes are. First time ever. Why would we give that back?" exact; Lira's "It's not settled, it's
  *outvoted*." exact; Log "*Shadow Path, Bronze, fifteen years' craft if he's a day…*" exact. The stair (Karis, then
  Lira, then Brom "I'll go round, then") tagged. The numbered plan "*One. … Four.*" Fine.
- ch18: POV Seln s1–s2 (the bridge, the courier, the product; the dark east hall) — mark the `---` into Cael's s3. The
  first product (italic) exact, "in the fourth hand". Seln's closing thought "Fifteen years say the file's question is
  the wrong question…" (unitalicised narration, protected) exact. Attribution note, OPTIONAL fix: line 113 `"So I've
  looked for his. Nineteen days. Through glass, in the lamp…"` opens a new paragraph straight after Cael's own `"No. He
  doesn't."`; alternation hands it to Karis for a sentence before the content ("I've looked… while I write down other
  people's bouts") and the closing "He shook his head" return it to Cael. A two-word tag would settle it. "the only
  lit window in a dark street" (Seln's deliberate echo of ch16). The rail count; "*spoiled: Fiske*"; the "*Discarded /
  cannot reach*" column (the slash is inside an italic heading: direct as "discarded, cannot reach"). Fine.
- ch19: the Current lecturer hums (unnamed). Brom "walked into the wall" (the rule under the rule). The two falls;
  Lira's calls "*left*, *round*, *low*" / "*late*, *late*, *on time*, *late*" (count cadence). "Ice for the ribs."
  The floor issue: Log "*Floor issue, Sixth-day the 80th: hall one for hall three…*" — "80th" is the book's only
  ordinal numeral; narration two lines above says "the eightieth"; an engine says "eightieth" — OPTIONAL "the
  eightieth". "*He fixed it. Sixth-day, hall three. Nobody asked him to.* / *We're playing now…*" exact. Fine.
- ch20: the brackets ("Copper ran to ninety-one names", "sixty-three", "nineteen" in words); Lira's seed line
  "*Twenty-two. Lira. Wind. Copper Rank Two. Transfer.*" Nyle (NYLE, as "mile") — "a dozen wins across two seasons"
  (lane A). The table's calls "Touch. Wind. One." … "Wind. Three. Bout." Eleven seconds (canon). Merrick (MERR-ik):
  "Touch. Iron Skin. One." / "Shield. One each." Rooke's "Again. Slower. Watch yourself." exact. "a tear in the
  lining" = TAIR. "*ugly, expensive, intelligent.*" Fine.
- ch21: the first-year in the Current smock (unnamed); "Touch, Blade," from the table. The twenty-three shut out (sum in
  words). Bracken's "evidence… admissible… not a verdict" (his voice). Ephram's rail; "*I had that wrong on Fourth-day;
  here's why*" (reported speech, italic). The season inventory (five italic lines, "No change in any of the five") and
  the "*Season's open…*" entry exact. The door cards in italics ("*Seln. Shadow. Bronze.*"). The Architect thought
  ("Somebody built these instruments… That was a decision.") stays unwritten, as mapped. Fine.
- ch22: Karis's notes under the door: "*Prynn's index, shelf-marks 40–60: two wrong.*" — the en dash between numerals;
  a human says "forty to sixty", an engine may say "forty sixty" — OPTIONAL "40 to 60". "*L.: "You want it." C.:
  "Yes."*" = the letters. Tarn (TARN) first named; Merrick. "Four bouts and none lost". Karis's finding "The conditions
  are met. If you directed it, I believe it would complete." / "Which is why we have to talk about whether you may."
  exact. "*Whether.*" Fine.
- ch23: the minute lines ("*L. states the enemy position…*", "*Minuted. One: … six methods named by C. …*",
  "*Researcher notes: …*") — the letters; the rule-two wording matches ch34 (lane B). Brom's "That's not a
  demonstration you're stealing. That's a weapon you're learning." exact. The six refused methods read as a list ("One.
  … Six."). The bags "*light*, *middle*, *heavy*"; "the full run" (lane A, no count). "like a hammer into a bell"
  (first, kept). Fine.
- ch24: Log "*Last year's me was afraid of not-knowing…*" exact; Karis's "An instrument doesn't change sides. It changes
  readings." exact (quoted inside an italic Log line). Rooke: "Tarn." / "Stop." / "Again. From the fourth. Slower.
  Everybody watch his left heel." Abbot (AB-ut; placeholder #11) named once with Path and rank, "the Mire boy" after;
  "Touch. Mire. One." The Iron girls' whispered "*watch her feet, just watch*" (italic reported speech). "low off her
  lead foot" = LEED; Brom "wound his wraps back on" = WOWND. "Stopped counting…" Log. Fine.
- ch25: the post ("*left*, *nothing*, *low*, *round*"; "Twelve on time"); "Three's a structure." POV: Lira s2 (the board
  at the fifth bell) — mark the `---` both sides. **FIX** — the chalked standings line "*Lira — Wind — Copper 2 — 6/0.*"
  is the book's one slash between words; an engine says "six slash zero". The chapter is titled "Six and Nothing" and
  the next sentence glosses "Six and nothing: six bouts unbeaten, none lost" → "6–0" (en dash: "six, nought/zero", a
  score; B1's slash fixes are the precedent). "Huh," said Lira. The Shield fifth-year (unnamed; forty-one wins):
  "Touch. Wind. One." in about eight seconds; the hip on the north stair; Brom in the archway. Bracken's top-line
  half-sheet (italic foot-note). "Fifteenth," on the stone. Fine otherwise.
- ch26: Tarn bout: "Blade. Position. Three to two. Bout." Rooke: "A tired man doesn't do what he's decided… He does the
  thing he practised the longest." exact. "Nineteen of them. Four a week." "thirteen feeds" (lane A's sum). Brom's
  clean swearing ("a great many kettles"). Karis ticks "Number one" … "Number four". The Current fourth-year
  (unnamed): "Wind. One." … "Current. One. Two to one." Fine.
- ch27: the plate "THE CORE MUST BE FREE BEFORE DECLARATION. CHECK THE PIN." (protected; capitals, unitalicised;
  sentence case at render, flat). Jask (JASK, as "mask") introduced with Path and rank. "What," he said (no question).
  The warden's word "one Cael had never once heard from staff" — not rendered. Rooke: "You went toward it." / "Most
  people go away from a thing like that." "a dozen paces" (lane A). The Log's "*…next to the word* undisclosed." —
  reverse emphasis inside an italic entry; parity even; fpaudio strips it. Fine.
- ch28: POV Seln s1–s3 (the four hands — fix 26–28/lane A confirmed: round / cramped / sloping / upright plain), the
  auditor at twenty-two, the walk down — mark the `---` into Cael's s4. The exception report (italic) with "*Response
  consistent with documented baseline.*" exact; "seven times in fifteen years" (lane A). "He filed the report. Then he
  sat for a while with the file drawer open, not filing anything else." exact. The duty clerk's entry (italic, four
  lines; "Hall three, north bay, sixth bell."). The incident report (italic) exact; "in eleven words" (canon). Brom's
  room: three, tagged. "polite as shopkeepers" stands here as well as ch16 (lane A cut ch30's; two remain — ledger
  note, no audio effect). "Fifteenth," said Fiske. / "Fifteenth," said Lira. "Twelve." Silver (lane A). Fine.
- ch29: Karis's four minute-lines in italics with initials ("*One. L. spends nothing. Why?*", "*Two. F. closes the doors.
  F. one.*", "*Four. F. stops placing. L. walks in. L. two to one.*") = the letters, flat. "Even," the instructor; "Force.
  One." / "Wind. One each." / "Wind. Two to one. Bout." "nine movements", "a dozen heartbeats" (lane A). Fiske's four
  protected lines and "Six weeks. I'll see you in the final." exact; Lira's recitation is narrated, not repeated. Karis
  "with tears running down her face" = TEERS. "like wind through standing corn" = the weather. Fine.
- ch30: POV Seln s1 (the bluff road; the cipher page; the small case; the four carbons) — mark the `---`. "a fifth thing,
  a private shorthand grown out of the cramped hand" (lane confirmed). The cipher lines ("*Range: six feet.* / *Interval:
  shorter than the return.* / *Heading: in.*") and "*Nobody builds that at fifteen unless somebody has been coming for
  him since his Kindling.*" exact (#9). The three carbons (italic) with "*No undisclosed capability observed.*" Cael s2:
  "Two and two, on the bell." Fix 32–33 and lane A's "By Third-day" clean; "Three days on the top line". The counter:
  "Third line. The clerk countersigns." (Seln, untagged, then "He signed"); "Your file says you watch things well. The
  course would tell us if the file's right." / "Sign me up." exact. "Something in my head." / "Leave it in your head on
  my floor." Fine.
- ch31: the locked common room (four; every line tagged or answered; Lira argues both sides). Brom: "If he wanted you,
  he'd have left you an easy way to refuse. He's left you a hard way to accept." Karis's four roads (numbered). The
  signed sheet (italic, four parts; "— deferral, unit, the lot —" pauses) and "*Tolerable: …*". The Log "*He watched me
  stop Iron-tier force with a Copper baseline…*" exact; "*Careful* for *me.*" (reverse emphasis, parity even); "*READ
  FIRST*" in pencil capitals. The board sheet in "the wing's round copying hand" (italic); "*Gwen — Second Year —
  Current*" and the eye. Karis's measurements ("which was eleven" — the middle bag). Fine.
- ch32: the fire-watch boy ("perhaps ten"; his fours); slate lines in italics ("*Records hall, fourth hour.*"). Karis's
  drawers; "not a dozen provision files" (lane B). The unit: Gwen (GWEN) — "You're the assay one," / "I'm Gwen.
  Current."; Seln's entrance ("No," said Cael. / "No," agreed Seln, from the doorway — two "No"s, both tagged). The
  slate "*Observe. Position. Presence.*" and "*A position is an argument about where attention will go.*" exact;
  "*FIELD ASSESSMENT*" in Gwen's capitals. Gault/Gwen in one scene (s4): Gault is only named in Seln's speech ("Gault
  approves the syllabus… He will not come."), Gwen speaks — GAWLT / GWEN, different vowels and shapes; fine by ear.
  "*Priced. Going anyway.*" Brom's coat; Lira's "put your hand up, once". Fine.
- ch33: night one on the gallery; the fire-watch (two men and the boy, unnamed); "*Records hall, last bell.*" "I saw
  two men see nothing." Gwen at the library desk ("You chose second-best on purpose, didn't you."). Night two on the
  stair; the scuff; "*Researcher's note. Two nights…*" and "*K. would like to say…*" (the letter). Brom: "I'm not
  marrying him" / "But I'd lend him my coat." Fine.
- ch34: rule two read aloud (italic) — matches ch23's minute word for word (lane B); the gloss; "*READ FIRST*". Karis's
  *before* (italic; "*K.D.*" = the letters). "a flight" ×3 (lane B). "the lead between the panes" = LED; "the half-yard"
  (fix 37). Seln on the stair ("That's a copying kit." … "Sit down on the step. Not that one. The one behind you.") —
  level, not loud. The reach counted on five fingers (italic words). **The notice** (code block, six lines) exact;
  fpaudio flattens it line by line with a full stop; brackets silent: "Fragment acquired. Unnamed — Shadow-adjacent.
  Duration: sustained. Integration: partial. Tier equivalent: Bronze. Note: presence-suppression component;
  movement-masking component. Contact-to-short range. Acquisition: directed. Engagement: adversarial, non-combat."
  Bracken: "Nobody touch that bag." The fire-watch man: "You all right, lad?" Fix 34 ("five months") clean. Fine.
- ch35: Karis in her nightgown; Jessup (JESS-up) named once (Jask absent from the chapter). The wing's two lines
  (italic) exact. Lira: "Your hand went up." Brom: "Was he all right?" / "Then he was all right." Log "*Sixth fragment.
  Bronze — …*" and "*A system that confirms you is a system that was listening.*" exact. The deferral form (italic).
  The Ash instructor ("show me your feet"). "a little over ninety-six hours". The misfire: "Is that one?" / "That's
  one." The unit: Gwen's "Sir. Is it true about the records hall?"; Seln: "There'll be a notice… Read it. It'll be
  accurate." / "Nine."; "thirteen" (lane B); "*READ THE NOTICE*", "*CARRY THE LADDER*" (Gwen's capitals). Karis's
  two sheets (italic), "*Manageable.*", "*K. is glad it was smaller…*". Fine.
- ch36: the tray, the stair, the clerk; Lira's "Rent." **FIX** — "Up at the window, Gwen was waving her count at him: a
  large, plain *0*." then "Nought," said Seln — an engine says "zero" and then "nought" a breath apart → "a large,
  plain *nought*" (the word Seln says; the book's register). The chalk columns "*AIMED*" / "*NOT*" (sentence case).
  Brom's "You've spent two years learning to be the most awake person in every room…" exact. "like it owes you
  money" (Lira's, kept). The working ledger (italic). "Mm," said Seln — check it survives the render (B1/B2 note the
  same for "Mm."). The "*Who knew.*" list (six italic lines in one paragraph: one segment, list cadence). "*Filed under
  debts, no current mechanism of payment,*" (first entry; ch59 has the protected second). Fine.
- ch37: the birthday. Fiske at dawn (a nod). "Floor sheet?" / "Floor sheet." Lira's "I asked Hesk. In a letter. A year
  ago…" and "You people treat information like it's rationed." exact; "*A year.*" (Cael, stressed). Velmere (VEL-meer,
  Brom's house) named twice; Vell absent from the chapter. Karis's chart with "*see holder*" exact. Brom's sister and
  the pear ("*it tastes exactly the same.*" / "*so it does*", reported speech in italics). Hesk's note (italic) exact,
  "— H." a pause. The inventory (six italic entries) and "*Still open. Still real. Patience.*" exact; "*The eleventh
  of Sowing.*"; "*Sixteen. Six fragments… Semester evaluation in seventeen days…*" exact. "*Grandmother: watchful
  eyes… Ask.*" Fine.
- ch38: Karis's coat log (italic; "the stiff knee", "the pair with the dog"). The courier in registry grey. The scope
  (italic) exact; the manifest read from the bottom up; "*Archmarshal Vastin.*" (VAS-tin, as "fasten"). Withrow's
  three roads; "The inspection is ordinary. His presence is the message…" exact; Gault's "My wing changes nothing." and
  "It is not good or bad. It is the mandate." exact. Rooke under the north arch (his correction). The unit: Gwen's
  "a large *41* with an eye drawn in the loop of the four" (reads "forty-one"). "nine more chairs" (lane B). Fine.
- ch39: Bracken: "Be dull." / "Give me a dull month." / "An argument persuades a person. A file survives a person
  leaving the room." exact. Karis's box card "*41 pages — tabbed — DO NOT RE-SORT*" (caps: sentence case; "forty-one
  pages"). The clerk with the cold ("Is it still raining?" / "It's stopped."). "a dozen years of indexes", "eight
  years ago" (lane B). The names: Havel (HAV-el; "the pear one"), Ilsev (IL-sev), and the one with no page. Fine.
- ch40: the two columns on the board, read aloud by Lira (quoted italics; dates in words: "the ninth and the tenth of
  Reaping", "the nineteenth", "the twentieth"). Log "*Last time the Compact came to an academy for me…*" exact.
  Bracken at the counter ("you may cite me"). Gwen ("I'll draw you an eye"). Jask in the gap ("It's the end with the
  bread."). Withrow's address: "twelve minutes" (lane B), "two minutes slow", "Nobody else here carries my decision.
  Least of all a sixteen-year-old." Ephram on the stair: "second month", "sixty people" (lane B fixes) — "Anybody
  looks good in an empty room." "Rooke'll say *noted*." Fine.
- ch41: POV Seln s1 (the requisition; the six filings quoted in italics, with "…" ellipses; "*Complete, consistent,
  and containing nothing.*"; "What he kept, he kept." unitalicised, the first of the refrain's two) — mark the `---`
  into Cael's s2. Rooke: "Back to the bars, Merrick… You'll see him on the tenth." / "Better," which from Rooke was a
  speech (kept). Merrick on the gallery stair ("I'd sit somewhere else on the tenth, if I were his friend"). Lira's
  room ("Fiske told me to make them look."); Brom's "*Brom, that is not what I meant and you know it,*" (reported,
  italic). "*unresolved: test*". Fine.
- ch42: the four boxes; "*4 of 4*", "*311*" (read "four of four", "three hundred and eleven"); Bracken's "It's a thing
  that goes on being true in a room where nobody who built it is standing." exact. "I've got something in my eye from
  the wax." The semifinal: POV shifts to Lira at s3 ("Lira walked back to her chalk and did not look at the hip…")
  and back to Cael at s4 — mark both `---`. Karis's four lines (italic, F./L.) = the letters. "Force. One." / "Wind.
  One each." / "Even. No touch. Third exchange." / "Wind. Two to one. Bout." Fiske: "You stood still for a minute
  in my yard. Nobody's ever done that." / "Sit north." "a door slamming in a high wind" = the weather. Fine.
- ch43: Merrick's feint ("He tried to move me."). "Shield. One." … "Iron Skin. Three to two. Bout." Brom's "I've been
  trying to solve her for two years. Now I get faculty supervision and a crowd." exact. "Rooke'll say *noted*." The
  batons: "Nine to me. Eleven to you." (the 9–11 record, canon); "Receipt," said Karis. Karis's slate columns
  "*GROWTH*", "*CONTROL*", "*FIVE*" (sentence case); fix 41 ("second month") clean; "whether you can* not *do it"
  (reverse emphasis, parity even). Hall three: "You went," said Brom; "How far." (Brom, by content). Fine.
- ch44: the instrument woman "wound it" = WOWND. POV Havel s2–s3 (the carriage; the courtyard; "he did not bow" = BAU;
  "two different pages numbered eleven" canon; "Records officer," / "You'll want the enrollment basis first") — mark
  the `---` into Cael's s4 at the rail. Lane B's one full stake statement ("as a man sets a stake in a field before he
  lets the horses out"). "That's the pear one," said Lira. / "That's him." Ilsev's arrival; the third carriage;
  Vastin's collar mark; "Everyone they've ever sent has had something showing… Even Seln." Log "*New opponent. No
  tells. Begin.*" exact. Fine.
- ch45: breakfast ("Nobody talks about hips."; Karis's crosses in the boxes); lane B's added stake line ("Cael ate. In
  seven days…"). POV Vastin s2–s4 (the guest floor; the watch; the wing's filings; the three bundles; "*Observer
  product is testimony about the observer.*", "*An evaluation that begins from its conclusion is a report about the
  evaluator.*", the three marginalia — all exact; "*Verify: three weeks' preparation — from what baseline?*" spaced
  dash = pause) — mark the `---` on both sides. Cael s5–s6: the three clerks (the old one's knee); the counsel's
  sentence resumed at the word; Karis's "I'm asking you not to go and stand where he'll be."; Ilsev's page (boxed);
  the Ash instructor's "Hm." Fine.
- ch46: Rooke's "Enrollee." / "Instructor." The inch. POV Havel s2 (the card; "*Beyond ordinary courtesy.*"; the pear)
  — mark the `---`. Lira's capitals on Havel's page "*Careful men go up. Doesn't tell you what he's careful FOR.*"
  (stress; sentence case at render). The fifth-line bout: "Force. One." / "Stone. One each." / "Stone. Two to one."
  Vastin at the north rail, gone before the result. Brom at supper: "You do that." Fine.
- ch47: the landing ("Read's off." / "On purpose." / "Then it's the right kind of off." — Brom/Cael/Brom, clear).
  POV Ilsev s3 (the quiet woman with the board; her four questions; "Seven crosses in a term. Two for sneezing." —
  lane B's seven; the counsel's "fourteenth question") — mark the `---` on both sides. "Fifty-four out of sixty";
  "fifty-two", "fifty-eight". The working ledger (italic). Karis with her supper. Fine.
- ch48: the counter (Seln "did not raise his head", lane B); the returned case with the blue stamp; Gault's "He did not
  mention you." Lira's weighbeam. The taxonomy log ("*Coss enforced… Havel complied… Seln operates… This one
  evaluates.*", "*The Compact finally sent someone who takes notes the way I take notes.*") exact. Withrow's note
  "*…Wall seat, our side. W.*" = the letter. The sitting: "document fourteen" (lane B), "Recorded," said Havel;
  "Article forty-one. Eleven clauses" (canon); "Document sixty-two"; the Archmarshal's pen marks counted ("*Two.*",
  "*Three,*"); the transitional article is narrated, not quoted. The hold going thin "in the gaps". Fine.
- ch49: POV Ilsev s1–s3 (the routing file; the return in italics exact; "*Misrouted, or no answer at all…*"; the
  grounds exact; "eleven minutes", "eleven months" canon). Lane B's fold: s3 hands from Ilsev to Cael at the
  name-led paragraph "Cael had spent the recess on that hard chair…" with no `---` — mark the POV change at the
  paragraph. POV Havel s4 (the courier; the four entries; "*Two years. Two of us now. Nothing has ever come back with
  a name on it.*" exact, protected pattern) — mark the `---`. Cael s5: Withrow at the window; Ilsev takes the room
  ("begin with the subordinate clause this time"); Gault's paragraph and "I have. I do. I will."; Ilsev's finding
  (quoted) exact; the numbered margin list "*1.*–*5.*" (list cadence); "*He is calibrating the instrument. I am the
  reading.*" exact. s6: the folder on the empty chair; Karis's foot. Six scenes (lane B's 8 → 6). Fine.
- ch50: Bracken, Karis and Cael shelving ("Lock up behind you, Miss Karis."). The directive's green tabs; "*Per
  standardization directive*"; "*Shattered*" and "the older word meant unbound" (lower-case, once, as mapped);
  "*Why retire a working method?*" exact. The fire-watch boy. Brom: "Huh," which from Brom was a celebration (kept).
  The numbered log ("*1. What held.*" … "*4. What I think the question is.*") and "*Four days to the final. Five to
  the twentieth.*" exact (protected pattern). Fine.
- ch51: POV Lira s1 (the hip; "Receipt," said Karis; the batons untied; "Nine days.") — mark the `---`. Cael s2
  (Bracken's two sealed sheets; Fiske "a front-row seat on the north tier" = ROH; the delegation sits; Havel with
  empty hands). POV Havel s3 (the card; "a certificate three years old", fix 47; the pear) — mark. POV Lira s4
  (inside the north door) — mark. Cael s5: the terms (quoted italic); the two clocks; "Even," she called. "Taken on
  the guard."; "Wind, touch to the ribs. Iron Skin, touch to the floor. To Iron Skin, the cleaner." "a fight out of
  the other one's wound" = WOOND (the book's one). "swept her lead foot" = LEED. Fine.
- ch52: POV Ilsev s1 (the yard as a document; "the girl's entrance"; "three years ago", fix 48) — mark. Cael s2–s3:
  "four minutes and eleven seconds" (canon); "Iron Skin, down. To Wind, the cleaner."; the fourth exchange "eleven
  seconds"; "Wind. Clean. Two touches to one. The bout."; "not to bow" = BAU. POV Ilsev s4: the ceremony; Bracken
  reads "Ten bouts unbeaten. None lost." then writes and reads "Eleven bouts unbeaten. None lost."; Fiske claps
  first; the second sheet unopened. Cael s5 (Lira's three capitals); Ilsev s6 (Gault's note, "*— Gault.*"; the long
  form's printed words; "It was three years old.", fix 49; "I will record that I was present."). Cael s7: "*She held
  it like an exhibit.*" exact; "Two years I've been trying to solve you." / "And?" / "Third one someday." exact;
  Vastin writes one line. Fine.
- ch53: the twenty steps ("*On purpose?*", reported). Brom's furniture wing; "Like somebody with something in his
  pocket." exact. Karis's slate (six lines, two brackets; "*ON THE NUMBER.*" in her capitals — sentence case at
  render); "*Two, at the enrollee's placing.*"; "*5. No rehearsal…*" and the stop rule (italic). Gault's three rules
  quoted back by Cael (italic inside quotes: a voice reciting). Lira's thumbnail: "there were ten", "*ten of ten*"
  (lane B); "Be the fighter. In a measured room. Both." exact. The slip (italic) exact, burned; Karis's "Was that—" /
  "No. Never mind." The Ember placed second. Log: "*He doesn't wish me harm. He wishes me* measured." (reverse
  emphasis, parity even) and "*Sleep. Fight in the morning.*" exact; "*Nobody gave me a present tonight*" = PREZ-ent.
  Fine.
- ch54: Brom on the stair ("I'll know. That's the best I've got."). Lira under the arch ("I've a crown to live up to"
  = LIV). The four chairs; Gault's opening ("It may watch; it may not steer."); fixes 50–57 (second month /
  baseline) all clean. "Working ceiling given by the enrollee: six. Baseline: four." / "That is what the provision is
  for." exact. The vessel; "a decision point" once, as mapped; "That is a better instrument reading than the Greyvane
  exhibit supports" (protected pattern) present; "Mm," said Gault. "Magister. I need an interval." (protected pattern)
  / "Which one slipped?" / "The answer, Magister." Fine.
- ch55: "Eleven of twelve at the fourth weight" / "seven of eight at the third in your second month" (fix 58); fixes
  59–65 all clean; "That is what a real semester looks like" (protected pattern) present; "Because the clerk was
  standing where I'd have landed." exact; "a quarter of an hour" ×2 (lane B). Gault's note read aloud (ll. 177–185):
  a correct multi-paragraph quotation — five paragraphs, each reopening, the last closing; the §10 sentences present
  with the wing's additions between them (the map's ellipsis). Direction: one voice (Gault reading), no falling
  cadence at the paragraph ends. The Mire instructor: "I'm not a magister." Bracken's note "*…Bring nothing. — B.*"
  = the letter. Ledger: "*Q.'s question*" = the letter Q; "*He didn't look twice.*" Fine.
- ch56: the charter subsection (italic) exact; "twelve feet by fourteen"; "Correct filing is all this counter sells."
  Brom "be him". Cael's two-paragraph answer (ll. 69–71) and (ll. 85–87): correct continued quotations. The interview:
  eleven questions; "Why concede the category?" asked fifth; "*extensive private notation habit*"; "A circuit. And
  everyone who beat me," / "So I can't lie to myself later." / "What is the Compact evaluating? Me, or the provision?"
  / "The Compact filed no question…" / "I came to see whether the record and the practitioner match." / "You expected
  an enforcer." / "I've met the enforcers." / "Wardens enforce. Assessors comply. I evaluate…" (two paragraphs, ll.
  285–287, correctly continued; spaced dash = pause) — all exact; "cage built for people who did not exist" and "most
  competent half-hour I have sat through in eleven years" (protected patterns) present. "twenty-two minutes",
  "twenty-nine minutes". The Archmarshal is "the man" throughout Cael's POV. Fine.
- ch57: "Third morning of ice" (Karis's date). Bracken's enrollment-book line (italic); the folder "*Ninety-four
  minutes.*"; "Correct filing." The counsel: "Favourable in substance. Neutral in tone." / "A triumph." Brom reports
  Rooke word for word — nested single quotes inside his speech: "'Your cohort standing holds. So, apparently, does
  your friend's paperwork. Noted.'" (exact; direct as Brom in Rooke's dry voice); "He adjusted, and he made sure
  somebody heard him do it." (protected pattern) present; "I'd go through a wall for him." Ilsev at the foot of the
  steps: "It is simply on your side, which is worth an enormous amount and is not the same as being loved by anybody."
  (protected pattern) present. POV Havel s5 (the sixteen seals; "Sixteen?" / "Sixteen."; "Safe road"; "Nobody checks
  them after me.") — mark the `---`. Cael s6: Log "*The system isn't confused about me.* / *Confused systems ask.
  This one checks.*" exact. Fine.
- ch58: POV Seln s1–s2 (the docket, "*No extract or copy retained.*"; the clean return; the quarterly's four lines
  exact; "the fifth hand, the shorthand that had grown out of the cramped one" (lane B); the cipher line "*unmarked
  file. one of three. probably the third.*" (lower-case start, protected pattern: deliberate); "What he kept, he
  kept." the second time) — mark the `---`. Cael s3: Gwen ("the ones you never see are the ones doing the work");
  "Thank you for the form." / "Mm," said Seln. s4: the cart; the card "*Reading room. Assigned: K. Dellenmoor.*"
  s5: Karis reads her corridor page, Seln's words nested in single quotes ('Miss Karis.' / 'Records retention.' …);
  "where the notebooks were since the third week of term" (protected pattern) present; "Then he knew where your
  notebooks live" = LIV. "So that's what he is now." / "That's what he's been since the pin. He just let us see it."
  exact. s6: "Gratitude is the leak." exact; "You'd break him," said Brom; Karis's "I was applying a correct principle
  to the wrong class of object. He isn't an instrument." (protected pattern) present; the Log line in her words. Fine.
- ch59: the last session ("Nine words." ×2); "*Pick a room and describe where its attention goes.*" exact; "harder
  and less interesting, which is the correct order" present; Gwen draws an eye on his hand. Log "*Filed under debts,
  no current mechanism of payment. Second entry. Same file. Same nothing.*" exact. POV Vastin s2–s6 (the posting-house;
  named "The Archmarshal, Vastin" in narration; the brass watch; the three tapes; "in forty years he had never once
  found the two to be identical" (protected pattern); "the quarter of an hour" ×2, lane B; the notebook pages exact,
  including "*The Copper champion is Iron-grade…*") — mark the `---`. **RENDERER ITEM**: the struck line is set in
  markdown strikethrough — "*Frame fault, trial five. Correction preceded the audible release. ~~Capability exceeds
  classification.~~*" — fpaudio strips `*` but not `~~`, so the tildes reach the engine; the words are protected
  ("struck once, legible") and the narration explains the stroke ("drawn a single line through three of the words"),
  so no text change: the segmenter must strip `~~` and the direction file read the struck sentence in a cancelled,
  lowered register. "*No adverse finding.*" / "*Subject warrants attention.*" (the two scraps); the letter to
  Bracken (italic, four sentences); "he would ask it in a room with the door shut and tell the boy first" (protected
  pattern) present; "*Classification error is unlikely. Continue observation.*" exact. Fine.
- ch60: Cael s1 (the counting house; Bracken's "Ninety seconds"). POV Lira s2–s3 (the clerk's lines; "sigil" =
  SIJ-il; the sequence run three times; the load figures; "Wind," said the man. "Iron. Rank One."; the supersession,
  "It took ten." — lane B; "stayed live underneath" = LYV) — mark the `---` both sides. Cael s4: "fifty-one minutes";
  the certificate (italic) exact; "*Wind Path, Iron-tier, Rank One*" said loud; "Louder. There's a clerk." (Karis, by
  alternation); "They didn't give me anything today. They caught up." exact. Fine.
- ch61: the crown retired: "There. It's retired." … "Prizes go to winners. That's what I got for having to." exact;
  "It can't live with the bread" = LIV. Log: Fiske's sentences quoted inside the italic entry exact; "*I've had a
  page headed* Fiske *since early in the term.*" (reverse emphasis). The porter rubs out the six letters; Fiske reads
  the pinned certificate twice. Ephram on the oak ("Assay. A minute."): "second month", "sixty people", "All season"
  (lane B); "Rooke's cohort works at a speed you have never been hit at." (protected pattern) present; Log "*I am
  going to be very careful about how I remember Halcenvane.*" present. The sweep: "*nil*"; Bracken's "Correct filing
  is all I have to offer anybody this side of the river." Withrow closes the year: the finding (one italic line,
  quoted); the two multi-paragraph speeches (ll. 183–185 and 191–199: "One:" / "Two:" / "Three:") are correct
  continued quotations, each paragraph reopening, the last closing; "eighteen years" (canon). Karis's banked clause
  "*Participating academies shall field any practitioner appearing on their enrollment record.*" and "*Interesting.*"
  exact; "A question you ask early is a question somebody else gets to answer first." (protected pattern) present.
  Fine.
- ch62: Hesk's reply (italic, four lines; 'keep looking.' in single quotes inside) exact, "a grandfather's guess";
  Vell's letter (italic, five sentences) exact, "Vell's mark" and the ledger's stamp. The recess sheet "*S. Seln.*" =
  the letter S. Gault's calendar line (italic). "Thank you for the form." / "Mm,". The year's inventory: six entries,
  each a multi-line paragraph (one segment each; the first is the book's longest, 1,074 chars — fpaudio splits it at
  sentences); the counts in words ("eleven clear of twelve", "eight of nine", "nine of eleven… eleven of eleven");
  "*Still open. Still real. Patience.*" exact; "*The system isn't confused about me.*"; "one retired word". The
  season off the walls; Rooke: "Nineteen. Round three. Four a week."; Fiske: "You made them look." / "North tier,
  next season." The wall: "Next year the continent comes to measure everybody." / "Good." exact; the closing exchange
  ("I have six things that aren't a Path." … "A semester stamp that says I proved it. And four people who know what it
  costs." … "And somewhere in a file, the most careful man I've ever met wrote that I'm not an error." / "You're not,"
  said Brom. / "Never were," said Lira. / "Noted," she said.) exact; "The bluff held. The stamp was real." exact. Fine.

## Running tally of fixes
Required (8): ch7 "Instr." (the pinned minute); ch15 "0 of 7" and "0 of 31" (nought); ch15 the three shorthand lines
joined with middle dots (" · " → " — "); ch25 the board line "6/0" (six and nothing); ch36 "a large, plain *0*"
(nought). Optional (3): ch18 an untagged speaker change after Cael's own line; ch19 "the 80th" (the eightieth); ch22
"40–60" (40 to 60). Renderer, not text: the `~~` strikethrough in ch59 (Vastin's struck verdict, protected: strip the
tildes, read it cancelled); the all-caps signs and chalk in sentence case; brackets, the one fence and the `---` never
voiced; "Mm." / "Hm." / "Huh." checked in the render; the italic documents and the POV cutaways marked per segment.
Lexicon, not fixes: lead = LEED (fighting) / LED (window lead, ch7, 17, 34); wound = WOWND (11) / WOOND (ch51);
bow = BOH (ch28 tape) / BAU (ch36, 44, 52; "bowed" ch3); live = LYV (ch6, 27, 30, 49, 60) / LIV elsewhere; the
initials (K., L., F., C., H., B., W., Q., S., K.D., TA) as letter-names; "41-7843-V" digit by digit.
