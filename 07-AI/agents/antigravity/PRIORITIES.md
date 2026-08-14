# Antigravity — Active Priorities Digest

*Refreshed by antigravity Run 172 · 2026-08-14. Scan of context.md (canonical), world.md, state.md, and the bus wave through ~06:08Z 08-14. Updates the Run 171 digest with the two post-01:18Z loop-end messages, both VERIFIED this run against source (not trusted from the bus): **codex Run 181** shipped forming-paws **PR #34** (browse-age calendar fix); **content-pipeline Run 186** shipped LinkedIn #186 (student-loan-repayment ministry). Headline unchanged: the Aug-13 Phase-2 Week-1 sign-off is **6/6 PASS agent-side**; the **sole open item is Stef's written founder approval**.*

> **Verification note (antigravity Run 172):** I re-checked the merge frontier LIVE via `gh pr list/view` across all 5 repos again. Result: **14 open PRs · 4 drafts · 10 non-draft MERGEABLE** — up exactly +1/+1 from Run 171's 13/4/9. **The +1 is legitimate, NOT an off-by-one:** it is forming-paws **#34**, a real new PR codex shipped in Run 181. I verified it directly: non-draft, `mergeable=MERGEABLE`, `mergeStateStatus=CLEAN`, and **file-disjoint from #32** (#32 = `app/api/upload/photo/route.ts` + `lib/image.ts` + test; #34 = `app/browse/page.tsx` + `lib/age.ts` + test — zero shared files), so codex's "zero overlap with #32" claim CHECKS OUT and both merge in any order. **`gh pr list` gotcha re-confirmed:** BOTH forming-paws PRs (#32 AND #34) came back `mergeable: UNKNOWN` at the list level (stale cache); a direct `gh pr view` forced GitHub to recompute → both **MERGEABLE / CLEAN.** Always resolve an UNKNOWN with a direct view before counting it out.

> **Consolidated founder view:** `~/clawd/AI-Organization/FOUNDER-ACTION-QUEUE.md` (clawd Run 196) is the single-page roll-up of everything awaiting Stef, PR/issue states `gh`-verified. **Merge companion:** `kai/07-AI/agents/codex/pr-review-merge-guide.md` (codex **Run 179/180**) is the safe merge order. This digest is the priorities layer above both. NOTE: both of those predate forming-paws #34 — the merge guide should gain #34 alongside #32 (same repo, disjoint, either order).

---

## P1 — OpenClaw Phase 1-4 (gates everything)
- **LIVE 2026-07-27 → 2026-08-17.** Completing Phase 1-4 is Stef's Priority 1; target **2026-10-12.** Gates all Track 1/2 execution.
- **Pre-staging window Aug 10-13 = COMPLETE.** Distinct from the **formal Phase 2 Week 1 gate, which stays Aug 18** (pre-gate work Aug 14-17). **Today is Aug 14 — pre-gate window is now OPEN.**
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
- **PRs are banked ahead of schedule** — Track 1 execution doesn't begin until Oct 13, so the psychic-bassoon stack is early credit, not urgent. The win now is clearing the review queue *cleanly*, not piling on more (codex Run 179/180).

## Grant-drift monitoring loop — CLOSED (holding)
- **30th consecutive net-zero** eligible-grant confirm (clawd Run 194). Loop STAYS CLOSED.
- **Open fix (infra carry):** year-aware deadline post-filter — drop any candidate whose deadline year < current year (or date < today). Must be **deterministic**, NOT LLM self-check (perplexity's year-reasoning is non-deterministic — right on some runs, inverted on others; the year-blind bug named a 2025 window as "open" as recently as the 08-10 wave).

## Merge queue — RE-VERIFIED LIVE (Run 172): 14 open · 4 drafts · 10 mergeable
**Ready-to-merge now (10 non-draft MERGEABLE, all live-confirmed this run):**
- 🟢 **psychic-bassoon (Track 1 · The Plug AI) — SIX small quality PRs, mutually file-disjoint AND disjoint from #1/#11 → merge ANY order, zero conflict:** **#13** mailer HTML-escape (injection sink · `lib/mailer.ts`) · **#14** /api/subscribe validation+254-cap · **#15** single-source canonical SITE_URL (**codex Run 180 hardened this** — now resolves `APP_URL ?? SITE_URL ?? default`, backward-compatible, tsc-clean) · **#16** mobile-menu accessible modal (WCAG 4.1.2) · **#17** per-page metadata/OG for 6 pages · **#18** form-status announce (WCAG 4.1.3). **Clear these first (minutes).**
- 🟢 **psychic-bassoon #1** — "Add real content, working forms, resource detail pages" (`+7718/-61`, 34 files, **non-draft, MERGEABLE**). Large but ready. Only stacking hazard is the `.env.example` add/add vs the DRAFT #11 (see below) — irrelevant until #11 un-drafts.
- 🟢 **forming-paws #32** (Track 2) — `fix(upload): reject non-image files with 400 instead of 500` (`+66/-8`, 3 files: `app/api/upload/photo/route.ts`, `lib/image.ts`, test). **NB: `gh pr list` reported UNKNOWN this run (stale cache); direct `gh pr view` → MERGEABLE / CLEAN.**
- 🟢 **forming-paws #34** (Track 2 · NEW, codex Run 181) — `fix(browse): count age in calendar years so the label matches the filter` (`+97/-5`, 3 files: `app/browse/page.tsx`, `lib/age.ts`, test). Real filter/display contradiction (365.25-day label vs calendar-math RPC filter → dog born exactly 1yr ago showed "0yo" under "min age 1yr"). Root-cause fix extracts `lib/age.ts` computing calendar years like Postgres `age()`; +9 unit tests. **FILE-DISJOINT from #32 → merge either order.** Also came back UNKNOWN at list level; direct view → MERGEABLE / CLEAN.
- 🟢 **ai-video-reel-generator #24** — `fix(supabase): clear, actionable error when Supabase env is unconfigured (refs #5)` (`+22/-4`). Improves the founder-blocked #5 experience; safe standalone.

**Blocked as DRAFT — cannot merge until un-drafted (4):**
- ⏸️ **psychic-bassoon #11** — Grant Matching Tracker (`+869/-0`, 10 files, **DRAFT**). GitHub blocks merge until un-drafted. Its `.env.example` add/add hazard vs #1 only applies once it's ready: **keep BOTH env blocks** (#1's Formspree keys + #11's Supabase/`MUTATION_SECRET`/`GROQ_API_KEY`/`CRON_SECRET`/`SMTP_*` are non-overlapping — concatenate). Everything else disjoint.
- ⏸️ **command-center-redirect #1** — PIN-locked command-center dashboard (`+514/-5`, **DRAFT**). **Its grant links regressed 404 → LOGIN WALL:** re-pointed from `psychic-bassoon-psi.vercel.app` to `psychic-bassoon-cam6stef.vercel.app`, an SSO/Deployment-Protection-gated preview; `curl -I` → `302 vercel.com/sso-api` for `/` and `/grants`. Public visitors clicking any of the **9 grant links** hit a Vercel login page. The public `-psi` site still 404s `/grants` (the route lives only on unmerged DRAFT #11).
- ⏸️ **Link-inbio #5** — Obsidian ops-vault docs (`+94/-0`, DRAFT). ⏸️ **Link-inbio #6** — binary resume PDF add (DRAFT; the `+0/-0` is git not line-counting a binary, NOT empty).

**Cross-repo ordering constraint (spans two repos):** before un-drafting **command-center #1**, (a) un-draft + merge psychic-bassoon **#11** to `main` and confirm the public `-psi` (or custom) domain serves `/grants` with **200**; (b) **repoint all 9 links** from the SSO-gated `-cam6stef` preview to the canonical public domain — else grant links are non-functional for every public visitor.

**Config-consistency trap — ✅ RESOLVED IN CODE (codex Run 180):** the prior trap — #15's `lib/site.ts` read only `NEXT_PUBLIC_APP_URL` while #11's `.env.example` documents `NEXT_PUBLIC_SITE_URL` for the same concept (a custom domain set via #11's template would be silently ignored) — is now **closed**: codex's PR #15 resolves `APP_URL ?? SITE_URL ?? default` (backward-compatible, neither set = byte-identical prod, runtime-proved all 4 env states). No rename needed post-merge; just land #15 and #11.

- **Standing carries:** psychic-bassoon #1 → set Formspree env vars on Vercel before forms submit. #11 grant-tracker → needs Supabase project + 4 Vercel env vars.
- **codex frontier:** **0 agent-actionable open issues account-wide** — the 3 open (forming-paws #8 IL-SOS filing, ai-video-reel-generator #5 Supabase project, skills-introduction-to-git #1 learning exercise) are all founder-blocked/learning.

## Track 2
- **BigHeart (bridge):** content automation pitch + title/comp ask ("Digital Content & AI Systems Specialist") in motion.
- **Forming Paws / Puppy Power:** execution phase, no more planning. Prototype live; **PR#32 (upload validation) + PR#34 (browse-age fix)** are the current review items — both mergeable, disjoint; issue #8 (IL articles of incorporation + bylaws) awaits Stef legal review/filing.

## Content pipeline (running)
- LinkedIn shipped **through #186** (content-pipeline Run 186, items 311). Recent resource-navigation lanes: **#183** reentry / record-sealing & expungement · **#184** property-tax-relief (first deliberate KEEP door) · **#185** unemployment-insurance / layoff-bridge (woman-52, 14yr housekeeping, laid off) · **#186** student-loan-repayment / getting-out-from-under-the-debt ministry — NEW lane distinct from FAFSA #175 (getting INTO college): the debt that comes home WITH the degree. Persona: first-gen college grad MAN, 28, low-paid public-service worker near/in default, ashamed to tell family; rotates gender back to a man + age younger off the 40s-60s run. Quiet-helper AI explains income-driven repayment / PSLF / curing default in plain words; 8 hedged doors incl. official federal student-aid site + real servicer, free nonprofit counseling, free legal aid, 211, HARD scam warning on debt-relief/forgiveness-for-a-fee outfits. Compliance twice, applying is FREE, never feed FSA password/SSN to AI or a third party; deliberately did NOT assert any current plan name/amount/program status (policy in flux).

## Open infra carry (updated 08-14, Run 172)
1. 🔴 **Stef's WRITTEN Week-1 sign-off** — the one remaining Aug-18 gate item (agent side complete). See FOUNDER-ACTION-QUEUE.md RED tier.
2. 🔴 **Fund OpenAI key (billing)** — de-hedges Criterion 1 + unblocks Phase-2 ChatGPT path; code-gen already covered by Claude default.
3. **Aug 14-17 pre-gate cost-tracking must-pass:** `test-cost-tracking.sh --live` 28/28 + `cost-tracker.js --week 2026-08-18 --strict` exit 0. **Window is open as of today (Aug 14).**
4. **Founder-review the frontier (verified order, codex `pr-review-merge-guide.md` Run 179/180):** clear the **10 mergeable** first — psychic #13-#18 (any order) + #1 + forming-paws #32 + **forming-paws #34** + ai-video #24; then decide the **4 drafts** (un-draft #11 first, then command-center #1 after repointing its 9 links; Link-inbio #5/#6 are low-stakes docs/binary). Whichever of #1/#11 merges 2nd needs the trivial `.env.example` concat; the SITE_URL/APP_URL rename is **no longer needed** (codex #15 resolved it in code). **Add #34 to the merge guide** — it postdates Run 179/180.
5. 🔴🔴 **Year-aware deadline filter in the grant loop** (deterministic post-filter — see grant-drift section).
6. **Formspree env vars on Vercel** → psychic-bassoon #1. **Supabase project + 4 Vercel env vars** → #11 + ai-video-reel-generator #5.
7. **Switch Supabase email templates to `token_hash` form (or add `?code=` fallback)** → forming-paws signup confirmation. **Branch-protection rule on forming-paws `main`** so `ci.yml` actually gates merges.
8. `ANTHROPIC_API_KEY` for aeos/orchestrator (load-bearing given Claude is permanent code-gen default).
9. **Tooling note (this env):** full-file **Write SUCCEEDED again this run (Run 172)**, as in 168-171 — used for PRIORITIES.md + state.md. **Edit re-tested Run 172 → STILL permission-denied** (re-confirmed live this run). Prefer Write (full file) or Bash heredoc.

## Continuous
- Vault management (inbox, atomic notes, index, tag/link hygiene) across all PARA areas.
