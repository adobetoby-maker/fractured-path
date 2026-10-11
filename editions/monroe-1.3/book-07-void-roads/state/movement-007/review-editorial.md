# Editorial review — Movement 007

**Verdict: RATIFY WITH REQUIRED LINE REPAIR.** The movement is structurally strong, canon-coherent, emotionally persuasive, and particularly successful as a sustained tactical set piece. It is not ready to close while five literal coordinator markers remain in the prose and one protected document is summarized instead of restored verbatim.

## Review posture and coverage

This is a fresh-context **informed editorial review** by the review seat, not a blind cold read and not a real human audience test. Canon, plan, formula, and protected-wording evidence were supplied. Coverage is limited to all eight declared files, chapters 45–52, in order: 43,141 prose words, days 111–115 past the Line.

The numerical discussion uses the supplied `formula_metrics.py` results without re-estimation. The source-reuse discussion uses the supplied overlap result.

## Unscored reader response

Interest catches first when Pike says the Fallow line in the crew's hearing and the whole Lowmarch room silently revises its judgment. It tightens again when the three-hundred-mark paper is diagnosed as a lure, and it becomes difficult to put down from Brom's bolt through Cael's call of “Back.” The day in the chamber is the movement's strongest sustained passage: each small resource decision matters, every power not used matters, and the eventual escape is earned by restraint, observation, and previously planted limits.

Interest slips briefly in the long procedural middle of chapter 52, after the immediate danger has ended and before *bearing* turns measurement into direction. The work remains meaningful, but a fluent thirteen-year-old is more likely than an adult genre reader to feel the accumulation of courses, cords, kinds, sheets, stations, and radii before the new question resolves it.

Seln matters most unexpectedly. His desire for a face, his refusal to remove the case unilaterally, and his breaking of the anonymous bow make his restraint and anger feel like the same character rather than competing versions of him. Oryn is equally important: her refusal at the public bench, later permission on the road, terms of service, and work without her Path make consent and vocation active story forces. Cael's defining movement is not that he can act inside the Quieting; it is that he repeatedly chooses when not to.

The next expected event is the bearing followed toward the Drowned Hall, with Karis's second-site evidence turning the isolated floors into a deliberate alignment. I would continue. The literal production markers must be removed first.

## Principal findings

### 1. Blocking: protected wording and production markers

Five `[[TIER-B: ... coordinator to supply protected text]]` markers appear as literal manuscript prose. Three replace BOOK_MAP-protected language outright; two mark additional protected packet units whose following BOOK_MAP lines are present. A sixth protected item—the Fallow copy—is narrated in summary although BOOK_MAP requires it exact when read again in this movement.

| Location | Finding |
|---|---|
| Chapter 45, line 109, beginning “It was the eighth line…” | Pike's protected Fallow copy is summarized rather than spoken verbatim: *Recovery, Fallow road, broker's posting… No price paid.* The map explicitly protects the Ch17 rereading. |
| Chapter 45, line 195 | Literal marker for Pike's Tier-B “Nothing else ever…” unit. “I'd not take it.” follows intact. |
| Chapter 46, line 109 | Literal marker for Seln's Tier-B “Take it…” unit. The protected “They'll send people… Six years I've wanted a face.” follows intact. |
| Chapter 48, line 13 | Literal marker replaces Oryn's protected affirmative answer beginning “Yes. That's the answer, and I'm the one giving it…” |
| Chapter 49, line 275 | Literal marker replaces the protected sentence containing “the bolt's the plug.” |
| Chapter 52, line 283 | Literal marker replaces the protected radius sentence containing “every ten cords and a piece. Two hundred and twenty yards and a stride, to the stride.” |

All other applicable BOOK_MAP §10 units for source chapters 17–20 were found in their intended scenes without a material wording variance: the Stair slip; “Eleventh. Teague's ten up”; the trap diagnosis and council; the protected movement logs; Oryn's refusal and terms; the road reading; the trap, stair, return, and Teague exchanges; the kit, *bearing*, forty-one kinds, and the ruler line.

