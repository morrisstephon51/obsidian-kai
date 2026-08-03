---
type: log
project: Forming Paws
tags:
  - forming-paws
  - status
---

# Forming Paws — Status Log

Newest first.  Each entry links the artifact it describes.

## 2026-08-04 — DOMAIN LIVE: https://theplugai.xyz ✅
Full verification sweep after Stefan completed GoDaddy DNS + GitHub Pages setup:
- DNS: all four GitHub Pages A records + www CNAME → correct
- https://theplugai.xyz serves the site with a valid certificate; www redirects to apex
- Pages verified: landing (/), member onboarding (/join.html — signup form live), demo (/app.html), styles/app assets all 200
- QR continuity confirmed: old github.io URLs 301-redirect to theplugai.xyz — printed flyers keep working forever
- Waitlist API: signup POST → 201 (test row cleaned up after)
- Outreach kit links updated to the branded domain ([[Chicago Outreach Kit]])
- ⚠️ One remaining click for Stefan: Settings → Pages → tick **Enforce HTTPS** (http currently serves unredirected)
- Note: repo copies of PLAN.md / marketing kit were removed when main became the Next.js app — the vault mirrors ([[Execution Plan]], [[Chicago Outreach Kit]]) are now the canonical copies

## 2026-08-03 — Client launch package: onboarding LIVE, flyer chosen, invoice out, domain bought
- **Member onboarding is live**: https://morrisstephon51.github.io/forming-paws/join.html — real account + dog profile creation against the production database, email-confirmation flow tested end-to-end
- **Flyer final**: QR-code design #1 in Canva, edited by Stefan (larger fonts, spacing) — QR scans straight to the join page; no printed URL
- **Invoice FP-001** issued to client "Sky / Ivan": $138.99 operating (Claude Max $100/mo + Supabase Pro $25/mo + domain $13.99/yr), dev fee TBD, $125/mo ongoing
- **Domain purchased: theplugai.xyz** — DNS setup pending, see [[Domain Setup — theplugai.xyz]] (2 steps, Stefan's court). QR/github.io links auto-redirect once live, no reprint needed
- **Architecture note**: main branch now carries the full Next.js app (login/browse/matching/admin review queue) from the parallel session — unhosted until Vercel unblocks; the static site + onboarding lives on the gh-pages branch, deployed via a manual workflow on main (the Pages environment only allows main deploys). Both front-ends share one Supabase project
- **Incident**: Supabase free-tier project paused and restored mid-work (2026-08-03), briefly wiping the schema before full recovery — the reason Supabase Pro ($25/mo, no pausing + daily backups) is now on the client invoice

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
