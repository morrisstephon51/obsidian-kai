# PR Review & Merge-Order Guide — ACCOUNT-WIDE

*Author: Codex · Run 198 · 2026-08-17 (supersedes Run 196)*
*Purpose: the founder-review backlog is the ecosystem's #1 open bottleneck. This guide makes clearing it fast and safe.*
*Provenance note (Run 198): a **GitHub API outage (HTTP 503 across all endpoints)** blocked live re-polling this run. Rather than leave the guide asserting a superseded `main` (`bf2b233`), it was **reconciled from the Run 197 handoff** — whose facts WERE live-verified last run (`gh`/GraphQL mergeable poll, rebase, `tsc`/`eslint`/`vitest`/`build`). Re-poll PR mergeable/CI state once GitHub recovers before merging.*

---

## What changed since the Run 196 guide (read this first)

**`main` MOVED AGAIN: `bf2b233` → `65b01d1`** — the founder **merged PR #45** ("Member home, full brand sweep, and account settings (Increments 2+3)", ~54 files incl. NEW `app/home`, `app/settings`, `app/account/reactivate`, `app/robots.ts`) into `main`. Still not clearing the stacked queue — a large founder-authored feature landed alongside it. The queue was re-verified against the new `main` (Run 197):

1. **All FIVE forming-paws PRs (#38, #39, #40, #41, #43) re-verified OPEN + MERGEABLE against `65b01d1`** — no textual conflict decay from #45.
2. **#45-vs-queue file overlap:** #39/#40/#41 are **fully file-disjoint** from #45. **TWO overlaps:** **#38** (#45 brand-swept `app/dogs/new/NewDogForm.tsx` again) and **#43** (both touch `app/robots.ts`). Git reports CLEAN, but treat these two as the semantic-review points.
3. **#43 grew a real behavior fix (was docs-only).** #45 added `/home` to the `robots.ts` disallow list but **MISSED its functional twin `/settings`** — `app/settings/page.tsx` does `redirect('/login')` when signed out + `metadata index:false`, the identical member-only pattern to `/home`, `/dashboard`, `/account/` which ARE disallowed. Left out, crawlers waste budget on it and can leak stray `/login` URLs into the index. **A defect #45 itself introduced.** Fix (conflict-safe throughput) was **folded INTO already-open PR #43** rather than opening a colliding sixth PR: #43 rebased onto `65b01d1` (`fix/robots-account-comment`, commit `e2f7ff6`), added `/settings` to the member-only disallow group, and refined the `/account/` comment to cover both `/account/password` AND the new `#45-era /account/reactivate` page. Verified: `tsc --noEmit` 0, `eslint app/robots.ts` 0, `vitest` 128 passed, `build` now emits `Disallow: /settings` in `/robots.txt`.
4. **#39 still carries TWO fixes and auto-closes ISSUE #42 on merge** (registered `closingIssuesReferences` on #39). No manual issue cleanup.
5. **Open ISSUES unchanged:** only forming-paws #42 is agent-actionable and is fixed-on-merge by #39; the rest are founder-gated (forming-paws #8 IL filing, ai-video-reel #5 Supabase, skills-introduction-to-git #1 exercise).

---

## The mergeable queue right now (6 non-draft + 4 draft, all MERGEABLE/CLEAN)

| Repo | PR | State | CI |
|------|----|-------|----|
| forming-paws | #38 | MERGEABLE/CLEAN | ✅ green |
| forming-paws | #39 | MERGEABLE/CLEAN | ✅ green |
| forming-paws | #40 | MERGEABLE/CLEAN | ✅ green |
| forming-paws | #41 | MERGEABLE/CLEAN | ✅ green |
| forming-paws | #43 | MERGEABLE/CLEAN | ✅ green |
| psychic-bassoon | #1 | MERGEABLE/CLEAN | (large feature PR — see Phase 2) |
| psychic-bassoon | #11 | **DRAFT** | un-draft before merging |
| command-center-redirect | #1 | **DRAFT** | gated — see cross-repo constraint |
| Link-inbio | #5 | **DRAFT** | MERGEABLE/CLEAN |
| Link-inbio | #6 | **DRAFT** | MERGEABLE/CLEAN |

Drafts cannot merge until un-drafted: **psychic-bassoon #11**, **command-center-redirect #1**, **Link-inbio #5**, **Link-inbio #6**.

---

## forming-paws — the current backlog (Track 2, Steph's Forming Paws)

**All five are correctness / docs fixes on core member flows or their metadata. Verified mutually file-disjoint — merge in ANY order, no rebase needed.**

| PR | Type | Size | Files | What it fixes |
|----|------|------|-------|---------------|
| #38 | validation | +100/-1, 3f | `app/dogs/new/NewDogForm.tsx`, `lib/dogBirthDate.ts`, `tests/unit/dogBirthDate.test.ts` | Future **birth date** slips past the guard west of UTC (evening Chicago) → could save a dog with a negative age. Fix compares calendar components in the member's local frame. |
| #39 | validation + proxy-safety | +201/-3, 4f (2 commits) | `app/api/upload/health-doc/route.ts`, `lib/dates.ts`, `tests/unit/dates.test.ts`, `tests/unit/health-doc-upload-route.test.ts` | **Two fixes on the same route.** (1) Future **health-document date** slips past a UTC-instant guard west of UTC → inflates the "Baseline health verified" badge + browse eligibility; anchors "today" to America/Chicago. (2) The **post-upload 303 redirect** built from `request.url` leaked the internal Vercel host (twin of #41's photo-route bug), now routed through `getRequestOrigin`. **Closes #42 on merge** (registered closing ref). 98 tests pass. |
| #40 | data (migration) | +97/-0, 1f | `supabase/migrations/0024_browse_dogs_max_age_calendar_band.sql` | Browse **max-age filter is off by a full year** vs the age label on each card (a 3y6mo dog labelled "3yo" is hidden by a "max age 3" search). New migration mirrors the calendar-correct min-age predicate. **Founder must APPLY the migration** (PR body has a read-only SQL-editor snippet to confirm live). |
| #41 | proxy-safety | +66/-1, 3f | `app/api/upload/photo/route.ts`, `lib/http.ts`, `tests/unit/http.test.ts` | After a **successful photo upload**, the 303 redirect built from `request.url` points at the internal Vercel deploy host, not the address-bar custom domain — on a protected preview that's a login wall, so a success looks like a failure. New `lib/http.ts` `redirectToPath()` builds the redirect from `getRequestOrigin(request)` (the repo's own tested helper). |
| #43 | docs + **behavior fix** | 1f | `app/robots.ts` | **Two things.** (1) **Behavior:** #45 added `/home` to the disallow list but MISSED its member-only twin `/settings` (`redirect('/login')` + `index:false`); #43 adds `Disallow: /settings` so crawlers stop wasting budget on it and can't leak `/login` into the index — **`/robots.txt` now emits `Disallow: /settings` (proven at build).** (2) **Docs:** the `/account/` comment (previously described *confirmation* pages — the opposite of what the line does, a maintainer trap) rewritten to cover both `/account/password` AND the `#45-era /account/reactivate` page. Rebased onto `65b01d1` (`e2f7ff6`); `vitest` 128 pass. |

### File-overlap matrix (verified this run)
```
#38  NewDogForm.tsx            lib/dogBirthDate.ts   tests/.../dogBirthDate.test.ts
#39  api/upload/health-doc     lib/dates.ts          tests/.../dates.test.ts   tests/.../health-doc-upload-route.test.ts
#40  migrations/0024_...sql
#41  api/upload/photo          lib/http.ts           tests/.../http.test.ts
#43  app/robots.ts
```
No file appears in two PRs — the five remain mutually conflict-free, merge in ANY order. (#43 was rebased onto current `main` `65b01d1` in Run 197; #38's base is older but still reported MERGEABLE against current `main`. The two files #45 also touched — `NewDogForm.tsx` (#38) and `app/robots.ts` (#43) — are git-CLEAN but are the human semantic-review points.)

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

There are **NO agent-actionable open issues account-wide** — #42's fix is already in #39 and auto-closes on merge; the other three are founder / manual / exercise items. `main` moved again in Run 197 (`bf2b233` → `65b01d1`, the founder-merged PR #45 member-home/settings feature), but the five forming-paws PRs were re-verified OPEN + MERGEABLE against it; #43 was rebased onto `65b01d1` and gained the `/settings` crawl-hygiene fix for a defect #45 introduced. The two files #45 also touched (`NewDogForm.tsx` → #38, `app/robots.ts` → #43) are git-CLEAN but are the semantic-review points. The highest-leverage move is still **founder review of #38-#41 and #43**, not opening a sixth PR (that would be inventory, not throughput). A Run 195 fresh source review across the subsystems the PRs do NOT touch (contact-message flow + RLS `0023`, waitlist `0015`, `lib/actions/location` + validator, `useShareLocation`, `/admin/messages` handling, `lib/promise`) found them **well-hardened — no new defect worth a sixth PR**. This guide is the throughput.

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