This is a narrow repair, but it is mandatory. The missing Tier-B sentences must come from the authorized protected source, not be reconstructed from the excerpts or newly composed.

### 2. Formula alignment: strong primary shape, weak spread and low register

The movement lands the primary working ranges for sentence mean, long-sentence share, and scene spacing. Its main numerical departure is not excessive clipping: it is a much narrower sentence distribution and substantially easier measured register than the selected formula.

| Metric | Observed | Target / working range | Editorial reading |
|---|---:|---:|---|
| Sentence mean | 13.86 | 14.6 / 13–15.5 | Aligned with working range. |
| Sentence median | 10 | 11 | Near target. |
| Population SD | 11.53 | ~26 | Material under-spread. The long tail exists, but the overall sentence distribution is much less varied than selected. |
| Sentences ≤5 words | 25.9% | 27.7% / up to ~34% | Close; no shortage requiring artificial fragments. |
| Sentences ≥40 words | 4.1% | 3.3% / 2.5–4.5% | Aligned with working range. |
| Paragraph mean | 36.16 | 26.8 directional proxy | High. |
| Paragraph median | 24 | 18 / up to ~30 | Within accepted print-prose drift. |
| Marked scene breaks per 10k | 9.04 | 8.7 | Aligned. |
| Words per scene | 917.9 | ~950 / 850–1,050 | Aligned. |
| Flesch Reading Ease | 94.8 | 72.3 | Material drift toward very easy prose. |
| Flesch-Kincaid grade | 3.48 | 6.8 / 3.5–6 | Essentially at the working floor, but far below the selected exact target. |

Method: Markdown H1s and marked scene breaks are stripped; fenced system notices are excluded from prose sentence/readability measures; paragraphs are non-empty manuscript lines; sentences use the repository regex tokenizer; syllables use a vowel-group heuristic with silent-e and `-le` adjustments. Proper names and system terms are estimated like ordinary words. The tool reports zero system-notice words; because the Tier-B markers are unfenced plain text, they are included in the prose totals. This creates a small known contamination but does not explain the size of the readability gap.

The productive repair is selective. Preserve short dialogue and fight landings. In the reflective and analytical passages—especially Seln's chapter 46 cutaway, the chapter 50 design discussion, Teague's chapter 51 cutaway, and the chapter 52 research sequence—allow more full hierarchical sentences and more precise multi-syllable vocabulary where the idea already warrants it. Do not inflate diction merely to move a score, and do not dismantle the clear action chronology.

The 43,141-word movement is 3,141 words above the 40,000 plan and therefore a plan deviation. It is not, by itself, a story defect. The Stair action earns its room, and the review rubric explicitly protects developed action from arbitrary shortening. If the book total later requires recovery, look first for redundant setup or repeated explanation outside the central trap rather than cutting the containment, ascent, or rim break.

Progression-vocabulary density, POV percentage, development-beat rate, and the optional secondary signals were not supplied by reproducible tooling and are therefore **UNMEASURED**, not estimated. Qualitatively:

- POV shape aligns: Cael dominates; the only substantial secondary segments are Seln after the day-112 council and Teague after the day-114 rescue, both purposeful and bounded.
- Progression teaching surfaces at genuine final-third turns rather than as repeated tutorial: Tide reading, Quieting failure, Shadow concealment, Anchor perception/unbinding, and the deployment inventory.
- Development is broadly distributed. Cael accepts refusal and delays self-reading; Lira carries rather than spans and finds the stair; Brom supplies the door insight and later bears the kit; Karis refuses false certainty; Seln rejects unilateral control; Oryn defines the route relationship; Teague turns a four-mark job into an honest promise kept.

## Continuity, canon, and plan audit

No verified canon contradiction was found.

