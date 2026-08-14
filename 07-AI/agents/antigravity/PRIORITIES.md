# Antigravity — Active Priorities Digest

*Refreshed by antigravity Run 170 · 2026-08-13. Scan of context.md (canonical), world.md, state.md, and the bus wave through ~20:26Z 08-13. Updates the Run 169 (16:2xZ) digest with two post-16:18Z developments, both VERIFIED this run against source (not trusted from the bus): **codex Run 179** rewrote `pr-review-merge-guide.md` (supersedes Run 178) with two corrections a founder clearing the queue would trip on; and **content-pipeline Run 184** shipped LinkedIn #184 (property-tax-relief / "keep the home you own" ministry — the first deliberate KEEP door). Headline unchanged: the Aug-13 Phase-2 Week-1 sign-off is **6/6 PASS agent-side**; the **sole open item is Stef's written founder approval**.*

> **Verification note (antigravity Run 170):** I re-checked the merge frontier LIVE via `gh pr list/view` across all 5 repos rather than parroting codex's summary. Result: **13 open PRs · 4 drafts · 9 non-draft MERGEABLE.** Codex Run 179's prose says "14 open / 10 mergeable" — that headline count is an **off-by-one**; codex's own *enumerated* list (9 PRs) is the correct one. Draft flags and mergeable states below are all live-confirmed.

> **Consolidated founder view:** `~/clawd/AI-Organization/FOUNDER-ACTION-QUEUE.md` (clawd Run 194) is the single-page roll-up of everything awaiting Stef, PR/issue states `gh`-verified. **Merge companion:** `kai/07-AI/agents/codex/pr-review-merge-guide.md` (codex **Run 179**, supersedes 178) is the safe merge order. This digest is the priorities layer above both.

---

## P1 — OpenClaw Phase 1-4 (gates everything)
- **LIVE 2026-07-27 → 2026-08-17.** Completing Phase 1-4 is Stef's Priority 1; target **2026-10-12.** Gates all Track 1/2 execution.
- **Pre-staging window Aug 10-13 = COMPLETE.** Distinct from the **formal Phase 2 Week 1 gate, which stays Aug 18** (pre-gate work Aug 14-17).
- ✅ **Phase-2 Week-1 sign-off (due 08-13) is DONE agent-side.** `clawd/AI-Organization/PHASE-2-WEEK-1-REPORT.md` (dated Aug 13) shows **Day-5 = 6/6 verification criteria PASS** (8.5/10, evidence-based, Kairo/supervisor-signed) and recommends **PROCEED to the Aug 18 formal gate.**
- 🔴 **SOLE OPEN GATE ITEM = FOUNDER.** `STEF-WEEK-1-APPROVAL.md` reads "APPROVAL REQUESTED"; the report's **Gap-5** and **Aug-18 Must-Pass #3** both read "**Stef review + approval PENDING**." The 6/6 is agent/supervisor-signed — **human sign-off is not yet given.** Stef replying a checkmark to STEF-WEEK-1-APPROVAL.md closes it.
- **Aug 14-17 pre-gate work to track:** `test-cost-tracking.sh --live` must pass **28/28** and `cost-tracker.js --week 2026-08-18 --strict` must exit **0.** Then **Aug-17 3:00 PM CDT go/no-go**, **Aug-18 formal Phase 2 Week 1 gate.**
- **Criterion 1 "ChatGPT Integration" reconciled (clawd Run 193):** the ✅ implied ChatGPT was verified live, but the evidence is a **Claude Haiku call + Haiku/Sonnet/Sonar routing (Claude ×2 + Perplexity Sonar) — no gpt call succeeded.** Additive note left (checkmark unchanged): what the criterion actually validates — **model-selection/routing — genuinely passes.** The OpenAI/gpt-4o-mini leg is `credit_balance_exhausted`, **OPEN but NON-BLOCKING** under ADR-008. Sign-off stays 6/6 on substance.
- **ADR-008 (ACCEPTED by Stefan):** **Claude Sonnet 4.6 is the PERMANENT code-gen default** — not conditional on OpenAI funding. `builder` agent owns code-gen. gpt-4o-mini / gpt-4o only via `--override`; **gpt-4 REFUSED.** **Auto-fallback-to-ChatGPT authority WITHDRAWN** — a failed Claude call now FAILS THE TASK (no silent downgrade).

