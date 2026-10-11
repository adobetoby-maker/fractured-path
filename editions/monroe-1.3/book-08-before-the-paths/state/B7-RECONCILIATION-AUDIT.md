# Book 8 plan — Book 7 reconciliation audit

**Audit seat:** Sol, fresh continuity context  
**Date:** 2026-10-11  
**Plan audited:** `BOOK_MAP.md`; entry `STATE_LEDGER.md`; `packets/MOVEMENT-001.md` … `MOVEMENT-009.md`  
**Edition canon checked:** closed Book 7 Movements 1–6 and their surviving manuscript; locked Book 6; Books 4–5 where the Book 8 plan reaches back; `OWNER-DECISIONS.md`; universe bible and canon rules  
**Method:** read-only continuity audit. Book 7 Movements 7–8 are PLAN, not canon.

This report follows the form and depth of `book-07-void-roads/state/B6-RECONCILIATION-AUDIT.md` and its F re-run. Its amendments are written so an apply seat can execute them without reconstructing the finding.

## Severity key

- **BLOCKS M1** — Book 8 Movement 1 must not be released with this unreconciled.
- **Affects later movement** — does not prevent Movement 1 after its own dependencies are locked, but must be applied before the named later movement.
- **Cosmetic** — wording, pointer or ledger precision; apply in the reconciliation pass.
- **PENDING B7 M7–M8** — the Book 8 plan depends on Book 7 events that are not canon yet. Do not turn the forecast into Book 8 entry canon until Book 7 closes.

Line citations are to the current files at audit time. “B7 ledger” means `book-07-void-roads/STATE_LEDGER.md`; chapter citations mean the closed Book 7 edition manuscript.

## Result in brief

Book 8 Movement 1 is **not presently releasable**. Its packet and entry ledgers still carry a pre-edition Book 7 close, including stale source-chapter references, named seasons, metric units, an incorrect Karis rank, an inverted Oryn debt, incomplete capability rules, the wrong mechanism-knower count, and language that gives Cael a Path. In addition, almost the whole detailed entry seam—day 131, the completed traverse, three readings of the still place, nine Pike lines, 52 sheets, 96 marks, Oryn at Thornwater, Teague’s term, and the final object inventory—depends on Book 7 Movements 7–8, which are not canon yet.

The Book 8 architecture itself remains viable. The three new fragments (Iron Wall, Rune, Force), the close at thirteen, and the trajectory toward twenty-two by Book 10 do not conflict with closed canon. The plan can be released after Book 7 is locked, this list is applied, and the required M7–M8 re-run passes.

---

## A. Findings that block Movement 1

### A1. The Book 8 entry state is being asserted from an unfinished Book 7 ending

**Grade: PENDING B7 M7–M8 / BLOCKS M1**

**Book 8 locations:**

- `BOOK_MAP.md:19–27`, especially `:22–26`.
- `STATE_LEDGER.md:3,7,13–20,27–55`.
- `packets/MOVEMENT-001.md:17`.

**Edition evidence:** Book 7 is CLOSED only through Movement 6 (`book-07-void-roads/STATE_LEDGER.md:613–701`). At that point it ends on day 112, not day 131; the five are leaving Thornwater, Oryn is on foot near the mill, the mule is with the crew, cash is 102, Pike has eight lines, three readings and a telling remain owed, and the fourth site has not been paced (`B7 ledger:659–699`). The Book 7 map’s day-129–131 close is explicitly its planned ending (`book-07-void-roads/BOOK_MAP.md:28–46`), not surviving prose. Movement 7 is being drafted and Movement 8 has not begun.

**Amendment:**

1. Put a binding note immediately above `BOOK_MAP.md` §1 Entry and immediately above `STATE_LEDGER.md`’s entry table:

   > **[B7 reconciliation — PENDING B7 M7–M8.]** The detailed Book 8 entry below is a forecast from the Book 7 plan, not canon, until Book 7 Movements 7–8 close. Before Book 8 Movement 1 is released, replace every entry fact with the closed Book 7 ledger/manuscript fact and record any difference in `state/B7-RECONCILIATION-APPLIED.md`.

2. Add the same one-sentence warning after `MOVEMENT-001.md:17` until the re-run is complete.
3. After Book 7 closes, remove the warnings only after all items in §H of this report are verified.

The forecasted seam facts are itemized under §H; none may be promoted merely because it appears in the Book 7 `BOOK_MAP.md`.

### A2. The no-source method is absent from all nine packets

**Grade: BLOCKS M1 for Movement 1; Affects later movement for Movements 2–9**

**Book 8 locations:** every `Read before drafting` line: `MOVEMENT-001.md:9`, `MOVEMENT-002.md:9`, `MOVEMENT-003.md:9`, `MOVEMENT-004.md:9`, `MOVEMENT-005.md:9`, `MOVEMENT-006.md:9`, `MOVEMENT-007.md:9`, `MOVEMENT-008.md:9`, `MOVEMENT-009.md:9`.

**Edition evidence:** coordinator override O3 is binding and says to retain source references for coordinator/reviewer tools while forbidding the author to open source chapters (`book-07-void-roads/state/B6-RECONCILIATION-COORDINATOR-OVERRIDES.md:26–34`).

**Amendment:** insert this note verbatim immediately above each of the nine lines:

> **[Coordinator note 2026-10-11 — NO-SOURCE drafting, binding.]** Draft WITHOUT opening any source chapter under `books/`. The source-chapter references in the line below are retained for the coordinator's and reviewers' tools only; the author does not read them. Events come from this packet, `BOOK_MAP.md` (the plan sections, the protected-text section and the reserved-truths section) and `STATE_LEDGER.md`. Write `EVENT-LIST.md` first. Where a protected unit is quoted in the plan only in part, leave `[[TIER-B: <unit> — coordinator to supply protected text]]` and write around it.

Do not delete the underlying `Read before drafting` lists. Their source-chapter bullets remain coordinator/reviewer references only.

### A3. The entry gives Karis the wrong rank and prematurely gives her an unstated hypothesis as knowledge

**Grade: BLOCKS M1**

**Book 8 locations:** `BOOK_MAP.md:23` (“unranked by choice”); `STATE_LEDGER.md:16` (same); `STATE_LEDGER.md:41` (“carvings command rather than describe”).

**Edition evidence:** Karis is Ember, Iron Rank Three (`B7 ledger:622,670`; `book-07-void-roads/manuscript/chapter-42.md:11`). At the close of Movement 6 her hypothesis is “NOT stated anywhere,” neither entered nor said (`B7 ledger:621–622,670,696`; `chapter-44.md:61`). Book 7 Movement 7 may give her more evidence, but that remains plan.

**Amendment:**

- In `BOOK_MAP.md:23` and `STATE_LEDGER.md:16`, replace `unranked by choice` with `Iron Rank Three`.
- Replace `STATE_LEDGER.md:41`’s command claim with: `that the repeated bands are made marks; she has a hypothesis, neither spoken nor entered at the end of closed Movement 6.`
- Append: `Reconcile this sentence to the surviving Movement 7–8 prose before M1; do not assume the command/description conclusion crossed the Book 7 seam.`

### A4. Oryn’s route, knowledge and debt are misstated

