# Book 2 — listening proof, running notes (Claude Fable, review seat, 2026-10-05)

Read order: prompt → Book 1 and Book 3 listening-proof.md (models) → COMPLETION-PLAN, whole-arc-read (§8 applied),
LANE-A-REPORT, LANE-B-REPORT → EDITION_BRIEF (audio, Reader Standard) → OWNER-DECISIONS #3, #33, #36 → BOOK_MAP §8, §9,
§10 → audio/fpaudio.py → mechanical sweep (script, scratchpad) → chapters 1–60 in order.

## Mechanical sweep (script over all 60 files, before the read)
- `"` count per paragraph: 0 odd. No curly quotes anywhere. No multi-paragraph open quotations at all.
- `*` count per paragraph: 0 odd. No `_`, no `**`, no backticks outside fences, no headings after line 1, no tabs.
- `---`: every one has a blank line before and after. 255 breaks (134 in ch1–30, 121 in ch31–60).
- Code fences: 4 (ch7, ch8 FRAGMENT UPDATE; ch28, ch58 FRAGMENT ACQUIRED). fpaudio flattens each line + "."
- Brackets: [unnamed] ×1 narration ch6; [Wind-adjacent] in the two UPDATE blocks; [SHATTERED] ch14 ×2, ch15, ch17,
  ch33 (all documents); [UNBOUND] ch36 (document); [unnamed] in the two ACQUIRED blocks. No other brackets.
- Spoken/narrated "Shattered": ch4, ch6 as *Shattered* plain. Good.
- Doubled words: 32 "had had", "kind to you you'll" (ch27), "told it it would" (ch53) — all grammatical. No true doubles.
- Lower-case paragraph start: ch35 "systemic protocol, origin: registry sub-layer." — the index line (protected §8.4).
- Paragraph ending without terminal punctuation: ch5 "*Cael,*" (letter salutation). Fine.
- Trailing space: ch50 line 179 (one). Harmless to fpaudio (split/join on whitespace).
- Numerals: ch2 "a *3*, in pencil"; ch6 "PATH DECLARATION — COPPER RANK 1", "Rank 1", "Rank 2"; ch30 "*money 9, gyms 3,
  rules 1*"; ch33/35 "Priority Level 4", "Section 12"; ch44 "Bronze Rank 1"; ch51 "*At rest: 12, 14, 16.*" etc. (Log).
