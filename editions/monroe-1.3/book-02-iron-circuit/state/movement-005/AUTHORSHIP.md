# AUTHORSHIP — Book 2, Movement 5 "The Circuit's Seasons" (chapters 30–36)

| Field | Value |
|---|---|
| Public byline | Monroe Jackson |
| Seat | `oconnor` 1.3.0 |
| Foundation | Monroe Jackson 1.3.0 |
| Requested author | Opus (Claude Opus 5.5) |
| Actual runtime model | `claude-opus-5-5` (Claude Opus 5.5), as stated in this session's environment |
| Packet | `editions/monroe-1.3/book-02-iron-circuit/state/movement-005/compiled-prompt.md` (movement brief: `editions/monroe-1.3/book-02-iron-circuit/packets/MOVEMENT-005.md`; checked identical to the compiled copy) |
| Edition | `monroe-1.3` |
| Book | The Fractured Path, Book 2 — Iron Circuit |
| Chapters | `editions/monroe-1.3/book-02-iron-circuit/manuscript/chapter-30.md` … `chapter-36.md` |
| Date | 2026-10-05 |

**One author, one run.** All seven chapters were written by this model in a single session, with no pause and no other agent or model touching them. No coordinator correction arrived during drafting, including none from the Movement 4 recheck.

**Reading before drafting.**
- The compiled prompt in full:
  - the profile;
  - formula sections 2–6 and 8–9;
  - the packet;
  - the edition brief (event-list method, 8-word gate, working ranges);
  - BOOK_MAP §§1–12, with particular attention to:
    - §3 C4–C5, E4–E5, E11;
    - §5 (Havel and Coss cutaway limits; the record window);
    - §7;
    - §8 items 3, 4, 24, 25 and 26;
    - §9;
    - §11 b, h, m and o;
  - STATE_LEDGER through "After Movement 4", with the coordinator rulings for every movement;
  - CANON_RULES.
