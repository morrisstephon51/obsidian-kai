# Antigravity — Active Priorities Digest

*Refreshed by antigravity **Run 234** · 2026-08-30 (~19:18Z UTC). This run: re-scanned context (context.md canonical + world.md), polled the bus (clawd / codex / content-pipeline #249 loop-start + loop-end broadcasts — none directed at antigravity), **re-measured the sole cold P1 gate** (`stat` → still `**Status:** APPROVAL REQUESTED`, byte-frozen 3125 b, mtime `2026-08-11T09:31:48Z` → now **19.41 days cold**), and **re-ran the account-wide `gh search prs --owner morrisstephon51 --state open` sweep** (verify-don't-trust-the-bus). **Headline: full no-drift confirmation vs Run 233.** Account-wide count unchanged: **32 open / 12 drafts → 20 non-draft across 7 repos** (no 8th repo appeared — the repo set held steady this loop). psychic #20 live-re-verified OPEN/MERGEABLE/CLEAN/base main. **Merged-since-Run-233 check: ZERO** — the only merges in the last 3 days (psychic #23, kai-obsidian-vault #1, obsidian-kai #1) all pre-date Run 233's 14:13Z sweep and were already logged. **Delta on merges/signatures/closures: ZERO; the board aged ~0.21 day.** Coldness clocks: jobscout 43.80 d · enroll 43.80 d · psychic 16.01 d · avrg 16.01 d · -Community_intake 21.80 d · forming-paws 7.80 d · gate 19.41 d.*

---

## 🔴 THE ONE THING — sole open P1 is the FOUNDER signature (now 19.41 days cold)
- `~/clawd/AI-Organization/STEF-WEEK-1-APPROVAL.md` **still reads `**Status:** APPROVAL REQUESTED`** — mtime **2026-08-11T09:31:48Z**, re-verified on disk this run → **19.41 days cold** (byte-for-byte unmoved since Aug 11, 3125 bytes).
- The report is **✅ Week-1 PASS** (12 tasks, 3.34× avg speedup, zero escalations, 8.6/10 confidence, 100% cost tracked) and recommends **APPROVE → proceed to Phase-2 Week-2**. Everything is agent/supervisor-signed; **only Stef's written checkmark is missing.**
- **The gate is aging, not thawing.** No agent can click it. One-line written approval (email, or set the in-file status line to ✅) closes it.

## P1 — OpenClaw Phase 1-4 (gates all Track 1/2 execution)
- **Phase 1 LIVE 2026-07-27 → 2026-08-17.** Completing Phase 1-4 is Stef's Priority 1; target **2026-10-12.**
- Phase-2 Week-1 sign-off is **DONE agent-side.** Sole open item = the founder gate above.
- **ADR-008 (ACCEPTED):** Claude Sonnet 4.6 is the **PERMANENT code-gen default** — a failed Claude call FAILS the task (no silent downgrade). Not conditional on OpenAI funding.

---

## Merge frontier — source-verified live via account-wide sweep, Run 234
*Account-wide: **32 open PRs / 12 drafts → 20 non-draft actionable across 7 repos** + **1 cold governance gate** + **open issues.** Net: **0 agent-actionable code blockers.** Every lever is founder-authority (sign / merge / file / set env). Tracked as: **product frontier 17/5** + **infra cluster 3/2.** Repo set held at 7 this run (no 8th surfaced). States below confirmed live this run via `gh search prs` + `gh pr view --json mergeable,isDraft,mergeStateStatus,baseRefName`.*

### 🟢 Track 2 · job_opportunity_scanner — 10-PR scorer batch, EMPIRICALLY batch-mergeable
- **PRs #7–#16 — all 10 OPEN, non-draft, MERGEABLE/CLEAN**, base default `claude/clever-cannon-IDh3G`.
- codex Run 236 **actually merged all ten into `clever-cannon` → 0 conflicts, 9/9 tests pass**; Run 239 re-confirmed 10/10 CLEAN + 58 pytest green. Batch-merge #7–#16 → clever-cannon → main, **any order, no rebases.**
- **Last merge still #6 (2026-07-18) → 43.80 days cold; zero of #7–#16 landed.** Coverage: token-boundary location/title scoring, `$85k` salary parse, "trainer" title signal, recency-window filters (weeks/months/30+ days ago, ISO posted_date), config-driven salary floor, loud-fail on count mismatch, KeyError-safe alerts.

### 🟢 Track 1 · psychic-bassoon (theplugai.net) — `main` hardened; 4 mergeable PRs open, NONE merged
- **PR #20** 🔒 bump Next.js 14.2.5 → 14.2.35 — closes published CVEs (incl. CVE-2025-29927 middleware-auth-bypass class). MERGEABLE/CLEAN (live-re-verified Run 234). **Highest-value single click on the whole queue** (a live published-CVE patch, 16.01 d unmerged).
- **PR #22** 🗓️ render date-only strings in local time — **closes issue #21** (Central-Time off-by-one). MERGEABLE/CLEAN, test fails-on-bug/passes-on-fix. **Merging #22 auto-closes #21.** codex Run 242 added `lib/utils.test.ts` (TZ-pinned, 4/4 pass).
- **PR #19** 🔒 baseline security response headers site-wide. **Recovered Run 233 (codex Run 243 resolved the `next.config.js` merge-backlog conflict — kept both main `rewrites()` + PR `headers()`, net diff = only the header block).** MERGEABLE/CLEAN. Disjoint from the others, any order.
- **PR #1** real content / working forms / resource detail pages. MERGEABLE/CLEAN **against current main** — ⚠️ **still conflicts with #22 on `lib/utils.ts` AFTER #22 lands (codex Run 239): #22 fixes `formatShortDate`+`formatDate`, #1 deletes `formatShortDate`. Merge #1 LAST with 1 manual resolve — keep #1's deletion (dead code, 0 callers), keep #22's fix.** Forms also need Formspree env on Vercel; `.env.example` add/add hazard with draft #11.
- **PR #11** Grant Matching Tracker — founder-authored **DRAFT**, MERGEABLE/CLEAN. Needs Supabase + 8 Vercel env vars. Founder-owned WIP (NOT in action frontier).
- **Last merge still #18 (2026-08-14T19:04Z) → 16.01 days cold.**
- **Suggested merge order: #20 (CVE) → #22 (date fix, auto-closes #21) → #19 (headers) → #1 (last, 1 manual resolve).**

### 🎬 Track 2 · ai-video-reel-generator (avrg) — 1 mergeable PR open
- **PR #25** `fix(schedule)`: stop `getBestPostTimes` from mutating the shared `PLATFORM_SCHEDULES` constant — single file (+5/−1), base `main`, MERGEABLE/CLEAN non-draft (codex Run 237).
- **Last merge #24 (2026-08-14T19:04Z) → 16.01 days cold.**
- **Issue #5** — Supabase project to run the content-automation loop. **PR#4 (the loop) already MERGED**, so #5 is a runtime env/provisioning item, **not a pending-merge blocker.**

### 📥 Track 2 · Enrollment_Funnel_Agent — 1 mergeable PR open
- **PR #14** `fix(csv)`: platform CSVs mis-routed by substring collisions (ig/tt/fb/yt) — single file (+18/−6), base default `claude/keen-noether-VED1j`, MERGEABLE/CLEAN non-draft (codex Run 238).
- **Last merge #13 (2026-07-18) → 43.80 days cold** — tied with jobscout for coldest PR repo. **0 open issues.**

### 📨 Track 2 · -Community_intake_Routing — 1 mergeable PR open
- **PR #2** `fix(classify)`: intake keywords matched as bare substrings misroute learners (fund/invest/serve/teach) — files `api/intake.js` + `intake.js` (+31/−7), base default `claude/quirky-galileo-UGnfz`, MERGEABLE/CLEAN non-draft. **Same substring-collision defect class as jobscout #7/#8 and Enrollment #14.**
- **Last merge #1 (2026-08-09) → 21.80 days cold. 0 open issues.**

### 🛠️ INFRA/TOOLING cluster — 3 non-draft PRs / 2 repos (MUNDI-governed, OUTSIDE the product queue)
*Surfaced Run 232, re-confirmed live Run 233/234. clawd correctly places these outside the 17/5 product frontier — they're the dashboard/command-center tooling MUNDI governs from, not Plug AI product code. Tracked so they don't silently rot.*
- **mundi-agent-dashboard #8** — "Allow cross-origin reads on /api/agents" (+8/−3, opened 2026-08-30 07:48Z). ⚠️ **CORS-widening — REVIEW BEFORE MERGE, not a blind click.** Flag to founder as a security-surface change.
- **mundi-agent-dashboard #7** — "Fix stale/missing entries in the links panel" (+23/−12, opened 2026-08-30 07:22Z). Low-risk fix.
- **Link-inbio #15** — "Rebuild Command Center as a live scroll-driven dashboard" (+2288/−541, opened 2026-08-30 08:26Z). ⚠️ **Large rebuild — likely wants human eyes before merge.**

### 🐾 Track 2 · forming-paws (Puppy Power) — caught up, 0 open PRs
- **0 open PRs.** Founder merged the visual-refresh epic through **#62** (Aug 23, 7.80 d ago) — the real signal the founder is active, just not on the items above.
- **Sole open issue #8** — IL articles of incorporation + bylaws **drafted**; filing is **founder-only** (IL Secretary of State). Track until Stef files or defers.

---

## Founder action queue (all founder-authority — the ONLY things between "open" and "done")
1. 🔴 **Sign the Week-1 gate** — `STEF-WEEK-1-APPROVAL.md`, **19.41 d cold**, agent side complete.
2. 🟢 **Batch-merge jobscout #7–#16** → clever-cannon → main, any order (empirically clean, **43.80 d cold, zero landed**).
3. 🟢 **Merge psychic-bassoon stack** — **#20 CVE → #22 date-fix (closes #21) → #19 headers → #1 (last, 1 manual resolve)** (16.01 d unmerged; all 4 CLEAN).
4. 🎬 **Merge avrg #25** — shared-mutable-state fix, CLEAN, base main (16.01 d cold).
5. 📥 **Merge Enrollment_Funnel_Agent #14** — CSV substring-collision fix, CLEAN, default base (**43.80 d cold**).
6. 📨 **Merge -Community_intake_Routing #2** — intake-classify substring-collision fix, CLEAN, default base (**21.80 d cold**).
7. 🛠️ **INFRA (review-then-merge):** mundi #7 (links fix, low-risk) then mundi #8 (**CORS-widening — review the origin scope first**); Link-inbio #15 (2288-line Command Center rebuild — human eyes).
8. 📝 **File forming-paws IL nonprofit docs** (issue #8 — drafted, filing is founder-only).
9. 🟠 **Env carries:** Formspree env on Vercel (gates psychic #1 forms); Supabase project → psychic #11 + avrg #5. **Fund OpenAI key** de-hedges Criterion 1 (non-blocking — Claude is the permanent default).

## Tracks (canonical, per context.md)
- **Track 1 · The Plug AI:** Execution starts **2026-10-13** (post-OpenClaw); fiscal-sponsor target **2026-11-30.** IL Digital Equity $75K is **LAPSING BY CHOICE** — not a blocker, stop flagging. theplugai.net `main` is banked and senior-grade; the wins now are merging the two green security PRs (#20 CVE, #19 headers) + the date fix (#22).
- **Track 2 · BigHeart (bridge):** content-automation pitch + "Digital Content & AI Systems Specialist" title/comp ask in motion.
- **Track 2 · Forming Paws:** execution; app caught up (through #62). Sole remaining item is founder legal filing (issue #8).

## Content pipeline (running, healthy)
- LinkedIn shipped **through #249** (content-pipeline Run 248). Latest opened a new domain: **utility shutoff / LIHEAP energy assistance** (free LIHEAP via CEDA + 211, deferred/budget/PIPP payment plans, IL winter shutoff protection, ICC + Citizens Utility Board) with the scam spine (disconnection phone imposter, fake energy-grant advance fee, supplier slamming, application-fee + refund scams). Safety spine holds every lane (dignity-not-deficit / quiet-helper, compliance stated twice, never fed prepaid-card/bank/SSN details).

## Continuous
- Vault management (inbox, atomic notes, index, tag/link hygiene) across all PARA areas.

---
*Run 234 finding: **full no-drift confirmation — still zero merges/signatures/closures since Run 228**, board aged ~0.21 day. Account-wide sweep held steady at **32 open / 12 drafts → 20 non-draft / 7 repos** (no 8th repo appeared this loop); psychic #20 live-re-verified OPEN/MERGEABLE/CLEAN/base main; merged-in-last-3-days (psychic #23, kai-vault #1, obsidian-kai #1) all pre-date Run 233 and were already logged, so nothing new landed. Live coldness: jobscout 43.80 d · enroll 43.80 d (last #6/#13, 2026-07-18) · psychic 16.01 d · avrg 16.01 d (last #18/#24, 2026-08-14) · -Community_intake 21.80 d (last #1) · forming-paws 7.80 d (last #62) · gate 19.41 d (APPROVAL REQUESTED, 3125 b frozen). Net: 0 agent-actionable code blockers account-wide — 1 signature + 1 batch (10 PRs) + 4 psychic + 1 avrg + 1 Enrollment + 1 -Community_intake + 3 infra reviews + 1 IL filing, all founder clicks. Tooling for this env: full-file Write for this digest (Edit tool gated on this Desktop/kai path); `stat -f` on the gate; `gh search prs --owner morrisstephon51 --state open` account-wide (the per-repo loop dropped -Community_intake for 3 runs AND missed the mundi/Link-inbio infra PRs — always sweep account-wide; merged-PR check uses `--merged --closed ">=DATE"`, NOT `--state merged`). HANDOFF: next loop re-measure gate coldness + re-check merges via account-wide sweep (jobscout #7–#16 / psychic #20/#22/#19/#1 / avrg #25 / Enrollment #14 / -Community_intake #2 / mundi #7/#8 / Link-inbio #15 / gate signature); if #22 merged confirm #21 auto-closed; if #22 AND #1 both merge confirm the manual `lib/utils.ts` resolve landed clean; if any jobscout PR merges confirm clever-cannon→main promotion; FLAG mundi #8 to founder as CORS-widening; keep watching for an 8th hidden repo (set has been stable 7 for 2 runs now).*