- Abbreviations: "def." ch1, ch14 (Vell's ledger; Book 1 ch59 precedent, protected there); "Iron-equiv." ch11, ch14
  (ledger lines); "Fri." ch37 (Dace's chalk note); "t.f." ch2 (text decodes); "h" ch3/ch6 (text decodes); "L.", "C.",
  "H." initials; "W" ch1 (margin). No Cu/Br/R1/wk/exch/unr/Mon anywhere. No slashes between words.
- All-caps: Log headings ch6/ch9/ch17/ch20/ch29 (WIND-ADJACENT, PRESSURE-ADJACENT, WHAT IT IS, SOURCE, CONDITIONS,
  DEPLOYMENT RANGE, COSTS, OPEN QUESTIONS, REVISIONS, UPDATE), OFFICIALS ch3, MAIN FLOOR / BROM. IRON SKIN.
  IRON-EQUIVALENT. / CAEL. ASSESSED. ch22, EAT, L SAYS ch47, EAT. L. SAYS. ch55, DOES THE FORM ASK FOR HIS FAMILY ch56,
  EAT. BOTH. ALL THE WAY THERE. ch59. Renderer sentence-case, as Book 1.
- Spaced em dashes: 13, all inside ledger/chalk/letter lines (pauses).
- Name pairs per scene (script): Coss/Doss — Doss absent. Darrow/Marrow — Marrow absent. Keth/Kestrel — Kestrel absent.
  Brom/Bede in one scene: ch43 s1, ch45 s4, ch50 s5, ch53 s1 (check for a spoken list). Vell/Velmere ch32 s3, ch56 s3.
  Keth/Hesk ch22 s5, ch41 s4. Vell/Dace 65 scenes (the keepers; distinct by ear: VELL / DAYSS).
- Homographs (contexts pulled): wound = WOWND in all 13 "wound round / wound hands / spring is wound"; ch8 "no longer
  only a wound" = WOOND (the injury) — one exception to direct. lead = LEED (lead hand/foot/forearm/shoulder/knee/shin)
  except LED metal: ch22 "filled with lead", ch23 "filled with lead", ch24 "lead seam" ×2 (one sentence has both:
  "his lead foot came down across the long lead seam"), ch59 "lead seam". tears: ch31 TEERS; ch36 TAIRS ×2. bow: BOH
  (tape bows, "like a bow", "drawn bow", "bow window") except ch59 "a small bow of the head" ×2 = BAU. live: LYV
  "find it live", "seen it once, live", "a live thing"; LIV elsewhere. lives: LIVZ ch13/14/41("Who lives")/44; LYVZ
  ch3/41/54. minute: all time. Winds = the Path plural. winding = cloth, WYND-ing. present(s) = PREZ-ent.
- ", as" clauses: 350 listed and read. Habitual/manner nearly all; the temporal ones are literal (ch3 "as the months went
  on", ch5 "as it landed", ch11 "as she came in close", ch14 "as he was putting it away", ch33 ×2, ch43 "as the blow came",
  ch48 "as Brom threw", ch55, ch59 "as he passed"). None hearable as a false "while". No fixes.
- Paragraphs over 700 flattened chars: 165 (list in the proof).

## Chapter notes
- ch1: clean. Ledger line "def. Ulric" (abbrev). Margin "*W, once.*" = the letter. Attribution clear; Ulric/Vell/Lira/Dace
  distinct. "Win?" / "Win." fine.
- ch2: "a *3*" reads "a three". "*t.f.*" decoded in text ("Told, face"). New name Stedd (STED). "Hm." (Vell). Fine.
- ch3: OFFICIALS (caps, italic). "(a mangle, h)" decoded. "C. Hesk-ward … with L." letters. Ilsev named once. Fine.
- ch4: "Hm." (Vell). Orvet (OR-vet) first named. "two *p*s and one *e*" — letter names. *Shattered* plain in narration.
  Fine.
- ch5: Lira's counts; "*one-and-two-and*—"; letter "*Cael,*" / "*— H.*". "Hm," (heavyset man). Fine.
- ch6: the Log in italics with caps headings (WIND-ADJACENT, WHAT IT IS, SOURCE, CONDITIONS, DEPLOYMENT RANGE, COSTS, OPEN
  QUESTIONS) — render sentence case, each field its own beat. "*[unnamed]*" in narration: brackets silent ("a name that
  was not a name, unnamed"). "two of Lira's* ands*" italic boundary mid-phrase — fpaudio strips it; fine. "*fell over.
  (L., seen.)*" — the letter. Protected "You're doing the thing" present. Fine.
- ch7: FRAGMENT UPDATE code block (protected §8.12), fenced; fpaudio flattens to three lines + "." "Huh," (Lira). Fine.
- ch8: the UPDATE recopied (protected). "REVISIONS." "*t.f.*" again. Letter to Hesk. "no longer only a wound" = WOOND
  (the one injury-sense "wound" in the book). Protected "I'll show you when it's nearly enough" present. Fine.
- ch9: FIX — Cael reads Vell's margin notes aloud: "*opp. tried the spinning cut, second.*" and "*opp. pressed hard from the
  word.*" — "opp." has no in-text decoding; an engine says "opp". Each matches once. → "opponent". Rest clean; Vell's
  "Thirteen" count; the big man by the barrel (Brom unnamed). Attribution clear.
- ch10: Dravin (DRAV-in), Keth (KETH) introduced; "*No reason for this page.*" (protected §8.23) present. Hesk letter
  "*H.*". Lira's "I want to be the best Wind practitioner alive" etc. (§8.23) exact. Fine.
- ch11: ledger "*Lira, Copper formal, Wind. L. to Dravin (Iron-equiv., Wind). Sixth exchange. Pressed throughout.*" —
  FIX "Iron-equiv." → "Iron-equivalent"; "L." (= lost) is the letter, direct it. The salt-end woman, the betting man.
  Lira POV then Cael POV split at `---` (mark). Fine.
- ch12: the six hooks; "performed commitment"; "ten degrees"; Keth's ring; sacking girl. Fine.
- ch13: "You're writing the wrong things." (§8.20) exact; Dessa's count. Fine.
- ch14: ledger "*Lira, Copper formal, Wind. def. —* … *(Iron-equiv., Blade). Fifth exchange. Pressed throughout.
  Matched pace.*" — FIX "Iron-equiv." → "Iron-equivalent"; "def." = Book 1's ledger form (lexicon: "defeated").
  Havel section: "[SHATTERED] class" in the standing instruction and "*[SHATTERED].*" on the folder — documents,
  brackets silent. Havel = HAV-el (vs Cael KAYL — distinct onset/stress). POV change at the `---` (Havel). Fine.
- ch15: Havel's checklist (§8.21) all four pairs exact. "Dunno." (Red Cap). "*[SHATTERED]*" on the leaf. Fine.
- ch16: Brom POV at the open and from s3 (mark the `---`). Velmere = the family yard (place), VEL-meer, in the same
  chapter as Vell (different scenes). "purses honest, records loose" italic talk. Fine.
- ch17: §8.22 all nine lines exact. Ledger "*B. to the Shield (Iron-equivalent). Seventh exchange. Hand up.*" — full
  word here (so ch11/ch14 "Iron-equiv." are the odd ones out). Corrin (KORR-in; Corbin absent in Book 2). Coss POV at
  the `---`; "*Noted.*"; "H." initials. Daughter's map. Fine.
- ch18: Corrin's account; the reading room; "Stimulus / Latency / Response"; "*Heels. Six in ten, more. Can't move off
  it — tried.*" (spaced dash = pause). Keth's "Tell me what's in it. The middle. After." Fine.
- ch19: "*L.: leave it home.*" the letter; letter "*Dear Hesk,*"; Orvet's Blade bout; "clear stillness" (not "bright").
  Vell's "Go and eat something." Fine.
- ch20: "*Ceiling for B.: nought.*" ("nought", not "0"). "like a bow" / "the bow's moment" = BOH. The three-way bread
  argument carries by tags. "Find it live" = LYV. Fine.
- ch21: Wendel (WEN-del). The kitchen supper (sister / heavyset man / his wife / Lira / Cael) carries by tags; the
  sister's lines are all tagged. "Twenty years on this row" is the heavyset man's, not Dace's. §8.24 "She's going to hit
  Silver-tier before she's done." exact. Brom's reported "*Don't read me tonight…*" in italics. Fine.
- ch22: ledger "*L. over Wendel (Iron-equivalent, Wind, guild-trained)…*" — "L." = Lira here (ch11's "L. to Dravin" =
  lost); say the letter either way. The slate "*p*" ringed = the letter. The bill "*MAIN FLOOR*" / "*BROM. IRON SKIN.
  IRON-EQUIVALENT.*" / "*CAEL. ASSESSED.*" — sentence case at render. "filled with lead" = LED. "Four to one". Fine.
- ch23: "filled with lead" = LED; "Twenty-six" lamps; "Five," (heavyset man = the odds). The old man at the back; Keth's
  "Watch the middle." Fine.
- ch24: "his lead foot came down across the long lead seam in the floor" — LEED then LED in one sentence; a human
  narrator reads it, an engine may not → optional 3B "leaded seam". "the lead seam" (ch24 s6, ch59) = LED; lexicon.
  "lead forearm / lead foot / lead arm / lead shoulder" = LEED throughout. Fine otherwise.
- ch25: Brom POV (s1–s3), Cael from s4 — mark at the `---`. §8.11 floor exchange: all eleven lines and the three after
  "I'm Brom." exact; "Good. I like problems I can't solve." whole, tag after (Lane A's join). "*Atypical movement, third
  exchange.*" Vell = "the keeper" in Brom's POV. Fine.
- ch26: "Oh, his *legs*," (the sister). §8.25 "Show me the log sometime." / "Maybe." exact. Brom's story at the wall;
  "*Also: made a friend today.*"; the *Carrying* column ruled. Three terms. Fine.
- ch27: "*bell, bell, bell*". The lean in the first touch. Keth at dusk. Fine.
- ch28: §8.1 FRAGMENT ACQUIRED (Iron-adjacent) code block exact; §8.13 "You absorbed part of my Path." exact; §8.2 whole
  ("Good. That means you get to choose the word." in one line, the beat cut by Lane A). FIX (broken join + attribution):
  line 212 "He took the coat off the nail at last." then line 220 `"Not tomorrow," he said. … He reached for his coat on
  its nail.` — the coat comes off the nail twice, and the "he said" follows Brom's own line, so a listener hears a
  speaker change that is not one. Lane A cut the mouth-corner beat here (§8.2), which is where the seam came from.
  → `"Not tomorrow," said Brom. … He stood with the coat over his arm.` (he "put the coat on" two sentences later).
  Lira's "That was ours." / "He read it from the front." Fine.
- ch29: the IRON-ADJACENT Log entry (six fields); "*L., through the wall. Didn't.*"; "That's forty". Fine.
- ch30: "*money 9, gyms 3, rules 1*" — an engine says "money nine, gyms three, rules one"; natural; no fix (same as
  "Rank 1", "Level 4", "Section 12", ch51's Log counts). The rope "bowed" = BOHD. The junior keeper. Orvet's Shield;
  "bright stillness" once (the bout). Hesk's letter "H." Fine.
- ch31: the complaint; "Read it out" — Cael reads his page aloud (plain, in quotes); Vell's "*t.f.*" corrections; the
  Force man's shouted "*Two years.*" in italics = reported speech. Wendel / Vell in one exchange ("Is Wendel—" /
  "Wendel hangs off a different nail") — WEN-del vs VELL, fine. The young Wind "tears ran" = TEERS. Fine.
- ch32: the three-person supper — every line tagged or answered; "Yes," said Brom and Cael together. "Velmere talks
  like Velmere" in the same scene as Vell (s3): VELL / vel-MEER, two syllables for the place. §8.24 "You should be
  competing at Iron-equivalent." / "I like him." / "I thought you might." exact. "*B., across the table. Did. Didn't
  ask. Will.*" Fix 4's "*A year and more ago…*" sits clean. Lira teaches Brom's feet. Fine.
- ch33: Havel POV from s3 (mark). "Section Twelve" in narration, "Section 12" in the documents — both fine aloud. §8.4
  long form and §8.25 Coss's reply exact. "*Hesk-ward, C.*" Fine.
- ch34: Lira's confirming bout (Stone from up the river); the watcher ×3; Brom "red to the ears". Fine.
- ch35: Coss POV (s1–s3), the record window (s4; the index line "*systemic protocol, origin: registry sub-layer.*" with
  its lower-case start, protected), the read-back (s5). "*Coss.*" at the foot of the note. Fine.
- ch36: the pulse ("*there?*"); §8.3 the marginal note with [UNBOUND] (document; brackets silent) and Cael's copy
  without them, both exact; "tears at the corner" = TAIRS; "*Copper* spelt with two *p*s"; §8.26 "The Compact does
  falsify things." / "I know." exact; Keth's eleven pages. Fine.
- ch37: FIX — Dace's chalk note "*Coast courier — results — Fri.*" → "Friday" (abbreviation; an engine says "fry" or
  spells it). "the ink on the back of his hand said eight and twenty-two" (words). Dace's "Go and eat. You're grey."
  Keth's ring; "*I like him.*" in the grey book. Fine.
- ch38: the barge lad, Orvet's square woman, the dock partner; "Thursday week". The knock "*there?*". Fine.
- ch39: Keth bout exchanges 1–2; Vell's preamble; "the width of a straw"; the grey-coat woman (Quenna, unnamed). Fine.
- ch40: §8.14 all exact: "*Iron-equivalent. Cael. No Path designation.*" / "First time I've written that." / "Does it
  matter?" / "In this room? No." … "Outside? Different question."; Keth's "You won because you knew something about me
  that I didn't know about myself." and "Come find me sometime." "Done," said Keth. "a drawn bow" = BOH. Fine.
- ch41: the stew supper (three, tagged); §8.27 "Iron-equivalent, unclassified, is a story. People travel for stories."
  exact; the mending woman's "*Lad, that's a copper.*" = reported speech; Coss POV from s5 ("Circuit talk"). Fine.
- ch42: Bede (BEED) introduced at the pump; Vell's preamble; the tally-book lines; "*Habit (train it)*" / "*Shape
  (guard it)*". Bede and Brom never share a spoken list (Brom enters s5 after Bede has gone). Fine.
- ch43: Maud (MAWD) introduced; Brom/Lira drill ("there" / "I know"); Lira POV s3–s5 (mark). Maud's "Feet." Vell's
  "provisional". Lane B's added line (the *Shape* column) sits clean. Hesk's note. Fine.
- ch44: Reydan POV from s2 (RAY-dan; Book 3 carry-forward). "Bronze Rank 1" reads naturally. "*Iron-equivalent. Cael.
  No Path designation.*" copied; §8.28 "I'd like it to stay that kind of fight." exact. Fix 5 (yard at ten, academy at
  eleven, Kindled at fourteen) reads clean. Fine.
- ch45: narration list "Feryn… Darrow Innes… Sarel" — FERR-in / DARR-oh / SAIR-el, distinct. Dace "twelve years" (fix 9)
  clean. Lira's bill: "*L*", "*B*", "*E*" in the squares = letter names; "*right foot*". The hesitation entry. Brom's
  Velmere speech. "*Thirteen days.*" Fine.
- ch46: Lira's "no beat before it"; "Bede counted two"; "May I?" / "You may… I like being asked."; Ansel (AN-sel)
  introduced at the cooper's; §8.28 "Survive first. Think second." exact. The cookshop scene (three) tagged. Fine.
- ch47: §8.28 Brom "It compresses inward before it fires outward." exact; "You've no wall" (ch53 quotes it); the plate
  "*EAT, L SAYS*" (caps, letter L) — sentence case at render; Vell at the table. Redirect on the turned RIGHT shoulder.
  Fine.
- ch48: Dace "Twelve years I've not owed a keeper anything" (fix 10) clean; the clerk's account read aloud by Brom
  (italics inside quotes — a voice reading a document); "declined to be interesting"; Brom's "three months on Keth…
  Three months" (fix 7) and "three months on Keth, doing exactly that" (fix 8) clean; "*— L.: Maud did it to me.*"
  (spaced dash, pause). "*Going right. Trained it.*" Fine.
- ch49: Ansel's round ("Even." / "Even."); Ansel says Reydan's name once; Brom relays "He said he'd buy the next one."
  Lira's leave for the knock ("Left," he said / "Yes," said Lira). Fine.
- ch50: pennants; Dace "Twelve years nobody's eaten…" and "keep your rules for twelve years" (fixes 11–12) clean;
  "We're very polite."; session nine, the thirteenth; "What I read in that one exchange was Tide-adjacent."; line 179
  carries the book's one trailing space (harmless); `"Thirteen," he said.` after Brom's line = Cael by alternation and
  by sense; the *Anomalies* entry (not the §8.5 line, which is ch51). Fine.
- ch51: the Log columns "*At rest: 12, 14, 16.*" / "*Moving: 9, 13, 16.*" / "*Defending: 10, 15. …*" / "*Tired: 12,
  16.*" — an engine says the numbers as words; natural, list cadence. §8.10 "Three integrated fragments, one anomaly."
  exact; §8.5 "*Note: Session nine. Could not reproduce. Still don't know what that was.*" exact; §8.29 plan line
  exact. Reydan POV s4 (mark). The nested italic "two *ands*" inside an italic Log line: asterisks even; fpaudio strips
  them. Fine.
- ch52: "Five hundred and four" / "Six hundred people, near enough" (words). Vell's preamble ("Iron, on a guild card.
  Rank eight."). Lira POV s3–s4 (mark). "Not broken. Badly hurt. It guards now." The redirect on the turned RIGHT
  shoulder, into the rope post. Fine.
- ch53: §8.15a "Iron-equivalent, Cael. Win. Method: forced incapacitation, fourth exchange." exact; "*You've no wall,*
  Brom had said … eleven days ago"; "*Whatever that was, it isn't in the book.*" Fine.
- ch54: Reydan POV s1–s2 (mark), then Cael. §8.7 four lines, §8.6, §8.15b/c, §8.30 (both lines and the provision
  sentence) all exact. Quenna (KWEN-a; Book 3 carry-forward) and Greyvane (GRAY-vayn) named. "the demonstration-
  provision track". Fine.
- ch55: the plate "*EAT. L. SAYS.*"; the accounting (fourteen / twelve / two; six Wind; three redirects); the *Note*
  line left exact; "Plum," said Lira; the Stone woman on the wall. Fine.
- Protected-line grep (flattened, all 60 files): every §8 item present; the five "misses" are lines split by a speech
  tag or ending in a comma before the tag (§8.2a, §8.14b, §8.14f, §8.18, §8.24a, §8.26) — words verbatim.
- ch56: the north-window lamp; the three at Lira's table (tagged; "I'm going," said Lira); Brom's questions; the page
  "*DOES THE FORM ASK FOR HIS FAMILY*" (caps, underlined — sentence case at render); Quenna's inn with "a bow window"
  (BOH); §8.16 Brom's three lines exact; Lira pulls Brom's ear. Fine.
- ch57: Lira writes the letter ("*L. wrote this. His hands are no good. He's eating. — L.*"); "*Ulric — Cael*" chalk;
  §8.16 Hesk's three sentences exact with "*H.*" below; Cael's reply "*I'll write when I arrive. — C.*" (fix 14);
  "*Q.*" initial on the struck form; the observer-track sentence (#36) exact; the binder. Fine.
- ch58: Ulric's bout ("Forfeit by the rope."); fix 15's memory exact; §8.8 FRAGMENT ACQUIRED (Compression) code block
  exact; "*Closed. Compression-adjacent…*"; "Four confirmed fragments. One anomaly."; Brom quotes "*Contact range*"
  / "*Damage redirect*". Fine.
- ch59: §8.9 "The records know you existed here." exact; Keth's "a small bow of the head … the same bow" = BAU (the
  book's only BAU); "*EAT. BOTH. ALL THE WAY THERE.*"; "*Gone east. Paid. Good lodgers.*"; "the lead seam" = LED;
  "Mind the shoulder." / "Mind him." / "I always do." Fine.
- ch60: Reydan POV s1 (mark); "*C. — gone east. No price.*"; §8.17 note and road exchange exact; §8.31 and "*Still
  true…*"; "*Exactly like Wind at the start.*"; fix 13 and fix 16 clean; "Oh, yes." Fine.

## Running tally of fixes
Required: ch9 ×2 (opp.), ch11 (Iron-equiv.), ch14 (Iron-equiv.), ch28 (doubled coat / "he said" after Brom's own
line), ch37 (Fri.). Optional: ch24 (lead foot / lead seam in one sentence). Lexicon, not fixes: "def." ×2 (Book 1's
ledger form, protected there), the single letters, "the read" = REED, wound = WOWND (13) except ch8, bow = BOH except
ch59, live/lives by sense.
