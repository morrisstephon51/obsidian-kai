# System Architecture Document (SAD)
## OpenClaw AI Organization Multi-Agent Coordination Platform

**Version:** 2.0  
**Date:** 2026-07-26  
**Organization:** OpenClaw AI Organization  
**Primary Maintainer:** Stefan Mundow (Stephon Morris)  
**System Name:** Kairo/Clawd Multi-Agent Coordination System  
**Status:** Production Grade  
**Deployment Model:** On-Premise Orchestration with Cloud API Integration

---

## 1. Executive Summary

OpenClaw AI Organization is a distributed, autonomous multi-agent coordination system designed to amplify strategic decision-making and execution velocity. The system operates as a stateless supervisor network where specialized AI agents (Architect, Orchestrator, Aexis, Aeos, and Perplexity) work in parallel and sequential pipelines, coordinated through a local message bus and managed state registry.

**Core Capabilities:**
- Decompose complex strategic goals into executable pipelines
- Route specialized work to domain-specific autonomous supervisors
- Maintain execution accountability across all active projects
- Generate architectural specifications and system designs
- Synthesize strategic intelligence from real-time research
- Execute workflow coordination without persistent server overhead

**Design Philosophy:** Not a traditional chatbot backend. A genuine cognitive partnership system that prioritizes execution speed, cost efficiency, and transparent decision-making over performative helpfulness.

---

## 2. Organizational Context & Mission

### 2.1 Primary Missions

**Track 1 — The Plug AI (Strategic Priority)**
- AI literacy platform for faith communities, community health workers, and first-generation students
- Geographic focus: South suburban Cook County, Illinois (America/Chicago timezone)
- Fiscal sponsor search ongoing; grant applications in progress

