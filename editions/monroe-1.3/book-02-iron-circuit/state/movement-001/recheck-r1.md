CLOSE — scope: Book 2, Movement 1 repair r1, chapters 1–8. Every repair-brief item is resolved; all specified gates pass; no manuscript line fix or second repair is warranted.

# Targeted recheck — repair r1

Review seat: Sol, via Codex. Author: Claude Opus 5.5. This is a targeted recheck of the same-author repair, not a fresh movement review. I read the full current movement, compared every chapter to `pre-repair/` with `diff -U0`, checked the cited Book 1 facts and Book 2 canon, and inspected every changed region and its joins.

## (a) Repair-brief findings

### 1. Copper-formal count — RESOLVED

The binding entry state is eleven before Ulric; the text now consistently makes Ulric number twelve:

- Ch1: “That's twelve Copper formals this year, by my count, and I'm the one who counts.”
- Ch6 Log: “Evidence: the straw every morning; twelve Copper formals, Ulric the last.”
- Ch7: “every one in twelve Copper bouts”.

No changed passage retains the old eleven-after-Ulric count.

### 2. Ten trials / nine bursts — RESOLVED

Trial nine visibly fails to activate. Ch5 says: “he dropped his left hip, and held his breath, and nothing happened”; “The floor stayed the floor. There was no loosening and no going short”; and he falls “in an ordinary mortal stumble, with no lock to hold him up”. Lira pulls the strike, so this is unmistakably a failed activation rather than a short or malformed burst.

The accounting then remains true:

- Ch5 immediately distinguishes “nine tries” from “Eight that came, and one that didn't”, then gives trial ten one successful burst. Its final total is “nine bursts and six hits and a lip.”
- Ch6 records “Ten trials, nine bursts in one hour” and “Depletion: after nine in an hour”.
- Ch7's later count is a different experiment and is internally explicit: “five tries to the right, five tolls paid for nothing. Then, with her, nine more.” These are failed right-hip summons, not additions to the landing-trial burst total.
- Ch8 repeats those right-hip conditions consistently and describes the landing sequence as “the ten trials … and the ninth, when Lira would not hit a falling man.”

This matches BOOK_MAP §6.1: ten trials, nine bursts, six hits and an exchange.

### 3. Ch8 REVISIONS block — RESOLVED

Ch7, ch8, and BOOK_MAP §8.12 now contain the same three lines, character for character:

```
FRAGMENT UPDATE
[Wind-adjacent] — Duration revised: sustained.
Integration: partial.
```

Ch8 correctly moves interpretation outside the protected block: “Integration is the same as it was; only the one field moved.”

### 4. Ch6 Power Log compression — RESOLVED

The recap is materially shorter without losing the brief's keep list:

- Six-field architecture: ch6 names, in order, “What it is”, “Source”, “Conditions”, “Deployment range”, “Costs”, and “Open questions”; Wind displays all six, and Pressure says it was written “in the same six fields” before quoting only “The heart of it”.
- Left-only clue: “half my body's width, to the left, the front-left or the back-left”, followed by Cael stopping over “to the left”.
- Ceiling and depletion: “Ceiling: three in an exchange, probable” and “Depletion: after nine in an hour”.
- Pressure's two faces: the prose and `WHAT IT IS` preserve taking (“spreads a strike into the floor”) and giving (“ridden out along my own strike on the other fighter's beat”).
- Concurrent-function question: “Darrow's fourth: both at once, unasked, the only time” and “Can it be called? Ruling: not yet.”
- Tool / self-record distinction: “The grey book was a tool. The slim one had to be held to Vell's standard instead”.

The compressed Pressure quotation omits two displayed field headings, but this is not a loss of architecture: the prose expressly states that the complete entry uses the same six fields and labels the quotation as only its heart.

### 5. Sweep stake and registry restatement — RESOLVED

Ch3 now gives immediate, present-tense consequence at the lodgers' book: “If the pencil stopped at his line” the landlord would face questions; a district-office talk would make Cael “miss the card”; and “a fighter who missed a card without a reason found his name rubbed off Dace's wall.” The closing sentence makes the present stake concrete: “all of it hung, this minute, on the speed of one man's pencil.” The fixed route, the district making itself small, and the logic of being predictably visible remain intact.

Ch4 supplies exactly the missing reader context: “The registry's word for him was *Shattered*. It had been written against four people before him. Three of them had been dead within weeks of their Kindling, and the fourth was a line that said nobody knew.” Book 1 ch4 records four prior instances, three dead within weeks of classification and one unknown; Book 1 ch6 carries “four entries, three of which had ended in a few weeks and one in a line that said nobody knew.” Because the classification is returned at Kindling, the restatement is consistent. It does not add cause, mechanism, Hesk's file knowledge, or any Book 2 reserved truth.

### 6. Watcher plant and payoff — RESOLVED

Ch1 plants the anonymous observer precisely: “third bench back from the east wall”, “a river-academy coat”, “both hands flat on his knees”, neither cheering nor groaning, and eyes “on the stone where Cael had landed”. Ch8 pays off every identifying detail after Dace reports the watcher; Cael recalls the same bench, coat, hands, and landing gaze, ending “He had seen it and filed it nowhere.” The plant remains unnamed and adds no scene.

### 7. Rhythm repair — RESOLVED

The frozen baseline measures 2,612 sentences and 6.7% at 40+ words; r1 measures 2,687 sentences and 3.0%, a net increase of 75 detected sentences after the author's splits and selective rejoins. The final diff contains 131 change hunks across the eight chapters. No spoken line has been split to manufacture short sentences. Changed dialogue is limited to factual count/wording repairs and remains in a single speech unit.

