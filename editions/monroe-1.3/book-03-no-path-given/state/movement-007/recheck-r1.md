# Recheck r1 — Book 3, Movement 7 (chapters 47–53)

**Seat.** Review seat, targeted recheck after same-author repair r1 (Claude Fable 5.1; author Claude Opus 5.5). Not a fresh review. Method: `diff -U0` of each chapter against `pre-repair/`, every changed region read in context in the current files, the brief walked item by item, the tools re-run, the M8 packet's coordinator notes checked against the page. No manuscript file was modified.

---

## Verdict: CLOSE WITH LINE FIXES

Seven line fixes, listed at the end — one POV slip the repair introduced (ch47), one duplicated tell the lengthening introduced (ch51), one join that moved a sentence closer to the source (ch50, 0.68), one unsupported callback (ch52), one object count and one orphaned object in the ch53 return scene, and one optional referent (ch48). None needs a second repair; none touches speech, a protected line, or the scenes the brief protects. Every brief item is resolved. Scope after the fixes: nothing further for this movement; the one note for the coordinator is a packet wording (c.8), not prose.

---

## (a) Brief items

### Coordinator fixes F1–F9 and the Prynn line, read in context

| Item | Status | Evidence |
|---|---|---|
| F1 blank line above the ch53 `---` | RESOLVED | ch53: "…the old knock, and went in." / (blank) / `---`. Script check of all 35 breaks in the seven files: every `---` has a blank line above and below. |
| F2 Brom's floor conversation same night | RESOLVED | ch53: "But we'd already sat on the floor that same night, and you'd told me about the window that wasn't a window, and we were friends before the lamps were out, and I never needed to." |
| F3 Oona until her Kindling | RESOLVED | ch49: "Oona had sat beside him under it until her Kindling". |
| F4 stub line at the top of the next page | RESOLVED | ch48: "At the top of the next page, hard against the stub, she wrote one line in her smallest hand". |
| F5 Karis never touches the binder | RESOLVED | ch53: "She took a loose sheet from inside the back cover and laid it on the table in front of him. 'One page is in that book. This one is yours, because clause six says you read it first and keep it. Put it with the others. I'd rather not know where that is.'" / "I know." Night: "Karis's other copy was in the back pocket of the binder, where he had put it himself an hour ago". The join reads: "I know." answers "I'd rather not know where that is", and her "I wanted you to hear me say it" now attaches to the hygiene she has just stated aloud, which is in character. Author's report §2 corrected. |
| F6 the memory of Denvash | RESOLVED | ch51: "when the memory of Denvash had come up through his body without asking". |
| F7 wanted to hear at fourteen | RESOLVED | ch53 log: "That's the part I'd have wanted to hear at fourteen." |
| F8 nobody's read it | RESOLVED | ch51: "nobody's read it in Prynn's lifetime, she told me so". |
| F9 Havel's five years | RESOLVED | ch49: "Five years of compliance visits, and one season of recording to panels since the grade"; "without seeming to for five years". |
| Prynn's packet line | RESOLVED | ch48: "Their code forgot to write the word that gives them you," said Prynn. "It remembered to write the word that takes my shelves." Exact; the overlap tool lists it among the 12 protected runs. The sentence before it was recomposed so the two no longer share words: "You found your seam in what their code left out. I've lost my shelves to what it put in." Read in context it is a two-beat — the plain statement, his silence ("there was nothing in him that was big enough"), then the sharpened one — and the restored line is the sharper of the two. Accepted. |

### Priority 1 — narration joins

RESOLVED. Mean 12.07 → 13.07 (brief 13.0–13.3); ≥40-word share 2.7% → 3.6% (brief ~3.5%). Verified by a quoted-speech comparison of every chapter pre vs post (multiset of `"…"` segments): **ch49 and ch50 have zero speech changes**; the only speech changes anywhere are the ones the brief ordered (ch47 the Assessor fixes; ch48 the seam sentence and the restored packet line; ch51 Hobb's line, the "Noted" replacement and F8; ch52 the new Prynn scene and the failed answer; ch53 F2, F5 and Lira's "Noted" replacement). So:

