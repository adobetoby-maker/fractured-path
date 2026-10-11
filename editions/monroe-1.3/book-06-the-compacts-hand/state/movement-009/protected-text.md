# Protected-wording and plan audit — Book 6, Movement 9

## Verdict

**CLOSE WITH FIXES.** All six marker units exist in the source and must be restored. The closing inventory also has protected source wording; the packet's protection is not cancelled by its omission from `BOOK_MAP.md` §8. The source last line is binding through the Book 7 seam and must replace the author's paraphrase. Three attribution rulings require repair: Lira, not Brom, first says “Nobody's watching”; “Both promises ride east with me” is a log entry, not speech to Lira; and Karis, not Cael, says/writes “Noted.” Lira's and Brom's two lines in the closing exchange are correct.

The Book 6 calendar is ratified as drafted in substance: Movement 9 enters on day 203, the academic year closes on day 207, the road begins after that close, the Line is crossed on the fifth road day, the first night beyond it is fireless under the cart, and the shelf is the second camp and the first fire beyond the Line. **Book 7's plan must change; Book 6 Movement 9 must not.**

All five new-canon items are ratified. None spends a Book 9 reveal. The last-station sigil remains a plant only: older, foreign stone and a house built round it, with no maker, intent, will or explanation.

Every `old` block below was checked with fixed-string matching (`rg -F`, with `-U` for multiline blocks) and matched **exactly once** in its named file.

Standing-ruling audit: the fixes introduce no season, month or English weekday name and no metric unit; Movement 9 already uses feet and yards. Instrument prose already uses *Caelen Hesk-ward* (`manuscript/chapter-55.md:71`, `manuscript/chapter-58.md:69`). Mandatory departures from source wording are confined to the personnel-query role/calendar/house frame, `Since my Kindling`, `Nine fragments`, and `two renewals on paper`; each is identified below. The ratified day-203/day-207/Line order is preserved.

## A. The six marker units

### A1. Gault's last note — restore in full

Governing text: `BOOK_MAP.md:618` protects “Gault's last note, ending *The instruments will not see its like.*” The complete source unit is:

> *Assay-provision enrollment: resigned in good standing prior to revocation date. Baseline file: closed complete. Four terms of evaluation-linked observation, no adverse finding, no anomaly of conduct. The evaluator of record notes that the file closes on the enrollee's own act and not the registry's, and that this is the correct closing, and the only just one available. The instruments will not see its like.* (`books/book-06-the-compacts-hand/chapters/chapter-21.md:59`)

No standing-ruling change is needed.

### A2. The personnel query — restore, with the edition's required recomposition

Governing text: `BOOK_MAP.md:602-604` protects the personnel query but permits recomposition where a word is wrong for the calendar. The source unit is at `books/book-06-the-compacts-hand/chapters/chapter-22.md:31`. The edition separately rules that Seln is the wing's **teaching assistant**, not its assessment clerk (`BOOK_MAP.md:729-730`), and the drafted scene makes this the house's question to the placing district office (`manuscript/chapter-57.md:43-51`). The calendar fixes Movement 9's opening to day 203 and the following First-day to day 204 (`STATE_LEDGER.md:1168-1172`).

Required changes, all explicit:

- `Assessment clerk` → `Teaching assistant` (edition role).
- `second bell of the twelfth` → `first bell of the First-day` (ratified calendar; no English weekday, season or month word).
- The source key list → the four keys actually left in this edition (`manuscript/chapter-57.md:15-17`).
- `office` → `house`, and the clean-service statement is limited to the two-year posting, because this is the house asking its district office rather than Seln's own office reporting up-chain.

### A3. The waystation board — restore in full

Governing text: `BOOK_MAP.md:602-604` protects the waystation board. Its complete wording is at `books/book-06-the-compacts-hand/chapters/chapter-23.md:17`. The next line's “Twenty days” depends on restoring the whole notice (`manuscript/chapter-59.md:79-81`).

No standing-ruling change is needed.

### A4. Cael to the last Arbiter — restore in full

Governing text: `BOOK_MAP.md:619` protects the unit from “You couldn't read me” through “Thanks for the eleven seconds.” The full source speech is at `books/book-06-the-compacts-hand/chapters/chapter-23.md:95`.

Required standing-ruling change: source `Four years I thought` becomes `Since my Kindling I thought` in first person. The edition requires Kindling-relative wording instead of an incremented count (`BOOK_MAP.md:731-733`; `packets/MOVEMENT-009.md:47`). No other word changes.

