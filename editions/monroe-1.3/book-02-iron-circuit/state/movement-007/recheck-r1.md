CLOSE WITH LINE FIXES — scope: Book 2, Movement 7 repair r1, chapters 44–51. Every repair-brief item is resolved; continuity, protected wording, Reader Standard, source distance, formula working ranges, reader clarity, and all required automated checks pass. Apply the single chapter-45 scene-separator spacing fix below, then close the movement. No second author repair is warranted.

# Targeted recheck — repair r1

Review seat: Sol, via Codex. Author: Claude Opus 5.5. This is an informed targeted recheck of the same-author repair, not author self-review, a fresh-context cold read, a human audience test, or independent demographic research. I read the full current movement in chapter order, compared all eight chapters to `pre-repair/` with `diff -U0`, and checked the movement against the repair brief and reviews, the author's `## Repair r1` report, `BOOK_MAP.md`, the entry state and latest “After Movement” blocks in `STATE_LEDGER.md`, `packets/MOVEMENT-007.md` including coordinator notes, the preceding movement join, source chapters 18–20, Book 3 chapter 1, and the Book 7 session-nine callbacks.

## (1) Brief items

### Coordinator rulings — RESOLVED

- **Courier sequence:** chapter 43 first establishes the up-river keeper's request for Cael's line. Chapter 44 preserves the earlier growing rumor—“The story about the boy had reached him in a guild hall in the spring”—then shows Reydan asking his keeper to write for confirmation. Chapter 48 correctly makes the returned nine-page report a loan that “must go back”. The rumor motivates; the keeper's exchange verifies and equips. Neither replaces the other.
- **Reydan:** current text keeps him twenty-two, Iron-tier Rank 8, burst-compression Pressure; his father's paid yard begins at ten and the academy at eleven. “Twelve years” is therefore inclusive life history, not twelve academy years.
- **Ansel:** current text leaves his Path unstated, places him at “perhaps twenty-seven or twenty-eight”, makes him a former coast-house Bronze, and gives the dock partner firsthand presence in the hall. His voluntary round remains on his terms.
- **Brom and Hesk:** Brom's questioning at eleven is not physical training and does not conflict with the ruling that he trained his body from twelve. Cael's workshop memory is explicitly at nine.
- **Crowd:** chapter 50 says “room for four hundred”; chapter 51 retains the street as a separate overflow. This leaves Movement 8 room to reach the later-canon total of about six hundred with the street included.
- **Bede and Maud:** the accepted names remain unchanged and do not create a new by-ear collision in this movement.

### Priority 1a — Countdown — RESOLVED

The `diff -U0` changes repair the ambiguous ordinal scheme by anchoring the dramatized days to weekdays:

- Ch45 changes “That's the second morning” to “That's Friday”, and changes the Log line from “Second morning” to “Friday”.
- Ch47 changes “On the second morning” to “On her second morning, the Friday”, and changes “the third afternoon” to “the Saturday afternoon”.
- Ch48 changes “On the sixth morning” to “On the sixth day, the Monday”, and “On the seventh morning” to “On the seventh day”.
- Ch49 changes “On the eighth morning” and “On the ninth morning” to “on the morning of the eighth day” and “on the morning of the ninth day”.
- Ch50 changes “On the tenth morning” to “On the morning of the tenth day, the Friday”.
- Ch51 changes “The tired stage began on the eleventh day” to “The tired stage began on the eleventh day, the Saturday”, and “On the thirteenth day” to “On the thirteenth day, the Monday”.

Independent day table:

| Day | Weekday | Training / event | Page evidence |
|---:|---|---|---|
| 0 | Tuesday | Reydan arrives | Ch44 opening and Tuesday card |
| 1 | Wednesday | Dace tells Cael; plan made | Ch45 “first light on the Wednesday”; bout “Tuesday fortnight” |
| 2 | Thursday | Lira morning 1; Brom session 1; Ansel's account | Ch46; Friday is still “tomorrow” |
| 3 | Friday | Lira morning 2; Brom session 2; redirects 1–3 | Ch47 “her second morning, the Friday” |
| 4 | Saturday | Lira morning 3; Brom session 3 | Ch47 “Saturday afternoon” after the morning |
| 5 | Sunday | Lira morning 4; Brom session 4; redirects 4–6 | Ch47 moving stage and six-redirect total |
| 6 | Monday | Lira morning 5; Brom session 5; report arrives | Ch48 “sixth day, the Monday” |
| 7 | Tuesday | Lira morning 6; Brom session 6; redirects 7–9; drop enters legs | Ch48 “seventh day” and evening drill |
| 8 | Wednesday | Ansel's round; Brom session 7 | Ch49 “morning of the eighth day”; Ansel says “Six nights” |
| 9 | Thursday | Lira grants leave; Brom session 8 | Ch49 “morning of the ninth day”; “Tomorrow's the ninth session” |
| 10 | Friday | Brom session 9; anomaly | Ch50 “tenth day, the Friday”; “Four days” to Tuesday |
| 11 | Saturday | Brom session 10; redirects 10–12 | Ch51 “eleventh day, the Saturday”; shoulder rests until Tuesday |
| 12 | Sunday | Brom session 11; chapel day | Ch51 “twelfth day”; Brom absent Monday |
| 13 | Monday | Rest / inventory; night before | Ch51 “thirteenth day, the Monday”; Dace says “tomorrow” |
| 14 | Tuesday | Reydan bout | Fixed in ch45 and handed into Movement 8 |

The two relative checks also land: “Six days” on Wednesday and “Four days” on Friday both point to Tuesday. Twelve redirects occur on Friday, Sunday, Tuesday, and Saturday—three per session with recovery days—and the shoulder then rests Sunday and Monday before the Tuesday bout.

### Priority 1b — Two line defects and mark scan — RESOLVED

The chapter-51 `diff -U0` closes Dace's speech:

> pre-repair: `Go away. You're one more body, and I'm counting you.` [no closing quotation mark]
>
> current: `Go away. You're one more body, and I'm counting you."`

It also repairs the malformed Wind emphasis:

> pre-repair: `The lock, two* ands*`
>
> current: `the lock is two *ands* he'll count`

Per-paragraph and whole-chapter scans find balanced quotation and asterisk counts in every chapter. No other malformed emphasis or unclosed speech remains.

### Priority 2a — Repeated interpretation in chapters 45–48 — RESOLVED

The repair makes each source contribute a distinct layer:

- Chapter 45 compresses Cael's notebook from a full explanation of paid-yard gap closing to the immediate method problem: “Every fight he had ever won above his weight he had won on a bench first, watching ... This time there was nothing to watch and never would be.” Brom therefore owns the paid-improvement explanation at supper.
- Cael's long supper restatement is cut from the full bench/range account to: “The one thing I'm good at, I won't have till I'm standing in front of him. And by then it'll be his tempo, not mine.”
- Chapter 46 compresses the post-Ansel conclusion from a multi-sentence reprise to the new point: “survival was not the opposite of the method, but its purse.” Ansel retains the memory, shame, and price only he can supply.
- Chapter 48 replaces the report's multi-paragraph replay with the explicit handoff “Most of it they already knew, from Ansel and the carters”, followed by the report's new evidence: stayed gathered, four rematches as different fighters, and the opponent who “declined to be interesting”.

No scene, drill, Ansel beat, or crucial report evidence was removed.

### Priority 2b — Post-tally restatement in chapters 47–48 — RESOLVED

The zero-context diff removes the two named redundant glosses:

- After fourteen in twenty, Brom's old “Seven in ten ... That's the stillness buying it” becomes only “We'll see what it does when I'm not standing like a gatepost.”
- After nine in twenty moving, Brom's old “Three things changed” explanation is removed; the actionable correction remains: “Plant harder ... knock when you've arrived.”
- Chapter 47's end-of-day theory recap is replaced by the single useful recognition that Brom is changing one condition at a time.
- Chapter 48 keeps `Thirteen in twenty` and `sixteen times in twenty` but reduces the after-tally prose to the changed foot timing and next-stage consequence.

The tallies still establish progression; the prose no longer explains each demonstrated result twice.

### Priority 2c — Orientation in chapters 44–46 — RESOLVED

The repair adds brief, local identification rather than a glossary:

- Ch44: “nearly three weeks after Maud” becomes “nearly three weeks after Lira's bout with Maud”; Maud's tactical “middle” is identified in the next sentence. “the two columns from the night of Bede” becomes “the two columns he had ruled on the night Bede beat him”, and *Habit* / *Shape* each receive a one-clause definition.
- Ch45: Feryn is “the Bronze from his first year whose Pressure he carried now”; Darrow Innes carries the Cinder House win; Keth is “the Blade whose seam had won him his rating”; Talis is dropped. The dock partner is reintroduced as “the broken-nosed Bronze washout Lira paid a mark an hour”.
- Ch46: the knock is reintroduced as “the close read he could have sent into her from a forearm away”.

These appositives are sufficient for the fluent thirteen-year-old lens without stalling the movement.

### Priority 2d — Chapter 51 inventory — RESOLVED

The repair preserves the body audit, exact costs, anomaly exclusion, count, Note, plan page, protected plan line, and final quiet while cutting repeated capability definitions. The clearest `diff -U0` example is:

> pre-repair: `Wind-adjacent. Left only; the fan. Half a body. The lock, two* ands* ...`
>
> current: `Wind: three an exchange at most, and the lock is two *ands* he'll count. The hip only when I know; when I don't, the feet, which have no doorway.`

The other entries now land once: “The knock: on the pulling in and nothing else”; three redirects with side/breastbone cost; and “The gaze: no ration tomorrow.” The movement still closes on fear accepted rather than on another explanation.

### Priority 3 — Sentence weight — RESOLVED

The `diff -U0` changes show selective hand-joining in the named explanatory passages, for example:

- “He did not know. He had thought for a year...” becomes “He did not know; he had thought for a year...”
- “It lasted perhaps half a beat. Then Brom let it go...” becomes one sentence with a clear temporal hinge.
- “There was no time ... There was no space...” becomes “There was no time, as Cael knew afterward, no space...”
- “The fear had not gone. It had only been written down...” becomes one semicolon-linked thought.

The repair also splits chapter 47 only where the thought turns, separating the remembered angle-denial lesson from the mechanics paragraph. Dialogue and landing beats remain short where they should.

Measured result: sentence mean rises from 13.19 to **13.57**, meeting the brief's “about 13.5 or higher” aim; the ≥40-word share rises only from 3.5% to **3.8%**, under the 4.5% ceiling; paragraph median remains **29**. Chapters 46 and 47 remain individually below 13 because of their dialogue-heavy drills, as the author disclosed, but the brief governs the completed movement measure.

### Length — RESOLVED

`wc`/gate words total **36,928**, inside the required 36,500–38,500 range. The formula tool's prose-token total is **36,841**; the difference is tool tokenization/headings, not missing prose.

## (2) Continuity

### Result

Manuscript continuity passes.

