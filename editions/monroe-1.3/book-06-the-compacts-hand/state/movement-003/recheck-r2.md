# THIRD REPAIR

**Scope and counts:** r2 resolves **81 of the 91** passages sent back for source-distance repair and leaves **10 STILL TRACKING**: ch14 **3**, ch15 **0**, ch16 **0**, ch17 **1**, ch18 **1**, ch19 **2**, ch20 **3**. The prior 45 resolved passages do not independently regress, so the complete 136-passage audit now stands at **126 RESOLVED / 10 STILL TRACKING**. I found **0 new tracking passages** in the added scenes. There is also **1 exact canon line fix** in ch19: the new Lira/Hesk recollection contradicts Book 4's on-page letter.

This is a narrow third repair, not another whole-movement rewrite: recompose the 10 listed local units, apply the one exact ch19 line fix, and synchronize the Movement 3 ledger entries identified below. The mechanical gates all pass, but the same manual standard used in r1 remains controlling.

## Findings

### Diff against `pre-repair-r2/`

Plain `diff -U0` (not git) confirms substantial r2 work in every chapter.

| Chapter | Diff hunks | Added lines | Deleted lines | Pre-r2 words | Current words |
|---|---:|---:|---:|---:|---:|
| 14 | 73 | 67 | 89 | 4,702 | 3,746 |
| 15 | 56 | 64 | 52 | 3,540 | 3,314 |
| 16 | 58 | 57 | 63 | 4,104 | 3,780 |
| 17 | 20 | 34 | 16 | 4,435 | 4,805 |
| 18 | 27 | 25 | 30 | 4,583 | 4,319 |
| 19 | 59 | 63 | 55 | 4,737 | 4,411 |
| 20 | 84 | 81 | 90 | 5,640 | 5,306 |
| **Movement** | **370** | **391** | **395** | **31,741** | **29,681** |

The shell word counts include headings and differ slightly from the author's formula count, but the direction and scope are clear. R2 genuinely changes entry points, objects, speakers, and local order. The remaining defect is confined to the 10 passages below.

### Source-distance passage audit

Method is unchanged from r1. Each key is the original `source-tracking.md` key. A passage is RESOLVED only when the source's substantive local progression no longer survives as a recognizable prose unit. A new opening object alone is not sufficient if the passage then walks through the same observations in the same order. Conversely, the hearing's plan-fixed event architecture may remain; the local observation order and carrier must be newly composed.

The source column below gives the exact identifying sentence or sentence-cluster, with an ellipsis only where the full source paragraph is longer than needed to identify the tracked unit. The current column records the r2 order/carrier beside it.

| Chapter | RESOLVED | STILL TRACKING | Total |
|---|---:|---:|---:|
| 14 | 21 | 3 | 24 |
| 15 | 12 | 0 | 12 |
| 16 | 11 | 0 | 11 |
| 17 | 3 | 1 | 4 |
| 18 | 4 | 1 | 5 |
| 19 | 12 | 2 | 14 |
| 20 | 18 | 3 | 21 |
| **R2 set** | **81** | **10** | **91** |

#### Chapter 14

