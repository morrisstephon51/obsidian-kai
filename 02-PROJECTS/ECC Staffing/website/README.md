# eccstaffing.com — static site

Complete rebuild of eccstaffing.com per the [Website Strategy](../Website%20Strategy.md).
28 static pages, no build dependencies to serve — deploy the contents of this
folder (everything except `_build/`) to any static host at the **domain root**
(links are root-relative: `/clients/`, `/apply/`, …).

## Deploy

Any static host works (Netlify, Vercel, Cloudflare Pages, S3+CloudFront, cPanel).
- Upload everything except `_build/`.
- Point the host's 404 handling at `/404.html`.
- Serve over HTTPS at `https://eccstaffing.com`.

## Email — the one functional requirement

Every form posts to **`https://formsubmit.co/info@eccstaffing.com`** and every
visible address/mailto is **`info@eccstaffing.com`**. Three forms exist:
Request Talent (`[Talent Request]` subject), Apply (`[Application]`, supports a
resume attachment), Contact (`[Contact]`).

**Before launch:**
1. Confirm the `info@eccstaffing.com` mailbox exists and is monitored.
2. Submit each form once from the live domain — FormSubmit sends a one-time
   activation email to info@ on first use; click it, then submissions flow.
3. If you prefer your own form backend later, change each `<form action=…>` —
   nothing else needs to change.

FormSubmit is a free relay and fine to launch with; a paid form backend or a
small serverless handler is a worthwhile upgrade once volume grows.

## Editing

Pages are generated from `_build/generate.py` (copy lives there in one place):

    python3 _build/generate.py   # regenerates all pages
    python3 _build/audit.py      # verifies email policy, links, structure, a11y basics

You can also edit the emitted HTML directly for one-off tweaks — just know a
later regeneration overwrites it.

## What's intentionally NOT in this build

- **Testimonials / client logos / team photos** — the strategy requires real
  names and faces; nothing is fabricated. `/about/results/` has an HTML
  comment template to paste approved stories into.
- **Live job listings** — `/applicants/open-roles/` uses an honest
  "most placements are never posted" state routing to Apply. Add real
  listings (with `JobPosting` schema) when there are real roles to post.
- **Final legal copy** — `/privacy/` and `/terms/` are drafts flagged for
  counsel review before launch.

## Assets

`assets/img/logo.png` and `assets/img/hero-team.jpg` were recovered from the
existing site capture; branding (navy/ink + gold, compass identity, tracked
uppercase eyebrows) is preserved. Typeface is Hanken Grotesk via Google Fonts
with a system-stack fallback.
