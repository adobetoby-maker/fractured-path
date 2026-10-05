# AUTHORSHIP — Book 2, Movement 6 "Assessed" (chapters 37–43)

| Field | Value |
|---|---|
| Public byline | Monroe Jackson |
| Seat | `oconnor` 1.3.0 |
| Foundation | Monroe Jackson 1.3.0 |
| Requested author | Opus (Claude Opus 5.5) |
| Actual runtime model | `claude-opus-5-5` (Claude Opus 5.5), as stated in this session's environment |
| Packet | `editions/monroe-1.3/book-02-iron-circuit/state/movement-006/compiled-prompt.md` (movement brief: `editions/monroe-1.3/book-02-iron-circuit/packets/MOVEMENT-006.md`, as compiled) |
| Coordinator rulings | Six binding rulings delivered with the task (names Bede/Maud; "declaration" reserved for the Arbiter; the consent boundary; the pulse to be earned from one in three; notebook marks; earlier rulings stand) |
| Edition | `monroe-1.3` |
| Book | The Fractured Path, Book 2 — Iron Circuit |
| Chapters | `editions/monroe-1.3/book-02-iron-circuit/manuscript/chapter-37.md` … `chapter-43.md` |
| Date | 2026-10-05 |

**One author, one run.** All seven chapters were written by this model in a single session. No other agent or model touched them, and no subagent was used.

**Reading before drafting.**
- The compiled prompt in full: the profile, formula sections 2–6 and 8–9, the packet, the edition brief, BOOK_MAP §§1–12, STATE_LEDGER through "After Movement 5" with every coordinator ruling, CANON_RULES, the owner voice.
- The end of Movement 5: ch35 and ch36 in full.
- For continuity, by grep and short reads: every Keth passage in this edition (ch10, 12, 18, 23, 27, 30, 31, 36); the ch30 Shield bout (Cael's fighting style, keeper calls); the ch23 main-floor opening (Vell's rule formula); ch33–34 (Lira's question and her confirming win, the hands); ch11 (Lira's cutaway voice); ch32 (supper voice); the straw post's origin (ch3).
- M5's AUTHORSHIP and AUTHOR-REPORT, for the report structure.
- Book 3 ch8, by grep for Keth and the seam: it remembers Keth's seam as the place where "precision itself created a cost", between the second and third of a sustained sequence. The edition's "join" between the second and third cut of a chain fits it.
- Source `books/book-02-iron-circuit/chapters/chapter-17.md`, read once, in full, and then closed. It was not reopened. Its duplicated recording scene was noted; the events are used once.