| Key | Source sentence / cluster | Current r2 order or carrier | Verdict |
|---|---|---|---|
| `14:19` | ch5:7: “For three years, every document … had crossed his desk as a *query* … This one crossed it as information. … Not asked. Told.” The adopted advisory follows. | Printed recipient list first; then prior papers wanting something; this paper wanting nothing; then the advisory marked adopted. The object is new, but the query/request contrast still leads to the adopted sentence in the source order. | **STILL TRACKING** |
| `14:33` | ch5:13: “Then he read the whole instrument once, at his own pace, with the office quiet enough to hear paper.” | Removed. He turns the bundle over and goes directly to the authorities table. | RESOLVED |
| `14:39` | ch5:15: “He did not need chapter fourteen read to him. He had written evaluations that triggered it. Twice.” | The daughter's kept letter comes first; the two files appear only as its context. | RESOLVED |
| `14:49` | ch5:7: he finds his sentence in the petitioner's paragraph, marked “*adopted*.” | The back-leaf authorities table carries “Advisory … (adopted)”; he never turns to the paragraph. | RESOLVED |
| `14:57` | ch5:19: “He got the enrollee's file out … because a finding was not a memory.” | The ruled interview sheet emerges after the letter-book; the memory maxim is gone. | RESOLVED |
| `14:61` | ch5:21: thickened file → nine leaves → observation schedule and interview sheet. | The boy's question is seen first, followed by the empty ruled twelfth line; the thick-file/nine-leaf catalogue is gone. | RESOLVED |
| `14:69` | ch5:21: he reads the eleven in order, then recognizes the unwritten twelfth. | The blank twelfth line is the object; the eleven are not reread in sequence. | RESOLVED |
| `14:75` | ch5:23: being right to decline the question has cost the file its usefulness. | A scrap sentence about the proceedings using only his manners is written, tested, and burned. | RESOLVED |
| `14:77` | ch5:25: “He put the leaves back in order and squared them and returned the file to the stack.” | Removed; the sheet goes back and he goes home. | RESOLVED |
| `14:93` | ch5:35: “Four for four. It was not a large sample. It was every instance there was.” | Four pasted acknowledgments are checked in reordered case order; there is no sample declaration, and the failed reassurance is what lands. | RESOLVED |
| `14:97` | ch5:31: clerk's pen pauses over routing → Vastin supplies the route → clerk writes it. | Evening blot first; the stopped pen and supplied route are reconstructed from the mark. The blot, not the live exchange, carries the beat. | RESOLVED |
| `14:119` | ch5:39: junior arrives with troubling file → review finds ordinary variance → “continue observation” → junior leaves reassured → Vastin lingers over copy. | Pinned thank-you note first; the junior's own floor description backfills the hour. The local scene has new dialogue and a new entrance. | RESOLVED |
| `14:139` | ch5:39: “The junior thanked him and went down, reassured. Vastin sat afterward with the file's copy for longer than the file warranted, and could not have said why.” | After the same reassurance, the copy remains, moves from *done* to *held*, and Vastin again looks longer without being able to say what he is looking for. The frame-shop scene follows, but this local unit retains the source progression and narrator carrier. | **STILL TRACKING** |
| `14:157` | ch5:45: “From the registry seat, sir. By seat courier, not the post.” | No live delivery dialogue; a discarded red-stamped wrapper starts the reconstruction. | RESOLVED |
| `14:161` | ch5:55: registry-seat stock and impressed seal are catalogued as a grade before the words. | Wrapper → folder → tread → arranged face → sentences. The reply grade is not catalogued. | RESOLVED |
| `14:169` | ch5:63: he has written a hundred sister refusals; they close a door cleanly and leave nothing to grip; he now recognizes the technique from the receiving side. | His pen writes the familiar guild-hall formula; he stops, recognizes it “from the other side,” recalls teaching it as decent, recalls an earlier field assessor, then rewrites it. The live action is useful, but the same write/recognize/justify/remember progression and narrator explanation survive. | **STILL TRACKING** |
| `14:177` | ch5:119: “They refused it in two sentences without citing a provision at all. That's not a ruling.” | The beat is carried by Vastin striking his own uncited formula and writing a cited, actionable refusal. | RESOLVED |
| `14:179` | ch5:65: fully constituted → full before he asked → schedule built by people who knew the desired result. | A pinned slip gives the two dates and asks who filled five chairs in four days; it does not answer. | RESOLVED |
| `14:181` | ch5:67: “the sentence had cost the sender nothing.” | Removed. | RESOLVED |
| `14:187` | ch5:85: clerk comes at the bell and finds the Archmarshal writing. | The scene opens after the clerk's one non-work sentence has already been spoken. | RESOLVED |
| `14:193` | ch5:95: Vastin orders a candle and orders it charged to his name. | The clerk brings the candle unasked and enters it himself; Vastin discovers the entry next morning and leaves it. | RESOLVED |
| `14:215` | ch5:105: the third page costs most because it distinguishes an honest instrument limit from a fault and applies the sentence to the boy. | The finding's claims are recalled end-first; the “third page cost” progression is gone. | RESOLVED |
| `14:221` | ch5:81: the ninth page's last paragraph is written slower because it is the paragraph an evaluator should not write. | The paragraph is read aloud to the empty room to test whether it stands. | RESOLVED |
| `14:227` | ch5:107–109: reads back → best finding in a decade → own locked records → unprecedented tab. | Morning drawer check → tab → claims recalled backward → rain walk home → blank addressee line. | RESOLVED |