- **Movement 6 join:** chapter 43 ends with Lira provisional after Maud, hands bruised, lamp lit nightly, the up-river keeper asking for Cael's line, and Cael writing “I didn't send it. It went.” Chapter 44 opens nearly three weeks after the Maud bout with those bruises fading, Lira still training the middle, and Reydan following the story and the keeper's returned line. Cause and elapsed time join cleanly.
- **Calendar:** the independent table above reconciles every weekday, ordinal, session number, “tomorrow”, “Six days”, “Four days”, and the Tuesday bout. No month is named; cold and frost remain compatible with departure before hard winter.
- **Bodies:** Lira's left knuckle continues to “talk” and her lamp sacrifice is voluntary. Cael accumulates forearm bruising, left-knee stiffness, ribs, the Ansel hook, and the redirect groove. The twelve redirects are paid and rested; nothing heals opportunistically. Reydan remains unhurt before the bout.
- **Counts and capability limits:** three confirmed partial fragments remain Wind, Pressure, and Iron. The knock progresses by staged conditions to about four in five at close range, still gives when rather than where, and still fails at two paces. Wind remains left-only with a two-*and* lock and three-per-exchange ceiling. Redirects remain three clean uses, twelve practice repetitions total, with three held for the bout. The gaze has no ration on bout night but remains an attention cost, not a new power.
- **Session nine:** it occurs once, on the thirteenth simulated burst of the ninth session. Seven subsequent attempts fail. No cost is found. Brom explicitly limits his basis to one secondhand account and says he can be wrong. The Log calls his finding “Description, not diagnosis”, distinguishes it from the Brom-bout absence—“that was nobody; this was somebody”—and records three hypotheses ending in “Evidence insufficient” and “Filed as anomaly. Monitor.” Cael refuses to rely on it Tuesday.
- **Knowledge and consent:** Cael asks Brom, Ansel, and Lira before using the knock. Lira bounds permission to mornings in the alcove through the floor, with every answer called aloud. On Reydan he uses only the outward gaze on what a public resting body gives the room; the private read stays shut. Reydan reads only visible facts and refuses to guess what Cael is. The scout stays unidentified and does not approach.
- **Ratings and people:** Cael remains Iron-equivalent with no Path designation; Lira remains provisional; Reydan is twenty-two, Iron R8, burst Pressure; Ansel remains a former Bronze with no stated Path. No rating moves during training.
- **Reserved truths:** nobody proposes deliberate acquisition by watching or contact. Compression-adjacent does not exist yet. Nobody describes a “still place”, says what all Paths were, links the anomaly to primordial truth, or gives the Arbiter/registry a maker, will, or intention. `[UNBOUND]` remains Cael's secret and is not raised.
- **Later-book canon:** Book 3 chapter 1 finds four confirmed fragments only after the Movement 8 Compression acquisition and quotes the chapter-51 Note exactly: `Session nine. Could not reproduce. Still don't know what that was.` Book 7 chapters 14 and 24 can still introduce the “still place” after a real Tide acquisition because Movement 7 supplies only an unreproduced read and no location or diagnosis.
- **Crowd and room:** stone foundry floor, low ceiling, lamps, room for four hundred, and separate street overflow follow BOOK_MAP §11. Movement 8 can include the later-canon six hundred with the street.
- **Protected wording:** every applicable mapped line survives exactly: `Iron-equivalent. Cael. No Path designation.`; “I'd like it to stay that kind of fight.”; “Survive first. Think second.”; “It compresses inward before it fires outward.”; `Session nine. Could not reproduce. Still don't know what that was.`; “Three integrated fragments, one anomaly” with required sentence-initial capitalization; and `If I can force him to abandon three consecutive reads, his fourth response will be pattern-broken. That's when I move.`

The pending Movement 7 ledger block already carries the repaired calendar and state in its coordinator-rulings section. Its status remains “recheck pending”, which is correct until the coordinator applies the one line fix and closes it. No ledger contradiction requires manuscript work.

## (3) Formula

Required commands were rerun on the current chapters.

`python3 editions/monroe-1.3/tools/formula_metrics.py editions/monroe-1.3/book-02-iron-circuit/manuscript/chapter-{44..51}.md`

