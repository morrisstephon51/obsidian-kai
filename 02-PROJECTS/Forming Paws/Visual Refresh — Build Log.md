---
type: project-note
project: Forming Paws
created: 2026-08-21
tags: [forming-paws, design-system, webgl, retrospective]
---

# Visual Refresh — Build Log

Branch `feat/visual-refresh`, 16 commits, 85 files, +2,664 −274 vs `main`. **Not merged** — Stefan reviews first.

## The arc

Stefan supplied one URL — `styles.refero.design`, typed with a transposition (`tyhttps://sles.…`) — and a three-part brief: imagery, scroll motion, a mascot. Everything else followed from that.

| Part | Outcome |
|---|---|
| Imagery | Already merged before the session (#51); AVIF later found missing (#55) |
| Design system | Not in the brief. Added as PR #0 (#52) because the refero work had to land somewhere |
| Scroll motion | #53 — built by **deleting** Framer Motion, not adding a library |
| Mascot | #54 — Sage, six states |
| WebGL | #57 — **reverses the brief's own "no WebGL"**, at Stefan's direction after previewing |
| Verification | #56, #58 — two audit passes, 30 defects |
| Landing splash | #59 — Sage front and centre; the mascot was on eight surfaces and not the landing page |

## Decisions worth keeping

**The vocabulary-redefinition trick.** A site-wide restyle touched no page logic because `.fp-card`, `.fp-btn`, `.fp-band` etc. were redefined *underneath their existing call sites*. Measured first: `fp-card` ×18, `fp-link` ×19, buttons ×31 carried most of the surface area. Change the vocabulary, change 26 pages. **Reuse this pattern.**

**Framer Motion was removed, not added.** It was driving three CSS custom properties from scroll position and charging ~34 KB gzipped on the critical path for it — the source of a +249ms LCP regression. A passive listener behind a rAF gate does the same in under a kilobyte.

**WebGL as progressive enhancement, never on the critical path.** three.js is a dynamic `import()` behind `requestIdleCallback`, so it does not start downloading until the LCP image has painted. First Load JS went 179 → 180 kB — the library is not in it. It also declines to run in seven situations, and every refusal is invisible because nothing is removed until the canvas has a frame to show.

**Not below 768px.** On a phone the hero stacks to ~1200px tall, putting the ridges a full screen below the fold. Mobile ships 633 KB of JS against desktop's 1,175 KB.

## What went wrong, and why

Two regressions were invisible without measuring:

- **`Reveal` made content disappear.** It hid sections already on screen at hydration; the observer's −12% rootMargin then excluded them, so they stayed at opacity 0 until the reader scrolled. 1.00 → 0.00, still 0.00 a hundred frames later.
- **`loading.tsx` downgraded auth redirects.** A Suspense boundary on a segment gated by server-side `redirect()` makes Next flush the shell first: `307 → /login` became `200` + client-side redirect. A segment `layout.tsx` fixes it but costs a third `getUser()` per request, so the boundaries were removed instead and `sleeping` is now unwired.

And one class of mistake happened **twice**:

> A migration keyed on an exact pattern, then audited by a grep with the same blind spot — so the audit agreed with the migration instead of testing it.

17 `<h2>`s were missed because they write `id=` before `className`. Later, ~14 CTAs were missed because they wrote the same utilities in a different order. **The lesson: never audit a transformation with the same matcher that performed it.**

## The splash (#59)

Stefan noticed what two audits had not: **Sage was wired into eight surfaces and none of them was `/`.** On the landing page it appeared only inside the shared footer at 30px.

Structure follows a second refero reference — *General Intelligence Company* — a full-bleed scene at viewport height with a glass overlay card, content below. The eyebrow, h1, lead and CTAs **moved** out of the old hero into the splash; the trust points and sign-in panel stayed and became "Start here", the first thing you reach on scroll. One h1 on the page throughout.

**Sage pops out from its own Z-plane above the WebGL scene, not inside it.** As geometry it would be rasterised and would vanish on every fallback path, including all of mobile. As an SVG at `translateZ(120px)` inside the stage's perspective it stays vector and renders in all six fallback states — verified, including JS-disabled.

Two things this exposed:

- **There was no "Log in" in the public nav at all.** The only sign-in route from the home page was the panel inside the hero, which a splash pushes below the fold. That was the "members" half of splash → landing → members.
- **A cascade-order bug that survived four attempts to fix it by sizing.** The mobile scroll cue kept landing under the fixed join bar. The cause was not layout: the mobile block sat *above* the base `.fp-splash-cue` rule, and **a media query adds no specificity**, so source order kept `position: absolute` winning. Trimming content moved nothing. Worth remembering as a class of bug — the symptom looked like a space problem and was a cascade problem.

Cost: LCP 60 → 72ms, CLS 0, +3 KB. Headline contrast over the glass card 14.39:1 / 14.29:1, sampled from rendered pixels.

## Numbers that mattered

- `brand.moss` was documented as "the rung that was missing" and **rendered nowhere** — its only consumer was unused. When finally applied it put `ink-soft` at 4.46:1, failing AA by four hundredths. Value moved `#CFE2D8` → `#D2E4DA`.
- The WebGL motes **were never on screen**: `BufferAttribute` stores its array by reference, so each frame's offset compounded. 702 units of drift per second against a 70–170 unit visible height.
- The design docs certified `#E8734A` as "clears 3:1 on ivory". It is **2.82:1**.

Related: [[Design System]] · [[Status Log]] · [[../../04-RESOURCES/Design/Verification Playbook|Verification Playbook]] · [[../../04-RESOURCES/Design/Refero Styles — Design Reference|Refero Styles]]
