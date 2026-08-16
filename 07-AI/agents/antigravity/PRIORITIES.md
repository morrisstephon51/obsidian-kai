# Antigravity — Active Priorities Digest

*Refreshed by antigravity **Run 182** · 2026-08-16. FULL live re-verification, not a trust-the-bus pass: `git fetch origin main` on forming-paws, account-wide `gh search prs/issues` + per-PR `gh pr view --json mergeable,mergeStateStatus,isDraft,commits,files`, and the P1 gate file mtime. **What changed since Run 181:** (1) the open loop this digest was tracking — forming-paws issue **#42**, the health-doc redirect twin — is **RESOLVED IN-PLACE**: codex folded the fix **plus a route-level regression test** into the already-open **PR #39** (commit `986a2d7`), so **merging #39 now closes #42 by itself** — no separate post-merge edit remains. (2) Timeline advanced: today is **Aug 16**, so the Aug-17 3pm go/no-go is now **T-1**. (3) Content pipeline advanced **#195 → #196** (new medical-debt/hospital-bill lane). Everything below is LIVE-verified this run.*

---

## 🔴 THE ONE THING — Sole open P1 gate is FOUNDER sign-off
- `~/clawd/AI-Organization/STEF-WEEK-1-APPROVAL.md` **still reads "APPROVAL REQUESTED"** — mtime **Aug 11 09:31**, untouched (re-verified live this run → now **5 days** cold). The report itself is **✅ Week-1 PASS (12 tasks, 3.34× avg speedup, zero escalations, 8.6/10)** and recommends APPROVE. Everything is agent/supervisor-signed; **only Stef's written checkmark is missing.**
- **Timeline is now T-1:** today is **Aug 16**. **Aug-17 3:00 PM CDT go/no-go (T-1 day)**, **Aug-18 formal Phase-2 Week-1 gate (T-2 days).** Every agent-side item stays green — the *only* moving part left is the founder's signature, and the window to sign before tomorrow's go/no-go is nearly shut.
- Clearing the merge queue is a *different* founder action from signing this gate. This gate is the P1 blocker.

## P1 — OpenClaw Phase 1-4 (gates all Track 1/2 execution)
- **LIVE 2026-07-27 → 2026-08-17.** Completing Phase 1-4 is Stef's Priority 1; target **2026-10-12.**
- Phase-2 Week-1 sign-off (due 08-13) is **DONE agent-side** (6/6 verification PASS, `PHASE-2-WEEK-1-REPORT.md`). Sole open item = the founder gate above.
- **Aug 14-17 pre-gate cost-tracking must-pass (window OPEN, closes with the go/no-go):** `test-cost-tracking.sh --live` → 28/28 + `cost-tracker.js --week 2026-08-18 --strict` → exit 0.
- **ADR-008 (ACCEPTED):** Claude Sonnet 4.6 is the **PERMANENT code-gen default** — not conditional on OpenAI funding. A failed Claude call FAILS the task (no silent downgrade to ChatGPT). `builder` owns code-gen. gpt-4 REFUSED.

## 🟠 BLOCKER — OpenAI billing (OPEN, NON-BLOCKING)
- `OPENAI_API_KEY` authenticates but has **no credits** → `credit_balance_exhausted`. A `GET /v1/models` 200 is NOT evidence of usable credit. Repro: `node AI-Organization/verify-credentials.js`.
- **Non-blocking** (ADR-008 makes Claude the permanent default), but it's the only thing keeping **Criterion 1 hedged** + gates the Phase-2 ChatGPT leg. Funding it de-hedges Criterion 1.

---

## Merge frontier — LIVE-VERIFIED THIS RUN (Run 182): 14 open · 9 drafts · 5 ready · 4 issues
*Account-wide `gh search prs/issues` + per-PR `gh pr view --json`. Counts unchanged vs Run 181; the movement is INSIDE #39.*

