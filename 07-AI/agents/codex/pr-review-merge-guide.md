# PR Review & Merge-Order Guide — ACCOUNT-WIDE

*Author: Codex · Run 179 · 2026-08-13 (supersedes Run 178)*
*Purpose: the founder-review backlog is the ecosystem's #1 open bottleneck (clawd Run 193, antigravity Run 168). This guide makes clearing it fast and safe. Every claim below was verified THIS run against live GitHub (`gh pr view` / `gh pr diff`) and live HTTP (`curl -I`), not assumed.*

---

## What changed vs the Run 178 guide (read this first)

Two corrections a founder clearing the queue would otherwise trip on:

1. **psychic-bassoon PR #11 (Grant Matching Tracker) is a DRAFT.** The Run 178 guide listed it as a Phase-2 mergeable PR. GitHub blocks merging a draft — it must be un-drafted first. Its `.env.example` add/add hazard vs #1 still applies once it's ready.
2. **command-center-redirect PR #1's grant links no longer 404 — they now hit a Vercel LOGIN WALL.** The PR was re-pointed from `psychic-bassoon-psi.vercel.app` (Run 167's target) to `psychic-bassoon-cam6stef.vercel.app`, which is an **SSO/Deployment-Protection-gated preview**. `curl -I` returns `302 → vercel.com/sso-api` for both `/` and `/grants`. So a public visitor clicking any grant link is bounced to a Vercel login page, and the route is *still* absent from the public production site anyway (see below). PR #1 is a DRAFT, so it's gated for now.

---

## Draft status matters — the real mergeable queue is 10, not 14

**4 of the 14 open PRs are DRAFTS and CANNOT be merged until un-drafted:**

| PR | Draft? | Note |
|----|--------|------|
| psychic-bassoon #11 | **DRAFT** | Grant Matching Tracker — adds `app/grants/page.tsx`, `app/api/grants/*`, grants migration, `.env.example` |
| command-center-redirect #1 | **DRAFT** | PIN-locked dashboard; grant links point at SSO-gated preview (see cross-repo section) |
| Link-inbio #5 | **DRAFT** | Obsidian ops vault docs (`+94/-0`, single file) |
| Link-inbio #6 | **DRAFT** | Binary add `Stephon-Morris-Resume.pdf` (the `+0/-0` is git not line-counting a binary — NOT an empty PR) |

The **10 ready-to-merge (non-draft, MERGEABLE/CLEAN)** PRs are: psychic-bassoon #1, #13, #14, #15, #16, #17, #18; forming-paws #32; ai-video-reel-generator #24. (#1 is large but non-draft.)

---

## psychic-bassoon — recommended merge order (The Plug AI, Track 1)

### Phase 1 — the six small quality fixes (any order, safe now, all non-draft)
File-disjoint from each other and from #1/#11. Verified no shared file. Merge freely:

| PR | Type | Files | Value |
|----|------|-------|-------|
| #13 | security | `lib/mailer.ts` | HTML-escape user fields in contact emails (injection sink) |
| #14 | hardening | `app/api/subscribe/route.ts` | Email validation + 254-char cap on last un-hardened write route |
| #15 | SEO | `lib/site.ts`, `app/layout.tsx`, `app/learn/[slug]/page.tsx`, `app/robots.ts`, `app/sitemap.ts` | Single-source canonical site URL |
| #16 | a11y | `components/shared/Navbar.tsx` | Mobile menu → accessible modal (WCAG 4.1.2) |
| #17 | SEO | `app/{about,community,contact,learn,workshops}/layout.tsx`, `app/resources/page.tsx` | Per-page titles/canonicals/OG cards (kills duplicate-title penalty) |
| #18 | a11y | `app/{community,contact,workshops}/page.tsx`, `components/shared/{EmailCapture,Footer}.tsx` | Announce form success/error to assistive tech (WCAG 4.1.3) |

*Verified near-misses that are NOT overlaps: #17 `app/resources/page.tsx` (index) vs #1 `app/resources/[slug]/page.tsx` (detail); #17 `app/*/layout.tsx` vs #18 `app/*/page.tsx`; #15 `app/learn/[slug]/page.tsx` vs #17 `app/learn/layout.tsx` — all different files.*

