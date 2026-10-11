# Book 6 completion pass — Lane B report (ch31–60)

Author seat: Claude Opus 5.5 (O'Connor 1.3 seat). Date: 2026-10-11.
Scope: `manuscript/chapter-31.md` … `chapter-60.md` only. Baseline: `state/completion/pre-lanes/`.
Method: every chapter read in order, edited in place with the Edit tool, one sentence at a time.
No script wrote to any manuscript file. No git command was run. Nothing under `books/` was opened
(the overlap and probe tools read it). After the first pass I re-read my whole diff sentence by
sentence and pulled back two edits that had added a small new action (ch33:195, ch36:47).

## 1. Counts, before → after (ch31–60)

Counted with `grep -oiE` over ch31–60, case-insensitive. Patterns are given so the run can be repeated.

| Target | Pattern | Before | After | Change | Brief |
|---|---|---|---|---|---|
| square family | `squar(e\|ed\|ing\|es\|ely)` | 101 | 62 | −39 | P1: about 55 |
| flat | `\bflat\b` | 127 | 62 | −65 | (square + flat combined) |
| quarter-turn | `quarter.?turn\|a quarter (turn\|of a turn\|round\|toward)\|by a quarter\|every quarter` | 20 | 15 | −5 | counsel's rule and Seln's cup only |
| pause | `for a (long \|little \|short )?(moment\|while\|time)\|for some time\|for the (space\|length) of` | 115 | 56 | −59 | P2: 60–70 combined |
| not-looking | `did not look\|without looking\|never looked\|not looking` | 90 | 77 | −13 | |
| silence | `(nobody\|no one) (said\|spoke\|answered)\|said nothing\|did not say anything` | 76 | 38 | −38 | |
| not-asking | `did not ask\|nobody asked\|without asking` | 32 | 22 | −10 | |
| "That was all." / "That was the whole of it." | literal | 10 | 4 | −6 | thin |
| "He/She found that…" | `\b(he\|she\|cael) found (that\|he\|she\|it) ` | 30 | 4 | −26 | thin |
| "the way he/she…" gloss | `\bthe way (he\|she\|it\|they\|a\|you\|<name>)` | 107 | 105 | −2 | thin where it explains |
| `not X but Y` | `\bnot [^.,;]{1,40},? but ` | 38 | 36 | −2 | |
| man/woman/person simile | `(like\|as) a (man\|woman\|person) (who\|…ing)` | 16 | 16 | 0 (2 recast outside the pattern: ch43:69, ch54:178) | thin where it explains |

My pause pattern is a little wider than the read's (it gave B 104); the other three pools match the
brief's Lane B figures exactly (90 / 76 / 32), as do square (101), flat (127) and the tics (10).

**Quarter-turns left (15):** the counsel's rule ×6 (ch32:204, ch44:67, ch46:65, ch47:39, ch48:71,
ch50:35) and Seln's cup ×9 (ch34:109, ch36:179, ch37:220, ch41:187, ch42:161, ch52:81, ch52:239,
ch58:269, ch60:71). Removed: Karis and the leaf (ch36:89), Jent's inkwell lid (ch48:59), the wool-press
capstan ×2 (ch50:55), Bracken's leaf (ch55:87).

**Two overshoots — coordinator please note (see §7.1).** Priority 1 came out at −104 against "about
55", and Priority 2 at −120 against "60–70".

## 2. Words, before → after, per chapter

