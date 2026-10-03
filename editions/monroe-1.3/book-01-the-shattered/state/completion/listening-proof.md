# Book 1 — Line and listening proof (Step 3)

Reader: Claude Fable 5.1, fresh context, 2026-10-02. Scope: `manuscript/chapter-01.md` … `chapter-60.md`
(306,683 words), read in order as a Breeze narrator will meet them (one segment per paragraph, `---` as a long
pause). Read first: `COMPLETION-PLAN.md` Step 3, `LANE-1-REPORT.md`, `LANE-2-REPORT.md`, `EDITION_BRIEF.md`
(audio and Reader Standard), `OWNER-DECISIONS.md` #29, `BOOK_MAP.md` §7, `protected-patterns.txt`, and the
Meridian ch1 `notes.txt` as the model of what the direction files need. Running notes: `listening-notes.md`.

**No manuscript file was modified.** Every fix below is a proposal; each old string was verified with
`grep -c -F` to match exactly once in the named file. No fix touches a protected line.

---

## 1. Verdict

**Render-ready after 21 small text fixes, all mechanical (abbreviations, slashes and numerals that an
engine will voice wrongly).** Nothing structural stands in the way:

- Quotation marks: every paragraph in all 60 chapters has an even count of `"` (straight quotes only; no curly
  quotes anywhere). No unbalanced or mismatched quotes. No nested double-in-double quotes; the three
  "quote inside a quote" cases use italics for the read text (ch20, ch32, ch49) and read cleanly.