### A5. Cael's reply to Daeva — restore the whole reply

Governing text: `BOOK_MAP.md:577` makes the whole reply Tier A, not only the quoted opening fragment. The full two paragraphs and signature are at `books/book-06-the-compacts-hand/chapters/chapter-23.md:145-149`.

No standing-ruling change is needed inside the protected reply. The following sentence does need the separately listed join fix: the restored reply is not usefully described there as “short.”

### A6. The closing exchange's first line — restore the entire Cael utterance

Governing text: `BOOK_MAP.md:622-623` protects the closing exchange, while the marker requests the whole first line rather than its quoted fragment. Cael's full utterance is at `books/book-06-the-compacts-hand/chapters/chapter-24.md:131`.

No standing-ruling change is needed.

## B. The four author flags

### B1. Closing inventory — protected source wording exists

The packet expressly protects “the inventory” (`packets/MOVEMENT-009.md:32`). The source supplies the complete unit from “Nine confirmed fragments” through the anomaly entry (`books/book-06-the-compacts-hand/chapters/chapter-24.md:43-51`). `BOOK_MAP.md` §8's failure to quote it is an omission, not permission to replace it with the chapter-34 form.

Required standing-ruling change: source `Nine integrated abilities` becomes **`Nine fragments`**. All other source wording stays unchanged. The author's second anomaly procedure is removed because the restored source entry already contains the protected anomaly wording and its closing *Still open. Still real. Patience.*

### B2. Last line — the protected seam line is mandatory

Book 6's binding ending places the close on the second day past the Line (`BOOK_MAP.md:67-79`), and the movement packet fixes the pressure line as “for the first time since his Kindling nothing anywhere ... deciding what he is except him” (`packets/MOVEMENT-009.md:45-47`). Book 7 then names the last line exactly:

> “nothing anywhere was deciding what he was, except him.” (`editions/monroe-1.3/book-07-void-roads/BOOK_MAP.md:26`)

The source supplies the sentence's full cadence, with only the standing year-count change required (`books/book-06-the-compacts-hand/chapters/chapter-24.md:145`). The author's three-sentence paraphrase must therefore be replaced.

### B3. Attributions

- **“Nobody's watching.” — wrong.** Lira says it first in the source; Cael then agrees (`books/book-06-the-compacts-hand/chapters/chapter-23.md:111-117`). The manuscript gives it to Brom at `manuscript/chapter-59.md:323`.
- **Closing Lira/Brom lines — correct.** Lira has “Let them escalate. They'll need better maps.” and Brom has “And better roads.” (`books/book-06-the-compacts-hand/chapters/chapter-24.md:137-139`; `BOOK_MAP.md:622-623`). No fix to those two lines.
- **Closing “Noted.” — wrong in the manuscript.** The source gives it to Karis, writing (`books/book-06-the-compacts-hand/chapters/chapter-24.md:141`); the manuscript gives it to Cael at `manuscript/chapter-60.md:355-359`.
- **“Both promises ride east with me.” — wrong as dialogue to Lira.** In the source it belongs to Cael's italic log entry, in a complete six-sentence unit (`books/book-06-the-compacts-hand/chapters/chapter-23.md:155-157`). Restore it as a log entry.

### B4. Calendar and the first camp — change the Book 7 plan

The ratified calendar requires day-203 entry, day-207 close, and a Line crossing after day 207 (`STATE_LEDGER.md:994-1002`, `STATE_LEDGER.md:1168-1172`). The manuscript obeys that order: the last-year frame sits before the road (`manuscript/chapter-58.md:15-23,113`), the Line is crossed the morning after the last station (`manuscript/chapter-59.md:235-305`), the first night beyond it is fireless under the cart (`manuscript/chapter-59.md:351-361`), and the shelf's fire is on the second day past the Line (`manuscript/chapter-60.md:51-53`).

Book 7's source opens “Second day past the Line” (`books/book-07-void-roads/chapters/chapter-01.md:3-11`), and its Movement 1 packet enters on the shelf on that second day (`editions/monroe-1.3/book-07-void-roads/packets/MOVEMENT-001.md:15-17`). Therefore the inconsistent phrase is Book 7 `BOOK_MAP.md:17`, “the first camp beyond the Registry Line.” Change it to the second camp and first fire beyond the Line. When Book 7 is drafted, its source's later “since the first camp” (`books/book-07-void-roads/chapters/chapter-01.md:13-15`) must likewise be recomposed as “since the shelf” or equivalent; do not move or delete Book 6's fireless first night.

