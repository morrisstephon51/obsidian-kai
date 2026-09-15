---
type: hub
created: 2026-07-11
---

# 🤖 AI Systems Hub

**AI-assisted automation, agent coordination, content generation, and intelligence infrastructure**

Master index for all AI-related work, agents, and generated outputs.

---

## 📊 Quick Navigation

| Category | Purpose | Files |
|---|---|---|
| **[[agents/index\|Agent Fleet]]** | 8 supervisor agents + command center | `agents/` |
| **[[Agent Registry - Master Status\|Agent Registry]]** | Master status & configuration | `Agent Registry - Master Status.md` |
| **[[Skills Inventory\|Skills Inventory]]** | 12 personal Claude Code skills, incl. `/ultimate` | `~/.claude/skills/` |
| **Content Pipeline** | LinkedIn posts, marketing outputs | `agents/content-pipeline/` |
| **Copilot Prompts** | Custom Claude prompts for this vault | `copilot-custom-prompts/` |
| **Chatroom Feed** | Real-time task router output | `chatroom/feed.md` |
| **Context & References** | World state, reference docs | `context/`, `Reference.md` |

---

## 🤖 The 8 Agent Supervisors

**Command Center:** [[agents/clawd/state|Kai (clawd)]] — Always-on coordinating hub  
**Orchestration:** [[agents/orchestrator/state|Orchestrator]] — Decomposes goals, sequences work  
**Design:** [[agents/architect/state|Architect]] — System & solution architecture  
**Build:** [[agents/codex/state|Codex]] — Code generation & PRs  
**Content:** [[agents/antigravity/state|Antigravity]] — LinkedIn, strategy, marketing  
**Research:** [[agents/perplexity-agent/state|Perplexity]] — Real-time research & citations  
**Accountability:** [[agents/aexis/state|Aexis]] — Open loops, overdue work tracking  
**Intelligence:** [[agents/aeos/state|Aeos]] — Strategic briefs & synthesis  

**Other Agents:** [[agents/community-intake/state|Community Intake]], [[agents/enrollment-funnel/state|Enrollment Funnel]], [[agents/job-scanner/state|Job Scanner]]

---

## 📁 Directory Structure

### `agents/`
- **`clawd/`** — Core command center (Telegram, Mundi integration)
- **`orchestrator/`** — Task decomposition and sequencing
- **`architect/`** — Design decisions, PRDs, system thinking
- **`codex/`** — Code generation, bug fixes, deployments
- **`antigravity/`** — Content creation, LinkedIn, strategy drafts
- **`perplexity-agent/`** — Research, fact-checking, current events
- **`aexis/`** — Stalled work, overdue reminders, blockers
- **`aeos/`** — Weekly briefs, grant landscape, competitive intel
- **`content-pipeline/`** — LinkedIn content generator (20+ outputs)
  - `state.md` — Pipeline configuration & status
  - `output/` — Generated posts (archived)
- **`community-intake/`** — Church/nonprofit routing system
- **`enrollment-funnel/`** — BigHeart training enrollment automation
- **`job-scanner/`** — ZipRecruiter MCP integration
- **`tools/`** — Shared utilities and base configurations

### `copilot-custom-prompts/`
Custom system prompts for Claude use in Obsidian/IDEs (13 files)

### `chatroom/`
- **`feed.md`** — Real-time output from Mundi task router

### `context/`
- **`world.md`** — Shared world state & context

### Root Files
- **`index.md`** — This file (navigation hub)
- **`Registry.md`** — Master agent registry & configuration
- **`Reference.md`** — API references, agent documentation
- **`agency-agents.md`** — Agent system design notes

---

## 🔄 How It Works

### Standard Pipeline
```
User Request
    ↓
Mundi (task router) → feed.md
    ↓
Orchestrator (decompose goal)
    ↓
[Architect → Codex] OR [Antigravity] OR [Perplexity] (parallel)
    ↓
Output → 02-PROJECTS/ or 06-OUTPUTS/
```

### Agent State Files
Each agent has a `state.md` file tracking:
- **Status:** Active / On Hold / Archived
- **Last Run:** When last invoked
- **Current Task:** What it's working on
- **Config:** API keys, model, parameters
- **Output:** Recent results or logs

See [[Agent Registry - Master Status|Agent Registry]] for master state dashboard.

---

## 📊 Generated Content Locations

| Agent | Outputs | Location |
|---|---|---|
| **Antigravity** | LinkedIn posts, blog drafts | `agents/content-pipeline/output/` |
| **Architect** | PRDs, system designs, briefs | `02-PROJECTS/`, `07-AI/context/` |
| **Codex** | PRs, code changes, deployments | GitHub repos, not stored in vault |
| **Perplexity** | Research reports, citations | `06-OUTPUTS/`, project-specific |
| **Aeos** | Weekly briefs, grant intel | `07-AI/morning-briefs/` (scheduled) |
| **All** | Task outputs | `07-AI/chatroom/feed.md` (real-time) |

---

## 🎯 Recent Activity

**Active agents (last 7 days):**
- Content Pipeline — 8 posts generated
- Clawd — Always-on monitoring
- Codex — 3 deployments
- Antigravity — Strategy updates

**On-hold agents:**
- Community Intake, Enrollment Funnel — Awaiting project restart
- Morning Briefs — Scheduled (not yet running)

---

## 🔗 Integration Points

**With 02-PROJECTS:**
- Agent outputs feed into project work
- Projects reference agent research (Perplexity)
- Codex handles all development on active projects

**With 01-DAILY:**
- Daily notes link to agent outputs
- Mundi task router creates daily action items

**With 06-OUTPUTS:**
- Final content published to OUTPUTS
- Antigravity drafts reviewed before final copy

**With _ops/:**
- Grant research (grant-research-log.md) ← Aeos & Perplexity
- Master tracker reflects agent priorities
- Important links updated by agent work

---

## 🚨 Governance Rules

1. **No silent failures:** If an agent errors, it goes to `feed.md` immediately
2. **Weekly sync:** All agent state files reviewed Friday EOD
3. **Active vs. Experimental:** Archive any agent not run in 30 days
4. **Output naming:** All generated content tagged with agent name
5. **Credential management:** All API keys in `agents/<name>/state.md` (git-ignored)

---

## 🛠️ For Developers

**Run an agent manually:**
```bash
cd ~/clawd/agents/<agent-name>
node run.js
```

**Check agent status:**
Read `agents/<agent-name>/state.md`

**Update Registry:**
Edit `Registry.md` when adding/removing agents

**View feed:**
Open `chatroom/feed.md` for real-time output

---

## 📚 Related

- [[02-PROJECTS/index|Active Projects]] — Where agent work lands
- [[../05-MAPS/Command Center|Command Center]] — Stefan's master dashboard
- [[../09-SYSTEM/CLAUDE.md|CLAUDE.md]] — Full agent system architecture
- [[Agent Registry - Master Status|Agent Registry]] — Master registry & configuration
- [[agents/index|Agents Hub]] — Detailed agent documentation

---

**Last Updated:** 2026-07-23  
**Status:** ✅ Active (8 supervisors + 3 specialized agents)  
**Coverage:** 62 files organized across agent fleet  
*This hub is the single source of truth for all AI system information.*