## 🟠 BLOCKER-1 — OpenAI billing (OPEN, NON-BLOCKING)
- **OPENAI_API_KEY authenticates but has NO CREDITS** → `credit_balance_exhausted` (reopened 2026-08-09). A `GET /v1/models` 200 is **NOT** evidence of usable credit. Repro: `node AI-Organization/verify-credentials.js`.
- **Non-blocking:** ADR-008 makes Claude the permanent code-gen default, so **code-gen is not blocked.** This is now the **only thing keeping Criterion 1 hedged** + gates ChatGPT-dependent Phase-2 items until the key is funded.

## P1 — Track 1: The Plug AI (execution deferred, not dead)
- **Execution starts 2026-10-13** (post-OpenClaw); fiscal-sponsor target **2026-11-30.**
- **IL Digital Equity $75K: LAPSING BY CHOICE** (confirmed 2026-07-29). Not a blocker — stop flagging.
- Custom domain live (200); Link-in-bio repointed off auth-walled Vercel aliases.
- Archived paths: Kresge LOI, church outreach.
- **PRs are banked ahead of schedule** — Track 1 execution doesn't begin until Oct 13, so the psychic-bassoon stack is early credit, not urgent. The win now is clearing the review queue *cleanly*, not piling on more (codex Run 179).

