# Book 5 — listening proof, running notes (Claude Fable, review seat, fresh context, standing in for Sol, 2026-10-06)

Read order: prompt → Book 1, Book 3 and Book 4 listening-proof.md (models; Book 4's listening-notes.md as the model for
this file) → COMPLETION-PLAN, whole-arc-read (§8 applied), PASS-BRIEF, LANE-A-REPORT, LANE-B-REPORT → EDITION_BRIEF
(audio-first, Reader Standard) → OWNER-DECISIONS #3, #11, #33, #35–#42 → BOOK_MAP §10, §13 → protected-patterns.txt →
audio/fpaudio.py → mechanical sweep (two scripts, scratchpad) → chapters 1–60 in order. No manuscript file touched; no
git command run.

## Mechanical sweep (script over all 60 files, before the read)
- 60 files, 296,931 words by `wc`. Every `---` has a blank line before and after (0 bad). No headings after line 1,
  no tabs, no trailing spaces, no double spaces, no curly quotes, no `_`, no `**`, no `~~`, no backticks outside the
  one fence.
- `*` count per paragraph: 0 odd. `"` count per paragraph: 3 odd — ch1 ll.157, 159, 161 (Withrow's "Three numbers"
  speech: opens, reopens, reopens; l.163 "Eighteen." opens and closes). Correct multi-paragraph quotation; the odd
  count the lanes noted was there before them and is not a defect.
