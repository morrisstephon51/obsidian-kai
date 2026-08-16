# Antigravity — Active Priorities Digest

*Refreshed by antigravity **Run 184** · 2026-08-16. FULL live re-verification, not a trust-the-bus pass: `git fetch origin main` on forming-paws, account-wide `gh search prs/issues`, per-PR `gh pr view --json mergeable,mergeStateStatus,isDraft,files,closingIssuesReferences`, and the P1 gate file mtime. **What changed since Run 183: nothing moved on the frontier — and that is the finding.** Two more agent cycles ran (codex Run 193, content-pipeline Run 198) and the merge queue + founder gate are byte-for-byte where Run 183 left them. (1) **codex Run 193 shipped NO new PR** (anti-inventory rule): a fresh full source review of forming-paws found the codebase well-hardened (only a cosmetic misplaced `robots.ts` comment, logged not shipped); codex instead brought `pr-review-merge-guide.md` current (docs-only, zero code). (2) Content pipeline advanced **#197 → #198** (new TAX / IRS-DEBT ministry lane). (3) **Timeline is now T-1 and this is the LAST FULL DAY:** today is **Aug 16**; the **Aug-17 3:00 PM CDT go/no-go is TOMORROW.** Everything below is LIVE-verified this run.*

---

## 🔴 THE ONE THING — Sole open P1 gate is FOUNDER sign-off (window closes tomorrow)
- `~/clawd/AI-Organization/STEF-WEEK-1-APPROVAL.md` **still reads "APPROVAL REQUESTED"** — mtime **Aug 11 09:31**, re-verified live this run → now **5 days cold**. The report itself is **✅ Week-1 PASS (12 tasks, 3.34× avg speedup, zero escalations, 8.6/10)** and recommends APPROVE. Everything is agent/supervisor-signed; **only Stef's written checkmark is missing.**
- **Timeline is T-1 — today (Aug 16) is the last full day before the gate.** **Aug-17 3:00 PM CDT go/no-go (tomorrow)**, **Aug-18 formal Phase-2 Week-1 gate (T-2).** Every agent-side item stays green — the *only* moving part left is the founder's signature, and the window to sign before tomorrow's go/no-go is essentially down to today.
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

## Merge frontier — LIVE-VERIFIED THIS RUN (Run 184): 14 open · 9 drafts · 5 ready · 4 issues
*Account-wide `gh search prs/issues` + per-PR `gh pr view --json`. **Every count and per-PR field is identical to Run 183** — the frontier is frozen. The only movement in the world since Run 183 was docs (codex) and one LinkedIn post (content pipeline); neither touched the queue or the gate.*

### 🧱 Base still @3a005a6 (NOT @407e7d3) — re-confirmed live
- forming-paws `origin/main` HEAD = **`3a005a6`** "Brand foundation: Forming Paws logo, palette tokens, display/body fonts" (author Claude, **2026-08-15 21:27:42Z**), parent = **`407e7d3`** (the old "frozen" SHA). Pushed **direct to `main`**, not via PR. Re-verified via `git fetch` this run.
- The brand commit is path-disjoint from all four stacked correctness PRs (touches only `app/globals.css`, `app/layout.tsx`, `public/admin.html`, `public/logo.svg`, `public/styles.css`, `tailwind.config.ts`). That is why GitHub still evaluates #38/#39/#40/#41 as **MERGEABLE / CLEAN** against the new base — merge-any-order guarantee **INTACT** (all four re-verified `draft=false, mergeable=MERGEABLE, mergeStateStatus=CLEAN` this run).
- **KEY INSIGHT (still holds, now 1 day older):** a direct-push actor (founder or proxy) was active on the repo on Aug-15 yet touched NEITHER the merge queue NOR the P1 gate file. The founder signature + 5-PR review remain the only moving parts — and the actor demonstrably *has* repo access.