- Italics: every paragraph has an even count of `*`. No underscores, one `**bold**` (ch3, the plate word).
- `---`: every break has blank lines on both sides. No setext accidents, no stray headings, no double hyphens.
- Halvern/Halden (decision #29): never in one scene. Halvern is named only in ch28 (Coss's POV); in ch31–32 the
  clerk upstairs is "the clerk". Halden is named in ch31, 32, 48, 49, 50, 53, 54. The mitigation holds.
- Every Tier A and Tier B protected line in BOOK_MAP §7 is present verbatim (grep-checked; see §2.6).
- Attribution: no speech paragraph whose speaker a listener cannot place. The three-voice-plus scenes
  (the community hall ch2, the nut stall ch7, Torvin's table ch11/19/27/52/59, Coss–Ilsev overheard ch49,
  Vell's table ch55) all carry by alternation or an explicit lead-in.
- Doubled words, broken joins, lower-case starts, tense slips from the texture passes: none found. The eleven
  lower-case sentence starts the sweep flagged are all inside Vell's or Cael's deliberate shorthand notes.

What remains is for the direction files, not the text: a second audio collision beyond #29 (Coss/Doss, and
Marrow/Darrow in the climax) that the narrator must hold apart by register; a short list of homographs the
engine is likely to misread; and the all-caps signs, which should be rendered in sentence case.

---

## 2. Findings by category

### 2.1 Quotation marks and attribution

- Balanced throughout (0 odd-quote paragraphs, 0 odd-asterisk paragraphs, script-checked).
- **Italics carry five different things**, and the narrator needs to know which: (a) Cael's notebook/Log text
  and Vell's ledger lines; (b) letters (Hesk's, Cael's, Feryn's note); (c) documents and notices read as text
  (the expulsion notice ch4, the summons ch30/ch48, Ilsev's paragraph ch53, the Handbook sections ch31/48/49);
  (d) remembered or reported speech (*Sunlight,* the fruit woman told him; *Don't let anyone see you move*);
  (e) inner thought and word stress. The split is always clear from the surrounding sentence; it only needs the
  direction file to say which is which per segment (the Meridian notes do this).
- Read text inside speech: ch20 Lira reads the notice ("*Continued cohabitation…*"), ch32 Lira writes the three
  sentences ("*[SHATTERED] is not recognized…*"), ch49 Ilsev recites section four. Direct as a voice reading
  aloud, flatter than her own speech.
- Interruptions: 42 paragraphs end or break on `—"`; all are cut-off speech ("Whatever happens tomorrow—" /
  "Hesk." / "—we'll figure it out." ch2; "Your hands are—" ch44; "He *cut* the—" ch49). They need the engine's
  short gap and no falling cadence, as the Meridian run handled s051.
- Overheard fragments beginning with a dash: the radio ch2 ("—and of course the Ardenmere quarter-final"), the
  two men at the board ch8 ("—won't take Brenna again"), the street after Corbin ch40 (four italic snatches),
  the bread woman under the barrels ch51 ("*—and you can stop calling me nothing*"). Direct as passing voices.
- Vell's spoken record lines are in quotes ("Result stands as called…"); her unspoken second lines are in italics.
  The narrator's quotes-vs-italics distinction carries the difference (ch25 is the clearest case).

### 2.2 Ear collisions

**Names in one scene.** A script split each chapter on `---` and counted name pairs per scene:

| Pair | Risk | Scenes together | Note |
|---|---|---|---|
| Halvern / Halden | high | **none** | Decision #29 mitigation holds; Halvern only in ch28. |
| **Coss / Doss** | **high** | ch30 s4; ch54 s1 | KOSS vs DOSS, one consonant apart; both men bear on Cael's lodging. ch30: "because Doss had gone out to the warehouses" two paragraphs before Cael reads "*Coss, field agent.*" ch54: the fourteen-name list ends "Sella. Doss." and two paragraphs on "Coss's drawer… Coss had said it plainly". Direction: Coss in the Compact's clipped register, Doss low and worn with a longer open vowel. Optional epithet in ch30 below. |
| **Marrow / Darrow** | **high** | ch57 s4; ch58 s1, s5 | MARR-oh (bookmaker) vs DARR-oh (the Bronze) in the climax. Every Marrow mention sits next to a slate ("Marrow watched them do it", "Marrow watched it happen… lifted the slate", "Marrow was paying out"). Direction: Marrow as in "bone marrow", Darrow as in "arrow"; slate lines in an aside register. Optional epithet in ch58 below. |
| Dessa / Doss | medium | ch24 s4; ch25 s2; ch27 s1–2; ch51 s1; ch52 s2; ch54 s1; ch57 s3 | DESS-uh (two syllables) vs DOSS (one). ch24 is the sharp one: Doss's first word is "Dessa." and his next is his own name; the text glosses it ("It took Cael a moment to understand that it was a name"). |
| Corbin / Corvane | medium | ch43 s4–5; ch44 s1; ch49 s2; ch51 s1; ch52 s5 | KOR-bin vs kor-VAIN — stress on different syllables; keep it. |
| Ressa / Dessa | low | ch29 s2; ch35 s5; ch36 s1 | Never in dialogue together; RESS-a (Denvash baker) vs DESS-a. |
| Sella / Sarel | low | ch54 s1 | SELL-a vs SAIR-el. |
| Talis / Alis | low | ch39 s1 | One is a letter from Denvash, the other the yard. |
| Renn / Brenna | low | many bout scenes | Different sex and Path; one vs two syllables; attribution carries. |
| Kestrel / Hesk; Feryn / Fenrow; Petra / Pellin; Lira / Ilsev | none | — | distinct by ear. |

Renames are the owner's call (decisions #6, #29); none is proposed. Two optional one-word epithets (§3B)
would do for Coss/Doss and Marrow/Darrow what "the clerk" does for Halvern.

**Homographs.** All occurrences were read in context; none is ambiguous to a human narrator. These are the
ones an engine is likely to voice wrongly, with the intended reading (for the lexicon/instruct files):

| Word | Intended | Where |
|---|---|---|
| wound (past of wind, WOWND) | all 8 uses | ch3 "part worry, wound so tightly"; ch4 "A cord was wound round it"; ch10 "wound the film back" ×2; ch29 "wound the string"; ch36 "strings wound twice"; ch44 "a spiral, wound tight"; ch45 "the spiral wound tight" |
| lead (LEED) | all 4 | ch3 "lead up to it"; ch11 "her lead leg"; ch25 "His lead foot planted" and "her lead foot" |
| tear (TAIR, a rip) | all 5 | ch7 "found its tear"; ch19 "tear the page out"; ch30 "looked at a tear before she mended it"; ch37, ch47 "tear it" (bread) |
| bow (BOH, a bend) | ch1 "thinking about bowing"; ch5 "considering a bow" (the bent bracket) | ch52 "with a small bow" is BAU |
| live / lives (LIV, verb) | ch18 "lives in the gap… You live in the lesson"; ch19 "where the boy lives" | ch25, ch45 "in their lives" are LYVZ |
| read (RED, past) | hundreds; the risky shape is "X read it twice." and "I read…" in letters (ch6 "*I read the book. I read the fifth one three times.*"; ch2 "You read the sheet."; ch4 "You read it." is REED, imperative) | engine risk only; no text fix |
| minute | all time-uses (31); no "my-NOOT" | — |
| row (ROH) | all place-names (Weaver's Row, Merchant Row, the second row) | no quarrel-rows |
| wind (noun, Wind Path) | all 68 | no "wind up / wind back" verbs |
| close, present, record, refuse, subject, object, separate, content, contract | all read naturally in context | — |

**"As" after Lane 1's simile conversions.** All 295 ", as …" clauses were listed and read. Nearly all are
habitual ("as he always did", "as a rule", "as she had on Tuesday") or manner ("as a man brushes off a fly")
and cannot be heard as "while". The few that *are* temporal are genuinely temporal and correct (ch9 "He found,
as he said it, that he had"; ch24 "as she came to the mark and turned"; ch39 "as the two of them went back to
their marks"; ch40 "as the elbow came round"; ch30 "as somebody went along ahead of them with a taper" — a
literal cause). Where Lane 1 used "just as" (ch9, ch17) it was the right call. **No fixes.** One direction note:
ch40 "It did not go out, as the word had gone out" wants a slight lift on "as" so it reads "the way".

**Accidental rhymes / repeats in adjacent sentences.** None worth a fix. The only aloud stumble is a grammatical
stutter, ch19 "had not let himself look at at all" (§3B, optional).

### 2.3 Formatting the narrator meets

- **Code blocks** (5): ch1 PATH DECLARATION; ch40 and ch42 FRAGMENT ACQUIRED (Wind); ch47 FRAGMENT ACQUIRED
  (Pressure); ch58 FRAGMENT NOTICE. All protected text. Read as notices, each line its own beat, brackets
  silent: "Fragment acquired. Unnamed — Wind-adjacent. Duration: undetermined. Integration: partial. Tier
  equivalent: unknown." ch1's heading "PATH DECLARATION — COPPER RANK 1" reads "Path Declaration, Copper Rank one;
  Rooted Stance — Passive."
- **`[SHATTERED]`** (24 places, ch1, 3, 4, 5, 6, 9, 20, 28, 30, 31, 32, 44, 46): brackets are never voiced,
  in speech (ch9, ch44, ch46 `"[SHATTERED]."`) or narration ("a [SHATTERED] file"). ch3 `**[SHATTERED].**` is the
  one bold: the plate word, said once, flat and cold. ch1 "Four (4) instances" is protected: read "Four — four —
  instances" or simply "Four instances" at the renderer's discretion.
- **Log entries in italics**: Cael's Log (numbered "*1. Renn. Copper R3…*" through "*Seventeenth.*"), the back
  pages, the four-item and five-item counts, Lira's chalk columns (*gone*, *W*, *P*, *same*, *less*, *arms.
  an hour.*, *both. nothing. arms anyway.*, *ribs*, *Sunday*). Vell's ledger lines use initials: "R." (Renn),
  "L." (Lira), "(Vell, h)" where the text itself explains the small *h* for "heard". Direct these as the
  letters. Lower-case starts inside them are deliberate.
- **Numerals vs words.** Ranks ("Copper Rank 1", "Rank 10", "Copper 4s"), registrations (41-7843-V, 22-1190-H),
  "Statute 14, Section 9", "32 years prior" (protected), "section 40", "statute 19", "Section 1: Definitions"
  all read naturally as numbers. The ones that do not — "8 in.", "0 and 4" (Log and narration), "41, sleet",
  "3 (h)", "4TH" — are fixed in §3A.
- **Abbreviations.** "Cu 3" is decoded by the text itself (ch8: "*Cu 5, Stone.* Copper, Rank 5, Stone Path"),
  so it is read as the two letters, "C-U five", consistently; "R3/R2/R4/R5" in the Log and the protected ch59
  "Bronze R1" read "R-three", "R-one"; "def." (ch59, protected) reads "defeated". The ones with no in-text
  decoding — "exch.", "unr.", "wk.", "Br 1/2", "Mon:", "Sun. wk.", the slashes — are fixed in §3A.
- **All-caps lines** (engines sometimes spell them): WARDEN-ADJUNCT PELLIN (ch3), ROOMS (ch7/16/28), NO PATH
  DAMAGE TO WALLS — YOU PAY (ch8), IF IT'S STILL HERE (ch8/14/24/34), WEST (ch8/27/48), *REGISTRY READING
  ROOM. OPEN TO ALL REGISTRANTS. MORNINGS.* (ch31), *SUMMONS FOR COMPLIANCE EVALUATION.* (ch30), *To CAELEN
  HESK-WARD* (ch48), *PART SIX. THE SENIOR EVALUATION. RESERVED TO ASSESSORS.* (ch48), *CORBIN PUT HIS HAND UP*
  (ch40), *TODAY* (ch45), *LAST BOUT, SUNDAY FORTNIGHT. DARROW INNES…* (ch55/56/57), *HESK-WARD*, *13 TO 1*,
  *SHAME* (ch57), *HESK-WARD. 4TH. VELL'S CALL.* (ch60). Render in sentence case (renderer substitution, as the
  Meridian run proposed); no text change except the numeral in ch60.
- **Single letters**: "the O leans" (ch7 on), "an *R* or a *B*" (ch28), "a *W*" / "two *V*s" (ch57), the
  *W* and *P* columns, "Yard"-style lone capitals: say the letter name.
- **Em-dashes**: closed throughout; spaced " — " appears only in letter salutations (*Joren —*, *— C.*,
  *— H.*, *— Cael*), inside the slate/ledger lines being fixed, in Lira's chalk note "*frustration — let him*"
  (ch38), and inside protected FRAGMENT lines. All are pauses.
- **Scene breaks**: 17–30 per chapter, all correctly spaced.
- **"Mm."** (Yeni, ch7, ch16, ch30; Lira ch26): may be dropped by the engine; check the render.

### 2.4 Line-level typos and grammar

- Doubled words: the sweep's three hits are all grammatical ("look at at all" ch19, "tells you you can" ch50,
  "Telling you you're" ch60). No true doubles.