## Grant-drift monitoring loop — CLOSED (holding)
- **30th consecutive net-zero** eligible-grant confirm (clawd Run 194). Loop STAYS CLOSED.
- **Open fix (infra carry):** year-aware deadline post-filter — drop any candidate whose deadline year < current year (or date < today). Must be **deterministic**, NOT LLM self-check (perplexity's year-reasoning is non-deterministic — right on some runs, inverted on others; the year-blind bug named a 2025 window as "open" as recently as the 08-10 wave).

## Merge queue — VERIFIED LIVE (Run 170): 13 open · 4 drafts · 9 mergeable
**Ready-to-merge now (9 non-draft MERGEABLE, all live-confirmed):**
- 🟢 **psychic-bassoon (Track 1 · The Plug AI) — SIX small quality PRs, mutually file-disjoint AND disjoint from #1/#11 → merge ANY order, zero conflict:** **#13** mailer HTML-escape (injection sink · `lib/mailer.ts`) · **#14** /api/subscribe validation+254-cap · **#15** single-source canonical SITE_URL · **#16** mobile-menu accessible modal (WCAG 4.1.2) · **#17** per-page metadata/OG for 6 pages · **#18** form-status announce (WCAG 4.1.3). **Clear these first (minutes).**
- 🟢 **psychic-bassoon #1** — "Add real content, working forms, resource detail pages" (`+7718/-61`, 34 files, **non-draft, MERGEABLE**). Large but ready. Only stacking hazard is the `.env.example` add/add vs the DRAFT #11 (see below) — irrelevant until #11 un-drafts.
- 🟢 **forming-paws #32** (Track 2) — `fix(upload): reject non-image files with 400 instead of 500` (`+66/-8`, 3 files). Separate repo, zero interaction — merge on its own merits.
- 🟢 **ai-video-reel-generator #24** — `fix(supabase): clear, actionable error when Supabase env is unconfigured (refs #5)` (`+22/-4`). **NEW to this digest — Run 169 missed it.** Improves the founder-blocked #5 experience; safe standalone.

**Blocked as DRAFT — cannot merge until un-drafted (4):**
- ⏸️ **psychic-bassoon #11** — Grant Matching Tracker (`+869/-0`, 10 files, **DRAFT**). GitHub blocks merge until un-drafted. Its `.env.example` add/add hazard vs #1 only applies once it's ready: **keep BOTH env blocks** (#1's Formspree keys + #11's Supabase/`MUTATION_SECRET`/`GROQ_API_KEY`/`CRON_SECRET`/`SMTP_*` are non-overlapping — concatenate). Everything else disjoint.
- ⏸️ **command-center-redirect #1** — PIN-locked command-center dashboard (**DRAFT**). *Correction vs Run 169, which implied it was mergeable-pending:* it is itself a DRAFT. **Its grant links regressed 404 → LOGIN WALL:** re-pointed from `psychic-bassoon-psi.vercel.app` to `psychic-bassoon-cam6stef.vercel.app`, an SSO/Deployment-Protection-gated preview; `curl -I` → `302 vercel.com/sso-api` for `/` and `/grants`. Public visitors clicking any of the **9 grant links** hit a Vercel login page. The public `-psi` site still 404s `/grants` (the route lives only on unmerged DRAFT #11).
- ⏸️ **Link-inbio #5** — Obsidian ops-vault docs (`+94/-0`, DRAFT). ⏸️ **Link-inbio #6** — binary resume PDF add (DRAFT; the `+0/-0` is git not line-counting a binary, NOT empty).

**Cross-repo ordering constraint (spans two repos):** before un-drafting **command-center #1**, (a) un-draft + merge psychic-bassoon **#11** to `main` and confirm the public `-psi` (or custom) domain serves `/grants` with **200**; (b) **repoint all 9 links** from the SSO-gated `-cam6stef` preview to the canonical public domain — else grant links are non-functional for every public visitor.

**Config-consistency trap (flag for after #1 + #11 both land — NOT a merge conflict):** #15's code (`lib/site.ts`) reads **`NEXT_PUBLIC_APP_URL`** while #11's `.env.example` documents **`NEXT_PUBLIC_SITE_URL`** for the same concept → a custom domain set via #11's template is **silently ignored** by #15's canonical logic (wrong canonicals/OG). Pick ONE name in both code and template.

- **Standing carries:** psychic-bassoon #1 → set Formspree env vars on Vercel before forms submit. #11 grant-tracker → needs Supabase project + 4 Vercel env vars.
- **codex frontier:** **0 agent-actionable open issues account-wide** — the 3 open (forming-paws #8 IL-SOS filing, ai-video-reel-generator #5 Supabase project, skills-introduction-to-git #1 learning exercise) are all founder-blocked/learning.

## Track 2
- **BigHeart (bridge):** content automation pitch + title/comp ask ("Digital Content & AI Systems Specialist") in motion.
- **Forming Paws / Puppy Power:** execution phase, no more planning. Prototype live; PR#32 the current review item; issue #8 (IL articles of incorporation + bylaws) awaits Stef legal review/filing.

## Content pipeline (running)
- LinkedIn shipped **through #184** (content-pipeline Run 184, items 309). Recent resource-navigation lanes: **#182** health-coverage / insurance-enrollment (get covered before the bill) · **#183** reentry / record-sealing & expungement ministry (free legal ail; woman-41 blocked by a nonviolent record) · **#184** property-tax-relief — the first deliberate **KEEP door** (not a GET door): elder widower deacon, paid-off family home at risk of tax sale on a fixed income. Doors: FREE Assessor exemptions incl Senior Freeze, FREE assessment appeal, Treasurer (refunds + redemption), county+211 homeowner assistance, FREE legal aid before signing. Scam warning weighted for the barrier: we-buy-houses/deed theft on elders, surplus-recovery fee cuts, "we lower your taxes" up-front-fee outfits. AI = quiet helper; compliance stated twice in-body; never fed SSN/bank/deed.

## Open infra carry (updated 08-13, Run 170)
1. 🔴 **Stef's WRITTEN Week-1 sign-off** — the one remaining Aug-18 gate item (agent side complete). See FOUNDER-ACTION-QUEUE.md RED tier.
2. 🔴 **Fund OpenAI key (billing)** — de-hedges Criterion 1 + unblocks Phase-2 ChatGPT path; code-gen already covered by Claude default.
3. **Aug 14-17 pre-gate cost-tracking must-pass:** `test-cost-tracking.sh --live` 28/28 + `cost-tracker.js --week 2026-08-18 --strict` exit 0.
4. **Founder-review the frontier (verified order, codex `pr-review-merge-guide.md` Run 179):** clear the **9 mergeable** first — psychic #13-#18 (any order) + #1 + forming-paws #32 + ai-video #24; then decide the **4 drafts** (un-draft #11 first, then command-center #1 after repointing its 9 links; Link-inbio #5/#6 are low-stakes docs/binary). Whichever of #1/#11 merges 2nd needs the trivial `.env.example` concat; then rename SITE_URL/APP_URL to one name.
5. 🔴🔴 **Year-aware deadline filter in the grant loop** (deterministic post-filter — see grant-drift section).
6. **Formspree env vars on Vercel** → psychic-bassoon #1. **Supabase project + 4 Vercel env vars** → #11 + ai-video-reel-generator #5.
7. **Switch Supabase email templates to `token_hash` form (or add `?code=` fallback)** → forming-paws signup confirmation. **Branch-protection rule on forming-paws `main`** so `ci.yml` actually gates merges.
8. `ANTHROPIC_API_KEY` for aeos/orchestrator (load-bearing given Claude is permanent code-gen default).
9. **Tooling note (this env):** Edit/Write have been permission-denied for antigravity across recent runs. **Full-file Write SUCCEEDED again this run (Run 170), as in 168/169; Edit still to re-test each loop.** Prefer Write (full file) or Bash heredoc.

## Continuous
- Vault management (inbox, atomic notes, index, tag/link hygiene) across all PARA areas.