| Metric | Result | Assessment |
|---|---:|---|
| Chapters | 8 | full current movement |
| Total / prose words | 36,841 / 36,841 | formula tool count; in repair range |
| System-notice words | 0 | no fenced notice |
| Sentences | 2,715 | — |
| Sentence mean | **13.57** | brief's ≥13.5 aim met; exact target 14.6 |
| Sentence median | 9 | below exact target 11 |
| Population SD | 11.56 | below the source's approximate 26 |
| Sentences at five words or fewer | 30.6% | above exact 27.7%; spoken/landing beats preserved |
| Sentences at forty words or more | **3.8%** | near 3.3%; below brief ceiling 4.5% |
| Paragraph mean / median | 44.12 / **29** | above 26.8 / 18 ASR proxy; median not raised by repair |
| Marked scene breaks | 32; 8.69/10k | matches 8.7/10k target |
| Words per scene | **921.0** | inside brief's 850–1,050 range; near 950 |
| Flesch Reading Ease | 91.0 | easier than 72.3 target |
| Flesch–Kincaid grade | 3.94 | inside repair working band 3.5–6; below 6.8 target |

The exact-target drift in sentence spread, paragraph size, and reading ease remains disclosed. The repaired prose meets every movement-specific working range and is clear aloud. A second repair to chase the source's extreme sentence variance or ASR-derived paragraph proxy would be disproportionate after the high-leverage repair passed.

`bash editions/monroe-1.3/tools/ed.sh overlap book-02-iron-circuit 7`

> `0 unprotected shared runs of >= 8 words; 5 protected runs (allowed)`

`bash editions/monroe-1.3/tools/ed.sh gates book-02-iron-circuit 7`

| Chapter | Gate words | Reader Standard | Metadata | Modern |
|---|---:|---:|---:|---:|
| 44 | 4,519 | 0 | 0 | 0 |
| 45 | 4,395 | 0 | 0 | 0 |
| 46 | 4,786 | 0 | 0 | 0 |
| 47 | 4,044 | 0 | 0 | 0 |
| 48 | 3,687 | 0 | 0 | 0 |
| 49 | 4,559 | 0 | 0 | 0 |
| 50 | 5,072 | 0 | 0 | 0 |
| 51 | 5,866 | 0 | 0 | 0 |
| **Total** | **36,928** | **0** | **0** | **0** |

`bash editions/monroe-1.3/tools/sweep_probe.sh book-02-iron-circuit 7 7`

| Chapter | Probe sentences | Skeleton | Close |
|---|---:|---:|---:|
| 44 | 196 | 1% | 7% |
| 45 | 202 | 1% | 8% |
| 46 | 205 | 0% | 4% |
| 47 | 173 | 1% | 5% |
| 48 | 153 | 2% | 7% |
| 49 | 183 | 0% | 6% |
| 50 | 212 | 0% | 6% |
| 51 | 243 | 1% | 6% |
| **Total** | **1,567** | **1%** | **6%** |

No formula, sweep, gate, or overlap result calls for a second repair.

## (4) Reader clarity

Reader clarity passes.

