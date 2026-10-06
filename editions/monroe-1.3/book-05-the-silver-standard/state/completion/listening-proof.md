# Book 5 — *The Silver Standard*: line and listening proof (Step 4)

Reader: Claude Fable 5.1, review seat, fresh context, standing in for Sol, 2026-10-06. Scope: `manuscript/chapter-01.md` …
`chapter-60.md` (296,931 words by `wc`), read in order as a Breeze narrator will meet them: one segment per paragraph,
`---` as a long pause, italics flattened, the one fenced notice flattened line by line. Read first: Book 1's, Book 3's and
Book 4's `listening-proof.md` (the models; Book 4's `listening-notes.md` as the model for the notes), `COMPLETION-PLAN.md`,
`whole-arc-read.md` (§8 fixes applied), `PASS-BRIEF.md`, `LANE-A-REPORT.md`, `LANE-B-REPORT.md`, `EDITION_BRIEF.md`
(audio-first, Reader Standard), `OWNER-DECISIONS.md` #3, #11, #33, #35–#42, `BOOK_MAP.md` §10 and §13,
`protected-patterns.txt`, and `audio/fpaudio.py`. Two scripts swept all 60 files first (quote and asterisk parity, break
spacing, fences, brackets, lower-case starts, paragraph ends, doubled words, slashes, numerals, abbreviations, all-caps,
spaced dashes, cut-offs, name pairs per scene, homograph contexts, every ", as" clause and bare "as", the 52 protected
patterns, paragraph lengths); the read then went through every chapter, with the lanes' joins and the scenes the prompt
names given extra attention. Running notes: `listening-notes.md`.

