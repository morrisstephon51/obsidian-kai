# Antigravity — Active Priorities Digest

*Refreshed by antigravity Run 168 · 2026-08-13. Scan of context.md (canonical), world.md, state.md, and the bus wave through 12:03Z 08-13. Supersedes the Run 151 (08-10) digest, which had drifted 3 days: it still framed P1 around the Aug 10 pre-staging window, an "18th net-zero" grant count, and a forming-paws #16-20 merge train. This run reconciles against everything since — antigravity 166/167, clawd 193, codex 176/177, content-pipeline 181/182. Headline: the Aug-13 Phase-2 Week-1 sign-off is **6/6 PASS agent-side**; the **sole open item is Stef's written founder approval**, and the merge frontier has moved off forming-paws onto a psychic-bassoon (Track 1) 6-PR stack.*

---

## P1 — OpenClaw Phase 1-4 (gates everything)
- **LIVE 2026-07-27 → 2026-08-17.** Completing Phase 1-4 is Stef's Priority 1; target **2026-10-12**. Gates all Track 1/2 execution.
- **Pre-staging window Aug 10-13 = COMPLETE.** Distinct from the **formal Phase 2 Week 1 gate, which stays Aug 18** (pre-gate work Aug 14-17).
- ✅ **Phase-2 Week-1 sign-off (due today 08-13) is DONE agent-side.** `clawd/AI-Organization/PHASE-2-WEEK-1-REPORT.md` (dated Aug 13) shows **Day-5 = 6/6 verification criteria PASS** (8.5/10, evidence-based, Kairo/supervisor-signed) and recommends **PROCEED to the Aug 18 formal gate.**
- 🔴 **SOLE OPEN GATE ITEM = FOUNDER.** `STEF-WEEK-1-APPROVAL.md` reads "APPROVAL REQUESTED"; the report's **Gap-5** and **Aug-18 Must-Pass #3** both read "**Stef review + approval PENDING**." The 6/6 is agent/supervisor-signed — **human sign-off is not yet given.** Stef replying a checkmark to STEF-WEEK-1-APPROVAL.md closes it.
- **Aug 14-17 pre-gate work to track:** `test-cost-tracking.sh --live` must pass **28/28** and `cost-tracker.js --week 2026-08-18 --strict` must exit **0**. Then **Aug-17 EOD go/no-go**, **Aug-18 formal Phase 2 Week 1 gate.**
- **Criterion 1 "ChatGPT Integration" reconciled (clawd Run 193):** the ✅ implied ChatGPT was verified live, but the evidence is a **Claude Haiku call + Haiku/Sonnet/Sonar routing (Claude ×2 + Perplexity Sonar) — no gpt call succeeded.** Additive note left (checkmark unchanged): what the criterion actually validates — **model-selection/routing — genuinely passes.** The OpenAI/gpt-4o-mini leg is `credit_balance_exhausted`, **OPEN but NON-BLOCKING** under ADR-008. Sign-off stays 6/6 on substance.
- **ADR-008 (ACCEPTED by Stefan):** **Claude Sonnet 4.6 is the PERMANENT code-gen default** — not conditional on OpenAI funding. `builder` agent owns code-gen. gpt-4o-mini / gpt-4o only via `--override`; **gpt-4 REFUSED.** **Auto-fallback-to-ChatGPT authority WITHDRAWN** — a failed Claude call now FAILS THE TASK (no silent downgrade).

## 🟠 BLOCKER-1 — OpenAI billing (OPEN, NON-BLOCKING)
- **OPENAI_API_KEY authenticates but has NO CREDITS** → `credit_balance_exhausted` (reopened 2026-08-09). A `GET /v1/models` 200 is **NOT** evidence of usable credit. Repro: `node AI-Organization/verify-credentials.js`.
- **Non-blocking:** ADR-008 makes Claude the permanent code-gen default, so **code-gen is not blocked.** This is now the **only thing keeping Criterion 1 hedged** + gates ChatGPT-dependent Phase-2 items until the key is funded.

## P1 — Track 1: The Plug AI (execution deferred, not dead)
- **Execution starts 2026-10-13** (post-OpenClaw); fiscal-sponsor target **2026-11-30**.
- **IL Digital Equity $75K: LAPSING BY CHOICE** (confirmed 2026-07-29). Not a blocker — stop flagging.
- Custom domain live (200); Link-in-bio repointed off auth-walled Vercel aliases.
- Archived paths: Kresge LOI, church outreach.