- Broken joins, sentences ending mid-clause, stray lower-case starts, tense slips: none found in 60 chapters.
  The texture passes left no seams at the line level.
- Spelling: British throughout ("colour", "neighbour", "recognised"/"recognized" both appear, "plowing" ch17 is
  US) — no audio effect. "labeled" inside the protected Fourth entry (ch6) stays.
- One continuity nit noticed in passing, out of this proof's scope (Step 2's lane): ch10 Hesk recalls saying
  "*It's easier to make a family choose*" aloud in ch4, where his words were "A family that chooses looks better
  than a city that puts a fourteen-year-old out on the road." No audio consequence.

### 2.5 Paragraphs over about 700 characters

79 paragraphs. Listed only; none is a defect, but each will be split by the segmenter and the direction file
should mark the split so it does not land mid-thought (the first sentence of each is given so it can be found).

| ch | chars | opens |
|---|---|---|
| ch01 | 842 | Denvash's Outer District was a long ring pressed against the… |
| ch01 | 786 | It was higher than any wall had a reason to be. Cael had fiv… |
| ch01 | 740 | They did it six more times. Joren talked through four of the… |
| ch02 | 758 | He had copied it a month ago from the foot of the registry s… |
| ch06 | 837 | He was glad of it, which surprised him. The first hours out … |
| ch06 | 790 | *A few years*, in the side room. *Some years*, under the lam… |
| ch08 | 708 | That was how it looked at first, from the street: noise and … |
| ch08 | 721 | He had come here meaning to watch, and he could do more than… |
| ch12 | 720 | "Then she picked a strange thing to say it about." Lira walk… |
| ch12 | 753 | "Explained and agreed are different animals. So you'll hear … |
| ch13 | 711 | "On the roof I said I wouldn't tell you what that figure loo… |
| ch20 | 825 | She laughed a little, as you laugh when somebody asks how yo… |
| ch21 | 775 | He had a month of it in his head by now, laid down as he lai… |
| ch23 | 817 | "They know already," he said. "The man was told Torvin's. Wh… |
| ch25 | 749 | Its whole idea had come to him on a plank bench, and been tu… |
| ch27 | 708 | "First exchange. You showed her three feints and stopped. Yo… |
| ch28 | 782 | He had shared a desk that year with a man who was. The man s… |
| ch28 | 931 | A non-standard result at Kindling set a procedure going. He … |
| ch28 | 702 | At the north edge of the district the ground began to rise, … |
| ch31 | 724 | The man in the dark coat had eaten at Amrit's on his first n… |
| ch32 | 746 | Every sentence he wrote wanted another sentence after it to … |
| ch32 | 712 | "The sweep that brought me out here was asked for by people … |
| ch32 | 756 | "Now I stamp the summons closed, pending, and I apply to reg… |
| ch34 | 766 | He said it. He had worked it out under the pear tree the eve… |
| ch34 | 733 | "Reckless is fighting six times because six is the biggest n… |
| ch35 | 713 | He read that three times. Hesk could not know that there had… |
| ch36 | 812 | He looked for the anger, because he thought he might be owed… |
| ch36 | 705 | There were three of them at the table: the reviewing officer… |
| ch37 | 766 | She came in and stayed, close, very close, inside the reach … |
| ch38 | 802 | It was a small flat tin that had once held throat sweets, an… |
| ch38 | 754 | The room was very small, smaller than the roof room in the t… |
| ch40 | 757 | It had come from the grey half. It had come from two months … |
| ch41 | 702 | He watched him as he had watched Lira for three months, whic… |
| ch42 | 830 | He watched as he had watched on Monday, without writing and … |
| ch42 | 765 | That surprised her. She had been sitting on the end of her o… |
| ch42 | 772 | "I thought it might feel like that. Hearing it. I thought, i… |
| ch42 | 755 | She thought about the drop, and about Dessa's fourth, and ab… |
| ch43 | 721 | He stopped chewing, and she did it slower than she had ever … |
| ch43 | 727 | "Passing through. He's from nowhere in particular, these day… |
| ch43 | 894 | "I'm saying it now. I'm going to work out whether it's true,… |
| ch44 | 712 | "A Blade strikes. A Force man strikes and then shoves. Ember… |
| ch44 | 776 | "That depends on the fighter." She tapped the spiral again, … |
| ch44 | 703 | That night, on the cot, he copied Corvane's figure into the … |
| ch45 | 718 | She stood at her mark in the grey half every morning with th… |
| ch46 | 857 | They were people who knew what they were looking at. The old… |
| ch46 | 829 | He came in as she had seen him come into three other yards i… |
| ch46 | 859 | She knew Feryn's weights. He had two of them, and she had wa… |
| ch46 | 773 | There was no place where it struck him. It was everywhere at… |
| ch46 | 720 | The air came down. It was as huge as before and as patient a… |
| ch46 | 702 | He came in fast and straight, and the speed changed everythi… |
| ch46 | 772 | The hand on his shoulder did not let go. The turn was finish… |
| ch47 | 718 | He told them as Cael wrote the Log, exactly and without merc… |
| ch47 | 720 | "Six years now, I've made my living letting go on people." H… |
| ch47 | 813 | He told her. He told it as he had told Lira, in order, but h… |
| ch48 | 735 | That was what he remembered about it afterward. Nothing had … |
| ch48 | 740 | The category was not for anybody whose classification could … |
| ch49 | 729 | "Section one also says what a primary classification is. *Th… |
| ch50 | 804 | He told her about the desk that did not rock, and the folded… |
| ch50 | 803 | It was not like the step, or the build, or anything he had l… |
| ch52 | 758 | He did not write about Sunday, except to say that he had won… |
| ch53 | 714 | "Legal will take the rest of the year." The section head had… |
| ch53 | 957 | He thought about his daughter, who would be fourteen at mids… |
| ch53 | 879 | He had been sitting there a quarter of an hour, after the gr… |
| ch53 | 781 | It had come in on Thursday from a house on the canal, a merc… |
| ch53 | 753 | The letter was on the end of the bench, where it had been fo… |
| ch54 | 772 | It did not take long. *Lira.* That one was first and needed … |
| ch55 | 750 | She had not been calm. She had been doing the thing she had … |
| ch55 | 739 | She could stand back. That was the first thing she made hers… |
| ch55 | 731 | She would not be any use by the gate. She knew how he fought… |
| ch55 | 826 | It sounded strange, like something said by somebody who was … |
| ch55 | 739 | He wrote his name on the back of the carter's slip, under Da… |
| ch56 | 775 | Cael had a bill of the mender's in his pocket, for washers, … |
| ch57 | 849 | Doss stood at the back on account of the knee. Renn was on t… |
| ch57 | 843 | So he went on doing it. He let Darrow walk him, and every ti… |
| ch58 | 835 | The front went first, as always, and went down easily, becau… |
| ch58 | 777 | He tried to draw it first, as Corvane had taught him to draw… |
| ch60 | 823 | He was very careful with himself about what it was, because … |
| ch60 | 787 | He told him the fourth exchange as near as he could, which w… |
| ch60 | 739 | The east wall's shadow lay long across the yard, as it did e… |

