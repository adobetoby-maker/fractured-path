# CLOSE WITH LINE FIXES — three local replacements

Scope: one paragraph in chapter 25 must identify Teague's fence as the planned axe-head hold job, and two sentences in chapter 30 must restore the quarter-hour overrun inherited by Movement 5. No scene rewrite or second repair is needed. No protected unit is altered.

## (1) Brief items

Baseline: `state/movement-004/pre-repair-r1/`. I read the full current movement before rechecking the repair. The evidence below is from `diff -U0` against that frozen baseline.

### Coordinator-applied protected units and joins — PARTIAL

The three protected units are now prose, verbatim, and each occurs exactly once:

- Pike: `"Teague's nine up," Pike said, to the book, asked by nobody. Then, still to the book, at the same size, as if it were the next line and not a different thing: "He read that slip yesterday. Read it twice, same as the boy did. Put it back under the stone and took the fence. I'd have done the same, and I told him, and he said he knew."`
- Brom: `"A survey kit's a cart's worth. Brass. A level, a chain, the rule. Nobody puts a cart's worth down and walks off from it unless they walked off fast." He looked at the jug. "That's not the reason. That's what it is."`
- Lira: `"It doesn't come on like a lamp. It's just there, and it's where it was, like a clock that stopped and started again without losing the time."`

The adjacent joins do not repeat their content. For Pike, the diff changes the follow-through from `Now he knew what that same man had done at the plank` to `Now he had the man's answer to a hundred marks as well, at second hand`, and from `Pike had not told him what the reason was` to `Pike had said what was done, and had not said why.` Brom's jug is already on the table, and nothing nearby repeats “walked off fast.” Lira's preceding answer is now only `"Back."`, leaving the clock unit to do its own work.

This item is PARTIAL only because the new fence staging after Pike's line identifies the wrong job; see §2 and line fix 1. The protected unit itself passes and must not be changed.

### A. Seln's locked case — RESOLVED

The diff adds the required object chain:

- Chapter 23: `Seln waded a little upstream of him. He had taken up the strap of the locked case by two holes before he stepped in, so that it rode high between his shoulder-blades, well clear of the river...`
- Chapter 27: `The only other thing that left the loft that morning was on a strap across Seln's chest, shut, as it had left every loft before.`
- Chapter 30: `Seln had the locked case as well, shut, on its strap across his chest.`

It stays shut, on him, and crosses the line. It is neither opened nor transferred.

### B. Four tracked passages — RESOLVED

1. **Chapter 29, Lira's burst becomes a step — RESOLVED.** The source has Cael watch the preparation, ordered body mechanics, commitment, release, and ordinary step. The repair instead keeps his eyes east: `So it was his own feet that told him.` He turns after the landing; Lira supplies the attempt in speech, and Brom supplies the external witness. The same-content/same-order chain is broken.
2. **Chapter 30, the floor's edge — RESOLVED.** The source and baseline begin with the edge, follow the rim, compare it to a vessel, then name the lip. The repair begins with Lira seeing the bands: `"There's writing on that," she said.` Temperature, silence and diameter follow; only later does the cord find the rolled edge: `"She won't lie down," said Brom`. No dish/basin comparison remains.
3. **Chapter 30, masonry samples — RESOLVED.** The source and baseline open the box, compare each sample serially, put each away, then conclude none matches. The repair enters after nine rejected samples, sorts the rest into three visible families, and tries one of each together: `She chose the freshest-broken from each heap and held the three against the grey together`. The chain is broken.
4. **Chapter 30, den approach — RESOLVED.** The source and baseline have Seln circle, stop silently, Cael notice, and the group converge. The repair has Brom expose the missing ground while packing, Cael meet the fresh print first, and only then see Seln; Seln speaks and calls the others: `"Bring the others round by the turf, and bring them quietly."` The chain is broken.

I opened the four source passages named in `source-tracking.md` and applied its same-content/same-order standard. The re-entered floor scene does not create a new tracked sequence, and no other repair passage does. The overlap check independently reports zero unprotected shared runs of eight or more words.

### C. Chapter 28 survey proved once — RESOLVED