- Movement 4 in full: this edition's ch23–29.
- M4's AUTHORSHIP and AUTHOR-REPORT, for the report structure.
- For continuity, the passages these chapters touch:
  - ch4 (the academy-coat Blade's first complaint; the cupboard and the one-armed keeper);
  - ch2 (the pine board, *t.f.*);
  - ch10 and ch12 (Keth's page);
  - ch14–15 (Havel's file, the green slip, the yellow room, the pear);
  - ch17 (Coss, the grey slip, the empty log pages, *Noted.*, his daughter's map).
- Later books, by grep: B3 ch18 (Ilsev's *Suppression-Advisory* / *registry sub-layer* wording; Havel's later grade) and B3 ch19 (the copied note *Assessed per pre-registry terminology as UNBOUND.*). Also a grep of source ch17 and B3 ch8, for how Keth's seam is remembered, so that the M6 seed fits.
- `packets/MOVEMENT-006.md`, "Where we enter", for the hand-off.
- Source `books/book-02-iron-circuit/chapters/chapter-14.md`, `chapter-15.md` and `chapter-16.md`, each read once, in full, and then closed. They were not reopened.

**Method.**
1. After the single read I wrote a private event list in my own words, in the scratchpad outside the repo.
2. I set the season's order myself:
   - the board, the *Carrying* column shown to Lira, and range bought with stillness;
   - the clean win;
   - the flood and the dispute;
   - Dace;
   - Vell's correction;
   - the dinner and the first footwork morning;
   - the walking channel and Lira's question;
   - Havel;
   - Lira's confirming bout;
   - the false positive and the three sightings;
   - Coss and the record window;
   - the read-back;
   - the pulse;
   - the archives;
   - the Keth seed.
3. I drafted forward from that list and the book map, with the source closed.
4. Protected wording (§8 items 3, 4, 24, 25 and 26) was copied from the map.

**The sweep probe after each chapter, as instructed.** The official `sweep_probe.sh` calls `read_text()` on all seven chapter paths, so it fails while some chapters are still missing. After each chapter I therefore ran a scratchpad wrapper around `skeleton_probe.py`. It uses the same sources `probe_sources.py` resolves (ch14–16) and covers only the chapters that existed. With `SHOW=1`, these are the places that had tracked the source from memory, and how each was rebuilt before I moved on:
- **ch31, dispute scenes (7% skeleton, 14% close on first draft).** Four lines followed the source's dispute beats:
  - "argue about what happened… three days";
  - "written down before the bout was ever booked";
  - "crossed it out and started another one";
  - "waiting… a third time".
  Each was recomposed ("Argue with the page…"; "This was on your page… before Dace ever put the two of you on his wall"; "There's a line through half the pages in it…"). Result: 0% / 7%.
- **ch32, dinner (scene 2 at 9%, scene 4 at 19% close).** These lines were recomposed:
  - "Two rooms and a borrowed table";
  - "three cities in two years";
  - "worth leaving things lying about in";
  - "I don't mind it as much as I'd have guessed";
  - "stayed up later than any of them meant to";
  - "All the people who've been in a room with me";
  - "I talk like a man who stopped listening".
  Result: 1% / 5%.
- **ch34:**
  - the watcher image (kept as the packet's image, reworded: "a fire somebody had banked for the night and then sat up beside, awake, with their eyes on the coals");
  - "wrote the cost beside the finding… the discipline";
  - "read it for a minute… a price".
- **ch35:** "He closed it the only way left to him" (Coss).
- **ch36, archives (scene 2 at 8% / 17%, scene 5 at 9% / 17%).** These were recomposed:
  - the asking lines ("You said once…", "I don't open those…");
  - the "costs you something every time" question;
  - the stamp/seal sentence;
  - "Somebody has to keep the record…";
  - "twenty years".

  The walk home's texture had followed the source's catalogue (the lamplighter, the bread shutters, two fighters arguing a lost bout). I replaced it with my own: the gulls on the coping, a barge with one lantern, the chestnut man banking his brazier, a woman calling a child in.

  The entry-finding sentence ("two-thirds of the way through") was also recomposed. Result: 0% / 6%.

**Blocking slips fixed as noticed.**
- Hesk's letter said the race had frozen "at midwinter", which would pass a season edge the edition keeps before midwinter. It also quoted "your grandmother", who is not established. It now reads "ice at the edges" and "My father used to say".
- "the season before this one" for the academy-coat man's first complaint is now "a few months back".
- Lira's pan "brought from Fenmark" was unestablished, so the phrase is cut. "since the barn" was in Cael's memory, but the barn is Lira's history, not his; it is now "the winter on the straw".
- Lira "cooked perhaps four times a year" contradicted ch4, where she cooks in the back kitchen. It now reads "most nights, plainly… But perhaps four times a year she cooked properly, for company".
- Vell's pine board:
  - I first had it "off its nail behind the table", with burned names and strings;
  - ch2 has white-painted names on the back-room wall beside the door;
  - the scene now goes into the back room.
- "Drunk" was removed from the salt-end keeper's account (Reader Standard caution): "sat late in the keeper's kitchen".
- Dace's "thirty years" at the door (not established) is now "since before you were born". Dace's scouted lad is moved from the brickworks to "out past the north gate", so he is not confused with the brickworks Shield.
- Lira's confirming opponent was first "a Stone from the north gate". That is the same gate as the Stone woman corrected down in ch31, so he is now "from up the river".
- Brom's "my read on half the Iron Skin there is" overclaims, because Iron Skin is proprietary. It now reads "every kind of Path that city had in it".
- The read-back:
  - I first had the watcher's weight thin out as Vell went into the back room;
  - that implied a link to Vell;
  - it now thins as Dace puts out the lamps, and Cael refuses to read meaning into either.
- The record window first said "the Tuesday morning" and "that week". That put Coss's note before he wrote it, so the scene now carries no date.
- Coss "three months ago" and Havel's "three months" became "some weeks" and "all season". About seven to nine weeks of story have passed since Havel's visit.
- Vell: "Kindled at fifteen" is now "fourteen" (the series' Kindling age), and "the way your friend found his hardness" is cut, because Vell does not know Brom's history.
- In ch36 the [UNBOUND] reasoning had "It was not about him" and "this was not about anybody". Each is a conclusion the packet forbids in either direction, so both are now plain evidence statements.
- Cael's "Your range is terrible" back to Brom made no sense. It now reads "They're terrible… and so were mine".
- Watcher sightings were respaced (back wall; market "ten days later"; the yard "a week after the market") so that "three in three weeks" holds.

**After all seven existed.**
1. **Scene merges.** Before any measurement, from my own per-scene word counts, I removed six `---` marks that split one continuous scene with no change of place, time or viewpoint:
   - the Shield bout (ch30);
   - the flood into the dispute (ch31);
   - the read into its aftermath (ch32);
   - the review into the supervisor's shelf (ch33);
   - the read-back (ch35);
   - the asking into the back room (ch36).
2. `ed.sh overlap book-02-iron-circuit 5`:
   - first run: **2 unprotected**, one a sentence of mine ("in a way that had nothing to do with") and one the packet's "the read reports presence, not intent. Intent is…";
   - both recomposed;
   - final: **0 unprotected, 6 protected**.
3. `ed.sh gates book-02-iron-circuit 5`: reader_standard=0, metadata=0 and modern=0 on all seven chapters.
4. `sweep_probe.sh book-02-iron-circuit 5 5`, the official run once all seven existed, gives **0% skeleton, 6% close** for the movement. Per chapter: 0/4, 0/5, 1/5, 1/7, 0/8, 0/7, 0/6. The remaining ≥0.50 pairs are the protected Coss reply and two coincidental short sentences.
5. `formula_metrics.py`. **Disclosure:** I ran it three times, not once.
   - The first run, on the finished draft, put sentence mean at 12.86 and ≥40 share at 2.3%, both below their working ranges.
   - I repaired by reading. About 240 hand-chosen joins of short narrative sentences that carried one thought. Each replacement was composed by hand from a read of the chapter: commas, semicolons, colons, *and/but/because*. No sentence was split.
   - The second run, after the repair: all three primaries in range.
   - I then added two short passages to the Havel cutaway and one to the Coss cutaway, to bring them nearer their packet sizes, and fixed the Lira-cooking line. The third run gives the final figures in AUTHOR-REPORT.
   - Untouched by the repair: speech, Log and notebook entries, the protected texts, and fight landing beats ("The lock let go." / "The shoulder dropped.").

I wrote only the seven chapter files and these two state files, plus scratchpad notes and helper scripts outside the repo. I ran no git commands.
