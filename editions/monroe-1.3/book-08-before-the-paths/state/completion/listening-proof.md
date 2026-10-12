# Book 8 — *Before the Paths*: line-and-listening proof (merged record)

Completion pass Step 4. Four independent full-text proofs on Sol (gpt-5.6-sol via Codex, ChatGPT plan), each with fresh context, run 2026-10-12 against the text as it stood after the texture lanes and the coordinator's two restorations (commit 49688a8).

| Part | Chapters | Scenes | Tokens used | Verdict | Required fixes | Optional fixes |
|---|---|---:|---:|---|---:|---:|
| 1 | 01–15 | 78 | 394,980 | PASS — render-ready | 0 | 0 |
| 2 | 16–30 | 80 | 320,640 | PASS — ready to lock | 0 | 0 |
| 3 | 31–45 | 82 | 317,890 | PASS — render-ready | 0 | 0 |
| 4 | 46–60 | 84 | 352,233 | PASS — render-ready | 0 | 0 |

## Coordinator's check of the reads (Claude Opus 5.5)
- **Coverage.** Each notes file (`listening-notes-part1.md` … `part4.md`) gives the first six and last six words of every scene. The coordinator computed the same words from the manuscript for all 324 scenes (264 breaks and 60 chapter openings) and found both ends of every scene verbatim in the notes: 324 of 324. All four runs are accepted as full reads.
- **Lane joins.** Every join that the two lanes and `LANE-RULINGS.md` sent for a second ear was reread in context by its part and ruled sound, including the two lines the coordinator restored (ch28:283; ch36:191).
- **ch60, "the old man"** (Hesk beside the letter, then Vastin fifty lines on; LANE-RULINGS, Lane B ruling 4): part 4 rules that the two do not blur by ear. No substitution is made.
- **One coordinator line fix after the proofs.** Part 3 reported the book's only Arabic numeral outside chapter headings, in Cael's own log at ch36:375 ("Night of the 291st."), and classed it as visible record text. Every other record in the sixty chapters writes its numbers out, so the coordinator spelled it: "Night of the two hundred and ninety-first." The line is the author's own (a scene new to this edition), not a protected unit. Overlap and gates were re-run for Movement 6 afterward (0 unprotected; gates 0). No digit now stands anywhere in the body of the book.

## Renderer notes carried to the lock file
- Single initials (`C.`, `K.`, `V.`, `S.`, `H.`, `L.`) are letter-names; the letter's sign-off "— C." is the letter "C", dash and stop silent. `HOLD` is spoken as the word, in sentence case. `[UNBOUND]` and `[SHATTERED]` are spoken with brackets silent.
- "read" is REED for the noun and the present tense and RED for the past; "the read" is always REED. "bow" is BOH for the weapon and for Teague's broad man, BAU for a boat's prow and a courtesy. "lead" is LED for the cord's weight and LEED for the verb. "Wind" the fragment and "wind" the weather are both short-i; "wind her" on the drum is WYND.
- The chronicle line keeps its dashes as light pauses. The roman word inside an italic unit (ch41 "withdrawn"; ch51 "someone made this") flattens to ordinary prose.
- Paragraphs over about 700 characters (27 in all; listed in each part) are split only at sentence boundaries.
- Pronunciation lexicons: one in each part below (Cael = KAYL and Lira = LEER-a are owner-confirmed).

The four proofs follow in full, unedited.



---

<!-- PART 1 -->

# Book 8 — *Before the Paths*: line-and-listening proof, part 1

Scope: `manuscript/chapter-01.md` through `chapter-15.md`, read in full and in order from complete numbered printouts. Per-chapter and per-scene evidence, including exact first and last six words for all seventy-eight scenes, is in `state/completion/listening-notes-part1.md`.

This proof follows Book 7's merged proof structure and applies the Book 8 completion plan, whole-arc read, pass brief, both texture-lane reports and the coordinator's rulings, the edition's audio and Reader Standards, the cited owner decisions, BOOK_MAP §§9–10, `protected-patterns.txt`, and the narrator behavior in `audio/fpaudio.py`.

No manuscript file was modified. No Git command was run.

## Verdict

**PASS — RENDER-READY, with no required or optional text fix.** Chapters 01–15 contain no quotation, speaker-attribution, ear-collision, narrator-formatting, typo, broken-join, numeral or continuity defect that warrants changing the manuscript. All protected text encountered in the range is intact.

## Findings by category

### 1. Quotation marks and speaker attribution

Straight quotation marks are balanced in every prose paragraph. There are no curly quotation marks, no quotation pair abutting without a beat, and no multi-paragraph speech that depends on an intentionally open paragraph.

The Lowmarch councils, Pike's bench readings, the fence, silent-yard bouts, ice-road rescue, Thornwater work, ferry set piece, Vastin's arrival and long-table examination, and the cut fight remain attributable by tag, position or stable role. In particular:

- Teague's `boy` or `young one` is never confused with Cael. The ferryman's boy and the tally-stick boy are each qualified by setting before they speak.
- Teague's tall spear-carrier remains a man, the broad man remains `the bow`, and the lean old woman remains distinct from Oryn.
- The factor, ferryman, keepers, carters, broker, clerk, patients and woman with the hide are stable unnamed roles and never exchange voices invisibly.
- Pike's spoken readings are announced or framed; replies from the meadow do not sound like part of a slip, board or ledger line.
- Oryn's patient speech, self-directed work speech and speech to the room stay distinct. Every treatment permission or refusal has an audible answer.
- Vastin's formal clauses and self-corrections remain in one voice; his low or clipped replies are anchored before another speaker enters.
- The tagless chapter-10 close, `Why us.`, is unmistakably Lira's from the two preceding sentences.

No quotation or attribution fix is required.

### 2. Ear collisions, homographs and bare `as`

No name collision requires a text change. Direction should keep these recurrent clusters separated:

