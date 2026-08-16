# Antigravity — Active Priorities Digest

*Refreshed by antigravity **Run 185** · 2026-08-16. FULL live re-verification, not a trust-the-bus pass: `git fetch origin main` on forming-paws, account-wide `gh search prs/issues`, per-PR `gh pr view --json isDraft,mergeable,mergeStateStatus,files,closingIssuesReferences`, and the P1 gate file mtime. **What changed since Run 184: exactly one thing on the frontier — codex Run 194 shipped a real new PR (#43), moving the ready count 5 → 6.** Two agent cycles ran since Run 184: (1) **codex Run 194 shipped forming-paws PR #43** — a comment-only fix to `app/robots.ts` where a comment claimed `/account/` was crawlable while the line actually `disallow`s it (a maintainer trap that could leak member URLs into the index). robots.txt output is **byte-identical**; tsc/eslint/86 tests/build green; +3/-2, 1 file. (2) Content pipeline advanced **#198 → #199** (new VETERANS / VA-DISABILITY ministry lane). The **founder gate is still byte-for-byte untouched** (Aug 11 09:31). **Timeline unchanged: T-1 — today (Aug 16) is the LAST FULL DAY; the Aug-17 3:00 PM CDT go/no-go is TOMORROW.** Everything below is LIVE-verified this run.*

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

## Merge frontier — LIVE-VERIFIED THIS RUN (Run 185): 15 open · 9 drafts · **6 ready** · 4 issues
*Account-wide `gh search prs/issues` + per-PR `gh pr view --json`. **DELTA vs Run 184: +1 open PR (#43) → 15 total, and ready count 5 → 6.** Everything else — main SHA, the four stacked correctness PRs, the #42 close-ref, all issue counts, and the gate — is identical to Run 184. The only world-movement since Run 184 was codex's one comment-only PR (#43) and one LinkedIn post (content pipeline #199).*

### 🧱 Base still @3a005a6 (NOT @407e7d3) — re-confirmed live
- forming-paws `origin/main` HEAD = **`3a005a6`** "Brand foundation: Forming Paws logo, palette tokens, display/body fonts" (author Claude, **2026-08-15 21:27:42Z**), parent = **`407e7d3`** (the old "frozen" SHA). Pushed **direct to `main`**, not via PR. Re-verified via `git fetch` this run.
- The brand commit is path-disjoint from all five stacked PRs (it touches only `app/globals.css`, `app/layout.tsx`, `public/admin.html`, `public/logo.svg`, `public/styles.css`, `tailwind.config.ts`). That is why GitHub still evaluates #38/#39/#40/#41/#43 as **MERGEABLE / CLEAN** against this base — merge-any-order guarantee **INTACT** (all five re-verified `draft=false, mergeable=MERGEABLE, mergeStateStatus=CLEAN` this run).
- **KEY INSIGHT (still holds, now 1 day older):** a direct-push actor (founder or proxy) was active on the repo on Aug-15 yet touched NEITHER the merge queue NOR the P1 gate file. The founder signature + the PR review remain the only moving parts — and the actor demonstrably *has* repo access.

### 🟢 Ready to merge now (6 non-draft MERGEABLE/CLEAN — verified against @3a005a6)
- **forming-paws #38** — reject a future **birth date** by the local calendar, not a UTC instant. **3 files** (`app/dogs/new/NewDogForm.tsx`, `lib/dogBirthDate.ts`, `tests/unit/dogBirthDate.test.ts`). **+100/-1. Code-only.**
- **forming-paws #39** — reject a future **health-doc document_date** by the members' calendar **+ carries the #42 redirect-twin fix**. **4 files** (`app/api/upload/health-doc/route.ts`, `lib/dates.ts`, `tests/unit/dates.test.ts`, `tests/unit/health-doc-upload-route.test.ts`). +201/-3. Commits `7bbed64` (date guard) + `986a2d7` (route redirect through public host). **`closingIssuesReferences` = #42 (VERIFIED live this run) → merging #39 auto-closes issue #42.**
- **forming-paws #40** — **browse max-age** filter off by a full year vs the age on the card (mirror of merged #34 min-age fix). **1 file** (`supabase/migrations/0024_browse_dogs_max_age_calendar_band.sql`). +97/-0. **Migration-only → REQUIRES a Supabase 0024 apply + browse smoke-test AFTER merge** (codex proved by calendar simulation only; its env has no live Postgres, and pg-mem's interval engine is non-conformant).
- **forming-paws #41** — post-upload redirect went to the internal Vercel host instead of the public domain (`new URL(path, request.url)` ignores `x-forwarded-host`), bouncing members off-domain after a *successful* upload, often into a deployment-protection login wall. Fixed via new `lib/http.ts redirectToPath()` on the repo's tested `getRequestOrigin`. **3 files** (`app/api/upload/photo/route.ts`, `lib/http.ts`, `tests/unit/http.test.ts`). +66/-1. **Code-only.**
- **forming-paws #43** (NEW this cycle — codex Run 194) — a comment in `app/robots.ts` claimed `/account/` was crawlable while the rule line actually **disallows** it; a maintainer editing to match the comment could have exposed member `/account/` URLs to indexing. **1 file** (`app/robots.ts`), **+3/-2, comment-only — robots.txt output byte-identical.** tsc/eslint/86 tests/build green. **Lowest-risk merge on the board.**
- **psychic-bassoon #1** (Track 1 · The Plug AI) — "Add real content, working forms, resource detail pages" (`+7718/-61`). `draft=false, MERGEABLE, CLEAN` (re-verified live), but **gated on setting Formspree env vars on Vercel** before forms submit.

**✅ All FIVE forming-paws PRs remain FULLY FILE-DISJOINT from each other AND from the brand-foundation main → merge in ANY order, no conflict.** #43 touches only `app/robots.ts` — disjoint from #38's form/lib/test, #39's health-doc route/lib/test, #40's migration, and #41's photo route/`lib/http.ts`/test. #40 is migration-only so it can't collide with any app/lib/test path.

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
- **→ 0 agent-actionable open issues account-wide.** codex Run 193 re-confirmed this from the code side (full source review found the codebase hardened); Run 194's #43 was the last cosmetic trap it had *logged but not yet shipped*, now shipped. The bottleneck is founder review, not missing fixes.

---

## Tracks
- **Track 1 · The Plug AI:** Execution starts **2026-10-13** (post-OpenClaw); fiscal-sponsor target **2026-11-30.** IL Digital Equity $75K **LAPSING BY CHOICE** — not a blocker, stop flagging. psychic-bassoon PRs are **banked ahead of schedule** — the win now is clearing review *cleanly*, not piling on more.
- **Track 2 · BigHeart (bridge):** content-automation pitch + "Digital Content & AI Systems Specialist" title/comp ask in motion.
- **Track 2 · Forming Paws / Puppy Power:** execution phase, no more planning. Prototype live; brand foundation on `main`. Codex has systematically cleared the forming-paws date/calendar/upload correctness bugs into **4 stacked, disjoint PRs** (#38/#39/#40/#41) + the #42 twin folded into #39 with a registered close-ref, and now **#43** (the last logged cosmetic robots.ts trap). **codex Run 193/194 declared the codebase hardened — nothing shippable left to invent.** Frontier = clear-the-queue, not write-more-code.

## Content pipeline (running)
- LinkedIn shipped **through #199** (content-pipeline Run 199, items 324). Recent resource-navigation lanes: **#193 SNAP/food** · **#194 funeral/burial-costs** · **#195 utility/energy-bill** · **#196 medical-debt / hospital-bill** · **#197 CAR / AUTO-DEBT** · **#198 TAX / IRS-DEBT** · **#199 VETERANS / VA-DISABILITY** (NEW lane, breaks cleanly off the debt/bill run: a young vet gets a partial VA denial + a "claims consulting" firm offering a bigger rating and back pay for a CUT of it, while free accredited help sits unused. Doors, hedged/unranked — appeal the denial (rights + deadline; supplemental claim / higher-level review / Board); FREE accredited VSO (county Veterans Assistance Commission, state/county veterans office, VFW/Legion/DAV, veterans law clinics/legal aid); understand the claim (service connection, rating, C&P exam, secondary conditions, effective date); other benefits owed (VA health care, GI Bill, VR&E, TDIU); Veterans Crisis Line 988→1; church benevolence + 211). Scam payload weighted for veterans: **CLAIM SHARKS** (illegal % cut of back pay — a VSO does it FREE), pension poachers, cash-for-benefits buyouts, VA-imposter phishing. Flat rule: real filing help is free, no one may take a % of your back pay to file, VA won't call/text for your SSN or bank login, prove accreditation in writing before you sign. Persona rotated to a **MAN (34, post-9/11 Army vet, forklift, two kids, bad back + tinnitus)** off woman-47 (#198) — fills the young-adult gap. Safety spine held every lane: quiet-helper / augment-not-replace, compliance stated twice (not legal/medical advice, not a rating/eligibility determination), no eligibility/amount/right promised, never fed an SSN/ITIN/VA-file/account number.

## Open infra carry
1. 🔴 **Stef's written Week-1 sign-off** — the one remaining Aug-18 gate item (agent side complete). **T-1: go/no-go is TOMORROW (Aug-17 3pm); today is the last full day to sign.**
2. 🔴 **Fund OpenAI key** — de-hedges Criterion 1; code-gen already covered by Claude default.
3. **Aug 14-17 cost-tracking must-pass:** 28/28 + `--strict` exit 0. Window open, closes with the go/no-go.
4. **Founder-review the frontier:** clear the **6 ready** — forming-paws #38/#39/#40/#41/#43 (any order; **#39 also closes #42**; #40 needs the Supabase 0024 apply + smoke-test after merge; #43 is the lowest-risk, comment-only merge) + psychic #1 (set Formspree env first). Then the drafts (un-draft #11 before command-center #1, and repoint its 9 links).
5. 🔴 **Year-aware deadline filter in the grant loop** — deterministic post-filter (drop candidates whose deadline year < current or date < today); NOT LLM self-check (Perplexity's year-reasoning is non-deterministic). Grant-drift loop otherwise CLOSED.
6. **Env carries:** Formspree vars on Vercel → psychic #1. Supabase project + 4 Vercel env vars → psychic #11 + ai-video-reel-generator #5. `ANTHROPIC_API_KEY` for aeos/orchestrator (load-bearing under ADR-008).
7. **Font follow-up (codex Run 190, NOT shipped):** Google Fonts render-blocking `@import` vs `next/font` (perf + IP-privacy) — founder decision, collides with active brand work; do not ship blind.

## Continuous
- Vault management (inbox, atomic notes, index, tag/link hygiene) across all PARA areas.

---
*Tooling note (this env): full-file **Write** is the reliable path for PRIORITIES.md + state.md. Per-repo + account-wide `gh` and `git fetch` are authoritative. Run 185 finding = **the merge board grew by one, the gate did not move**: codex shipped its last logged cosmetic fix (#43) so there are now 6 ready PRs (5 forming-paws all disjoint + psychic #1), yet the founder signature is still 5 days cold and the go/no-go is T-1. When the only frontier motion is one more agent-side PR while the founder gate stays frozen, the digest's job is to prove the board is even more merge-ready than yesterday and that the sole remaining variable is the founder's signature — with the clock now down to today.*
