# Antigravity — Active Priorities Digest

*Refreshed by antigravity **Run 178**, **live re-verified Run 179** · 2026-08-15. Run 179 re-ran the full per-repo `gh` sweep (account-wide PR/issue search + per-PR `mergeable`/`mergeStateStatus` + file-path disjointness + `forming-paws` main HEAD + gate mtime): **frontier is byte-for-byte STABLE** — nothing merged since Run 187 (main still @407e7d3), all 5 ready PRs still MERGEABLE/CLEAN and file-disjoint, 3 open issues all non-actionable. codex Run 188's 'no new PR' bus claim CONFIRMED against live GitHub, not trusted. Full scan of context.md (canonical Stefan), world.md, state.md, PRIORITIES.md, and the bus wave through ~13:44Z Aug 15. The merge frontier below is **LIVE-verified this run** via direct per-repo `gh pr list/pr view --json` (not the bus, not the search index) across all 5 active repos + the 3-issue account-wide sweep + the P1 gate file mtime. Supersedes the Run 174 digest and its Run 175 correction banner — both predate codex PRs #40 and #41 and their "16 open · 12 mergeable" numbers are stale.*

---

## 🔴 THE ONE THING — Sole open P1 gate is FOUNDER sign-off
- `~/clawd/AI-Organization/STEF-WEEK-1-APPROVAL.md` **still reads "APPROVAL REQUESTED"** — mtime **Aug 11 09:31**, untouched (re-verified this run). The report itself is **✅ Week-1 PASS (12 tasks, 3.34× avg speedup, zero escalations, 8.6/10)** and recommends APPROVE. Everything is agent/supervisor-signed; **only Stef's written checkmark is missing.**
- **Timeline is now tight:** today is **Aug 15**. **Aug-17 3:00 PM CDT go/no-go (T-2 days)**, **Aug-18 formal Phase-2 Week-1 gate (T-3 days).** The gate file has now been **untouched for 4 days** (mtime Aug 11 09:31) while every agent-side item stays green — the *only* moving part left is the founder's signature, and the window to sign before the go/no-go is closing.
- Clearing the merge queue is a *different* founder action from signing this gate. This gate is the P1 blocker.

## P1 — OpenClaw Phase 1-4 (gates all Track 1/2 execution)
- **LIVE 2026-07-27 → 2026-08-17.** Completing Phase 1-4 is Stef's Priority 1; target **2026-10-12.**
- Phase-2 Week-1 sign-off (due 08-13) is **DONE agent-side** (6/6 verification PASS, `PHASE-2-WEEK-1-REPORT.md`). Sole open item = the founder gate above.
- **Aug 14-17 pre-gate cost-tracking must-pass (window OPEN):** `test-cost-tracking.sh --live` → 28/28 + `cost-tracker.js --week 2026-08-18 --strict` → exit 0.
- **ADR-008 (ACCEPTED):** Claude Sonnet 4.6 is the **PERMANENT code-gen default** — not conditional on OpenAI funding. A failed Claude call FAILS the task (no silent downgrade to ChatGPT). `builder` owns code-gen. gpt-4 REFUSED.

## 🟠 BLOCKER — OpenAI billing (OPEN, NON-BLOCKING)
- `OPENAI_API_KEY` authenticates but has **no credits** → `credit_balance_exhausted`. A `GET /v1/models` 200 is NOT evidence of usable credit. Repro: `node AI-Organization/verify-credentials.js`.
- **Non-blocking** (ADR-008 makes Claude the permanent default), but it's the only thing keeping **Criterion 1 hedged** + gates the Phase-2 ChatGPT leg. Funding it de-hedges Criterion 1.

---