| Pair or cluster | Direction |
|---|---|
| Cael / Karis | KAYL versus KAIR-iss. |
| Seln / the Stair | SELN versus ordinary STAIR. |
| Teague / Treswick / Ternhall | TEEG, TRESS-wick, TERN-hall. |
| Oryn / Ostrand | OR-in versus OST-rand. |
| Lowmarch / the Fallow / hall | LOH-march, FAL-oh, ordinary HALL. |
| Lira / Line / leaf / lean | LEER-a, LINE, LEEF, LEEN. |
| Pike / Hesk / Vastin / Brom | PYKE, HESK, VAS-tin, BROM; keep each clipped and distinct. |

Homographs are clear in context and belong in direction:

| Word | Intended reading in chapters 01–15 |
|---|---|
| `lead` | LEED, the verb, in both occurrences. |
| `wound` | WOWND for the cart and line wound in on the drum; no WOOND noun occurs. |
| `close` | KLOHS as adjective, adverb or noun; KLOHZ when fingers close. |
| `read` | REED for present tense and Cael's perceptive faculty; RED for narrated past and perfect forms. `the read` is always REED. |
| `tear` | Does not occur as a standalone word in this range. `tearing` is the ordinary TAIR-ing form. |
| `live` | LIV in `keep the live from going after it`. |
| `wind` | WIND for weather, breath and the Path; WYND for the drum/boat command `Wind her` and `nothing to wind`. |
| `bow` | BOH for the weapon and Teague's broad man; BAU for a boat's prow and Vastin's courtesy bow. |
| `row` | ROH throughout, including rows of records. |
| `minute` | MIN-it for time, a record and the verb meaning to enter in minutes. |
| `lean` | LEEN throughout. |
| `leaf` | LEEF throughout, for a page and for the water comparison. |
| `flat` | FLAT throughout, including the courier's leather case. |
| `bar`, `mark`, `set`, `still` | Ordinary contextual readings; none creates a plausible alternate sentence. |

No bare `as` can be heard as “while” in a way that changes agency, order or meaning. No ear-collision fix is required.

### 3. Formatting the narrator meets

Formatting is sound after the transformations in `fpaudio.py`:

- All italic markers are balanced. Cael's logs, inventories, trial entries, Karis's findings and receipt, Pike's lines, the chronicle citation, the clearance slip and the letter remain intelligible when asterisks are removed.
- The chapter-12 chronicle citation keeps its dashes. Lira's reading of the technician's sheet alternates cleanly with her own words; the Compact date is described but never printed.
- Internal roman/italic changes in mixed prose and dialogue are paired. No italic acquisition unit occurs in this range; the eleventh, twelfth and thirteenth remain outside scope.
- There are no Arabic numerals in manuscript narration or displayed material in chapters 01–15. Days, marks, distances, cordage, stake counts, breaths, sheets and deployment counts are all words.
- `C.` and `K.` are letter-names. `HOLD` is spoken as the word in sentence case. Italics and punctuation marks are silent.
- There are no code fences, backticks, bracketed all-caps forms or indented code in the range.
- Every `---` has a blank line before and after and should receive the specified long pause.
- No named season, month, month order or English weekday appears. `cold term`, `first snow` and `thaw` are lawful events or intervals. No metric unit appears.

No narrator-formatting fix is required.

### 4. Typos, broken joins, restored units and continuity

No accidental doubled word, lower-case sentence start, mid-clause ending, dangling comparison, cut-off antecedent or viewpoint-illegal name remains. The repeated-word probe found only seven intentional `had had` constructions.

The numerical chains are coherent in this range:

- Deployment: twenty-seven → twenty-eight → twenty-nine → thirty.
- Purse: ninety-six → seventy-six → a hundred and sixteen → a hundred and eighteen.
- The fence, shale-back, silent-yard, river rescue, ferry, survey-sheet and eight-hound counts agree with their echoes.

The restored protected-unit joins are sound:

- **ch05 ruler rule:** `She said it again then, to the table.` → protected ruler sentence → `Nobody answered her.`
- **ch06 west/Treswick speech:** `Karis answered him without looking away from the map.` → protected speech → Seln's named reply, `It has a gate, with a book in it`.
- **ch09 recognition:** the ordered survey of the landing → `Cael knew the stance before he knew the face.` → the Ostrand memory that explains the recognition.
- **ch09 Seln/Vastin line:** the description of how the man stands → Seln's protected naming line → the sentence establishing that he spoke low and to nobody on the planks.
- **ch12 Oryn direction:** Karis completes her order → Oryn's protected `She's right` direction → the sentence confirming it was Oryn's first speech to Cael since noon.
- **ch13 clearance slip:** the drawing beside the words → protected italic slip → Pike's named price statement.

The texture-lane second-ear joins in range are sound:

- **ch13:** Pike's `They never do; they'd have to pay more.` moves directly to Cael's second reading; the rereading supplies the beat removed with the silence tag.
- **ch14:** Vastin's long speech moves to `He was a little out of breath...`; he is the only possible referent, and Cael's answer resets the voice.
- **ch15:** `That was what stopped him.` stands cleanly between the Ember judgment and `They would not have turned.`

No typo, join or continuity fix is required. No protected line, log, leaf, chronicle line, slip, ledger, letter or closing prose should be changed.

### 5. Paragraphs over about 700 characters

| Chapter:line | Characters | Opens |
|---|---:|---|
| ch06:257 | 716 | `"It's west," she said. "Treswick. The last Compact city...` |
| ch07:85 | 716 | `"Under the book." Seln put one finger on the wood...` |
| ch10:25 | 724 | `Cael turned the four sentences over while the stick...` |
| ch10:213 | 763 | `"Then you will understand me the more readily when...` |
| ch12:123 | 702 | `"I do not know. I held it to a window...` |
| ch13:59 | 771 | `"It's the same road, and I can read...` |
| ch15:101 | 900 | `Everything that he owned came to him then at once...` |

## Exact line fixes

### Required (0)

None.

### Optional (0)

None.

There are no old strings to verify for uniqueness and no proposed replacement to submit to the eight-word overlap gate.

## Pronunciation lexicon

Only names and terms occurring in chapters 01–15 are included. Shared pronunciations are carried from earlier books; Book 8 additions are marked proposed.

### People

