# Book 6 — *The Compact's Hand*: line and listening proof (Step 4)

Reader: Codex, independent review seat, fresh context, 2026-10-11. Scope: `manuscript/chapter-01.md` through
`chapter-60.md` (294,099 words by `wc`), read in order as the narrator will meet them: one segment per paragraph,
`---` as a long pause, italics flattened and fenced notices flattened line by line. Read first: Book 4's and Book 5's
proofs; Book 6's completion plan, whole-arc read, lane rulings, pass brief and both applied lane reports; the edition's
audio and Reader Standard; OWNER-DECISIONS through #50; BOOK_MAP §8; `protected-patterns.txt`; and `audio/fpaudio.py`.
The shared pronunciation entries below were checked against the Book 1, 3, 4 and 5 proofs. Running chapter notes and
the closing mechanical audit are in `listening-notes.md`.

**No manuscript file was modified; no git command was run.** Every change below is a proposal. The required fix's old
string was verified to occur exactly once in the manuscript, its new string nowhere, and the old string in neither
BOOK_MAP §8 nor `protected-patterns.txt`. No proposed change touches a protected line or a FRAGMENT ACQUIRED notice.
Cael = KAYL and Lira = LEER-a (owner-confirmed, #33). Bede, Maud, Gwen and Abbot do not occur and remain owner-pending
placeholders, not findings (#3, #11). No named season, month order or English weekday occurs; the Halcenvane weekdays
are First-day through Seventh-day. Measures remain feet and yards, with inches, paces, strides, hands and miles where
appropriate. Ratings, formats and the calendar conform to #38, #39 and #41.

---

## 1. Verdict

**Render-ready after one required narrator-format fix.** The only manuscript change needed is the all-caps program card
in ch12: `LIRA / FORCE THIRD-YEAR` must become `LIRA AGAINST FORCE THIRD-YEAR`. The slash is the only slash in all sixty
chapters, and `fpaudio.py` does not convert it to spoken language. A narrator or synthesis layer may therefore say
“slash.” The replacement states the bout relation already established by the scene and changes no story fact.

No other defect was found: no unbalanced or mismatched quotation, no speech whose owner a listener cannot place, no
broken post-lane join, lower-case start, mid-clause end, doubled word, dangling comparison, inconsistent number echo,
or protected-text fault. The requested second-ear points all pass:

- ch13:217–219: Seln completes “they write it down”; `At the residence door` makes the location/time cut explicit.
- ch18:97: the grey-seal observation follows directly from the already established post piles; the later pause over the
  Auremont letter remains and the scene needs no replacement silence.
- ch49: the protected certification minute remains exactly the form's own wording. The next narration distinguishes the
  Archmarshal's refusal from Gault's evaluator-of-record title, as OWNER-DECISIONS #47 requires.
- ch60: Seln stays awake through the rota argument and only later lies beneath the pine; his surveyor's case goes with
  the boxes under the canvas; his contribution to the pooled purse precedes Brom's purchase question.

The remaining risks belong in the direction files: homographs; sentence-case handling of capitals; neutral, exact
notice/document delivery; silent markdown and brackets; spoken forms for visual numerals and initials; and clean
sentence-boundary splits for the 106 paragraphs over 700 characters.

---

## 2. Findings by category

### 2.1 Quotation marks and attribution

- Every paragraph has balanced straight quotation marks except eight valid paragraphs in three intentional
  multi-paragraph quotations. Ch35:259, 261 and 263 are the first three paragraphs of one letter and close at 265.
  Ch51:177 is the first paragraph of a ruling and closes in the continued quoted paragraph at 179. Ch52:215, 217, 219
  and 221 are successive heads of Karis's forfeiture bibliography and resolve in the continued reading. There are no
  curly quotes and no odd-asterisk paragraphs.
- The councils with Cael, Lira, Brom, Karis, Ephram, Daeva and Seln remain attributable by tags, action beats, role or
  short alternation. Bracken's registrar voice, Withrow's counsel voice, Gault's evaluator voice, Rooke's coaching voice
  and Vastin's institutional voice stay separate from the council members.
- The challenge, panel and ruling scenes keep read instrument text distinct from the speaker reading it. The same holds
  for letters, forms, minutes, charter language, notices, notebook lines and remembered speech embedded in dialogue.
- The Kindling chapters preserve the separation among the Arbiter's voice, the plate's reported wording, the people in
  the room and Cael's read of the event. The road chapters past the Line, ch55–60, retain identifiable speakers even in
  short fire-side exchanges and untagged two-line alternations.
- Intentional written fragments remain intentional: ch14's struck-through draft ends at `not contemplated by`; ch47's
  begun Log entry `In the records hall` is struck and replaced in the next paragraph. Neither is a broken join.
- `Mm.` is usually Seln and sometimes an imitation of him; it is load-bearing acknowledgment and should survive the
  render. Interrupted lines ending in an em dash need a held, non-final cadence, but none has lost the answering voice.

### 2.2 Ear collisions and homographs

No collision requires a rename or line fix. The names that actually meet in scenes stay distinct by onset, vowel,
syllable count and role:

| Pair or cluster | Direction |
|---|---|
| Gault / Gold | GAWLT, with a long aw and audible final *t*, versus GOHLD. |
| Bracken / Brom | BRACK-en versus BROM; keep the registrar dry and Brom warmer. |
| Seln / Zerin | SELN, one syllable, versus ZERR-in. No Selm- name occurs. |
| Hesk / Hesk-ward | HESK in both; `Caelen Hesk-ward` is KAY-len HESK-ward, two words. |
| Vell / Velmere | VELL versus VEL-meer; no troublesome same-scene exchange. |
| Karis / Cael / Daeva | KAIR-iss, KAYL and DAY-va; keep Cael clipped to one syllable. Kestrel does not occur. |
| Havel / Halcenvane | HAV-el versus HAL-sen-vayn. Halvern does not occur. |
| Ephram / Ember | EF-ram versus EM-ber; Ephram is a person, Ember a Path. |
| Reydan / Rhagen / Rooke | RAY-dan, RAH-gen with hard *g*, and ROOK. |
| Auremont / Ardenmere | AW-re-mont versus AR-den-meer. |
| Ilsev / Lira | IL-sev versus LEER-a. |

Marek, Ivenne, Quenna and Fiske are not in Book 6. Gwen and the other owner-pending placeholder names are absent.
Ostrand, Withrow, Vastin, Umber, Daeva, Zerin, Jent, Norhold and the other named people and places remain clear in their
actual scenes.

All homographs were read in context. None needs a text change, but the narrator directions should pin these readings:

| Word | Intended reading |
|---|---|
| `lead` | LEED for lead hand, lead foot, lead rider and leader; LED for pencil lead (ch30), a lead seal (ch58), and lead bags/material (ch59). |
| `wound` | WOWND throughout: a clock wound, tape or scarf wound around something. There is no WOOND injury use. |
| `close` | KLOHS as adjective/noun and KLOHZ as verb, by syntax. |
| `read` | REED for Cael's perceptive faculty, including `the read`; RED for past-tense reading. |
| `tear` | TAIR in ch52. |
| `live` | LIV throughout; no LYV adjective/adverb use. |
| `wind` | WIND for the Path and weather; WYND when linen or a clock is wound/winds. |
| `bow` | BOH for a drawn bow and a key's bow; BAU for a courtesy. |
| `present` | PREZ-ent throughout. |
| `minute` | MIN-it, including the certification minute. |

Every bare `as` was read in place. The clauses express manner, comparison, habit or genuine simultaneity without an
audible logical ambiguity; none needs to become `while`.

### 2.3 Formatting the narrator meets

- **FRAGMENT ACQUIRED notices:** three complete fenced blocks: Anchor (ch32), Shadow (ch37) and Blade (ch54). Each
  protected line is intact. `fpaudio.py` removes the fences and presents the notice line by line, adding sentence stops.
  Read each in a neutral system cadence; do not voice the fence or brackets.
- **First stability warning:** ch1:89, remembered in italic prose: `Stability: provisional — architecture under load.`
  It precedes the fenced notices and must land as remembered system text. Ch37 is the Shadow notice, not the first
  occurrence of the warning.
- **Registry forms, gallery sheets and broadsides:** their prose and figures are always introduced as writing, a board,
  a card, a filing, a copied sheet or a public notice. Give them a modest document register, sentence-case all-caps
  wording, and return cleanly to scene prose.
- **Log and notebook entries:** italics flatten without emphasis markers. Cael's Log, Hesk's book, Karis's grey notebook
  and ruled columns, Seln's reports, the minute, the charter and the notices need a slight register shift rather than
  character dialogue. Sign-offs and single initials are letter-names; brackets and asterisks are silent.
- **Numerals and tallies:** the remaining digits are visual document or notebook marks: petition paragraphs 34 and 7;
  `Priority Level 4`; ch16's meaningful column `0`; day counts 44, 54 and 45; the five road figures; ratings 28, 27 and
  26; measurements 10 and 36; and `Day 88`. Say digits as ordinary numbers in context. `SW` in the ch24 visual note is
  “southwest.” There is no unexplained T-number.
- **Markdown:** no underscore emphasis, strikethrough, curly quote or stray backtick. Backticks occur only as the three
  complete fences. One trailing space at ch17:185 and extra blank lines in ch14 and ch33 are narrator-silent.
- **Scene breaks:** all 254 `---` breaks have a blank line before and after and should become long pauses.
- **Slash:** the manuscript contains exactly one, the ch12 program card. It is the required fix in §3.

### 2.4 Typos, joins and continuity after the lanes

No typo or broken join remains after the two applied texture lanes. The full read found no lower-case paragraph start,
doubled article or preposition, mid-clause paragraph end, dangling simile/comparison or numerical echo that changed in
only one location. The repeated-word sweep found only grammatical `had had` constructions.

The highest-risk apparent fragments are deliberate documents (ch14 and ch47, above). The ch35 letter, ch51 ruling and
ch52 bibliography are correct multi-paragraph quotations, not lost closing marks. Ch16's italic `0` is a meaningful
visual count beside the other columns, not a letter-O typo. Ch9's `casing` is the answer's stated misspelling and is
immediately identified as such. Ch58's future administrative close deliberately precedes the return to First-day; the
transition says so.

The calendar and measure audit also passes. Generic uses such as `season's open`, `season's worth` and `in the spring`
do not name a season. No month-order statement or English weekday occurs. Distances and dimensions use the edition's
feet-and-yards system.

### 2.5 Paragraphs over 700 characters (list only)

These are flattened paragraph lengths before `fpaudio.py` applies its sentence-boundary split:

| Chapter:line | Characters | Opens |
|---|---:|---|
| 01:7 | 760 | He had Hesk's book open… |
| 01:59 | 705 | The read came next… |
| 01:89 | 725 | It had come to him… |
| 01:119 | 1,205 | The record was a public thing… |
| 01:209 | 743 | “We went to Norhold,”… |
| 02:13 | 747 | The stranger was a Stone… |
| 03:41 | 716 | “They'll put three assessors… |
| 03:85 | 775 | Gault sat… |
| 04:219 | 1,030 | He had it by heart… |
| 05:111 | 735 | She was quiet… |
| 05:137 | 743 | An escort… |
| 07:13 | 935 | “I filed one once… |
| 07:73 | 1,123 | “The morning after… |
| 07:77 | 801 | “It's expulsion… |
| 08:105 | 739 | The first was Karis's… |
| 08:147 | 851 | He remembered… |
| 08:215 | 739 | It was a short bout… |
| 09:23 | 716 | “Ninety-one.”… |
| 09:145 | 728 | It was the leaf… |
| 09:241 | 741 | “Here's the other half… |
| 11:19 | 945 | He turned back a leaf… |
| 11:39 | 895 | “Is good law.”… |
| 11:93 | 877 | She was an Iron… |
| 11:129 | 729 | Cael knew the Force… |
| 12:5 | 712 | Nobody had announced… |
| 13:93 | 726 | Cael counted… |
| 13:161 | 772 | The seat opened… |
| 13:171 | 729 | They were not with him… |
| 14:73 | 797 | The junior… |
| 14:142 | 735 | The rest… |
| 14:144 | 908 | He had gone home… |
| 15:5 | 713 | He took the rail… |
| 15:45 | 915 | “I went into the shop… |
| 15:63 | 830 | “The weeklies… |
| 16:41 | 782 | There was a hat… |
| 16:133 | 882 | The girl shut… |
| 17:229 | 853 | It was the house's exhibits… |
| 18:37 | 791 | Because he should not… |
| 18:197 | 734 | On the First-day… |
| 19:175 | 822 | “He tipped it… |
| 20:19 | 754 | He let the read… |
| 20:107 | 723 | She was on… |
| 20:127 | 748 | Everything else… |
| 20:143 | 912 | What Jent… |
| 20:171 | 967 | It was the names… |
| 21:95 | 750 | Up there… |
| 22:113 | 780 | Forty days… |
| 25:165 | 743 | Cael wrote up… |
| 27:109 | 748 | “Before anybody… |
| 28:213 | 1,052 | Karis gave him… |
| 29:57 | 742 | That had been… |
| 30:27 | 758 | The first was… |
| 30:99 | 717 | Brom had… |
| 30:169 | 724 | It was a deep… |
| 31:225 | 710 | Every course… |
| 32:172 | 1,059 | “Think how it reads… |
| 32:258 | 809 | He had believed… |
| 32:286 | 764 | Lira's ankle… |
| 34:101 | 722 | Cael watched… |
| 35:95 | 741 | Karis came… |
| 35:227 | 711 | He had been kept… |
| 36:15 | 864 | There were twenty-three… |
| 36:37 | 990 | So she started… |
| 36:155 | 727 | “My fourth posting… |
| 36:159 | 821 | “Over five weeks… |
| 36:165 | 776 | “A corridor… |
| 36:195 | 1,016 | “She kept the books… |
| 37:15 | 935 | He told the circle… |
| 37:133 | 750 | Cael went on… |
| 37:152 | 819 | He told the rest… |
| 37:178 | 709 | Cael did not… |
| 38:59 | 720 | “I'm not asking… |
| 38:201 | 703 | “One.” Karis… |
| 38:237 | 713 | The hall came… |
| 39:5 | 755 | Nobody saw… |
| 39:7 | 852 | Cael went up… |
| 39:33 | 836 | “I sorted them… |
| 39:63 | 913 | “Eleven seconds… |
| 39:109 | 851 | “Middle.”… |
| 39:125 | 899 | “That was the old way… |
| 39:185 | 883 | “Now I've got it… |
| 40:25 | 712 | “He verifies it… |
| 40:103 | 737 | Lira went… |
| 40:113 | 801 | What the room… |
| 40:201 | 848 | “The first is verification… |
| 41:231 | 706 | “The same quiet… |
| 43:13 | 789 | She was a third-year… |
| 44:35 | 791 | Nothing in it… |
| 44:223 | 947 | “Eleven of them… |
| 47:69 | 804 | “The house moves… |
| 48:9 | 932 | He took the benches… |
| 48:45 | 872 | “The enrollment was… |
| 48:173 | 707 | It was a strange… |
| 49:55 | 828 | “I should like… |
| 49:83 | 832 | “Instruments,”… |
| 49:127 | 720 | “Now I come back… |
| 51:177 | 868 | “The seat… |
| 51:255 | 720 | “It is exactly… |
| 52:65 | 853 | “I'm arguing… |
| 52:191 | 973 | “I've got it written… |
| 52:301 | 815 | “I told you… |
| 53:31 | 860 | “The ruling says… |
| 53:83 | 707 | “There is no form… |
| 54:262 | 766 | Nine. Taken… |
| 55:95 | 751 | “There is a margin… |
| 60:13 | 752 | So they did it… |

### 2.6 Protected lines

All 51 `protected-patterns.txt` expressions are present. Forty-six occur once; five occur twice by deliberate callback
or quotation: `distinction feels important`, the Compact advisory, the challenge address, Karis's question, and `move
him back inside the instrument`. All three FRAGMENT ACQUIRED blocks are intact. BOOK_MAP §8's protected lines were read
in place, including the closing inventory and exchange. The ch49 certification minute remains untouched under #47. The
required ch12 fix is outside all protected material.

---

## 3. Exact line fixes

### 3A — Required before render (1)

The slash is a visual bout separator, not intended speech. The old string occurs exactly once in the manuscript and the
new string occurs nowhere.

1. `manuscript/chapter-12.md`
   old: `PROGRAM TRIAL. SECOND-DAY, SECOND BELL. LIRA / FORCE THIRD-YEAR. RATED.`
   new: `PROGRAM TRIAL. SECOND-DAY, SECOND BELL. LIRA AGAINST FORCE THIRD-YEAR. RATED.`

### 3B — Optional, engine-safety only (0)

None. The homographs in §2.2 are better handled in direction: their senses are clear, and no wording change improves the
text enough to justify touching it.

---

## 4. Pronunciation lexicon

Stress is shown in capitals. “Owner-confirmed” refers to OWNER-DECISIONS #33. “Carried” means the same pronunciation is
present in the Book 1, 3, 4 or 5 proof. Book 6 additions are proposed for the direction files.

### People

| Name | Say | Identification | Status |
|---|---|---|---|
| Cael | KAYL, one syllable | the enrollee; the fifth man of the bluff | owner-confirmed #33 |
| Caelen Hesk-ward | KAY-len HESK-ward | Cael's full name; two words | carried B1/B3/B4/B5 |
| Hesk | HESK | his grandfather; Hesk's book and clock | carried |
| Lira | LEER-a | Wind; the program's rated fighter | owner-confirmed #33 |
| Brom | BROM, as in “from” | Iron Skin; the wall | carried B4/B5 |
| Karis Dellenmoor | KAIR-iss DEL-en-moor | Ember; counsel and analyst | carried B3/B4/B5 |
| Ephram | EF-ram | Blade; “Assay” is his name for Cael | carried proposal B4/B5 |
| Rooke | ROOK, as in “book” | coach and instructor | carried proposal B4/B5 |
| Gault | GAWLT, as in “fault” | Magister; evaluator of record | carried proposal B4/B5 |
| Bracken | BRACK-en | registrar | carried proposal B4/B5 |
| Withrow | WITH-roh | chancellor and counsel | carried proposal B4/B5 |
| Seln | SELN, one syllable | teaching assistant; records and scheduling | carried proposal B4/B5 |
| Vastin | VAS-tin, as in “fasten” | Archmarshal | carried proposal B4/B5 |
| Ilsev | IL-sev | Compact evaluation seat | carried B1/B3/B4/B5 |
| Havel | HAV-el, short *a* | records officer | carried B3/B4/B5 |
| Prynn | PRIN | Prynn's index | carried B3/B4/B5 |
| Vell | VELL | Ardenmere ledger-keeper | carried |
| Reydan | RAY-dan | Reydan's give | carried B3/B4/B5 |
| Feryn | FERR-in | named in records/history | carried B1/B3 |
| Coss | KOSS | named in records/history | carried B1/B3 |
| Pellin | PEL-in | named in records/history | carried B1 |
| Daeva | DAY-va | Auremont's Gold | carried proposal B5 |
| Zerin | ZERR-in | Auremont's Wind | carried proposal B5 |
| Umber | UM-ber | Chief Adjudicator | carried proposal B5 |
| Jent | JENT | counsel's junior/reader | proposed B6 |

Marek, Ivenne, Quenna and Fiske have carried lexicon entries but do not occur in Book 6. Bede, Maud, Gwen and Abbot are
owner-pending placeholders and do not occur; no Book 6 direction entry should be invented for them.

### Places

| Name | Say |
|---|---|
| Halcenvane | HAL-sen-vayn, three syllables; carried B4/B5 |
| Ostrand; the Ost | OST-rand; OST; carried B4/B5 |
| Greyvane | GRAY-vayn; carried B3/B4/B5 |
| Denvash | DEN-vash; carried |
| Ardenmere | AR-den-meer; carried |
| Fenmark | FEN-mark; carried B3/B4/B5 |
| Velmere | VEL-meer; carried B3/B4/B5 |
| Ternhall | TERN-hall; carried B3/B5 |
| Dellenmoor | DEL-en-moor; carried B3/B5 |
| Norhold | NOR-hohld; carried proposal B5 |
| Auremont | AW-re-mont, stress first; carried proposal B5 |
| Rhagen Institute | RAH-gen, hard *g*, stress first; carried proposal B5 |
| the Concourse | KON-kors; carried proposal B5 |

The Crown yard, sprung oak, covered walk, records hall, assessment wing, guesting-house, Line, waystations, district
stations and the other descriptive sites are pronounced as written.

### Terms, documents and visual forms

| Term | Say / handle |
|---|---|
| Kindling; Kindled | KIND-ling; KIND-eld |
| Arbiter | AR-bit-er |
| the Compact | KOM-pakt |
| sigil | SIJ-il |
| Path names | Wind, Pressure, Iron Skin, Blade, Force, Stone, Shield, Mire, Current, Ash, Glass, Ember, Shadow, Tide, Lattice, Rune and Storm as ordinary words; Wind is the noun WIND. |
| `-adjacent` | ad-JAY-sent, with a light hyphen pause |
| Tiers and ranks | Copper, Iron, Bronze, Silver and Gold as written; digits in rank/rating forms as numbers, not individual characters. |
| the read | REED; Cael's perceptive faculty |
| Reydan's give | GIV |
| the Log; Hesk's book | document titles where context marks them; slight register change, no italic emphasis |
| FRAGMENT ACQUIRED notices | neutral system voice; one beat per flattened line; fences and brackets silent |
| First-day … Seventh-day | ordinal number plus “day”; never substitute English weekday names |
| `Priority Level 4`; `Day 88`; ratings and figures | “Priority Level four”; “Day eighty-eight”; ordinary spoken numbers |
| `SW` | “southwest” |
| `0` in ch16 | “zero” |
| initials K., C., L., D. and H. | say the letter; do not say “period” |
| `Mm.` | voiced acknowledgment; preserve it, especially for Seln |
| brackets | silent; speak the enclosed designation only |
| all-caps cards, sheets and broadsides | read in sentence case, never spell ordinary words letter by letter |

---

## 5. Direction notes for segmentation and render (not text changes)

1. Keep Cael = KAYL and Lira = LEER-a in every chapter direction (#33).
2. Read the three fenced notices in a neutral system cadence, one flattened line at a time. Do not voice markdown,
   brackets or `---`; the scene break is a long pause.
3. Mark ch1:89 as the first stability warning even though it is remembered italic text, not a fenced notice.
4. Give the Log, notebooks, columns, minute, charter, forms, sheets and broadsides a light document register. All-caps
   text is sentence case; single initials are letter-names.
5. Ch12's card must use the §3 fix so the engine says “against,” never “slash.”
6. Homographs follow §2.2, especially LEED/LED, WIND/WYND, REED/RED and BOH/BAU.
7. Keep the councils' voices distinct without adding theatrical characterisation: Gault's long aw beside Gold;
   Bracken dry beside Brom; Seln's compact counter voice; Vastin even; Daeva level; Ephram exact; Rooke flat.
8. Preserve a held cadence through intentional em-dash interruptions and across the three multi-paragraph quotations.
9. Split the §2.5 paragraphs only at sentence boundaries, as `fpaudio.py` does. Do not let an inserted split masquerade
   as a scene break or speaker change.
