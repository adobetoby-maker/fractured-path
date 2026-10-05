# Book 4 — *Copper Crown*: line and listening proof (Step 4)

Reader: Claude Fable 5.1, review seat, fresh context, 2026-10-05. Scope: `manuscript/chapter-01.md` … `chapter-62.md`
(290,068 words by `wc`), read in order as a Breeze narrator will meet them: one segment per paragraph, `---` as a long
pause, italics flattened, the one fenced notice flattened line by line. Read first: Book 1's, Book 3's and Book 2's
`listening-proof.md` (the models; Book 2's `listening-notes.md` as the model for the notes), `COMPLETION-PLAN.md`,
`whole-arc-read.md` (§8 fixes applied), `LANE-A-REPORT.md`, `LANE-B-REPORT.md`, `EDITION_BRIEF.md` (audio, Reader
Standard), `OWNER-DECISIONS.md` #11, #33, #35 (and #7–#10, #37), `BOOK_MAP.md` §9–§10 (and §11, §13),
`protected-patterns.txt`, and `audio/fpaudio.py`. A script swept all 62 files first (quote and asterisk parity, break
spacing, brackets, numerals, abbreviations, doubled words, paragraph ends and starts, name pairs per scene, homograph
contexts, every ", as" clause, paragraph lengths); the read then went through every chapter, with the lanes' joins
given extra attention. Running notes: `listening-notes.md`.

**No manuscript file was modified.** Every fix below is a proposal; each old string was verified with a script to match
exactly once in the named file and once in the manuscript, and each new string to occur nowhere yet. No fix touches a
protected line (BOOK_MAP §10, `protected-patterns.txt`). Gwen and Abbot are owner-pending placeholders and not findings
(#11); Cael = KAYL and Lira = LEER-a (#33); no month order, month length, season name or cross-month day count appears
(#35), and the Halcenvane weekdays are First-day … Seventh-day throughout.

---

## 1. Verdict

**Render-ready after 8 small text fixes, all mechanical: one abbreviation on a pinned minute the narrator reads (ch7),
three figures "0" that an engine says as "zero" where the book's own word is "nought" (ch15 ×2, ch36), the one slash
on the standings board (ch25), and three shorthand lines joined with middle dots, a symbol with no spoken form that
`fpaudio.py` does not strip (ch15).** Three further optional fixes (ch18, ch19, ch22). One renderer requirement that is
not a text change: the strikethrough in Vastin's notebook (ch59) is set in markdown `~~…~~`, which the segmenter does
not strip; the struck words are protected and the narration explains the stroke, so the tildes must be removed at
render and the sentence read as cancelled. Nothing structural stands in the way:

- Quotation marks: every paragraph in all 62 chapters has an even count of `"` except twelve, and all twelve are the
  correct openings and continuations of multi-paragraph speeches (ch55 Gault reads his note, five paragraphs; ch56
  Cael's two-paragraph answer and his two-paragraph reason, and Vastin's two-paragraph close; ch61 Withrow's
  announcement and her three numbered sentences). No curly quotes anywhere. No mismatched quotes. Quote-inside-quote
  cases use either italics (the Log, the documents, reported speech) or single quotes (ch57 Brom repeating Rooke; ch58
  Karis reading Seln's words) and read cleanly.
- Italics: every paragraph has an even count of `*`. No `_`, no `**`, no stray markdown except the one `~~` pair in
  ch59 (§2.3). One fenced block (the ch34 notice). No headings after line 1, no tabs, no trailing spaces.
- `---`: all 256 breaks have a blank line before and after (128 in ch1–31, 128 in ch32–62, as the lanes reported).
- Attribution: no speech paragraph whose speaker a listener cannot place. The three-person and four-person suppers and
  common-room councils (ch1, 2, 5, 7, 9, 12, 17, 22–23, 31, 37, 38, 43, 45, 53, 55, 56, 58, 61, 62), the bouts (the
  table's calls are flat and attributed by form), the cookshop-equivalents (the refectory hatch ch7, the stew line
  ch14, the kitchen gate), Quenna's approach (ch4, two people), the unit (ch32–36, 38, 59; Gwen is always tagged on
  first speech), the sittings (ch48–49, ch52, ch54–56) all carry by tags, by alternation or by the content of the
  line. Two places where alternation misleads for a sentence before a tag or the content corrects it are noted
  (ch12 l.137, a direction note; ch18 l.113, optional fix 9).
- Ear collisions: Halvern, Kestrel, Fisk-, Selm-, Wren, Doss, Marrow, Corbin do not occur in Book 4. Gault and Gwen
  share four scenes and are never adjacent in one spoken list (§2.2). Bracken and Brom share 37 scenes and are distinct
  by ear (two syllables against one; BRACK- against BROM); Havel and Cael share 21 (HAV-el against KAYL). No rename is
  proposed.
- Protected lines: every §10 item is present verbatim where mapped (checked in place while reading; a flattened grep
  of all 14 `protected-patterns.txt` lines and a sample of twenty §10 lines found every one, each the expected number of
  times). None of the fixes in §3 touches any of them.
- Doubled words, lower-case starts, mid-clause ends, dangling comparisons, tense slips from the lanes: none found. The
  seven "had had" are grammatical; the one lower-case start is Seln's cipher page (ch58, protected); the nine
  paragraphs without terminal punctuation all end in a colon introducing a Log line, a note or a sign. The lanes'
  joins (the one-sentence maps in ch15, the shortened retelling in ch17, the cut fatigue page in ch18, the hip calendar
  in ch30–31, the rule-two gloss in ch31 and ch34, the ch47 anecdote, the two ch49 folds, the stake line in ch45, every
  de-elevened figure) were read in place and all sit clean. The only trace of a fold a listener meets is a POV change
  inside a section (ch49 s3, Ilsev to Cael at a name-led paragraph) and it is a direction item, not a text defect.

What remains is for the direction files, not the text: the homographs an engine will misread (`lead` as the metal in
the window leading against the twenty-odd `lead foot / lead arm`; `wound` round a wrist against the one `wound` that is
an injury; `bow` as a tape bow against three bows of the head; `live` as an adjective); the all-caps signs, chalk and
columns, which should be rendered in sentence case; the single letters in the Log, the minutes, the notes and the board
(`K.`, `L.`, `F.`, `C.`, `H.`, `B.`, `W.`, `Q.`, `S.`, `K.D.`, `TA`); and the POV cutaways, which change the referent of
"he" or "she" at a `---` (and once inside a section).

---

## 2. Findings by category

### 2.1 Quotation marks and attribution

- Balanced throughout (12 odd-quote paragraphs, all correct multi-paragraph speech; 0 odd-asterisk paragraphs, 0 curly
  quotes, script-checked).
- **Italics carry seven different things**, and the narrator needs to know which: (a) the Power Log and the observation
  notebook (the day entries, the inventories, the working ledger, the numbered lists, the shorthand); (b) documents read
  as text (the enrollment record ch5, the office's half-sheets, the notices ch7, ch12, ch38, the minute ch23, Karis's
  before-sheet ch34, the wing's two lines ch35, Seln's product and quarterly ch18, ch41, ch58, the return ch49, the
  charter subsection ch56, the certificate ch60, the tournament clause ch61); (c) letters and notes (Bracken's and
  Karis's ch2, Withrow's ch48, Hesk's ch37 and ch62, Vell's ch62, Gault's ch52, Bracken's ch55); (d) chalk, slates and
  boards (the fire-watch slate, the standings line ch25, Karis's columns, the unit's slate, the plate ch27 in capitals
  and unitalicised); (e) Karis's minute lines and tally columns with initials; (f) remembered or reported speech
  (*watch her feet, just watch*; *it tastes exactly the same*; *Brom, that is not what I meant and you know it*);
  (g) inner thought and word stress, including reverse emphasis inside an italic entry (ch27 "*…next to the word*
  undisclosed."; ch31 "*Careful* for *me*"; ch43 "*whether you can* not *do it*"; ch53 "*He wishes me* measured."). The
  split is always clear from the surrounding sentence; the direction file should say which is which per segment.
- Read text inside speech: ch8 Brom reads Rooke's sentence off his wrap "in Rooke's flat rhythm"; ch40 Lira reads the two
  board columns aloud; ch53 Cael recites Gault's three rules; ch55 Gault reads his note (five paragraphs); ch57 Brom
  repeats Rooke word for word in single quotes; ch58 Karis reads her corridor page with Seln's words in single quotes.
  Direct as a voice reading aloud, flatter than its own speech.
- Interruptions: the `—"` cut-offs are few and all deliberate ("This must have taken—" ch4; "Why didn't she—" ch42;
  "Karis—" ch35; "Is it still—" ch36; "What—" ch58; "Was that—" ch53; "An omission—" ch48; "That is all he—" ch58; "The
  read'll be on its stub. I won't have—" ch53). They want the engine's short gap and no falling cadence. The clerk's
  "Interval—" (ch13, ch54) closes inside the quote and is followed by narration ("and a number off the pendulum").
- Counts said aloud: Lira's thirty ("Twenty-eight. Twenty-nine. Thirty.", ch10); the Lattice pupil's "One, and set. Two,
  and set. Draw. Three, and set." (ch11); Lira's calls "*left*, *round*, *low*" and "*late*, *late*, *on time*, *late*"
  (ch19); Brom's "Thirty-one… Thirty-two… thirty-five" at the post (ch29); the bout counts (eleven seconds, four
  minutes eleven seconds); Bracken's "Sixteen?" / "Sixteen." (ch57). Keep the deliberate count rhythm.
- "Mm." (Seln ch36, ch58, ch62; Gault ch54; the Ash instructor "Hm." ch45; Brom "Huh." ch25, ch43, ch50, ch60; Jask
  "Huh." ch27): may be dropped or stretched by the engine; check the render. They are characters' words and carry
  weight (Seln's "Mm" is the whole of a conversation).
- The table's calls in the bouts ("Touch. Edran. One."; "Wind. Three. Bout."; "Even. Taken on the guard."; "Iron Skin,
  down. To Wind, the cleaner.") are in quotes and flat; the ladder's results are chalked (italic). Quotes-vs-italics
  carries the difference, as in Books 1 and 2.
- Two attribution notes: ch12 l.137 `"So make him look." She turned her head at last.` opens a new paragraph straight
  after Lira's own paragraph; alternation suggests Cael for three words before "She" resolves it (Lira is the only
  woman present): keep Lira's colour across both segments. ch18 l.113 is fix 9 (optional).

### 2.2 Ear collisions

**Names in one scene.** A script split each chapter on `---` and counted name pairs per scene:

| Pair | Risk | Scenes together | Note |
|---|---|---|---|
| Gault / Gwen | medium | ch32 s4; ch38 s5; ch58 s3; ch59 s1 | In all four Gwen speaks and Gault is only named in Seln's or the narrator's mouth ("Gault approves the syllabus… He will not come. I will."). GAWLT (long aw, as "fault") vs GWEN (short e, glide onset): different vowel, shape and length. Never in one spoken list. No text change. |
| Fiske / Fisk- | — | none | No other Fisk- name occurs. FISK, one syllable. |
| Seln / Selm- | — | none | SELN, one syllable, as "kiln" with an s; nothing else on -eln/-elm. |
| Karis / Kestrel | — | none | Kestrel does not occur. KAIR-iss (carried, B3). |
| Havel / Halvern | — | none | Halvern does not occur. HAV-el (carried, B2/B3). |
| **Bracken / Brom** | low | 37 scenes (ch2, 5, 6, 7, 10, 12, 17, 25, 28, 30, 32, 34, 35, 37, 40, 41, 45, 47, 49, 50, 51, 53, 55–58, 60, 62) | The registry's flagged collision (#6), kept. BRACK-en (two syllables, short a) vs BROM (one, short o); Bracken is "the registrar" in most narration and never in a spoken list with Brom. Attribution carries everywhere (Brom speaks, Bracken files). |
| Havel / Cael | low | 21 scenes (ch16, 39, 44–51, 54, 55, 57) | HAV-el vs KAYL: different onset, stress and length; Havel is "the records officer" in his own windows. |
| Ilsev / Lira | none | 10 scenes | IL-sev vs LEER-a. |
| Merrick / Tarn; Jask / Jessup; Nyle / Lira; Edran / Ephram | none | few or none | MERR-ik / TARN; JASK (as "mask") / JESS-up (never together; Jessup is named once, ch35); NYLE (as "mile"); ED-ran / EF-ram (together once, ch14 s2, in narration). |
| Withrow / Rooke; Vell / Velmere; Wray / Greyvane | none | — | WITH-roh / ROOK (as "book"); Vell and Velmere never share a scene (Velmere is Brom's house, ch37); Wray / Greyvane co-occur in ch3, 4, 8, 10, 20 (RAY vs GRAY-vayn, both syllables, as B3). |
| Halcenvane / Greyvane | low | 24 scenes | HAL-sen-vayn vs GRAY-vayn: the two academies, always one against the other; different onsets and three syllables against two. The -vane cluster is the owner's (#6). |
| Vastin / Vell; Gault / Cael; Prynn / Brom | none | — | VAS-tin; the two never meet. Gault / Cael 71 scenes: GAWLT vs KAYL, distinct. Prynn / Brom: PRIN vs BROM. |

No rename is proposed (decisions #6, #11).

**Homographs.** All occurrences were read in context; none is ambiguous to a human narrator. These are the ones an
engine is likely to voice wrongly, with the intended reading (for the lexicon/instruct files):

| Word | Intended | Where |
|---|---|---|
| lead (LEED, the front limb) | 22 | "lead arm / lead hand / lead shell / lead foot / lead leg / lead thigh / lead shoulder": ch3 ×13, ch9, ch19, ch21 ×2, ch24, ch51 ×3, ch52; and the verb ch36 "turned to lead the others", ch49 "don't lead to the same place". |
| lead (LED, the metal) | 5 | ch7 "the cost of lead" (glazing); ch17 "the lead of the window-pane", "a little grey curl of old lead", "her thumbnail still on the lead"; ch34 "the shapes of the lead between the panes". |
| wound (WOWND, past of wind) | 11 | wraps, cords, the gauge, the roll, the bandage, the drum, the scarf: ch8, 11, 15, 16, 24, 44, 49, 51 ("wound the bandage"), 54, 58, 59. **Exception:** ch51 "building a fight out of the other one's wound" = WOOND (the injury). |
| bow | — | ch28 "tying the box's tape in a flat bow" = BOH. ch36 "stepped aside for it with a little bow", ch44 "he did not bow", ch52 "come down to one knee, and not to bow" = BAU; ch3 "He bowed to the table" = BAUD. |
| live (LYV, adjective) | 9 | ch6 "a live thing", "kept live"; ch27 "a live hazard", "anything live"; ch30 "a live delivery", "A live situation"; ch49 "remains live on an active file" (protected); ch60 "stayed live underneath". LIV (verb) elsewhere: ch6, 7, 29, 34, 38, 54, 58, 61. |
| lives | — | LIVZ (verb): ch1 "where it lives", ch27 "lives over a smithy", ch57 "only lives as long as". LYVZ (noun): ch13, ch43, ch48. |
| tear / tears | — | ch20 "a tear in the lining" = TAIR; ch29 "tears running down her face" = TEERS. |
| the read (REED, noun) | hundreds | "the read", "the surface read", "a read drill", "the read's silence". Always REED; "had read", "read it" (past) = RED. ch18 "I've written *none observed*" etc. are RED. |
| present | — | PREZ-ent (gift): ch37 "this isn't a present", ch53 "Nobody gave me a present". pre-ZENT (verb): ch12 "will present himself". Adjective elsewhere. |
| row | all | ROH: front-row, the back rows, the second row, "the whole row", rows of benches. No quarrel-rows. |
| wind / Wind | all | the Path (noun) and its practitioners; the weather (ch11, 13, 18, 22, 29, 32, 33, 34, 40, 42, 46, 47, 58). No "wind up / wind back" verbs. |
| minute (121), record(s), subject, refuse, separate, object, content, polish, produce, entrance | — | all read naturally in context (nouns and verbs clear); ch52 "I will record that I was present" = ree-KORD. |
| sigil (ch60) | SIJ-il | carried. |

**"As" after the lanes' conversions.** All 345 ", as …" clauses were listed and read. Nearly all are habitual ("as he
was there every afternoon", "as he always broke it", "as she sat every week") or manner ("as a man tells a thing he has
told so often he could tell it asleep", "as polite as shopkeepers") and cannot be heard as "while". The temporal ones
are literal and correct (ch11 "as she moved her head", "as her foot slid forward"; ch14 "as they went down the tiers";
ch22 "as he came past the settle", "as he came down"; ch42 "as Fiske's weight was still going forward"; ch48 "as he
turned"; ch56 "as he sat"). **No fixes.**

**Accidental rhymes / repeats in adjacent sentences.** None worth a fix. "polite as shopkeepers" stands twice (ch16, kept
by lane A as the first; ch28 l.165, which lane A's report does not list) — no audio effect; noted for the ledger.

### 2.3 Formatting the narrator meets

- **Code block** (1): ch34 FRAGMENT ACQUIRED (Shadow-adjacent; §10, exact). `fpaudio.py` strips the fence, keeps each
  line and adds a full stop. Read as a notice, each line its own beat, brackets silent: "Fragment acquired. Unnamed —
  Shadow-adjacent. Duration: sustained. Integration: partial. Tier equivalent: Bronze. Note: presence-suppression
  component; movement-masking component. Contact-to-short range. Acquisition: directed. Engagement: adversarial,
  non-combat." Its own segment and a long pause (direction note 3).
- **`[SHATTERED]`** (1, ch2): inside Cael's italic answer to Bracken, with the narration saying "in brackets… as the
  station had written it". Brackets never voiced; the word plain. The spoken and narrated word elsewhere is plain:
  ch50 "*Shattered* was written in at that table" (and "the older word meant unbound", lower-case, once, as mapped).
  **`[unnamed]`** in the notice only. No other brackets in the book.
- **Strikethrough** (1, ch59 l.133): "*Frame fault, trial five. Correction preceded the audible release. ~~Capability
  exceeds classification.~~*" — markdown `~~` that `fpaudio.py` does not strip (it strips `*` only), so the tildes reach
  the engine. The struck words are protected ("struck once, legible") and the narration explains the stroke ("drawn a
  single line through three of the words… so that the words could still be read under it"). **Renderer requirement, not
  a text fix:** strip `~~` in the segmenter (or the renderer substitution table) and direct the struck sentence in a
  lowered, cancelled register; never voice "tilde".
- **The Log and the notebooks in italics.** The day entries, the inventories (ch21, ch37, ch62: six multi-line entries,
  each one paragraph), the working ledger (ch36, ch47, ch53, ch55, with its headings *Have / Spends / Risk / Won't
  share / Good for / Fails / Net*), the numbered lists (ch17 *One.–Four.*; ch23 the six refused methods; ch31 the
  four-part plan; ch49 *1.–5.*; ch50 *1.–4.*; ch53 *5.*), Karis's minute lines with initials (*L.: "You want it." C.:
  "Yes."*; *One. L. spends nothing. Why?*; *Minuted. One: … C. …*; *K. would like to say…*; *K.D.*), the chart's
  *see holder*, and the shorthand (*Day sixty-one — …*, after fix 4). Direct each as a document, each line its own beat;
  the initials as letter-names; the numbered lines as a list.
- **Numerals vs words.** The book writes nearly every number in words. The numerals that remain all read naturally
  except the four fixed in §3A: "41-7843-V" (ch2, the registry number: "four-one, seven-eight-four-three, V"); the
  fame tally "*29 of 91*", "*9 of 14*", "*5 of 11*", "*7 of 19*" (ch15); "*41 pages*", "a large *41*" (ch38–39);
  "*4 of 4*", "*311*" (ch42); "Priority Level 4" (ch49); the numbered Log lists. "Rank One", "Rank Two", "Copper Rank
  Eight", "Iron Rank Six" are all words; "Copper 2" on the board line (ch25) reads "Copper two". No "4TH"; "the 80th"
  (ch19) is fix 10, optional. No d-numbers (d144 etc.) appear anywhere in the manuscript.
- **Abbreviations.** None of Cu/Br/R1/wk/exch/unr/def/opp/equiv/Fri occurs. The one with no spoken form is "Instr."
  on the pinned minute (ch7, fix 1). "TA" (the teaching assistant; the Log's protected "*New TA in Gault's office…*"
  ch14 and the tally ch15) is the two letters, and ch15 decodes it ("A teaching assistant carried paper"). Initials:
  *K.* (Karis: Brom's pocket book ch1, her sign-off ch2, her margin notes ch33, ch35), *L.* and *F.* (Lira and Fiske in
  Karis's minute ch29, ch42), *C.* (Cael, the minute ch23), *K.D.* (ch34), *H.* (Hesk ch37), *W.* (Withrow ch48), *B.*
  (Bracken ch55), *Q.* (Quenna, ch55 Log), *S.* (Seln, the recess sheet ch62). Say the letter.
- **All-caps lines** (engines sometimes spell them): *COPPER* written on the board (ch6); *KILLED, NO SIGNAL* across a
  dead map (ch15); THE CORE MUST BE FREE BEFORE DECLARATION. CHECK THE PIN. (ch27, protected, unitalicised: flat, a
  plate); *READ FIRST* (ch31, ch34); *FIELD ASSESSMENT*, *READ THE NOTICE*, *CARRY THE LADDER* (Gwen's capitals, ch32,
  ch35); *AIMED* / *NOT* (the wash-house wall, ch36); *41 pages — tabbed — DO NOT RE-SORT* (ch39); *GROWTH* /
  *CONTROL* / *FIVE* (Karis's slate, ch43); *ON THE NUMBER* (ch53 ×2, ch54); Lira's capitals on Havel's page *Careful
  men go up. Doesn't tell you what he's careful FOR.* (ch46). Render in sentence case (renderer substitution, as Books 1
  and 2); no text change.
- **Em-dashes**: closed throughout; spaced " — " appears in letters, notes and board lines (ch25 "*Lira — Wind — Copper
  2 — …*", ch31 "*Gwen — Second Year — Current*", ch37 "*— H.*", ch55 "*— B.*", ch52 "*— Gault.*", ch45 "*Verify: three
  weeks' preparation — from what baseline?*", ch31 "— deferral, unit, the lot —"), in three protected spoken lines (ch7
  Withrow "Not the summary — the transcript", ch29 Fiske "It's the looking that matters — it was always the looking",
  ch56 Vastin "as you rise — I would encourage you"), and in the ch9 register aside ("*over* — the fourth-year's name —
  *Stone, Copper Six.*": the dashes bracket a narrator's aside inside a read document; give the aside the narrator's own
  colour, since fpaudio strips the italics that mark it). All pauses, never "dash".
- **Scene breaks**: 256, all correctly spaced. **Whitespace**: no trailing spaces, no tabs, no double spaces.
- **Paragraphs ending in a colon** (9: ch5, 15, 28, 38, 40, 41, 46 ×2, 49) introduce a Log line, a note or a sign in the
  next segment: a short pause, rising.

### 2.4 Line-level typos and grammar

- Doubled words: 7 "had had" (ch18, 23, 33, 42, 49, 59 ×2). All grammatical. No true doubles; no ", ,", "..", "?.",
  "the the", "in in" or any other pattern the script looked for.
- Broken joins: **none**. Each place the lanes cut or recomposed was read in place: ch15's one-sentence maps ("The
  first map was a clock… *Time is the wrong axis*"); ch17's retelling stopping at the overlay ("He did not walk them
  through the four dead maps"); ch18's cut fatigue page (the "*Discarded / cannot reach*" column stands whole); ch23's
  "the full run" with no swing count; ch30–31's hip calendar ("this morning she had stopped pretending", "By Third-day
  she meant to be back in hall one"; "Three days on the top line"; ch31 "at the sixth bell"); the rule-two wording in
  ch23, ch31 and ch34 (identical); ch40's "second month" ×2 and "sixty people"; ch45's added stake line ("Cael ate. In
  seven days…"); ch47's one-sentence anecdote; ch49's two folds (the name-led hand-off "Cael had spent the recess on
  that hard chair…" and Havel's logging inside his window, mark four kept); ch58's cipher-hand seam ("the fifth hand,
  the shorthand that had grown out of the cramped one"); ch59's "within minutes"; ch61's "All season"; every
  de-elevened figure (a dozen instruments, ten / tenth, thirteen feeds, nine movements, a dozen heartbeats, seven
  filings, Twelve., a quarter of an hour, seven crosses, fourteen questions, document fourteen, ten thumbnail marks,
  twelve minutes, "It took ten."). All sit clean; no mid-clause end, no lower-case start, no tense slip, no dangling
  comparison where a simile was cut.
- The one lower-case paragraph start is Seln's cipher line (ch58 "*unmarked file. one of three. probably the third.*",
  protected pattern); the nine paragraphs with no terminal punctuation end in colons (above).
- Spelling: British throughout ("colour", "favour", "apologise", "scandalised", "realised"); "realized" (ch2, ch8),
  "recognised" (ch14) both appear. No audio effect.

### 2.5 Paragraphs over about 700 characters

114 paragraphs (flattened: asterisks removed, whitespace collapsed, as the segmenter sees them). Listed only; none is a
defect, and `fpaudio.py` splits them at sentence boundaries. The direction file should mark the split so it does not land
mid-thought; the first sixty characters of each are given so it can be found.

| ch | chars | opens |
|---|---|---|
| ch01 | 717 | "I found four lines." She looked at him across the table, and … |
| ch01 | 716 | On the first morning back she had put him on the defensive flo… |
| ch01 | 725 | There were three places a repealed clause would have had to go… |
| ch05 | 731 | Persons on foot, two coppers. Persons with a pack beast, five.… |
| ch05 | 868 | Halcenvane stood along its top. The first thing he noticed was… |
| ch05 | 727 | Cael had braced himself for it since the bridge. The only othe… |
| ch06 | 769 | He walked the north edge first, where the three long halls sto… |
| ch06 | 953 | He had sixty-three entries from three days, and he went throug… |
| ch08 | 813 | They did not come all at once. They came in turn, a short exch… |
| ch08 | 725 | At the Ironyard, men twice his age had come off the boards sha… |
| ch08 | 760 | Her second touch found the other shoulder; she laughed, and wa… |
| ch08 | 836 | Brom tried things, and long after the touches had blurred toge… |
| ch08 | 844 | Brom's turn needed a read; that was its nature and its strengt… |
| ch08 | 824 | Ephram came off the wall with his weight forward and stopped t… |
| ch09 | 862 | Cael watched her read it. She went down the Copper column slow… |
| ch09 | 708 | The Crown yard ran differently on practice afternoons. The sun… |
| ch09 | 923 | The Rank Four came out hard, as Cael had seen half the Copper … |
| ch11 | 760 | He had watched the Lattice pupils four times, always from too … |
| ch11 | 788 | The low hall was one room, low-ceilinged as its name, with its… |
| ch11 | 777 | He lay in the dark and went back, as he had not been able to s… |
| ch11 | 782 | At the far end, where an old hitching post stood up out of the… |
| ch12 | 728 | It was not the room he feared; he had stood before two hundred… |
| ch12 | 790 | In the first, under a Shield instructor who crossed over at th… |
| ch12 | 745 | Fifty feet by thirty, the room was floored in oak laid on bear… |
| ch12 | 857 | Two weeks of asking had got him the names of nine pieces out o… |
| ch12 | 777 | "Three rules of this room. The first. When you reach something… |
| ch13 | 719 | He walked out onto the oak and found the crossing, two strips … |
| ch13 | 711 | He had never known how to describe the read to anybody who did… |
| ch14 | 772 | He worked out how before supper, because working out how was t… |
| ch14 | 754 | By the end of the hour there was the old flat greyness behind … |
| ch14 | 822 | He read it as water reads a hillside. Where would people go, a… |
| ch14 | 723 | The face was the thing, as he had once tried to tell a young o… |
| ch14 | 939 | Each door on the bluff had its card, eye-high in a little fram… |
| ch15 | 729 | The tally had taught him other things on the way, as tallies d… |
| ch15 | 718 | The other four in the wing were not strangers. They had read t… |
| ch16 | 704 | The bout went on. The Current girl took the first touch, and t… |
| ch18 | 797 | He had been taught the art in his third year by somebody else'… |
| ch18 | 708 | The boy had not looked up that morning. Seln had been sure of … |
| ch18 | 766 | "That's why it matters on a floor." He found he was leaning fo… |
| ch19 | 717 | Nobody had complained. He was certain of that, because the onl… |
| ch20 | 719 | Most read upward. Their eyes went from their own name to the n… |
| ch20 | 701 | Cael felt it go before he saw it: a fold low in his own hips, … |
| ch20 | 711 | It was not the hush of people who have been impressed. Impress… |
| ch21 | 1031 | "No," said Bracken. He laid his pen down square to the desk's … |
| ch21 | 759 | The commentary was good. Cael would have liked it to be worse.… |
| ch22 | 703 | Six weeks now Brom had belonged, every evening, to what the re… |
| ch22 | 753 | "Edran wanted a bout," she said. "I wanted a match. Neither of… |
| ch23 | 1079 | "I won't make the conditions. I won't set anything up to bring… |
| ch23 | 774 | "Minuted. One: conditions not to be manufactured; six methods … |
| ch23 | 736 | Of everything he carried, Reydan's fragment, the Compression-a… |
| ch24 | 883 | The Iron afternoon followed the Copper card, and Ephram fought… |
| ch25 | 732 | There had been a hall at Fenmark with a long table and a woman… |
| ch26 | 739 | The third went to Brom, ugly and short. He took three feeds fl… |
| ch26 | 958 | The first was nothing but this. Brom stood hardened, with the … |
| ch26 | 828 | The plan showed in the first exchange, and it showed most clea… |
| ch27 | 710 | Rooke came in while she was still crouched there. Nobody had s… |
| ch28 | 788 | Hall three (east), north bay, sixth bell, Third-day. Apparatus… |
| ch31 | 733 | He read it from the observation notebook, word for word, becau… |
| ch31 | 815 | "Position: it breaks nothing in the minute, because you didn't… |
| ch31 | 733 | "No. I don't." Brom looked up. "But if that's recruiting, it's… |
| ch31 | 778 | "It fits your reading. Other roads run through it too. I want … |
| ch31 | 708 | "An instrument doesn't change sides. It changes readings." She… |
| ch32 | 807 | He had read the boy's slate every morning since his second wee… |
| ch32 | 873 | The third was on the building's east face, round the corner, w… |
| ch32 | 798 | Then he went back round to the covered walk and climbed to its… |
| ch34 | 933 | Every other thing he carried had come to live somewhere inside… |
| ch35 | 759 | At the fourth bell the deferral went into the wing in his own … |
| ch35 | 844 | "Two," she said. "I have two of them. Two isn't a pattern. Two… |
| ch36 | 735 | He tried. He had been trying all morning, on the bed, and the … |
| ch37 | 862 | He thought about where he had been at the start of this half-y… |
| ch38 | 863 | Nobody had read it, and nobody needed to. Withrow's runner had… |
| ch38 | 833 | Somebody had cleared the long table to the bare wood and laid … |
| ch38 | 792 | Nine of them stood in a loose line under the lecture range's w… |
| ch39 | 1129 | Her chain of proof ran through thirty-odd volumes, from the fo… |
| ch39 | 846 | At Greyvane, Karis had spent eleven weeks proving a negative: … |
| ch39 | 955 | On the fifth afternoon Karis tested it. She did not ask anyone… |
| ch39 | 702 | He had met Havel twice. The first time was at Ardenmere, in th… |
| ch41 | 811 | "Think about what she's got," said Lira. She did not look at h… |
| ch41 | 718 | "Fiske told me to make them look." She said it slowly, laying … |
| ch42 | 744 | "Three hundred and eleven sheets," he said. "Every link in the… |
| ch43 | 722 | It had sounded like kindness, and Cael had carried it about fo… |
| ch43 | 709 | "The final. It's the nineteenth. They'll have been here a week… |
| ch43 | 709 | "Five." He said them as she wrote. "The Wind. The Pressure. Th… |
| ch43 | 715 | It was an ordinary supervised hour. The wing sent somebody to … |
| ch44 | 895 | Nothing moved. That was all, and every bit of it was hard. A b… |
| ch44 | 874 | The final stayed on the nineteenth, and the evaluation stayed … |
| ch44 | 826 | He did it properly. He had been trained to arrive at a place p… |
| ch44 | 757 | He had known it since the coast. He had sat at the end of the … |
| ch44 | 1054 | He looked at the courtyard. He took it in the way he had been … |
| ch44 | 755 | He wore the plain grey that inspectors wore on the road. At hi… |
| ch45 | 783 | He read the grey bundle first and all of it, from the top: the… |
| ch47 | 756 | So Cael told him, there on the landing, with his voice low and… |
| ch47 | 785 | He slept the nine hours and woke a little before the bell with… |
| ch48 | 841 | He thought of every hour he had worked under the wing that ter… |
| ch48 | 759 | "It works when the later law is silent about what it's sweepin… |
| ch48 | 796 | Cael watched every attempt with the gaze opened as far as he d… |
| ch49 | 705 | Cael had spent the recess on that hard chair, because a clerk … |
| ch49 | 738 | There were two sheets in it, and he knew them both. He logged … |
| ch49 | 729 | For a moment there was no sound in the hall at all. Then there… |
| ch50 | 900 | "I'm not saying anything about them at all." It came out quick… |
| ch50 | 715 | "That's all of it," said Karis. "I'm not asking who did it. I'… |
| ch53 | 1026 | "The wing posts its order for a semester sitting beside the Ma… |
| ch54 | 744 | The quadrangle was still grey when he crossed it, and so cold … |
| ch55 | 745 | In the gap after, while the panel conferred, he chose the Mire… |
| ch57 | 703 | "Those six words are the whole of it," she said. "The rest is … |
| ch58 | 744 | Of the form's five parts, four were furniture, and he had fill… |
| ch58 | 743 | He tried the first three the way the old man at the long table… |
| ch58 | 749 | "I said yes. He said, 'Records retention.' The box shifted ont… |
| ch59 | 853 | He had been watching people meet the thing they did not expect… |
| ch60 | 725 | Every morning since she came to the bluff, at the fifth bell, … |
| ch60 | 812 | It took four seconds. Nobody had ever told her that, either: t… |
| ch62 | 1074 | Six. Shadow-adjacent. Bronze. Presence-suppression; movement-m… |
| ch62 | 795 | That evening, in the third week, they had each held a road tha… |
| ch62 | 774 | There was one thing more. He knew what kind of thing it was be… |

### 2.6 Protected lines (checked, untouched)

Every BOOK_MAP §10 item was read in place: the enrollment record (ch5), Gault's baseline note (ch13), Seln's brief
(ch14), the first product (ch18; recompiled ch41), the plate (ch27), the incident report (ch28), the exception report's
close (ch28; ch41), the notice (ch34), the assessment-office note (ch35), Hesk's note (ch37), the notice of inspection
(ch38), the return and Ilsev's grounds (ch49), Ilsev's finding (ch49), the slip (ch53), Gault's evaluation note (ch55,
read in five paragraphs with the wing's additions between the mapped sentences), the charter subsection and the
twelve-by-fourteen room (ch56), Seln's quarterly (ch58), Vastin's notebook with its struck line (ch59), the file note
signed with his whole name (ch59), Lira's certification (ch60), the tournament clause beside *Interesting.* (ch61),
Hesk's reply framed as a guess and Vell's five sentences (ch62); and every spoken line and Log entry from "Told you it
would be soon." (ch4) to "Noted." and "The bluff held. The stamp was real." (ch62), including Quenna's prior-book
question answered "yes" (ch55 "*Answer, on the twentieth of Reaping: yes.*"). A flattened grep found all 14
`protected-patterns.txt` lines (each once, in its mapped chapter) and a sample of twenty §10 lines (the ones repeated by
design — "Still open. Still real. Patience." ×2, "Why retire a working method?" ×2, "An instrument doesn't change
sides…" ×3, "Because the clerk was standing where I'd have landed." ×2 — at their expected counts). None of the fixes in
§3 touches any of them.

---

## 3. Exact line fixes

### 3A — Required before render (8)

Each old string matches exactly once in its file and once in the manuscript; no new string occurs anywhere yet.

1. `manuscript/chapter-07.md`
   old: `*Instr. Rooke: the provision may be sound;`
   new: `*Instructor Rooke: the provision may be sound;`
   (The clerk's pinned minute, read by Cael at the board; "Instr." has no spoken form and an engine says "instr" or
   spells it. "Instructor Rooke" is the narration's own form two paragraphs above.)

2. `manuscript/chapter-15.md`
   old: `*TA, assessment office: 0 of 7.*`
   new: `*TA, assessment office: nought of seven.*`
   (Cael's binder tally; an engine says "zero". The book's word is "nought" — ch36 ×2, and "Nought," said Seln — and
   Book 1's fixes 10–11 set the precedent. The other tally lines, 29 of 91, 9 of 14, 5 of 11, 7 of 19, read as numbers
   naturally and stay.)

3. `manuscript/chapter-15.md`
   old: `*TA: 0 of 31.*`
   new: `*TA: nought of thirty-one.*`

4. `manuscript/chapter-15.md`
   old: `*Day sixty-one · second bell · hall three gallery · west end by the turned post · all floor, both doors.*`
   new: `*Day sixty-one — second bell — hall three gallery — west end by the turned post — all floor, both doors.*`
   (The shorthand is joined with middle dots, a symbol with no spoken form; `fpaudio.py` strips asterisks only, so the
   dots reach the engine, which may say "dot" or nothing. The spaced em dash is the book's own shorthand separator —
   the board line ch25, the sign ch31, the notes ch37, ch55 — and is a pause at render.)

5. `manuscript/chapter-15.md`
   old: `*Day sixty-two · fifth bell · yard · high west, middle of five · rings lengthwise, north stair, wing gate.*`
   new: `*Day sixty-two — fifth bell — yard — high west, middle of five — rings lengthwise, north stair, wing gate.*`

6. `manuscript/chapter-15.md`
   old: `*Day sixty-three · third bell · lecture stair · second landing, wall side · whole stair, top to foot.*`
   new: `*Day sixty-three — third bell — lecture stair — second landing, wall side — whole stair, top to foot.*`

7. `manuscript/chapter-25.md`
   old: `*Lira — Wind — Copper 2 — 6/0.*`
   new: `*Lira — Wind — Copper 2 — six and nothing.*`
   (The chalked standings line, the book's only slash between words; an engine says "six slash zero". The chapter is
   titled "Six and Nothing", the next sentence glosses "Six and nothing: six bouts unbeaten, none lost", and Cael says
   "Six and nothing." at breakfast. Book 1's slash fixes are the precedent. If the author prefers a figure on the board,
   `6–0` with an en dash is the next-safest form, but engines differ on the dash.)

8. `manuscript/chapter-36.md`
   old: `a large, plain *0*.`
   new: `a large, plain *nought*.`
   (Gwen's written count held up at the window; an engine says "zero" and the next line is `"Nought," said Seln`.)

### 3B — Optional, engine-safety only (author's call; 3)

A human narrator will read these correctly; a TTS engine or a listener relying on alternation may not. Not required.
Each old string matches once.

9. `manuscript/chapter-18.md` — an untagged speaker change that is not one.
   old: `"So I've looked for his. Nineteen days.`
   new: `"So I've looked for his," said Cael. "Nineteen days.`
   (The paragraph opens straight after Cael's own `"No. He doesn't."`, so alternation hands it to Karis for a sentence
   before the content — "I've looked… while I write down other people's bouts" — and the closing "He shook his head"
   return it. Two words settle it.)

10. `manuscript/chapter-19.md` — the book's only ordinal numeral.
    old: `*Floor issue, Sixth-day the 80th:`
    new: `*Floor issue, Sixth-day the eightieth:`
    (The narration two lines above says "the eightieth"; most engines say it right, as Book 1's "4TH" fix shows they
    do not always.)

11. `manuscript/chapter-22.md` — an en dash between numerals.
    old: `shelf-marks 40–60: two wrong.`
    new: `shelf-marks 40 to 60: two wrong.`
    (Karis's note under the door; "forty to sixty" is the reading, and some engines say "forty sixty".)

Not proposed, but flagged for the lexicon: "lead" in the window leading (ch7, ch17 ×3, ch34) stays LED against the
twenty-two LEED fighting uses — the phrases are fixed and the engine's context handling should carry them, but check the
render; "wound" (WOWND ×11) and the one WOOND (ch51); the bows (§2.2). And for the renderer, not the text: the `~~`
strikethrough in ch59 (§2.3).

---

## 4. Pronunciation lexicon (for the Breeze direction files)

Stress in capitals. "Owner-confirmed" = decision #33. "Carried" = the same entry in Book 1's, Book 2's or Book 3's
lexicon, unchanged. "Proposed" = BOOK_MAP §13 or this proof; not substituted at render until the owner confirms.
"Placeholder" = decision #11.

### People (33 named, plus the unnamed roles)

| Name | Say | Who | Status |
|---|---|---|---|
| Cael | KAYL (one syllable, as "sail") | the boy; "the assay one"; "Enrollee" | owner-confirmed #33 |
| Caelen Hesk-ward | KAY-len HESK-ward | his full name (ch2 "*Caelen Hesk-ward. 41-7843-V.*"); "Hesk-ward" as two words, stress HESK | carried (B1–B3) |
| Hesk | HESK | grandfather, Fen Street; letters signed "*— H.*" | carried |
| Lira | LEER-a | Wind; Copper Rank Two → Iron Rank One; "*L.*" in Karis's minute | owner-confirmed #33 |
| Brom | BROM (as "from") | Iron Skin, Copper; Rooke's cohort; "*B.*" nowhere (B. is Bracken here, ch55) | carried (B2, B3) |
| Karis Dellenmoor | KAIR-iss DEL-en-moor | Ember, Iron Rank Three; "Miss Karis" (Bracken, Seln); "*K.*", "*K.D.*" | carried (B3) |
| Quenna | KWEN-a | Greyvane assessor; "*Q.*" (ch55 Log) | carried (B2, B3) |
| Wray | RAY | Greyvane instructor (ch1–4, 8, 10, 20) | carried (B3) |
| Naveth | NAV-eth | Greyvane provost | carried (B3) |
| Prynn | PRIN | Greyvane archivist; the index; the shelf gap | carried (B3) |
| Hobb | HOB | Greyvane, the north mark (ch1, ch3) | carried (B3; owner-pending there, #12) |
| Edran | ED-ran | Glass; the rematch (ch3); "Third one someday." | carried (B3) |
| Vell | VELL | the Ardenmere ledger-keeper; her letter and mark (ch62) | carried |
| Coss | KOSS (as "moss") | the Warden of Book 1–3, named in memory only (ch2, 40, 44, 48, 57) | carried |
| Feryn | FERR-in | the Pressure's source, named in memory (ch13, 23, 34–37, 55, 62) | carried |
| Reydan | RAY-dan | the Compression's source, named in memory | carried (B2, B3) |
| Ilsev | IL-sev | senior evaluation seat of the delegation; "Assessor Ilsev" | carried (B1–B3) |
| Havel | HAV-el (short a) | records officer of the delegation; "the pear one"; not Halvern | carried (B2, B3) |
| Bracken | BRACK-en | registrar, Halcenvane; "*— B.*" (ch55); "the registrar" | proposed; the owner's flagged collision with Brom (#6) kept |
| Withrow | WITH-roh | chancellor, Halcenvane; "*W.*" (ch48) | proposed |
| Gault | GAWLT (as "fault") | Magister, the assessment office; "the officer of record" | proposed; keep distinct from Gwen |
| Rooke | ROOK (as "book") | the Blade instructor; "Instructor Rooke" (ch7 minute, after fix 1) | proposed |
| Ephram | EF-ram | Blade, Iron Rank Six, top of the Iron column | proposed |
| Fiske | FISK | Force, Copper Rank Eight, the holder; "the champion" (Ilsev's windows) | proposed |
| Merrick | MERR-ik | Shield, Copper Rank Four; Brom's semifinal | proposed |
| Tarn | TARN | Blade, Copper Rank Seven; the best short feeder | proposed |
| Nyle | NYLE (as "mile") | Stone, Copper Rank Five; the eleven seconds | proposed |
| Jask | JASK (as "mask") | Force third-year; the pin | proposed |
| Jessup | JESS-up | the records-broker (ch35, once) | proposed |
| Seln | SELN (one syllable, as "kiln" with an s) | Shadow, Bronze; the teaching assistant; "*S. Seln.*" (ch62) = "S., Seln" | proposed |
| Vastin | VAS-tin (as "fasten") | the Archmarshal; "the man", "the fourth chair", "the Archmarshal" in Cael's POV; named in narration ch38, 45, 59 | proposed; no age stated (#8) |
| Gwen | GWEN | second-year, Current; the unit; the eye | placeholder #11 |
| Abbot | AB-ut | Mire, Copper Rank Six; the ninth session (ch24, once; "the Mire boy" after) | placeholder #11 |
| the porter (of the Crown yard) / the Ash Path instructor / the Mire Path instructor / the Lattice instructor and her fifth-year pupil / the floor warden / the senior clerk / Gault's clerk / the desk clerk / the instrument woman (oil and brass) / the quiet woman from the wing (the board) / the fire-watch (the old man, the young man, the boy) / the Current lecturer / the Shield instructor / the old Stone master / the Gold fellow / the Shield fifth-year (forty-one wins) / the Current first-year (seventy-fourth) / the Stone fourth-year (ch9) / the delegation's counsel / the house's counsel (Withrow's) / the three clerks (the young one, the list clerk, the old one with the knee) / the four escort riders / the inky-knuckled clerk / the clerk with the cold / Bracken's young clerk / the safety instructor / the adjudicating instructor / the duty practitioner / the hatch woman / the outfitter / the laundry woman / the man at the kitchen gate / the lamp-man, the lamp-boy / the night porter / the paper-boy / the gate clerk / the provost's clerk / the stationer / the draper / Brom's grandmother, sister, mother / Gwen's aunt (Fenmark) / the man with the slate and the woman with the book (the station) / the two grey coats (the tall one, the stiff knee, the pair with the dog) | — | unnamed recurring roles | keep each a fixed colour across chapters; never name them (BOOK_MAP §13) |

### Places (24)

| Name | Say |
|---|---|
| Halcenvane | HAL-sen-vayn (three syllables; the -vane cluster is the owner's, #6) |
| Ostrand | OST-rand; the Ost = OST (the river) |
| Greyvane | GRAY-vayn; both syllables (carried, B3) |
| Denvash | DEN-vash (carried) |
| Ardenmere | AR-den-meer (carried) |
| Fenmark | FEN-mark (carried, B3) |
| Velmere | VEL-meer; both syllables (carried, B3; Brom's house, ch37) |
| Dellenmoor | DEL-en-moor (carried, B3) |
| Fen Street; Weighbridge Street | as written |
| the Ironyard | EYE-ern-yard (carried, B2/B3) |
| the Crown yard; the sunk floor; the tiers; the rail; the long board | as written; "the oak" = the floor |
| the bluff; the bluff road; the ferry landing; the road's foot; the bridge; the river street; the fish steps | descriptive; no stress |
| the covered walk; the north arch; the gallery; the second quadrangle; the wall; the wash-house; the post | as written |
| carrel eleven; the law range; the lecture range; the long reading room; the top-floor reading room | as written; "carrel" = KARR-el |
| hall one (the north hall, stone); hall three (the east hall, timber); the low hall (Lattice) | as written; the office's numbers are said aloud only in the Log and the floor issues |
| the assessment wing; the demonstration room; the copying table; the counter; the end office | as written |
| the records hall; the enrollment section; the charter archive; the east room (twelve by fourteen) | as written |
| the posting-house; the counting house (the registry station) | as written |
| the Continental (the tournament); the qualifying season; the registry; the Compact | as written |

### Terms and invented words (40)

| Term | Say / handle |
|---|---|
| Kindling, Kindled | KIND-ling (as in kindling a fire) (carried) |
| Arbiter | AR-bit-er (carried) |
| the Compact; the registry; the chain of review | KOM-pakt (noun) (carried) |
| sigil (ch60) | SIJ-il (carried) |
| [SHATTERED] (ch2, in a document) | SHAT-erd; brackets never voiced; "*Shattered*" plain (ch50) |
| unbound (ch50, once, lower-case) | un-BOUND; "the older word" |
| [unnamed] (the notice) | brackets silent |
| Archmarshal | ARCH-mar-shal; the rank; "the fourth chair" |
| Magister / Magistra | MAJ-iss-ter / MAJ-iss-tra (Gault takes the title; the Lattice instructor and the Mire instructor refuse it) |
| Path names: Wind, Pressure, Iron Skin, Blade, Force, Stone, Shield, Mire, Lattice, Current, Ash, Glass, Ember, Shadow, Tide, Compression | as written; "Wind" the noun; "a Mire", "a Lattice", "a Shield" = practitioners |
| -adjacent (Wind-, Pressure-, Iron-, Compression-, Ember-, Shadow-, Tide-adjacent) | ad-JAY-sent, light pause at the hyphen |
| Tiers: Copper, Iron, Bronze, Silver, Gold; -equivalent; -tier; "Rank One" … "Rank Eight"; "Copper 2" (ch25) | as written; ranks as words; "Copper two" |
| the assay provision; assay-provision enrollee; "evaluation by demonstration"; the baseline; the semester evaluation; the standing; renewed | ASS-ay (noun, stress first; "a mint word… a smith's word", ch1); the rest as written |
| the ladder; the brackets; the seeding; the top line; the holder; the brass stud; the standings; the season; the final; the crown | as written; "6/0" → "six and nothing" (fix 7) |
| First-day … Seventh-day; the eleventh of Sowing; the ninth … twenty-seventh of Reaping; the fifth, twelfth of the new month | as written; SOH-ing, REEP-ing; no English weekday at Halcenvane (Greyvane keeps Thursday, Tuesday, Wednesday, ch1–2, as Book 3) |
| the bells (first … eighth); the hours after the last bell (first … fifth); the glass (the sand-glass) | as written |
| TA | the two letters, "tee-ay" (ch14 Log, ch15 tally); decoded ch15 |
| K. / L. / F. / C. / H. / B. / W. / Q. / S. / K.D. | the letters; "L." and "F." = Lira and Fiske in Karis's minute (ch29, ch42); "B." = Bracken (ch55), not Brom |
| 41-7843-V | "four-one, seven-eight-four-three, V" (carried) |
| the Log (the Power Log); the observation notebook (the "coat-notebook"); the binder; the grey notebook; the marbled book (the watcher log); the shorthand; the working ledger | document titles where context marks them |
| the gaze; the read (REED); the surface read; the reach; the stub; the well, the cup, the purse; the landing beat; the burst; the framework; the toll; the half-breath; the hip line | Cael's and Lira's terms; no stress |
| the hold; the stake; the corner; the edges; "ordinary"; the rent; the drift; "thin" | the Shadow ledger's terms (ch36–57) |
| the seam; the stall; the redirect; the turn; the hardening; the drive; the feed (honest / empty / cheap); "the taking-apart"; the nineteen (exercises) | Brom's and Rooke's terms |
| the pane; the anchor; the sheen; the frame (Lattice: three points, "One, and set"); the shell (Glass); the slick, the placing (Force); the ride (Current) | the Paths' workings |
| the frame (the drop-frame); the rail; the pawl; the notch; the plate; the shutter-board, the louvres, the drum; the pendulum; the brass (the grid); the crossing; the chalk tray; the vessel (the copper pot, the glass straw); the posts (the resistance posts), the core, the pin, the dial | the wing's apparatus; "the frame" is both the Lattice working and the apparatus — context marks it |
| the slate (Cael's, the fire-watch boy's, the unit's, Karis's); the board (the residence board, the main board, the woman's board) | as written |
| the enrollment record; the half-sheet; the floor issue; the floor sheet; the carbon; the docket; the requisition; the exception report; the product; the quarterly; the filing; the return; the referral; Priority Level 4; Suppression-Advisory Watch | as written; "Level four" |
| the minute; the covenant; the procedure; rule two; "earnest engagement"; "awake and directed"; "the subject begins himself" | as written |
| the fire-watch; the oil book; the quarter-sheet; the counting lock; the sweep; a named room | as written |
| the standing eight; sampled; structural; "the fame tally"; the control column; the overlay; the fifth map | Cael's method |
| "Nobody talks about hips."; "Count the half-second."; "Be dull."; "Correct filing."; "Thank you for the form." / "Mm." | refrains; keep each in its owner's colour |
| marks, coppers, silver marks; the toll; the purse | currency |
| the hearth, the settle, the good lamp, the good chair, the pear fork | the residence |

Lexicon size: 33 named people (plus the unnamed-role group), 24 places, 40 terms — **97 entries**.

---

## 5. Direction notes the segmenter and instruct files will need (not text changes)

1. **Keep Cael = KAYL and Lira = LEER-a** in every chapter direction (#33).
2. **POV cutaways**: the "he/she" changes referent at the `---`. Seln: ch14 s3–s4, ch18 s1–s2, ch28 s1–s3, ch30 s1,
   ch41 s1, ch58 s1–s2. Lira: ch25 s2, ch42 s3, ch51 s1 and s4, ch60 s2–s3. Havel: ch44 s2–s3, ch46 s2, ch49 s4, ch51
   s3, ch57 s5. Vastin: ch45 s2–s4, ch59 s2–s6. Ilsev: ch47 s3, ch49 s1–s3, ch52 s1, s4 and s6. One hand-off inside a
   section: ch49 s3 passes from Ilsev to Cael at the name-led paragraph "Cael had spent the recess on that hard
   chair…" (lane B's fold) — mark it at the paragraph. The notice (ch34) and the documents have no POV: flat, exact.
3. **Notices and brackets**: a neutral system cadence for the one fenced block, its own segment with a long pause; never
   voice brackets, fences, asterisks, tildes or the `---`. "Shattered" plain where it is said (ch50).
4. **The ch59 strikethrough**: strip `~~` before synthesis (the segmenter or the renderer substitution table) and read
   "*Capability exceeds classification.*" in a lowered, cancelled register; the narration has already said it was
   struck "so that the words could still be read under it".
5. **Italic documents**: give the Log, the notebooks, the minute, the chalk, the letters, the notices and the certificates
   a slight register change and return cleanly at the next prose cue; the salutations and sign-offs ("*— H.*", "*— B.*",
   "*— Gault.*", "*K.D.*", "*S. Seln.*") are pauses and letter-names, never "dash". The ch9 register aside ("*over* —
   the fourth-year's name — *Stone, Copper Six.*") takes the narrator's own colour between the dashes.
6. **All-caps** (§2.3: the plate ch27, the dead map ch15, READ FIRST, Gwen's and Karis's capitals, AIMED / NOT, ON THE
   NUMBER, DO NOT RE-SORT, Lira's FOR) in sentence case; the single letters by name.
7. **Counts**: preserve the slow count architecture — Lira's thirty (ch10), the Lattice "One, and set" (ch11), the
   calls "*left*, *round*, *low*" / "*late*, *late*, *on time*" (ch19), Brom's exercise counts at the post, the
   table's bout calls, Bracken's "Sixteen?" / "Sixteen." (ch57), the numbered Log lists (ch49, ch50), the glance tally
   in ch55 ("Gault: twice… The fourth chair: once").
8. **Collisions by register**: Gault flat and exact, Bracken dry and precise, Withrow level and unhurried, Rooke flat
   with no lift at the end, Seln pitched for a counter at the dullest hour, Vastin even and without weight, Ilsev
   exact, Havel careful, the counsel low and pleasant and never stopping, Gwen's whisper that carries. Give Gault its
   long aw and Gwen its short e wherever both are in a scene (ch32, 38, 58, 59); Bracken its two syllables beside
   Brom (37 scenes); Halcenvane its three beside Greyvane.
9. **Homographs**: "the read" = REED; "lead foot / arm / leg" = LEED against "the lead of the window-pane" = LED (ch7,
   17, 34); "wound" = WOWND (11) and the one WOOND (ch51); "a flat bow" = BOH (ch28) against "a little bow", "did not
   bow", "not to bow" = BAU (ch36, 44, 52); "a live thing / live hazard / remains live / stayed live" = LYV (ch6, 27,
   30, 49, 60); "a tear in the lining" = TAIR (ch20), "tears" = TEERS (ch29); "a present" = PREZ-ent (ch37, 53).
10. **Interruptions**: the `—"` cut-offs (§2.1) want the engine's short gap and no falling cadence. "Mm." / "Hm." /
    "Huh." — check they survive the render; Seln's "Mm" is load-bearing (ch36, 58, 62).
11. **Multi-paragraph speeches** (ch55 Gault's note; ch56 Cael ×2 and Vastin; ch61 Withrow ×2): one voice across the
    paragraphs, no closing cadence until the last.
12. Long paragraphs (§2.5) may be split only at sentence boundaries, as `fpaudio.py` does; mark the split so it does not
    land mid-thought, especially in the bout paragraphs (ch8, ch26, ch29, ch42, ch51–52), the sittings (ch48–49) and
    the year's inventory (ch62, the book's longest paragraph).