| Name | Say | Identification | Status |
|---|---|---|---|
| Cael | KAYL, one syllable | log-keeper; carries the fragments | owner-confirmed #33 |
| Lira | LEER-a | Wind, Iron Rank One | owner-confirmed #33 |
| Brom | BROM, as in “from” | Iron Skin; builder and load-bearer | carried |
| Karis | KAIR-iss | Ember; researcher and recorder | carried |
| Seln | SELN, one syllable | scout and former reporting officer | carried |
| Hesk | HESK | Cael's grandfather; author of the book and clock | carried |
| Reydan | RAY-dan | source of Compression | carried |
| Daeva | DAY-va | source of Storm | carried |
| Ephram | EF-ram | source of Blade; recipient of Cael's letter | carried |
| Rooke | ROOK, as in “book” | instructor named in the letter | carried |
| Pike | PYKE | one-armed Lowmarch ledger-keeper | carried B7 |
| Teague | TEEG, one syllable, hard final *g* | independent crew captain | carried B7 |
| Oryn | OR-in | Tide healer and route-keeper | carried B7 |
| Vastin | VAS-tin, as in “fasten” | former Archmarshal | carried |

### Places

| Name | Say | Status |
|---|---|---|
| Lowmarch | LOH-march | carried B7 |
| Thornwater | THORN-waw-ter | carried B7 |
| Ostrand | OST-rand | carried |
| Denvash | DEN-vash | carried |
| Ardenmere | AR-den-meer | carried |
| Ternhall | TERN-hall | carried |
| the Fallow | FAL-oh | carried B7 |
| the Stair | STAIR | carried B7; the Quieting site/road |
| Treswick | TRESS-wick | proposed B8; keep distinct from Teague and Ternhall |
| the Deepstacks | DEEP-stacks | proposed B8; one compound place-name |

### Creatures, Paths and working terms

| Term | Say / handle | Note |
|---|---|---|
| stillhound | STILL-hound; one compound | the grey road-hunting animal |
| shale-back | SHAYL-back; one compound | the high-country animal |
| Kindling | KIND-ling | carried |
| Arbiter | AR-bit-er | carried |
| Compact | KOM-pakt | ordinary word; institutional name when capitalized |
| Architect | AR-ki-tekt | title, not a personal name |
| the Line | LINE | western boundary; keep distinct from Lira |
| Path; fragments | ordinary words in the story's technical senses | slight stress only where contrast requires it |
| Wind | WIND | Path name; use WYND only for the drum/boat verb |
| Pressure | PRESH-er | fragment name |
| Iron; Iron Skin | EYE-ern; EYE-ern SKIN | fragment/Path terms |
| Compression | kum-PRESH-un | fragment name |
| Ember | EM-ber | fragment and Karis's Path |
| Shadow | SHAD-oh | fragment and Seln's Path |
| Storm | STORM | fragment name |
| Anchor | ANG-ker | fragment name |
| Blade | BLAYD | fragment name |
| Force | FORSS | Path name |
| Tide | TYDE | Oryn's Path |
| the read | REED | Cael's perceptive faculty |
| Tiers and ranks | Copper, Iron, Bronze, Silver and Gold as ordinary words | no displayed digits in this range |
| marks; coppers | ordinary words | currency |
| feet; yards; miles; paces; strides; cords | ordinary words | approved measures used in the range |
| `HOLD` | “hold” | visible board instruction; do not spell the letters |

## Direction notes for segmentation and render

1. Preserve one manuscript paragraph per audio segment and render every `---` as the long pause.
2. Give logs, letters, slips, leaves, ledger lines, inventories, receipts and copied record passages a light document register; do not voice markdown.
3. Keep Pike's public board-reading voice distinct from replies at the bench or in the meadow.
4. Keep Teague's four roles fixed: Teague; the tall man with the spear; the broad man called `the bow`; the unnamed young one. Do not turn `the boy` into Cael.
5. Observe the homograph table, especially BOH/BAU, WIND/WYND and REED/RED.
6. Split the seven long paragraphs only at sentence boundaries if the audio engine requires it.


---

<!-- PART 2 -->

# Book 8 listening proof, part 2

Range: `manuscript/chapter-16.md` through `manuscript/chapter-30.md`.

## Verdict

**PASS — ready to lock for this range.**

All fifteen chapters were read in full, in order: eighty scenes and 76,215 words. No required or optional line fix is warranted. The text is intelligible in a single narrator voice after the audio flattener removes Markdown emphasis, and every long-pause break falls at a sound scene boundary. Protected language remains untouched.

The binding scene-by-scene coverage record, including exact six-word scene openings and closings and the second-ear rulings on protected/restored joins, is in `state/completion/listening-notes-part2.md`.

## Findings by category

### 1. Quotation marks and speaker attribution

- No unbalanced or mismatched quotation marks were found. No two repaired quotations abut as an unmediated `.” “` scar.
- The council-like working scenes at the fork-stone, Treswick loft, cook-house, registry counter, lower gallery, and shared tables remain followable by ear. Karis's exact speech, Vastin's formal clauses, Cleon's rough clipped instructions, and Seln's mild interventions have distinct syntax as well as adequate tags or action beats.
- Pike's written slips are consistently introduced as writing or as something read. No slip is mistaken for present dialogue.
- Oryn's patient speech remains attributable through questions, permissions, instructions, self-address, and speech directed to a room. No answer to an implied or explicit request is orphaned.
- The unnamed factor, keepers, clerks, carters, yard-man, porter, and working voices retain enough local physical or occupational anchoring. In this range, `the boy` at the registry is audibly Cael; Teague's unnamed young one is not present.
- Tagless protected turns are sound. In particular, `Do we now?` in chapter 23 is Cael between two Karis turns, and `Four. / Right.` in chapter 26 is resolved by the following sentence naming Cael as the person who supplied the figure.
- All lane joins identified for chapters 16–30 were heard in context and ruled sound. The coordinator-restored Shadow sentence in chapter 28 has a clear subject on both sides.

### 2. Ear collisions and homographs

