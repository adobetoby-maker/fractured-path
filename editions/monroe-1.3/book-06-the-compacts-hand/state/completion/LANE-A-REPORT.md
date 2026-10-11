# Book 6 completion pass — Lane A report (ch1–30)

Author seat: Claude Opus 5.5 (O'Connor 1.3 seat). Date: 2026-10-11. **Final, after the coordinator's
Lane A rulings (LANE-RULINGS.md, Lane A §1–4).**
Scope: `manuscript/chapter-01.md` … `chapter-30.md` only. Baseline: `state/completion/pre-lanes/`.
Method: every chapter read in order, edited in place with the Edit tool, one sentence at a time.
No script wrote to any manuscript file. No git command was run. Nothing under `books/` was opened
(the overlap and probe tools read it; where I needed more than the probe's rounded percentages I
printed counts and manuscript sentences only, never source text).

**Three steps.** (1) The first pass came out at −81 square/flat and −117 pause/look/silence/ask.
(2) I restored 68 of those edits by hand so that Lane A sat on the brief's numbers (−49 / −60), and
listed them as a reserve. (3) The coordinator ruled the reserve re-applied, holding back seven, so
that both halves of the book are thinned at the same rate. I re-applied them one at a time with the
Edit tool, re-reading each in its present context. **59 of the 68 are applied; 7 are held back by
the ruling; 2 I left as written** (§6). The figures below are the final ones.

## 1. Counts, before → after (ch1–30)

Counted with `grep -oiE` over ch1–30, case-insensitive. These patterns reproduce the brief's Lane A
figures exactly (98 / 73 / 10 / 78 / 81 / 66 / 37 / 5 / 6).

| Target | Pattern | Before | After | Change | Brief / ruling |
|---|---|---|---|---|---|
| square family | `\bsquar(e\|ed\|es\|ing\|ely)\b` | 98 | 73 | −25 | P1: about 45; reserve applied |
| flat | `\bflat\b` | 73 | 35 | −38 | (square + flat combined: **−63**, 37% of the pool; Lane B 46%) |
| quarter-turn | `quarter[- ]turn\|a quarter of the way round` | 10 | 9 | −1 | counsel's rule and Seln's cup only |
| pause | `for a (moment\|while\|time)\|for some time\|for a long (moment\|while\|time)` | 78 | 35 | −43 | P2: 50–60; reserve applied |
| not-looking | `did not look\|without looking\|never looked\|not looking` | 81 | 65 | −16 | |
| silence | `(nobody\|no one) (said\|spoke\|answered)\|said nothing\|did not say anything` | 66 | 18 | −48 | |
| not-asking | `did not ask\|nobody asked\|without asking` | 37 | 29 | −8 | (P2 combined: **−115**, 44% of the pool; Lane B 38%) |
| "That was all." / "That was the whole of it." | literal | 5 | 2 | −3 | thin |
| "He found that…" | `he found that` | 6 | 3 | −3 | thin |
| "the way he/she…" gloss | `\bthe way (he\|she\|they\|a\|an\|one\|you\|it\|<name>)\b` | 151 | 148 | −3 | thin where it explains |
| man/woman/person simile | `(like\|as) (a\|an) (man\|woman\|person\|boy\|girl\|clerk\|someone)\b` | 45 | 43 | −2 | thin where it explains |
| `not X but Y` | `\bnot [^.,;?!]{1,40},? but\b` | 20 | 20 | 0 | |

Also outside the patterns: eleven more "He found he…" / "without a word" / "Nobody needed to" tics
removed (ch5:199, ch6:53, :83, :169, ch7:27, :81, :209, ch8:207, ch9:189, ch11:95, ch15:25).

**Special-attention chapters (pause / look / silence / ask, before → after):**
ch7 6/4/6/0 → 2/2/1/0 · ch19 4/1/6/5 → 2/1/1/3 · ch23 5/1/3/3 → 2/0/1/2 · ch24 3/2/0/1 → 3/2/0/1
(the bout is untouched) · ch25 2/4/2/1 → 1/3/0/1.

**Quarter-turns left (9):** the counsel's rule ×2 (ch20:95, :189) and Seln's cup ×7 (ch15:151,
ch18:201, ch19:113, :157, ch27:201 ×3). Removed: one of the three cup-turns in the bean scene
(ch19:61), where it had become a metronome (accepted, ruling §4). Jent's lid in ch10 stays (ruling §3).

**KEEP motifs intact:** `flat hand` and the push; Bracken's small square hand and capitals, his
clocks and glasses; Seln's exact squares, square-to-the-edge pen and spoon, cup, case and flat
hands (ch27:209–225, ch29:101); Gault's straight case; Hesk's losing clock; Brom's pockets
(hand flat over the letter: ch16:109, ch22:49, ch29:249), his squared cases (ch30:241) and his
"one step"; Ilsev's files never quite square; Havel squaring his things (ch13:147) and the
minute-book twice (ch20:235); Jent's and the Anchor woman's weight "square" with no lean
(ch10:127, ch20:135, ch26:175), one image across three chapters; all floor, court and ring geometry.

## 2. Words, before → after, per chapter (`wc -w`)

| Ch | Before | After | Δ | | Ch | Before | After | Δ | | Ch | Before | After | Δ |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 01 | 5369 | 5361 | −8 | | 11 | 4400 | 4387 | −13 | | 21 | 3950 | 3928 | −22 |
| 02 | 4226 | 4215 | −11 | | 12 | 5089 | 5054 | −35 | | 22 | 3178 | 3156 | −22 |
| 03 | 4820 | 4801 | −19 | | 13 | 5930 | 5881 | −49 | | 23 | 3861 | 3640 | −221 |
| 04 | 4933 | 4875 | −58 | | 14 | 3514 | 3514 | 0 | | 24 | 4485 | 4376 | −109 |
| 05 | 4022 | 4004 | −18 | | 15 | 3314 | 3271 | −43 | | 25 | 3545 | 3355 | −190 |
| 06 | 3620 | 3597 | −23 | | 16 | 3780 | 3662 | −118 | | 26 | 4774 | 4754 | −20 |
| 07 | 4472 | 4415 | −57 | | 17 | 4813 | 4787 | −26 | | 27 | 4172 | 4121 | −51 |
| 08 | 4786 | 4756 | −30 | | 18 | 4271 | 4218 | −53 | | 28 | 4726 | 4674 | −52 |
| 09 | 4730 | 4568 | −162 | | 19 | 4399 | 4333 | −66 | | 29 | 4803 | 4794 | −9 |
| 10 | 3731 | 3728 | −3 | | 20 | 5383 | 5375 | −8 | | 30 | 5430 | 5411 | −19 |

**Total: 132,526 → 131,011, −1,515.** ch14 (Vastin, long metre by design) is unchanged.
With Lane B's −1,616 the book loses about 3,130 words by `wc`.

## 3. ch23–25 re-briefing: −520 words (brief: 500–700)

ch23 −221, ch24 −109, ch25 −190. Duplicate explanation only. The confluence bout (ch24:1–189) is
untouched apart from one clause after it; the production order, the four floor facts, Rooke's
bread brief, "growth" / "honesty", the false quarter entered as Rooke's, `Again. Faster. It's there.`,
the bout sheet, the box, and "One of these is the best night of my life." / "Noted." all stand.
The reserve touched none of these three chapters.

- **ch23:19** — Bracken's colours note: two clauses explaining why registrars write things down.
- **ch23:29** — "he understood that he had been allowed to know there was a question, and nothing else."
- **ch23:49–53** (Rooke in the yard) — the sealed-line speech said once, not three times: out went
  "It doesn't read the Stone's card…", "That's all it's ever read…", the sheet-laying gesture, "The
  program is getting things written down where nobody can rub them off", "It's the only thing that
  does catch up", and Cael's "not a defence, a trade". Kept: "It reads meet records… And nobody can
  take it out again. That's the program. Everything else is mornings." and the ladder / stamps turn.
- **ch23:85, :97** — "nobody ever asked him" said by Rooke only; Lira's repeat of it on the apron went
  (the payoff, "Eleven years. Nobody asked." / "I asked.", ch24:181–183, is untouched).
- **ch23:117** — the apron scene's ending (see §4).
- **ch24:189** — "their instructor, the man they had sent up the hill for a year".
- **ch24:199** — Cael's report of her feet no longer re-narrates exchanges one and two beat by beat.
- **ch24:225** — Rooke's bill: "borrowed against tomorrow" (said at :139 and :161), the hand-span
  gesture, and "no frames, and no bursts until it was quiet" (ch12:179 word for word; ch25:91 repeats it).
- **ch25:37** — Lira's account of why the officer waited is two sentences now; Seln gives the full
  version, with the clerk and the nineteen minutes, at supper (:51–61). "He did not say anything. She
  was right…" went.
- **ch25:63, :77, :99** — "There was a silence at the table."; "Cael looked down the table at her. She
  did not look back."; "It was the thing she had said to Rooke at the rope, turned round the other way…".
- **ch25:133** — Lira's recall of the meet-record idea keeps the file and the clerk; Rooke's speech is
  not quoted back a second time.
- **ch25:167** — one sentence cut that was also a defect: see §7.

## 4. Scene endings broken (current chapter:line)

Each used to run object → stillness → interpretive sentence → maxim. Each now lands on a task, a
movement or a concrete fact.

1. **ch9:61** — after Bracken asks for his own misspelling back, a paragraph explained what the two
   of them had just done. Ends on "Bracken read it, and nodded once, and went back to the lamp-oil."
2. **ch13:265** (Movement 2's close) — ended "It was the first page he had ever begun that he hoped
   he would never need to fill." Ends on the empty column: "He left the rest of it empty, for now."
3. **ch16:187–189** — a paragraph said what he had really been measuring. Ends on the five seats over
   the door, "whatever his feet did", and "Then he went to bed."
4. **ch17:211** — "She did not say anything else. She did not need to. They looked at the shaky
   signature for a while…" Ends on Karis gathering the copy, the press and the key.
5. **ch18:219** — ended on Cael finding he had been taught something and not knowing when. Ends on Seln
   crossing the court and Cael standing in the cold with nothing in his hands.
6. **ch23:117** — "She looked at it for a long time. She did not say anything about it, and he did not
   ask…" Ends on the east river and "After a while they went in."
7. **ch27:103** — "He had stood in the one place in the room nobody else would stand, and the room had
   moved round him." Ends "He had not mentioned the gate once."

Smaller breaks of the same machine inside a scene: ch4:245 (the declared stillness and the squared
wrap before Brom's speech), ch6:55 (the "Cael sat with it a while" opener), ch9:91 (the gloss on
Karis's slip), ch16:109 ("The arrangement held. It had started to cost the table something…";
Lira says it better on the stair), ch28:161 ("He found that he did not have anything to say…"), and,
with the reserve, ch28:177 (the council's "I mean the reach." now runs straight on to the rain).

## 5. Checks (re-run after the reserve)

- **Protected text.** All 51 patterns in `protected-patterns.txt`: per-chapter match counts
  identical to the baseline for ch1–30 (0 mismatches; 22 chapter-hits in this range). 40 further
  Tier A/B and locked-figure phrases checked verbatim, 0 changed. Every italic-only paragraph in
  ch1–30 (Log entries, notices, forms, letters, slips, board cards) is byte-identical to the baseline.
- **Overlap** (`ed.sh overlap`, 8-word): M1 0, M2 0, M3 0, M4 0, M5 0 unprotected; protected runs
  19 / 10 / 13 / 7 / 11, the same as before.
- **Gates** (`ed.sh gates`): reader_standard 0, metadata 0, modern 0 for every chapter in M1–M5.
- **Probe** (`sweep_probe.sh … 1 5`), skeleton / close, baseline → now: M1 2/11 → 2/10; M2 1/8 → 1/8;
  M3 1/13 → 1/13; M4 1/10 → 1/10; M5 1/11 → 1/10. Matched-sentence counts (same method, numbers
  only): skeleton 24 → 22, 9 → 9, 19 → 18, 11 → 11, 4 → 4; close 148 → 142, 97 → 92, 170 → 163,
  120 → 115, 67 → 63 (M5 counted over ch28–30). No chapter's count rose. **One display line rose:
  ch9 skeleton 0% → 1%.** It is the same single sentence before and after (Lira's "But there's
  usually a yard out the back."); 1/201 = 0.497% became 1/195 = 0.513% because six other sentences
  left the chapter. I did not touch her line.
- **Metrics** (`formula_metrics.py`), ch1–30: sentence mean 13.61 → **13.60**; ≥40-word share 4.1% →
  **4.1%**; words per scene 937.7 → **927.0**; 111 scene breaks before and after (scene order
  unchanged). By movement now: M1 13.47 / 3.5% / 945; M2 13.07 / 3.9% / 976; M3 13.85 / 4.4% / 856;
  M4 13.79 / 4.4% / 909; M5 13.39 / 4.5% / 965 (shared with Lane B). M2's own mean was 13.08 before
  this pass and M4's ≥40 share was 4.7%; the lane holds all three limits.
- Calendar, counts, ranks, standings, distances, names: no figure, day, date or title was edited.
  The lane bill (ten / ten / twelve), "two renewals on paper" (ch16:133, ch20:171, ch26:103), the
  first pole, `Caelen Hesk-ward`, "evaluator of record" and the eighty-one words are as they were.
  No season name, month order, English weekday name or metric unit was introduced. No new named
  character. No new material: the one sentence I wrote rather than cut (ch7:135, "She kept the pen
  on the line she had drawn.") replaces a narrated silence with the pen already in her hand.

## 6. Declined, and why

**From the reserve (ruling §1 asked me to say so):**

- **ch1:99** — "like putting a hand flat against the morning and pressing" stays. "A palm against the
  morning" reads thinner, and the line is the lane's own answer to the `flat hand` of the push three
  paragraphs earlier.
- **ch17:155** — "She looked at him for a long moment with her quiet face." stays. Without the pause
  the sentence fell into the probe's close band (0.38), and ch17's close count rose by one. Restored;
  the count is back to 33.
- **Held back by the ruling (7):** ch10:127, ch20:135, ch26:175 (the "square" weight with no lean);
  ch16:109, ch22:49, ch29:249 (Brom's hand flat over the pocket); ch30:241 (Brom's squared cases).
- Still as written from the first pass, for the same probe reason as ch17:155: ch19:217, ch20:261,
  ch26:11.

**From the pass as a whole:**

- **ch24:1–189, the confluence bout.** Not edited at all, including its fourteen literal "square"s
  (the ring), "flat and hard and clean", and "looked at him for a long time" (:151).
- **Consent boundaries.** Every "nobody asked" about Brom's letters stands (ch12:265, :277; ch16:109;
  ch19:69, :71; ch22:123), as do Ephram's "I'm not asking you anything" (ch3:221–223), the unasked
  case (ch29:129, :233) and Lira's "She did not ask him again" at the ferry (ch21:85).
- **Silence that is a named character's own language.** Seln's, Rooke's, Bracken's, Brom's and Havel's
  chosen not-speaking and not-looking mostly stand (ch13:125, :157, :181; ch17:15; ch22:119; ch27:207, :225).
- **ch14** (Vastin): no change; long metre by design. **ch29–30** (the catechism, the road cut): five
  small cuts only; M5 keeps its room by ruling #45.
- **Aphoristic closes that are the argument of their scene**: ch6:55 (a date as a kindness), ch7:231
  (the copy left open "waiting for better light", Movement 1's close), ch13:139 (the hood), ch20:277
  (Seln's last line), ch22:149, ch26:139–143 ("He wasn't even careful"). Left.
- **ch9:245** — "But there's usually a yard out the back." A probe near-match, and Lira's line. Left.

## 7. Small fixes made in passing (all accepted, ruling §4)

- **ch25:167** — "…wait to see if anything came and sat in it. / Nothing did." had a sentence about
  Lira's hand in her coat wedged between the two, so "Nothing did." pointed at the wrong thing (and
  the hand in the coat is already in the same paragraph). Cut the wedged sentence.
- **ch12:25** — "his hands folded… like a man waiting outside a shop" repeated ch2:13 word for word,
  about the same man. Removed the second.
- **ch18:157** — "He did not know yet what it was." scored 0.50 in the probe against an unrelated
  source sentence. Now "He had no name for it yet." This is why M3's skeleton count fell by one.

## 8. For the coordinator

### 8.1 The reserve — applied

59 of 68 applied, by hand, each re-read in place. By family: square/flat 14 (ch5:201, ch9:11,
ch9:189, ch10:91, ch10:193, ch13:125, ch13:241, ch15:5, ch20:95, ch20:157, ch26:211, :239, ch29:125,
ch30:187); pause 18; silence 16; mixed 7; not-looking / not-asking 4. Nothing in the reserve touched a protected run, a consent boundary or ch23–25.

Two joins worth a second ear at the listening proof, because the cut removed the only beat between
two speeches or between a speech and an action: **ch13:217–219** (Seln's "they write it down" now
goes straight to the residence door) and **ch18:97** (the two declared silences over the post are
gone; the grey seal laid on Bracken's pile carries it).

### 8.2 "Square capitals" (accepted, ruling §2)

Bracken, Rooke (ch12:5, ch17:121, ch21:95, ch24:205; Lane B's ch34:5, ch56:65) and Ephram's
"square, cramped hand" (ch3:205, ch5:5, ch17:135) keep them. Lira's are "large capitals" /
"capitals" (ch8:61, ch21:103, :173, ch28:243). Bracken's own hand is "small upright" at ch2:107,
ch6:5 and ch13:11 and "small square" at ch23:15; left.

### 8.3 Found, not changed

- **ch14:94–95** has a doubled blank line and **ch17:185** a trailing space after the closing quote.
  Cosmetic; left so the diff stays to prose.
- **ch18:169 / ch29:199** — the lodge-man is "a short square man with a grey beard" and the coachman
  "a short broad man with grey whiskers". Close by ear.
- **M2 sentence mean is 13.07** (13.08 before the pass), under the book's 13.3 floor at movement
  level though the lane is at 13.60. Pre-existing.