- **Causal spine:** no file creates hesitation; Lira trains movement without warning; Brom isolates the inward gathering and the read's directional limit; the redirect supplies a costly fallback; Ansel makes waiting usable; the report supplies one narrow opening; session nine complicates rather than solves; the final inventory turns all of it into a bounded plan.
- **Speaker attribution:** the three-person supper, cookshop, report-table, training, and post-round scenes remain attributable by ear. Lira's sharp imperatives, Brom's measured literalism, Ansel's flat economy, Dace's ledger language, and Reydan's formal plainness are distinct. Action beats re-anchor speakers before any long exchange becomes ambiguous.
- **Referents:** *gaze* means outward observation; *knock* means the close-range Iron read; *inward* means gathering; *drop and roll* means rightward footwork; *redirect* means the passed receiving face; *lock* means the two-*and* stillness after Wind. Each term is demonstrated before it bears tactical weight. “When, not where” is repeated only where it governs the final plan.
- **Orientation:** the repair's appositives are enough. Feryn, Darrow, Keth, Maud, Bede, and the dock partner are placed by role or remembered event; Talis no longer burdens the early list. Reydan and Ansel receive full local introductions.
- **Fluent thirteen-year-old lens:** the system load is real but readable in one pass because mechanics are expressed through doors, springs, carts, stairs, water, feet, and prices. Ratios are followed by action rather than abstract arithmetic. The emotional stakes—Lira giving up her lamp, Ansel reclaiming a floor, Brom teaching honestly, Cael asking leave—remain simpler than the terminology and keep the movement attached to people.
- **Adult genre-reader lens:** the opposing methods are fresh and intelligible. Reydan's managed stillness, Ansel's voluntary round, and the anomaly each escalate a different kind of uncertainty. The movement pays off training without spending the main fight early.
- **Reader Standard:** pass. Automated totals are zero, and the full read finds no profanity, sexual material, crude humor, gore, cruelty-as-reward, or glamorized harm. Violence remains bounded by consent, restraint, costs, witness, and care.
- **Pull:** Reydan's coppers and foot-reading catch interest immediately; Ansel's round is the emotional/action center; session nine restores mystery; the Monday-night mutual study points directly to the Tuesday bout. I would continue.

No unclear speaker, unstable pronoun, unexplained tactical jump, or thirteen-year-old comprehension failure warrants prose repair.

## (5) Listening proof

Every chapter and every changed region was checked for balanced quotation and emphasis marks, `---` spacing, narrator-risk numerals and abbreviations, homographs and ear collisions, speaker attribution, and broken joins.

| Chapter | `"` marks | `*` marks | Listening result |
|---|---:|---:|---|
| 44 | 82 | 22 | pass; Reydan/Cael cut and four scene joins are clean |
| 45 | 180 | 38 | pass after fix 1; all speech and emphasis balance, but one separator lacks its preceding blank line |
| 46 | 230 | 20 | pass; Lira/Brom/Ansel transitions and three-person cookshop attribution are clear |
| 47 | 204 | 36 | pass; drill stages, counts, and the bruise-paragraph split read cleanly |
| 48 | 142 | 24 | pass; report quotation nesting and table speakers remain clear |
| 49 | 182 | 26 | pass; Ansel's three exchanges, public account, and later drills have clean joins |
| 50 | 174 | 60 | pass; anomaly action, explanation limits, and Log hypotheses are distinct by ear |
| 51 | 116 | 62 | pass; repaired Dace quote and `two *ands*` are clean; Cael/Reydan cutaways are separated |

All whole-chapter totals are even, and the per-paragraph scan finds no unmatched quotation or emphasis mark. There are no code fences. Seven chapters have standard blank lines on both sides of every scene separator. Chapter 45 has one valid but nonstandard join: the separator immediately follows the paragraph ending “with her thumb.” Fix 1 adds the missing blank line; its multiline old string and its unique paragraph anchor each match exactly once.

The numeral/abbreviation scan finds only chapter numbers; `Rank 1`; the intentional chalk/Log initial `L`; and the chapter-51 tally lists. All are speakable in context. There are no unsafe Roman numerals or unexplained abbreviations. `EAT, L SAYS` is meant to sound as the letter name “ell”, not as a word.

Potential homographs—`read`, `lead`, `close`, `live`, `record`, `row`, `Force`/`force`, `Pressure`/`pressure`, and `Wind`/`wind`—are disambiguated by syntax and immediate context. Bede/Brom never occur in a confusing spoken list; Reydan, Ansel, Dace, Vell, Lira, and Cael remain distinct at speed. No duplicated join, false attachment, or broken sentence remains.

## Exact line fixes

1. `manuscript/chapter-45.md`
   old: `Lira picked up the charcoal and rubbed out the question marks beside every *B*, one by one, with her thumb.\n---`
   new: `Lira picked up the charcoal and rubbed out the question marks beside every *B*, one by one, with her thumb.\n\n---`