**No manuscript file was modified; no git command was run.** Every fix below is a proposal; the one old string was
verified with grep to match exactly once in the manuscript and its new string to occur nowhere. No fix touches a
protected line (BOOK_MAP §10, `protected-patterns.txt`) or the FRAGMENT ACQUIRED notice. Cael = KAYL and Lira = LEER-a
(#33); Bede, Maud, Gwen and Abbot do not occur in Book 5 (#3, #11); no season name, month order or English weekday
appears (#35–#37: the Halcenvane weekdays are First-day … Seventh-day throughout; "spring" is the oak's spring, "march"
the colour-guard's tune; the only month names are Book 4's dated recollections, the eleventh of Sowing and the
fifteenth and twentieth of Reaping); measures are feet, yards, inches, paces, strides, hands and miles.

---

## 1. Verdict

**Render-ready with no required text fix.** Sixty chapters read and swept, and nothing was found that an engine will
voice wrongly or a listener will stumble on: no unbalanced or mismatched quotation, no speaker a listener cannot place,
no broken join, doubled word, lower-case start, mid-clause end, dangling comparison or number changed in one place and
not its echo, no slash, middle dot, ordinal numeral, "0", en-dash range or abbreviation without a spoken form. One
**optional** engine-safety fix is offered (§3B: the book's single "lead" that is the metal, ch49, against ten that are
LEED). The rest is for the renderer and the direction files, not the text:

- Quotation marks: every paragraph in all 60 chapters has an even count of `"` except three, and all three are
  Withrow's "Three numbers" speech in ch1 (ll.157, 159, 161 open and reopen; l.163 "Eighteen." opens and closes) — the
  odd count the lanes noted was there before them and is a correct multi-paragraph quotation, the book's only one. No
  curly quotes. Quote-inside-quote cases use italics (documents, reported speech) or single quotes (ch1 "'Yes.'").
- Italics: every paragraph has an even count of `*`. No `_`, no `**`, no `~~`, no backticks outside the one fence, no
  headings after line 1, no tabs, no trailing or double spaces.
- `---`: every break has a blank line before and after. One fenced block (ch56, the notice; §10 verbatim; byte-identical
  per lane B).
- Attribution: every speech paragraph can be placed by a listener. The scenes the prompt names were each traced line
  by line — the back-room councils (ch33, 41, 48, 53, 58, 59), the boards and the long table (ch30, 36, 45, 48, 59), the
  bouts' corner talk, the ring walk (ch52 s5) and the hour (ch58 s5), and the two-speaker runs the lanes cut tags from
  (ch47, 52, 53) — and all carry by tags, by action beats inside the line, by alternation never longer than two lines,
  or by content (§2.1).
- Ear collisions: Gwen, Selm-, Kestrel, Halvern, Coss, Doss, Marrow, Corbin, Bede, Maud and Abbot do not occur. Umber
  never shares a scene with the word "Ember"; Vell and Velmere never share one; Ivenne and Ilsev never share one. The
  pairs that do share scenes (Bracken/Brom 42, Withrow/Rooke 30, Rhagen/Rooke 27, Marek/Karis 18, Daeva/Cael 14,
  Gault/Gold 10, Ephram/Ember 6, Rhagen/Reydan 2, Hesk/Fiske 1) are distinct by onset, vowel or syllable count and are
  held apart by register (§2.2). No rename is proposed (#6, #11, BOOK_MAP §13).
- Protected lines: all 52 `protected-patterns.txt` lines are present, each once in its mapped chapter (the "things that
  are going to happen" line twice, ch46 and ch48, as mapped); every §10 item was read in place (§2.6).
- The lanes' joins (lane A's one-paragraph merry Blade, the bill-line Logs, the audit, the road sorting, the eleven
  moves; lane B's re-ordered Daeva window, the two seen moments after the lane, the panel night's heard arguments, the
  trial recap, the pen-case, the guard of two, the Fiske line in its Silver-bracket form) were read in place and all
  sit clean.

What remains is for the direction files: the POV cutaways (Vastin, Seln, Havel, Ilsev, Umber, Daeva), two of which hand
off inside a section; the homographs an engine will misread (the one "lead" = LED, the one "wound" = WOOND, the two
"wind" = WYND, "live" = LYV twice, "present" always PREZ-ent, "the read" = REED, "the leave" = LEEV, "the give" = GIV);
the all-caps boards, chalk, woodcut titles and signs in sentence case; the brackets, the fence and the one "vs." (say
"versus"); the single letters and sign-offs; the decimals read aloud ("eight point six six" = "six six"); and the
protected attestation in ch31 that ends without a full stop.

---

## 2. Findings by category

### 2.1 Quotation marks and attribution

- Balanced throughout (3 odd-quote paragraphs, all ch1's Withrow speech; 0 odd-asterisk paragraphs; 0 curly quotes;
  script-checked).
- **Italics carry ten different things**, and the narrator needs to know which: (a) Cael's Log — the old volume, and
  from ch45 Hesk's book — and the observation notebook (day entries, inventories, the costings, the engineered-scatter
  list, the bank minute ch53, the costed rule ch59, the year's close ch60); (b) Karis's grey notebook, her open lines,
  her cards (ch4 the numbered card, ch34 the panel page, ch53 the burned card), the wall and door sheets (ch53), her
  "*Finding*" (ch39), the minute lines; (c) Seln's reports and roster/manifest lines (ch19, 26, 58, 60), his strip
  (ch53 = §10 item 52), the wing's two lines; (d) documents read as text — the clause and the provisions (ch4), the
  certificate sentence (ch2), the memorandum (ch3), the advisory (ch5), the card line (ch5, ch6), the ruling (ch10,
  ch20), the manual's rule and annotation (ch12), the bands table (ch5), the profiles' margins (ch3), the index entries
  (ch19), Rooke's boards and cards (ch3, 4, 14, 20, 25, 40), the deferral notice (ch33), Ivenne's paragraph (ch34),
  Ilsev's form (ch38), the trial rule (ch32, 45), the filings (ch48), the hearing's items (ch50), the forms (ch50), the
  exercise sheet (ch49), the entry (ch57), the return (ch58), Vastin's day-book and requisition lines (ch29, 50), the
  convening's question (ch60); (e) letters and notes with sign-offs — Hesk's five (ch4, 19, 26, 44, 60; "— H."),
  Quenna's (ch44, "— Q."), Vell's (ch44, ch60), the Velmere line (ch39), Withrow's note (ch36), Lira's note (ch43,
  "— L."), Vastin's half-sheet (ch58); (f) chalk, boards, slates and signs (the roster ch1, the cohort board ch14, the
  standings and draw lines ch30, ch36, the betting-row sign, the woodcut titles ch29, Gault's calendar ch2); (g)
  remembered, reported and overheard speech and crowd voices (ch9 "*Quick feet*, said one voice"; ch29 "*The Gold's at
  the back…*"; ch31 "*That's the clause house…*"; ch42 Ephram's stage voice "*and now! the blade descends!*"; ch46 "*he
  hasn't got that*"; ch56 the crier's "*and the boy —*"); (h) inner thought and the counts said inward ("*One.*" …
  "*Four. Of five.*"; "*Hold. First.*"; "*Not now.*"; "*Where is she?*"); (i) the inventory ch55 said without a pen, in
  the Log's voice; (j) word stress ("You've been watching my *hand*."; "The file is *finished*"; "The doctrine is
  *filling*"; "*Under*… Not *by*"). The split is always clear from the surrounding sentence; the direction file should
  say which is which per segment, as Books 1–4 did.
- Read text inside speech: ch4 Cael reads the two provision lines; ch10 Karis reads the ruling (and ch20 the innkeeper
  reads it off his wall "in a ringing voice"); ch12 Cael reads the manual's rule and its annotation; ch23 Karis reads
  the steward's sentence "in the voice she used for charters"; ch30 Karis reads the scoring paragraph; ch34 Cael reads
  Ivenne's paragraph; ch45 Umber reads the trial rule aloud once; ch49 the counsel reads "*Withdrawal of a filing…*";
  ch51 Brom reads Marek's line aloud, slowly; ch57 Umber reads the entry to the room. Direct as a voice reading, flatter
  than its own speech.
- Interruptions: the `—"` cut-offs are few and all deliberate — ch4 Brom's "What—", "So a fighter who can't be
  seeded—" / "—can be fielded." (an interruption pair) and "If it fails—"; ch18 Lira's "And he said—" (her own pause
  before the board-man's line); ch19 "She—" (the withheld name); ch20 "Does that mean—" / "It means we're going"; ch25
  "Lira—" (Lira already gone); ch29 "Was that—"; ch34 "And the reason it's blank—" / "Say it,"; ch49 "Seven years of—".
  They want the engine's short gap and no falling cadence. The steward's stammer "The—the Ember." (ch11) and "The—Blade."
  (ch22) and Rooke's narrated mid-sentence dash in ch34 ("…and from this one's pages—" he tipped his head… "—is her
  shape.") are hesitations inside one speech, not cut-offs: one voice across them.
- Counts said aloud and the score calls: the referees' and stewards' calls are in quotes and flat ("Touch. Halcenvane."
  / "Even." / "Two to one. Bout to Halcenvane." at the meets; "Nought to three," / "Two to one. Two to four on the
  bout." / "Three to nothing, closed early." at Norhold; "Touch," said the referee. "One to nought." / "No touch" in the
  ring); the clerk's "Twenty-four and a third"; Rooke's exchanges "Naught-three, two-one, one-two, one-three." (ch36);
  Brom's spoon; the eight claps (ch59). Keep the deliberate count rhythm.
- The card readings in ch6 (ll.85–111) alternate Rooke (five marks) and Karis (the strike and the average) untagged
  after the first pair; the content carries it. The decimals are read "Eight point six six", "Seven point three three":
  say "six six" / "three three", never "sixty-six".
- "Mm." (Seln: ch2, 4, 14, 20, 32, 48 ×2; Brom in Seln's voice ch32), "Hm." (the foreman ch40), "Huh," (the ganger ch9,
  Lira ch15, ch20): may be dropped or stretched by the engine; check the render. Seln's "Mm" is load-bearing (the
  counter's whole correspondence).
- The two-speaker runs the prompt names, traced: **ch52 s5, the ring walk** (Cael and Daeva alone, 40-odd lines):
  every short alternation (ll.173–175, 181–183, 207–209, 213–215, 239–241) is carried by an action beat inside the line
  ("A sideways look", "She stepped back", "He looked along the barrier", "She said it flatly") or by content ("I" on the
  oak = Cael; "my program" = Daeva); no untagged run exceeds two lines. **ch58 s5, the hour** (Cael and Vastin): every
  question is Cael's and every answer Vastin's; the three untagged lines ("Who sends you the minutes?", "There's talk of
  a sitting.", "And then?") fall to Cael by alternation and by sense. **ch47** (the wharfmen and the fishwife; the hall
  with Lira and Karis) and **ch53** (the four in the back room) are tagged line by line. The boards (ch30, ch45, ch48),
  the long table (ch48, ch59) and the councils (ch32, 41, 48, 53) tag every change of speaker; the bouts' rail talk
  ("said Brom, very low", "said Karis", "said Rooke") is tagged or alternates for one line at most.
- Three attribution notes, none a text defect: ch44 s2 opens "an hour earlier" than s1 (Seln's walk), a step back in
  time at the `---`; ch45 s4 passes from Umber's tower to Cael's breakfast table inside the section at "Bracken collected
  the notice himself…" (l.203); ch57's rating clerk is a woman ("she had stood up with the first volume") — keep her
  colour apart from the junior clerk and the oldest judge.

### 2.2 Ear collisions

**Names in one scene.** A script split each chapter on `---` and counted name pairs per scene:

| Pair | Risk | Scenes together | Note |
|---|---|---|---|
| Gault / Gwen | — | none | Gwen does not occur. GAWLT (as "fault", B4). |
| Seln / Selm- | — | none | SELN, one syllable (B4). |
| Karis / Kestrel | — | none | KAIR-iss (B3). |
| Havel / Halvern | — | none | HAV-el (B2/B3). |
| Umber / Ember | — | none in one scene | UM-ber vs EM-ber, one vowel apart, and Karis is Ember Path; checked separately: Umber (ch5, 30, 31, 37, 45, 50, 54, 57, 60) never shares a scene with the word. Give Umber its U. |
| Vell / Velmere | — | none | both in ch60, different scenes (B3's VELL / VEL-meer). |
| Ivenne / Ilsev | — | none | both in ch38, different scenes. |
| **Bracken / Brom** | low | 42 scenes | the registry's flagged pair, kept (#6): BRACK-en vs BROM; Bracken is "the registrar" and files, Brom speaks (B4's ruling holds). |
| Withrow / Rooke | none | 30 | WITH-roh vs ROOK (as "book"). |
| **Rhagen / Rooke** | low | 27 | RAH-gen (hard g) vs ROOK: different vowel and syllable count; Rhagen is a house, Rooke a man. |
| Marek / Karis | none | 18 | MAR-ek vs KAIR-iss, different onset. |
| **Daeva / Cael** | low | 14 (ch29, 31, 43, 46, 47, 50, 54, 55, 57) | DAY-va vs KAYL share the long A; different onset and two syllables against one; she is "the Gold" or "she" in most narration. Keep Cael one clipped syllable. |
| **Gault / Gold** | low | 10 (ch1 ×2, 36, 38, 42, 48, 54 ×2, 55, 59) | the one pair this book adds: GAWLT (long aw, -lt) against the tier word GOHLD (-ld). Hold Gault's aw wherever "Gold" is in the scene; never GOLT. |
| Ephram / Ember | low | 6 (ch1, 5, 11, 21, 22, 38) | EF-ram vs EM-ber; Ephram speaks, Ember is a Path word. |
| Brom / Bronze | none | 16 | BROM vs BRONZ; the -nz carries it. |
| Rhagen / Reydan | low | 2 (ch41 s2, ch45 s1) | both only in narration ("Reydan's give", "Rhagen's book"): RAH-gen vs RAY-dan — give Rhagen the short a. |
| Hesk / Fiske | low | 1 (ch60 s6) | HESK vs FISK, one sentence apart ("Hesk's book… no letter from Fiske"); the context ("book", "letter", "watched") separates them. |
| Auremont / Ardenmere | none | 7 | AW-re-mont vs AR-den-meer; different vowels. |
| Zerin / Seln; Zerin / Daeva; Ilsev / Lira; Quenna / Karis; Halcenvane / Greyvane; Norhold / Halcenvane | none | 3; 6; 2; 2; 12; 9 | ZERR-in; IL-sev; KWEN-a; HAL-sen-vayn vs GRAY-vayn (B4); NOR-hohld. |

No rename is proposed (decisions #6, #11; BOOK_MAP §13 names none pending).

**Homographs.** All occurrences were read in context; none is ambiguous to a human narrator. The ones an engine is likely
to voice wrongly, with the intended reading:

| Word | Intended | Where |
|---|---|---|
| lead (LEED) | 10 | "lead shoulder" ch22 ×2; "lead him" ch43; "lead instructor" ch49 ×4, ch57, ch59; "lead-in" ch52. |
| lead (LED, the metal) | 1 | ch49 l.95 "a single pane of thick glass set in lead" — the same chapter as four "lead instructor". **Optional fix 1.** |
| wound (WOWND) | 7 | the strap ch6, ch8; "like a cord being wound" ch12; forearms "wound in wet linen" ch38 ×2, ch39; the clock "wound it" ch53. |
| wound (WOOND) | 1 | ch59 l.47 "feel like a wound" (§10 item 29). |
| wind (WYND, the verb) | 2 | ch44 "made to wind a gate himself" and "not be allowed to wind anything else today" (the lock-keeper's gate). Everywhere else "Wind" / "wind" is the Path or the weather, WIND. |
| live (LYV) | 2 | ch37 "find it live"; ch53 "*trial, read live*". LIV elsewhere (ch1, 3, 9, 12, 33, 34). |
| lives | — | LIVZ ch3, 5, 22, 50; LYVZ ch25, 26 ×2, 45, 49, 56, 57. |
| tear / tears | — | TAIR ch12 "tear a strip", ch59 "tear it to pieces"; TEERS ch35. |
| bow / bowed | — | BOH ch1 "a drawn bow"; BAU ch8, 40, 42 ("He'd bow to the pump"), ch50 "bow-wave"; "bowed" ×16 = BAUD. |
| present | all PREZ-ent | the gift ch3, 43, 53, 55; the adjective elsewhere; ch10 "*Present Cycle*", ch57 "*Present by observation right*". No verb. |
| close | — | KLOHS as noun/adjective ("the close of intake", "close-ruled", "close-printed", "close-written", "close hand", "close under the cap", "at the close of the trials"); KLOHZ as verb — all clear in context. |
| the read (REED) | hundreds | "the read", "a read", "the full gaze"; "had read / read it" (past) = RED. |
| the leave (LEEV), the give (GIV) | — | "The leave runs out where the lane does." (ch53, 55); "Reydan's give" throughout. |
| row, minute, record(s), refuse, subject, object, content, separate, produce | — | all read naturally in context (row always ROH; minute always MIN-it, including "the minute"; refuse always the verb). |
| sowing | — | ch4 "the eleventh of Sowing" = SOH-ing; ch56 "as a woman sowing a field" = SOH-ing. |

**"As" after the lanes' conversions.** All 510 ", as …" clauses and the 70-odd bare "as he/she/it …" clauses were listed
and read. Nearly all are habitual ("as he always did", "as it always did", "as she had laid them since she was a
first-year") or manner ("as a buyer looks at a horse", "as you test a child for fever", "as you hold still in front of a
bird") and cannot be heard as "while". The temporal ones are literal and correct (ch1 "Six," she said round the tape, as
Cael walked out onto the oak"; ch1 "Karis arrived as the bell stopped"; ch12 "as the light crossed his eyes"; ch16 "as he
landed"; ch32 "as Brom came past to hand over his coat"; ch33 "caught her as she landed"; ch34 "as she passed him on her
way up she touched the top of his head"; ch45 "as he listened"; ch46 "as she walked"; ch59 "as the procession turned").
**No fixes.**

**Accidental rhymes / repeats in adjacent sentences.** None worth a fix. The deliberate repeats stand ("the way a crowd
steps aside for a steward", ch53 and ch56; "struck flint", ch46, 49, 55, 56; "walked his circle"; "slept like a quarry
stone" counted aloud; "a wave breaking" with its own callback in ch31).

### 2.3 Formatting the narrator meets

- **Code block** (1): ch56 ll.193–200, FRAGMENT ACQUIRED, Storm-adjacent (§10, verbatim). `fpaudio.py` strips the fence,
  keeps each line and adds a full stop: "Fragment acquired. Unnamed — Storm-adjacent. Duration: sustained. Integration:
  partial. Tier equivalent: Gold. Stability: provisional — architecture under load. Note: pressure-differential
  component; corridor-seeding component. Short range. Acquisition: directed. Engagement: adversarial, combat." Read as a
  notice, each line its own beat, the brackets silent, the spaced dashes pauses; its own segment and a long pause
  (direction note 3). The first stability warning the book contains is this line; the narration glosses it ("No notice
  before this one had ever told him that what it gave might not hold").
- **Brackets** (3): `[UNCLASSIFIED]` on the finals board (ch48 l.93, §10 item 14, not italic); `[unnamed]` in the
  notice; `[SHATTERED]` in the convening's question (ch60 l.113, italic, §10 item 18). Brackets never voiced; the word
  plain. The narration's "a word inside two square brackets" (ch48) explains the first. No other brackets.
- **"vs."** (ch48 l.93 the board; l.105 "the little *vs.*" in narration): say "versus" both times; the board line is
  protected.
- **Registry forms, gallery sheets and broadsides.** The entry instrument line (ch2), the deficiency memorandum (ch3),
  the advisory (ch5), the printed card (ch5, ch6), the credentials and validation tables (ch7), the challenge forms with
  their reasons ("*Want to see it before the story's finished.*", "*my lads asked me to*", "*the town asked me*",
  "*Doctrinal interest.*", "*The crowd.*", "*Overdue.*"), the index entries (ch19), the seedings and draw lines (ch26,
  ch30), the deferral notice (ch33), Ilsev's validation form (ch38), the registry notice (ch39), the filing and the
  acceptance (ch48, ch50), the hearing's four items (ch50), the protocols (ch54), the entry (ch57), the return (ch58),
  Seln's quarterly and report (ch19, 26, 58): all italic, all in words except the few numerals below. The broadsides'
  columns (ch37, ch42, ch48) are italic paragraphs read as print; ch37's exchange figures are already spelled for the
  ear ("*nought to three, two to one, one to two, one to three*").
- **The Log, the notebooks, Karis's columns, the minute, the charter and notice texts** — see §2.1(a)–(f). Karis's wall
  and door in ch53 ("*We don't know.*", "*A pipe. Dead. Brom: she turned.*", "*she arrives third*" with "*trial, read
  live*" small, "*Permitted.*") are written sheets; her ruled columns in ch34 ("*QUARTERFINAL*", "*Unknown.*") and ch52
  (the seconds) likewise. The bank minute (ch53) and the costed rule (ch59, §10 item 32) are entries in Hesk's book; the
  three numbered rules (ch56) are B4's minute recalled in italics. The lower-case italic lines are deliberate written
  text: ch24 "*eighteen years. counted anyway.*", ch31 Umber's attestation (§10 item 11, which also ends without a full
  stop — the engine simply ends the segment; a renderer may add the stop, the text stays), ch51 the scribe's note (item
  15), ch57 "*our fighter does not mis-seed.*" (item 55).
- **Numerals vs words.** The book writes nearly every number in words. The numerals that remain all read naturally:
  "41-7843-V" (ch2 the line, ch5 Karis says it: "four-one, seven-eight-four-three, V", carried); the numbered lists
  "*1. … 2. … 3.*" (ch4 Karis's card, ch13 the four rotations, ch50 the hearing's items: read "One." … "Four."); the
  index and board lines "Iron, Rank 9" and "Copper, Rank 1" (ch19), "IRON 9." / "COPPER 1. FIRST SEED." / "IRON 3." (ch30),
  "ZERIN — AUREMONT — 9. LIRA — HALCENVANE — 4." (ch36, the points), "Figure: 25." (ch38), "Gold Rank 3" (ch46, ch52, §10
  items 25, 27), "GOLD 3." (ch48, item 14), "Priority Level 4" (ch60): numbers as words. No "0" (the book's word is
  "nought", 15 times, and once Rooke's "Naught-three", BOOK_MAP §8's spelling — ear-identical, NAWT), no ordinal numeral,
  no slash, no middle dot, no en-dash range, no T-number or d-number anywhere in the manuscript. The composites are
  spoken in words ("Twenty-four and a third", "Eight point six six").
- **Abbreviations.** None of Cu/Br/R1/wk/exch/unr/def/Instr/opp/equiv occurs. The only one is "vs." (above). Initials:
  "*S. Seln*" (ch1, ch26, roster), "*C. Cael*" (ch5, ch6, the card), "*K. Dellenmoor*" (ch26 the door card), "— H."
  (Hesk ×5), "— L." (Lira ch43), "— Q." (Quenna ch44). Say the letter. "the little *vs.*" = "versus".
- **All-caps lines** (75 hits, engines sometimes spell them): *DEMONSTRATION* (ch7, ch10 the day boards); the woodcut
  titles (ch29: *THE UNNAMED OF HALCENVANE*, *THE BOY THE REGISTRY COULD NOT SORT*, *LIRA OF THE BLUFF*, *DAEVA OF
  AUREMONT*, *THE FIVE FROM THE BLUFF*); QUALIFIED (ch24); Rooke's capitals (ch25 *A BRACKET OF CEILINGS.* and the five
  names; ch40 the four cards *ONE. IT COVERS GROUND. NOT A MAN.* …); the draw and standings lines (ch30, ch36); the
  betting-row sign *NO BOOK ON THE DEMONSTRATION BOUTS.* (ch32, 45, 54) and *THE FIVE: GONE* (ch32); *QUARTERFINAL* (ch34,
  36); *THE CROWD* and *HE'S BETTER THAN THE WOODCUTS.* (ch42); Lira's *TAKEN. HALCENVANE. ASK THE GIRL WITH ONE ARM.*
  (ch44); HALCENVANE — AUREMONT, HALCENVANE — SQUAD AS FILED, *NONE* (ch45); WHO FIGHTS THE ENROLLEE? (ch47); the finals
  board (ch48); HALCENVANE on the bedsheets and THE ARGUMENT AND THE TABLE (ch51); [SHATTERED] (ch60). All written signs
  and boards; render in sentence case (renderer substitution, as Books 1–4); no text change.
- **Em dashes**: closed throughout; spaced " — " appears in 60 chapter-title lines (never voiced), inside documents,
  letters, board lines and the notice, and in four spoken or read lines, all protected (ch17 Seln "confirmed — the
  market", ch40 Rooke "comes down to four — you lose the bout", ch52 Withrow "finals day — they counted us", ch10/ch20
  the ruling). All pauses, never "dash". The crier's "*and the boy —*" (ch56) is a cut-off inside italics: short gap.
- **Scene breaks**: all correctly spaced. **Whitespace**: clean. **Paragraphs ending in a colon** (6: ch5, 6, 11, 24 ×2,
  59) introduce a written line or a spoken one in the next segment: a short rising pause. **Ellipsis**: one, Rooke's
  "Bursts..." (ch42 l.67, three dots): a trailing pause.

### 2.4 Line-level typos and grammar

- Doubled words: "six six" / "three three" ×9 (ch5, ch6: the decimals read aloud, deliberate); "had had" ×7 (ch6, 15,
  17, 25, 44, 47, 52); "that that" ×1 (ch18). All grammatical. No true doubles; no ", ,", "..", "?.", "the the", "in in"
  or any other pattern the script looked for.
- Broken joins: **none**. Each place the lanes cut or recomposed was read in place: lane A's one-paragraph merry Blade
  (ch21) with its burst count agreeing with the Log; the bill-line Logs (ch12, 21, 23); the audit cut to two rules
  (ch18); the road sorting as two carters (ch28); every eleven moved (ch3 "a dozen more times" = 7 + 4 + 1; ch4 "twelve
  of them by the heel alone" of twenty; ch18 "Twenty pages"; ch24 "seven years ago"; ch25 "nine breaths"; ch28 "perhaps
  ten"; ch33 "Ten exchanges" ×2; ch34 "seven pages… the first six… The seventh"; ch44 "at ten" and "nine days by coach";
  ch49 "Nine pages"; ch51 "the ten paces"; ch51 "Halcenvane was twelfth to be read." standing alone; ch53 "a dozen more"
  / "the dozen" and "The tenth thing… under nine others"; ch56 "ten seconds by a carter's count"; ch60 "a dozen of them
  now"); lane B's re-ordered Daeva window (ch49: the lining, the exercise sheet, the registry page "kept from the bottom
  up… Below it", "It was the garden." as the hinge, "It had been four years since the coast.", then "She went back to
  the glass, and to the trial."); the two seen moments after the lane (ch56); the panel night's heard arguments (ch57,
  all tagged); the trial recap (ch51); the pen-case (ch53 ×4) beside the locked case (ch58); the guard of four, two on
  either side (ch31) and of two (ch51, ch59 "As on the first day, no house walked behind it."); the bay "a yard deep"
  (ch40 ×2, ch41); "The city was still nine days off" (ch27) beside "a week out"; "healed months ago" (ch14); "this time"
  (ch9); "the pole" in the leaf list and the Fiske line in its Silver-bracket form (ch60); the captain's restored nod
  (ch41) that ch59 calls back. All sit clean: no mid-clause end, no lower-case start, no tense slip, no dangling
  comparison where a simile was cut, no number changed in one place and not its echo (every page count is a different
  document: twenty, seven, nine, four, six, ninety).
- The four lower-case paragraph starts are written lines (§2.3); the one paragraph without terminal punctuation is the
  protected attestation (ch31).
- Spelling: British throughout ("colour", "favour", "realised"/"realized" both appear); "theater" ×2, "favorite",
  "honorably" are inside protected lines (ch32, 51, 52, 39) and stay. "Naught-three" (ch36, once) against "nought"
  (fifteen times) is the map's spelling and sounds the same. No audio effect from any of these; noted for the ledger.
- The Reader Standard holds as the arc read found it (the one oath is "a perfectly clean word" through a wall; the coast
  deaths in ch49 are stated in one plain sentence).

### 2.5 Paragraphs over about 700 characters

97 paragraphs (flattened: asterisks removed, whitespace collapsed, as the segmenter sees them; the longest 1,160, ch21's
one-paragraph merry Blade). Listed only; none is a defect, and `fpaudio.py` splits them at sentence boundaries. The
direction file should mark the split so it does not land mid-thought; the first sixty characters of each are given so it
can be found.

| ch | chars | opens |
|---|---|---|
| ch01 | 751 | Halcenvane stood along the top of a bluff above the river Os… |
| ch01 | 833 | That was the recess's finding, and it had taken him most of… |
| ch01 | 717 | Cael had come up to the great hall of the lecture range earl… |
| ch01 | 867 | "Whoever goes out for this house goes because the tournament… |
| ch02 | 777 | The entry instrument lay open on the records-hall counter wi… |
| ch02 | 705 | He had seen the name before, of course. It was on the regist… |
| ch02 | 873 | "This morning I have decided nothing about you." Bracken sai… |
| ch02 | 940 | "Your next evaluation. The provision's second." Gault tipped… |
| ch03 | 736 | He came off the mark at half speed, then at a quarter, then… |
| ch04 | 827 | Karis had spread the charter's three copies down its length… |
| ch04 | 772 | "It's a fossil," said Karis. She had got her breath back, an… |
| ch04 | 723 | He did it standing, with his spectacles on the end of his no… |
| ch04 | 750 | "Now look at the sequence. It's the only part that matters."… |
| ch04 | 743 | The response had gone down the bluff on the morning courier… |
| ch04 | 746 | Rooke did not post the first meet's bout targets. Every othe… |
| ch04 | 894 | The floor, at least, did not wait for anybody. On the Fourth… |
| ch05 | 736 | He had seen perhaps five such paragraphs in forty years. It… |
| ch05 | 875 | Cael saw it in the order he had watched it stop. Rooke's fir… |
| ch05 | 794 | It was the first evening of the fifth week. The map room lay… |
| ch05 | 706 | "I've been in this trade a long time," he said. "I've seen f… |
| ch05 | 849 | He could not. Not because he did not know what he could do;… |
| ch05 | 837 | Then, because the habit was older than the doubt, he sat on… |
| ch06 | 734 | Rooke had changed the floor. The long room had a ring on it… |
| ch06 | 729 | He had six free on the sprung oak. This floor was not the oa… |
| ch06 | 800 | The second exchange was long, and it was Ephram's, because h… |
| ch06 | 780 | The third exchange he spent learning Ephram's walk. He did n… |
| ch06 | 740 | He did not know he was going to do it until it had begun. Th… |
| ch06 | 717 | Cael watched how she did it, and for the first time understo… |
| ch06 | 875 | Karis was sitting with one hand on the charter and the other… |
| ch11 | 802 | "By buying one mark with another." She turned the book a lit… |
| ch11 | 754 | He was an Iron Rank Four of the mill guild, a Force Path, br… |
| ch11 | 925 | Then Karis read Lira perfectly. Cael could see it happen fro… |
| ch11 | 728 | Cael had watched that bout from the far rope with a sinking… |
| ch11 | 716 | In the fourth exchange Ephram threw the second-year entry th… |
| ch11 | 714 | That night Ephram bought the whole table's supper. He did it… |
| ch12 | 736 | "Not by pushing one leg up," he said. "You were right about… |
| ch12 | 712 | "I was there first," he said. "Long before anybody pointed t… |
| ch12 | 821 | Cael understood it within a dozen heartbeats, and admired it… |
| ch12 | 834 | He could spend it now. If he did, he would have the touch in… |
| ch12 | 844 | The first was a hill-house fighter who had been told to test… |
| ch12 | 785 | He was a Bronze Rank Five, half guild and half academy, as h… |
| ch13 | 708 | Karis sat at the table's end nearest the stove with the grey… |
| ch13 | 767 | "Rich." She turned the boot and started on the heel. "We use… |
| ch13 | 792 | Seln did not move. He let his eyes go up the board to the br… |
| ch13 | 774 | The meet records were public. They went out by courier to ev… |
| ch13 | 895 | It was what Gault had promised at the end of last term and e… |
| ch13 | 763 | Their second night on the road was at a coaching inn where t… |
| ch13 | 721 | He set the season down in figures before he let himself writ… |
| ch14 | 755 | Cael rode the tailboard, as he always did, and spent the lon… |
| ch17 | 815 | "The office would put its name to it before any panel you ca… |
| ch18 | 821 | "The clerk." She held the book open toward them so they coul… |
| ch21 | 1160 | His first challenger was the confluence-house Blade who had… |
| ch22 | 751 | It was not a family argument this time, but an exam between… |
| ch23 | 892 | The meet record went up on the main hall's board at the firs… |
| ch25 | 745 | The squad was five: Lira, Brom, Karis, Ephram, and Cael in t… |
| ch32 | 984 | "Think of a fighter's standing as money in a bank," she said… |
| ch32 | 744 | "Rhagen first, because Rhagen's the one that matters." He la… |
| ch32 | 863 | He looked along the row. He had known it for four days by fa… |
| ch36 | 777 | It had been building all bout, and Cael had watched it build… |
| ch37 | 706 | Marek stood still on his chalk. Cael knew that kind of still… |
| ch41 | 707 | He could not see himself paying it. That was what the card h… |
| ch45 | 710 | He watched the houses read it. Rhagen's people read their li… |
| ch45 | 804 | "I'll say how it's scored once, so we're all saying the same… |
| ch45 | 705 | Umber had been up since before light, as he usually was duri… |
| ch46 | 912 | He did nothing else for the whole exchange, and nothing else… |
| ch46 | 907 | Cael felt the read come back up to its ordinary depth and se… |
| ch46 | 706 | "I want that understood before you get to the stair, because… |
| ch49 | 880 | People who had never done it supposed that the air was empty… |
| ch49 | 756 | She had been Auremont's since twelve, a year before the gard… |
| ch49 | 790 | She had stopped for one whole second, with eight thousand pe… |
| ch49 | 824 | For two days she had watched the frame in the north tunnel,… |
| ch49 | 782 | "My name goes on the bottom of the safety sheet," he said. "… |
| ch50 | 702 | It began by saying that the underwriters' printed schedule h… |
| ch50 | 701 | All round, the new barrier would stand six feet, with a roun… |
| ch51 | 826 | Karis had gone up onto the western saddle and stamped on it,… |
| ch51 | 875 | It was dull work, and it was the hardest of the day. Nobody… |
| ch51 | 705 | It was a small delegation in grey from somewhere inland, six… |
| ch52 | 812 | Gault had gone up to his room and come down again with a sha… |
| ch53 | 733 | "Wind past six, if the fight asks for a seventh: six is wher… |
| ch53 | 783 | Cael lay in the dark with the shutter open a crack on the ha… |
| ch54 | 777 | The betting rows had done something new. The office had let… |
| ch54 | 840 | Then the protocols were read, and then they were read again.… |
| ch54 | 746 | He went round it the way he had gone round every floor of hi… |
| ch54 | 793 | It was the same, and it was worse, because she was trying so… |
| ch55 | 1028 | She braided him down the east side, mast to mast. He paid fo… |
| ch56 | 736 | He put his right palm to the boards and pushed, the fourth p… |
| ch56 | 723 | That was all it ever was. It was not taking. It was nothing… |
| ch56 | 749 | Not less than usual. Nothing. He had pushed against air ever… |
| ch56 | 1024 | Ephram told him afterwards how it had gone outside. He had g… |
| ch57 | 887 | It had been hers. She had known it the moment it opened, bef… |
| ch57 | 891 | It did it gently, a little at a time, like a good coat in it… |
| ch57 | 827 | The keeper had the first. He told it to them at breakfast, g… |
| ch58 | 784 | The designation in the enrollee's file had been her question… |
| ch58 | 785 | "I asked for a witness once," he said, "with a warden across… |
| ch58 | 740 | He noticed that before he had written a word, and it was str… |
| ch58 | 715 | "If I gave you names I would be guessing, and I don't guess.… |
| ch59 | 856 | Gault had taken the shallow box out of his inside pocket, th… |

### 2.6 Protected lines (checked, untouched)

Every BOOK_MAP §10 item was read in place: the charter and office text (items 1–18: the clause ch4, the certificate
sentence ch2, the memorandum ch3, the provisions ch4, the advisory ch5, the card line ch5/ch6, the ruling ch10/ch20, the
manual's rule and annotation ch12, the query's three nouns ch24, the steward's sentence ch23, Umber's attestation ch31,
the trial rule and "*Again.*" ch32/ch45, "*Overdue.*" ch48, the finals board ch48, the scribe's note ch51, the entry ch57,
the return ch58, the convening's question and "*entered for formal proceedings*" ch60); the notice (ch56, in its code
block, six lines, exact); the Log entries (19 ch2, 20 ch9, 21 ch13 with its "three years", 22 ch41, 23 ch45, 24 ch1/45/60,
25 ch46, 26 ch52, 27 ch52, 28 ch53 in all four parts, 29 ch59 with its "three years", 30 ch59, 31 ch60, 32 ch59 with its
added line); the spoken lines and letters (33 ch2/ch45 … 59 ch60, every one, including 38 Lira's "*right now*", 41
Zerin's four lines, 43 Ivenne's and Karis's exchange, 45 Hesk's "Seventeen…", 47 Umber's five sentences, 51 the ring
walk's four lines, 54 "That was mine," with its comma, 55 Umber's "Write the entry." and Auremont's four words, 56
Vastin's and Seln's lines, 57 "Rematch." and Hesk's and Vell's letters, 58 Vastin's testimony, 59 the closing exchange
and the closing paragraph); 60 thirteen in a garden court (ch49); 61 "Gratitude is the leak." (ch2), "Thank you for the
form." / "Mm." (every Fifth-day), "Sixteen suits you." (ch4), "The recess's problem." (ch60, #37 O5). A flattened grep
found all 52 `protected-patterns.txt` lines, each once in its mapped chapter. The one §10 string whose case differs from
the map is item 32 ("*The conditions may complete…*" for the map's "*the conditions…*"), with no audio effect. The
optional fix in §3B does not touch any of them.

---

## 3. Exact line fixes

### 3A — Required before render (0)

None. Nothing in the text will be voiced wrongly by an engine or misplaced by a listener; the sweep and the read found no
abbreviation, slash, numeral, join or quotation that needs changing.

### 3B — Optional, engine-safety only (author's call; 1)

A human narrator will read this correctly; a TTS engine, with ten "lead" = LEED in the book and this the only LED, is
likely not to. Book 4 left its five window-leads to the lexicon; Book 1 fixed its "wound"s. Either precedent serves. The
old string matches exactly once in the manuscript; the new string occurs nowhere.

1. `manuscript/chapter-49.md`
   old: `a single pane of thick glass set in lead, with a small brass plate on the sill`
   new: `a single pane of thick leaded glass, with a small brass plate on the sill`
   (Daeva's window; "leaded glass" is a fixed compound engines carry as LED-id, and the sentence keeps its fact.)

Not proposed, but flagged for the lexicon and the ledger: "wind a gate" ×2 (ch44) = WYND against the Path; "a wound"
(ch59, protected) = WOOND; "find it live" (ch37) and "*read live*" (ch53) = LYV; Rooke's "Naught-three" (ch36) for the
book's "nought" (ear-identical; BOOK_MAP §8's spelling); the protected attestation without its full stop (ch31; the
segmenter or renderer may add one, the text stays).

---

## 4. Pronunciation lexicon (for the Breeze direction files)

Stress in capitals. "Owner-confirmed" = decision #33. "Carried" = the same entry in Book 1's, Book 3's or Book 4's lexicon,
unchanged. "Proposed" = Book 4's proof or this one; not substituted at render until the owner confirms. "Placeholder" =
decisions #3 and #11 (none occurs here).

### People (36 named, plus the unnamed roles)

| Name | Say | Who | Status |
|---|---|---|---|
| Cael | KAYL (one syllable, as "sail") | the boy; "the enrollee"; "the fifth man of the bluff"; "*C. Cael*" on the card | owner-confirmed #33 |
| Caelen Hesk-ward | KAY-len HESK-ward | his full name (ch2 "*Caelen Hesk-ward, 41-7843-V*"); two words, stress HESK | carried (B1–B4) |
| Hesk | HESK | grandfather, the instrument-maker; five letters signed "*— H.*"; "Hesk's book", "Hesk's clock" | carried |
| Lira | LEER-a | Wind, Iron Rank One; "the Wind girl"; "LIRA OF THE BLUFF"; "*— L.*" (ch43) | owner-confirmed #33 |
| Brom | BROM (as "from") | Iron Skin, Copper; "the wall"; continental Copper champion; the Velmere letters | carried (B2–B4) |
| Karis Dellenmoor | KAIR-iss DEL-en-moor | Ember, Iron Rank Three; "*K. Dellenmoor*" on the reading-room card | carried (B3, B4) |
| Ephram | EF-ram | Blade, Iron Rank Six; trial caller; "Assay" is his name for Cael | proposed (B4) |
| Rooke | ROOK (as "book") | the coach; "Instructor"; card four | proposed (B4) |
| Gault | GAWLT (as "fault"; long aw, never GOLT) | Magister, evaluator of record; the case with the handle; "fourth on the figures" | proposed (B4); keep apart from "Gold" (§2.2) |
| Bracken | BRACK-en | the registrar; "twelve years"; the sand, the pouch | proposed (B4); the flagged pair with Brom kept |
| Withrow | WITH-roh | the chancellor; "eighteen years" | proposed (B4) |
| Seln | SELN (one syllable, as "kiln" with an s) | the teaching assistant; "*S. Seln, assessment office: records and floor scheduling*"; "the office"; "Mm." | proposed (B4) |
| Vastin | VAS-tin (as "fasten") | the Archmarshal; "the man in the twelfth chair"; "the officer of record"; no age stated | proposed (B4) |
| Ilsev | IL-sev | senior evaluation seat of the Compact's row; "the first seat" | carried (B1–B4) |
| Havel | HAV-el (short a) | records officer, the second seat; "the quiet records officer from the bluff" | carried (B2–B4) |
| Quenna | KWEN-a | Greyvane assessor, named in memory and her card "*— Q.*" (ch44) | carried (B2–B4) |
| Prynn | PRIN | "Prynn's index" (ch2, once) | carried (B3, B4) |
| Vell | VELL | the Ardenmere ledger-keeper; her letters (ch44, ch60) | carried |
| Reydan | RAY-dan | "Reydan's give", named in memory | carried (B2–B4) |
| Fiske | FISK | named in memory (ch1, ch11, ch60) | proposed (B4) |
| Jask | JASK (as "mask") | named once in Seln's memory (ch17) | proposed (B4) |
| **Daeva** | DAY-va (two syllables; "ae" as in "Mae") | Auremont's Gold, Rank Three; nineteen; "the Gold"; "DAEVA OF AUREMONT"; Storm Path | proposed (this proof); keep apart from KAYL by the onset |
| **Zerin** | ZERR-in (short e, stress first) | Auremont's Wind, Iron Rank Nine; "the program's" fighter | proposed |
| **Marek** | MAR-ek (stress first, short a) | Rhagen Institute's Glass, Copper Rank One, first seed; "the best reader" | proposed |
| **Ivenne** | ih-VEN (stress second) | Ternhall's Ember, Karis's old partner; Karis never says the name aloud | proposed |
| **Umber** | UM-ber (as the pigment) | Chief Adjudicator; "the grey man in the tower"; never in a scene with "Ember" | proposed |
| the Shield reserve / the Stone reserve / the wagoner / the porter (of the bluff) / the desk clerk / Bracken's inky-knuckled clerk / the night porter / the ganger / the vain Bronze / the yard-master / the curiosity Bronze / the guild champion / the buried Copper and the lean man in brown / the river academy's patient Blade / the Fenmark boy and the woman with the tape box / the southern coach and his boy / the foreman (quarry) / the barge-master / the caravan captain / the builder / the merry Blade / the board-man / the grey-wool woman (the compiler) / the two from Auremont (the scouts) / the validator / the stewards / the clerk with the niece / the presiding adjudicator's clerk / the convenor / the innkeeper with the frame / the keeper (he; counts aloud) / the marshal / the lock-keeper / the proprietor of the blue door / the fishwife / the fiddler / the likeness-seller and the barrow-man / the foreman (the ring) / the floor-crew woman with the oil / the Rhagen captain / the lake man (the duelist) / the lattice-breaker / the two Silver seniors / the coast coach / Auremont's delegation head, risk officer, lead instructor, counsel, the eager young man / the senior rating clerk (a woman) and the junior clerk / the oldest judge, the woman from the coast, the youngest judge / the three scribes / the healers of the north station / the referee / the Ternhall chancellor / the hill fighter / the Ash fighter / the Rune Path fighter / the eastern Silver with the form / the man on the barrel | — | unnamed recurring roles (BOOK_MAP §13: never name them) | keep each a fixed colour across chapters |

### Places (22)

| Name | Say |
|---|---|
| Halcenvane | HAL-sen-vayn (three syllables; carried B4); "the bluff", "the hill" |
| Ostrand; the Ost | OST-rand; OST (carried B4) |
| Greyvane | GRAY-vayn, both syllables (carried B3, B4) |
| Denvash; Ardenmere | DEN-vash; AR-den-meer (carried) |
| Fenmark | FEN-mark (carried B3, B4) |
| Velmere | VEL-meer, both syllables (carried B3, B4; Brom's house) |
| Ternhall | TERN-hall (carried B3) |
| Dellenmoor | DEL-en-moor (carried B3) |
| **Norhold** | NOR-hohld; "the city"; "a crossroads city" |
| **Auremont** | AW-re-mont (stress first); "the program"; "the favourites" |
| **Rhagen** (Institute) | RAH-gen, hard g (stress first); keep apart from Reydan and Rooke |
| **the Concourse** | KON-kors; the main floor, the bowl, the tiers, the west tower (the adjudication office), the east tower (the timekeepers), the oak round, the sockets, the ring |
| the wool town; the mill town; the quarry town (the slate country, the slate exchange, the salt store is the confluence); the confluence | descriptive; no stress |
| the Crown yard; the sprung oak; the covered walk; the records hall; the assessment wing and its counter; the long upper room; the map room; the reading room | as written (carried B4 where shared) |
| the guesting-house; the back room (the rocking table, the pump); the hired hall; the warm-up halls; the delegation quarter; the outer court; the betting rows; the processional way; the north tunnel; the copy line | as written |
| the blue door (the cookshop); the powder wharf; the lock-house; the basin steps; the coopers' row; the fish market | as written |
| the Compact's house (Vastin's room, the porter and the pigeons); the district seat; the regional seat; the registry's annex | as written |

### Terms and invented words (46)

| Term | Say / handle |
|---|---|
| Kindling, Kindled; Arbiter; the Compact; sigil | KIND-ling; AR-bit-er; KOM-pakt; SIJ-il (carried) |
| [SHATTERED] (ch60) / [UNCLASSIFIED] (ch48) / [unnamed] (the notice) | brackets never voiced; the words plain |
| vs. (ch48, the board and "the little *vs.*") | "versus" |
| Path names: Wind, Pressure, Iron Skin, Blade, Force, Stone, Shield, Mire, Current, Ash, Glass, Ember, Shadow, Tide, Lattice, Rune, Storm | as written; "Wind" the noun; "a Mire", "a Shield" = practitioners |
| -adjacent (Storm-adjacent, Wind-adjacent) | ad-JAY-sent, light pause at the hyphen |
| Tiers: Copper, Iron, Bronze, Silver, Gold; "Rank One" … "Rank Nine"; "Gold Rank 3" / "GOLD 3." / "IRON 9." / "COPPER 1." / "Rank 9" / "Rank 1" | numbers as words ("Gold Rank three") |
| the Silver Standard; the Standard; the mark; par; the bands; the composite; execution, control, effect; the strike (of the high and low); the figure; the rating; "in-band" | as written; "par" = PAR; "the bands" the rating bands |
| the demonstration-exhibition provision; the category; the exhibition; the frame (the category's board); the register; the filing; "*Overdue.*" | as written |
| the brackets; the seeding; the draw; the foot and head of the list; the standings; the threshold; the circular; the qualifying season; the four meets; the Continental; the finals; the sitting | as written |
| the team trial; the scenario floor; the platforms; the objective ledger; the engagement ledger; quarter-minutes; the barrier; the diagonal; the hill; the crossings and saddles | as written |
| the ring (fifty-two by forty-eight); the masts; the cables; the trench; the breaks; the cap, the bull-nose; the crown; the oak | as written; "bull-nose" one word aloud |
| the lane; the fold; the crease; the wash; the leave (LEEV); the stormlane is not used in the text | "the leave runs out where the lane does" |
| the read (REED); the full gaze; the landing beat; the burst; the gather; the hip's bill; the rate; the bank; the ceilings | Cael's and Lira's terms; no stress |
| Reydan's give (GIV); the push; Karis's spark (the ignition, the contact); the quiet thing from the stair; the still place; "Still open. Still real. Patience." | as written |
| the doctrine; the record; the public suite; "managed effort"; "Variance is cheap. Buy some."; the engineered scatter (items one to four); page three; page thirty-one; "adjacent to it"; "Used-to is a rating. It just doesn't post." | as written |
| the clause (sixth part, fourth subsection); the third schedule; the enrollment record; "without omission"; the mirror; the memorandum; the advisory; the card; the ruling; "the remedy… not available from this office" | as written |
| the Log (the old volume; Hesk's book from ch45); the observation notebook; the grey notebook; the marbled log; the coaching file; the file book; the travel file; the pouch; the pen-case and the locked case | document titles where context marks them |
| First-day … Seventh-day; the bells (first … twelfth); "the eleventh of Sowing"; "the fifteenth / twentieth of Reaping"; "the cold term"; "the recess" | as written; SOH-ing, REEP-ing; no English weekday |
| 41-7843-V | "four-one, seven-eight-four-three, V" (carried) |
| the composites: "Twenty-four and a third", "Eight point six six" | the decimals as "six six", "three three" |
| nought / Naught-three | NAWT |
| the numbered lists "*1. … 2. … 3.*" (ch4, 13, 50) | "One." … "Four." |
| Initials: S. (Seln), C. (Cael), K. (Karis), H. (Hesk), L. (Lira), Q. (Quenna) | the letters |
| "Thank you for the form." / "Mm."; "Early."; "Ready. Not early."; "Walk."; "Survive the first one."; "Terms hold."; "Rematch."; "Noted." | refrains; keep each in its owner's colour |
| marks, coppers; "two coppers a sheet"; "a whole mark" | currency |
| Magister / Magistra; Chief Adjudicator; Archmarshal; Assessor; the chancellor; the registrar; the convenor; the risk officer; the design staff; the colour-guard; the marshals; the criers; the compilers; the handicappers; the board-man | as written |

Lexicon size: 36 named people (plus the unnamed-role group), 22 places, 46 terms — **104 entries**.

---

## 5. Direction notes the segmenter and instruct files will need (not text changes)

1. **Keep Cael = KAYL and Lira = LEER-a** in every chapter direction (#33).
2. **POV cutaways**: the "he/she" changes referent at the `---`. Vastin: ch5 s1, ch24 s3–s5, ch29 s5, ch43 s1–s2, ch50 s3,
   ch59 s1. Seln: ch13 s2, ch17 s1–s3, ch26 s3, ch44 s1 (and s2 opens "an hour earlier"), ch53 s1, ch58 s4. Havel: ch25 s1,
   ch32 s7, ch58 s2. Ilsev: ch38 s1, ch46 s4, ch58 s1. Umber: ch31 s1–s2, ch37 s5, ch45 s4, ch57 s2–s5. Daeva: ch49 whole
   chapter, ch57 s1, ch59 s6. One hand-off inside a section: ch45 s4 passes from Umber's tower to the breakfast table at
   "Bracken collected the notice himself…" (l.203) — mark it at the paragraph. The notice and the documents have no POV:
   flat, exact.
3. **Notices and brackets**: a neutral system cadence for the one fenced block (ch56), its own segment with a long pause;
   never voice brackets, the fence, asterisks or the `---`. "[SHATTERED]" (ch60), "[UNCLASSIFIED]" (ch48) and "[unnamed]"
   plain; "vs." as "versus".
4. **Italic documents**: give the Log and Hesk's book, the notebooks, Karis's columns and wall, Seln's reports, the
   letters, the forms, the entry and the return a slight register change and return cleanly at the next prose cue; the
   sign-offs ("*— H.*", "*— L.*", "*— Q.*") and the initials are pauses and letter-names, never "dash". The lower-case
   written lines (ch24, 31, 51, 57) are deliberate. The ch31 attestation ends without a stop: a full pause after "alike".
5. **All-caps** (§2.3) in sentence case; the woodcut titles as titles; the single letters by name.
6. **Counts and calls**: preserve the slow count architecture — the referees' and stewards' calls flat; the clerk's
   totals; Rooke's exchanges "Naught-three, two-one, one-two, one-three." (ch36); Cael's inward burst counts ("*One.* …
   *Four. Of five.*"); the eight claps (ch59); the keeper counting to five; the copy-line numbers under the window (ch58);
   the decimals as "six six".
7. **Collisions by register**: Gault flat and exact with its long aw beside every "Gold"; Bracken dry and precise beside
   Brom; Withrow level and unhurried beside Rooke; Rooke flat with no lift at the end; Seln pitched for a counter; Vastin
   even and without weight; Ilsev exact; Havel careful; Umber the inventory voice, dry and unremarkable, carrying to the
   top bench without being raised; Daeva level, exact and unhurried (the ring walk ch52 s5 and the hour ch58 s5 are the
   two scenes where one other voice must stay distinct from Cael's across forty lines); Zerin clipped; Marek spare;
   Ephram with the cohort's exactness and, from ch51, almost no voice; the rating clerk (ch57) a woman.
8. **Homographs** (§2.2): "lead" = LEED everywhere but ch49's window (LED, or fix 1); "wound" = WOWND ×7 and WOOND once
   (ch59); "wind a gate" = WYND (ch44 ×2); "live" = LYV ch37, ch53; "present" always PREZ-ent; "the read" = REED; "the
   leave" = LEEV; "the give" = GIV; "bow" BOH ch1, BAU ch8/40/42/50.
9. **Interruptions**: the `—"` cut-offs (§2.1) want the engine's short gap and no falling cadence; the two steward
   stammers and Rooke's narrated dash (ch34) are one voice across. "Mm." / "Hm." / "Huh." — check they survive the render.
10. **The one multi-paragraph speech** (ch1, Withrow's three numbers): one voice across the four paragraphs, no closing
    cadence until "I don't intend to repeat the experiment."
11. **Read text inside speech** (§2.1): a voice reading aloud, flatter than its own; Umber's reading of the entry (ch57)
    and of the attestation (ch31) are the two the book builds toward.
12. Long paragraphs (§2.5) may be split only at sentence boundaries, as `fpaudio.py` does; mark the split so it does not
    land mid-thought, especially in the bout paragraphs (ch6, 11, 12, 46, 51, 54–56) and the hearing (ch50).
