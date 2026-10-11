# REPAIR REPORT r1 — Book 7, Movement 7 (chapters 45–52)

Author seat: `claude-opus-5-5` (Claude Opus 5.5), same-author repair, 2026-10-11.
Brief: `REPAIR-BRIEF.md`. Baseline for every "before" reference: `state/movement-007/pre-repair-r1/`.
Method: nothing under `books/` or `v3-runs/` was opened; no git command was run. I also left
`plan-audit.md` and `source-tracking.md` unopened, since either may quote the source; I worked from
the brief, `audit-notes.md`, `review-cold.md` and `review-editorial.md`. Every change was composed
by reading and placed as a single exact replacement; no rule-based splitting or joining was used.
Chapter 45 is untouched.

References are `chapter:line`; **b** = baseline, **n** = now.

## Result

| | words (tool) | words (`wc`) | net vs baseline | mean | ≥40 | para mean | scenes | words/scene |
|---|---|---|---|---|---|---|---|---|
| ch45 | 4,394 | 4,403 | 0 | 14.08 | 3.5% | 40.3 | 5 | 879 |
| ch46 | 6,223 | 6,237 | −8 | 13.98 | 4.0% | 37.3 | 7 | 889 |
| ch47 | 4,439 | 4,448 | +1 | 13.62 | 4.3% | 37.3 | 5 | 888 |
| ch48 | 4,693 | 4,703 | +30 | 13.64 | 4.4% | 33.8 | 5 | 939 |
| ch49 | 4,875 | 4,885 | −261 | 13.66 | 3.4% | 32.7 | 5 | 975 |
| ch50 | 5,311 | 5,324 | −345 | 14.12 | 3.7% | 37.4 | 6 | 885 |
| ch51 | 6,533 | 6,544 | −285 | 13.87 | 4.0% | 35.3 | 7 | 933 |
| ch52 | 5,880 | 5,895 | +179 | 13.77 | 4.4% | 32.9 | 6 | 980 |
| **movement** | **42,348** | **42,439** | **−689** | **13.85** | **4.0%** | **35.6** | **46** | **921** |

Every chapter holds the three ranges (mean 13.3–14.2; ≥40-word share ≤ 4.5%; 850–1,050 words per
scene). Movement: 3,058 sentences, median 10, ≤5 words 25.8%, paragraph median 25, FK grade 3.46,
Flesch 94.9. Secondary POV: Seln's window 2,029 words, Teague's 2,103.

**Gates** (`ed.sh gates book-07-void-roads 7`): reader_standard 0, metadata 0, modern 0 on all
eight chapters.
**Overlap** (`ed.sh overlap book-07-void-roads 7`): 0 unprotected shared runs of 8 words or more;
34 protected runs (allowed).
**Protected units:** each of the restored units stands once and whole (45:195 "Nothing else ever.";
46:109 "Take it." and 46:111 the council speech; 48:13 Oryn's yes, 48:27, 48:29; 49:267 the bolt;
50:219 Shadow with no ordinal; 52:295 the line between the courses; 52:299; 52:311; 52:223 the
bearing; 52:357–359 the closing log). No `[[` marker remains. No wall-groove wording remains in
chapter 52 (the only "groove" left in the movement is the channel of a crossbow, chapters 48–51).

## The coordinator's ten fixes — joins only

None was undone. Two joins needed text of mine to make the restored words true on the page:

- **ch48, the road (b9–21 → n9–23).** Oryn's restored line says "the same day as the lean-to and a
  different question". My draft had him ask the same question twice. Now Cael asks "A different
  question?" (n17) and she answers in her own terms (n19): at the bench he asked the healer, at her
  own table, with a line at the door; here he is asking "a woman on a rock", who can say yes. Her
  reason for offering follows (n21–23). The scene runs unbroken from the rock to the count.
- **ch47 (b105 → n105; b123 → n123).** So that the lean-to request is plainly the other question,
  he now asks "whether I may read you, here, when the bench is done", and the log reads "Asked
  her, at her own bench, whether I might read her." Two sentences, no new event.
- **ch48, the count (b33–57 → n35–59).** The restored staging gives him one hand on her wrist, so
  the short reading is now done with the right hand alone: "turned toward his hand" (n35), "back
  under his palm almost before he had counted" (n39), "took his hand away" (n45, n53). The long
  reading keeps the second hand, at the back of the neck, as she orders it (n81).
- ch45, ch46, ch49:267, ch50:219: the joins read cleanly as placed; no edit.

## A. Three tracked passages in ch52 — chains broken

