---
type: log
project: Forming Paws
tags:
  - forming-paws
  - status
---

# Forming Paws — Status Log

Newest first.  Each entry links the artifact it describes.

## 2026-08-09 — Full audit + roadmap reset: the app gets deployed
Audited both codebases, the live site, and the database end to end. See [[Roadmap — Deploy and Five Slices]] for the full plan.

- **Core finding**: two divergent products, one database — and the real people are on the weaker one. The static site's member dashboard says *"we'll email you when your dog's health vault is ready"*, while health-doc upload, admin review, geo browse, and mutual matching **already work** in the Next.js app nobody can reach. **5 of 7 confirmed members are at a dead end**
- **Decision reversed**: the 2026-07-22 no-hosted-deploy call is closed. App deploys to **`app.theplugai.xyz`** (subdomain — no purchase; `formingpaws.org` was available at $8.49/yr and declined)
- **Sequence locked** — ship-first: **A** deploy & harden → **C** growth/legal → **B** in-app chat → **D** photo gallery → **E** vet referral/education. C before B because grant applications can't point at a site with no privacy policy
- **Health check**: `tsc` clean, `next build` clean (15 routes), 27/27 unit tests pass, migrations at 0018
- **DB census**: 7 owners · 5 dogs · 4 health docs · 2 interests · 1 match · 1 waitlist · 5/7 confirmed
- **12 errors logged** (full list in the roadmap note). Worst three: `npm run lint` fails outright (ESLint 9, no flat config — zero lint coverage); auth fixes stranded uncommitted on `fix/upload-redirect`; `dog_photos_select_browsable` is `USING (true)` so any signed-in user can enumerate every photo row
- **RLS re-audit passed** — owners, waitlist, health documents, and interests all correctly gated. July's hardening held
- ⚠️ **Needs a Supabase dashboard change during Slice A**: add `app.theplugai.xyz` to Authentication → URL Configuration → Redirect URLs, or new signups' confirmation links break

**Slice A progress — 5 PRs open, awaiting Stefan's merges:**

| PR | Task | Verified |
|---|---|---|
| [#16](https://github.com/morrisstephon51/forming-paws/pull/16) | Auth: cross-device email confirmation, `x-forwarded-host` origins, `next`-param hardening | tsc 0 · 27/27 · build clean |
| [#17](https://github.com/morrisstephon51/forming-paws/pull/17) | ESLint flat config + CI (stacked on #16) | tsc 0 · lint 0 · 27/27 |
| [#18](https://github.com/morrisstephon51/forming-paws/pull/18) | Slice A spec + implementation plan | — |
| [#19](https://github.com/morrisstephon51/forming-paws/pull/19) | Migration 0019 — couple photo visibility to browse. **Already applied live** | orphan-path test filtered 0; rollback clean |
| [#20](https://github.com/morrisstephon51/forming-paws/pull/20) | Dashboard verification badge | 2 new tests · 19/19 · tsc 0 · build OK |

**Three corrections to the 2026-08-09 audit, found by re-checking rather than trusting the first pass:**
1. **Audit finding #10 was overstated.** `dogs_browsable` is `dogs JOIN breeds` with *no* verification filter, so every dog is browsable and photos being readable by signed-in members matches how `/browse` already works. Not a live leak — 0 photo rows, 0 files exist. Migration 0019 still landed, reframed as coupling: the policies expressed no relationship to browsability, so they'd silently fail to follow any future filter.
2. **The Supabase advisor never flagged `dog_photos`** — that finding was derived by hand from `pg_policies`.
3. **The spec contradicted itself** on `home.html` (fix its badge *and* redirect it away). The app's `/dashboard` showed only name and sex, so the redirect would have downgraded the member experience — fix moved to the app (#20).

Also avoided a regression: the branch holding the stranded auth work was *behind* `main` and would have reverted the `303` on upload redirects from #14. Rebranched off `origin/main`.

**Remaining in Slice A:** deploy to Vercel (blocked on #16 merging — `getRequestOrigin` is required behind the proxy), then repoint the static site.

## 2026-08-07 — Member experience shipped: login, dashboard, confirmation landing
- **login.html** — member sign-in with working forgot-password reset flow
- **home.html** — member dashboard (their dogs + add-dog form, verification status, community stats, Founding Member badge); root URL auto-redirects signed-in members here; marketing page unchanged for visitors
- **confirm.html** — the email-link landing page: finishes pending dog profiles, handles password resets, forwards to dashboard (fixes the dead-end after confirming email)
- **⚠️ ONE SETTING NEEDED from Stefan to kill the 403 on email links** — Supabase dashboard → Authentication → URL Configuration: set Site URL to https://theplugai.xyz and add https://theplugai.xyz/confirm.html to Redirect URLs. Until then, confirmation/reset emails may land on a broken address.
- DB: community_stats() function added for dashboard tiles

## 2026-08-04 (later) — FIRST REAL MEMBER 🎉 + member ops built
- **Terrell Anderson (terrella031@icloud.com) joined via the live site** — first organic member; confirmed their email (the automatic confirmation email works in the wild). Their dog profile didn't complete (confirmed on a different device than they signed up on) — join page now handles that: resubmitting the form logs them in and finishes the profile
- **Admin dashboard live: https://theplugai.xyz/admin.html** — running member roster (name, email, location, dogs, joined date), waitlist list, stat tiles, CSV export. Sign-in required; only accounts with is_admin=true see data (RLS-enforced)
- **Daily member report Routine** — every day 9am Chicago, Claude checks for new members/dogs/waitlist, pushes a phone notification when there's news, stays quiet otherwise. Also auto-promotes the founder account to admin once it exists
- **DB changes**: owners.email column added (captured on signup, backfilled), is_admin() helper + admin read policies on owners/dogs/waitlist
- **Stefan's one task → to see the dashboard: sign up at https://theplugai.xyz/join.html with morrisstephon51@gmail.com** (any dog is fine), confirm the email. Admin access activates automatically within a day (or ask Claude to do it instantly)
- Data note: 4 e2e-fixture accounts from the parallel session's tests remain in the DB (excluded from reports); left in place since that session's test suite may rely on them

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
| Public site + onboarding | **https://theplugai.xyz** (github.io URLs redirect here) |
| Member signup | https://theplugai.xyz/join.html |
| Code | github.com/morrisstephon51/forming-paws (static site on `gh-pages`, Next.js app on `main`; deploy via "Deploy static site" workflow) |
| Database | Supabase project `forming-paws` (wyzcnkdonbdykidmcxvx) — waitlist, owners, dogs, breeds, dog_photos, health_documents |
| Plan | PLAN.md in repo · [[Execution Plan]] |

## Coordination note
Two Claude sessions are building this (this one + the MUNDI-infra session that owns the DB schema). Schema ownership: the other session's `owners/dogs/health_documents` design is canonical; this session added only `waitlist`.