#### Chapter 15

| Key | Source sentence / cluster | Current r2 order or carrier | Verdict |
|---|---|---|---|
| `15:35` | ch6:9: assistant returns from Ostrand with four market sheets and a receipt. | Printer's ink on both cuffs is first; she has entered the shop and carries a duplicate print she wants to return. | RESOLVED |
| `15:47` | ch6:9: “Six titles in Ostrand alone,” followed by the catalogue. | The catalogue is reduced to one late clause after Brom has priced the market. | RESOLVED |
| `15:51` | ch6:11: seller is asked what sold before challenge/tournament → no series → series begun for Cael → second press. | The printer tells his own shop story while his boy inks; the two presses appear before the wager and origin story. | RESOLVED |
| `15:69` | ch6:11: Karis says to put the press owner in Cael's notebook. | She writes *the printer* on a slip and pushes it across without speech. | RESOLVED |
| `15:77` | ch6:13: Cael derives the weekly working-man's wage figure. | Brom states “A carter's year. Every week.” first and works backward to it; Lira then prices the copper. | RESOLVED |
| `15:105` | ch5:115: counsel hears sideways at the wharf inn, drives up, and reports. | “When did he get it?” / “He hasn't” comes first; “The wharf” follows; Cael reconstructs the inn later. | RESOLVED |
| `15:127` | ch5:117: Withrow hears the sentence twice, says she has written it, and recalls teaching it as kindness. | She silently opens the drafting book to model thirty and her nineteen-year-old margin note, *the kindest one*. | RESOLVED |
| `15:151` | ch5:119: Karis reads the two provisions aloud and counts their uses. | She reads nothing aloud; the open digest carries the proof, Lira reads the number, and Karis gives the two-door conclusion. | RESOLVED |
| `15:167` | ch5:121–123: counsel gives the table her standing explanation on the stair. | Her warning is left on a card propped at the top stair. | RESOLVED |
| `15:205` | ch5:133: Brom's look at Seln → stair explanation that Seln meant Vastin and himself. | Brom asks Cael “Who?” and “And?”; Cael has to supply the second answer. | RESOLVED |
| `15:223` | ch5:117: log records that Withrow taught the refusal as kindness. | One line records the object fact: Withrow wrote *the kindest one* at nineteen. | RESOLVED |
| `15:227` | ch5:139: log contrasts disputing the finding with declining to contemplate it. | Replaced by the line about Brom making Cael say the answer himself. | RESOLVED |

#### Chapter 16

| Key | Source sentence / cluster | Current r2 order or carrier | Verdict |
|---|---|---|---|
| `16:3` | ch6:19–21: post sacks overwhelm the house; Bracken builds four intake piles and records counts. | Cael reads the already-ruled daybook columns upside down; no sacks-to-procedure progression. | RESOLVED |
| `16:19` | ch6:21–23: fourteen houses write about the clause; Bracken explains they ask about the provision, not Cael. | Green-taped *Houses. Answered.* bundle; one fair copy; Bracken says only “Fourteen.” | RESOLVED |
| `16:61` | ch6:17: second correspondent waits at the switchback; Rooke finds him. | Rooke's satchel goes down first; then a hat on the milestone resolves into a waiting man. | RESOLVED |
| `16:93` | ch6:37: visitor log → counts → one visitor's question → Rooke moves drills. | The visitor's question is quoted first; Lira then reveals the second ledger, the counts, and Rooke's reading practice. | RESOLVED |
| `16:119` | ch6:25: Lira adopts the sacks and sorts the institutional mail before the three named piles. | The schoolroom letter is already isolated; three one-word slips reveal the system. | RESOLVED |
| `16:127` | ch6:25: kind pile is largest; its contents are catalogued; child letter is read. | Cael takes one item from each pile; Lira takes the unkind one back unread. | RESOLVED |
| `16:153` | ch6:29–33: Ephram says Cael is a case, distinguishes stories/cases/files, and notes the faculties teaching him. | A faculty syllabus physically places *The Halcenvane matter (pending)* in week nine; file versus syllabus carries the joke. | RESOLVED |
| `16:177` | ch6:41: fee query arrives → Karis calls it proper → one careful clerk versus a pattern. | Cael reads Karis's answer first and infers the question printed on its back; no narrator gloss. | RESOLVED |
| `16:195` | ch6:43–45: assistant reports at length → says she was boring → Karis says accuracy under surprise is the work. | “I was boring” is the entrance; Karis orders “Start at the end”; the encounter is told backward. | RESOLVED |
| `16:229` | ch6:35: “The cost landed on the others first.” | Hesk's book gives four columns and total lines, with *0* under Cael's own. | RESOLVED |
| `16:245` | ch6:47: log says the cost has begun landing on others and “the order is the thing I got wrong.” | Removed; the zero carries the conclusion, followed by Cael walking wing three at night. | RESOLVED |