| Ch | Before | After | Δ | | Ch | Before | After | Δ |
|---|---|---|---|---|---|---|---|---|
| 31 | 5094 | 5090 | −4 | | 46 | 5110 | 5016 | −94 |
| 32 | 5516 | 5491 | −25 | | 47 | 4834 | 4672 | −162 |
| 33 | 5450 | 5382 | −68 | | 48 | 4361 | 4349 | −12 |
| 34 | 5011 | 4957 | −54 | | 49 | 5415 | 5395 | −20 |
| 35 | 5313 | 5283 | −30 | | 50 | 5544 | 5498 | −46 |
| 36 | 4683 | 4653 | −30 | | 51 | 5820 | 5797 | −23 |
| 37 | 4630 | 4603 | −27 | | 52 | 6492 | 6475 | −17 |
| 38 | 6255 | 6218 | −37 | | 53 | 7453 | 7444 | −9 |
| 39 | 4771 | 4747 | −24 | | 54 | 5822 | 5625 | −197 |
| 40 | 6684 | 6635 | −49 | | 55 | 4599 | 4559 | −40 |
| 41 | 4987 | 4895 | −92 | | 56 | 5919 | 5646 | −273 |
| 42 | 4831 | 4808 | −23 | | 57 | 5101 | 5078 | −23 |
| 43 | 4746 | 4714 | −32 | | 58 | 5481 | 5466 | −15 |
| 44 | 5061 | 4908 | −153 | | 59 | 7998 | 7966 | −32 |
| 45 | 5518 | 5447 | −71 | | 60 | 6200 | 6266 | +66 |

**Total (wc -w): 164,699 → 163,083, −1,616.** ch60 rises because of the coordinator-directed
continuity fix (§5).

**The three named stretches (brief: 700–1,100 words in all): −949.**
- ch44–47: −480 (ch44 −153, ch45 −71, ch46 −94, ch47 −162).
- ch54:164–312: −196 (one further word earlier in the chapter).
- ch56: −273.

What went, by stretch (duplicate explanation only; no event, scene or beat was removed):
- **ch44** — the "Winning had become a form… one door shorter and no wider" paragraph and two
  restating sentences before it; Havel's "The six sheets held what the registers could not answer.
  This, they could."; his sitting on at the window; Withrow's squared pile.
- **ch45** — Ephram's "did not ask…" gloss recast; the squared plate and "gave no sign"; "He looked
  at *she knows* for a moment and left it."
- **ch46** — "*That is how the honest ones do it*…" (the same thought lands once, at ch49:215);
  "Hiding had turned into waiting…"; the gloss on what Ephram had decided.
- **ch47** — the oilcloth-and-contents-leaf restatement at the boxes (it is in ch46); the sentence
  re-listing what Bracken had read all year; "Not one of them said so. He did not say so either.";
  "He did not think any of them had decided it…"; "Neither of them looked at it again…".
- **ch54** — the simile on the clerk's double entry; Brom's "looks at a hurt" callback; the
  paragraph interpreting Withrow's face; "she was the last out of the yard" (said at :210);
  the re-explanation of why Ephram is not told (priced in full at ch53:113); two short connectives.
- **ch56** — three explanatory callbacks: Cael's paragraph explaining Lira's note-taking (her own
  scene explains it at :49–51); the gloss on Withrow's "All four"; the gloss on Rooke's "Doors open
  both ways". Plus four short backward references (the head groom's escort, the four riders at the
  gate, the wool press, the coats' year). Every departure image stands: Lira's last class, the key
  on the red book, Seln at the copying table and the stove, Brom's pack and the two papers on his
  table, the three boxes carried one at a time, the district officer, Ephram walking beside the
  third box, the lodge book, Withrow in the arch, Rooke, the lamp, the watchers, the ferry, the Log.

## 3. Scene endings broken (current chapter:line)

The machine: object placed → stillness → interpretive sentence → aphorism. Each now lands on a task,
a movement, a spoken line or a concrete unanswered fact.

1. **ch33:195** — was "Lira sat in the chair for a long while…"; ends on Rooke's "He went."
2. **ch41:211** — was "Nobody had decided anything… It had only been said."; now "Nothing had been
   decided. Karis's pencil went on down the first slip."