The repair removes the second full tenth-station demonstration. Baseline:

> `"It has been six and a half ten times," said Karis... I shall go on measuring, since a wrist is not an instrument. But I know already what he is going to write.`

Current:

> `He laid the short cord down all the same, since a wrist is not an instrument, and wrote what the knot said. He had written that figure nine times already.`

It also cuts the repeated south-side offset explanation and reduces the closing proof to one governing inference. The first procedure, stake 31, constant offset, protected circumference, ten cords to the middle, and Seln's stake conclusion all remain.

### D. Two anchors — RESOLVED

- Chapter 23 now opens the injury inventory with one emotional fact rather than a recap: `Six days ago the side of a mountain had come down on five people and a cart... he had not yet got used to counting them and finding five.`
- Chapter 29 makes the disclosure cost concrete and names Seln: `One had come out of the mild man who stood six feet off...` and `A healer spoke to every carter on seven roads. She would not have meant the least harm by it.` This spends the already-established source-protection and healer-network facts, not any reserved Movement 5 or 6 disclosure. It does not explain the anomaly.

### E. Bounded cadence pass — RESOLVED

The diff shows real-turn paragraph breaks in chapters 24, 25, 28, 29 and 30, plus limited causal rejoins. Dialogue and landing beats remain intact. The movement holds all three repair bounds: mean 13.93 (13.3–14.2), sentences of at least forty words 4.2% (at most 4.5%), and 942.7 words per scene (850–1,050). The broader formula drift remains visible in §3 but does not require another repair.

## (2) Continuity

### Calendar, state, counts and geometry

Days 84–96, road order, bodies, money, board rank, the Fallow hundred, three boxes, the mule, papers and equipment all reconcile with the Movement 3 entry state and the Movement 4 coordinator rulings. The repaired case chain closes the only carried-object omission. The settled Ring geometry is undisturbed: the western line stone is 220 yards from the floor's middle; the floor is twenty-six of Cael's yard-strides across; the den is under the eastern lip. No cord or stride length is stated. Stake 31, sixty-two cords and twenty strides, eleven uprights and eleven finished Ring sheets all remain.

### “Took the fence” — AMEND

The repair's upper-inn paddock is not the fence Teague took. It gives the job as `the upper inn's paddock`, `three days`, and `five marks`. The plan and later canon identify one continuous job instead:

- the axe-head hold's **longer fence** on the east road;
- **forty marks**, `HOLD`;
- Teague takes it on day 89 and his crew works it;
- it remains unfinished when the Stair takes them south;
- Pike later gives that same cold-term fence to the five: `"Fence. Forty. Teague says it's yours if you want it; he's got the winter road"` / `"Ours."`

The plan does not assign the fence a three-day duration. Its duration is deliberately open-ended: Teague begins it, the Stair interrupts it, and the five inherit the unfinished cold-term work. Line fix 1 restores the identity, price and `HOLD` status and removes the false three-day term without touching Pike's protected line.

### Cut bands and Ring sheets — KEEP

Keep the repaired fact: each of the eleven uprights has a band around its foot, a hand above the floor, and no lip band is described. The source requires bands around each upright but fixes neither chest height nor a lip band. The baseline's chest-height version is physically impossible on the knee-high upright. The current version still produces one numbered rubbing per upright, so `Ring 11` remains sound; Movement 7's twenty-nine Stair sheets and Movement 8's twelve Hall sheets then give the binding total of 52.

Two downstream summaries are stale, not the manuscript: Movement 5/STATE_LEDGER says `the eleven uprights and lip carry unknown bands`, and Movement 6 calls the Ring sheets `cut to the uprights' heights`. At close, the first should lose `and lip`; the second should be understood or refreshed as eleven numbered upright rubbings with each upright's height recorded. Neither requires a manuscript line fix.

### Cael's overrun — AMEND

The repair changes the overrun from one quarter-hour to three quarters through `her quarter of an hour had run to three` and `let the quarter run to three`. That conflicts with the binding Movement 4 ruling, STATE_LEDGER open thread (`A captain's quarter of an hour`), next-movement inheritance (`he spent a quarter-hour past his declared two-hands limit`), and Movement 5's opening pressure. The author report's sun rationale does not authorize a changed fact and does not supersede those bindings. Line fixes 2–3 restore one quarter-hour while retaining all eleven completed sheets.

