# CLOSE WITH LINE FIXES

Scope: apply the one exact line fix at the end of this report, then close Movement 8. The author repair resolves every item in `REPAIR-BRIEF.md`; protected text, source distance, naming, reader clarity, overlap, gates, and sweep checks pass. The remaining fix restores Ephram's one-month shoulder prognosis outside protected text so the page supports the binding Movement 9 body inheritance. No second author repair is warranted.

## 1. Brief items

Baseline method: `diff -U0` from `pre-repair/` to the current manuscript establishes the complete repair; `diff -U0` from `pre-repair-author/` to the current manuscript isolates the author's r1 from the coordinator's nine exact fixes.

### 1. Seams around the coordinator-restored text — RESOLVED

The ruling reaction now answers one paragraph rather than five heads. The diff changes `it paused at the end of each head` to `it paused at the end of each sentence`, and replaces the old reaction with: “It was all one paragraph” and “Karis's fifty-one minutes had been answered in a single sentence.” Ch52 now says “the fourteenth chapter when the frame returns nothing” and “at the district station.” Ch53 says “the station's frame-house” and gives Rooke's clerk “the house's book.”

The ch54 joins no longer assume two books, loser-chalking, a blank rule, or chalk in Ephram's hand. The author-only diff adds: “after a bout on the oak the clerk chalked the result, and the two who had fought stood at the board while he did”; gives each fighter one side of the ladder; joins the handshake cleanly; and keeps the unpriced shoulder as Cael's own next Log paragraph: “*Not priced: his shoulder… Entered.*”

The four protected units are intact after r1:

- Ch51 ruling paragraph: verbatim source wording except the expressly authorized `term's end` → `the close of the present academic year`.
- Ch54 Ephram speech: all spoken words are verbatim; only source stage business is adapted to the bound shoulder.
- Ch54 ninth-fragment Log entry: verbatim in both paragraphs.
- Ch54 boards-ritual line: “Ephram looked at the board rather than at Cael, which was the register the ritual ran in.”

The author-only diff does not alter any of those restored words.

### 2. “Evaluator of record” naming — RESOLVED

The diff replaces “that office had been the protocol's evaluator of record” with “the certifying office had put its name to that protocol” and replaces “the house's own evaluator of record” with the unqualified “the evaluator of record” for Gault. Ch50 likewise changes “that office's name” to “the certifying office's name.” The protected certification line remains exact. The resulting usage is clear: the Archmarshal's office is the certifying office; Gault is the unqualified evaluator of record.

### 3. The two tracked source passages — RESOLVED

- Ch49:83 now opens, “The other seven name a person, and I have read each of them through.” It recasts the source proposition as complaints about acts, changes the ordering and syntax, and removes the distinctive `never once / been turned / on a person / for what he is` chain.
- Ch54:154 no longer reads the final field twice, surveys earlier notices, or follows the source's machine-grammar interpretation. It begins with the unnamed field, lets the arm account for the middle fields, and leaves “the last two words” for the Log.

The full author-only r1 diff against `pre-repair-author/` creates no new tracked passage. The exact overlap run also finds 0 unprotected runs of eight or more words. Protected source restorations remain excluded by design.

### 4. One recap in Karis's closing — RESOLVED

The diff removes “because everybody here knows what it will return. It will return nothing,” changes the remedy opening to the tighter “Stand a man on that scale, write down that it returned nothing,” and removes “No drafter writes a remedy for *where the registry has made sure of failing*. And that is what is asked.” The legal spine, wool-scale analogy, Jent's agreement, and four-second omission remain.

### 5. Explanatory echoes — RESOLVED

Ch50 removes the after-image beginning “*It isn't broken*” and compresses the later reflection to two sentences. Ch51 removes Havel's “That was the public record,” “That was what a public record was for,” the repeated statement that he still did not understand, and “yet it was.” Seln's section merges Cael's repeated looking and removes the explanatory inventory of what stood where an arm should be, while retaining “This is the hand. It does not have another.”

### 6. Havel's opening orientation — RESOLVED

The first sentence now reads: “Havel, in the junior chair at the records table, had written the time…” This establishes viewpoint and office in one phrase without recapping his history.

## 2. Continuity

### Calendar and proceeding

Pass. The page supports day 201 for Brom's second-bell panel and the hour-after-noon ruling; the council begins after the tenth bell and crosses midnight before the five hands rise; the bout is day 202 at the fourth bell; four withdrawal forms wait for day 203; the academic year and revocation close on day 207. The four call days, Ilsev's six-minute return rather than a sitting, and Bracken's fourteen all reconcile.

### Protected text and removed-version leftovers

Pass. The ruling, “Still glad” speech, ninth Log entry, boards-ritual line, certification line, boxes exchange, Withrow line, Seln line, and Blade notice are exact at their governed altitude. Searches across ch51–54 find no surviving assumption of five numbered ruling heads, “the second head,” loser-chalking, a blank rule over Ephram's name, two record books, or five drill days for Lira. Ch51's “five ruled heads” belongs to Havel's transfer form and is unrelated.

### Ch52 cross-book joins

Pass. “District station” and “the station's frame-house” agree with the ruling and the Ostrand station vocabulary. Ephram's repaired lead-in—“I told you at the trial that whatever you are, I was glad it was on my side of the floor”—correctly points to Book 5 ch46:331: “Whatever you are, I'm glad it's on my side of the floor.” The later protected speech repeats that antecedent accurately.

### M9 inheritance

Dates, Cael's bills, fragment inventory and deployments, knowledge boundaries, the unopened Velmere envelope, unsigned finding and guidance slip, four forms, Karis's three boxes, Seln's case, and Brom's two personal boxes all still match the page after r1. Havel's transfer request is signed, dated, and set out for immediate submission; no knowledge boundary changes.

