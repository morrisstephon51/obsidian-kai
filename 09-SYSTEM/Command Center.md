---
type: hub
category: command-center
created: 2026-07-04
last-updated: 2026-07-05
---

# 🎛️ Command Center

**Single hub for every live site, repo, agent, and subagent across Stefan's systems.** This is the source of truth — the [public dashboard.html](https://morrisstephon51.github.io/Link-inbio/dashboard.html) and the [[project-agent-world|MUNDI Agent Dashboard]] both mirror what's here; update this page first, then propagate.

← [[05-MAPS/00 Home|Home]]

---

## 🐾 Active Projects

| Project | Track | Stage | Notes |
|---|---|---|---|
| **The Plug AI** | Track 1 | Live, in development | See [[02-PROJECTS/The Plug AI/project-overview\|project overview]]. Repo `psychic-bassoon` |
| **BigHeart / Puppy Power** | Day job / Track 2 funding bridge | Active campaign | Docs at `~/clawd/puppy-power/` |
| **Forming Paws** | Track 2 | Phase 0+1 spec approved 2026-07-05, Phase 2 plan next | Health-first nonprofit dog-breeding matchmaking platform, $0 capital, Chicago IL launch. Repo `~/forming-paws` (local, not yet pushed to GitHub). Spec: `docs/superpowers/specs/2026-07-04-forming-paws-foundation-design.md` |

---

## 🚀 Live Websites & Apps

