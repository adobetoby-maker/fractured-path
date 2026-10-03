# Book 3 — completion pass, Lane 1 report (chapters 1–31)

Author: Claude Opus 5.5 (O'Connor 1.3 seat, writing as Monroe Jackson), 2026-10-02.
Brief: `PASS-BRIEF.md`, Lane 1. Read first: `whole-arc-read.md` §§3, 4 and 9; `whole-arc-notes.md`;
O'Connor `VOICE.md`; `EDITION_BRIEF.md`; `BOOK_MAP.md` §9; `protected-patterns.txt`. Depth was
calibrated against Book 1's `LANE-1-REPORT.md`.

**Files edited.** `manuscript/chapter-01.md` … `chapter-31.md` and this report. Nothing else was
touched. No git command was run. The coordinator's 24 line fixes were left as they stood: none was
redone or undone.

**Method.** Every change was made by reading the paragraph and writing the replacement by hand,
applied as an exact single-match Edit. No sed, regex or script touched prose. Before starting, ch1–31
were snapshotted to the session scratchpad; every before/after figure below compares that snapshot with
the finished files.

The lane author did ch27–31 (both priorities). Four same-seat workers (Opus 5.5, same brief, same
keep-list) did Priority 1 in ch1–7, ch8–14, ch15–20 and ch21–26 in parallel, each touching only its own
chapters. The lane author read their changelists, spot-read their diffs, and made two corrections
(§6). Read-only helpers in the scratchpad: `count2.sh` (the grep counts) and `closecheck.py` (the
skeleton-probe method, before vs after, listing any newly close sentence).

## 1. Texture counts (grep, ch1–31, case-insensitive)

| Target | Before | After | Change |
|---|---|---|---|
| Words, ch1–31 (`wc`) | 144,226 | 141,769 | −2,457 |
| **"the way" (every use)** | **239** | **128** | **−46%** |
| — with a generic subject ("the way a/an/you/people/someone…") | 53 | 25 | −53% |
| "as if" / "as though" | 156 | 97 | −38% |
| — "as if it/she/he/they had/were" | 62 | 44 | |
| "a long time" | 52 | 18 | |
| "a long moment" | 20 | 5 | |
| "for a moment" | 49 | 21 | |
| "for a while" | 23 | 2 | |
| "for some time" | 8 | 1 | |
| **Duration pads, total** | **152** | **47** | **−69%** |
| — "for a long time/moment/while" (the read's measure) | 55 | 19 | −65% |
| **"found that"** | **43** | **2** | **−95%** |
| "exactly" | 140 | 78 | −44% |
| Document re-readings ("read it twice/again/a third time…") | 23 | 11 | |
| "a third time" | 6 | 3 | |
| "three times" | 21 | 16 | |
| "did not look up" / "without looking up" | 16 | 7 | |
| finger's / hand's width, hair's breadth | 14 | 11 | |
| "a hair" | 6 | 2 | |
| "squared" | 9 | 6 | |
| "went (very) still" | 13 | 12 | |
| Oona: "whole (serious) face" | 8 | 3 | |
| Oona: "slate under her arm" | 14 | 6 | |
| Wray "off a gauge" | 2 | 2 | ch7 and ch17, the §3 keeps |
| the knock, "door shutting in another room" | 3 | 3 | ch1, ch7 (keeps) and ch28's "slammed" (escalation, allowed) |
| Iron Skin "frost on a pane" | 1 | 1 | ch6 (keep) |
| Brom's laugh, "did him for a laugh" | 2 | 1 | ch4 (keep) |
| the bread's "larger half/piece" | 6 | 1 | ch15, the first, kept as the anchor for ch39's rule |
| "with great dignity/seriousness" | 5 | 2 | |
| "I'd think less of you" | 5 | 2 | |
| Gerda "tall and narrow" | 7 | 3 | ch8, the first full use, kept |
| "patient as a gatepost / like a post" | 2 | 1 | ch27, the first, kept |
| "the square/plain hand he kept/saved" | 7 + 2 "slow, square" forms | 0 + 2 | ch2 and ch6, the §3 keeps, are untouched |
| *Watched:* "like a" | 88 | 89 | |
| *Watched:* "as" (every use) | 719 | 694 | Conversions were outnumbered by cuts |

**Against Book 1's depth.** "the way" −46% (Book 1 −48%); "found that" −95% (−82%); duration pads
−69% (−77%). The pads were cut less deeply here, on purpose: the 47 left are counted beats or speech.
Examples are Quenna's decision in the fourth exchange (ch19), "For a moment nobody moved" before
Lira's reach (ch11), Lira's silence on the wall (ch29), "Karis was quiet a long time" before the Tide
verdict (ch30), and Gerda "very hungry for a long time" (ch27, meaning-bearing). They also include
every pad inside a bout and the speech lines.

**Keeps from §3, verified present.**
- Brom "the way a smith considers a bar of iron" (ch1).
- The knock (ch1, ch7).
- The frost (ch6).
- The gauge (ch7, ch17).
- The chest-laugh (ch4).
- The square hand (ch2, ch6).
- Oona's whole face (ch12, the first; ch16/ch17).
- The slate (ch5).
- P6's triple reading with the tea going cold (ch2).
- The petition reading (ch16).
- Every simile inside a bout or training exchange.
- Karis "went very still, the way she went still before an ignition" (ch30). This is the first
  occurrence in this edition (see §6).

## 2. Priority 2 — ch27–31

| Chapter | Before | After | Change |
|---|---|---|---|
| ch27 | 4,618 | 4,567 | −51 |
| ch28 | 4,386 | 4,078 | −308 |
| ch29 | 4,398 | 4,282 | −116 |
| ch30 | 4,323 | 4,336 | +13 (the new beat, below, net of cuts) |
| ch31 | 4,246 | 3,907 | −339 |
| **ch27–31** | **21,971** | **21,170** | **−801** |

**ch28 (the reported week).**
- The session 5–10 margin entry is compressed to one line per pair. Every variable and the "Consent
  given" beat are kept.
- The first-year's grievance over the room is folded into one sentence.
- The barley line is trimmed to its fact.
- The morning-after cost paragraph is cut. It duplicated, item for item, the Compression entry that
  follows it. The breastbone ache stays, because ch29 and ch36 recall it.
- The push-mechanics paragraph is tightened.
- The read-back list is cut from fourteen items to eight, the ones that carry the variety.
- "That was the strangest thing about the whole week…" is cut, along with the closing paragraph's
  doubled clauses.

Kept whole:
- session nine and the pen;
- the release-lag conversation, because the match depends on Karis's lag;
- the whole push, on the eighth try with the elbow on the sixth;
- Oona's "Seven weeks. And two days." and Hesk's hand;
- the thickening, "Three in about twelve", and the grey fingertips;
- "Fourteen boundaries";
- "eight more sessions";
- the missing-something close.

**ch31 (the twenty-second session).**
- The plan paragraph no longer re-lists the variables that ch28's read-back already listed.
- "He knew her now" no longer re-states ch28's tells, the quarter-second, the half-breath and the
  lengthening release. It keeps the new beat: he knows her better than Lira in one narrow way, he
  knows where the next point will fall, the thickening comes twice, and he has learned her below
  memory.
- The ruled line keeps its figure and loses the pause.
- The Hesk letter's ledger sentence is shortened, because it re-stated ch28's epiphany.
- The recap of Quenna's and Karis's lines before the note is cut, since ch30 had just shown them.
- The calendar paragraph loses "Show enough to pass. Bank everything that matters." and the
  reader-under-a-lamp line, which ch32's opening repeats the next morning (see §6).
- The closing log is trimmed to its counts.
- Untouched: Gerda's bout (every exchange and landing beat), "We are missing a condition", Karis's
  wish to be the source, "Noted", the barley clause, the wall scene, "Same rule. Heavier load.", the
  note text and "*Part of me is still waiting.*"

**Short of the target.** ch28 and ch31 lose 647 words between them, and ch27–31 lose 801, against
the brief's "about 1,000". The rest of the overlap sits in beats a later chapter pays: the lag (ch36),
the thickening (ch37), Oona's Kindling account (ch41), Karis's volunteering (ch32, P18), and the
missing-condition close (ch29, ch36). I stopped rather than cut into those.

**"Part of me is waiting" in ch30.** It is a new paragraph at the end of the chapter, as Cael climbs
the stair after leaving Gerda and Lira on the floor the night before her bout:

> Halfway up the stair it came to him that the part of him he had written down a week ago had been
> listening too. *Part of me is waiting for it.* None of the nulls since had moved it. It had heard
> Gerda say she would come out of the haze and take what was put on her where the chairs could see,
> and it had leaned toward the words, because somewhere ahead there was still a floor that was his.
> He did not like it any better than he had at the desk. He went on up.

The paragraph quotes ch29's binder line exactly. It sets Cael's stake beside Gerda's on the night her
stake is paid, and it bridges to ch31's closing "*Part of me is still waiting.*" ("Part of me is"
now counts 2 → 3.)

## 3. Changelist

"Conv." means a "the way" or "as if" simile was recast as "as" or "like", with the image kept.

- **ch1:** Cut the arm-weight gloss, the river and chipped-tooth similes, the overnight re-read of
  the notice, the clerk's "as if", "found that", two "exactly" and three pads. Kept the smith, the
  cupped hands (training) and the hot bar (cost).
- **ch2:** Cut "found that" ×2, three pads, the clerk's "twice", Lira's "again", Brom's hold simile
  and "exactly as he remembered". P6 and the square hand are untouched.
- **ch3:** Cut "found that" ×3, three pads, the voice and gloves similes, and two "as if". The
  orientation line is now "hold it against you", so Naveth's "I'd think less of you" stands alone.
  "For a long time now" became "for months now" (see §6).
- **ch4:** Cut two "as if", the second weather simile (a repeat of ch3), "found that", a pad and two
  "exactly". The orthodoxy "exactly"s and Brom's "long moment" are kept as training-exchange text.
- **ch5:** Oona is down to one tag per scene. Cut "found that" ×4, the notice and request re-reads,
  Brom's "did not look up" and "went very still", two "exactly" and three "as if". The instructor's
  "went very still" is kept, because it times "shattered".
- **ch6:** Oona is down to one tag. Cut the weather and bruise similes, "found that" ×2, two pads and
  the refusal's "read it twice". Kept the frost, the square hand, the hinge (mechanism) and Prynn's
  "exactly"s.
- **ch7:** Cut three "as if", the closed-eyes simile, three pads, three "exactly" and the crowd's
  "without looking up". Demonstration exchanges, the knock, the gauge and every protected line are
  untouched.
- **ch8:** Cut six pads, three "exactly", two "found that", the second crowd simile and Edran's
  filing gloss. Conv. ×3. Everything in Lira's standings bout is kept, along with Gerda's first "tall
  and narrow" and Hobb's "exactly as hard".
- **ch9:**
  - Two "did not look up" are now "went on with his porridge" and "paid no attention".
  - The provision count is now "more than once that week".
  - Kept: the clerk's double reading (it pays Lira's rumour) and "speaks a fraction early into a
    silence" (Karis's partner).