- No name collision creates an attribution error. Cael/Karis/Cleon, Seln/the Stair, Oryn/Ostrand, Lowmarch/Millrace, the Fallow/the Hall, and Lira/line/leaf/lean remain distinguishable through rhythm and context. The closest deliberate pair is `The Fallow has it. The hall has it.` in chapter 17; two syllables for Fallow and one for hall keep the contrast audible.
- `read` is REED for the noun/present-tense sense and RED for past/perfect constructions. The grammar resolves every occurrence, including `I read your file` in chapter 21, which is RED.
- `Wind` as a named fragment and ordinary weather `wind` are both short-i WIND; capitalization need not be performed. `bow` in this range is the weapon, BOH. `row` is ROH. `minute` is MIN-it. Noun `wound` is WOOND.
- `close`, `flat`, `bar`, `mark`, `set`, `still`, `leaf`, and `lean` occur in ordinary contextual senses and do not require a performance intervention. No bare `as` creates a consequential “while” ambiguity.
- `[UNBOUND]` and `[SHATTERED]` should be voiced as “unbound” and “shattered,” with brackets silent. `L.`, `S.`, and `V.` are letter names; they should not be expanded.

### 3. Formatting the narrator meets

- Italic thoughts, Path prompts, visible records, read-aloud text, and Cael's logs all remain intelligible after `fpaudio.py` strips emphasis. No code block occurs in the range. The eleventh, twelfth, and thirteenth acquisition units occur outside chapters 16–30.
- The repeated `Deployment since the Line: thirty-two.` line is intact wherever it appears. The purse is a hundred and thirty-eight before lodging and a hundred and thirty-six afterward. The sheet, hand, corner, day, distance, and stair counts agree with their echoes.
- The chapter 24 card is correctly framed as Lira reading italic words inside her own quoted speech. Hesk's book entries and Karis's quoted form language retain their boundaries after flattening.
- No Arabic numeral appears in narration or dialogue; the only digits are the chapter numbers in Markdown headings.
- No stray Markdown, unbalanced asterisk, or malformed `---` spacing was found. Every scene break has a blank line before and after and will become the intended long pause.

### 4. Typos, broken joins, and continuity

- No typo, broken repair join, mid-clause stop, accidental lower-case start, dangling comparison, or severed pronoun was found.
- A repeated-word scan found only intentional constructions such as `had had` and the deliberate calming call `easy, easy, stand`.
- The chapter 23 whole-arc fix (`whole way round`) reads naturally in its scene.
- The chapter 28 sentence restored by the coordinator reads cleanly between the seven-bowl meal beat and Cael opening Hesk's book.
- Viewpoint knowledge remains controlled: Cleon is named only after introduction; unnamed registry workers stay role-bound; no Teague-crew identity leaks into this range.
- Deployment holds at thirty-two throughout these chapters. Purse continuity holds at a hundred and thirty-eight, then a hundred and thirty-six. No date, season name, month name, English weekday, or disallowed unit has entered the prose.

### 5. Paragraphs over about 700 characters

Character counts below use narrator-facing flattened text (Markdown emphasis removed and internal whitespace collapsed). These are the only paragraphs over 700 characters in the assigned range.

| File | Line | Characters | Opening |
|---|---:|---:|---|
| `manuscript/chapter-16.md` | 197 | 706 | `He had gone back over it a dozen times since the ice…` |
| `manuscript/chapter-16.md` | 205 | 756 | `The man had come out of the long house with his copper spent…` |
| `manuscript/chapter-16.md` | 249 | 701 | `Beyond the cut's head the ruts came out onto the open shoulder…` |
| `manuscript/chapter-18.md` | 29 | 736 | `He did not ask himself what it meant…` |
| `manuscript/chapter-21.md` | 101 | 715 | `"It began with a day, and a word in square brackets…` |
| `manuscript/chapter-21.md` | 113 | 710 | `"Four feet. I measured it, as I measure everything."…` |
| `manuscript/chapter-21.md` | 151 | 701 | `He had wanted that answer for four days…` |
| `manuscript/chapter-25.md` | 71 | 802 | `She had met one body in which ten ran together…` |
| `manuscript/chapter-25.md` | 101 | 726 | `"A hand is a thing that a clerk looks at…` |
| `manuscript/chapter-26.md` | 75 | 877 | `He had been looking at a town. He ought to have been looking at her…` |
| `manuscript/chapter-28.md` | 95 | 743 | `Cael went over it, standing there with a box on his back…` |
| `manuscript/chapter-30.md` | 273 | 746 | `"You've been reading the strata. Old, older, oldest…` |

## Exact line fixes

No line fixes are proposed.

- **REQUIRED:** none.
- **OPTIONAL:** none.

There are therefore no old strings to verify for unique replacement and no overlap-gate exposure introduced by this proof.

## Pronunciation lexicon

Shared entries carry forward the earlier-book pronunciations; Book 8-specific entries are marked as such.

