# ECC Website — Build Notes

**Built:** 2026-08-31 · **Location:** [[Website Strategy]] → `website/` folder in this project
**Status:** Built, audited (3 passes), ready to deploy. Pre-launch checklist below.

## What was built

Complete static rebuild of eccstaffing.com implementing the strategy — 28 pages:

- **Home** — preserved hero copy/CTAs, pillars, stats bar, industries section, true-north band
- **For Clients** hub + **Contract Staffing**, **Contract-to-Hire**, **Direct Placement**
- **Industries** ×5 — Healthcare, Administrative, Light Industrial, Finance & Accounting, Technology
- **Request Talent** ★ (5-field form)
- **For Applicants** hub, **How It Works**, **Open Roles**, **Apply** ★ (short form + optional resume)
- **About ECC**, **Results** (testimonial slots ready for real stories)
- **Insights** + 2 launch articles (one per audience)
- **Contact** ★, 3 thank-you pages, Privacy/Terms/Accessibility drafts, 404
- `sitemap.xml`, `robots.txt`, `EmploymentAgency` JSON-LD on Home/Contact

**Brand preserved:** real logo and hero photo recovered from the site capture; navy/ink + gold palette, compass voice, verbatim homepage copy, existing stats (48 hrs · 92% · 5 · 1:1).

**Email requirement met:** all 3 forms post to FormSubmit → `info@eccstaffing.com` with `[Talent Request]` / `[Application]` / `[Contact]` subject prefixes; every visible address is `info@eccstaffing.com`. The old site's misspelled footer address (`info@eccstsffing.com`) appears nowhere.

## Audit results (all passing)

1. **Automated scan** (`_build/audit.py`) — 28 pages: email policy, internal link integrity, exactly one H1 + title/meta/canonical/viewport per page, img alt text, labeled form controls, form recipients/subjects, sitemap coverage. ✅
2. **Real browser** (Chromium/Playwright) — all 28 pages at 7 widths (1440→320px): zero horizontal overflow, no hero/photo collision (the old site's bug), mobile nav works, apply-form vertical preselect works, no console/page errors. Two bugs found and fixed during this pass: header CTAs overflowing at phone widths (now a second header row, keeping both money actions visible) and a 2px grid overflow at 320px (grid minimums capped at 100%). ✅
3. **HTML parse + strategy compliance** — 0 structural problems; misspelled domain absent, 3/3 forms correct, verbatim tagline preserved, stats and true-north band sitewide, phone consistent on all pages. ✅

## Pre-launch checklist (needs a human)

- [ ] Confirm `info@eccstaffing.com` mailbox exists and is monitored (SLA owner assigned)
- [ ] Deploy `website/` (minus `_build/`) to the host at the domain root, HTTPS
- [ ] Submit each of the 3 forms once from the live domain; click FormSubmit's one-time activation email at info@; confirm delivery incl. resume attachment
- [ ] Point host 404 handling at `/404.html`
- [ ] Have counsel review `/privacy/` and `/terms/` drafts (flagged in-page)
- [ ] Optional now / Phase 2: real testimonials into `/about/results/` (template in HTML comment), client logos, team photos, live role listings with JobPosting schema, Google Business Profile decision (Texas geo layer)

## Editing

`python3 _build/generate.py` regenerates all pages from one source; `python3 _build/audit.py` re-verifies. Direct HTML edits work too (regeneration overwrites them). Details in `website/README.md`.

## Addendum — Owner console (added 2026-08-31)

`/admin/` — an unlinked, noindexed management hub for the owner: sign-in links to each platform (lead inbox for info@eccstaffing.com, FormSubmit, hosting dashboard, Search Console, Business Profile, LinkedIn), routine tasks, editing instructions, and the launch checklist. It stores no credentials — each platform authenticates itself. For true privacy, enable the host's password protection on `/admin/` (noted on the page itself). Excluded from sitemap.xml and disallowed in robots.txt.

## Addendum — Client preview (added 2026-08-31)

Shareable preview of the full site (all 29 pages, navigable, forms disabled):
**https://claude.ai/code/artifact/9779ff0d-5c23-4490-a754-49679eb266a4**
The link is private until shared — open it and use the page's share menu to send it to the client. Regenerate after edits with `python3 _build/preview.py` and republish. (Direct Vercel deployment was attempted but the Vercel–GitHub integration doesn't have access to this repo; linking it in the Vercel dashboard would enable auto-deploy from `02-PROJECTS/ECC Staffing/website/`.)

---
*Backlinks: [[01-DAILY/To-Do-List|To-Do-List]] · [[02-PROJECTS/ECC Staffing/Website Strategy|Website Strategy]]*