#### Chapter 17

| Key | Source sentence / cluster | Current r2 order or carrier | Verdict |
|---|---|---|---|
| `17:168` | ch6:53: adjudication office transmits the complete file with Umber's covering note. | Umber's unsteady signature is seen first; only then is the note exposed. | RESOLVED |
| `17:174` | ch6:55–61: Karis maps the no-discretion transmission, the parcel, the last sentence, and its mandatory reading into the minute. | Cael calls it another true number; Brom says *not me*; Karis corrects to *not in my name*; Lira asks whether anything could be withheld; “No.” | RESOLVED |
| `17:222` | ch6:77: Bracken objects to faculty release; Withrow explains why libraries outlast rulings. | Three signed release sheets appear as objects after the sitting, carrying *For teaching. Let them argue.* and Bracken's reservation/overrule. | RESOLVED |
| `17:230` | ch6:81–83: Umber, Vastin, and Ilsev each file true reports; every true report becomes an exhibit; the machine runs on true reports “the way a mill runs on water.” | The log moves from Ephram's true chart and Umber's true sentences to “every true thing” reaching the other table, then to the machine burning honest reports like seasoned oak. The examples and metaphor noun change, but the same truth-report → hostile use → consuming-machine sequence remains in the same Log carrier. | **STILL TRACKING** |

#### Chapter 18

| Key | Source sentence / cluster | Current r2 order or carrier | Verdict |
|---|---|---|---|
| `18:37` | ch6:103: Ephram counts the statement's words and contrasts them with Auremont's forty-page faculty. | He counts silently on his fingers to fifteen and looks at his hands; the faculty contrast is gone. | RESOLVED |
| `18:55` | ch6:109–113: fossil provision → recorded uses → never a Gold → why Golds do not file → new total after Daeva. | Digest table beside receipt → Lira reads “No Golds” → Karis explains why → “Forty-five, now.” The count changes with the edition, but the source's local sequence and explanatory carrier remain. | **STILL TRACKING** |
| `18:97` | ch6:119: private letter arrives; Cael recognizes Daeva's hand from *Overdue*. | Seln holds it a beat, says “Auremont,” and lays it face down. | RESOLVED |
| `18:113` | ch6:127: four readings → direct/no comfort → recognition that Daeva lived the mirror of his treatment. | He does not reread; copying it into the Log reveals the dash, missing salutation, and postscript placement before the Storm-piece connection. | RESOLVED |
| `18:123` | ch6:131–135: Log reads the letter → letter filed with Hesk's and Vell's pages behind the old volume's board. | Copy into the Log → one interpretation line → letter pinned inside the back board of Hesk's current book opposite the cost column; Bracken's night entry follows. | RESOLVED |

#### Chapter 19

