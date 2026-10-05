CLOSE — scope: Book 2, Movement 4 repair r1, chapters 23–29. Every repair-brief item is resolved; the continuity, formula, reader-clarity, and listening checks pass; no manuscript line fix or second repair is warranted.

# Targeted recheck — repair r1

I read the full current movement and checked every changed region against `pre-repair/` with `diff -U0`, then checked the movement against the book map, ledger rulings and entry state, Movement 3, the source chapters, and the movement packet.

## (1) Brief items

### 1a. Remove spoken/thought bracket notation — RESOLVED

The zero-context diff in chapter 26 replaces the spoken document-style token:

> pre-repair: `"[SHATTERED]," said Cael.`
>
> current: `"Shattered," said Cael. "That's my word. The one the hall in Denvash wrote down."`

That follows the edition convention: brackets appear only inside documents read verbatim; spoken language is plain. The comparison named in the brief, Book 3 chapter 5, likewise has plain spoken `"Where's shattered?"` and `"Shattered. My uncle says..."`.

A bracket sweep of chapters 23–29 finds only `[unnamed]` in chapter 28, inside the fenced and verbatim system notice. No other spoken or thought bracketed token remains.

### 1b. Give the chapter 25 Brom cutaway new knowledge instead of replay — RESOLVED

The opening has been recast from the generic pre-repair summary—`Brom had known what the boy was carrying from the first blow.`—to the precise observation:

> `Brom had known from the first blow that the boy had brought Lira's dock partner onto the floor with him.`

The cutaway then moves promptly into knowledge available only from Brom's side:

> `That was why he threw people far. Tonight he had thrown the boy further than any blow needed. ... every time and on purpose, out past the place where the purse lay open and the boy could have reached in.`

> `Pressure had gathered behind the boy's next attempt. Twice. Both times he had held it. ... The Wind-flicker in him had dimmed with the holding.`

> `In the third the boy was very quiet on the read.`

> `Then it was not.`

This preserves Brom's permitted full interiority while making the scene additive: deliberate displacement beyond the recovery gap, the held Pressure and its cost, and the third-exchange absence.

### 2. Compare the third-exchange absence with the Iron-adjacent read without explaining it — RESOLVED

Chapter 29 makes the comparison by observed difference and explicitly distrusts the temptation to equate the events:

> `The temptation was to put that beside what had happened in the third exchange and make them fit as neatly as a lock and a key. That neatness was the reason not to trust it.`

> `Not the same thing. This came with a hush and a notice; the third came with neither. This left me emptied; the third left nothing behind because nothing had been there. This is a piece of his read. The third was his read finding nobody there. One I have and can't use yet. The other I never had, and can't find. It stays where it fell.`

