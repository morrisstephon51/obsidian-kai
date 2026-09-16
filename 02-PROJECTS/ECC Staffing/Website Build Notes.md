 see what I'm looking at# ECC Website — Build Notes

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

## Addendum: Client review prep (2026-09-15)

**Review:** Tue Sep 15, 8:30pm CT, video call, Stefan screen-sharing.

**Live-site facts (checked 2026-09-15):** current eccstaffing.com runs on Lovable (IP 185.158.133.1), now 5 pages (Home, Clients, Applicants, Insights, About), no /contact, no forms. Misspelled `info@eccstsffing.com` is still in the footer of every page, and that typo domain is unregistered. Registrar + DNS: Hover (paid through 2027-07-04). Email: Google Workspace (`MX 1 smtp.google.com`). No SPF, no DKIM, DMARC `p=none`. Record TTL 300.

**Copy pass:** em dashes cut from 74 to 1 (the client's own verbatim hero line kept). "(or Claude)" removed from /admin/. generate.py regenerated; audit.py passes 29/29; Playwright check 28 pages x 5 widths (1440 to 320px), 0 problems.

**Preview:** Cloudflare Workers (assets upload) (https://soft-cloud-48db.morrisstephon51.workers.dev), uploaded via dashboard from `~/Desktop/ecc-staffing-preview`. Built with noindex header + disallow-all robots, forms show a "not connected yet" note, /admin/ excluded. The Aug 31 claude.ai preview link was already sent to the client; turn off its sharing after tonight.

**Hosting facts (verified 2026-09-15):** Vercel Hobby forbids commercial use (Pro $20/mo). Cloudflare Pages is free, but an apex domain requires moving DNS to Cloudflare (copy MX/verification/DMARC exactly first). Netlify works with DNS kept at Hover (free with a credit cap that pauses sites, or $9/mo). Lovable needs a paid plan (from $25/mo) to keep a custom domain.

**Docs (Stefan's Google Drive):**
- Launch plan (client-facing): https://docs.google.com/document/d/1Rm4Ayme3pm3JlnMSsCjIsFEojmEoPLYF3dk5Qoy6iCw/edit
- Change requests sheet: https://docs.google.com/spreadsheets/d/1aj77_95cDzdh5d3bs0HlwGlMH_oFmgkJRBXVfK55W4E/edit
- Review talk track (private): https://docs.google.com/document/d/1zU4HyJ4aPNPGh7Zugxv0AyeJJz6euRKmyRu9M27f_ng/edit

**Tooling note:** `wrangler login` can't finish from Claude's sandbox (the OAuth callback to localhost is blocked). Use a dashboard upload or a CLOUDFLARE_API_TOKEN.

**Pricing (agreed 2026-09-15):** build $2,400 regular / **$240 family rate** (90% off), paid $80/mo for 3 months; care $150/mo regular / **$39/mo family rate**. Months 1-3 total $119/mo, then $39/mo. Unlinked pricing page at `/proposal/` exists in the preview build only (not in `website/`, so it never ships to the live site). Pricing doc: https://docs.google.com/document/d/1fIjuRppi9e217YKFzZVQngiayRq0PGOk-6meAOmTWVQ/edit
