---
type: project
status: active
started: 2026-07-04
target: 
tags:
  - project
  - track-2
  - nonprofit
---

# Project — Forming Paws

## Goal
A health-first, safety-first nonprofit platform facilitating documented, responsible dog breeding — launching in Chicago, IL, on $0 capital. Dogs only at MVP; data model built extensible so other species can be added later without a rework.

## Why This Matters
Track 2 (per the [[03-NOTES/two-track-rule|two-track rule]], everything besides The Plug AI). Uses the same agent infrastructure (MUNDI Router, 233-persona subagent pool) built for Track 1 as a live second test of that infrastructure, while pursuing a separate mission Stefan wants to build.

## Structure
501(c)(3) nonprofit, no separate for-profit arm, open to fiscal sponsorship to accept donations pre-IRS-approval. Revenue model (donations, listing boosts, vet-referral partnerships, sponsored education, membership tiers) phased during Phase 2/3 planning, not fixed yet.

## Trust & Safety (non-negotiable)
- Matching/chat unlocked only after baseline health docs (vet wellness exam ≤12mo + core vaccinations)
- Automated **plausibility-checking** at launch, not automated medical judgment — anything questionable routes to manual review
- Optional "Gold" badge (OFA hip/elbow + DNA panel) — premium-feature hook, not gated
- In-app chat locked until mutual match, neutral/public meeting-location prompts; ID verification deferred until the platform scales
- Anti-mill: 1 litter/dog/12mo, breeding age gates, education acknowledgment, community reporting, rescue/adoption cross-promoted

## Operating Constraint
Stefan has ~30 min/day for this. The agent system carries nearly all execution — his time goes to approvals and irreversible/paid decisions only.

## Milestones
- [x] Phase 0 — Discovery interview → Alignment Brief
- [x] Phase 1 — Agent team architecture mapped to real MUNDI personas
- [x] Spec written, self-reviewed, committed, and approved by Stefan (2026-07-05)
- [x] Phase 2 — MVP live at **https://theplugai.xyz**: onboarding (join.html), waitlist, admin member dashboard (admin.html), daily member-report notifications. FIRST REAL MEMBER joined 2026-08-04 🎉
- [ ] Phase 3 — Business plan & nonprofit structure (decisions locked 2026-07-19: 501c3 path, verified-badge fee $29/dog as first revenue — see [[Execution Plan]])
- [ ] Phase 4 — Zero-capital funding strategy (via the Granted MCP tool — live grant data, no invented grants)
- [x] Phase 5 — Execution roadmap committed ([[Execution Plan]], repo PLAN.md) — Chicago launch, day-by-day first 30 days, go/no-go gates

## Hosting — three things, easy to confuse (verified 2026-08-06)

| What | Where | Contains |
|---|---|---|
| **Public static site** | [theplugai.xyz](https://theplugai.xyz) — GitHub Pages, `gh-pages` branch | Landing, `/join.html`, `/admin.html`. **The shareable link** |
| Vercel project `forming-paws` | forming-paws.vercel.app | Serves the static landing only — `/browse` and `/join.html` both 404. Not the real app |
| **The Next.js app** | `~/forming-paws`, branch `main` — **local only** | Owner accounts, dog profiles, health-doc verification + admin review, geolocation `/browse`, mutual-match `/matches`. Migrations at 0018 |

The app being unhosted is a **decision, not a blocker** (2026-07-22): Stefan chose to keep iterating locally rather than carry deploy-platform overhead, after the project hit a Vercel billing cap once. Don't propose Vercel/Netlify deploys unless he reopens it. Task 11 in the foundation plan is SKIPPED for this reason — closed, not pending.

The repo **is** public on GitHub: [morrisstephon51/forming-paws](https://github.com/morrisstephon51/forming-paws).

## Risks
- Agent team lost its Gemini provider entirely — `gemini-agent` was **archived** to `~/clawd/agents/_archived/` after every call returned HTTP 429 with `limit: 0` (the Google Cloud project had zero free-tier quota; needed a billing decision, not a code fix). ChatGPT provider still not built. Subagent work routes through Claude
- 30 min/day constraint means scope creep is the biggest execution risk — stay disciplined about what Phase 2 actually needs for an MVP

## Resources to Gather
- OpenAI API key (for the ChatGPT provider agent, not yet built)
- Google Cloud billing decision for Gemini's quota
- Fiscal sponsor for pre-IRS-approval donations

## Related Vault Notes
- [[Status Log]] — dated progress log with live links (newest first)
- [[Execution Plan]] — the committed roadmap (mirror of repo PLAN.md)
- [[Chicago Outreach Kit]] — vet targets, breed groups, ready-to-send scripts
- [[09-SYSTEM/Command Center|Command Center]] — agent fleet status this project depends on
- [[07-AI/MUNDI System Reference|MUNDI System Reference]]
- Spec: `~/forming-paws/docs/superpowers/specs/2026-07-04-forming-paws-foundation-design.md` (repo not yet pushed to GitHub)
- Live: site https://morrisstephon51.github.io/forming-paws/ · code github.com/morrisstephon51/forming-paws · DB Supabase `forming-paws`