- **Calendar and geography:** days 111–115, Thornwater → Lowmarch → Millrace → the Stair, and the road distances all reconcile. Oryn's route reaches Millrace through the previously established bending circuit without reopening the resolved “north” issue.
- **Bodies:** Lira remains flat-footed on the unmended right ankle and keeps the left arm slung; the arm reopens on the twentieth stair and is closed again outside the line. Brom's right shoulder takes one bolt, is taped inside, then drawn and mended once outside. Cael pays for Shadow, the stock blow, Storm lag, and the Ember burn. Seln remains unmarked. Oryn's reserve is priced aloud.
- **Capability rules:** the tenth is used only with permission on Oryn and does nothing in the fight. Shadow is used for the second and final time, below sightlines that could carry it west. Anchor perception appears at its established twelve/ten-foot boundary; the later unbinding is separate, at touch, with no invented ranged unbinding. Wind keeps the one-count landing lock; Storm produces the ten-count lag; Compression is contact-bound.
- **Deployment count:** the movement advances the log from thirteen to fourteen after the road reading and to twenty-three after the Stair, with each counted use itemized. The eleven prior Wind practice leans do not re-enter the deployment number.
- **Knowledge boundaries:** the rim sees only an outside declaration and cannot see the concealed ascent. Teague infers multiple capabilities but not the mechanism. No face, name, seal, office, or decoded index/mark is disclosed. Karis's hypothesis remains unspoken. The case remains shut.
- **Objects and accounts:** three boxes, the mule, Seln's case, the crossbow and five unspent bolts, 102 marks in hand, the unpaid three hundred, recovered kit, field ledger, and twenty-nine Stair sheets all carry correctly.
- **Plan adherence:** Teague's crew stays unnamed; Oryn is a stop on her route rather than “the sixth”; the Stair is paced on day 115; the movement closes with the brass edge poised above the map.

## Reader Standard

**Pass, after marker repair.** The prose contains no detected banned profanity, obscenity, crude slang, blasphemous oath, sexual content, or innuendo. Violence is consequential but not gory. Brom's wound, Lira's reopened arm, Cael's bills, and Oryn's limits all prevent spectacle from becoming consequence-free.

The moral frame is especially strong for the intended thirteen-year-old reader: Oryn's “no” is accepted immediately; her later “yes” is hers to reopen; Cael withholds force under pressure to protect others and a secret; he declines to strike an exposed man; Seln rejects the apparently kind unilateral act of taking the case away because it would erase the crew's choice; Teague keeps a promise that has no price. Courage, loyalty, restraint, and truth all cost something on the page.

One-pass comprehension is generally good during the action. The five literal markers fail the audio-first standard completely until repaired, and chapter 52's clustered measurement terms warrant the selective clarity pass described above.

## Reader-lens scores

These are editorial lenses, not demographic research or a release average. Confidence is **medium** for the simulated thirteen-year-old response and **high** for the adult genre judgment unless noted.

