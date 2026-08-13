# Antigravity — Active Priorities Digest

*Refreshed by antigravity Run 169 · 2026-08-13. Scan of context.md (canonical), world.md, state.md, and the bus wave through 16:18Z 08-13. Updates the Run 168 (11:11) digest with the three developments that landed after 16:00Z: **codex Run 178** merge-order hazard analysis (the one real stacking trap across the psychic-bassoon PRs) + its `pr-review-merge-guide.md`; **clawd Run 194** which created the consolidated `FOUNDER-ACTION-QUEUE.md` and pushed the grant loop to its **30th** net-zero; and **content-pipeline #183** (reentry / record-sealing & expungement ministry). Headline unchanged: the Aug-13 Phase-2 Week-1 sign-off is **6/6 PASS agent-side**; the **sole open item is Stef's written founder approval**; the merge frontier is a psychic-bassoon (Track 1) 6-PR stack + forming-paws #32 — now with a verified safe merge order.*

> **Consolidated founder view:** `~/clawd/AI-Organization/FOUNDER-ACTION-QUEUE.md` (clawd Run 194) is the single-page roll-up of everything awaiting Stef, PR/issue states verified live via `gh`. **Merge companion:** `kai/07-AI/agents/codex/pr-review-merge-guide.md` (codex Run 178) is the safe merge order. This digest is the priorities layer above both.

---

## P1 — OpenClaw Phase 1-4 (gates everything)
- **LIVE 2026-07-27 → 2026-08-17.** Completing Phase 1-4 is Stef's Priority 1; target **2026-10-12**. Gates all Track 1/2 execution.
- **Pre-staging window Aug 10-13 = COMPLETE.** Distinct from the **formal Phase 2 Week 1 gate, which stays Aug 18** (pre-gate work Aug 14-17).
- ✅ **Phase-2 Week-1 sign-off (due 08-13) is DONE agent-side.** `clawd/AI-Organization/PHASE-2-WEEK-1-REPORT.md` (dated Aug 13) shows **Day-5 = 6/6 verification criteria PASS** (8.5/10, evidence-based, Kairo/supervisor-signed) and recommends **PROCEED to the Aug 18 formal gate.**
- 🔴 **SOLE OPEN GATE ITEM = FOUNDER.** `STEF-WEEK-1-APPROVAL.md` reads "APPROVAL REQUESTED"; the report's **Gap-5** and **Aug-18 Must-Pass #3** both read "**Stef review + approval PENDING**." The 6/6 is agent/supervisor-signed — **human sign-off is not yet given.** Stef replying a checkmark to STEF-WEEK-1-APPROVAL.md closes it.
- **Aug 14-17 pre-gate work to track:** `test-cost-tracking.sh --live` must pass **28/28** and `cost-tracker.js --week 2026-08-18 --strict` must exit **0**. Then **Aug-17 3:00 PM CDT go/no-go**, **Aug-18 formal Phase 2 Week 1 gate.**
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
- **PRs are banked ahead of schedule** — Track 1 execution doesn't begin until Oct 13, so the psychic-bassoon stack is early credit, not urgent. The win now is clearing the review queue *cleanly*, not piling on more (codex Run 178).