| Name or term | Narrator pronunciation | Note |
|---|---|---|
| Cael | **KAYL** | Owner-confirmed. One syllable. |
| Lira | **LEER-a** | Owner-confirmed. Two syllables. |
| Brom | **BROM** | Carried forward. Short o. |
| Karis | **KAIR-iss** | Carried forward. Stress first syllable. |
| Seln | **SELN** | Carried forward. One syllable. |
| Oryn | **OR-in** | Carried forward. Stress first syllable. |
| Vastin | **VAS-tin** | Carried forward; first syllable as in “fast” with v. |
| Cleon | **KLEE-on** | Book 8 entry. Two syllables. |
| Pike | **PYKE** | Carried forward. One syllable. |
| Hesk | **HESK** | Carried forward. One syllable. |
| Ostrand | **OST-rand** | Carried forward. Stress first syllable. |
| Lowmarch | **LOH-march** | Carried forward. Stress first syllable. |
| Oxhollow | **OKS-hol-oh** | Carried forward. Three syllables. |
| Denvash | **DEN-vash** | Carried forward. Stress first syllable. |
| Treswick | **TRESS-wick** | Book 8 entry. Stress first syllable. |
| Velmere | **VEL-meer** | Book 8 entry. Stress first syllable. |
| Millrace | **MILL-rayss** | Ordinary compound; stress first syllable. |
| the Fallow | **FAL-oh** | Two syllables; distinguish from `the Hall`. |
| the Hall | **HAWL** | One syllable. |
| the Stair | **STAIR** | One syllable. |
| the Line | **LINE** | One syllable; capitalized world term. |
| the Compact | **the KOM-pakt** | Noun stress on first syllable. |
| Path | **PATH** | Broad a as in standard American “path.” |
| sigil | **SIJ-il** | Soft g; stress first syllable. |
| Kindling | **KIND-ling** | Named Path term; ordinary English pronunciation. |
| Ember | **EM-ber** | Named fragment; stress first syllable. |
| Wind | **WIND** | Named fragment, short i, same sound as moving air. |
| Anchor | **ANG-ker** | Named fragment; ordinary English pronunciation. |
| Shadow | **SHAD-oh** | Named fragment; ordinary English pronunciation. |
| Storm | **STORM** | Named fragment; one syllable. |
| Blade | **BLAYD** | Named fragment; one syllable. |
| Tide | **TYDE** | Named fragment; one syllable. |
| Pressure | **PRESH-er** | Named fragment; stress first syllable. |
| Compression | **kum-PRESH-un** | Named fragment; stress second syllable. |
| Iron Wall | **EYE-urn WALL** | Named Path; stress `Wall`. |
| Copper | **KOP-er** | Tier name; stress first syllable. |
| Bronze | **BRONZ** | Tier name; one syllable. |
| Gold | **GOHLD** | Tier name; one syllable. |
| Archmarshal | **ARCH-mar-shul** | Stress first syllable. |
| `[UNBOUND]` | **unbound** | Brackets silent. |
| `[SHATTERED]` | **shattered** | Brackets silent. |
| `L.` / `S.` / `V.` | **L / S / V** | Speak the letter name only; punctuation silent. |

## Narrator direction

- Treat each paragraph as its own segment and each `---` as a long pause, exactly as configured.
- Do not perform italics as a separate voice. Use the prose frame to distinguish inner Path prompt, visible text, quoted reading, and log entry.
- Keep Cleon's delivery clipped and work-focused without turning fragments into separate speakers. Keep Vastin's clauses formal, including his audible corrections and qualifications.
- In chapter 17, preserve the two-syllable/one-syllable distinction in `The Fallow has it. The hall has it.`
- In chapter 26, let the three short protected paragraphs answer one another: Lira, Cael, Lira.
- In chapter 30, continue Cleon's voice across the action beat after `built the same way twice`; `The two fingers` are his.


---

<!-- PART 3 -->

# Book 8 — *Before the Paths*: listening proof, part 3 (chapters 31–45)

Scope: `manuscript/chapter-31.md` through `manuscript/chapter-45.md`, read in full and in order. The scene-by-scene reading record, exact boundary words, and restored-unit context are in `listening-notes-part3.md`. No manuscript file was modified.

## 1. Verdict

**PASS — render-ready. No line fix is required or recommended in chapters 31–45.**

Quotation, attribution, formatting, repaired joins, and count continuity all survive a single-voice listening pass. The two paragraphs over about 700 characters are listed below for production awareness; neither contains an internal ambiguity or warrants a prose change. Protected material remains untouched.

## 2. Findings by category

### 2.1 Quotation marks and speaker attribution

- All spoken paragraphs have balanced straight quotation marks. No mismatched multi-paragraph speech and no abutting `.” “` repair scar occurs in this range.
- The Lowmarch council, Cleon's closed-eye account, the two crews at the yard fire, and the grade-table discussion remain attributable by address, blocking, or the preceding sentence. Pike's read-aloud lines and the answers to them are equally clear.
- Oryn's patient-room dialogue, including each short permission or answer, has an audible speaker. Lira's protected tagless replies in chapter 40 are unmistakably hers from the immediately preceding question and action.
- The alley fight's orders and counts remain attached to Cael, Brom, Karis, or the opposing men. Teague's four are consistently distinguishable as the tall spear-carrier, the broad man called the bow, the young one, and the lean old woman; the young one cannot be mistaken for Cael in the scene.
- Every speech join named by the two texture lanes was reread with its preceding and following sentence. All seven are sound; the exact contexts and rulings are recorded in `listening-notes-part3.md`.

### 2.2 Ear collisions, homographs, and bare `as`

- Cael / Karis / Cleon remain distinct as KAYL / KAIR-iss / KLEE-on. Oryn / Ostrand, Lowmarch / Millrace, the Fallow / the Hall, Lira / Line, and Teague / Treswick / Ternhall are never introduced so densely that a listener loses the referent.
- `the bow` is BOH when it names Teague's broad crossbowman or the weapon; the scow's `bow` in chapter 44 is BAU. `lead` in the cord's `pear of lead` is LED. Present-tense or faculty `read` is REED; past-tense `read` is RED. The remaining homographs are resolved by immediate syntax and need no recast.
- `leaf`, `lean`, `flat`, `bar`, `mark`, `set`, and `still` all have a concrete local referent before or within the sentence. No use produces a plausible competing name or role on first hearing.
- No bare `as` in the range needs replacement with `while`; each marks comparison, manner, identity, or a clearly completed temporal relation.

### 2.3 Formatting the narrator meets

- The eleventh acquisition unit in chapter 33 and the twelfth in chapter 35 are intact, wholly italic, and paragraph-isolated. Audio flattening preserves their sentence order and does not create a change of speaker.
- Cael's italic logs, inventories, Hesk's note, Karis's entries, Pike's read-aloud material, the leaf in chapter 38, and the chronicle line were checked as flattened narration. The leaf's quoted words remain distinguishable from Karis's own interpolated words by syntax and delivery. The chronicle's dashes should be treated as light internal pauses.
- The roman word `withdrawn` inside the chapter 41 italic log is intentional emphasis reversal. It becomes ordinary prose under the audio preprocessor without damaging the sentence.
- Initials `K.`, `V.`, `S.`, and `H.` occur only in documentary lists or tallies and should be read as letter names. No stray Markdown, unbalanced asterisk, bracketed form, underscore, backtick, or code fence occurs in the range.
- All 67 `---` scene breaks have a blank line before and after. They divide the fifteen chapters into 82 scenes and should receive the specified long pause.
- The only Arabic numeral outside chapter headings is visible record text: `291st` in the chapter 36 log. Read it as “two hundred and ninety-first.” All narrative quantities and the remaining record quantities are spelled out.

