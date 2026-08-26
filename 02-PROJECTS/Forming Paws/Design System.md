---
type: project-note
project: Forming Paws
created: 2026-08-21
updated: 2026-08-21
tags: [design-system, forming-paws]
---

# Forming Paws — Design System

Source of truth: `~/forming-paws/DESIGN.md` · tokens in `tailwind.config.ts` · vocabulary in `app/globals.css`

Adapted from three systems on [[../../04-RESOURCES/Design/Refero Styles — Design Reference|Refero Styles]] — Ease Health, Function, Steep — matched on descriptor to this brand's existing warmth.

## What did not change

Fraunces, Nunito, `#2F6B5C` green, `#E8734A` terracotta, `#FBF7F0` ivory. The brand kept its voice; it changed its posture.

## The surface ramp

| Level | Token | Hex | Use |
|---|---|---|---|
| 0 | `ivory` | `#FBF7F0` | Page canvas |
| 1 | `paper` | `#FFFCF7` | Cards — warm, never `#fff` |
| 2 | `wash` | `#F2EDE3` | Inputs, insets |
| 3 | `brand.soft` | `#E3EFE9` | Emphasis bands |
| 4 | `brand.moss` | `#D2E4DA` | The closing CTA band |
| 5 | `brand` | `#2F6B5C` | Inverted, fills |

`hairline` `#E7DFD1` for borders.

**Every rung is chosen so `ink-soft` `#6C6155` clears 4.5:1 on it.** That constraint set `brand.moss` — its first value `#CFE2D8` measured 4.46:1, failing by four hundredths, and was only caught because the rung finally got used.

**Two colour rules, both learned the hard way:**
- `accent` `#E8734A` is **fill only** — 2.82:1 on ivory. Never text, never a focus ring. The docs originally certified it at "3:1".
- `accent.dark` is `#AD4727`, darkened from `#C95A33` (3.94:1) so the documented escape hatch for accent text actually passes.
- **Never** `accent.dark` on `brand.moss` — 4.28:1. Does not occur today; must not be introduced.

## Type scale

Fluid `clamp()` across 375→1440. Weight splits at 24px: `.fp-display` / `.fp-h1` / `.fp-h2` / `.fp-h3` at **400**; `.fp-h4` / `.fp-h5` at **700** — below 24px a light serif goes limp against body copy. Plus `.fp-eyebrow` (11px, 0.1em, uppercase) and `.fp-lead`.

The minimum term of every clamp is a plain `rem`, so browser text-resize still works — a `vw`-only clamp fails WCAG 1.4.4.

## The pattern worth reusing

A site-wide restyle touched **no page logic** because the `.fp-*` classes were redefined *underneath their existing call sites*. Measured first: `fp-card` ×18, `fp-link` ×19, buttons ×31. Change the vocabulary, change 26 pages at once.

## Mascot — Sage

`components/mascot/Sage.tsx`. Six moods, one shared 72×72 viewBox so swapping mood never shifts the mark. Deliberately **mixed-breed** — one ear perked, one folded — because the platform is anti-puppy-mill and a purebred head would endorse a breed. Smallest shipping instance is 30px in the footer.

`sleeping` is currently **unwired**: it lived on four route `loading.tsx` files until those were removed for downgrading auth redirects (see [[Visual Refresh — Build Log]]).

## The landing splash

`/` opens on a full-viewport splash (`components/landing/Splash.tsx`): the WebGL
meadow full-bleed, **Sage popping out** from his own Z-plane above it, a glass
overlay card carrying the headline, and a scroll cue down to "Start here" — the
trust points and sign-in panel. Structure follows a second refero reference,
*General Intelligence Company*.

The eyebrow, h1, lead and CTAs **moved** here out of the old hero rather than
being duplicated; one h1 on the page throughout.

**Sage is an SVG on a near plane, never scene geometry.** As geometry he would be
rasterised and would vanish on every fallback path, including all of mobile. As
SVG at `translateZ(120px)` inside the stage's perspective he stays vector and
renders in all six fallback states, verified including JS-disabled.

The public nav gained a **"Log in"** link, which it had never had — the only
sign-in route from the home page was the panel inside the hero, and a splash
pushes that below the fold.

## WebGL hero

`components/art/webgl/` — five ridge silhouettes at real Z depths, unlit flat colour, page-tinted fog, drifting motes. A perspective camera derives the parallax. Dynamic `import()` behind `requestIdleCallback`; **not in the initial bundle** (First Load JS 179 → 180 kB). Declines to run in seven situations, each invisible because the SVG planes are never removed until the canvas has a frame.

## Result vs main

LCP **~320ms → ~72ms** · CLS **0.0035 → 0** · 0–1 dropped frames at 4× CPU · transfer +228 KB.
Splash headline contrast over the glass card: **14.39:1** at 1440, **14.29:1** at 375,
sampled from rendered pixels rather than computed from tokens.

**Known limitation:** on 375–390px phones the scroll cue's lower half sits under
the mobile sticky join bar until the first scroll. Both CTAs and the headline are
fully visible, and the cue is in normal flow so it is never permanently hidden.

Related: [[Visual Refresh — Build Log]] · [[../../04-RESOURCES/Design/Verification Playbook|Verification Playbook]]