## C. New-canon check

### C1. Last station unstaffed four years; stamp in the keeper's drawer — ratified

The map requires the last station's stopped four-year book and open line (`BOOK_MAP.md:310-314`). The manuscript supplies both the unstaffed interval and the delegated brass in the waystation keeper's drawer (`manuscript/chapter-59.md:83-87`), then the register stopping four years ago (`manuscript/chapter-59.md:187-207`). This is compatible local logistics, not a reserved revelation. Book 7's binding entry only requires that the last watcher turned back and the party is outside jurisdiction (`editions/monroe-1.3/book-07-void-roads/BOOK_MAP.md:23-25`).

### C2. A second Denvash visit in one clause — ratified

The single recess clause at `manuscript/chapter-58.md:39` makes the present visit the third, exactly as the Book 6 spine requires (`BOOK_MAP.md:303-309`) and as the binding end state records (`BOOK_MAP.md:86-90`). It reveals nothing of Hesk's reserved history; Book 6's limit remains “letters only” at that altitude (`BOOK_MAP.md:640`), and Book 7 still reserves Hesk's history (`editions/monroe-1.3/book-07-void-roads/BOOK_MAP.md:343-344`).

### C3. Seln burns nineteen bundles of duplicates — ratified

The plan permits Seln's fifteen years of duplicates in his Movement 9 window (`BOOK_MAP.md:488-491`) and requires nineteen postings / fifteen years as his carried history (`BOOK_MAP.md:218-219`). The manuscript burns the nineteen duplicate bundles but preserves the locked case and its different contents (`manuscript/chapter-57.md:93-109`). Book 7's entry still receives Seln with the locked maintenance-record case (`editions/monroe-1.3/book-07-void-roads/BOOK_MAP.md:20-23`). No later reservation is spent.

### C4. New file line on an unsigned slip of advice — ratified

The closing line itself is Tier A (`BOOK_MAP.md:563`), and the spine requires “the faceless window and the new line” (`BOOK_MAP.md:317-323`). The manuscript's unmarked, uninitialled slip (`manuscript/chapter-60.md:307-317`) is a mechanism for that already-required closing entry. It is not a third field move by the faceless faction: the two prohibited-to-exceed reaches remain the escort order and road action (`BOOK_MAP.md:638`; `packets/MOVEMENT-009.md:35`). The text names no office, person, face or location.

### C5. Older foreign sigil-stone with the station built round it — ratified as the Book 9 plant

Canon withholds “The Arbiter system is the Architect's infrastructure” until Book 9 and requires at least two Book 6 plants (`universe/CANON_RULES.md:46-52,58-68`). Book 6 expressly allows the last station's sigil to be older than the paper around it, while forbidding a named maker, intent or will (`BOOK_MAP.md:635-636`). Book 7 likewise allows only plants at that altitude and forbids explanation or Arbiter activity (`editions/monroe-1.3/book-07-void-roads/BOOK_MAP.md:327-333`).

The manuscript stays inside that boundary: the stone is foreign to the hill, the masonry is cut around it, the founding leaf says the station was established *at the sigil*, and the conversation stops at “It says *at*. That's all the paper there is.” (`manuscript/chapter-59.md:211-229`). No maker, purpose, will, Architect, infrastructure or mechanism is supplied. Keep as written.

## Exact fixes

1. `manuscript/chapter-55.md`

   old:

   ```text
   [[TIER-B: Gault's last note, ending *The instruments will not see its like.* — coordinator to supply protected text]]
   ```

   new:

   ```text
   *Assay-provision enrollment: resigned in good standing prior to revocation date. Baseline file: closed complete. Four terms of evaluation-linked observation, no adverse finding, no anomaly of conduct. The evaluator of record notes that the file closes on the enrollee's own act and not the registry's, and that this is the correct closing, and the only just one available. The instruments will not see its like.*
   ```

2. `manuscript/chapter-57.md`

   old:

   ```text
   [[TIER-B: the personnel query — coordinator to supply protected text]]
   ```

   new:

   ```text
   *Teaching assistant, Bronze grade, fifteen years' service, absent without notice from first bell of the First-day. Residence room found vacated; no personal effects; bed made. All working files completed and cross-indexed to date. Inner-door key, records-press key, post-room key and wing side-door key surrendered on the copying-table blotter. Floor schedule posted one week forward. No note left, no leave applied for, no address of forwarding held by this house. The house records no disciplinary matter, no irregularity of any kind in the two years of this posting, and no view as to cause. Query submitted to the placing district office per code; direction requested.*
   ```

