# Recheck r1 — Book 3, Movement 3 (chapters 17–23)

Review seat: Claude Fable 5.1 (targeted recheck of Repair r1; author Claude Opus 5.5). Date: 2026-10-01.
Scope: the REPAIR-BRIEF items and every changed region (diff of `manuscript/chapter-17..23.md` against `pre-repair/`), read with context. Not a fresh review. No manuscript file was modified.

## Verdict: CLOSE WITH LINE FIXES

Every brief item is resolved or honestly flagged by the author. The Glass rule is stated once in ch18 and every exchange in ch19, the rebuild in ch21 and the rail in ch22 obey it. The calendar holds the coordinator's week-8 ruling at every day and week marker I could find. The repair introduced three small defects (one continuity slip, two speaker-attribution joins) and left one clause of the rule imprecise; all four are single-line fixes. No second repair is warranted.

Independent checks: `ed.sh overlap book-03-no-path-given 3` → 0 unprotected, 1 protected (allowed). `ed.sh gates` → 0 on all seven files. `formula_metrics.py` on the seven chapters reproduces the author's figures exactly (mean 13.33, ≥40-word 3.9%, 971 words/scene, 33,974 tool words; `wc` 34,052). "directed" occurs once in the whole manuscript, in the protected ch23 log, which matches BOOK_MAP §9.2 to the character.

---

## (a) Brief items

### Priority 1 — Calendar and attribution