| Key | Source sentence / cluster | Current r2 order or carrier | Verdict |
|---|---|---|---|
| `19:21` | ch7:43: none names Cael; each touches an attached person; each is lawful; together they form a pattern. | Lira notices there is no bean for Cael; Seln answers, “That's the way to know it isn't a mistake.” | RESOLVED |
| `19:31` | ch7:47–53: Lira names the certification file, the buried Fenmark entry, and the correction above it. | She asks only whether Fenmark was requested by name and leaves the buried history unsaid. | RESOLVED |
| `19:51` | ch7:61–63: Brom asks whether the query shows at the estate; Seln explains the open ledger and says Brom's father is entitled to it. | Seln first asks who reads Velmere's post; “My grandmother”; only then does he explain the open query book. | RESOLVED |
| `19:55` | ch7:67: Karis writes four offices in a column and rules an empty fifth line. | Four written slips under four beans plus one blank slip. | RESOLVED |
| `19:65` | ch7:75–83: fifth letter arrives; hand recognized; Cael opens it walking and carries the third paragraph to the table/window. | Seln brings it from the evening sort and places it unopened on the blank slip; Cael opens and reads it sitting. | RESOLVED |
| `19:79` | ch7:83: Cael reads the third paragraph again, carries it fast to the residence, and reads it aloud at the window. | Cael reads silently and passes it to Brom, who reads the protected paragraph aloud. | RESOLVED |
| `19:135` | ch7:121–123: Karis says the four are about the circle, identifies Hesk under the ninth category, and asks somebody to say they noticed. | Karis physically separates the Denvash slip, names what the inquiry is really finding, asks somebody to say it, and Brom answers “Said.” | RESOLVED |
| `19:143` | ch7:129–131: Lira lists the wins, contrasts the men in Denvash, then asks what they do the day after. | The protected day-after line comes first; she explains the sittings/Denvash contrast afterward. | RESOLVED |
| `19:153` | ch7:137–141: Withrow reads standing; Cael counts her pause; she names the trade licences and title. | Cael reads the letter aloud; her pen stops in the air and is laid down before she enters through “The girl.” | RESOLVED |
| `19:177` | ch7:149–153: haulier's rank/Path/age/trade/family/property, then nine inventory categories. | Withrow's old margin note gives initials, children, house, then Path/rank/trade; the flour sack is the story's first object. | RESOLVED |
| `19:191` | ch7:161: he goes east past the last station → it takes eighteen months → beyond the line he stops producing records. | “The last record” is an eastbound ferry toll at the last station → eighteen months → after the ferry there is nothing because records were her only eyes. The first noun changes, but the action/duration/records-stop sequence and Withrow's speech carrier are unchanged. | **STILL TRACKING** |
| `19:199` | ch7:161–165: grandfather's *grew up in it* entry → licence review → review can be arbitrarily slow → protected hand-on-clock line. | Cael asks what happens to Hesk; the protected line comes first; Withrow explains the ninth heading and review afterward. | RESOLVED |
| `19:207` | ch7:167–169: Withrow says she is still choosing, the word costs more, she has priced it, and she is paying. | She writes *Choosing* wordlessly in the old code margin and sends Cael to bed. | RESOLVED |
| `19:213` | ch7:173–175: Log: winning sessions/filings → men measuring the shop → asks where system ends and people begin because the difference is hard to find. | Log becomes *ours / theirs* columns: sittings and filings ours → Denvash/tin box theirs → he cannot find the line between text and people. The typography changes, but the same win/Denvash/vanishing-line progression remains in the same Log carrier. | **STILL TRACKING** |

#### Chapter 20