### 🧱 Base moved — forming-paws `main` is @3a005a6 (NOT @407e7d3)
- On **2026-08-15 21:27Z** a **Brand-foundation** commit was pushed **direct to `main`** (not via PR): `3a005a6` "Forming Paws logo, palette tokens, display/body fonts". Parent is `407e7d3` (the old "frozen" SHA). Re-confirmed live via `git fetch` this run (`origin/main` HEAD = `3a005a6`).
- The brand commit touches only `app/globals.css`, `app/layout.tsx`, `public/admin.html`, `public/logo.svg`, `public/styles.css`, `tailwind.config.ts` — **fully path-disjoint** from all four stacked correctness PRs. That is why GitHub still evaluates #38/#39/#40/#41 as **MERGEABLE / CLEAN** against the new base: the merge-any-order guarantee is **INTACT** (all four re-verified `draft=false, mergeable=MERGEABLE, mergeStateStatus=CLEAN` this run).
- **KEY INSIGHT (still holds):** a direct-push actor (founder or proxy) was active on the repo on Aug-15 yet touched NEITHER the merge queue NOR the P1 gate file. The founder signature + 5-PR review remain the only moving parts.

### 🟢 Ready to merge now (5 non-draft MERGEABLE/CLEAN — verified against @3a005a6)
- **forming-paws #38** — reject a future **birth date** by the local calendar, not a UTC instant. Files: `app/dogs/new/NewDogForm.tsx`, `lib/dogBirthDate.ts`, `tests/unit/dogBirthDate.test.ts`. **Code-only.**
- **forming-paws #39** — reject a future **health-doc document_date** by the members' calendar **+ now also carries the #42 redirect-twin fix** (see below). Commits: `7bbed64` (date guard) + `986a2d7` (route post-upload redirect through the public host). Files: `app/api/upload/health-doc/route.ts`, `lib/dates.ts`, `tests/unit/dates.test.ts`, **`tests/unit/health-doc-upload-route.test.ts`** (new 3-case route regression test). **Code-only. Merging #39 auto-closes issue #42.**
- **forming-paws #40** — **browse max-age** filter off by a full year vs the age on the card (mirror of merged #34 min-age fix). File: `supabase/migrations/0024_browse_dogs_max_age_calendar_band.sql`. **Migration-only → REQUIRES a Supabase 0024 apply + browse smoke-test AFTER merge** (codex proved by calendar simulation only; its env has no live Postgres, and pg-mem's interval engine is non-conformant).
- **forming-paws #41** — post-upload redirect went to the internal Vercel host instead of the public domain (`new URL(path, request.url)` ignores `x-forwarded-host`), bouncing members off-domain after a *successful* upload, often into a deployment-protection login wall. Fixed via new `lib/http.ts redirectToPath()` built on the repo's own tested `getRequestOrigin` helper. Files: `app/api/upload/photo/route.ts`, `lib/http.ts`, `tests/unit/http.test.ts`. **Code-only.**
- **psychic-bassoon #1** (Track 1 · The Plug AI) — "Add real content, working forms, resource detail pages" (`+7718/-61`). MERGEABLE, but **gated on setting Formspree env vars on Vercel** before forms submit.

**✅ All four forming-paws PRs remain FULLY FILE-DISJOINT from each other AND from the new brand-foundation main → merge in ANY order, no conflict.** #40 is migration-only so it can't collide with the app/lib/test paths of #38/#39/#41. (#41 fixes the photo route via `lib/http.ts`; #39 fixes the health-doc route inline — different files, no add/add collision.)

**✅ OPEN LOOP CLOSED IN-PLACE (was the standing follow-up in Run 181):** the **twin** health-doc upload route carried the *same* proxy-unsafe redirect that #41 fixed on the photo route. codex has now **folded the fix + a route-level regression test directly into PR #39** (commit `986a2d7`, "Closes #42 on merge") rather than opening a new PR — throughput, not inventory. **There is no longer a separate post-merge edit to make:** merging #39 both lands the date guard AND closes the upload-redirect pair. Issue #42 stays OPEN only until #39 merges.

### ⏸️ Drafts (9 — GitHub blocks merge until un-drafted)
- **psychic-bassoon #11** — Grant Matching Tracker. Needs Supabase project + 4 Vercel env vars. `.env.example` add/add vs #1 → keep BOTH env blocks (non-overlapping, concatenate).
- **command-center-redirect #1** — PIN-locked dashboard. **Cross-repo ordering constraint:** before un-drafting, (a) un-draft+merge psychic #11 and confirm the public domain serves `/grants` 200; (b) repoint all 9 grant links off the SSO-gated `-cam6stef` preview to the canonical public domain, else public visitors hit a Vercel login wall.
- **Link-inbio #5** (Obsidian ops-vault docs) · **#6** (résumé PDF, binary). Low-stakes.
- **Dormant, don't surface as fresh work:** content-machine #3/#4/#5/#10 + `----Workspace-notes` #1 (cold since Jun 28).

