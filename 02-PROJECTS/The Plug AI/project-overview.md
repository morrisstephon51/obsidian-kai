---
type: project
status: active
started: 2026-01-01
tags:
  - project
  - track-1
  - nonprofit
  - plug-ai
---

# Project — The Plug AI

← [[09-SYSTEM/Command Center|Command Center]] · [[02-PROJECTS/index|Projects]] · [[02-PROJECTS/The Plug AI Progress|Progress Log]]

**Track 1 — the critical path.** Anything that doesn't serve Plug AI funding or launch gets flagged as Track 2 before going deep.

## Mission
Close the AI literacy gap for people the tech world forgot — faith communities, community health workers, and first-gen students in south suburban Cook County, Chicago.

**Tagline:** "Get Connected. Get Skilled. Get into AI."

## Brand
- **Deep Space** `#0B0B1A` · **Amber Gold** `#F4B942` · **Electric Indigo** `#5B4FE8`
- **Voice:** short declarative sentences. No corporate language. No dashes/hyphens.
- **Recurring phrases:** "the gap," "people like me," "people the tech world forgot," "The plug is in."

⚠️ **The live site does not match this brand.** Current palette is light lavender/green. Stefan explicitly chose content and functionality first over styling — the mismatch is known and deferred, not an oversight. Flag it again when visual work starts.

## Website
| | |
|---|---|
| **Live** | [theplugai.info](https://theplugai.info) — verified 🟢 2026-08-06 |
| **Fallback** | [psychic-bassoon-psi.vercel.app](https://psychic-bassoon-psi.vercel.app) |
| **Repo** | [psychic-bassoon](https://github.com/morrisstephon51/psychic-bassoon) — Next.js 14 App Router, TypeScript, Tailwind, Framer Motion |
| **Deploy branch** | `claude/amazing-mccarthy-zZl3L` — **not `main`**. Local `main` is an unrelated single-commit project with no shared history |
| **Open PR** | Draft PR #1 tracks the deploy branch |

⚠️ Never share the `psychic-bassoon-cam6stef` URL — it hits a Vercel SSO wall.

⚠️ Stefan has pushed to the deploy branch from other sessions before (caused a merge conflict on 2026-07-13 when two sessions fixed the same bug independently). **Always `git fetch` first** — don't assume local matches remote.

### Content-hardening pass — done 2026-07-13
A 12-task pass removed all fabricated content: fake testimonials attributed to named people, fake stats, fake video view counts, fake workshop dates and past events. Built a reusable `NotifyModal` email-capture component wired into every dead-end CTA (workshop registration, community channels, footer/contact socials, resources video library) so nothing points at a dead link. Fixed 5 forms that previously claimed success regardless of the actual Formspree response.

**What still needs Stefan's real-world input** — see `tasks/content-checklist.md` in the repo: Formspree account/IDs, real stats, real testimonials with consent, workshop dates and venues, social account URLs, founder photo.

Design spec: `docs/superpowers/specs/2026-07-11-content-hardening-design.md` · Plan: `docs/superpowers/plans/2026-07-11-content-hardening.md`

## Status
Brand ✅ · PRD ✅ · Entity-path analysis ✅ (LLC vs 501c3 vs fiscal sponsorship) · Kresge Foundation LOI ✅ (Fluxx portal live, username `The_Plug_AI`)

## Funding pipeline
| Source | Status |
|---|---|
| Illinois Digital Equity Capacity Kickstarter Grant | ❌ Terminated |
| Open Collective Foundation | ❌ Shut down |
| Open Source Collective | ❌ Rejected |
| Illinois "Eliminate the Digital Divide" (up to $75K) | ⏳ Live option — needs a Community Technology Center partner |
| Kresge Foundation | ⏳ LOI submitted |
| Woods Fund | 📄 See `ThePlugAI WoodsFund AppPrep.pdf` in this folder |

**Blocker:** fiscal sponsor / 501(c)(3) partner. Kenneth Vasser's church is the live option — still need legal name, address, pastor confirmation, and a workshop date before applying.

See [[_ops/grant-research-log|Grant Research Log]] for the full funding tracker.

## ⚠️ Conflict of interest to manage
Stefan's church access (MOFEC, All Nations, Faith Mission, Holy City) was built through BigHeart relationships. Approaching those churches about Plug AI without disclosing BigHeart is professional exposure.

Two paths: **(1)** fold Plug AI into BigHeart as a formal internal initiative, or **(2)** build proof-of-concept with churches that have zero BigHeart overlap. Not yet decided.

## Content
The faith-community angle is the best-performing LinkedIn content by a wide margin — outperforms general AI content significantly. Drafts land in [[06-OUTPUTS/index|06-OUTPUTS]].

## Timing note
Per the [[09-SYSTEM/Command Center|OpenClaw AI Organization]] plan, formal **Track 1 execution is gated on Oct 13**, after governance Phases 2–4 complete. Work continues before then, but the full-court press has a date.

---

*Created 2026-08-06 to fill a link that had been broken in Command Center since 2026-07-05. Content assembled from session memory, the vault's context files, and live site verification.*