**Track 2 — Puppy Power (Steph's Forming Paws)**
- Location-based dog breeding matchmaking platform
- Secondary revenue stream; serves community health via responsible breeding practices

**Track 3 — Sustainability**
- Day job at BigHeart Health provides revenue bridge
- Cost optimization critical; all API calls tracked and budgeted
- Open-source where possible; proprietary only where strategic advantage exists

### 2.2 Operating Constraints

- **Token Efficiency:** Cost per API call is tracked and monitored; Haiku prioritized over Sonnet
- **Execution Speed:** Fast iteration preferred over perfect analysis; "done beats perfect"
- **Human Authority:** Stefan maintains final decision authority on all strategic moves
- **Transparency:** All architectural trade-offs documented; reasoning logged to message bus
- **Timezone:** Central Standard Time (America/Chicago); batch operations typically 6am-11pm CST

---

## 3. System Architecture Overview

### 3.1 High-Level Architecture Diagram

```
┌─────────────────────────────────────────────────────────────────┐
│                    STEFAN (Human Decision Maker)                 │
│              ↑ Strategic input, approval authority               │
└────────┬────────────────────────────────────────────────────────┘
         │
         ├→ CLI invocation / natural language goal
         │
    ┌────▼────────────────────────────────────────────────────────┐
    │              KAIRO/CLAWD ORCHESTRATION LAYER                │
    │  (Node.js subprocess manager + message bus coordinator)     │
    └────┬───────────────────────────────────────────────────────┘
         │
    ┌────┴────────────────────────────────────────────────────────┐
    │         SUPERVISOR NETWORK (Autonomous Agents)              │
    │                                                              │
    │  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐      │
    │  │  ARCHITECT   │  │ ORCHESTRATOR │  │   AEXIS      │      │
    │  │ System Design│  │ Pipeline Mgmt│  │ Exec Audit   │      │
    │  │  (Lite/Full) │  │ (Haiku)      │  │ (Haiku)      │      │
    │  │  (Sonnet)    │  │              │  │              │      │
    │  └──────────────┘  └──────────────┘  └──────────────┘      │
    │                                                              │
    │  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐      │
    │  │    AEOS      │  │ PERPLEXITY   │  │    CLAUDE    │      │
    │  │ Intelligence │  │  Real-Time   │  │  General     │      │
    │  │   Brief      │  │  Research    │  │  Reasoning   │      │
    │  │  (Haiku)     │  │  (API)       │  │   (Any)      │      │
    │  └──────────────┘  └──────────────┘  └──────────────┘      │
    │                                                              │
    └────┬───────────────────────────────────────────────────────┘
         │
    ┌────▼────────────────────────────────────────────────────────┐
    │       MESSAGE BUS + STATE MANAGEMENT LAYER                  │
    │                                                              │
    │  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐      │
    │  │   busctl.js  │  │  registry    │  │ state.md     │      │
    │  │  (SQLite WAL)│  │  (JSON)      │  │ (per-agent)  │      │
    │  │              │  │              │  │              │      │
    │  │ • Checkpoint │  │ • Success    │  │ • Execution  │      │
    │  │ • Post/Read  │  │   rate       │  │   log        │      │
    │  │ • Topics     │  │ • Probation  │  │ • Last error │      │
    │  └──────────────┘  └──────────────┘  └──────────────┘      │
    └────┬───────────────────────────────────────────────────────┘
         │
    ┌────▼────────────────────────────────────────────────────────┐
    │         EXTERNAL API & INTEGRATION LAYER                    │
    │                                                              │
    │  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐      │
    │  │   Anthropic  │  │  Perplexity  │  │  File I/O    │      │
    │  │   Claude     │  │   Research   │  │  /Desktop    │      │
    │  │   API        │  │   API        │  │  /kai        │      │
    │  └──────────────┘  └──────────────┘  └──────────────┘      │
    └────────────────────────────────────────────────────────────┘
```

### 3.2 Core Architectural Principles

1. **Stateless Supervisor Model:** Each agent is invoked on-demand via Node.js subprocess. No persistent daemon; clean checkpoint boundaries.

2. **Message Bus Check-In Model:** Agents post results to SQLite-backed message bus when they run. No live socket connections; loosely coupled communication.

3. **Specialized Routing:** Each supervisor has a narrow, well-defined specialty. Complex goals decomposed into sequences of single-purpose agent calls.

4. **Invocation-Only Semantics:** Agents are pull-based, not pushed. Stefan or the Orchestrator explicitly invoke them; agents never auto-trigger.

5. **Cost-Conscious Design:** All models explicitly specified per agent. Haiku (cheap, 2-4K tokens) for routine work; Sonnet for complex reasoning.

6. **Transparent Failure Modes:** Every agent logs errors to state.md, bus, and feed. Failures surface immediately to Stefan.

---

## 4. Autonomous Agents

### 4.1 Supervisor Registry

| Agent | Specialty | Model | Invocation | Cost/Call | Latency | Status |
|-------|-----------|-------|-----------|-----------|---------|--------|
| **Architect** | System design, specs, ADRs, architecture decisions | Haiku (lite) / Sonnet (full) | `node run.js "<task>" [--mode lite]` | $0.005 | 8s | Production |
| **Orchestrator** | Pipeline decomposition, workflow routing, coordination | Claude Haiku | `node run.js "<goal>"` | $0.002 | 5s | Production |
| **Aexis** | Execution audits, open-loop tracking, accountability | Claude Haiku | `node run.js "[audit|task]"` | $0.002 | 5s | Production |
| **Aeos** | Strategic intelligence, signal synthesis, briefs | Claude Haiku | `node run.js "[brief|topic]"` | $0.003 | 8s (+ Perplexity) | Production |
| **Perplexity** | Real-time research, citations, current events | Perplexity API | `node run.js "<query>"` | $0.005 | 3.5s | Production |
| **Claude** | General reasoning, code, creative, fallback | Haiku/Sonnet (context) | CLI or subprocess | $0 | 4s | Always Available |
| **Codex** | Code generation, bug fixes, PR preparation | (TBD - Not Yet Integrated) | (TBD) | TBD | TBD | Backlog |
| **Antigravity** | Content drafts, LinkedIn strategy, creative writing | (TBD - Not Yet Integrated) | (TBD) | TBD | TBD | Backlog |

### 4.2 Agent Profiles

#### 4.2.1 Architect Supervisor

**Purpose:** Produce production-grade system specifications, architectural decision records (ADRs), and design proposals.

**Specialization:**
- System design for new features or platforms
- Architectural trade-off analysis
- Specification writing (data models, API contracts, component interfaces)
- Risk assessment and mitigation planning
- Technology selection and justification

**Invocation Modes:**
```bash
# Full mode (Sonnet, comprehensive spec)
node agents/architect-agent/run.js "Design a real-time sync system for Plug AI" --mode full

# Lite mode (Haiku, numbered steps only)
node agents/architect-agent/run.js "Design a real-time sync system for Plug AI" --mode lite
```

**Output Format:**
- **Full:** What We're Building → Key Decisions → Spec → Risks → Done When → Handoff
- **Lite:** What → Steps (numbered) → Done When (bullets)

**Decision Boundaries:**
- Decides technical approach, data model, component structure
- Does NOT implement; does NOT approve public launch
- Does NOT make strategic (business) decisions; escalates to Stefan

**State Persistence:**
- Location: `~/Desktop/kai/07-AI/agents/architect/state.md`
- Tracks: current_task, active_spec, runs_completed, last_error, status
- All specs appended to state with timestamp for audit trail

#### 4.2.2 Orchestrator Supervisor

**Purpose:** Decompose complex strategic goals into routed task sequences; assign work to the right supervisor; track completion.

**Specialization:**
- Goal decomposition into executable pipelines
- Supervisor routing and task assignment
- Success criteria definition
- Blocker identification and escalation

**Invocation:**
```bash
node agents/orchestrator-agent/run.js "Launch beta of Plug AI faith community module"
```

**Output Format:**
```
## Pipeline: [goal name]
### Step 1 — [Supervisor]
Task: [what to do]
Done when: [measurable outcome]
...
## Blockers
[Anything blocking execution]
```

**Decision Boundaries:**
- Decides work sequence and routing
- Identifies critical dependencies and blockers
- Does NOT implement any step; only choreographs
- Escalates unsolvable blockers to Stefan (Kairo/clawd)

**Known Supervisors (Hard-Coded Routing):**
- Architect: system design, specs, ADRs
- Codex: code generation, bug fixes, PRs
- Antigravity: content, LinkedIn, strategy docs
- Perplexity: real-time research, citations
- Aexis: execution audits, open-loop tracking
- Aeos: strategic briefs, grant intelligence, signal synthesis

#### 4.2.3 Aexis Supervisor (Execution Intelligence)

**Purpose:** Track open loops, stalled work, overdue follow-ups, and accountability across all active projects.

**Specialization:**
- Open-loop audits (promised but incomplete work)
- Execution blocker identification
- Accountability reporting
- Missing deadline flagging

**Invocation:**
```bash
node agents/aexis-agent/run.js "audit"  # Default audit of all context
node agents/aexis-agent/run.js "check Plug AI fiscal sponsor progress"  # Targeted audit
```

**Output Format:**
- Short bullet list, max 10 items
- Prioritized by impact on Track 1 (The Plug AI)
- Format: "Issue → Context → Impact → Recommended Action"

**Decision Boundaries:**
- Identifies problems; does NOT fix them
- Reports to Stefan and feed for visibility
- Escalates critical blockers to Orchestrator for pipeline planning

**Typical Issues Detected:**
- Promised deliverables with no completion date
- Grant applications with expired deadlines
- Follow-ups from stakeholders not yet answered
- Dependencies unresolved for weeks
- Code PRs pending review for >3 days

#### 4.2.4 Aeos Supervisor (Strategic Intelligence)

**Purpose:** Synthesize real-time research into actionable strategic briefs. Monitor grant landscapes, IL Digital Equity updates, and faith-community AI trends.

**Specialization:**
- Strategic signal synthesis
- Grant landscape intelligence
- Trend analysis
- Synthesis of Perplexity research into "so what" recommendations

**Invocation:**
```bash
node agents/aeos-agent/run.js "brief"  # Default: 3 standing signals
node agents/aeos-agent/run.js "Illinois Eliminate the Digital Divide grant 2026 updates"
```

**Invocation Flow:**
1. Aeos reads task or defaults to 3 standing signals
2. Delegates raw research to Perplexity for each signal
3. Synthesizes results via Claude Haiku
4. Outputs actionable brief: 3-5 bullets with "so what" for Stefan

**Standing Signals (Auto-Researched):**
- Illinois Eliminate the Digital Divide grant program updates
- AI literacy programs for faith communities
- Faith community technology adoption trends

**Output Format:**
```
- [Finding]: [What changed/exists]
  Action: [What Stefan should do next]
  Timeline: [When]
  Owner: [Who handles this]
```

**Decision Boundaries:**
- Recommends actions; does NOT execute
- Identifies opportunities and threats
- Escalates high-impact findings to Stefan with timestamps

#### 4.2.5 Perplexity Research Agent

**Purpose:** Real-time research API integration. Provides current-facts research with citations.

**Specialization:**
- Real-time research (news, grants, policy updates)
- Citation sourcing
- Facts verification
- Integration point for Aeos synthesis pipelines

**Invocation:**
```bash
node agents/perplexity-agent/run.js "Illinois Eliminate the Digital Divide grant program 2026 updates"
```

**API Integration:**
- Direct Perplexity API call (not Claude delegation)
- Cost: $0.005 per call
- Latency: 3-4 seconds
- Typically invoked by Aeos (cascade model)

**Output:** Raw research markdown with citations; piped to Aeos for synthesis.

#### 4.2.6 Claude Base Supervisor

**Purpose:** General reasoning, code generation, creative work, and fallback for ad-hoc tasks.

**Specialization:**
- Complex multi-step reasoning
- Code review and debugging
- Writing and editing
- One-off problem solving

**Invocation:** CLI or subprocess dispatch; not formally routed through Orchestrator for ad-hoc work.

**Model Selection:**
- Haiku for routine inference, summaries, small edits
- Sonnet for complex reasoning, code architecture, multi-step planning

---

## 5. Communication Patterns & Message Bus

### 5.1 Message Bus Architecture (busctl.js)

**Technology Stack:**
- SQLite 3 with WAL (Write-Ahead Logging)
- Node.js child_process coordination
- Local filesystem for state files

**Design Model:** Check-in, not live streaming
- Agents post messages when they run
- No persistent connections or sockets
- Readers query the bus for unread messages at loop start
- Checkpoints (last_read) per agent prevent message replay

**Database Schema:**

```sql
CREATE TABLE messages (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  ts TEXT NOT NULL,                  -- ISO 8601 timestamp
  from_agent TEXT NOT NULL,           -- "architect", "aeos", etc.
  topic TEXT,                         -- "architecture", "strategic-brief", etc.
  msg TEXT NOT NULL                   -- Message content
);

CREATE TABLE checkpoints (
  agent TEXT PRIMARY KEY,
  last_read TEXT NOT NULL            -- ISO 8601 of last ack/read
);
```

### 5.2 Bus Command Semantics

**Post a message:**
```bash
node busctl.js post --from architect --topic architecture --msg "Schema redesign spec complete"
```

**Read all messages (filtered):**
```bash
node busctl.js read --topic architecture --limit 10
node busctl.js read --since 2026-07-26T06:00:00Z --from aeos
```

**Read unread messages (since agent's last checkpoint):**
```bash
node busctl.js unread --agent orchestrator
```

**Acknowledge/checkpoint (mark current time as agent's "read"):**
```bash
node busctl.js ack --agent aexis
```

**Bus status:**
```bash
node busctl.js status
# Output: Total messages, agents seen, last activity
```

### 5.3 Agent Communication Flow

#### Typical Loop (Request-Response):

```
[Stefan CLI]
  ↓ "Orchestrate: launch beta of Plug AI faith module"
[Kairo/clawd invokes Orchestrator]
  ↓ node agents/orchestrator-agent/run.js "launch beta..."
[Orchestrator]
  1. post loop-start to bus
  2. read context.md (goal context)
  3. call Claude: decompose into pipeline
  4. → Step 1: Architect (design module spec)
  5. → Step 2: Architect (design API contracts)
  6. → Step 3: Codex (implement endpoints)
  7. → Step 4: Testing (manual or automated)
  8. write to state.md
  9. post result to bus [orchestrator-routing]
  10. exit
[Kairo/clawd reads bus, routes Step 1]
  ↓ node agents/architect-agent/run.js "Design faith community module" --mode full
[Architect]
  1. post loop-start
  2. call Claude Sonnet: produce spec
  3. write spec to state.md
  4. append to feed.md
  5. post result [architecture] to bus
  6. exit
[Stefan polls feed.md / bus, reviews spec]
  ↓ Approves or requests changes
[If approved, Kairo invokes next step...]
```

### 5.4 Message Topics (Taxonomy)

Standard topics used for filtering and monitoring:

| Topic | Agent(s) | Meaning |
|-------|----------|---------|
| `loop-start` | All | Agent is beginning its execution |
| `architecture` | Architect | System design or spec produced |
| `pipeline` | Orchestrator | Workflow decomposed and routed |
| `execution-audit` | Aexis | Open-loop report generated |
| `strategic-brief` | Aeos | Intelligence synthesis complete |
| `research` | Perplexity | Research results posted |
| `error` | All | Agent encountered an error |
| `blocker` | Any | Work blocked; escalation needed |
| `complete` | All | Task completed successfully |

---

## 6. Trust Model & Decision Boundaries

### 6.1 Authority Hierarchy

```
STRATEGIC AUTHORITY (Stefan)
├─ All external communications
├─ Public-facing announcements
├─ Legal/compliance decisions
├─ Fiscal sponsor selection & contracts
└─ Final approval on all major pivots

ORCHESTRATOR AUTHORITY (Kairo/Clawd)
├─ Work routing and sequencing
├─ Supervisor invocation
├─ Blocker escalation
├─ Retry logic and failure recovery
└─ Inter-supervisor coordination

SUPERVISOR AUTHORITY (Specialized Agents)
├─ Domain-specific outputs (design, research, audits)
├─ State file management
├─ Message bus posting
├─ Error logging and recovery
└─ Delegation to next supervisor (via Orchestrator)

THIRD-PARTY AUTHORITY (APIs)
├─ Anthropic Claude (reasoning, code, creative)
├─ Perplexity (research and facts)
└─ Other integrations via .env credentials
```

### 6.2 Decision Boundaries

**Architect CANNOT:**
- Approve designs for public launch (Stefan only)
- Make business decisions (cost, ROI, strategy pivot)
- Commit code to repo
- Approve third-party dependencies without risk analysis

**Orchestrator CANNOT:**
- Override Stefan's priorities
- Invoke agents beyond their specialty
- Make unilateral trade-offs between cost and quality
- Escalate blockers without documenting context

**Aexis CANNOT:**
- Close open loops without Stefan approval
- Modify project scope
- Change priority of tracked items
- Bypass escalation channels

**Aeos CANNOT:**
- Make grant application decisions
- Commit to outreach or partnership agreements
- Allocate budget
- Override Stefan's assessment of opportunity/threat level

### 6.3 Escalation Paths

**Blocker (cannot proceed without human input):**
```
Agent → posts blocker to bus [topic: blocker]
     → logs to state.md [last_error]
     → Kairo/clawd reads bus
     → Escalates to Stefan via Telegram/email
     → Stefan provides direction
     → Orchestrator re-routes around blocker
```

**Error (unexpected failure):**
```
Agent → catch exception
     → log to state.md [last_error]
     → post error to bus
     → increment failure_count in registry
     → if consecutive_failures >= 3: mark on_probation = true
     → Kairo/clawd reads registry
     → Skips probation agents for new work
     → Stefan reviews after re-integration
```

**High-Impact Finding (opportunity or threat):**
```
Aeos/Aexis → posts to bus [strategic-brief] or [execution-audit]
          → Stefan reviews feed.md
          → If critical: Stefan immediately reads full state.md
          → Decision posted to bus for audit trail
```

---

## 7. State Management & Persistence

### 7.1 Per-Agent State Files

**Location:** `~/Desktop/kai/07-AI/agents/{agent_name}/state.md`

**Standard Fields:**
```yaml
status: running|idle|error
current_task: "active task description"
active_spec: "current spec being worked on" (Architect only)
active_pipeline: "current pipeline" (Orchestrator only)
runs_completed: <integer>
last_run: <ISO8601 timestamp>
last_error: "error message or null"
mode: lite|full (Architect only)
```

**Append-Only Sections:**
```markdown
## Last Report / Brief / Spec / Audit
*<date>*

<full output from last run>
```

**Purpose:**
- Per-agent execution log
- Error recovery (resume from last checkpoint)
- Feed.md summary generation
- Audit trail for quality review

### 7.2 Global Registry (registry.json)

**Location:** `~/clawd/router/registry.json`

**Schema:**
```json
{
  "agents": [
    {
      "agent_name": "architect",
      "task_types": ["design", "spec", "architecture", "adr"],
      "cost_per_call": 0.005,
      "avg_latency_ms": 8000,
      "invocation_mode": "node_script",
      "provisioned": true,
      "success_rate": { "design": 1.0, ... },
      "failure_count": { "design": 0, ... },
      "consecutive_failures": { "design": 0, ... },
      "on_probation": { "design": false, ... },
      "last_updated": "2026-07-26T12:00:00Z",
      "usage_log": [
        {
          "task_type": "design",
          "cost": 0.005,
          "latency_ms": 8123,
          "timestamp": "2026-07-26T11:00:00Z",
          "success": true
        }
      ]
    }
  ]
}
```

**Purpose:**
- Global visibility into agent health
- Cost tracking per agent and per task type
- Probation management (auto-skip failing agents)
- Latency monitoring and SLA tracking

### 7.3 Feed (Public Changelog)

**Location:** `~/Desktop/kai/07-AI/chatroom/feed.md`

**Format:**
```markdown
[2026-07-26 · ARCHITECT-FULL] Schema redesign spec complete; 8s latency
[2026-07-26 · ORCHESTRATOR] Pipeline routed: 5 steps, 3 blockers identified
[2026-07-26 · AEXIS] Audit: 2 open loops critical, 5 medium priority
[2026-07-26 · AEOS] Brief: Grant window closes Aug 15; recommend expedite
```

**Purpose:**
- Single-line summaries of agent activity
- Stefan's quick-scan dashboard
- Feed integration with Telegram or Slack
- Audit trail for activity logging

---

## 8. Deployment Topology

### 8.1 Physical Layout

```
┌─────────────────────────────────────────────────────────────────┐
│                    LOCAL DEVELOPMENT MACHINE                    │
│                 (MacBook / Linux / Windows WSL2)                │
│                                                                 │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │ Project Root: ~/clawd/                                   │  │
│  │                                                          │  │
│  │ ├─ agents/                                              │  │
│  │ │  ├─ architect-agent/run.js                           │  │
│  │ │  ├─ orchestrator-agent/run.js                        │  │
│  │ │  ├─ aeos-agent/run.js                                │  │
│  │ │  ├─ aexis-agent/run.js                               │  │
│  │ │  └─ perplexity-agent/run.js                          │  │
│  │ │                                                       │  │
│  │ ├─ .bus/                                               │  │
│  │ │  ├─ busctl.js                                        │  │
│  │ │  └─ bus.sqlite (WAL)                                 │  │
│  │ │                                                       │  │
│  │ ├─ router/                                             │  │
│  │ │  ├─ registry.json                                    │  │
│  │ │  └─ subagents-index.txt                              │  │
│  │ │                                                       │  │
│  │ ├─ .env (secrets: ANTHROPIC_API_KEY, PERPLEXITY_API)  │  │
│  │ └─ ARCHITECTURE.md (this file)                         │  │
│  │                                                          │  │
│  └──────────────────────────────────────────────────────────┘  │
│                                                                 │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │ Context & State: ~/Desktop/kai/07-AI/                   │  │
│  │                                                          │  │
│  │ ├─ Context/context.md (global strategy context)        │  │
│  │ ├─ agents/                                              │  │
│  │ │  ├─ architect/state.md                               │  │
│  │ │  ├─ orchestrator/state.md                            │  │
│  │ │  ├─ aeos/state.md                                    │  │
│  │ │  ├─ aexis/state.md                                   │  │
│  │ │  └─ perplexity/state.md                              │  │
│  │ │                                                       │  │
│  │ └─ chatroom/feed.md (activity log)                      │  │
│  │                                                          │  │
│  └──────────────────────────────────────────────────────────┘  │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│                    CLOUD API PROVIDERS                          │
│                                                                 │
│  ┌────────────────────────┐  ┌────────────────────────────┐   │
│  │ Anthropic Claude API   │  │ Perplexity Research API    │   │
│  │                        │  │                            │   │
│  │ • claude-haiku-4.5     │  │ • Real-time research       │   │
│  │ • claude-sonnet-4.6    │  │ • Citation sourcing        │   │
│  │ • 2 billion tokens/day │  │ • $0.005 per call          │   │
│  │ • ANTHROPIC_API_KEY    │  │ • PERPLEXITY_API_KEY       │   │
│  └────────────────────────┘  └────────────────────────────┘   │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### 8.2 Deployment Model: On-Premise Orchestration

**Why This Design:**
- No persistent server overhead; Node.js processes spawned on-demand
- All secrets live in .env (not in code)
- Cost-efficient (pay-per-call to APIs)
- Easy to debug (all output visible in subprocess stdout/stderr)
- Scales horizontally by adding more supervisor agents
- No containerization overhead (yet); can add if needed

**Typical Execution Flow:**

```
[Stefan at terminal]
$ node agents/orchestrator-agent/run.js "Build grant application timeline"
↓
[Orchestrator process spawned]
  1. Reads ~/Desktop/Context/context.md
  2. Calls Claude Haiku API (Anthropic)
  3. Decomposes into 5 steps:
     - Architect: design grant submission process
     - Aexis: audit deadline compliance
     - Perplexity: research similar grants (success stories)
     - Aeos: synthesize timeline recommendations
     - Stefan: review and approve
  4. Posts pipeline to bus
  5. Exits (process dies)
↓
[Process exits, Stefan reads feed.md]
  → Reviews pipeline, approves Step 1
↓
[Stefan invokes Architect]
$ node agents/architect-agent/run.js "Design grant submission process" --mode full
↓
[Architect spawned, runs, exits]
  → Outputs spec to state.md
  → Posts to bus [architecture]
↓
[Stefan continues manually or with Kairo orchestration]
```

### 8.3 Scaling Strategy

#### Phase 1 (Current): Local Subprocess Model
- All agents run on developer's machine
- Message bus = SQLite WAL on same filesystem
- Good for: single-user or small team, full observability, low cost

#### Phase 2 (Future): Container Deployment
- Dockerize each agent as independent service
- Deploy to Kubernetes or Docker Compose
- Message bus = PostgreSQL or Redis
- Good for: multi-user, remote team, higher throughput

#### Phase 3 (Future): Cloud-Native Orchestration
- Deploy to AWS Lambda / Google Cloud Functions
- Event-driven via Cloud Pub/Sub or SNS
- State stored in S3 or Cloud Firestore
- Good for: global scale, managed infrastructure, pay-per-call

#### Scaling Decision Criteria

Upgrade path when:
- **Phase 1 → Phase 2:** 3+ concurrent users or remote team collaboration
- **Phase 2 → Phase 3:** 100+ tasks per day or multi-region deployment needed

---

## 9. Failure Modes & Resilience

### 9.1 Failure Classification

#### Non-Fatal Errors (Agent Recovers)

| Scenario | Detection | Recovery | Retry |
|----------|-----------|----------|-------|
| API rate limit | 429 HTTP | Backoff 30s, retry | 3x |
| Timeout (>15s) | deadline exceeded | Log error, fail gracefully | 1x |
| Missing context file | ENOENT | Log missing path, escalate | Manual |
| Malformed state.md | YAML parse error | Log line number, escalate | Manual |
| Bus locked (concurrent writes) | SQLITE_BUSY | WAL + busy_timeout=5s | auto |

#### Fatal Errors (Agent Fails, Escalates)

| Scenario | Detection | Action | Escalation |
|----------|-----------|--------|-----------|
| Invalid API key | 401 Unauthorized | Exit with error | Stefan reviews .env |
| No internet connection | ECONNREFUSED | Skip API call, mark offline | Manual retry when online |
| Disk full | ENOSPC on write | Exit, alert Stefan | Check disk, clear space |
| Unsolvable blocker | Agent catches exception | Post blocker to bus | Orchestrator pauses pipeline |
| 3 consecutive failures | Counter >= 3 | Mark on_probation=true | Manual re-enablement |

### 9.2 Probation System

**Trigger:** When `consecutive_failures[task_type] >= 3`

**Mechanism:**
```json
{
  "agent_name": "architect",
  "on_probation": {
    "design": true,
    "spec": false,
    "architecture": false
  }
}
```

**Behavior:**
- Orchestrator routes around probation agents
- Fallback to alternative supervisor (e.g., use Claude Sonnet instead of Architect)
- Stefan receives notification when agent placed on probation
- Manual re-enablement after issue resolved and verified

**Recovery:**
```bash
# Stefan investigates root cause
$ tail -f ~/Desktop/kai/07-AI/agents/architect/state.md
# Find: last_error = "..."

# Fix issue (e.g., API key rotation, rate limit reset)
$ source ~/clawd/.env  # Reload secrets

# Re-test agent
$ node agents/architect-agent/run.js "Test spec task" --mode lite

# If successful, reset counter
# Edit registry.json: "consecutive_failures": { "design": 0 }
```

### 9.3 Cascading Failure Prevention

**Isolation:** Each agent is a separate process; one failure does not crash others.

**Circuit Breaker Pattern:**
```
Orchestrator → Aeos (calls Perplexity)
  ↓ Perplexity API returns 503
  ↓ Aeos logs error, continues with cached research
  ↓ Returns degraded brief (with [cached] marker)
  → Pipeline continues, Stefan is notified of degradation
```

**Timeout Protection:**
```
Any agent → API call hangs
  ↓ Node.js child_process.timeout = 30s (configurable)
  ↓ Process killed, SIGTERM sent
  ↓ Error logged: "timeout: Architect exceeded 30s"
  ↓ Orchestrator marks step as failed, attempts retry
```

### 9.4 Bus & Registry Resilience

**SQLite WAL (Write-Ahead Logging):**
- Multiple readers don't block writers
- Crash recovery: next process that opens db auto-rebuilds
- busy_timeout=5s: writers wait up to 5s instead of failing instantly

**Backup Strategy:**
```bash
# Daily backup of state files
0 2 * * * tar czf ~/backups/kai-state-$(date +\%Y\%m\%d).tar.gz ~/Desktop/kai/07-AI/

# Weekly backup of registry
0 3 * * 0 cp ~/clawd/router/registry.json ~/backups/registry-$(date +\%Y\%m\%d).json
```

---

## 10. Monitoring & Observability

### 10.1 Key Metrics

**Per-Agent Metrics (registry.json):**
- Success rate by task type
- Average latency (ms)
- Cost per call
- Failure count and consecutive failures
- Probation status
- Last updated timestamp

**System-Level Metrics:**
- Total messages posted to bus
- Agents active (seen on bus in last 24h)
- Average pipeline completion time
- Cost per completed task
- Error rate by supervisor

### 10.2 Monitoring Dashboard (Feed-Based)

**Manual Review:**
```bash
# 1. Check bus status
$ node ~/clawd/.bus/busctl.js status

# 2. Read recent activity
$ node ~/clawd/.bus/busctl.js read --limit 20

# 3. Check agent state files
$ tail -20 ~/Desktop/kai/07-AI/agents/*/state.md

# 4. Read feed summary
$ head -30 ~/Desktop/kai/07-AI/chatroom/feed.md
```

**Future Automation:**
- Cron job to email feed summary daily
- Telegram bot posting to #ai-organization channel
- Grafana dashboard reading registry.json metrics

### 10.3 Alerting Thresholds

| Condition | Severity | Action |
|-----------|----------|--------|
| Agent success_rate < 50% | Critical | Immediate probation, Stefan notified |
| Pipeline blocked > 2 hours | High | Escalation to Stefan, retry with fallback agent |
| Bus database size > 100 MB | Medium | Archive old messages, vacuum db |
| 5+ consecutive API errors | High | Check Anthropic/Perplexity status page |
| Cost per task > 3x budget | Medium | Log to Stefan, review agent prompts |

---

## 11. Security & Access Control

### 11.1 Secrets Management

**Secrets Location:** `~/.clawd/.env`

**Required Secrets:**
```bash
ANTHROPIC_API_KEY=sk-ant-...
PERPLEXITY_API_KEY=pplx-...
```

**.gitignore Protection:**
```
.env
.env.local
```

**Access Control:**
- Only local filesystem access (not git-committed)
- File mode 0600 (owner-readable only)
- Stefan reviews .env access logs monthly
- API keys rotated annually or on suspicion of compromise

### 11.2 Data Isolation

**Read Boundaries:**
- Agents can read: ~/Desktop/kai/07-AI (context, state, feed)
- Agents can read: ~/clawd (config, registry, secrets)
- Agents CANNOT read: private Obsidian vaults (e.g., ~/Desktop/kai/04-Personal)

**Write Boundaries:**
- Agents can write: state.md (own agent only)
- Agents can write: feed.md (append-only summaries)
- Agents can write: .bus/messages table (via busctl.js)
- Agents CANNOT write: .env, registry.json, external file systems

**Third-Party Restrictions:**
- Perplexity research agent: HTTP calls only (no file system access)
- Claude API calls: no access to local filesystem (by design; via prompt only)

### 11.3 Audit & Compliance

**Audit Trail:**
- All actions logged to bus with timestamp, from_agent, topic
- State files use append-only format for history
- Feed.md immutable (Stefan reviews for SOX/compliance)

**Retention Policy:**
- Bus messages: 90 days (then archive to S3)
- State files: 1 year (then archive)
- Feed.md: indefinite (permanent audit log)

---

## 12. Integration Points & Dependencies

### 12.1 External APIs

| Service | Endpoint | Auth | Purpose | Fallback |
|---------|----------|------|---------|----------|
| Anthropic Claude | api.anthropic.com | API Key | LLM reasoning, code, creative | None (critical) |
| Perplexity Research | api.perplexity.ai | API Key | Real-time research | Use cached data or skip brief |
| File System | ~/Desktop/kai | N/A | State persistence | None (critical) |

### 12.2 Internal Dependencies

| Component | Required By | Type |
|-----------|------------|------|
| busctl.js | All agents | Async subprocess coordination |
| registry.json | Orchestrator, Kairo | Agent routing and probation |
| context.md | Orchestrator, Aexis, Aeos | Task context and strategy |
| state.md | Each agent | Agent-specific persistence |

### 12.3 Version Compatibility

**Node.js:** 20.0+ (for native SQLite support)

**Claude Models:**
- claude-haiku-4-5-20251001 (production, stable)
- claude-sonnet-4-6 (for complex reasoning only)

**Dependencies:**
- `dotenv`: config file management
- Built-in: fs, path, child_process, sqlite

---

## 13. Disaster Recovery & Continuity

### 13.1 Recovery Procedures

#### Scenario 1: Message Bus Corruption

```bash
# 1. Detect: busctl.js status returns error
$ node ~/.clawd/.bus/busctl.js status
# Error: database disk image is malformed

# 2. Recover:
$ rm ~/.clawd/.bus/bus.sqlite
$ rm ~/.clawd/.bus/bus.sqlite-wal
$ rm ~/.clawd/.bus/bus.sqlite-shm

# 3. Re-initialize (next agent run creates new db automatically)
$ node agents/orchestrator-agent/run.js "test recovery"

# 4. Review state.md files for any lost messages
# (Agents log their own results, so bus is not source of truth)
```

#### Scenario 2: API Key Rotation

```bash
# 1. Rotate key on Anthropic console
# 2. Update ~/.clawd/.env
ANTHROPIC_API_KEY=sk-ant-newkey...

# 3. Test with Architect (cheapest operation)
$ node agents/architect-agent/run.js "Test key rotation" --mode lite

# 4. Verify success rate in registry.json (should remain 1.0)

# 5. Monitor next 24h of activity for errors
```

#### Scenario 3: Critical Blocker Blocking All Work

```bash
# 1. Orchestrator posts blocker to bus
# 2. Kairo/clawd receives notification
# 3. Manual intervention:

# Option A: Resolve blocker at source
$ # e.g., resolve grant deadline extension, fix file path

# Option B: Route around blocker
$ node agents/orchestrator-agent/run.js "Replannning: skip blocked step, focus on parallel work"

# Option C: Escalate to Stefan
$ # Stefan makes strategic call, provides new direction
$ # Kairo re-routes with new priorities
```

### 13.2 Business Continuity

**RTO (Recovery Time Objective):** 15 minutes
- Restore from backup .env and registry.json
- Reinitialize SQLite bus
- Resume where left off (from state.md)

**RPO (Recovery Point Objective):** 1 hour
- Agents checkpoint to state.md every run
- Bus backed up hourly to local archive
- Feed.md is append-only; no data loss

---

## 14. Future Roadmap & Expansion

### 14.1 Planned Agent Integrations

**Codex (Code Generation Supervisor)** — Q3 2026
- Code generation from specs (Architect output)
- Bug fix and refactoring
- PR preparation and filing
- Integration with GitHub API

**Antigravity (Content Supervisor)** — Q4 2026
- LinkedIn post drafting and scheduling
- Blog content generation
- Grant narrative writing
- Long-form strategy documents

**Scout (Web Automation Supervisor)** — Q1 2027
- Grant application filling
- Automated research collecting (Perplexity + web scraping)
- Form submission and filing
- Document generation (PDFs, compliance reports)

### 14.2 Scaling Features

**Multi-User Support** (Phase 2)
- User context isolation (separate context.md per user)
- Role-based access control (Stefan = admin, team members = limited)
- Shared registry with per-user probation status
- Team feed vs. personal feed

**Distributed Deployment** (Phase 2-3)
- Agent containerization (Docker per agent)
- Kubernetes orchestration
- Horizontal scaling (multiple instances per agent)
- Load balancing via message queue (RabbitMQ or Kafka)

**Advanced Coordination** (Phase 3)
- DAG-based pipeline (Directed Acyclic Graphs)
- Conditional branching (if/else in pipelines)
- Parallel task execution (fan-out/fan-in)
- Cost optimization (select cheapest agent for task)

### 14.3 Integration Roadmap

**Short-term (Next 3 months):**
- GitHub API: pull latest issues, auto-assign to Codex
- Telegram bot: push critical alerts and feed summaries
- Obsidian sync: read vault structure as context

**Medium-term (3-6 months):**
- Supabase: store historical runs and cost analytics
- Notion API: sync status updates with Stefan's workspace
- Slack: post pipeline results and blockers

**Long-term (6-12 months):**
- Email integration: send summaries, receive voice commands
- Calendar integration: respect Stefan's busy hours, avoid invoking during meetings
- Financial API: track spending per mission, cost reporting

---

## 15. Operational Runbooks

### 15.1 Daily Operations

**Morning Standup (6 AM CST):**
```bash
# 1. Check bus status
node ~/.clawd/.bus/busctl.js status

# 2. Review last 24h of activity
node ~/.clawd/.bus/busctl.js read --since $(date -u -d "24 hours ago" +"%Y-%m-%dT%H:%M:%SZ")

# 3. Check agent health (registry.json)
# Are any agents on probation? Any high failure counts?

# 4. Read feed
head -50 ~/Desktop/kai/07-AI/chatroom/feed.md

# 5. Read state files for last errors
tail -5 ~/Desktop/kai/07-AI/agents/*/state.md
```

**Invoking an Agent:**
```bash
# 1. Know the agent specialty
# 2. Craft a concise task description
# 3. Run with appropriate flags
node agents/architect-agent/run.js "Design X" --mode lite  # Fast, cheap
node agents/orchestrator-agent/run.js "Decompose Y"        # Route work
node agents/aeos-agent/run.js "brief"                      # Synthesize research

# 4. Check feed for summary
# 5. Read state.md for full output
```

### 15.2 Weekly Maintenance

**Monday (Weekly Review):**
```bash
# 1. Audit open loops (Aexis)
node agents/aexis-agent/run.js "audit"

# 2. Refresh strategic intelligence (Aeos)
node agents/aeos-agent/run.js "brief"

# 3. Review registry.json for probation status
# 4. Check cost tracking (sum all cost_per_call * usage_log entries)
# 5. Plan week's pipelines based on strategy context
```

**Thursday (Cost Review):**
```bash
# 1. Calculate weekly spend
jq '.agents[].usage_log[] | select(.timestamp >= "2026-07-21") | .cost' \
  ~/clawd/router/registry.json | \
  paste -sd+ | bc

# 2. Compare to budget (e.g., $10/week)
# 3. If overspend, review high-cost agents (Architect, Aeos)
# 4. Adjust mode flags (--mode lite) for future runs
```

**Friday (Quarterly Planning):**
```bash
# 1. Archive old bus messages (>90 days)
# 2. Backup state files to S3
# 3. Review roadmap vs. quarterly goals
# 4. Plan next sprint of agent improvements
```

### 15.3 Emergency Response

**When an Agent Fails:**

```bash
# 1. Identify failing agent from feed or bus
# 2. Read full error
tail -20 ~/Desktop/kai/07-AI/agents/{agent_name}/state.md | grep last_error

# 3. Categorize:
#    - API error (401, 429, 503) → check secrets or rate limit
#    - Timeout → retry or increase timeout
#    - Missing file → verify path, run context sync
#    - Logic error → report bug, escalate to Stefan

# 4. Manual retry
node agents/{agent_name}/run.js "{test task}"

# 5. If successful, reset counter
# Edit registry.json: consecutive_failures = 0

# 6. If still failing, place on probation
# Edit registry.json: on_probation = true
# Notify Stefan

# 7. Escalate to Stefan for decision:
#    - Fix root cause and retry
#    - Use fallback supervisor
#    - Defer work to manual execution
```

---

## 16. Governance & Decision Records

### 16.1 Architecture Decision Records (ADRs)

All architectural decisions documented in:
`~/clawd/AI-Organization/ADRs/`

**Template:**
```markdown
# ADR-NNN: [Title]

## Status
Proposed | Accepted | Deprecated

## Context
[What problem are we solving?]

## Decision
[What are we doing and why?]

## Consequences
[Positive and negative trade-offs]

## Alternatives Considered
[Other options and why we rejected them]
```

**Key ADRs:**
- ADR-001: SQLite WAL for message bus (not Redis or Kafka)
- ADR-002: On-premise subprocess model (not persistent daemon)
- ADR-003: Haiku-first cost strategy (Haiku, then Sonnet, then Claude)
- ADR-004: Request-response messaging (not event-driven initially)

### 16.2 Change Control

**Process for changes to architecture:**

1. Stefan proposes change (verbal or in Obsidian)
2. Architect drafts ADR and alternative approaches
3. Stefan approves ADR
4. Implementation phase (code changes, testing)
5. Validation phase (test against real workloads)
6. Deployment (update agents and registry.json)
7. Monitoring phase (watch metrics for 7 days)
8. Post-mortem (document lessons learned)

---

## 17. Appendix: Quick Reference

### 17.1 Agent Invocation Cheat Sheet

```bash
# Architect — System Design
node agents/architect-agent/run.js "Design <system>" [--mode lite|full] [--project "<name>"]

# Orchestrator — Decompose & Route
node agents/orchestrator-agent/run.js "<goal description>"

# Aexis — Execution Audit
node agents/aexis-agent/run.js "[audit|<specific task>]"

# Aeos — Strategic Brief
node agents/aeos-agent/run.js "[brief|<research topic>]"

# Perplexity — Research
node agents/perplexity-agent/run.js "<query>"

# Bus — Communication
node ~/.clawd/.bus/busctl.js post --from {agent} --topic {topic} --msg "{msg}"
node ~/.clawd/.bus/busctl.js read [--since <iso8601>] [--topic {topic>] [--limit N]
node ~/.clawd/.bus/busctl.js unread --agent {agent}
node ~/.clawd/.bus/busctl.js ack --agent {agent}
node ~/.clawd/.bus/busctl.js status
```

### 17.2 File Structure Reference

```
~/clawd/
├─ agents/
│  ├─ architect-agent/run.js
│  ├─ orchestrator-agent/run.js
│  ├─ aeos-agent/run.js
│  ├─ aexis-agent/run.js
│  └─ perplexity-agent/run.js
├─ .bus/
│  ├─ busctl.js
│  └─ bus.sqlite (auto-created)
├─ router/registry.json
└─ .env

~/Desktop/kai/07-AI/
├─ Context/context.md (CRITICAL: agent reads at loop start)
├─ agents/
│  ├─ architect/state.md
│  ├─ orchestrator/state.md
│  ├─ aeos/state.md
│  ├─ aexis/state.md
│  └─ perplexity/state.md
└─ chatroom/feed.md
```

### 17.3 Common Tasks

| Task | Command |
|------|---------|
| Start new pipeline | `node agents/orchestrator-agent/run.js "..."` |
| Design a system | `node agents/architect-agent/run.js "..." --mode full` |
| Quick design check | `node agents/architect-agent/run.js "..." --mode lite` |
| Audit open loops | `node agents/aexis-agent/run.js "audit"` |
| Get strategic brief | `node agents/aeos-agent/run.js "brief"` |
| Check agent health | `jq '.agents[] \| {name: .agent_name, success: .success_rate}' router/registry.json` |
| View recent activity | `node .bus/busctl.js read --limit 20` |
| Find errors | `grep -r "last_error" ~/Desktop/kai/07-AI/agents/*/state.md` |

---

## 18. Glossary

| Term | Definition |
|------|-----------|
| **Agent** | Autonomous supervisor responsible for one or more task types |
| **Supervisor** | An agent with full invocation authority and decision-making boundaries |
| **Orchestrator** | Special supervisor that decomposes goals into pipelines and routes work |
| **Check-in Model** | Communication pattern where agents post to a bus; no live sockets |
| **Message Bus** | SQLite WAL database storing timestamped messages from agents |
| **State File** | Per-agent markdown file logging execution history and errors |
| **Registry** | Global JSON file tracking agent health, cost, success rate, probation status |
| **Probation** | Status applied when agent fails 3+ consecutive times on a task type |
| **Loop** | Single execution of an agent: read context → call API → write state → post to bus |
| **Pipeline** | Sequenced set of tasks routed to supervisors to accomplish a goal |
| **Blocker** | Work item that cannot proceed without manual intervention or escalation |
| **Feed** | Append-only activity log (feed.md) for monitoring and audit |
| **On-Premise** | Deployed locally on developer machine; not cloud-hosted |
| **Token Efficiency** | Optimizing API calls to minimize cost (prefer Haiku over Sonnet) |

---

## 19. Contact & Escalation

**System Owner:** Stefan Mundow (Stephon Morris)  
**Email:** morrisstephon51@gmail.com  
**Timezone:** America/Chicago (CST/CDT)

**For Issues:**
1. Check state.md for agent errors
2. Review bus for escalations
3. File GitHub issue or email Stefan
4. Escalate to CTO/architect for design questions

---

**Document Version History:**
- 2026-07-26: Version 2.0 — OpenClaw AI Organization SAD (production-grade)
- 2026-07-26: Version 1.0 — Initial Stefan AI Organization SAD

**Last Updated:** 2026-07-26  
**Next Review:** 2026-10-26 (quarterly)