### 2.4 Typos, broken joins, restored units, and continuity

- No typo, doubled accidental word, lower-case restart, mid-clause stop, orphaned pronoun, dangling comparison, or viewpoint-illegal name was found.
- All seven lane joins in range are sound: chapter 31's shortened council reply; chapter 36's restored refusal; chapter 38's leaf transition; chapter 42's planting inference; the two adjacent chapter 43 cuts; and chapter 45's shortened grade-table exchange.
- The audit-restored boundaries around Cleon's stopped word, the different ledger, the title, the stopped apparatus inference, pole two, Oryn's sixth-chair term, and Lira's arm exchange are grammatical and audible. Exact before/join/after evidence appears in the notes file.
- Deployment remains thirty-two throughout this range. The purse sequence is continuous: one hundred and thirty-four, one hundred and thirty after the chapter 37 dinner, one hundred and twenty-eight after the chapter 42 rope, and one hundred and twenty-seven after the chapter 45 food purchase.
- Sheet counts, site ranks, stake numbers, breath counts, distances, and bolt flights do not contradict their local echoes.

### 2.5 Paragraphs over about 700 characters (list only)

| Location | Characters | Opening cue |
|---|---:|---|
| `manuscript/chapter-32.md:189` | 761 | `Wind was first, as it had always been…` |
| `manuscript/chapter-45.md:227` | 764 | `Karis cracked the grade. The sites are ranked…` |

### 2.6 Protected material

The protected notices, logs, leaf, chronicle line, and owner-set lines were checked only for their joins and narrator handling. The eleventh and twelfth acquisition units remain exact. No protected line is treated as a finding, and no change is proposed to any protected text.

## 3. Exact line fixes

### A. Required

None.

### B. Optional

None.

There are therefore no old strings to verify and no proposed replacement to submit to the overlap gate.

## 4. Pronunciation lexicon

Earlier-book entries are carried unchanged where shared. Book 8 additions are marked as such.

### People

| Name | Say | Identification/status |
|---|---|---|
| Cael | KAYL, one syllable | Owner-confirmed #33; protagonist. |
| Lira | LEER-a | Owner-confirmed #33; Wind. |
| Brom | BROM, as in “from” | Carried; Iron Skin. |
| Karis | KAIR-iss | Carried; Ember and field analyst. |
| Seln | SELN, one syllable | Carried; records and ground reader. |
| Oryn | OR-in | Carried from Book 7; healer, Tide. |
| Teague | TEEG, one syllable | Carried from Book 7; independent crew captain. |
| Pike | PYKE | Carried from Book 7; Lowmarch ledger-keeper. |
| Hesk | HESK | Carried; Cael's grandfather, his notes and ledger. |
| Reydan | RAY-dan | Carried; Compression source named in records. |
| Daeva | DAY-va | Carried; Storm source named in records. |
| Ephram | EF-ram | Carried; Blade source named in records. |
| Vastin | VAS-tin, first syllable as in “fast” | Proposed Book 8; old man and field adjudicator. |
| Cleon | KLEE-on, two syllables | Proposed Book 8; former technician. |

### Places

| Name | Say |
|---|---|
| Lowmarch | LOH-march |
| Millrace | MILL-rays |
| Ostrand | OST-rand |
| Ardenmere | AR-den-meer |
| Ternhall | TERN-hall |
| Treswick | TREZ-wick |
| the Fallow | FAL-oh, two syllables |
| the Stair | STAIR; the Quieting site |
| the Hall / the drowned hall | HAWL |

### Terms and forms

| Term | Say / handle |
|---|---|
| the Line | LYNE |
| Path | PATH; ordinary vowel, with category status supplied by context |
| Wind | WIND, the noun; never WYND for the Path or fragment |
| Pressure; Iron; Compression; Ember; Shadow; Storm; Anchor; Blade; Tide | Ordinary-word pronunciations; preserve each as a Path or fragment category by context. |
| Iron Wall | Ordinary words; two-word fragment name, distinct from Brom's Iron. |
| Rune | ROON; fragment family and perceptive faculty. |
| the Quieting | KWY-et-ing, three syllables |
| the Quiet | KWY-et; distinct from *the Quieting* |
| the Compact | KOM-pakt |
| Arbiter | AR-bit-er |
| Architect | AR-ki-tekt |
| Kindling | KIND-ling |
| sigil | SIJ-il |
| the read | REED; Cael's perceptive faculty |
| `un-bound` | un-BOUND; historical category, with a light hyphen pause |
| marks | Ordinary plural; currency in context |
| cold term | Ordinary words; an allowed seasonal interval, not a named season |
| `K.`, `V.`, `S.`, `H.` | Speak the individual letter, then pause lightly before its tally. |

## 5. Direction handoff

- Preserve one paragraph per narration segment and give every `---` a long pause.
- Use a restrained record-reading register for italic logs and lists; italics themselves are silent after preprocessing.
- Give the chapter 38 leaf one continuous quoted voice, with Karis's interpolations returned briefly to her ordinary voice. Keep the chronicle's missing span missing; do not supply or explain words.
- In Teague's crew, read `the bow` as BOH and keep `the young one` neutral and unnamed.
- The two long paragraphs can remain single segments. Their syntax supplies enough internal breath points without editorial subdivision.


---

<!-- PART 4 -->

# Book 8 — *Before the Paths*: line and listening proof, part 4 (Step 4)

Reader: Codex, independent review seat, fresh context, 2026-10-12. Scope: `manuscript/chapter-46.md` through `manuscript/chapter-60.md` only (79,365 words; eighty-four scenes), read in full and in order from whole-file numbered output. The listening model is one narrator, one segment per paragraph, with every `---` rendered as a long pause and Markdown emphasis flattened by `audio/fpaudio.py`.