The retained or rejoined long sentences named in the author report read as deliberate syntactic units: the ch1 burst and lock, Hesk's pouch, ch5 trial-ten recovery, the ch7 barge and update conditions, and the ch8 carrier's bag all maintain one subject/action hierarchy rather than splicing unrelated thoughts. The final snapshot cannot independently reconstruct the author's intermediate operation totals of “about 108” splits and “about twenty” rejoins, but the resulting prose satisfies the brief and the measurable target.

### 8. Length — RESOLVED

The gates total is 35,952 words, inside the required 35,500–38,000 range.

## (b) Required command results

### `ed.sh overlap book-02-iron-circuit 1`

`0 unprotected shared runs of >= 8 words; 5 protected runs (allowed)`

### `ed.sh gates book-02-iron-circuit 1`

| Chapter | Words | Reader Standard | Metadata | Modern |
|---|---:|---:|---:|---:|
| 01 | 5,622 | 0 | 0 | 0 |
| 02 | 4,599 | 0 | 0 | 0 |
| 03 | 4,161 | 0 | 0 | 0 |
| 04 | 3,991 | 0 | 0 | 0 |
| 05 | 4,978 | 0 | 0 | 0 |
| 06 | 3,606 | 0 | 0 | 0 |
| 07 | 4,550 | 0 | 0 | 0 |
| 08 | 4,445 | 0 | 0 | 0 |
| **Total** | **35,952** | **0** | **0** | **0** |

### `sweep_probe.sh book-02-iron-circuit 1 1`

| Chapter | Sentences | Skeleton | Close |
|---|---:|---:|---:|
| 01 | 229 | 0% | 10% |
| 02 | 216 | 0% | 6% |
| 03 | 179 | 0% | 6% |
| 04 | 176 | 0% | 2% |
| 05 | 216 | 0% | 5% |
| 06 | 157 | 0% | 7% |
| 07 | 183 | 0% | 7% |
| 08 | 185 | 1% | 10% |
| **Total** | **1,541** | **0%** | **7%** |

### `formula_metrics.py` on chapters 1–8

| Metric | Result |
|---|---:|
| Chapters | 8 |
| Total words | 35,869 |
| Prose words | 35,853 |
| System-notice words | 16 |
| Sentences | 2,687 |
| Sentence mean | **13.34** |
| Sentence median | 9 |
| Population SD | 11.1 |
| Share ≤5 words | 30.9% |
| Share ≥40 words | **3.0%** |
| Paragraphs | 813 |
| Paragraph mean | 44.1 |
| Paragraph median | 30 |
| Marked scene breaks | 32 |
| Scene breaks / 10k | 8.92 |
| Words / scene | **896.7** |
| Flesch Reading Ease | 91.2 |
| Flesch–Kincaid grade | 3.86 |

The requested author figures are confirmed: mean **13.34**, ≥40-word share **3.0%**, and **896.7 words/scene**, which rounds to **897**.

One report-only discrepancy: rerunning the same tool on the frozen `pre-repair/` files gives 36,249 total words and 906.2 words/scene, matching the original editorial review, not the AUTHOR-REPORT baseline row of 36,236 and 905.9. This does not affect the verified r1 figures or the manuscript verdict.

## (c) Changed-region and boundary checks

- **Joins, fragments, referents:** PASS. Every `diff -U0` hunk was checked in context. The splits land at complete thought turns; no new syntactic fragment, dangling modifier, ambiguous pronoun, or stranded attribution was found. The retained/rejoined long sentences remain readable as joins.
- **Callbacks:** PASS. No repair orphaned an earlier plant. The watcher, lock-as-price, Hesk fixed-joint letter, left-only clue, old-Log Darrow exception, Lira's farmer, and REVISIONS heading all receive their intended later reference.
- **Calendar:** PASS. No month is named. Relative markers (“three days”, “next week”, “midwinter”) remain compatible with the unnamed-month rule and the ledger chronology.
- **Knowledge boundaries:** PASS. Brom is absent. The Compact officers observe the market, boards, Ironyard entrance, and lodgers' book but never contact Cael. Vell, Dace, the academy watcher, and the distant keeper learn no fragment secret. Hesk learns only what Cael chooses to put in his letter. Lira's unshown work remains hers.
- **Reserved disclosures:** PASS. “Borrow”, “fingerprints”, and copies carrying habits stay within BOOK_MAP §7's Book 2 allowance. Nobody states a general witnessed-ability rule, attempts deliberate acquisition, links the watcher to the Compact/file, identifies `[UNBOUND]`, explains *sustained*, or discloses any later-book truth.
- **Protected wording:** PASS. The exact applicable BOOK_MAP §8 lines survive: the Registry/ledger declaration in ch2; “The keepers talk” and “The oldest ones use different words for things” in ch4; and the three-line `FRAGMENT UPDATE` in both ch7 and ch8. The two coordinator-approved one-word packet variants remain as accepted.
- **Reader Standard:** PASS. All eight automated Reader Standard totals are zero. On reading, the repaired passages remain clear on one pass, non-gory, free of sexual content, and grounded in consequence, restraint, loyalty, and honest recordkeeping. The ch6 compression improves momentum without turning the Log into summary shorthand.
- **Scene architecture and source distance:** PASS. All 32 marked scene breaks remain; sweep skeleton stays 0% total; source overlap remains 0 unprotected runs.

Two stale lines remain in the lower, explicitly superseded “Author's end-state” portion of `STATE_LEDGER.md`: line 147 still says “eleven Copper formals this year”, and line 175 says “No watcher.” The coordinator-rulings block above them already supplies the binding corrections (twelve after Ulric and the watcher-Blade plant/payoff), so these are ledger-cleanup items, not manuscript defects and not grounds for another author repair.

## Exact line fixes

None.