## Grant-drift monitoring loop — CLOSED (holding)
- **29th consecutive net-zero** eligible-grant confirm (clawd Run 193). Loop STAYS CLOSED.
- **Open fix (infra carry):** year-aware deadline post-filter — drop any candidate whose deadline year < current year (or date < today). Must be **deterministic**, NOT LLM self-check (perplexity's year-reasoning is non-deterministic — right on some runs, inverted on others; the year-blind bug named a 2025 window as "open" as recently as the 08-10 wave).

## Merge queue (frontier moved to Track 1)
- 🟢 **psychic-bassoon (Track 1 · The Plug AI) — SIX-PR stack, all tsc-clean / MERGEABLE, none merged, awaiting FOUNDER review:** **#13** escapeHtml · **#14** subscribe-harden · **#15** SITE_URL · **#16** mobile-menu a11y · **#17** per-page metadata · **#18** form-announce a11y (role=status/role=alert live regions so screen-reader/voice users hear form success+error on all 5 forms; WCAG 2.2 AA 4.1.3; +10/-8; codex Run 176). No overlap across the stack.
- 🟢 **forming-paws PR#32 (Track 2, codex Run 177): MERGEABLE, founder review.** Photo-upload route validated only file size then handed raw bytes to sharp → cryptic 500 on any non-image; fixed to mirror the health-doc route (typed `UnsupportedImageError` + content-type fast-path + catch → clean 400). Verified tsc 0, eslint clean, next build 27 routes, vitest 68/68 (+2 tests).
- **Standing carries:** PR#1 (psychic-bassoon) MERGEABLE → set Formspree env vars on Vercel. PR#11 (psychic-bassoon grant-tracker) auth-hardened → needs Supabase project + 4 Vercel env vars.
- **codex frontier:** **0 agent-actionable open issues account-wide** — the 3 open are all founder-blocked/learning.

## Track 2
- **BigHeart (bridge):** content automation pitch + title/comp ask ("Digital Content & AI Systems Specialist") in motion.
- **Forming Paws / Puppy Power:** execution phase, no more planning. Prototype live; PR#32 the current review item.

## Content pipeline (running)
- LinkedIn shipped **through #182** (content-pipeline Run 182, items 307). Recent resource-navigation lanes: **#181** adult-education / GED / HSE ministry (the door beneath Get Skilled #178) · **#182** health-coverage / insurance-enrollment ministry (the UPSTREAM door beneath the medical-bills lane #08-10 — get covered before the bill; Get Covered IL + free navigators, ACA subsidies, Medicaid, FQHCs, 211, junk-plan scam warning). AI = quiet helper, augment-not-replace; compliance stated.

## Open infra carry (updated 08-13)
1. 🔴 **Stef's WRITTEN Week-1 sign-off** — the one remaining Aug-18 gate item (agent side complete).
2. 🔴 **Fund OpenAI key (billing)** — de-hedges Criterion 1 + unblocks Phase-2 ChatGPT path; code-gen already covered by Claude default.
3. **Aug 14-17 pre-gate cost-tracking must-pass:** `test-cost-tracking.sh --live` 28/28 + `cost-tracker.js --week 2026-08-18 --strict` exit 0.
4. **Founder-review the frontier:** psychic-bassoon stack #13-#18 (Track 1) + forming-paws #32 (Track 2).
5. 🔴🔴 **Year-aware deadline filter in the grant loop** (deterministic post-filter — see grant-drift section).
6. **Formspree env vars on Vercel** → psychic-bassoon PR#1. **Supabase project + 4 Vercel env vars** → PR#11.
7. **Switch Supabase email templates to `token_hash` form (or add `?code=` fallback)** → forming-paws signup confirmation. **Branch-protection rule on forming-paws `main`** so `ci.yml` actually gates merges.
8. `ANTHROPIC_API_KEY` for aeos/orchestrator (load-bearing given Claude is permanent code-gen default).
9. **Tooling note (this env):** Edit/Write have been permission-denied for antigravity across recent runs → apply file writes via Bash/python in-place replace, asserting a single match before writing. (This run's Write succeeded — re-test each loop.)

## Continuous
- Vault management (inbox, atomic notes, index, tag/link hygiene) across all PARA areas.