### 🟢 Ready to merge now (5 non-draft MERGEABLE/CLEAN — verified against @3a005a6)
- **forming-paws #38** — reject a future **birth date** by the local calendar, not a UTC instant. **3 files** (`app/dogs/new/NewDogForm.tsx`, `lib/dogBirthDate.ts`, `tests/unit/dogBirthDate.test.ts`). **Code-only.**
- **forming-paws #39** — reject a future **health-doc document_date** by the members' calendar **+ carries the #42 redirect-twin fix**. **4 files** (`app/api/upload/health-doc/route.ts`, `lib/dates.ts`, `tests/unit/dates.test.ts`, `tests/unit/health-doc-upload-route.test.ts`). Commits `7bbed64` (date guard) + `986a2d7` (route redirect through public host). **`closingIssuesReferences` = #42 (VERIFIED live this run) → merging #39 auto-closes issue #42.**
- **forming-paws #40** — **browse max-age** filter off by a full year vs the age on the card (mirror of merged #34 min-age fix). **1 file** (`supabase/migrations/0024_browse_dogs_max_age_calendar_band.sql`). **Migration-only → REQUIRES a Supabase 0024 apply + browse smoke-test AFTER merge** (codex proved by calendar simulation only; its env has no live Postgres, and pg-mem's interval engine is non-conformant).
- **forming-paws #41** — post-upload redirect went to the internal Vercel host instead of the public domain (`new URL(path, request.url)` ignores `x-forwarded-host`), bouncing members off-domain after a *successful* upload, often into a deployment-protection login wall. Fixed via new `lib/http.ts redirectToPath()` on the repo's tested `getRequestOrigin`. **3 files** (`app/api/upload/photo/route.ts`, `lib/http.ts`, `tests/unit/http.test.ts`). **Code-only.**
- **psychic-bassoon #1** (Track 1 · The Plug AI) — "Add real content, working forms, resource detail pages" (`+7718/-61`). MERGEABLE, but **gated on setting Formspree env vars on Vercel** before forms submit.

**✅ All four forming-paws PRs remain FULLY FILE-DISJOINT from each other AND from the brand-foundation main → merge in ANY order, no conflict.** #40 is migration-only so it can't collide with the app/lib/test paths of #38/#39/#41. #41 fixes the photo route via `lib/http.ts`; #39 fixes the health-doc route inline — different files, no add/add collision.

**✅ #42 CLOSE-REF STAYS REGISTERED:** live `gh pr view 39 --json closingIssuesReferences` → `{number: 42}`. Merging #39 lands the date guard AND auto-closes issue #42. #42 stays OPEN only until #39 merges. **Lesson still banked from Run 183: assert a close-ref only after `closingIssuesReferences` confirms it — a "Closes #N" in prose is not a registered reference.**

### ⏸️ Drafts (9 — GitHub blocks merge until un-drafted)
- **psychic-bassoon #11** — Grant Matching Tracker. Needs Supabase project + 4 Vercel env vars. `.env.example` add/add vs #1 → keep BOTH env blocks (non-overlapping, concatenate).
- **command-center-redirect #1** — PIN-locked dashboard. **Cross-repo ordering constraint:** before un-drafting, (a) un-draft+merge psychic #11 and confirm the public domain serves `/grants` 200; (b) repoint all 9 grant links off the SSO-gated `-cam6stef` preview to the canonical public domain, else public visitors hit a Vercel login wall.
- **Link-inbio #5** (Obsidian ops-vault docs) · **#6** (résumé PDF, binary). Low-stakes.
- **Dormant, don't surface as fresh work:** content-machine #3/#4/#5/#10 + `----Workspace-notes` #1 (cold since Jun 28).

### Account-wide open issues (4 — all NON-actionable by an agent)
- forming-paws **#42** — health-doc redirect twin of #41. **Fix staged in PR #39 (`986a2d7`) and a registered closing ref; auto-closes on merge.** No agent action left; waits on #39 merging.
- forming-paws **#8** — IL articles of incorporation + bylaws drafted → founder legal review/filing.
- ai-video-reel-generator **#5** — Supabase project setup → founder-gated (also blocks its PR#4 loop).
- skills-introduction-to-git **#1** — git learning exercise.
- **→ 0 agent-actionable open issues account-wide.** codex Run 193 re-confirmed this from the code side (full source review found nothing shippable). The bottleneck is founder review, not missing fixes.

---

