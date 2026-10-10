# CLOSE WITH LINE FIXES — 8 RESOLVED / 2 STILL TRACKING

**Counts:** r3 resolves **8 of the 10** units left open by r2 and leaves **2 STILL TRACKING**: `14:139` and `20:193`. The complete 136-passage audit therefore stands at **134 RESOLVED / 2 STILL TRACKING**. Both remaining chains can be broken with the exact one-line substitutions below; no scene repair is required.

This is an independent targeted recheck of the current r3 text against source chapters 5–8, using the r2 rule that a source sentence's internal progression may not survive under changed wording.

## Findings

### Source-distance decisions

| Key | Source chain | Current r3 chain | Verdict |
|---|---|---|---|
| `14:19` | three years of requests → this paper asks nothing → his words marked adopted | authorities table marks his advisory adopted → yesterday's minute → his after-the-fact question about accompanying material → “Only the slip”; the request-history link is gone and the surviving links are reversed | **RESOLVED** |
| `14:139` | junior leaves reassured → Vastin keeps the copy and cannot explain why | the junior's pinned “I shan't worry” note → the same copy repeatedly held/moved → Vastin cannot settle to the tray and goes to the frame shop | **STILL TRACKING** |
| `14:169` | receives a familiar refusal → recognizes his own technique from the receiving side → remembers an earlier field assessor | Vastin's expanded guild-hall refusal is already in `done` → he finds his own struck short form beneath it → remembers teaching that line to juniors; receiving-side recognition and the old assessor are gone | **RESOLVED** |
| `17:230` | honest reports → hostile use as exhibits → consuming-machine metaphor | three honest lines from Gault, Umber, and Withrow → an imagined later reader → Cael wants to be worth that reader's trouble; hostile use and machine metaphor are gone | **RESOLVED** |
| `18:55` | old provision and use history → no Gold filing → explanation → incremented total | the protected “Never. Not at Gold.” occurs earlier in Bracken's scene → Karis silently rings `45` in the digest → Lira asks → “Her”; the history, explanation, and source order are gone | **RESOLVED** |
| `19:191` | east past the last station → eighteen months → records stop | the daughter keeps coming after records have stopped → one eastbound ferry toll is found → Withrow gives her the last recorded line; the duration and records-as-eyes explanation are gone | **RESOLVED** |
| `19:213` | paper wins → Denvash loss → line between system and people disappears | Cael rereads the first pole with pen in hand → writes nothing beneath it → writes separately about the clock being neither person nor text; the win/loss tally and Denvash sequence are gone | **RESOLVED** |
| `20:193` | Greyvane → four earlier challenges → each lost on the text | in the coach, Karis answers: “Greyvane's, and four older ones, all on the text.” The hearing carrier moved off-page, but the full internal chain remains in the source order in one sentence | **STILL TRACKING** |
| `20:195` | instrument-audit preamble → ninety-one-use breakdown → none about what a person is | use count first: seven conduct / eighty-four things / never what a person was → preamble afterward; the order is inverted and the category carrier is recomposed | **RESOLVED** |
| `20:293` | four couriers → rapid dissemination → win/fraud split | Brom recalls only a bruise, a departing satchel buckle, and an unseen boy; there is no courier count, dissemination claim, town claim, or split public reading | **RESOLVED** |

`14:139` remains because the reassuring note still supplies the first source link and the held, repeatedly moved copy supplies the second. The intervening mentor memory and frame-shop scene deepen the beat but do not break that local progression. The proposed line fix removes only the reassurance link; it preserves the packet-required troubling file, *Continue observation*, the copy staying with Vastin, and the unnamed unease.

`20:193` remains because a delayed coach answer changes location and speaker timing, not the source unit's internal sequence. The proposed line fix leads with the result of five challenges and gives Greyvane afterward, while retaining every required fact.

### Changed-unit seams and forward continuity