### 2.6 Protected lines (checked, untouched)

Tier A: the four-line `[SHATTERED]` entry (ch1), *Better when it's done…* (ch1, starred), Hesk's *I don't know
how to describe it* (ch1), "Caelen Hesk-ward. Registration 41-7843-V." (ch3), the eleven seconds / Alis Trent /
Joren (ch1–3), the three code blocks (ch40, 47, 58), *First person outside Denvash…* (ch9), "What tier are you?" /
"[SHATTERED]" / "When you figure it out, I want to know." (ch46–47), "What are you?" / "I don't fully know yet."
(ch58). Tier B: all present by grep — ch2 (×2), ch3 (notice, archive, "You're not behind…"), ch4/6 (Hesk's
entries incl. the added *When you don't know what you can do yet…*), ch5 (gate entry + corollary), ch9, ch13
(×3), ch18, ch20, ch25, ch30, ch32, ch41, ch53 (×2), ch56 (×2), ch58 (×2), ch59, ch60. None of the fixes in §3
touches any of them.

---

## 3. Exact line fixes

### 3A — Required before render (21)

All are abbreviations, slashes or numerals inside slates, ledger lines, chalk and Log notes that an engine will
voice as "slash", "ex-ch", "unr", "wk" or spell letter by letter. Each old string matches exactly once in its file.

1. `manuscript/chapter-11.md`
   old: `*8 in. past the fist. My eye says less.*`
   new: `*Eight inches past the fist. My eye says less.*`
   (Lira has just said "About eight inches past where his hand ends"; ch12 repeats it in speech.)

2. `manuscript/chapter-12.md`
   old: `*Over/under: 1 exch.*`
   new: `*Over-under: one exchange.*`
   (Lira's gloss follows: "whether you last more than one exchange".)

3. `manuscript/chapter-15.md`
   old: `*Over/under: 2 exch.*`
   new: `*Over-under: two exchanges.*`

4. `manuscript/chapter-16.md`
   old: `*Over/under: 3 exch.*`
   new: `*Over-under: three exchanges.*`

5. `manuscript/chapter-35.md`
   old: `*Over/under: 3 exch.*`
   new: `*Over-under: three exchanges.*`

6. `manuscript/chapter-37.md`
   old: `*Over/under: 3 exch.*`
   new: `*Over-under: three exchanges.*`

7. `manuscript/chapter-17.md`
   old: `*Over/under: 4 exch.*`
   new: `*Over-under: four exchanges.*`

8. `manuscript/chapter-29.md`
   old: `*Over/under: 4 exch.*`
   new: `*Over-under: four exchanges.*`

9. `manuscript/chapter-25.md`
   old: `*Over/under: 5 exch.*`
   new: `*Over-under: five exchanges.*`

10. `manuscript/chapter-17.md`
    old: `*0 and 4. Four, five, six, seven.*`
    new: `*Nought and four. Four, five, six, seven.*`
    ("Nought" matches the book's register — "fortnight", "colour"; the engine would say "zero".)

11. `manuscript/chapter-22.md`
    old: `He had been 0 and 4, not 0 and 2.`
    new: `He had been nought and four, not nought and two.`
    (Numerals in narration.)

12. `manuscript/chapter-45.md`
    old: `*Mon: F. (Br 2) — unr.*`
    new: `*Monday: F. (Bronze 2) — unrated.*`
    (Marrow's unpriced slate; "Br" has no in-text decoding, unlike "Cu".)

13. `manuscript/chapter-46.md`
    old: `*41, sleet, Monday noon*`
    new: `*Forty-one, sleet, Monday noon*`
    (Vell's private note; the narration before it already says "made it forty-one".)

14. `manuscript/chapter-50.md`
    old: `*Sun. wk. — Dessa (Cu 5, Stone) / unrated (vouched). Asked by both.*`
    new: `*Sunday week — Dessa (Cu 5, Stone) against unrated (vouched). Asked by both.*`
    ("against" is the ledger's own form, ch23.)

15. `manuscript/chapter-51.md`
    old: `*D. / unr.*`
    new: `*D. — unrated*`

16. `manuscript/chapter-55.md`
    old: `(the Stone woman, wk 2)`
    new: `(the Stone woman, week two)`

17. `manuscript/chapter-55.md`
    old: `DARROW INNES (Br 1, Iron Path)`
    new: `DARROW INNES (Bronze 1, Iron Path)`

18. `manuscript/chapter-56.md`
    old: `DARROW INNES (Br 1, Iron Path)`
    new: `DARROW INNES (Bronze 1, Iron Path)`

19. `manuscript/chapter-57.md`
    old: `DARROW INNES (Br 1, Iron Path)`
    new: `DARROW INNES (Bronze 1, Iron Path)`
    (Vell's card, copied in the district return and quoted at the board; all three copies must match.)

20. `manuscript/chapter-56.md`
    old: `*Claim. Evidence: 3 (h), Doss (h), Stone woman (h). Ruling: pending.*`
    new: `*Claim. Evidence: three (h), Doss (h), Stone woman (h). Ruling: pending.*`

21. `manuscript/chapter-60.md`
    old: `*HESK-WARD. 4TH. VELL'S CALL.*`
    new: `*HESK-WARD. FOURTH. VELL'S CALL.*`
    (All-caps "4TH" is the one numeral an engine may spell out.)

### 3B — Optional, engine-safety only (author's call; 9)

Human narrators will read these correctly; a TTS engine may not. None is required. Each old string matches once.

22. `manuscript/chapter-03.md` — "wound" (WOWND) is likely to be voiced as the injury.
    old: `part pride and part worry, wound so tightly together`
    new: `part pride and part worry, twisted so tightly together`

23. `manuscript/chapter-44.md`
    old: `she drew a spiral, wound tight,`
    new: `she drew a spiral, coiled tight,`

24. `manuscript/chapter-45.md`
    old: `the stick figure and the spiral wound tight and the row of four strokes`
    new: `the stick figure and the spiral coiled tight and the row of four strokes`

25. `manuscript/chapter-30.md` — "a tear" is likely to be voiced as a teardrop.
    old: `as she looked at a tear before she mended it`
    new: `as she looked at a rip before she mended it`

26. `manuscript/chapter-19.md` — grammatical, but a stammer aloud.
    old: `had not let himself look at at all`
    new: `had not once let himself look at`

27. `manuscript/chapter-30.md` — Coss/Doss in one scene (the only text mitigation proposed; cf. #29's "the clerk").
    old: `because Doss had gone out to the warehouses at dusk`
    new: `because the night-watchman had gone out to the warehouses at dusk`

28. `manuscript/chapter-58.md` — Marrow/Darrow in the climax.
    old: `Marrow watched it happen.`
    new: `Marrow, at his slate, watched it happen.`

29. `manuscript/chapter-01.md` — "bowing" (BOH-ing, bending) may be voiced as BAU-ing.
    old: `as if it were thinking about bowing`
    new: `as if it were thinking about bending`

30. `manuscript/chapter-05.md` — same bracket, same word.
    old: `as if it were considering a bow`
    new: `as if it were considering a bend`

Not proposed, but flagged for the lexicon: "lead leg/foot" (ch11, ch25 ×2) — "front leg/foot" would be safe but
"lead" is the fighting term and should stay; direct it as LEED.

---

## 4. Pronunciation lexicon (for the Breeze direction files)

Stress in capitals. "Confirmed" means the text itself gives a cue (a rhyme, a gloss, a spelling-out); the rest
are proposals for the owner to confirm, as the Meridian run listed its unconfirmed names.

### People (46)

| Name | Say | Who | Note |
|---|---|---|---|
| Cael | KAYL (one syllable) | the boy | ch9 "Just Cael" |
| Caelen Hesk-ward | KAY-len HESK-ward | his full name | ch3; "Hesk-ward" as two words, stress on HESK |
| Hesk | HESK | grandfather, instrument-maker | |
| Joren | JOR-en | Denvash friend | |
| Alis Trent | AL-iss TRENT | Denvash, Tide Path | keep distinct from Talis |
| Garrik | GARR-ik | cart-mender, projector | |
| Ressa | RESS-a | Denvash baker | distinct onset from Dessa |
| Pellin | PEL-in | Warden-Adjunct, Weaver's Row | |
| Torvin | TOR-vin | lodging-house keeper | |
| Yeni | YEN-ee | the seamstress | |
| Lira | LEER-a | Wind Path, the vouch | |
| Vell | VELL | the Ledger-keeper | |
| Marrow | MARR-oh (as "bone marrow") | the bookmaker | collides with Darrow in ch57–58 |
| Renn | REN | Blade, Copper 3 | |
| Brenna | BREN-a | Shield, Copper 2 | |
| Dessa | DESS-a | Stone, Copper 5 | collides with Doss |
| Baro | BAH-roh | unrated Blade, ch15 | |
| Amrit Sole | AM-rit SOHL | Ember, the cook | |
| Petra Voss | PET-ra VOSS | Force, Copper 3 | |
| Doss | DOSS (rhymes with "moss") | night-watchman, once Bronze | collides with Coss and Dessa |
| Coss | KOSS (rhymes with "moss") | Compact field agent | clipped, formal register |
| Halvern | HAL-vern | the post's clerk (ch28 only by name) | decision #29 |
| Halden | HAL-den | reading-room keeper | decision #29 |
| Sarel | SAIR-el | Bronze 1 Blade, scaffolds | |
| Talis | TAL-iss | Stone, Copper 4 | |
| Dellin | DEL-in | Force, Copper 3, carter | |
| Corbin | KOR-bin | Shield, Copper 3, "the ruler" | decision #5 flags Corrin/Corbin for Book 2 |
| Kestrel | KESS-trel | Force, Copper 5, ropewalk | |
| Feryn | FERR-in | Bronze 2, Pressure | |
| Corvane | kor-VAIN | the old Pressure student, brickworks | stress away from Corbin |
| Ilsev | IL-sev | Assessor, Regional Evaluation | |
| Darrow Innes | DARR-oh IN-ess (as "arrow") | Bronze 1, Iron | |
| Sella | SELL-a | the boots woman | named ch52 |
| Red Cap | — | errand boy | a name |
| the old man / the woman with the shoulder / the mender / the pie boy / the bread woman / the fruit woman / the eel woman / the chalk-board woman / the lantern woman / the nut boy and his sister / the wheezing man / the brothers / the boots woman / the widow / Torvin's wife | — | unnamed recurring roles | keep each a fixed colour across chapters |
| Dava, Tamsin, the Ashwood boy | DAH-va, TAM-zin | names on the board, ch8 | once only |

### Places (14)

| Name | Say |
|---|---|
| Denvash | DEN-vash |
| Ardenmere | AR-den-meer |
| Valdris | VAL-driss |
| Fenrow | FEN-roh |
| Weaver's Row, Merchant Row, Fen Street, Tallow Lane, Chandler Street, Lantern Street | as written; "Row" = ROH |
| the Cinder House | SIN-der |
| the post | the Compact office at the fish steps (common noun; unstressed) |
| the grey half, the four lanes, the cut, the triangle, the long quay, the fish steps, the Ranked core, the Unranked District | descriptive; no stress |

### Terms and invented words (22)

| Term | Say / handle |
|---|---|
| Kindling | KIND-ling (as in kindling a fire) |
| Arbiter | AR-bit-er |
| the Compact | KOM-pakt (noun) |
| sigil | SIJ-il |
| [SHATTERED] | SHAT-erd; brackets never voiced; ch3 bold = the plate word, once, flat |
| Path names: Tide, Blade, Stone, Shield, Force, Ember, Wind, Iron, Pressure, Ash | as written; "Wind" the noun |
| Tiers: Copper, Iron, Bronze, Silver, Gold; Unranked; Ranked | as written |
| "Rank 1", "Rank 10", "Copper 4s" | "Rank one", "Rank ten", "Copper fours" |
| "Copper Rank 0" (ch9) | "Rank nought" |
| Cu 3 / Cu 5 | the letters, "C-U three" — the text decodes it (ch8) |
| R3, R2, R4, R5, Bronze R1 (Log and ch59) | "R-three", "Bronze R-one" |
| def. (ch59, protected) | "defeated" |
| (Vell, h) / "the small h" | the letter h; the text explains it means "heard" |
| L., R. (Vell's ledger) | the letters |
| Thirdweek, Secondweek, Fourthweek | THIRD-week (one word, first syllable) |
| Over-under (after fix) | OH-ver UN-der |
| marks, half-marks, a quarter-mark | currency |
| vouch, vouched, unrated, assessed-Copper, Ledger-keeper, the book, the card, the call | as written |
| the step, the build, the crossing, the gap, the nod | Lira's/Cael's terms; no stress |
| 41-7843-V / 22-1190-H | "four-one, seven-eight-four-three, V" / "two-two, one-one-nine-oh, H" |
| Statute 14, Section 9; section 40; statute 19; Part Six; Section 1 | numbers as words |
| "the O leans" | the letter O |

Lexicon size: 46 people (plus the unnamed-role group), 14 places, 22 terms — **82 entries**.

---

## 5. Direction notes the segmenter and instruct files will need (not text changes)

1. POV cutaways: ch10 (Hesk), ch13 and ch23 (Vell), ch18 (Lira, second half), ch28, ch30, ch33, ch53, ch60
   (Coss), ch36 (Hesk, first half), ch38, ch42, ch55 (Lira), ch46 (Vell, opening). The "he/she" changes
   referent at the `---`; mark it.
2. Counts said inward: ch3 "One. Two. Three… Eleven." (the circle), ch19 "Four. Five… Nine." (the yard at
   midnight), ch58 Vell's "One." … "Ten." (aloud, level). Direct as the Meridian counts were.
3. Letters: salutation "*Cael,*" / "*Hesk,*", sign-off "*— H.*" / "*— Cael*" as a pause, not read as "dash".
4. The one bold word (ch3) and the three code blocks (ch40/42, 47, 58) each get their own segment and a long pause.
5. The all-caps signs (§2.3) in sentence case; "Mr" never occurs.
6. The two collisions beyond #29 (Coss/Doss; Marrow/Darrow) by register, as in §2.2, unless the owner takes
   the optional epithets (#27, #28).