### Phase 2 — the two large feature PRs
- **#1** — "Add real content, working forms, resource detail pages" (`+7718/-61`, 34 files, **non-draft**)
- **#11** — "Grant Matching Tracker" (`+869/-0`, 10 files, **DRAFT — un-draft before merging**)

**The ONLY stacking hazard account-wide:** #1 and #11 both create `.env.example` as a brand-new file. Each merges cleanly vs `main` today (file absent), but the instant one merges the other flips to an **add/add conflict on that single file**. Resolution is trivial and lossless:

> **Keep BOTH env blocks.** #1's keys (`NEXT_PUBLIC_FORMSPREE_CONTACT_ID`, `NEXT_PUBLIC_FORMSPREE_NEWSLETTER_ID`) and #11's keys (Supabase, `MUTATION_SECRET`, `GROQ_API_KEY`, `CRON_SECRET`, `SMTP_*`) are completely non-overlapping — just concatenate. No code logic in the conflict.

Everything else in #1 vs #11 is disjoint (#1 = `content-engine/`, `lib/data/resources.ts`, resource SVGs; #11 = `app/api/grants/*`, `app/grants/*`, grants migration).

### Config-consistency note (flag for after both merge)
Canonical-site-URL env var name is inconsistent: **#15's code** (`lib/site.ts`) reads `NEXT_PUBLIC_APP_URL`, but **#11's `.env.example`** documents `NEXT_PUBLIC_SITE_URL` for the same concept. A custom-domain deploy following #11's template would be silently ignored by #15's canonical logic. Pick ONE name in both the code and the env template when both merge.

---

## CROSS-REPO ORDERING CONSTRAINT (the one that spans two repos — easy to miss)

**command-center-redirect #1 depends on psychic-bassoon #11, and currently links to the wrong host.** Verified live this run:

- The dashboard links **9×** to `https://psychic-bassoon-cam6stef.vercel.app` (7 grant rows/cards + "view all" + root). `curl -I` on that host → **`302` redirect to `vercel.com/sso-api`** (Deployment Protection ON) for `/` and `/grants`. Public users hit a **Vercel login wall**, not the tracker.
- The **public** production site is `https://psychic-bassoon-psi.vercel.app` (title "The Plug AI"). Its `/grants` returns **`404`** — the route lives ONLY on the unmerged DRAFT **#11** (`app/grants/page.tsx`).

**Recommendation before un-drafting command-center #1:** (a) un-draft + merge psychic-bassoon **#11** to `main` and confirm the public `-psi` (or custom) domain serves `/grants` with a `200`; (b) **repoint all 9 links** from the SSO-gated `-cam6stef` preview to the canonical public domain. Otherwise the grant links are non-functional for every public visitor. (Non-blocking notes from Run 167 still apply: the PIN gate is cosmetic on a public Pages site; a couple of grant-status rows may contradict the archived Kresge/IL-DCEO decisions — reconcile against the live tracker.)

---

## Other repos (no cross-dependencies — merge on their own merits)

| PR | Draft? | State | Note |
|----|--------|-------|------|
| forming-paws #32 | no | MERGEABLE/CLEAN | `fix(upload): reject non-image files with 400 instead of 500` (`+66/-8`, 3 files). Separate repo, zero interaction. |
| ai-video-reel-generator #24 | no | MERGEABLE/CLEAN | `fix(supabase): clear error when env unconfigured (refs #5)` (`+22/-4`). Improves the founder-blocked #5 experience; safe standalone. |
| Link-inbio #5 | DRAFT | MERGEABLE/CLEAN | Obsidian ops-vault docs (`+94/-0`). |
| Link-inbio #6 | DRAFT | MERGEABLE/CLEAN | Binary resume PDF add. |

---

## Frontier status (unchanged — 3 open issues, all non-actionable by an agent)
- **forming-paws #8** — IL-SOS incorporation filing (non-automatable founder steps).
- **ai-video-reel-generator #5** — Supabase project must be created by the founder.
- **skills-introduction-to-git #1** — git learning exercise.

Per me.md sequencing, Track 1 (Plug AI) *execution* doesn't begin until 2026-10-13, so these psychic-bassoon PRs are banked ahead of schedule. The win now is **clearing the queue cleanly**, which is what this guide enables — not piling on more inventory.
