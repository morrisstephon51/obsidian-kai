---
type: log
project: Forming Paws
tags:
  - forming-paws
  - status
---

# Forming Paws — Status Log

Newest first.  Each entry links the artifact it describes.

## 2026-09-03 — Sage gets a full body, the hero copy gets a correction, and a puppy-marketplace plan

`feat/sage-full-body` ([PR #64](https://github.com/morrisstephon51/forming-paws/pull/64), open, not merged), built in the isolated worktree `~/forming-paws-scrollcraft`.

**Sage's mascot now has a full-body illustrated register, not just the 72×72 flat mark.** Two poses generated (kie.ai/seedream, ~14 credits each against the real ledger — well under the skill's conservative 28-credit planning number), same risograph line-and-wash style as the worldflight's world-leg backgrounds, character locked via image-to-image reference. The homepage worldflight's small corner mark now fades out into the full-body Sage standing in the meadow at the peak. `docs/visual/SAGE-BRAND.md` documents the two coexisting registers (flat UI mark vs. full-body brand art), the hard rules (asymmetric ears always, accent color as a prop never the coat), and the reusable generation preamble.

**A real positioning bug, caught by Stefan, not by review.** The hero copy described Forming Paws as breeder-verification ("most breeding happens in the dark"). The actual product is geolocation matching between owners of healthy dogs, who message each other directly — health verification gates the match, it isn't the whole platform's framing. Rewrote all four hero beats around that. Also gave "Forming Paws" real visual weight: a proper icon+wordmark lockup at hero scale (was an 11px tracked label), and the sitewide header wordmark went 18px→24px with a bigger mark — the header change doesn't show on the homepage itself (WorldflightHero's fixed stage covers it there) but shows everywhere else.

**A git mistake worth remembering.** First push targeted `redesign/scrollcraft-homepage`, assuming PR #63 was still open — it had already been squash-merged into `main` earlier that day. Pushing to it recreated a same-named branch replaying 2000+ already-merged lines. Caught before opening a PR from it: rebuilt clean off current `origin/main`, cherry-picked the one real commit, opened #64 from that instead, deleted the stray branch both locally and on origin. **Lesson: a memory note saying a PR is "open" is a claim about the past — `gh pr view <n> --json state` before trusting it, every time**, the same discipline as verifying any other stale-memory claim.

**PAWS Chicago named as the real, current vet-referral, replacing an overclaim.** The homepage's Health section said dogs that fail verification are "referred to partner veterinarians" — `/vets` itself already discloses "we do not have partner veterinarians yet," so the homepage was contradicting a page one click away. Fixed by naming PAWS Chicago's Medical Center (verified live via web search — the org does run public-facing low-cost veterinary/spay-neuter services, not just care for its own shelter animals) as the concrete current referral, worded carefully as "not an exclusive partnership" rather than implying a signed agreement that doesn't exist. Homepage roadmap now has a real "PAWS Chicago referral" card under Now.

**Puppy marketplace: planned, not built.** Full spec at `docs/superpowers/specs/2026-09-03-puppy-marketplace-design.md`. Builds on a finding already on record here — the 2026-08-26 admin-console entry below: "Selling puppies is deferred, deliberately. No payment library is installed, live-animal sales are a restricted category for most processors, and Illinois PA 102-0227 constrains retail pet sales. Scoped to listings-with-inquiries first, no checkout." The new spec keeps that scope and works out the rest: data model (`litters` table + two nullable columns on `dogs`, reusing `dogs_browsable`/`dog_interests` rather than a parallel system), the flows, and legal flags that need an actual lawyer (PA 102-0227 applicability, payment-processor animal-sale restrictions, UBIT exposure for a nonprofit taking transaction fees). **Also surfaced a second overclaim while researching this**: the homepage's "Litter caps per profile" claim has zero implementing code — `grep -rn "litter"` across the whole repo returns two copy strings. The real number already exists in `project-overview.md` ("1 litter/dog/12mo") and `Execution Plan.md` ("litter caps enforced from day one") — decided in the original plan, never built. Not fixed this pass (out of the scope actually requested); flagged in the spec and here so it isn't lost again. Roadmap now also lists "Puppy marketplace" under Next, honestly, as a direction rather than a live feature.

Verification: 181/181 unit tests, `tsc` clean, `eslint` clean, Playwright screenshots of all four hero beats (desktop + mobile) and the updated Health/Roadmap/Vets sections.

## 2026-08-26 — Admin console: the AI Organization's first real dispatch, and three bugs that return empty sets

