# Architecture Review — Book 8: Before the Paths

**Seat:** editor (structural review), pre-drafting gate. Mirrors the Book 7 architecture review's brief and rubric (`v3-runs/book-07/packets/arch-editor-prompt.md`).
**Under review:** `books/book-08-before-the-paths/CHAPTER_ARCHITECTURE.md` (458 lines), read in full, as revised against Book 7's closed prose on 2026-09-04.
**Read first:** `craft/THE_AUTHOR.md`; `craft/VOICE_CHARTER.md`; `universe/CANON_RULES.md`; `universe/UNIVERSE_BIBLE.md`; `series/THE_FRACTURED_PATH_SERIES.md` (Arc 3 header, Book 7 "As drafted", Books 8–9); `v3-runs/book-07/SERIES-FIT.md`; `v3-runs/book-08/audits/b7-reconciliation.md`; `v3-runs/book-08/DECISIONS-B7-RECONCILIATION.md`; `v3-runs/book-08/state-b8-pre-ch01.md`; `craft/NAME_REGISTRY.md`.
**Read-only:** no architecture or prose file was modified by this review.

---

## Verdict: **READY_WITH_FINDINGS**

The book's spine is sound and the reveal is correctly placed, correctly disciplined, and correctly sized. The reconciliation pass repaired the large majority of the `[B7-PROV]` seam. Two findings are BLOCKER-grade — one is a season/calendar contradiction with Book 7's closed prose that the header itself mandates, one is a half-applied reconciliation decision that would mint an uncounted fifth Quieting site and break the argument Part 3 rests on. Neither is expensive to repair at the card. Ten HIGH findings are structural gaps a chapter packet cannot resolve on its own.

**Counts:** BLOCKER 2 · HIGH 10 · MEDIUM 15 · LOW 6 (33 total).

---

## Findings

### BLOCKERS