**Grade: BLOCKS M1, with route location PENDING B7 M7–M8**

**Book 8 locations:** `BOOK_MAP.md:24,38`; `STATE_LEDGER.md:18,83`; `MOVEMENT-003.md:40–42`.

**Edition evidence:** at the closed M6 seam Oryn is on foot, the mule is with the crew, and she is near a mill on day 112 (`B7 ledger:624,653,657,662,674,699`; `chapter-44.md:223–301`). Cael—not Oryn—owes three self-readings on three days and then the full telling (`B7 ledger:616–617,656,664`; `chapter-44.md:169–211`). Oryn knows the mechanism as a retelling, with sources by Path rather than person; she does **not** know Seln supplied Shadow-adjacent (`B7 ledger:616,672,674,686`). Reading always requires an ask and an answer; the form does not imply consent (`chapter-39.md:29–37`; `chapter-44.md:157`).

**Amendment:**

- Replace `BOOK_MAP.md:24` and `STATE_LEDGER.md:83`’s “Oryn owes Cael a reading” with: `Cael owes Oryn three self-readings on three different days, then the full account at once, on a day she sets. Reconcile the paid/owed state to Book 7’s final ledger.`
- In `STATE_LEDGER.md:18`, replace the fixed `At Thornwater` with the post-M8 location from the final Book 7 ledger. Until then mark it `[PENDING B7 M7–M8]`.
- Add to Oryn’s knowledge entry: `She knows sources by Path, not by person except those she has touched; she does not know Seln is Shadow-adjacent’s source.`
- Replace `MOVEMENT-003.md:42`’s `with consent implied by the form` with `after she asks and receives an explicit yes`.

### A5. The mechanism-knower count omits Cael

**Grade: BLOCKS M1**

**Book 8 location:** `STATE_LEDGER.md:39`.

**Edition evidence:** Book 7 closes M6 with six knowers, including Cael: “The mechanism: six” (`B7 ledger:686`). Oryn is the sixth addition; Teague, Pike and Vastin do not know (`book-07-void-roads/BOOK_MAP.md:38,327–330`).

**Amendment:** replace the sentence with:

> **Who knows the integration mechanism:** Cael, Lira, Brom, Karis, Seln and Oryn — six. Oryn was told sources by Path and not by person except the three she has touched; she does not know Seln supplied Shadow-adjacent. **Not** Vastin, Teague, Pike or Cleon.

### A6. The plan says Cael has a Path

**Grade: BLOCKS M1 where it defines entry canon; Affects later movement in protected lines**

**Book 8 locations:** `STATE_LEDGER.md:30`; protected `BOOK_MAP.md:405,408,410`; the surrounding premise at `BOOK_MAP.md:22,117` must carry the exact mechanics.

**Edition evidence:** Cael has no Path. His own Arbiter woke at Kindling; its plate lit eleven seconds late; the failed-safe word replaced the old name; it then went dark. The fragments still answer inside quiet ground, and nobody has said why (`OWNER-DECISIONS.md:154–157`; locked B6 `manuscript/chapter-36.md:117`, `chapter-39.md:59–63`; B7 `chapter-01.md:29`, `chapter-38.md:5`). Owner #49 grandfathered two loose **Book 7** protected clauses as shorthand; it also binds narration and dialogue to the actual mechanics. It does not authorize new Book 8 statements that he has a Path.

**Amendment:**

- Replace `STATE_LEDGER.md:30` with: `His own Arbiter has been dark since Kindling. At quiet ground every live Arbiter in the party stops; his is dark before and after, while the fragments still answer. He has no Path. Nobody has said why.`
- In the general entry inventory, add the plate and failed-safe facts once, not at every quiet line.
- Make the protected-text changes listed in §F3, citing OWNER #49.

### A7. The fragment ledger loses edition-fixed rules and states one false Tide rule

**Grade: BLOCKS M1**

**Book 8 locations:** `BOOK_MAP.md:22,117,257–268`; `STATE_LEDGER.md:57–73`; `MOVEMENT-001.md:21,26,28,44`.

**Edition evidence:** closed Book 7 fixes numbers and bills that Book 8 must not erase:

- Iron reads air **or** body/ground at Gold weight, never both; when Storm holds air, body read is lost (`B7 ledger:537`; `chapter-39.md:143`).
- Storm’s laid lanes are ten/ten/twelve; clean limits eleven/eleven/thirteen; untested beyond three lanes; the late beat is billed (`B7 ledger:537`).
- Anchor perception is sure at ten feet, faint at twelve, absent at fourteen; purposeful unbinding is separate and counts as a deployment (`B7 ledger:537`).
- Shadow was used once by M6 and sealed again (`B7 ledger:538,664`). The planned Stair use would make two only if it survives M7.
- Tide is self **and** contact. It has already been used on Cael himself. “Ask first” applies when it turns outward (`B7 ledger:616–617,664`; `chapter-40.md:367–385`).
- Deployment since the Line is thirteen at M6 (`B7 ledger:619,664`).

**Amendment:** replace the terse rows/notes with the following minimum ledger text:

| Capability | Required Book 8 entry rule |
|---|---|
| Iron-adjacent | `At Gold weight it reads air or body/ground, never both; holding Storm’s air read loses the body read.` |
| Storm-adjacent | `Laid lanes 10/10/12; clean limits 11/11/13; untested beyond three lanes; late-beat bill retained.` |
| Anchor-adjacent | `Perception sure at 10 feet, faint at 12, absent at 14. Purposeful unbinding is a separate deployment. Reach/rate/price beyond those findings remain blank.` |
| Shadow-adjacent | `Used once through closed M6 and sealed. Reconcile the final Book 7 count after M7–M8; if the Stair use survives, entry count is exactly twice.` |
| Tide-adjacent | `Self and contact; clinical; self first; ask first every time when outward; tell Oryn. It has already read Cael himself.` |

Also:

- Change `MOVEMENT-001.md:28` and `BOOK_MAP.md:117` from `does not run/read on himself` to `has read himself; no outward use without an ask and an explicit yes`.
- Change `MOVEMENT-001.md:44` and `STATE_LEDGER.md:73` from `Invent no numeric ceilings` to `Invent no new numeric ceilings. Preserve every numeric ceiling and bill already fixed by canon.`
- Add a field to the entry ledger: `Deployment since the Line: [final Book 7 number]. Closed M6 baseline: thirteen.`

### A8. Money, objects and open debts are flattened into a future forecast

**Grade: BLOCKS M1 / PENDING B7 M7–M8**

**Book 8 locations:** `BOOK_MAP.md:22–24`; `STATE_LEDGER.md:49–55`; `MOVEMENT-001.md:17,24–25`.

**Edition evidence:** at closed M6 there are 102 marks in hand; the sealed cart-and-gelding reserve remains in the third box under five thumbprints; the ferryman’s rope is owed; the Fallow hundred is unpaid in Pike’s box; two HOLD slips are unresolved; Seln’s case is shut; the mule is with the crew; Oryn has taken the spare thirty-foot rope; the yard crossbow has five bolts; three letters are unanswered (`B7 ledger:196–200,617,653,672,678,698`; `chapter-15.md:153`; `chapter-27.md:13`; `chapter-43.md:197`; `chapter-44.md:211–245`). OWNER #23 makes the reserve binding (`OWNER-DECISIONS.md:30`).