`feat/admin-console-role-system` is **9 commits / 18 files / +2,109 −44** ahead of `main`. Not merged. **Migrations 0026 and 0027 are written but NOT applied** — the Supabase MCP write tools are refused by the Claude Code permission classifier, so this needs a permission change from Stefan, not a code fix. Full write-up: [[Admin Console — Build Log]].

**"Build an admin panel" was already half-done.** `app/admin/` had three working sections — messages, review-queue, reports — each gated on `is_admin` at both page and server action. The real job was a role model and a shell, not a panel.

**Kairo produced a genuinely useful spec and three wrong table names.** First governed dispatch in 14 days (trace `20260826T003353762Z-kairo-uja`, architect/Sonnet, $0.259306 measured, $0 real on the Max subscription). The architecture reasoning was sound; the bindings referenced `review_queue_items` and a `conversations` table, **neither of which exists**. `builder`'s own system prompt explains why: *"You cannot read or write files."* **A Kairo spec is a draft to verify, not a spec to implement.** The `--timeout` override was load-bearing — `architecture` inherits the 30s default and the previous such dispatch (Aug 11) timed out there.

**Three defects, all with the same signature.** A permission bug does not throw, it returns an empty set:

1. 11 RLS policies gate on admin status. Freezing `owners.is_admin` without redefining `public.is_admin()` would have given a console-granted admin a **fully rendered, entirely empty console**. Fixed by pointing `is_admin()` at `has_role('admin')` — one swap, 9 policies migrated, no policy edits.
2. `user_roles_select_own` would have filtered `/admin/users`' nested embed to the admin's own row, rendering all 36 members as "no roles."
3. The fix for #2 declared a policy calling `is_admin()` before `is_admin()` was redefined — worked here by accident, broken on a fresh database.

**`gokai status` reports success it never measures.** Proven, not argued: with `HOME` pointed at an empty directory it prints byte-identical output and exits 0. Its numbers are also wrong, and how they are wrong found a second bug — every count is exactly **half** the file contents, because the Phase-3 monitors re-scan the whole ledger each run and re-append with no idempotency key (13 rows Aug 11, the same 13 again Aug 23). **Anything reading these ledgers must count `distinct task_id`, not lines.**

**⚠️ `spatial_ref_sys` is writable by anon and cannot be fixed from our role.** Confirmed live — a read with the anon key returns rows, and the ACL grants anon `arwd` on all 8,500 projection rows that `browse_dogs` distance search depends on. The table is owned by `supabase_admin` via the `postgis` extension, so **neither `ALTER TABLE … ENABLE RLS` nor `REVOKE` works as `postgres`** — Supabase's own suggested fix would error. Needs Supabase support. Measured counterpart: RLS *is* working everywhere it matters — anon reads return 0 rows from owners, dogs, messages, match_reports, contact_messages, health_documents and waitlist.

**Selling puppies is deferred, deliberately.** No payment library is installed, live-animal sales are a restricted category for most processors, and Illinois PA 102-0227 constrains retail pet sales. Scoped to listings-with-inquiries first, no checkout.

Verification: `tsc` clean · `eslint` clean · **200/200 unit tests** · `next build` green with all five `/admin/*` routes.


## 2026-08-21 — Visual refresh: five PRs, two audits, and a security assumption that expired

`feat/visual-refresh` is **16 commits / 85 files / +2,664 −274** ahead of `main` and has not been merged — Stefan reviews first. Preview runs locally; the Vercel branch previews are behind deployment protection and only load for a signed-in account.

**⚠️ A deferral in the 2026-08-18 entry below is now invalid.** That entry deferred the Next.js `sharp` CVEs on the reasoning that *"the app imports `next/image` nowhere, so Next's bundled sharp is never invoked on a request."* This refresh uses `next/image` in `HeroScene`, `BannerArt` and `guideArt`, and turns the optimizer **on** (`images.formats: ['image/avif','image/webp']`). Verified live: `/_next/image` returns `200 image/avif`, so sharp 0.35.3 runs per request. `npm audit` still reports **4 highs** — `next`, `sharp`, `postcss`, `nanoid` — and `sharp`'s are fresh libvips CVEs (33327/33328/35590/35591), not the ones fixed in #49. The Next.js set includes *DoS in the Image Optimization API using SVGs*, which is now a reachable path. **Not fixed here; needs a decision.**

**2026-08-22 — #59, the landing splash.** Stefan flagged that the mascot was nowhere on the landing page, which was true and which two audits had missed. `/` now opens on a full-viewport splash: Sage popping out from a Z-plane above the meadow, a glass card with the headline, and a scroll cue down to the rest. Also added the **"Log in" link the public nav never had** — without it a splash leaves returning members no way in. `feat/visual-refresh` is now 18 commits ahead of `main`.