- **ch10:** Karis's "I'd think less of you" is now "I'd have worried if you had". Cut four "exactly",
  two "found that", two pads, Quenna's "did not look up" and the kept-hand line. The first "Noted"
  and the off-hand plant are kept.
- **ch11:**
  - The clauses, "at the end of the month" (fix 1) and the anchors are untouched.
  - Cut the re-reads of clause 4 and the declaration card, three "exactly" and a second Karis tag.
  - Kept: Karis squaring the folder, "For a moment nobody moved", and the receipt "exactly"s.
- **ch12:** Cut Quenna's weather simile, Lira's rain simile, Oona's seriousness and slate, three pads,
  "found that" and "a hair". Conv. ×4. Kept Quenna's second reading of the terms and Cael's four
  sheets read twice (both are the beat), and Oona's first whole-face tag.
- **ch13:** Coss reads the approval "slowly, because the speed of it was information". Two pads were
  recast. Cut Naveth's first "squared" and two "exactly". Coss's three readings are kept, because
  they are his method.
- **ch14:**
  - Cut four glosses, the baker's "exactly", three "found that", a pad, Oona's imagined slate and the
    saved-hand line.
  - The transmittal is now read twice.
  - Kept: the honey thief, the forty copies, Karis's one "did not look up", and the coordinator's
    Wray fix.
