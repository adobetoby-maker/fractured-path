# Book 3 — *No Path Given*: line and listening proof

Scope: all 61 manuscript chapters, read as Breeze will meet them: one narrated segment per paragraph, `---` as a long pause, italics flattened, and fenced notices flattened line by line. Book 1's listening proof is the model for structure and judgment.

**No manuscript file was modified.** This report and `listening-notes.md` are the only files written by this pass.

## 1. Verdict

**PASS WITH ONE REQUIRED LINE FIX AND AUDIO DIRECTION.**

The manuscript is exceptionally clean after the completion lanes. There is one genuine aloud stumble, in ch49: a doubled `in`. I found no broken quotation, unattributable speaker change, clipped join, stray Markdown, or protected-line problem. The two paragraphs with odd straight-quote counts are both correct openings of continued multi-paragraph quotations.

The hearing remains followable by ear. Its formal role labels, direct addresses, and response structure distinguish Coss, Cael, Yorlan, Ilsev, Havel, Quenna, Naveth, Edran, Hobb, and the recorder even when the listener cannot see paragraphing or italics. The recurring four-person suppers are also attributable without added tags.

There are **181 paragraphs over 700 flattened characters**. They are listed in §2.6 only; length is not itself a defect, and `fpaudio.py` already splits them at sentence boundaries for synthesis.

## 2. Findings by category

### 2.1 Quotation marks and speaker identity

- **No unbalanced or mismatched quotation marks.** There are no curly quotation marks.
- **ch21 line 203:** the odd-count paragraph begins Karis's continued speech. Each intervening paragraph reopens the quotation, and the final paragraph closes it. Correct as set.
- **ch59 line 9:** the odd-count paragraph begins Yorlan's continued ruling. Each following ruling paragraph reopens, and the last closes. Correct as set.
- **Hearing, ch54–59:** speaker identity remains clear. Questions are attached to a named questioner, role, direct address, or immediate answer. The long ruling is explicitly introduced as Yorlan reading the panel's ruling and stays in his voice until its close.
- **Suppers and table scenes:** the Cael/Lira/Brom/Karis exchanges use action beats, stable character syntax, and orderly turn-taking. No repair tags are needed.
- Italic documents sometimes contain quoted speech, but flattening the italics does not change who owns the document voice.

### 2.2 Ear collisions

| Pair or cluster | Book 3 result | Direction |
|---|---|---|
| Coss / Doss | Doss does not occur in Book 3; no live collision | Coss = KOSS, clipped and formal |
| Karis / Kestrel | Kestrel does not occur; no live collision | Karis = KAIR-iss |
| Havel / Halvern | Halvern does not occur; no live collision | Havel = HAV-el; preserve the short first vowel |
| Vell / Velmere | Co-occur in ch1 and ch10 | VELL versus VEL-meer; give Velmere its second syllable |
| Wray / Greyvane | Co-occur repeatedly at the academy | RAY versus GRAY-vayn; keep the full second syllable in Greyvane |
| Quenna / Karis | Frequent shared scenes | KWEN-a versus KAIR-iss |
| Prynn / Wray | Archive/training roles keep them distinct | PRIN versus RAY |
| Yorlan / Naveth | Hearing/council contexts keep them distinct | YOR-lan versus NAV-eth |
| Oona / Quenna | Shared academy scenes remain clear | OO-na versus KWEN-a |
| Brom / Hobb | Shared training scenes remain clear | BROM versus HOB |
| Edran / Gerda | Shared academy/hearing scenes remain clear | ED-ran versus GER-da |

No name change or prose repair is warranted. Owner decision #6 leaves the established collisions unchanged, and decision #29's Halvern/Halden distinction has no Book 3 scene to solve. Owner decision #33 governs Cael and Lira.

### 2.3 Homographs and `as`