One body detail is not presently on the page: the binding inheritance says Ephram's set right shoulder “expected to want a month,” but restoring the protected speech removed the first draft's only month prognosis. The page still shows the displacement, setting, sling, and his decision to stay. The exact fix below restores only the missing prognosis, outside protected text.

## 3. Formula

Reproduced on all seven current chapters with:

`python3 editions/monroe-1.3/tools/formula_metrics.py editions/monroe-1.3/book-06-the-compacts-hand/manuscript/chapter-{48..54}.md`

| Metric | Observed | Target / assessment |
|---|---:|---|
| Total words | 40,779 | Under the 42,000 ceiling |
| Prose words | 40,755 | 24 notice words excluded from sentence/readability figures |
| Sentences | 2,905 | Tool tokenizer |
| Mean / median | 14.03 / 11 | Mean within 13–15.5 working range; median on target |
| Population SD | 11.09 | Still materially below the ~26 design target |
| ≤5-word share | 25.9% | Close to 27.7% |
| ≥40-word share | 3.4% | On the 3.3% target |
| Paragraph mean / median | 40.92 / 29 | Mean high; median within accepted ceiling; ASR proxy caveat applies |
| Marked breaks / 10k | 8.83 | Target ~8.7 |
| Words per scene | 948.3 | Target ~950 |
| Flesch ease / grade | 89.4 / 4.27 | Easier than 72.3 / 6.8; grade within edition working range |

The low spread and unusually easy readability remain measured departures, but the repair's protected restorations did not create a new line-level defect, and the brief did not authorize a broad metric-chasing rewrite. The primary working checks—mean, long-sentence share, and scene length—pass.

`bash editions/monroe-1.3/tools/ed.sh overlap book-06-the-compacts-hand 8`

- 0 unprotected shared runs of at least eight words.
- 21 protected runs, allowed.

`bash editions/monroe-1.3/tools/ed.sh gates book-06-the-compacts-hand 8`

- All seven chapters: `reader_standard=0`, `metadata=0`, `modern=0`.

`bash editions/monroe-1.3/tools/sweep_probe.sh book-06-the-compacts-hand 8 8`

- Total: 1% skeleton, 11% close across 1,827 probe sentences.
- Ch48 0/9; ch49 1/12; ch50 0/10; ch51 2/11; ch52 1/9; ch53 0/10; ch54 4/13. The ch51/ch54 rise is accounted for by protected restoration.

## 4. Reader clarity

Pass after the line fix. Speaker attribution and referents remain stable through the procedural scenes, the five-person council, and all four exchanges. The naming repair removes the principal audio-first ambiguity: the unqualified “evaluator of record” now consistently points to Gault outside the protected certification formula, while “certifying office” points to the Archmarshal's office.

For the fluent thirteen-year-old lens, Karis's closing and the ruling remain the densest passages, but each legal proposition is grounded by a scale, a frame, a stopped pen, a door, or a physical record. The ch49 recap cut improves forward motion without removing the reasoning. Havel is oriented immediately. The ch54 notice interpretation now proceeds top-to-bottom once and is easier to hold by ear. The protected ruling's long first paragraph is demanding but coherent and intentionally formal.

The Reader Standard passes with no flagged language, sexual content, crude slang, blasphemy, or gore. Violence carries pain, treatment, uncertainty, and lasting cost.

## 5. Listening proof

All seven chapters were checked in full, including every r1 region.

| Chapter | Result |
|---|---|
| 48 | Pass. Quotes and italics balance; every `---` has blank-line spacing; numbers are spelled out; speaker turns and the blanket rehearsal are clear by ear. |
| 49 | Pass. Quotes and italics balance; scene marks are clean; no narration-risk abbreviation or numeral occurs; the shortened remedy sequence and certifying-office/evaluator distinction read cleanly. |
| 50 | Pass. Quotes and italics balance; scene marks are clean. `Priority Level 4` is the only prose digit and is protected record wording with an unambiguous spoken “four.” Station/frame-house referents remain distinct. |
| 51 | Pass. The ruling uses valid continued-paragraph quotation: the first paragraph opens the quotation and the final protected line closes it. Italics and scene marks are balanced; the Havel and Seln cuts leave no broken join. |
| 52 | Pass. Karis's bibliography uses valid continued-paragraph quotation with Karis held as speaker throughout. Italics and scene marks balance; the repaired station and Book 5 trial callbacks are unambiguous by ear. |
| 53 | Pass. Quotes, italics, and scene marks balance. Board capitals contain no abbreviations or digits; burst counts are written as words and remain trackable. The one-morning/key sentence has a clean referent. |
| 54 | Pass subject to the continuity line fix below. Quotes, italics, fenced notice, and scene marks balance. The notice fields, “Both. Enter both,” board ritual, protected speech, protected Log, and post-Log shoulder accounting have clean joins and distinct speakers. |

No narrator-risk abbreviation, unresolved homograph, ear collision, or malformed Markdown join requires another fix. Chapter numbers are headings rather than narrated prose.

## Exact line fixes

1. `manuscript/chapter-54.md`
   old: `Then the healer had Ephram's wrist in one hand and his elbow in the other, and Brom had him round the chest. She said something short, and there was a second sound like the first, and Ephram made a noise that he afterward denied.`
   new: `Then the healer had Ephram's wrist in one hand and his elbow in the other, and Brom had him round the chest. She said something short, and there was a second sound like the first, and Ephram made a noise that he afterward denied. She bound his arm across his chest and said the shoulder would want a month.`
