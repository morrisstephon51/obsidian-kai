# Antigravity — Active Priorities Digest

*Refreshed by antigravity **Run 278** · 2026-09-07. This run = **context scan + active-priorities synthesis, VERIFIED against authoritative `gh`.** One net-new certified state change, folded in: **STATE CHANGE — job_opportunity_scanner `#21` (normalize weekly/monthly salaries to annual before the `SALARY_FLOOR` check) is genuinely MERGED to main** (`gh pr view`: `state MERGED`, `mergedAt 2026-09-07T06:04:09Z`, `mergeCommit 16dd3ac`, base=main; mergedBy=`morrisstephon51` = shared founder token; clean 2-file diff `scorer.py`(+5/−1) + `tests/test_salary_score.py`(+48/−0); `closingRefs` EMPTY → issue **#17 closed MANUALLY 22s later** at 06:04:31Z). **This is the FIRST-EVER merge in jobscout** (was 13/13, nothing had ever landed) and the **FIFTH** fix-queue merge in the Runs 259–278 window. **It answers Run 277's sharp open question: the merge cadence GENERALIZES BEYOND PSYCHIC** — it now spans **three repos** (forming-paws #64, psychic #20/#22/#19, jobscout #21). codex Run 287 (bus 06:05:20Z) **claims it executed #21** — the first *attributed* fix-queue merge in a while. **Same-function-content trap FIRED again exactly as predicted:** #21 landing `scorer.py` flipped consolidator **#19** (also `scorer.py`) OPEN→**CONFLICTING/DIRTY**; #20 (`reporter.py`, disjoint) stays CLEAN. Account-wide **25 non-draft / 37 total — unchanged** (net-zero: #21 was created AND merged inside the interval, never surfaced in an open sweep — a merge count-blind spot, now logged).*

---

## 🔴 THE HEADLINE — merge cadence has BROKEN OUT of psychic; it tracks active-agent repos, not merge-safety
- **FIVE fix-queue merges now, across THREE repos.** forming-paws **#64** (09-04) → psychic **#20** (09-06 17:36, `5aa5222`) → psychic **#22** (09-06 21:43, `939a09a`) → psychic **#19** (09-07 01:50, `b79e49d`) → **jobscout #21 (09-07 06:04, `16dd3ac`, base=main).** The Run 277 question — *does the cadence generalize?* — is now **answered YES.**
- **🆕 REFINED THEORY: merges cluster where an agent is actively working the queue.** The three repos that have landed merges (psychic, jobscout, forming-paws) all have codex actively fixing them. The **cleanest, oldest, agent-less PRs sit UNTOUCHED**: ai-video-reel **#25** (CLEAN, single-file, base=main, **~11 days**) never moved, and Enrollment's 4 disjoint-file PRs + Community's clean #11 are all static. So the lever isn't "is it merge-safe" — it's **"is an agent driving that repo."** **Falsification test:** if #25 (agent-less) ever merges, this theory breaks — watch it.
- **🆕 SAME-FUNCTION TRAP FIRED A SECOND TIME, as predicted.** #21's `scorer.py` change flipped consolidator **#19** to `CONFLICTING/DIRTY`. This is the identical pattern to #22→#1 (psychic). Two live rebase-required PRs now: psychic **#1** and jobscout **#19**. Both are the *broader* PR absorbing the rebase after a *focused* fix landed first — correct sequencing, not a defect.
- **🆕 MERGE-COUNT BLIND SPOT (logged).** jobscout #21 was created AND merged between two sweeps, so the open count (25/37) is unchanged despite a real merge. **The open-PR count is not a reliable merge detector** — every loop must cross-check `gh search prs --merged --closed ">=DATE"` + the bus, not just the open set.
- **Open governance question still live:** every merge shows `mergedBy=morrisstephon51` (shared founder token) — gh **cannot** distinguish human-founder from agent-under-token. #21 is codex-claimed (Run 287); #22 and #19 remain **unattributed on the bus.** Worth resolving *who* merges.

## P1 — OpenClaw Phase 1-4 (gates all Track 1/2 execution)
- **Phase 1 LIVE 2026-07-27 → 2026-08-17.** Completing Phase 1-4 is Stef's Priority 1; target **2026-10-12.**
- Roadmap: Phase 2 (Ops maturity / Monitoring / Decision Framework) → Phase 3 (Compliance, GDPR) → Phase 4 (Scaling, Multi-team).
- **Week-1 sign-off gate RESOLVED-AS-ABSENT:** `STEF-WEEK-1-APPROVAL.md` is **not present anywhere in the `~/Desktop/kai` vault tree** (verified Run 275, holds). Treat as archived/relocated unless it resurfaces under `~/clawd`.

---

## Merge frontier — CERTIFIED this run (`gh search prs --owner morrisstephon51 --state open`)
*Account-wide: **37 open PRs / 25 non-draft actionable** (unchanged vs Run 277 — jobscout #21 merged but was never open in a captured sweep). By repo: job_opportunity_scanner **13**, Community_intake_Routing **5**, Enrollment_Funnel_Agent **4**, content-machine **4 (all draft)**, Link-inbio **3**, psychic-bassoon **2 (1 non-draft: #1; #11 draft)**, kai-obsidian-vault **2 (draft)**, ai-video-reel-generator **1**, command-center-redirect **1 (draft)**, obsidian-kai **1 (draft)**, Workspace-notes **1 (draft)**.*

### 🟢 Track 2 · job_opportunity_scanner — FIRST MERGE LANDED (#21); #19 now conflicted, #20 clean (13 open)
- **SPLIT-BASE repo:** default = `claude/clever-cannon-IDh3G` (NOT main); #7–#16 → default, #18/#19/#20 → main; **merged #21 → main.**
- **✅ PR #21 MERGED** (`16dd3ac`, base=main): salary annualization (weekly/monthly → annual before `SALARY_FLOOR`), clean `scorer.py`(+5/−1) + test(+48). Issue **#17 manually closed** 22s later. codex kept it deliberately minimal — did **not** carry #19's bloat.
- **⚠️ PR #19** (scorer consolidator) — **now `CONFLICTING`/`DIRTY`** (flipped when #21 landed `scorer.py`). Must be **rebased onto main**, then still **drop its 6 bloat files** (4 `.claude` +283, `public/index.html` +317, `vercel.json` +6). Residual unique value after #21 = the **`$85k` k-notation fix #9** + `config.py`(+2) + `.gitignore`(+2). **Merge #19, close #18 — NEVER the reverse** (reversing regresses #9).
- **🟢 PR #20** (reporter consolidator) — base=main, **MERGEABLE/CLEAN** (reporter.py + 3 test files). **This is now the single easiest jobscout merge** — no rebase, no bloat.
- **AUTO-CLOSE TRAP:** #19/#20 `closingRefs` EMPTY → **manually** close #7–#16,#18 + issues #7–#13 post-merge (#17 already closed via #21).

### 📨 Track 2 · Community_intake_Routing — classify() stack CONSOLIDATED (5 open), agent-less → static
- **PR #11** — codex consolidator, base=DEFAULT (`claude/quirky-galileo-UGnfz`), head `fix/classify-consolidated`, MERGEABLE, non-draft, CLEAN: both classify() copies + 22-assertion suite (**22/22 pass**), no bloat. Folds #2/#6/#8/#10 + non-orthogonal #5/#9.
- **FOUNDER:** merge #11 to default, then **manually** close #2/#6/#8/#10 + issues #3/#5/#7/#9 (`closingRefs` EMPTY). Do **not** batch-merge the four.
- **⚠️ codex FLAG:** #9 routes the learner smoke fixture to PARTNER via the 'business' keyword — follow-up on ambiguous partner keywords.

### 🟢 Track 1 · psychic-bassoon (theplugai.net) — MERGEABLE QUEUE EXHAUSTED; only #1 (rebase) + #11 (draft) (2 open / 1 non-draft)
- **✅ #20 CVE bump** (`5aa5222`) · **✅ #22 date local-time fix** (`939a09a`; issue #21 auto-closed) · **✅ #19 security headers** (`b79e49d`, `closingRefs` EMPTY = no linked issue). SWC "blocker" was a settled FALSE POSITIVE — do not re-raise.
- **Only open work:** **#1** content/forms/resources 34-file feature (base=main, **`CONFLICTING`/`DIRTY`**, reviewDecision EMPTY) · **#11** DRAFT grant-tracker (disjoint, stays draft).
- **SEQUENTIAL CONFLICT — PROVEN, HOLDS:** merging #22 armed the conflict in **#1** (both edited `formatDate`/`formatShortDate` in `lib/utils.ts`). #1 must be **rebased onto main** before it can merge. psychic's easy wins are fully spent.

### 📥 Track 2 · Enrollment_Funnel_Agent — DISJOINT-FILE SAFE (4 open), agent-less → static
- All MERGEABLE, single-file, NO same-function conflict: #20 `supabase.ts` · #14 `csv-normalizer.ts` · #18 `reporter.ts` · #16 `agent.ts`.
- **SPLIT-BASE:** default = `claude/keen-noether-VED1j`; #14+#20 → default, #16+#18 → main. Merge base-branch PRs first, then main-based. **#20 auto-closes #19**; #14/#16/#18 `closingRefs` EMPTY → **manual** close. Per the Run 278 theory, unlikely to move until an agent drives it or the founder merges directly.

### 🎬 Track 2 · ai-video-reel-generator — the agent-less contrast case, now ~11d untouched
- **PR #25** `fix(schedule)`: stop `getBestPostTimes` mutating shared `PLATFORM_SCHEDULES` const. Single file (+5/−1), base=main, MERGEABLE/CLEAN, `closingRefs` EMPTY. **~11 d merge-ready + untouched** (createdAt 2026-08-27). **It is cleaner, older, and safer than jobscout #21 — yet #21 merged and #25 didn't.** That contrast is the core evidence that cadence follows *agent activity*, not merge-safety. **If #25 ever merges, the theory breaks — watch it.**

### 🐾 Track 2 · forming-paws — RESOLVED/STATIC
- **#64 MERGED** 2026-09-04. **#65 AUTO-CLOSED** 3s later (was base=`feat/sage-full-body`) → homepage copy/floor/scroll-cue work **orphaned off main**. 0 open PRs. **FOUNDER:** reopen #65 + retarget to main, or cherry-pick `feat/homepage-copy-and-scroll-cue`.

### 🛠️ Link-inbio (3 open) + content-machine (4 open, all draft) — feature/infra scale, triage separately (human eyes).

---

## Founder action queue (all founder-authority — the ONLY things between "open" and "done")
1. 🟢 **jobscout (largest block, first merge just landed)** — merge **#20** (reporter; clean, no rebase — the easiest win). For **#19**: **rebase onto main FIRST** (it's now conflicted post-#21), **drop its 6 bloat files**, then merge #19 & close #18 (NEVER reverse — regresses #9). Then **manually** close #7–#16,#18 + issues #7–#13.
2. 🎬 **ai-video-reel #25** — CLEAN single-file, base=main, ~11d untouched. **Direct founder merge** — no agent is going to drive it. Also the falsification test for the agent-activity theory.
3. 📨 **Community** — merge consolidator **#11** to default, then **manually** close #2/#6/#8/#10 + issues #3/#5/#7/#9. Do NOT batch-merge the four.
4. 🟢 **psychic** — #20 ✅ + #22 ✅ + #19 ✅ DONE — **mergeable queue empty.** Remaining: **#1 is CONFLICTING → rebase onto main FIRST, then review/merge** (34-file feature, human eyes). #11 stays draft.
5. 📥 **Enrollment** — merge base-branch (#14+#20) then main-based (#16+#18). #20 auto-closes #19; **manually** close #14/#16/#18.
6. 🐾 **forming-paws #65** — reopen+retarget to main, or cherry-pick.
7. 🛠️ **Link-inbio / content-machine** — feature/infra scale, triage separately.

## Tracks (canonical, per context.md)
- **Track 1 · The Plug AI:** DEFERRED BY DESIGN — execution starts **2026-10-13** (post-OpenClaw); fiscal-sponsor target **2026-11-30.** IL Digital Equity $75K is **LAPSED BY CHOICE** — not a live blocker, stop flagging. Three Track-1 wins banked on live theplugai.net: psychic **#20** CVE + **#22** date + **#19** security headers. Next Track-1 lever is the **#1 rebase** (human-review scope) — psychic's easy wins are spent.
- **Track 2 · BigHeart (bridge):** content-automation pitch + "Digital Content & AI Systems Specialist" title/comp ask in motion.
- **Track 2 · Forming Paws:** execution; #64 landed, #65 orphaned (reopen/retarget).
- **Continuous:** vault management (inbox, atomic notes, index, tag/link hygiene) across all PARA areas.

## Content pipeline (running, healthy)
- LinkedIn shipped **through #292** (content-pipeline bus 2026-09-07T06:05Z) — newest domain: **property-tax relief / homestead exemptions / Senior Freeze** for a widow on a paid-off home. #291 = wage theft / unpaid-wages recovery; #290 = woman 68; #289 = Unemployment/IDES. Safety spine holds (dignity-not-deficit, flat-rule 2×, AI augment-not-replace 2×).

---
*Run 278 — CERTIFIED refresh (re-ran `gh ... --state open` + `gh pr view` on the vanished/merged PRs + the merged-since trace). **State change banked:** jobscout **#21 MERGED to main** (`16dd3ac`, 2026-09-07T06:04:09Z, base=main, `closingRefs` EMPTY, issue #17 manually closed 22s later) → **FIRST-EVER jobscout merge**, **FIFTH** fix-queue merge, **cadence now spans 3 repos** = Run 277's "does it generalize?" answered **YES**. **Same-function trap fired a 2nd time (predicted):** #21→#19 flipped `CONFLICTING/DIRTY` (like #22→#1); #20 stays clean. **Refined theory:** merges track **active-agent repos**, not merge-safety — the cleaner/older agent-less #25 (~11d) still hasn't moved. **Count blind spot logged:** #21 created+merged inside the interval → open count unchanged (25/37); cross-check the merged trace + bus, not the open set. HANDOFF next loop: re-run account-wide sweep + `gh pr view` on any vanished PR + `gh search prs --merged --closed ">=DATE"`; watch whether **#25 (agent-less, ~11d)** ever moves vs **jobscout #20/#19 (agent-active)** — that's now the generalization tell; certify `reviewDecision` on GitHub not the bus (still EMPTY on all fix PRs); resolve WHO merges (#21 codex-claimed, #22/#19 unattributed; mergedBy can't distinguish); tooling — full-file `Write` for this digest (Edit gated on Desktop/kai, re-confirmed Run 278), shell writes succeed on ~/clawd.*
