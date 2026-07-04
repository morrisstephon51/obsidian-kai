---
type: hub
category: command-center
created: 2026-07-04
last-updated: 2026-07-04
---

# 🎛️ Command Center

**Single hub for every live site, repo, agent, and subagent across Stefan's systems.** This is the source of truth — the [public dashboard.html](https://morrisstephon51.github.io/Link-inbio/dashboard.html) and the [[project-agent-world|MUNDI Agent Dashboard]] both mirror what's here; update this page first, then propagate.

← [[05-MAPS/00 Home|Home]]

---

## 🚀 Live Websites & Apps

| Site | URL | Status | Notes |
|---|---|---|---|
| **The Plug AI** | [psychic-bassoon-psi.vercel.app](https://psychic-bassoon-psi.vercel.app) | 🟢 Live | Repo `psychic-bassoon`. The `-cam6stef` domain hits a Vercel SSO wall — use `-psi` for public sharing |
| **Stefan's Portfolio** | [stefan-portfolio-eight.vercel.app](https://stefan-portfolio-eight.vercel.app) | 🟢 Live | Repo `Stefan-Portfolio` |
| **Content Machine** | [content-machine-wine.vercel.app](https://content-machine-wine.vercel.app) | 🟡 Live but repo archived | GitHub repo `content-machine` archived 2026-07-03 — quality agents ported to `psychic-bassoon/content-engine`; deployment still up, treat as legacy |
| **AI Video Reel Generator** | [ai-video-reel-generator.vercel.app](https://ai-video-reel-generator.vercel.app) | 🟢 Live | Remotion-based |
| **Psychic Octo Engine** | [psychic-octo-engine-psi.vercel.app](https://psychic-octo-engine-psi.vercel.app) | 🟢 Live | Repo archived on GitHub but Vercel deployment still serving |
| **MUNDI Agent Dashboard** | [agent-world-olive.vercel.app](https://agent-world-olive.vercel.app) | 🟢 Live | Corrects prior "local only" assumption — it IS publicly deployed. Local dev: `~/Desktop/agent-dashboard`, `./start.sh` for tunnel |
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
| **gemini-agent** | 🟡 not-provisioned | Code ready at `~/clawd/agents/gemini-agent/run.js`. Needs `GEMINI_API_KEY` from aistudio.google.com/apikey (free tier) |
| **perplexity-agent** | 🟡 not-provisioned | Code ready at `~/clawd/agents/perplexity-agent/run.js`. Needs `PERPLEXITY_API_KEY` from perplexity.ai/settings/api (paid) |
| **MUNDI Router** | 🟢 built 2026-07-03 | `~/clawd/router/` — classifies tasks, routes to cheapest qualified agent among the above + chatgpt/groq/llama (those 3 are `not_provisioned` placeholders). Cooldown/probation failure-recovery state machine |

### Archived personas (audited 2026-07-03, zero real implementation)
`tools`, `job-scanner`, `community-intake`, `enrollment-funnel` — state files remain at `~/Desktop/kai/07-AI/agents/` marked `status: archived` for the record.

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

**Automation status:** local scheduling (launchd, `ai.mundi.fleet.plist`) is blocked on a macOS Full Disk Access grant — see [[project-agent-world]] for detail. Once granted, the periodic fleet-state refresh will also be the trigger point for refreshing this page's status table. Until then, treat this as manually maintained — ask Claude Code to re-run the audit + refresh whenever something changes.

---

## 🔗 Related
- [[_ops/important-links|Important Links Registry]]
- [[07-AI/Subagent Registry|Subagent Registry]]
- [[07-AI/MUNDI System Reference|MUNDI System Reference]]
- [[project-agent-world]]
- [[reference-agent-system]]
- [[09-SYSTEM/domains-and-email|Domains & Email]]
- [[05-MAPS/00 Home|Home]]

*Last updated: 2026-07-04*
