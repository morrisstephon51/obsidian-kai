---
type: hub
created: 2026-07-11
---

# 🎯 Agent Fleet

8 supervisory agents coordinating The Plug AI and BigHeart Health work.

## Agent Directory

| Agent | Role | Bus Name | State |
|-------|------|----------|-------|
| **Kai / clawd** | Coordinating hub — always-on, Telegram-connected | `clawd` | [[../../09-SYSTEM/CLAUDE.md|CLAUDE.md]] |
| **Orchestrator** | Pipeline management — decomposes goals, sequences tasks | `orchestrator` | state.md |
| **Architect** | System design — Full mode (Plug AI) / Lite mode (BigHeart) | `architect` | state.md |
| **Codex** | Code generation, PRs, bug fixes | `codex` | state.md |
| **Antigravity** | Content, LinkedIn, strategy drafts | `antigravity` | state.md |
| **Perplexity** | Real-time research, citations | `perplexity-agent` | state.md |
| **Aexis** | Execution accountability, open loops, overdue follow-ups | `aexis` | state.md |
| **Aeos** | Strategic intelligence, synthesizes research into briefs | `aeos` | state.md |

## Agent State
Each agent maintains state in: `~/clawd/agents/<name>-agent/state.md`

## Communication
- Feed: `../chatroom/feed.md` — Cross-agent visibility
- Commands: Orchestrator dispatches via bus name

## Build Pipeline
Standard: `Orchestrator → Architect → Codex`

## Related
- [[../../09-SYSTEM/CLAUDE.md|System Instructions (CLAUDE.md)]]
- [[../../02-PROJECTS/Learning/Claude Code Guide|How to Work With Agents]]
