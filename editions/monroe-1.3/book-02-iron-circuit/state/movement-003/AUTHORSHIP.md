# AUTHORSHIP — Book 2, Movement 3 "Iron Skin" (chapters 16–22)

| Field | Value |
|---|---|
| Public byline | Monroe Jackson |
| Seat | `oconnor` 1.3.0 |
| Foundation | Monroe Jackson 1.3.0 |
| Requested author | Opus (Claude Opus 5.5) |
| Actual runtime model | `claude-opus-5-5` (Claude Opus 5.5), as stated in this session's environment |
| Packet | `editions/monroe-1.3/book-02-iron-circuit/state/movement-003/compiled-prompt.md` (movement brief: `editions/monroe-1.3/book-02-iron-circuit/packets/MOVEMENT-003.md`) |
| Edition | `monroe-1.3` |
| Book | The Fractured Path, Book 2 — Iron Circuit |
| Chapters | `editions/monroe-1.3/book-02-iron-circuit/manuscript/chapter-16.md` … `chapter-22.md` |
| Date | 2026-10-04 to 2026-10-05 |

**One author, one interruption.** All seven chapters were written by the same author (this model) in one run, with one pause in the middle.

**The disk-full pause.** While I was revising ch21, the data volume reached 100% (117–196 MB free). The Bash tool could no longer write its output, and one Edit to ch21 failed. I checked with Read that ch21 was intact. Then I stopped writing so that no manuscript file could be truncated. At that point ch16–21 existed as drafts, ch22 did not exist, and no checks had been run. I touched nothing outside this book; the files filling `/private/tmp` were not mine. The coordinator freed the disk (112 GB available) and told me to resume. I resumed from the same notes and applied the five replacements I had composed for ch21 before the pause. No other agent or model touched these chapters.

**Reading before drafting.**
- The compiled prompt in full:
  - the profile;
  - formula sections 2–6 and 8–9;
  - the packet;
  - the edition brief (event-list method, 8-word gate, working ranges);
  - BOOK_MAP §§1–12, including §8 items 22 and 24 and §11 a, g, k, m, r and s;
  - STATE_LEDGER through "After Movement 2" and its coordinator rulings;
  - CANON_RULES.
- The end of Movement 2 (this edition's ch14–15).
- Book 1 `chapter-24.md`, for Coss's voice.
- `craft/NAME_REGISTRY.md` collision #6.
- The Book 2 rule that "Iron Skin" is always spelled in full.
- Source `books/book-02-iron-circuit/chapters/chapter-08.md`, `chapter-09.md` and `chapter-10.md`, each read once and then closed.
- On resuming, I re-read this edition's ch16–21 in full, to carry state forward, and the M3 portion of the compiled prompt. I did not reopen the source.

**Method.** After the single read of the source, I wrote a private event list in my own words, outside the repo. For the resumed part I wrote a second list in the scratchpad: ch22's five beats and the lengthening scenes. I drafted from those lists and the book map with the source closed. Protected wording (BOOK_MAP §8 items 22 and 24) was copied from the map.

**Drafting.** The seven chapters were written forward in order. No formula tool was run between chapters. To lengthen the movement toward the ~37,000 budget, I added these scenes and passages after the pause, all from the event list:
- ch17: Cael reads Brom's eight lines in Vell's book; the first-bout loss, "Did not know the floor."
- ch18: Keth at dawn on Brom's coppers ("Eyes open").
- ch19: the letter to Hesk; the interim bout given room (Orvet's corner, the first exchange, the Blade's question afterward).
- ch21: the five replacements and the corner conversation given room; the kitchen supper the night before Wendel (the heavyset man "went down").
- ch22: all of it.

**Blocking slips fixed as noticed.**
- Red Cap is a boy. I had drafted him as "she".
- Keth holds a practice blade, not a stick. Invented details about his ring were removed.
- Invented Hesk lines and Book 1 travel details were removed from the letter scene.
- Two continuity slips: the heavyset man's "last week" and Wendel's tense in ch22.
- The challenger, not Cael, chooses the mark.

**After all seven existed.**
1. `ed.sh overlap book-02-iron-circuit 3`:
   - First run: 12 unprotected runs (ch16 ×3, ch17 ×4, ch19 ×4, ch20 ×1). Two of them were packet lines whose wording I had carried too far: "leave it home… half-carry" and "what does the hardening cost him". Each sentence was recomposed in context.
   - Final: **0 unprotected, 2 protected**.
2. `ed.sh gates book-02-iron-circuit 3`: reader_standard=0, metadata=0 and modern=0 on all seven chapters, both before and after the probe repairs.
3. `bash editions/monroe-1.3/tools/sweep_probe.sh book-02-iron-circuit 3 3`. The script resolved the packet's actual sources, ch8, ch9 and ch10.
   - First run: **2% skeleton**, with ch19 at 5%. Ch19's scene 1, the self-inventory, was at 13%: it had followed the source's sentence order from memory. Ch20, ch16 and ch17 each had a few close sentences.
   - Every flagged sentence that was not a packet quote was recomposed. Changes included: the Log laid out with the salt cellar, not the source's whetstone; "a spare coat… a knife with the handle pointed at me"; "the Log sits on the bench"; the drill, ceiling and account lines in ch20; and Vell's recommendation reworded ("Her line to stand at Iron-equivalent, provisional, until two more bouts confirm it").
   - Final: **0% skeleton, 9% close** across the movement; no chapter above 1% skeleton. The remaining close pairs are the packet's own lines (Corrin's water and wall, Cael's "to understand what I am…") and one coincidental pair.
4. `formula_metrics.py`, run once on the seven chapters (see AUTHOR-REPORT).
5. After the metrics, one change by reading: two scene breaks in ch22 were removed where the scene runs on continuously (dawn at Vell's table → the side-door step; the noon session → the conversation on the bench). No text changed. This takes the movement from 43 to 41 scenes. I did not re-run the metrics; the report gives the arithmetic.

I wrote only the seven chapter files and these two state files, plus a scratchpad event list outside the repo. I ran no git commands.
