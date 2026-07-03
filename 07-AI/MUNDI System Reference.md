---
type: reference
created: 2026-07-03
tags: [ai, agent-world, clawd]
---

# MUNDI System Reference

Full reference for the agent fleet, infrastructure, and websites built/audited/fixed across the 2026-07-03 session. Read this before touching any of it — several stale-path bugs existed here for weeks before being found (see Known Issues Fixed at the bottom).

---

## Websites & Deployments

| Site | URL | Repo | Status |
|---|---|---|---|
| **The Plug AI** (live site) | https://psychic-bassoon-cam6stef.vercel.app | `psychic-bassoon` ([github](https://github.com/morrisstephon51/psychic-bassoon)) | Live, actively developed. Deploy branch: `claude/amazing-mccarthy-zZl3L` |
| **Stefan's Portfolio** | https://stefan-portfolio.vercel.app | `Stefan_portfolio` | Live, untouched this session |
| **MUNDI Agent Dashboard** | `http://localhost:3131` (local) + ephemeral Cloudflare tunnel | `mundi-agent-dashboard` ([github, private](https://github.com/morrisstephon51/mundi-agent-dashboard)) | No fixed public URL — run `./start.sh` for a temporary public link |
| ~~Content Machine~~ | — | `content-machine` (archived) | Retired 2026-07-03; its 8 quality-check agents were ported into `psychic-bassoon/content-engine` before archiving |

**Also archived this session** (dead tutorial repos, no live deployment): `psychic-octo-engine`, `studious-umbrella`, `scrimba-workouts`, `desktop-tutorial`. Reversible via `gh repo unarchive <name>`.

---

## Agent Fleet (MUNDI personas — `~/Desktop/kai/07-AI/agents/<name>/state.md`)

| Persona | Status | How to invoke | Notes |
|---|---|---|---|
| `clawd` | running | Always-on — Telegram bridge (LaunchAgent) | Coordination hub; does NOT dispatch other agents, purely a Telegram gateway |
| `codex` | running | `bash ~/Desktop/run-agents.sh` | Per-task coding agent, fires `claude -p` |
| `antigravity` | running | `bash ~/Desktop/run-agents.sh` | Per-task general agent |
| `content-pipeline` | running | `bash ~/Desktop/run-agents.sh` | Real logic lives in `psychic-bassoon/content-engine/server/agents/quality/` |
| `gemini-agent` | not-provisioned | `node ~/clawd/agents/gemini-agent/run.js "<task>"` | Needs `GEMINI_API_KEY` in `~/clawd/.env` — get one free at aistudio.google.com/apikey |
| `perplexity-agent` | not-provisioned | `node ~/clawd/agents/perplexity-agent/run.js "<task>"` | Needs `PERPLEXITY_API_KEY` in `~/clawd/.env` — perplexity.ai/settings/api (requires billing) |
| `tools` | archived | — | No implementation exists anywhere |
| `job-scanner` | archived | — | Real code exists but dormant/unwired: [job_opportunity_scanner](https://github.com/morrisstephon51/job_opportunity_scanner) |
| `community-intake` | archived | — | Real code exists but dormant/unwired: [-Community_intake_Routing](https://github.com/morrisstephon51/-Community_intake_Routing) |
| `enrollment-funnel` | archived | — | Real code exists but dormant/unwired: [Enrollment_Funnel_Agent](https://github.com/morrisstephon51/Enrollment_Funnel_Agent) — Track 2 (BigHeart) |

**Fleet scheduling:** a `launchd` job (`~/Library/LaunchAgents/ai.mundi.fleet.plist`, fires `run-agents.sh` every 4h) exists but is currently blocked on a macOS Full Disk Access grant. Until that's resolved, run the fleet manually: `bash ~/Desktop/run-agents.sh`.

---

## MUNDI Router (`~/clawd/router/`)

Cost-optimized task-routing CLI — classifies a task and dispatches it to the cheapest qualified agent, with automatic failure cooldown/recovery. Separate from the persona fleet above; does not touch the bus or any `state.md`.

```
node ~/clawd/router/run.js "<task text>"
```

| Provider | Registry status | Real today? |
|---|---|---|
| `claude` | provisioned | ✅ yes — `claude -p` |
| `antigravity` | provisioned | ✅ yes — `claude -p` (same mechanism as `claude`, kept as a distinct row per spec) |
| `gemini` | not-provisioned | reuses `gemini-agent/run.js` once keyed |
| `perplexity` | not-provisioned | reuses `perplexity-agent/run.js` once keyed |
| `chatgpt`, `groq`, `llama` | not-provisioned | placeholder only, no integration built yet |

State: `registry.json` (7 agents, cost/latency/success-rate/cooldown tracking), `subagents.json` (233 personas seeded from `~/.claude/agents/`), `dashboard.log` (escalation log).

---

## 233 Specialized Subagents

Full categorized roster already documented at [[07-AI/agency-agents|Agency Agents Roster]]. Two ways to use them:
- **Interactively in Claude Code:** "activate [agent-name] and help me with..."
- **Programmatically via MUNDI Router:** consulted by a primary agent (never the router directly) through `~/clawd/router/subagents.json`, matched by `capability_tags[]`

---

## Infrastructure Commands

| What | Command |
|---|---|
| Shared bus — post | `node ~/clawd/.bus/busctl.js post --from <agent> --topic <t> --msg "<text>"` |
| Shared bus — read unread | `node ~/clawd/.bus/busctl.js unread --agent <agent>` |
| Shared bus — status | `node ~/clawd/.bus/busctl.js status` |
| Run the whole fleet manually | `bash ~/Desktop/run-agents.sh` |
| Check the fleet's launchd job | `launchctl list \| grep mundi` |
| OpenClaw gateway status (Telegram bridge — unrelated to MUNDI Router despite the name) | `launchctl list \| grep openclaw`, logs at `~/Library/Logs/openclaw/gateway.log` |
| Dashboard, local only | `cd ~/Desktop/agent-dashboard && npm run dev` |
| Dashboard, with public tunnel | `cd ~/Desktop/agent-dashboard && ./start.sh` |
| Agent/repo audit sweep | Skill tool → `auditing-agents` |
| Check if a repo is archived on GitHub | `gh repo view <owner>/<repo> --json isArchived` |

---

## Known Issues Fixed (2026-07-03)

- **Stale path bug, machine-wide:** every persona's Loop Rules, `run-agents.sh`, and the dashboard's `lib/agents.ts` all pointed at `~/Desktop/kai/agent-world/`, which never existed (real path: `07-AI/`) — the dashboard had been silently showing zero agents for weeks.
- **`busctl.js` `KNOWN_AGENTS` gate:** hardcoded to 4 names, silently rejecting `content-pipeline` and any new agent's bus calls. Fixed to include all real personas.
- **YAML-corruption + shell-injection bugs** in the new `gemini-agent`/`perplexity-agent`/router scripts — found via deliberate testing, fixed, re-verified.
- **"Zero implementation" claim for job-scanner/community-intake/enrollment-funnel was wrong** — real code exists in GitHub repos that were never cloned locally. Corrected in each persona's state.md.