| Key | Source sentence / cluster | Current r2 order or carrier | Verdict |
|---|---|---|---|
| `20:103` | ch8:29–35: evaluation-seat covers off → Cael recognizes Ilsev → empanelment read. | Lira whispers “That's her” before Cael looks; he reads the five chairs and Ilsev through Lira's cue. | RESOLVED |
| `20:119` | ch8:37: future Log calls Ilsev the Compact's most honest instrument, installed to legitimize the machine. | Karis whispers that they put the straightest person in the middle so nobody looks past her. New speaker and immediate whispered carrier. | RESOLVED |
| `20:121` | ch8:39: Havel logs the opening and does not look at the respondent all morning; Cael interprets the not-looking. | Brom says “None,” his count; Cael identifies the count and does not supply the source's full moral sentence. | RESOLVED |
| `20:123` | ch6:115: Daeva statement read into the minute → received → set aside → Cael narrates the rhyme with Vastin. | Clerk reads it; hood receives and puts it on the pile; Cael writes days *44* and *54* and Karis nods. | RESOLVED |
| `20:141` | ch8:47: Jent concedes lawful execution first. | Counsel's prewritten *EXECUTION* heading is struck; the concession is backfilled from the mark. | RESOLVED |
| `20:143` | ch8:49: Jent concedes the provision is law and adopts the house's provenance. | The second margin heading, *PROVISION*, is struck and backfilled. | RESOLVED |
| `20:145` | ch8:51: Jent concedes the documentation, repeats the compliment, and insists “every word” enter the minute. | The third margin heading, *RECORD*, is struck; “Every word” is the remembered instant of the stroke. | RESOLVED |
| `20:171` | ch8:67: Jent tenders Umber's file, cites it once by page, and omits the match. | He gives one page number; Karis writes it down and does not look it up. | RESOLVED |
| `20:173` | ch8:69–71: Jent sits; Cael's Log explains that he is courteous, truthful, and a good instrument used well. | Lira says she likes him; Cael agrees and calls that the trouble. | RESOLVED |
| `20:193` | ch8:81: Greyvane ruling → four prior challenges → well-resourced adversarial testing → each lost on the text. | “The shelf” gives Greyvane → four older rulings → four houses with money and counsel → lost on the text. Moving the unit to third in the larger argument does not change this passage's internal sequence or counsel carrier. | **STILL TRACKING** |
| `20:195` | ch8:83: integrity provisions' origin in instrument audits → ninety-second preamble → ninety-one uses divided by object/person → none about what a person is. | Preamble makes pencils go down → ninety seconds → instrument purpose → Karis's ninety-one → things/persons/none about what a person was. This is the same local observation sequence in the same courtroom argument carrier. | **STILL TRACKING** |
| `20:203` | ch8:85–87: hood asks incapacity-in-law versus never applied; counsel answers “the second.” | Counsel's answer comes first; Cael infers the hood's question from it. | RESOLVED |
| `20:215` | ch8:93: demonstration record → four panels/season/tournament/inspection → twenty-two officers named one by one. | Twenty-two names are the entrance and physical action; Ilsev writes at her own name; record summary follows the names. | RESOLVED |
| `20:225` | ch8:97: closing asks seat to prefer human evaluators over instrument silence; “The only thing that has changed is who is asking.” | New close: measure him with the instrument that cannot see him; twenty-two names; “Ask them.” | RESOLVED |
| `20:255` | ch8:113: ruling runs enrollment → clause → record → charter. | Reheard in reverse: charter → record → clause → enrollment. | RESOLVED |
| `20:259` | ch8:117: gallery starts moving mid-ruling; boards rise and one correspondent half-stands. | A correspondent knocks his hat to the floor; Lira catches Cael's sleeve; the second paragraph continues. New physical carrier. | RESOLVED |
| `20:265` | ch8:121: “Both things at once. You are lawful. The machine will proceed.” | Removed. The r1 orientation beat remains later in its required plain-language form. | RESOLVED |
| `20:269` | ch8:125–137: Ilsev asks leave → asks scope → hood answers → she requests exact minute → records it herself. | Hood's answer is heard first; question inferred; Karis names the chair-fencing; exact-minute action follows. | RESOLVED |
| `20:293` | ch8:141–143: four couriers in four directions → paragraph will be printed → public splits it into win versus fraud. | Runner collides with Brom → three more → “four towns by tonight” → Cael imagines the printer needing two opposing headlines. The multi-speaker recollection is new, but the same couriers/dissemination/two-readings progression survives. | **STILL TRACKING** |
| `20:299` | ch8:145–155: Jent stops beside counsel and marks her third movement; counsel analyzes his cost-free accuracy. | Jent stops beside Karis and asks whether she counted the ninety-one herself; counsel's next-time conclusion follows in the coach. | RESOLVED |
| `20:333` | ch8:160–176: coach/river → paper-versus-proceeding exchange → one-line Log at ferry → Seln's final line. | Ferry watcher and document cases → far-landing exchange → protected Log line → protected Seln line. The protected ending stays, with a new observation causing its silence. | RESOLVED |