- **ch15:** The water opener is now "like floodwater coming up a stair". Cut three "as if", three
  pads, "found that", one "exactly" and the second "larger half". Kept the first "larger piece", the
  coal simile, the off-hand "listening" and the bout silences.
- **ch16:**
  - Quenna's "did not look up" is now "went on writing". Gerda's stays, because the next line needs it.
  - Oona keeps one gesture.
  - Cut Gerda's "tall and narrow".
  - The petition reading and the tea callback are untouched.
- **ch17:** Brom's nod is recast. Cut Gerda's "as if deciding", "tall and narrow", three pads, Oona's
  slate ×2 and two of her tags. Kept her whole face, Wray's gauge, and Edran's "I'd think less of
  you".
- **ch18:** Six "the way" were converted or cut. Oona is down to one tag. Cut three "exactly",
  "found that", the hand's width and three pads. The tout's book and "Tires in the sequence" are
  untouched.
- **ch19:** Bout exchanges are untouched. In the framing, cut Brom's funeral-simile echo, four "the
  way", three "exactly", two pads and Oona's whole face. Quenna's "long moment" is kept.
- **ch20:**
  - "As if" is down from eight to three.
  - Cut Hobb's third "handed something" figure, two slate tags, "great seriousness", four pads,
    three "found that", the withdrawal read twice, and the chart gone through twice.
  - The one-line "Naveth was quiet for a moment" paragraph is gone, and "He was quiet again" is now
    "He let that sit".
  - Untouched: "Thank me with your assessments", "Worry when they start to agree", Wray's record line
    and fix 3.
