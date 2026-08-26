---
type: resource
created: 2026-08-21
tags: [design, design-system, reference, ai-tooling]
---

# Refero Styles — Standing Design Reference

**https://styles.refero.design**

The default design-system reference for **every website and app build from now on** (decision made 2026-08-21).

## What it is

A searchable catalog of **2,000+ design systems extracted from real shipping product sites**, published as machine-readable `DESIGN.md` files built specifically for AI coding agents (Claude Code, Cursor, v0).

Each entry contains:

- Exact colour tokens — hex + the **role** each colour plays
- Typography — family, weights, sizes, tracking, leading, full type scale
- Spacing scale and base unit
- Border radii per element class
- Elevation strategy (usually: *how* they avoid shadows)
- Layout/grid, max-widths, section gaps
- Component specs — buttons, cards, badges, inputs, nav
- Imagery treatment
- Explicit **Do / Don't** rules

## URL structure

| Purpose | URL |
|---|---|
| Index / search | `https://styles.refero.design` |
| Single system | `https://styles.refero.design/style/{uuid}` |
| Screenshot library (parent) | `https://refero.design` — 125k+ real product screens |

`styles.` is the token layer and is the more useful of the two for building. The parent `refero.design` is for visual browsing.

## Method — how to actually use it

1. Read the index. Cards show a product name plus a **poetic descriptor** — *"Botanical greenhouse on cream paper"*, *"warm apothecary journal"*, *"prismatic light through obsidian"*. The descriptor is the fastest matching key.
2. Pick **2–3 entries** whose descriptor matches the target brand's *existing* palette and voice.
3. Pull each `DESIGN.md`.
4. Look for **convergence** — where all three independently agree, that's a real rule, not one team's taste.
5. Take the **structure**, keep your **identity**. Adopt surface ramps, type weights, radii, spacing, shadow policy. Keep your own palette and typefaces.

> Do not copy hex values across brands. Copy the system, not the skin.

## Applied — Forming Paws, 2026-08-21

Three matched entries, all in the "warm paper" family:

| Entry | Descriptor | Why matched |
|---|---|---|
| [Ease Health](https://styles.refero.design/style/e9f5e976-53f7-42f5-a882-4e63b3c2f734) | Botanical greenhouse on cream paper | Green-on-cream health product; depth via tinted layers, zero shadows |
| [Function](https://styles.refero.design/style/21b71be3-78a0-4681-a5b9-64cc4b40eb67) | Warm apothecary journal | Terracotta on parchment — near-identical to FP's `#E8734A` on `#FBF7F0` |
| [Steep](https://styles.refero.design/style/75fdb89f-ca64-41b3-af36-7a78bd09448e) | Serif analytics on warm paper | Serif display + pill controls + surface-level rhythm |

**Four rules all three converged on** (and which Forming Paws was breaking):

1. **No box-shadows on content cards.** Depth comes from a tinted surface ramp, not elevation.
2. **Serif display at weight 300–400, never bold.**
3. **Negative letter-spacing that scales with size** — roughly −0.025em at 90px, −0.015em at 64/44px.
4. **Card padding ≥ 24px.** Ease Health: "no tight padding under 21px."

### How it turned out

Worth knowing before using this resource again: the three systems' **structural**
rules transferred cleanly and were the whole value — surface ramp, serif weight
split, size-scaled tracking, padding floor. What did not transfer was any of
their colour; that stayed Forming Paws'.

The refero DESIGN.md files are accurate about their *own* sites. They are not a
substitute for measuring your own — the contrast figures written into the
adapted system had to be recomputed locally, and two were wrong.

See [[../../02-PROJECTS/Forming Paws/Design System|Forming Paws Design System]],
[[Verification Playbook]].