1. **Scene 2, the air at the twentieth step (b63–75 → n61–83).** Re-entered on the bolt on the
   thirty-first step (n61), which Lira takes up as she passes (n63–65: "That's twelve."). The two
   lamps come next (n67). Brom notices a flame behaving wrongly before any step is named (n69:
   "Your flame's wrong"); Karis holds hers up (n75); only then does Seln give the step (n77: "Since
   the twentieth… The air stops there"). The cold and the missing smells wait until all six are
   inside, and they are Oryn's (n83: "It's colder than the frost up there… And it smells of
   nothing. A cellar smells of earth, and a well of water."). The list of four absent smells is
   gone; she names two and turns to sick-rooms.
2. **Scene 2, the catalogue (b77–83 → n87–93).** The sentence that announced a proper catalogue and
   set it against the day before is gone. The chamber now opens on a measurement (n87: Cael paces
   ten strides each way, and that part of his count holds) and on a discrepancy (n87–89: he had
   called the roof a foot above Brom's head; Brom's palm lies on it with the elbow bent: "A hand…
   I wasn't standing up straight."). What the day before prevented is said only after that (n91).
   The dust, the five courses (the coordinator's wording, n93) and the Oryn/Karis exchange (n105
   "What are they", n109 "Lines,") are kept.
3. **Scene 3, the kit (b117–129 → n127–139).** The order is turned round. The scene begins on the
   cord already run out toward the eastern wall and stopped half way (n127–129: "Somebody had been
   measuring from the middle of that room to its wall, and had got half way."). Brom names the
   tools as he comes to them (n131); Karis says what each is for (n133: "a kit for one thing").
   The open case is named after them (n135); and Seln reads the order last, in one speech (n137:
   "They lie in the order that they came out… Nobody packs so. He meant to take them up again.").
   "It was a case. He had taken it…" and the packing-versus-working explanation are gone.

## B. ch52 — the design confirmed once

- The confirmation stays where it is earned, at the end of the pacing (n53–57), with Lira's reply
  and Karis's answer shortened (b57–59 → n55–57).
- The surveyor's eight identical distances are no longer greeted as a second proof. "The same," /
  "The same, eight times…" (b187–189) is replaced by the new finding that they carry (n197–203;
  see D).
- The radius line in the ledger is read and written down without a reaction beat (b193–195 →
  n205–209).
- The six hours at the walls: Cael's writing arm and the slips are told once (b253 → n269); the
  count of grains loses its recapitulation (b263 → n279).
- Seln's doubt and Karis's lead-in to the ruler line are shortened (b289 → n305; b295 → n311); the
  protected line itself is untouched (n311).
- The log line "*Karis has the round, and it is the Fallow's. Twenty-nine sheets.*" (b353), which
  summed what two scenes had shown, is cut. The protected closing log is untouched.
- Kept whole: the field method of the pacing, the forty-one kinds, the line between the courses,
  the bearing reveal and Karis's refusal to draw it by lamplight.

## C. The set piece told once (ch49–51)

No exchange, rule, fragment use or bill was cut. The night log of the 114th stands whole with its
nine lines and its sum (51:193–217). Removed:

- **ch49.** "Nothing had changed in that low ground…" (b8–9, a position re-described); "Wind lay
  in his feet the whole way, asking…" (b149–150, said already at 49:107–119); the second half of
  the *Twenty.* air line (b185 → n179); the room's smell and silence, which chapter 52 now carries
  (b199–201 → n193); the closing sum of injuries, replaced by one sentence (b315 → n307). Seln's
  count of the rim says the new thing only (b103 → n99: "Six, and four bows… I walked past every
  one of those places twice."). The first two scenes are joined (b40 break removed), since the
  second began where the first stood.
- **ch50.** The opening re-anchor of the square and of Lira's post (b5–7 → n5–7); Lira's
  explanation of why the bolt stays in the bow, which the gate-walk and chapter 51 both carry
  (b55–59 → n55–59); the bread (b73 → n73); Oryn's two fingers and what she learned at the other
  floor (b83–85 → n83–85); the cold (b87 → n87); Karis and the wall at her back (b95–103 →
  n95–99); Seln's reading of the trap, where a narrated summary came before the same thing in his
  mouth (b109–121 → n105–107; 254 words to 134); "They turned toward him in the dark" (b162); the
  restated consequence in the design talk (b173 → n157).
- **ch51.** "He could not feel it." before "dead to the elbow" (b7 → n7); the repeated pricing of
  the one bolt (b19 → n19); the run (b35 → n35); the stillness explained twice (b67 → n67); the
  forearm told again in the bill (b159 → n159); Seln's knots, and what the rim saw, where a
  preamble and a recapitulation stood either side of the account (b169–177 → n169–173; 279 words
  to 198); the crossbow described (b183 → n179); Teague's silence narrated (b251 → n247).

**Words.** By word diff against the baseline, 1,887 baseline words are gone from chapters 49–52
and 1,175 are new, a net of −712 (movement −689 with the ch46–48 edits). Most of the new words are
the re-entered scenes that item A required in chapter 52 (771 out, 950 in there) and the supports
for D and for the restored units. Chapters 49–51 alone: 1,116 out, 225 in, net −891.

## D. The closing log's date

The protected log (52:357–359) is untouched. The scene before it now carries the observation that
lets "five years" stand, and keeps the newer mark a separate thing:

- **n197** Karis: the ledger's eight stations are the old irons; "There was a bar at each of those
  eight points this morning, scaled as the old one at the stone is scaled."
- **n199** Seln: "Then this is the book of whoever drove them. I put five cold terms on the old
  iron at the stone, and I see no cause to alter that for his book."
- **n201–203** Lira points at the bar in the kit, which carries the newer one's mark. Seln: "So
  that mark lay in this man's case five cold terms ago, and somebody set the same on a bar at our
  stone a good deal later. Those are two visits, and I can tell you no more of them… I shall not
  put a date on them either."
- **n143** Lira at the bar: "And it's got the mark that the newer one has."

Nobody decodes the index or the stroke-and-bar, and nobody says what the second visit was.

## E. Register (reflective prose only)

- **Seln's window, ch46 (b267–317 → n267–329).** Six over-long paragraphs broken at real turns
  (the dictation heard in the clerk's line; the paper against the names; the hand against the four
  who came home; the lure; the thumb on the scale; the south road). Related simple statements
  joined (n273, n291, n305, n323); "a lure that is taken must be met" for "something had to be
  done about a lure"; "Seln found that…" removed (n307). No fact changed; #50 stands as it did
  (the case a twelve-year matter, no sum with "six").
- **The design talk, ch50 (n145–199).** Left nearly as it was: "state the whole of the question"
  (n145); the cut noted under C (n157); one exact word (n199). Elsewhere in the chapter eight
  semicolon joins were returned to two sentences each (n7, n11, n29, n33, n145, n215, n235, n251)
  to bring the mean back inside the range after the cuts: 14.44 → 14.12.
- **Teague's window, ch51 (b283–379 → n279–379).** The paper reasoning told once (b283 → n279);
  "He had not said how late, and he saw that now:" joined and the hour set off (n315–317); "he
  found that the rule held" → "the rule held" (n293); his piece at the stone shortened (b355–357 →
  n353); the bow's line (n365); the rank paragraph broken at "So he knew a little…" and its four
  short statements joined (n369–371); the last paragraph broken at "But a crew that has been shot
  at…" (n377–379).
- **The research sequence, ch52.** "It was there, as it was every time." (n255); Karis's start at
  the word *bearing* broken at the turn (n227–229); "the ones which the second floor had shown her
  to be no kind at all" (n273).
- The Stair's action (49 scene 1 from the bolt onward, 50:215 to the end, 51 scenes 1–2) had no
  register edits beyond the three full stops in chapter 50 noted above (n215, n235, n251); the cuts
  made there are listed under C.

## Supports added for the restored unit in ch52

- **n251** Karis twice leaves the paper and walks the foot of a wall with the short cord, counting,
  so that "I've paced the spacing because I pace things" has something behind it.
- **n291** "She had been over the Fallow's eleven strips for four days at a trestle in a barn",
  so that "I looked for it for four days" is plain.
- **n297** "She sat back on her heel, with the pencil still on the paper." replaces "She had gone
  quite still with the sheet in her hand", which belonged to the groove staging.
- **n287** the forty-one are now "in the courses here", so that the line between the courses
  stands outside the count, as the unit has it.
- **Scene 6 (b327–345 → n343–351).** The bolt count in dialogue is replaced by narration: the boy
  lays the shafts in a row by the four bows, Lira adds hers, and an iron head with no shaft lies by
  the stone. Brom tries a shaft "along the stock of the healer's bow, where it stood proud of its
  channel". The figure thirteen stays in the night log (51:193).

## Declined, and flags for a ruling

1. **Length.** The movement stands at 42,348 by the tool against "roughly 41,000–42,000". Gross
   removal is inside the 1,200–2,000 aim (1,887), but item A's re-entries and the supports for D
   and for the restored units put 1,175 back. I read chapters 49–51 through once more after the
   last cut and found nothing further said twice; another 350 would have had to come out of the
   Stair's action, which the ruling forbids.
2. **"Two hundred and twenty yards… on the wall" (52:295).** The restored unit has the line recur
   "every ten cords and a piece… on the wall, at the perimeter's radius", in a room ten strides
   square. I have not glossed how a spacing of two hundred and twenty yards is read off four walls
   of that size (a scale, a count along the courses, or a figure cut beside the line). The pages
   round it say only that she paced and counted and wrote a figure where nobody could see it. If
   the map means something particular, one clause at n251 would carry it.
3. **The roof.** In my draft the chamber's height was loose. It is now fixed by a correction on
   the page: called "a foot above Brom's head" on the 114th (49:193), found to be a hand above it
   on the 115th (52:87–89).
4. **"A different question" (48:13–19; 47:105, 47:123).** My reading of the restored words is
   given above: the healer asked at her table, the woman asked on a rock. If the source's
   difference was another one (the short reading against the long, say), n19 is the one paragraph
   to change.
5. **Not done:** I did not re-run the sweep probe (the brief allows it once, and it was used). I
   did not alter `EVENT-LIST.md`, the packets, the map, the ledger or `protected-patterns.txt`.
   `AUTHOR-REPORT.md` is updated: the status lines, the chapter and formula tables, "New canon
   minted" and "State at movement end". Its line references in the fragment and protected-unit
   tables predate the repair and are marked so there; the current lines of the units are listed
   under "Result" above.