### Why the 10 remain

The remaining units are not failures of vocabulary. Each has a new noun, surface image, or entrance, but then retains the source sentence's internal chain:

- ch14: direct-request history → no request → adopted words; reassurance → inexplicable lingering; familiar refusal → receiving-side recognition → old victim.
- ch17–18: true report → hostile institutional use → consuming-machine metaphor; old uses → no Gold → explanation → new total.
- ch19: eastward last station → eighteen months → records stop; paper wins → Denvash loss → system/person line disappears.
- ch20: Greyvane → four litigated losses; preamble → ninety-one-use breakdown; couriers → fast spread → two contradictory public readings.

These are bounded passages. Their surrounding scenes, including the hearing's plan-fixed macro-order, do not need to be rebuilt.

### New tracking audit: r2 additions

**No new tracking found.** I checked each added scene directly against source chapters 5–8.

- **Vastin at the frame shop and walking home:** new setting, new mender, wet-frame/shim problem, rain walk, and no source-local observation chain.
- **The Current's “went short”:** new close-range consequence of the wing-three bout; the opponent, physical clue, and “step” cover are original to this movement.
- **Rooke on Lira's heel:** new coaching beat caused by the lamp closure; no source analogue.
- **Karis and counsel choose the hearing order:** new pre-hearing scene, new slips and steel-rule invention. The resulting hearing must still carry planned evidence, but the scene itself does not track source prose.
- **Bracken's daybook:** new night scene, new self-entry, and a character-specific consequence of abandoning the counter.

### Continuity and r1 protections

#### Passed

- **Velmere letter:** ch16 puts it unopened in Brom's left inside pocket. Ch18 shows the cream envelope on the frame and Brom's hand returning to the left side. Ch19 says the dark-red seal is still whole and the letter unopened. Ch20 explicitly distinguishes Karis's slip in the right pocket from the sealed Velmere letter in the left. Ch17 does not contradict the chain.
- **Seln / Shadow:** no disclosure of Shadow, its seal, or its reason appears in ch14–20. The M6 knowledge boundary remains intact.
- **Hearing orientation:** both r1 beats remain. After Jent: “What was left was one question … may the registry stand him in a frame?” After the ruling: “What they had won, they had for good … What they had not won was the only thing that could still reach him.”
- **Town count:** ch15 says three other towns besides Ostrand and immediately totals “Four towns.” Ch20 says “four towns by tonight.”
- **Protected and packet wording:** the denial, tab, Seln's benched line, Daeva statement and letter, Hesk paragraph, “Nine weeks. They are in the sixth,” the day-after line, the hand-on-clock line, final paper/proceeding exchange, counting-doors line, and Seln's last line are exact. The overlap check reports 13 protected runs and zero unprotected runs.
- **Dropped advisory quotation:** M3 does **not** require the full three-sentence quotation. The protected-pattern entry assigns that quotation to **M1**; BOOK_MAP's M3 spine and `packets/MOVEMENT-003.md` require that Vastin's sentence be adopted, not quoted whole. Ch14's authorities-table entry satisfies M3. The two fewer protected overlap hits therefore do not represent a missing M3 line.
- **Knowledge boundaries:** Daeva's letter remains Cael-only; Lira knows a letter came but not its text. Vastin's junior-file unease remains unnamed. Havel's note, the returns' wording, falsification, the sub-layer, `[UNBOUND]`, Tide, the Architect, and the Quieting remain undisclosed.
- **Referents and joins:** I found no dangling pronoun or broken reference. The two letters remain distinguishable; the right/left pocket distinction is explicit; speaker attribution remains clear in the crowded table and hearing scenes.
- **Quotes and italics:** straight quotes and asterisk italics are balanced on every line in all seven chapters. Counts by chapter are: ch14 28/52, ch15 124/24, ch16 104/46, ch17 128/50, ch18 130/50, ch19 192/38, ch20 162/50 (quotes/asterisk marks). No odd-count line remains.
- **The prior 45 resolved source-distance keys:** none reappears as a separate tracked passage. The closest overlap is the refusal material now counted under still-open `14:169`; it does not create a second independent passage under former key `14:173`.

