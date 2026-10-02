# Recheck r1 — Book 1, Movement 7 (chapters 41–47)

Review seat: Claude Fable 5.1, 2026-10-02. Author of the repair: Claude Opus 5.5 (r1 from
`REPAIR-BRIEF.md`; r1b the 8-word source-reuse sweep). Targeted recheck of the brief's findings
and of every changed region (`diff -U0` of each chapter against `pre-repair/`), not a fresh
review. No manuscript file was modified.

**Verdict: CLOSE WITH LINE FIXES** — two required, three recommended, one optional. No second
repair is warranted: nothing concrete is unresolved.

---

## (a) Brief items

| Item | Status | Where / evidence |
|---|---|---|
| P1 — Corvane's "What are you?" (Darrow's Tier A line) | **RESOLVED** | ch44:139 now "What's your word, boy? The one they gave you. Your friend wouldn't say. She said that was yours to tell." `grep '"What are you?'` over ch41–47 returns nothing. Vell still hears "[SHATTERED]" for the first time at her table (ch46:235–237, "Behind him he heard Vell's pen stop"). |
| P1 — ch42 Wind notice exact, three lines | **RESOLVED** | ch42:133–137 is a code block: `FRAGMENT ACQUIRED` / `[unnamed] — Wind-adjacent. Duration: undetermined. Integration: partial.` / `Tier equivalent: unknown.` — character-exact to BOOK_MAP §7. "four plain lines" → "three plain lines" (ch42:165); "four lines" → "three lines" (ch43:25). |
| P1 — bracket decision | **RESOLVED** | `[SHATTERED]` with brackets at every occurrence (ch44:143, ch46:235); matches the protected lines. |
| P2 — counts at the peak | **RESOLVED** | ch46:29 "won two since, and four of the six before it; that's thirteen bouts in my book"; ch46:49 "thirteen bouts now"; ch47:89 "fifteenth entry in the Log and the fourteenth bout in Vell's book, because the Log had counted Baro". Checked against the ledger: 5–6 after M6 (six M6 bouts W W L L W W = four of six), + Fenrow W + dyers' W = 13 before Feryn; Baro is Log entry 3 "Watched" (ch15:107), so Feryn is Log 15 and Vell's 14. Arithmetic closes. "Assessed, in my hand" vs "Against unrated" now told apart twice (ch43:121, ch46:29); Feryn's posting reworded to "any rating at all so long as a keeper has signed for it" (ch43:117), and Vell's "I've signed for one" (ch43:121) answers it. |
| P2 — calendar lines | **RESOLVED** | ch43:121 "a fortnight ago" (assessed day 97, told day 110: 13 days). ch46:29 "five weeks gone" (day 97 → 131: 34 days). ch44:157 "three weeks less three days" (told Mon day 110, Corvane Thu 113, bout 131: 18 days). ch45:189 "the last Tuesday". ch45:27 "anybody else". ch46:169 "the second Sunday" replaced by Renn's front heel in the fifth exchange — verified: ch35:347 "was in his fifth", ch35:419 "Fifth exchange. Called." |
| P2 — ch45 montage order | **RESOLVED** | The Vell-card Saturday scene moved intact ahead of "The district knew." (ch45:83–115). Board line changed to match: "Vell never put a bout with a gate on the board" (ch45:119). Hesk's protected quote inside the moved letter is exact (ch45:207). One dangling referent left by the move — see fix 3. |
| P2 — Feryn's ages | **RESOLVED** | Copper at nineteen (ch43:127, ch46:13); first Bronze evaluation at twenty-one (ch47:29); twenty-four now (ch46:13); "three cities over five years" (ch43:127, ch46:13), "four times in five years" (ch46:49); "I stood in front of Bronze panels for a year" as a candidate (ch46:247); "letting go on people for six years" (ch47:49) sits inside this. All agree. |
| P2 — doubled "at Copper 3" | **RESOLVED** | ch41:125 "the shove Petra had taught Cael, and the one Dellin had never got the chance to give him". Canon-checked: Cael's Dellin plan was "block nothing" so the shove never landed; won, fourth exchange, called (ch39:315). |
| P2 — ch42 cut courtyard beat | **RESOLVED** | ch42:37 is one sentence: "That night, on the low wall by the pump, the word at the edge of his tongue stayed exactly where it had been on Monday." The image is planted in ch41:183 ("right at the edge of your tongue"), so the callback lands. The keys and locks (ch41:77–87) and "not the Arbiter's kind of nothing" (ch41:193) are untouched. ch47:143 still counts "the two nights on the wall by the pump". |
| P3 — merges | **RESOLVED** | ch42 ×1 (before "Then she asked him the question", ch42:188); ch44 ×2 (Corvane's lesson, joins at ch44:37→39 and 91→94 read continuous); ch47 ×3 (Amrit's into the "goat" turn, ch47:41; the ruling into the notice, ch47:103–105; the notice night into the Kestrel reread, ch47:139–141). Each join is same place, same hour; none reads as a jump. Scenes 29 → 968.8 words/scene, inside 850–1,050. |
| P3 — pause beats | **RESOLVED** | "for a long time" 28 → 5; the replacements are concrete and placed (pie boy on the rope, Yeni's lamp going out, the girls on the wall chewing, the barge beyond Corvane's wall, the range ticking). Two small echoes remain (see (c), non-defects). |
| Length | **RESOLVED** | wc 34,962 (4,476 + 4,648 + 4,933 + 4,887 + 5,005 + 5,680 + 5,333), inside 34,000–35,500. |

## (b) The 8-word sweep (r1b)