- **ch21:**
  - Conv. ×2. Cut two other "the way", two "as if", four pads, "found that", Brom's "squared", "read
    them twice" and two "exactly".
  - Kept: Lira reading like an opponent (the first), her "did not look up" (the next line needs it),
    "Told you she had a method", "Not asked" and the fetch column.
- **ch22:** Cut "found that" ×3 and a gloss. Conv. ×2. Cut Oona's whole face and her echo of
  Karis's flat hands. Brom's sentence and fix 4's bread sentence are untouched.
- **ch23:** Hesk's letter is read once, and the bench line again. Cut four pads, the saved-hand line
  and two "as if". "Same rule. Heavier load." and "the second one's the floor" are untouched.
- **ch24:**
  - Six "the way" were cut or converted.
  - The Fenmark sheet's re-reads are thinned, and Cael now sees Lira read it "more than once". The
    final search for the made-up sentence is kept, because it is the beat.
  - Cut the larger half, "tall and narrow", "squared", three "found that", four "exactly" and three
    pads.
- **ch25:**
  - "I'd think less of you" is now "I'd trust the answer less if you did".
  - Cut "like a post", Quenna's "without looking up", "found that" ×3 and five pads.
  - The triple reading of the safety clause is kept, because it is the beat.
- **ch26:** Cut the chest-laugh, the plain-hand line, "two posts", the duplicate of ch23's "the way
  she said the score", Quenna's "did not look up" and four "exactly". The notation heard three times
  is now heard twice. Both bouts, Wray's seven strikes, P8, P9 and the records line are untouched.
- **ch27:**
  - Cut Gerda's "tall and narrow", "for some time" on Quenna's pen, the slip-hour simile (the
    signature line keeps "every letter separate"), and "precisely" ×1.
  - Cut "as if reading out a clause" (ch30 keeps the Prynn version) and the hands "as if".
  - Cut "for a long time" ×2, "for a long moment" on Prynn, and "exactly how".
  - Gerda now looks after Hobb "until the hall door had shut behind him", replacing the second
    heavy-thing "as if".
  - Kept: the swimmer (bout), the fish, the wall taking rain, the gatepost (the first), Brom's "great
    seriousness" (the first), and "for exactly as long as it took Gerda to wonder".
- **ch28:** Priority 2, above. Also: "a hair more" is now "a little more"; the high-wall simile and
  the body-weight simile stacked on the felt were cut; Oona's slate and whole-face tags and her "long
  time" were cut; the larger half was cut; and "found that the map" was recast.
