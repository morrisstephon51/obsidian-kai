---
type: reference
created: 2026-07-03
tags: [ai, agent-world, clawd]
---

# MUNDI System Reference

Full reference for the agent fleet, infrastructure, and websites built/audited/fixed across the 2026-07-03 session. Read this before touching any of it — several stale-path bugs existed here for weeks before being found (see Known Issues Fixed at the bottom).

---

## Websites & Deployments

> **Updated 2026-08-06.** This table was written 2026-07-03 and had gone stale in three places: custom domains now exist for everything, the MUNDI dashboard *does* have a fixed public URL, and Forming Paws was missing entirely. Canonical link registry is [[_ops/important-links|Important Links]] — check there first.

| Site | URL | Repo | Status |
|---|---|---|---|
| **The Plug AI** (live site) | https://theplugai.info | `psychic-bassoon` ([github](https://github.com/morrisstephon51/psychic-bassoon)) | Live, actively developed. Deploy branch: `claude/amazing-mccarthy-zZl3L`. **Never share the `-cam6stef` URL** — Vercel SSO wall |
| **Forming Paws** | https://theplugai.xyz | `forming-paws` ([github](https://github.com/morrisstephon51/forming-paws)) | Live static site on GitHub Pages (`gh-pages`). The full Next.js app on `main` runs **local-only** at `~/forming-paws` by design |
| **MUNDI Agent Dashboard** | https://theplugai.live (fallback `agent-world-olive.vercel.app`) | `mundi-agent-dashboard` ([github, private](https://github.com/morrisstephon51/mundi-agent-dashboard)) | **Fixed public URL since 2026-07-05** — no tunnel needed. Live agent data arrives via status-only Edge Config sync from Stefan's Mac every 5 min (`ai.mundi.sync.plist`). Local dev still `http://localhost:3131` |
| **Stefan's Portfolio** | https://theplugai.life (fallback `stefan-portfolio-eight.vercel.app`) | `Stefan-Portfolio` | Live |
| **Link-in-Bio / Command Center / Resume** | theplugai.net · theplugai.online · `/resume.html` | `Link-inbio`, `command-center-redirect` | GitHub Pages. ⚠️ **theplugai.online HTTPS is broken** — no cert issued |
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
| `gemini-agent` | keyed but blocked | `node ~/clawd/agents/gemini-agent/run.js "<task>"` | Key is set, but every call gets HTTP 429 with `limit: 0` on all free-tier quota metrics — confirmed via direct API test, the underlying Google Cloud project has zero free-tier quota. Needs a billing decision in Google Cloud Console, not new code |
| `perplexity-agent` | running | `node ~/clawd/agents/perplexity-agent/run.js "<task>"` | Fixed and verified 2026-07-04 — see Known Issues Fixed below |
| `tools` | archived | — | No implementation exists anywhere |
| `job-scanner` | archived | — | Real code exists but dormant/unwired: [job_opportunity_scanner](https://github.com/morrisstephon51/job_opportunity_scanner) |
| `community-intake` | archived | — | Real code exists but dormant/unwired: [-Community_intake_Routing](https://github.com/morrisstephon51/-Community_intake_Routing) |
| `enrollment-funnel` | archived | — | Real code exists but dormant/unwired: [Enrollment_Funnel_Agent](https://github.com/morrisstephon51/Enrollment_Funnel_Agent) — Track 2 (BigHeart) |
| `architect` | running (fixed 2026-08-03) | `node ~/clawd/agents/architect-agent/run.js "<task>" [--mode lite]` | AI-Organization "supervisor" — not in `run-agents.sh`. Was broken since creation (2026-07-08), see Known Issues Fixed below |
| `aexis` | running (fixed 2026-08-03) | `node ~/clawd/agents/aexis-agent/run.js "<task or audit>"` | Same as above |
| `aeos` | running (fixed 2026-08-03) | `node ~/clawd/agents/aeos-agent/run.js "<task or brief>"` | Same as above; delegates research to `perplexity-agent` internally |
| `orchestrator` | running (fixed 2026-08-03) | `node ~/clawd/agents/orchestrator-agent/run.js "<goal>"` | Same as above |

**Fleet scheduling:** resolved 2026-07-04 — Stefan granted Full Disk Access to `/bin/bash`, and the `launchd` job (`~/Library/LaunchAgents/ai.mundi.fleet.plist`) now fires `run-agents.sh` every 4h successfully (`launchctl list | grep mundi` shows last exit code 0). Manual run still available: `bash ~/Desktop/run-agents.sh`.

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

## Known Issues Fixed (2026-07-04)

- **`busctl.js` SQLite lock contention:** `DatabaseSync` had no busy-timeout, so concurrent writers (e.g. multiple agents posting around the same moment via the launchd fleet job) could collide — one gets an immediate `database is locked` error instead of waiting. This is what broke perplexity-agent's first real run. Root-caused by reproducing it on demand (8 concurrent writers → 3 failures at the exact file/line perplexity-agent's error pointed to), fixed with `PRAGMA journal_mode = WAL` + `PRAGMA busy_timeout = 5000` in `openDb()`, verified with a 20-concurrent-writer stress test (zero failures, `PRAGMA integrity_check` clean). Then re-ran perplexity-agent's actual queued task for real — completed end-to-end.
- **Gemini's 429 root-caused, not fixed (external):** direct API test shows `limit: 0` on every free-tier quota metric — the Google Cloud project behind the key has zero free-tier quota allocated, not a "too many requests" rate limit. This needs Stefan to enable billing on that project or issue a fresh key from a project that gets real free-tier quota — not a code fix.
- **`~/clawd` git-initialized:** the whole workspace had never been committed. Initialized and committed locally (root commit `f6ecd09`) — `.env`, `bus.sqlite` (mutable runtime state), and `router/dashboard.log` are gitignored; not yet pushed to a remote.

## Known Issues Fixed (2026-08-03)

- **Stale-OAuth-token pattern took down two independent systems the same day:** any long-lived process reading the Anthropic OAuth token from macOS Keychain once and holding it can end up using an expired snapshot (`401 OAuth access token has expired`), even though `claude auth status` shows a valid session moments later. Hit (1) the OpenClaw gateway's `claude-cli` runtime — fixed via `openclaw gateway restart`; and (2) the whole MUNDI fleet (clawd/codex/antigravity/content-pipeline) via `run-agents.sh`/`ai.mundi.fleet` — down for ~17h (06:12–22:56 UTC, 6 missed cycles) until a fresh token read + manual `bash ~/Desktop/run-agents.sh` catch-up run. `clawd`'s own loop-end self-diagnosed it as "STALL CONFIRMED."
- **`architect`/`aexis`/`aeos`/`orchestrator` (AI-Organization supervisors, `~/clawd/agents/*-agent/run.js`) never worked, since creation (2026-07-08/09):** each called the raw Anthropic Messages API directly with `x-api-key: $ANTHROPIC_API_KEY`, but this system has no pay-as-you-go Anthropic API key — Claude access here is OAuth-only via the `claude` CLI. Every invocation failed instantly with `ANTHROPIC_API_KEY not set` and silently — nothing ever posted to the bus until tested today, despite `AI-Organization/PHASE-2-BLOCKERS-DEPENDENCIES.md` marking the related blocker "resolved" weeks earlier without ever actually running them. Fixed by rewriting each `callClaude()` to shell out to `claude -p --model <model> --system-prompt <prompt> <userPrompt>` instead — same OAuth mechanism as `claude`/`antigravity` above, no new billing. Verified live: all 4 now post real (non-error) results to the bus.
- **`AI-Organization/antigravity-invoke.js` was a hardcoded stub** (`ANTIGRAVITY_READY = false`, fake `/usr/local/bin/antigravity` path) despite the doc set marking Antigravity's blocker "resolved." Rewired to post real `task-assigned` messages via `busctl.js`; verified live.
- **Duplicate/drifting agent-status registries:** [[07-AI/Agent Registry - Master Status|Agent Registry - Master Status]] had independently claimed all 4 broken supervisors above were "✅ Active" since 2026-07-23 — nobody had cross-checked it against reality. That doc remains the authoritative one for supervisor *status*; this file stays authoritative for fleet *mechanics* (invoke commands, scheduling, infra). Cross-check both when either changes — see the correction added to Agent Registry today.