#### One new canon regression

Ch19's new top-stair scene says Lira wrote Hesk from Greyvane and received “two lines” telling her to keep Cael out of draughts. Book 4 ch37 gives the actual exchange on the page: Lira wrote once from Greyvane to ask Cael's birthday, and Hesk answered in **three lines**—the date, *thank you*, and *he won't have told you*. The exact fix is below. The rest of the top-stair scene is sound.

### Ledger and Books 4–5 check

- **Daeva's letter:** current ch18 correctly puts it inside the **back board of Hesk's current book**, opposite the cost column. This is canon-safe: Book 5 ch60 closes the old volume on the last ferry and states that all later writing goes into Hesk's book; the old volume already holds the older letters behind its front board. However, B6 `STATE_LEDGER.md` is stale at the Movement 3 resources entry: it still says Daeva's letter is behind the old volume's front board. That line must be synchronized after the manuscript repair.
- **Vastin's rewritten refusal:** current ch14 clearly makes it a **guild hall's request for further time**, not a station request. That is compatible with his established institutional work. The Movement 3 coordinator summary only says he rewrites “a refusal of his own”; the new-canon section should specify the guild hall when synchronized.
- **Lira's meet:** day 45 + eighteen days = day 63; day 54 + nine days = day 63. Ch16 says eighteen days on day 45, and the B6 ledger's calendar/open-thread entries place the meet around day 63 and nine days after the ruling. The arithmetic is consistent.
- **Bracken's pouch:** Cael's ch19 reply is consistent with Book 5's two-way records-office pouch: locked in Ostrand, unlocked by Seln, with sealed letters. No continuity break.
- **Bracken's daybook:** current ch18 adds *Counter unattended, a quarter of an hour, by the registrar, on the registrar's own account.* The B6 ledger currently lists only post counts and faculty releases under the daybook; it should acquire this entry.
- **Ledger header/length:** the Movement 3 ledger still labels the state “repair r1 applied; recheck pending” and carries 31,667 words. R2 is 29,681 shell-count words (the author reports 29,611 by the formula tokenizer). Those administrative fields are stale.
- **Book 4 contradiction:** the Lira/Hesk reply described above is the only Books 4–5 manuscript contradiction I found in the r2 changes.

### Rerun checks

Commands were run exactly from the requested directories.

`cd editions/monroe-1.3 && bash tools/ed.sh gates book-06-the-compacts-hand 3`

- ch14–20: `reader_standard=0 metadata=0 modern=0` in every chapter.
- Reported word counts: 3,746 / 3,314 / 3,780 / 4,805 / 4,319 / 4,411 / 5,306.

`cd editions/monroe-1.3 && bash tools/ed.sh overlap book-06-the-compacts-hand 3`

- **0 unprotected shared runs of 8 or more words**.
- **13 protected runs**, all allowed.

`bash editions/monroe-1.3/tools/sweep_probe.sh book-06-the-compacts-hand 3 3`

| Chapter | Sentences | Skeleton | Close |
|---|---:|---:|---:|
| 14 | 165 | 1% | 13% |
| 15 | 126 | 2% | 9% |
| 16 | 173 | 0% | 16% |
| 17 | 206 | 0% | 16% |
| 18 | 187 | 3% | 12% |
| 19 | 187 | 3% | 19% |
| 20 | 238 | 2% | 9% |
| **Movement** | **1,282** | **1%** | **13%** |

The close band improves from r1's 16% to 13%. As in r1, the manual semantic-order audit controls the remaining decision.

## Exact line fixes

The following old string was verified with fixed-string grep to occur **exactly once** across ch14–20.

1. `manuscript/chapter-19.md`
   old: `"I wrote to him once, you know. From Greyvane. He wrote back two lines and told me to keep you out of draughts."`
   new: `"I wrote to him once, you know. From Greyvane. I asked when you were born. He sent back the date, and *thank you*, and *he won't have told you*."`

No exact one-line substitutions are proposed for the 10 source-distance findings. They require local recomposition of their observation order or carrier; synonym edits would repeat the r1 problem.
