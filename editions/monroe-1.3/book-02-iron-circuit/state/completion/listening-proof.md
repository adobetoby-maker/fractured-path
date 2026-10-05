# Book 2 — *Iron Circuit*: line and listening proof (Step 4)

Reader: Claude Fable 5.1, review seat, fresh context, 2026-10-05. Scope: `manuscript/chapter-01.md` … `chapter-60.md`
(287,541 words by `wc`), read in order as a Breeze narrator will meet them: one segment per paragraph, `---` as a long
pause, italics flattened, fenced notices flattened line by line. Read first: Book 1's and Book 3's `listening-proof.md`
(the models), `COMPLETION-PLAN.md`, `whole-arc-read.md` (§8 fixes applied), `LANE-A-REPORT.md`, `LANE-B-REPORT.md`,
`EDITION_BRIEF.md` (audio, Reader Standard), `OWNER-DECISIONS.md` #3, #33, #36, `BOOK_MAP.md` §8–§10, and
`audio/fpaudio.py`. A script swept all 60 files first (quote and asterisk parity, break spacing, brackets, numerals,
abbreviations, doubled words, paragraph ends and starts, name pairs per scene, homograph contexts, every ", as" clause,
paragraph lengths); the read then went through every chapter. Running notes: `listening-notes.md`.