### #49 default and reserved truths — PASS

- Outside protected log entries, nothing calls the exception `his Path`, says Cael's Arbiter is awake or unaffected, or explains why the fragments answer. The two occurrences of `his Path` are Brom's Path in Oryn and Karis's exchange.
- `Quieting` does not occur. `Compact` is not spoken. `made` is said of the place once, by Karis: `"A circle is a made shape."`
- No stillhound is seen; the movement shows prints, hair, scat, bones and an empty den. Oryn reads nobody inside.
- Cael's own Arbiter remains dark. His Iron and Wind tests are private, unwitnessed, unlogged and not deployments; deployment since the Line remains one. Shadow stays untouched.
- The chapter 29 Seln anchor uses no Movement 5 map-memory, visible hounds, combat, or Movement 6 mechanism/telling material.

### Protected text and later canon — PASS after the three fixes

Pike, Brom and Lira's restored units are verbatim, each once, and unrepeated nearby. Seln's case is shut on his strap throughout and over the line. The two HOLD slips remain unresolved. Movement 5 receives six at the eastern den, no visible hound, the exact Ring geometry, eleven sheets, the correct quarter-hour command error, and the existing capability/knowledge limits. Movements 6–8 retain Ring 11, fifty-two total sheets, the axe-head fence at forty, and the cold-term handoff. Owner decisions #18, #23, #24, #42, #46, #48, #49 and #50 are not spent early or contradicted.

## (3) Formula

Commands reproduced:

```text
python3 editions/monroe-1.3/tools/formula_metrics.py editions/monroe-1.3/book-07-void-roads/manuscript/chapter-{23..30}.md
bash editions/monroe-1.3/tools/ed.sh overlap book-07-void-roads 4
bash editions/monroe-1.3/tools/ed.sh gates book-07-void-roads 4
bash editions/monroe-1.3/tools/sweep_probe.sh book-07-void-roads 4 4
```

Formula output:

| Measure | Current |
|---|---:|
| Chapters | 8 |
| Prose words | 37,708 |
| Sentences | 2,706 |
| Mean / median | 13.93 / 10 |
| Population SD | 11.54 |
| Sentences ≤5 words | 25.6% |
| Sentences ≥40 words | 4.2% |
| Paragraph mean / median | 36.61 / 26 |
| Marked breaks | 32 |
| Breaks per 10k | 8.49 |
| Words per scene | 942.7 |
| Flesch / FK grade | 93.5 / 3.67 |

The repair's binding hold passes. Against the larger O'Connor targets, median remains one word short, sentence spread is narrow, short sentences are slightly low, paragraph mean is long, and readability is much easier than the numerical target. Those are movement-level tendencies already present after the bounded pass, not a reason to disturb a clear 37.7k-word movement with another repair.

Overlap: `0 unprotected shared runs of >= 8 words; 36 protected runs (allowed)`.

Gates: all eight chapters report `reader_standard=0 metadata=0 modern=0`.

Sweep:

| Chapter | Sentences | Skeleton | Close |
|---|---:|---:|---:|
| 23 | 214 | 1% | 16% |
| 24 | 195 | 5% | 25% |
| 25 | 220 | 9% | 30% |
| 26 | 196 | 7% | 20% |
| 27 | 197 | 5% | 23% |
| 28 | 192 | 2% | 19% |
| 29 | 210 | 1% | 20% |
| 30 | 221 | 4% | 20% |
| **Total** | **1,645** | **4%** | **22%** |

## (4) Reader clarity

Speaker attribution and referents pass. Pike's unasked statement now has a visible ledger target and a clean response; Brom's council contribution has the jug in place; Lira's protected line follows a clearly staged result. The line trials preserve a stable order, observers and recorded rows. The re-entered floor scene now moves by visible cause: writing draws the group in, the floor is tested, the cord discovers the lip, the samples narrow the material, the rubbings consume the remaining light, and packing exposes the den.