- `wound` occurs only as the past tense of *wind*: **WOWND**.
- `lead` is the verb/noun meaning to guide or an advantage: **LEED**, never the metal.
- ch23 `bow` is the weapon: **BOH**. ch59 `bow` is the gesture: **BAU**.
- `live` is **LIV** in its Book 3 uses. `row` is **ROH** where it names a line of seats or buildings.
- `read` and `record` change pronunciation by grammar; the surrounding clauses make every instance clear. Hearing narration uses noun **REK-erd** and verb **ree-KORD** conventionally.
- The full `as` pass found no sentence where the texture pass left a false or confusing “while” reading. The surviving temporal uses are intentional and locally clear; the comparison/manner uses do not need conversion.

### 2.4 Formatting the narrator meets

- **Fenced notices:** three blocks occur: the Compression notice in ch1, `[Drawn Channel]` in ch11, and the Ember notice in ch36. The renderer removes the fences, retains the line text, and adds terminal punctuation. These need a flat, system-register performance, not literal Markdown.
- **Brackets:** `[SHATTERED]` occurs in the protected ch59 ruling. Voice **Shattered**; do not speak “open bracket” or “close bracket.” The bracketed declaration names in notices are also voiced without brackets.
- **Italics:** `fpaudio.py` removes every asterisk. Log entries, binder entries, formal clauses, letters, notices, and the ruling therefore need direction-based separation from surrounding narration. The prose supplies enough introduction and exit context; no textual labels need adding.
- **Recorder dashes:** ch49's nine dashes and ch57's explanation are silence-count notation. Treat each run as a held silence in the quoted record; do not say “dash.”
- **Scene breaks:** every `---` has clean blank-line spacing. Keep the established long pause.
- **Registry number:** `41-7843-V` is “four-one, seven-eight-four-three, V.”
- **Other numerals:** speak ranks, clause/article numbers, days, weeks, bells, exchanges, box counts, and the ch21 drill sequence as words. Preserve the deliberate count rhythm rather than turning it into a list read at speed.
- **Abbreviations named in the brief:** no manuscript occurrences of `D1`, `D6`, `wk`, `Cu`, `Br`, or `R1`–`R6` remain. No expansion fix is needed.
- **Stray Markdown:** none. Code fences, italics, headings, and scene breaks are all structurally paired.

### 2.5 Typos and broken joins

- **One required repair:** ch49 `carried it in in three tied stacks` is a true doubled-word stumble. See §3.
- The apparent repetitions `that that`, five instances of `had had`, and `predecessor's predecessor's` are grammatical and intentional.
- No mid-clause paragraph ending, lower-case prose start, doubled space, tab, trailing space, or punctuation collision remains.

### 2.6 Paragraphs over 700 flattened characters — list only

Character counts remove Markdown asterisks and collapse whitespace, matching the text shape the narrator effectively receives before the segmenter's sentence split.