**B01 — Cael's twentieth birthday is placed in the wrong season; Book 7 fixes his birthday in autumn.**
*Severity:* BLOCKER · *Gate:* CANON_RULES (drafted timeline LOCKED); charter §1 (canon > architecture); THE_AUTHOR §7.4 precedence.
*Architecture — L4:* "He turns **TWENTY** on-page in Chapter 14 — the series' fifth staged birthday, and the first spent back inside a governed city's walls since the academy above Ostrand in Arc 2."
*And L258–261 (Ch14 card):* "**Chapter 14 — Twenty** … Cael turns twenty in the outer district of Treswick".
*Closed prose it contradicts — B7 ch14:151:* "*Hundred and second day past the Line. Nineteen. Written at Thornwater, in the steading's common room, **autumn**, the fire lit for us.*" — and ch14:139, "The birthday fell on the third day … against the last of Thornwater's **autumn**"; ch24:63 places first snow on the hundred and twenty-ninth day, ~27 days later.
*Consequence:* Book 8 opens at winter's end / the thaw (L5, L114: "The ferry runs when the ice goes … Ice goes next week"), and Part 1–2's own clock puts Ch14 roughly five to seven weeks after that — i.e. spring. Cael's birthday is in autumn. As architected he turns twenty roughly seven months early, silently, in the one book whose header forbids silent age drift. Any drafted Ch14 contradicts B7 ch14 on the page and breaks the "one year per book" LOCKED timeline the series bible just rebased everything onto. It also unpicks Ch14's other loads: the Hesk gift (B7's arrived "six weeks late" for the nineteenth), the four-birthday-old written-log custom, and the Book-11 anomaly tripwire staged on the birthday walk.
*Minimal card repair:* choose one, at the header and the Ch14 card, and state the day-count spine that supports it — (a) span the book thaw → the following autumn (Part 2's archive work and Part 3's bearing work carry a season each, with stated day counts), leaving the birthday in Ch14 where its structural work is; or (b) keep the book a spring–summer book, restate the header to "nineteen throughout; twenty arrives in Book 9", and re-purpose Ch14's chapter promise. Do not leave the birthday's date unstated.

**B02 — Ch4 still stages a fifth Quieting perimeter that the reconciliation decision removed; the card contradicts itself in two consecutive paragraphs.**
*Severity:* BLOCKER · *Gate:* B7 seam (b7-reconciliation §2 item 4; DECISIONS row 6); charter §6.4 (no silently minted canon); architecture's own L87 and L411.
*Architecture — L145:* "a stillhound pack that has moved into a stretch of void road through a frozen sink (**NO quiet ground** — Book 7's four sites are the only known perimeters and they lie on one line east of Lowmarch; nothing west of the Line is a site)".
*Architecture — L147, the very next paragraph:* "a defile with a frozen runnel down its center, scree walls too steep to climb fast, **the pack denning in a small quiet perimeter fifty meters off the road where their prey can't declare.** **First exchange:** the crew walks the defile silent; **the hounds break from the quiet ground**".
*Closed prose it would contradict — B7 ch23:11:* "He wrote *third site confirmed on bearing* and stopped. I took the bearing off his first two sites … **Three points make a line. Four make an argument.**" ; ch24:123: "The sites were on an alignment. Not random."
*Consequence:* the drafter has two mutually exclusive instructions in one card and will resolve them by writing the fight as choreographed — i.e. with quiet ground in it. That mints a fifth perimeter, west of the Line, off the bearing, unpaced and uncounted, in Chapter 4. It falsifies Karis's whole alignment argument (the engine of Part 3), contradicts L87 ("First-tier — … NONE found by the companions yet") and L411 ("five sites now known", enumerated as Ring/Stair/Hall/Span/Court), and hands Book 9 a loose site nobody surveyed.
*Minimal card repair:* delete the two quiet-ground clauses from L147 and give the hounds a non-Quiet reason to den in the sink (B7's own mechanic serves: they hunt Path discharge and the sink is where the road's traffic declares). Keep L145's parenthetical as the standing rule.

---

### HIGH

**H01 — Ch12's card still asserts the faceless faction knows nothing about Cael and the Quiet; B7 shows them watching him walk out of it declaring.**
*Severity:* HIGH · *Gate:* b7-reconciliation §2 item 10; DECISIONS row 10.
*Architecture — L239:* "the Compact's reach demonstrated and repelled, its knowledge of the crew's movements now certain, **its knowledge of *what the Quiet does to Cael* still zero** (they saw a fight in an alley; they did not see quiet ground)."
*Closed prose — B7 ch19:151:* "a trap whose door had opened from inside and whose bowl had produced, **on its own rim, a practitioner doing Gold-tier work where the design said he could not be**" ; ch19:195: "\"**You walked out of the Quiet declaring**\"".
*Consequence:* the checkpoint at L411 was repaired to the correct formula and this card was not, so the two disagree inside one document. A drafter working from the Ch12 card will write the faction's posture — and Book 9's antagonist logic — on a false premise: the faction's *entire* reason for escalating is that it saw something at the Stair's rim it cannot explain.
*Minimal card repair:* replace the clause with L411's wording — it knows quiet ground exists, that every Arbiter dies at its line, and that one practitioner walked out of it declaring; what it does not know is what works *inside*.

**H02 — Ch3 stages the Arbiter sub-layer as a disclosure without staging Karis as the woman who already named it aloud in Book 7.**
*Severity:* HIGH · *Gate:* b7-reconciliation §2 item 5; DECISIONS row 7; charter §5.5 (continuity), §7.5.
*Architecture — L134:* "Third, the **sub-layer** (Book-9 plant a; Book-11 plant 2): **Vastin's plainest and worst finding** — the Arbiter evaluation protocol contains an administrative layer beneath the one the Compact uses, which no living official can access".
*Closed prose — B7 ch15:95 (Karis, aloud, at a table):* "it's older than **the sub-layer that modification was written into** — because **that sub-layer is under every station on the continent**".
*Consequence:* the plant ledger at L47 carries the correction ("the NEW fact is the inaccessibility and the six-year deep-layer log, not the sub-layer's existence") but the chapter card does not, and the card is what ships in the packet. A drafter writing Ch3 from L134 alone will write Karis as first hearer of a fact she has carried for a book and said out loud — a visible character regression at the seam.
*Minimal card repair:* add one beat to the Ch3 card — Karis supplies the sub-layer's existence from her own mouth and Vastin supplies the two new facts on top of it; her reaction is to the *inaccessibility*, not the layer.

**H03 — The eastward leg (Treswick back past the Line to the fourth site) is unbudgeted, and Ch18's "a day out" is unreachable from B7's geography.**
*Severity:* HIGH · *Gate:* charter §10 (scene vs summary; travel may be summarized but must be dated); THE_AUTHOR §1.5.
*Architecture — L300 (Ch17):* "Out of Treswick … the crew **turns back east to the sites** with three things they did not have".
*Architecture — L315 (Ch18 close):* "the two crews and the healer setting out east into the deep edge at dawn, twelve on the road … **the Sunken Span a day out** and the Still Court beyond it".
*Closed prose it must reconcile with:* B7's Lowmarch is "a river-ford **three days east of the Line**" (UNIVERSE_BIBLE, §Edge Territories), Treswick "straddling the Registry Line" (L77), and the fourth site was reached from the Drowned Hall and paced at dusk on the 123rd, with Lowmarch regained on the 129th — roughly six days east of Lowmarch (STATE_LEDGER calendar).
*Consequence:* Treswick → the Sunken Span is on the order of nine days and re-crosses the Line, Lowmarch, and the three known sites. The architecture spends that entire traverse in the white space between two cards and then declares the Span one day away. No card carries it, no day-count exists, and Ch18's own business (Oryn's rejoin, the deep reading) is placed *at the far end* of a journey the reader has not been walked through. The book's most legible asset — Book 7's paced, counted geography — goes dark for its whole third act's approach.
*Minimal card repair:* state the leg's day-count in Ch17's card and give Ch18 an explicit position on the road (e.g. Ch17 covers Treswick→Lowmarch and the board, Ch18 opens some stated number of days east with the rendezvous already made); or convert Ch17's close into the dated travel-log the series uses for skips.