- No changed unit has a dangling pronoun, missing antecedent, broken speaker attribution, or abrupt logical join.
- The old assessor from source `14:169` is no longer used anywhere downstream. The current guild-hall refusal and Vastin's question about the five chairs remain self-contained.
- The eighteen-month duration removed from `19:191` is not required later. Chapter 21 establishes the Line independently through Lira's three carters, the last station, and the place where stamps and books stop.
- Chapter 20 and later chapters do not rely on the removed four couriers or “four towns by tonight.” Chapter 21's “Sixty days since the courier” refers to the escorted service courier introduced in chapter 5, not to the deleted post-ruling couriers. The four-town market fact remains independently established in chapter 15.
- Straight quotation marks and asterisk italics are balanced on every line of chapters 14–20.

### Protected continuity and wording

- **Velmere letter:** chapter 16 places the unopened, whole-sealed letter in Brom's left inside pocket; chapter 18 returns his hand to the left side; chapter 19 keeps the dark-red seal whole and the envelope unopened; chapter 20 explicitly reserves the left pocket for Velmere and puts Karis's slip in the right. Chapters 21–22 continue the same sealed-letter state.
- **Seln boundary:** Seln is not told about Shadow, its seal, or the reason it was sealed. No such disclosure appears in chapters 14–20.
- **Hearing orientation:** both required explanations remain intact in chapter 20: the post-Jent “may the registry stand him in a frame?” beat and the post-ruling “What they had won … What they had not won” beat.
- **Town count:** chapter 15 still says the weeklies sell in three towns besides Ostrand and states “Four towns.” Removing the later “four towns by tonight” did not alter this count.
- **Hesk's three-line answer:** chapter 19 now matches Book 4 chapter 37's three pieces: the date, *thank you*, and *he won't have told you*. The incorrect “two lines” wording is gone.
- **Protected wording:** the denial and folder tab; Seln's benched-instrument line; Daeva's statement and private letter; Hesk's Denvash paragraph; “Nine weeks. They are in the sixth.”; the day-after line; the hand-on-the-clock line; the final paper/proceeding exchange; the counting-doors entry; Seln's final line; and the other r2-held packet phrases remain verbatim. The overlap gate independently reports **13 protected runs** and **0 unprotected runs**.

## Rerun checks

Run from `editions/monroe-1.3`:

`bash tools/ed.sh gates book-06-the-compacts-hand 3`

- Chapters 14–20 all report `reader_standard=0 metadata=0 modern=0`.
- Word counts: 3,518 / 3,314 / 3,780 / 4,813 / 4,271 / 4,399 / 5,386.

`bash tools/ed.sh overlap book-06-the-compacts-hand 3`

- **0 unprotected shared runs of 8 or more words**.
- **13 protected runs**, allowed.

Run from the repository root:

`bash editions/monroe-1.3/tools/sweep_probe.sh book-06-the-compacts-hand 3 3`

| Chapter | Sentences | Skeleton | Close |
|---|---:|---:|---:|
| 14 | 152 | 1% | 14% |
| 15 | 126 | 2% | 9% |
| 16 | 173 | 0% | 16% |
| 17 | 207 | 0% | 16% |
| 18 | 184 | 3% | 11% |
| 19 | 189 | 3% | 19% |
| 20 | 239 | 2% | 10% |
| **Movement** | **1,270** | **1%** | **13%** |

The mechanical checks pass. The two manual semantic-order findings above control the verdict.

## Exact line fixes

Each old string was verified by fixed-string grep to occur **exactly once** in the current manuscript.

1. `manuscript/chapter-14.md`
   old: `*Thank you, sir. I shan't worry about it now.* The note was in a young man's hand, a hand still deciding what shape it meant to be. It was pinned to the copy of a station's Kindling entry, four years old, for a girl in the northern district: her Path, her first rank, in a station clerk's ordinary writing.`
   new: `*Second frame reading: within tolerance.* The note was in a young man's hand, a hand still deciding what shape it meant to be. It was pinned to the copy of a station's Kindling entry, four years old, for a girl in the northern district: her Path, her first rank, in a station clerk's ordinary writing.`

2. `manuscript/chapter-20.md`
   old: `Cael asked Karis which rulings had been on the shelf. She told him: Greyvane's, and four older ones, all on the text.`
   new: `Cael asked Karis what the shelf had established. "The clause survived five challenges," she said. "Greyvane was the newest."`
