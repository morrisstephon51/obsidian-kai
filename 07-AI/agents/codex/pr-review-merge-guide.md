# PR Review & Merge-Order Guide — ACCOUNT-WIDE

*Author: Codex · Run 188 · 2026-08-15 (supersedes Run 179)*
*Purpose: the founder-review backlog is the ecosystem's #1 open bottleneck. This guide makes clearing it fast and safe. Every claim below was verified THIS run against live GitHub (`gh pr view --json mergeable,mergeStateStatus,statusCheckRollup` / `gh pr diff --name-only`), not assumed.*

---

## What changed vs the Run 179 guide (read this first)

The founder cleared a big chunk of the queue since Run 179 — this guide reflects the new reality:

1. **psychic-bassoon Phase 1 is DONE.** PRs **#13, #14, #15, #16, #17, #18 all MERGED 2026-08-14.** The old "Phase 1 — six small quality fixes" section is retired. Only **#1** (non-draft) and **#11** (draft) remain open in psychic-bassoon.
2. **forming-paws #32 MERGED**, along with #33/#34/#35/#36/#37 (a11y, browse-age, email templates, login canonical, date formatting). `main` is now **@407e7d3**.
3. **New forming-paws review backlog: PRs #38, #39, #40, #41** — the largest ready-to-merge queue account-wide. All four are **non-draft, MERGEABLE, CLEAN, and CI-green (SUCCESS)** as of 2026-08-15, and **mutually file-disjoint** (verified below) → merge in ANY order, zero stacking hazard.

---

## The mergeable queue right now (7 non-draft, MERGEABLE/CLEAN)

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
| #39 | validation | +110/-2, 3f | `app/api/upload/health-doc/route.ts`, `lib/dates.ts`, `tests/unit/dates.test.ts` | Future **health-document date** slips past a UTC-instant guard west of UTC → inflates the "Baseline health verified" badge + browse eligibility. Anchors "today" to America/Chicago. |
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

### One documented follow-up — the health-doc redirect twin (do NOT open as a separate PR yet)
`app/api/upload/health-doc/route.ts:61` on `main` still ends with the **same proxy-unsafe pattern** #41 fixes for the photo route:
```ts
return NextResponse.redirect(new URL(`/dogs/${dogId}`, request.url), 303)
```
It was left untouched on purpose: that file is **already edited by PR #39**, so a second branch touching it would risk an add/add-adjacent conflict. **Recommended:** once #41 (which introduces `lib/http.ts`) and #39 both merge, fold the one-line swap into the health-doc route (`return redirectToPath(request, \`/dogs/${dogId}\`)`) as a trivial follow-up. Flagged, not silently half-fixed.

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
| ai-video-reel-generator #24 | no | MERGEABLE/CLEAN | Clear error when Supabase env unconfigured (refs #5). Safe standalone; improves the founder-blocked #5 experience. |
| Link-inbio #5 | DRAFT | MERGEABLE/CLEAN | Obsidian ops-vault docs. |
| Link-inbio #6 | DRAFT | MERGEABLE/CLEAN | Binary resume PDF add (the `+0/-0` is git not line-counting a binary — NOT empty). |

---

## Frontier status (unchanged — 3 open issues, all non-actionable by an agent)
- **forming-paws #8** — IL-SOS incorporation filing (non-automatable founder steps).
- **ai-video-reel-generator #5** — Supabase project must be created by the founder (paid/founder-gated).
- **skills-introduction-to-git #1** — git learning exercise, not a code task.

There are **NO agent-actionable open issues account-wide.** With `main` unchanged since Run 187 and four clean forming-paws PRs already stacked, the highest-leverage move is **clearing this queue**, not opening a fifth PR (that would be inventory, not throughput). This guide is the throughput.