- **ch29:** Conv. ×3. Cut the kept-hand line, five pads, "found that" ×2, "exactly" ×2, the second
  hand's width, Oona's whole face ×2, her slate and three of her "as if"s (she keeps the stair "as
  if"), Hobb's "long moment" and Karis's "for a long time". The early-point simile is kept, because
  it is Karis's partner.
- **ch30:**
  - The new beat, above.
  - Cut Brom's "long moment", the forehead simile and Karis's second stool tag.
  - The notebooks ritual is folded into fewer sentences.
  - Cut the pen's "small definite click", "found that", and two "exactly".
  - The mark simile is now "as a person signs…".
  - The stone-in-a-boot simile is re-composed (see §5).
  - "Karis was quiet a long time" is kept, because it times the verdict.
- **ch31:**
  - Priority 2, above.
  - Cut the tout's "great dignity", Gerda's third clause simile, the laugh's "long moment", "found
    that" ×2, two pads, the note "read twice, and then a third time", and the kept-hand line.
  - The bout is untouched, including its "for a long moment" and "exactly where".

## 4. Checks

**Protected wording.** Every `protected-patterns.txt` pattern and every §9 / §9.2 line in ch1–31 was
grepped against the snapshot, and every count is unchanged. The checks covered:
- the clerical-error and nerve-to-sign-for lines;
- "Today proves you're real" and "Thank me with your assessments";
- P6/P7;
- Wray's D1 record;
- "Trust is a finding";
- the seven clauses and "at the end of the month";
- "real, unexplained, keep" (4);
- P8 (2), P9 and the records line;
- "Same rule. Heavier load." (2) and "the second one's the floor";
- "Told you she had a method" and "Not asked" (9);
- "You supplied that part yourself" (2) and "like a hand looks at bread" (3);
- the log anchors;
- "We are missing a condition" and "Twenty-two controlled sessions. Twenty-two nulls.";
- "Fourteen boundaries", "Three in about twelve", "Seven weeks" and "eight more sessions";
- "Waiting's a kind of looking", "Don't you ever make her the stakes", "Didn't go back" and the
  barley clause;
- Oona's "a little under six weeks".

Also unchanged: the 24 coordinator-fix strings, every count, date and fact, and every first occurrence
of a line later chapters quote.

**Scene breaks.** Identical in all 31 chapters (124).

**`ed.sh overlap`** (8-word gate):

| Movement | Unprotected | Protected |
|---|---|---|
| M1 (ch1–8) | 0 | 4 → 4 |
| M2 (ch9–16) | 0 | 1 → 1 |
| M3 (ch17–23) | 0 | 1 → 1 |
| M4 (ch24–31) | 0 | 4 → 3 |

The M4 drop is the ch31 recurrence of "Show enough to pass. Bank everything that matters.", cut in
Priority 2. BOOK_MAP §4 KEEPs it at D1, and its first occurrence (ch6) and its later uses (ch32, ch46)
are untouched.

**`ed.sh gates`, M1–M4.** reader_standard, metadata and modern are 0 in all 31 chapters.

**Skeleton probe** (`sweep_probe.sh book-03-no-path-given 1 4`):

| Movement | Before: skeleton / close | After: skeleton / close |
|---|---|---|
| M1 | 2% / 13% | 2% / 13% |
| M2 | 1% / 15% | 1% / 15% |
| M3 | 1% / 9% | 1% / 9% |
| M4 | 1% / 10% | 1% / 8% |

- No movement rose.
- Raw sentence counts (closecheck): no chapter's skeleton or close count rose. Skeleton went from 65
  to 60 and close from 728 to 675 across ch1–31.
- One percentage reads up: ch2 close went from 17% to 18%. That is rounding, because its raw count is
  33 → 33 on one fewer sentence.
- Every sentence that turned newly close after a cut was re-composed by hand. Across the five ranges
  that was about two dozen. In the lane author's chapters they were ch27's hands, and ch30's stone,
  ledger, listening and fifteenth-session lines.

## 5. Formula metrics (`formula_metrics.py`, ch1–31)

| Measure | Before | After | Working range |
|---|---|---|---|
| Words | 143,827 | 141,370 | — |
| Sentences | 10,843 | 10,793 | — |
| Sentence mean | 13.26 | 13.09 | 13–15.5 |
| Sentence median | 9 | 9 | — |
| ≤5-word share | 32.5% | 32.8% | up to ~34% |
| ≥40-word share | 3.5% | 3.4% | 2.5–4.5% |
| Paragraph median | 24 | 23 | up to ~30 |
| Words per scene | 927.9 | 912.1 | 850–1,050 |
| Flesch Reading Ease | 86.0 | 86.2 | — |
| Flesch–Kincaid grade | 4.56 | 4.49 | 3.5–6 |

**By movement** (sentence mean · ≥40 share · words/scene):

| Movement | Before | After |
|---|---|---|
| M1 | 13.37 · 4.5% · 969 | 13.23 · 4.4% · 956 |
| M2 | 13.38 · 3.2% · 869 | 13.22 · 3.0% · 858 |
| M3 | 13.16 · 3.4% · 971 | 12.99 · 3.3% · 957 |
| M4 | 13.13 · 2.9% · 914 | 12.93 · 2.7% · 888 |

**ch27–31** went from 12.64 · 2.7% · 877 to 12.43 · 2.6% · 844.

The whole range stays inside every working range. The sentence mean drops about 0.17, which is
expected: cutting a simile tail or a pad shortens its sentence, and nothing was joined to compensate.
M3 (12.99) and M4 (12.93) now sit a hair under the 13.0 floor. ch27–31 were already the read's §7
meter-only outliers. Removing about 800 words there without touching a scene break also puts their
words-per-scene at 844, just under 850. I did not join sentences to chase either number, under "No
scripted prose surgery" and §7's "do not force them".

## 6. Flags for the coordinator

1. **The ignition stillness.** §3 item 9 names ch25 as the first "went still, as she went still
   before an ignition". In this edition the first is ch30 ("Karis went very still, the way she went
   still before an ignition, all of her listening at once"), and ch37 repeats it word for word. ch25
   has only the off-hand plant. I briefly cut the ch30 instance and then restored it, so ch30 is
   kept as the first. Lane 2 should thin ch37 and ch51, not ch30.
2. **"Show enough to pass. Bank everything that matters."** The ch31 recurrence is cut; ch6 (the D1
   KEEP), ch32 and ch46 stand. M4's protected-run count is 3 as a result.
3. **ch3, "for months now"** replaces a worker's "for most of a year now". It stands in for "for a
   long time now", where Cael has been his own bell. I chose it to avoid stating a new elapsed time,
   given BOOK_MAP §12.16's calendar tension.
4. **"I'd think less of you"** now appears in ch3 (Naveth) and ch17 (Edran) only within ch1–31.
   Karis's ch10 and ch25 lines are reworded in her own register ("I'd have worried if you had", "I'd
   trust the answer less if you did"). The read's chain note "(ch3, ch10, ch25, ch32)" is now ch3,
   ch17, ch32.
5. **The bread.** In ch1–31 only ch15's "larger piece", the first, remains, as the anchor for ch39's
   rule. ch17 and ch20 now say "half". ch28's "stole the whole of his bread and gave him back the
   larger half" is cut; ch30's "stole his bread" remains.
6. **Gerda's "tall and narrow and very straight"** is kept only at ch8 (the first full use). ch5's
   "tall and narrow-shouldered" introduction is a different phrase and is untouched.
7. **Re-read counts changed, with no later quote affected:**
   - ch9's provision count is gone;
   - ch14's transmittal is read twice;
   - ch24 and ch26 no longer say Lira read the Fenmark sheet three times;
   - ch23's Hesk letter is read once.
   ch25's Karis terms are still "read aloud, twice, as she had read the first terms", which echoes ch11.
8. **Pads at −69%** against Book 1's −77%. The remainder is listed in §1. If the coordinator wants
   parity, ch8–14 and ch21–26 hold most of the candidates.
9. **Priority 2 is short at −801 of ~1,000.** The reasons are in §2. If more is wanted, the next
   candidates are ch31's Hesk letter (the Brom and Lira paragraphs) and ch28's Oona Kindling
   account. Both are warm scenes I chose to keep.
10. **Unchecked, not touched:** ch17 says Oona has been at Greyvane "for six weeks". The ch15–20
    worker noted it in passing; it was not verified against the ledger.
