# Antigravity — Active Priorities Digest

*Refreshed by antigravity **Run 186** · 2026-08-17. FULL live re-verification, not a trust-the-bus pass: `git fetch origin main` on forming-paws, account-wide `gh search prs/issues`, per-PR `gh pr view --json isDraft,mergeable,mergeStateStatus,files,closingIssuesReferences`, and the P1 gate file mtime. **What changed since Run 185: (1) TODAY IS THE GO/NO-GO — the calendar crossed from T-1 to T-0; the Aug-17 3:00 PM CDT go/no-go is TODAY. (2) forming-paws `main` MOVED AGAIN — two more direct-push commits landed Aug-16 (`5bcba51` UX pass from live button-testing + `bf2b233` "Apply brand system across all app surfaces"), advancing base `3a005a6` → `bf2b233`. (3) The brand-system commit edited `app/dogs/new/NewDogForm.tsx` — the SAME file as PR #38 — yet GitHub STILL evaluates all 5 stacked PRs as MERGEABLE/CLEAN (non-overlapping regions, git auto-merges).** The founder gate is **still byte-for-byte untouched (Aug 11 09:31 → now 6 days cold).** Everything below is LIVE-verified this run.*

---

## 🔴 THE ONE THING — Sole open P1 gate is FOUNDER sign-off (window is TODAY)
- `~/clawd/AI-Organization/STEF-WEEK-1-APPROVAL.md` **still reads "APPROVAL REQUESTED"** — mtime **Aug 11 09:31**, re-verified live this run → now **6 days cold**. The report itself is **✅ Week-1 PASS (12 tasks, 3.34× avg speedup, zero escalations, 8.6/10)** and recommends APPROVE. Everything is agent/supervisor-signed; **only Stef's written checkmark is missing.**
- **Timeline is T-0 — the Aug-17 3:00 PM CDT go/no-go is TODAY.** **Aug-18 formal Phase-2 Week-1 gate = tomorrow (T-1).** Every agent-side item stays green — the *only* moving part left is the founder's signature, and the window to sign before the go/no-go has narrowed to a few hours.
- Clearing the merge queue is a *different* founder action from signing this gate. This gate is the P1 blocker.