## Merge frontier — LIVE-VERIFIED THIS RUN (Run 178): 9 open · 4 drafts · 5 ready
*Per-repo `gh pr list/view --json` across the 5 active repos. Delta since the Run 174 digest: the 11-PR Aug-14 founder merge burst cleared the old queue; codex has since shipped **4 forming-paws correctness PRs** (#38/#39/#40/#41), all still open awaiting review.*

### 🟢 Ready to merge now (5 non-draft MERGEABLE/CLEAN)
- **forming-paws #38** — reject a future **birth date** by the local calendar, not a UTC instant. Files: `app/dogs/new/NewDogForm.tsx`, `lib/dogBirthDate.ts`, `tests/unit/dogBirthDate.test.ts`. **Code-only.**
- **forming-paws #39** — reject a future **health-doc document_date** by the members' calendar. Files: `app/api/upload/health-doc/route.ts`, `lib/dates.ts`, `tests/unit/dates.test.ts`. **Code-only.**
- **forming-paws #40** — **browse max-age** filter off by a full year vs the age on the card (mirror of merged #34 min-age fix). File: `supabase/migrations/0024_browse_dogs_max_age_calendar_band.sql`. **Migration-only → REQUIRES a Supabase 0024 apply + browse smoke-test AFTER merge** (codex proved by calendar simulation only; its env has no live Postgres, and pg-mem's interval engine is non-conformant).
- **forming-paws #41** — post-upload redirect went to the internal Vercel host instead of the public domain (`new URL(path, request.url)` ignores `x-forwarded-host`), bouncing members off-domain after a *successful* upload, often into a deployment-protection login wall. Fixed via new `lib/http.ts redirectToPath()` built on the repo's own tested `getRequestOrigin` helper. Files: `app/api/upload/photo/route.ts`, `lib/http.ts`, `tests/unit/http.test.ts`. **Code-only.** (Was UNSTABLE while the Vercel preview built at handoff — now **CLEAN**.)
- **psychic-bassoon #1** (Track 1 · The Plug AI) — "Add real content, working forms, resource detail pages" (`+7718/-61`). MERGEABLE, but **gated on setting Formspree env vars on Vercel** before forms submit.

**✅ All four forming-paws PRs are FULLY FILE-DISJOINT (zero shared paths, verified this run) → merge in ANY order, no conflict.** #40 is migration-only so it can't collide with the app/lib/test paths of #38/#39/#41.

**⚠️ OPEN LOOP (codex Run 187):** the **twin** health-doc upload route still carries the *same* proxy-unsafe redirect that #41 fixed on the photo route. It was left untouched because it lives in **#39**'s file (`app/api/upload/health-doc/route.ts`) — swapping it in #41 would cause an add/add import conflict. **Next step once #39 merges:** change its one redirect line to `redirectToPath(request, \`/dogs/${dogId}\`)` (or fold the fix into #39). That closes the upload-redirect pair.

### ⏸️ Drafts (4 — GitHub blocks merge until un-drafted)
- **psychic-bassoon #11** — Grant Matching Tracker. Needs Supabase project + 4 Vercel env vars. `.env.example` add/add vs #1 → keep BOTH env blocks (non-overlapping, concatenate).
- **command-center-redirect #1** — PIN-locked dashboard. **Cross-repo ordering constraint:** before un-drafting, (a) un-draft+merge psychic #11 and confirm the public domain serves `/grants` 200; (b) repoint all 9 grant links off the SSO-gated `-cam6stef` preview to the canonical public domain, else public visitors hit a Vercel login wall.
- **Link-inbio #5** (Obsidian ops-vault docs) · **#6** (résumé PDF, binary). Low-stakes.

### Account-wide open issues (3 — all NON-actionable by an agent)
- forming-paws **#8** — IL articles of incorporation + bylaws drafted → founder legal review/filing.
- ai-video-reel-generator **#5** — Supabase project setup → founder-gated (also blocks its PR#4 loop).
- skills-introduction-to-git **#1** — git learning exercise.
- **→ 0 agent-actionable open issues account-wide.** The bottleneck is founder review, not missing fixes.

---

## Tracks
- **Track 1 · The Plug AI:** Execution starts **2026-10-13** (post-OpenClaw); fiscal-sponsor target **2026-11-30.** IL Digital Equity $75K **LAPSING BY CHOICE** — not a blocker, stop flagging. psychic-bassoon PRs are **banked ahead of schedule** — the win now is clearing review *cleanly*, not piling on more.
- **Track 2 · BigHeart (bridge):** content-automation pitch + "Digital Content & AI Systems Specialist" title/comp ask in motion.
- **Track 2 · Forming Paws / Puppy Power:** execution phase, no more planning. Prototype live. Codex is systematically clearing forming-paws date/calendar/upload correctness bugs, one root-cause PR at a time — **4 now stacked and disjoint** (#38/#39/#40/#41).

## Content pipeline (running)
- LinkedIn shipped **through #192** (content-pipeline Run 192, items 317). Recent resource-navigation lanes: #188 estate-planning/heirs-property (legacy horizon) · #189-#191 · **#192 eviction-prevention / rental-assistance / tenant-rights** — the renter counterpart to the #184 property-tax homeowner lane. Safety spine: a notice is not being put out; do not self-evict or ignore the court date before talking to legal aid. Compliance stated twice; AI held to quiet-helper / augment-not-replace.

## Open infra carry
1. 🔴 **Stef's written Week-1 sign-off** — the one remaining Aug-18 gate item (agent side complete).
2. 🔴 **Fund OpenAI key** — de-hedges Criterion 1; code-gen already covered by Claude default.
3. **Aug 14-17 cost-tracking must-pass:** 28/28 + `--strict` exit 0. Window open.
4. **Founder-review the frontier:** clear the **5 ready** — forming-paws #38/#39/#40/#41 (any order; #40 needs the Supabase 0024 apply + smoke-test after merge) + psychic #1 (set Formspree env first). Then the 4 drafts (un-draft #11 before command-center #1, and repoint its 9 links).
5. 🔴 **Year-aware deadline filter in the grant loop** — deterministic post-filter (drop candidates whose deadline year < current or date < today); NOT LLM self-check (Perplexity's year-reasoning is non-deterministic). Grant-drift loop otherwise CLOSED (30th consecutive net-zero).
6. **Env carries:** Formspree vars on Vercel → psychic #1. Supabase project + 4 Vercel env vars → psychic #11 + ai-video-reel-generator #5. `ANTHROPIC_API_KEY` for aeos/orchestrator (load-bearing under ADR-008).
7. **Post-merge follow-up:** after #39 merges, close the upload-redirect twin (health-doc route) per the OPEN LOOP above.
8. **Dormant, don't surface as fresh work:** content-machine #3/#4/#5/#10 + workspace-notes #1 (cold since Jun 28).

## Continuous
- Vault management (inbox, atomic notes, index, tag/link hygiene) across all PARA areas.

---
*Tooling note (this env): full-file **Write SUCCEEDED** for PRIORITIES.md + state.md. **Edit is permission-denied** — prefer Write (full file) or Bash append. Per-repo `gh pr list/view --json` is authoritative and matched reality this run.*
