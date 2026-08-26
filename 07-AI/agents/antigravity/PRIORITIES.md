# Antigravity — Active Priorities Digest

*Refreshed by antigravity **Run 212** · 2026-08-23 (~19:25Z). This run: re-scanned context (context.md canonical + world.md), polled the bus, **re-measured the sole cold P1 at the file** (`stat` mtime + status-line read on `STEF-WEEK-1-APPROVAL.md`) → still `**Status:** APPROVAL REQUESTED`, mtime byte-frozen `2026-08-11T14:31:48Z UTC` (3125 bytes, unmoved), now **12.20 days cold** (up from 12.03 at Run 211), and **source-verified every frontier PR at GitHub** (verify-don't-trust-the-bus). **Deltas folded in this run:** (a) **ZERO founder action since Run 211** — psychic-bassoon #20/#19/#1 and jobscout #7 all re-verified **OPEN/MERGEABLE/CLEAN** at source; nothing merged, nothing closed, gate still unsigned. (b) **NEW green one-click PR confirmed real:** codex Run 222 shipped **job_opportunity_scanner PR#8** (`_title_score` matched `TITLE_SIGNALS` by bare substring → "ai" false-hit retAIl/mAIntenance/repAIr/trAIner on the 40%-weight signal; fixed with word-boundary regex, +first tests in the repo 3/3 pass) — bus-claimed, now **source-verified OPEN/MERGEABLE/CLEAN** at GitHub. jobscout now has **TWO** green one-click PRs (#7 location + #8 title, independent files). (c) **forming-paws re-confirmed caught up** — zero open PRs, `main` = `01537c3` (#61). **Net agent-actionable open items remains 0** — every lever is founder-authority. Reframed frontier is now **1 signature + 1 close (PR#1) + 4 green one-click merges (#19, #20, jobscout #7, jobscout #8)**. Prior deltas held: psychic-bassoon `main` = `a515639` (#18) hardened; forming-paws visual-refresh epic (#61+#62) still merged/live; PR#1 → **CLOSE (obsolete, settled — do NOT re-litigate)**.*

---

## 🔴 THE ONE THING — Sole open P1 is the FOUNDER signature (now 12.20 days cold)
- `~/clawd/AI-Organization/STEF-WEEK-1-APPROVAL.md` **still reads `**Status:** APPROVAL REQUESTED`** — mtime **2026-08-11T14:31:48Z UTC**, re-verified live at the file this run → **12.20 days cold** (up from 12.03 at Run 211; byte-for-byte unmoved since Aug 11, 3125 bytes).
- The report is **✅ Week-1 PASS (12 tasks, 3.34× avg speedup, zero escalations, 8.6/10 confidence)** and recommends **APPROVE → proceed to Phase-2 Week-2**. Everything is agent/supervisor-signed; **only Stef's written checkmark is missing.**
- **The gate is aging, not thawing.** The Aug-17 3pm go/no-go and the Aug-18 formal Phase-2 Week-1 gate are both behind us. Nothing agent-side is blocked on producing more — the single remaining act is the founder signing this one file. *(Reply line in-file: ✅ approve | 🔍 review further | 📋 questions.)*

## P1 — OpenClaw Phase 1-4 (gates all Track 1/2 execution)
- **Phase 1 LIVE 2026-07-27 → 2026-08-17.** Completing Phase 1-4 is Stef's Priority 1; target **2026-10-12.**
- Phase-2 Week-1 sign-off is **DONE agent-side** (Week-1 PASS report). Sole open item = the founder gate above.
- **ADR-008 (ACCEPTED):** Claude Sonnet 4.6 is the **PERMANENT code-gen default** — a failed Claude call FAILS the task (no silent downgrade to gpt-4). Not conditional on OpenAI funding.

## 🟠 OpenAI billing (OPEN, NON-BLOCKING)
- `OPENAI_API_KEY` authenticates but has **no credits** (`credit_balance_exhausted`). A `GET /v1/models` 200 is NOT usable-credit evidence.
- **Non-blocking** — ADR-008 makes Claude the permanent default. It only keeps **Criterion 1 hedged** + gates the Phase-2 ChatGPT leg. Funding it de-hedges Criterion 1.

---

## Merge frontier — source-verified at GitHub, Run 212
*The Aug-17 board (7 ready PRs) is GONE — it merged. The forming-paws visual-refresh epic is GONE too — it merged Run 211. What follows is the current frontier, **re-verified at source this run**. **Net: 0 agent-actionable open items account-wide.** Every remaining lever is founder-authority (sign / close / merge / set env / deploy) or a founder-owned draft. **FOUR** low-risk PRs are CI-green and merge-ready (2 Track-1 security + 2 jobscout scorer fixes).*

### 🟢 Track 1 · psychic-bassoon (theplugai.net) — `main` hardened; TWO green security PRs merge-ready; PR#1 → CLOSE
- **`main` HEAD = `a515639` (#18)** — production is **senior-grade and self-consistent**: `components/shared/EmailCapture.tsx` ships **`role=status` + `role=alert` (WCAG 4.1.3)** and a **first-party `fetch(/api/subscribe)`**; **every form-bearing CTA** (Contact / Community / Workshops / Footer-newsletter / Resources) carries BOTH the a11y announce AND a first-party `/api` call. 3 live API routes: `/api/contact`, `/api/subscribe`, `/api/workshop-request`. Lesson-data referential integrity confirmed (10 lessons, all 20 `nextSteps` refs resolve → zero broken `/learn/[slug]` links).
- **PR#20 "bump Next.js 14.2.5 → 14.2.35" (OPEN, non-draft, MERGEABLE, mergeState CLEAN, base `main`) — codex Run 220.** Within-minor patch (no breaking changes) closing published CVEs (cache-poison XSS 2024-46982, authz-bypass 2024-51479, middleware-bypass CVSS 9.1 2025-29927, cache-poison DoS 2025-49826) + image-optimizer hardening. Repo has **no CI at all**, so the outdated framework was invisible to every gate. Surgical 2-line `package.json` + regenerated lockfile. Vercel checks PASS → founder one-click merge, zero-risk. **Still unmerged (re-verified `updatedAt` 2026-08-22T21:57Z).** *Founder-merge-gated, not agent-actionable.*
- **PR#19 "HTTP security headers" (OPEN, non-draft, MERGEABLE, mergeState CLEAN, base `main`) — codex Run 219.** `async headers()` in `next.config.js` applying 5 render-neutral baseline headers to `/:path*` (X-Frame-Options SAMEORIGIN, X-Content-Type-Options nosniff, Referrer-Policy strict-origin-when-cross-origin, HSTS max-age=31536000+includeSubDomains, Permissions-Policy camera/mic/geo denied). **CSP deliberately omitted** (needs nonces + origin allow-list vs unsplash/picsum/placeholder + Next inline — a wrong CSP breaks prod). Zero risk to live pages; images config untouched. **Still unmerged (re-verified `updatedAt` 2026-08-22T07:31Z)** → founder one-click merge. *Founder-merge-gated.*
- **PR#1 "Add real content, working forms, resource detail pages" (OPEN, non-draft, MERGEABLE) → recommended action = CLOSE, do NOT merge.** Obsolete, not half-finished (settled Run 208 loop-break; do NOT re-litigate — redirect any peer who re-runs it here):
  - `NotifyModal.tsx` + `lib/formspree.ts` = **absent from main** → dead/abandoned path (main went API-routes, not Formspree/modal).
  - `lib/data/resources.ts` = **already on main** → duplicate.
  - `app/resources/[slug]/` = the **ONLY unique value** on the branch — but it opens `'use client'` with `useParams`/`useState` and exports **no `generateMetadata`/`metadata`** → SEO-regressed, cannot ship as-is.
  - **Salvage = re-author `resources/[slug]` as a NEW server-component PoC** (drop `'use client'`, add `generateMetadata`). Codex's corrected go/no-go is comment **5374338233**. *Closing PR#1 is a pending founder action.*
- **PR#11 "Grant Matching Tracker"** — founder-authored **DRAFT**, MERGEABLE, Track-1-relevant (grant matching ↔ Plug AI Grant Research). Needs a Supabase project + **8 Vercel env vars**. Founder-owned WIP, not agent-actionable.

### 🟢 Track 2 · job_opportunity_scanner — TWO green one-click scorer fixes (independent files)
- **PR#7 "match Illinois state code as a token, not a bare substring" (OPEN, non-draft, MERGEABLE, CLEAN) — codex Run 221.** `_location_score` bare-`il` substring false-positive → word-boundary `\bil\b`; verified across 12 cases. Founder-merge-gated.
- **PR#8 "match TITLE_SIGNALS as whole tokens, not bare substrings" (OPEN, non-draft, MERGEABLE, CLEAN) — codex Run 222, source-verified this run.** `_title_score` matched `TITLE_SIGNALS` by bare substring, so "ai" false-hit retAIl / mAIntenance / repAIr / trAIner on the **heaviest-weight (40%) signal**, corrupting top-3 ranking. Fixed with word-boundary regex (0 new deps); 6 false-positives → 0.0 with genuine titles preserved; added `tests/test_scorer.py` (repo had **zero** tests) 3/3 pass. Independent of #7's files. Founder-merge-gated.

### 🐾 Track 2 · forming-paws (Puppy Power) — visual-refresh epic MERGED, LIVE on main (re-confirmed caught up)
- **`main` HEAD = `01537c3` (#61)** — re-verified this run, **zero open PRs.** The founder merged the whole visual-refresh epic Run 211: **PR#62** (Newsreader + Public Sans typography, em-dashes stripped) → `feat/visual-refresh` at `2026-08-23T13:53:44Z`, then **PR#61** (imagery, design system, scroll motion, Sage; `+3320/-855`) → `main` at `2026-08-23T13:54:54Z`. The entire Aug-17 bug-clearing stack (#38–#48) AND the visual-refresh epic (#57–#62) are all in `main`.
- **Sole open issue #8** — IL articles of incorporation + bylaws drafted → **founder legal review/filing.** (Not a code lever.)

### ⏸️ Other repos — all founder-gated / human / draft
- **command-center-redirect PR#1** — keep **DRAFT** (PIN flaw; cross-repo ordering constraint on the grant links).
- **ai-video-reel-generator #5** — Supabase project setup → founder-gated (also blocks its PR#4 loop).
- **skills-introduction-to-git #1** — human git-learning exercise.
- **content-machine** — **ARCHIVED** → retired from the actionable set (its 4 draft PRs are dead; stop surfacing).

---

## Tracks (canonical, per context.md)
- **Track 1 · The Plug AI:** Execution starts **2026-10-13** (post-OpenClaw); fiscal-sponsor target **2026-11-30.** IL Digital Equity $75K is **LAPSING BY CHOICE** — not a blocker, stop flagging. theplugai.net production (`main`) is **banked and senior-grade**; the wins now are **closing the obsolete PR#1 cleanly** + **merging the two low-risk green security PRs (#19 headers, #20 CVE bump)**, not merging a 2-month-stale branch.
- **Track 2 · BigHeart (bridge):** content-automation pitch + "Digital Content & AI Systems Specialist" title/comp ask in motion.
- **Track 2 · Forming Paws / Puppy Power:** execution phase. Bug frontier cleared AND the visual-refresh epic merged into `main` (`01537c3`) — the app is fully caught up. Sole remaining item is founder legal filing (issue #8), not code.

## Content pipeline (running, healthy)
- LinkedIn shipped **through #227** (content-pipeline Run 227). Recent resource-navigation lanes: #223 FAFSA/free-federal-aid · #224 unemployment-insurance/workforce-help/benefit-scam · #225 utility-shutoff/energy-assistance (LIHEAP-CEDA)/disconnect-scam · #226 SNAP/food-assistance/EBT-skimming (working-single-mother persona) · **#227 prescription/medication affordability + Medicare Extra Help / Part D LIS / drug-maker patient assistance + Medicare-card/discount-card/copay scams** (retired-senior-man 67 persona — first senior in this run). Safety spine held every lane: quiet-helper / augment-not-replace, compliance stated twice, never fed an SSN/ITIN/EBT-PIN/Medicare-number/account/password/bank login.

## Open infra carry (all founder-authority)
1. 🔴 **Stef's written Week-1 sign-off** — the one remaining P1 gate item (agent side complete). **12.20 days cold, past its window.**
2. 🔴 **Close psychic-bassoon PR#1** — obsolete/superseded (codex comment 5374338233). Founder action.
3. 🟢 **Merge psychic-bassoon PR#20** — Next.js CVE patch bump, MERGEABLE, Vercel-GREEN; founder one-click, zero-risk. Still open.
4. 🟢 **Merge psychic-bassoon PR#19** — 5 baseline security headers, MERGEABLE, Vercel-GREEN; founder one-click. Still open.
5. 🟢 **Merge job_opportunity_scanner PR#7** — location-scoring root-cause fix; MERGEABLE/CLEAN; founder one-click.
6. 🟢 **Merge job_opportunity_scanner PR#8** — title-scoring root-cause fix (+first repo tests); MERGEABLE/CLEAN; founder one-click. *(New this run — codex Run 222, source-verified.)*
7. ✅ **forming-paws visual-refresh epic — MERGED (Run 211)** (#61 + #62 → `main` = `01537c3`; WebGL flag resolved). Lever closed; re-confirmed zero open PRs. Remaining forming-paws item = founder legal filing (issue #8).
8. 🟠 **Fund OpenAI key** — de-hedges Criterion 1; code-gen already covered by Claude default (non-blocking).
9. **Env carries:** 8 Vercel env vars + Supabase project → psychic-bassoon #11; Supabase setup → ai-video-reel-generator #5.
10. **Grant-drift loop = CLOSED** (deterministic year-aware post-filter: drop candidates whose deadline year < current or date < today). Stays closed.

## Continuous
- Vault management (inbox, atomic notes, index, tag/link hygiene) across all PARA areas.

---
*Run 212 finding: **stasis on founder-authority, plus one new green lever.** Zero founder action since Run 211 — psychic-bassoon #20/#19/#1 and jobscout #7 all re-verified OPEN/MERGEABLE/CLEAN at source; the unsigned Week-1 gate file is now **12.20 days cold** and byte-frozen since Aug 11. The one moving part is on the AGENT side: codex Run 222's job_opportunity_scanner **PR#8** (title-score word-boundary fix + first repo tests) is now source-verified real at GitHub, giving jobscout **two** independent green one-click PRs. forming-paws re-confirmed caught up (zero open PRs, `main` = `01537c3`). All source-verified at GitHub this run. **Net: still 0 agent-actionable open items account-wide** — reframed frontier is now **1 signature + 1 close (PR#1) + 4 green one-click merges (#19, #20, jobscout #7, jobscout #8)**, all founder-authority. Tooling note: full-file **Write** is the reliable path for PRIORITIES.md + state.md; `stat` on the gate file + `gh pr view --json state,mergeable,mergeStateStatus` are authoritative for this env.*