- **The deposition rhythm** (ch49 s3): every question and every one-word answer byte-identical; the pen stopping kept ("Then it stopped, and Cael heard it stop, and heard in the stopping that the recording officer had looked up, and did not look round to see"); the nine dashes unchanged in all four places (ll. 279, 281, 285, 341). The joins around it are the right ones — "They went on, at the same pace, as if the hour had a length already fixed and both of them knew it" reads as the hour, not a splice.
- **"Count." / "Marks." / "Sign."** — the three speech lines and the whole count scene are outside the diff; unchanged.
- **Yorlan's formula** — present once, verbatim, in ch52; "the panel notes it" ×2 in ch52 plus Karis's new "The panel notes it. The respondent has not answered." in Yorlan's voice, which is the rehearsal's premise used correctly.
- **Joins read as joins.** Spot-read in ch47 s5 ("He waited, and she let him wait long enough to know that she meant him to"; "She sat back in her chair, as if she had laid the last stone herself"), ch48 s2/s5, ch49 s3, ch50 s2, ch51 s1/s3/s6, ch52 s1, ch53 s4: they carry one thought each and keep the beats short where the beat lands ("He stood still." in the moved Prynn scene; "The fire ticked."; "Nobody helped him."). The protected scenes (ch50 s3–5, ch49 s4 and s6, ch51 s5, ch52 count) are outside the diff except the one three-step dating passage in ch50 s4 the brief asked for.
- **The ~40 re-splits** are clean where sampled (ch48 l.5 "Prynn had told him to look at something else for a morning…"; ch50 l.5 the ring walk; ch51 l.217 the stable). No fragment left behind; no dangling "and" or orphaned subordinate clause found in any changed line.
- One cost of the lengthening: two bare beats were padded with the same tell twice in one scene (ch51 "with her whole face", l.25 new and l.47 existing) — fix 2.

### Priority 2 — say it once; spread the eve

