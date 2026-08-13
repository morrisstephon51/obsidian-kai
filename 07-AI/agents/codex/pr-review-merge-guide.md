# PR Review & Merge-Order Guide — psychic-bassoon (The Plug AI)

*Author: Codex · Run 178 · 2026-08-13*
*Purpose: the founder-review backlog is the ecosystem's #1 open bottleneck (clawd Run 193, antigravity Run 168). This guide makes clearing it fast and safe. Every claim below was verified this run against live GitHub (`gh pr view` / `gh pr diff --name-only`), not assumed.*

---

## TL;DR

- **8 open PRs on psychic-bassoon** (#1, #11, #13, #14, #15, #16, #17, #18) + **1 on forming-paws** (#32). All 9 are **OPEN + MERGEABLE + CLEAN** against `main` right now.
- **Only ONE stacking hazard exists**: PRs **#1 and #11 both create `.env.example` as a brand-new file.** Each merges cleanly against `main` today (the file doesn't exist yet), but the instant one merges, the other flips to an **add/add conflict** on that single file. Nothing else in them overlaps.
- **6 of the 8 PRs (#13–#18) are mutually file-disjoint** and disjoint from #1/#11 → merge in **any order, zero conflict risk.** Clear these first in minutes.

---

## Recommended merge order

### Phase 1 — the six small quality fixes (any order, safe now)
File-disjoint from each other and from #1/#11. Verified no shared file. Merge freely:

| PR | Type | Files | Value |
|----|------|-------|-------|
| #13 | security | `lib/mailer.ts` | HTML-escape user fields in contact emails (injection sink) |
| #14 | hardening | `app/api/subscribe/route.ts` | Email validation + 254-char cap on last un-hardened write route |
| #15 | SEO | `lib/site.ts`, `app/layout.tsx`, `app/learn/[slug]/page.tsx`, `app/robots.ts`, `app/sitemap.ts` | Single-source canonical site URL |
| #16 | a11y | `components/shared/Navbar.tsx` | Mobile menu → accessible modal (WCAG 4.1.2) |
| #17 | SEO | `app/{about,community,contact,learn,workshops}/layout.tsx`, `app/resources/page.tsx` | Per-page titles/canonicals/OG cards (kills duplicate-title penalty) |
| #18 | a11y | `app/{community,contact,workshops}/page.tsx`, `components/shared/{EmailCapture,Footer}.tsx` | Announce form success/error to assistive tech (WCAG 4.1.3) |

*Note on apparent near-misses (all verified NON-overlapping): #17 touches `app/resources/page.tsx` (index) while #1 touches `app/resources/[slug]/page.tsx` (detail) — different files. #17 touches `app/*/layout.tsx` while #18 touches `app/*/page.tsx` — different files. #15 touches `app/learn/[slug]/page.tsx` while #17 touches `app/learn/layout.tsx` — different files.*

### Phase 2 — the two large feature PRs (order is founder's choice; one conflict to resolve)
- **#1** — "Add real content, working forms, resource detail pages" (+7718/-61)
- **#11** — "Grant Matching Tracker" (+869/-0)

Merge whichever is the higher feature priority **first**. Before merging the **second**, GitHub will show a conflict on **`.env.example` only**. Resolution is trivial and lossless:

> **Keep BOTH env blocks.** #1's keys (`NEXT_PUBLIC_FORMSPREE_CONTACT_ID`, `NEXT_PUBLIC_FORMSPREE_NEWSLETTER_ID`) and #11's keys (Supabase, `MUTATION_SECRET`, `GROQ_API_KEY`, `CRON_SECRET`, `SMTP_*`) are **completely non-overlapping** — they serve different features. Just concatenate the two files. No code logic is involved in the conflict.

Everything else in #1 vs #11 is disjoint (#1 = `content-engine/`, `lib/data/resources.ts`, resource SVGs; #11 = `app/api/grants/*`, `app/grants/*`, grants migration).

---

## One config-consistency note (NOT a merge conflict — flag for after both merge)

The canonical-site-URL env var name is inconsistent across two PRs:
- **#15's code** (`lib/site.ts`) reads **`NEXT_PUBLIC_APP_URL`**.
- **#11's `.env.example`** documents **`NEXT_PUBLIC_SITE_URL`** for the same concept.

If a custom domain is ever configured by following #11's template (`NEXT_PUBLIC_SITE_URL`), #15's canonical logic (reading `NEXT_PUBLIC_APP_URL`) will **silently ignore it** and fall back to the vercel default → wrong canonicals/OG URLs. **Pick one name** in both the code and the env template when both are merged. Cheap to fix; easy to miss.

---

## forming-paws #32 (separate repo)
`fix(upload): reject non-image files with 400 instead of 500` — OPEN + MERGEABLE + CLEAN. No interaction with any psychic-bassoon PR. Merge on its own merits.

---

## Frontier status (unchanged this run)
The 3 open **issues** account-wide remain non-actionable by an agent:
- **forming-paws #8** — IL-SOS incorporation filing (non-automatable founder steps).
- **ai-video-reel-generator #5** — Supabase project must be created by founder.
- **skills-introduction-to-git #1** — git learning exercise.

Per me.md sequencing, Track 1 (Plug AI) *execution* doesn't begin until 2026-10-13, so these psychic-bassoon PRs are banked ahead of schedule — no urgency to pile more; the win now is **clearing the queue cleanly**, which is what this guide enables.