| Item | Status | Location / evidence |
|---|---|---|
| "three weeks ago" (ch18) | RESOLVED | ch18 ~l.143 Karis: "I fought him, not a week ago." Bout W6D1; Karis speaks evening of study day 3 (W6D6) → 5 days. |
| "three weeks ago" (ch19) | RESOLVED | ch19 ~l.173 Lira: "nine points on that boy not a fortnight ago." Exhibition W7D4 → 10 days. |
| Ch21 session order / hypothesis in week 8 | RESOLVED | ch21 l.25 "on the first Tuesday after the exhibition"; chalk line, post permission, three cloths, read-back, felt, *Not asked* all inside that one Tuesday hour (l.29–93); l.137 "The next evening, Wednesday, Brom gave back volume six" → hypothesis. "second Tuesday" and "the Thursday" are gone. ch22 l.49 Thursday (clause four), Friday (lecture, rail, wall; Brom "Two days after Karis says it might be aimable"; "since Wednesday night"); ch23 Saturday; ch23 l.233 "*Week eight*". |
| Ch23 "a week on the board, two days ago" | RESOLVED | Withdrawal posted exhibition day W7D4; a week on the board → down W8D4; ch23 is W8D6 → "two days ago" agrees. |
| Lira's reassessment "nine days" → ~five | RESOLVED | ch23 l.169 "five days off" (→ W9D4, inside weeks 8–9); Gerda l.177 "Five days for her. Six for me." and l.197 "Six days." Both posted "three weeks ago" (l.165) honored. |
| "Hobb had said" → Wray | RESOLVED | ch19 l.55: "Wray had said behind Naveth's shut door that he always pressed with a crowd, and Hobb had said it at the rail before her" — matches ch17 and the editorial's ch15 citation. |
| Naveth "tonight Quenna will copy" vs Quenna "last night" | RESOLVED | ch20 l.175 unchanged; ch23 l.118 Quenna: "I copied it into the ledger the night of the bout; the fair copy took me longer than it should have." The sixth-bell doorway remark is cut. |
| Six vs nine points | RESOLVED | ch19 l.11 "six practice points on her second afternoon at Greyvane" (rotating seat's memory) vs l.173 "nine points on that boy" (standings bout). Two events, now unmistakably distinct. |
| Hesk's "back door" vs ch3 | RESOLVED | ch23 l.77: "had once stood beside a boy with a hand on his shoulder on the worst morning of his life" — aligned with ch3:31. No new Hesk fact. |
| Whether Lira "saw" the half push | RESOLVED | ch19 l.115 "had read in the binder what it cost him to catch half of a slow push and seen him the morning after, holding his shoulder"; ch23 l.45 "I've read what half a push costs, and I saw you the morning after." Lira reads the binder (ch18 l.279). Note: ch19 l.115 still opens "She had seen it wake on Brom's floor" — pre-existing, not flagged by either review, and defensible (Lira is in Brom's room in ch6; the road work "moved indoors with them"). Leave. |
| Non-use count | RESOLVED | ch18 l.255 "I've only done it once in my life when it counted, and that was half by surprise"; ch20 l.227 log "Third time I've chosen that, counting Brom's floor" = D1 + Brom's floor + D3. Agrees with the editorial's three-count. |

### Priority 2 — Glass rule and ch23 codas

| Item | Status | Location / evidence |
|---|---|---|
| One rule, stated once in ch18 | RESOLVED (one clause imprecise — line fix 1) | ch18 l.75–79: two at once, one per forearm; ready pair built slowly at the mark (shell left, edge right); each structure takes the whole mind; everything after the pair made fresh "after the last one had gone". Sliver paragraphs l.193–209 restate it for the listener ("not free until the last of the ready pair had gone"). The sentence "What he could not do was build a new one while another still stood" is absolute, and two sentences later he builds the second of the pair while the first stands (slowly, "like a man threading a needle"). The paragraph's real rule is mind-share + time; the absolute sentence needs one word (see fix 1). |
| Every exchange obeys it | RESOLVED | See (b). |
| Ch23 codas | RESOLVED | ch23 is 4,268 words (−328). Quenna's stair beat keeps only the new information (copied bout night; fair copy later; "You've read every other page… I didn't see why the academy's should be the exception"); Naveth's "dullest paragraph" is not repeated; the record restatement is one sentence. Brom's porridge and Karis's handwriting trimmed; the wall absorbs the accounts and the log without a break. Kept whole: Hesk's letter and bench, "glad of the third", Lira's shoulders ("came down by about an inch"), Gerda, Lira drilling, the reply to Hesk, the two closing binder lines. |

### Priority 3 — Rhythm

| Item | Status | Evidence |
|---|---|---|
| Three primaries into range | RESOLVED | Reproduced: mean 13.33 (13–15.5), ≥40-word 3.9% (2.5–4.5), 971 words/scene (850–1,050). Ch19 untouched except the arm clauses. |
| Progression vocabulary toward ~65/10k | PARTIAL (author-flagged) | ~29/10k by the author's proxy. Terms added where a speaker would use them (ch17 Quenna's no-rank/no-tier; "Iron Rank Two"; "Copper ranks… over the threshold into Iron"; ch22 "Four fragments, four tolls, and four names"). Forcing the rest into these quiet chapters would be decoration; the author's deferral to M4's null sessions is the right call. Not a defect. |
| Length 34,000–36,500 | RESOLVED | 34,052 (wc), at the floor but inside. |

---

## (b) The Glass rule, exchange by exchange

Rule as stated (ch18 l.77–79, l.201–209): at most two structures, one per forearm; Edran enters every sequence with a ready pair built at his mark (shell left, edge right); a structure takes the whole of a Glass fighter's mind, so after the pair is spent the next is made cold, with both forearms bare for a sliver; the sliver is in the Path, not in Edran.

| Exchange (ch19) | What the text shows | Obeys? |
|---|---|---|
| 1 (l.57–83) | Ready pair up before two steps, "built at his mark before Wray's hand ever fell"; kick with "nothing on the shin but cloth"; pair "stayed whole and unspent" through the questions; sixth strike spends the left shell on Cael's guard; "pressed him for the rest of the exchange with the edge alone, and did not spend it". The old "twice Edran ran a sequence of three" is gone (he cannot build cold while the edge stands). | Yes |
| 2, Lira POV (l.131–145, 171) | "a fresh pair built at his mark, shell up on the left and edge on the right"; shell driven short and "burst on empty air"; edge "the other half of the ready pair"; edge bursts on the right → "nothing on either of Edran's forearms"; third "made cold" on the right; graze. Karis's eyes "on Edran's right forearm". | Yes |
| 3 (l.217–247) | "The ready pair first, rebuilt at his mark between exchanges… Then the third, made cold. Then the fourth."; shell spent on Cael's guard; edge bursts, "Edran had to let it go to call the third"; "both of Edran's forearms were bare"; palm on the breastbone; the useless third is a shell "still on his right forearm". | Yes |
| 4 (l.277–295) | Pair up; shell spent, edge standing; left shoulder loads "while the second still stood"; explanation now ch18's ("a full structure needed the whole of a Glass fighter's mind, and nobody had a whole mind to spare while another structure still stood… had decided to pay for it"); third comes up thin "on the left arm, where no third had ever come before". The old "glitter on the forearm" sentence is gone. | Yes — new under the rule, not against it |
| ch18 drills (l.193–209) | Sets of four: pair spent one after the other, "The third did not come so fast", both forearms bare in the sliver, "always after the second, always before the third". | Yes |
| ch21 rebuild (l.9) | "calling the third structure on his free arm while the second still stood… thin and pale and late"; sequences of three. | Yes |
| ch22 rail (l.140) | Sliver "between the second structure and the third" in a third-year, "wider than Edran's by half". | Yes |

Beats, touches, rulings and speech: unchanged. The score (Cael 2, Edran 1), "A fourth." (l.253), Quenna's fourth-exchange ruling (l.263), the graze, the palm, the rib rake, Edran's withdrawal — all verbatim against pre-repair. Only arm/structure clauses moved.

Residual (not a violation): ch19 l.143, Lira's free indirect "the bare right forearm, where the third would have to come" asserts necessity for what is Edran's habit. Exchange 4 names the habit explicitly ("On the other arm"; "where no third had ever come before"), so a reader reconciles it within two pages. Optional softening to "where the third always came"; I do not require it.

---

## (c) The calendar, marker by marker

Week-day numbering assumes a seven-day week with the exhibition on W7D4; nothing below depends on which weekday D1 is.

| Marker | Text | Agrees? |
|---|---|---|
| Posting | ch17 "eight days"; ch16–17 W6 ~D3 | — |
| Study days | ch18 "The first three days taught him the Path"; archive "On the third day"; Karis on the wall same evening ("not a week ago" = 5 days after W6D1); Oona "the next morning"; seam found day 4; "On the fifth and sixth days he confirmed it"; Brom's floor "fifth night"; Lira "sixth night… Tomorrow's the seventh" | Yes |
| Exhibition | ch19 = eighth day from posting = W7D4; Lira "not a fortnight ago" (10 days) | Yes |
| After | ch20 Wray "Edran will be on my floor tomorrow morning"; night log moved before Karis's chart, which comes "the next evening" (W7D5) | Yes (see note 1) |
| ch21 | "the next morning" Edran rebuild; "The week turned, and on the first Tuesday after the exhibition" (W8D2); everything through *Not asked* in that hour; "The next evening, Wednesday" (W8D3) | Yes |
| Brom's column | "FROM THE DAY WRAY WROTE. DAYS 1–15… Seven today"; Wray "for a fortnight"; Karis "Fifteen days of it" | Yes to within a day (Wray wrote in ch16, W6D2–3; W8D3 is day 15 or 16). Inside BOOK_MAP §3's "a few days" latitude. |
| ch22 | "The Thursday session"; "felt from Tuesday"; "something wrong on Wednesday"; "The second day was worse" (Friday); Brom "Two days after Karis says it might be aimable… since Wednesday night"; "Lira had not asked him anything in two days… Wednesday night" | Yes |
| ch23 | "counted the days since Wednesday"; "carry this for two days"; Brom "Last night… Seven again yesterday"; Karis "slip for Tuesday's session"; petition "two days ago, after their week on the board"; Lira's line "went up three weeks ago… five days off"; Gerda "next morning… Six for me… Twice this week"; log "Week eight" | Yes |
| Reassessment | W9D4 (Lira), W9D5 (Gerda) — inside §3 weeks 8–9; nulls free to bind from week 9 | Yes |

Note 1 (pre-existing, not a repair defect): Wray says Edran will be on her floor "tomorrow morning" (W7D5); ch20 ends with Karis's chart "the next evening" (W7D5); ch21 opens "He went to watch Edran the next morning", which strictly reads as W7D6. The author's calendar treats ch21's opening as W7D5 with the chart as a forward coda. The wobble is one day, crosses no anchor, and existed in pre-repair in a worse form (the log read as chart-night). Leave.

---

## (d) Joins and new defects

Every changed region was read with context. Clean joins: ch17 crowd/Gerda merge (l.176–182), the Edran-at-the-standings-board reorder (l.195–199), the Edran/rail reorder (l.283–291); ch18 the rule paragraphs and the sliver sequence, the Brom wrist disentangling ("his own left wrist… His own wrist, the one he had misrouted" — two "his own"s in adjacent paragraphs but the subject is clear), Lira's sixth night; ch20 the Edran-walks-out paragraph, the log's new position, Karis's chart line; ch21 the Tuesday compression, the cloth sequence, the *Not asked* fold, the hypothesis-aftermath merges; ch22 the backward read, the Oona and rail scenes, the Brom/narrowed-thing merge; ch23 the wall merges, the Quenna compression, Lira at the calendar, Lira drilling. Protected lines verified verbatim: ch17 "Don't." / "I mean it. Don't tell me." (one "Don't tell me" in pre-repair too); ch18 "*Tires in the sequence, not the body.*"; ch19 "A fourth."; ch23 Hesk's "glad of the third", Lira's shoulders, Gerda, the log line. Orphans after the ch21 cuts and the ch23 coda cuts: none found (the rotating seat's written sentence, cut from ch23, is not referenced elsewhere; "Wray's twelve words" still counted in ch20).

Defects:

1. **ch21 l.35 — continuity (introduced by the repair).** New sentence: "His recovery between passes at the working speed had been three counts at the second sitting and was four now". Karis could not have timed anything at the second sitting: ch14 l.37 "Karis was waiting in the passage outside the hall… The sitting was closed". Her timings come from her own sessions (ch21 l.33, habitual). Fix 2 below.
2. **ch23 l.150 — speaker separated from line (introduced by the repair).** `"He mended the bench."` follows a paragraph whose subject is Lira ("she only nodded…") with its tag removed; a reader assigns it to Lira for two lines, and Lira has not read the letter. Fix 3.
3. **ch23 l.39 — speaker ambiguity (introduced by the repair).** `"You're not afraid of it." It was not quite a question.` follows Lira's speech and a narration paragraph with its tag removed; the line reads as Lira's until her answer arrives. Fix 4.
4. **ch18 l.79 — rule imprecision (brief P2).** "What he could not do was build a new one while another still stood" is contradicted by the ready pair two sentences later and by exchange 4. The paragraph's actual rule is that a *fast* full structure needs the whole mind. One word. Fix 1.

Not defects, noted for the ledger: Cael now signs a slip for each session (ch23 l.101) — a small new mechanism replacing the binder glance; consistent with clause one and with Quenna signing the strip after sessions. The Compression drop costs "none found yet". Edran "first for most of three years" (ch17 log, ch20) agrees with BOOK_MAP §3 (Karis takes first in week 5–6). ch21 l.254 "As a research question it was simple." now carries its contrast by juxtaposition only (the floor sentence); readable, Monroe-plain, left alone.

Reader Standard: gates 0; no modern slips found in the changed regions. Reveal limits: the hypothesis stays spoken, to Cael/Lira/Brom only; Karis's "directable" (pre-existing) is not "directed"; Quenna states nothing.

---

## (e) Second repair?

No. All Priority 1 items are resolved at the phrase level; Priority 2's rule is stated and obeyed, with one word to tighten; Priority 3 is inside range with one honestly deferred target. The four fixes below are the whole list; none touches a beat, a touch, a ruling or a line of speech.

## Line fixes (file; old text, exactly once; new text)

1. `manuscript/chapter-18.md`
   old: `What he could not do was build a new one while another still stood.`
   new: `What he could not do was build a new one quickly while another still stood.`

2. `manuscript/chapter-21.md`
   old: `had been three counts at the second sitting and was four now`
   new: `had been three counts at every session before the exhibition and was four now`

3. `manuscript/chapter-23.md`
   old: `"He mended the bench."`
   new: `"He mended the bench," Cael said.`

4. `manuscript/chapter-23.md`
   old: `"You're not afraid of it." It was not quite a question.`
   new: `"You're not afraid of it," he said. It was not quite a question.`

After applying: re-run `ed.sh overlap` (no change expected) and `ed.sh gates`; word count +6.
