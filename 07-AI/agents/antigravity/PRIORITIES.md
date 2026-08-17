# Antigravity — Active Priorities Digest

*Refreshed by antigravity **Run 188** · 2026-08-17. FULL live re-verification: `git fetch origin main` on forming-paws, account-wide `gh search prs/issues`, per-PR `gh pr view --json isDraft,mergeable,mergeStateStatus,files,closingIssuesReferences`, and the P1 gate mtime + status line. **Delta since Run 187: (1) A SEVENTH READY PR APPEARED — forming-paws `#46` "Site-wide navigation, rotating member tab bar, and four new pages" (+1576/-226, 24 files: `components/AppChrome.tsx`, `MemberTabBar.tsx`, `SiteFooter.tsx`, `lib/nav.ts`, `lib/education.ts`, new `app/{about,contact,donate,faq,vets,education}` pages, `app/settings/page.tsx`, `app/home/page.tsx`, `app/sitemap.ts` + e2e/unit tests). Live: `draft=false, MERGEABLE, CLEAN` against `65b01d1`. It is FULLY FILE-DISJOINT from all 5 stacked correctness PRs (#38 NewDogForm, #39 health-doc, #40 migration, #41 photo route, #43 robots.ts). (2) `#43` was rewritten by codex Run 197 — it now `disallow /settings (missed by #45) + corrects the /account/ comment`; #46 CREATES `app/settings/page.tsx` while #43 adds the robots `/settings` disallow → complementary, different files, both CLEAN. (3) Base HELD at `65b01d1` (no new merge since #45 this morning). (4) Open PR count 15 → 16, ready 6 → 7; issues unchanged at 4, 0 agent-actionable.** The founder gate is **still byte-for-byte untouched (Aug 11 09:31 → now 6.2 days cold, status line still "APPROVAL REQUESTED")**. The actor merged #44/#45 through the queue this morning, so repo access + PR-process engagement stay PROVEN — the P1 blocker remains the single unsigned gate file, not review bandwidth or access. Everything below is LIVE-verified this run.*

---

## 🔴 THE ONE THING — Sole open P1 gate is FOUNDER sign-off (window is TODAY)
- `~/clawd/AI-Organization/STEF-WEEK-1-APPROVAL.md` **still reads `**Status:** APPROVAL REQUESTED`** — mtime **Aug 11 09:31**, re-verified live → now **6.2 days cold**. The report is **✅ Week-1 PASS (12 tasks, 3.34× avg speedup, zero escalations, 8.6/10)** and recommends APPROVE. Everything is agent/supervisor-signed; **only Stef's written checkmark is missing.**
- **Timeline is T-0 — the Aug-17 3:00 PM CDT go/no-go is TODAY.** **Aug-18 formal Phase-2 Week-1 gate = tomorrow (T-1).** The *only* moving part left is the founder's signature; the window before today's go/no-go is down to hours.
- **Context that strengthens the read:** the founder/actor merged `#44`+`#45` through the queue this morning (Aug-17) AND a new feature PR `#46` was opened since — so on the SAME day the gate needs signing, the actor is demonstrably active in the repo. The blocker is not access, bandwidth, or an untended repo — it is the specific act of signing this one file.

## P1 — OpenClaw Phase 1-4 (gates all Track 1/2 execution)
- **LIVE 2026-07-27 → 2026-08-17 (go/no-go = today).** Completing Phase 1-4 is Stef's Priority 1; target **2026-10-12.**
- Phase-2 Week-1 sign-off (due 08-13) is **DONE agent-side** (6/6 verification PASS, `PHASE-2-WEEK-1-REPORT.md`). Sole open item = the founder gate above.
- **Aug 14-17 pre-gate cost-tracking must-pass (window closes with TODAY's go/no-go):** `test-cost-tracking.sh --live` → 28/28 + `cost-tracker.js --week 2026-08-18 --strict` → exit 0.
- **ADR-008 (ACCEPTED):** Claude Sonnet 4.6 is the **PERMANENT code-gen default** — not conditional on OpenAI funding. A failed Claude call FAILS the task (no silent downgrade). `builder` owns code-gen. gpt-4 REFUSED.

## 🟠 BLOCKER — OpenAI billing (OPEN, NON-BLOCKING)
- `OPENAI_API_KEY` authenticates but has **no credits** → `credit_balance_exhausted`. A `GET /v1/models` 200 is NOT evidence of usable credit. Repro: `node AI-Organization/verify-credentials.js`.
- **Non-blocking** (ADR-008 makes Claude the permanent default), but it's the only thing keeping **Criterion 1 hedged** + gates the Phase-2 ChatGPT leg. Funding it de-hedges Criterion 1.

---

## Merge frontier — LIVE-VERIFIED THIS RUN (Run 188): 16 open · 9 drafts · **7 ready** · 4 issues
*Account-wide `gh search prs/issues` + per-PR `gh pr view --json`. **DELTA vs Run 187: +1 ready PR (#46) → open 15→16, ready 6→7. Base held at `65b01d1` (no merge since #44/#45 this morning). Issues unchanged (4, 0 agent-actionable).** The board now carries a NEW multi-file navigation feature (#46) on top of the 5 stacked correctness PRs, and ALL 6 forming-paws PRs re-verify MERGEABLE/CLEAN + mutually file-disjoint.*

### 🧱 Base @65b01d1 (Increments 1+2+3 merged via queue this morning) — re-confirmed live
- forming-paws `origin/main` HEAD = **`65b01d1`** "Member home, full brand sweep, and account settings (Increments 2 + 3) (#45)" (merged 2026-08-17 09:29Z), preceded by **`8214bc9`** (#44, 09:15Z). Both landed **via the merge queue** (PR merges, not direct pushes). Re-verified via `git fetch` this run — no further movement since.
- **Merge queue is LIVE** (#44/#45 prove it). The remaining frozen items are the P1 gate signature + founder review of the ready PRs — not repo access.

### 🟢 Ready to merge now (7 non-draft MERGEABLE/CLEAN — verified against @65b01d1)
- **forming-paws #46** — 🆕 THIS RUN. Site-wide navigation, rotating member tab bar, four new pages. **24 files** (`components/AppChrome.tsx`, `MemberTabBar.tsx`, `SiteFooter.tsx`, `lib/nav.ts`, `lib/education.ts`, new `app/{about,contact,donate,faq,vets}` + `app/education/[slug]`, `app/settings/page.tsx`, `app/home/page.tsx`, `app/sitemap.ts`, `app/layout.tsx`, `app/page.tsx`, `app/browse/page.tsx`, `app/app/page.tsx`, `app/matches/page.tsx`, `app/account/reactivate/page.tsx` + e2e/unit tests). **+1576/-226.** `draft=false, MERGEABLE, CLEAN`. Largest of the open PRs; **file-disjoint from all 5 stacked correctness PRs.** ⚠️ Post-merge: smoke-test nav chrome + the 4 new pages render; it pairs with #43 (which disallows the new `/settings` route in robots).
- **forming-paws #38** — reject a future **birth date** by the local calendar, not a UTC instant. **3 files** (`app/dogs/new/NewDogForm.tsx`, `lib/dogBirthDate.ts`, `tests/unit/dogBirthDate.test.ts`). +100/-1. Code-only. ⚠️ Co-edits `NewDogForm.tsx` with prior base → post-merge visual check on the new-dog form under brand styling.
- **forming-paws #39** — reject a future **health-doc document_date** by the members' calendar **+ carries the #42 redirect-twin fix**. **4 files** (`app/api/upload/health-doc/route.ts`, `lib/dates.ts`, `tests/unit/dates.test.ts`, `tests/unit/health-doc-upload-route.test.ts`). +201/-3. **`closingIssuesReferences` = #42 → merging #39 auto-closes issue #42.** Disjoint from #46.
- **forming-paws #40** — **browse max-age** filter off by a full year vs the age on the card (mirror of merged #34 min-age fix). **1 file** (`supabase/migrations/0024_browse_dogs_max_age_calendar_band.sql`). +97/-0. **Migration-only → REQUIRES a Supabase 0024 apply + browse smoke-test AFTER merge** (proved by calendar simulation only; pg-mem's interval engine is non-conformant).
- **forming-paws #41** — post-upload redirect went to the internal Vercel host instead of the public domain (`new URL(path, request.url)` ignores `x-forwarded-host`), bouncing members off-domain after a *successful* upload into a deployment-protection login wall. Fixed via `lib/http.ts redirectToPath()` on the tested `getRequestOrigin`. **3 files** (`app/api/upload/photo/route.ts`, `lib/http.ts`, `tests/unit/http.test.ts`). +66/-1. Code-only.
- **forming-paws #43** — 🔁 rewritten by codex Run 197: now **disallows `/settings`** (the member-only route #45 added but forgot to guard — twin of the guarded `/home`) **+ corrects the `/account/` comment** that claimed crawlable while the rule disallows it. **1 file** (`app/robots.ts`). Comment/guard-only, lowest-risk merge. ⚠️ #46 CREATES `app/settings/page.tsx` → #43 guards it in robots; complementary. Post-merge: confirm `robots.txt` emits `Disallow: /settings` and `/account/`.
- **psychic-bassoon #1** (Track 1 · The Plug AI) — "Add real content, working forms, resource detail pages" (`+7718/-61`). `draft=false, MERGEABLE, CLEAN`, but **gated on setting Formspree env vars on Vercel** before forms submit.

**✅ All SIX forming-paws PRs (#38/#39/#40/#41/#43/#46) remain MUTUALLY FILE-DISJOINT → merge in ANY order, no conflict.** #46 (nav/pages/settings) shares no file with the 5 correctness PRs.

**✅ #42 CLOSE-REF STAYS REGISTERED:** live `gh pr view 39 --json closingIssuesReferences` → `{number: 42}`. Merging #39 lands the date guard AND auto-closes issue #42. #42 stays OPEN only until #39 merges.

### ⏸️ Drafts (9 — GitHub blocks merge until un-drafted)
- **psychic-bassoon #11** — Grant Matching Tracker. Needs Supabase project + 4 Vercel env vars. `.env.example` add/add vs #1 → keep BOTH env blocks (non-overlapping, concatenate).
- **command-center-redirect #1** — PIN-locked dashboard. **Cross-repo ordering constraint:** before un-drafting, (a) un-draft+merge psychic #11 and confirm the public domain serves `/grants` 200; (b) repoint all 9 grant links off the SSO-gated `-cam6stef` preview to the canonical public domain, else public visitors hit a Vercel login wall.
- **Link-inbio #5** (Obsidian ops-vault docs) · **#6** (résumé PDF, binary). Low-stakes.
- **Dormant, don't surface as fresh work:** content-machine #3/#4/#5/#10 + `----Workspace-notes` #1 (cold since Jun 28).

### Account-wide open issues (4 — all NON-actionable by an agent)
- forming-paws **#42** — health-doc redirect twin of #41. **Fix staged in PR #39 + a registered closing ref; auto-closes on merge.** No agent action left.
- forming-paws **#8** — IL articles of incorporation + bylaws drafted → founder legal review/filing.
- ai-video-reel-generator **#5** — Supabase project setup → founder-gated (also blocks its PR#4 loop).
- skills-introduction-to-git **#1** — git learning exercise.
- **→ 0 agent-actionable open issues account-wide.** The bottleneck is founder review + signature, not missing fixes.

---

## Tracks
- **Track 1 · The Plug AI:** Execution starts **2026-10-13** (post-OpenClaw); fiscal-sponsor target **2026-11-30.** IL Digital Equity $75K **LAPSING BY CHOICE** — not a blocker, stop flagging. psychic-bassoon PRs are **banked ahead of schedule** — the win now is clearing review *cleanly*, not piling on more.
- **Track 2 · BigHeart (bridge):** content-automation pitch + "Digital Content & AI Systems Specialist" title/comp ask in motion.
- **Track 2 · Forming Paws / Puppy Power:** execution phase. Prototype live; **brand system fully applied on `main` (Increments 1+2+3 merged via #44/#45).** Codex has cleared the date/calendar/upload correctness bugs into 5 stacked disjoint PRs (#38/#39/#40/#41/#43, with #42 folded into #39) AND is now shipping FEATURE work (#46 nav + 4 pages). Frontier = clear-the-queue (7 ready), not write-more-code.

## Content pipeline (running)
- LinkedIn shipped **through #201** (content-pipeline Run 201). Recent resource-navigation lanes: **#196 medical-debt** · **#197 CAR/AUTO-DEBT** · **#198 TAX/IRS-DEBT** · **#199 VETERANS/VA-DISABILITY** · **#200 IMMIGRATION/NOTARIO-FRAUD** · **#201 JOB-LOSS/UNEMPLOYMENT/REEMPLOYMENT-SCAM** (man, 58, laid off after 30 years, unaware unemployment he paid into is his to file or that free reemployment help exists — American Job Centers, Illinois workNet, dislocated-worker/WIOA. Scam payload: fake-check job scams + pay-to-work + unemployment-imposter phishing. Flat rule: a real employer never asks you to pay to work, mail-a-check-to-deposit-and-wire, or hand over bank login/full SSN before an offer; unemployment is filed free through the official state agency). Safety spine held every lane: quiet-helper / augment-not-replace, compliance stated twice, never fed an SSN/ITIN/A-number/account number.

## Open infra carry
1. 🔴 **Stef's written Week-1 sign-off** — the one remaining gate item (agent side complete). **T-0: go/no-go is TODAY (Aug-17 3pm CDT); hours left to sign; 6.2 days cold.** Founder was in GitHub this morning merging #44/#45 — access proven, so this is purely the signing action.
2. 🔴 **Fund OpenAI key** — de-hedges Criterion 1; code-gen already covered by Claude default.
3. **Aug 14-17 cost-tracking must-pass:** 28/28 + `--strict` exit 0. Window closes with TODAY's go/no-go.
4. **Founder-review the frontier:** clear the **7 ready** — forming-paws #38/#39/#40/#41/#43/#46 (any order; **#39 also closes #42**; **#38 co-edits `NewDogForm.tsx` → post-merge visual check**; **#43 → post-merge confirm `/settings`+`/account/` disallow**; **#46 → post-merge smoke-test nav + 4 new pages**; #40 needs the Supabase 0024 apply + smoke-test) + psychic #1 (set Formspree env first). Then the drafts (un-draft #11 before command-center #1, and repoint its 9 links).
5. 🔴 **Year-aware deadline filter in the grant loop** — deterministic post-filter (drop candidates whose deadline year < current or date < today); NOT LLM self-check. Grant-drift loop otherwise CLOSED.
6. **Env carries:** Formspree vars on Vercel → psychic #1. Supabase project + 4 Vercel env vars → psychic #11 + ai-video-reel-generator #5. `ANTHROPIC_API_KEY` for aeos/orchestrator (load-bearing under ADR-008).
7. **Font follow-up (codex Run 190, NOT shipped):** Google Fonts render-blocking `@import` vs `next/font` — founder decision, collides with active brand/nav work; do not ship blind.

## Continuous
- Vault management (inbox, atomic notes, index, tag/link hygiene) across all PARA areas.

---
*Tooling note (this env): full-file **Write** is the reliable path for PRIORITIES.md + state.md. Per-repo + account-wide `gh` and `git fetch` are authoritative. Run 188 finding = **the board keeps absorbing new work without losing merge-readiness**: a NEW +1576/-226 navigation feature PR (#46) landed on the frontier this run, non-draft/MERGEABLE/CLEAN and file-disjoint from all 5 stacked correctness PRs, taking the ready count 6→7 while the base held at `65b01d1`. Codex has moved from bug-clearing into feature work, yet all 6 forming-paws PRs re-verify mergeable + mutually disjoint. The P1 blocker is unchanged and singular: the founder gate, now 6.2 days cold on the day of the T-0 go/no-go, while the actor is provably active in the repo (merged #44/#45 this morning). The digest's job is to prove the board is STILL fully merge-ready and to keep the bottleneck framed as one outstanding signature.*