### What shipped

| PR | | Cost |
|---|---|---|
| #51 | AI imagery on public pages | +24–31 KB/page |
| #52 | Design system adapted from three refero systems (see below) | +1.2 KB gzip CSS, 0 JS |
| #53 | Scroll motion — Framer Motion **removed**, not added | +1.03 kB route, 0 shared |
| #54 | Sage, a six-state mascot | ~0 except `/signup` +1.27 kB |
| #55 | AVIF (a brief requirement silently unmet) | −21% image bytes |
| #57 | WebGL hero — **reverses the brief's "no WebGL"**, Stefan's call | +137 KB after load event |
| #56, #58 | The two audit-fix passes | — |

### Against main

LCP **~320ms → ~56ms** · CLS **0.0035 → 0** · 0 dropped frames at 4× CPU · transfer +225 KB. `main`'s LCP swings 260–472ms because it fetches fonts from Google; self-hosting via `next/font` is most of the win.

### Two audits found 30 defects. Most were mine.

The worst two were both regressions I introduced and neither was visible without measuring:

1. **Content disappeared.** `Reveal` hid sections already on screen at hydration, and the observer's −12% rootMargin then excluded them — so a 1440×900 visitor watched "How Forming Paws works" vanish and not return until they scrolled. Measured 1.00 → 0.00, still 0.00 100 frames later.
2. **Auth redirects were downgraded.** Adding `loading.tsx` created Suspense boundaries on segments gated by a server-side `redirect()`, so logged-out `/browse` and `/matches` went from `307 → /login` to `200` + a client-side redirect. This broke the presentation-only claim the whole refresh rests on.

Two more worth remembering because the *method* caused them: a heading migration keyed on an exact regex missed 17 `<h2>`s that write `id=` before `className`, **and the grep meant to audit it had the same blind spot** — so the check agreed with the migration instead of testing it. The same mistake recurred with CTA class strings.

See [[Visual Refresh — Build Log]], [[../../04-RESOURCES/Design/Verification Playbook|Verification Playbook]] and [[../../04-RESOURCES/Design/Refero Styles — Design Reference|Refero Styles]].

## 2026-08-18 — Audit: CI red herring, an anon-readable moderation leak, and a near-miss regression

Stefan reported "all jobs failed". **Production was never broken** — all 8 routes correct, `main` CI green. The failure was PR #47 alone: a duplicate of #48 that changed `lib/nav.ts` without updating the two tests asserting the old value. Closed #47; #48 is the complete fix.

**The regression #47/#48 were fixing is mine.** Making the header global in #46 left the public nav on bare `#how`/`#health`, which resolve against the *current* path — so on `/about` they pointed at `/about#how`, a section that only exists on the homepage. Dead links on every non-home page. #48 also fixes `isActive`, whose `href.startsWith('#')` guard stops matching once hrefs become `/#how`.

**Worse finding — anon could enumerate who is under moderation review.** Migration 0022 revoked EXECUTE on `purge_deactivated_accounts()` but not the two helpers it calls, so PostgREST published them to `anon`. Verified live with only the public key: `owners_locked_by_open_report` and `owners_due_for_purge` both returned HTTP 200, while `purge_deactivated_accounts` correctly returned 401. They returned `[]` only because there were zero open reports at that moment — the first harassment report would have made both parties' owner ids anonymously readable. Fixed in **migration 0025** (renumbered from 0023, which was already taken), [PR #49](https://github.com/morrisstephon51/forming-paws/pull/49).

**4 high-severity libvips CVEs in `sharp`**, on the member-upload path — `lib/image.ts` runs sharp over uploaded bytes. Upgraded 0.33.5 → 0.35.3 and verified resize, EXIF-stripping and garbage-rejection all still work. Remaining `npm audit` highs are all inside `next@15.5.20`'s own tree; clearing them needs Next 16. **Deferred by decision** — the app imports `next/image` nowhere, so Next's bundled sharp is never invoked on a request.

**Near-miss caught in the PR backlog.** PR #40 restates `browse_dogs()` via CREATE OR REPLACE and, having been branched before 0022, omitted `and o.deactivated_at is null`. Merging it would have silently un-hidden every deleted member's dogs in browse — migration succeeds, tests pass, no error anywhere. Filter restored on that branch.

**Migration numbering is colliding.** `main` already carries two `0022_*` files. Mine was renumbered to 0025 to avoid a third collision at 0023. Worth a convention before it bites.