| Site | URL | Status | Notes |
|---|---|---|---|
| **The Plug AI** | [psychic-bassoon-psi.vercel.app](https://psychic-bassoon-psi.vercel.app) | 🟢 Live | Repo `psychic-bassoon`. The `-cam6stef` domain hits a Vercel SSO wall — use `-psi` for public sharing |
| **Stefan's Portfolio** | [stefan-portfolio-eight.vercel.app](https://stefan-portfolio-eight.vercel.app) | 🟢 Live | Repo `Stefan-Portfolio` |
| **Content Machine** | [content-machine-wine.vercel.app](https://content-machine-wine.vercel.app) | 🟡 Live but repo archived | GitHub repo `content-machine` archived 2026-07-03 — quality agents ported to `psychic-bassoon/content-engine`; deployment still up, treat as legacy |
| **AI Video Reel Generator** | [ai-video-reel-generator.vercel.app](https://ai-video-reel-generator.vercel.app) | 🟢 Live | Remotion-based |
| **Psychic Octo Engine** | [psychic-octo-engine-psi.vercel.app](https://psychic-octo-engine-psi.vercel.app) | 🟢 Live | Repo archived on GitHub but Vercel deployment still serving |
| **MUNDI Agent Dashboard (public URL)** | [agent-world-olive.vercel.app](https://agent-world-olive.vercel.app) | 🟢 Live, current build | Fixed 2026-07-05 — Vercel project's Root Directory (was `agent-world`, leftover from the old `studious-umbrella` repo) and Framework Preset (was `Other`) were reset to `.` / `Next.js`, then deployed directly from `~/Desktop/agent-dashboard` via `vercel --prod`. Now serves the current Next.js app with the Links panel, verified live |
| **Community Intake & Routing** | community-intake-routing.vercel.app | 🔴 Dead (404) | Confirms 2026-07-03 audit finding: archived, no real implementation |
| **Link-in-Bio** | [morrisstephon51.github.io/Link-inbio](https://morrisstephon51.github.io/Link-inbio/) | 🟢 Live | GitHub Pages, repo `Link-inbio` |
| **Command Center (public)** | [dashboard.html](https://morrisstephon51.github.io/Link-inbio/dashboard.html) | 🟢 Live | PIN-locked. Same repo as Link-in-Bio |
| **Living Resume** | [resume.html](https://morrisstephon51.github.io/Link-inbio/resume.html) | 🟢 Live | Same repo |

---

## 🐙 GitHub Repositories (morrisstephon51)

### Active
| Repo | Visibility | Purpose |
|---|---|---|
| [psychic-bassoon](https://github.com/morrisstephon51/psychic-bassoon) | Public | The Plug AI website — live |
| [kai-obsidian-vault](https://github.com/morrisstephon51/kai-obsidian-vault) | Private | This vault, git-synced via obsidian-git |
| [mundi-agent-dashboard](https://github.com/morrisstephon51/mundi-agent-dashboard) | Private | MUNDI Agent World dashboard source |
| [Link-inbio](https://github.com/morrisstephon51/Link-inbio) | Public | Link-in-bio + public Command Center (dashboard.html) |
| [Stefan-Portfolio](https://github.com/morrisstephon51/Stefan-Portfolio) | Public | Portfolio v2 — currently deployed |
| [ai-video-reel-generator](https://github.com/morrisstephon51/ai-video-reel-generator) | Public | Remotion video pipeline |
| [-Community_intake_Routing](https://github.com/morrisstephon51/-Community_intake_Routing) | Public | Repo exists; feature itself archived — no real implementation found |
| [Enrollment_Funnel_Agent](https://github.com/morrisstephon51/Enrollment_Funnel_Agent) | Public | BigHeart Track 2 — archived persona, repo still present |
| [job_opportunity_scanner](https://github.com/morrisstephon51/job_opportunity_scanner) | Public | Archived persona, repo still present |
| [agent_I_content](https://github.com/morrisstephon51/agent_I_content) | Public | First-gen content agent |
| [agent-II](https://github.com/morrisstephon51/agent-II) | Public | Next-gen agent, in development |
| [aeos](https://github.com/morrisstephon51/aeos) | Public | — |
| [Stefan_portfolio](https://github.com/morrisstephon51/Stefan_portfolio) | Public | Older portfolio (v1), superseded by Stefan-Portfolio |
| [-portfolio](https://github.com/morrisstephon51/-portfolio) | Public | Latest portfolio iteration |
| [Link-in-bio](https://github.com/morrisstephon51/Link-in-bio) | Public | Original link-in-bio (v1), superseded by Link-inbio |
| [skills-introduction-to-git](https://github.com/morrisstephon51/skills-introduction-to-git) | Public | Learning repo |
| [----Workspace-notes-2025-01-07_notes.md](https://github.com/morrisstephon51) | Public | — |

### Archived (2026-07-03 fleet audit — zero real implementation found)
`content-machine`, `desktop-tutorial`, `psychic-octo-engine` *(repo archived, Vercel deploy still live — inconsistent, worth reconciling)*, `scrimba-workouts`, `studious-umbrella`

---

## 🤖 Real Agent Fleet (verified, not just scaffolded)

Full detail: [[07-AI/MUNDI System Reference|MUNDI System Reference]] · [[project-agent-world]] · [[reference-agent-system]]

| Agent | Status | What it actually does |
|---|---|---|
| **clawd** / OpenClaw | 🟢 running | Always-on LaunchAgent, Telegram gateway, coordination hub. Doesn't schedule others — fleet is prompt-driven, not code-orchestrated |
| **codex** | 🟢 running | Per-task coding agent, ad hoc `claude -p` via `run-agents.sh` |
| **antigravity** | 🟢 running | Per-task general agent, same invocation pattern as codex |
| **content-pipeline** | 🟢 running | Real work lives in `psychic-bassoon/content-engine` |
| **gemini-agent** | 🔴 keyed but blocked | Key is provisioned, but every real call gets HTTP 429 with `limit: 0` on all free-tier quota metrics — the Google Cloud project behind the key has zero free-tier quota allocated. Needs a billing decision in Google Cloud Console, not a code fix |
| **perplexity-agent** | 🟢 running | Keyed and working — fixed 2026-07-04 (see below) |
| **MUNDI Router** | 🟢 built 2026-07-03 | `~/clawd/router/` — classifies tasks, routes to cheapest qualified agent among the above + chatgpt/groq/llama (those 3 are `not_provisioned` placeholders). Cooldown/probation failure-recovery state machine |

### Archived personas (audited 2026-07-03, zero real implementation)
`tools`, `job-scanner`, `community-intake`, `enrollment-funnel` — state files remain at `~/Desktop/kai/07-AI/agents/` marked `status: archived` for the record.

### Fixed 2026-07-04: shared bus lock contention
`busctl.js`'s SQLite connection had no busy-timeout, so concurrent writes from multiple agents (e.g. the launchd fleet job firing several at once) could collide with a `database is locked` error — this is what broke perplexity-agent's first real run. Fixed with `PRAGMA journal_mode = WAL` + `PRAGMA busy_timeout = 5000`; verified with a 20-concurrent-writer stress test (zero failures, DB integrity clean).

---

## 🗂️ 233-Subagent Registry

The full categorized list (marketing, engineering, GIS, sales, security, design, and 55 more categories) lives in its own page to keep this hub scannable:

**→ [[07-AI/Subagent Registry|Subagent Registry — all 233]]**

These are passive `.claude/agents/*.md` definitions, invoked directly or dispatched via MUNDI Router's keyword-tagging. Only the 7 primary agents above have a verified real invocation path — treat the 233 as an available menu, not a battle-tested roster.

---

## 🌐 Domains

Full detail: [[09-SYSTEM/domains-and-email|Domains & Email]]

- **The Plug AI:** theplugai.info (active, email here), .net, .world, .live, .store, .life, .online, .xyz
- **Other:** zenat.us, usego.us, segaa.co.uk, abebo.co.uk, fanuk.net, fanuk.uk
- **Primary email:** founder@theplugai.info

---

## 🔧 Infrastructure & Daily Tools

| Tool | Link | Purpose |
|---|---|---|
| GitHub | [github.com/morrisstephon51](https://github.com/morrisstephon51) | All repos |
| Vercel | [vercel.com/cam6stef](https://vercel.com/cam6stef) | Deployments (team: Stefan's projects) |
| Supabase | [dashboard](https://supabase.com/dashboard/project/fqdrvhpdntflfkqxlvkq) | DB — morrisstephon51's Project (us-west-1) |
| Anthropic Console | [console.anthropic.com](https://console.anthropic.com/) | API keys & usage |
| LinkedIn | [stephonmorris51](https://www.linkedin.com/in/stephonmorris51/) | Professional |

---

## 🔁 Keeping This Current

**Update cadence:** review after every agent-fleet audit, new deployment, or repo archive/creation — this page, the [[07-AI/Subagent Registry|Subagent Registry]], `_ops/important-links.md`, the public `dashboard.html`, and the MUNDI dashboard links panel should all move together.

**Automation status:** resolved 2026-07-04 — Stefan granted Full Disk Access to `/bin/bash`, and the `ai.mundi.fleet.plist` launchd job now fires `run-agents.sh` every 4 hours successfully (`launchctl list` shows last exit code 0). This page is still manually maintained, not auto-refreshed — ask Claude Code to re-run the audit whenever something changes.

---

## 🔗 Related
- [[_ops/important-links|Important Links Registry]]
- [[07-AI/Subagent Registry|Subagent Registry]]
- [[07-AI/MUNDI System Reference|MUNDI System Reference]]
- [[project-agent-world]]
- [[reference-agent-system]]
- [[09-SYSTEM/domains-and-email|Domains & Email]]
- [[02-PROJECTS/Forming Paws/project-overview|Forming Paws]]
- [[05-MAPS/00 Home|Home]]

*Last updated: 2026-07-05*