The 96 marks, nine Pike lines, 52 sheets, one remaining bolt, completed fourth-site kit and received letters in the Book 8 plan are Book 7 M7–M8 forecasts.

**Amendment:**

1. Add the sealed reserve to both `BOOK_MAP.md` §1 and `STATE_LEDGER.md` resources: `The cart-and-gelding reserve remains sealed in the third box under the five thumbprints unless closed Book 7 prose explicitly spends it.`
2. Replace `Nothing owed` at `BOOK_MAP.md:22` and `STATE_LEDGER.md:49` with a final-Book-7 accounts line. Until closure it must read: `Open at M6: ferryman’s rope; Fallow hundred unpaid in Pike’s box; two HOLD slips unresolved.`
3. Call Seln’s object `his locked case, shut and unopened`, not a generic cache.
4. After M8, copy cash, bolt count, sheets, Pike lines, kit contents, map, mule, reserve and debts from the CLOSED ledger—not from the Book 7 map.

### A9. The series calendar is treated as settled when it is not

**Grade: BLOCKS M1 for the opening date and elapsed-month line; Affects later movement elsewhere; some facts PENDING B7 M7–M8**

**Book 8 locations:** `BOOK_MAP.md:19,21–22,28–29,37,48,56,71,86–88,206–244,390,407,410,437,447,488`; `STATE_LEDGER.md:7,13`; `MOVEMENT-001.md:17,24–31,53`; `MOVEMENT-005.md:31`; `MOVEMENT-009.md:26,34`.

**Edition evidence:** Book 7 counts days past the Line; closed M6 ends at day 112 (`B7 ledger:613,659–660`). Day 102 is Cael’s nineteenth birthday and may never be placed beside a season, a month order or a count back (`B7 ledger:620`; `OWNER-DECISIONS.md:146–151`). The planned Book 7 close at days 129–131 is not canon yet. Owner #35 deliberately leaves month lengths/order undefined (`OWNER-DECISIONS.md:55–59`).

**Amendment:**

- Retain Cael as nineteen and retain “no birthday in Book 8.” Delete `in autumn` from `BOOK_MAP.md:22` and `STATE_LEDGER.md:13`.
- Keep the Book 8 day spine internally, but mark the opening `day 131` and all cross-book intervals `[PENDING B7 M7–M8]` until the final Book 7 day is known. If the Book 7 close moves, shift Book 8’s whole relative day spine by the same delta unless a scene depends on a fixed date; list every shifted date in the applied report.
- Replace the protected/duplicated Thornwater interval at `BOOK_MAP.md:56,390` and `MOVEMENT-001.md:31`: `Five months and twenty days.` → `Since the Ring.` Retain the generic reply `That’s a season. Take it off.` Generic *season* and *month* are permitted.
- Replace the elapsed Kindling counts and the “whole year” claims as specified in A10 and §F.
- At `BOOK_MAP.md:488`, replace the Book 9 birthday forecast with: `Cael remains nineteen at the Book 9 opening. Do not place or calculate his next birthday until the owner rules the series calendar.`
- `Vastin day 30 of Oryn’s month` (`BOOK_MAP.md:37`) is a treatment-course count, not a named calendar month; it may stay, but clarify `the thirtieth day of Oryn’s treatment month` so it cannot be read as month-of-year.

### A10. Numeric time since Kindling and implicit five-year arithmetic violate the standing ruling

**Grade: BLOCKS M1 for Movement 1 text; Affects later movement for later protected units**

**Book 8 locations:** `BOOK_MAP.md:63,71,364,389,400,405,437,447`; `MOVEMENT-001.md:53`; `MOVEMENT-003.md:27`; `MOVEMENT-005.md:31`; `MOVEMENT-008.md:66`.

**Edition evidence:** OWNER #18 requires “since his Kindling,” with no number (`OWNER-DECISIONS.md:25`), and #48 explicitly extends that rule into Book 7 (`OWNER-DECISIONS.md:146–150`). Cael is nineteen, but the edition does not use his ages to state an elapsed five years since Kindling. Book 6 gives the event mechanics, not a duration.

**Amendment:**

- `BOOK_MAP.md:63` and `MOVEMENT-003.md:27`: replace `five years and a hundred-some days back` with `the date matches his Kindling day`; retain `six years` only as the office’s survey-record rounding, never as Cael’s age arithmetic.
- `BOOK_MAP.md:71` and `MOVEMENT-005.md:31`: replace `I was fourteen. I’m nineteen. I’m not there yet either.` with `Since my Kindling. I’m not there yet either.`
- `BOOK_MAP.md:405` and `MOVEMENT-008.md:66`: replace `since I/he was fourteen` with `since my/his Kindling`.
- Rewrite `BOOK_MAP.md:437` so the policy reads: `No numeric span since Kindling. Anchor academy/cache spans to events; office survey records may keep their own six-year rounding where explicitly identified as the office’s.` Delete the sentence saying five years “is correct and stays.”
- Rewrite `BOOK_MAP.md:447`: `Six years is the office’s survey-record rounding. It is not paired with a numeric count since Cael’s Kindling.`
- Apply the protected changes at `BOOK_MAP.md:364,389,400` listed in §F2.

### A11. All named seasons and metric units must be normalized, including protected text

**Grade: BLOCKS M1 where present in Movement 1 and entry state; Affects later movement elsewhere**

**Edition evidence:** coordinator O4 bans named seasons, named months/month order, English weekdays and metric units, while retaining generic `season` and `month`; the change applies inside protected lines (`B6-RECONCILIATION-COORDINATOR-OVERRIDES.md:36–54`; `OWNER-DECISIONS.md:146–150`). Book 7’s current callbacks are `After the thaw…` (`book-07-void-roads/BOOK_MAP.md:269,321`) and its fourth site is about 440 yards in radius (`:43`).

No English weekday name and no named calendar month occurs in the Book 8 plan. Generic `season` and `month` are permitted and must remain. Literal water springs at `BOOK_MAP.md:63,78,119,142,192,219,233`, `MOVEMENT-003.md:27,32,46`, and `MOVEMENT-007.md:25` remain **spring**. Physical `fall` at `MOVEMENT-008.md:48` remains **fall**.

Apply every row below.

#### A11.1 Named-season occurrences

