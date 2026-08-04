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
- [x] Phase 2 — MVP live at **https://theplugai.xyz**: onboarding (join.html), waitlist, admin member dashboard (admin.html), daily member-report notifications. FIRST REAL MEMBER joined 2026-08-04 🎉 (full Next.js app sits on `main` awaiting hosting — Vercel blocked)
- [ ] Phase 3 — Business plan & nonprofit structure (decisions locked 2026-07-19: 501c3 path, verified-badge fee $29/dog as first revenue — see [[Execution Plan]])
- [ ] Phase 4 — Zero-capital funding strategy (via the Granted MCP tool — live grant data, no invented grants)
- [x] Phase 5 — Execution roadmap committed ([[Execution Plan]], repo PLAN.md) — Chicago launch, day-by-day first 30 days, go/no-go gates

## Risks
- Agent team currently short one working provider (Gemini blocked on Google Cloud billing/quota) and one not yet built (ChatGPT) — most subagent work still routes through Claude until resolved
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
