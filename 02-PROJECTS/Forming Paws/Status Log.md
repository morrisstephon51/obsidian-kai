---
type: log
project: Forming Paws
tags:
  - forming-paws
  - status
---

# Forming Paws — Status Log

Newest first.  Each entry links the artifact it describes.

## 2026-07-20 — Chicago locked, outreach kit delivered
- Launch market confirmed: **Chicago metro**
- Researched 5 vet clinic targets (Midwest Animal Hospital Orland Park is #1 — dedicated breeder reproduction services) + 7 breed clubs/owner groups
- Outreach kit with ready-to-send vet email + breed-group post: [repo](https://github.com/morrisstephon51/forming-paws/blob/main/marketing/chicago-outreach.md), mirrored at [[Chicago Outreach Kit]]
- Stefan's checklist this week: send 5 vet emails, join 3 FB groups, post after a week of participating

## 2026-07-19 — Plan committed, waitlist LIVE, first revenue decisions locked
- Decisions: 501(c)(3) path · **verified-badge fee ($29/dog) as first revenue** · <5h/wk founder time · starting from zero (no entity)
- **Waitlist live** on the site (email+city+breed → Supabase `waitlist` table, insert-only RLS, tested end-to-end). Founding Member offer: first 20 dogs verified free for life
- Execution plan committed: [PLAN.md](https://github.com/morrisstephon51/forming-paws/blob/main/PLAN.md), mirrored at [[Execution Plan]]
- Fixed deploy pipeline: site now auto-publishes from `main` via GitHub Actions

## 2026-07-11 — Public site LIVE
- **https://morrisstephon51.github.io/forming-paws/** — landing + interactive demo (profiles, filters, health badges, match flow, chat on seeded data)
- Repo `morrisstephon51/forming-paws` created by Stefan; site deployed via GitHub Pages
- Parallel session contributed XSS-hardening + chat fixes

## 2026-07-09 — Client demo shipped under deadline
- Vercel blocked (fair-use 402) and Supabase edge functions can't serve HTML (forced text/plain) — pivoted to claude.ai artifact, then standalone HTML file for direct sharing, then GitHub Pages as the permanent home
- Demo smoke-tested headless: filters, match→chat, modals all pass

## 2026-07-04 — Project kickoff
- Master build prompt written (aeos repo, PR #1); name locked: **Forming Paws**

## Live infrastructure
| Thing | Where |
|---|---|
| Public site + waitlist | https://morrisstephon51.github.io/forming-paws/ |
| Code | github.com/morrisstephon51/forming-paws (`main` auto-deploys) |
| Database | Supabase project `forming-paws` (wyzcnkdonbdykidmcxvx) — waitlist, owners, dogs, breeds, dog_photos, health_documents |
| Plan | PLAN.md in repo · [[Execution Plan]] |

## Coordination note
Two Claude sessions are building this (this one + the MUNDI-infra session that owns the DB schema). Schema ownership: the other session's `owners/dogs/health_documents` design is canonical; this session added only `waitlist`.