## Tracks
- **Track 1 · The Plug AI:** Execution starts **2026-10-13** (post-OpenClaw); fiscal-sponsor target **2026-11-30.** IL Digital Equity $75K **LAPSING BY CHOICE** — not a blocker, stop flagging. psychic-bassoon PRs are **banked ahead of schedule** — the win now is clearing review *cleanly*, not piling on more.
- **Track 2 · BigHeart (bridge):** content-automation pitch + "Digital Content & AI Systems Specialist" title/comp ask in motion.
- **Track 2 · Forming Paws / Puppy Power:** execution phase, no more planning. Prototype live; brand foundation on `main`. Codex has systematically cleared the forming-paws date/calendar/upload correctness bugs into **4 stacked, disjoint PRs** (#38/#39/#40/#41), with the #42 twin folded into #39 and its close-ref registered. **codex Run 193 declared the codebase hardened — no new PR to invent.** Frontier = clear-the-queue, not write-more-code.

## Content pipeline (running)
- LinkedIn shipped **through #198** (content-pipeline Run 198, items 323). Recent resource-navigation lanes: **#193 SNAP/food** · **#194 funeral/burial-costs** · **#195 utility/energy-bill assistance** · **#196 medical-debt / hospital-bill** · **#197 CAR / AUTO-DEBT ministry** · **#198 TAX / IRS-DEBT ministry** (do NOT panic / verify the notice is real — the IRS mails first, call the number on the official notice or IRS.gov not a caller number; IRS payment options — installment agreement, possibly offer-in-compromise or currently-not-collectible; FREE help — VITA, Taxpayer Advocate Service, Low-Income Taxpayer Clinic; check/dispute the notice; EITC; legal aid/LITC; church benevolence + 211). Scam payload weighted for taxes: IRS-impersonation gift-card / arrest-threat calls, the "pennies-on-the-dollar" upfront-fee tax-relief trap (parallel to #197's title-loan trap), ghost preparers, refund-anticipation-loan traps, refund/account-locked phishing. Persona rotated back to a WOMAN (home health aide/CNA, 47) off man-38 (#197). Safety spine held every lane: quiet-helper / augment-not-replace, compliance stated twice, no eligibility/amount/right promised, never fed an SSN/ITIN/account/card number.

## Open infra carry
1. 🔴 **Stef's written Week-1 sign-off** — the one remaining Aug-18 gate item (agent side complete). **T-1: go/no-go is TOMORROW (Aug-17 3pm); today is the last full day to sign.**
2. 🔴 **Fund OpenAI key** — de-hedges Criterion 1; code-gen already covered by Claude default.
3. **Aug 14-17 cost-tracking must-pass:** 28/28 + `--strict` exit 0. Window open, closes with the go/no-go.
4. **Founder-review the frontier:** clear the **5 ready** — forming-paws #38/#39/#40/#41 (any order; **#39 also closes #42**; #40 needs the Supabase 0024 apply + smoke-test after merge) + psychic #1 (set Formspree env first). Then the drafts (un-draft #11 before command-center #1, and repoint its 9 links).
5. 🔴 **Year-aware deadline filter in the grant loop** — deterministic post-filter (drop candidates whose deadline year < current or date < today); NOT LLM self-check (Perplexity's year-reasoning is non-deterministic). Grant-drift loop otherwise CLOSED.
6. **Env carries:** Formspree vars on Vercel → psychic #1. Supabase project + 4 Vercel env vars → psychic #11 + ai-video-reel-generator #5. `ANTHROPIC_API_KEY` for aeos/orchestrator (load-bearing under ADR-008).
7. **Font follow-up (codex Run 190, NOT shipped):** Google Fonts render-blocking `@import` vs `next/font` (perf + IP-privacy) — founder decision, collides with active brand work; do not ship blind.

## Continuous
- Vault management (inbox, atomic notes, index, tag/link hygiene) across all PARA areas.

---
*Tooling note (this env): full-file **Write** is the reliable path for PRIORITIES.md + state.md. Per-repo + account-wide `gh` and `git fetch` are authoritative. Run 184 finding = **a verified-stable frontier**: two agent cycles passed (codex 193 docs-only + no PR, content 198) with the merge queue and founder gate untouched; a repo-access actor was present Aug-15 but signed nothing. When nothing moves, the value is proving nothing moved — and naming that the clock (T-1) is now the only variable in play.*
