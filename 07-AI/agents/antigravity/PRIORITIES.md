# Antigravity — Active Priorities Digest

*Refreshed by antigravity **Run 233** · 2026-08-30 (~14:13Z UTC). This run: re-scanned context (context.md canonical + world.md), polled the bus (clawd Run 257 / codex Run 243 / content-pipeline Run 247 loop broadcasts — none directed at antigravity), **re-measured the sole cold P1 gate** (`stat` → still `**Status:** APPROVAL REQUESTED`, byte-frozen 3125 b, mtime `2026-08-11T09:31:48Z` → now **19.20 days cold**), and **source-verified the merge frontier live via the account-wide `gh search prs --owner morrisstephon51 --state open` sweep** (verify-don't-trust-the-bus). **Headline delta vs Run 231/232: psychic-bassoon #19 was CONFLICTING/DIRTY earlier today, and codex Run 243 resolved the `next.config.js` conflict (kept both `main` rewrites() + PR headers()) — I live-re-verified all 4 psychic PRs (#20/#22/#19/#1) now OPEN / MERGEABLE / CLEAN / base main.** Second correction: the Run-232 frontier count of "20/8 repos" was a one-repo overcount — the live sweep is **20 non-draft PRs across 7 repos** (32 open total; 12 drafts). Framed the way clawd tracks it: **product frontier 17 non-draft / 5 repos** (jobscout, psychic, avrg, Enrollment, -Community_intake) **+ infra/tooling cluster 3 non-draft / 2 repos** (mundi-agent-dashboard #7/#8, Link-inbio #15) = 20/7. **Delta on merges/signatures: ZERO** — nothing merged, nothing signed, nothing closed; the board aged ~0.4 day. Coldness clocks: jobscout 43.59 d · enroll 43.59 d · psychic 15.80 d · avrg 15.80 d · -Community_intake 21.59 d · forming-paws 7.59 d · gate 19.20 d.*

---

## 🔴 THE ONE THING — sole open P1 is the FOUNDER signature (now 19.20 days cold)
- `~/clawd/AI-Organization/STEF-WEEK-1-APPROVAL.md` **still reads `**Status:** APPROVAL REQUESTED`** — mtime **2026-08-11T09:31:48Z**, re-verified on disk this run → **19.20 days cold** (byte-for-byte unmoved since Aug 11, 3125 bytes).
- The report is **✅ Week-1 PASS** (12 tasks, 3.34× avg speedup, zero escalations, 8.6/10 confidence, 100% cost tracked) and recommends **APPROVE → proceed to Phase-2 Week-2**. Everything is agent/supervisor-signed; **only Stef's written checkmark is missing.**
- **The gate is aging, not thawing.** No agent can click it. One-line written approval (email, or set the in-file status line to ✅) closes it.

## P1 — OpenClaw Phase 1-4 (gates all Track 1/2 execution)
- **Phase 1 LIVE 2026-07-27 → 2026-08-17.** Completing Phase 1-4 is Stef's Priority 1; target **2026-10-12.**
- Phase-2 Week-1 sign-off is **DONE agent-side.** Sole open item = the founder gate above.
- **ADR-008 (ACCEPTED):** Claude Sonnet 4.6 is the **PERMANENT code-gen default** — a failed Claude call FAILS the task (no silent downgrade). Not conditional on OpenAI funding.

---

## Merge frontier — source-verified live via account-wide sweep, Run 233
*Account-wide: **32 open PRs / 12 drafts → 20 non-draft actionable across 7 repos** + **1 cold governance gate** + **open issues.** Net: **0 agent-actionable code blockers.** Every lever is founder-authority (sign / merge / file / set env). Tracked as: **product frontier 17/5** + **infra cluster 3/2.** States below confirmed live this run via `gh search prs` + `gh pr view --json mergeable,isDraft,mergeStateStatus,baseRefName`.*

### 🟢 Track 2 · job_opportunity_scanner — 10-PR scorer batch, EMPIRICALLY batch-mergeable
- **PRs #7–#16 — all 10 OPEN, non-draft, MERGEABLE/CLEAN**, base default `claude/clever-cannon-IDh3G`.
- codex Run 236 **actually merged all ten into `clever-cannon` → 0 conflicts, 9/9 tests pass**; Run 239 re-confirmed 10/10 CLEAN + 58 pytest green. Batch-merge #7–#16 → clever-cannon → main, **any order, no rebases.**
- **Last merge still #6 (2026-07-18) → 43.59 days cold; zero of #7–#16 landed.** Coverage: token-boundary location/title scoring, `$85k` salary parse, "trainer" title signal, recency-window filters (weeks/months/30+ days ago, ISO posted_date), config-driven salary floor, loud-fail on count mismatch, KeyError-safe alerts.

### 🟢 Track 1 · psychic-bassoon (theplugai.net) — `main` hardened; 4 mergeable PRs open, NONE merged
- **PR #20** 🔒 bump Next.js 14.2.5 → 14.2.35 — closes published CVEs (incl. CVE-2025-29927 middleware-auth-bypass class). MERGEABLE/CLEAN. **Highest-value single click on the whole queue** (a live published-CVE patch, 15.80 d unmerged).
- **PR #22** 🗓️ render date-only strings in local time — **closes issue #21** (Central-Time off-by-one). MERGEABLE/CLEAN, test fails-on-bug/passes-on-fix. **Merging #22 auto-closes #21.** codex Run 242 added `lib/utils.test.ts` (TZ-pinned, 4/4 pass).
- **PR #19** 🔒 baseline security response headers site-wide. **Was CONFLICTING/DIRTY earlier today (merge backlog on `next.config.js`); codex Run 243 resolved it — kept both main `rewrites()` + PR `headers()`, net diff = only the header block. Live-re-verified MERGEABLE/CLEAN this run.** Disjoint from the others, any order.
- **PR #1** real content / working forms / resource detail pages. MERGEABLE/CLEAN **against current main** — ⚠️ **still conflicts with #22 on `lib/utils.ts` AFTER #22 lands (codex Run 239): #22 fixes `formatShortDate`+`formatDate`, #1 deletes `formatShortDate`. Merge #1 LAST with 1 manual resolve — keep #1's deletion (dead code, 0 callers), keep #22's fix.** Forms also need Formspree env on Vercel; `.env.example` add/add hazard with draft #11.
- **PR #11** Grant Matching Tracker — founder-authored **DRAFT**, MERGEABLE/CLEAN. Needs Supabase + 8 Vercel env vars. Founder-owned WIP (NOT in action frontier).
- **Last merge still #18 (2026-08-14T19:04Z) → 15.80 days cold.**
- **Suggested merge order: #20 (CVE) → #22 (date fix, auto-closes #21) → #19 (headers) → #1 (last, 1 manual resolve).**

### 🎬 Track 2 · ai-video-reel-generator (avrg) — 1 mergeable PR open
- **PR #25** `fix(schedule)`: stop `getBestPostTimes` from mutating the shared `PLATFORM_SCHEDULES` constant — single file (+5/−1), base `main`, MERGEABLE/CLEAN non-draft (codex Run 237).
- **Last merge #24 (2026-08-14T19:04Z) → 15.80 days cold.**
- **Issue #5** — Supabase project to run the content-automation loop. **PR#4 (the loop) already MERGED**, so #5 is a runtime env/provisioning item, **not a pending-merge blocker.**

### 📥 Track 2 · Enrollment_Funnel_Agent — 1 mergeable PR open
- **PR #14** `fix(csv)`: platform CSVs mis-routed by substring collisions (ig/tt/fb/yt) — single file (+18/−6), base default `claude/keen-noether-VED1j`, MERGEABLE/CLEAN non-draft (codex Run 238).
- **Last merge #13 (2026-07-18) → 43.59 days cold** — tied with jobscout for coldest PR repo. **0 open issues.**

### 📨 Track 2 · -Community_intake_Routing — 1 mergeable PR open
- **PR #2** `fix(classify)`: intake keywords matched as bare substrings misroute learners (fund/invest/serve/teach) — files `api/intake.js` + `intake.js` (+31/−7), base default `claude/quirky-galileo-UGnfz`, MERGEABLE/CLEAN non-draft. **Same substring-collision defect class as jobscout #7/#8 and Enrollment #14.**
- **Last merge #1 (2026-08-09) → 21.59 days cold. 0 open issues.**

### 🛠️ INFRA/TOOLING cluster — 3 non-draft PRs / 2 repos (MUNDI-governed, OUTSIDE the product queue)
*Surfaced Run 232, re-confirmed live Run 233. clawd Run 257 correctly places these outside the 17/5 product frontier — they're the dashboard/command-center tooling MUNDI governs from, not Plug AI product code. Tracked so they don't silently rot.*
- **mundi-agent-dashboard #8** — "Allow cross-origin reads on /api/agents" (+8/−3, today 07:48Z). ⚠️ **CORS-widening — REVIEW BEFORE MERGE, not a blind click.** Flag to founder as a security-surface change.
- **mundi-agent-dashboard #7** — "Fix stale/missing entries in the links panel" (+23/−12, today 07:22Z). Low-risk fix.
- **Link-inbio #15** — "Rebuild Command Center as a live scroll-driven dashboard" (+2288/−541, today 08:26Z). ⚠️ **Large rebuild — likely wants human eyes before merge.**

### 🐾 Track 2 · forming-paws (Puppy Power) — caught up, 0 open PRs
- **0 open PRs.** Founder merged the visual-refresh epic through **#62** (Aug 23, 7.59 d ago) — the real signal the founder is active, just not on the items above.
- **Sole open issue #8** — IL articles of incorporation + bylaws **drafted**; filing is **founder-only** (IL Secretary of State). Track until Stef files or defers.

---

## Founder action queue (all founder-authority — the ONLY things between "open" and "done")
1. 🔴 **Sign the Week-1 gate** — `STEF-WEEK-1-APPROVAL.md`, **19.20 d cold**, agent side complete.
2. 🟢 **Batch-merge jobscout #7–#16** → clever-cannon → main, any order (empirically clean, **43.59 d cold, zero landed**).
3. 🟢 **Merge psychic-bassoon stack** — **#20 CVE → #22 date-fix (closes #21) → #19 headers → #1 (last, 1 manual resolve)** (15.80 d unmerged; #19 conflict cleared by codex Run 243, all 4 now CLEAN).
4. 🎬 **Merge avrg #25** — shared-mutable-state fix, CLEAN, base main (15.80 d cold).
5. 📥 **Merge Enrollment_Funnel_Agent #14** — CSV substring-collision fix, CLEAN, default base (**43.59 d cold**).
6. 📨 **Merge -Community_intake_Routing #2** — intake-classify substring-collision fix, CLEAN, default base (**21.59 d cold**).
7. 🛠️ **INFRA (review-then-merge):** mundi #7 (links fix, low-risk) then mundi #8 (**CORS-widening — review the origin scope first**); Link-inbio #15 (2288-line Command Center rebuild — human eyes).
8. 📝 **File forming-paws IL nonprofit docs** (issue #8 — drafted, filing is founder-only).
9. 🟠 **Env carries:** Formspree env on Vercel (gates psychic #1 forms); Supabase project → psychic #11 + avrg #5. **Fund OpenAI key** de-hedges Criterion 1 (non-blocking — Claude is the permanent default).

## Tracks (canonical, per context.md)
- **Track 1 · The Plug AI:** Execution starts **2026-10-13** (post-OpenClaw); fiscal-sponsor target **2026-11-30.** IL Digital Equity $75K is **LAPSING BY CHOICE** — not a blocker, stop flagging. theplugai.net `main` is banked and senior-grade; the wins now are merging the two green security PRs (#20 CVE, #19 headers) + the date fix (#22).
- **Track 2 · BigHeart (bridge):** content-automation pitch + "Digital Content & AI Systems Specialist" title/comp ask in motion.
- **Track 2 · Forming Paws:** execution; app caught up (through #62). Sole remaining item is founder legal filing (issue #8).

## Content pipeline (running, healthy)
- LinkedIn shipped **through #248** (content-pipeline Run 247). Latest opened a new domain: **medical debt / hospital bills / charity care** (501(r) financial-assistance rights, itemized-bill errors, free hospital financial counselor, No Surprises Act) with the scam spine (fake debt-relief mill, collections imposter, advance-fee "grant"). Safety spine holds every lane (quiet-helper / augment-not-replace, compliance stated twice, never fed SSN/account/bank login).

## Continuous
- Vault management (inbox, atomic notes, index, tag/link hygiene) across all PARA areas.

---
*Run 233 finding: **still full stasis on founder-authority — zero merges/signatures/closures since Run 228**, but two real corrections landed this run. (1) **psychic #19 recovered:** it briefly went CONFLICTING/DIRTY today; codex Run 243 resolved the `next.config.js` conflict, and I live-re-verified all four psychic PRs (#20/#22/#19/#1) OPEN/MERGEABLE/CLEAN/base main — the stack is once again fully green and merge-order-ready. (2) **Frontier count fixed:** the account-wide sweep gives **20 non-draft / 7 repos** (Run 232's "8" overcounted by one); clawd's framing = 17 product/5 + 3 infra/2. Live states: jobscout #7–#16 all 10 CLEAN on shared base (last #6, 43.59 d, zero landed); avrg #25 CLEAN base main (last #24, 15.80 d); Enrollment #14 CLEAN default base (last #13, 43.59 d); -Community_intake #2 CLEAN default base (last #1, 21.59 d); infra mundi #7/#8 + Link-inbio #15 open today (outside product queue, #8 CORS-widening + #15 2288-line rebuild = review-before-merge); forming-paws 0 open PRs, issue #8 open (7.59 d since #62); gate byte-frozen at APPROVAL REQUESTED (19.20 d). Net: 0 agent-actionable code blockers account-wide — 1 signature + 1 batch (10 PRs) + 4 psychic + 1 avrg + 1 Enrollment + 1 -Community_intake + 3 infra reviews + 1 IL filing, all founder clicks. Tooling for this env: full-file Write for this digest (Edit tool gated on this Desktop/kai path); `stat` on the gate; `gh search prs --owner morrisstephon51 --state open` account-wide (the per-repo loop dropped -Community_intake for 3 runs AND missed today's mundi/Link-inbio infra PRs — always sweep account-wide, the PR-bearing repo set is unstable, 5→7→ possibly more). HANDOFF: next loop re-measure gate coldness + re-check merges via account-wide sweep (jobscout #7–#16 / psychic #20/#22/#19/#1 / avrg #25 / Enrollment #14 / -Community_intake #2 / mundi #7/#8 / Link-inbio #15 / gate signature); if #22 merged confirm #21 auto-closed; if #22 AND #1 both merge confirm the manual `lib/utils.ts` resolve landed clean; if any jobscout PR merges confirm clever-cannon→main promotion; FLAG mundi #8 to founder as CORS-widening; watch for an 8th hidden repo.*
