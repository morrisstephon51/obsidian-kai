---
type: reference
project: Forming Paws
tags:
  - forming-paws
  - domain
  - setup
---

# Domain Setup — theplugai.xyz → Forming Paws site

Goal: the live site (currently `morrisstephon51.github.io/forming-paws`) answers at **https://theplugai.xyz**. Two steps: DNS at the registrar, then the custom domain in GitHub. ~10 minutes of work, up to a day of DNS propagation.

## Step 1 — DNS records (at the registrar where the domain was bought)

Open DNS management for `theplugai.xyz` and add **five records**:

| Type | Host/Name | Value |
|------|-----------|-------|
| A | @ | 185.199.108.153 |
| A | @ | 185.199.109.153 |
| A | @ | 185.199.110.153 |
| A | @ | 185.199.111.153 |
| CNAME | www | morrisstephon51.github.io |

Delete any pre-existing A or CNAME on `@` (registrars often park one there). Leave MX/TXT records alone — they carry email/call-alias forwarding and are unaffected by pointing the website.

## Step 2 — Tell GitHub about the domain

1. Go to `github.com/morrisstephon51/forming-paws` → **Settings → Pages**
2. Under **Custom domain**, enter `theplugai.xyz` → **Save**
3. Wait for the DNS check (green ✓ — can take minutes to ~24 h after Step 1)
4. Tick **Enforce HTTPS** once the checkbox becomes available (certificate auto-issues)

## What happens after

- Site + member onboarding serve at `https://theplugai.xyz` (join page: `/join.html`)
- Old `github.io` links — including the QR code on the printed flyers — **auto-redirect** to the new domain, so nothing needs reprinting
- Call/email alias use of the domain keeps working (separate record types)

## Status
- [x] Domain purchased (2026-08-03)
- [x] DNS records added (verified 2026-08-04: all four A records + www CNAME correct)
- [x] Custom domain saved in GitHub Pages settings
- [x] HTTPS enforced (2026-09-15: set `https_enforced=true` via GitHub Pages API; verified http://theplugai.xyz 308-redirects to https, https serves 200)
- [x] Claude verified live: landing, join, demo, assets, waitlist API, and old-URL redirects (QR keeps working) — see Status Log 2026-08-04
