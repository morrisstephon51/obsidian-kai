# Antigravity — Active Priorities Digest

*Updated by antigravity Run 151 · 2026-08-10. Scan of context.md (canonical), world.md, state.md, and bus (unread wave through ~09:28Z 08-10). Reconciles the Run 150 digest against post-150 bus deltas: **codex Run 160, content-pipeline Run 165, perplexity 09:28Z run**, and the concurrently-landed **clawd Run 177 + codex Run 161** (which refine item (c) and clear PR#20). Headline this run: the item (b) year-blind date bug **RECURRED** at perplexity 09:28Z (fresh recurrence one run after clawd Run 176 flagged it), and codex independently verified **PR#17 SAFE TO MERGE after #16**.*

---

## P1 — OpenClaw Phase 1 (gates everything)
- **LIVE 2026-07-27 → 2026-08-17.** Completing Phase 1-4 is Stef's Priority 1; target 2026-10-12. Gates all Track 1/2 execution.
- **Pre-staging window Aug 10-13** per Kairo master timeline; **formal Phase 2 Week 1 gate stays Aug 18.**
- 🔴 **Phase 3 audit-readiness sign-off was due 2026-08-10 (TODAY)** — flagged by Aexis. Still unconfirmed on the bus as of 09:28Z; verify status.
- ⚠️ **PHASE-2-WEEK-1-PREFLIGHT.md remains RETRACTED** (Kairo audit @19:48Z 08-09). Cost model corrected: real Haiku call ~$0.031 (~38x old est); Claude-CLI = subscription, $0 marginal; routing never 100%.
- **ADR-008 ACCEPTED by Stefan (clawd Run 174):** **Claude Sonnet 4.6 is the PERMANENT code-gen default** (not conditional on OpenAI funding). New **`builder`** agent owns code-gen. gpt-4o-mini / gpt-4o only via `--override`; **gpt-4 REFUSED**. **Auto-fallback-to-ChatGPT authority WITHDRAWN** — a failed Claude call now FAILS THE TASK (no silent downgrade).
- **Budget corrected to $250/wk METERED-ONLY.** New doc/code-agreement gate `sec[13]`, **88 checks passing**. Perplexity per-request $0.005 fee + dated-model-id $0.00 leak fixed. Fabricated-success class fixed across architect/aexis/aeos/orchestrator/perplexity.
- Parallel execution: Kairo load-tests show 2.51x (3-task) / 9.85x (10-task) speedup, but still **NOT formally implemented**.

## 🔴 BLOCKER-1 — REOPENED (clawd Run 174, still open)
- **OPENAI_API_KEY authenticates but has NO CREDITS** → `credit_balance_exhausted`. A `GET /v1/models` 200 is **NOT** evidence of usable credit. **Phase-2 ChatGPT path is blocked on BILLING, not code.** Repro: `node AI-Organization/verify-credentials.js`.
- Mitigation already in place: ADR-008 makes Claude the permanent code-gen default, so **code-gen is NOT blocked**. Only ChatGPT-dependent Phase-2 items wait on funding the OpenAI key.

## P1 — Track 1: The Plug AI (execution deferred, not dead)
- **Execution starts 2026-10-13** (post-OpenClaw); fiscal-sponsor target 2026-11-30.
- **IL Digital Equity $75K: LAPSING BY CHOICE** (confirmed 2026-07-29). Not a blocker — stop flagging.
- Custom domain **https://theplugai.info live (200)**; all 11 Link-in-bio links repointed off auth-walled Vercel aliases (PR#14 merged).
- Archived paths: Kresge LOI, church outreach.

## Grant-drift monitoring loop — CLOSED (holding) · reflects perplexity 09:28Z run
- **18th consecutive net-zero** eligible-grant confirm, 8/07 → 8/10. Loop STAYS CLOSED. The 09:28Z perplexity run surfaced **zero** eligible open grants (its only "open" candidate is a closed 2025 window — see below).
- 🔴🔴 **HEADLINE — item (b) year-blind date bug RECURRED (perplexity 09:28Z, results/2026-08-10.md L71-77):** perplexity again named the **OpenAI People-First AI Fund** as "**one clearly relevant open opportunity**" whose deadline "**October 8, 2025 … is more than 7 days out relative to the date you gave.**" As of today (2026-08-10) that window is **~10 months PAST.** This is the same worst-drift class clawd Run 176 flagged, **recurring in the very next perplexity run.**
  - **New evidence it is NON-DETERMINISTIC, not consistent:** the SAME results file shows earlier runs that reasoned correctly — L9 ("not active now and should be excluded"), L30 ("not open now"). So perplexity CAN year-aware-reason but does so unreliably. **Implication: do not trust the LLM to self-correct — add a deterministic year-aware post-filter that drops any deadline with year < current year (or date < today).** Escalates infra-carry #5 from "fix" to "confirmed-recurring, prioritize."
- 🟠 **item (c) SHIFTED, not recurred (per clawd Run 177):** the 174/175/176 internal headline/body contradiction is now **ABSENT** in the 09:28Z run — perplexity affirmatively treats Oct-8-2025 as future in BOTH headline and body, so the run is **internally consistent but uniformly FALSE**. Drift moved from self-contradictory (a built-in hedge a reader could catch) to **confidently-consistent-and-false** (no internal signal) — arguably worse downstream. Net: item (c) as originally defined stops manifesting; the whole positive output now rests solely on the item (b) date-compare bug, which is the single fix that closes it.
- ✅ **Held this run — item (a) geo post-filter:** Tracy Family Foundation (West Central IL, outside Cook-County service area) was **NOT surfaced** in the 09:28Z run. ⚠️ But it DID appear in an earlier same-day run (L29-33, named "best confirmed open match"), so the geo filter is **still flip-floppy** across runs (174→175→176→same-day) — not yet proven persistent.
- ✅ **Held — item (d):** IDEC correctly excluded in the 09:28Z run (L80: "May 8, 2025 deadline, so they are closed and out of scope"). Consistent with dated-and-disqualified.

## Merge queue
- 🟢 **forming-paws PR#17 (eslint flat-config + CI): VERIFIED SAFE TO MERGE after #16 (codex Run 160).** Independent clean-checkout repro of full CI: `npm ci` exit 0 (lock in sync), `tsc --noEmit` exit 0, lint **0 problems**, tests **27/27**. Lint coverage confirmed REAL not vacuous: eslint inspected **45 files with 98 active rules** (21 @next/next, 20 @typescript-eslint). **NEW non-blocking follow-up:** `ci.yml` is added but **NOT a required check** — needs a **branch-protection rule on `main`** to actually gate merges. (Upgrades PR#17 from "unreviewed" in the Run-150 digest.)
- 🔴 **forming-paws PR#16 (email-confirm auth): DEPLOY-BLOCKING coupling (codex Run 159).** `/auth/confirm` handles **ONLY `token_hash`** with **no `?code=` fallback**, while confirmation links come from Supabase **dashboard email templates (not in the repo)**. If templates aren't switched to the `token_hash` form, every new-signup confirmation lands on `/auth/confirm?code=...` and is **rejected**. Fix: **code-exchange fallback + template update.** **Do not merge/deploy PR#16 until resolved.** (PR#17 merges only after this clears.)
- **forming-paws PR#19: SAFE to merge** (codex Run 158). Couples dog-photo RLS to the browse surface; reuses 0009/0010 policy names so it REPLACES permissive `USING(true)`. **Latent footgun:** the `exists(... dogs_browsable)` coupling depends on the view keeping definer rights — if the `security_definer_view` linter fix (`security_invoker=true`) lands, `/browse` silently shows only your own dogs. Codex recommends a security-definer `dog_is_browsable()` helper.
- 🟢 **forming-paws PR#20 (dashboard health-verification badge, +35/-3): VERIFIED SAFE TO MERGE (codex Run 161).** Clean-clone CI reproduced — npm ci in sync, tsc exit 0, **19/19 tests**; the lint failure is pre-#17 `main` state, not a regression. Auth-guarded, owner-scoped, reuses an existing security-definer RPC with **no new migration → mergeable independently of #16/#17/#19**; land before the Task 6 static repoint.
- 🔵 **PR#11 (psychic-bassoon grant-tracker): standing merge carry** (clawd Run 174). Auth HARDENED (codex Run 157) — `lib/mutation-auth.ts` fails CLOSED, RLS deny-all, tsc=0 + build OK. Residual: leaves-draft gate + `NEXT_PUBLIC_*` bundle-visible (light gate) + Supabase project + 4 Vercel env vars.
- **PR#1 (psychic-bassoon): MERGEABLE** (codex Run 156). Residual: set **Formspree env vars on Vercel**.
- **Still open + UNREVIEWED:** forming-paws **#18 (docs) ONLY** — codex Run 161 cleared #20, Run 160 cleared #17, so the review frontier is now a single docs PR. No migration-number collision across the #16-20 train.
- Already merged: ai-video-reel #23, forming-paws #14, community-intake #1, Link-in-bio #11/#14.

## Track 2
- **BigHeart (bridge):** content automation pitch + title/comp ask ("Digital Content & AI Systems Specialist") in motion.
- **Forming Paws / Puppy Power:** execution phase, no more planning. Prototype live; active PR train #16-20 (PR#17 verified-safe-after-#16 / PR#19 + PR#20 safe / PR#16 blocked / only PR#18 docs unreviewed — see merge queue).

## Content pipeline (running)
- LinkedIn shipped **through #165** (content-pipeline Run 165, items 290). Resource-navigation lanes, each distinct, all tie to Community Intake (+ JobScout on the job lane): #160 employment/jobs · #161 veterans/VA · #162 disability/special-needs · #163 kinship-care · #164 domestic-violence / safety ministry · **#165 utility / energy-assistance ministry** (NEW lane: LIHEAP timing/priority window, PIPP income-capped bill + arrears forgiveness, cold-weather disconnection protection + physician medical certificate, free IHWAP weatherization incl. renters, deferred-payment arrangement + reconnection-deposit waiver, stacked ComEd/Nicor/Peoples Gas hardship grants, CUB free bill audit; analog = funded CEDA/LIHEAP caseworker, real help via CEDA intake / 2-1-1 / utility hardship line). Adds a **carbon-monoxide safety note** (never heat with an oven/stove/grill; gas-smell emergency line) as a deliberate template deviation for the higher risk profile.

## Open infra carry (updated)
1. 🔴 **Fund OpenAI key (billing)** — unblocks Phase-2 ChatGPT path only; code-gen already covered by Claude default.
2. **Formspree env vars on Vercel** → psychic-bassoon PR#1.
3. **Supabase project + 4 Vercel env vars** → PR#11.
4. 🔴 **Switch Supabase email templates to `token_hash` form (or add `?code=` fallback)** → unblocks forming-paws PR#16 signup confirmation (PR#17 merges after).
5. 🔴🔴 **Year-aware deadline comparison in the grant filter — CONFIRMED RECURRING (perplexity 09:28Z).** Drop any candidate whose deadline year < current year (or date < today). Deterministic post-filter, NOT LLM self-check (perplexity's year-reasoning is non-deterministic — right on some runs, inverted on others).
6. **NEW — branch-protection rule on forming-paws `main`** so the added `ci.yml` actually gates merges (codex Run 160; today `ci.yml` runs but is not required).
7. **Issue #8 (IL legal)** → on Stef. **ai-video-reel #5** → on Supabase.
8. `ANTHROPIC_API_KEY` for aeos/orchestrator (load-bearing given Claude is permanent code-gen default).

## Continuous
- Vault management (inbox, atomic notes, index, tag/link hygiene) across all PARA areas.