| Chapter | Characters | Opens |
|---|---:|---|
| ch01 | 756 | Cael knew the numbers, as everybody in Valdris knew them. But he… |
| ch01 | 708 | Cael knew it too. Declarations were the language an Arbiter used… |
| ch02 | 928 | Cael ate. It was hot and plain and there was enough of it, and h… |
| ch03 | 935 | Cael sat in the plain chair and understood what he had been give… |
| ch03 | 820 | The training hall came first, a single long floor under a high r… |
| ch03 | 873 | Three lines below, on the same day, Lira's name sat beside Re-ce… |
| ch04 | 748 | Brom stood in the middle of the section in his usual stance, low… |
| ch04 | 809 | He went back to his barley, and Cael watched him eat and thought… |
| ch05 | 895 | Cael had chosen it off the schedule on purpose. It was listed as… |
| ch05 | 830 | A chart hung on the wall behind the lectern, large and painted o… |
| ch05 | 735 | Cael was thinking of Brom at the midday rest on the road, refusi… |
| ch05 | 850 | He set his bag against the wall, and it turned out to be a stran… |
| ch05 | 914 | "Form efficiency. How much more you get out of a declaration, ra… |
| ch05 | 848 | He had seen the date on the public board already, and had known … |
| ch06 | 903 | She went away between the shelves, and he sat and read. The prov… |
| ch06 | 925 | Not by Quenna and not by Wray. They would be in the room, and wh… |
| ch06 | 789 | Wind-adjacent first: Lira's framework, drilled through every bou… |
| ch06 | 711 | And under all four, the thing that was not a fragment at all: ho… |
| ch06 | 1251 | They ran it eleven more times. The first three were bad, because… |
| ch07 | 817 | Someone had cleared it. The chalk lines of the six sections had … |
| ch07 | 731 | Quenna sat in the centre chair with a slate on her knee. To her … |
| ch07 | 705 | Cael knew within the first strike what she was testing. If his f… |
| ch07 | 1208 | The partner stood easy in the ring throughout. He did not sit, t… |
| ch07 | 1019 | He did not leave at once. The quiet a panel left behind it was i… |
| ch08 | 777 | Cael had watched him for most of an hour, filling a page. Glass … |
| ch08 | 890 | It was section four again, and Quenna again, standing at the cha… |
| ch08 | 1256 | That was what an observer was allowed to do, so he did it from t… |
| ch08 | 848 | The Stone Path page was the broad student's. Cael had watched hi… |
| ch08 | 777 | It was not an assessment, not exactly. The re-certification trac… |
| ch08 | 941 | The first exchange went the way a procedural bout was supposed t… |
| ch08 | 830 | The Force Path was not a fool, and in the third exchange he trie… |
| ch08 | 787 | Lira stood on the edge for a heartbeat, breathing, and Cael watc… |
| ch08 | 783 | She did not let him have distance. A Force Path's push needed ro… |
| ch08 | 1004 | Glass, from Edran. Stone, from Hobb. Shield, from Wray, from the… |
| ch08 | 744 | He had walked through the gate two weeks ago thinking of the obs… |
| ch08 | 1211 | He read back over the two weeks before he closed the binder, as … |
| ch10 | 736 | "I know a bit about being written down." Her voice dropped. "Fen… |
| ch13 | 1066 | Each line on the Compact's list turned into its own slip, and ea… |
| ch15 | 758 | It was not the bout she had fought in the second week. That one … |
| ch15 | 731 | He learned. Cael watched him learn it. For the rest of the excha… |
| ch16 | 765 | "It stops when something I'm seeing now agrees with something I … |
| ch16 | 717 | The second page set out the record. It did that accurately too. … |
| ch17 | 751 | "An exhibition bout, held in the formal yard, under standings ru… |
| ch18 | 804 | Glass ran on discrete commitments. Cael had known that in outlin… |
| ch18 | 839 | On the fifth and sixth days he confirmed it from three direction… |
| ch19 | 806 | She had been watching for that since the frost lifted, if she wa… |
| ch20 | 745 | Cael had half expected him to. He had expected, without ever qui… |
| ch20 | 764 | He did not get to the kitchen for nearly half an hour, because t… |
| ch21 | 706 | Quenna signed the strip. Cael took it and stood by the post a mo… |
| ch21 | 780 | He did it in the stable after supper, at the scarred table under… |
| ch21 | 868 | Karis had never seen the binder. Cael kept coming back to that t… |
| ch22 | 853 | He had not done that since the road. He read it often, but alway… |
| ch22 | 721 | He sat through a lecture at the third bell, the declaration ethi… |
| ch23 | 936 | He stayed out there long after the door had shut. The cold settl… |
| ch23 | 883 | He read it over once by the light of the single lit window in th… |
| ch24 | 727 | The annex was a narrow room at the end of the archive passage, w… |
| ch24 | 731 | That was the first thing, and it went into her like the wrong en… |
| ch24 | 978 | She had spent two years furnishing that room. That was the thing… |
| ch24 | 731 | She ate barley at the midday meal, which she hated, and a heel o… |
| ch24 | 854 | She ran the Ardenmere sequences in the near corner, the ones she… |
| ch25 | 708 | What she was offering was not small, and he would not let himsel… |
| ch25 | 958 | He had watched her Ember a dozen times from the edge of a sectio… |
| ch26 | 712 | It was not the exhibition. Nobody had climbed onto the roof of t… |
| ch26 | 893 | He did not. When Wray lowered her finger he stayed out at the ed… |
| ch26 | 844 | He had not seen her use it since Ardenmere. It was a thing she h… |
| ch26 | 820 | He knew what it was. He had spent his whole life inside records … |
| ch26 | 754 | It was the thing Karis had asked him about in the first week, th… |
| ch26 | 719 | "No." Wray said it at once, and firmly, and Cael saw that she ha… |
| ch27 | 785 | In the third exchange the Blade fourth-year began to come in and… |
| ch27 | 709 | The second bout went to her, and it was worse to watch than the … |
| ch27 | 784 | Nothing had gone wrong. That was the whole of it. Nobody had che… |
| ch27 | 727 | She had been in her second year at a school in the south, Copper… |
| ch28 | 1225 | He could not help it. He had never been able to help it. He had … |
| ch28 | 754 | It ran most of the afternoon. Brom came for the first hour and L… |
| ch28 | 839 | He waited to feel what he had always felt, all his life, when so… |
| ch28 | 706 | He did not say anything. He sat with the binder shut in front of… |
| ch29 | 717 | Wind-adjacent was first, and Lira's. He made himself go back pas… |
| ch30 | 839 | He told her. It did not take long, which was the worst of it. Th… |
| ch30 | 705 | She opened the ledger again, but she did not turn to the nulls. … |
| ch30 | 764 | Session nine had ridden with him since the road, small and shape… |
| ch30 | 787 | Cael went up to the residence wing and left them there. Halfway … |
| ch31 | 962 | Lira was at the front, with her shoulder unstrapped at last and … |
| ch31 | 704 | The third exchange went by slower. He had learned; she had shown… |
| ch31 | 840 | He knew her now. That was what he understood, standing three pac… |
| ch31 | 759 | "Whatever it is that closes it," said Karis, "someday there may … |
| ch33 | 736 | "That's Ternhall. Every Ember school in the country teaches the … |
| ch33 | 743 | The instructor dropped his hand, and Hobb set himself, and Karis… |
| ch33 | 711 | His framework had a seam, and he had known it since Ardenmere. W… |
| ch34 | 769 | "At Fenmark," she said, "I knew the right foot for the third tur… |
| ch35 | 717 | The presiding assessor may halt the match at any moment, at the … |
| ch35 | 933 | He tapered the last three days, as Vell had taught him to taper … |
| ch36 | 741 | The benches had stopped meaning anything. Students stood on them… |
| ch36 | 702 | Karis came forward, laying as she came, and a breath before her … |
| ch36 | 731 | He knew it as he had known the south chalk at his heels in the f… |
| ch36 | 822 | He would spend pages afterward trying to say what it was like, a… |
| ch36 | 746 | Her fourth channel lay ruined round her feet, her off hand still… |
| ch36 | 838 | Behind them the panel was breaking up. Quenna had gone back to t… |
| ch37 | 832 | He had carried the oldest of the four since Ardenmere and never … |
| ch38 | 888 | She wrote the match into it as she would have written any bout: … |
| ch38 | 768 | She did that six times between the fourth bell and the sixth, un… |
| ch38 | 868 | He was at the far end of the long table with the observation not… |
| ch38 | 781 | Seven clauses, and one word that could stop everything: that had… |
| ch39 | 827 | Quenna had written hers in the record's language. Her page would… |
| ch40 | 781 | It began under his breastbone, a sudden cold drop, the feeling o… |
| ch40 | 754 | On the Wednesday he made five marks. The first two came larger t… |
| ch41 | 913 | He had sat on the end nearest the far door. His feet had not qui… |
| ch41 | 1026 | But Denvash sat with him the whole time. It did not come as a me… |
| ch41 | 958 | The drafting records had been in three places, none of them wher… |
| ch41 | 776 | Then he had found the precedents, which had been easier, because… |
| ch41 | 799 | He did not try to explain the rest, because the rest did not fit… |
| ch41 | 739 | He put it in that night, in the flat language the form demanded,… |
| ch42 | 781 | It was the middle of the morning on the Monday of the nineteenth… |
| ch42 | 738 | That was the part he would turn over afterward and never get to … |
| ch42 | 716 | The walk took four minutes, and he spent every one of them count… |
| ch42 | 767 | "I have." Coss brought out a second paper, a thick packet tied c… |
| ch43 | 1053 | He felt it everywhere he went. In the stable at meals the talk c… |
| ch43 | 878 | It did not arrive as an idea, and it never had, for him, with a … |
| ch43 | 1008 | "There's a word in the code I can't find the bottom of," he said… |
| ch44 | 857 | "Before anybody hands out jobs," she said, "I'm taking mine, and… |
| ch44 | 784 | "Enactment order," she said. "That's how you'll read it." She tu… |
| ch44 | 766 | She took the concordance and he took the text, and the first aft… |
| ch44 | 819 | It was the concordance, in the end, that showed him the shape. H… |
| ch44 | 875 | On the Thursday, at the sixth bell, he went from the long table … |
| ch45 | 834 | It held him still, there in the cold. In those days the guilds h… |
| ch45 | 907 | He walked the road for eleven hours. He traced every revision an… |
| ch45 | 857 | He had spent two years reading things that did not want to be re… |
| ch45 | 788 | The defensive floor was the long hall beyond the training hall w… |
| ch45 | 979 | "It isn't a queue," said Wray. "That's the difference. Last time… |
| ch45 | 879 | Hobb came. It was his honest walking weight, both forearms up, t… |
| ch45 | 853 | The third round was where Cael began to see it, and he saw it be… |
| ch45 | 809 | The others had seen it too, and they were learning. Cael watched… |
| ch47 | 862 | It was all on one page now. The concession first, plain and whol… |
| ch50 | 1013 | "Your counsel has spent three weeks fighting my timetable," said… |
| ch50 | 809 | "I've written about you every quarter for two years," he said at… |
| ch50 | 769 | The cards were pasteboard, bought from the draper in bundles of … |
| ch50 | 737 | The waystation had kept its books as any working house on a guil… |
| ch50 | 1020 | Karis had learned the clerks before anything else, because it wa… |
| ch50 | 1095 | The traveller registers were not all alike, and that was still t… |
| ch51 | 782 | He read it again, and on the second reading his body understood … |
| ch51 | 857 | She did it at once, there at the reading shelf, while the lamp w… |
| ch51 | 752 | So he read it aloud, low, in the cold, from the register, with t… |
| ch51 | 871 | "Everything I'm going to say on Monday stands on one thing. The … |
| ch52 | 767 | There were three people in the whole of the service, so far as h… |
| ch53 | 774 | "Is not code." He put the spoon down. "If it were, there'd be no… |
| ch53 | 811 | He had counted them by candle in his room after the fire went ou… |
| ch53 | 1318 | Brom had written it down the way he wrote down a fetch drill, ev… |
| ch53 | 990 | "That's the one that's true." She watched him read it again. "I … |
| ch54 | 914 | It was not practice. Lira had a word for it, and the word was up… |
| ch54 | 862 | At the rope they stopped. There was a cord strung across the roo… |
| ch54 | 792 | It was perhaps twenty paces from the rope to the respondent's ta… |
| ch54 | 834 | The lecturer's dais at the end had been raised on the platform f… |
| ch54 | 986 | "Magistrate. Assessors." Coss spoke as he always spoke, evenly, … |
| ch54 | 806 | He read it in full, from the certified copy with Prynn's pencil … |
| ch55 | 842 | The tout was on it. He was four rows back and to the right, with… |
| ch55 | 820 | Edran said it. He said it as he had said he would, plainly, in t… |
| ch55 | 913 | He read the respondent's name and number as the registry held th… |
| ch55 | 807 | "There's one thing about his case I want you to have," she said,… |
| ch55 | 1004 | He gave each its district and its year and its name. The first w… |
| ch56 | 865 | "Procedure," she said. "Then you can go to bed. Tomorrow you are… |
| ch56 | 753 | "It isn't that I don't want you there." He made himself go on, b… |
| ch57 | 768 | The room was fuller than yesterday, if that was possible. The pe… |
| ch57 | 719 | He knew this quiet. It was the quiet of the main floor at the Ir… |
| ch57 | 1009 | "I read the code the way I'd read anybody I had to fight," he sa… |
| ch57 | 1124 | After the annex the boy read the appendix of disputed standings.… |
| ch57 | 758 | Nobody was restless. Nobody was whispering. Two hundred people a… |
| ch58 | 1403 | "I'd like to say where it isn't, one place at a time, so that no… |
| ch58 | 965 | "I'm not telling the panel the word is nothing," said Cael. "It'… |
| ch58 | 808 | "Four, in the Compact's own digests, in all the years they go ba… |
| ch58 | 1054 | "So I want to say exactly what I'm asking, and not one thing mor… |
| ch58 | 1019 | "The respondent has read the panel an empty line," said Coss, "a… |
| ch58 | 740 | "Because a list doesn't consent to anything, Assessor. It holds … |
| ch58 | 1026 | "And the Warden's own exhibits tell the panel the same thing. Th… |
| ch59 | 724 | "No," said Coss. "You made it true." He held Cael's eyes. "That … |
| ch59 | 712 | He wrote the morning in Denvash: the station, the instrument, th… |
| ch59 | 830 | He knew what the desk above him would want. He had known since t… |
| ch59 | 778 | The officer of contact of record recommends as follows. The subj… |
| ch60 | 850 | Letters came up the hill on every coach, every one of them addre… |
| ch60 | 1006 | "Something that's there. Not the lack of their right. A right of… |
| ch60 | 1012 | She did not read it all that night. She read it at the table, sl… |
| ch61 | 823 | The boxes had been coming back since the Wednesday morning, thre… |
| ch61 | 731 | "When you were reading the schedule," she said, "somewhere near … |