- **Gesture thinning — RESOLVED.** Counts pre → post across the seven files: "larger half" 4 → 2 (ch49 both halves; ch52 Lira's "Good"; the ch47 establishing scene uses other words and is intact); hand-over-mouth laugh 2 → 1 (ch53 only; ch50 "looked guiltily at the high desk", ch51 "looked away at the low lamp", ch52 "laughed at the rafters"); "lips moved" 6 → 4 (Karis's two cut; the four left are Ilsev's, two of them in protected ch49 s6); "Noted" as a closer 3 → 1 (ch51 now "It's on the record," said Cael. "Mine." — which answers Karis's "so it's on the record somewhere" exactly; ch53 Lira now "I'll write it in the binder… In the square hand", paid off by "Written." in the log; the protected "Noted." / "The archive notes it too" kept). The chest sentence: ch49 kept, ch50 "Hearing it was like a weight being set down on the table between them, and he felt the table take it." The ch48 bread → tea → spoon works, with one small referent (fix 7, optional).
- **The eve's gifts — RESOLVED.** Prynn's beat is now a new scene at the end of ch52's Saturday count, after the cart ("You know where they live now. Put them back yourself."), where it answers her loss directly; on the eve the callback is wordless ("She only looked toward the back of the room, past the pillar, where the code's case stood by the old wall. So he took them back himself."). Eve gifts: Brom midday, Karis afternoon, Lira at dusk. Lira's slip delivered on the eve (ch53: "put it in the inside pocket of his coat, against Brom's page"); nothing held for M8. The log's gift list drops "P." accordingly; the ledger's "she let him shelve the code himself" is still true on the page (Sunday, unprompted).
- **The custom objection, shown — RESOLVED.** ch52 end of rehearsal 2, on the page: Karis in Yorlan's voice ("Long and general practice is how most law begins. The respondent will answer."); the hot wrong answer ("But that's the whole wrong of it…"); "The panel will not hear that… It is asked whether it is written."; "Custom can be wrong," he tried. / "So can a schedule… The respondent has not answered."; the argument going "soft under him at one place, like a board that gives"; Brom's Wray question in his own voice; **"It amends,"** he said slowly; "How many times?" / "I don't know." / "The panel will want to know." She held out the concordance card… "Find out. Tonight." Then ch53 s1 opens on the count: "He had counted them by candle in his room after the fire went out, with Prynn's concordance card unfolded on the desk… There were forty-one amendments to the schedule", given to Karis Saturday night, drilled past midnight. Breakfast's "Custom" / "Is not code" and the forty-one speech unchanged. The ch53 opening line ("kept him at Karis's bench of books until long after the fire was out") agrees.

### Priority 3 — cold-reader stumbles

1. **Assessor — RESOLVED.** ch47 gate: "Assessor Havel," he said. "Recording officer now, I see. You've a new grade."; Coss greets "Assessor Ilsev of the senior evaluation seat"; Cael to Quenna: "The senior assessor," he said. "Ilsev." The one defect is in the sentence before Coss speaks (fix 1).
2. **ch50 dating chain — RESOLVED.** "So the count went in three steps, and she could say them in order. First, the yearbooks counted the house's own years… Next, the weather log's last line gave that last year in both reckonings at once. Then the accession register counted on from that same year… all the way to this week." Legible on one hearing; the four-hundred-years passage and the hand on the wall untouched.
3. **ch51 "it" — RESOLVED.** "He had carried the notebook everywhere for so long…" now precedes the bread.
4. **Concordance — RESOLVED.** A hand-ruled card in ch48, ch52 (×3: folded inside the index's cover; unfolded and laid flat; held out folded) and ch53. One loose end: the card goes up to Cael's room Saturday night and is never seen going back to Prynn (fix 5 closes it).
5. **Optional items — both taken.** The Yorlan portrait ends at "and had never once raised his voice."; Hobb says "Second hour." then "Say what I saw." and Oona's "four words… in a row" still counts.

---

## (b) Source distance

`skeleton_probe.py` (source ch18–20 vs ch47–53): **TOTAL sentences 1,560, skeleton 2%, close 12%** (pre-repair run for comparison: 1,541, 3%, 13%). By chapter: ch47 3/12, ch48 1/9, ch49 1/7, ch50 1/8, ch51 4/14, ch52 3/16, ch53 3/17. No scene over 15% skeleton (highest: ch52 s7 rehearsal 2 at 11%, ch51 s3 and s6 at 10%, both carrying P12).

Unprotected sentences ≥ 0.65 on the current text:

| Where | Score | Sentence | Note |
|---|---|---|---|
| ch47 s4 | 0.81 | The Compact was not a machine that made a new face for every case. | pre-existing, unchanged |
| ch47 s5 | 0.73 | You walk in with nothing and you sit with nothing. | speech, pre-existing |
| ch49 s3 | 0.69 | Coss walked him through the enrollment and every paper attached to it, and Cael confirmed every signature and every date. | pre-existing, unchanged |
| **ch50 s1** | **0.68** | Cael said nothing, because there was nothing to say that would not give Coss more than the silence did… | **created by the join** (pre-repair "Cael said nothing. There was nothing to say…" was under the line; the join reproduces the source's "Cael said nothing, because there was nothing useful to say") — fix 3 |
| ch50 s1 | 0.78 | "For what it's worth," said Coss, "I hope the argument's a good one." | speech, pre-existing |
| ch50 s3 | 0.72 | The waystation had kept books the way a working house on a guild road had to. | pre-existing, protected cutaway |
| ch51 s6 | 0.74 | "Think what the room does with it," he said at last. | speech, pre-existing |
| ch52 s7 | 0.73 | "You can't remove me under rules that don't have me in them." | speech, pre-existing |

The 1.00s are all protected (P12 ×2, P15, Brom's page, "Findings to date", the ch53 log line). The author's two probe recompositions worked: ch52 s2's "She turned a page of the concordance without looking at it" (0.74) and ch53 s5's two framing sentences (0.68, 0.78) are gone from the list.

`ed.sh overlap book-03-no-path-given 7`: **0 unprotected shared runs ≥ 8 words; 12 protected.** Matches the author.

---

## (c) Every changed region

- **Joins, fragments, dangling referents.** Checked across all 834 diff lines. One POV slip: ch47 l.71, in Havel's own section, "Then he turned to the young man with the recording case." — Havel describing himself from outside, with Cael's label for him, in a sentence that already has Coss's "young man with two satchels" and after Havel "handed the case down to the porter" (fix 1). One padded tell duplicated inside a scene: ch51 "with her whole face" ×2 (fix 2). One referent: ch48 "why the tea had gone cold in front of her" reads as a question about tea (fix 7, optional).
- **Orphaned callbacks.** Prynn's spoken beat moved; every pointer followed it: ch53's return scene is wordless and no longer carries the count-at-the-desk dialogue; the log list no longer names P. The "Noted" callbacks: ch53 "Written." pays Lira's new line. The "Find out. Tonight." card: counted Saturday night (ch53 l.27) — but the card itself never returns to Prynn on the page (fix 5). ch52 l.43 "as he had promised Oona once that he always would" has no promise behind it — the only promise to Oona on record is ch22's "he would not lie to her" (fix 4). ch52 l.347 "a sentence she had given the taxonomy master at the same table" is supported (ch44 l.89 and ch48 l.117).
- **ch53 return scene counts.** "the fourteen digests with Yorlan's name in the margin" — the fourteen are hearings, not volumes (ch48: one digest volume holds many hearings; ch52: "There had been fourteen, and Prynn had brought them down"); and three charter volumes + the index + the digests are "the armful", where the same books went up "in two armfuls" (fix 5, fix 6).
- **Calendar, week 21.** Mon delegation at the third bell, Quenna at the seventh; Tue notice, contest at the fifth bell, dusk drill, ledger page; Wed deposition at the first bell, Havel B, query "with the evening courier… evening courier, down" (ch49 l.315–323), Coss at the ring at dusk, Karis finishes the schedule; Thu witness list, the find; Fri breakfast, toll books, rehearsal 1 (bench built after the eighth bell); Sat count from the second bell, last box "a little before the fourth bell", **new Prynn scene "in the middle of the afternoon"**, courier "a little after the fifth bell", Ilsev "at the sixth bell", Havel C that night, rehearsal 2, the count by candle, drill past midnight; Sun breakfast, last pass, Brom midday, archive afternoon, Lira at dusk, log. Coherent; the Prynn scene sits before the fifth bell and after the cart. Courier calendar as ruled (Wed evening down, Sat after the fifth bell, Monday up: "It goes down with Monday's courier").
- **Karis never touches the binder.** ch48: he files her cut page himself that night; ch53: she hands the loose sheet, "I'd rather not know where that is"; night: "where he had put it himself an hour ago". Nowhere else does she come near it.
- **Protected lines exact (BOOK_MAP §9 and brief).** Grep-verified verbatim: Yorlan's formula; "Findings to date: the phenomenon is a person. Study continues."; "The archive notes it too"; "I won that bout"; Brom's page line; P12 all three texts; P15; "Tomorrow I argue that their system never contained me."; "Nobody ever mended a hole by pretending to stand on it"; "Somebody writes the law"; the deposition's "The ledger says so" / "That's a classification question" / "I understand that everything may be noted. That's what a record is" / "The provision lets the candidate elect" / "Four weeks" / "Because it was the door the provision had," said Cael, "and I wanted to go to school."; Karis's stub line; the witness-list text; P16's return and referral; "Five days."; "This is real. Start from that."; Prynn's two-beat line.
- **`---` rendering.** All 35 breaks have a blank line above and below (scripted check, zero findings).
- **Reader Standard.** `ed.sh gates`: reader_standard=0, metadata=0, modern=0 on all seven. Nothing in the new prose the gate would catch; no modern register in the new Prynn scene or the failed answer.
- **M8 coordinator notes, checked on the page.** Yorlan's opening verbatim ✓; deposition lines exact ✓, nine dashes ✓; box seven, nine volumes, fifty-three boxes, "Four hundred and some volumes", the per-box line, "They'll come back… For the duration. The officer entered it." ✓; courier calendar ✓; Cael knows nothing of the query (Havel-POV only) ✓; in Cael's possession on the eve: Karis's sheet (binder back pocket), Brom's page and Lira's slip (coat), the cut ledger page ✓; the six places ("The schedule went through all six places") ✓; Edran's "four in four" (ch51 l.67) ✓; "Into the notebook, then" ✓; the r1 update line (forty-one Saturday night, Prynn Saturday afternoon, Lira's slip on the eve) ✓. **One packet wording to correct (no prose change):** the note "The custom objection was rehearsed and answered ('Somebody writes the law. Nobody ever mended a hole…')" quotes the answer to Brom's hole-in-the-world, not the custom objection; the custom objection's on-page answer is "It amends" / the forty-one amendments / "Custom is not code".

---

## (d) Metrics

`formula_metrics.py` on the seven current chapters, confirming the author's after-column exactly:

| Metric | Author | Recheck | Range |
|---|---|---|---|
| Words (tool / wc) | 36,209 / 36,284 | 36,209 / 36,284 | 34,500–36,500 ✓ |
| Sentence mean | 13.07 | 13.07 | ≥13 ✓ (brief ~13.0–13.3) |
| Median | 9 | 9.0 | — |
| ≤5-word share | 31.0% | 31% | — |
| ≥40-word share | 3.6% | 3.6% | ≤4.5% ✓ |
| Scene breaks / words per scene | 35 / 862.1 | 35 / 862.1 | 850–1,050 ✓ |
| Flesch RE / FK | 86.8 / 4.40 | 86.8 / 4.4 | — |

Per chapter (wc): 47 4,401; 48 5,168; 49 4,973; 50 5,009; 51 5,458; 52 6,576; 53 4,699.

---

## Line fixes

Each old string verified to occur exactly once in its file (`grep -c -F`). Paths under `editions/monroe-1.3/book-03-no-path-given/`.

1. `manuscript/chapter-47.md`
   old: `Then he turned to the young man with the recording case.`
   new: `Then he turned to Havel.`

2. `manuscript/chapter-51.md`
   old: `Oona considered that for some time, with her whole face.`
   new: `Oona considered that for some time, from every side.`

3. `manuscript/chapter-50.md`
   old: `Cael said nothing, because there was nothing to say that would not give Coss more than the silence did, and the silence was already giving him enough.`
   new: `Cael let the silence stand, since anything he said would give Coss more than the silence did, and the silence was already giving him enough.`

4. `manuscript/chapter-52.md`
   old: `He thought about it properly, as he had promised Oona once that he always would.`
   new: `He thought about it properly, which was the only kind of answer she had ever taken from him.`

5. `manuscript/chapter-53.md`
   old: `the charter's three volumes and the schedule's index from Karis's bench of books, and the fourteen digests with Yorlan's name in the margin.`
   new: `the charter's three volumes and the schedule's index from Karis's bench of books, with Prynn's concordance card folded back inside its cover, and the digest volumes with Yorlan's fourteen hearings in them.`

6. `manuscript/chapter-53.md`
   old: `She watched him set the armful down on the end of her desk,`
   new: `She watched him set the two armfuls down on the end of her desk,`

7. `manuscript/chapter-48.md` (optional, referent)
   old: `and why the tea had gone cold in front of her.`
   new: `and why she had let the tea go cold in front of her.`

After the fixes: re-run `ed.sh overlap` (no new 8-word run is possible from these strings) and the probe (fix 3 is the only sentence that was over 0.65; the new wording shares no clause with the source).
