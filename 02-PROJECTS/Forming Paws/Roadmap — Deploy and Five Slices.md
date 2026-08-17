---
type: plan
project: Forming Paws
status: active
created: 2026-08-09
tags:
  - forming-paws
  - plan
  - roadmap
---

> Decided with Stefan 2026-08-09. Supersedes the "no hosted deploy" decision of 2026-07-22 for the Next.js app. See [[project-overview]], [[Status Log]], [[Execution Plan]].

# Forming Paws — Roadmap: Deploy & Five Slices

## The problem this fixes

Two divergent products run against one database, and the real people are stuck on the weaker one.

The live static site ([theplugai.xyz](https://theplugai.xyz)) lets someone sign up and add a dog, then tells them *"we'll email you when your dog's health vault is ready."* Health-doc upload, admin review, geo browse, and mutual matching **all exist and work** — in the Next.js app, which nobody can reach because it only runs on Stefan's laptop.

**5 of 7 registered members are email-confirmed and sitting at a dead end.**

## Decisions locked 2026-08-09

| Decision | Choice |
|---|---|
| Close the gap by | Deploying the Next.js app — the static site stops being the product |
| Domain | ~~`app.theplugai.xyz`~~ — **reversed 2026-08-10**. Everything serves from `theplugai.xyz` itself; Stefan's call was "no new links or sites". (`formingpaws.org` was available at $8.49/yr; declined) |
| Marketing site | ~~GitHub Pages~~ — **retired 2026-08-11**. The marketing page is now `app/page.tsx` in the Next app, sign-in panel included |
| Sequence | **Ship-first**: A → C → B → D → E |

## Verified state as of 2026-08-09

**Next.js app** (`~/forming-paws`): `tsc` clean · `next build` clean (15 routes) · 27/27 unit tests pass · migrations at 0018. Slice 1 feature-complete.

**Live site**: all 5 pages return 200. Vanilla JS hitting Supabase REST directly.

**Database** (`wyzcnkdonbdykidmcxvx`): 7 owners · 5 dogs · 4 health docs · 2 interests · 1 match · 1 waitlist signup · 5/7 users email-confirmed.

**Deploy readiness**: no `.vercel` link in the repo, no CI workflows on `main`, app needs exactly **two** env vars (`NEXT_PUBLIC_SUPABASE_URL`, `NEXT_PUBLIC_SUPABASE_ANON_KEY`). Deployment is genuinely small.

## The five slices

Each gets its own spec → plan → build cycle. Nothing is built ahead of its slice.

### Slice A — Ship & harden ✅ **DONE 2026-08-11**
Deployed to **`theplugai.xyz`** — the apex, not the subdomain. Error backlog cleared, ESLint restored, CI added.

### Slice C — Growth & legal ✅ **DONE 2026-08-11**
SEO, Open Graph, `robots.txt`, sitemap, privacy policy, terms. Merged in PR #23.

### Slice B — Real in-app chat ✅ **DONE 2026-08-11**
Messages table, match-scoped RLS, unread counts, block, report, admin moderation queue. PRs #24–28. Migration 0021 fixed a moderation path that 404'd silently.

### Slice D — Photo gallery & profile polish ⬜ next
Multiple photos, primary-photo selection, richer dog detail page.

### Slice E — Vet referral network + education hub ⬜
The "Next" and "Later" items on the public roadmap. **Last because it's gated on real vet partners existing**, not on code.

---

## Added 2026-08-17 — brand system, member home, settings

Not in the original five slices; requested directly by Stefan ("we need a landing/home page as well as a settings page"). Three increments, spec at `docs/superpowers/specs/2026-08-17-brand-home-settings-design.md`.

| # | Scope | State |
|---|---|---|
| 1 | `fp-*` component classes, `Logo`, shared `SiteHeader`, landing rebrand | PR #44 — open |
| 2 | Member home at `/home`, brand across all remaining pages | PR #45 — open |
| 3 | `/settings`, deactivate-then-purge deletion, `/account/reactivate` | PR #45 — open, **migration 0022 not yet applied** |

The brand work exists because `bf2b233` swapped `bg-gray-900` → `bg-brand` in 22 files but left 111 other gray classes, no shared header, and `logo.svg` unused outside the favicon. Increment 1 supplies the system that swap was reaching for.

## Error backlog found in the 2026-08-09 audit

Fixed in Slice A unless noted.

**Live site**
1. `home.html` hardcodes `Verification pending` on every dog — a verified dog would still read as pending
2. No Open Graph/Twitter tags, no `robots.txt`, no sitemap, no canonical — shared links render blank *(→ Slice C)*
3. No privacy policy or terms, while collecting names, emails, city, dog data — and pursuing grants *(→ Slice C)*
4. `index.html` redirects on any stored `fp_session` without checking expiry → stale-session flash bounce to login
5. Breed list, auth, and dog-insert logic duplicated across `join.html`, `home.html`, `admin.html`, and the Next app — four copies, already drifting
6. `app.html` is a fake seeded demo with canned chat — competes with the real app once it's live

**App / infra**
7. `npm run lint` **fails outright** — ESLint 9 with no `eslint.config.mjs`. Zero lint coverage
8. Uncommitted auth fixes stranded on `fix/upload-redirect` (4 modified + `app/auth/confirm/`, `lib/auth/`, `HashSessionRecovery.tsx`) — unpushed
9. No CI — nothing runs tsc/tests on PRs
10. `dog_photos_select_browsable` uses `USING (true)` for `authenticated` — any signed-in user can enumerate every photo row, including unverified dogs'
11. Supabase leaked-password protection disabled
12. `spatial_ref_sys` RLS disabled + PostGIS in `public` (PostGIS defaults, low risk, documented not fixed)

**RLS is otherwise solid** — owners, waitlist, health documents, and interests are all correctly gated. The July hardening held up under re-audit.

## Migration note

Existing members carry over automatically — the deployed app hits the same Supabase project, so their accounts and dogs are already there. What they gain is access to health-doc upload and matching.

**Requires a Supabase dashboard change**: `app.theplugai.xyz` must be added to Authentication → URL Configuration → Redirect URLs, or email confirmation links will break for new signups.