The required model and completion records were read first. Chapter-by-chapter scene evidence, every in-range restored-unit lead-in and follow-on, all Lane B second-ear joins, the chapter 60 `old man` ruling, and the supplemental mechanical audit are in `listening-notes-part4.md`.

**No manuscript file was modified, and no git command was run.**

---

## 1. Verdict

**PASS — render-ready; no required or optional line fix.**

All fifteen chapters pass the line-and-listening proof. I found no unbalanced or mismatched quotation, fused adjacent quotation, unplaceable speaker, narrator-hostile homograph in context, broken restoration or lane join, mid-clause ending, lower-case restart, accidental doubled word, cut antecedent, dangling comparison, viewpoint-name leak, or inconsistent count echo.

The protected record passages, acquisition unit, logs, slips, ledger, letter, departures, and closing prose remain intact and were not treated as findings. The tagless protected lines in chapter 58 have unmistakable speakers. Chapter 60's two uses of `the old man` for Hesk and, later, Vastin do not blur by ear and need no substitution.

The only render-direction work is to preserve document register, direct the listed homographs, and handle the six paragraphs over about 700 flattened characters without changing the locked prose.

---

## 2. Findings by category

### 2.1 Quotation marks and speaker attribution

- Straight quotation marks balance within every paragraph. There is no mismatched curly quotation, unresolved multi-paragraph speech, or doubled `.” “` repair scar.
- The blanket council, shale-step council, pass action, court rim, and two crews at one fire remain attributable through tags, physical blocking, role, or short controlled alternation.
- Pike's remembered bench voice remains distinct from Cael's narration and the answers that followed the readings.
- Oryn's patient speech, self-directed speech, room instructions, and every `May I?` remain clear. The unanswered request at the young one's death is a deliberate emergency exception, explicitly waited on for one breath and examined in chapter 57.
- Vastin's formal clauses and self-corrections remain distinguishable from Teague's compressed field speech and Cleon's remembered method.
- Teague's four remain stable by role: the tall man with the spear; the broad man called the bow; the unnamed young one; and the lean old woman. The young one never blurs with Cael, and the narration never prints his name.
- In chapter 58, tagless `Right.` is Lira's: her return from the cut and the following explanation frame it. Tagless `It's the first one.` is Karis's: she is the named next crosser, and the next sentence continues her action.

No quotation or attribution fix is required.

### 2.2 Ear collisions, homographs, and bare `as`

No name collision requires a text change. Narrator direction should preserve these contrasts:

| Pair or cluster | Direction |
|---|---|
| Cael / Karis / Cleon | KAYL / KAIR-iss / KLEE-on. |
| Seln / the Stair / the Span | SELN / STAIR / SPAN. |
| Teague / Ternhall | TEEG / TERN-hall. Treswick does not occur in this range. |
| Oryn / Ostrand | OR-in / OST-rand. |
| Lowmarch / Millrace | LOH-march / MILL-rays. |
| the Fallow / the Hall | FAL-oh / HAWL. |
| Hesk / Pike / Vastin / Brom | HESK / PYKE / VAS-tin / BROM. |
| Lira / Line / leaf / lean | LEER-a / LYNE / LEEF / LEEN. |

All requested homographs were heard in their full scenes:

| Word | Intended reading in chapters 46–60 |
|---|---|
| `lead` | LED for the cord's or pencil's metal; LEED where it is a verb. |
| `wound` | WOOND for injury; WOWND for something wrapped. |
| `close` | KLOHS as adjective/adverb; KLOHZ as verb. |
| `read` | REED for present/infinitive and `the read`; RED for completed past. |
| `tear` | TAIR where used of cloth or paper. |
| `live` | LYVE in `live ruts`; LIV where the verb is intended. |
| `wind` | WIND for weather and the fragment; WYND only where syntax makes the verb. |
| `bow` | BOH for the weapon and Teague's crew-role; BAU for an inclination if encountered. |
| `row` | ROH. |
| `minute` | MIN-it. |
| `lean` | LEEN for the old woman's build and the slant of a sign. |
| `leaf` | LEEF for skin, notebook, or document leaf. |
| `flat` | FLAT for the courier's case, ground, and hand position; the noun is established by context. |
| `bar`, `mark`, `set`, `still` | Ordinary pronunciations; technical force comes from context, not a changed sound. |

Every bare `as` was read in context. None creates a damaging `while` mishearing or needs a recast.

### 2.3 Formatting the narrator meets

- There is no code fence, stray backtick, bracketed form, or unresolved marker in this range. Every paragraph has paired asterisks, and `fpaudio.py` removes the emphasis markers without breaking a sentence.
- The thirteenth acquisition unit in chapter 51 correctly contains roman `someone made this` inside surrounding italics. Flattened, it remains one grammatical log passage.
- Cael's logs, including repeated `Deployment since the Line` lines, keep a coherent document order. The S22 log in chapter 57 and the ledger and letter in chapter 60 flatten cleanly.
- The two sealed slips in chapter 52 remain separately introduced and separately heard. Hesk's notes, Karis's entries, and the court measurements retain document context.
- No Arabic numeral appears in body narration or a record passage; digits occur only in chapter headings. Day counts, marks, cords, strides, yards, sheet totals, corner figures, stake numbers, breath counts, and bolt flights are written out.
- The only initial is the protected Hesk-letter signoff `— C.` in chapter 60. Say the letter name “C”; the dash and full stop are silent.
- Every `---` has a blank line before and after and should receive the specified long pause.

The deployment progression is coherent: thirty-two through the return road; thirty-three at the seep; thirty-four before the court crossing; thirty-five after Cael's court read. His deliberate inward read is expressly uncounted. The purse moves from one hundred and twenty-seven to one hundred and twenty-three and then remains there.

No narrator-format text fix is required.

### 2.4 Typos, broken joins, and continuity

- All six in-range Lane B line joins and the referred chapter 60 `old man` case are sound. No shortened sentence strands a noun, pronoun, comparison, or speech handoff.
- All twenty-two restored protected units have complete, audible lead-ins and follow-ons. Longer units' internal author-written beats preserve the same speaker or make the handoff explicit. Exact evidence and rulings are in the notes.
- No typo, mid-clause ending, lower-case prose start, accidental doubled word, viewpoint-inaccessible name, or damaged paragraph boundary was found.
- The only duplicate-word scan hits are grammatical `had had` constructions.
- All protected owner defaults stand: `the whole year`; Cael's Path/machine lines; `Tell Lira's family I said so`; the unnamed young one; the tall male spear-carrier; and the unprinted technician date.
- No English weekday, named month, month order, named season, or metric unit appears. `spring` is a water source; `thaw`, `first snow`, and `cold term` are permitted events.
- The Reader Standard holds. The death and its consequences are serious but not lingeringly graphic; consent, evidence, institutional harm, and the limits of inference remain legible by ear.

