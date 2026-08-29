# Antigravity — Active Priorities Digest

*Refreshed by antigravity **Run 229** · 2026-08-29 (~05:48Z UTC). This run: re-scanned context (context.md canonical + world.md), polled the bus, **re-measured the sole cold P1 gate** (`stat` on `STEF-WEEK-1-APPROVAL.md` → still `**Status:** APPROVAL REQUESTED`, byte-frozen 3125 b, mtime `2026-08-11` → now **17.84 days cold**), and **source-verified the entire merge frontier live via `gh`** (verify-don't-trust-the-bus) across **all 5 active repos** — psychic-bassoon, job_opportunity_scanner, ai-video-reel-generator, Enrollment_Funnel_Agent, and forming-paws. **Delta vs Run 228 & clawd Run 253: ZERO frontier change** — nothing merged, nothing signed, nothing closed; the board aged ~0.5 day. **This run FULLY FOLDS IN clawd Run 253's correction:** the frontier hid TWO real CLEAN/MERGEABLE PRs — avrg #25 (surfaced in the interim pass) and **Enrollment_Funnel_Agent #14 (surfaced now)**. Both repos ARE owned by `morrisstephon51`. True frontier = **17 PRs / 4 repos** (16 non-draft MERGEABLE + 1 draft). Also folded codex Run 239's **psychic #1↔#22 merge-order hazard**. `~/clawd` writable this run → propagated live Run-229 figures into canonical `FOUNDER-ACTION-QUEUE.md`; no pending queue-refresh handoff remains. Coldness clocks: jobscout 40.84→41.36 d, enroll 41.36 d (now tracked), psychic 13.92→14.45 d, avrg 13.92→14.45 d, gate 17.32→17.84 d.*

---

## 🔴 THE ONE THING — sole open P1 is the FOUNDER signature (now 17.84 days cold)
- `~/clawd/AI-Organization/STEF-WEEK-1-APPROVAL.md` **still reads `**Status:** APPROVAL REQUESTED`** — mtime **2026-08-11**, re-verified on disk this run → **17.84 days cold** (up from 16.72 d at Run 228; byte-for-byte unmoved since Aug 11, 3125 bytes).
- The report is **✅ Week-1 PASS** (12 tasks, 3.34× avg speedup, zero escalations, 8.6/10 confidence, 100% cost tracked) and recommends **APPROVE → proceed to Phase-2 Week-2**. Everything is agent/supervisor-signed; **only Stef's written checkmark is missing.**
- **The gate is aging, not thawing.** No agent can click it. One-line written approval (email, or set the in-file status line to ✅) closes it.

## P1 — OpenClaw Phase 1-4 (gates all Track 1/2 execution)
- **Phase 1 LIVE 2026-07-27 → 2026-08-17.** Completing Phase 1-4 is Stef's Priority 1; target **2026-10-12.**
- Phase-2 Week-1 sign-off is **DONE agent-side.** Sole open item = the founder gate above.
- **ADR-008 (ACCEPTED):** Claude Sonnet 4.6 is the **PERMANENT code-gen default** — a failed Claude call FAILS the task (no silent downgrade). Not conditional on OpenAI funding.

---

## Merge frontier — source-verified live at GitHub, Run 229
*Account-wide: **17 open PRs across 4 repos — 16 non-draft MERGEABLE/CLEAN + 1 draft** + **1 cold governance gate** + **3 open issues.** Net: **0 agent-actionable code blockers.** Every lever is founder-authority (sign / merge / file / set env). All states below confirmed live this run via `gh pr list` / `gh issue list` (`mergeable` + `mergeStateStatus` + `isDraft`).*

### 🟢 Track 2 · job_opportunity_scanner — 10-PR scorer batch, EMPIRICALLY batch-mergeable
- **PRs #7–#16 — all 10 OPEN, non-draft, MERGEABLE/CLEAN**, base default `claude/clever-cannon-IDh3G` (live-confirmed: 10 open, all CLEAN, single shared base).
- codex Run 236 **actually merged all ten into `clever-cannon` → 0 conflicts, 9/9 tests pass on the merged tree**; Run 239 re-confirmed 10/10 CLEAN + 58 pytest green. Verified batch-safe comment on anchor PR #16: batch-merge #7–#16 → clever-cannon → main, **any order, no rebases.**
- **Last merge still #6 (2026-07-18) → 41.36 days cold; zero of #7–#16 landed.** Coverage: token-boundary location/title scoring, `$85k` salary parse, "trainer" title signal, recency-window filters (weeks/months/30+ days ago, ISO posted_date), config-driven salary floor, loud-fail on count mismatch, KeyError-safe alerts.

### 🟢 Track 1 · psychic-bassoon (theplugai.net) — `main` hardened; 4 mergeable PRs open, NONE merged
- **PR #20** 🔒 bump Next.js 14.2.5 → 14.2.35 — closes published CVEs (incl. CVE-2025-29927 middleware-auth-bypass class). MERGEABLE/CLEAN. **Highest-value single click on the whole queue** (a live published-CVE patch, 14.45 d unmerged).
- **PR #22** 🗓️ render date-only strings in local time — **closes issue #21** (Central-Time off-by-one). 2-file diff (`lib/utils.ts` +11/−2, `tests/utils.date.test.ts` +29), test fails-on-bug / passes-on-fix. MERGEABLE/CLEAN. **Merging #22 auto-closes #21.**
- **PR #19** 🔒 baseline security response headers site-wide. MERGEABLE/CLEAN, disjoint, any order.
- **PR #1** real content / working forms / resource detail pages. MERGEABLE/CLEAN — ⚠️ **conflicts with #22 on `lib/utils.ts` after #22 lands (codex Run 239): #22 fixes `formatShortDate`+`formatDate`, #1 deletes `formatShortDate`. Merge #1 LAST with 1 manual resolve — keep #1's deletion (dead code, 0 callers), keep #22's fix.** Also: forms need Formspree env on Vercel; `.env.example` add/add hazard with draft #11.
- **PR #11** Grant Matching Tracker — founder-authored **DRAFT**, MERGEABLE/CLEAN. Needs Supabase + 8 Vercel env vars. Founder-owned WIP.
- **Last merge still #18 (2026-08-14T19:04Z) → 14.45 days cold.** `main` HEAD production is senior-grade (WCAG 4.1.3 status messages, first-party `/api` routes).
- **Suggested merge order: #20 (CVE) → #22 (date fix, auto-closes #21) → #19 (headers) → #1 (last, 1 manual resolve).**

### 🎬 Track 2 · ai-video-reel-generator (avrg) — 1 mergeable PR open
- **PR #25** `fix(schedule)`: stop `getBestPostTimes` from mutating the shared `PLATFORM_SCHEDULES` constant — single file `src/lib/skills/schedule-optimizer.ts` (+5/−1), base `main`, MERGEABLE/CLEAN non-draft. Real shared-mutable-state bug fix (codex Run 237).
- **Last merge #24 (2026-08-14T19:04Z) → 14.45 days cold.** avrg IS under `morrisstephon51` (prior runs mislabeled it "not in owner list").
- **Issue #5** — Supabase project needed to unblock the content-automation loop (PR#4). Open, founder-blocked env.

### 📥 Track 2 · Enrollment_Funnel_Agent — 1 mergeable PR open (SECOND hidden PR, surfaced this run)
- **PR #14** `fix(csv)`: platform CSVs mis-routed by substring collisions (ig/tt/fb/yt) — single file (+18/−6), base default `claude/keen-noether-VED1j`, MERGEABLE/CLEAN non-draft. Correctness fix (codex Run 238, diff verified clawd Run 252).
- **Last merge #13 (2026-07-18) → 41.36 days cold** — tied with jobscout for coldest PR repo on the frontier. **0 open issues.** Was never listed on the founder queue until Run 229 (caught by clawd Run 253).

### 🐾 Track 2 · forming-paws (Puppy Power) — caught up, 0 open PRs
- **0 open PRs** (live-confirmed). Founder merged the visual-refresh epic through **#62** (Aug 23, ~5.66d ago) — the real signal the founder is active, just not on the items above.
- **Sole open issue #8** — IL articles of incorporation + bylaws **drafted** (on `archive/static-prototype-main` head `6edcef4`); filing is **founder-only** (no agent can file with the IL Secretary of State). Track until Stef files or defers.

---

## Founder action queue (all founder-authority — the ONLY things between "open" and "done")
1. 🔴 **Sign the Week-1 gate** — `STEF-WEEK-1-APPROVAL.md`, **17.84 d cold**, agent side complete.
2. 🟢 **Batch-merge jobscout #7–#16** → clever-cannon → main, any order (empirically clean, **41.36 d cold, zero landed**).
3. 🟢 **Merge psychic-bassoon stack** — **#20 CVE → #22 date-fix (closes #21) → #19 headers → #1 (last, 1 manual resolve)** (14.45 d unmerged).
4. 🎬 **Merge avrg #25** — shared-mutable-state fix, CLEAN, base main (14.45 d cold).
5. 📥 **Merge Enrollment_Funnel_Agent #14** — CSV substring-collision fix, CLEAN, default base (**41.36 d cold**).
6. 📝 **File forming-paws IL nonprofit docs** (issue #8 — drafted, filing is founder-only).
7. 🟠 **Env carries:** Formspree env on Vercel (gates psychic #1 forms); Supabase project → psychic #11 + avrg #5. **Fund OpenAI key** de-hedges Criterion 1 (non-blocking — Claude is the permanent default).

## Tracks (canonical, per context.md)
- **Track 1 · The Plug AI:** Execution starts **2026-10-13** (post-OpenClaw); fiscal-sponsor target **2026-11-30.** IL Digital Equity $75K is **LAPSING BY CHOICE** — not a blocker, stop flagging. theplugai.net `main` is banked and senior-grade; the wins now are merging the two green security PRs (#20 CVE, #19 headers) + the date fix (#22).
- **Track 2 · BigHeart (bridge):** content-automation pitch + "Digital Content & AI Systems Specialist" title/comp ask in motion.
- **Track 2 · Forming Paws:** execution; app caught up (through #62). Sole remaining item is founder legal filing (issue #8).

## Content pipeline (running, healthy)
- LinkedIn shipped **through #244** (content-pipeline Run 243). Recent resource-navigation lanes rotate personas/domains: #242 grandmother 66 · #243 small-business / self-employment · #244 long-term care for an aging parent (sandwich-generation daughter 48; Medicare-doesn't-pay truth, AAA/ADRC/SHIP doors, no-secret-grant). Safety spine holds every lane (quiet-helper / augment-not-replace, compliance stated twice, never fed SSN/ITIN/bank login).

## Continuous
- Vault management (inbox, atomic notes, index, tag/link hygiene) across all PARA areas.

---
*Run 229 finding: **continued full stasis on founder-authority — zero frontier drift since Run 228/253** (nothing merged/signed/closed). Live `gh` re-verify across all 5 repos: psychic #22/#20/#19/#1 + draft #11 all OPEN/MERGEABLE/CLEAN (last merge #18, 14.45 d); jobscout #7–#16 all 10 OPEN/MERGEABLE/CLEAN on the single shared base (last merge #6, 41.36 d, zero landed); avrg #25 OPEN/MERGEABLE/CLEAN base main (last merge #24, 14.45 d); Enrollment #14 OPEN/MERGEABLE/CLEAN default base (last merge #13, 41.36 d); forming-paws 0 open PRs, issue #8 open; gate file byte-frozen at APPROVAL REQUESTED (17.84 d). **Accuracy fix (clawd Run 253 fully folded): true frontier is 17 PRs/4 repos — the queue had hidden avrg #25 AND Enrollment #14.** Also folded codex Run 239's psychic #1↔#22 edit/delete merge-order hazard. Net: 0 agent-actionable code blockers account-wide — 1 signature + 1 batch-merge (10 PRs) + 4 psychic merges + 1 avrg merge + 1 Enrollment merge + 1 IL filing, all founder clicks. `~/clawd` writable this run → propagated live Run-229 figures into canonical FOUNDER-ACTION-QUEUE.md; no pending queue-refresh handoff remains. Tooling for this env: full-file Write for digests; `stat`/`date -r` on the gate file + `gh pr list --json number,title,isDraft,mergeable,mergeStateStatus,baseRefName` for the frontier. HANDOFF: next loop re-measure gate coldness + re-check merges (jobscout #7–#16 / psychic #19/#20/#22/#1 / avrg #25 / Enrollment #14 / gate signature); if #22 merged confirm #21 auto-closed; if #22 AND #1 both merge confirm the manual `lib/utils.ts` resolve landed cleanly; if any jobscout PR merges confirm clever-cannon→main promotion path; forming-paws #8 filing stays a live founder item until Stef files or defers.*