| Book 8 location | Current minimum target | Apply exactly |
|---|---|---|
| `BOOK_MAP.md:22` | `in autumn` | delete |
| `BOOK_MAP.md:25` | `winters`; `Spring. Whatever’s…` | `stays through the cold term`; `After the thaw. Whatever’s on that bearing. My crew comes.` |
| `BOOK_MAP.md:38` | `Spring. Bring…` | `After the thaw: bring the map, and lie still when I say. — O.` |
| `BOOK_MAP.md:39` | `Next spring` | `After the next thaw` |
| `BOOK_MAP.md:51` (both) | `winter frame`; `winter is priced` | `cold-term frame`; `cold stay is priced` |
| `BOOK_MAP.md:52` | `winter board` | `cold-term board` |
| `BOOK_MAP.md:56` | `spring’s first stops` | `first stops after the thaw` |
| `BOOK_MAP.md:83` | `Not one winter` | `Not one cold term` |
| `BOOK_MAP.md:106` (both) | `winter` | `cold-weather` |
| `BOOK_MAP.md:108` | `winter` | `cold-weather` |
| `BOOK_MAP.md:117` | `in winter` | `during the cold term` |
| `BOOK_MAP.md:127` (both) | `winter months`; `board in winter` | `cold months`; `cold-term board` |
| `BOOK_MAP.md:128` | `prepares for spring` | `prepares for the road after the thaw` |
| `BOOK_MAP.md:132` | `in the autumn` | `at the Hall` |
| `BOOK_MAP.md:147` | `spring term` | `after-thaw term` |
| `BOOK_MAP.md:148` | `Prices the winter` | `Prices the cold term` |
| `BOOK_MAP.md:167` | `Put the winter on the page` | `Put the cold term on the page` |
| `BOOK_MAP.md:192` | `a winter night` | `a cold night` |
| `BOOK_MAP.md:195` | `in winter` | `during the cold term` |
| `BOOK_MAP.md:206` | `Winter priced` | `Cold stay priced` |
| `BOOK_MAP.md:215` | `Teague’s spring` | `Teague’s after-thaw term` |
| `BOOK_MAP.md:275` | `winter inventory` | `cold-term inventory` |
| `BOOK_MAP.md:369` | `Spring’s over`; `Next spring`; `Spring. Bring…` | `The thaw’s past`; `After the next thaw`; current B7 Oryn line above |
| `BOOK_MAP.md:380` | stale Oryn `Spring:` callback | current B7 Oryn line above |
| `BOOK_MAP.md:382` | stale Teague `Spring.` callback | current B7 Teague line above |
| `BOOK_MAP.md:403` | `came for spring` | `came after the thaw` |
| `BOOK_MAP.md:456` | `New winter` | `New cold-term` |
| `BOOK_MAP.md:488` | Oryn `Spring`; Teague `Next spring`; `autumn birthday` | current B7 callbacks; delete the season/birthday forecast per A9 |
| `STATE_LEDGER.md:13` | `in autumn` | delete |
| `STATE_LEDGER.md:19` | `Wintering` | `Staying through the cold term` |
| `STATE_LEDGER.md:98` | `spring term` | `after-thaw term` |
| `MOVEMENT-001.md:12` | `C (winter)` | `C (cold term)` |
| `MOVEMENT-001.md:21` | `Put the winter` | `Put the cold term` |
| `MOVEMENT-001.md:24` (both) | `winter priced`; `board in winter` | `cold stay priced`; `cold-term board` |
| `MOVEMENT-001.md:25` | `winter road` | `cold road` |
| `MOVEMENT-001.md:27` | `across the winter` | `across the cold term` |
| `MOVEMENT-001.md:30` | `through the winter` | `through the cold term` |
| `MOVEMENT-001.md:35` | `winter night` | `cold night` |
| `MOVEMENT-001.md:49` | `winter takes` | `cold term takes` |
| `MOVEMENT-002.md:17` | `spring stop` | `first post-thaw stop` |
| `MOVEMENT-002.md:24` | `ready for spring` | `ready for the road after the thaw` |
| `MOVEMENT-002.md:28` | `at a table in the autumn` | `at a table before we left Ostrand` |
| `MOVEMENT-008.md:28` | `in the autumn` | `earlier at the Hall` |
| `MOVEMENT-008.md:31` | `Not one winter` | `Not one cold term` |
| `MOVEMENT-009.md:39` | `Next spring`; `Spring. Bring…` | `After the next thaw`; current B7 Oryn line above |

#### A11.2 Metric occurrences

| Book 8 location | Current | Replacement |
|---|---|---|
| `BOOK_MAP.md:26`; `STATE_LEDGER.md:29` | `400 m radius` | `about 440 yards’ radius` |
| `BOOK_MAP.md:34,88` | `1,012 m across` | `about 1,107 yards across` |
| `BOOK_MAP.md:321` | `fifty metres below` | `fifty-five yards below` |

The protected changes in this table must be listed old/new in the applied report and tagged as OWNER-pending #48, following the Book 7 precedent.

### A12. Book 7 callbacks and source pointers name obsolete source chapters

**Grade: BLOCKS M1 / PENDING B7 M7–M8**

**Book 8 locations:** `BOOK_MAP.md:7,378–384`; `STATE_LEDGER.md:3,13,41`; `MOVEMENT-001.md:11`; `MOVEMENT-008.md:11`.

**Edition evidence:** Book 8 points to old Book 7 “Ch20/23/24” source chapters. The edition’s current Book 7 has sixty planned chapters and is closed only through chapter 44. The callbacks cited at `BOOK_MAP.md:378–384` are planned to land in edition chapters 45–60, but their exact surviving loci cannot be known before M7–M8 close. O3 also means those references are not author reading.

**Amendment:**

- Retitle `BOOK_MAP.md:7`’s provenance as historical planning provenance, not canon: `Source chapters were used by the planner; Monroe 1.3 canon is the edition manuscript and CLOSED ledgers.`
- Replace every `B7 Ch20/23/24` and `Book 7 Ch14/15/23/24` pointer in the audited files with the final edition chapter and line after M7–M8 close.
- For `MOVEMENT-001.md:11` and `MOVEMENT-008.md:11`, keep the bullet under the O3 note but retarget it to the exact edition chapter(s) that contain the surviving seam/fourth-site material.
- If a quoted callback does not survive, delete the callback rather than attaching it to a merely similar scene.
- Current closed facts can already be retargeted: the birthday to `chapter-40.md:55,189–211`; [UNBOUND] to `chapter-42.md:269`; Oryn’s M6 debt/terms to `chapter-44.md:169–211`. Final close material remains pending.

---

## B. Findings affecting later movements

### B1. The “whole year” closing frame is impossible on the plan’s own day spine

**Grade: Affects later movement — M9**

**Book 8 locations:** `BOOK_MAP.md:87,407,410`; `MOVEMENT-009.md:34`.

**Edition evidence:** the plan opens on day 131 and closes on day 308 (`BOOK_MAP.md:19,21,88`), about 177 days. The edition does not define a short year that would make this “the whole year”; OWNER #35/#42/#48 forbid using unresolved calendar structure to repair it.

**Amendment:** in all four places, replace `the whole year` / `whole year` with `all these days`. Preserve the rest of each protected unit. Record the protected changes under OWNER #48.

### B2. “First words to the six in a year” is unsupported and conflicts with the Book 8 span

**Grade: Affects later movement — M9**

**Book 8 locations:** `BOOK_MAP.md:86`; `MOVEMENT-009.md:26`.

**Edition evidence:** Teague’s tall woman is unnamed and silent toward the five in planned Book 7/Book 8 scenes, but no edition canon establishes a one-year interval. The whole Book 8 plan is only about 177 days.

**Amendment:** replace with `The tall woman speaks to the six for the first time.` Do not add an elapsed duration.

### B3. Lira’s age-sixteen wall history is unsupported

**Grade: Affects later movement — M1 relationship ledger**

**Book 8 location:** `STATE_LEDGER.md:79`.

