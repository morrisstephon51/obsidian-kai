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
- [ ] Phase 6 — Deploy the real app + five build slices ([[Roadmap — Deploy and Five Slices]], locked 2026-08-09) — Slice A in progress

## Hosting — SETTLED 2026-08-11: one site, live

**The app is live at [theplugai.xyz](https://theplugai.xyz).** The 2026-07-22 "no hosted deploy" rule is dead, and so is the intermediate `app.theplugai.xyz` plan — Stefan's call was "everything on theplugai.xyz, no new links or sites," so there is **no subdomain and no static site**.

| What | Where |
|---|---|
| **The app** | **[theplugai.xyz](https://theplugai.xyz)** — Vercel project `forming-paws`, branch `main`, auto-deploys on push. Marketing page *and* sign-in on `/`, plus member home, browse, matches, chat, settings, admin. Migrations at **0021** live; **0022 written but not applied** |
| Fallback URL | [forming-paws.vercel.app](https://forming-paws.vercel.app) — the same deployment |
| Retired | GitHub Pages / the `gh-pages` branch. No longer served by anything |
| Carried over | `/admin.html` and `/app.html` still served from `public/` — still vanilla JS hitting Supabase directly. Known debt |

Legacy `/join.html`, `/login.html`, `/home.html`, `/confirm.html` all 307 to their app equivalents, so printed flyers and QR codes keep working.

## Routes

**Live now** (verified 2026-08-17): `/` · `/signup` · `/login` · `/dashboard` · `/browse` · `/matches` · `/matches/[id]` · `/dogs/new` · `/dogs/[id]` · `/account/password` · `/app` · `/faq` · `/contact` · `/privacy` · `/terms` · `/admin/review-queue` · `/admin/reports` · `/admin/messages`

**Built but not merged** — PRs [#44](https://github.com/morrisstephon51/forming-paws/pull/44) and [#45](https://github.com/morrisstephon51/forming-paws/pull/45); these 404 on production today:

| Route | What it is |
|---|---|
| `/home` | Member home — one "next action", your dogs, location. Replaces `/dashboard`, which then 307s here |
| `/settings` | Profile, location, email, notifications, sign out, delete account |
| `/account/reactivate` | Restore an account inside the 30-day deletion window |

`/settings` and `/account/reactivate` also need **migration 0022 applied**, or they render and then error on columns that do not exist yet. See [[Status Log]] 2026-08-17.

Domain: no purchase — `formingpaws.org` was available at $8.49/yr and declined. TLS is Let's Encrypt, issued 2026-08-11; Vercel did **not** auto-issue it, it needed `vercel certs issue`.

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
- [[_ops/important-links|Important Links]] — verified live status of every URL
- Spec: `~/forming-paws/docs/superpowers/specs/2026-07-04-forming-paws-foundation-design.md`
- Live: **https://theplugai.xyz** (github.io URLs redirect here) · code [github.com/morrisstephon51/forming-paws](https://github.com/morrisstephon51/forming-paws) (public) · DB Supabase `wyzcnkdonbdykidmcxvx`
- Cost analysis artifact (2026-07-23): [nonprofit vs for-profit, app store, mobile build](https://claude.ai/code/artifact/23064c5f-0ca6-447d-a92b-ecbbf9ac7d86) — re-verify dollar figures before quoting; platform commission rules are still in litigation