Re-ran `tools/ed.sh overlap book-01-the-shattered 7` to the scratchpad (stdout only):
`# summary: 0 unprotected shared runs of >= 8 words; 0 protected runs (allowed)`. Confirmed.

**Protected wording, checked character for character:** Wind notice (ch42:133–137); Pressure notice
(ch47:109–113); "What tier are you?" said Feryn. / "[SHATTERED]." / "When you figure it out, I want
to know." (ch46:231, ch46:235, ch47:63); "Don't let anyone see you move. Not until you know what
you're doing." (ch45:207, and the echo at ch45:217). All exact. The Hesk-letter sentence that was
changed to break a run ("When I said it, I knew none of this.") sits after the protected line and
does not touch it.

**The Feryn bout (ch46:77–221), read whole.** The four exchanges still change one variable on each
side and stay trackable:

1. Feryn walks, everything loose / Cael looks for the held place and cannot find it → "the roof fell in"; flat, up at eight.
2. Feryn strolls with the shoulder-roll on top / Cael narrows to the middle of the shirt, reads it halfway, turns the guard edge-on → stays up, two furrows, the arm paid. "You read that."
3. Feryn stands still and talks (hides it under stillness) / Cael reads the decision itself, the step comes unbidden → round it, the open flank not taken. The exchange stays unexplained, as protected.
4. Feryn settles to working weight, comes in fast, builds and does not release, puts the hand where Cael will go / Cael reads it fine, calls the step (it does not come), trained slip → thrown with his own speed; the held grip. Vell's call, exact ("Good call." / "I know.").

Vell's call and the consent argument (ch46:39–47) are intact; only "for a long time afterward"
became "through the whole of that winter". Cost accrues as before (arm → ribs both sides → right
side → six breaths to stand), and ch47's Log entry (ch47:91–99) matches the exchanges as written
("up at eight", "Skidded two paces", "Thrown with my own speed").

**Re-composed sentences, each checked for meaning, referent, speaker and construction.** All 42
still mean what they did. Speakers: every dropped tag in ch44 and ch45 ("That's what you'll be
standing in front of.", "Tell me.", "I'll do it slowly.", "There.", "Something stays still.",
"That.", "It's not going to be reliable.", "I'll be here.") is unambiguous from the paragraph
before or the content of the line. No fragments. "rematch" (ch47:61) is in register — the board
notices use it (ch08:251, ch12:215, ch25:307). The listener-trips found are below; the first two
are real defects, the rest are small.

### Line fixes

**Required**

1. **ch45:191** — the r1 replacement for "did not open it for a long time" now doubles with the
   next paragraph ("Then he opened it.").
   - old: `and turned it over twice in his hands before he opened it.`
   - new: `and turned it over twice in his hands.`

2. **ch47:89** — "since the autumn" dangles at the end of the subordinate clause and reads as the
   Log counting Baro since the autumn, or Cael watching him since the autumn.
   - old: `It was the fifteenth entry in the Log and the fourteenth bout in Vell's book, because the Log had counted Baro, whom he had only watched, since the autumn.`
   - new: `It was the fifteenth entry in the Log since the autumn, and the fourteenth bout in Vell's book, because the Log had counted Baro, whom he had only watched.`

**Recommended**

3. **ch45:119** — after the scene move, "those days" has no antecedent (the Saturday scene now sits
   between it and Vell's "three days").
   - old: `He found that out over those days a piece at a time,`
   - new: `He found that out a piece at a time,`

4. **ch46:89** — "It" follows "his guard did not break so much as fold" and grabs the guard on
   first hearing; the subject is the air.
   - old: `It slammed his own forearms flat against his chest,`
   - new: `The air slammed his own forearms flat against his chest,`

5. **ch45:267** — "without moving to take stock" garden-paths ("did not move to take stock").
   - old: `and lay without moving to take stock, as he did on days that mattered:`
   - new: `and lay still and took stock, as he did on days that mattered:`

**Optional**

6. **ch47:207** — "went from black to grey" after Lira has already "read it in the grey light"
   (ch47:199).
   - old: `while the sky over the east wall went from black to grey.`
   - new: `while the sky over the east wall went on paling.`

Each old text occurs exactly once in its file. None of the new texts reintroduces a source run
(all are new wording or shorter than the author's text).

## (c) New defects

None of substance. Checked and clean:

- Continuity of the new concrete beats: Yeni's lamp (ch41:33, ch47:85), the girls on the wall
  (ch42:87, 93), the pie boy on the rope (ch41), the range at Torvin's (ch43:5, ch44:195), the
  low wall and the river at Corvane's (ch44:149, ch45:258), Vell's quarter-turn of the cup kept
  for Vell (ch45:89) and Feryn now squaring his with a finger (ch47:41).
- "Vell never put a bout with a gate on the board" (ch45:119) is compatible with her own "keep a
  Bronze off the board for three days" (ch45:81).
- Reader Standard, metadata and modern-register gates: 0/0/0 on all seven chapters (`ed.sh gates`).
- No protected line altered (see (b)).

Non-defects worth a glance, no fix required: two range-ticking pause beats five thousand words
apart (ch43:9, ch44:193) and the pen-over-paper / pencil-over-sentence pair (ch43:9, ch44:203)
are the author's own small echoes from thinning "for a long time"; a listener will not trip on
them. ch46:247 "for a year… Months of it" is pre-repair text and out of scope.

## (d) Second repair

Not warranted. The brief's findings are all resolved and the sweep left the bout, Vell's call and
the consent argument intact. The two required fixes are single-sentence hand edits with no
knock-on; the three recommended ones are the same. Close after the fixes are applied; re-run
`ed.sh overlap book-01-the-shattered 7` once afterward (expected: still 0).