### 2.7 Protected lines

BOOK_MAP §9 and `protected-patterns.txt` were checked against the sole proposed repair. The repair does not touch protected wording. No protected line is proposed for change.

## 3. Exact line fixes

Each old string below was checked across `manuscript/chapter-01.md` through `chapter-61.md` and matches **exactly once**.

### 3A — Required before render (1)

1. `manuscript/chapter-49.md`
   old: `the Warden's aide had carried it in in three tied stacks and gone away again.`
   new: `the Warden's aide had brought it in three tied stacks and gone away again.`

### 3B — Optional, engine-safety only (0)

None. The remaining risks are better handled in the Breeze direction than by changing clean prose.

## 4. Pronunciation lexicon for Book 3

Owner-confirmed pronunciations govern where stated. Shared Book 1 entries that recur in Book 3 are carried forward unchanged.

### People

| Name | Say | Who / note |
|---|---|---|
| Cael | **KAYL** (one syllable) | owner-confirmed, decision #33 |
| Caelen Hesk-ward | **KAY-len HESK-ward** | full name; `Hesk-ward` as two words, stress HESK |
| Hesk | **HESK** | grandfather; Book 1 carry-forward |
| Lira | **LEER-a** | owner-confirmed, decision #33 |
| Vell | **VELL** | Ledger-keeper; Book 1 carry-forward |
| Coss | **KOSS** (rhymes with *moss*) | Compact Warden; Book 1 carry-forward |
| Feryn | **FERR-in** | Pressure fighter; Book 1 carry-forward |
| Ilsev | **IL-sev** | senior assessor; Book 1 carry-forward |
| Brom | **BROM** (rhymes with *from*) | Iron Path |
| Karis Dellenmoor | **KAIR-iss DEL-en-moor** | Ember Path; keep unlike Kestrel |
| Quenna | **KWEN-a** | assessor |
| Prynn | **PRIN** | archivist |
| Wray | **RAY** | instructor; keep distinct from Greyvane |
| Yorlan | **YOR-lan** | magistrate |
| Naveth | **NAV-eth** | provost |
| Oona | **OO-na** | observer-track child, then Anchor |
| Hobb | **HOB** | defensive student |
| Edran | **ED-ran** | Glass Path student |
| Gerda | **GER-da** | re-certification candidate |
| Havel | **HAV-el** | delegation recorder/assessor; not Halvern |
| Reydan | **RAY-dan** | Compression fighter |
| Marlowe | **MAR-loh** | Ternhall lecturer |