**Edition evidence:** the edition supports Lira’s history with the walls at the academy above Ostrand (locked B6 `manuscript/chapter-09.md:207,247`) but does not date it to age sixteen. The plan may not invent an age as a seam fact.

**Amendment:** replace `since the training hall at sixteen` with `since the walls at the academy above Ostrand`.

### B4. Brom’s advancement review is already closed

**Grade: Cosmetic / Affects later callback handling**

**Book 8 location:** `STATE_LEDGER.md:101`.

**Edition evidence:** Brom’s advancement review is closed in Book 6 (`book-06-the-compacts-hand/STATE_LEDGER.md:1269,1275`). His Book 7 state is continental Copper champion, formal Copper, with the Iron finding unsigned (`book-07-void-roads/BOOK_MAP.md:21`).

**Amendment:** delete `Brom’s advancement review` from the carried-open list. If Book 8 recalls it, label it closed history, not an open thread.

### B5. Seln’s three different spans need explicit separation

**Grade: Affects later movement — M2–M5**

**Book 8 locations:** `BOOK_MAP.md:60,63,393,447`; `MOVEMENT-002.md:30`; `MOVEMENT-003.md:27`; `STATE_LEDGER.md:17`.

**Edition evidence:** Seln served fifteen years; his locked case has been carried twelve years. The protected Book 7 line “Six years I’ve wanted a face” stays unglossed under OWNER #50; Book 7 also dates the survey at “five years ago by the stake, maybe six” (`OWNER-DECISIONS.md:159–162`; B7 `BOOK_MAP.md:21,309,314`).

**Amendment:** add to Seln’s entry row:

> `Fifteen years in service; case carried twelve years, shut and unopened; “six years” is never used as the case’s age. Book 8’s office survey abstraction may say six only as an office/survey rounding.`

Do not add a new six-year personal event.

### B6. “Forty years” is correct for Vastin; an age must never appear

**Grade: Checked with one cosmetic safeguard**

**Book 8 locations:** `STATE_LEDGER.md:20`; `MOVEMENT-002.md:43`; `BOOK_MAP.md:368,391–392,400,436`.

**Edition evidence:** OWNER #8/#17: Vastin’s career is “forty years”; age 51/53/60 is never stated (`OWNER-DECISIONS.md:15,24`).

**Amendment:** keep all `forty years` career lines. At `BOOK_MAP.md:436`, replace the meta sentence that repeats `53` with: `No numeric age for Vastin appears in plan, packet, narration or dialogue; “forty years” is career length only.` This prevents an apply seat from treating 53 as allowable metadata.

### B7. The plan’s Tide consent language must remain ask-first, not form-first

**Grade: Affects later movement — M3 and every later reading**

**Book 8 locations:** `MOVEMENT-003.md:42`; `BOOK_MAP.md:264,268,372`; `STATE_LEDGER.md:70`.

**Edition evidence:** “ask first, every time” is in Oryn’s and Cael’s hands (`chapter-44.md:157`; B7 `BOOK_MAP.md:32,286`). Oryn’s previous lack of consent is not repaired after the fact (`B7 ledger:616`).

**Amendment:** every planned reading must show or explicitly inherit an ask and an answer. Change `consent implied by the form` as in A4. Keep the protected/standing phrase `ask first, every time`; do not abbreviate it to implied consent.

### B8. “The still place,” “the Quieting,” [UNBOUND], and “the Compact” must not be re-coined

**Grade: Affects later movement; entry details PENDING B7 M7–M8**

**Book 8 locations:** `BOOK_MAP.md:22,26–27,265,335,368,384,409,425,428`; `STATE_LEDGER.md:28,31,41,45,71`; `MOVEMENT-004.md:24`; `MOVEMENT-005.md:24`; `MOVEMENT-009.md:34,37,48,61`.

**Edition evidence:**

- `the Quieting` has been said aloud and means the process that happens at quiet ground, not a place (`B7 ledger:621,646`; `chapter-41.md:169,193–197,257`).
- `[UNBOUND]` was said once as a stratum limit, not a current classification (`B7 ledger:621`; `chapter-42.md:269`).
- `the still place` is an old private log label. At M6 Cael has located the non-flowing place but has not said the label in that movement; its spoken/shared Book 7 status depends on M8 (`B7 ledger:621,638,664`).
- `the Compact` already exists as the institution; it knows quiet ground exists and what it does to Arbiters, but not that Cael’s fragments function inside (`B7 ledger:45,686`; B7 `BOOK_MAP.md:44`).

**Amendment:** add a terminology box to the Book 8 entry ledger with exactly those four definitions. After Book 7 closes, update only the still-place sharing/read-count line from surviving M8 prose. In Book 8, language such as `Not the Quiet`, `Not a fragment`, and `the same kind of made` must read as a refinement of an existing label, not as a first naming.

### B9. The deployment count and Shadow-use count need final seam fields

**Grade: PENDING B7 M7–M8 / Affects M1 onward**

**Book 8 locations:** `STATE_LEDGER.md:57–73`; `BOOK_MAP.md:22,257–270,404,409,443`; `MOVEMENT-001.md:28`.

**Edition evidence:** deployment since the Line is thirteen at closed M6; Shadow has been used exactly once and resealed (`B7 ledger:537–538,619,664`). Book 7’s planned Stair use would make Shadow exactly twice, but it is not canon yet. Book 8 plans three acquisitions, reaching thirteen; the series trajectory remains nineteen before Book 10 and twenty-two by Book 10, with the Book 9 additions deliberately open (`BOOK_MAP.md:270,443`).

**Amendment:** after Book 7 closes, write these two explicit entry lines:

> `Deployment since the Line: [exact final B7 total].`  
> `Shadow-adjacent Book 7 uses: [exact final count and loci]; sealed at entry.`

Do not infer either number from the old Book 7 plan. After every Book 8 movement, the appended state block must list that movement’s deployments and the new running total; any practice excluded from the count must be identified explicitly. Keep Book 8’s three-acquisition/thirteen-fragment close and the open Book 9 trajectory note.

### B10. The young crew member’s name instruction contradicts the approved naming state

**Grade: OWNER ITEM — needed before M9**

**Book 8 locations:** `BOOK_MAP.md:39,86,151,195,480`; `MOVEMENT-009.md:8,26`.

**Edition evidence:** Teague’s crew is deliberately unnamed in Book 7 and Book 8 planning (`B7 ledger:626`; `BOOK_MAP.md:151`; `MOVEMENT-008.md:8`). `OWNER-DECISIONS.md` contains no approved name for the young one. Saying a name once but “never writing” it still requires the author to mint a spoken name.

**Amendment:** none without owner choice. See OWNER ITEM OI-3.

### B11. Several histories and resources are correct only if Book 7’s last two movements survive

**Grade: PENDING B7 M7–M8**

This includes Lira’s final arm/ankle state and crossbow/bolt count; Brom’s final shoulder state; Karis’s 52 sheets and the Ring/Stair/Hall split; the carter’s map; the final survey kit; Pike’s nine lines; Oryn’s letter and Thornwater position; Hesk’s straightedge arrival; the completed fourth-site survey; the “season line”; Teague’s after-thaw contract; 96 marks; and the final state of the rope, mule, reserve and letters.