3. **ch44:77** (brief's :69–79) — the rule's quarter-turn (kept, it is the counsel's) no longer runs
   on into "Winning had become a form. That was the size of it."; the beat ends on *None, Advocate*
   and the clerk's "Received and entered."
4. **ch44:209** — Havel's scene ended on him sitting at the window until the lantern went out; it
   ends on the kit buckled.
5. **ch45:79** — ended on a squared plate and "if he saw the hand he gave no sign of it"; ends on the
   last plate hung.
6. **ch45:225** (brief's :227) — the priced leaf no longer closes on "He looked at *she knows* for a
   moment and left it."
7. **ch46:245** — ended on what Cael did and did not know about Ephram's two lines; ends on the
   green-taped file going down the corridor.
8. **ch47:157** — ended "Neither of them looked at it again, and both of them knew exactly where it
   was."; ends on the envelope in the last light.
9. **ch47:221** (brief's :179–221) — ended "Not one of them said so. / He did not say so either.";
   ends "He passed Karis the bread."
10. **ch59:163** — ended "He could not have said why that seemed better."; ends "Cael left the board
    face up."

Smaller breaks of the same machine inside a scene: ch50:207, ch54:216–220, ch57:121 (the maxim "A
thing left where it lay was sometimes all the mark a man could make" is gone; the image stays).

## 4. OWNER-DECISIONS #47 — the ch49 join

Re-read in context (ch49:199–215). The coordinator's sentence stands word for word. One change beside
it: the next sentence began "He sat with his case straight…", and after "…only Gault's title to put it
under" the pronoun could be heard as the Archmarshal; it now reads "**Gault** sat with his case
straight on his knees…" (ch49:209). The protected minute at ch49:201 is untouched. I also dropped the
tic "That was the whole of it." at ch49:213 and recast "Cael found that it was enough" to "It was
enough, and that surprised him."

## 5. Coordinator-directed continuity fix (Seln's case)

The protected closing exchange says the records are "in a case under that canvas". The case rode in
Seln's post satchel all the way east and nothing moved it. Fixed in unprotected prose, in Brom's
reload at the shelf.

**ch60:165 — added (two sentences, three words of speech), after "Brom put the second box on top.":**

> Seln had got up from the fire, and he took the surveyor's case out of his post satchel, where it had ridden against his hip since Halcenvane, and held it out across the tailboard. "With the boxes," he said, and Brom set it in beside the third, and drew the canvas down over case and boxes together when the load was done.

**ch60:219 — before:**
> The man it came from had been told, and he was asleep under a pine with a satchel for a pillow.

**after:**
> The man it came from had been told, and he sat across the fire with his cup in his hands and an empty satchel at his feet.

**ch60:227 — before:**
> And it did not say what was in the satchel. It said nothing about a case, …

**after:**
> And it did not say what lay under the canvas with the three boxes. It said nothing about a case, …

Checked ch58–60 for anything else that contradicts the new state: none. Before the shelf the case is
still in the satchel (ch57:115, :133–135; ch58:217; ch59:87, :327). After it, ch60:363 ("with the
satchel under his head") still reads true. The closing exchange, the inventory and every other
protected run are untouched.

Brom's Velmere envelope: no line east of Ostrand mentions it. It stays on his table (ch56:147–165).

## 6. Checks

- **Protected text.** All 51 patterns in `protected-patterns.txt`: per-chapter match counts identical
  to the baseline for ch31–60 (0 mismatches; 33 patterns occur in this range). Every italic span and
  every fenced notice in ch31–60 is byte-identical to the baseline except two that were narration, not
  record, and were cut on purpose (ch45 "*she knows*" as a narrated mention; ch46 "*That is how the
  honest ones do it*"). No notice, form, minute, letter, slate, Log entry or quoted callback changed.
- **Overlap** (`ed.sh overlap`, 8-word): M5 0, M6 0, M7 0, M8 0, M9 0 unprotected.
- **Gates** (`ed.sh gates`): reader_standard 0, metadata 0, modern 0 for every chapter in M5–M9.
- **Probe** (`sweep_probe.sh … 5 9`), skeleton / close, baseline → now: M5 1/11 → 1/10; M6 2/14 →
  1/14; M7 1/16 → 1/15; M8 1/11 → 1/11; M9 3/15 → 3/15. No movement and no chapter rose.
- **Metrics** (`formula_metrics.py`), ch31–60: sentence mean 13.63 → **13.60**; ≥40-word share 3.9% →
  **3.8%**; words per scene 949.8 → **940.5**; 143 scene breaks before and after (scene order
  unchanged). By movement now: M5 13.38 / 4.5% / 966 (shared with Lane A); M6 13.57 / 3.9% / 972;
  M7 13.50 / 4.4% / 905; M8 13.98 / 3.3% / 942; M9 13.75 / 3.3% / 943. All inside the brief's limits.
- Calendar, counts, ranks, standings, distances, names: no figure, day, date or title was edited.
  No season name, month order, English weekday name or metric unit was introduced. No new named
  character.

## 7. For the coordinator

### 7.1 Two targets overshot — ruling wanted, or simply note

- **Priority 1: −104 (square −39, flat −65) against "about 55".** Roughly half of the extra is the
  word "flat" on hands laid on tables, cloths, wallets and box lids by Cael, Karis, Lira, Withrow and
  Vastin, which recurred several times a chapter in M6–M8; the rest is literal but repeated use
  ("squared sheet" five times in ch33, "flat patch of crown" three times in ch31, "flat knot"). Every
  KEEP motif is intact: Seln's flat hands and squared leaves, Bracken's squared forms and square
  capitals, Brom's squared loads and recounts, Gault's straight case and square hand, Rooke's square
  capitals, flat-hand and "low and flat" fight technique, floor and stone geometry.
- **Priority 2: −120 against "60–70".** Most of the excess is the bare modifier "for a moment / for a
  while / for some time" removed from a sentence whose beat stays, and "Nobody said anything" removed
  where the next line already shows the room. Kept on purpose: the long silences in the reading room
  (ch35:179–185), the borrowed office (ch40:185–193) and after the limit (ch39:145); every
  consent boundary (not asking Brom, ch47:143–145; Seln's terms, ch37:198–202; Ephram asking,
  ch52:303; "I'm not asking" in Ephram's, Withrow's and the assistant's mouths); Seln's, Havel's,
  Ilsev's and Vastin's chosen not-looking.

If either is more than was wanted, the baseline makes any single change easy to restore; I would not
restore the ch44–47 and ch54–57 ones.

### 7.2 A continuity conflict found and fixed in passing (ch60)

ch60:217 (old numbering) had Seln "asleep under a pine" during Cael's first watch, but ch60:327 says
"He had not yet lain down. He was sitting by the fire with his coat round him and his cup in his
hands", and he lies down only at ch60:363. The satchel line had to change anyway (§5), so I made it
agree with :327 — he is awake, across the fire, cup in hand. Say if you want "asleep" back; then
ch60:327 needs the ruling instead.

### 7.3 Found, not changed

- **ch60:177** — the purse "pooled … in a parlour in Ostrand" lists Seln's wallet, but Seln was not in
  the Ostrand parlour (he joined at the crossroads, ch58:215). The sentence can be read as his share
  joining later ("and nobody had remarked on it then"), so I left it. One word would settle it.
- **ch52:163** — "with her pale fingers flat on the cloth" sits between two lines of the protected
  boxes exchange. Narration, not protected, but I left it rather than edit inside the exchange.
- **ch60:345–355** — the narration between the lines of the closing exchange: left untouched for the
  same reason.
- **M5 ≥40-word share is 4.5%**, on the limit, before and after; it is shared with Lane A's ch28–30.

### 7.4 Declined

- **ch40:329** (the Archmarshal's "hardest thing he did that week…") and **ch48:63** ("An honest man
  had only to stand up and ask") are aphoristic closes, but each is the argument of its chapter and
  neither sits in a named stretch. Left.
- **ch60:261–275**, the two poles side by side: left whole. It is the book's thesis, and both lines
  are protected.
- **ch57 and ch59** long metre and length: no meter repair, per the brief.
- No pause, silence or simile was changed inside any Log entry, letter, form or notice.