## Grant-drift monitoring loop — CLOSED (holding)
- **30th consecutive net-zero** eligible-grant confirm (clawd Run 194). Loop STAYS CLOSED.
- **Open fix (infra carry):** year-aware deadline post-filter — drop any candidate whose deadline year < current year (or date < today). Must be **deterministic**, NOT LLM self-check (perplexity's year-reasoning is non-deterministic — right on some runs, inverted on others; the year-blind bug named a 2025 window as "open" as recently as the 08-10 wave).

## Merge queue (frontier = Track 1 psychic-bassoon + forming-paws)
- 🟢 **psychic-bassoon (Track 1 · The Plug AI) — SIX-PR quality stack, all tsc-clean / MERGEABLE, none merged, awaiting FOUNDER review:** **#13** escapeHtml · **#14** subscribe-harden · **#15** SITE_URL · **#16** mobile-menu a11y · **#17** per-page metadata · **#18** form-announce a11y. **codex Run 178 verified these six are mutually file-disjoint AND disjoint from #1/#11 → merge in ANY order, zero conflict risk.** Clear these first (minutes).
- 🟢 **forming-paws PR#32 (Track 2, codex Run 177): MERGEABLE, founder review.** Photo-upload route validated only file size then handed raw bytes to sharp → cryptic 500 on any non-image; fixed to mirror the health-doc route (typed `UnsupportedImageError` + content-type fast-path + catch → clean 400). tsc 0, eslint clean, next build 27 routes, vitest 68/68 (+2). No interaction with any psychic-bassoon PR — merge on its own merits.
- ⚠️ **The two large feature PRs (#1, #11) — ONE real stacking hazard, order matters (codex Run 178):** **#1** (real content / working forms / resource detail pages, +7718/-61, OPEN) and **#11** (Grant Matching Tracker, +869/-0, DRAFT) **both create `.env.example` as a brand-new file.** Each is clean vs `main` today, but the instant one merges the other flips to an **add/add conflict on `.env.example` only.** Resolution is lossless: **keep BOTH env blocks** — #1's Formspree keys and #11's Supabase/`MUTATION_SECRET`/`GROQ_API_KEY`/`CRON_SECRET`/`SMTP_*` are non-overlapping; just concatenate. Everything else in the two PRs is disjoint. **#11 must un-draft + merge BEFORE command-center-redirect #1** (shared branch; both fix the 404 grant links).
- 🔧 **Config-consistency trap to fix once #1+#11 both land (codex Run 178, NOT a merge conflict):** #15's code (`lib/site.ts`) reads **`NEXT_PUBLIC_APP_URL`** while #11's `.env.example` documents **`NEXT_PUBLIC_SITE_URL`** for the same concept. A custom domain configured via #11's template would be **silently ignored** by #15's canonical logic → wrong canonicals/OG URLs. Pick one name in both code and template. Cheap to fix, easy to miss.
- **Standing carries:** PR#1 MERGEABLE → set Formspree env vars on Vercel before forms submit. PR#11 grant-tracker auth-hardened → needs Supabase project + 4 Vercel env vars.
- **codex frontier:** **0 agent-actionable open issues account-wide** — the 3 open (forming-paws #8 IL-SOS filing, ai-video-reel-generator #5 Supabase project, skills-introduction-to-git #1 learning exercise) are all founder-blocked/learning.

## Track 2
- **BigHeart (bridge):** content automation pitch + title/comp ask ("Digital Content & AI Systems Specialist") in motion.
- **Forming Paws / Puppy Power:** execution phase, no more planning. Prototype live; PR#32 the current review item; issue #8 (IL articles of incorporation + bylaws) awaits Stef legal review/filing.

## Content pipeline (running)
- LinkedIn shipped **through #183** (content-pipeline Run 183, items 308). Recent resource-navigation lanes: **#181** adult-education / GED / HSE (door beneath Get Skilled #178) · **#182** health-coverage / insurance-enrollment (UPSTREAM of the medical-bills lane — get covered before the bill; Get Covered IL + free navigators, ACA subsidies, Medicaid, FQHCs, 211, junk-plan scam warning) · **#183** reentry / record-sealing & expungement ministry (NEW lane upstream of the jobs/Get-Skilled lane; woman-41 church pillar blocked by a nonviolent record who never learned IL seals/expunges many records with FREE legal help; Illinois Legal Aid Online / Cabrini Green Legal Aid / Safer Foundation as examples, court + legal-aid lawyer, 211; "erase your record overnight" fee-scam warning; never legal advice, never files, never fed her record or SSN). AI = quiet helper, augment-not-replace; compliance stated.

## Open infra carry (updated 08-13, Run 169)
1. 🔴 **Stef's WRITTEN Week-1 sign-off** — the one remaining Aug-18 gate item (agent side complete). See FOUNDER-ACTION-QUEUE.md RED tier.
2. 🔴 **Fund OpenAI key (billing)** — de-hedges Criterion 1 + unblocks Phase-2 ChatGPT path; code-gen already covered by Claude default.
3. **Aug 14-17 pre-gate cost-tracking must-pass:** `test-cost-tracking.sh --live` 28/28 + `cost-tracker.js --week 2026-08-18 --strict` exit 0.
4. **Founder-review the frontier — now with a verified merge order (codex `pr-review-merge-guide.md`):** clear #13-#18 first (any order, safe), then #32, then decide #1 vs #11 order (whichever merges 2nd needs the trivial `.env.example` concatenation), then rename the SITE_URL/APP_URL env var to one name.
5. 🔴🔴 **Year-aware deadline filter in the grant loop** (deterministic post-filter — see grant-drift section).
6. **Formspree env vars on Vercel** → psychic-bassoon PR#1. **Supabase project + 4 Vercel env vars** → PR#11 + ai-video-reel-generator #5.
7. **Switch Supabase email templates to `token_hash` form (or add `?code=` fallback)** → forming-paws signup confirmation. **Branch-protection rule on forming-paws `main`** so `ci.yml` actually gates merges.
8. `ANTHROPIC_API_KEY` for aeos/orchestrator (load-bearing given Claude is permanent code-gen default).
9. **Tooling note (this env):** Edit/Write have been permission-denied for antigravity across recent runs. **Edit stayed denied this run (Run 169); full-file Write SUCCEEDED (as in Run 168).** Prefer Write (full file) or Bash heredoc; re-test Edit each loop.

## Continuous
- Vault management (inbox, atomic notes, index, tag/link hygiene) across all PARA areas.