**Amendment:** apply only through the seam table in §H after closure.

---

## C. Exact protected-text amendments required by standing decisions

These are not OWNER ITEMS: a standing owner/coordinator decision already supplies the answer. Apply the minimal replacement and list old/new in `B7-RECONCILIATION-APPLIED.md`.

### C1. Named-season and metric protected text — OWNER #48

**Grade: BLOCKS M1 where M1 uses it; otherwise Affects later movement**

Apply the protected rows in A11, especially:

- `BOOK_MAP.md:369`: `Spring’s over` → `The thaw’s past`; `Next spring` → `After the next thaw`; Oryn’s line → current Book 7 wording.
- `BOOK_MAP.md:380`: Oryn callback → `Route’s whole. The knee held. Nobody died of three weeks. After the thaw: bring the map, and lie still when I say. — O.`
- `BOOK_MAP.md:382`: Teague callback → `After the thaw. Whatever’s on that bearing. My crew comes.`
- `BOOK_MAP.md:403`: `came for spring` → `came after the thaw`.
- `MOVEMENT-009.md:39`: both callbacks to the same current wording.

### C2. Numeric time since Kindling — OWNER #18/#48

**Grade: BLOCKS M1 for the Ch1 log; later changes affect M5/M8**

- `BOOK_MAP.md:364`: `For five years I thought the system forgot to make room for me` → `Since my Kindling I thought the system forgot to make room for me`.
- `BOOK_MAP.md:389`: `I’ve spent five years staying out of registries` → `Since my Kindling I’ve stayed out of registries`.
- `BOOK_MAP.md:400`: `I’ve spent five years learning to give ground and disappear` → `Since my Kindling I’ve learned to give ground and disappear`.
- `MOVEMENT-001.md:53`: make the same Ch1-log change.
- `BOOK_MAP.md:405` and `MOVEMENT-008.md:66`: `since I/he was fourteen` → `since my/his Kindling`.

### C3. No-Path mechanics — OWNER #49 and locked Book 6 canon

**Grade: Affects later movement — M8/M9**

- `BOOK_MAP.md:405`: `Because every other site, my Path worked while everyone’s died.` → `Because at every other site, their Arbiters stopped and my fragments still worked.`
- `BOOK_MAP.md:408`: `His Path did not die. It also did not notice it should have.` → `His Arbiter was dark before the line and after it. The fragments still answered.`
- `BOOK_MAP.md:410`: `a machine that lit for everyone but him` → `a machine whose plate lit eleven seconds late for him and then went dark`.

Do not say the machine “never lit” for Cael. Do not attach an explanation to the difference; nobody has one at Book 7’s end.

### C4. Unresolved-year language — OWNER #35/#42/#48

**Grade: Affects later movement — M9**

- `BOOK_MAP.md:407,410` and `MOVEMENT-009.md:34`: `whole year` → `all these days`.
- `BOOK_MAP.md:488`: delete the `autumn birthday (about the 467th day)` forecast and insert the no-calculation sentence from A9.

---

## D. Source-routing audit

### D1. Every packet needs the O3 note

The exact nine insertion points are A2. This is a mechanical pass and should be applied before any author receives a packet.

### D2. Book 7 pointers that must be retargeted

**Grade: BLOCKS M1 / PENDING B7 M7–M8**

| Location | Stale pointer | Required action |
|---|---|---|
| `BOOK_MAP.md:7` | Book 7 Ch23–24 as seam read | Replace with final edition B7 chapter range and CLOSED ledger M7/M8 blocks. |
| `STATE_LEDGER.md:3` | universe ledger / Book 7 Ch23–24 / source Ch1 | Make edition B7 final ledger and manuscript the authority; label source items historical planning aids. |
| `BOOK_MAP.md:378` | B7 Ch20 | Retarget the ruler line to the exact edition chapter/line if it survives. |
| `BOOK_MAP.md:379–384` | B7 Ch23–24 callbacks | Retarget each quotation independently after M8; delete any nonsurvivor. |
| `STATE_LEDGER.md:13` | B7 Ch14 birthday | Retarget to edition `chapter-40.md:55,189–211`. |
| `STATE_LEDGER.md:41` | B7 Ch15 [UNBOUND] | Retarget to edition `chapter-42.md:269`. |
| `MOVEMENT-001.md:11` | B7 source Ch23–24 | Under O3, retarget to exact final edition seam chapters, expected within ch45–60. |
| `MOVEMENT-008.md:11` | B7 source Ch23 | Under O3, retarget to the final fourth-site chapter/lines, expected within ch45–52. |

### D3. Book 8 source pointers remain reviewer-only

**Grade: Cosmetic, but binding method**

All `Source chapter-XX.md` bullets under the nine packet read lists may remain for coordinator/reviewer tooling. The O3 note makes them forbidden author reading. No packet may paraphrase the bullet as an instruction that the author open the old source.

---

## E. Assumptions the Book 8 plan makes about Books 6–7

### E1. Assumptions contradicted by closed canon

| Book 8 location | Assumption | Closed canon | Amendment |
|---|---|---|---|
| `BOOK_MAP.md:23`; `STATE_LEDGER.md:16` | Karis unranked | Ember, Iron R3 (`B7 ledger:622,670`) | Correct rank. |
| `BOOK_MAP.md:24`; `STATE_LEDGER.md:83` | Oryn owes Cael | Cael owes Oryn (`B7 ledger:617,656`) | Reverse debt and recheck final payment. |
| `STATE_LEDGER.md:30` | Cael’s Path works | He has no Path; dark Arbiter, fragments answer (`OWNER #49`) | Use exact mechanics. |
| `STATE_LEDGER.md:39` | Five know mechanism | Six, including Cael (`B7 ledger:686`) | List six. |
| `STATE_LEDGER.md:41` | Karis knows carvings command | M6 hypothesis unstated/unentered (`B7 ledger:621–622`) | Recast as hypothesis; recheck M7–M8. |
| `STATE_LEDGER.md:49`; `BOOK_MAP.md:22` | Nothing owed | Rope, Fallow hundred and HOLD slips open at M6 (`B7 ledger:678,698`) | Copy final accounts after close. |
| `STATE_LEDGER.md:66` | Shadow used only at Stair | One Ring use is already canon; Stair is later plan (`B7 ledger:538`) | Record exact final two loci/count. |
| `STATE_LEDGER.md:70`; `MOVEMENT-001.md:28` | reader cannot read self / no self use | Cael has already self-read (`B7 ledger:617,638,664`) | Self and contact; ask-first outward. |
| `STATE_LEDGER.md:79` | Lira wall fixation since age 16 | Age anchor unsupported | Use event anchor. |
| `STATE_LEDGER.md:101` | Brom review open | Closed in B6 | Delete. |

### E2. Assumptions not yet contradicted, but not canon until M7–M8 close

See §H. These must be labeled pending, not stated as settled entry canon.

---

## F. OWNER ITEMS — protected text and owner-only decisions

Only the owner can choose among these options. No replacement is authorized in this audit.

### OI-1. Karis’s protected “right for five years or wrong for five years”