**No manuscript file was modified.** Every fix below is a proposal; each old string was verified with `grep -c -F` to
match exactly once in the named file and once in the manuscript. No fix touches a protected line (BOOK_MAP §8) or the
record window (§9). The redirect shoulder is RIGHT throughout (#36); Bede and Maud are drafted under the owner-pending
names and are not a finding (#3); Cael = KAYL and Lira = LEER-a (#33).

---

## 1. Verdict

**Render-ready after 6 small text fixes: 5 mechanical (an abbreviation an engine would voice as a non-word, in a ledger
line, a margin note read aloud, and a chalk notice) and 1 broken join left by the texture pass (ch28).** One further
optional fix for engine safety (ch24). Nothing structural stands in the way:

- Quotation marks: every paragraph in all 60 chapters has an even count of `"` (straight quotes only; no curly quotes
  anywhere). No unbalanced or mismatched quotes, and no multi-paragraph open quotation at all; every speech closes in
  its own paragraph. No double-in-double nesting: the 18 "quote inside a quote" cases (Cael reading his page aloud ch31,
  Brom reading the clerk's account ch48, Vell's slate and ledger lines read out) use italics inside the speech.
- Italics: every paragraph has an even count of `*`. No `_`, no `**`, no stray markdown of any kind.
- `---`: all 255 breaks have a blank line before and after. No setext accidents, no double hyphens, no slashes.
- Attribution: no speech paragraph whose speaker a listener cannot place. The three-person suppers (ch32, ch41, ch45,
  ch46, ch48, ch56, ch59), the kitchen-table crowd scenes (ch21, ch23), the bouts, the cookshop (ch46, ch59) and
  Quenna's approach (ch54) all carry by tags, by alternation or by the content of the line; the one place alternation
  misleads (ch28, "he said" straight after Brom's own line) is fix 5.
- Ear collisions: Doss, Marrow, Kestrel, Halvern, Talis and Corbin do not occur in Book 2; the live pairs are all
  distinct by ear (§2.2). Brom and Bede never share a spoken list; they share one narration run (ch50), noted for
  direction.
- Protected lines: every §8 item is present verbatim (grep over flattened text; the five that a literal search misses
  are lines split by a speech tag or ending in a comma before the tag). The §9 record window (ch35) states only what
  §9 allows.
- Doubled words, lower-case starts, mid-clause ends, tense slips from the lanes: none found beyond the ch28 seam. The
  32 "had had", "kind to you you'll" (ch27) and "told it it would" (ch53) are grammatical; the one lower-case start is
  the protected index line (ch35); the one unpunctuated paragraph is a letter salutation (ch5 "*Cael,*").

What remains is for the direction files, not the text: the homographs an engine will misread (`wound` round a hand,
`lead` foot against the `lead` seam, `the read` as a noun, `live` as an adjective, `bow` as a window and once as a
gesture); the all-caps Log headings, bill and plates, which should be rendered in sentence case; the single letters in
the ledger and Log (`L.`, `B.`, `C.`, `H.`, `Q.`, `W`, `t.f.`, `h`, `def.`); and the POV cutaways, which change the
referent of "he" or "she" at a `---`.

---

## 2. Findings by category

### 2.1 Quotation marks and attribution

- Balanced throughout (0 odd-quote paragraphs, 0 odd-asterisk paragraphs, 0 curly quotes, script-checked).
- **Italics carry six different things**, and the narrator needs to know which: (a) the Power Log and the grey book
  (field headings, entries, the *Carrying* and *Anomalies* columns, the two columns *Habit* / *Shape*); (b) Vell's
  ledger lines and chalk (the slate, the bill, Dace's notes, the betting man's board); (c) letters (Hesk's ch5, ch10,
  ch30, ch43, ch57; Cael's ch8, ch19, ch41, ch57; the salt-end keeper's ch31; Lira's postscript ch57); (d) documents
  read as text (the Compact file and index ch14, ch15, ch17, ch33, ch35; the clerk's account ch48; the old ledger and
  its margin ch36; Quenna's provision ch54, ch57); (e) remembered or reported speech (*fight me properly and I'll stop
  you every time it comes*; *Don't read me tonight*; *Lad, that's a copper*); (f) inner thought and stress. The split is
  always clear from the surrounding sentence; the direction file should say which is which per segment.
- Read text inside speech (18 paragraphs): ch31 Cael reads his own page to Vell's table; ch48 Brom reads the clerk's
  fourth page aloud ("*In the spring of the second season the subject lost once…*"); ch9 Cael reads Vell's margin
  ("*opp. tried the spinning cut*" — fix 1–2). Direct as a voice reading aloud, flatter than its own speech.
- Interruptions: 7 paragraphs end on `—"`, all cut-off speech ("Did you see—" ch26; "I can—" ch26; "Is Wendel—" ch31;
  "She's not my—" ch32; "That's—" ch33; "My classification—" ch54). They need the engine's short gap and no falling
  cadence. One overheard dash-opening line.
- Counts said aloud: Lira's "One" … "Ten" and "*one-and-two-and*" (ch5, ch8, ch17); Brom's "That's forty" (ch29); the
  knock tallies ("Twelve in twenty", "Three in five", ch46–51); the bout count "*and one, and two*" with the bursts on
  the *three* (ch53). Keep the deliberate count rhythm.
- "Hm." (Vell ch4; the heavyset man ch5), "Huh," (Lira ch7), "Dunno." (Red Cap ch15), "Oh," (ch26, ch60): may be
  dropped or stretched by the engine; check the render. No "Mm" in Book 2.
- Vell's spoken result lines ("Called. Hand up. Fifth exchange."; "Iron-equivalent, Cael. Win. Method: forced
  incapacitation, fourth exchange.") are in quotes; her written lines are in italics. The quotes-vs-italics
  distinction carries the difference, as in Book 1.

### 2.2 Ear collisions

**Names in one scene.** A script split each chapter on `---` and counted name pairs per scene:

| Pair | Risk | Scenes together | Note |
|---|---|---|---|
| Coss / Doss | high | **none** | Doss does not occur in Book 2. Coss (ch3, 14, 15, 17, 33, 35, 41) = KOSS, clipped. |
| Darrow / Marrow | high | **none** | Marrow does not occur. Darrow Innes is named ch1, 2, 5, 6, 7, 8, 45, 59 (DARR-oh, as "arrow"). |
| Keth / Kestrel | high | **none** | Kestrel does not occur. Keth = KETH (as "Beth"). |
| **Brom / Bede** | medium | ch43 s1; ch45 s4; ch50 s5; ch53 s1 | Never in one spoken list. One narration run, ch50 "as he had learned from Brom and from Bede": give Bede its long E (BEED) and Brom its short O; no text change needed. BOOK_MAP §10's by-ear screen holds. |
| Vell / Dace | low | 65 scenes | The two keepers, constantly together. VELL vs DAYSS (as "face"); Vell writes, Dace chalks; attribution carries. |
| Vell / Velmere | low | ch16; ch32 s3; ch56 s3 | VELL vs vel-MEER; give Velmere both syllables (Book 3 direction). |
| Keth / Hesk | low | ch22 s5; ch41 s4 | KETH vs HESK; different onsets; never adjacent. |
| Dravin / Dace | low | ch10–11, 14 | DRAV-in (short a) vs DAYSS. |
| Dessa / Dace | low | ch4 s2 | DESS-a vs DAYSS. |
| Maud / Dace | low | ch43, ch56, ch60 | MAWD vs DAYSS. |
| Havel / Cael | low | ch14–15 (same chapter, different scenes) | HAV-el vs KAYL; different stress. |
| Reydan / Renn; Ansel / Hesk; Ulric / Orvet; Lira / Ilsev; Sarel / Feryn / Darrow (ch45 list) | none | — | distinct by ear. |

No rename is proposed (decisions #3, #6).

**Homographs.** All occurrences were read in context; none is ambiguous to a human narrator. These are the ones an
engine is likely to voice wrongly, with the intended reading (for the lexicon/instruct files):

| Word | Intended | Where |
|---|---|---|
| wound (past of wind, WOWND) | 13 of 14 | cloth "wound round" a wrist/hand, "hands wound", "his wound hands": ch9, 13, 18, 20, 23, 24, 29, 35, 37, 38 ×2, 39; ch48 "the way a spring is wound". **Exception:** ch8 "a half-breath that was no longer only a wound" = WOOND (the injury). |
| lead (LEED, the front limb) | 20 | "lead hand/foot/forearm/shoulder/knee/shin/arm": ch1, 5, 20, 22, 24, 30, 31, 34, 42, 50. |
| lead (LED, the metal) | 5 | ch22 "filled with lead"; ch23 "filled with lead"; ch24 "the long lead seam", "the lead seam"; ch59 "the lead seam". ch24 has both in one sentence ("his lead foot came down across the long lead seam") — fix 7, optional. |
| the read (REED, noun) | 84 | Brom's read, "the read on him", "a read burst", "his read lost me". Always REED; "had read" / "read it" (past) = RED. |
| tear(s) | — | ch31 "the tears ran" = TEERS; ch36 "If it tears at the corner, it tears" = TAIRS. |
| bow (BOH) | 11 | tape bows ch2, 4, 36; "like a bow" and "the bow's moment" ch20; "a drawn bow" ch40; "bow window" ch56, 57. **Exception:** ch59 "a small bow of the head … the same bow" = BAU. ch30 the rope "bowed" = BOHD. |
| live (LYV, adjective) | 7 | ch20 "Find it live", "*Live.*", "live, after three fast"; ch21 "seen it once, live"; ch24 "found live" ×2; ch43 "a live thing". LIV (verb) elsewhere: ch23, 25, 43 ×2, 49, 55, 59, 60. |
| lives | — | LIVZ (verb): ch13 "She lives in the build", ch14 "He lives here", ch41 "Who lives over there", ch44 "where the middle lives". LYVZ (noun): ch3, ch41, ch54. |
| wind / Wind / Winds | all | the Path (noun) and its practitioners; "winding the cloth" (ch20, 27, 37, 39) = WYND-ing. No "wind up / wind back" verbs. |
| row | all | ROH: the market row, the row (the street), in a row, rows of benches. No quarrel-rows. |
| present(s) | — | PREZ-ent, a gift: ch5, ch40 ("offering him presents"), ch47. |
| minute | 24 | all time-uses. |
| record(s), subject, refuse, separate, contract, digest, permit, content | — | all read naturally in context (nouns and verbs clear). |

**"As" after the lanes' conversions.** All 350 ", as …" clauses were listed and read. Nearly all are habitual ("as he
always did", "as she did most nights", "as the ration had taught him") or manner ("as a man holds a ticket for a coach
he is not sure he wants to catch") and cannot be heard as "while". The temporal ones are literal and correct (ch3 "as
the months went on"; ch5 "as it landed"; ch11 "as she came in close"; ch14 "as he was putting it away"; ch33 "as she
went on behind him" and "as he attended"; ch43 "as the blow came"; ch48 "as Brom threw the slow push at the wall";
ch55 "as Cael passed"; ch59 "as he passed … as she passed"). **No fixes.** One direction note: ch29 "a drop, sharp,
all at once, as the hip went" reads either way and is right either way.

**Accidental rhymes / repeats in adjacent sentences.** None worth a fix. The only aloud stutter is the doubled coat in
ch28 (fix 5).

### 2.3 Formatting the narrator meets

- **Code blocks** (4): ch7 and ch8 FRAGMENT UPDATE (Wind; §8.12, recopied), ch28 FRAGMENT ACQUIRED (Iron; §8.1), ch58
  FRAGMENT ACQUIRED (Compression; §8.8). All protected text. `fpaudio.py` strips the fences, keeps each line and adds a
  full stop. Read as notices, each line its own beat, brackets silent: "Fragment acquired. Unnamed — Iron-adjacent.
  Duration: sustained. Integration: partial. Tier equivalent: unknown. Note: surface-awareness component. Pressure
  read, limited range." Each block gets its own segment and a long pause (direction note 4).
- **`[SHATTERED]`** (6 places, all documents): ch14 the standing instruction ("any monitoring file of the [SHATTERED]
  class") and the folder (*[SHATTERED].*), ch15 and ch17 the file leaf, ch33 the classification. Brackets are never
  voiced. The spoken and narrated word is plain: ch4 "The registry's word for him was *Shattered*", ch6 "as the
  registry had pinned *Shattered*", ch26 Cael says "Shattered" to Brom. **`[UNBOUND]`** ch36, in the old ledger's
  margin (§8.3), brackets silent; Cael's copy *UNBOUND* without them. **`[unnamed]`** in narration ch6 ("a name that
  was not a name, unnamed") and in the two ACQUIRED blocks; **`[Wind-adjacent]`** in the UPDATE blocks. No other
  brackets in the book.
- **The Log in italics.** The six fields with caps headings (*WIND-ADJACENT.*, *WHAT IT IS.*, *SOURCE.*, *CONDITIONS.*,
  *DEPLOYMENT RANGE.*, *COSTS.*, *OPEN QUESTIONS.*; ch6, 9, 17, 20, 29), *REVISIONS.* (ch8), *IRON-ADJACENT.* (ch29),
  the knock columns (ch51 "*At rest: 12, 14, 16.*" etc.), the *Carrying* lines ("*L., through the wall. Didn't.*",
  "*B., across the table. Did. Didn't ask. Will.*", "*The old man at the dray. Did. Didn't ask. Stopped.*"), the
  *Anomalies* leaf with its *Note* line (§8.5), and the grey-book habit-marks (*the finger*, *the drop*, *the tally*,
  *the hip*). Direct the caps in sentence case, each field its own beat; the single letters as letter-names.
- **Numerals vs words.** The book writes nearly every number in words. The numerals that remain all read naturally:
  ch2 "a *3*, in pencil" ("a three"); ch6 "PATH DECLARATION — COPPER RANK 1", "Rank 1", "Rank 2", "Rank 10"; ch30
  "*money 9, gyms 3, rules 1*"; ch33 and ch35 "Priority Level 4", "Level 4", "Section 12"; ch44 "Bronze Rank 1"; ch51
  the knock columns. "Section Twelve" (narration) and "Section 12" (documents) both occur and both read the same.
  No "0", no ordinals in numerals, no "4TH". No registration numbers in Book 2.
- **Abbreviations.** The ones with no in-text decoding are fixed in §3A: "opp." (ch9, read aloud), "Iron-equiv."
  (ch11, ch14 ledger lines; ch17 and ch22 use the full word), "Fri." (ch37 chalk). The ones that stay: "def." (ch1
  "assessed-Copper, def. Ulric"; ch14 "Wind. def. —") is Vell's ledger form carried from Book 1, where the same form
  is protected (ch59); direct it as "defeated", as Book 1 does. "t.f." (ch2, ch31) is decoded by the text ("*Told,
  face.*"); "h" for heard (ch3, 6, 7) is decoded by the text. Initials: "L." (= Lira in the Log; = lost in Vell's
  ch11 line "L. to Dravin"), "B." (Brom), "C." (Cael), "H." (Hesk; Havel in the file), "Q." (Quenna), "W" (ch1
  margin), "R" none. Say the letter.
- **All-caps lines** (engines sometimes spell them): the Log headings above; *OFFICIALS* (ch3); *UPDATE* (ch7); the bill
  *MAIN FLOOR* / *BROM. IRON SKIN. IRON-EQUIVALENT.* / *CAEL. ASSESSED.* (ch22); the plates *EAT, L SAYS* (ch47), *EAT.
  L. SAYS.* (ch55), *EAT. BOTH. ALL THE WAY THERE.* (ch59, three different plates on purpose); *DOES THE FORM ASK FOR HIS
  FAMILY* (ch56, underlined). Render in sentence case (renderer substitution, as Book 1); no text change.
- **Em-dashes**: closed throughout; spaced " — " appears only inside ledger, chalk and letter lines (ch6 "PATH DECLARATION
  — COPPER RANK 1"; ch14 "def. —"; ch18 "*Can't move off it — tried.*"; ch37 "*Coast courier — results — Fri.*"; ch48
  "*— L.: Maud did it to me.*"; ch57 "*Ulric — Cael*", "*— L.*", "*— C.*"; ch60 "*C. — gone east.*") and in the
  protected §8.11 line. All are pauses, never "dash".
- **Scene breaks**: 255, all correctly spaced (134 in ch1–30, 121 in ch31–60, as the lanes reported).
- **Whitespace**: one trailing space (ch50 line 179). `fpaudio.py` splits and rejoins on whitespace, so it has no audio
  effect; listed only.

### 2.4 Line-level typos and grammar

- Doubled words: 32 "had had", "kind to you you'll" (ch27), "told it it would" (ch53). All grammatical. No true doubles.
- Broken joins: **one**, ch28. Lane A cut the mouth-corner beat after §8.2 ("Good. That means you get to choose the
  word.") and the seam shows eight lines on: Brom "took the coat off the nail at last" (line 212), then "reached for his
  coat on its nail" (line 220) before he "put the coat on". The same paragraph opens `"Not tomorrow," he said.` straight
  after Brom's own line `"I know you have," said Brom.`, so a listener hears a change of speaker that is not one; the
  content ("I've had the read two years. Since my station.") corrects it a sentence later. Fix 5 does both.
- Mid-clause ends, lower-case starts, tense slips, dangling comparisons where a simile was cut: none found in 60
  chapters. Lane B's added ch43 line and the arc read's 16 fixes all sit clean in context (checked each in place).
- Spelling: British throughout; "recognized" (ch2) and "specialize" (ch54) are the only -ize forms. No audio effect.

### 2.5 Paragraphs over about 700 characters

165 paragraphs (flattened: asterisks removed, whitespace collapsed, as the segmenter sees them). Listed only; none is a
defect, and `fpaudio.py` splits them at sentence boundaries. The direction file should mark the split so it does not land
mid-thought; the first sixty characters of each are given so it can be found.

| ch | chars | opens |
|---|---|---|
| ch01 | 899 | There was a page in the observation book about it, the newes… |
| ch01 | 842 | It was where the page had said it would be. Every time Ulric… |
| ch01 | 775 | His weight came back into his heels all at once, and he was … |
| ch01 | 821 | It was a standard purse for an assessed bout: twelve marks b… |
| ch01 | 745 | She had been the one to find the lock. It had been in the we… |
| ch01 | 843 | Her own leg ached a little. Not from anything that had been … |
| ch01 | 767 | She knew her own ledger by heart, and it was short. Wind Pat… |
| ch01 | 1254 | It was a year and some weeks now since he had come into Arde… |
| ch01 | 786 | The shelf was the thing he looked at first every evening. At… |
| ch01 | 958 | He sat down at the crate desk with the lamp and copied the m… |
| ch02 | 723 | "Then the string was bad somewhere. A link I thought was sou… |
| ch02 | 782 | "You know what we say before a bout. Nobody dies in the circ… |
| ch02 | 824 | "Darrow was empty." She did not seem surprised that he had a… |
| ch02 | 786 | "Every season. A registered venue. Licensed bouts. A modest … |
| ch03 | 959 | The market had not changed, and it had changed completely. T… |
| ch03 | 841 | That was the strangest thing on the officials page, and the … |
| ch03 | 736 | "He looked in," she said. "The young one. On the way past th… |
| ch04 | 1018 | Cael knew him a little, as you know anybody you have watched… |
| ch04 | 883 | He wrote, that evening, under the box with the four steps an… |
| ch05 | 748 | He went at her. The floor went short, and the half body's wi… |
| ch05 | 906 | And this time he did not want to be out of it. He let it hol… |
| ch05 | 729 | He had not known, until that day, how much of him was the bu… |
| ch06 | 848 | He had been meaning to look at it for weeks. He had kept the… |
| ch06 | 840 | He found four other lines like it, once he started looking. … |
| ch06 | 972 | And they went somewhere. That was the other thing about them… |
| ch07 | 763 | "Not known," said Lira. "I had a feeling, and then I had a g… |
| ch07 | 757 | She showed him with the staff, slowly at first. She did not … |
| ch07 | 763 | She came at him from his left, again and again, each time a … |
| ch07 | 814 | Three nights before, he had copied the Wind entry into the P… |
| ch09 | 733 | He had been in the lock a thousand times. It had always been… |
| ch09 | 741 | He had two ands, and he spent both of them looking, as he ha… |
| ch09 | 720 | In the lock, he had seen a commitment whole. He had seen the… |
| ch10 | 736 | "You have." He kept his voice level, as he had learned from … |
| ch10 | 711 | Cael had noticed it as he came in and set it aside, and now … |
| ch10 | 765 | Not fast and careful, as she went at everybody, testing, loo… |
| ch11 | 745 | What was not nothing was the sound the room had made when it… |
| ch11 | 715 | He had seen all of it. He had seen her go in for the fourth … |
| ch11 | 727 | He thought about that on the way home, walking very slowly b… |
| ch11 | 757 | "I told him I'd think about it." Vell watched Lira go in, an… |
| ch11 | 712 | He had told Vell he was sure, and he had meant it, and stand… |
| ch12 | 1134 | He had been putting them there since the night of the river-… |
| ch12 | 852 | The entry was underlined in the grey book in ink, which he n… |
| ch12 | 754 | The ration was harder than the gaze. Once he had the gaze, e… |
| ch12 | 742 | On the way out he passed the girl with the sacking in her ha… |
| ch13 | 837 | She stayed there, and stayed, and he counted it on his own b… |
| ch13 | 710 | By the middle of the morning he had begun to see it, and it … |
| ch14 | 730 | He did not start with the hooks but with the question he had… |
| ch14 | 704 | In the fourth he tried to go faster than she could. He drove… |
| ch14 | 1049 | Files came to him by rotation, and had come that way for fou… |
| ch14 | 1066 | The supervisor read the standing instructions for the week a… |
| ch14 | 736 | They did not happen to him. Nobody was rude, and nobody ran.… |
| ch14 | 839 | It was not disorder; Havel had never thought it was, not eve… |
| ch14 | 791 | Havel thanked him and stood a while on the row, as he always… |
| ch14 | 709 | He came into the market at its foot, by a flight of worn sto… |
| ch15 | 970 | He went over it once more as he took his coat off the peg, b… |
| ch15 | 740 | It was not much of a square: a wide place where four lanes m… |
| ch15 | 729 | He saw the officer first, as he had known he would; he had a… |
| ch15 | 702 | So far, he was the page. But Cael had a newer page now, with… |
| ch15 | 703 | That was the whole of it. Cael had been through it before, w… |
| ch15 | 779 | There was one more thing, and it was not for the officials p… |
| ch15 | 724 | He had come back through the river gate a little after noon,… |
| ch15 | 809 | There was a proper way, and he knew it as he knew the forms:… |
| ch16 | 729 | A low record was worth travelling for. Anything this book sa… |
| ch16 | 705 | Gold ran down through the family. His grandmother's card sai… |
| ch16 | 788 | He lost them all the same way, and it took him a while to un… |
| ch16 | 813 | He had found the keeper's book, and found it low. He had fou… |
| ch16 | 979 | The read was part of the Path. It had come with the hardness… |
| ch16 | 783 | He had stood there at both of the boy's bouts in that time, … |
| ch17 | 749 | The designation had no prefix he knew. Its shape was the sha… |
| ch17 | 726 | Under nobody's line, the young man had signed his own. Havel… |
| ch18 | 947 | The register was laid out as the Compact laid out everything… |
| ch18 | 755 | "Because of the big one." Corrin did not wait for an answer.… |
| ch18 | 789 | He had been nine or ten. Hesk had taken him down to the whee… |
| ch19 | 850 | "You told me something once," she said. "Last winter. You sa… |
| ch19 | 863 | It was a side-floor bout on a thin evening card, between a S… |
| ch20 | 726 | The first went out clean. The second went out clean, and the… |
| ch20 | 713 | It was not a hard decision, when he looked at it. He had lef… |
| ch20 | 938 | Brom was not hard all over. That was the first thing the dra… |
| ch21 | 771 | He came out with his weight on his right side, his good side… |
| ch22 | 760 | He thought of the brown register in the reading room over th… |
| ch23 | 848 | He lay where he was and did not reach for the lamp. There wa… |
| ch23 | 733 | The grey book lay beside the Log with a scrap of string in i… |
| ch23 | 1104 | She took him to the cobbler at the bottom of the tannery lan… |
| ch23 | 1114 | He had fought before a hundred and sixty on a middling night… |
| ch24 | 731 | The third he threw with everything he had in his body and no… |
| ch24 | 715 | He stopped it with the strike already half thrown, and stopp… |
| ch24 | 780 | He stood on the north mark and waited for his breath to come… |
| ch25 | 834 | The Wind was shut, as he had shut it; the hip line was no br… |
| ch26 | 747 | "The man was the beginning." Brom looked across at the pump.… |
| ch26 | 942 | He had come home from the station Iron Skin and Copper with … |
| ch31 | 717 | It was not thirty people. That was what he had hoped for, so… |
| ch32 | 713 | They talked about nothing after that, which was the best par… |
| ch33 | 773 | Lira said yes before he had finished asking, and then, "Do i… |
| ch34 | 923 | He had begun to do a thing at the end of every evening card,… |
| ch34 | 704 | It was not sleep: he knew the sleeping man's slow rise and f… |
| ch34 | 766 | Lira had hired a yard for the afternoon, as she did twice a … |
| ch35 | 728 | Once, late in the month, he went further back than that. He … |
| ch35 | 720 | They had planned it in the alcove, between crosses, over thr… |
| ch36 | 735 | He had spent a week after the back bench trying to make the … |
| ch36 | 756 | There were a great many pages, more than he had known. There… |
| ch37 | 763 | The ring was a circle of old chalk on the bare stone at the … |
| ch38 | 730 | In the third exchange he did not burst at all. He knocked si… |
| ch39 | 836 | He counted faces, because counting was what his eyes did whe… |
| ch39 | 796 | He knew the difference between a burst he asked for and a bu… |
| ch40 | 762 | He gave it in a slow turning spiral, round and back and roun… |
| ch40 | 729 | The faster Keth went, the less he chose. In the first exchan… |
| ch40 | 726 | "Not because it's wrong. It's not wrong. You got it from a b… |
| ch41 | 706 | Then it was everywhere. Dace stopped calling him the unranke… |
| ch42 | 767 | Cael was filling the house's second bucket, because the heav… |
| ch42 | 905 | He worked on the first exchange: he made himself go first, i… |
| ch43 | 744 | The long build came, from the bottom of the woman's feet, sl… |
| ch43 | 730 | That was the thing she had not let herself see until tonight… |
| ch44 | 868 | His father's house had a training yard, because his father w… |
| ch44 | 1030 | So he had started taking these trips. He would hear of someb… |
| ch44 | 769 | He had no idea what the boy was, and he knew it. The story s… |
| ch45 | 748 | It went on like that the whole length of the row, though nob… |
| ch45 | 895 | "Dace has given this to the main floor. An outside Iron, who… |
| ch46 | 722 | There was no beat before it. That was what she meant, and it… |
| ch46 | 701 | It was quiet work, and it was slow, and nobody watching from… |
| ch46 | 742 | It was not like looking, and it never had been, which was wh… |
| ch46 | 760 | "Two exchanges." He said it flatly. "In the first I threw my… |
| ch47 | 879 | So the second session was that: Brom standing a forearm off,… |
| ch47 | 731 | Brom came at him with the slow burst, the gathering and the … |
| ch48 | 805 | It was slow work, slower than the standing had been, because… |
| ch48 | 721 | "Here. Halfway down." He read it out in his flat careful voi… |
| ch48 | 786 | He tried to imagine it: standing in front of a man like that… |
| ch49 | 749 | It was not a bout. Vell's table was empty and her books were… |
| ch49 | 796 | Ansel came at full speed, as he had in the first, with nothi… |
| ch49 | 704 | "Ansel," he said. "I was Bronze, on the coast. Three years a… |
| ch50 | 816 | "Stew," he said. "Inside my doors. On the night." He looked … |
| ch50 | 857 | "Listen to all of it before you do anything with that," said… |
| ch51 | 769 | "Here's my trouble," said Dace, without looking round, thoug… |
| ch51 | 856 | And tomorrow a man with a guild card for Iron, rank eight, w… |
| ch51 | 835 | He did it lightly, as he would have on any man on any bench … |
| ch51 | 739 | He thought of the thirteen days since Dace's shadow came acr… |
| ch51 | 811 | The lamp burned down a little as he sat. Out in the main roo… |
| ch52 | 716 | She had seen it once before, in the autumn, when the Shield … |
| ch52 | 732 | Reydan did not give him time to think. He came on, not hard … |
| ch52 | 870 | He planted, a stride from the rope, and turned his right sho… |
| ch53 | 837 | He had never once used it this way on a floor, though Lira h… |
| ch53 | 773 | The knock had always been best at a forearm. Here it was not… |
| ch53 | 727 | In the alcove the night before, under the plan, he had writt… |
| ch53 | 703 | For once the bursts were coming at the side he had drilled. … |
| ch53 | 990 | And it did not make him do anything. That was the part he wo… |
| ch53 | 705 | Nobody had thrown him. He went like a stack of grain sacks w… |
| ch53 | 861 | It came apart from the edges inward. The beams went first, m… |
| ch54 | 730 | People came up to the rope and looked at him and went away a… |
| ch55 | 765 | He went with no direction at all, which he had not done sinc… |
| ch55 | 792 | He knew, without anybody having told him, that the chestnut … |
| ch55 | 834 | His feet took him round by the north gate and back down the … |
| ch56 | 972 | Cael saw it from the bottom of the market steps on his way b… |
| ch56 | 831 | "I lost to her. Fifth exchange. You both saw it. And Vell wr… |
| ch56 | 706 | "I know I don't. That's what frightens me." Brom said it wit… |
| ch56 | 760 | He sat. The front room of the inn was the kind of room a car… |
| ch56 | 742 | "Tell him this," said Quenna. "Every one of these questions … |
| ch56 | 725 | "And there's the other thing," he said. "I'll say it once, a… |
| ch57 | 708 | She sat at the crate desk in his room with the lamp at her e… |
| ch57 | 733 | There were four sheets. She went through them with him one a… |
| ch58 | 749 | His body had spent the week mending in the order it chose, w… |
| ch58 | 814 | That day Cael watched Ulric. He did it out of habit as much … |
| ch58 | 709 | He knew the room. He had stood in it for half a second on th… |
| ch59 | 871 | He knew what it was before he looked. He knew her hand as we… |
| ch59 | 795 | "You don't know. I'll tell you, so you do." She took off her… |
| ch59 | 740 | "Don't." She put her spectacles back on. "You earned every l… |
| ch60 | 1064 | The district lay below him in the first light with the smoke… |

### 2.6 Protected lines (checked, untouched)

Every BOOK_MAP §8 item was searched in the flattened text of all 60 files: §8.1 (ch28), §8.2 (ch28, whole, the beat cut
by Lane A), §8.3 margin and copy (ch36), §8.4 long form (ch33, ch35) and the index line (ch35), §8.5 the *Note* line
(ch51, quoted ch55, ch59), §8.6 (ch54, recalled ch60), §8.7 (ch54), §8.8 (ch58), §8.9 (ch59), §8.10 (ch51), §8.11 all
lines (ch25), §8.12 (ch7, ch8), §8.13 (ch28), §8.14 (ch40), §8.15 (ch53, ch54), §8.16 (ch57 Hesk; ch56 Brom), §8.17
note and road (ch60), §8.18 (ch2), §8.19 (ch4), §8.20 (ch13), §8.21 all four pairs (ch15), §8.22 all nine (ch17), §8.23
(ch10), §8.24 (ch21, ch32, ch31 Dace), §8.25 (ch28, ch33), §8.26 (ch36), §8.27 (ch41), §8.28 (ch44/45, ch46, ch47),
§8.29 (ch51), §8.30 (ch54, ch57), §8.31 (ch60). The five a literal search misses (§8.2a, §8.14b, §8.14f, §8.18, §8.24a,
§8.26) are lines with a speech tag inside them or a comma before the tag; the words are verbatim. The §9 record window
(ch35 s4) states the designation, the manual's Gold-tier reservation, no sign-off, "systemic protocol, origin: registry
sub-layer" and the earlier date, and nothing else. None of the fixes in §3 touches any of them.

---

## 3. Exact line fixes

### 3A — Required before render (6)

Each old string matches exactly once in its file and once in the manuscript.

1. `manuscript/chapter-09.md`
   old: `*opp. tried the spinning cut, second.*`
   new: `*opponent tried the spinning cut, second.*`
   (Cael is reading Vell's margin note aloud to her; "opp." has no in-text decoding and an engine says "opp".)

2. `manuscript/chapter-09.md`
   old: `*opp. pressed hard from the word.*`
   new: `*opponent pressed hard from the word.*`

3. `manuscript/chapter-11.md`
   old: `L. to Dravin (Iron-equiv., Wind).`
   new: `L. to Dravin (Iron-equivalent, Wind).`
   (Vell's ledger line; her other lines write the word out: ch17 "(Iron-equivalent)", ch22 "(Iron-equivalent, Wind,
   guild-trained)".)

4. `manuscript/chapter-14.md`
   old: `*(Iron-equiv., Blade). Fifth exchange.`
   new: `*(Iron-equivalent, Blade). Fifth exchange.`

5. `manuscript/chapter-28.md`
   old: `"Not tomorrow," he said. "The sparring. I'll come at the same hour, but we're not going to hit each other." He reached for his coat on its nail.`
   new: `"Not tomorrow," he went on. "The sparring. I'll come at the same hour, but we're not going to hit each other." He stood with the coat over his arm.`
   (Brom has already "taken the coat off the nail at last" eight lines above, and the paragraph follows his own line;
   "he went on" keeps the speaker, and the coat stays off the nail until "He put the coat on" two sentences later.
   §8.2 is untouched.)

6. `manuscript/chapter-37.md`
   old: `*Coast courier — results — Fri.*`
   new: `*Coast courier — results — Friday.*`
   (Dace's chalk note, read by the narrator; the next sentence says "Came up the river road on Friday".)

### 3B — Optional, engine-safety only (author's call; 1)

A human narrator will read this correctly; a TTS engine may not. Not required. The old string matches once.

7. `manuscript/chapter-24.md` — LEED and LED in one sentence.
   old: `his lead foot came down across the long lead seam in the floor`
   new: `his lead foot came down across the long leaded seam in the floor`

Not proposed, but flagged for the lexicon: "def." (ch1, ch14) stays as Vell's Book 1 ledger form and is directed as
"defeated", as Book 1 §4 directs its protected ch59 line; the 13 "wound round / wound hands" (WOWND) stay, as "lead
leg" stayed in Book 1 — the phrase is fixed and the engine's context handling should carry it, but check the render.

---

## 4. Pronunciation lexicon (for the Breeze direction files)

Stress in capitals. "Owner-confirmed" = decision #33. "Carried" = the same entry in Book 1's or Book 3's lexicon,
unchanged. "Proposed" = BOOK_MAP §10 or this proof; not substituted at render until the owner confirms.

### People (33 named, plus the unnamed roles)

| Name | Say | Who | Status |
|---|---|---|---|
| Cael | KAYL (one syllable, as "sail") | the boy | owner-confirmed #33 |
| Caelen Hesk-ward | KAY-len HESK-ward | his full name (ch3 "C. Hesk-ward"); "Hesk-ward" as two words, stress HESK | carried (B1, B3) |
| Hesk | HESK | grandfather, Denvash; letters signed "*H.*" | carried |
| Lira | LEER-a | Wind, Copper; the vouch; "*L.*" in the Log | owner-confirmed #33 |
| Vell | VELL | the keeper (Bronze once) | carried |
| Dace | DAYSS (as "face") | the Circuit Master; keeps the slate | proposed |
| Brom | BROM (as "from") | Iron Skin, Copper; "*B.*" in the Log | carried (B3) |
| Keth | KETH (as "Beth") | Blade; the line at Iron; "*the finger*" in the grey book | proposed; keep distinct from Hesk (absent Kestrel) |
| Ulric | UL-rik | Copper Blade, ch1 and ch58 | proposed |
| Dravin | DRAV-in (short a) | Iron-equivalent Wind, guild line, ch10–11 | proposed |
| Wendel | WEN-del | Iron-equivalent Wind, guild pin, ch21 | proposed |
| Orvet | OR-vet | runs the tannery-lanes gym; shouts; red neckcloth | proposed |
| Bede | BEED | the Shield with the tally-book, ch42 | owner-pending #3 (BOOK_MAP §10); long E, never in a run with Brom |
| Maud | MAWD | Bronze Force, forewoman at the ropewalk, ch43 | owner-pending #3 (BOOK_MAP §10) |
| Reydan | RAY-dan | Iron rank eight, Pressure (burst), from up the river | carried (B3) |
| Ansel | AN-sel | Bronze washout from the coast; the cooper's back room | proposed |
| Quenna | KWEN-a | senior teaching-practitioner, Greyvane, Silver; "*Q.*" | carried (B3) |
| Havel | HAV-el | Assessor, district compliance; "*H.*" in the file | carried (B3); not Halvern |
| Coss | KOSS (as "moss") | the contact of record; eleven years; the daughter's map | carried (B1, B3) |
| Stedd | STED | the Copper washout who says "Fair." (ch2) | proposed |
| Corrin | KORR-in | the old Stone with the stick, ch17–18, ch22 | carried (B1 flagged Corrin/Corbin; Corbin absent here) |
| Dessa | DESS-a | Stone, Copper (B1); ch4, ch13 | carried |
| Renn | REN | Blade (B1); "the elbow" ch4 | carried |
| Darrow Innes | DARR-oh IN-ess (as "arrow") | Bronze 1, Iron (B1); named ch1, 2, 5–8, 45, 59 | carried |
| Feryn | FERR-in | Bronze 2, Pressure (B1); the Pressure's source | carried |
| Sarel | SAIR-el | Bronze 1 Blade (B1); ch45 list only | carried |
| Joren | JOR-en | Denvash friend; the declaration ch6 | carried |
| Torvin | TOR-vin | the first lodging (B1); "Torvin's old street" | carried |
| Ilsev | IL-sev | Assessor (B1); named once ch3 | carried |
| Red Cap | — | errand boy; sells chalk | carried (a name) |
| the heavyset man / his wife / the sister (and her hen and dog) / the fruit woman / the pie woman / the paper-stall man / the mending-stall woman / the chestnut man / the betting man / the dock partner / the river-academy man / the clock / the academy-coat man / the brickworks Shield / the Stone woman / the girl with sacking in her hair / the tall lad / the boy with the broken tooth / the four girls from the wall / the old man (the Cinder House yard) / the junior keeper / the doorkeeper / the eel-market men / the barge lad / Orvet's square woman / the watcher / the salt-end keeper / the lamp-oil keeper / Coss's daughter / Havel's supervisor / the night man / the sweepers | — | unnamed recurring roles | keep each a fixed colour across chapters |

### Places (20)

| Name | Say |
|---|---|
| Ardenmere | AR-den-meer (carried) |
| Denvash | DEN-vash (carried) |
| Valdris | VAL-driss (carried) |
| Fenrow | FEN-roh (carried) |
| Fenmark | FEN-mark (carried, B3) |
| Greyvane | GRAY-vayn; both syllables (carried, B3) |
| Velmere | VEL-meer; both syllables, unlike Vell (carried, B3) |
| the Ironyard | EYE-ern-yard (carried, B3) |
| the Cinder House | SIN-der (carried) |
| Fen Street (the mill) | as written |
| the river city, the second city, the salt end, the coast, up the river | descriptive; no stress |
| the market row, the dyers' steps, the tannery lanes, the ropewalk, the eel market, the triangle, the north gate, the river gate, the practitioners' quarter, the carters' inn, the saddler's, the cooper's, the boat shed | descriptive; "Row" = ROH |

### Terms and invented words (36)

| Term | Say / handle |
|---|---|
| Kindling, Kindled | KIND-ling (as in kindling a fire) (carried) |
| Arbiter | AR-bit-er (carried) |
| the Compact; the registry | KOM-pakt (noun) (carried) |
| sigil (ch2) | SIJ-il (carried) |
| [SHATTERED] | SHAT-erd; brackets never voiced; spoken "Shattered" plain (ch4, 6, 26) |
| [UNBOUND] | un-BOUND; brackets silent in the margin (ch36); Cael's copy has none |
| [unnamed], [Wind-adjacent] | brackets silent (notices) |
| Path names: Wind, Pressure, Iron Skin, Blade, Force, Stone, Shield, Tide, Ember, Glass, Compression | as written; "Wind" the noun; "Winds" its practitioners |
| -adjacent (Wind-adjacent, Pressure-adjacent, Iron-adjacent, Compression-adjacent, Tide-adjacent) | ad-JAY-sent, light pause at the hyphen |
| Tiers: Copper, Iron, Bronze, Silver, Gold; -equivalent; Assessed; unrated; provisional; "the line at Iron" | as written; "Rank 1", "Rank 10", "rank eight" as words |
| "Atypical movement pattern" | Vell's word; flat, a figure read off a page |
| the Power Log / the Log; the grey book / the observation book; the binder | document titles where context marks them |
| the six fields (What it is, Source, Conditions, Deployment range, Costs, Open questions); Claim / Evidence / Ruling | sentence case; each its own beat |
| the hooks: dormant, primed, building, committed, release, recovery; the hinge; performed commitment | Cael's terms; no stress |
| the gaze; the ration; the ten degrees | Cael's terms |
| the knock / the pulse ("*there?*"); the read (REED); smear; "inward" | Cael's and Brom's terms |
| the burst; the step; the fan; the empty quarter; the lock; two *ands*; the landing; the chain of two | Lira's and Cael's terms; "*ands*" = the word "ands" |
| the drop and the roll; going right; the step that doesn't stop; going home; turning in; the late door; paying early | Lira's words |
| the taking face / the giving face; the redirect; the hold; the throw; the lean; the wall; the purse | the Pressure's and Brom's terms |
| the join; the seam | Keth's chain |
| session nine; the thirteenth; *Anomalies*; *Carrying*; *Habit* / *Shape* | as written |
| FRAGMENT ACQUIRED / FRAGMENT UPDATE; REVISIONS | sentence case, system register |
| Suppression-Advisory Watch, Priority Level 4; Section 12 / Twelve; the supplementary marker (the green slip); the contact of record | numbers as words; "Level four" |
| the demonstration-provision track / the observer track; re-certification | as written |
| t.f. (Vell's margin) | the letters; the text decodes it ("Told, face.") |
| h (the small h, for heard) | the letter |
| def. (Vell's ledger, ch1, ch14) | "defeated" (Book 1's direction for the same form) |
| L. / B. / C. / H. / Q. / W | the letters; "L." = Lira in the Log, = lost in ch11's ledger line |
| marks, coppers, half a mark; the purse; the door; Iron share | currency |
| the slate / the wall; rings, dots, stitches; "watch this one" | Dace's grammar |
| the main floor, the side floor, the east bench, the alcove, the straw post, the north window, the rope, the mark | as written |
| Thursday week, Tuesday fortnight, the chapel day, the season | as written |

Lexicon size: 33 named people (plus the unnamed-role group), 20 places, 36 terms — **89 entries**.

---

## 5. Direction notes the segmenter and instruct files will need (not text changes)

1. **Keep Cael = KAYL and Lira = LEER-a** in every chapter direction (#33).
2. **POV cutaways**: the "he/she" changes referent at the `---`. Lira: ch1 s4, ch11 s1–2, ch43 s3–5, ch52 s3–4.
   Brom: ch16 s1 and s3–5, ch20 s3, ch25 s1–3. Havel: ch14 s5–6, ch15 s5, ch33 s3–5. Coss: ch17 s5–6, ch35 s1–3,
   ch41 s5–6. Reydan: ch44 s2–4, ch51 s4, ch54 s1–2, ch60 s1. The record window (ch35 s4) has no POV: flat, exact.
3. **Notices and brackets**: a neutral system cadence for the four fenced blocks, each its own segment with a long pause;
   never voice brackets, fences, asterisks or the `---`. "Shattered" plain wherever it is spoken.
4. **Italic documents**: give the Log, the ledger, the chalk, the letters and the Compact file a slight register change
   and return cleanly at the next prose cue; the salutations ("*Cael,*", "*Dear Hesk,*") and sign-offs ("*— H.*",
   "*— C.*", "*— L.*", "*Q.*") are pauses and letter-names, never "dash".
5. **All-caps** (Log headings, the bill ch22, the plates ch47/55/59, *DOES THE FORM ASK FOR HIS FAMILY* ch56) in
   sentence case; the single letters by name.
6. **Counts**: preserve the slow count architecture — Lira's "*one-and-two-and*", the knock tallies ("Twelve in
   twenty"), the bout count on the *three* (ch53), Vell's "Nine days", Dace's "Five hundred and four".
7. **Collisions by register**: Vell flat and exact, Dace brisk; Brom slow and level; Keth dry; Reydan even; Quenna plain
   and unhurried; Havel careful; Coss restrained. Give Bede (BEED) its long vowel wherever Brom is near (ch43, 45, 50,
   53); give Velmere its second syllable (ch16, 32, 56).
8. **Homographs**: "the read" = REED (84); "wound round" = WOWND (13) and the one WOOND (ch8); "lead foot" = LEED
   against "lead seam" = LED (ch24 ×2, ch59); "find it live" = LYV; "bow window" = BOH and "a small bow of the head" =
   BAU (ch59); "tears at the corner" = TAIRS (ch36).
9. **Interruptions**: the 7 `—"` cut-offs want the engine's short gap and no falling cadence. "Hm." / "Huh," / "Dunno."
   / "Oh," — check they survive the render.
10. Long paragraphs (§2.5) may be split only at sentence boundaries, as `fpaudio.py` does; mark the split in the
    direction file so it does not land mid-thought, especially in the bout paragraphs (ch24, ch40, ch53).
