# PR Review & Merge-Order Guide — ACCOUNT-WIDE

*Author: Codex · Run 193 · 2026-08-16 (supersedes Run 190)*
*Purpose: the founder-review backlog is the ecosystem's #1 open bottleneck. This guide makes clearing it fast and safe. Every claim below was verified THIS run against live GitHub (`gh pr view --json mergeable,mergeStateStatus`, `gh pr checks`, GraphQL `closingIssuesReferences`), not assumed.*

---

## What changed since the Run 190 guide (read this first)

**`main` is UNCHANGED at `3a005a6`** (the "Brand foundation" commit). Nothing merged since Run 190; the four forming-paws PRs are still stacked and unreviewed. What *did* change is the queue got cleaner and one open issue is now self-closing:

1. **All four PRs re-verified fully CI-GREEN today** — not just MERGEABLE/CLEAN. `gh pr checks` on each shows **both** the `verify` GitHub Action **and** the Vercel deployment passing (Supabase Preview "skipping" is expected — no branch DB). Merge-safe on the build, not just on conflict state.
2. **PR #39 now carries TWO fixes and auto-closes ISSUE #42 on merge.** The health-doc redirect twin that Run 190's guide listed as a *pending* fold-in was **already folded into #39** (Run 191, commit `986a2d7`), and Run 192 corrected #39's body to register the close. Verified this run via GraphQL: **#42 is a registered `closingIssuesReferences` on #39 → it auto-closes on merge, no manual cleanup.** The "redirect twin follow-up" section below is therefore **RESOLVED**, not outstanding.
3. **#39's real footprint is now 4 files / +201 / −3 / 2 commits / 98 tests** (was the "+110/−2, 3f" of the future-date-only version). Row updated below.
4. **The brand commit is still file-disjoint from every open PR** (`app/globals.css`, `app/layout.tsx`, `public/admin.html`, `public/logo.svg`, `public/styles.css`, `tailwind.config.ts` — none appear in #38-#41), so all four remain CLEAN against `main @3a005a6` with zero conflict decay.

---

## The mergeable queue right now (5 non-draft + 2 draft, all MERGEABLE/CLEAN)

| Repo | PR | State | CI |
|------|----|-------|----|
| forming-paws | #38 | MERGEABLE/CLEAN | ✅ green |
| forming-paws | #39 | MERGEABLE/CLEAN | ✅ green |
| forming-paws | #40 | MERGEABLE/CLEAN | ✅ green |
| forming-paws | #41 | MERGEABLE/CLEAN | ✅ green |
| psychic-bassoon | #1 | MERGEABLE/CLEAN | (large feature PR — see Phase 2) |
| command-center-redirect | #1 | **DRAFT** | gated — see cross-repo constraint |
| psychic-bassoon | #11 | **DRAFT** | un-draft before merging |

Drafts that cannot merge until un-drafted: **psychic-bassoon #11**, **command-center-redirect #1**, **Link-inbio #5**, **Link-inbio #6**.

---

## forming-paws — the current backlog (Track 2, Steph's Forming Paws)

**All four are calendar/proxy-correctness fixes on core member flows. Verified mutually file-disjoint — merge in ANY order, no rebase needed.**

| PR | Type | Size | Files | What it fixes |
|----|------|------|-------|---------------|
| #38 | validation | +100/-1, 3f | `app/dogs/new/NewDogForm.tsx`, `lib/dogBirthDate.ts`, `tests/unit/dogBirthDate.test.ts` | Future **birth date** slips past the guard west of UTC (evening Chicago) → could save a dog with a negative age. Fix compares calendar components in the member's local frame. |
| #39 | validation + proxy-safety | +201/-3, 4f (2 commits) | `app/api/upload/health-doc/route.ts`, `lib/dates.ts`, `tests/unit/dates.test.ts`, `tests/unit/health-doc-upload-route.test.ts` | **Two fixes on the same route.** (1) Future **health-document date** slips past a UTC-instant guard west of UTC → inflates the "Baseline health verified" badge + browse eligibility; anchors "today" to America/Chicago. (2) The **post-upload 303 redirect** built from `request.url` leaked the internal Vercel host (twin of #41's photo-route bug), now routed through `getRequestOrigin`. **Closes #42 on merge** (registered closing ref). 98 tests pass. |
| #40 | data (migration) | +97/-0, 1f | `supabase/migrations/0024_browse_dogs_max_age_calendar_band.sql` | Browse **max-age filter is off by a full year** vs the age label on each card (a 3y6mo dog labelled "3yo" is hidden by a "max age 3" search). New migration mirrors the calendar-correct min-age predicate. **Founder must APPLY the migration** (PR body has a read-only SQL-editor snippet to confirm live). |
| #41 | proxy-safety | +66/-1, 3f | `app/api/upload/photo/route.ts`, `lib/http.ts`, `tests/unit/http.test.ts` | After a **successful photo upload**, the 303 redirect built from `request.url` points at the internal Vercel deploy host, not the address-bar custom domain — on a protected preview that's a login wall, so a success looks like a failure. New `lib/http.ts` `redirectToPath()` builds the redirect from `getRequestOrigin(request)` (the repo's own tested helper). |

### File-overlap matrix (verified this run)
```
#38  NewDogForm.tsx            lib/dogBirthDate.ts   tests/.../dogBirthDate.test.ts
#39  api/upload/health-doc     lib/dates.ts          tests/.../dates.test.ts
#40  migrations/0024_...sql
#41  api/upload/photo          lib/http.ts           tests/.../http.test.ts
```
No file appears in two PRs. Zero add/add or edit/edit collisions. (#38's base is an older commit `550aaae` but still MERGEABLE/CLEAN against current `main`.)

### ~~Follow-up — health-doc redirect twin~~ — RESOLVED (folded into #39)
The health-doc route's proxy-unsafe `NextResponse.redirect(new URL(…, request.url), 303)` — the twin of #41's photo-route bug — was **folded directly into PR #39** (Run 191, commit `986a2d7`): the route now builds its redirect from `getRequestOrigin(request)`, and #39 adds 3 route-level tests (`tests/unit/health-doc-upload-route.test.ts`) asserting the 303 `Location` lands on the public forwarded host and never the internal deploy host. It uses the on-`main` `getRequestOrigin` helper, so it has **no dependency on #41** — #39 stands alone in any merge order. Tracking issue **#42 auto-closes on #39 merge** (verified closing ref). Nothing outstanding here.

---

## psychic-bassoon — remaining (The Plug AI, Track 1)

Phase 1 (#13–#18) is merged. Two PRs remain:

- **#1** — "Add real content, working forms, resource detail pages" (large, **non-draft**, MERGEABLE/CLEAN).
- **#11** — "Grant Matching Tracker" (**DRAFT — un-draft before merging**).

**The ONLY stacking hazard in this repo:** #1 and #11 both create `.env.example` as a brand-new file. Each merges cleanly vs `main` today (file absent); the instant one merges, the other flips to an **add/add conflict on that single file**. Resolution is trivial and lossless:

> **Keep BOTH env blocks.** #1's keys (`NEXT_PUBLIC_FORMSPREE_CONTACT_ID`, `NEXT_PUBLIC_FORMSPREE_NEWSLETTER_ID`) and #11's keys (Supabase, `MUTATION_SECRET`, `GROQ_API_KEY`, `CRON_SECRET`, `SMTP_*`) are completely non-overlapping — just concatenate.

(Config-consistency note from Run 180 is already resolved inside the now-merged #15: `lib/site.ts` resolves `SITE_URL` from `NEXT_PUBLIC_APP_URL` → `NEXT_PUBLIC_SITE_URL` → Vercel default, so either env-var name works. No action needed.)

---

## CROSS-REPO ORDERING CONSTRAINT (spans two repos — easy to miss)

**command-center-redirect #1 depends on psychic-bassoon #11.** The dashboard links to a grants route that lives ONLY on the unmerged DRAFT #11, and (as of Run 179) pointed at an SSO-gated `-cam6stef` preview host that bounces public visitors to a Vercel login wall. **Before un-drafting command-center #1:** (a) un-draft + merge psychic-bassoon **#11** and confirm the public domain serves `/grants` with a `200`; (b) repoint the grant links from the gated preview to the canonical public domain. Both are drafts, so nothing merges accidentally.

---

## Other repos (no cross-dependencies)

| PR | Draft? | State | Note |
|----|--------|-------|------|
| Link-inbio #5 | DRAFT | MERGEABLE/CLEAN | Obsidian ops-vault docs. |
| Link-inbio #6 | DRAFT | MERGEABLE/CLEAN | Binary resume PDF add (the `+0/-0` is git not line-counting a binary — NOT empty). |

---

## Frontier status — 4 open issues account-wide, none needing a NEW agent PR
- **forming-paws #42** — health-doc redirect twin. **Fix already in PR #39; auto-closes on merge.** No action beyond merging #39.
- **forming-paws #8** — IL-SOS incorporation filing (non-automatable founder steps).
- **ai-video-reel-generator #5** — Supabase project must be created by the founder (paid/founder-gated).
- **skills-introduction-to-git #1** — git learning exercise, not a code task.

There are **NO agent-actionable open issues account-wide** — #42's fix is already in #39 and auto-closes on merge; the other three are founder / manual / exercise items. `main` has NOT moved since Run 190 (still `3a005a6`), so the four clean forming-paws PRs remain stacked. The highest-leverage move is still **founder review of #38-#41**, not opening a fifth PR (that would be inventory, not throughput). A Run 193 fresh full-source review of forming-paws found **no new high-severity defect** worth a fifth PR (one cosmetic note logged below). This guide is the throughput.

---

## Documented follow-up from the brand commit (founder decision — NOT agent-shipped)

The Run 190 brand commit loads Fraunces + Nunito via a **render-blocking remote `@import`** at the top of `app/globals.css`:
```css
@import url('https://fonts.googleapis.com/css2?family=Fraunces:...&family=Nunito:...&display=swap');
```
No `next/font` is used (`app/layout.tsx` has no font import). Two non-urgent considerations for the founder — **left un-touched on purpose because this is the founder's active brand work and a PR here would collide with it**:
- **Performance:** a remote CSS `@import` blocks first paint on a round-trip to Google. `next/font/google` self-hosts the files, removes the extra request, and eliminates layout shift.
- **Privacy:** loading Google Fonts from Google's CDN leaks visitor IPs to Google — relevant given the app's legal/consent posture. Self-hosting via `next/font` keeps fonts first-party.

Flagged for the founder to decide, not shipped.

---

## Documented follow-up from the Run 193 source review (cosmetic — NOT agent-shipped)

A fresh full read of the forming-paws source this run found the codebase well-hardened (auth-link handling, upload validation, calendar-date logic, browse RPC all sound). One cosmetic note: `app/robots.ts` disallows `/account/` under a comment reading *"Confirmation pages. Crawlable on purpose so the noindex tag on them is actually read; a disallow here would hide that tag instead."* — but `/account/` holds only the **member-only** `/account/password` page (redirects to `/login` when signed out; already sets `index: false`). The confirmation pages that comment describes (`/thank-you`, `/auth/confirm`) live elsewhere and are handled correctly. So the **behavior is fine** (a member-only page is right to disallow, matching `/dashboard`), but the **comment is misplaced** and reads as a self-contradiction. One-line comment fix; deliberately NOT shipped as a fifth PR to avoid adding a cosmetic item to the review pile — logged here, foldable into any future robots/SEO change.
