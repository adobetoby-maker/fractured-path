# Book 6 — completion pass, Step 3: same-author texture pass (from the whole-arc read)

**Source.** `whole-arc-read.md` (Sol, a straight read of ch1–60), §§3, 4 and 9.

The book holds as one arc and lands its argument. The read checked and found holding: the calendar
day by day; the lane bill, renewals, Anchor distances, fragment count, the clean door, "twice more",
Hesk's clock; titles and offices; every quoted callback; names, bodies, objects; both seams;
knowledge boundaries and reserved truths; all protected text; the Reader Standard; rhythm. Source
distance in Movements 1–4: no unprotected source-shaped passage. **No rebuild. No new material.**

**Already applied by the coordinator (do not redo):** one sentence in ch49 after "he had declined
nothing in his life" (OWNER-DECISIONS #47: the protected minute's "evaluator of record" is the
form's own mislabel and stays verbatim). Lane B: re-read it in context and smooth the join if needed.

The pass runs in two lanes, **Lane A ch1–30** and **Lane B ch31–60**. Each lane edits only its own
chapters. Do not open any file under `books/` (the source edition).

## Both lanes — Priority 1: thin the shared object-and-pose vocabulary (§3 items 2, 3, 10)

One reading pass, sentence by sentence, never by script. The problem is not any one image; it is
the same small physical vocabulary doing emotional work for nearly everyone.

- **Square / squared / squaring** (A 98, B 101) and **flat** (A 73, B 127). Papers, files, cases
  and piles are squared to edges with near-ritual frequency; "flat" supplies voice, pose and
  surface. **Lane A: revise or remove about 45 generic uses. Lane B: about 55**, concentrated in
  ch41–47 and ch55–57. Replace with action specific to the object in hand, or drop the gesture and
  let the spoken line stand.
- **Quarter-turns** (A 10, B 18). It began as the counsel's rule and Seln's cup. Keep it for those
  two; everyone else finds another movement or none.
- **KEEP:** literal geometry; `flat hand` and quarter-angle fight technique; Bracken's square
  capitals, clocks and glasses; Seln's cup, case and exact office hand; Gault's straight case;
  Hesk's losing clock; Brom's pockets, loads and first-count-right recounts.

## Both lanes — Priority 2: stop declaring every pause, silence and withheld question (§3 items 1, 4, 5, 7)

Pools: pause phrases "for a moment / a while / some time" (A 78, B 104); "did not look / without
looking" (A 81, B 90); "said nothing / nobody said / no one answered" (A 66, B 76); "did not ask /
nobody asked" (A 37, B 32).

- **Lane A: recast or cut 50–60 combined**, with special attention to ch7, ch19 and ch23–25.
- **Lane B: recast or cut 60–70 combined**, especially ch34, ch41–49 and ch54–57.
- Use one of three alternatives: end on the object or the line without explaining the room; give
  the next character a concrete task; or let a short spoken reply replace the narrated silence.
- **KEEP** the plot-bearing consent boundaries (the decision not to ask Brom; Seln's terms for
  Shadow; Ephram explicitly asking for the bout) and silence that is a named character's own
  language rather than scene punctuation.

## Both lanes — Priority 3: vary the scene-ending machine; take out duplicate explanation, not event (§3 items 6, 8, 9; §4)

The machine: object placed or quarter-turned → collective stillness → a `not X but Y` or
"the way he/she…" interpretive sentence → a plain aphoristic close. Also thin the
"like a man / a person who…" explanatory simile where it explains a feeling rather than shows a
movement, and the tics "That was all." / "That was the whole of it." (A 5, B 10) and
"He found that…" (A 6, B 20).

- **Lane A:** break **six to eight** such endings, and remove **500–700 words** of re-briefing in
  **ch23–25** (the approach re-explains sealed lines, ladders, files and what a public floor proves
  after those ideas are secure: ch23:41–123, :171–209; ch24:193–233; ch25:19–77). Keep the
  confluence bout, the production order, every required file beat and `Again. Faster.`
- **Lane B:** break **eight to ten** endings, and remove **700–1,100 words** in all from:
  - **ch44–47**, where four chapters stage alike (paper or rule placed, room silent, a sentence
    saying what the silence means: ch44:69–79, :177–179, :237; ch45:227; ch46:253–259; ch47:179–221);
  - **ch54:164–312**, where the bout ends and then ending follows ending (Gault, the crowd, Withrow
    leaving, the Current girl, the handshake and speech, the Log, the ninth's reading, Bracken's
    forms, the good-room callback). Keep every beat's fact, the protected notice, speech and Log
    entry; shorten the connective reaction around them;
  - **ch56**, the procession of exits after ch55's four leaves. Two or three explanatory callbacks
    can go; every departure image stays.
- Alternative endings land on a changed task, a movement in space, an unanswered concrete fact or
  an immediate consequence. Not another maxim. **Do not change scene order. Add no new material.**
- OWNER-DECISIONS #45 stands: Movements 5–9 are fuller by ruling. Cut duplicate explanation only;
  the road cut (ch30–32), the case (ch35–40), ch41–43, ch48–53 and the M9 departures keep their room.
- ch57 and ch14 run long in sentence and paragraph by design. No meter repair.

Expect to lose about 1,500–2,500 words across the book.

## Both lanes

**Method.** By reading, in place, never by script. If a sentence is good and its repeat is the
problem, change the weaker instance.

**Protect:**
- every BOOK_MAP §8 Tier A and Tier B unit and every pattern in `protected-patterns.txt`
  (the whole-arc read §5 lists each with chapter:line);
- both FRAGMENT ACQUIRED notices and every other notice, form, minute, letter and Log entry;
- every count, day, date, interval, distance, rank and standing; the lane bill (ten/ten/twelve);
  "two renewals on paper" and the protected first pole's "a stamp renewed four times" (ch7, ch60);
- every line quoted back later in the book (whole-arc read §1, "Quotations");
- Gault = evaluator of record; the Archmarshal's office = the certifying office; `Caelen Hesk-ward`;
- season-blind: no season names, no month order, no English weekday names; feet and yards only;
- Bede, Maud, Gwen and Abbot as written (owner-pending placeholders); no new named characters;
- the Reader Standard (a 13-year-old reader), the Monroe 1.3 voice and the O'Connor controls.

**Count.** Count each Priority 1–3 target before and after, with grep, within your range, and
report both. Your untouched baseline is `state/completion/pre-lanes/` (use `diff`, never git).

**After:**
- From editions/monroe-1.3: `bash tools/ed.sh overlap book-06-the-compacts-hand N` stays at 0
  unprotected for every movement in your range, and `bash tools/ed.sh gates book-06-the-compacts-hand N`
  stays at 0. Movements: M1 ch1–7, M2 8–13, M3 14–20, M4 21–27, M5 28–34, M6 35–40, M7 41–47,
  M8 48–54, M9 55–60. Lane A is movements 1–5 (ch28–30 only in M5); Lane B is movements 5–9
  (ch31–34 only in M5).
- From the worktree root: `bash editions/monroe-1.3/tools/sweep_probe.sh book-06-the-compacts-hand F L`
  does not rise.
- Run `python3 editions/monroe-1.3/tools/formula_metrics.py` on your range. Hold the mean ≥ 13.3,
  ≥40w ≤ 4.5%, and 850–1,050 words per scene.
- Write `LANE-A-REPORT.md` or `LANE-B-REPORT.md` in this folder: counts before/after per target,
  words before/after per chapter, the endings you broke (chapter:line), anything you declined
  and why, and anything you found that needs a coordinator ruling.
- No git commands of any kind.
