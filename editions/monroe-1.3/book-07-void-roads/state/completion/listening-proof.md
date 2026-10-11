# Book 7 — Line-and-listening proof (Step 4), merged record

**Book:** *Void Roads* · Monroe 1.3 edition · chapters 1–60 · proofed 2026-10-11 on the independent review seat (Sol, gpt-5.6-sol via Codex).

## Verdict
**RENDER-READY after one required line fix (applied).** Four proofreaders read fifteen chapters each, in full: Part 1 (ch1–15) found two items; Parts 2, 3 and 4 (ch16–30, ch31–45, ch46–60) found none. No quotation, attribution, join, numeral, continuity or protected-text defect remains. All protected text is intact.

## How this proof was run — and one run rejected
- **r0, rejected.** A first single-seat run returned "PASS — RENDER-READY, 0 fixes" in seven minutes. Its token use (267,200, against 774,752 for Book 6's proof) and its log (about 1 MB, smaller than the manuscript) show it did not read the whole text. The coordinator rejected it; it is kept as `listening-proof-r0-NOT-A-FULL-READ.md` and is not evidence.
- **r1, accepted.** Four parallel runs, each bound to print every chapter in full and to record, for every scene, its first and last six words. Token use 404,260 / 384,930 / 426,519 / 384,341. The coordinator sampled 160 of the 683 recorded scene-boundary snippets against the manuscript: 152 are verbatim in the stated range (the rest differ only by emphasis marks or punctuation).
- A real read found what r0 missed: the ambiguous "he" in ch9.

## Coordinator rulings on the proof's fixes
1. **ch9 (applied):** after a scene break, "when he had done" had no noun; it now reads "when Seln had done". Overlap re-run: 0 unprotected.
2. **ch2 "*Cu 3*" → "*Copper 3*" (NOT applied; renderer note instead).** The locked Book 1 prints the same board ratings as "Cu 3" / "Cu 5", decodes them on the page, and its proof's lexicon reads them as the letters, "C-U three". Book 7's sentence says the names "carried letters after it, and a number". The text stays as it is; the narrator reads "C-U three", as in Book 1.

## Renderer notes carried to DIRECTOR_CUT_READY
- "Cu 3" (ch2) is read as letters: "C-U three". `[UNBOUND]` (ch42) and the FRAGMENT ACQUIRED notice (ch37): brackets and fences silent; the notice flattened line by line. All-caps HOLD and board lines read in sentence case. Single initials are letter-names.
- Homographs per the parts' tables: read (REED / RED: "the Iron read" is REED), wind (the Wind Path against the wind), bow (BOH for the crossbow; BAU to bow), lead, wound, close, minute, row.
- Paragraphs over 700 characters: 17 in the book (listed in the parts); split only at sentence boundaries.
- Pronunciation lexicon: the four parts' tables below, merged by reading; shared names carry earlier books' entries (Cael = KAYL, Lira = LEER-a owner-confirmed #33).

---

# PART 1 — chapters 1–15

## Book 7 — *Void Roads*: listening proof, part 1

Scope: `manuscript/chapter-01.md` through `chapter-15.md`, read in full and in order from complete numbered printouts. This proof follows the Book 5 and Book 6 listening-proof structure and applies the Book 7 completion rulings, OWNER-DECISIONS, BOOK_MAP §10, `protected-patterns.txt`, and the narrator behavior in `audio/fpaudio.py`.

## Verdict

**PASS WITH TWO REQUIRED LINE FIXES.** Apply §3A, verify the two replacements, and then this range is ready to lock and hash-bind.

The full read found no broken lane join, no damaged protected unit, no unbalanced quotation sequence, no unclear fight order, no calendar violation, and no deployment-count error. One visual abbreviation will flatten ambiguously for audio, and one pronoun reaches across a scene break to the wrong immediate noun before resolving. Both fixes are outside protected text and log entries. Neither proposed replacement introduces an eight-word source overlap.

No manuscript file was modified during this proof.

---

## 1. Findings by category

### 1.1 Quotation marks and speaker attribution

Straight quotation marks are balanced in every chapter. The only paragraph-level odd counts are the first two paragraphs of Karis's three-paragraph read-aloud hypothesis in chapter 9; they correctly use multi-paragraph speech convention, and the third paragraph closes the quotation.

The councils, board readings, ford fight, unnamed Thornwater speakers, and treatment scenes remain attributable by tag, position, or unique role. In particular:

- The steading's woman, bowman, injured survivor, carter and carter's wife do not blur into one another.
- Brom's counted `Five` during the ford fight remains his established pack count.
- The bowman's later `Five dead` is separated from the steading's woman's `Four / Out of five` by scene position and attribution.
- Pike's public readings are consistently framed as readings to the meadow; replies from the party remain identifiable.
- Chapter 15's untagged answer to `"Can it be done?"` is audibly Brom's because his inspection occupies the preceding paragraph and the answer is a builder's judgment.

One narrator-facing referent stumble remains at the opening of chapter 9's fourth scene: `when he had done` refers to Seln across the scene break, but the sentence begins with Karis. Required fix 2 names Seln.

### 1.2 Ear collisions, homographs and bare `as`

No name collision requires a text change. Direction should keep the recurrent pairs separated:

| Pair or cluster | Direction |
|---|---|
| Karis / Cael | KAIR-iss versus KAYL. |
| Brom / the bowman | BROM versus BOH-man. Both occur in the Thornwater and ford sequences. |
| Seln / Selm- | SELN, one syllable; no Selm- name occurs in this range. |
| Lira / Line | LEER-a versus LINE. |
| Ostrand / Oxhollow | OST-rand versus OKS-hol-oh; they do not share a scene. |
| Pike / Teague | PYKE versus TEEG. |
| Hesk / Vell / Ephram | HESK, VELL, EF-ram. |
| Lowmarch / Thornwater | LOW-march versus THORN-waw-ter. |

Homographs are clear in context and are better handled in direction:

| Word | Intended reading in chapters 1–15 |
|---|---|
| `lead` | LEED in `a Bronze to lead` (ch2); LED for the metal-colour river (ch4). |
| `wound` | WOWND in every occurrence: rope, linen and winding. No WOOND noun occurs. |
| `close` | KLOHZ as a verb; KLOHS as adjective/adverb. |
| `read` | REED for present tense and Cael's perceptive `read`; RED for narrated past. |
| `live` | LIV in both occurrences. |
| `wind` | WIND for weather and the Path; WYND for the well crank in ch14. |
| `bow` | BOH for the weapon and saddle-bow; BAU for the scow's bow (ch2) and the gravel bar's blunt bow (ch8). |
| `row` | ROH throughout. |
| `minute` | MIN-it throughout. |
| `tear` | Does not occur in this range. |

No bare `as` produces a plausible “while” mishearing that changes sense. Pike's `as I say everything` in chapter 15 means “in the manner that” and is clear from the exchange.

### 1.3 Formatting the narrator meets

Required fix 1 expands the visible abbreviation `Cu` so the flattened text cannot be voiced as “C U.” The digit remains appropriate because this is a displayed old rating, not a narration numeral.

Other formatting is sound:

- The only Arabic numerals outside chapter headings are the displayed `Cu 3` in chapter 2 and the displayed `110` measurements in chapters 6 and 9. Read them as “Copper three” after fix 1 and “one hundred ten.”
- Cael's italic log entries remain intact, including every `Deployment since the Line` line in this range. The progression is `none` through chapter 10, then `one` from chapter 11 onward.
- Hesk's chapter 14 letter, Karis's leaves and tables, Seln's reports, Pike's slips and ledger lines, and all board text should receive a light document register. Italic markers are silent.
- `HOLD` is an ordinary word displayed in capitals: say “hold,” not the letters.
- Initials `L.`, `C.` and `H.` are letter-names; do not say “period.”
- No fenced notice, bracketed form, or stray backtick occurs in chapters 1–15.
- Every `---` has a blank line before and after and should become the specified long pause.
- `Fifth-day` is the house ordinal day, not an English weekday. Generic `month`, `season`, `thaw`, `frost` and `snow` comply with the calendar rulings.

### 1.4 Typos, broken joins and restored units

Required fix 2 resolves the only pronoun stumble. No doubled word, lower-case sentence start, mid-clause ending, dangling comparison, or inconsistent count remains.

The deployment sequence is coherent: `none` until Cael spends Wind at the ford, then `one`. The money, distance, knot, candle-depth, fight and injury counts in this range agree with their echoes.

The Lane A second-ear joins in range are sound:

- **ch1 log:** the fourth-day entry moves through `Under it he added the other. It was getting to be a habit.` into `Deployment since the Line: none.` The document/narration/document changes are audible.
- **ch2 Brom speech:** `Copper. For good, and I can say why.` runs directly into `And then the man with the book's a Copper himself...`; the preceding tag holds both sentences in Brom's voice.
- **ch15 slope:** the revealed slope runs directly into Lira's `Can it be done?`; Brom's answer remains secure.

The restored chapter 13 gate unit is sound. The sentence before is `The woman's eyes went from Brom's sling to Lira's bound foot on the stave.` The sentence after is `The woman said it as she might have said that barley stopped at a certain height on a hill.` Between them, the protected sequence woman → Lira → woman is immediately audible and stands intact.

Lane B has no listed second-ear join in chapters 1–15.

### 1.5 Paragraphs over about 700 characters

| Chapter:line | Characters | Opens |
|---|---:|---|
| ch01:29 | 708 | He had no Path of his own, and so no tier and no rank… |
| ch02:45 | 760 | The carts lay along the river side with their shafts down… |
| ch02:87 | 830 | Somebody had brought it up from some river long ago… |
| ch05:95 | 741 | Cael watched the carter at that halt, and at the next… |
| ch05:211 | 780 | Wind had his feet first. They had leaned for a month… |
| ch08:281 | 715 | There was nothing to do it against. He lay on his back… |
| ch09:205 | 825 | The country kept one rule for fire, and voices, and Paths… |
| ch15:5 | 787 | She had gone up to the eave on purpose to be first… |

### 1.6 Protected material

All protected wording encountered in chapters 1–15 stands unchanged. This includes Cael's protected log language, Pike's board copies, and the BOOK_MAP §10 units in this range. The chapter 13 gate restoration was read with its lead-in and follow-on and is sound. Neither proposed fix touches a protected pattern, a protected line, a log entry, an inventory, the notice, or the closing.

---

## 2. Exact line fixes

### 2A — Required before render (2)

Each old string was verified across the full Book 7 manuscript and occurs exactly once. Each new string currently occurs zero times. An in-memory comparison against the source found no new shared run of eight or more words.

1. `manuscript/chapter-02.md`
   old: `*Cu 3*`
   new: `*Copper 3*`

2. `manuscript/chapter-09.md`
   old: `Karis had written through the whole of it, and when he had done she turned the leaf back to its head.`
   new: `Karis had written through the whole of it, and when Seln had done she turned the leaf back to its head.`

### 2B — Optional, engine-safety only (0)

None. The remaining homographs and document forms are unambiguous with the direction in §§1.2–1.3.

---

## 3. Pronunciation lexicon

Only names and terms occurring in chapters 1–15 are included. Stress is shown in capitals. “Carried” means the pronunciation is carried from the earlier listening proofs; Book 7 additions are proposed for the direction files.

### People

| Name | Say | Identification | Status |
|---|---|---|---|
| Cael | KAYL, one syllable | the log-keeper; carries nine fragments | owner-confirmed #33 |
| Lira | LEER-a | Wind, Iron Rank One | owner-confirmed #33 |
| Brom | BROM, as in “from” | Iron Skin; builder and load-bearer | carried B4–B6 |
| Karis | KAIR-iss | Ember; researcher and recorder | carried B3–B6 |
| Seln | SELN, one syllable | scout and former reporting officer | carried B4–B6 |
| Hesk | HESK | Cael's grandfather; author of the ch14 letter | carried |
| Vell | VELL | Ardenmere ledger-keeper | carried |
| Bracken | BRACK-en | registrar named in memory | carried B4–B6 |
| Reydan | RAY-dan | source of Compression | carried B3–B6 |
| Daeva | DAY-va | source of Storm | carried B5/B6 |
| Ephram | EF-ram | source of Blade | carried B4–B6 |
| Pike | PYKE | one-armed keeper of the Lowmarch board | proposed B7 |
| Teague | TEEG | captain at the top of Pike's sheet | proposed B7 |

### Places

| Name | Say | Status |
|---|---|---|
| Ostrand | OST-rand | carried B4–B6 |
| Ardenmere | AR-den-meer | carried |
| Denvash | DEN-vash | carried |
| Norhold | NOR-hohld | carried B5/B6 |
| Fenmark | FEN-mark | carried B3–B6 |
| Lowmarch | LOW-march | proposed B7 |
| Thornwater | THORN-waw-ter | proposed B7 |
| Oxhollow | OKS-hol-oh | proposed B7 |

### Creatures, Paths and working terms

| Term | Say / handle |
|---|---|
| stillhound | STILL-hound; one compound | the grey road-hunting animal |
| shale-back | SHAYL-back; one compound | the high-country animal named by Pike |
| quiet ground | ordinary words, lower-case in this range | the carter's wife's unsourced term; not `the Quieting` |
| Kindling | KIND-ling | carried |
| Arbiter | AR-bit-er | carried |
| the Line | LINE | the western boundary; keep distinct from Lira |
| Path; fragments | ordinary words in the story's technical senses | slight stress only where contrast requires it |
| Wind | WIND | Path name; never WYND |
| Pressure | PRESH-er | fragment name |
| Iron; Iron Skin | EYE-ern; EYE-ern SKIN | Cael's read fragment; Brom's Path |
| Compression | kum-PRESH-un | fragment name |
| Ember | EM-ber | fragment and Karis's Path |
| Shadow | SHAD-oh | sealed fragment |
| Storm | STORM | fragment from Daeva |
| Anchor | ANG-ker | unnamed-source fragment |
| Blade | BLAYD | fragment from Ephram |
| Force | FORSS | Path name and practitioner label |
| the read | REED | Cael's perceptive faculty |
| Tiers and ranks | Copper, Iron, Bronze, Silver and Gold as ordinary words | read displayed digits as numbers; after fix 1, `Copper 3` is “Copper three” |
| `110` | “one hundred ten” | displayed measurement in Karis's notes |
| marks; coppers | ordinary words | currency |
| paces; yards; feet; cords | ordinary words | approved measures |
| `HOLD` | “hold” | visible board instruction; do not spell the letters |
| `Hm.` | voiced acknowledgment | preserve the short response |

---

## 4. Direction notes for segmentation and render

1. Keep Cael = KAYL and Lira = LEER-a throughout (#33).
2. Use the §2 fixes before rendering. In particular, never let `Cu 3` become “C U three.”
3. Give logs, letters, slips, leaves, tables and ledger lines a light document register. Do not voice italics or markdown.
4. Preserve paragraph segmentation: one paragraph per audio segment. Render every `---` as the long pause.
5. Keep Pike's public board voice distinct from replies from the meadow. His repeated readings and repeated looks are deliberate.
6. Keep the Thornwater roles fixed: the steading's woman, the bowman, the injured survivor, the carter and the carter's wife.
7. Observe the homograph directions in §1.2, especially boat BAU versus weapon BOH, Path/weather WIND versus crank WYND, and faculty REED versus past-tense RED.
8. The chapter 9 hypothesis is one Karis reading across three quoted paragraphs. Continue her voice until the closing quotation mark.


---

# PART 2 — chapters 16–30

## Book 7 — *Void Roads*: line and listening proof, part 2 (Step 4)

Reader: Codex, independent review seat, fresh context, 2026-10-11. Scope: `manuscript/chapter-16.md` through
`chapter-30.md`, read in full and in order from numbered whole-file prints. The per-scene evidence and the closing
mechanical audit are in `listening-notes-part2.md`.

Read first: Book 5's and Book 6's listening proofs; Book 7's completion plan, whole-arc read, pass brief, both applied
lane reports and lane rulings; the edition's audio and Reader Standards; the cited owner decisions; BOOK_MAP §10;
`protected-patterns.txt`; and `audio/fpaudio.py`.

**No manuscript file was modified; no git command was run.** No proposed change touches a protected line, log entry,
notice, inventory or closing. Cael = KAYL and Lira = LEER-a (owner-confirmed #33). No named season, month name, month
order or English weekday occurs in this range. Generic `month` is used lawfully; measurements remain in the edition's
allowed vocabulary.

---

## 1. Verdict

**Render-ready with no required or optional text fix.** All fifteen chapters pass the line-and-listening proof. There
is no unbalanced or mismatched quotation, unidentified speaker, broken lane join, mid-clause ending, lower-case prose
start, accidental doubled word, dangling comparison, inconsistent count echo or narrator-hostile abbreviation.

The in-range Lane A second-ear joins and the three restored units all sound complete in context. Lane B begins at
chapter 31, so it contributes no join inside this part. The deployment line remains `one` wherever it appears in this
range; chapter 30 deliberately stops the log before that expected line and says that it has done so.

The remaining work is direction only: pronounce the homographs by sense, voice written numerals as numbers, read
initials as letters, keep document voice distinct from narration, and let `---` carry the long pause.

---

## 2. Findings by category

### 2.1 Quotation marks and speaker attribution

- Every paragraph has an even number of straight quotation marks. There are no curly quotation marks and no
  multi-paragraph quotation exceptions in chapters 16–30.
- The five-person mountain councils, the six-person Fallow work, and Pike's Lowmarch board remain attributable by
  tags, direct alternation, task or physical position. Oryn's patient speech, self-directed counting and room-directed
  instructions remain distinct.
- The unnamed speakers are stable by role: ford-keeper, ferryman, gate woman, bowman, carter, clerk, spear, bow and
  boy. Brom and the bowman share the Thornwater departure scene without an audible handoff problem.
- All in-range Lane A joins pass: ch17:135–139; ch18:55–59; ch20:73–77; ch21:243–247 and 285; ch22:125; ch24:25 and
  201–205; and ch26:89. The sentence before and after each is quoted and ruled in `listening-notes-part2.md`.

### 2.2 Ear collisions and homographs

- Oryn / Ostrand / Oxhollow are separable as OR-in / OST-rand / OKS-hol-oh. Karis / Cael are KAIR-iss / KAYL;
  Seln is one syllable and no Selm- name occurs. Teague / Pike are TEEG / PYKE. Lowmarch occurs; Millrace and the
  Quieting do not occur in this range. The Fallow is FAL-oh; the only `hall` is an ordinary district hall.
- Hesk, Ephram, Brom, Lira and the Line keep their established sounds. The Brom / bowman and Lira / Line pairings are
  distinct in context and onset.
- `lead` occurs once as the verb LEED. All five forms of `wound` are past tense of *wind*, WOWND. `tear` is the verb
  TAIR. `live` is LIV. `Wind`, whether Path or weather, is WIND. `minute` is MIN-it.
- `bow` has three audible senses: the boat's prow and a courteous inclination rhyme with *cow*; the weapon and the
  role named for it are BOH. `row` is always ROH. `close` is KLOHZ as a verb and KLOHS as an adjective or adverb.
  `read` is REED in present/infinitive use and RED in completed past-tense narration; `the read` is REED.
- The full read found no bare `as` whose intended relation would be mistaken for temporal “while.” No recast is
  needed.

### 2.3 Narrator-facing formatting

- The FRAGMENT ACQUIRED notice (ch37) and `[UNBOUND]` form (ch42) are outside this part. No fenced block or
  square-bracketed form occurs in chapters 16–30.
- Cael's italic logs, Karis's observations, Pike's ledger lines, the Fallow slip, and the Ephram and `— V.` letters
  flatten coherently under `fpaudio.py`. `HOLD` is a word, not four spelled letters. Signoffs `— E.` and `— V.` are
  voiced as the letters E and V; punctuation is silent. Karis's `K. L. B. S. O.` is read letter by letter.
- The only Arabic numerals in body text are visible marks: `water at 36` in the registry annotation (ch26:115) and
  `95th` in Karis's notebook (ch28:55). Say “thirty-six” and “ninety-fifth.” All narration counts and measurements use
  words.
- Pike's lower-case italic `less six, the cart.` (ch24:95) is a deliberate second ledger line, introduced as four
  written words beneath the first; it is not a broken join.
- Every `---` break has a blank line before and after. Asterisk counts are even; there is no stray underscore,
  backtick or malformed emphasis.

### 2.4 Typos, protected restorations and broken joins

- The restored ch20 `Cold` unit, ch25 Pike-to-the-book unit and ch29 Lira clock unit have complete lead-ins and
  follow-ons and sound natural. Their sentence-before / protected-unit / sentence-after evidence is in the notes.
- The Lane A removals leave no orphaned pronoun, missing noun, doubled action, lower-case continuation or false
  speaker change. Lane B has no in-range edit.
- The number chain is stable in this part: deployment is one. The mountain's distances, the route days, the seven
  contract lines, the tenth placement, the sixty-two cords, the eleven uprights, the hound estimates and the Fallow
  trial rows retain their stated echoes.
- No typo or broken post-audit repair was found.

### 2.5 Paragraphs over 700 characters (list only)

Flattened lengths after asterisks are removed and whitespace is collapsed, before `fpaudio.py` applies its
sentence-boundary split:

| Chapter:line | Characters | Opens |
|---|---:|---|
| 23:53 | 865 | The five waded after. It was a hundred yards of gravel… |
| 23:127 | 750 | He knew, since he could hear her. She had been told… |

### 2.6 Protected text

The protected log wording in this range—including `Mine didn't. Hers did.`, the Path references and every
`Deployment since the Line: one.`—stands unchanged and is not a finding. The other owner-protected lines named in
#50 and #51 occur outside chapters 16–30. The restored protected units above were reviewed only for their joins; no
change is proposed.

---

## 3. Exact line fixes

### A. Required

None.

### B. Optional

None.

There is therefore no old string to grep and no proposed replacement to test against the eight-word overlap gate.

---

## 4. Pronunciation lexicon — chapters 16–30 only

Stress is shown in capitals. “Carried” means the pronunciation is carried from the earlier-book proofs; Book 7-only
entries are direction proposals. Millrace, the Quieting and the name Vell do not occur in this range and are omitted;
the visible signoff `V.` is handled above.

| Name or term | Say / handle | Status |
|---|---|---|
| Cael | KAYL, one syllable | owner-confirmed #33 |
| Hesk | HESK | carried |
| Lira | LEER-a | owner-confirmed #33 |
| Brom | BROM, as in *from* | carried |
| Karis | KAIR-iss | carried |
| Seln | SELN, one syllable | carried |
| Oryn | OR-in | proposed Book 7 |
| Teague | TEEG | proposed Book 7 |
| Pike | PYKE | proposed Book 7 |
| Ephram | EF-ram | carried |
| Rooke | ROOK, as in *book* | carried |
| Bracken | BRACK-en | carried |
| Withrow | WITH-roh | carried |
| Lowmarch | LOH-march | proposed Book 7 |
| Thornwater | THORN-waw-ter | proposed Book 7 |
| Oxhollow | OKS-hol-oh | proposed Book 7 |
| the Fallow; Fallow Ring | FAL-oh; FAL-oh RING | proposed Book 7 |
| Ardenmere | AR-den-meer | carried |
| Denvash | DEN-vash | carried |
| Ostrand | OST-rand | carried |
| Fenmark | FEN-mark | carried |
| Ternhall | TERN-hall | carried |
| Norhold | NOR-hohld | carried |
| shale-back | SHAYL-back | proposed Book 7 |
| stillhound | STILL-hound | proposed Book 7 |
| Kindling | KIND-ling | carried |
| Arbiter | AR-bit-er | carried |
| sigil | SIJ-il | carried |
| Path; the Line | PATH; LINE | carried / ordinary words |
| quiet ground | KWY-et ground | proposed Book 7 term |
| void road / void roads | VOYD road / VOYD roads | proposed Book 7 term |
| the read | REED | carried |
| Wind | WIND | ordinary word; Path name |
| Iron Skin | EYE-urn SKIN | ordinary words; Path name |
| Ember | EM-ber | ordinary word; Path name |
| Tide | TYDE | ordinary word; Path name |
| Shadow | SHAD-oh | ordinary word; Path name |
| Storm | STORM | ordinary word; Path name |
| Compression | kuhm-PRESH-un | ordinary word; fragment name |
| Anchor | ANG-ker | ordinary word; fragment name |

---

## 5. Direction notes for recording

1. Each `---` is a long pause; scene count and exact boundary words are recorded chapter by chapter in the notes.
2. Keep Cael's logs and all letters, ledger lines, slips and observations in a restrained document register; italics
   themselves are silent.
3. Read `HOLD` as one word, written numerals as full numbers, and initials as letters. Do not voice dashes, stops or
   markdown.
4. Keep BOH for the weapon/crew role and the *cow* vowel for the boat's bow or an inclination.
5. Split the two listed long paragraphs only at sentence boundaries.


---

# PART 3 — chapters 31–45

## Book 7 listening proof — part 3 (chapters 31–45)

Reader: Codex, independent review seat, fresh context, 2026-10-11. Scope: `manuscript/chapter-31.md` through
`manuscript/chapter-45.md` (77,782 words by `wc`), read in full and in order as the narrator will meet them: one segment
per paragraph, `---` as a long pause, italics stripped and the fenced notice flattened line by line. Read first: Book 5's
and Book 6's listening proofs; Book 7's completion plan, whole-arc read, pass brief, both lane reports and lane rulings;
the edition audio and Reader Standard; the named owner decisions; BOOK_MAP §10; `protected-patterns.txt`; and
`audio/fpaudio.py`. Per-chapter scene evidence, all restored-unit and lane-join rulings, and the closing mechanical audit
are in `listening-notes-part3.md`.

**No manuscript file was modified; no git command was run.** No change is proposed below. Cael = KAYL and Lira =
LEER-a (owner-confirmed, #33). No named season, month name/order, English weekday or metric unit occurs in the assigned
range. Generic `season` and `month` are allowed; distances use feet, yards, paces, strides, hands and cords. The protected
`mine` / `Path` logs and the owner-protected lines remain findings-exempt and unchanged.

---

## 1. Verdict

**PASS — render-ready in chapters 31–45 with no line fixes.** I found no unbalanced or mismatched quotation, no speech
whose owner a listener cannot recover, no ear collision that requires prose alteration, no malformed narrator-facing
document, no narration numeral that violates the edition rule, no broken post-lane join, and no typo or continuity fault.

The four in-range Lane B speech joins pass. The eight in-range restored protected units identified by the movement
audits pass with their lead-ins and follow-ons intact. In particular, the Ring fight orders remain attributable; the
six-person loft council remains audible; Pike's Lowmarch board reading remains distinct from the meadow's answers; and
Oryn's clinical speech consistently identifies whether she addresses a patient, herself, the room or the country.

The remaining work is direction only: preserve name pronunciations; distinguish homographs; read visible documents in a
light document register; make markdown and brackets silent; and flatten the ch37 notice in a neutral system cadence.
There are no paragraphs over 700 characters in this range.

---

## 2. Findings by category

### 2.1 Quotation marks and speaker attribution

- Every paragraph has balanced straight quotation marks. There is no intentional multi-paragraph open quotation in
  chapters 31–45, no curly quotation mark and no odd-asterisk paragraph.
- The Ring action in ch31–32 keeps every called order attached by tag, file position or immediate action. Even at the
  fastest points, Brom's crossbow actions, Karis's point-setting, Seln's route and Cael's commands cannot exchange owners.
- The ch36 loft council places all five speakers before the argument and maintains attribution through tags, rough-voice
  cues, role and short alternation. Oryn is not in the loft, so no sixth council voice is implied.
- The ch44 six-person account is ordered by Karis's questioning. Oryn's account remains one continuous turn across the
  applied lane join; the retained palms-up beat supplies the next visual/audible reset.
- Pike reads the Lowmarch board before the door is shut in ch45. The hide-woman, the three-person crew, the carter, the
  boy, Teague and the five are all established before their reactions; no answer from the room or meadow can be mistaken
  for Pike's ledger voice.
- The unnamed Thornwater woman and bowman remain differentiated by their stations (door/hold versus gate/platform).
  Brom is always named or tied to the crossbow before the unnamed bowman speaks, so `Brom` / `bowman` creates no audio
  ambiguity.
- Oryn's work scenes are unusually clear for audio: `to the arm`, `to the country`, the table setup, direct patient tags
  and the room's reactions establish addressee and speaker. Her interior ch44 route passage is separated from the crew by
  a scene break.
- Flat question punctuation such as Brom's `How many people.` (ch39) is deliberate character delivery. The immediate
  answer supplies the interrogative sense; no line fix is needed.

### 2.2 Ear collisions and homographs

No name collision requires a rename or prose fix.

| Pair or cluster | Direction |
|---|---|
| Oryn / Ostrand / Oxhollow | OR-in / OST-rand / OKS-hol-oh; distinct onset and syllable shape. |
| Karis / Cael | KAIR-iss / KAYL; preserve Karis's second syllable. |
| Seln / Selm- | SELN, one syllable; no Selm- name occurs in the range. |
| Teague / Pike | TEEG / PYKE; strong final consonants. |
| Lowmarch / Millrace | LOH-march / MILL-rayss. |
| Thornwater / the Fallow | THORN-waw-ter / FAL-oh; `the Hall` does not occur in the range. |
| Hesk / Vell / Ephram | HESK / VELL / EF-ram; each appears in a different syntactic role. |
| Brom / the bowman | BROM versus the descriptive role BOH-man; do not swallow the second syllable of `bowman`. |
| Lira / Line | LEER-a versus LINE; keep Lira's final vowel audible. |

Homograph direction:

| Form | Direction in chapters 31–45 |
|---|---|
| `read` | REED for the faculty/noun and present/infinitive; RED for past tense (`he read`, `had read`). |
| `lead` | LED for the metal tag at ch34:83; LEED in `rope fit to lead with` at ch43:199. |
| `wound` | WOWND in `wound a strip` / `He wound`; WOOND for Oryn's clinical noun at ch38:217. |
| `close` | KLOHZ as a verb (`would not close`); KLOHS for nearness (`close by`, `close to`). |
| `Wind` / `wind` | WIND for the Path and for moving air; no WYND verb occurs. Preserve the capital concept by context, not a changed vowel. |
| `bow` | BOH throughout this range: crossbow or longbow. No BAU occurrence. |
| `row` | ROH throughout: a line of entries, objects or people. |
| `minute` | MIN-it throughout: time. No my-NOOT occurrence. |

`tear` and `live` do not occur as homograph risks. The bare `as` constructions read as comparison, role or manner in
context; none can reasonably be heard as a temporally confusing `while` that would change an action's order.

### 2.3 Narrator-facing formatting

- Ch37's fenced notice flattens correctly under `fpaudio.py`: `FRAGMENT ACQUIRED` and each field become neutral spoken
  lines; code fences and the brackets around `[unnamed]` are silent. Keep one beat per flattened field and do not add
  dramatic character voice.
- Ch42's `[UNBOUND]` is spoken `unbound`, with brackets silent. It occurs once and functions only as a dating limit.
- Italic log entries, the covenant leaves, Karis's findings, Pike's slips and the Stair posting all remain intelligible
  after asterisks are stripped because narration identifies the document before or after it. Give them a light document
  register without voicing markdown.
- Cael's repeated `Deployment since the Line: thirteen` entries agree throughout the assigned range. The notice and the
  birthday inventory also agree on the tenth fragment; there is no number-echo drift here.
- The only Arabic numerals outside chapter headings are visual marks: ch41's italic `103rd` note and ch44's quoted written
  row `96th` / `110th`. Say `one hundred and third`, `ninety-sixth` and `one hundred and tenth`. No Arabic numeral appears
  in narration.
- No abbreviation, slash, stray markdown marker or all-caps `HOLD` slip occurs in chapters 31–45. `FRAGMENT ACQUIRED` is
  the sole all-caps narrator-facing form.
- All 68 `---` breaks have a blank line before and after and should receive the 1500 ms long pause.

### 2.4 Typos, repaired prose and continuity joins

- No typo, lower-case paragraph start, mid-clause end, accidental doubled word, orphaned pronoun or dangling comparison
  was found. The repeated-word scan returns only grammatical sequences such as `had had`, `that that` and `as it had
  had`.
- Lane B's in-range speech joins are all sound: ch40 Seln (`I had it the last time, also.` → `I stood in a corridor…`);
  ch41 Oryn (`I never knew…` → `I never went near enough.`); ch43 Oryn (`You'd know…` → `That's sixteen…`); and ch44
  Oryn (`fire in his fist.` → `I've been told…`). Lane A has no join in this range.
- The restored-unit joins are sound in ch31 (`Nothing in my hands`), ch34 (Brom's string treatment and Oryn's route
  cost), ch37 (the banks), ch38 (`colour of the wall`), ch39 (`Here … nearer`), ch44 (`North in the morning`) and ch45
  (`Nothing else ever`). The exact before/after sentences and individual rulings are recorded in the notes file.
- The one-hand/four-finger-pad repair remains consistent from treatment through the hundredth-day restriction. Lira's
  arm/ankle orders, Cael's calf and Karis's voice also carry forward without silent healing.
- The deployment count is thirteen everywhere it appears in this range. The book-wide progression `none → one →
  thirteen → twenty-three → twenty-seven` has no contradictory echo in chapters 31–45.
- No named season/month/weekday or metric unit appears. Generic `season` (Oryn's medical order) and `month` (Oryn's bone
  timing) are permitted by #42/#48. Apparent `spring` hits are water sources or the ordinary verb/noun, not a season.
- The Reader Standard holds. The Ring injuries are consequential without gore, and the consent violation is named,
  weighed and answered without excuse. The restored wording does not blur permission to read Cael with permission to
  take from Oryn.
- Protected lines, logs, the notice, the covenant, Pike's documents and the birthday/quiet-ground material remain exact.
  None is a finding or a proposed change.

### 2.5 Paragraphs over about 700 characters (list only)

None. The longest flattened paragraph is 699 characters (`chapter-38.md:229`).

---

## 3. Exact line fixes

None. There is no old/new string to verify, and the eight-word overlap gate is therefore not invoked. No protected line
is touched.

---

## 4. Pronunciation lexicon

Only names and terms that occur in chapters 31–45 are included. Stress is shown in capitals. `Carried` means the same
pronunciation appears in an earlier book's listening proof; Book 7 additions are proposed direction entries.

### People

| Name | Say | Identification | Status |
|---|---|---|---|
| Cael | KAYL, one syllable | crew lead; the reader | owner-confirmed #33 |
| Hesk | HESK | Cael's grandfather; Hesk's book/clock | carried |
| Lira | LEER-a | Wind; the runner | owner-confirmed #33 |
| Brom | BROM, as in `from` | Iron Skin; crossbow carrier | carried |
| Karis | KAIR-iss | Ember; analyst and recorder | carried |
| Ephram | EF-ram | Blade source, named in the council leaves | carried |
| Gault | GAWLT, as in `fault` | evaluator, remembered at Pike's board | carried |
| Seln | SELN, one syllable | surveyor and records hand | carried |
| Vastin | VAS-tin, as in `fasten` | Archmarshal in the courtesy-copy cutaway | carried |
| Vell | VELL | Ardenmere ledger-keeper | carried |
| Reydan | RAY-dan | Compression source | carried |
| Daeva | DAY-va | Storm source; named in the birthday log | carried |
| Oryn | OR-in | Tide healer; route-keeper | proposed B7 |
| Teague | TEEG, one syllable | Lowmarch crew captain | proposed B7 |
| Pike | PYKE | one-armed Lowmarch book-keeper | proposed B7 |

### Places

| Name | Say | Status |
|---|---|---|
| Ostrand | OST-rand | carried |
| Denvash | DEN-vash | carried |
| Ardenmere | AR-den-meer | carried |
| Fenmark | FEN-mark | carried |
| Ternhall | TERN-hall | carried |
| Lowmarch | LOH-march | proposed B7 |
| Thornwater | THORN-waw-ter | proposed B7 |
| Oxhollow | OKS-hol-oh | proposed B7 |
| Millrace | MILL-rayss | proposed B7 |
| the Fallow | FAL-oh | proposed B7 |

### Terms and forms

| Term | Say / handle |
|---|---|
| Quieting | KWY-et-ing; Karis's coined name, three syllables |
| Kindling | KIND-ling |
| Arbiter | AR-bit-er |
| the Compact | KOM-pakt |
| sigil | SIJ-il |
| Path | PATH; capital concept, ordinary vowel |
| Wind | WIND, noun |
| Iron Skin | EYE-urn SKIN; two words |
| Pressure | PRESH-er |
| Compression | kom-PRESH-un |
| Ember | EM-ber |
| Shadow | SHAD-oh |
| Storm | STORM |
| Anchor | ANG-ker |
| Blade | BLAYD |
| Tide | TYDE |
| Tide-adjacent | TYDE ad-JAY-sent; light hyphen pause |
| the read | REED; Cael's perceptive faculty |
| quiet ground | KWY-et ground; descriptive precursor to `the Quieting` |
| the Line | LINE |
| the Ring | RING; the Fallow site |
| the Stair | STAIR; the road/site on Pike's slip |
| Iron / Copper / Bronze / Gold | ordinary tier names; do not spell them |
| `FRAGMENT ACQUIRED` | `fragment acquired`, neutral system voice; ordinary words, not letters |
| `[UNBOUND]` | `unbound`; brackets silent |
| Hesk's book / Cael's log | light document register; italic emphasis silent |

`stillhound` and `shale-back` do not occur in chapters 31–45 and are therefore intentionally absent from this part's
range-limited lexicon.

---

## 5. Direction handoff

1. Apply Cael = KAYL and Lira = LEER-a in every assigned chapter.
2. Use the lexicon above for Oryn, Teague, Pike and the place names; keep the narrator single-voice and restrained.
3. Follow the homograph table, especially LED/LEED, REED/RED, KLOHZ/KLOHS and WOWND/WOOND.
4. Give logs, leaves, slips and the covenant a light document register. Do not voice italics, brackets, fences or scene
   break rules.
5. Render the ch37 notice neutrally, one flattened line at a time, and ch42 `[UNBOUND]` without brackets.
6. Read the three visual ordinal forms as full spoken ordinals. Do not otherwise alter the written word lock.
7. Preserve the long pause at every `---`; no paragraph in this range needs `fpaudio.py`'s over-700 sentence split.


---

# PART 4 — chapters 46–60

## Book 7 — *Void Roads*: line and listening proof, part 4 (Step 4)

Reader: Codex, independent review seat, fresh context, 2026-10-11. Scope: `manuscript/chapter-46.md` through `manuscript/chapter-60.md` only (74,480 words; eighty scenes), read in full and in order from numbered output. The listening model is one narrator, one segment per paragraph, `---` as a long pause, with italics flattened by `audio/fpaudio.py`.

Read first: Book 5’s and Book 6’s listening proofs; Book 7’s completion plan, whole-arc read, pass brief, both applied lane reports and lane rulings; the edition’s audio and Reader Standard; OWNER-DECISIONS #33, #42 and #48–51; BOOK_MAP §10; `protected-patterns.txt`; and `audio/fpaudio.py`. Chapter-by-chapter scene evidence, every requested restored-unit ruling, every in-range lane-join ruling and the closing mechanical audit are in `listening-notes-part4.md`.

**No manuscript file was modified, and no git command was run.**

---

## 1. Verdict

**PASS — render-ready; no line fixes proposed.**

The fifteen chapters are clean at the line-and-listening level. No unbalanced or mismatched quotation, unplaceable speaker, broken lane join, cut antecedent, mid-clause ending, lower-case restart, accidental word duplication, dangling comparison, or inconsistent count was found. The contract council, Millrace treatment scenes, trap and Hall action, Oryn’s work, Lowmarch board readings and Teague-crew exchanges all remain attributable by tag, position, role or short controlled alternation.

The eight Lane B speech joins in this range are sound: ch46 ×2, ch48, ch51, ch53, ch55 and ch60 ×2. Lane A covers chapters 1–30 and therefore contributes no join to this range. The coordinator-restored units in ch46–49, ch52, ch54–56 and ch58 have intact lead-ins and follow-ons. The full before/unit/after evidence is in the notes.

The deployment sequence is coherent: twenty-three after the trap, twenty-six after three Hall uses, and twenty-seven after the Tide read. Chapter 58 approaches and paces the fourth site from outside without touching or crossing it. All protected lines, log entries, the inventory and the closing stand untouched.

---

## 2. Findings by category

### 2.1 Quotation marks and speaker attribution

- All 2,432 straight double-quote marks resolve within their paragraphs. There is no odd-quote paragraph, unresolved multi-paragraph speech or curly double quote in chapters 46–60.
- The ch46 contract council calls each vote-holder in turn. The two joined speeches remain single-speaker arguments, and Lira’s non-vote is clearly distinguished from the four raised hands.
- Oryn’s patient speech, self-talk and room-directed orders remain separable through physical position, tags and the treatment sequence. The old woman, steading’s woman, bowman and carter are introduced by stable roles.
- At Lowmarch, Pike’s repeated board wording is explicitly introduced as reading aloud. Meadow answers, Teague’s crew and the five-person council do not blur into Pike’s document voice.
- During the trap and Hall action, counts and orders retain owners. Seln’s bolt count, Oryn’s mending count, Karis’s experimental count, Lira’s warnings and Cael’s relayed wall order are all anchored before any untagged continuation.

No quotation or attribution fix is required.

### 2.2 Ear collisions and homographs

No collision requires a rename or line change. Direction should preserve these contrasts:

| Pair or cluster | Direction |
|---|---|
| Oryn / Ostrand / Oxhollow | OR-in / OST-rand / OKS-hol-oh. Oryn is a person; the latter two are places. |
| Karis / Cael | KAIR-iss / KAYL; two syllables against one clipped syllable. |
| Seln / Selm- | SELN, one syllable. No Selm- name occurs in this range. |
| Teague / Pike | TEEG / PYKE; both are crew-and-board voices, but their onsets and roles are distinct. |
| Lowmarch / Millrace | LOH-march / MILL-rays. `mill-race` in the water-channel sense is the same ordinary pronunciation as *Millrace*. |
| Thornwater / the Fallow / the Hall | THORN-waw-ter / FAL-oh / HAWL. Keep *Fallow* at two syllables. |
| Hesk / Vell / Ephram | HESK / VELL / EF-ram; each occurs in document or memory context. |
| Brom / the bowman | BROM / BOH-man. Teague’s role-label `the bow` is BOH. |
| Lira / Line | LEER-a / LYNE. |

All requested homographs were heard in context:

| Word | Intended reading in this range |
|---|---|
| `lead` | LEED in `lead it off`. |
| `wound` | WOOND for the injury; WOWND for tape or binding wrapped around something. |
| `close` | KLOHS as adjective/adverb; KLOHZ as verb, by syntax. |
| `read` | REED for an imperative, infinitive, present tense or Cael’s perceptive faculty; RED for past-tense document or ground reading. |
| `tear` | TAIR for cloth or paper. |
| `live` | LYV in `live ruts`. |
| `wind` | WIND for weather and the Path; WYND in `Wind it round`. |
| `bow` | BOH for the weapon and the bowman’s role-label; BAU in `the bow of a skiff`. |
| `row` | ROH for stitches, stakes, pebbles or bowls. |
| `minute` | MIN-it throughout. |

Every bare `as` was checked in context. The name-led examples (`as Pike counted`, `as Karis did`, `as Cael had seen`, `as Lira had taught`, `as Seln had counted`) express manner or comparison, not an ambiguous substitute for “while.”

### 2.3 Formatting the narrator meets

- There is no FRAGMENT ACQUIRED block, bracketed form or code fence in chapters 46–60. The earlier notice and `[UNBOUND]` are outside this range.
- All 268 asterisks pair. `fpaudio.py` strips them, so Cael’s logs, Pike’s ledger line, Seln’s field entry, Hesk’s note, Cael’s letters, Oryn’s letter, the inventory and the closing written findings need a modest document register rather than voiced emphasis.
- Pike’s `HOLD.` in ch46 is an ordinary word in capitals: say “hold,” not the letters.
- Initials in the letters (`H.`, `C.`, `O.`) are letter names; the punctuation is silent.
- No Arabic numeral occurs in body text. All day counts, stake numbers, sheet totals, marks, distances and combat counts are already written as words. The deployment progression is internally consistent.
- Every `---` has a blank line before and after and should receive the specified long pause.
- Generic `season` and `cold term` comply with the edition rule. There is no season name, month name, month order or English weekday. Measures remain feet, yards, paces, strides, cords, hands, fathoms and furlongs.
- The protected ch60 inventory is one 912-character paragraph. The renderer will split it at sentence boundaries; keep one neutral log voice through the split and do not alter its wording.

No narrator-format text fix is required.

### 2.4 Typos, joins and continuity

- All eight in-range Lane B speech joins are grammatical and audible. The removed beats do not create a speaker switch or fuse unrelated thoughts.
- Each coordinator-restored unit retains a complete sentence before and after it. In particular, ch55’s restored reserve-cost sentence supplies the ethical antecedent for Oryn’s `Twice`, and ch56’s restored trail evidence supplies the antecedent for Teague’s `such pains` inference.
- Ch47–48 preserve the distinction between the refused request concerning the boy and Oryn’s later permission to read her own wrist. The consent sequence is explicit aloud.
- Ch58 says `Nobody crossed`, then keeps Cael’s boots beside the others. The fourth site remains approached and paced from outside, not touched.
- The apparent repetitions `had had` are grammatical pluperfect constructions. No accidental doubled word was found.
- The incomplete ch52 field-ledger phrase `third site confirmed on bearing —` is an intentional unfinished written entry and is described as such in the next narration.

No typo, broken join or continuity fix is required.

### 2.5 Paragraphs over about 700 characters

Lengths are narrator-flattened characters after markdown emphasis is removed and whitespace is collapsed. These are the only paragraphs over 700 characters in the range:

| Location | Characters | Opening cue |
|---|---:|---|
| `manuscript/chapter-47.md:153` | 794 | `"I was to be at this gate on the ninety-sixth…` |
| `manuscript/chapter-50.md:95` | 709 | `"I am touching it. That is a different thing…` |
| `manuscript/chapter-50.md:177` | 717 | `"I shall say the condition, since it is to be used…` |
| `manuscript/chapter-51.md:173` | 708 | `"A fence that failed at dusk, at its knot…` |
| `manuscript/chapter-55.md:113` | 719 | `The first was the one that she had lit…` |
| `manuscript/chapter-56.md:117` | 761 | `It kept a road for the first of them…` |
| `manuscript/chapter-60.md:37` | 912 | `Wind-adjacent — Lira. Pressure-adjacent…` |

---

## 3. Exact line fixes

None. No old/new replacement is proposed, so the unique-match and eight-word overlap gates are not invoked. No protected line is changed.

---

## 4. Pronunciation lexicon

Only names and terms that occur in chapters 46–60 are included. Shared entries carry forward Book 5/6 direction; Book 7-only entries are proposed direction, not manuscript changes.

### People

| Name | Say | Identification/status |
|---|---|---|
| Cael | KAYL, one syllable | Owner-confirmed #33; protagonist. |
| Hesk | HESK | Carried; Cael’s grandfather, his book and letter. |
| Lira | LEER-a | Owner-confirmed #33; Wind. |
| Brom | BROM, as in “from” | Carried; Iron Skin. |
| Karis | KAIR-iss | Carried; Ember and field analyst. |
| Seln | SELN, one syllable | Carried; records and ground reader. |
| Oryn | OR-in | Proposed Book 7; healer, Tide. |
| Teague | TEEG, one syllable | Proposed Book 7; independent crew captain. |
| Pike | PYKE | Proposed Book 7; Lowmarch ledger-keeper. |
| Rooke | ROOK, as in “book” | Carried; quoted instructor. |
| Vell | VELL | Carried; Ardenmere ledger-keeper, letter addressee. |
| Ephram | EF-ram | Carried; Blade, named in the inventory. |
| Reydan | RAY-dan | Carried; Compression source, named in the inventory. |
| Daeva | DAY-va | Carried; Storm source, named in the inventory. |

### Places

| Name | Say |
|---|---|
| Lowmarch | LOH-march |
| Millrace | MILL-rays |
| Thornwater | THORN-waw-ter |
| Oxhollow | OKS-hol-oh |
| Ostrand | OST-rand; carried |
| the Fallow | FAL-oh, two syllables |
| the Stair | STAIR; the Quieting site |
| the Hall / the drowned hall | HAWL |
| Denvash | DEN-vash; carried |
| Ardenmere | AR-den-meer; carried |
| Ternhall | TERN-hall; carried |

### Terms and document handling

| Term | Say / handle |
|---|---|
| the Quieting | KWY-et-ing; three syllables |
| the Quiet | KWY-et; distinct from the named process/site class *the Quieting* |
| the Line | LYNE |
| Path | PATH; capitalize only as the system category already printed |
| Wind | WIND, the noun; do not use WYND for the Path |
| Pressure; Iron; Compression; Ember; Shadow; Storm; Anchor; Blade; Tide | Ordinary-word pronunciations; preserve each as a Path or fragment category by context. |
| `-adjacent` | ad-JAY-sent, with a light hyphen pause; carried |
| the Compact | KOM-pakt; carried |
| Arbiter | AR-bit-er; carried |
| sigil | SIJ-il; carried |
| wold-wyrm | WOAHLD-wurm; one compound with a light hyphen pause |
| the read | REED; Cael’s perceptive faculty |
| Hesk’s book; the field ledger; Pike’s book | Document register where introduced; italics do not survive preprocessing. |
| `HOLD.` | “hold,” sentence case; never spell the letters |
| marks | Ordinary plural; currency in context |
| cold term | Ordinary words; the allowed seasonal interval, not a named season |

---

## 5. Lock recommendation

Chapters 46–60 can be locked and hash-bound as they stand. Preserve the seven long-paragraph split points as audio-direction work only, and carry the homograph and lexicon notes into narrator direction.