For a fluent thirteen-year-old, the movement remains followable despite procedural density. Contracts, price, `HOLD`, board rank and measurement are repeatedly attached to concrete objects and decisions. Violence remains prospective at the handoff; injuries have cost without gore; no prohibited language, innuendo or moral ambiguity is introduced. Cael's concealment is presented as a debt and self-deception, not endorsed cleverness. After the three line fixes, the fence history and the size of his command error will also agree with what later chapters ask the reader to remember.

## (5) Listening proof

All eight chapters were checked in full, including every changed region. Quotes and italics are balanced in every chapter. All `---` separators have blank-line spacing on both sides. No broken paragraph join remains.

| Chapter | Changed-region and chapter listening result |
|---|---|
| 23 | The new mountain anchor lands before the inventory; the case sentence has an unambiguous subject and strap position. No quote, italic, separator, numeral, abbreviation, homograph or ear-collision fault. |
| 24 | Cadence-only paragraph breaks preserve their joins and antecedents. `HOLD` is the spoken word “hold,” not initials. No listening fault. |
| 25 | Pike's protected unit, Teague window, Brom unit and witness split read continuously. The current paddock sentence is grammatical but canonically wrong; line fix 1 keeps the same audible join. `read` and `bow` are disambiguated by syntax. No protected wording is touched. |
| 26 | No repaired join is broken. The map inscription `water at 36` is naturally “water at thirty-six”; there are no other prose numerals or abbreviations likely to be misvoiced. `read`, `wind` and `does` are context-clear. |
| 27 | The added case sentence attaches cleanly to the loft departure. Capitalized Wind and ordinary wind remain distinct in context; `read` is unambiguous. No listening fault. |
| 28 | The survey trims remove repetition without dropping a speaker or referent. `K. L. B. S. O.` is an intentional written initial list and reads letter by letter; `95th` occurs inside Karis's field note and is unambiguous. The protected circumference lands intact. |
| 29 | The restaged step is audible in cause-and-effect order: Cael's feet, grass, turn, Lira's account, Brom's witness, clock line. The Seln/healer anchor keeps every pronoun anchored. `wound` is plainly the past tense of “wind” in `Lira wound the shirt on again`; Wind is otherwise capitalized. No fault. |
| 30 | The floor, sample and den re-entry has clean joins and speaker control. `row`, `read`, `close`, `bow`, `wind` and `live` are resolved by immediate syntax. The current phrase `her quarter of an hour had run to three` is an audible ambiguity (“three” what?) as well as a canon error; line fixes 2–3 remove it. No other listening fault. |

## Exact line fixes

Each `old` string below was checked with `grep -Fxc` against its named manuscript file and returned exactly `1`.

1. `manuscript/chapter-25.md`
   old: `It was all either of them said about it. There was a fence on the oak, four slips along: the upper inn's paddock, in sight of the ferry, three days of posts and rails at five marks, and work that a person with a bad hip could do sitting. Teague drew its tack and held it out, and Pike wrote his name to it before he shut the book and tucked it under what was left of his arm.`
   new: `It was all either of them said about it. There was a fence on the oak, four slips along: the axe-head hold's longer fence on the east road, forty marks, HOLD. Teague drew its tack and held it out, and Pike wrote his name to it before he shut the book and tucked it under what was left of his arm.`

2. `manuscript/chapter-30.md`
   old: `Karis finished the eleventh sheet with the sun a hand lower than he had measured it. The tenth had torn under her pencil, and she had done it over from the first stroke; her quarter of an hour had run to three.`
   new: `Karis finished the eleventh sheet at the quarter-hour.`

3. `manuscript/chapter-30.md`
   old: `It was on the ridge. He had measured two hands under it, and given away a quarter of an hour, and let the quarter run to three; and the lower rim of it was touching the hills now, red and flattened, and going. The shadows of the eleven stones had run out across the floor and joined. Between them, where the last light struck it level, the grey had begun to shine.`
   new: `It was on the ridge. He had measured two hands under it and spent the quarter of an hour he had given away; now the lower rim of it was touching the hills, red and flattened, and going. The shadows of the eleven stones had run out across the floor and joined. Between them, where the last light struck it level, the grey had begun to shine.`
