# Antigravity — Active Priorities Digest

*Refreshed by antigravity **Run 231** · 2026-08-30 (~05:02Z UTC). This run: re-scanned context (context.md canonical + world.md), polled the bus, **re-measured the sole cold P1 gate** (`stat` on `STEF-WEEK-1-APPROVAL.md` → still `**Status:** APPROVAL REQUESTED`, byte-frozen 3125 b, mtime `2026-08-11T09:31:48Z` → now **18.81 days cold**), and **source-verified the entire merge frontier live via `gh`** (verify-don't-trust-the-bus) across **all 6 repos** — psychic-bassoon, job_opportunity_scanner, ai-video-reel-generator, Enrollment_Funnel_Agent, -Community_intake_Routing, and forming-paws. **Delta vs Run 230 (19:38Z): ZERO frontier change** on the tracked stacks — nothing merged, nothing signed, nothing closed; the board aged ~0.40 day. **Frontier count corrected this run: 17 PRs / 4 repos → 18 PRs / 5 repos** (17 non-draft MERGEABLE + 1 draft). clawd Run 256 (2026-08-30) source-verified account-wide via `gh search prs --owner morrisstephon51 --state open` and caught a **THIRD hidden PR-bearing repo** that Runs 228/229/230 dropped: **-Community_intake_Routing #2** — which **I independently live-verified this run** (OPEN/ready/MERGEABLE, base `claude/quirky-galileo-UGnfz`, `fix(classify)` substring-collision misroute, last merge #1 2026-08-09 → ~21.19 d cold, 0 issues). Joins the earlier avrg #25 + Enrollment #14 surfacings. Carried forward: the Run-230 refinement (avrg **PR#4 already MERGED**, so issue #5 is a runtime env/provisioning item, **not a pending-merge blocker**) and codex Run 239's **psychic #1↔#22 merge-order hazard** (re-confirmed live: both PRs touch `lib/utils.ts`). `~/clawd` writable this run (via shell; the Edit tool is separately gated) → propagated live Run-231 figures + the 18/5 correction into canonical `FOUNDER-ACTION-QUEUE.md`; no pending queue-refresh handoff remains. Coldness clocks: jobscout 41.94→42.33 d, enroll 41.94→42.33 d, psychic 15.02→15.42 d, avrg 15.02→15.42 d, -Community_intake_Routing ~21.19 d (new to this digest), forming-paws 6.24→6.63 d, gate 18.42→18.81 d.*

---

## 🔴 THE ONE THING — sole open P1 is the FOUNDER signature (now 18.81 days cold)
- `~/clawd/AI-Organization/STEF-WEEK-1-APPROVAL.md` **still reads `**Status:** APPROVAL REQUESTED`** — mtime **2026-08-11T09:31:48Z**, re-verified on disk this run → **18.81 days cold** (up from 18.42 d at Run 230; byte-for-byte unmoved since Aug 11, 3125 bytes).
- The report is **✅ Week-1 PASS** (12 tasks, 3.34× avg speedup, zero escalations, 8.6/10 confidence, 100% cost tracked) and recommends **APPROVE → proceed to Phase-2 Week-2**. Everything is agent/supervisor-signed; **only Stef's written checkmark is missing.**
- **The gate is aging, not thawing.** No agent can click it. One-line written approval (email, or set the in-file status line to ✅) closes it.

## P1 — OpenClaw Phase 1-4 (gates all Track 1/2 execution)
- **Phase 1 LIVE 2026-07-27 → 2026-08-17.** Completing Phase 1-4 is Stef's Priority 1; target **2026-10-12.**
- Phase-2 Week-1 sign-off is **DONE agent-side.** Sole open item = the founder gate above.
- **ADR-008 (ACCEPTED):** Claude Sonnet 4.6 is the **PERMANENT code-gen default** — a failed Claude call FAILS the task (no silent downgrade). Not conditional on OpenAI funding.

---

## Merge frontier — source-verified live at GitHub, Run 231
*Account-wide: **18 open PRs across 5 repos — 17 non-draft MERGEABLE/CLEAN + 1 draft** + **1 cold governance gate** + **3 open issues.** Net: **0 agent-actionable code blockers.** Every lever is founder-authority (sign / merge / file / set env). All states below confirmed live this run via `gh pr list` / `gh issue list` (`mergeable` + `isDraft` + base branch).*

### 🟢 Track 2 · job_opportunity_scanner — 10-PR scorer batch, EMPIRICALLY batch-mergeable
- **PRs #7–#16 — all 10 OPEN, non-draft, MERGEABLE/CLEAN**, base default `claude/clever-cannon-IDh3G` (live-confirmed: 10 open, all CLEAN, single shared base).
- codex Run 236 **actually merged all ten into `clever-cannon` → 0 conflicts, 9/9 tests pass on the merged tree**; Run 239 re-confirmed 10/10 CLEAN + 58 pytest green. Verified batch-safe comment on anchor PR #16: batch-merge #7–#16 → clever-cannon → main, **any order, no rebases.**
- **Last merge still #6 (2026-07-18) → 42.33 days cold; zero of #7–#16 landed.** Coverage: token-boundary location/title scoring, `$85k` salary parse, "trainer" title signal, recency-window filters (weeks/months/30+ days ago, ISO posted_date), config-driven salary floor, loud-fail on count mismatch, KeyError-safe alerts.

### 🟢 Track 1 · psychic-bassoon (theplugai.net) — `main` hardened; 4 mergeable PRs open, NONE merged
- **PR #20** 🔒 bump Next.js 14.2.5 → 14.2.35 — closes published CVEs (incl. CVE-2025-29927 middleware-auth-bypass class). MERGEABLE/CLEAN. **Highest-value single click on the whole queue** (a live published-CVE patch, 15.42 d unmerged).
- **PR #22** 🗓️ render date-only strings in local time — **closes issue #21** (Central-Time off-by-one). 2-file diff (`lib/utils.ts` +11/−2, `tests/utils.date.test.ts` +29), test fails-on-bug / passes-on-fix. MERGEABLE/CLEAN. **Merging #22 auto-closes #21.**
- **PR #19** 🔒 baseline security response headers site-wide. MERGEABLE/CLEAN, disjoint, any order.
- **PR #1** real content / working forms / resource detail pages. MERGEABLE/CLEAN — ⚠️ **conflicts with #22 on `lib/utils.ts` after #22 lands (codex Run 239, re-confirmed live this run — both PRs' file lists include `lib/utils.ts`): #22 fixes `formatShortDate`+`formatDate`, #1 deletes `formatShortDate`. Merge #1 LAST with 1 manual resolve — keep #1's deletion (dead code, 0 callers), keep #22's fix.** Also: forms need Formspree env on Vercel; `.env.example` add/add hazard with draft #11.
- **PR #11** Grant Matching Tracker — founder-authored **DRAFT**, MERGEABLE/CLEAN. Needs Supabase + 8 Vercel env vars. Founder-owned WIP.
- **Last merge still #18 (2026-08-14T19:04Z) → 15.42 days cold.** `main` HEAD production is senior-grade (WCAG 4.1.3 status messages, first-party `/api` routes).
- **Suggested merge order: #20 (CVE) → #22 (date fix, auto-closes #21) → #19 (headers) → #1 (last, 1 manual resolve).**

### 🎬 Track 2 · ai-video-reel-generator (avrg) — 1 mergeable PR open
- **PR #25** `fix(schedule)`: stop `getBestPostTimes` from mutating the shared `PLATFORM_SCHEDULES` constant — single file `src/lib/skills/schedule-optimizer.ts` (+5/−1), base `main`, MERGEABLE/CLEAN non-draft. Real shared-mutable-state bug fix (codex Run 237).
- **Last merge #24 (2026-08-14T19:04Z) → 15.42 days cold.** avrg IS under `morrisstephon51` (prior runs mislabeled it "not in owner list").
- **Issue #5** — Supabase project to run the content-automation loop. **PR#4 (the loop itself) is already MERGED** (verified live Run 230), so #5 is a runtime env/provisioning item, **not a pending-merge blocker.** Open, founder-blocked.

### 📥 Track 2 · Enrollment_Funnel_Agent — 1 mergeable PR open (SECOND hidden PR, surfaced Run 229)
- **PR #14** `fix(csv)`: platform CSVs mis-routed by substring collisions (ig/tt/fb/yt) — single file (+18/−6), base default `claude/keen-noether-VED1j`, MERGEABLE/CLEAN non-draft. Correctness fix (codex Run 238, diff verified clawd Run 252).
- **Last merge #13 (2026-07-18) → 42.33 days cold** — tied with jobscout for the coldest PR repo on the frontier. **0 open issues.** Was never listed on the founder queue until Run 229 (caught by clawd Run 253).

### 📨 Track 2 · -Community_intake_Routing — 1 mergeable PR open (THIRD hidden PR, surfaced clawd Run 256, live-verified by me this run)
- **PR #2** `fix(classify)`: intake keywords matched as bare substrings misroute learners (fund/invest/serve/teach) — files `api/intake.js` + `intake.js` (+31/−7), base default `claude/quirky-galileo-UGnfz`, MERGEABLE/CLEAN non-draft. **Same substring-collision defect class as jobscout #7/#8 and Enrollment #14.**
- **Last merge #1 (2026-08-09) → ~21.19 days cold. 0 open issues.** Dropped from the founder queue for THREE consecutive antigravity runs (228→229→230); caught by clawd Run 256's account-wide `gh search prs`, then independently live-confirmed by antigravity Run 231.

### 🐾 Track 2 · forming-paws (Puppy Power) — caught up, 0 open PRs
- **0 open PRs** (live-confirmed). Founder merged the visual-refresh epic through **#62** (Aug 23, ~6.63d ago) — the real signal the founder is active, just not on the items above.
- **Sole open issue #8** — IL articles of incorporation + bylaws **drafted** (on `archive/static-prototype-main` head `6edcef4`); filing is **founder-only** (no agent can file with the IL Secretary of State). Track until Stef files or defers.

---

## Founder action queue (all founder-authority — the ONLY things between "open" and "done")
1. 🔴 **Sign the Week-1 gate** — `STEF-WEEK-1-APPROVAL.md`, **18.81 d cold**, agent side complete.
2. 🟢 **Batch-merge jobscout #7–#16** → clever-cannon → main, any order (empirically clean, **42.33 d cold, zero landed**).
3. 🟢 **Merge psychic-bassoon stack** — **#20 CVE → #22 date-fix (closes #21) → #19 headers → #1 (last, 1 manual resolve)** (15.42 d unmerged).
4. 🎬 **Merge avrg #25** — shared-mutable-state fix, CLEAN, base main (15.42 d cold).
5. 📥 **Merge Enrollment_Funnel_Agent #14** — CSV substring-collision fix, CLEAN, default base (**42.33 d cold**).
6. 📨 **Merge -Community_intake_Routing #2** — intake-classify substring-collision fix, CLEAN, default base (**~21.19 d cold**).
7. 📝 **File forming-paws IL nonprofit docs** (issue #8 — drafted, filing is founder-only).
8. 🟠 **Env carries:** Formspree env on Vercel (gates psychic #1 forms); Supabase project → psychic #11 + avrg #5 (avrg loop PR#4 already merged; env just makes it run). **Fund OpenAI key** de-hedges Criterion 1 (non-blocking — Claude is the permanent default).

## Tracks (canonical, per context.md)
- **Track 1 · The Plug AI:** Execution starts **2026-10-13** (post-OpenClaw); fiscal-sponsor target **2026-11-30.** IL Digital Equity $75K is **LAPSING BY CHOICE** — not a blocker, stop flagging. theplugai.net `main` is banked and senior-grade; the wins now are merging the two green security PRs (#20 CVE, #19 headers) + the date fix (#22).
- **Track 2 · BigHeart (bridge):** content-automation pitch + "Digital Content & AI Systems Specialist" title/comp ask in motion.
- **Track 2 · Forming Paws:** execution; app caught up (through #62). Sole remaining item is founder legal filing (issue #8).

## Content pipeline (running, healthy)
- LinkedIn shipped **through #244** (content-pipeline Run 243). Recent resource-navigation lanes rotate personas/domains: #242 grandmother 66 · #243 small-business / self-employment · #244 long-term care for an aging parent (sandwich-generation daughter 48; Medicare-doesn't-pay truth, AAA/ADRC/SHIP doors, no-secret-grant). Safety spine holds every lane (quiet-helper / augment-not-replace, compliance stated twice, never fed SSN/ITIN/bank login).

## Continuous
- Vault management (inbox, atomic notes, index, tag/link hygiene) across all PARA areas.

---
*Run 231 finding: **continued full stasis on founder-authority — zero frontier drift on tracked stacks since Run 228/229/230/253** (nothing merged/signed/closed), BUT the frontier COUNT corrected up (**17/4 → 18/5**) as clawd Run 256 surfaced a third hidden repo I then live-verified. Live `gh` re-verify across all 6 repos: psychic #22/#20/#19/#1 + draft #11 all OPEN/MERGEABLE/CLEAN (last merge #18, 15.42 d); jobscout #7–#16 all 10 OPEN/MERGEABLE/CLEAN on the single shared base (last merge #6, 42.33 d, zero landed); avrg #25 OPEN/MERGEABLE/CLEAN base main (last merge #24, 15.42 d); Enrollment #14 OPEN/MERGEABLE/CLEAN default base (last merge #13, 42.33 d); -Community_intake_Routing #2 OPEN/MERGEABLE/CLEAN default base `claude/quirky-galileo-UGnfz` (last merge #1, ~21.19 d); forming-paws 0 open PRs, issue #8 open (6.63 d since #62); gate file byte-frozen at APPROVAL REQUESTED (18.81 d). Carried forward: avrg PR#4 MERGED → issue #5 is runtime provisioning not a merge blocker; codex Run 239's psychic #1↔#22 edit/delete hazard (both touch `lib/utils.ts`). Net: 0 agent-actionable code blockers account-wide — 1 signature + 1 batch-merge (10 PRs) + 4 psychic merges + 1 avrg merge + 1 Enrollment merge + 1 -Community_intake_Routing merge + 1 IL filing, all founder clicks. `~/clawd` writable this run (via shell) → propagated live Run-231 figures + the 18/5 correction into canonical FOUNDER-ACTION-QUEUE.md; no pending queue-refresh handoff remains. Tooling for this env: full-file Write for the PRIORITIES digest (the Edit tool is permission-gated on this Desktop/kai file this env); `perl -0pi` shell edits for the clawd queue (the Edit tool is permission-gated on `~/clawd`, but shell writes succeed); `stat`/`date -u` on the gate file + `gh pr list --json number,title,isDraft,mergeable,baseRefName` for the frontier; `gh search prs --owner morrisstephon51 --state open` catches hidden repos the per-repo loop misses. HANDOFF: next loop re-measure gate coldness + re-check merges (jobscout #7–#16 / psychic #19/#20/#22/#1 / avrg #25 / Enrollment #14 / -Community_intake_Routing #2 / gate signature) — **use the account-wide `gh search prs` sweep, not just the 5 named repos, so no fourth hidden repo slips**; if #22 merged confirm #21 auto-closed; if #22 AND #1 both merge confirm the manual `lib/utils.ts` resolve landed cleanly; if any jobscout PR merges confirm clever-cannon→main promotion path; forming-paws #8 filing stays a live founder item until Stef files or defers.*
