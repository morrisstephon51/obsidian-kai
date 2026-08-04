---
created: 2026-07-23
type: system-reference
status: active
last-updated: 2026-08-03
---

# Agent Registry — Master Status Dashboard

**Authoritative registry of all AI agents, their status, configuration, and governance.** This doc owns supervisor *status* (healthy/broken); [[07-AI/MUNDI System Reference|MUNDI System Reference]] owns fleet *mechanics* (invoke commands, scheduling). Cross-check both when either changes — see 2026-08-03 correction below, which is exactly the kind of drift that happens when they aren't.

**2026-08-03 correction:** Orchestrator, Architect, Aexis, and Aeos were listed below as "✅ Active" since this doc's creation (2026-07-23) — that was never actually true. All 4 had been failing instantly on every invocation since they were written (2026-07-08/09) with `ANTHROPIC_API_KEY not set` (they called the raw Anthropic API directly; this system only has OAuth via the `claude` CLI, no pay-as-you-go API key) and had never once posted a successful result to the bus. Nobody had actually run them until tested today. Fixed by rewiring each to shell out to `claude -p` instead — verified live, all 4 now genuinely active. Lesson: "✅ Active" in this table means someone actually invoked it, not that it was configured correctly at creation — the monthly review below didn't catch this because a broken agent that's never run also generates no "hasn't run in 30 days" alert.

---

## 🟢 Active Supervisors (8 Total)

### Core Coordination

| Agent | Purpose | Status | Last Run | Output Location | Bus Name |
|---|---|---|---|---|---|
| **Kai (clawd)** | Command center, Telegram integration, always-on monitoring | ✅ Active | Continuous | `agents/clawd/state.md` | `clawd` |
| **Orchestrator** | Goal decomposition, task sequencing, dependency management | ✅ Active | On-demand | `agents/orchestrator/state.md` | `orchestrator` |
| **Architect** | System design, PRD development, solution architecture | ✅ Active | On-demand | `agents/architect/state.md` | `architect` |
| **Codex** | Code generation, PR creation, bug fixes, deployments | ✅ Active | On-demand | `agents/codex/state.md` | `codex` |

### Execution & Content

| Agent | Purpose | Status | Last Run | Output Location | Bus Name |
|---|---|---|---|---|---|
| **Antigravity** | LinkedIn content, strategy drafts, blog posts | ✅ Active | Daily | `agents/content-pipeline/state.md` | `antigravity` |
| **Perplexity** | Real-time research, fact-checking, citations | ✅ Active | On-demand | `agents/perplexity-agent/state.md` | `perplexity-agent` |
| **Aexis** | Stalled work detection, open loops, overdue tracking | ✅ Active | Weekly | `agents/aexis/state.md` | `aexis` |
| **Aeos** | Strategic briefing, grant landscape, intelligence synthesis | ✅ Active | Weekly | `agents/aeos/state.md` | `aeos` |

---

## 🟡 Specialized Agents (3 Total)

| Agent | Purpose | Status | Last Run | Integration | Bus Name |
|---|---|---|---|---|---|
| **Community Intake** | Church/nonprofit routing & categorization | ⏸️ On-hold | 2026-06-15 | BigHeart outreach | `community-intake` |
| **Enrollment Funnel** | BigHeart training intake automation | ⏸️ On-hold | 2026-06-20 | My Health My Power | `enrollment-funnel` |
| **Job Scanner** | ZipRecruiter MCP integration, job matching | ✅ Active | On-demand | `agents/job-scanner/state.md` | `job-scanner` |

---

## 📊 Supervisor Configuration

### Kai / clawd
```
Status: ✅ ACTIVE (always-on)
Type: Command center
Location: agents/clawd/
Last Updated: See state.md
Integration: Telegram (@morrisstephon51), Mundi, Vercel
Responsibilities:
  - Coordinate all agent work
  - Route Telegram messages to supervisors
  - Monitor system health
  - Feed updates to mundi/chatroom/feed.md
```

### Orchestrator
```
Status: ✅ ACTIVE
Type: Pipeline manager
Location: agents/orchestrator/
Trigger: On-demand (when Stefan says "break this down")
Responsibilities:
  - Decompose complex goals into tasks
  - Sequence work across agents
  - Identify dependencies
  - Route to specialized agents
```

### Architect
```
Status: ✅ ACTIVE
Type: System designer
Location: agents/architect/
Trigger: Design phase of projects
Responsibilities:
  - Full-mode design (Plug AI)
  - Lite-mode design (BigHeart)
  - PRD writing
  - Technical specifications
Output: 02-PROJECTS/ design documents
```

### Codex
```
Status: ✅ ACTIVE
Type: Code generator
Location: agents/codex/
Trigger: Implementation phase of projects
Responsibilities:
  - Write production code
  - Fix bugs with full tests
  - Create PRs
  - Deploy to staging/production
Output: GitHub repos (not vault-stored)
```

### Antigravity
```
Status: ✅ ACTIVE
Type: Content creator
Location: agents/content-pipeline/
Trigger: Daily content schedule
Responsibilities:
  - Generate LinkedIn posts
  - Draft strategy updates
  - Create marketing copy
  - Blog post ideation
Output: agents/content-pipeline/output/
```

### Perplexity
```
Status: ✅ ACTIVE
Type: Research agent
Location: agents/perplexity-agent/
Trigger: On-demand (research questions)
Responsibilities:
  - Real-time internet search
  - Fact verification
  - Citation gathering
  - Current events synthesis
Output: 06-OUTPUTS/, project-specific
```