**Method.**
1. After the single read I wrote a private event list in my own words, in the scratchpad outside the repo (`m6-event-list.md`): first what the source's events are, then my own order and inventions for chapters 37–43.
2. I drafted forward from that list and the book map, with the source closed. Entry points and beat order are my own (the movement opens on the knock tally; the drill comes before the yes; the seam tests teach the knock's rules; the bout is split across two chapters; the district's change is a sequence of named small encounters; Bede comes to Cael at a pump; Lira's bout is told from inside).
3. Protected wording (BOOK_MAP §8 items 14 and 27, and the §8.14 Keth lines) was copied from the map only.

**Per-chapter probe, as instructed.** After each chapter, before starting the next, I ran `skeleton_probe.py --source books/book-02-iron-circuit/chapters/chapter-17.md -- chapter-NN.md` (the one source `probe_sources.py` resolves for this packet), plus `source_overlap.py --min 8` on the same chapter. Results and rebuilds:
- **ch37**: 0% skeleton / 7% close on first draft; no flagged pairs. Revised for length and rhythm before ch38 (a Lira scene added); re-probed 0% / 6%.
- **ch38**: 0% / 5%; no flagged pairs.
- **ch39**: 2% / 7% on first draft, with two 8+ runs. The Dace-at-the-arch passage had followed the source's arrival lines from memory ("came to the arch at the quarter bell", "He stood in the gap…looked at Cael the way he looked at…"), and so had "The main floor never sat empty on a card night" and the *First time* line. All four were rebuilt from the event list (Dace's shadow on the arch and his rule about alcoves; the card-night money; "He set the two words down at the back of himself, like a coin"). Re-probed 0% / 4%, 0 runs.
- **ch40**: **8% / 14% on first draft — over the 5% bar — with six 8+ runs.** The bout's turning lines and the aftermath had tracked the source: "the real thing opened", "building a guess", "rolled his shoulder once and looked at Cael down the length of the floor", "came to finish it", "the best … he had ever seen him fight", "every one of them watched you do it", "It needed a page, and it would get one", "what else is on those pages about me", "Vell was writing when Cael came to the table", "One did not read over Vell's shoulder", "taking the fight apart… there would be questions". Every one was re-composed from the event list, and the protected Keth line was set as its own paragraph so that no attribution extended the run. Re-probed 1% / 9%, then 1% / 8% after the exchange-four expansion. The remaining ≥0.50 pair is the protected line itself.
- **ch41**: 2% / 7% on first draft, with two 8+ runs ("for the length of a bowl of stew"; the old man's line with a trailing "he"). Rebuilt, along with "Now the interesting ones will come", "Keth's name went two cities…", "the right shape for a fight to have" and the digest's "no Path at all". Re-probed 0% / 5%, 0 runs.
- **ch42**: 0% / 3%; no flagged pairs.
- **ch43**: 0% / 4%; one incidental 0.50 pair ("It was not a blow to hit with" against an unrelated source sentence), left as is.

**Blocking slips fixed as noticed.**
- Invented names removed. The cookshop man was "Marten" in my first draft, a place was "the Fenwater" and the coast keeper sat "at Saltmarsh". All three are now unnamed ("the cookshop man", "the river", "a keeper on the coast"), per the ruling that no other names be invented.
- "Since Torvin's" (Lira's line on Cael's breath) and "the straw at Torvin's" put Book 1 training at Torvin's. The straw post came from the Cinder House (ch3), so both now say the Cinder House.
- Bede's book "since the night of the Shield from the salt end": that bout was M3's, not the season's first. It now reads "the afternoon you beat Orvet's Shield" (ch30).
- The pulse hooks were misnumbered ("the third hook" for the meaning). The knock now goes out at the fourth hook, *committed*, matching ch37's "Committed… when you've meant it".
- The Log's pulse range said "all inside a pace", but the first knock in the Keth bout was at a pace and a half. It now says so.
- In exchange four, a near miss I had first given to the hip would have made a fourth unasked burst and broken the accounting. It is now his feet, a hair slow, and the boot is cut.
- Coss's "five weeks" since his note was too short by the M5 calendar (sightings, read-back, pulse week, archives and the Keth reread all came after it, and then M6's first three weeks). It is now "two months".
- The lit Ironyard "on the river in bars" assumed a waterside building nobody has placed. It is now a lit roof up the hill on the far bank.
- Lira's step-catch: the dawn glimpse (ch43, Cael POV) shows it happen once with Brom a week before the bout. Her bout section first called it entirely new; it now remembers the once and the week of not finding it.
- Hesk's reply would have taken weeks by a post the edition fixes at days. The letter now came a fortnight earlier and lay under a carter's bill until the sister found it.
- "Summer", "autumn" and "the season" calendar words that would date the step or the scout were replaced with "months ago" and "before the season posted".
- Lira's card "since the Arbiter at her Kindling" was replaced with "since before Fenmark" (her formal tier history is not mine to set).
- Keth's "twenty years" on the floor did not fit twenty-eight; it is now "ten years".
- Dace's "It's unbearable" echoed a line he never heard, so it is cut.

**After all seven existed.**
1. Scene merges and one split, from my own per-scene counts, for continuous action:
   - ch37: Lira on the landing runs into the grey book;
   - ch42: the bout's reset, and the hand-up into the aftermath;
   - ch43: the second and fourth exchanges run on.
   One break was added in ch43, where a dawn a week later had been run into the night of the booking.
2. Length: the first complete draft measured 34,051 words, under the floor. I added material where the brief had room:
   - the tall lad and the girl at the alcove arch (ch39);
   - exchange four's near miss and the "the faster he went, the less he chose" passage (ch40);
   - the barge lad's question (ch38);
   - Lira on Bede (ch42);
   - the academy-coat man's coin (ch41);
   - Brom and Lira's dawn drill on the middle (ch43);
   - Coss and the cross-reference slip (ch41).
3. `ed.sh overlap book-02-iron-circuit 6`: **0 unprotected, 2 protected**.
4. `ed.sh gates book-02-iron-circuit 6`: reader_standard=0, metadata=0 and modern=0 on all seven chapters.
5. `sweep_probe.sh book-02-iron-circuit 6 6`: **0% skeleton, 5% close** for the movement. Per chapter: 0/6, 0/5, 0/4, 1/8, 0/5, 0/4, 0/5.
6. `formula_metrics.py`. **Disclosure:** besides the per-chapter runs inside my check helper, I ran it on the movement four times:
   - after ch41 (13.96 mean);
   - after the first complete draft (13.52; 34,051 words);
   - after the expansions (13.49);
   - after the Coss addition and the final fixes (13.55).
   The ch39 ≥40-word share was 7.2% on first draft. I split nine of its long narrative sentences by hand, where each carried several turns. In ch42 I joined six runs of short narrative sentences by hand. No sentence was split or joined by script, and speech, Log entries, protected text and fight landing beats were untouched.

I wrote only the seven chapter files and these two state files, plus scratchpad notes and a check helper outside the repo. A `metrics.txt` I briefly wrote into `state/movement-006/` was deleted at once, so the folder holds only the two deliverables beside `compiled-prompt.md` and `range`. I ran no git commands.