### Account-wide open issues (4 — all NON-actionable by an agent)
- forming-paws **#42** — health-doc redirect twin of #41. **Fix already staged in PR #39 (commit `986a2d7`); auto-closes on merge.** No agent action left; waits on #39 merging.
- forming-paws **#8** — IL articles of incorporation + bylaws drafted → founder legal review/filing.
- ai-video-reel-generator **#5** — Supabase project setup → founder-gated (also blocks its PR#4 loop).
- skills-introduction-to-git **#1** — git learning exercise.
- **→ 0 agent-actionable open issues account-wide.** The bottleneck is founder review, not missing fixes.

---

## Tracks
- **Track 1 · The Plug AI:** Execution starts **2026-10-13** (post-OpenClaw); fiscal-sponsor target **2026-11-30.** IL Digital Equity $75K **LAPSING BY CHOICE** — not a blocker, stop flagging. psychic-bassoon PRs are **banked ahead of schedule** — the win now is clearing review *cleanly*, not piling on more.
- **Track 2 · BigHeart (bridge):** content-automation pitch + "Digital Content & AI Systems Specialist" title/comp ask in motion.
- **Track 2 · Forming Paws / Puppy Power:** execution phase, no more planning. Prototype live; brand foundation now on `main`. Codex is systematically clearing forming-paws date/calendar/upload correctness bugs, one root-cause PR at a time — **4 stacked and disjoint** (#38/#39/#40/#41), with the #42 twin now consolidated into #39.

## Content pipeline (running)
- LinkedIn shipped **through #196** (content-pipeline Run 196, items 321). Recent resource-navigation lanes: **#192 eviction/rental-assistance/tenant-rights** · **#193 SNAP/food** · **#194 funeral/burial-costs** · **#195 utility/energy-bill assistance** (LIHEAP, shutoff protections, deferred-payment, 211) · **#196 medical-debt / hospital-bill** (hospital charity care/financial assistance by name, itemized-bill error review, No Surprises Act, presumptive/retroactive Medicaid + financial counselor, interest-free hospital plan before any card; scam-warned phantom-debt collectors, settlement-fee scams, "bill past due" phishing, deferred-interest medical-card trap). Safety spine held every lane: quiet-helper / augment-not-replace, compliance stated twice, no eligibility or amount promised, never feed it an SSN/account/insurance ID/card number.

## Open infra carry
1. 🔴 **Stef's written Week-1 sign-off** — the one remaining Aug-18 gate item (agent side complete). **T-1** to the Aug-17 3pm go/no-go.
2. 🔴 **Fund OpenAI key** — de-hedges Criterion 1; code-gen already covered by Claude default.
3. **Aug 14-17 cost-tracking must-pass:** 28/28 + `--strict` exit 0. Window open, closes with the go/no-go.
4. **Founder-review the frontier:** clear the **5 ready** — forming-paws #38/#39/#40/#41 (any order; **#39 also closes #42**; #40 needs the Supabase 0024 apply + smoke-test after merge) + psychic #1 (set Formspree env first). Then the drafts (un-draft #11 before command-center #1, and repoint its 9 links).
5. 🔴 **Year-aware deadline filter in the grant loop** — deterministic post-filter (drop candidates whose deadline year < current or date < today); NOT LLM self-check (Perplexity's year-reasoning is non-deterministic). Grant-drift loop otherwise CLOSED.
6. **Env carries:** Formspree vars on Vercel → psychic #1. Supabase project + 4 Vercel env vars → psychic #11 + ai-video-reel-generator #5. `ANTHROPIC_API_KEY` for aeos/orchestrator (load-bearing under ADR-008).
7. **~~Post-merge follow-up on the #42 twin~~ — DONE:** the fix is folded into PR #39 (`986a2d7`); no separate edit remains, #42 auto-closes when #39 merges.
8. **Font follow-up (codex Run 190, NOT shipped):** Google Fonts render-blocking `@import` vs `next/font` (perf + IP-privacy) — founder decision, collides with active brand work; do not ship blind.

## Continuous
- Vault management (inbox, atomic notes, index, tag/link hygiene) across all PARA areas.

---
*Tooling note (this env): full-file **Write** is the reliable path for PRIORITIES.md + state.md. Per-repo + account-wide `gh` and `git fetch` are authoritative and matched the bus's claims this run (bus was accurate for codex Run 191's #42-into-#39 fold and content Run 196; still verified rather than trusted).*
