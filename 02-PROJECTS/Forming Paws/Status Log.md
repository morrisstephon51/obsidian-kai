---
type: log
project: Forming Paws
tags:
  - forming-paws
  - status
---

# Forming Paws — Status Log

Newest first.  Each entry links the artifact it describes.

## 2026-08-16 — Full UX button audit of production + fixes shipped
Every interactive element walked with a real browser against live theplugai.xyz, two test members, full loop: signup → login → add dog → browse → interest → mutual match → chat both directions. Test data created and fully cleaned up after (sibling session's e2e fixtures untouched).

**Worked perfectly:** all landing/footer links, legacy flyer redirects, login, signup, add-dog (115 breeds incl. pit bulls confirmed in the live dropdown), browse filters + location prompt, verification gating on interest (mission-correct), match creation, chat delivery both ways, unread badge.

**Found & FIXED (deployed, re-verified live):**
1. No way to sign out anywhere → new POST /auth/signout + Sign out button in dashboard nav
2. Sent chat messages invisible to the sender for up to 5s ("No messages yet" after sending → double-send risk) → immediate poll after send, dedupe design preserved
3. "Needs verified health documents" notice was a dead end → now links to dashboard upload, mentions free Founding Member verification
4. "Password" nav label → "Account"
5. Intuitive action hierarchy via brand tokens: Add-a-dog CTA in brand green, unread badge accent, own chat bubbles brand

All shipped with tsc clean / eslint clean / 86 unit tests / build clean; Vercel deploy verified; each fix re-tested on production with the browser.

## 2026-08-15 (later) — Course correction: brand landed on the REAL app (Vercel main)
- Mid-work discovery: theplugai.xyz has served the **Next.js app from Vercel since 08-11** — the gh-pages pipeline this session had been deploying to is retired. Today's earlier gh-pages deploys were dead-ends
- **Breeds were never at risk**: the app reads breeds from the database at runtime, so all 112 (incl. pit bull types) were live in the real app the moment the DB insert ran
- **Brand foundation shipped to main** (verified: tsc clean, next build clean, 86/86 tests, Vercel deploy READY, aliased to theplugai.xyz): logo.svg favicon + asset, Tailwind brand/accent/ivory/ink tokens + display/body font families (additive), Fraunces headings + Nunito body site-wide, public/ legacy copies (admin.html, styles.css) synced to the redesigned versions — admin gains the review queue there
- **Remaining design work**: the app's React components still use stock Tailwind grays — applying the brand tokens page-by-page (landing hero, dashboard, browse cards) is the next pass and MUST be coordinated with the session actively developing main (PRs #31–#41, some open)
- ⚠️ Process lesson recorded: this session must stop deploying to gh-pages; main + Vercel is the only pipeline

## 2026-08-15 — Brand system shipped + breed catalog tripled
- **Forming Paws now has a real brand**: vector logo (pine-green paw, terracotta heart pad — favicon + nav sitewide), formalized palette (pine #2F6B5C primary / terracotta #E8734A accent / warm ivory), Fraunces display + Nunito body type. Fixed the old two-brand clash (landing was orange, app pages green). Footer: "Built by The Plug AI"
- Design verified twice per Stefan's instruction: code-consistency scan (no stray hex colors) + real-browser screenshots at 1280px and 390px (no overflow, mobile clean). Deployed and confirmed via pipeline
- **Breeds: 52 → 112** — added American Pit Bull Terrier, AmStaff, Staffy, American Bully, Pit Bull Mix + ~50 more mixes/doodles/missing breeds (Pug, Cocker Spaniel, Shiba Inu…), synced across join/dashboard/admin
- Fixed the double-save bug that duplicated Torrence's dogs (guard added; existing duplicate rows left pending Stefan's OK to delete)
- Brand decisions (interview): own warm identity (not Plug AI dark/amber), logo designed in-house, full-site rollout in one pass

## 2026-08-12 — 💬 Slice B live: owners can actually talk to each other
The core loop no longer dead-ends at a match. Shipped and deployed to https://theplugai.xyz.

- **Conversations** at `/matches/[id]` — server-rendered, polling every 5s from the client, gated on `document.visibilityState` so background tabs stop asking. Polling not Realtime: the `supabase_realtime` publication was empty, so Realtime would be net-new infrastructure *and* a second RLS surface, on a repo already bitten three times by RLS filtering. Schema is identical either way, so upgrading later needs no migration.
- **Unread badges** on the matches list and the dashboard — the dashboard matters because that's where members land, and unread is the only notification (no email, by decision).
- **Block** closes the thread for both. Blocker sees "You closed this conversation"; the other sees "This conversation is no longer available" — deliberately not naming who, so blocking doesn't invite an offline confrontation. Messages stay visible, because hiding them would destroy the evidence a report depends on.
- **Report + `/admin/reports` queue.** Admin access to message content is granted by RLS *only* while a report is open or reviewing, and ends when it closes.
- **Privacy policy + terms amended in the same PR** — the policy said nothing about messages and would have been inaccurate on day one.

**Migration 0020** — `messages`, `match_reads`, `match_blocks`, `match_reports`, plus `owner_in_match()` and `match_is_blocked()`. Verified live in rolled-back transactions: stranger 0 · participant 1 · admin-before-report 0 · admin-with-open-report 1 · **admin-after-resolved 0** · blocked insert rejected · sender spoofing rejected. The three admin numbers matter together — the middle alone wouldn't prove access *ends*.

**Design call worth remembering:** participants are identified by their **dog**, never by owner name. `owners` is RLS'd to your own row, so `display_name` for the other party comes back empty — the same trap as the dogs join. Rather than add an owner-name view, the thread reads "Luna ↔ Duke". Keeps a member's real name off a surface shared with someone they haven't met.

**Two of my own errors caught by running things rather than trusting them:** the plan's RLS steps used `set local request.jwt.claims = json_build_object(...)`, but `SET LOCAL` takes a literal not an expression — every verification step would have failed with a syntax error (fixed, PR #26). And the plan's admin probe invented an `owners` row with a synthetic uuid, which risks an FK failure that reads as a *policy pass* — rewritten to promote one of the 4 real dogless owners.

**⚠️ Then a verification pass found the moderation feature had NEVER worked** (PR #27, fixed + deployed). Two faults in already-shipped code, both found by exercising the admin route instead of re-reading it:
1. **Admin got a 404 before reaching a single message.** Migration 0020 let an admin read the *messages* of a reported conversation but left the *`matches` row* restricted to participants — and `/matches/[id]` loads the match first, then `notFound()`s. Verified: `admin_can_see_match_row = 0` while `admin_can_see_messages = 1`.
2. **Past that, `markRead()` threw** — its upsert requires `owner_in_match`, which an admin fails. The page would have 500'd.

So `report` — the whole reason block and report shipped together — had no working review path. **Lesson: an RLS policy that grants access to a table's *contents* is useless if the page's *first* query hits a different table with narrower RLS.** Migration 0021 adds `matches_select_admin_reported`, scoped identically to the messages policy so visibility begins at the report and ends when it closes. `markRead` is now non-throwing (bookkeeping must never break a page). Admins get a read-only view with an amber banner.

**Now genuinely verified end to end:** Playwright suite run, **5/5 passing** (2 new conversation tests + 3 pre-existing). The block test asserts the party who did *not* close it never sees who did. Fixture restored afterwards — 0 blocks left behind, 2 read markers written. Plus tsc 0, lint 0, 43 unit tests, build clean.

**Still open:** leaked-password toggle · `deploy-static-site.yml` still on main · `admin.html`/`app.html` still vanilla-JS copies in `public/`.

## 2026-08-11 — 🚀 THE REAL APP IS LIVE AT https://theplugai.xyz
The Next.js app now serves the apex domain. GitHub Pages is retired. **The five email-confirmed members who were stuck at "add a dog" can now reach health-doc upload, browse, and matching.**

- **One site, no subdomain** — Stefan's call: "everything on theplugai.xyz, no new links or sites." The `app.theplugai.xyz` plan was dropped. Marketing content ported into `app/page.tsx` with the sign-in panel on it; `admin.html`/`app.html`/`styles.css`/`app.js`/`fp-auth.js` copied into `public/` and served verbatim; `/index.html` `/join.html` `/login.html` `/home.html` `/confirm.html` are 307 redirects, so flyers and QR codes keep working
- **7 PRs merged** (#16 auth · #17 lint+CI · #18 docs · #19 migration 0019 · #20 dashboard badge · #21 landing sign-in · #22 single-site · #23 SEO/legal). main green throughout: tsc 0, lint 0, 36/36 tests
- **Slice C shipped early** — Open Graph + generated 1200×630 OG card (real 127KB PNG), robots.txt, sitemap.xml, and **privacy policy + terms**. Policy written against the real schema: names `location_point` honestly, states other members see distance only, and **does not claim 501(c)(3) status** because the entity doesn't exist yet. Terms separate document review from veterinary judgement. **Both need a lawyer's review before backing a grant application**
- **Cutover gotchas, for next time:**
  - Missing Vercel env vars made **every** route 500 including static files in `public/` — `middleware.ts` uses `process.env.…!` non-null assertions across a matcher covering all paths. Redirects still worked, because they're evaluated before middleware. That signature = missing env vars
  - Vercel **never auto-issued the TLS cert** for theplugai.xyz after DNS landed. Apex served HTTP 200 but HTTPS failed at the handshake. Fixed with `vercel certs issue theplugai.xyz www.theplugai.xyz` — 12 seconds
  - A `server: GitHub.com` reading on www was a **local DNS cache**, not real DNS. Always cross-check with `dig @8.8.8.8`
- **Supabase auth config updated**: Site URL `https://theplugai.xyz`, Redirect URLs `https://theplugai.xyz/**` + `http://localhost:3000/**` (the localhost entry keeps local dev signup working now that Site URL is production)
- **Live verification**: valid Let's Encrypt cert; `/` `/login` `/signup` `/privacy` `/terms` `/robots.txt` `/sitemap.xml` `/opengraph-image` `/admin.html` `/app.html` all 200; www 301→apex; all legacy `.html` paths forward correctly with query strings preserved; `/auth/confirm` returns a recoverable error + resend prompt on a dead link
- **Still open**: leaked-password toggle; `deploy-static-site.yml` workflow still on main (harmless, points at a dead host); `admin.html`/`app.html` are still the old vanilla-JS Supabase copies, now living in `public/` — drift relocated, not removed

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
| [#21](https://github.com/morrisstephon51/forming-paws/pull/21) | Landing sign-in — app front door rebuilt from an 8-line stub, `?email=` prefill (stacked on #16) | 7 new tests · 34/34 · tsc 0 · lint clean · build OK |

**Login field on the landing (requested 2026-08-09)** — split across both landings, because they have different constraints. The **app** landing (`app/page.tsx`) was an 8-line stub with no navigation at all; after deploy anyone hitting `app.theplugai.xyz` would have found a dead page. It now has a hero and a real inline sign-in panel (#21). The **marketing** landing gets an email field that *hands off* to the app rather than a working credential form — Slice A exists to remove copies of auth logic, and a vanilla-JS sign-in on a page we're already redirecting away would add a sixth. It also can't ship before the deploy, since it points at a host that doesn't resolve yet, so it's folded into Task 6.

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