### Aexis
```
Status: ✅ ACTIVE
Type: Accountability agent
Location: agents/aexis/
Trigger: Weekly (Friday EOD)
Responsibilities:
  - Find stalled projects
  - Identify open loops
  - Surface overdue work
  - Suggest next actions
Output: 01-DAILY/Weekly Reviews
```

### Aeos
```
Status: ✅ ACTIVE
Type: Intelligence agent
Location: agents/aeos/
Trigger: Weekly (Monday morning)
Responsibilities:
  - Synthesize weekly insights
  - Monitor grant landscape
  - Competitive intelligence
  - Strategic briefings
Output: 07-AI/morning-briefs/ (scheduled)
```

---

## 📋 Specialized Agent Status

### Community Intake
```
Status: ⏸️ ON-HOLD
Last Active: 2026-06-15
Reason: Awaiting Plug AI intake workflow finalization
Restart Condition: Post-2026-10-13, once Plug AI execution resumes and church partnership approach is redesigned independent of BigHeart (Vasser path lapsed 2026-07-29, not being chased)
Responsibilities: Route church inquiries to appropriate handler
```

### Enrollment Funnel
```
Status: ⏸️ ON-HOLD
Last Active: 2026-06-20
Reason: BigHeart My Health My Power project paused
Restart Condition: When BigHeart formally restarts training initiative
Responsibilities: Automate training intake & confirmation
```

### Job Scanner
```
Status: ✅ ACTIVE
Trigger: On-demand (when looking for opportunities)
Integration: ZipRecruiter MCP
Responsibilities: Find and score jobs matching skills/interests
Output: 06-OUTPUTS/job-search/
```

---

## 🔗 Integration Map

### Input Channels
- **Telegram:** @morrisstephon51 → Kai → Router → Supervisors
- **GitHub:** PR triggers → Codex automatic review
- **On-demand:** Stefan asks directly in Obsidian
- **Scheduled:** Cron jobs for daily/weekly agents

### Output Channels
- **Vault:** AI outputs → `07-AI/` or project folders
- **GitHub:** Code → repos (Codex)
- **Vercel:** Deployments (Codex → infrastructure)
- **Email:** Notifications (not yet configured)
- **Telegram:** Status updates (Kai → @morrisstephon51)

---

## 📊 Agent Governance

### Addition Protocol (New Agent)
1. Create `agents/<name>/` directory
2. Add `state.md` with configuration
3. Update this Registry
4. Document in [[index|07-AI Index]]
5. Link to appropriate supervisor if specialized

### Removal Protocol (Retire Agent)
1. Archive state to `agents/<name>-archived/`
2. Update status to "ARCHIVED"
3. Note date & reason
4. Update this Registry
5. Move to historical section

### Monthly Review
- **First Friday:** Review all agent states
- Check "Last Run" dates — archive if > 30 days dormant
- Update this Registry with any changes
- Report status to Stefan

---

## 🎯 Current Workstreams

### Track 1: The Plug AI (Primary)
**Active Agents:** Architect, Codex, Antigravity, Perplexity  
**Status:** Design + content phase  
**Next Milestone:** Illinois grant submission (FY2027)  

### Track 2: BigHeart (Instrumental)
**Active Agents:** Antigravity (content), Codex (tools)  
**Status:** Content automation live, training automation paused  
**Next Milestone:** Formal title change + compensation review  

### Track 3: Infrastructure & Learning
**Active Agents:** Perplexity, Aeos  
**Status:** Continuous improvement  
**Next Milestone:** Quarterly skills audit  

---

## 🚨 Alert System

**Red flags that trigger immediate review:**
- Agent hasn't run in 30 days (unless intentionally paused)
- Agent produces error output → goes to `feed.md`
- Dependency chain blocked (Orchestrator reports)
- Two agents produce conflicting outputs

---

## 📝 Configuration Template

**When adding a new agent, use this template:**

```yaml
---
name: [agent-name]
type: [supervisor|specialized]
status: [active|on-hold|archived]
created: [YYYY-MM-DD]
last-run: [YYYY-MM-DD]
last-updated: [YYYY-MM-DD]
bus-name: [hyphenated-name]
model: [claude-opus|claude-sonnet|etc]
token-budget: [null|number]
---

# [Agent Name]

## Purpose
[What does this agent do?]

## Responsibilities
- [Responsibility 1]
- [Responsibility 2]
- [Responsibility 3]

## Configuration
- **Trigger:** [How it's activated]
- **Frequency:** [Schedule or on-demand]
- **Output Location:** [Where results are saved]
- **Dependencies:** [Other agents/systems it needs]

## Integration
- **Input from:** [Which systems feed data]
- **Output to:** [Where results go]
- **Error handling:** [What happens if it fails]

## Recent Activity
- [Date]: [Brief summary]
- [Date]: [Brief summary]

## Notes
[Any special considerations]
```

---

## 🔄 Quick Reference: Run Commands

```bash
# Start any agent
cd ~/clawd/agents/<agent-name>
node run.js

# Check status
cat agents/<agent-name>/state.md

# View task feed
cat 07-AI/chatroom/feed.md

# Check recent errors
grep ERROR 07-AI/chatroom/feed.md | tail -10
```

---

## 📚 Related

- [[index|07-AI Index]] — Navigation hub
- [[Reference|Agent Reference]] — API docs
- [[../09-SYSTEM/CLAUDE.md|CLAUDE.md]] — Full system architecture
- [[../05-MAPS/Command Center|Command Center]] — Stefan's master dashboard

---

**Status:** ✅ COMPLETE & CURRENT  
**Last Updated:** 2026-08-03  
**Maintained By:** Claude Code + Kai  
**Review Schedule:** Monthly (first Friday)  

*This registry is the authoritative source for agent status, configuration, and governance.*
