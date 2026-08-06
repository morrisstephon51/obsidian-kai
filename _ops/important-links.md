---
type: operations
category: links-registry
created: 2026-06-13
last-checked: 2026-08-06
last-audit: 2026-08-06
---

# Important Links Registry

> For the full cross-linked hub see **[[09-SYSTEM/Command Center|Command Center]]**. This page is the quick-reference table for all live sites and repos.

**Every status below was verified live on 2026-08-06** (HTTP status + DNS resolution + page title), not carried over from the previous pass. Two things that were previously marked 🟢 are not actually healthy — see the ⚠️ rows.

---

## 🌐 All Sites — Master Table

| # | Name | Custom Domain | Fallback URL | GitHub Repo | Purpose | Status |
|---|---|---|---|---|---|---|
| 1 | **The Plug AI** | [theplugai.info](https://theplugai.info) | [psychic-bassoon-psi.vercel.app](https://psychic-bassoon-psi.vercel.app) | [psychic-bassoon](https://github.com/morrisstephon51/psychic-bassoon) | AI literacy platform | 🟢 Live |
| 2 | **MUNDI Agent Dashboard** | [theplugai.live](https://theplugai.live) | [agent-world-olive.vercel.app](https://agent-world-olive.vercel.app) | [mundi-agent-dashboard](https://github.com/morrisstephon51/mundi-agent-dashboard) | Agent fleet control panel | 🟢 Live |
| 3 | **Stefan's Portfolio** | [theplugai.life](https://theplugai.life) | [stefan-portfolio-eight.vercel.app](https://stefan-portfolio-eight.vercel.app) | [Stefan-Portfolio](https://github.com/morrisstephon51/Stefan-Portfolio) | Personal portfolio / resume | 🟢 Live |
| 4 | **Forming Paws** | [theplugai.xyz](https://theplugai.xyz) | [morrisstephon51.github.io/forming-paws](https://morrisstephon51.github.io/forming-paws/) | [forming-paws](https://github.com/morrisstephon51/forming-paws) | Dog-breeding matchmaking — public site + signup | 🟢 Live |
| 5 | **Link-in-Bio** | [theplugai.net](https://theplugai.net) | [morrisstephon51.github.io/Link-inbio](https://morrisstephon51.github.io/Link-inbio/) | [Link-inbio](https://github.com/morrisstephon51/Link-inbio) | Main link aggregator | 🟢 Live — DNS finished propagating |
| 6 | **Command Center (public)** | [theplugai.online](http://theplugai.online) | [morrisstephon51.github.io/Link-inbio/dashboard.html](https://morrisstephon51.github.io/Link-inbio/dashboard.html) | [command-center-redirect](https://github.com/morrisstephon51/command-center-redirect) | PIN-locked hub (apps, agents, links) | ⚠️ **HTTP only — HTTPS broken** |
| 7 | **Content Machine** | — | [content-machine-wine.vercel.app](https://content-machine-wine.vercel.app) | — (archived) | Content pipeline agent UI | 🟢 Live (legacy) |
| 8 | **AI Video Reel Generator** | — | [ai-video-reel-generator.vercel.app](https://ai-video-reel-generator.vercel.app) | [ai-video-reel-generator](https://github.com/morrisstephon51/ai-video-reel-generator) | Auto video reel builder | ⚠️ **307 redirect loop** |
| 9 | **Psychic Octo Engine** | — | [psychic-octo-engine-psi.vercel.app](https://psychic-octo-engine-psi.vercel.app) | [psychic-octo-engine](https://github.com/morrisstephon51/psychic-octo-engine) (archived) | Link-in-bio variant | 🟢 Live |
| 10 | **Living Resume** | — | [morrisstephon51.github.io/Link-inbio/resume.html](https://morrisstephon51.github.io/Link-inbio/resume.html) | [Link-inbio](https://github.com/morrisstephon51/Link-inbio) | Public resume page | 🟢 Live |
| 11 | **Puppy Power (old prototype)** | — | [breeding-community-pets.deploypad.app](https://breeding-community-pets.deploypad.app/) | — | Superseded by #4 | 🟡 Up but retired |
| 12 | **Community Intake & Routing** | — | community-intake-routing.vercel.app | [-Community_intake_Routing](https://github.com/morrisstephon51/-Community_intake_Routing) | Intake routing agent | 🔴 404 / archived |

### ⚠️ Two things that need a fix

**`theplugai.online` — HTTPS is broken.** DNS is correct (resolves to GitHub Pages `185.199.108–111.153`) and `http://theplugai.online` returns 200, but `https://` fails to establish TLS entirely. GitHub Pages has not issued a certificate for this domain. **Fix:** repo `command-center-redirect` → Settings → Pages → re-save the custom domain to retrigger cert issuance, then tick *Enforce HTTPS*. Until then, don't share the `https://` form of this link — it looks dead to anyone who clicks it.

**`ai-video-reel-generator.vercel.app` returns 307 and never lands.** Following redirects still ends on a 307 from `server: Vercel`, i.e. a redirect loop rather than a page. Previously logged as 🟢 Live because only the root was spot-checked. Needs a look at the project's redirect/middleware config.

---

## 🐾 Forming Paws — two different deployments, don't confuse them

| What | Where | Contains |
|---|---|---|
| **Public static site** | [theplugai.xyz](https://theplugai.xyz) (GitHub Pages, `gh-pages` branch) | Landing page + `/join.html` signup. This is the one to share. |
| **Vercel project `forming-paws`** | [forming-paws.vercel.app](https://forming-paws.vercel.app) | Serves the static landing only — `/browse` and `/join.html` both 404 there. Not the real app. |
| **The actual Next.js app** | `~/forming-paws` — **local only** | Owner accounts, dog profiles, health-doc verification, `/browse`, `/matches`. Migrations at 0018. Deliberately unhosted per the 2026-07-22 decision. |

The GitHub repo [forming-paws](https://github.com/morrisstephon51/forming-paws) is now **public and pushed** — the older note that it was "local, not yet pushed to GitHub" is obsolete.

---

## 🗂️ Repos Without Live Sites

| Repo | Purpose | Notes |
|---|---|---|
| [obsidian-kai](https://github.com/morrisstephon51/obsidian-kai) | **This vault's live remote** (private) | ⭐ Auto-syncs every few minutes via `git-obsi-sync`. This is `origin` for `~/Desktop/kai` |
| [kai-obsidian-vault](https://github.com/morrisstephon51/kai-obsidian-vault) | Original vault repo (private) | **Superseded** — last push 2026-07-05. The vault no longer points here |
| [command-center-redirect](https://github.com/morrisstephon51/command-center-redirect) | Redirect shim for theplugai.online | Created 2026-08-01 |
| [mundi-world-state](https://github.com/morrisstephon51/mundi-world-state) | Git-based agent world state store | Replaces Vercel write quota usage |
| [aeos](https://github.com/morrisstephon51/aeos) | Aeos strategic-intelligence agent | Local: `~/clawd/agents/aeos-agent` |
| [Onsidian](https://github.com/morrisstephon51/Onsidian) | Notes repo | Created 2026-07-18 |
| [Enrollment_Funnel_Agent](https://github.com/morrisstephon51/Enrollment_Funnel_Agent) | Enrollment funnel agent | Vault: `07-AI/agents/enrollment-funnel` — dormant |
| [job_opportunity_scanner](https://github.com/morrisstephon51/job_opportunity_scanner) | Job & opportunity scanner agent | Vault: `07-AI/agents/job-scanner` |
| [agent-II](https://github.com/morrisstephon51/agent-II) | Agent II project | — |
| [agent_I_content](https://github.com/morrisstephon51/agent_I_content) | Content pipeline agent (v1) | Superseded by content-machine |
| [Stefan_portfolio](https://github.com/morrisstephon51/Stefan_portfolio) | Portfolio v1 | Superseded by `Stefan-Portfolio` |
| [-portfolio](https://github.com/morrisstephon51/-portfolio) · [Link-in-bio](https://github.com/morrisstephon51/Link-in-bio) | Early iterations | Superseded |
| [skills-introduction-to-git](https://github.com/morrisstephon51/skills-introduction-to-git) | Learning repo | — |

**Archived on GitHub:** `content-machine`, `studious-umbrella`, `desktop-tutorial`, `psychic-octo-engine`, `scrimba-workouts`. Note `psychic-octo-engine`'s Vercel deploy is still serving despite the repo being archived — inconsistent, worth reconciling.

**Not on GitHub at all:** `~/ai-consulting-business/` (git-initialized, zero commits) and `~/clawd/AI-Organization/` (governance doc set). Neither is backed up anywhere but this machine.

---

## ☁️ Vercel Projects (team `cam6stef`, verified 2026-08-06)

`forming-paws` · `psychic-bassoon` · `agent-world` · `community-intake-routing` · `psychic-octo-engine` · `ai-video-reel-generator` · `stefan-portfolio` · `content-machine-migh` · `content-machine`

`community-intake-routing` and `content-machine-migh` are dead weight — no live site maps to either. Candidates for deletion.

---

## 🌐 Domain Registry

| Domain | Pointed To | Host | Status |
|---|---|---|---|
| theplugai.info | The Plug AI | Vercel (76.76.21.21) | ✅ Live |
| theplugai.live | MUNDI Dashboard | Vercel | ✅ Live |
| theplugai.life | Stefan's Portfolio | Vercel | ✅ Live |
| theplugai.xyz | **Forming Paws** | GitHub Pages | ✅ Live |
| theplugai.net | Link-in-Bio | GitHub Pages | ✅ Live |
| theplugai.online | Command Center redirect | GitHub Pages | ⚠️ HTTP 200, HTTPS fails (no cert) |
| theplugai.world | Registrar parking page | — | 🔲 Unassigned |
| theplugai.store | Registrar parking page | — | 🔲 Unassigned |
| zenat.us · usego.us · segaa.co.uk · abebo.co.uk · fanuk.net · fanuk.uk | — | — | 🔲 Unassigned |

**Primary email:** founder@theplugai.info · full detail in [[09-SYSTEM/domains-and-email|Domains & Email]]

---

## 📋 Link Health — Last Verified 2026-08-06

| Site | Domain | Result | Next Check |
|---|---|---|---|
| The Plug AI | theplugai.info | 🟢 200 | 2026-08-13 |
| MUNDI Dashboard | theplugai.live | 🟢 200 | 2026-08-13 |
| Stefan's Portfolio | theplugai.life | 🟢 200 | 2026-08-13 |
| Forming Paws | theplugai.xyz | 🟢 200 | 2026-08-13 |
| Link-in-Bio | theplugai.net | 🟢 200 | 2026-08-13 |
| Command Center | theplugai.online | ⚠️ HTTPS fails / HTTP 200 | **fix first** |
| Living Resume | github.io/Link-inbio/resume.html | 🟢 200 | 2026-08-13 |
| Content Machine | — | 🟢 200 | 2026-08-13 |
| AI Video Reel Generator | — | ⚠️ 307 loop | **fix first** |
| Psychic Octo Engine | — | 🟢 200 | 2026-08-13 |
| Community Intake & Routing | — | 🔴 404 | — |

---

## 📝 Quick Copy-Paste

```
The Plug AI:            https://theplugai.info
Forming Paws:           https://theplugai.xyz
MUNDI Dashboard:        https://theplugai.live
Stefan's Portfolio:     https://theplugai.life
Link-in-Bio:            https://theplugai.net
Command Center:         http://theplugai.online   (https broken - use the github.io URL below)
Command Center (alt):   https://morrisstephon51.github.io/Link-inbio/dashboard.html
Living Resume:          https://morrisstephon51.github.io/Link-inbio/resume.html
Content Machine:        https://content-machine-wine.vercel.app
GitHub:                 https://github.com/morrisstephon51
```

---

## 🔗 Related

- [[09-SYSTEM/Command Center|Command Center]] — full cross-linked hub
- [[link-health-checker|Link Health Checker]] — weekly verification checklist
- [[master-tracker|Master Tracker]]
- [[09-SYSTEM/domains-and-email|Domains & Email]] — full domain registry
- [[02-PROJECTS/Forming Paws/project-overview|Forming Paws]]

---

*Last updated: 2026-08-06 — full live re-verification of every URL, domain, repo, and Vercel project.*
