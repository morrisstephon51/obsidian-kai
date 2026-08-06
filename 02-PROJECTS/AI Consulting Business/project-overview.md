---
type: project
status: built-not-launched
started: 2026-07-17
tags:
  - project
  - track-3
  - for-profit
  - consulting
---

# Project — AI Implementation Consulting (for-profit)

← [[09-SYSTEM/Command Center|Command Center]] · [[02-PROJECTS/index|Projects]]

## Goal
A scalable, for-profit AI implementation consulting business generating recurring MRR. Stefan acts as the implementation layer between AI tools and small business owners who lack the capacity to deploy them.

**This is a third, separate track.** Distinct from [[02-PROJECTS/The Plug AI/project-overview|The Plug AI]] (nonprofit, faith communities) and BigHeart (day job). Don't conflate funding, branding, or docs across them.

## Positioning
The implementation gap *is* the product — small business owners don't need AI explained, they need someone to deploy it. Positioning leans on Stefan being a known local community member, not a polished tech outsider. That's a stronger trust signal with this audience than technical credentials.

## Two niches (confirmed 2026-07-17 — both, not either/or)
1. **Law firm intake automation** — south suburban Cook County, IL. Chosen over HVAC for simpler script logic, faster ROI demo, easier client persuasion.
2. **Apps and websites for local small businesses** — runs in parallel, not as a replacement.

## Automation boundary
Outreach is **semi-autonomous**. Low-stakes first-touch drafts can be agent-assisted. Pricing, meetings, replies, and phone calls always stay with Stefan.

## Where it lives
`~/ai-consulting-business/`

| Folder | Contents |
|---|---|
| `docs/` | 7 docs — business model, niche targeting, risk management, tech stack, onboarding checklist, 90-day roadmap, outreach automation plan |
| `outreach/` | Three-touch sequence + 2 proposal templates |
| `prospects/` | `law-firms-cook-county.md` (8 real firms, ranked — McDermott Law Group in Homewood is target #1) · `small-business-leads.md` (**empty**) |
| `dashboard/index.html` | Checkable roadmap/prospect tasks + live MRR tracker with localStorage persistence |
| `PERPLEXITY_SETUP.md` | Exact setup command, needs API key |

Also published as a Claude Artifact: [Field Ledger — AI Implementation Consulting](https://claude.ai/code/artifact/b02e34fa-1e71-442d-a450-5a445495a6c9)

## ⚠️ Not backed up
Verified 2026-08-06: the repo is git-initialized but has **zero commits and no GitHub remote**. Everything above exists only on this machine. Committing and pushing it is the cheapest risk reduction available on this project.

## Open blockers
- [ ] **Back it up** — commit and push to GitHub
- [ ] **Perplexity MCP not added** — needs API key: `claude mcp add perplexity --env PERPLEXITY_API_KEY=... -- npx -y @perplexity-ai/mcp-server`
- [ ] **Gmail MCP connector not authorized** — blocks any autonomous Touch-1 sending. Authorize via claude.ai connector settings
- [ ] **Law firm ranking unverified** — current Tier 1/2/3 is a first-pass web-search ranking by firm size/tenure, not checked against live Google review patterns
- [ ] **Niche 2 prospect list empty** — needs the same hyperlocal sourcing pass the law firms got
- [ ] **Attorney emails need sourcing** — likely by calling the receptionist

## Outreach mechanics
Three-touch sequence: no-pitch observation email → 60-second phone script → value-drop follow-up email. Optimal first-call time identified as **Wed 10:15am**.

## Notes
Before rebuilding anything here, check `~/ai-consulting-business/` for current state — verify files still exist and the blockers above are still accurate. See [[03-NOTES/two-track-rule|two-track rule]] for how this track gets prioritized against Plug AI.

---

*Created 2026-08-06 from session memory + live filesystem verification. The project itself dates to 2026-07-17.*