**H04 — Ch15's "designed and deployed" plus Ch20's "a spiritual entity does not have a wire" puts Book 9's reveal one sentence away, with no staged refusal beat.**
*Severity:* HIGH · *Gate:* CANON_RULES reveal schedule ("The Arbiter system is the Architect's infrastructure | Reveal book 9"); charter §1, §6.3; B7's own precedent (SERIES-FIT §C: "the refusal is staged four times").
*Architecture — L337 (Ch20):* "Karis states the finding she has been circling since Book 7: every Arbiter, every Path, every person, fails *identically* at every perimeter, \"**the way a hundred lamps fail when one wire's cut, not the way a hundred souls fall silent**,\" and **a personal spiritual entity does not have a wire**. She files it, still, as an observation she cannot explain."
*Against L272 (Ch15, five chapters earlier):* "a historical individual who *designed and deployed* the classification apparatus roughly four hundred years before the present."
*Consequence:* Book 8 puts both halves of Book 9's reveal on one table, in one crew's hands, in one act — a made apparatus with a designer (Ch15) and Arbiters behaving as terminals on a shared circuit (Ch20). The ledger's discipline note at L53(b) says the connection is "the tomb's, Book 9", but no card *stages the refusal*. Book 7 solved exactly this problem by dramatizing the refusal four times on the page. Without an equivalent beat, the most likely drafted line in Ch20 is Karis or Vastin closing the loop — which is a Book 9 leak in the book that must not leak.
*Minimal card repair:* add the refusal to the Ch20 card explicitly, as B7 staged it — someone reaches for the sentence and it is not said, and the card names *who* declines and *why* (Karis's own discipline line, B7 ch20:111, is the tool: "A measurement is a fact about a ruler, not about the hand that held it.").

**H05 — Seln has no scene about Seln; every citation for his want belongs to another character's want-scene.**
*Severity:* HIGH · *Gate:* charter §7.4 ("in a scene that is about them, not about Cael"); the checkpoint's own listing requirement.
*Architecture — L409:* "Seln — Shadow, Bronze; want (his cache/his old life) — tradecraft gets the party into the Deepstacks (**Ch9**), teaches Vastin to \"draft nothing\" (**Ch5**), the cache still targeted and kept (**Ch12**)."
*Consequence:* Ch9's card (L204–206) assigns that chapter to Lira's want-scene; Ch5's "draft nothing" exchange (L158) is staged inside Vastin's want-beat and is explicitly *about Vastin*; Ch12 is a fight. Seln is the only companion whose independent want is discharged entirely as service to other people's chapters — the precise failure §7.4 names ("A companion who spends a whole book only reacting to Cael fails"). Book 7 gave him the angriest beat in the series; Book 8 gives him utility.
*Minimal card repair:* designate one chapter beat as Seln's own — the cache is the obvious lever, and Treswick is the first governed city he has stood in since defecting, which is a scene about him and no one else. Ch10 or Ch11 has room; the checkpoint must then cite a single scene, not three borrowed ones.

**H06 — The Force-adjacent fragment has no stated mechanics, limit, or cost anywhere in the document.**
*Severity:* HIGH · *Gate:* charter §6.1 ("no ability's first on-page use precedes its first stated cost or limit"), §5.3; THE_AUTHOR §1.2, Gate 2.
*Architecture — L326 (Ch19), the whole of it:* "The acquisition notice renders in full (charter §5.1–5.3), Force-adjacent, distinct from the crew's other close-range abilities, integration partial, tier equivalent unknown."
*Contrast:* Rune Path gets a full reference block with limits, weaknesses, costs and a stated uselessness in a fight (L83); Iron Wall Path gets the same, with its limit stated *before* integration (L85). Force gets neither — the only cost mentioned is retroactive ("a Force-line recoil-cost paid by Teague", L328), and the fragment is then in Cael's hands for Ch21 and the book's close.
*Consequence:* the third of three integrations, and the one that lands in the book's final fight, arrives with no limitation/weakness/cost table. A drafter has nothing to write the Ch21 exchanges from and nothing to constrain them with; charter Gate 2 fails on the second use.
*Minimal card repair:* add a Force Path reference paragraph in the same register as Rune and Iron Wall (what it declares, its civil face, its limit/weakness/cost), and move the recoil-cost statement to Ch17 or the reference so it precedes the integration.

**H07 — Ch21, the book's most consequential fight, is the only combat card with no exchange structure and no terrain-caused beats.**
*Severity:* HIGH · *Gate:* charter §4.1, §4.2; THE_AUTHOR Gates 9 and 16 ("≥2 combat beats causally depend on terrain; deletable environment = FAIL").
*Architecture — L350:* "**The fight, terrain first (charter §4.1):** a defile on the bearing short of the Still Court — no Quiet ground here … just hard terrain and a prepared enemy: the team has taken the high ground of a narrow pass and rigged the choke. **Exchanges:** ten practitioners against a smaller prepared force; the crew's full doctrine deployed — Vastin's wall …, Teague's Force, Brom's Iron Skin, Lira's speed, Seln's absence, Cael's compound gaze and now thirteen fragments".
*Contrast:* Ch4 (L147), Ch12 (L239) and Ch19 (L324) each carry numbered First/Second/Third/Fourth exchanges with terrain causing the turns. Ch21 has a roster and an outcome.
*Consequence:* this is the fight that kills a member of Teague's crew and carries its cost into the ending. It is architected as a list of who was present. "Hard terrain" is not terrain; a "rigged choke" with no rig described cannot generate the flank the win-sentence claims. Gate 16 cannot be met from this card, and the death — the book's largest emotional debit — rests on choreography that does not yet exist.
*Minimal card repair:* give Ch21 the same four numbered exchanges the other three combat cards carry, name the rig and the two beats the pass *causes*, and place the death inside a named exchange rather than in the summary.

**H08 — No scheduled no-deflection scene is designated in any of the three Parts.**
*Severity:* HIGH · *Gate:* THE_AUTHOR Gate 25 ("≥1 scene per act shows the protagonist processing without deflection"); charter §3.6.
*Evidence:* the string "no-deflection" / "scheduled quiet" / "Gate 25" returns **zero** hits across all 458 lines. Book 7's architecture designated its scene explicitly (`books/book-07-void-roads/CHAPTER_ARCHITECTURE.md`:376 — "the book's **scheduled no-deflection scene** (charter §25), the losable stake's checkpoint").
*Consequence:* a per-act charter gate has no owner. Ch22 and Ch16 are the plausible candidates for Parts 3 and 2; Part 1 has no candidate at all — Ch7 is the closest and is written as an instrument problem, not as Cael processing. The gate will be discovered as failed at the acceptance pass, after eight chapters are drafted.
*Minimal card repair:* designate one chapter per Part in the Continuity Checkpoint and mark the beat on those three cards (Part 1 needs the new one; Ch16 and Ch22 need only the label).

**H09 — The fragment trajectory under-delivers against the acceleration Book 7 explicitly instructed Book 8 to plan.**
*Severity:* HIGH · *Gate:* series bible (22 fragments by Book 10); SERIES-FIT §B — "Trajectory: twenty-two by Book 10 needs twelve across Books 8–9 — **Book 8's architecture must plan the acceleration explicitly**."
*Architecture — L407:* "integrates **3** this book … Exits at **13** confirmed fragments … **Accelerated acquisition rate, and the book says so (Ch19 log):** 3 in one book vs. the 1–2 of B5–B7, on the bible trajectory to 22 by Book 10 (**leaving ~9 across B9 + the B10 skip**)."
*Consequence:* the architecture states the arithmetic and then accepts a number that does not solve it. Twelve were owed across two books; Book 8 takes three, leaving nine for Book 9 plus a skip — a rate three times Book 8's, in the book that is structurally a *tomb-and-record* book with even less combat than this one. Either Book 9 becomes an integration treadmill or the bible's 22-by-Book-10 figure quietly breaks. Deciding this after Book 8 is drafted costs a book.
*Minimal card repair:* resolve at this gate, not later — either raise Book 8 to five or six integrations (Treswick is full of practitioners Cael can legitimately witness; the Compact watch at the Span is a second source), or take the figure to the bible pass as an OPEN item with a proposed revision. Do not leave the acknowledgement standing in place of the fix.

**H10 — Ch17's log misattributes Book 7's straightedge line to Hesk; B7 attributes it to Cael's grandmother.**
*Severity:* HIGH · *Gate:* charter §1 (canon > architecture); charter §3.2 (a document entry containing what its writer could not have written fails).
*Architecture — L304 (Ch17 close, log):* "a straightedge my guardian sent me because **he said** a man who catalogues everything eventually needs to draw a line through it."
*Closed prose — B7 ch24:87 (Hesk's note, verbatim):* "*Nineteen. I'm told it's late; the ferry's fault, not mine. **Your grandmother said** a man who catalogues everything eventually needs to draw a line through it. This one's true to a hair. Mind the shape. — H.*"
*Consequence:* the card's sample log line, if drafted as written, contradicts closed prose on the page and quietly transfers a dead woman's sentence to a living man — losing the beat B7 built (Hesk is *quoting* her, which is why the gift lands). The word "guardian" for Hesk is also unsupported by B7's prose and should be checked before it enters Book 8's vocabulary.
*Minimal card repair:* restore the attribution in the sample line and check "guardian" against the B1–B6 registry before use.

---

### MEDIUM

**M01 — Ch19 still dates the fourth site's cordon to five/six years; Book 7 dates only the kit.**
*Gate:* b7-reconciliation §2 item 2; DECISIONS row 3 ("No 'five-to-six years' dating on the cordon").
*L322:* "The confrontation is the payoff of \"the Compact already knows\": **they built a fence around this five to six years ago**, and they are still watching it." *L328 (log):* "the Compact **fenced it five years ago** and left men on it."
*B7:* ch20:55 dates the *kit* — "\"**Five years**,\" Seln said … \"By the scale on the case. By the stakes.\"" The fourth site's cordon carries no age (ch23:99 gives only "They've been here more than once").
*Consequence:* the reference block (L89) was repaired to the iron cordon; the Ch19 card and its log were not, and they assert a date nobody on the page derived. *Repair:* drop the date, or give Karis/Seln an on-page derivation at the Span.

**M02 — Ch9 miscounts Lira's Book 7 record.**
*L206:* "she fought the Ring and the Hall **one-armed and without Wind** and was fast anyway `[B7-PROV]`".
*B7:* her forearm is bitten through *at* the Ring (ch11), so she does not fight the Ring one-armed; she loses Wind only inside perimeters; her deliberate no-declaration fight is the ford (ch03:91, "**Without Wind.** A burst is a shout"). *Repair:* "fought the Hall one-armed, the ford without declaring, and lost Wind only inside the line."

**M03 — Ch4's win-sentence reproduces Book 7 Ch3's almost verbatim.**
*L147:* "*Cael removed the pack's ability to converge on Vastin by becoming the louder target and taking the break onto Seln's blade.*"
*B7 ch03:251:* "*I moved first, away from Karis, and every one of them turned, and Seln was behind the big one when it turned. One sentence: we took away the pack's first mover by being it, and Seln took the dog.*"
*Gate:* charter §9 (self-repetition); THE_AUTHOR Gate 14. The tactical *problem* is genuinely new (a rooted ally as the noise source); the resolution beat is the old one. *Repair:* change the terminal beat — let the wall, not the blade, be what the pack breaks into, so the new element resolves the fight it created. Flagged by the reconciliation audit (§2 item 8) and not yet addressed.

**M04 — "A stretch of void road" is used for a road west of the Registry Line.**
*L145:* "a stillhound pack that has moved into **a stretch of void road** through a frozen sink".
*Canon:* UNIVERSE_BIBLE §Edge Territories — "**Void roads:** on Compact maps, roads **beyond the Line** inked dashed and unlabeled; in the edge idiom, the stretches through quiet ground walked fast and silent." Both senses are wrong for a maintained border road on the governed side. *Repair:* "the border road" or "the last good road".

**M05 — The book has no day-count spine, and Ch5 and Ch7 disagree about the distance to Treswick.**
*L5:* the skip is "**roughly** the length of one edge-territory winter" — no date. *L160 (Ch5 close):* "**Two more days.**" *L182 (Ch7 close):* "**Two days.** The walls are close enough now to have a color." — two chapters and a fork later, the same distance. Meanwhile B7 places Lowmarch three days east of the Line and Treswick on it, so the western leg should run about three days, not the five-plus the cards imply.
*Consequence:* Book 7's legibility came from counted days and paced distances. Book 8 currently states neither, and the two numbers it does state contradict each other. *Repair:* fix the opening day-count in the header, give Part 1 an explicit day ladder, and reconcile Ch5/Ch7.

**M06 — Three of the five site names now carry S-onsets, and "the Still Court" collides by ear with "the still place" at the exact moment they must be distinguished.**
*L419:* "\"Still Court\" deliberately rhymes with Cael's \"still place\" (intended, thematic, not a collision)."
*Gate:* charter §8.1, §8.2. The five sites read aloud as Fallow Ring, Long **S**tair, **S**unken **S**pan, **S**till Court — and Ch20/Ch23 name them in sequence. Worse, Ch24's whole beat (L381) is that the still place is **not** the Quieting: "'Not the Quiet' stands". A listener hearing "still court" and "still place" in the same paragraph is being asked to hold a distinction the sounds are working against. The rhyme is a defensible motif (charter §9 protects named repetition), but it is unscreened as an *audio* risk rather than a thematic one. *Repair:* either give the Court a non-S adjective, or require in the card that the two never appear unqualified in the same passage.

**M07 — Chapter 1 carries more scene than 4,600 words can hold.**
*L110–L116* ask one chapter to deliver: the dated winter-skip log movement; the winter's ledger and cash reconciliation; the instrument-anomaly plant established across a season; a two-day walk to Thornwater; Oryn's release of Lira's arm after five months; the mending of the ankle; a surface reading of Cael's ribs; Oryn's reading of the map; the two-day walk back; the crew reconstituted at six; and the closing log. *Gate:* charter §10 (±15% of 4,600). *Repair:* move the Thornwater rendezvous into its own chapter or into Ch2's opening movement, or compress the winter frame to the log and open in motion.

**M08 — The Rune fragment's witnessed-use citation includes a chapter where Cael is not staged present.**
*L407:* "**Rune witnessed Ch11 and Ch13**". *L226–L230 (Ch11)* places Cleon, Karis and Brom in the stacks; Cael appears only in a later exchange ("He asks Cael, later"). *Gate:* Continuity Rule 6 ("The ability must be performed in his presence"); charter §5.3. Ch13 alone carries a clean witness, and witness and integration then occur in the same scene — legal, but thinner than the series' own Tide precedent (taught B7 Ch7, integrated B7 Ch13). *Repair:* put Cael in the Ch11 room as labor, or drop Ch11 from the citation.

**M09 — Ch19's Quiet-boundary tactic needs its own fairness statement.**
*L324:* "the crews **who have walked into quiet ground three times and come out** `[B7-PROV]` will, briefly, which gives them a wall the watch cannot cross."
*Gate:* THE_AUTHOR §1.1 (Fairness Law), charter §4.7. Stepping over the line costs the crew their Paths exactly as it costs the watch theirs; the asymmetry is willingness, not capability. As written the card reads as if the crew gains something inside. *Repair:* state in the card that the advantage is nerve and prior experience, not mechanics, and price what the crew gives up for the seconds it holds.

**M10 — The Deepstacks access rule does not say what happens to a [SHATTERED] on a party roster.**
*L79 / L204:* access runs through "the old scholars' provision … which admits *registered historical-studies practitioners*" and "Cael goes in as *labor* — an unranked hand carrying boxes".
*Canon:* UNIVERSE_BIBLE §City Access — "Unranked / [SHATTERED] — Unranked Districts only; **cannot legally enter inner city**." The Deepstacks sit under the registry office, inside the tiers. *Gate:* charter §6.5, §3.7 (institutions as mechanism). *Repair:* state the rule that resolves it — whether a working-party pass suspends the classification bar, or whether the clerk simply never checks (and therefore what the exposure is). The book's central access problem should be a machine, not an assertion.

**M11 — `[B7-PROV]` no longer distinguishes verified from stale, and the document still orders a re-verification that has been performed.**
*53 `[B7-PROV]` flags remain.* *L2:* "Book 7's prose is finishing on a separate track … MUST be re-verified against Book 7's drafted Ch23–24 before any Book 8 chapter is drafted". *L397:* "**RE-VERIFY AGAINST DRAFTED B7 CH23–24 BEFORE DRAFTING ANY B8 CHAPTER**". *L417(iii), (vi):* the same, including the fragment total the audit closed at 10+1.
*Consequence:* Book 7 is closed and the reconciliation is complete, but the flag now means three different things in one document (confirmed / corrected / still stale), and a drafter cannot tell which from the flag. *Repair:* retire or re-letter the flag — `[B7-OK]` for the 38 confirmed, keep `[B7-PROV]` only where a decision is still open — and update L2/L397/L417 to point at the reconciliation and DECISIONS files as the settled record.

**M12 — The pre-Ch1 state snapshot still lists instruments Book 7 never put in the kit.**
*`v3-runs/book-08/state-b8-pre-ch01.md`, Carried objects:* "the Compact survey kit (registry-stamped; **sighting-glass, tally-rule**, cord)".
*B7 ch20:45–51* inventories the case in full: a pacing cord knotted at the fives, an iron stake numbered thirty-two, a mallet, a field ledger, and no pen. The architecture's Ch1 was repaired (L116 item 3, "No sighting-glass, no tally-rule"); the state file the drafter loads alongside it was not. *Repair:* correct the state file's inventory line.

**M13 — Chapters 23 and 24 spend ~9,200 words on arrival, a walk to a centre, and a walk back.**
*L370–L374 (Ch23)* holds deliberately at the threshold; *L381–L387 (Ch24)* is Cael crossing a seamless floor alone, feeling nothing, and returning. Both are correct decisions structurally — the withheld centre is the book's best-earned move — but neither card names enough *scene* to carry its length. Ch24 in particular has one character, no dialogue until the return, and a discovery that is by design an absence. *Gate:* charter §10 (±15%), §3.6. *Repair:* name the material — the pacing of the larger perimeter and the crew's reactions at the line (Ch23), and in Ch24 the physical business of the crossing, the Rune reading run on the floor itself, and the return to five faces — so the drafter is not asked to inflate.

**M14 — Oryn's departure is now staged twice, and the crew's only healer is absent across the archive act and two of four fights.**
Book 7 spent her fork (ch23); Book 8 stages the rendezvous (Ch1), a second fork (L167–L171, Ch6), and a rejoin (Ch18). She is offstage Ch7–Ch17, which contains the Treswick alley fight (Ch12) and Brom's standing "it will not hold three times this season" shoulder (B7 ch21:185).
*Gate:* charter §4.3 (costs persist and are paid on the page); the reconciliation's warning against spending her departure twice. *Repair:* the architecture should state what the crew does for a healer in Part 2 — that absence is a real cost and currently an unpriced one — and consider whether the Ch6 fork earns its chapter given Ch1 now carries the reunion.

**M15 — L59's thread summary still calls the fourth site's cordon a watch-post, conflating B7's fact with Book 8's invention.**
*L59:* "*The fourth site* … its **cordon is a Compact watch-post**, the payoff of the \"the Compact already knows\" plant." The reference block (L89) correctly separates them ("the registry-stamped iron cordon Book 7 found … and, **NEW this book**, a watch-post at it"). *Repair:* bring L59 into line with L89 so no card inherits the conflation.

---

### LOW

**L01 —** L2's canon-status header ("Book 7's prose is finishing on a separate track") is factually stale; Book 7 closed 2026-09-04.
**L02 —** L261 reads as though Hesk's straightedge arrives a second time: "Hesk's letter and gift arrive … the straightedge from Book 7 `[B7-PROV]` **now companioned by** a set of dividers". Clarify that only the dividers are new.
**L03 —** L127 gives Pike the ferry ("**Pike's ferry**, behind him, turns back west"). B7 gives Pike the board; the ferry is the ferryman's and the mail's.
**L04 —** L278's sample passage renders the effaced name as a typographic gap — "*and the [ ———— ] set the apparatus over all the land*". L32 already requires the damage to be *described*; the sample line should model that, since it is the line most likely to be copied verbatim.
**L05 —** The closer sequence at L423 passes the adjacency rule but rotates log·dialogue·image in strict order for the first nine chapters. Legal, audible as a pattern; consider one deliberate break in Part 1.
**L06 —** The Ch14 card does not stage the written-log birthday custom B7 established as "now four birthdays old" (ch14:149) — the fifth staged birthday should keep the form, and Ch14 currently closes on an image.

---

## Strengths — preserve these through repair

1. **The reveal is correctly disciplined, and the discipline is written down.** L43's four-part "DO NOT OVERSHOOT" clause and the sealed-secrets checkpoint at L399 are the tightest reveal-governance the series has produced: the record is a claim about history, the name is physically unreadable, the rationale is reported and not endorsed, and the connection to live sigils is explicitly reserved for the tomb. The effaced name (L272) is a genuinely good invention — it delivers the bible's requirement and creates a permanent mystery-texture without scheduling a reveal.

2. **The exclusion → prevention distinction is precise, and the book refuses to let it blur.** L20 and L285 hold the same sentence pair at both poles and articulate exactly why fourteen chapters can pass without the reader feeling cheated: "from the outside exclusion and prevention look identical — a locked door is a locked door whether you were forgotten or feared." That is an arc statement that can actually be drafted against.

3. **Three Book-11 plants that are individually deniable and cumulatively lethal.** L55's design — a hedged chronicle phrase, a six-year counter nobody can read, and instrument errors that cluster and *increase* — is the best plant architecture in the series so far, because every instance has a sufficient in-world explanation already on the page (his unreadable architecture) and none of them requires a character to be stupid.

4. **Rune Path and Iron Wall Path are both built limits-first.** L83 and L85 state what each cannot do before either is load-bearing, and Iron Wall's limit is *dramatized* in Ch4 as a liability before it is integrated in Ch12 as an asset — the Fairness Law executed as structure, not as a citation.

5. **The two-instruments problem is a genuinely original engine.** Tide reads current and can only report current-absent; Rune reads made structure and returns *bones*. Holding the two readings in disagreement (Ch18, Ch22) lets the book go deeper into what Cael is than any prior book while saying strictly less — and it is the mechanism that makes Ch24's ending land without a word from Book 9.

6. **Treswick's argument in one image.** "A Compact registry office built directly on top of a pre-Compact archive it has never read" (L77) is worldbuilding by mechanism in the register §6.5 asks for, and the access problem (a [SHATTERED] entering the oldest record of what he is *as labor*, because labor is what the city thinks he is worth) is the best institutional irony the series has staged since the ladder mathematics of Book 4.

7. **Cleon is correctly built and correctly aimed.** L81's differentiation — "where Oryn approaches Cael as a patient who doesn't work, Cleon never examines Cael at all … the book keeps him pointed at the page, not the boy, which is exactly why Cael can be in the room" — is a specialist who solves a scene problem rather than a plot problem, and his want (finished and believed) is legible without a speech.

8. **The reconciliation pass did most of its job.** Of the audit's seventeen corrections, thirteen are fully applied and visible in the document — the roster, Lira's arm, the iron cordon, the still-place negation at Ch24, the straightedge count, the "no column" idiom, the mule image's re-citation, "walked into quiet ground three times", the Thornwater-ford error, the index-vs-grade distinction, the kit's real instruments, the eleven/twelve counts, and every name on the rename list. The document is in materially better shape than the raw claim counts suggest.

---

*Review complete. No architecture or prose file was modified.*
