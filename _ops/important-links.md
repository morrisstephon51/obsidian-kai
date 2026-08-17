---
type: operations
category: links-registry
created: 2026-06-13
last-checked: 2026-08-11
last-audit: 2026-08-11
---

# Important Links Registry

> For the full cross-linked hub see **[[09-SYSTEM/Command Center|Command Center]]**. This page is the quick-reference table for all live sites, repos, and consoles.

**Every status below was verified live on 2026-08-11** — HTTP status, redirect target, `server:` header, page title, DNS resolution, `gh repo list`, and the Vercel project list. Nothing is carried over from the previous pass.

**Three entries from the 2026-08-06 audit were wrong, not merely stale.** They are corrected below and called out in [[#Corrections to the previous audit]].

---

## 🌐 All Sites — Master Table

| # | Name | Custom Domain | Fallback URL | GitHub Repo | Purpose | Status |
|---|---|---|---|---|---|---|
| 1 | **Forming Paws** | [theplugai.xyz](https://theplugai.xyz) | [forming-paws.vercel.app](https://forming-paws.vercel.app) | [forming-paws](https://github.com/morrisstephon51/forming-paws) | **The real app** — accounts, dog profiles, health verification, browse, matching, chat | 🟢 Live on Vercel |
| 2 | **The Plug AI** | [theplugai.info](https://theplugai.info) | [psychic-bassoon-psi.vercel.app](https://psychic-bassoon-psi.vercel.app) | [psychic-bassoon](https://github.com/morrisstephon51/psychic-bassoon) | AI literacy platform | 🟢 Live |
| 3 | **MUNDI Agent Dashboard** | [theplugai.live](https://theplugai.live) | [agent-world-olive.vercel.app](https://agent-world-olive.vercel.app) | [mundi-agent-dashboard](https://github.com/morrisstephon51/mundi-agent-dashboard) *(private)* | Agent fleet control panel | 🟢 Live |
| 4 | **Stefan's Portfolio** | [theplugai.life](https://theplugai.life) | [stefan-portfolio-eight.vercel.app](https://stefan-portfolio-eight.vercel.app) | [Stefan-Portfolio](https://github.com/morrisstephon51/Stefan-Portfolio) | Personal portfolio / resume | 🟢 Live |
| 5 | **Link-in-Bio** | [theplugai.net](https://theplugai.net) | [morrisstephon51.github.io/Link-inbio](https://morrisstephon51.github.io/Link-inbio/) | [Link-inbio](https://github.com/morrisstephon51/Link-inbio) | Main link aggregator | 🟢 Live (GitHub Pages) |
| 6 | **Command Center (public)** | [theplugai.online](http://theplugai.online) | [github.io/Link-inbio/dashboard.html](https://morrisstephon51.github.io/Link-inbio/dashboard.html) | [command-center-redirect](https://github.com/morrisstephon51/command-center-redirect) | PIN-locked hub | ⚠️ **HTTP only — HTTPS still broken** |
| 7 | **Community Intake & Routing** | — | [community-intake-routing.vercel.app](https://community-intake-routing.vercel.app) | [-Community_intake_Routing](https://github.com/morrisstephon51/-Community_intake_Routing) | "Join The Plug AI Community" signup | 🟢 **Live** — was wrongly logged 404 |
| 8 | **AI Content Engine** | — | [ai-video-reel-generator.vercel.app](https://ai-video-reel-generator.vercel.app) | [ai-video-reel-generator](https://github.com/morrisstephon51/ai-video-reel-generator) | Video reel / content builder | 🟢 **Live** — was wrongly logged as a redirect loop |
| 9 | **Content Machine** | — | [content-machine-wine.vercel.app](https://content-machine-wine.vercel.app) | [content-machine](https://github.com/morrisstephon51/content-machine) *(private, archived)* | Autonomous marketing engine | 🟢 Live (legacy) |
| 10 | **Psychic Octo Engine** | — | [psychic-octo-engine-psi.vercel.app](https://psychic-octo-engine-psi.vercel.app) | [psychic-octo-engine](https://github.com/morrisstephon51/psychic-octo-engine) *(archived)* | Link-in-bio variant | 🟢 Live — repo archived but deploy still serving |
| 11 | **Living Resume** | — | [github.io/Link-inbio/resume.html](https://morrisstephon51.github.io/Link-inbio/resume.html) | [Link-inbio](https://github.com/morrisstephon51/Link-inbio) | Public resume page | 🟢 Live |
| 12 | **Puppy Power (old prototype)** | — | [breeding-community-pets.deploypad.app](https://breeding-community-pets.deploypad.app/) | — | Superseded by #1 | 🟡 Up but retired |

---

## 🐾 Forming Paws — ONE site now, the old three-way split is gone

**As of 2026-08-11 the Next.js app serves the apex domain.** GitHub Pages is retired for this project, and `app.theplugai.xyz` was considered and **rejected** — there is no subdomain.

| | |
|---|---|
| **Live app** | **[theplugai.xyz](https://theplugai.xyz)** — Vercel, `main` branch, auto-deploys on push |
| Vercel project | `forming-paws` · `prj_AM2ABCIeP8UtZ8DDFEVVo7FF7kW3` · team `cam6stef` |
| Repo | [morrisstephon51/forming-paws](https://github.com/morrisstephon51/forming-paws) (public) |
| Database | Supabase `wyzcnkdonbdykidmcxvx` — migrations at **0021** |
| TLS | Let's Encrypt, issued 2026-08-11. Vercel did **not** auto-issue it; it needed `vercel certs issue` |

### App routes

**Live in production right now** (re-verified 2026-08-17):

| Public | Members only | Admin |
|---|---|---|
| `/` — landing, marketing **and sign-in** | `/dashboard` | `/admin/review-queue` — health docs |
| `/signup` · `/login` | `/browse` · `/matches` | `/admin/reports` — reported conversations |
| `/app` · `/faq` · `/contact` | `/matches/[id]` — conversation | `/admin/messages` — contact inbox |
| `/privacy` · `/terms` | `/dogs/new` · `/dogs/[id]` | |
| `/robots.txt` · `/sitemap.xml` | `/account/password` | |

**Pending on branches, NOT live** — PRs [#44](https://github.com/morrisstephon51/forming-paws/pull/44) and [#45](https://github.com/morrisstephon51/forming-paws/pull/45) are unmerged, so these 404 on production today (checked 2026-08-17):

| Route | Becomes |
|---|---|
| `/home` | The member home. Replaces `/dashboard`, which will 307 here |
| `/settings` | Profile, location, email, notifications, sign out, delete account |
| `/account/reactivate` | Restore an account inside the 30-day deletion window |

`/settings` and `/account/reactivate` additionally need **migration 0022 applied** — they read columns that do not exist in production yet. Merging the PRs without the migration gets you a page that renders and then errors.

### Legacy URLs — all still work

Printed on flyers and in QR codes, so they are kept alive as 307s:

`/index.html` → `/` · `/join.html` → `/signup` · `/login.html` → `/login` · `/home.html` → `/dashboard` · `/confirm.html?token_hash=…` → `/auth/confirm` *(query preserved)*

After #45 merges, `/home.html` and `/dashboard` both point at `/home` instead.

Still served as real files from `public/`: [/admin.html](https://theplugai.xyz/admin.html) (member roster + waitlist + CSV export) and [/app.html](https://theplugai.xyz/app.html) (sample-data preview). **Both are still the old vanilla-JS pages talking to Supabase directly** — known debt, not yet ported into the app.

---

## 🔧 Consoles & Dashboards *(new section — these were missing entirely)*

| What | Link |
|---|---|
| Supabase — **Forming Paws** | [dashboard](https://supabase.com/dashboard/project/wyzcnkdonbdykidmcxvx) · ref `wyzcnkdonbdykidmcxvx` |
| Supabase — **The Plug AI** | [dashboard](https://supabase.com/dashboard/project/fqdrvhpdntflfkqxlvkq) · ref `fqdrvhpdntflfkqxlvkq` (us-west-1) — **a separate project, don't mix them up** |
| Supabase → auth URL config | [URL Configuration](https://supabase.com/dashboard/project/wyzcnkdonbdykidmcxvx/auth/url-configuration) |
| Supabase → users | [Users](https://supabase.com/dashboard/project/wyzcnkdonbdykidmcxvx/auth/users) |
| Supabase → SQL editor | [SQL](https://supabase.com/dashboard/project/wyzcnkdonbdykidmcxvx/sql) |
| Vercel team | [vercel.com/cam6stef](https://vercel.com/cam6stef) |
| Vercel → forming-paws | [project](https://vercel.com/cam6stef/forming-paws) · [domains](https://vercel.com/cam6stef/forming-paws/settings/domains) |
| GitHub profile | [morrisstephon51](https://github.com/morrisstephon51) |
| Forming Paws pull requests | [PRs](https://github.com/morrisstephon51/forming-paws/pulls) |
| Domain registrar | GoDaddy — all `theplugai.*` and the other six domains |

**Supabase auth config, as set 2026-08-11:** Site URL `https://theplugai.xyz` · Redirect URLs `https://theplugai.xyz/**` and `http://localhost:3000/**`. The localhost entry is required for local dev signup now that Site URL points at production.

---

## ⚠️ Open problems

**`theplugai.online` — HTTPS still broken.** Unchanged since 2026-08-06. DNS is correct (GitHub Pages `185.199.108–111.153`), `http://` returns 200, `https://` fails TLS outright — no certificate issued. **Fix:** repo `command-center-redirect` → Settings → Pages → re-save the custom domain to retrigger issuance, then tick *Enforce HTTPS*. Until then don't share the `https://` form; it looks dead to anyone who clicks it.

**Leaked-password protection is off** in Supabase. One toggle, Authentication settings.

**`deploy-static-site.yml` is still on `forming-paws@main`.** Manual-trigger only and harmless — but it publishes the retired GitHub Pages site to a host nothing points at. Worth deleting to avoid confusion.

---

## 🗂️ Repos Without Live Sites

| Repo | Purpose | Notes |
|---|---|---|
| [obsidian-kai](https://github.com/morrisstephon51/obsidian-kai) | **This vault's live remote** (private) | ⭐ `origin` for `~/Desktop/kai`. Syncs only while Obsidian is open — not continuously |
| [kai-obsidian-vault](https://github.com/morrisstephon51/kai-obsidian-vault) | Original vault repo (private) | **Superseded** — last push 2026-07-05 |
| [ai-consulting-business](https://github.com/morrisstephon51/ai-consulting-business) | AI consulting business (private) | ✅ **Is** on GitHub — last push 2026-08-06. Previously logged as "not on GitHub at all" |
| [command-center-redirect](https://github.com/morrisstephon51/command-center-redirect) | Redirect shim for theplugai.online | Pushed 2026-08-11 |
| [mundi-world-state](https://github.com/morrisstephon51/mundi-world-state) | Git-based agent world state store | Replaces Vercel write quota usage |
| [aeos](https://github.com/morrisstephon51/aeos) | Aeos strategic-intelligence agent | Local: `~/clawd/agents/aeos-agent` |
| [job_opportunity_scanner](https://github.com/morrisstephon51/job_opportunity_scanner) | Job & opportunity scanner agent | Pushed 2026-08-07 |
| [Onsidian](https://github.com/morrisstephon51/Onsidian) | Notes repo | 2026-07-18 |
| [Enrollment_Funnel_Agent](https://github.com/morrisstephon51/Enrollment_Funnel_Agent) | Enrollment funnel agent | Dormant |
| [agent-II](https://github.com/morrisstephon51/agent-II) · [agent_I_content](https://github.com/morrisstephon51/agent_I_content) | Agent projects v1/v2 | Superseded by content-machine |
| [Stefan_portfolio](https://github.com/morrisstephon51/Stefan_portfolio) · [-portfolio](https://github.com/morrisstephon51/-portfolio) · [Link-in-bio](https://github.com/morrisstephon51/Link-in-bio) | Early iterations | Superseded |
| [skills-introduction-to-git](https://github.com/morrisstephon51/skills-introduction-to-git) | Learning repo | — |
| [----Workspace-notes-2025-01-07_notes.md](https://github.com/morrisstephon51/----Workspace-notes-2025-01-07_notes.md) | Stray notes repo | Not previously registered. Deletion candidate |

**Archived on GitHub (5):** `content-machine` (private) · `psychic-octo-engine` · `studious-umbrella` · `desktop-tutorial` (private) · `scrimba-workouts`.

**Not on GitHub at all:** `~/clawd/AI-Organization/` (governance doc set). Backed up nowhere but this machine.

---

## ☁️ Vercel Projects — team `cam6stef` (verified 2026-08-11)

| Project | Maps to | Verdict |
|---|---|---|
| `forming-paws` | **theplugai.xyz** | ⭐ Active — the real app |
| `psychic-bassoon` | theplugai.info | Active |
| `agent-world` | theplugai.live | Active |
| `stefan-portfolio` | theplugai.life | Active |
| `community-intake-routing` | community-intake-routing.vercel.app | **Live** — not dead weight, as previously recorded |
| `ai-video-reel-generator` | ai-video-reel-generator.vercel.app | **Live** — serves an "AI Content Engine" dashboard |
| `psychic-octo-engine` | psychic-octo-engine-psi.vercel.app | Live, but the repo is archived — inconsistent |
| `content-machine` | content-machine-wine.vercel.app | Live (legacy) |
| `content-machine-migh` | — | Only genuine dead weight. Deletion candidate |

Nine projects, one deletion candidate. The previous audit named two; one of those (`community-intake-routing`) is actually serving a live signup page.

---

## 🌐 Domain Registry

| Domain | Pointed To | Host | A record | Status |
|---|---|---|---|---|
| **theplugai.xyz** | **Forming Paws (the app)** | **Vercel** | `76.76.21.21` | ✅ Live — `www` also points here |
| theplugai.info | The Plug AI | Vercel | `76.76.21.21` | ✅ Live |
| theplugai.live | MUNDI Dashboard | Vercel | `76.76.21.21` | ✅ Live |
| theplugai.life | Stefan's Portfolio | Vercel | `76.76.21.21` | ✅ Live |
| theplugai.net | Link-in-Bio | GitHub Pages | `185.199.108–111.153` | ✅ Live |
| theplugai.online | Command Center redirect | GitHub Pages | `185.199.108–111.153` | ⚠️ HTTP 200, HTTPS fails |
| theplugai.world | Registrar parking | Parking service | `76.223.105.230` · `13.248.243.5` | 🔲 Parked (serves a placeholder) |
| theplugai.store | Registrar parking | Parking service | `3.33.130.190` · `15.197.148.33` | 🔲 Parked |
| zenat.us · usego.us · segaa.co.uk · fanuk.net · fanuk.uk | — | Parking service | `13.248.169.48` · `76.223.54.146` | 🔲 Parked |
| abebo.co.uk | — | Parking service | `76.223.105.230` · `13.248.243.5` | 🔲 Parked |

All eight unassigned domains resolve to registrar parking rather than nothing — they will serve a placeholder page to anyone who visits.

**Primary email:** founder@theplugai.info · full detail in [[09-SYSTEM/domains-and-email|Domains & Email]]

---

## 📋 Link Health — verified 2026-08-11

| Site | URL | Result |
|---|---|---|
| Forming Paws | theplugai.xyz | 🟢 200 (Vercel) |
| The Plug AI | theplugai.info | 🟢 200 |
| MUNDI Dashboard | theplugai.live | 🟢 200 |
| Stefan's Portfolio | theplugai.life | 🟢 200 |
| Link-in-Bio | theplugai.net | 🟢 200 |
| Command Center | theplugai.online | ⚠️ HTTP 200 · HTTPS fails |
| Community Intake | community-intake-routing.vercel.app | 🟢 200 |
| AI Content Engine | ai-video-reel-generator.vercel.app | 🟢 200 (via 307 → `/dashboard`) |
| Content Machine | content-machine-wine.vercel.app | 🟢 200 |
| Psychic Octo Engine | psychic-octo-engine-psi.vercel.app | 🟢 200 |
| Living Resume | github.io/Link-inbio/resume.html | 🟢 200 |
| Puppy Power (retired) | breeding-community-pets.deploypad.app | 🟢 200 (AmazonS3) |

**Next check: 2026-08-18.**

> **Do not treat these five as broken.** `obsidian-kai`, `kai-obsidian-vault`, `ai-consulting-business`, `content-machine`, and `mundi-agent-dashboard` are **private repos**. They return 404 to any request that is not signed in, so an automated link checker will flag them every time. Verified against `gh repo list` on 2026-08-11 — all five exist and all five are private.

---

## Corrections to the previous audit

Three entries from 2026-08-06 were **wrong**, not stale. Recording them so the same conclusions are not re-derived:

1. **`ai-video-reel-generator` was logged as a "307 redirect loop."** It is not a loop. The root 307s once to `/dashboard`, which returns 200 and serves a page titled "AI Content Engine." The earlier check followed the redirect but read the intermediate status as the final one.
2. **`community-intake-routing` was logged 🔴 404 / archived and marked a deletion candidate.** It returns 200 and serves "Join The Plug AI Community." Deleting it would have taken down a live signup page.
3. **`~/ai-consulting-business/` was logged "not on GitHub at all, zero commits."** The repo exists, is private, and was last pushed 2026-08-06.

Also corrected: `mundi-agent-dashboard` is **private**, and the vault remote `obsidian-kai` does **not** sync "every few minutes" — `git-obsi-sync` only commits while Obsidian is running.

---

## 📝 Quick Copy-Paste

```
Forming Paws (the app):  https://theplugai.xyz
The Plug AI:             https://theplugai.info
MUNDI Dashboard:         https://theplugai.live
Stefan's Portfolio:      https://theplugai.life
Link-in-Bio:             https://theplugai.net
Command Center:          http://theplugai.online   (https broken — use the github.io URL)
Command Center (alt):    https://morrisstephon51.github.io/Link-inbio/dashboard.html
Living Resume:           https://morrisstephon51.github.io/Link-inbio/resume.html
Community Intake:        https://community-intake-routing.vercel.app
AI Content Engine:       https://ai-video-reel-generator.vercel.app
Content Machine:         https://content-machine-wine.vercel.app
GitHub:                  https://github.com/morrisstephon51
Supabase:                https://supabase.com/dashboard/project/wyzcnkdonbdykidmcxvx
Vercel:                  https://vercel.com/cam6stef
```

**The one link to share with a dog owner:** `https://theplugai.xyz`

---

## 🔗 Related

- [[09-SYSTEM/Command Center|Command Center]] — full cross-linked hub
- [[link-health-checker|Link Health Checker]] — weekly verification checklist
- [[master-tracker|Master Tracker]]
- [[09-SYSTEM/domains-and-email|Domains & Email]] — full domain registry
- [[02-PROJECTS/Forming Paws/project-overview|Forming Paws]] · [[02-PROJECTS/Forming Paws/Status Log|Status Log]] · [[02-PROJECTS/Forming Paws/Roadmap — Deploy and Five Slices|Roadmap]]

---

*Last updated: 2026-08-11 — full live re-verification of every URL, redirect target, DNS record, GitHub repo, and Vercel project. Three prior entries corrected. Consoles section added.*
