# Repair brief — Book 3, Movement 7 (one consolidated same-author repair)

Sources: `review-editorial.md` and `review-cold.md` (both Claude Fable 5.1, fresh context; the
cold read is manuscript-only). Both would keep reading. The deposition, the Brom-as-Coss rehearsal,
the box-seven count ("the single best plant in the movement") and the two restrained reveals
(UNBOUND → SHATTERED; a designation with "no originating authority of record") all land. The
event-list method held: skeleton 3%, and the editorial spot-check found the Coss ring-walk and the
find new prose. Reader Standard passes; protected lines verbatim; overlap 0. Pre-repair text is
frozen in `pre-repair/`. Repair in reading order, in place, by reading — never by script.

**Rulings on your flags — all accepted:** the courier calendar (query down Wednesday evening,
return Saturday after the fifth bell) is the edition's canon; Havel seeing the designation by name
in the Compact's routing papers is consistent with source ch18, B4 ch18 and B2 ch15; Brom's "I won
that bout" is canon-true (B2 ch11); UNBOUND from the margin of Vell's oldest ledger is right
(B2 ch16); the deposition's "No." and "four weeks" stand (four weeks is exact); Karis's cut-out page
stands; all new canon is accepted. Of the five packet lines you recomposed, the coordinator has
restored Prynn's exactly ("Their code forgot to write the word that gives them you." / "It
remembered to write the word that takes my shelves.") and added it to protected-patterns; the
other four stay as you wrote them.

**Already applied by the coordinator (do not redo):** editorial fixes F1–F9 — the blank line above
the ch53 `---` after "the old knock, and went in."; Brom's floor conversation "that same night";
Oona beside him "until her Kindling"; Karis's line "at the top of the next page, hard against the
stub"; Karis hands Cael the loose sheet and does not touch the binder ("Put it with the others. I'd
rather not know where that is." / "I know." / the copy is in the back pocket "where he had put it
himself"); "the memory of Denvash"; "wanted to hear at fourteen"; "nobody's read it in Prynn's
lifetime"; Havel's "Five years". Re-read them in context and smooth any join.

**Protect:** the deposition's rhythm (the plain question, the one word, the pen stopping, the nine
dashes after "No"); Prynn's "Count. Marks. Sign."; Yorlan's opening formula and "the panel notes it"
exactly (Movement 8 uses it verbatim); the box-seven Saturday count exactly as counted; "Findings to
date: the phenomenon is a person. Study continues." and the "Noted." / "The archive notes it too."
exchange; Brom's "I won that bout"; every protected and brief-quoted line; the Karis cutaway in ch50
(scenes 3–5); ch49 scene 6; ch51 scene 5; ch52 scenes 3–4.

## Priority 1 — Sentence mean: join narration, never speech (editorial)

Mean 12.07 against 13–15.5. The dialogue load matches Movements 5–6, which passed; the gap is pure
narration (14.48 against ~15.8), cut into three- to nine-word sentences in these scenes: ch47 s5
(Quenna's room, narration averages 9.2) and s6; ch48 s2, s5, s6; ch49 s3 (the narration around the
deposition's questions — not the questions or answers); ch50 s2; ch51 s1, s3, s6 (the decline, 11.76),
s7; ch52 s1 (12.11), s5 (Havel's third entry), s6; ch53 s4. About 190–230 joins in total, by
reading: join clipped runs that are one thought; keep the short sentence where a beat lands (a
recognition, a hit, a turn). Let a few earn real length. Target mean ~13.0–13.3, ≥40-word share
~3.5%. The Karis cutaway is not a place to join — it is already the longest-sentenced prose.

## Priority 2 — Say it once; spread the eve (cold read)

- **Gesture repertoire:** bread-halving ×6, Karis's hand-over-mouth laugh ×3, "lips moved very
  slightly" ×6, "Noted" as a scene-closer ×3, and the near-duplicate chest sentences at ch49 s4 /
  ch50 s2. Keep each where it is load-bearing (the first, and the one that pays); cut or vary the
  rest.
- **The eve's four gifts in a row (ch53):** spread them — e.g. move Prynn's "put them back
  yourself" beat to the end of ch52 after the cart, or hold Lira's slip for the Monday morning (if
  held, note it for Movement 8). Your choice; say which in the report.
- **The custom objection:** show one bad answer on the page in rehearsal instead of "badly, and then
  less badly, and then well".

## Priority 3 — Five cold-reader stumbles

- "Assessor" covers four roles; make the first one at the gate in ch47 unmistakable and keep the
  others distinguishable by a word.
- The ch50 dating chain: make the order of days legible on one hearing.
- ch51 s2: the "it" referent after the bread.
- Prynn's concordance is a card in ch48 and a volume in ch52 — make them agree.
- Optional (editorial taste): ch47's Havel coach portrait of Yorlan could lose its last three
  sentences; Hobb's "Same as the sittings." after "Second hour." reads as if the sittings were at the
  second hour (they are at first bell).

**Length.** Finish within 34,500–36,500 words.

## After the repair

Run `editions/monroe-1.3/tools/ed.sh overlap book-03-no-path-given 7` (must stay 0 unprotected),
`ed.sh gates`, `python3 editions/monroe-1.3/tools/skeleton_probe.py --source
books/book-03-no-path-given/chapters/chapter-1{8,9}.md books/book-03-no-path-given/chapters/chapter-20.md
-- editions/monroe-1.3/book-03-no-path-given/manuscript/chapter-4{7,8,9}.md
editions/monroe-1.3/book-03-no-path-given/manuscript/chapter-5{0,1,2,3}.md` (stay ≤5%), and
`formula_metrics.py` on the seven chapters; then append "## Repair r1" to `AUTHOR-REPORT.md`
(before/after metrics, overlap and probe, the eve-gift choice, changelist by chapter) and correct §2
to match F5 (Karis has never seen the binder). Edit only the seven chapter files and
AUTHOR-REPORT.md. No git commands.