**Needed by:** Movement 3  
**Location:** `BOOK_MAP.md:393`  
**Conflict:** Closed Book 7 says her relevant hypothesis is not spoken or entered and presents it as a present fear (`B7 ledger:621–622,670`; `chapter-44.md:61`). The Book 8 line may be meant to reveal an older private research conviction, but no edition page establishes a five-year version of this hypothesis. The line is protected, and there is no standing decision authorizing a replacement.

**Options:**

1. Canonize a separate five-year private research conviction and add one clear plan sentence distinguishing it from the Book 7 quiet-ground hypothesis.
2. Release the clause for event-anchored recomposition, without a numeric duration.
3. Keep it as Karis’s emotional rounding and mark the surrounding narration so it is not a ledger fact.

### OI-2. Protected “it took four years and a hearing to walk out”

**Needed by:** Movement 4  
**Location:** `BOOK_MAP.md:396`  
**Conflict:** The plan itself admits the figure does not fit the locked academy span (`BOOK_MAP.md:437`). Standing #18 bars numeric time since Kindling, but this protected sentence is framed as a city/academy exit duration and therefore needs an explicit owner choice rather than an inferred rewrite.

**Options:**

1. Keep it as Cael’s rough spoken exaggeration and do not repeat it as fact.
2. Release only `four years` for event-anchored wording.
3. Alter the underlying timeline to support it, with a series-calendar pass.

### OI-3. The young member of Teague’s crew is named aloud once

**Needed by:** Movement 9  
**Locations:** `BOOK_MAP.md:39,86,151,195,480`; `MOVEMENT-009.md:8,26`  
**Conflict:** the role is intentionally unnamed and no name is owner-approved. “Said once but never written” still mints a spoken/audiobook name.

**Options:**

1. Keep the role unnamed even at death; the broad man’s cry is not lexically rendered.
2. Owner approves a name before M9; add it to the name registry and pronunciation list before drafting.
3. Preserve the fact that a name was spoken in-world but narrate only the reaction, never the name’s sound.

### OI-4. “Tell Lira’s family I said so” still has no setup

**Needed by:** Movement 9  
**Location:** `BOOK_MAP.md:409`; acknowledged at `:446`  
**Evidence:** OWNER #25 keeps the line verbatim but asks the owner to confirm intent (`OWNER-DECISIONS.md:32`). Nothing in Book 8’s plan creates the referent.

**Options:**

1. Confirm the opaque line as intentional; add no setup.
2. Authorize one earlier setup beat with Lira/Hesk/family.
3. Release or remove the clause.

---

## G. Checked and presently consistent

The following were checked and do not presently require a continuity amendment, except where the final Book 7 seam is expressly pending:

- Cael is nineteen from day 102 past the Line, and Book 8 gives him no birthday. The season tag beside the old citation must be removed, but the age is correct (`B7 ledger:620,664`; `chapter-40.md:55,189–211`).
- Vastin’s career is forty years and his age is never stated. Book 8’s operational packets respect that; only the meta discussion should stop repeating “53” (`OWNER #8/#17`).
- Daeva receives no age or career-length statement in the Book 8 plan. Her exceptional age-thirteen Kindling under OWNER #16 is not reopened; the rematch is only a carried promise.
- Pike has one arm and has kept the ledger thirty years (`B7 chapter-02.md:151,161`; `chapter-42.md:327`).
- Seln is Shadow, Bronze, fifteen years in service; his case is shut and was never opened in closed Book 7. OWNER #50’s protected six-year line remains a separate, unglossed item.
- Karis is Ember, Iron Rank Three. Her three field boxes and the Ring’s eleven sheets are canon by M6; the final 52-sheet split is pending M7–M8 (`B7 ledger:622,645,670`).
- Lira’s ankle is taped and never mended in Book 7 through M6; she uses the crossbow one-armed and cannot span it (`B7 ledger:651,666`; `chapter-43.md:115–159`).
- Brom is continental Copper champion, formal Copper, and his hand is whole by M6. His final shoulder state remains a seam check.
- Oryn is Tide, Iron Rank Four; sources were told by Path, not by person; she does not know Seln is Shadow’s source; she left the mule with the crew and took one pannier plus the thirty-foot spare rope (`B7 ledger:616,624,653,674`).
- Teague’s crew remains four practitioners plus an older healer of no Path, all unnamed except Teague. Teague is about forty, which Book 7 already supports; this is not Vastin’s forbidden age issue.
- Reydan’s `find me later`, Daeva’s rematch, Ephram’s letter, Hesk’s missing/expected parcel and Vell’s `The session still stands` can remain as open callbacks. Exact delivered-letter state must be copied from the final B7 ledger.
- The sealed reserve under five thumbprints exists and must carry unless final Book 7 prose spends it (`B7 chapter-15.md:153`; `chapter-27.md:13`; OWNER #23).
- `the Quieting` as process, `[UNBOUND]` as a one-time historical limit, and the Compact’s limited knowledge are compatible with Book 8’s intended reveal schedule once the terminology box in B8 is corrected.
- The Book 8 acquisitions Iron Wall, Rune and Force are new Book 8 events, not retroactive Book 7 canon. Ending on thirteen fragments is arithmetically sound. The trajectory note toward nineteen and twenty-two leaves Book 9’s additions open as it should (`BOOK_MAP.md:270,443`).
- The Book 8 reveal that the Fractured Path predates classification is compatible with `universe/CANON_RULES.md`, provided Book 8 does not explain why Cael functions inside quiet ground or expose Book 9’s infrastructure truth.
- The remaining duration statements were checked individually: the office’s six-year survey abstraction (`BOOK_MAP.md:60`; `MOVEMENT-002.md:30`) may remain when labeled as an office record; Vastin’s forty-year career may remain; Cleon’s thirty years and decade (`BOOK_MAP.md:398–399`) are new Book 8 personal history with no B6/B7 contradiction; `years` without a number for buried iron (`BOOK_MAP.md:83`; `MOVEMENT-008.md:31`) may remain; and Oryn’s future `a month`/`a year` healing estimate (`BOOK_MAP.md:390`) uses allowed generic units and does not calculate the unresolved series calendar. Karis’s five-year claim and the protected four-year hearing line are separated as OI-1/OI-2.
- Generic `season` and `month` are legal under O4. Literal water springs and the physical verb/noun `fall` are legal. No English weekday name or named calendar month occurs in the audited plan.
- The protected line `Tell Lira’s family I said so` is correctly recognized by the plan as OWNER #25; it remains OI-4 rather than a continuity rewrite.
- `The session still stands` matches the edition wording (`B7 chapter-27.md:57`).
- The Compact may know which crew walks out declaring, but not that Cael’s fragments work inside; Book 8’s M8 restriction at `MOVEMENT-008.md:54` is correct.
- The final court/still-place answer may deepen the anomaly to `the same kind of made`, but it does not resolve it, count it as a fragment, equate it with the Quieting, or supply a next-fit design. That limit is consistent with the universe reserved truths.

---

## H. Re-run after Book 7 M7–M8 close (required)

Run this section against the CLOSED M7 and M8 ledger blocks **and** the surviving chapters 45–60. The Book 7 plan is not evidence for a pass.

| Re-verify | Current Book 8 forecast | Required final evidence/action |
|---|---|---|
| Final day and opening instant | Day 131, morning after last ferry (`BOOK_MAP.md:19`; M1 `:17`) | Confirm final B7 last scene/day/weather and whether B8 opens the same morning. Shift B8 relative dates if required. |
| Snow/ferry sequence | first snow day129; ferry130; letter131 | Cite exact final chapters; do not infer from B7 map. |
| Cael inventory | ten fragments; still place read three times; untouched | Confirm count, exact number of self-readings, who knows the label, and last touch/order. |
| Oryn debt | B8 assumes reading complete/“owes Cael” | Copy final paid/owed state and direction. Confirm ask-first use and whether Teague non-reading pays a term. |
| Still-place vocabulary | `Not the Quiet. Not a fragment. Older than the log. Observation continues.` | Verify exact surviving wording, who heard it, and whether “the still place” was said aloud. |
| Quieting / [UNBOUND] / Compact | current M6 definitions | Confirm M7–M8 introduce no new public meaning or Compact knowledge. |
| Deployment count | M6 baseline thirteen | Enter exact B7-final total and cite deployments. |
| Shadow | M6 exactly once; plan predicts second at Stair | Confirm exact final count and loci, then state sealed at B8 entry. |
| Iron / Storm / Anchor / Tide rules | M6 numeric rules in A7 | Confirm no M7–M8 refinement; carry any new bill exactly. |
| Cash | B8 forecast 96 | Copy final cash arithmetic. Keep sealed reserve separate from living purse. |
| Pike ledger | B8 forecast nine completed lines, no number, five names eleventh | Confirm exact lines, wall order, season-line wording, HOLD slips and Stair price. |
| Objects | 52 sheets; kit; map; two straightedges; one bolt; mule; three boxes; case | Confirm each count/location/holder, including carter’s map, Ring/Stair/Hall split, bolt count, stake number, and whether Hesk’s straightedge arrived. |
| Debts | `nothing owed` forecast | Confirm ferryman rope, Fallow hundred, Stair three hundred, both HOLD slips, board/inn accounts. Do not conflate “taken; not paid” with a debt the crew promises to settle. |
| Reserve | sealed under five thumbprints | Confirm unopened/unspent and its box/location. |
| Oryn route | forecast Thornwater; letter received; mule with crew | Confirm final location, lateness, letter wording, mule holder and spare rope. |
| Teague | after-thaw term; crew stays; axe-head fence | Confirm exact current callback and contract. Crew must remain unnamed unless owner rules OI-3. |
| Lira | sling/order, ankle unmended, Oryn’s crossbow, one bolt | Confirm exact final body and equipment state. |
| Brom | shoulder bound/forward; kit/middle box | Confirm final injury and carried objects. |
| Karis | 52 sheets; map; kit ledger; command hypothesis; voice | Confirm sheet split, voice, hypothesis status and exactly what the Hall establishes. Do not promote an inference. |
| Seln | case unopened; six-year protected line; Stair shadow work | Confirm case never opens, final holder, exact Shadow use, and no invented six-year case age. |
| Hesk/Vell/Vastin | letters/parcel; `session still stands`; Vastin silence | Confirm sent/received/answered status and exact carried letters. Vastin remains age-free. |
| Mechanism knowers | six | Confirm no seventh person learns it in M7–M8. |
| Fourth site | about 440 yards radius, iron cordon, not entered | Confirm radius, stake number/count, location, central shape, effect knowledge and terminology. |
| Source pointers | old B7 Ch20/23/24 | Retarget every pointer in D2 to final edition chapter:line. |
| Book 7 quotations | ruler, pattern, line, letters, Teague, Pike, still-place inventory | Compare word for word to current prose. Replace the old quotes, not the current prose. |
| Calendar | day131 seam and all Book 8 day numbers | Confirm no cross-book birthday/count-back claim is introduced. Keep season-blind policy. |
| Book 8 opening release | all above | Add a CLOSED re-run note with pass/fail and the final ordered amendments actually applied. |

---

## I. Proposed final ordered amendment list

This is the apply order. Items that depend on Book 7 closure must wait where marked.

1. **Insert O3 no-source notes** above all nine packet `Read before drafting` lines (A2).
2. **Mark the Book 7 seam provisional** in Book 8 map, ledger and M1 packet; do not release M1 yet (A1).
3. **Apply standing season/unit normalization everywhere**, including protected text, from A11; preserve generic `season`/`month`, literal springs and physical fall.
4. **Apply standing calendar/Kindling wording changes** from A9, A10 and C2/C4; remove the Book 9 autumn/day-467 birthday forecast.
5. **Correct fixed closed-M6 canon now:** Karis Iron R3; six mechanism knowers; Cael no Path; Oryn-debt direction; Tide self/contact; ask-first consent; Lira age anchor; Brom review closed (A3–A7, B3–B4, B7).
6. **Expand the capability ledger** with Iron, Storm, Anchor, Shadow and Tide’s exact rules and numeric bills; add final deployment/Shadow fields (A7, B9).
7. **Add current money/object safeguards:** sealed reserve; open M6 debts; shut case; mule and spare-rope provenance (A8).
8. **Add the four-term vocabulary box** for the still place, Quieting, [UNBOUND] and Compact knowledge (B8).
9. **Apply standing protected-text repairs** for Cael’s no-Path mechanics and plate history (C3).
10. **Retarget already-closed citations** (birthday, [UNBOUND], debt) and convert provenance language so old source chapters are historical planning aids only (A12/D2).
11. **Place OWNER ITEMS OI-1–OI-4** in the owner queue with their movement deadlines. Do not improvise replacements.
12. **Wait for Book 7 M7–M8 to close.** Then execute every check in §H against CLOSED ledger blocks and surviving prose.
13. **Replace the entire detailed Book 8 entry seam**—dates, bodies, knowledge, inventory, money, debts, objects, letters, Pike board, fragment/deployment counts—from final Book 7 canon. Remove the pending warnings only after this pass.
14. **Retarget all final Book 7 callback citations** and compare every quoted line word for word, especially Oryn, Teague, Pike, Karis and the still-place inventory.
15. **Run zero-hit checks** for named seasons used temporally and for metric units across the audited Book 8 files. Manually exempt literal water springs and physical `fall`; generic `season` and `month` should remain.
16. **Run focused canon checks** for `his Path|my Path|nothing owed|unranked by choice|owes Cael|reader cannot read the reader|five years|whole year|in a year|age 53|day 467|chapter-23|chapter-24|400 m|1,012 m|metre|meter` and resolve every hit by this report or an owner item.
17. **Write `state/B7-RECONCILIATION-APPLIED.md`** listing each applied amendment, each protected old/new pair, final evidence citations, owner items left open, and the M7–M8 re-run verdict.

## Release decision

**No: Book 8 Movement 1 cannot be released today.** Book 7 is not locked, and the Book 8 entry seam depends materially on its unfinished Movements 7–8.

**Yes: Movement 1 can be released once Book 7 is locked, the ordered list above is applied, and the §H re-run passes.** The open owner items do not all block M1: OI-1 is needed by M3, OI-2 by M4, and OI-3/OI-4 by M9. No unresolved owner choice prevents M1 after the canon/mechanical repairs and final seam reconciliation are complete.
