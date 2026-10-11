# Book 7 — completion pass, Step 3: same-author texture pass (from the whole-arc read)

**Source.** `whole-arc-read.md` (Sol, a straight read of ch1–60), §§4, 5, 8 and 10.

Verdict: PASS — RATIFY. The book holds as a complete novel. Found holding: the calendar; the
deployment count and every fragment rule; money, the board, bolts and sheets; bodies; distances and
geography; quotations, names and both seams; knowledge boundaries and reserved truths; the consent
thread ("meets the Reader Standard without qualification"); every protected line; rhythm. Source
distance: no unprotected source-shaped passage anywhere. **No line fixes. No rebuild. No new
material. No scene is cut, moved or re-staged.**

The read's one recommendation is this pass: the book's hand, count and accounting motifs are right,
but its retrospective glosses, measured pauses and repeated looks make the surface more patterned
than the events need.

The pass runs in two lanes, **Lane A ch1–30** and **Lane B ch31–60**. Each lane edits only its own
chapters. Do not open any file under `books/` (the source edition) or `v3-runs/`.

## Priority 1 — thin retrospective interpretation (read §4 items 3, 4, 6)

The narration gives an image or a statement and then interprets it ("That was…", "…, which was…"),
or pulls a present action back through an earlier scene ("as Brom had on the ford", "as he had
done at the wall").
- Pools: "That was" A 156, B 181; "as [someone] had" A 104, B 158; "which was" A 46, B 69.
- **Lane A: revise or remove 35–45**, concentrating on ch15–22 and ch27–30.
- **Lane B: revise or remove 50–60**, concentrating on ch38–43 and ch54–60.
- Let the present object, the changed body or the spoken finding carry the meaning. Where a
  callback is needed, keep one concrete shared detail, not the earlier scene's interpretation.
- LEAVE: protected logs and lines; explicit injury clocks; comparisons the cause depends on.

## Priority 2 — vary the attention and pause choreography (§4 items 8, 9, 10)

- Pools: "at once" A 44, B 47; measured pauses ("for a moment / a while / some time", "after a
  while", breath- and count-length pauses) A about 42, B about 47; repeated evaluative looks
  (looked once, twice, again) A about 44, B about 25 by the read's count.
- **Lane A: recast or cut 25–30 combined**, especially double looks given to people other than Pike
  (for example ch2:149; ch11:321–327; ch24:23–35).
- **Lane B: recast or cut 30–35 combined**, especially the research plateau and the return
  (ch41–43; ch57–60).
- Instead: begin the next task; let an object change hands; answer with a bodily limit; or end the
  paragraph on the observed fact.
- KEEP: Pike's deliberate rereading (it is his signature); medical count pauses; consent pauses;
  every protected run.

## Priority 3 — keep the motifs, reduce their generic spill (§4 items 1, 2, 5)

Do NOT attack "hands", "count", "entered", "price" or "bill" as words. They are the book's design.
- **Lane A: remove or recast 35–45** non-functional instances; **Lane B: 45–55**, with special
  attention to ch41–46 and ch53–57: a hand that merely rests or moves; a thought "entered" as
  metaphor; a cost already visible being priced again; attention called a count when it changes
  nothing.
- Replace generic hand placement with the task's own action. Replace metaphorical ledger language
  with the immediate consequence. Let a count stand only when it changes a rule, a distance, a
  reserve, consent or a deployment.
- LEAVE untouched: healing contact; body ownership and every asking; Pike's board; Cael's log;
  Karis's measurements; Seln's report craft; Brom's load arithmetic; all protected wording.
- Smaller shared habits to thin while you are there: "let it stand" (A 2, B 5) and "put / set it
  by" (A 2, B 6); "as if / as though" where it explains a face or a silence that could stand alone.

## Lane-specific pacing notes (§5) — light, optional, no cuts for their own sake

- **Lane B, ch41–43:** the research plateau. The findings are distinct; the fourth begins to feel
  re-proved. Priority 1 work there should also drop any restatement that adds no evidence.
- **Lane B, ch51:259–383:** Teague's retrospective after the Stair delays the exhale. Tighten its
  glosses under Priority 1; keep every fact and his voice. Do not shorten the Stair's action.
- Movements 3 and 7 earn their length. Leave their structure alone.

Expect to lose about 1,500–3,000 words across the book. The reading grade measures low because of
short dialogue and counted observations; do NOT lengthen sentences or raise vocabulary to chase it.

## Both lanes

**Method.** By reading, in place, with the Edit tool, sentence by sentence. Never by script or bulk
find-and-replace. If a sentence is good and its repeat is the problem, change the weaker instance.

**Protect — nothing below may change:**
- every BOOK_MAP §10 unit, every unit the audits restored, and every pattern in
  `protected-patterns.txt` (the whole-arc read §6 and §11 list anchors with chapter:line);
- the FRAGMENT ACQUIRED notice; every log entry, letter, slip, ledger line and document;
- every count, day, date, distance, sum of money, rank and standing; every "Deployment since the
  Line" line and its number (none → one → thirteen → twenty-three → twenty-seven);
- every line quoted back later in the book; the consent thread's wording in ch36–38, ch47–48,
  ch55–56 (change nothing there but an obvious tic, and then only outside dialogue);
- owner defaults: #49 (protected "Path… mine" log wording), #50 ("Six years I've wanted a face"),
  #51 ("Tomorrow makes three") stay word for word and unglossed;
- season-blind (no season names, month names or order, English weekday names); feet, yards, paces,
  cords; never "his Path" for Cael outside protected lines; no new names; Teague's crew unnamed;
- the Reader Standard (a 13-year-old reader), the Monroe 1.3 voice and the O'Connor controls.

**Do not introduce** any run of eight or more words that also stands in the source: the overlap
gate will show it (see "After").

**Count.** Count each target before and after, with grep, within your range, and report both. Your
untouched baseline is `state/completion/pre-lanes/` (use `diff`, never git).

**After:**
- From the worktree root: `bash editions/monroe-1.3/tools/ed.sh overlap book-07-void-roads N` stays
  at 0 unprotected and `bash editions/monroe-1.3/tools/ed.sh gates book-07-void-roads N` stays at 0
  for every movement in your range. Movements: M1 ch1–7, M2 8–14, M3 15–22, M4 23–30, M5 31–37,
  M6 38–44, M7 45–52, M8 53–60. Lane A is movements 1–4; Lane B is movements 5–8.
- `bash editions/monroe-1.3/tools/sweep_probe.sh book-07-void-roads F L` does not rise.
- `python3 editions/monroe-1.3/tools/formula_metrics.py` on your range, per chapter: hold mean
  13.3–14.2 where it is in range now (ch10, ch32 and ch33 are known outliers; do not move them
  further out), ≥40-word share ≤ 4.5%, and scene lengths as they are.
- Verify the protected text by diff: every changed hunk against `pre-lanes/` must lie outside
  protected runs. Report how you checked.
- Write `LANE-A-REPORT.md` or `LANE-B-REPORT.md` in this folder: counts before/after per target,
  words before/after per chapter, anything declined and why, anything needing a coordinator ruling,
  and any join you want a second ear on in the listening proof.
- No git commands of any kind. Helper files only inside `state/completion/laneA/` or `laneB/`.