### Places and institutions

| Name | Say / handle |
|---|---|
| Denvash | **DEN-vash** |
| Ardenmere | **AR-den-meer** |
| Valdris | **VAL-driss** |
| Greyvane | **GRAY-vayn**; voice both syllables, unlike Wray |
| Velmere | **VEL-meer**; voice both syllables, unlike Vell |
| Ternhall | **TERN-hall** |
| Fenmark | **FEN-mark** |
| Sarnholt | **SARN-holt** |
| Wexley | **WEKS-lee** |
| Dellenmoor | **DEL-en-moor** |
| the Ironyard | **EYE-ern-yard** |
| the Compact | **KOM-pakt** (noun) |

### Paths, ranks, documents, and technical terms

| Term | Say / handle |
|---|---|
| Kindling | **KIND-ling**, as in kindling a fire |
| Arbiter | **AR-bit-er** |
| sigil | **SIJ-il** |
| `[SHATTERED]` | **SHAT-erd**; brackets silent |
| Path names: Anchor, Ash, Blade, Compression, Ember, Force, Glass, Iron, Pressure, Shield, Stone, Tide, Wind | ordinary pronunciations; `Wind` is the noun |
| Tiers: Copper, Iron, Bronze, Silver, Gold; Ranked, Unranked | ordinary pronunciations |
| `Iron Rank 3`, `Priority Level 4`, `Copper 5` | numbers spoken as words |
| `[Drawn Channel]` | **drawn channel**; brackets silent |
| `Suppression-Advisory Watch` | speak the full compound, with a light pause at the hyphen |
| `41-7843-V` | **four-one, seven-eight-four-three, V** |
| Power Log / Log | `Log` as a document title where context marks it |
| binder / observation notebook / marbled book | common nouns; document voice begins only after the prose cue |
| the step, the build, the framework, the redirect, the surface read, the spark, the letting-go | character terms; natural stress, no capitalization effect |
| `---` | long pause; never voiced |

## 5. Direction notes for segmentation and instruction files

1. Keep **Cael = KAYL** and **Lira = LEER-a** in every chapter direction.
2. Give notices a neutral system cadence. Do not voice brackets, Markdown fences, asterisks, or scene-break dashes.
3. Give italic Log, binder, letters, charter text, deposition text, and ruling text a slight register change. Return cleanly to narrative voice at the next prose cue; do not add quotation wording that is not present.
4. In ch49 and ch57, render recorder dashes as measured silence, not the word “dash.”
5. In ch54–59, distinguish formal speakers by cadence rather than by character voices: Coss precise and clipped; Cael plain and deliberate; Yorlan flat and institutional; Ilsev exact; Quenna dry; Naveth restrained. Breeze remains a single narrator.
6. Preserve the slow count architecture in drills, bells, weeks, ranks, clause numbers, and box inventories. Read `41-7843-V` digit by digit as specified above.
7. For the co-present collisions, sustain **VELL / VEL-meer** and **RAY / GRAY-vayn**. No special treatment is needed for absent Doss, Kestrel, or Halvern.
8. Long paragraphs may be split only at sentence boundaries, as `fpaudio.py` does. Do not introduce extra dramatic pauses inside legal arguments merely because a synthesis chunk changed.