The passage reports phenomenology only. It offers no theory of the absence's source, does not equate it with the unbidden Iron-adjacent fragment, and does not spend the session-nine reserved formulation `Still don't know what that was.`

### 3. Reduce repetition and local density in chapters 27–29 — RESOLVED

The `diff -U0` record shows the intended local work without damage to speech, notices, or bout beats:

- Chapter 27 deletes redundant re-explanations such as `From the knuckles: the hold is a well`, the repeated hit/answer recap, and `The well. The turn.`; it also joins short runs that are one thought and divides dense paragraphs at shifts of image or inference.
- Chapter 28 removes another lean/well/angle recap and a repetitive strike loop, while breaking the long interpretive paragraphs around the fragment and preserving the notice verbatim.
- Chapter 29 shortens the source recap, consolidates the exclusivity statement, and separates the final comparison into audible units.

The current movement is 36,457 chapter-file words (36,356 prose words in the formula tool), within the brief's 35,500–38,000 range. The revised passages retain the necessary tactile anchors but no longer repeatedly rename the same action.

## (2) Continuity

Continuity passes.

- **Calendar:** the bout is Tuesday; the wall follows Wednesday; day four lands Saturday; the next sequence runs Sunday through Tuesday; teaching is Wednesday; posting is the following Monday. The order and elapsed recovery time agree across chapters.
- **Body state:** Cael's swollen knees, crossed fixes, forearm and shoulder effects, and staged return to full-strength work remain cumulative. Brom's rib bruise and Lira's bruise also carry correctly.
- **Status and counts:** Cael remains fifteen and Assessed-Copper. The bout has four exchanges and ends when Cael raises his own hand. Brom is Iron-equivalent; Lira remains provisional Iron-equivalent. Cael has three partial fragments after the notice.
- **Knowledge boundaries:** no character learns a deliberate ability-taking method. The Iron-adjacent fragment arrives unbidden after three mornings. Brom says only the protected observation `You absorbed part of my Path.` The third exchange has no hush, notice, cost, or usable handle, and neither Cael nor the narration explains its source. No Compact, UNBOUND, Architect, watcher, or later-volume reveal leaks into the movement.
- **Relationship boundary:** Lira's controlled distance remains intact; the Movement 5 declaration is not advanced.
- **Protected lines:** the floor exchange in chapter 25, `"Show me the log sometime." / "Maybe."`, the chapter 28 notice, `"You absorbed part of my Path."`, and the final word-choice exchange all remain exact where mapped.

The bout mechanics also remain consistent with Movement 3. Activation still begins with the half-beat breath before contact; the unfamiliar hold lasts about one beat and shortens with repetition; recovery lengthens under expenditure. The plan fails by those intervals, not against them: Brom's hard answer throws Cael beyond the recovery opening, and the second route fails because Brom can activate from the read before contact. The chapter 25 cutaway confirms that the displacement was deliberate and that Cael twice held Pressure at a cost. Nothing makes recovery vanish or moves activation to a contradictory point.

## (3) Formula

Required commands were rerun on the current chapters.

`python3 editions/monroe-1.3/tools/formula_metrics.py editions/monroe-1.3/book-02-iron-circuit/manuscript/chapter-{23..29}.md`

| Metric | Result | Reading |
|---|---:|---|
| Chapters | 7 | complete movement |
| Total words | 36,374 | tool total |
| Prose words | 36,356 | inside brief range |
| System-notice words | 18 | documentary text |
| Sentences | 2,667 | — |
| Sentence mean | 13.63 | within 13–15.5 working range |
| Sentence median | 9 | short of the 11 target, but not a new local clarity fault |
| Population SD | 12.0 | below the 15 target |
| Sentences at five words or fewer | 30.2% | controlled short-beat emphasis |
| Sentences at forty words or more | 4.3% | within 2.5–4.5% working range |
| Paragraphs | 909 | — |
| Paragraph mean / median | 40.0 / 26 | median remains inside the accepted ceiling |
| Scene breaks | 35 | 9.62 per 10k words |
| Words per scene | 866.0 | within 850–1,050 working range |
| FRE / FK | 92.7 / 3.72 | plainer than formula targets; intelligible and voice-consistent |

The exact-formula departures—median sentence length, variance, and reading-level indices—remain movement-level tendencies rather than defects introduced by repair r1. They do not produce mechanical cadence or reader confusion in the revised regions.

`bash editions/monroe-1.3/tools/ed.sh overlap book-02-iron-circuit 4`

> `0 unprotected shared runs of >= 8 words; 7 protected runs (allowed)`

`bash editions/monroe-1.3/tools/ed.sh gates book-02-iron-circuit 4`

All seven chapters report `reader_standard=0 metadata=0 modern=0`.

`bash editions/monroe-1.3/tools/sweep_probe.sh book-02-iron-circuit 4 4`

| Chapter | Sentences | Skeleton | Close |
|---|---:|---:|---:|
| 23 | 222 | 1 | 11 |
| 24 | 235 | 0 | 10 |
| 25 | 209 | 2 | 15 |
| 26 | 265 | 1 | 13 |
| 27 | 213 | 1 | 13 |
| 28 | 185 | 2 | 11 |
| 29 | 217 | 0 | 10 |
| **Total** | **1,546** | **1** | **12** |

No formula result requires another repair.

## (4) Reader clarity

Reader clarity passes.

- Speakers remain attributable in the crowded yard scene and in the three-person teaching conversations; action beats refresh identity before ambiguity can develop.
- The bout's geometry is trackable through the rope, post, reach, and displacement images. The failed plan is understandable before the later explanation confirms it.
- Chapter 25 clearly distinguishes what Brom observed from what Cael experienced. Chapter 29 then distinguishes the two anomalous events through notice, hush, cost, and retained fragment without asking the reader to accept an unsupported theory.
- Technical inference remains accessible through concrete comparisons—door, well, floor, weight, and reach—rather than abstract exposition, meeting the thirteen-year-old-reader lens without flattening Cael's established fifteen-year-old perspective.
- The Reader Standard gates are zero: no metadata leakage, modernism, profanity, sexual content, or gratuitous gore. The violence is consequential, consent and privacy remain active concerns, and uncertainty is stated honestly.

## (5) Listening proof

Every chapter and every changed region was checked aloud/on the page for balanced dialogue and emphasis marks, scene-break spacing, narrator-safe numerals and abbreviations, homographs and ear collisions, and broken joins.

| Chapter | `"` marks | `*` marks | Fences | Listening result |
|---|---:|---:|---:|---|
| 23 | 222 | 18 | 0 | pass |
| 24 | 8 | 20 | 0 | pass |
| 25 | 90 | 10 | 0 | pass; the 24/25 POV seam is clean |
| 26 | 338 | 46 | 0 | pass; `Shattered` is natural spoken text |
| 27 | 268 | 20 | 0 | pass; revised joins and paragraph breaks hold |
| 28 | 212 | 88 | 2 | pass; the fenced notice is balanced and verbatim |
| 29 | 98 | 42 | 0 | pass; the final comparison remains aurally distinct |

All quote, emphasis, and fence totals are balanced; the per-line odd-mark scan found no unmatched line. Every `---` has blank-line spacing. Prose contains no unsafe numeral or abbreviation; `B.` and `L.` occur only as deliberate log initials, and `[unnamed]` occurs only in the verbatim notice. The potentially variable readings of `read`, `Wind`/`wind`, `lead`, `live`, and `wound` are disambiguated by syntax and context. No broken sentence, false attachment, duplicated join, or audible referent collision remains.

## Exact line fixes

None.