3. `manuscript/chapter-59.md`

   old:

   ```text
   [[TIER-B: the waystation board — coordinator to supply protected text]]
   ```

   new:

   ```text
   *By charter of the registry, this house being chartered: TIER VERIFICATION available at the district station, Ostrand, four days west. No station lies east of the river crossing, and the station at the ford is unstaffed. TRAVEL ENDORSEMENTS may be lodged at this house for forward transmission; allow twenty days. ENROLLMENT INQUIRIES by the same. The chartered rates of this house are posted within. Complaints of a chartered house lie to the district seat.*
   ```

4. `manuscript/chapter-59.md`

   old:

   ```text
   [[TIER-B: "You couldn't read me… Thanks for the eleven seconds." — coordinator to supply protected text]]
   ```

   new:

   ```text
   "You couldn't read me," he told it, conversationally, the way you tell a fact to an old machine. "Since my Kindling I thought that was the system failing. Turns out it was the most honest thing the system ever did — the one time the layer under you couldn't finish its job, because there was no bin beneath me to file the lie in." He looked at the dark frame a moment longer. "You're the only part of the whole apparatus that never lied about me. You just went quiet. Everything above you did the lying." He shouldered the satchel. "Thanks for the eleven seconds. They were the truest measurement I ever got."
   ```

5. `manuscript/chapter-59.md`

   old:

   ```text
   [[TIER-B: Cael's reply to Daeva (Tier A: *The rematch stands. Not postponed — relocated. It happens on a floor nobody owns…*, whole) — coordinator to supply protected text]]
   ```

   new:

   ```text
   *They ruled. We left — resigned, before the date, in good standing, four files closed complete and one man who filed nothing. You said keep myself unclassified. Done, permanently, on my own paper this time: I'm past the Registry Line, where the word has no meaning, which turns out to be the only place the word is safe.*

   *The rematch stands. Not postponed — relocated. It happens on a floor nobody owns, and I think you'd prefer that anyway; a Gold-tier fact and an unclassified one, fighting where no seal can score either of us, is the only honest version of the bout, and we both knew it at Norhold. Find me when you're ready to fight something no ladder built. I'll be east.*

   *— C.*
   ```

6. `manuscript/chapter-59.md`

   old:

   ```text
   He read it over once. It was short, and it was true, and there was nothing in it that he would have minded a clerk copying. He folded it in three and wrote her name on the outside, and *Auremont*, and nothing else.
   ```

   new:

   ```text
   He read it over once. It was true, and there was nothing in it that he would have minded a clerk copying. He folded it in three and wrote her name on the outside, and *Auremont*, and nothing else.
   ```

7. `manuscript/chapter-60.md`

   old:

   ```text
   [[TIER-B: the closing exchange, first line (Cael: "I have nine things that aren't a Path…") — coordinator to supply protected text]]
   ```

   new:

   ```text
   "I have nine things that aren't a Path," Cael said, eventually, to nobody in particular, "no tier, no rank, no enrollment, no protection — and four people who signed out of the world that was supposed to provide them, and one of the nine taken from a hand the world sent to hold me, and one taken in earnest from a friend, and the machine's own maintenance records in a case under that canvas, which we can't file and can't publish and are carrying east anyway because the truth is worth carrying even when it can't be spent."
   ```