| Dimension | Exact passage location | Fluent thirteen-year-old | Adult genre reader |
|---|---|---|---|
| Opening pull | Ch. 45, departure from Thornwater through Cael declining the hurried self-reading; then Pike says the line before the door shuts | **7/10** — concrete cold-road texture and character continuity, but the true movement problem arrives late. Medium. | **8/10** — the quiet departure carries accumulated state and makes Lowmarch's changed judgment land. High. |
| Keep reading | Ch. 45, the nail and three-hundred-mark Stair paper; Ch. 46, the council | **9/10** — obvious trap, divided honest votes, and a credible reason to take it. Medium. | **9/10** — local payoff at the board plus a larger institutional threat. High. |
| Interest / freshness | Ch. 46, the pre-restriction inventory; Chs. 49–51, a trap designed around Pathlessness | **9/10** — powers matter most when the story makes not using them tactical. Medium. | **9/10** — contract-board economics, medical logistics, and counter-surveillance make the problem specific. High. |
| Clarity / flow | Chs. 45:195, 46:109, 48:13, 49:275, 52:283; Ch. 52 from the twenty-nine sheets to the radius inference | **6/10** — action geography is clear, but production markers and dense measurement vocabulary break one-pass reading. High on marker effect. | **7/10** — the causal chain is excellent; the literal gaps prevent a higher score. High. |
| Character attachment | Ch. 46, Seln chooses not to take the case alone; Ch. 47–48, Oryn's refusal, terms, and permission; Ch. 51, “No faces.” | **9/10** — choices reveal who these people are under pressure. Medium. | **9/10** — Seln, Oryn, Lira, Brom, and Teague all act from distinct private values. High. |
| Humor / warmth | Ch. 45, the mule at the ford; Ch. 47, six bowls and the grey jenny; Ch. 48, “He asked twice and got one”; Ch. 50, Brom's list | **8/10** — welcome relief without puncturing danger. Medium. | **8/10** — dry, character-specific humor carries affection and competence. High. |
| Action / suspense | Ch. 49, “Ridge” through the run down; Ch. 50, the grey square and ascent; Ch. 51, declaration and rim break | **9/10** — positions, resources, choices, and costs remain trackable across a long contest. Medium-high. | **9/10** — the stalemate develops tactics and relationship rather than repeating exchanges. High. |
| Progression payoff | Ch. 48, first permitted reading of another; Chs. 50–51, Shadow plus Anchor plus the declared suite; Ch. 51 deployment log | **9/10** — earlier lessons solve new problems under changed conditions. Medium. | **9/10** — the win synthesizes restraint, perception, costs, and planted rules without an unexplained upgrade. High. |
| Connection | Ch. 45, day-111 injuries and debts; Ch. 46, Rooke's words; Ch. 52, Fallow/Stair equality and *bearing* | **9/10** — prior promises visibly become present tools. Medium. | **9/10** — state, relationships, research, and institutional pressure all carry across chapters. High. |
| Read-aloud quality | The five bracketed markers; otherwise Ch. 49's bolt/run sequence and Ch. 51's rim action | **6/10** — distinct voices and clean action cadence, but the markers are impossible narration and some technical passages are clause-heavy. High on marker effect. | **7/10** — strong attribution and cadence outside the unresolved inserts. High. |

## Source originality

**Pass on the supplied source-overlap result:** 0 unprotected shared runs of eight or more words; 32 protected runs, allowed. No unprotected source reuse is a finding. After the protected-text repair, rerun the same gate so the inserted language is classified as protected and no surrounding bridge accidentally reproduces unprotected source phrasing.

## Repair brief

1. **Location:** chapter 45 line 109; chapter 45 line 195; chapter 46 line 109; chapter 48 line 13; chapter 49 line 275; chapter 52 line 283. **Observed issue:** one protected document is summarized and five literal Tier-B coordinator markers remain; three markers replace explicit BOOK_MAP wording. **Effect on the reader:** publication and audiobook prose breaks visibly/audibly, and protected continuity cannot be certified. **Proposed scope:** coordinator supplies the complete authorized Tier-B units and the exact Fallow copy, then verifies every Ch17–20 protected unit once and reruns overlap; no surrounding scene rewrite. **Strength to preserve:** the existing scene staging and the exact protected language already present.

2. **Location:** movement-wide, concentrated in chapter 46's Seln cutaway, chapter 50's design discussion, chapter 51's Teague cutaway, and chapter 52's research sequence. **Observed issue:** sentence SD 11.53 versus ~26, FRE 94.8 versus 72.3, FK 3.48 versus 6.8; paragraph mean is also high at 36.16. **Effect on the reader:** the conceptual maturity sometimes rides on syntactically and lexically very simple prose, while clustered technical paragraphs can still feel dense; the intended thirteen-year-old/adult crossover register is flatter than the formula. **Proposed scope:** a selective sentence-level cadence/register pass in reflective and analytical prose only—join related simple thoughts where hierarchy is clear, use precise vocabulary already natural to the viewpoint, and break paragraphs at true turns. Do not add fragments, chase decimals, or shorten the Stair action. **Strength to preserve:** the exceptionally clear geography, dry dialogue, moral restraint, and earned long-form suspense.