- Code fences: 1 (ch56 ll.193–200, FRAGMENT ACQUIRED, Storm-adjacent; §10 verbatim). fpaudio flattens each line + ".".
- Brackets: `[UNCLASSIFIED]` ch48 l.93 (the board, §10 item 14); `[unnamed]` ch56 l.195 (the notice); `[SHATTERED]`
  ch60 l.113 (the convening's question, §10 item 18). No other brackets.
- Lower-case paragraph starts: 4, all italic documents — ch24 l.109 "*eighteen years. counted anyway.*" (the
  half-sheet under Vastin's seal); ch31 l.275 Umber's attestation (§10 item 11); ch51 l.239 the trial-sheet
  recommendation (§10 item 15); ch57 l.221 "*our fighter does not mis-seed.*" (§10 item 55). Deliberate.
- Paragraphs with no terminal punctuation: 1 — ch31 l.275, the attestation ends "…measured alike*" with no stop
  (protected; the engine simply ends the segment; direction item). Six others end in a colon introducing a written
  line (ch5, ch6, ch11, ch24 ×2, ch59): a short rising pause.
- Doubled words: "six six" / "three three" ×9 (ch5, ch6) are the composites read aloud, "Eight point six six" — the
  decimal, deliberate; "had had" ×7 (ch6, 15, 17, 25, 44, 47, 52); "that that" ×1 (ch18). All grammatical. No true
  doubles, no ", ," or "..".
- Slashes between words: 0. Abbreviations: only "vs." (ch48 l.93 the board line, §10 item 14; l.105 "the little vs."
  in narration about it). None of Cu/Br/R1/wk/exch/unr/def/Instr/T-numbers/d-numbers.
- Numerals: "41-7843-V" (ch2, ch5); the numbered lists "1. 2. 3." (ch4 l.247 Karis's three; ch13 ll.187–193 the four
  rotations; ch50 l.49 the minute's headings); the board/card lines "Iron, Rank 9" (ch19), "Rank 1" (ch19), "IRON 9."
  / "COPPER 1. FIRST SEED." / "IRON 3." (ch30), "ZERIN — AUREMONT — 9. LIRA — HALCENVANE — 4." (ch36 l.135, the
  seeds), "Figure: 25." (ch38 Ilsev's form), "Gold Rank 3" (ch46, ch52, §10 items 25, 27), "GOLD 3." (ch48, item 14),
  "Priority Level 4" (ch60). All read naturally as numbers. No "0", no ordinal numerals, no en-dash ranges.
- All-caps (75 hits): the woodcut titles (ch29), the board lines (ch30, ch36, ch45, ch48), Rooke's capitals (ch25 A
  BRACKET OF CEILINGS and the five names; ch40 the four cards), DEMONSTRATION (ch7, ch10), QUALIFIED (ch24), the
  betting-row sign NO BOOK ON THE DEMONSTRATION BOUTS (ch32, 45, 54), THE FIVE: GONE (ch32), QUARTERFINAL (ch34, 36),
  THE CROWD / HE'S BETTER THAN THE WOODCUTS (ch42), Lira's TAKEN. HALCENVANE. ASK THE GIRL WITH ONE ARM. (ch44),
  HALCENVANE — AUREMONT / SQUAD AS FILED / NONE (ch45), WHO FIGHTS THE ENROLLEE? (ch47), HALCENVANE on the bedsheets
  (ch51), THE ARGUMENT AND THE TABLE (ch51), [SHATTERED] (ch60). All written signs and boards; renderer sentence case,
  as Books 1–4.
- Spaced em dashes: 92 lines, of which 60 are the chapter-title lines; the rest are inside documents, letters,
  board lines and the notice, plus four spoken: ch17 l.183 (Seln), ch40 l.95 (Rooke), ch52 l.47 (Withrow, §10 item
  50), ch20 l.221 (the ruling read aloud). All pauses, never "dash".
- Cut-off speech `—"`: 11 (ch4 ×2, ch18, ch20, ch29, ch34, ch49, and four that are narration ending in a quote).
  Read in place.
- Name pairs per scene (script, split on `---`): Gwen, Selm-, Kestrel, Halvern, Coss, Doss, Marrow, Corbin, Bede,
  Maud, Abbot absent. Bracken/Brom 42 scenes; Withrow/Rooke 30; Rhagen/Rooke 27; Marek/Karis 18; Daeva/Cael 14;
  Halcenvane/Greyvane 12; Zerin/Daeva 6; Havel/Cael 5; Zerin/Seln 3; Ivenne/Ephram 3; Umber/Auremont 3; Ilsev/Lira 2;
  Rhagen/Reydan 2 (ch41 s2, ch45 s1); Quenna/Karis 2; Vastin/Withrow 1; Hesk/Fiske 1 (ch60). Umber never shares a
  scene with the word "Ember" (checked separately: UM-ber vs EM-ber is one vowel apart and Karis is Ember Path).
  Vell/Velmere never in one scene (ch60 both, different scenes). Ivenne/Ilsev never in one scene (both in ch38).
- Protected patterns: all 52 `protected-patterns.txt` lines present, each once in its mapped chapter (the "things
  that are going to happen" line twice, ch46 and ch48, as mapped).
- Homographs (contexts pulled): lead = LEED in "lead shoulder" (ch22 ×2), "lead him" (ch43), "lead instructor" (ch49
  ×4, ch57, ch59), "lead-in" (ch52); LED once: ch49 l.95 "a single pane of thick glass set in lead" (Daeva's window,
  same chapter as four "lead instructor"). wound = WOWND ×7 (the strap ch6, ch8; "a cord being wound" ch12; forearms
  in linen ch38 ×2, ch39; the clock ch53); WOOND ×1: ch59 l.47 "feel like a wound" (§10 item 29). tear = TAIR (ch12
  "tear a strip", ch59 "tear it to pieces"); tears ch35 = TEERS. live = LIV except ch37 l.99 "find it live" and ch53
  l.111 "read live small in the corner" = LYV. lives = LIVZ ch3, ch5, ch22, ch50; LYVZ ch25, 26 ×2, 45, 49, 56, 57.
  bow: ch1 "a drawn bow" = BOH; ch8, ch40, ch42 the gesture = BAU; ch50 "bow-wave" = BAU; "bowed" ×16 = BAUD. present:
  all PREZ-ent (gift ch3, 43, 53, 55; adjective elsewhere; no verb). refuse: all verb. close: nouns and adjectives
  (KLOHS) in "the close of intake", "close-ruled", "close-printed", "close-written", "close hand", "close under the
  cap"; verbs (KLOHZ) elsewhere — all clear in context. wind: the Path and the weather; the verb twice, ch44 l.91
  "made to wind a gate" and l.121 "allowed to wind anything else" (the lock-keeper's gate) = WYND. row: all ROH.
  minute (79): all time-uses except "the minute" as the bank minute (noun MIN-it, same). record/records: nouns and
  verbs clear in context. read: REED/RED by grammar; "the read" (noun) = REED throughout.
- ", as" clauses: 510 listed; read below.
- Paragraphs over 700 flattened chars: 97 (list in the proof).

## Chapter notes
- ch1: Withrow's "Three numbers" (ll.157–163) is a four-paragraph speech: three open paragraphs, the fourth
  ("Eighteen.") opens and closes — correct, not a defect. "*Hold. First.*" inner word. "Rooke's back… said, 'Yes.'"
  (single quotes inside speech). The roster lines in italics; "*S. Seln, assessment office…*" = the letter S. "a drawn
  bow" = BOH. "paying for wind" = the Path, lower-case. "Everybody I live with" = LIV. The four at the hall and the
  board (Lira/Brom/Karis/Ephram) tagged. Fine.
- ch2: "*Caelen Hesk-ward, 41-7843-V, …*" (digit by digit; carried). Bracken's sand. Karis's bench ("Be the regional
  registrar"): two voices, alternation clean. The counter: "Thank you for the form." / "Mm." / "Pack for the third
  one…" (§10 item 34) exact. Gault's handle. Supper: Brom/Lira/Karis/Ephram all tagged. Log item 19 exact. Fine.
- ch3: "Yes, Instructor." ×2 (Brom; then Cael after "Rooke looked at Cael"). Ephram calls him "Assay". Rooke's board
  "*Wait for the heel. Cost: the first share. Fine.*"; the profile margins in italics; "*Rank Four on paper. Fights
  like a Seven. Buried.*" The broom: four voices tagged; "a dozen more times, by Karis's count" (lane A's move: 7 + 4
  + 1). The memorandum (§10 item 3) exact; Withrow's sentence quoted inside Bracken's speech in italics. Fine.
- ch4: the clause (§10 item 1) and the provision lines (item 4) exact, read aloud by Cael in quotes with italics. Three
  cut-offs: Brom's "What—" (l.35), "So a fighter who can't be seeded—" / "—can be fielded." (ll.59–61, an interruption
  pair: short gap, no falling cadence), "If it fails—" (l.239, Lira completes). Karis's card "*1. … 2. … 3. …*" (read
  "One. Two. Three."); Brom's pencil line. Hesk's letter with "— H." (pause). "the eleventh of Sowing" = SOH-ing.
  "square to the others" (Seln). Fine.
- ch5: POV Vastin s1 (the routing slip; "*Received. Logged. Assessed. Referred for advisory.*"; "*Classification error
  is unlikely. Continue observation.*"; the advisory, §10 item 5, exact with its spaced dash) — mark the `---`. s2 the
  card: "*C. Cael, enrolled practitioner, unclassified — scheduled per…*" (item 6) exact; Karis says "*Caelen
  Hesk-ward, 41-7843-V* is the registry's" aloud — digit by digit. s3 the map room: Rooke's card read by Karis
  ("Seven. Eight. Nine. Eight. Eight." … "Eight point six six."), the bands table in italics (words throughout),
  "Chief Adjudicator Umber" (UM-ber) first named. s4 the Log. Fine.
- ch6: the mock bouts. The card reading (ll.85–111) alternates Rooke (five marks) and Karis (the strike and the
  average) untagged after the first pair; the content carries it (five figures = Rooke, three figures and "point" =
  Karis). Direction: "Eight point three three", "Eight point six six" are decimals — read "three three", never
  "thirty-three". "*execution, nine.*" / "*Control, nine*" = Cael's inner pricing. "Touch, Brom." Rooke's "In twenty
  years of coaching…" Brom "wound it into a neat roll" = WOWND. Karis's strip in the manual. Fine.
- ch7: steward's calls "Touch. River." / "Touch. Halcenvane." flat. The format speech (l.157). "*DEMONSTRATION.*" on
  the day board (sentence case at render). The validator's "adjacent to it" (§10 item 35) and Lira's "Nobody gets to be
  surprised by me anymore…" exact. "*Want to see it before the story's finished.*" (the form). Fine.
- ch8: "Touch. Hills." The buried Copper; "the clearest touch Cael had ever seen" (keep). "He bowed to the man" = BAUD.
  Karis's "Institutions are like fighters…" (protected pattern) present. Ephram at the rope: two voices. Cael's
  notebook: "the bravest thing I've heard on this floor" (keep). The midday table: Brom/Lira/Karis tagged. Fine.
- ch9: the ganger (unnamed by design). "Huh," said the ganger. The handshake: "Story undersold you" (aloud) then
  low: "I know managed effort when I'm the one being managed." (protected pattern) exact; "Undersold! Tell them it's
  undersold!" The overheard sorting in italics ("*Quick feet*, said one voice…"): passing voices. Lane A's "five feet
  beyond the east rope" (l.15) reads clean. Rooke's review on the steps, one sentence each, in one paragraph; "I'll
  lend you that exchange this time." (the arc read's fix) sits clean; "You fought exactly as well as you intended to."
  (protected) exact. Log item 20 exact, "I'm being — accommodated." = a pause. Fine.
- ch10: the waystation: Seln hands the ruling to Karis; the ruling (§10 item 7) read aloud in quotes with italics — a
  voice reading, flatter than her own; "The category is going to hold you exactly as long as nobody makes you."
  (protected) exact. Table: Lira/Ephram/Brom/Gault/Rooke tagged. Lira's "right shoulder was tight" (the debut bill;
  the left shoulder is the burst, ch35 on). The rail: three voices tagged. "*Examiner's Manual. Annotated. Present
  Cycle.*" = PREZ-ent. The mill town; "*DEMONSTRATION*", "*curiosity.*". Fine.
- ch11: the rating table ("eleven minutes", canon). Log: "*It's Vell's ledger, done by five people…*". The manual's
  three words in italics. The guild champion: "Touch. Guild." The pillar corner; Rooke's file line in italics. The
  family argument: "Touch. Halcenvane." / "The—the Ember." (the steward's hesitation inside speech, not a cut-off) /
  "Touch. Halcenvane. The Wind." / "Bout to the Wind." Lira's "You've been watching my *hand*." Ephram's upper Iron:
  "Touch. River." / "Bout and upper Iron to Halcenvane."; "*Iron, upper draw*" on the card. Fine.
- ch12: page thirty-one: "*Judges rate the performance demonstrated, not the capacity inferred.*" and the annotation
  (§10 item 8) read aloud; Karis's "The fairest instrument on the continent has exactly one blind spot, and you live in
  it." (item 36) exact, "live" = LIV. The yard-master: "Touch. Guild." ×1; "like a cord being wound" = WOWND; "*Oh*,"
  from an apprentice. "You fight like an auditor." The curiosity Bronze's nine questions: two voices, alternation
  clean. Log: "The mask has stopped being a thing I hold up and started being a register I speak in." (protected)
  exact. Fine.
- ch13: the stove: five voices plus Gault, all tagged; Gault's letter ("*Sir. I write to thank you, profoundly, for the
  handle.*"); Ephram's ears (the first, kept); "The difference between now and Fenmark is solvency." (protected)
  exact. **POV Seln s2** (copying the record: "Twenty-four and a third. Twenty-one and two-thirds…", "Six figures
  inside three points"; "Variance is cheap. Buy some." exact; "the enrollee" throughout his window) — mark both
  `---`. s3 the evaluation: "*Gault, with two.*", "the twentieth of Reaping" (REEP-ing), "*Renewed.*", "Routine," ×2;
  the Log inventory; "Used-to is a rating. It just doesn't post." (protected) exact. s4 Rooke's "They keep time like
  a metronome."; the engineered-scatter list "*1.*–*4.*" (read "One."–"Four."). s5 the tailboard; Log item 21 exact.
  Fine.
- ch14: the cohort board lines in italics; "healed months ago" (the arc read's fix, l.145) clean; Rooke's capitals
  "*Early eyes, late feet. One in two. He holds like a gentleman. Find somebody who doesn't.*"; "Thank you for the
  form." / "Mm,"; Bracken's pouch; Karis's open lines "*Records hall, last term. The reader. Client unidentified.*",
  "*Pattern is consistent with private interest. Not Compact pattern.*" (italic inside speech: read as quoted
  text), "*The trade in records.*"; the milestone silence. Fine.
- ch15: the quarry town. Rooke's doctrine speech. "*Pack for the third one…*" recalled in italics. The slate: "Four,"
  said Cael (bursts). The Stone reserve's one long sentence. The coat-rack: "Huh," said Lira. "It's small." / "No,"
  he said. "You mean it's small." (§10 item — the B4 echo) exact. The gallery's three columns; Karis's "It's the
  clients who get to be nobody." (protected) exact; the grey-wool woman (unnamed by design). Fine.
- ch16: page three (the southern coach, unnamed). The Fenmark boy: "Touch. Halcenvane." / "Even." / "Two to nothing.
  Bout to Halcenvane."; Rooke's four words "*Good. Schooled. Expects respect.*"; the figures "Lira twenty-six, the boy
  twenty-one". Brom's "Do your own next season." Karis's loss "twenty-three to twenty-two". Supper: "They kept your
  name and threw out your foot." Seln: "the office has a matter to put to the table." Fine.
- ch17: **POV Seln s1–s3** (the alehouse and the bargemen's dog; the file read by candle, "*Managed?*"; his four
  things including "*unmarked file. one of three. probably the third.*" quoted mid-sentence, lower-case by design;
  "Jask" (JASK) named once; the wing's two lines "*Pattern is consistent with private interest. Not Compact
  pattern.*"; "Karis Dellenmoor" in his thought) — mark the `---` into s4 ("Cael watched him do it"). s4 the table:
  Seln's finding "private interest, confirmed — the market, not the Compact." (§10 item 37, spaced dash = pause);
  Lira's "And it was a *shop*?"; Cael's "I'd rather fight people who prepared for the wrong me than people who
  prepared for nothing." exact; Brom's "That's page three." s5 the chalk "*No book on the demonstration bouts.*";
  Brom's semifinal "Two to nothing. Bout to Halcenvane."; Log "Brom is standing at the narrow end charging
  admission." (protected) exact. Fine.
- ch18: "Touch. Quarry house." / "Touch. Halcenvane. One to one." / "Bout to the quarry house."; Rooke's one word
  "Walk."; Ephram's page "*Quarry house, Stone, semifinal: account*". Supper: Lira does the board-man ("No book,"
  she said, in the board-man's voice…; "And he said—" (l.165) is her own pause before she gives the line); "He's the
  most classified fighter on this circuit. Some clerk ought to write and let the registry know." (protected) exact.
  Ephram's account "Item. Heat-shadow…"; Rooke's "*Takes a loss like freight. Ready.*"; Karis's "Twenty pages." (lane
  A). The audit: Seln's heading "*Delegation: correspondence and floor discipline.*" Item three in italics; "Two to
  nothing." The Auremont pair (unnamed). Fine.
- ch19: the foreman (unnamed): "Touch. Quarry." / "Even." / "Touch. Halcenvane. One to one." / "Two to one. Bout to
  Halcenvane."; "*my lads asked me to*"; "It's only angry." Rooke: "Slow on purpose is still slow." Lira's "There's
  your bill." Log inventory. Hesk's letter: "the fault's in the workshop, never the instrument" and "Mind the
  difference between the ones measuring you and the ones reading you." (protected) exact, "— H." The quay steps:
  "*ZERIN — Auremont — Wind — Iron, Rank 9 — nineteen. …*" (read "Rank nine"; the dashes pauses); "She—" (l.397,
  the withheld name: a cut-off, short gap); "The moment was three years of work, and I already had it." exact;
  "She's not faster than me," / "She's faster than me *right now*." (item 38) exact. Rooke's "It's a bracket of
  ceilings."; "*MAREK — Rhagen Institute — Glass — Copper, Rank 1 — notations attached.*" ("Rank one"; Rhagen =
  RAH-gen); Brom's "This one's been mispriced too. The dangerous direction." exact. The record "twenty-six and
  twenty"; "*Title.*" Seln's quarterly in italics. Fine.
- ch20: Rooke's sheet "*Slow on a cold floor: walk the slow…*". The circular at the waystation: "Does that mean—"
  said Ephram / "It means we're going," said Brom (l.75–77); Seln's "Approximately four hours ago." The innkeeper
  reads the framed ruling aloud (item 7, in quotes with italics: a ringing voice reading). The draw; the five filings
  in italics ("*Iron Rank Nine. Force. Barges.*"). "Huh," said Lira. Fine.
- ch21: the merry Blade is one paragraph (lane A): "Touch. Confluence." / "Two to one. Bout to Halcenvane." inside
  it; "*the town asked me*". The caravan captain (unnamed by design): Rooke's "He's pricing the floor"; "Touch. The
  convoy."; the shout "*The salt road!*" (a passing voice); "Touch. Halcenvane. One to one."; the handshake "You found
  the change of guard… charged me toll on it." (canon); "*Shield runs on a clock*" (inner). Karis's "That has never
  happened at a regional meet." Log bill lines only. Fine.
- ch22: the builder: "Touch. Hill-river house."; "lead shoulder" ×2 = LEED; "Level after four. The figures decide.";
  "twenty-seven, and the builder twenty-five"; Log "she has stopped fighting inside other people's bouts at all"
  (protected) exact; "went red to the ears" (Lira; lane A's keep). Karis/Ephram "twenty-four to twenty-two"; "The pool
  was worth more than the placing." exact. Brom's final "You've a very dull way of winning." The Iron final: "Touch.
  Halcenvane." / "The—Blade." (the steward's hesitation inside speech, as ch11); "Touch. Halcenvane, the Wind. One to
  one."; "Bout and title to Halcenvane."; "Lira twenty-six, Ephram twenty-five"; Rooke's "Bank it." Fine.
- ch23: the coastal Wind "went red to the ears" (left as is). The barge-master (unnamed): "Touch. The confluence.";
  "You found the bed"; "*What are you carrying?*" (the hail, italic inside speech) / "I don't know yet." / "Then I
  hope it's cargo." Log bill lines. The record "twenty-one… twenty-four… twenty-three, twenty-five… twenty-two".
  Karis reads the steward's sentence (§10 item 10) standing, in quotes with italics; "*It must be admitted*," she
  said (Lira). Log: "The strata keep holding me up. Karis says she'll get to why…" (protected) exact. The convenor:
  "*Halcenvane*," (stress). Withrow's "Now we go be measured by everyone at once." (item 39) exact. Fine.
- ch24: Gault's story: "Fourth." / "I have been mispriced by professionals, young man." (protected) exact. The gate:
  "*Copper! Copper!*" (a chant), QUALIFIED (sentence case at render), "*eighteen years. counted anyway.*"
  (lower-case, a written line: deliberate). **POV Vastin s3–s5** (the digest; the query's three nouns in italics,
  §10 item 9; his three answers in italics, each opening "Read as:"; the reply "*Acknowledged. The submission of the
  evaluating office is entered.*"; "seven years ago… the drains" is lane A's move) — mark the `---` at s3. Fine.
- ch25: **POV Havel s1** ("Assessor Havel"; the rotation sheet "*Continental finals, Norhold. Observation support.
  Seat two of six.*"; the notebook's four entries, no fifth; packed "like part of the work") — mark the `---`. s2
  Rooke's sheet: "*A BRACKET OF CEILINGS.*" and the five lines in his capitals (sentence case at render; the names as
  names); Ephram's "Trial caller." and his ears (the kept appointment); "Yes, sir." (the Shield reserve). s3 Lira
  builds Zerin (Brom's spoon). s4 Brom and the notations ("*the same join, found and then worked*"); Rooke's "Sound".
  s5 the bench floor: Ephram's "Lira—" (l.213, cut off by Lira going: short gap); "North." / "Gap." "Second." s6 the
  Shield reserve ("That's not fair"; "Oh,"); Rooke's "One reserve." Fine.
- ch26: the card "*Reading room. Assigned: K. Dellenmoor.*" (the letter K); the map of provinces; the founding
  articles' slip ("After the season"); the marbled log's "four". Hesk's letter, "— H." ("Tell the big one…"); Brom's
  "Then I'll keep it flat." Log inventory ("Six. The record holds two of them public…"). **POV Seln s3** (the report
  in italics; the roster line "*S. Seln, assessment office: records and floor scheduling.*" = the letter S) — mark
  the `---`. s4 the seedings; the wall: "*Not glad tonight. Morning.*" s5 the melt; the bridge; "We've been
  published." Log "Seventeen days to the city". Fine.
- ch27: the coast coach (unnamed; "She nodded." / "that's a long conversation"). Brom's snowdrops. Gault on the
  bench. The corner game: Brom's spoon; "North-east," said Cael; Lira's "That's not fair"; Rooke's "Early." (canon);
  "*Early,*" in pencil on her hand. The flag; the keeper (unnamed); Seln's "The office logs the road."; "The city was
  still nine days off" (the arc read's fix, l.293) reads clean beside Karis's "a full week from the city. More."
  Fine.
- ch28: Withrow at the five-arch bridge; Bracken's "I slept like a quarry stone."; "The tournament will measure the
  five of you. The continent will measure all of us." (protected) exact. Brom in the dark: "Seln." The road sorting
  (lane A's two carters); Rooke's "Because they did it last time."; Log "*Customs don't need a clerk…*". The rise:
  "seven, eight; perhaps ten" (lane A's move); Karis's "The prospectus was counting people."; Lira's "It's bigger
  than they said." The board: "eleventh from the top"; the pie man ("That's the clause house"); the champion's gate.
  Log "This city is the system with the roof off." exact. The keeper is "he" (counts aloud). Seln squares the
  papers. Karis's "*All of them.*" Fine.
- ch29: the boy at the pump ("Are you the unclassified one?"); the woodcut titles in caps and italics (*THE UNNAMED OF
  HALCENVANE*, *THE BOY THE REGISTRY COULD NOT SORT*, *LIRA OF THE BLUFF*, *DAEVA OF AUREMONT*, *THE FIVE FROM THE
  BLUFF*) — sentence case at render; the barrow-man's "The sinister one sells better." Seln's "Inaccurate. The
  office's ledger is larger." and Ephram's "Was that—" (l.113, cut off: short gap). The rail: Ephram's "At
  Halcenvane you arrived pre-explained. Here you arrived pre-*sold*. Try to be a disappointing product." (§10 item
  40) exact. Auremont's column: the overheard "*The Gold's at the back. She'll be last. That's the one.*" / "*Daeva.
  There. Last of all.*" (passing voices). **POV Vastin s5** (seat twelve: "*Seat twelve: held. No plate. Stewards to
  keep the seat clear…*"; his day-book line in italics) — mark the `---`. Fine.
- ch30: the marshal (unnamed); the rules paragraph read aloud by Karis in italics (a voice reading); Brom's "Five."
  Gault's "Better. I'd have lost the bout." Rooke on Umber at the rail. The steward (unnamed) and "It's cheaper than
  deciding." The draw: "like a stone into a pond" (lane A's one use); the board lines in caps and italics "*ZERIN —
  AUREMONT — WIND — IRON 9.*" (read "Iron nine"), "*MAREK — RHAGEN — GLASS — COPPER 1. FIRST SEED.*" ("Copper one"),
  "*KARIS — HALCENVANE — EMBER — IRON 3.*", "*IVENNE*" — sentence case, dashes as pauses; Brom's "Somebody in the
  seeding office reads past the paper." exact; Cael's "Everyone else knows who they're fighting… I'm about to find
  out who volunteers." (item 40) exact. Fine.
- ch31: **POV Umber s1–s2** ("Chief Adjudicator Umber"; the case and the three seals; the thumbnail scratch; the
  calibration ledger and the struck Blade judge; his master's "*You checked them last night. So your hands may shake.
  The seals did not.*") — mark the `---` into s3. s3 the procession: "four men in grey, two on either side of a tall
  staff" (the arc read's fix) and "No house walked behind it."; the overheard "*That's the clause house. At the
  back…*"; Daeva read at a hundred yards; Lira's "She just counted us." s4 Umber on the floor: the attestation (§10
  item 11) in italics, lower-case, no closing stop — the segmenter passes it as is; direction: flat, the inventory
  voice, a full pause after. Rooke's "They *trust* the seal."; "a wave breaking" (lane B's kept pair). s5 Lira's Ash
  fighter: "Nought to two." / "Two to one. Two to three on the bout." / "Three to one. Five to four." / "Eight to
  four."; Karis's Rune Path fighter "Eight to one". Fine.
- ch32: Brom's first ("It's an old edition."), the hill fighter (five exchanges; Rooke's "Nobody stands still.
  Walk."; "Nine to seven"; "twenty-four, the hill fighter twenty-three"); Ephram's coast Blade ("Nine to five"; the
  coast coach's nod; Ephram's ears at the handshake = lane B's kept one; Rooke's quarter-hour; "*Two points for a
  stride. Karis read it. Cheap.*"). The filings: "*Doctrinal interest.*" / "*The crowd.*"; Karis's bank; Withrow's
  "File it"; Rooke's council ("Four days to the first and seven to the second." — superseded by ch33's deferral, as
  the arc read rules); Seln's "Scheduling is opinion." and Brom's "Mm," in Seln's voice. The trial rule: "*Squads
  shall be drawn from the academy's roster.*" / "*Again.*" (item 12) exact; "Twice is starting to look like a door
  somebody built on purpose. A note for after Norhold." exact. The court: "*NO BOOK ON THE DEMONSTRATION BOUTS.*",
  "*THE FIVE: GONE*" (sentence case); Brom's "And when the theater and the mechanism are the same thing?" exact.
  **POV Havel s7** (the attendance sheet, "*held*") — mark both `---`. s8 seat twelve ("sigil" = SIJ-il). Fine.
- ch33: Hesk's clock "an hour fast"; Lira's quarterfinal "Ten to three"; "Eleven minutes," (canon). The deferral
  notice in italics with "*deferred*"; Brom's "You said four days, Rooke." / Seln's "The tower has changed its
  opinion." (the ch32 figure killed, as the arc read rules). The back room (the table that rocks, the pump): Lira's
  "*stop*" (inner-italic inside narration); "She doesn't gather"; "Ten exchanges" (lane B's move, both). Ephram's
  lake Shield: "One to three" / "Three to five on the bout" / "Four to eight" / "Six to eleven"; "Paid in full. I'd
  like a receipt." The second evening: "*Behind.*" on her hand; "I'll go and live in it. I've lived there before." =
  LIV. Fine.
- ch34: Karis's columns; Ivenne's paragraph in the russet file read aloud in italics; "Standardization is legibility"
  (Book 3's line); "And the reason it's blank—" / "Say it," (ll.67–69, an interruption pair); "The reason it's out of
  date is you." (protected) exact; "*Unknown.*" Rooke's speech with a narrated mid-sentence dash ("—is her shape.",
  l.103): one voice across the dash. Ephram "scarlet to the roots of his hair" (a varied sign, not ears). Rhagen on
  the open floor; Brom's "They're peer-reviewing." Supper: "You beat me the times you made me play yours. Don't play
  hers." exact; Karis's page "*These five like to see a thing finished…*"; Ephram reads "*Every structure is its
  gaps.*" Zerin's file "seven pages… the first six… The seventh" (lane B's move); "*No season wasted.*"; "It's an
  *audit* of the other road."; "I'm fighting the version of me they were supposed to build." exact. The chart on the
  stair: "Behind." Fine.
- ch35: the fight morning; "*Bluff! Bluff!*" (a child's shout); "as a buyer looks at a horse" (lane B's kept half).
  The semifinal: "Nought to three," / Ephram's calls "North." "West." / "Two to one, at the bell. Two to four on the
  bout." / "One to two… Three to six" / "One to three," … "Four to nine on the bout."; Rooke's three fingers; the
  shoulder is the LEFT ("the shoulder she led her bursts with"); figures 29 / 27, "Twenty-nine was a Silver figure."
  Fine.
- ch36: Brom's semifinal, the buried Copper: "Second time's the real rating," (canon); "Then you're rated."; figures
  24 / 23; "Somebody ought to file for her." Rooke reads the exchanges "Naught-three, two-one, one-two, one-three."
  (BOOK_MAP §8's spelling; the narration elsewhere has "Nought" ×4 — ear-identical, NAWT, no audio effect; for the
  ledger only). "Best loss I've coached in twenty years. Eat something." exact; Withrow's "*Semifinalist. Continental.
  Noted twice.*"; "He'll find every gap. Plan to have fewer." (item 42) exact. The boards: "*ZERIN — AUREMONT — 9.
  LIRA — HALCENVANE — 4.*" = the points (read "nine" / "four"; sentence case). Zerin: "Fenmark threw you away?" /
  "Their ledger said Copper." / "Their ledger is garbage." … "Silver bracket, next cycle. Be there." (item 41) exact.
  The hearth: "the way Brom had sat down next to him once" (protected pattern); "I used to want them to admit what I
  already was." … "Now I want to become something they haven't seen yet." … "It's a better want. It costs more." exact.
  Karis on the stair: "The file is accurate." / "The file is *finished*," … "You're not." (item 43) exact; the burned
  plan; "Ternhall's file will fight the woman who left. Halcenvane sends the one who arrived." exact. Fine.
- ch37: the broadside read by Ephram "in the voice of a town crier with a cold"; the figures already spelled for the
  ear ("*nought to three, two to one, one to two, one to three*"); the last line in quotes with italics. Brom's
  "honestly, as he considered everything" (the kept first). The Copper final on the main floor: the seam and the oak;
  "One to nothing." … "One to three, closed early." / "Nought to one. One to one." / "Two to two." / "Three to two,
  closed early. Four to five on the bout." / "Three to one, closed early. Seven to six." / "Three to nothing," …
  "Ten to six on the bout."; "*Every structure is its gaps.*"; "like a door slammed by the wind" (weather). **POV
  Umber s5** (the screen; "the big one" / "the small one") — mark both `---`. s6 the rail: Marek's "*I read it as
  your mistake.*" inside Brom's speech; figures 25 / 25; "Brom. You're continental champion." / "Am I," … "So I
  am." Fine.
- ch38: **POV Ilsev s1** (the validation form in italics: "*Bracket: Copper. Result: title. Practitioner: Brom,
  Halcenvane, Iron Skin. Registry tier at entry: Copper. Figure: 25.*" — "Figure: twenty-five"; "squared the form";
  her pending referral) — mark the `---`. s2 Ternhall in a body (their chancellor, unnamed); Karis's "No. Thank you.
  But no."; "*former partners*". The bout: "Nought to one." … "Nought to three, closed early."; "*Flawless.*";
  Ivenne's paragraph recalled in italics; "One to nothing." … "Three to one, closed early. Three to four on the
  bout." / "One to three, closed early. Four to seven." / "Three to one, closed early. Seven to eight on the bout." /
  "Ten to nine."; figures 25 / 24. The verdicts, each tagged (Rooke, Brom, Lira, Ephram, Cael); "It can't be
  scouted because it wasn't decided." (protected) exact; "*in her.*" on her palm. Fine.
- ch39: the clerk's "Continental Copper. Brom. Halcenvane."; the registry notice; Karis's "*Pending. Not a gift. A
  summons.*"; Brom's "Good. I'll bring the plaque." The Velmere letter: "*Grandmother watched the lists for your
  name. She found it.*" (item 42) exact, "Noted," said Brom exact. Withrow: "*we taught her none of that.*" /
  "They taught her all the parts. We taught her they were parts." exact. The boards: Ivenne and Karis (item 43:
  "Ternhall's file on you is the best document I've ever worked from." … "It was perfect through the first exchange."
  / "I know," said Karis. "I wrote most of it." … "Whatever you transferred for," … "Did you find it?" / "Yes.")
  exact. Karis's two entries (the bill; "*Finding*": "Today was the first day I understood what it costs him that
  nobody can study him back." exact). The lattice-breaker (unnamed): "Two to one." … "Nought to three, closed early.
  Five to nine."; "He bowed to her a little" = BAUD; figures 27 / 23; "Wait for her at the next cycle." Rooke's sheet
  line (protected: "We've now lost to their third-best and their fourth-best, honorably, by margins. The team trial
  seeds us against the whole set at once.") exact; "I sent four of you onto three floors this week and I've got four
  of you back." The ring going up; Lira in the heat-wrap over her coat. Fine.
- ch40: the ring: "Fifty-two north to south, a few feet less across. Crowned… Bays at both gates, a yard deep" (lane
  B's "a yard"); "*Four bursts, probably. Stone.*" Rooke's session: the four cards in his capitals (*ONE. IT COVERS
  GROUND. NOT A MAN.* …; sentence case at render, "One." … "Four." as a list); "*No answer recorded.*"; the pocket
  tap; "If the bout comes down to four — you lose the bout. In-band. On flags. And we go to dinner." (protected
  pattern; the spaced dash a pause) / "I lose the bout," said Cael. "And we go to dinner." Lira's "It's called having
  a house." The main floor: the captain (unnamed) bows (BAU/BAUD); the referee's rules; "Touch," said the referee.
  "Nought to one."; "like rain on a roof" and "stones into a lake" (lane B's single uses); "Silver is not a bigger
  Iron" (canon). Fine.
- ch41: the relocations ("Four. Five. Six." … "The eleventh"); "*Two,* he thought. *Wide costs him.*"; "Touch," said
  the referee. "One to one."; Lira's "Eleven," and Rooke's "Watch the crown."; the two unscripted moves (the turn,
  the drop) and the two contacts; "One to one," at the bell; Gault's "The flexor. Not torn. Pulled."; the uphill
  burst; "Touch," said the referee, "and the bout. Two to one." The captain's finding (§10 item 44: "We found the
  edges of what you showed us. We could not find the edges of you. Rhagen distinguishes between those findings.")
  exact; figures 30 / 27; Rooke's "We're going to dinner anyway." The back room: Lira's "A handspan"; Brom's long nod
  (lane B's restoration reads clean); Karis's "The doctrine isn't failing. The doctrine is *filling*." (protected)
  exact; "Minuted," said Cael. Log item 22 (the pivot) exact. Fine.
- ch42: the keeper (he) on the stair; the broadside's last paragraph in italics; Gault's "Four days." The frame's
  empty lines; Karis's "Nobody below Gold." Rooke's session: Gault's line "*Walk. No run. No burst. No fire until the
  fourth day.*" and "*THE CROWD*"; Ephram as the lake man ("*and now! the blade descends!*" — a stage voice, italic
  inside narration); Karis on the windows; item two. The fourteenth day: the twelfth chair filled; "The Archmarshal
  Vastin had come to Norhold". The bout: the bows; "Touch," said the referee. "One to nought." / "One to one." /
  "and the bout. Two to one."; "He's better than the woodcuts," (canon) and the chalk "*HE'S BETTER THAN THE
  WOODCUTS.*" (sentence case); figures 28 / 25. Fine.
- ch43: **POV Vastin s1–s2** (the post road; the row's report line "*Subject's footwork in the third exchange not
  previously recorded.*"; the steward's "This way, Archmarshal"; his two book lines in italics; "*Mitigation.
  Containment. Trajectory.*"; "He did not know what the boy was… It was only the place where the findings stopped.")
  — mark the `---` into s3. s3 supper: Seln's "The office notes that the chair was held for him for thirteen days
  before he sat in it" (protected) exact; "Somebody announced it for him."; Log "I'd wager he signed it with his
  whole name"; "I'm seventeen in about two hours." s4 the rest day: Lira's note "*Blue door… — L.*" (the letter L);
  the hiring board in italics; the brass plate; the queue of thirty-one; the fiddler's four bars (the colour-guard's
  march). Fine.
- ch44: **POV Seln s1** (the pouch; "*Stationery, bound, one.*"; the plain brown coat; the counter) — mark the `---`;
  s2 opens "an hour earlier" (the proprietor, unnamed; "I opened the door at ten" is lane B's move): a step back in
  time at the break — direction item. "*TAKEN. HALCENVANE. ASK THE GIRL WITH ONE ARM.*" (sentence case). Brom's "I sit
  down, and I look like I'm going to be here a while." Ephram's lock gates: "made to wind a gate himself" and "not be
  allowed to wind anything else today" = WYND (the verb; the only two in the book); the lock-house page with "*late*".
  Seln moved to the bench by the mussels; "Four of them knew both his ledgers…" The game: Karis's "*Things adults say
  that the paper does not support.*" / "*This won't hurt.*" / "*It did. The healer said afterward that it would.*";
  Seln's "nine days by coach" (lane B's move) and "no *I* in it" (the letter, as a word). The post: Quenna's card
  "— Q." (the letter Q); Vell's "*Should the tournament's books ever go missing, ours will not.*"; Hesk's "*Seventeen.
  My trade says an instrument is finished when it measures true — not when it looks done. You measure true. Let the
  rest of them look. — H.*" (item 45) exact; Karis's "He's left you a margin."; Seln's "That is the first one it has
  been sorry to hand over." (protected) exact; "Three people had decided that the day mattered" (B4 echo). Fine.
- ch45: the old volume's four lines; Hesk's book's first page (the inventory in italics; "*Still open. Still real.
  Patience.*" item 24 exact; "as I do at every opening and every closing"). The draw: "Halcenvane," said the marshal …
  "Auremont."; the board "HALCENVANE — AUREMONT." (caps, dash a pause); the Ternhall cup; "*NO BOOK ON THE
  DEMONSTRATION BOUTS.*"; the criers' "No price on the fifth man of the bluff!"; Karis's page ("*Squads shall be drawn
  from the academy's roster.*" … "*Again.*"); "You're on the roster," she said. "The clause does the rest. Again."
  (item 33) exact; Withrow's slip and "It's a list."; Log item 23 exact (with its spaced dash). Rooke's five sheets
  ("I've no plan for her."; "We win the places she isn't."). **POV Umber s4** (the trial clerk; the rule read aloud
  in quotes with italics; "There's only a list."; "Approve it before somebody makes me invent something." — protected
  pattern "i would like the room…" is ch57; this one is canon) — mark the `---`; the section hands off to Cael's
  table WITHOUT a break at l.203 "Bracken collected the notice himself…" — mark the paragraph. Bracken's "slept like
  a quarry stone… That's twice since the bluff."; "HALCENVANE — SQUAD AS FILED." and "*NONE*" (sentence case). The
  walk: Lira's "Fast north, slow south"; Brom's "Two gaps"; Cael's "*The diagonal. Corner to corner, unbroken…*" /
  "*The feature nobody has priced.*" Fine.
- ch46: the fifth name; Rooke's four sentences; the presentation. First exchange: "North."; the words "*Left. Back.
  Two coming. Gap.*"; Lira's "Early." Second: Karis walks her frame; "*South.*" (Ephram, italic in quotes: a call).
  **POV Ilsev s4** (the ten-column form; "*Authorizing office: not traced.*"; "her pen stopped") — mark both `---`.
  s5 the lane: "a smell like a struck flint" (motif); "*We built a house on this floor…*" (inner); "*Don't know.*";
  "His ears popped" (literal); the one second ("She was reading him."). s6 the fourth: Zerin's "*unknown cost, go
  round.*"; "Two exchanges to Halcenvane. Two to Auremont." s7 the tunnel: Rooke's "The third goes in the file as
  weather."; the five sheet lines in italics ("*Ready. Not early.*", "*Left the gap. Should have left it sooner.*",
  "*A frame with a door in it,*" / "*She came from where no ramp was. Think about that.*", "*South.*", "*The
  diagonal. I had it on paper this morning and didn't know what it was.*"). s8 Ephram at the pump: "I'm done waiting.
  Whatever you are, I'm glad it's on my side of the floor." (item 46) exact; "It had four more sentences and Lira cut
  them." (protected) exact. Log item 25 exact ("Gold Rank 3" = "Gold Rank three"); the margin "*Half.*"; Lira's
  "Then your storm." Fine.
- ch47: the other semifinal; the new last page "*Survived Daeva's lane at trial speed.*"; Karis's "It shuts the
  frame." The frame and the register's steward (unnamed). Rooke's one-line drills; "You're the man who sells the
  ticket. You're not the turnstile."; "A thing you've only written down is a thing you've found too late." The
  eastern Silver's unfiled form; "That's the whole category's problem, standing at a board in a wet coat." (protected)
  exact. The rain and the two hundred; "WHO FIGHTS THE ENROLLEE?" (sentence case); the price on "*no further filing
  at this sitting*"; the fishwife's "somebody's got to come *down*." The hall: "Now," he said; Karis's "Read what she
  leaves behind."; "Two days." / "it fills from above, or it dies." Fine.
- ch48: the warm-up hall going quiet; Brom's "That's a filing."; Seln's "The office's copy"; the form: "*Gold*",
  "*Three*", "*Overdue.*" (item 13) exact; "Mm," said Seln. Bracken's three difficulties ("*a division by a blank*").
  The broadside column in italics. The board: "CAEL — HALCENVANE — [UNCLASSIFIED] vs. DAEVA — AUREMONT — GOLD 3."
  (item 14; not italic; brackets never voiced; "vs." = "versus"; "GOLD 3" = "Gold three"; sentence case at render);
  "*filed; acceptance pending*"; the narration's "the little *vs.*" (say "versus"); "They finally wrote it down the
  honest way," he said. "A blank, with my name next to it." (item 48) exact. The long table: Withrow down the form;
  Seln's "The adjudication office has requested three additional recording scribes for finals day." (item 48) exact;
  "Mm,". The back room: Brom's "Attention you can read. Traffic you can't."; Karis's "*publication*"; Lira's case
  against and her own side; "I'll accept in the morning." / "I was always going to. Tonight was for making sure I know
  why." (protected) exact; Karis's "*Decided in the back room, the night before. All four.*" Fine.
- ch49: **POV Daeva, the whole chapter** ("she" = Daeva from the first line; mark it at the chapter head). The
  warehouse chart in italics ("*Phase one: assessment,*" …; "*Opponent insufficient for profile. Revise upward.*");
  her lead instructor (LEED; unnamed). Zerin at the bench ("I went round him." / "Good."). The pressure hour ("struck
  flint"); "the half-second he had been early". The file: "Nine pages in grey board" (lane B's move); "*peculiar
  timing*". The window "set in lead" = LED. Lane B's re-ordered window reads in sequence: the lining; the exercise
  sheet "*Corrective: lane integrity under counter-slackening*" and "*The exercise worked. That was the trouble.*";
  the registry page ("The top line was the newest… Below it, because the page was kept from the bottom up…"; the first
  line = the Kindling); "It was the garden." as the hinge into the memory; "Am I early," she said, "or are you late?"
  (canon; thirteen, a garden court, §10 item 60); "*Specimen.*" (canon); "It had been four years since the coast."
  Then "She went back to the glass, and to the trial." (lane B's join) — clean. The form: "*Gold*", "*Three*",
  "*Overdue.*"; the steward's hands. Breakfast: Zerin's "Good." The risk officer (unnamed; the four dead on the coast
  stated without gore); "You haven't brought me an objection. You've brought me a list." The office: the eager young
  man's "Seven years," he said, sitting forward. "Seven years of—" (l.253, cut off: short gap); the counsel reads
  "*Withdrawal of a filing,*" … "*By the filing party only.*"; "Then the objection is noted," in the program's phrase.
  "the first decision of her entire career that nobody had scheduled for her" (protected) exact. Fine.
- ch50: the clerk's three pens; "*Accepted in person. Bout entered for finals day…*"; "*Accepted.*" on the board. The
  hearing: the four items "*1. The parties. 2. Underwriting. 3. Protocols and the ring. 4. The rating.*" (read "One.
  The parties…"); "Confirmed," ×2; the counsel's "*unpriceable but bounded*"; Umber's third item (the ring: six feet,
  four breaks, four masts); his fourth: "The category was made to judge a performance where the brackets cannot. It has
  waited three hundred years for a bout that requires it. We will not refuse the one it was built for. The panel will
  rate what is demonstrated. The tables will hold, or we will learn something about the tables." (item 47) exact;
  "No," said Umber. **POV Vastin s3** (nineteen years in his room; the four silences; the requisition "*Official
  interest.*", "*Accommodation: own account.*", "*Traveller: one.*"; his two Norhold notes recalled; the italic thought
  — item 49 — exact) — mark both `---`. s4 the squall on the harbour wall: "the way a bow-wave runs ahead of a barge"
  = BAU; the masts hum; "Now," he said; Lira's "I asked you three times."; the Log line. Fine.
- ch51: the hill ("Sixty-one paces"; "the ten paces at its middle", lane B's move); Cael's "We price the way down."
  Rooke's brief ("Five-as-one-argument."); the bedsheets "HALCENVANE" (sentence case). First exchange: Ephram's
  "South's theirs." / "Ridge is ours. West crossing. Lira, Brom, go." Second: the Wind's three lessons; Karis's taxes;
  Cael's words "*West, old. Crown, slow.*" / "*Show him something.*"; Marek over the saddle; Karis's catch; "THE
  ARGUMENT AND THE TABLE." (sentence case); the scribe's three names. Third and fourth: "*West, old*", "*Crown, two,
  wait*", "*South, now.*" Rooke: "You were the only one that's a household." (protected) exact. Marek at the boards:
  "*One point,*" Brom read aloud, slowly. "*Everything goes through the fifth man.*" (a voice reading); "Tell him
  Rhagen's floor will be watching for the fight, not the theater." (protected) exact. The standings: the house with no
  line; "one of the colour-guard at either side"; "Halcenvane was twelfth to be read." (lane B's cut sits clean);
  "Third of fourteen, as the count stands at the close of the trials. To be confirmed at the closing." The scribe's
  note (item 15), lower-case italic, exact. Fine.
- ch52: the party (the keeper's "A cheese I was saving for nobody in particular."; Gault's ribbon; Bracken and Seln
  at the window; the lock-keeper's song, "forty verses… taught eleven of them" — canon; Karis dances). Withrow's
  toast: "Third on the continent, by the instrument's own arithmetic." … "Whatever else happens on finals day — they
  counted us. Remember when they wouldn't." (item 50) exact, the spaced dash a pause. Lira on the stair: "Whatever
  happens in that ring, you come back to this table." (protected) exact. The ring built: "*one-two*"; "*Bull-nose*";
  Log item 26 exact. The hall: "ten in ten"; Karis's "That's your half."; Brom's "Then I'll stamp." **The ring walk
  (s5)**: Cael and Daeva alone, two voices; every line placed — the short alternations (ll.173–175, 181–183,
  207–209, 213–215, 239–241) are carried by the action beats inside the lines ("A sideways look", "She stepped back",
  "He looked along the barrier", "She said it flatly") and by content ("I" = Cael on the top/oak; "my program" =
  Daeva); no untagged run longer than two lines. Direction: Daeva level, exact and unhurried; Cael plain. Item 51
  exact ("They measure you and get nothing…" / "Neither number is us," said Cael. / "*Neither number is us.*
  Nineteen years…" / "Don't hold anything back that matters. I'll know, and it will insult us both."); "I'll have
  changed it by the day after tomorrow." Log item 27 exact ("Gold Rank 3" = "three"). "She's the mirror," he said.
  "All the way down." (protected) exact. Fine.
- Recheck after the lanes (grep over all 60): no English weekday; "spring" ×7 = the oak's spring (ch14, 19, 20);
  "march" ×4 = the colour-guard's tune (ch31, ch43); the only month names are Book 4's dated recollections (Sowing
  ch4; Reaping ch2, 13, 33, 58); no metric word. The arc read's ch49 "Tuesday calibration" is no longer in the text.
- ch53: **POV Seln s1** (the five folders; "his own pen-case" — four pen-case mentions, the coordinator's fix, all
  smooth; the strip cut against a steel rule; the nobody's hand; the slip in italics = §10 item 52 exact; "squared
  the row") — mark the `---`. s2 Rooke with the pads: "There were a dozen more in that." (lane B's move) / "I'd
  thought I'd mind not knowing what it is. I find I don't." s3 the back room: "The tenth thing… under nine others"
  (lane B); the sheet "*We don't know.*"; the door's lines "*A pipe. Dead. Brom: she turned.*" / "*Most of an
  hour.*"; Lira's "My hair didn't move."; Cael's "Fold. Lane. Her. She arrives third."; "*she arrives third*" with
  "*trial, read live*" (LYV) small in the corner; "the way a crowd steps aside for a steward with a staff"
  (deliberate repeat); "*Permitted.*"; "Half a beat," said Cael. "Then we're rich."; Karis's card "*Air first. Not
  her. The leave runs out where the lane does. Half a beat and it's yours.*" burned on the coals. Brom: "You've never
  fought anyone where survival was the win condition." … "Score is for the judges." (item 52) exact; "Going down well
  is a skill". Lira: "The person who walks onto that floor has to still be you." exact. The business: Karis argues
  the other side; the bank named ("Ceilings, not rates."); "A rate you have shown is a rate you have shown forever.";
  the minute in italics; "The quiet thing stays sealed." / "Because of who it came from." s4 the strip found at
  midnight; the ash already broken; "There had been one before. Now there were two."; the old volume's last leaves.
  s5 the house lying still (the keeper counts to five); the clock "wound it" = WOWND; Log item 28 exact in all four
  parts ("Quenna asked if I could not-do it…" / "Tomorrow's question…" / "*I don't think I can.*" / "*Write it down
  before, not after.*"). Fine.
- ch54: the clock put back; the keeper's cap; Brom's loaf; the queue; the second betting board ("the figure"); the
  broadsides' "*the exhibition*"; the card heard through the ceiling; Ephram's "They kept her in a box all morning.";
  the twelfth chair filled again; Umber walks the ring and tests it with his foot; Rooke's three minutes ("Chart
  her."; "Frightened is expensive and it isn't information."); Brom's "Survive the first one."; Seln's folder with
  nothing extra; "Thank you for the forms." The reading: "Daeva. Auremont Academy. Storm Path. Gold, Rank Three." /
  "Unclassified." (the Ardenmere courtesy); the protocols twice; the walk; "Terms hold?" / "Terms hold," said Cael
  (item 53) exact. First exchange: the west barrier; "the first" burst; the wash into the give ("in the book"); the
  push "One blow of the four."; the cap seam; the bell; Brom's one finger — "One. Survived." Fine.
- ch55: Gault's "One of four?" / "One."; Lira's "Put her down." (as her "*Early*"). Second exchange: the fold; "*The
  leave runs out where the lane does.*"; the fourth burst; the spark at contact; "Seven of nine."; "Touch," said the
  referee. "One to nought."; "Nobody had scored on Daeva in four years." (protected) exact; her face ("a child who
  has been given a present" = PREZ-ent). Third: two folds, three; the lane that bent; "*She has never shown that to
  anybody.*" / "*Where is she?*"; the empty lane and the fire down the left side; "Four of nine." / "No touch," said
  the referee. / "Your hand,"; the healers up and down; Rooke's palm over the cap; "a fifth of a beat". The break: the
  inventory in italics, no pen ("*Wind: seven gone…*" … "*The floor: true.*"); "*Not now.*" Fine.
- ch56: the oak; "as a woman sowing a field throws seed" (SOH-ing, the verb); the Wind lost ("a tenth… the hip simply
  said no"), the give, the push ("the fifth, past the four and into the minute"), the spark; driven north. The three
  rules in italics ("*One. The conditions are not to be made.*" / "*Two. A reach only inside a fight the other
  begins, in earnest, awake, and on purpose.*" / "*Three. The whole cost on paper first.*"); "the quiet thing… stayed
  sealed." "Karis said afterwards that it was the worst moment of her life." (the kept superlative); Rooke's hand;
  "as you hold still in front of a bird so that it will stay" (manner). The lane of his own ("fifteen feet long…
  a third as deep"); "like a flint struck once"; the mast flares. Lane B's two seen moments: the crier "*and the boy
  —*" (a cut-off inside italics: short gap, no falling cadence) and "ten seconds by a carter's count" (lane B's
  move); the ledgers face down; "*he hasn't got that.*"; nine still pens; Havel standing. The stumble ("Chin in. Arms
  in. Loose."); the air thickening; "Stoppage." / "Stoppage. Daeva."; the healers ("What day is it?" / "Finals
  day."); the five at the rail. **The notice** (ll.193–200), the book's one code block, §10 verbatim: fpaudio strips
  the fence and gives each line a stop — read as a notice, each line its own beat, "[unnamed]" with the brackets
  silent, the spaced dashes pauses; its own segment and a long pause (direction). "Seven, now. And two firsts. No
  notice before this one had ever said *Gold*." Item 54 exact ("That was mine," she said. / "A piece of it," said
  Cael. / "Nineteen years," she said. "Nobody has ever shown me something I couldn't name." / "Find out what you
  are. Then find me. I want the rematch with whatever that is."); Rooke's "That's the whole education, right there.
  Not the lane. The mercy, on a clock." exact; "*Before the figure*, Cael thought. *Again.*" Fine.
- ch57: **POV Daeva s1** (the healer's "Four years,"; the lane that was hers; "never in her life been so happy about
  anything she did not understand" — the kept superlative; the two ways to use the slackened air; "*Today somebody
  asked me something.*") — mark the `---`. **POV Umber s2–s5** (lane B's heard moments, all tagged: the handcart;
  "The short sheets will do," said the oldest of the panel / "Very likely," said the rating clerk… "I would like the
  room to be able to say that we looked." (protected) exact / "Nine," said the elder of them / "Will the eighty-first
  serve?" / "I found only one of them."; the rating clerk is a woman ("She had worked…", "she had stood up with the
  first volume"); the observation-right man "who spoke no word" and the minute line in italics; the ordinary thing
  tried; "The column asks me for his tier."; the three arguments reported and quoted, tagged; the ruling; "*The Chief
  Adjudicator paused.*"; "It was built for a world with a schedule in it… The record is the truth or it is nothing.
  Write the entry." (item 55) exact; the words tried in italics (*Unassessed*, *Rating withheld*, *beyond the scale*,
  *by*, *under*, *Referred*); the look between the two men; the entry read to the room: "*Result: stoppage, Daeva,
  fourth exchange. Performance rating: unscorable under standard. Referred.*" (item 16; eleven words) exact) — mark the
  `---` into s6. s6 Cael: the frame; "*Under*," she said, at last. "Not *by*." (stress); the copy line and Auremont in
  it; the six guesses; "*our fighter does not mis-seed.*" (item 55, lower-case italic) exact; "Nobody guesses
  digestion." Fine.
- ch58: **POV Ilsev s1** (the file; "*Under*, not *by*"; the return "*Referral closed at registry level; no further
  inquiry authorized.*" item 17 exact; her girlhood hand; her private sheet) and **POV Havel s2** (the fifth sheet) —
  mark both `---`. s3 Withrow's note (the half-sheet in italics; "that sentence is not a formality"); the circle's
  argument (Karis, Lira, Brom's one line, Ephram "not of the circle and knew it"); Cael's "I want to know what's worth
  that much to him."; Seln's "Listen accordingly." **POV Seln s4** (the report in italics; the last word not written;
  "The locked case… apart from the pen-case beside it. He had not opened it." — the coordinator's clause reads clean).
  s5 the hour: every line placed (Vastin tagged on his long speeches; Cael's three untagged questions fall to him by
  sense); the eight words in italics, "*containment.*" lower and quieter; "You should stop competing publicly." / Cael
  asked why. / "Because the people who want this to stop are not going to use official channels much longer." (item 56)
  exact; "If I gave you names I would be guessing, and I don't guess." exact; "I won't answer that one," said Vastin;
  "The method is not a boy's."; "No. I evaluated you." … "But you'll know when the channel changes, now. Knowing is
  worth something. It's the only thing I had to give." exact; the card "*Slow. Owner informed.*"; Brom's "Fifty-one
  minutes." Fine.
- ch59: **POV Vastin s1** (the copy line; the eleven words; the summons; "a room in the drawing he had never seen") —
  mark the `---`. s2 the rail: Log item 29 exact ("three years"; "feel like a wound" = WOOND). s3 the long table: Lira's
  "Karis would tear it to pieces" = TAIR; Ephram "As a report it's thin"; Brom's "Grade the man."; Karis's "grade it
  both ways"; Seln's "Wardens threaten. Politicians hint. That was neither." … "Treat the warning as real, because it
  is." (item 56) exact; Lira's "Same build." and Karis's box; "Fifty-one minutes," she said (Lira, the Arbiter). s4 the
  back room: the costed rule in italics (item 32; the map's "the conditions" is here "The conditions" — case only);
  four initials; "Now it's the house's."; Log item 30 exact. s5 the closing: the eight claps; "Fourth," read the
  official. "The Rhagen Institute." / "Third. Halcenvane Academy."; Lira's "Eighteen years they didn't come." … "what
  the scrapyard placed."; the banner "two of them, one at either side. As on the first day, no house walked behind it."
  (lane B's join, clean); the four ties; the two registrars. **POV Daeva s6** ("Rematch," she said — item 57 exact;
  "Four seconds."; the citation into the lining) — mark the `---`. Fine.
- ch60: the year closed in Hesk's book (the leaf list with "the pole"; "four years of trying to trim it"; "Daeva's
  storm… Fifteen feet of it, a third deep."; "*Still open. Still real. Patience.*" item 24; "*Reydan will read the
  accounts. It still isn't the answer. Not yet.*" item 31 exact). The letters: Hesk's six pages ("*I still don't know
  what I am…*"); Vell's ("*Your ledger rated me before any of theirs could. It's still the one I check the others
  against.*" item 57 exact). Brom's "The recess's problem." (#37 O5) exact. The harbour wall: "Four flags and an
  exchange."; "Silver bracket. Next cycle." The road: Seln on the bench; the manifest "*records and floor
  scheduling*"; "Eleven," said Seln (the joke kept at eleven). The convening: "*Whether the classification [SHATTERED]
  shall be designated an active threat category.*" (item 18; brackets silent); Vastin's testimony (item 58) exact;
  "Suppression-Advisory Watch, Priority Level 4" ("Level four"); "a flag no living hand had authorized"; "*entered for
  formal proceedings*". "a dozen of them now" (lane B's move); "*The flag stands.*"; Brom's summons ("ninety days"; "It
  isn't a promotion. It's a hearing about whether I get offered one." — protected) exact; Hesk's letter (item 57, "— H.")
  exact; the watchers ("They may be the last watchers I get whose names I could learn." — protected) exact; Karis's
  "Two hundred and six sheets"; the ferry: the Fiske line in lane B's Silver-bracket form; the close (item 59) exact,
  the closing paragraph in italics with its spaced dash. Hesk and Fiske in one paragraph (HESK / FISK; the context
  separates them). Fine.

## Running tally
Required: none. Optional (1): ch49 "set in lead" → "leaded glass" (the book's single LED against ten LEEDs; an
engine's default is the wrong way; Book 4 left its window-leads to the lexicon, Book 1 fixed its "wound"s). Renderer,
not text: the brackets (ch48, 56, 60), the one fence, "vs." as "versus", the all-caps boards and signs in sentence
case, the decimals as "six six", the ch31 attestation's missing stop, "Mm." / "Hm." / "Huh." in the render, the
italic documents and the POV cutaways marked per segment (one in-section hand-off, ch45 s4; one step back in time,
ch44 s2). Lexicon, not fixes: Gault's aw beside "Gold" (10 scenes); Daeva's DAY-va beside KAYL (14); Rhagen's RAH-gen
beside Reydan (2) and Rooke (27); Umber's U (never beside "Ember"); Hesk/Fiske one sentence apart (ch60); the
homographs above. For the ledger: "Naught-three" (ch36) beside "nought" ×15; "theater" ×2, "favorite", "honorably"
inside protected lines; §10 item 32's "The conditions" for the map's "the conditions"; the arc read's ch49 "Tuesday"
no longer in the text.