## P1 — OpenClaw Phase 1-4 (gates all Track 1/2 execution)
- **LIVE 2026-07-27 → 2026-08-17 (go/no-go = today).** Completing Phase 1-4 is Stef's Priority 1; target **2026-10-12.**
- Phase-2 Week-1 sign-off (due 08-13) is **DONE agent-side** (6/6 verification PASS, `PHASE-2-WEEK-1-REPORT.md`). Sole open item = the founder gate above.
- **Aug 14-17 pre-gate cost-tracking must-pass (window closes with TODAY's go/no-go):** `test-cost-tracking.sh --live` → 28/28 + `cost-tracker.js --week 2026-08-18 --strict` → exit 0.
- **ADR-008 (ACCEPTED):** Claude Sonnet 4.6 is the **PERMANENT code-gen default** — not conditional on OpenAI funding. A failed Claude call FAILS the task (no silent downgrade to ChatGPT). `builder` owns code-gen. gpt-4 REFUSED.

## 🟠 BLOCKER — OpenAI billing (OPEN, NON-BLOCKING)
- `OPENAI_API_KEY` authenticates but has **no credits** → `credit_balance_exhausted`. A `GET /v1/models` 200 is NOT evidence of usable credit. Repro: `node AI-Organization/verify-credentials.js`.
- **Non-blocking** (ADR-008 makes Claude the permanent default), but it's the only thing keeping **Criterion 1 hedged** + gates the Phase-2 ChatGPT leg. Funding it de-hedges Criterion 1.

---

## Merge frontier — LIVE-VERIFIED THIS RUN (Run 186): 15 open · 9 drafts · **6 ready** · 4 issues
*Account-wide `gh search prs/issues` + per-PR `gh pr view --json`. **DELTA vs Run 185: the base MOVED again (two new direct-push commits Aug-16), but PR/issue counts are identical — 15 open (6 ready), 4 issues, 0 agent-actionable.** The board absorbed a moving base for the SECOND straight day without losing merge-readiness.*

### 🧱 Base advanced @3a005a6 → @bf2b233 — re-confirmed live
- forming-paws `origin/main` HEAD = **`bf2b233`** "Apply brand system across all app surfaces" (author Claude, **2026-08-16 23:59:07Z**), preceded by **`5bcba51`** "UX pass from live button-testing: sign out, instant chat feedback, no dead ends". Both pushed **direct to `main`**, not via PR. Old base `3a005a6` is now 2 commits back. Re-verified via `git fetch` this run.
- The two new commits touch **22 app-surface files** (login/signup/waitlist/contact/browse/dashboard/dogs/matches/faq forms + pages, `app/auth/signout/route.ts`, `components/StickyJoinBar.tsx`). **One of them — `app/dogs/new/NewDogForm.tsx` — is ALSO a file in PR #38.** GitHub still reports **#38 MERGEABLE/CLEAN**: the brand edit and the birth-date-guard edit are in non-overlapping regions, so git auto-merges. ⚠️ **Reviewer note: after #38 merges, eyeball the new-dog form renders correctly under the new brand styling — it's the one PR that now co-edits a file with main.**
- All five stacked PRs re-verified this run: **#38/#39/#40/#41/#43 = `draft=false, mergeable=MERGEABLE, mergeStateStatus=CLEAN`** against `bf2b233`. Merge-any-order guarantee **INTACT**.
- **KEY INSIGHT (now doubly confirmed):** a direct-push actor (founder or proxy) has been active on the repo on BOTH Aug-15 AND Aug-16, shipping brand + UX work straight to main — yet has touched NEITHER the merge queue NOR the P1 gate file across both days. The founder signature + the PR review remain the only frozen moving parts, and the actor demonstrably *has* repo access and *is* actively committing.

### 🟢 Ready to merge now (6 non-draft MERGEABLE/CLEAN — verified against @bf2b233)
- **forming-paws #38** — reject a future **birth date** by the local calendar, not a UTC instant. **3 files** (`app/dogs/new/NewDogForm.tsx`, `lib/dogBirthDate.ts`, `tests/unit/dogBirthDate.test.ts`). **+100/-1. Code-only.** ⚠️ Now co-edits `NewDogForm.tsx` with main (still CLEAN) → post-merge visual check on the new-dog form.
- **forming-paws #39** — reject a future **health-doc document_date** by the members' calendar **+ carries the #42 redirect-twin fix**. **4 files** (`app/api/upload/health-doc/route.ts`, `lib/dates.ts`, `tests/unit/dates.test.ts`, `tests/unit/health-doc-upload-route.test.ts`). +201/-3. Commits `7bbed64` (date guard) + `986a2d7` (route redirect through public host). **`closingIssuesReferences` = #42 (VERIFIED live this run) → merging #39 auto-closes issue #42.**
- **forming-paws #40** — **browse max-age** filter off by a full year vs the age on the card (mirror of merged #34 min-age fix). **1 file** (`supabase/migrations/0024_browse_dogs_max_age_calendar_band.sql`). +97/-0. **Migration-only → REQUIRES a Supabase 0024 apply + browse smoke-test AFTER merge** (codex proved by calendar simulation only; its env has no live Postgres, and pg-mem's interval engine is non-conformant).
- **forming-paws #41** — post-upload redirect went to the internal Vercel host instead of the public domain (`new URL(path, request.url)` ignores `x-forwarded-host`), bouncing members off-domain after a *successful* upload, often into a deployment-protection login wall. Fixed via new `lib/http.ts redirectToPath()` on the repo's tested `getRequestOrigin`. **3 files** (`app/api/upload/photo/route.ts`, `lib/http.ts`, `tests/unit/http.test.ts`). +66/-1. **Code-only.**
- **forming-paws #43** — a comment in `app/robots.ts` claimed `/account/` was crawlable while the rule line actually **disallows** it; a maintainer editing to match the comment could have exposed member `/account/` URLs to indexing. **1 file** (`app/robots.ts`), **+3/-2, comment-only — robots.txt output byte-identical.** tsc/eslint/86 tests/build green. **Lowest-risk merge on the board.**
- **psychic-bassoon #1** (Track 1 · The Plug AI) — "Add real content, working forms, resource detail pages" (`+7718/-61`). `draft=false, MERGEABLE, CLEAN` (re-verified live), but **gated on setting Formspree env vars on Vercel** before forms submit.

**✅ All FIVE forming-paws PRs remain FULLY FILE-DISJOINT from each other → merge in ANY order, no conflict.** #43 touches only `app/robots.ts`; #38 form/lib/test; #39 health-doc route/lib/test; #40 migration-only; #41 photo route/`lib/http.ts`/test. Against the moved base, only #38 now co-edits a main-touched file (`NewDogForm.tsx`) and git still auto-merges it CLEAN.

**✅ #42 CLOSE-REF STAYS REGISTERED:** live `gh pr view 39 --json closingIssuesReferences` → `{number: 42}`. Merging #39 lands the date guard AND auto-closes issue #42. #42 stays OPEN only until #39 merges. **Lesson banked (Run 183): assert a close-ref only after `closingIssuesReferences` confirms it — a "Closes #N" in prose is not a registered reference.**

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
- **→ 0 agent-actionable open issues account-wide.** The bottleneck is founder review + signature, not missing fixes.

---

## Tracks
- **Track 1 · The Plug AI:** Execution starts **2026-10-13** (post-OpenClaw); fiscal-sponsor target **2026-11-30.** IL Digital Equity $75K **LAPSING BY CHOICE** — not a blocker, stop flagging. psychic-bassoon PRs are **banked ahead of schedule** — the win now is clearing review *cleanly*, not piling on more.
- **Track 2 · BigHeart (bridge):** content-automation pitch + "Digital Content & AI Systems Specialist" title/comp ask in motion.
- **Track 2 · Forming Paws / Puppy Power:** execution phase, no more planning. Prototype live; **brand system now applied across all app surfaces on `main` (2 direct-push commits Aug-16).** Codex has cleared the forming-paws date/calendar/upload correctness bugs into **4 stacked, disjoint PRs** (#38/#39/#40/#41) + the #42 twin folded into #39 with a registered close-ref, and **#43** (the last logged cosmetic robots.ts trap). **codex Run 193/194 declared the codebase hardened — nothing shippable left to invent.** Frontier = clear-the-queue, not write-more-code.

## Content pipeline (running)
- LinkedIn shipped **through #200** (content-pipeline Run 200, milestone). Recent resource-navigation lanes: **#195 utility/energy-bill** · **#196 medical-debt** · **#197 CAR / AUTO-DEBT** · **#198 TAX / IRS-DEBT** · **#199 VETERANS / VA-DISABILITY** · **#200 IMMIGRATION / CITIZENSHIP / NOTARIO-FRAUD** (NEW lane — woman, 29, first-gen LPR eligible to naturalize, ESL, about to pay a storefront *notario* (not a lawyer) to file citizenship paperwork. Doors: get it checked before filing; REAL accredited help (licensed immigration attorney or DOJ-accredited rep, nonprofit legal aid, law-school clinics); understand the option (naturalization/green-card renewal/adjustment/family petition/DACA/work permit/fee waiver); fee waivers + free citizenship/civics/ESL classes; 211/988 for the fear. Scam payload: NOTARIO FRAUD + guarantee/fee scams + selling the free USCIS forms + USCIS/ICE gift-card imposter phishing + document/identity theft). Safety spine held every lane: quiet-helper / augment-not-replace, compliance stated twice (not legal/medical advice, not an eligibility determination), never fed an SSN/ITIN/A-number/account number.

## Open infra carry
1. 🔴 **Stef's written Week-1 sign-off** — the one remaining gate item (agent side complete). **T-0: go/no-go is TODAY (Aug-17 3pm CDT); hours left to sign.**
2. 🔴 **Fund OpenAI key** — de-hedges Criterion 1; code-gen already covered by Claude default.
3. **Aug 14-17 cost-tracking must-pass:** 28/28 + `--strict` exit 0. Window closes with TODAY's go/no-go.
4. **Founder-review the frontier:** clear the **6 ready** — forming-paws #38/#39/#40/#41/#43 (any order; **#39 also closes #42**; **#38 now co-edits `NewDogForm.tsx` with main → post-merge visual check**; #40 needs the Supabase 0024 apply + smoke-test after merge; #43 is the lowest-risk, comment-only merge) + psychic #1 (set Formspree env first). Then the drafts (un-draft #11 before command-center #1, and repoint its 9 links).
5. 🔴 **Year-aware deadline filter in the grant loop** — deterministic post-filter (drop candidates whose deadline year < current or date < today); NOT LLM self-check (Perplexity's year-reasoning is non-deterministic). Grant-drift loop otherwise CLOSED.
6. **Env carries:** Formspree vars on Vercel → psychic #1. Supabase project + 4 Vercel env vars → psychic #11 + ai-video-reel-generator #5. `ANTHROPIC_API_KEY` for aeos/orchestrator (load-bearing under ADR-008).
7. **Font follow-up (codex Run 190, NOT shipped):** Google Fonts render-blocking `@import` vs `next/font` (perf + IP-privacy) — founder decision, collides with active brand work; do not ship blind. **Note: brand work is now live on main (`bf2b233`) — this decision is more relevant than ever.**

## Continuous
- Vault management (inbox, atomic notes, index, tag/link hygiene) across all PARA areas.

---
*Tooling note (this env): full-file **Write** is the reliable path for PRIORITIES.md + state.md. Per-repo + account-wide `gh` and `git fetch` are authoritative. Run 186 finding = **the base moved for the SECOND straight day and the board still absorbed it CLEAN**: two direct-push brand/UX commits landed Aug-16 (base `3a005a6` → `bf2b233`), one of them co-editing PR #38's `NewDogForm.tsx`, yet all 5 stacked PRs re-verify MERGEABLE/CLEAN and merge-any-order holds. The go/no-go is now TODAY (T-0) and the founder signature is 6 days cold. When the actor is demonstrably active on the repo (shipping brand work straight to main) but keeps skipping both the merge queue and the gate, the digest's job is to prove the board is STILL fully merge-ready under a moving base — so the only variable at the go/no-go is the founder's signature, with the clock now down to hours.*
