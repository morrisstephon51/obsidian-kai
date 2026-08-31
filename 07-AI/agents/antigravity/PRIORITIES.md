# Antigravity — Active Priorities Digest

*Refreshed by antigravity **Run 236** · 2026-08-31 (~04:23Z UTC). This run: re-scanned context, polled the bus (clawd / codex / content-pipeline #251 loop-start + loop-end — none directed at antigravity), **re-measured the sole cold P1 gate** (`stat` → still `**Status:** APPROVAL REQUESTED`, 3125 b frozen, mtime `2026-08-11T09:31:48Z` → now **~19.8 days cold**), and **re-ran the account-wide `gh search prs --owner morrisstephon51 --state open` sweep + `--merged --closed ">=2026-08-30"` merge check** (verify-don't-trust-the-bus). **HEADLINE: STABILITY — no new merge event since Run 235's drift.** The merged-PR check returns only the 4 already-caught landings (mundi-agent-dashboard #7+#8 @ 22:26:5xZ, psychic-bassoon #23 @ 06:04Z, kai-obsidian-vault #1 @ 05:58Z) — nothing new since the Run 235 sweep. **mundi-agent-dashboard has now correctly DROPPED OUT of the open sweep** (both its PRs merged) → infra cluster confirmed cleared. Account-wide count **unchanged: 30 open / 12 drafts → 18 non-draft across 11 repos.** psychic #20 live-re-verified OPEN/MERGEABLE/CLEAN/base main. Coldness: jobscout ~44.0 d · enroll ~44.0 d · psychic PRs ~16.6 d · avrg ~17.0 d · -Community_intake ~22.0 d · forming-paws ~8.0 d · gate ~19.8 d.*

---

## 🔴 THE ONE THING — sole open P1 is the FOUNDER signature (now ~19.8 days cold)
- `~/clawd/AI-Organization/STEF-WEEK-1-APPROVAL.md` **still reads `**Status:** APPROVAL REQUESTED`** — mtime **2026-08-11T09:31:48Z**, re-verified on disk this run → **~19.8 days cold** (byte-for-byte unmoved since Aug 11, 3125 bytes).
- The report is **✅ Week-1 PASS** (12 tasks, 3.34× avg speedup, zero escalations, 8.6/10 confidence, 100% cost tracked) and recommends **APPROVE → proceed to Phase-2 Week-2**. Everything is agent/supervisor-signed; **only Stef's written checkmark is missing.**
- **The gate is aging, not thawing.** No agent can click it. One-line written approval (email, or set the in-file status line to ✅) closes it.

## P1 — OpenClaw Phase 1-4 (gates all Track 1/2 execution)
- **Phase 1 LIVE 2026-07-27 → 2026-08-17.** Completing Phase 1-4 is Stef's Priority 1; target **2026-10-12.**
- Phase-2 Week-1 sign-off is **DONE agent-side.** Sole open item = the founder gate above.
- **ADR-008 (ACCEPTED):** Claude Sonnet 4.6 is the **PERMANENT code-gen default** — a failed Claude call FAILS the task (no silent downgrade). Not conditional on OpenAI funding.

---

## Merge frontier — source-verified live via account-wide sweep, Run 236
*Account-wide: **30 open PRs / 12 drafts → 18 non-draft actionable** + **1 cold governance gate** + open issues. Net: **0 agent-actionable code blockers.** Every lever is founder-authority. **Product frontier 17/5** + **infra remnant 1/2** (only Link-inbio #15 left; mundi cluster CLEARED and dropped from the sweep). Sweep spans 11 repos (4 draft-only vault/content repos). States below confirmed live this run via `gh search prs` + `gh pr view`.*

### 🟢 Track 2 · job_opportunity_scanner — 10-PR scorer batch, EMPIRICALLY batch-mergeable
- **PRs #7–#16 — all 10 OPEN, non-draft** (re-confirmed 10 open this run), base default `claude/clever-cannon-IDh3G`.
- codex Run 236 **actually merged all ten into `clever-cannon` → 0 conflicts, 9/9 tests pass**; Run 239 re-confirmed 10/10 CLEAN + 58 pytest green. Batch-merge #7–#16 → clever-cannon → main, **any order, no rebases.**
- **Last merge still #6 (2026-07-18) → ~44.0 days cold; zero of #7–#16 landed.** Coverage: token-boundary location/title scoring, `$85k` salary parse, "trainer" title signal, recency-window filters, config-driven salary floor, loud-fail on count mismatch, KeyError-safe alerts.

### 🟢 Track 1 · psychic-bassoon (theplugai.net) — `main` hardened; 4 mergeable PRs open + 1 draft
- **PR #20** 🔒 bump Next.js 14.2.5 → 14.2.35 — closes published CVEs (incl. CVE-2025-29927 middleware-auth-bypass class). MERGEABLE/CLEAN/base main (live-re-verified Run 236). **Highest-value single click on the whole queue** (a live published-CVE patch, ~16.6 d unmerged).
- **PR #22** 🗓️ render date-only strings in local time — **closes issue #21** (Central-Time off-by-one). MERGEABLE/CLEAN, test fails-on-bug/passes-on-fix. **Merging #22 auto-closes #21.** codex Run 242 added `lib/utils.test.ts` (TZ-pinned, 4/4 pass).
- **PR #19** 🔒 baseline security response headers site-wide. MERGEABLE/CLEAN (codex Run 243 resolved the `next.config.js` conflict — kept both `rewrites()` + `headers()`). Disjoint, any order.
- **PR #1** real content / working forms / resource detail pages. MERGEABLE/CLEAN **against current main** — ⚠️ **still conflicts with #22 on `lib/utils.ts` AFTER #22 lands: #22 fixes `formatShortDate`+`formatDate`, #1 deletes `formatShortDate`. Merge #1 LAST with 1 manual resolve — keep #1's deletion (dead code, 0 callers), keep #22's fix.** Forms need Formspree env on Vercel; `.env.example` add/add hazard with draft #11.
- **PR #11** Grant Matching Tracker — founder-authored **DRAFT**, needs Supabase + 8 Vercel env vars. Founder-owned WIP (NOT in action frontier).
- **Note:** repo's most-recent merge is **#23 (scroll-driven home, 2026-08-30T06:04Z)** — the 4 actionable PRs above stay unmerged ~16.6 d.
- **Suggested merge order: #20 (CVE) → #22 (date fix, auto-closes #21) → #19 (headers) → #1 (last, 1 manual resolve).**

### 🎬 Track 2 · ai-video-reel-generator (avrg) — 1 mergeable PR open
- **PR #25** `fix(schedule)`: stop `getBestPostTimes` from mutating the shared `PLATFORM_SCHEDULES` constant — single file (+5/−1), base `main`, MERGEABLE/CLEAN non-draft (codex Run 237). **~17.0 d cold** (last merge #24, 2026-08-14).
- **Issue #5** — Supabase project to run the content-automation loop. **PR#4 (the loop) already MERGED**, so #5 is a runtime env/provisioning item, **not a pending-merge blocker.**

### 📥 Track 2 · Enrollment_Funnel_Agent — 1 mergeable PR open
- **PR #14** `fix(csv)`: platform CSVs mis-routed by substring collisions (ig/tt/fb/yt) — single file (+18/−6), base default `claude/keen-noether-VED1j`, MERGEABLE/CLEAN non-draft (codex Run 238).
- **Last merge #13 (2026-07-18) → ~44.0 days cold** — tied with jobscout for coldest PR repo. **0 open issues.**

### 📨 Track 2 · -Community_intake_Routing — 1 mergeable PR open
- **PR #2** `fix(classify)`: intake keywords matched as bare substrings misroute learners (fund/invest/serve/teach) — `api/intake.js` + `intake.js` (+31/−7), base default `claude/quirky-galileo-UGnfz`, MERGEABLE/CLEAN non-draft. **Same substring-collision defect class as jobscout #7/#8 and Enrollment #14.**
- **Last merge #1 (2026-08-09) → ~22.0 days cold. 0 open issues.**

### 🛠️ INFRA/TOOLING remnant — 1 non-draft PR left (MUNDI-governed, OUTSIDE the product queue)
*mundi-agent-dashboard cluster CLEARED — both #7+#8 merged 2026-08-30T22:26Z and the repo has now dropped out of the open sweep entirely (Run 236 confirms 0 open there). ⚠️ **#8 widened CORS on `/api/agents` and merged despite the review-before-merge flag — surfaced retroactively to founder as a security-surface change that already landed (verify origin scope is acceptable).** Only the Link-inbio rebuild remains.*
- **Link-inbio #15** — "Rebuild Command Center as a live scroll-driven dashboard" (+2288/−541, opened 2026-08-30 08:26Z). ⚠️ **Large rebuild — likely wants human eyes before merge.** (Link-inbio also has 2 open drafts: #6 resume PDF, #5 Obsidian ops vault.)

### 🐾 Track 2 · forming-paws (Puppy Power) — caught up, 0 open PRs
- **0 open PRs** (not surfaced in this run's sweep). Founder merged the visual-refresh epic through **#62** (Aug 23, ~8.0 d ago) — real signal the founder is active, just not on the items above.
- **Sole open issue #8** — IL articles of incorporation + bylaws **drafted**; filing is **founder-only** (IL Secretary of State). Track until Stef files or defers.

### 🗂️ Draft-only repos (tracked, NOT actionable — all drafts/WIP)
*The account-wide sweep surfaces 4 draft-only vault/content/tooling repos — no merge action, logged so they don't silently rot: **content-machine** (4 open / 4 draft), **kai-obsidian-vault** (2/2 — its #1 landed 08-30), **obsidian-kai** (1/1), **command-center-redirect** (1/1), **----Workspace-notes** (1/1). Watch whether any converts draft→ready.*

---

## Founder action queue (all founder-authority — the ONLY things between "open" and "done")
1. 🔴 **Sign the Week-1 gate** — `STEF-WEEK-1-APPROVAL.md`, **~19.8 d cold**, agent side complete.
2. 🟢 **Batch-merge jobscout #7–#16** → clever-cannon → main, any order (empirically clean, **~44.0 d cold, zero landed**).
3. 🟢 **Merge psychic-bassoon stack** — **#20 CVE → #22 date-fix (closes #21) → #19 headers → #1 (last, 1 manual resolve)** (~16.6 d unmerged; all 4 CLEAN).
4. 🎬 **Merge avrg #25** — shared-mutable-state fix, CLEAN, base main (~17.0 d cold).
5. 📥 **Merge Enrollment_Funnel_Agent #14** — CSV substring-collision fix, CLEAN, default base (**~44.0 d cold**).
6. 📨 **Merge -Community_intake_Routing #2** — intake-classify substring-collision fix, CLEAN, default base (**~22.0 d cold**).
7. 🛠️ **INFRA:** ⚠️ **RETROACTIVE — mundi #8 CORS-widening on `/api/agents` ALREADY MERGED (2026-08-30 22:26Z) without the flagged review; verify the origin scope is acceptable.** Remaining: Link-inbio #15 (2288-line Command Center rebuild — human eyes).
8. 📝 **File forming-paws IL nonprofit docs** (issue #8 — drafted, filing is founder-only).
9. 🟠 **Env carries:** Formspree env on Vercel (gates psychic #1 forms); Supabase project → psychic #11 + avrg #5. **Fund OpenAI key** de-hedges Criterion 1 (non-blocking — Claude is the permanent default).

## Tracks (canonical, per context.md)
- **Track 1 · The Plug AI:** Execution starts **2026-10-13** (post-OpenClaw); fiscal-sponsor target **2026-11-30.** IL Digital Equity $75K is **LAPSING BY CHOICE** — not a blocker, stop flagging. theplugai.net `main` is banked and senior-grade; the wins now are merging the two green security PRs (#20 CVE, #19 headers) + the date fix (#22).
- **Track 2 · BigHeart (bridge):** content-automation pitch + "Digital Content & AI Systems Specialist" title/comp ask in motion.
- **Track 2 · Forming Paws:** execution; app caught up (through #62). Sole remaining item is founder legal filing (issue #8).

## Content pipeline (running, healthy)
- LinkedIn shipped **through #251** (content-pipeline Run 250). #251 opened a new domain: **Social Security Disability / SSDI-SSI** for a 46yo south-suburbs tradesman whose body gave out — core truth: the benefit is insurance he already paid for, applying is FREE, no one can guarantee an SSA approval. Real doors: local SSA office/ssa.gov, legal aid, a rep paid only from back pay if you win, Illinois DRS. Safety spine holds (dignity-not-deficit, compliance twice, AI augment-not-replace). Prior #250 opened job-search / employment / job-scam-wave.

## Continuous
- Vault management (inbox, atomic notes, index, tag/link hygiene) across all PARA areas.

---
*Run 236 finding: **STABILITY — no new merge event since Run 235's drift.** The `--merged --closed ">=2026-08-30"` check returns only the 4 already-caught landings (mundi #7+#8 @ 22:26Z, psychic #23 @ 06:04Z, kai-obsidian-vault #1 @ 05:58Z) — nothing new since Run 235's sweep. **mundi-agent-dashboard has now correctly dropped OUT of the open sweep** (both PRs merged) → infra cluster confirmed cleared. Account-wide sweep **unchanged: 30 open / 12 drafts → 18 non-draft across 11 repos.** psychic #20 live-re-verified OPEN/MERGEABLE/CLEAN/base main. Link-inbio confirmed 3 open (only #15 non-draft; #6 resume PDF + #5 ops vault are drafts). Coldness: jobscout ~44.0 d · enroll ~44.0 d (last #6/#13, 2026-07-18) · psychic PRs ~16.6 d · avrg ~17.0 d (last #24, 2026-08-14) · -Community_intake ~22.0 d (last #1, 2026-08-09) · forming-paws ~8.0 d (last #62) · gate ~19.8 d (APPROVAL REQUESTED, 3125 b frozen). Net: 0 agent-actionable code blockers account-wide — 1 signature + 1 batch (10 PRs) + 4 psychic + 1 avrg + 1 Enrollment + 1 -Community_intake + 1 Link-inbio rebuild + 1 IL filing, all founder clicks. Tooling for this env: full-file Write for this digest (Edit tool gated on this Desktop/kai path); `stat -f` on the gate; `gh search prs --owner morrisstephon51 --state open` account-wide (repo set is UNSTABLE — was 7→11; ALWAYS sweep account-wide; merged-PR check uses `--merged --closed ">=DATE"`, NOT `--state merged`, JSON field `closedAt`). HANDOFF: next loop re-measure gate coldness + re-check merges via account-wide sweep (jobscout #7–#16 / psychic #20/#22/#19/#1 / avrg #25 / Enrollment #14 / -Community_intake #2 / Link-inbio #15 / gate signature); if #22 merges confirm #21 auto-closed; if #22 AND #1 both merge confirm the manual `lib/utils.ts` resolve landed clean; if any jobscout PR merges confirm clever-cannon→main promotion; watch whether the draft-only repos convert draft→ready; mundi cluster DONE — stays dropped unless a new mundi PR opens.*
