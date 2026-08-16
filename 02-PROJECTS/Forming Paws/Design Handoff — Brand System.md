---
type: reference
project: Forming Paws
tags:
  - forming-paws
  - design
  - handoff
---

# Design Handoff — Forming Paws Brand System

**For: the session developing `main` (the Next.js app).** Written 2026-08-16 by the session that built the brand. The brand is now APPLIED across the app — this note exists so future work stays on-system instead of drifting back to grays.

## The identity (decided with Stefan, 2026-08-15)
Warm, trustworthy, dog-family — deliberately NOT The Plug AI's dark/amber tech look (Stefan's explicit choice; Plug AI appears only as the "Built by The Plug AI" footer credit).

## Tokens — already in `tailwind.config.ts`, use these classes
| Token | Hex | Use for |
|---|---|---|
| `bg-brand` / `text-brand` | #2F6B5C | Primary actions, links-on-hover, own chat bubbles, logo ground |
| `bg-brand-dark` | #245448 | Primary hover states |
| `bg-brand-soft` | #E3EFE9 | Tinted backgrounds, selected states |
| `bg-accent` / `text-accent` | #E8734A | Unread badges, highlights, the heart in the logo — sparingly |
| `bg-accent-soft` | #FDEEE7 | Accent-tinted backgrounds |
| `bg-ivory` | #FBF7F0 | Page grounds (marketing surfaces) |
| `text-ink` / `text-ink-soft` | #26221C / #6C6155 | Body / secondary text |
| `font-display` | Fraunces | Headings (already applied globally via globals.css @layer base) |
| `font-body` | Nunito | Body (already the global default) |

## Rules of thumb
1. **One brand-green primary action per view.** Secondary actions: outline/text style, never a second solid green.
2. **Accent (terracotta) is a spice** — badges, counts, the logo heart. Never a big button (it reads destructive-adjacent at size).
3. **Semantic colors stay semantic**: success/approve = green-600, destructive/reject = red family, warnings = amber. Don't brand-wash them.
4. Logo: `/public/logo.svg` (also the favicon via `app/layout.tsx`). Don't recreate it; reference the file.
5. Legacy vanilla pages in `public/` (admin.html, styles.css) carry the same palette in CSS-variable form — keep them in sync if touched.

## State as of 2026-08-16
- ✅ Tokens + fonts in config and globals; favicon = logo
- ✅ All 26 primary-action sites app-wide swapped to brand (commit bf2b233); unread badges = accent
- ✅ UX fixes shipped from the production button audit: POST /auth/signout + dashboard Sign out, instant chat-send feedback (immediate poll, dedupe preserved), verification notice links to upload, "Password"→"Account"
- Verified each step: tsc / eslint / 86 unit tests / next build / live production re-test

## Suggested next design increments (not done)
- Card hover/elevation language on browse dog cards (see gh-pages `styles.css` `.dog-card` for the reference feel)
- `bg-ivory` page ground on marketing routes (`/`, `/faq`, `/contact`) for warmth; app routes can stay white
- Empty states with the paw mark instead of bare text