Backlog re-verified — all five bugs still real on current main, all now CLEAN: #38 dog birth date (UTC-midnight), #39 health-doc date (same class), #40 browse max-age off-by-a-year, #41 upload redirect uses `request.url` (internal Vercel host behind the proxy), #43 robots doesn't disallow `/settings`.

**Open and green: #38 #39 #40 #41 #43 #48 #49.** Migration 0025 to be applied after #49 merges.

## 2026-08-17 — Site-wide navigation, rotating member tab bar, four new pages
Stefan: "more pages… a navigation bar at the top… buttons along the bottom on a rotating carousel… every page should have a home button." [PR #46](https://github.com/morrisstephon51/forming-paws/pull/46) — **open, needs merge**.

**The finding that shaped it: 15 of 21 pages rendered no header at all.** `/dogs/[id]`, `/matches/[id]`, `/dogs/new`, `/login`, `/signup`, `/faq`, `/contact`, `/privacy`, `/terms`, `/thank-you` and every admin page were dead ends — back button only. A home button on *every* page is only true if a page cannot forget one, so `SiteHeader` + tab bar moved into `app/layout.tsx`. Trade: every route is now dynamic. It also collapsed three separate per-page unread RPCs into one.

**The two requirements conflicted.** A rotating home button rotates away. Resolved by pinning Home on the left and rotating `CAROUSEL_LINKS` beside it, with a test asserting Home survives rotation. Auto-rotate was explicitly chosen by Stefan over my recommendation, so it ships — with the mitigations that keep a moving tap target usable: stops permanently on first interaction, pauses on hover/focus/hidden-tab, honours `prefers-reduced-motion`, arrows + a dot per destination, `aria-live` off.

**`/` now redirects signed-in members to `/home`**, which made every `signedIn` branch below unreachable — deleted rather than left as dead code. The redirect sits after `getUser()` deliberately: implicit-flow auth links carry the session in the URL *fragment*, so those requests look signed-out server-side and need `HashSessionRecovery` to run.

**Four new pages, notable for what they refuse to claim** — this project has a documented history of stripped fabrications, so:
- `/about` — states plainly Forming Paws is **not an IRS-approved 501(c)(3)**
- `/vets` — **no directory**, because there are no partner vets; said above the fold
- `/donate` — **no donate button**. Soliciting donations while implying tax-deductible status you don't hold is a legal problem
- `/education` + 3 prerendered guides — process/safety only, each flagged **not veterinary advice** since no vet reviewed them

**This caught a live false claim:** the landing page's roadmap card promised "expert-reviewed guides on responsible breeding." Aspirational when nothing existed; checkable and false the moment `/education` shipped. Reworded.

Verified: tsc clean · **149 unit tests** (30 new) · eslint clean · build clean with guides prerendered · all 14 public routes 200 locally · all 15 previously header-less pages confirmed serving logo + nav · sitemap at 15 URLs.

## 2026-08-17 — Brand *system*, member home at /home, and account settings
Requested directly by Stefan: "we need to create a landing/home page for forming paws as well as a settings page." Spec at `docs/superpowers/specs/2026-08-17-brand-home-settings-design.md`, decomposed into three increments so the only DB-touching work lands last.

**Why a brand system when the brand was "applied" the day before:** `bf2b233` swapped `bg-gray-900` → `bg-brand` in 22 files. It left **111 other gray classes**, no shared header, `logo.svg` unused outside the favicon, and `body` never picking up Fraunces/Nunito at all. There was nothing to *swap to*. Increment 1 supplies it.

- **[PR #44](https://github.com/morrisstephon51/forming-paws/pull/44)** — `.fp-btn` / `.fp-card` / `.fp-band` / `.fp-link` / `.fp-badge` in `@layer components`; `components/Logo.tsx` (paw mark inline); `components/SiteHeader.tsx` in public + member variants; `lib/nav.ts` as testable data; landing, footer and sticky bar rebranded. Rebranding a page is now a class swap, not a redesign.
- **[PR #45](https://github.com/morrisstephon51/forming-paws/pull/45)** — `/home` replaces `/dashboard` (307 redirect, `/home.html` repointed); `lib/home/nextAction.ts` picks one next action as a pure function; **111 gray classes across 24 files → zero**; `/settings` with profile, location, email, notifications, danger zone; `/account/reactivate`.

**Deletion is deactivate-then-purge, and that's the whole point.** `messages.sender_owner_id` is `on delete cascade` (0020), so a hard delete erases the messages that are the *evidence in an open harassment report*. Someone reported for bad behaviour could delete their account and wipe the record. Migration 0022's purge skips anyone whose dog is in a match named by an open/reviewing report — **both parties**, since a purging reporter leaves the admin reviewing a one-sided thread.

**Three findings worth keeping:**
1. `deactivated_at` **cannot** be protected by an RLS policy. `USING` sees the old row, `WITH CHECK` the new one, and neither can reference the other — "this column is unchanged" is not expressible. Column-level `GRANT` instead. My own spec said RLS; it was wrong.
2. `dogs_browsable` deliberately does **not** filter deactivated owners. It also resolves dog *names* for `/matches`, `/matches/[id]` and the admin queue — filtering it would blank those names in every existing conversation. Fifth instance of this repo's recurring bug family.
3. `/dogs/[id]` first got a plain `select deactivated_at from owners where id = <other owner>` — which under `owners_select_own` returns nothing, so the check would have read null and concluded "active" for every dog on the site. Now `owner_is_active()`, security definer, boolean-only. Caught before commit.

**Also found: real schema drift.** `owners.email` exists in production with no migration, and the live `handle_new_user()` writes it while committed `0001` doesn't — replaying the repo into an empty DB produced a different schema than live. Reconciled in 0022, same as 0015 did for `waitlist`.

Notification toggles store real preferences and say plainly that nothing sends email yet.

Verified: tsc clean · 128 unit tests · eslint clean · `next build` clean · live routing confirmed (`/dashboard`→`/home` 307, `/home.html`→`/home` 307, `/home`→`/login` 307 signed out, `/` 200) · compiled CSS confirms `.fp-btn` = `rgb(47 107 92)`.

✅ **All shipped the same day.** Migration 0022 applied by Stefan, then PR #44 (`8214bc9`) and PR #45 (`65b01d1`) merged. Production verified: `/` 200 · `/home` 307→`/login` · `/dashboard` 307→`/home` · `/settings` 307→`/login` · `/home.html` 307→`/home` · `/join.html` 307→`/signup` · `/admin.html` 200. Live CSS confirms `.fp-btn` = `rgb(47 107 92)`; **zero gray classes remain on the landing page**; all six section anchors intact.

All seven assertions from `supabase/tests/0022_deactivation_assertions.sql` were run against production inside rolled-back transactions and **pass** — including the three-state browse check and the guard proving `dogs_browsable` keeps resolving names while deactivated. 12 owners / 16 dogs untouched, no fixtures left behind.

**Squash-merge gotcha, for next time:** #44 was squash-merged while #45 was stacked on it. `delete_branch_on_merge` is **false** on this repo, so GitHub did *not* retarget #45 — it silently kept pointing at `design/brand-home-settings`, and merging it would have merged into that dead branch instead of `main`. Fixed with `git rebase --onto origin/main design/brand-home-settings`, which replayed only the three Increment 2/3 commits and dropped the six duplicated ones with zero conflicts. **If a PR is stacked, either merge the base with a merge commit, or expect to rebase and retarget the child.**

## 2026-08-17 — Weekly promo reel + email Routine established
- New automated Routine: every **Monday 9am Chicago**, Claude drafts a reel-style promotional script (hook/beats/CTA, on-screen text + voiceover separated), a 5-8 shot shot-list, and the email copy that carries it to existing subscribers (members + waitlist) — retention/re-engagement framing, not cold-lead acquisition
- Output saved to `02-PROJECTS/Forming Paws/Content/promo-reel-YYYY-MM-DD.md` each week, committed to the vault
- **Safety rail: creates a Gmail DRAFT only, never auto-sends** — sending to real subscribers is Stefan's call every week
- Video production intentionally deferred — script + shot list first, actual reel generation layered in once the format is proven
- Push notification fires each Monday with the week's hook line when the draft is ready

## 2026-08-17 — Brand applied app-wide + design handoff complete
- **All 26 primary actions across the live app** (landing CTAs, log in/sign up, add-a-dog, browse filters, chat send, contact, waitlist, admin) moved from stock gray to brand green; unread badges terracotta; semantic colors untouched. Commit bf2b233, pure class swaps, zero behavior changes
- Quality gate on every step: tsc clean · 86/86 unit tests · next build clean · verified on production after deploy (6 brand-green actions on landing, Fraunces headings, /logo.svg favicon)
- **[[Design Handoff — Brand System]] written and indexed** for the main-branch session: token table, five usage rules, current state, three suggested next increments (browse-card hover language, ivory marketing grounds, paw-mark empty states)
- The platform is now visually one product from flyer QR → landing → dashboard → chat

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