8. `manuscript/chapter-60.md`

   old:

   ```text
   *What I carry: nine confirmed.*

   *Wind-adjacent — Lira, the burst. Pressure-adjacent — the Bronze from Ardenmere, the push. Iron-adjacent — Brom, the read. Compression-adjacent — Reydan, the give; a cup, and not for edges. Ember-adjacent — Karis, the spark. Shadow-adjacent — the stair; sealed, on his terms; rent from waking. Storm-adjacent — Daeva, the lane; ten counts after, a bill and not a flag.*

   He came to the eighth and wrote its first word. Then he lifted the pen and moved it along the line, and set it down again further on.

   *Anchor-adjacent —            ; the hand with no face. Idle by naming. Asked nothing at the Line.*

   *Blade-adjacent — Ephram. Idle by naming. Agreed with, once, on a scree.*

   *Spent since the Line: nothing. Not one of the nine.*

   *Under all nine, the still place I don't count.*
   ```

   new:

   ```text
   *Nine confirmed fragments.*

   *Wind-adjacent — Lira. Pressure-adjacent — Feryn. Iron-adjacent — Brom. Compression-adjacent — Reydan. Ember-adjacent — Karis. Shadow-adjacent — source protected, sealed still, the logic updated and the discipline held: a defector's tradecraft in my hands would confirm the surveillance-era acquisition, so the seal stays, and Seln knows now that it does, and knows why, which changes nothing about the seal and everything about the debt. Storm-adjacent — Daeva. Anchor-adjacent — unnamed; the hand with no face; the piece of the machine itself. Blade-adjacent — Ephram; the only "non-hostile" in the log; taken in earnest from a friend who asked to be shown straight.*

   *Nine fragments. Each with a name beside it, one of them protected and one of them missing — and the missing line I have left blank on purpose, because the blank is the truest thing the entry says.*

   *One anomaly. Session nine. Tide-adjacent. Turned over once, per the custom at intervals that matter — checked against the cache, checked against everything the cache explained, and touching none of it. Still open. Still real. Patience.*
   ```

9. `manuscript/chapter-60.md`

   old:

   ```text
   That left the last thing, which was not a line, and had a procedure.
   ```

   new:

   ```text
   The anomaly entry had a procedure behind it.
   ```

10. `manuscript/chapter-60.md`

   old:

   ```text
   He opened his eyes and wrote the three words under the inventory. He had written them before, on a sill, on a birthday.

   *Still open. Still real. Patience.*
   ```

   new:

   ```text
   He opened his eyes. The three words stood under the inventory, as they had stood before, on a sill, on a birthday.
   ```

11. `manuscript/chapter-60.md`

   old:

   ```text
   *I can work within the system. I have the receipts: a hearing, a provision, a stamp renewed four times, a tournament their own clause put me in. The system has text, and text has held me every time the people failed. This is more text. We'll read it better than they do. We always have.*
   ```

   new:

   ```text
   *I can work within the system. I have the receipts: a hearing, a provision, two renewals on paper, a tournament their own clause put me in. The system has text, and text has held me every time the people failed. This is more text. We'll read it better than they do. We always have.*
   ```

12. `manuscript/chapter-59.md`

   old:

   ```text
   "Nobody's watching," said Brom.
   ```

   new:

   ```text
   "Nobody's watching," said Lira.
   ```

13. `manuscript/chapter-59.md`

   old:

   ```text
   "That's one," said Lira. She was wringing out her sleeve. "There were two. The Compression. Reydan. He told you to find him later, and you've never written to him."

   "No. I've nothing to tell him yet. He asked a question, and I haven't the answer."

   "But you mean to."

   "I mean to. It's the same debt as hers. It only wants longer." He pulled the satchel's strap straight on his shoulder. "Both promises ride east with me."
   ```

   new:

   ```text
   The log banked the thread beside its lineage:

   *Reydan wanted the answer when I have it. Daeva wants the rematch with whatever I am. Both promises ride east with me. Both get kept. Not yet. The road's long and it runs the right direction.*
   ```

14. `manuscript/chapter-60.md`

   old:

   ```text
   "Noted," he said.

   He did not write it down. The book stayed shut.
   ```

   new:

   ```text
   Karis wrote one word in the field archive.

   "Noted."

   Cael did not write it down. His book stayed shut.
   ```

15. `manuscript/chapter-60.md`

   old:

   ```text
   He had not been without that column since his Kindling. There was nothing left anywhere that was deciding what he was. There was only him.
   ```

   new:

   ```text
   And for the first time since his Kindling, nothing anywhere was deciding what he was, except him.
   ```

16. `editions/monroe-1.3/book-07-void-roads/BOOK_MAP.md`

   old:

   ```text
   - **Where/when:** the switchback shelf above an unnamed valley, the first camp beyond the Registry Line. Book 7 dates everything *past the Line*: Book 6's "sixth day" from Ostrand is Book 7's **second day past the Line**.
   ```

   new:

   ```text
   - **Where/when:** the switchback shelf above an unnamed valley, the second camp beyond the Registry Line and the first fire beyond it. Book 7 dates everything *past the Line*: Book 6's "sixth day" from Ostrand is Book 7's **second day past the Line**.
   ```
