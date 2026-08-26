---
type: resource
created: 2026-08-21
tags: [design, verification, qa, method]
---

# Verification Playbook

Distilled from the Forming Paws visual refresh (2026-08-21), where two audit passes found **30 defects across 85 files** — most of them introduced by the same person who then failed to find them by eye. Everything here exists because something got past a review that felt thorough.

## The rule that produced the most findings

> **Never audit a transformation with the same matcher that performed it.**

This happened twice in one session. A regex migrating `<hN className="…">` missed every heading written `<h2 id="…" className="…">` — and the grep meant to verify the sweep used the same pattern, so it reported completion. Same again for CTA class strings matched as exact strings, which missed every call site writing the same utilities in a different order.

**Verify by property, not by pattern.** Don't grep for the thing you replaced; assert the property you wanted — "no heading renders at 24px/700", "every filled CTA has `border-radius: 9999px`" — and check it in a real browser against computed styles.

## Measure, never assume

Claims that sounded obviously true and were false:

| Claim | Reality |
|---|---|
| "`#E8734A` clears 3:1 on ivory" | **2.82:1** |
| "banners all sit below the fold" | 148–302px — above it on every page |
| "WebP/AVIF" | WebP only; Next defaults `formats` to WebP alone |
| "the parallax adds depth" | 0px separation while the hero is on screen |
| "the motes drift" | They exit frame in <1s; never visible |
| "the ramp has a new rung" | The rung was rendered nowhere |

**Compute contrast in code, don't eyeball it.** A relative-luminance function is ten lines. Failures cluster at 4.2–4.5:1, exactly where eyes cannot adjudicate. One value failed by *four hundredths*.

## Checks worth running every time

1. **Every route renders** — walk all of them, assert one `<h1>`, real text length, no console errors, no "Application error". Log in with a test fixture for member routes; auth-gated pages are where regressions hide.
2. **HTTP status parity against the base branch.** This caught `loading.tsx` silently converting `307 → /login` into `200` + client redirect. `curl -o /dev/null -w '%{http_code}'` per route, both branches, diff them.
3. **The fallback matrix**, not just the happy path — reduced motion, JS disabled, no WebGL context, save-data, low core count, small viewport. Each should be *invisible*, which means asserting the fallback is still on screen, not merely that nothing crashed.
4. **Perf from freshly started servers.** A long-running dev server degrades badly — one comparison showed a flattering "−224ms" that was entirely the old server dying. If a delta looks too good, restart and re-measure before believing it.
5. **Frame timing under CPU throttle**, at the viewport where the effect actually runs. A frame-rate test at 412px told me nothing about a feature gated to ≥768px.
6. **Mount/unmount cycles** for anything holding a GPU or native resource. Eight navigations away and back; assert heap flat and context ids not accumulating.
7. **Sample real pixels for contrast over imagery.** Hide the text, screenshot its bounding box, compute the worst ratio in it. Analytic contrast is meaningless over a gradient or a 3D scene.

## A symptom in one layer can have its cause in another

The mobile scroll cue on the Forming Paws splash kept landing under a fixed bar.
Four attempts to fix it by *trimming content* moved it exactly zero pixels,
because the cause was not space — the mobile override sat **above** the base rule
in the stylesheet, and **a media query adds no specificity**, so source order kept
`position: absolute` winning.

Dumping the computed geometry (`getComputedStyle(el).position`) found it in one
step, after four rounds of guessing at sizes did not. **When a fix that should
obviously work changes nothing, stop adjusting it and go read the computed
value.** The model is wrong, not the magnitude.

## Use adversarial verification for the findings themselves

Multi-agent review produces plausible-but-wrong findings at a high rate. Every finding got a second reviewer whose instruction was to **refute** it, defaulting to *not real*, and explicitly to check `git show origin/main:<path>` for whether the defect was pre-existing. Roughly a third were killed — several because the "regression" had shipped months earlier.

## Docs are part of the artifact

Half the confirmed findings in the second pass were false statements in `DESIGN.md` and code comments — a contrast ratio that did not hold, a mascot "nav" usage that never existed, "three paths" for a two-path SVG, a vocabulary listed as in-use when a third of it was unused. **A design system that documents primitives as though they were in use is a system nobody can trust.** List in-use and available separately.

Related: [[Refero Styles — Design Reference]] · [[../../02-PROJECTS/Forming Paws/Visual Refresh — Build Log|Forming Paws Build Log]]