No typo, join, or continuity fix is required.

### 2.5 Paragraphs over about 700 characters

Lengths are narrator-flattened characters after Markdown emphasis is removed and whitespace is collapsed. These are the only paragraphs over 700 characters in the range:

| Location | Characters | Opening cue |
|---|---:|---|
| `manuscript/chapter-49.md:195` | 716 | `He had not been able to say so by one lamp...` |
| `manuscript/chapter-51.md:345` | 771 | `Twelfth—no, count it again—thirteenth. Wind, Pressure...` |
| `manuscript/chapter-52.md:13` | 722 | `It was the trodden path that they took...` |
| `manuscript/chapter-57.md:253` | 954 | `Turned the Rune fragment on myself. Cleon said don't...` |
| `manuscript/chapter-59.md:27` | 711 | `He went over them, as he might have gone over his pockets...` |
| `manuscript/chapter-60.md:303` | 963 | `He had spent the whole year learning that the world...` |

### 2.6 Protected material

All protected wording encountered in chapters 46–60 stands unchanged. This includes the protected Path and machine sentences, tagless court lines, the thirteenth acquisition unit, Cael's logs, the S22 entry, the two slips, S20 and S23 closes, the ledger, Hesk's letter, both departures, and the closing prose. The restored-unit and Lane B join evidence in the notes confirms that their lead-ins and follow-ons are sound.

---

## 3. Exact line fixes

### Required (0)

None.

### Optional (0)

None.

There is no old/new string to verify, so the unique-match grep requirement and eight-word overlap gate are not invoked. No protected line is changed.

---

## 4. Pronunciation lexicon

Only names and terms occurring in chapters 46–60 are included. Shared entries carry the earlier books' pronunciations; Cael and Lira are owner-confirmed.

### People

| Name | Say | Identification / status |
|---|---|---|
| Cael | KAYL, one syllable | Owner-confirmed #33; log-keeper and viewpoint. |
| Lira | LEER-a | Owner-confirmed #33; Wind. |
| Brom | BROM, as in `from` | Carried; Iron Skin and builder. |
| Karis | KAIR-iss | Carried; Ember, researcher, and recorder. |
| Seln | SELN, one syllable | Carried; scout and ground reader. |
| Oryn | OR-in | Carried from Book 7; Tide healer. |
| Teague | TEEG, one syllable | Carried from Book 7; captain of the four. |
| Vastin | VAS-tin, as in `fasten` | Carried; former Arbiter / Archmarshal. |
| Hesk | HESK | Carried; Cael's grandfather and teacher. |
| Cleon | KLEE-on | Carried; instrument reader remembered in this range. |
| Pike | PYKE | Carried from Book 7; Lowmarch keeper. |

### Places

| Name | Say | Status / note |
|---|---|---|
| Denvash | DEN-vash | Carried; destination on Hesk's letter. |
| Lowmarch | LOH-march | Carried from Book 7. |
| Millrace | MILL-rays | Carried from Book 7; same sound as the ordinary mill channel. |
| Ostrand | OST-rand | Carried. |
| Ternhall | TERN-hall | Carried; Ternhall brass. |
| Thornwater | THORN-waw-ter | Carried from Book 7. |
| the Fallow | FAL-oh, two syllables | Carried site name. |
| the Hall | HAWL | Site name; distinct from the Fallow. |
| the Stair | STAIR | Carried site name. |
| the Span / the Sunken Span | SPAN / SUNK-en SPAN | The iron crossing and site. |

### Systems, Paths, and working terms

| Term | Say / handle |
|---|---|
| Kindling | KIND-ling. |
| Arbiter | AR-bit-er. |
| Architect | AR-ki-tekt. |
| the Compact | KOM-pakt. |
| the Line | LYNE; keep distinct from Lira. |
| Path | PATH; ordinary vowel, technical category. |
| the Quiet | KWY-et. |
| sigil | SIJ-il. |
| the read | REED; Cael's perceptive faculty. |
| oldest-last | OHL-dest LAST; light compound stress. |
| shale-back | SHAYL-back; one compound. |
| Wind | WIND; fragment and Path name, never WYND here. |
| Pressure | PRESH-er. |
| Iron / Iron Wall | EYE-urn / EYE-urn WAWL. |
| Compression | kum-PRESH-un. |
| Ember | EM-ber. |
| Shadow | SHAD-oh. |
| Storm | STORM. |
| Anchor | ANG-ker. |
| Blade | BLAYD. |
| Tide | TYDE. |
| Rune | ROON. |
| Force | FORSS. |
| Impulse | IM-pulss. |
| `-adjacent` | ad-JAY-sent, with a light compound boundary. |
| marks | Ordinary plural; currency where the context gives a purse or price. |
| cold term | Ordinary words; a permitted interval, not a named season. |
| Cael's logs; Hesk's notes and letter; Karis's entries; the slips and ledger | Use a light document register. Italics and punctuation markers are silent; voice the protected signoff `— C.` as the letter name “C.” |

---

## 5. Lock recommendation

Chapters 46–60 can be locked and hash-bound as they stand. Carry the lexicon and homograph table into single-narrator direction, preserve one paragraph per segment except for the renderer's sentence-boundary handling of the six long paragraphs, and render every `---` as the prescribed long pause.
