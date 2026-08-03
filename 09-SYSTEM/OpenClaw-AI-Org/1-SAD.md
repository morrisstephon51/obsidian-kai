# System Architecture Document (SAD)
## OpenClaw AI Organization: Kairo/Clawd Multi-Agent Coordination System

**Version:** 2.0  
**Date:** 2026-07-26  
**Organization:** OpenClaw AI (Kairo/Clawd Workspace)  
**Primary Authority:** Stefan Mundow (Stef)  
**Executive Agent:** Kairo (clawd OpenClaw runtime)  
**Status:** Production Grade

---

## 1. Executive Summary

The OpenClaw AI Organization operates as a distributed, multi-tier supervisor network designed to amplify human decision-making while maintaining strict governance boundaries, token efficiency, and compliance isolation. The system employs:

- **Three-tier agent topology**: Executive layer (Kairo), Specialty Supervisors (Architect, Orchestrator, etc.), and Service Integrations (Claude API, Perplexity, Obsidian)
- **Canonical authority model**: Stefan holds strategic authority; Kairo holds operational delegation; Supervisors hold domain-specific execution authority
- **Token-efficiency constraints**: Sub-$0.05/week operational cost via Haiku-first routing and prompt caching
- **Compliance boundaries**: Fault isolation via subprocess invocation, data segmentation by sensitivity classification, audit trails via message bus

---

## 2. Multi-Layer Agent Topology

### 2.1 Organizational Structure

```
┌─────────────────────────────────────────────────────────────┐
│ TIER 0: HUMAN AUTHORITY                                     │
│ ┌─────────────────────────────────────────────────────────┐ │
│ │ Stefan Mundow (Stef) — Strategic Authority             │ │
│ │ - All external communications                           │ │
│ │ - All public-facing decisions                           │ │
│ │ - All funding and legal moves                           │ │
│ │ - Vault authority (Obsidian PARA system)               │ │
│ └─────────────────────────────────────────────────────────┘ │
└──────────────────────────┬──────────────────────────────────┘
                           │
           ┌───────────────┼───────────────┐
           │               │               │
┌──────────v─────────┐ ┌──v──────────────┐ ┌──v──────────────┐
│ TIER 1A:          │ │ TIER 1B:        │ │ TIER 1C:        │
│ EXECUTIVE AGENT   │ │ GOVERNANCE      │ │ INTEGRATIONS   │
│                  │ │ BOARD           │ │                 │
│ Kairo (OpenClaw) │ │ (TBD: Future)   │ │ Claude API      │
│ - Route requests │ │ - Compliance    │ │ Perplexity API  │
│ - Coordinate     │ │ - Audit         │ │ Obsidian Vault  │
│ - Escalate       │ │ - Oversight     │ │ Git/GitHub      │
└────────┬──────────┘ └─────────────────┘ └─────────────────┘
         │
    ┌────┴────────────────────────────────────┐
    │                                         │
┌───v───────────────────────────────────┐   │
│ TIER 2: SPECIALTY SUPERVISORS         │   │
│                                       │   │
│ ┌─ Orchestrator (Pipeline)           │   │
│ ├─ Architect (Design & Specs)         │   │
│ ├─ Aexis (Execution Audit)            │   │
│ ├─ Aeos (Strategic Intelligence)      │   │
│ ├─ Perplexity Agent (Research)        │   │
│ └─ Claude Base (General)              │   │
└───────────────────────────────────────┘   │
                                            │
                                    ┌───────v────────┐
                                    │ TIER 3:        │
                                    │ COMMUNICATION  │
                                    │                │
                                    │ Message Bus    │
                                    │ (SQLite WAL)   │
                                    └────────────────┘
```

**Tier 0: Human Authority**
- Stefan Mundow holds all strategic decision authority
- Approves external communications and public actions
- Manages Obsidian vault (PARA system) as source of truth
- Reviews and approves all supervisor outputs before external action

**Tier 1A: Executive Agent (Kairo)**
- Single point of operational coordination
- Routes tasks to appropriate supervisors
- Monitors supervisor health (via registry)
- Escalates blockers and system errors
- No autonomous external actions

**Tier 1B: Governance Board** (Placeholder for future)
- Compliance oversight
- Audit trail verification
- Policy enforcement
- Reserved for multi-team expansion

**Tier 1C: Integrations**
- External API providers (Claude, Perplexity)
- Vault access (Obsidian, Git)
- Message bus and storage layers

**Tier 2: Specialty Supervisors**
- Domain-specific reasoning and execution
- Stateless, request-response operation
- Single-writer guarantee per supervisor (state files)
- No supervisor waits for another

**Tier 3: Communication Layer**
- SQLite WAL-backed message bus
- Topic-based pub/sub (check-in model, not live)
- Audit trail of all supervisor activity
- Asynchronous by design (no blocking)

### 2.2 Supervisor Roles & Responsibilities

| Supervisor | Tier | Domain | Models | Cost/Call | Startup Time | Status |
|---|---|---|---|---|---|---|
| **Orchestrator** | 2 | Pipeline decomposition, workflow routing | Haiku | $0.002 | <5s | Provisioned |
| **Architect** | 2 | System design, specs, ADRs | Haiku/Sonnet | $0.0005–0.005 | <8s | Provisioned |
| **Aexis** | 2 | Execution audit, open loops, accountability | Haiku | $0.002 | <5s | Provisioned |
| **Aeos** | 2 | Strategic intelligence, synthesis, grants | Haiku | $0.003 | <8s | Provisioned |
| **Perplexity** | 2 | Real-time research, citations, trends | Perplexity API | $0.005 | <9s | Provisioned |
| **Claude Base** | 2 | General reasoning, code, creative | Haiku (default) | $0 (via OpenClaw) | <4s | Always available |

**Specialization Rules:**
- Each supervisor has explicit task type ownership (from registry)
- Router checks registry before invocation
- If supervisor on probation: escalate to Kairo or Orchestrator
- No supervisor can override another's output without explicit routing

---

## 3. Canonical Identity & Authority Model

### 3.1 Authority Hierarchy & Delegation

```
┌─────────────────────────────────────────────────────────────┐
│ STRATEGIC AUTHORITY (Stefan)                                │
├─────────────────────────────────────────────────────────────┤
│ • All external communications (Telegram, GitHub, email)     │
│ • All public actions (publishing, announcements)            │
│ • All funding and legal decisions                           │
│ • All strategic choices (mission, roadmap)                  │
│ • Vault authority (read/write PARA system)                  │
│ DELEGATION: Explicit written approval required              │
└────────────────┬────────────────────────────────────────────┘
                 │
┌────────────────v────────────────────────────────────────────┐
│ OPERATIONAL AUTHORITY (Kairo)                               │
├──────────────────────────────────────────────────────────────┤
│ • Standing authorization: Full vault read/write (PARA)      │
│ • Route and invoke supervisors based on task type           │
│ • Post to message bus and feed                              │
│ • Update registry (health, probation status)                │
│ • Read context.md for current project state                 │
│ • Escalate blockers to Stefan                               │
│ LIMITATION: No external comms without Stefan approval       │
│ LIMITATION: No approval of Stefan-facing outputs            │
└────────────────┬────────────────────────────────────────────┘
                 │
┌────────────────v────────────────────────────────────────────┐
│ DOMAIN AUTHORITY (Specialty Supervisors)                    │
├──────────────────────────────────────────────────────────────┤
│ • Orchestrator: Decompose goals into task pipelines         │
│ • Architect: Produce specifications and designs             │
│ • Aexis: Audit and track execution status                   │
│ • Aeos: Synthesize strategic insights                       │
│ • Perplexity: Conduct real-time research                    │
│ LIMITATION: Stateless; no persistent decisions              │
│ LIMITATION: Output requires Stefan review/approval          │
│ LIMITATION: No external actions without explicit routing    │
└────────────────┬────────────────────────────────────────────┘
                 │
                 v
        [Message Bus & Feed]
        [Registry & State Files]
        [Obsidian Vault (read)]
```

### 3.2 Stef/Kairo Delegation Model

**Stef's Responsibilities:**
```
Decision Authority:
├─ Strategic direction (what to build, why)
├─ External communications (when, how, what to say)
├─ Approval of supervisor outputs (accept/reject/revise)
├─ Vault updates (strategy, planning documents)
├─ Policy changes (new task types, new supervisors)
└─ Escalation decisions (how to resolve blockers)

Delegation to Kairo:
├─ Execute approved tasks via supervisors
├─ Monitor supervisor health and probation
├─ Maintain audit trail (bus + feed)
├─ Read vault and update context
├─ Post daily summaries to feed
└─ Flag critical issues for Stef review
```

**Kairo's Responsibilities:**
```
Execution Authority:
├─ Route tasks to healthy supervisors
├─ Invoke supervisors via subprocess
├─ Post loop-start/loop-end to bus
├─ Update supervisor state files
├─ Track cost and performance in registry
├─ Read Obsidian vault (full authority)
└─ Maintain message bus and feed

Constraints:
├─ Never make strategic decisions
├─ Never communicate externally
├─ Never approve outputs (Stefan only)
├─ Never modify registry unless metrics trigger
├─ Never skip approval gates for strategic work
└─ Escalate all ambiguity to Stefan
```

**Supervisors' Responsibilities:**
```
Execution Authority:
├─ Generate output in domain specialty
├─ Read context.md if applicable
├─ Call Claude/Perplexity API
├─ Write result to state.md
├─ Post to bus with topic tag
└─ Update run count in registry

Constraints:
├─ Stateless (no persistent decisions)
├─ No external API calls except Claude/Perplexity
├─ No vault write (read only)
├─ No bus commands except post/ack
├─ No approval authority
└─ No cross-supervisor communication
```

### 3.3 Approval Gates

**Gate 1: Output Validation (Kairo)**
- Supervisor produces output
- Kairo checks format and completeness
- If malformed → log error, escalate to Stefan

**Gate 2: Strategic Review (Stefan)**
- Kairo presents output to Stefan
- Stefan approves, requests revision, or rejects
- If approved → gate 3; if revision → supervisor re-runs; if rejected → archive

**Gate 3: External Action (Kairo)**
- Stefan approves external action (e.g., publish, send email)
- Kairo executes action
- Posts confirmation to bus and feed

**Gate 4: Vault Integration (Kairo)**
- If strategic output → copy to Obsidian vault
- Link from feed.md
- Update context.md with new state

---

## 4. Token Efficiency Constraints & Context Management

### 4.1 Token Budget Philosophy

**Principle: Minimize context injection; maximize reasoning efficiency.**

Every task has a "token budget" — expected input + output tokens.

**Current Token Budgets (per task type):**

| Task Type | Model | Input | Output | Cost | Monthly (assume 4×) | Notes |
|---|---|---|---|---|---|---|
| Pipeline | Haiku | 500 | 800 | $0.002 | $0.032 | Reads context.md |
| Lite Spec | Haiku | 300 | 400 | $0.0005 | $0.008 | Task-only |
| Full Spec | Sonnet | 800 | 1000 | $0.005 | $0.080 | Complex design |
| Execution Audit | Haiku | 1000 | 500 | $0.002 | $0.032 | Reads context.md |
| Strategic Brief | Haiku | 2000 | 800 | $0.003 | $0.048 | Reads context.md + vault |
| Research Query | Perplexity | 200 | 2000 | $0.005 | $0.040 | Public data only |
| **Total Monthly** | — | — | — | — | **$0.24** | Highly efficient |

### 4.2 Context Injection Rules

**Rule: Read only what you need.**

**Context Layers:**

**Layer 1: Task Description (Always)**
```
Every supervisor receives:
- Task name (e.g., "Design user authentication")
- Task type (e.g., "spec", "audit", "pipeline")
- Invocation time
- Any explicit parameters
Cost: ~50 tokens
```

**Layer 2: Project Context (Conditional)**
```
Supervisors that read context.md:
- Orchestrator (full file, ~2000-3000 tokens)
- Aexis (full file, for auditing)
- Aeos (full file, for strategy)
- Architect (NOT—uses task only, fresh eyes)
- Perplexity (NOT—uses query only)
Cost: +2000 tokens if read
```

**Layer 3: Vault Context (Conditional)**
```
Supervisors that read vault notes:
- Orchestrator (reads project notes from PARA Projects/)
- Aeos (reads strategic docs from Resources/)
- Kairo (reads vault index at startup)
Cost: +500-1000 tokens if read
```

**Layer 4: Session State (Never injected)**
```
Data NOT sent to supervisors:
- Prior run outputs (breaks freshness)
- Detailed execution logs (too verbose)
- Personal vault notes (privacy)
- Financial data (security)
```

### 4.3 Prompt Caching Strategy

**Opportunity 1: Static Prompt Templates**
```
Each supervisor uses a fixed prompt template.
These templates are identical across runs.
→ Use Claude API prompt caching (24-hour window)
→ Save 90% of input token cost on repeated template

Example (Architect Full Mode):
Cached section: 800 tokens of prompt
New section: 200 tokens of task description
Result: ~300 input tokens instead of 1000
```

**Opportunity 2: Context.md Caching**
```
context.md is read by 3+ supervisors per loop.
Does not change between supervisors (except during Stefan review).
→ Cache for 5-minute window at system level
→ Save 6000+ tokens/day

Implementation:
Cache wrapper in Kairo:
  if (cache_hit && <5 min old): return cached
  else: read file, cache, return
```

**Opportunity 3: Vault Index Caching**
```
_INDEX.md is read on every startup.
→ Cache for 24-hour window
→ Rebuild on manual trigger

Cost: 100 tokens saved per startup (e.g., 5× per day = 500 tokens/day)
```

### 4.4 Token Monitoring & Optimization

**Tracking:**
```javascript
// In registry.json, per supervisor, per task type:
{
  "usage_log": [
    {
      "task_type": "design",
      "input_tokens": 750,
      "output_tokens": 1200,
      "cost": 0.005,
      "timestamp": "2026-07-26T09:15:00Z",
      "success": true
    },
    ...
  ]
}
```

**Alerts:**
- If cost per task exceeds budget → log warning
- If avg latency >10s → investigate model selection
- If output tokens >budget × 1.5 → escalate task to Sonnet

**Optimization Loop (Monthly):**
1. Aggregate usage by task type
2. Identify overbudget tasks
3. Revise prompts to be more concise
4. Test token reduction with dry runs
5. Update budget in registry if justified

---

## 5. Fault Isolation & Compliance Boundaries

### 5.1 Fault Isolation Architecture

**Design Principle: Failure in one supervisor must not cascade to others.**

**Isolation Mechanisms:**

**Mechanism 1: Subprocess Invocation**
```
Each supervisor runs in a separate Node.js process.
├─ Supervisor crashes → process exits, doesn't affect others
├─ Supervisor hangs → timeout, kill process, escalate
├─ Supervisor memory leak → gone after process exits
├─ Supervisor infinite loop → detect via timeout, escalate
└─ No shared memory or global state (per supervisor)
```

**Mechanism 2: State File Isolation**
```
Each supervisor owns one state.md file.
├─ Orchestrator: /path/to/orchestrator/state.md
├─ Architect: /path/to/architect/state.md
├─ Aexis: /path/to/aexis/state.md
└─ Last-write-wins; only that supervisor writes to its file
Result: No state contention; no locking required
```

**Mechanism 3: Registry Probation**
```
If a supervisor fails 3× in a row on a task type:
├─ Mark on_probation[task_type] = true
├─ Set cooldown_until = now + 24 hours
├─ Skip that supervisor for that task type (escalate to Orchestrator)
└─ After cooldown: reset consecutive_failures counter, retry

Effect: Broken supervisor doesn't block the system; work routes around it
```

**Mechanism 4: API Rate-Limiting**
```
If Claude API returns rate limit error:
├─ Catch error in supervisor
├─ Implement exponential backoff (base 2, max 60s)
├─ Log to state.md and bus
├─ Escalate to Kairo if retry fails
└─ Do NOT retry immediately (prevents cascade)
```

**Mechanism 5: Timeout Guards**
```
Every supervisor call has a timeout:
├─ Default: 30 seconds
├─ Rationale: Claude latency is <10s typical, 20s 99th percentile
├─ On timeout: kill process, log error, escalate
└─ Prevent hanging processes from accumulating
```

### 5.2 Compliance Boundaries

**Definition: Data classifications and access controls.**

**Classification Levels:**

**Level 1: Public (No Restriction)**
```
Data that can be shared externally without impact.
├─ Example: System designs, code, published research
├─ Supervisors that can read: All
├─ Supervisors that can write: Architect, Perplexity
└─ Vault location: Projects/ (published)
```

**Level 2: Internal (Kairo Only)**
```
Data needed for system operation; not sensitive.
├─ Example: Execution logs, task pipelines, open loops
├─ Supervisors that can read: Orchestrator, Aexis, Aeos
├─ Supervisors that can write: All (to bus and state)
└─ Vault location: Areas/ (operations)
Constraint: Never shared externally without Stefan approval
```

**Level 3: Strategic (Stefan Only)**
```
Strategic plans, financial decisions, personal notes.
├─ Example: Roadmap, grants, personal contacts
├─ Supervisors that can read: Kairo (if in context.md)
├─ Supervisors that can write: Stefan only
└─ Vault location: PARA top-level (private)
Constraint: Never transmitted to external API except in explicit Stefan-approved task
```

**Level 4: Confidential (Offline Only)**
```
Credentials, API keys, personal secrets.
├─ Example: ANTHROPIC_API_KEY, PERPLEXITY_API_KEY
├─ Supervisors that can read: None (via environment only)
├─ Storage: .env file (never committed)
└─ Constraint: Rotate quarterly
```

**Data Flow Rules:**

```
┌─────────────────────────────────────────────────────────────┐
│ BOUNDARY: Vault ↔ Supervisor                               │
├─────────────────────────────────────────────────────────────┤
│ Level 1 (Public) →    Read: Any    Write: Architect
│ Level 2 (Internal) →  Read: Kairo  Write: Kairo
│ Level 3 (Strategic) → Read: Stefan Write: Stefan
│ Level 4 (Secret) →    Read: Never  Write: Offline
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│ BOUNDARY: Supervisor ↔ External API                         │
├─────────────────────────────────────────────────────────────┤
│ No credentials transmitted in API calls
│ Task description may include Level 1, Level 2 data
│ Task description must NOT include Level 3, Level 4 data
│ Exception: Stefan explicitly approves inclusion
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│ BOUNDARY: Vault ↔ External                                  │
├─────────────────────────────────────────────────────────────┤
│ Level 1: May be published (GitHub, web)
│ Level 2: Never published
│ Level 3, 4: Never published
│ Gate: Stefan explicit approval required
└─────────────────────────────────────────────────────────────┘
```

### 5.3 Audit Trail & Compliance

**Audit Sources (Immutable):**

**Source 1: Message Bus (bus.sqlite)**
```
Append-only log of all agent messages.
├─ Schema: timestamp, from, topic, message, checksum
├─ Properties: WAL-enabled (concurrent writes safe)
├─ Retention: Indefinite
├─ Query example: "All messages from architect since 2026-07-20"
└─ Used for: Compliance audit, debugging, compliance investigations
```

**Source 2: Feed (feed.md)**
```
Daily markdown summary of all supervisor activity.
├─ Format: Markdown; one section per supervisor per day
├─ Example:
   ## 2026-07-26
   ### Orchestrator
   - 1 pipeline decomposition (goal: "Build Plug AI web UI")
   - Estimated cost: $0.002
   - Status: Success
   ### Architect
   - (None today)
├─ Retention: Indefinite
└─ Used for: High-level activity review, cost tracking
```

**Source 3: State Files (per supervisor)**
```
Full output of last run per supervisor.
├─ Location: /Desktop/kai/07-AI/agents/*/state.md
├─ Retention: Last 5 runs (older versions deleted)
├─ Properties: Readable by Stefan and Kairo
└─ Used for: Detailed output review, error debugging
```

**Source 4: Registry (registry.json)**
```
Health and performance metadata.
├─ Metrics: Success rate, failure count, probation status, latency
├─ Retention: Rolling 90-day window
├─ Properties: Updated after every supervisor run
└─ Used for: Routing decisions, performance analysis
```

**Compliance Queries:**

```bash
# Audit trail: All work done in past 7 days
node busctl.js read --since 2026-07-19T00:00:00Z

# Compliance: All external research (may have URLs)
node busctl.js read --topic research

# Cost tracking: All messages with cost
grep "cost" feed.md

# Error investigation: All errors in past 24 hours
node busctl.js read --topic error --since 2026-07-25T00:00:00Z

# Probation status: Any supervisor on probation
jq '.agents[] | select(.on_probation | any)' registry.json
```

---

## 6. Governance & Oversight

### 6.1 Governance Model

**Decision Framework:**

```
┌─────────────────────────────────────────────────────────────┐
│ DECISION TYPE          AUTHORITY      TIMELINE    ESCALATION │
├─────────────────────────────────────────────────────────────┤
│ Task invocation        Kairo          Immediate   Stefan     │
│ Output approval        Stefan         <24 hours   Manual     │
│ Supervisor addition    Stefan         1 week      Board      │
│ Policy change          Stefan+Board   2 weeks     Vote       │
│ Emergency (API down)   Kairo          Immediate   Stefan     │
│ Budget increase        Stefan         2 weeks     Funding    │
│ External comms         Stefan         <24 hours   Manual     │
│ Vault access grant     Stefan         Manual      Case-by    │
│ Probation resolution   Kairo + Stefan 24 hours    Review     │
└─────────────────────────────────────────────────────────────┘
```

**Escalation Paths:**

```
Ambiguity or blocker identified by supervisor
    ↓
Post to bus with topic "blocker" or "question"
    ↓
Kairo reads bus, logs to state.md
    ↓
Kairo posts to Stefan (via Telegram or feed)
    ↓
Stefan provides decision
    ↓
Kairo implements, re-runs supervisor if needed
    ↓
Update context.md and bus
```

### 6.2 Review Schedule

**Daily (9 AM CST):**
- Stefan reviews feed.md (last 24 hours)
- Check bus for errors or blockers
- Approve or reject outputs
- Update context.md if needed

**Weekly (Friday EOD):**
- Kairo generates compliance summary
- Review registry for health issues
- Cost analysis (target: <$0.05/week)
- Probation status check

**Monthly (Last Friday):**
- Full audit of bus.sqlite
- Archive completed work to vault
- Update prompt templates if needed
- Reset consecutive failure counters

**Quarterly (End of quarter):**
- SAD review and update
- API key rotation
- Cost analysis and optimization
- Scaling assessment

### 6.3 Policy Framework

**Policy 1: No Autonomous External Actions**
```
No supervisor or Kairo can:
├─ Send emails
├─ Post to social media
├─ File GitHub issues
├─ Execute merges or deployments
└─ Share confidential data

Requirement: Stefan explicit approval (documented in bus and feed)
```

**Policy 2: Token Efficiency**
```
Cost per task type must stay within budget.
├─ Lite spec: <$0.001
├─ Full spec: <$0.006
├─ Pipeline: <$0.003
├─ Audit: <$0.003
└─ Strategic brief: <$0.005

Violation: Log warning in registry, escalate if pattern emerges
```

**Policy 3: Data Classification**
```
All data must be labeled with classification level.
├─ Public (L1): Safe to share externally
├─ Internal (L2): Stefan approval to external
├─ Strategic (L3): Never external without explicit Stefan approval
├─ Confidential (L4): Never external
```

**Policy 4: Supervisor Health**
```
If a supervisor fails 3× on a task type → probation.
├─ During probation: skip supervisor, escalate to Orchestrator
├─ Cooldown: 24 hours
├─ After cooldown: reset consecutive_failures counter
├─ If supervisor fails to recover: escalate to Stefan for review
```

**Policy 5: Audit Trail Integrity**
```
All activity must be logged in one of:
├─ bus.sqlite (transactional)
├─ feed.md (daily summary)
├─ state.md (per-supervisor output)
├─ registry.json (health metrics)

Logs are immutable; cannot be deleted or modified retroactively.
Retention: Indefinite
```

---

## 7. Implementation Details

### 7.1 Message Bus Protocol

**Endpoint:** SQLite WAL database at `/clawd/.bus/bus.sqlite`

**Schema:**
```sql
CREATE TABLE messages (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  timestamp TEXT NOT NULL,          -- ISO8601 (UTC)
  from_agent TEXT NOT NULL,         -- supervisor name
  topic TEXT NOT NULL,              -- pipeline, architecture, audit, etc.
  message TEXT NOT NULL,            -- full message body
  cost REAL,                        -- API cost (optional)
  latency_ms INTEGER,               -- execution time
  success BOOLEAN,                  -- true = success, false = error
  checksum TEXT                     -- SHA256(message) for integrity
);

CREATE TABLE checkpoints (
  agent_name TEXT PRIMARY KEY,
  last_read_timestamp TEXT NOT NULL -- ISO8601 when agent called ack()
);
```

**CLI Commands:**
```bash
# Post message
node busctl.js post \
  --from orchestrator \
  --topic pipeline \
  --msg "Decomposed into 5 steps" \
  [--cost 0.002] [--latency 5000]

# Read all
node busctl.js read

# Read since timestamp
node busctl.js read --since 2026-07-26T09:00:00Z

# Read by topic
node busctl.js read --topic architecture --limit 10

# Read unread (since last checkpoint)
node busctl.js unread --agent architect

# Acknowledge (set checkpoint)
node busctl.js ack --agent architect

# System status
node busctl.js status
```

### 7.2 Registry Structure

**Location:** `/clawd/router/registry.json`

**Per-Supervisor Entry:**
```json
{
  "agent_name": "orchestrator",
  "task_types": ["pipeline", "workflow", "coordination", "planning"],
  "cost_per_call": 0.002,
  "avg_latency_ms": 5000,
  "invocation_mode": "node_script",
  "provisioned": true,
  "success_rate": {
    "pipeline": 1.0,
    "workflow": 1.0,
    "coordination": 1.0,
    "planning": 1.0
  },
  "failure_count": {
    "pipeline": 0,
    "workflow": 0,
    "coordination": 0,
    "planning": 0
  },
  "consecutive_failures": {
    "pipeline": 0,
    "workflow": 0,
    "coordination": 0,
    "planning": 0
  },
  "cooldown_until": {
    "pipeline": null,
    "workflow": null,
    "coordination": null,
    "planning": null
  },
  "on_probation": {
    "pipeline": false,
    "workflow": false,
    "coordination": false,
    "planning": false
  },
  "last_updated": "2026-07-26T10:30:00.000Z",
  "usage_log": [
    {
      "task_type": "pipeline",
      "input_tokens": 500,
      "output_tokens": 800,
      "cost": 0.002,
      "latency_ms": 5000,
      "timestamp": "2026-07-26T10:30:00.000Z",
      "success": true
    }
  ]
}
```

### 7.3 State File Format

**Location:** `/Desktop/kai/07-AI/agents/{supervisor_name}/state.md`

**Example (Architect):**
```markdown
---
supervisor: architect
status: idle
current_task: null
last_run: 2026-07-26T10:15:00Z
runs_completed: 12
last_error: null
input_tokens: 800
output_tokens: 950
cost: 0.005
latency_ms: 8200
---

## Task
Design a RESTful API for user authentication

## Output

### What We're Building
A lightweight, OAuth2-compatible REST API for managing user identities and permissions.

### Key Decisions
1. Use JWT tokens (stateless, scalable) over sessions (requires server state)
2. Implement role-based access control (RBAC) for extensibility
3. Rate-limit auth endpoint to prevent brute force (10 req/min per IP)

### Spec
- **Endpoints:**
  - POST /auth/register
  - POST /auth/login
  - POST /auth/refresh
  - GET /auth/verify
  - DELETE /auth/logout

- **Data Model:**
  - User: { id, email, password_hash, created_at, updated_at }
  - Token: { id, user_id, type, expires_at }

### Risks
1. Token theft via XSS → mitigation: HttpOnly cookies, CORS policy
2. Brute force password attacks → mitigation: rate-limiting, account lockout
3. Token expiration complexity → mitigation: refresh token pattern

### Done When
- [ ] API endpoints tested with curl
- [ ] Rate limiting verified (10 req/min enforced)
- [ ] JWT payload validated

### Handoff
First PR: Implement POST /auth/register endpoint with validation

## Review by Stefan
Status: APPROVED
Notes: Add support for social login (OAuth2 Google) as stretch goal
Date: 2026-07-26T10:45:00Z
```

### 7.4 Supervisor Lifecycle

**Every supervisor invocation follows this pattern:**

```javascript
// 1. STARTUP
const supervisor = 'orchestrator';
const taskDescription = argv[2];  // from command line
const contextPath = '/Desktop/Context/context.md';
const statePath = `/Desktop/kai/07-AI/agents/${supervisor}/state.md`;

// 2. POST LOOP-START
bus('post', {
  from: supervisor,
  topic: 'loop-start',
  msg: `Starting: ${taskDescription}`,
  timestamp: new Date().toISOString()
});

// 3. READ CONTEXT (if applicable)
const context = (readContextNeeded)
  ? fs.readFileSync(contextPath, 'utf-8')
  : null;

// 4. CALL CLAUDE
const response = await claude({
  system: SUPERVISOR_PROMPT[supervisor],
  user: `Task: ${taskDescription}\n\nContext: ${context || '(none)'}`,
  model: selectModel(supervisor),
  maxTokens: tokenBudget[supervisor].output
});

// 5. UPDATE STATE
setState({
  status: 'idle',
  current_task: null,
  last_run: new Date().toISOString(),
  runs_completed: runs_completed + 1,
  last_error: null,
  output: response.text,
  input_tokens: response.usage.input_tokens,
  output_tokens: response.usage.output_tokens,
  cost: computeCost(response),
  latency_ms: response.latency
});

// 6. APPEND TO FEED
const feedPath = '/Desktop/kai/07-AI/chatroom/feed.md';
appendToFile(feedPath, `\n### ${supervisor}\n- Task: ${taskDescription}\n- Status: Success\n- Cost: $${computeCost(response).toFixed(4)}\n`);

// 7. UPDATE REGISTRY
const registry = JSON.parse(readFileSync('/clawd/router/registry.json', 'utf-8'));
const agent = registry.agents.find(a => a.agent_name === supervisor);
agent.usage_log.push({
  task_type: inferTaskType(taskDescription),
  input_tokens: response.usage.input_tokens,
  output_tokens: response.usage.output_tokens,
  cost: computeCost(response),
  latency_ms: response.latency,
  timestamp: new Date().toISOString(),
  success: true
});
writeFileSync('/clawd/router/registry.json', JSON.stringify(registry, null, 2));

// 8. ACKNOWLEDGE ON BUS
bus('ack', { agent: supervisor });

// 9. RETURN / EXIT
process.exit(0);
```

---

## 8. Performance & Scalability

### 8.1 Current Performance Profile

**Latency:**
- Supervisor startup: 50-200 ms (Node.js init)
- Claude API call: 1500-8000 ms (typical 4-5 seconds)
- State file write: 10-50 ms (sync)
- Bus post: 20-100 ms (SQLite WAL)
- **Total per task:** 1.6-8.2 seconds (typical 5-6 seconds)

**Throughput:**
- Sequential: 1 task every 5-6 seconds (~600 tasks/day if continuous)
- Practical: 5-10 supervisor calls per day (human paced)

**Cost:**
- Current: ~$0.04/week ($2/year)
- Scaling: Linear with task count
- Optimization: Token efficiency measures can reduce by 40-50%

### 8.2 Scaling Roadmap

**Phase 1 (Now, through Q4 2026):**
- Single human (Stefan)
- Sequential supervisor invocation
- Local state (files + SQLite)
- Single machine

**Phase 2 (Q1 2027):**
- Parallel supervisor calls (Promise.all for independent tasks)
- Redis-backed bus (replaces SQLite for distributed env)
- Context caching layer (5-min TTL)
- Cost: Similar ($0.04-0.06/week)

**Phase 3 (Q2-Q3 2027, if needed):**
- Multi-agent team (Stefan + 1-2 others)
- Distributed supervisor network (multiple machines)
- Central message broker (RabbitMQ or Kafka)
- Audit compliance (Sarbanes-Oxley, HIPAA if health data involved)
- Cost: ~$0.20/week

**Phase 4 (2028+, strategic expansion):**
- Multi-team OpenClaw deployments
- Role-based access control (RBAC)
- SLA guarantees (99.9% uptime)
- Cloud storage (S3, GCS)
- Cost: $1-5/week

### 8.3 Cost Optimization

**Current Spend:**
- Claude Haiku: ~$0.02/week (10 calls × $0.002 avg)
- Claude Sonnet: ~$0.005/week (1 call × $0.005)
- Perplexity: ~$0.015/week (3 calls × $0.005)
- **Total: ~$0.04/week**

**Optimization Tactics (achievable in Q3 2026):**

1. **Prompt Caching** (saves ~90% on template)
   - Effect: Architect calls from $0.005 to $0.0005
   - Quarterly savings: ~$0.020

2. **Lite Mode Default** (Haiku instead of Sonnet)
   - Effect: Reduce full-spec calls from 2× to 0.5× per week
   - Quarterly savings: ~$0.010

3. **Context Caching** (5-minute TTL)
   - Effect: Reduce context reads by 60%
   - Quarterly savings: ~$0.015

4. **Batch Voicing Research** (3 queries/day instead of scattered)
   - Effect: Amortize latency and API setup
   - Quarterly savings: ~$0.005

**Target:** Reduce to **$0.02/week** (50% reduction) by Q4 2026.

---

## 9. Future Extensions & Vision

### 9.1 Planned Integrations

**GitHub Integration (Q3 2026):**
- Architect writes ADRs as .md files → auto-PR to repo
- Orchestrator files issues → tracked in GitHub Issues
- Automated PR review via Architect → code quality gates
- Kairo closes PRs after Stefan approval

**Telegram Integration (Q3 2026):**
- Stefan sends `/decompose [goal]` → Kairo routes to Orchestrator
- Kairo posts results as Telegram message
- Stefan approves/rejects via reaction emoji
- Near-real-time workflow

**Calendar Integration (Q4 2026):**
- Aexis reads Google Calendar for deadlines
- Orchestrator respects meeting times when planning
- Deadline-aware task routing
- Automatic context injection for time-sensitive work

**Notion Integration (Q1 2027, if needed):**
- Backup of Obsidian vault state
- Public-facing project dashboard (if needed)
- Client/stakeholder visibility

### 9.2 New Supervisor Archetypes

**Codex — Code Execution & Testing**
- Runs test suites, debugs code
- Integrates with GitHub CI/CD
- Produces PRs automatically
- Specialty: code-execution, debugging, testing

**Antigravity — Content Production**
- Writes marketing copy, LinkedIn posts, blog articles
- Integrates with CMS (if applicable)
- Content calendar automation
- Specialty: content, creative-writing, marketing

**Nexus — Team Coordination** (for multi-team phase)
- Aggregates team updates and status
- Sends summaries to Slack/email
- Manages async team decisions
- Specialty: team-coordination, async-leadership

**Sentinel — Security & Compliance**
- Scans code for vulnerabilities
- Ensures compliance with policies
- Generates audit reports
- Specialty: security-audit, compliance-check

### 9.3 Long-Term Vision

**5-Year Roadmap (2026-2031):**

```
2026 (Foundation)
├─ Current: Kairo + 6 supervisors
├─ Goal: Prove system at single-human scale
└─ Metric: <$0.05/week cost, 95%+ success rate

2027 (Expansion)
├─ Goal: Support 2-3 human team members
├─ Extend: Add Codex, Antigravity supervisors
├─ Scale: Distributed supervisor network
└─ Metric: <$0.20/week cost, 99%+ success rate

2028 (Productization)
├─ Goal: Package Kairo as reusable framework
├─ Release: Open-source Kairo architecture
├─ Support: Documentation, examples, templates
└─ Metric: 5-10 external teams using Kairo

2029 (Integration)
├─ Goal: Full enterprise compliance (SOC 2, HIPAA)
├─ Market: Premium Kairo SaaS offering
├─ Customers: Early-stage startups, nonprofits
└─ Metric: $50K+ annual revenue

2030 (AI Governance)
├─ Goal: Thought leadership on AI organization governance
├─ Publish: Peer-reviewed research on multi-agent systems
├─ Build: Industry standards for AI team structure
└─ Metric: Speaking at major AI conferences
```

---

## 10. Operations Manual

### 10.1 Daily Standup Checklist

```bash
# 1. Check vault freshness
cat /Users/abdoulayemundow/Desktop/kai/_INDEX.md | head -3

# 2. Review context
cat /Users/abdoulayemundow/Desktop/Context/context.md | head -50

# 3. Check bus health
node /Users/abdoulayemundow/clawd/.bus/busctl.js status

# 4. Run audit
node /Users/abdoulayemundow/clawd/agents/aexis-agent/run.js audit

# 5. Review yesterday's feed
tail -30 /Users/abdoulayemundow/Desktop/kai/07-AI/chatroom/feed.md

# 6. Check for probation status
jq '.agents[] | select(.on_probation | any)' /Users/abdoulayemundow/clawd/router/registry.json
```

### 10.2 Task Invocation Examples

```bash
# Decompose a goal
node agents/orchestrator-agent/run.js "Build user signup flow for Plug AI"

# Design a system
node agents/architect-agent/run.js "Design Postgres schema for education platform"

# Quick spec (lite mode)
node agents/architect-agent/run.js "List steps to deploy to production" --mode lite

# Audit open loops
node agents/aexis-agent/run.js audit

# Get strategic insight
node agents/aeos-agent/run.js "What are key funding opportunities in education AI?"

# Research topic
node agents/perplexity-agent/run.js "Latest AI safety regulations in 2026"
```

### 10.3 Error Recovery

**If a supervisor hangs (>30 seconds):**
```bash
# Kill the process
ps aux | grep "node agents/.*run.js" | grep -v grep | awk '{print $2}' | xargs kill -9

# Check state file for partial output
cat /Desktop/kai/07-AI/agents/{supervisor}/state.md

# Escalate to Stefan
echo "Supervisor {supervisor} timed out. Check state.md for details."
```

**If bus is corrupted (can't post messages):**
```bash
# Backup current bus
cp /clawd/.bus/bus.sqlite /clawd/.bus/bus.sqlite.bak

# Recreate bus
rm /clawd/.bus/bus.sqlite
node busctl.js status  # This will auto-initialize

# Restore from backup if needed
cp /clawd/.bus/bus.sqlite.bak /clawd/.bus/bus.sqlite
```

**If registry is inconsistent:**
```bash
# Backup registry
cp /clawd/router/registry.json /clawd/router/registry.json.bak

# Regenerate (reset all counters)
# TODO: Implement registry reset script
```

---

## 11. Appendix: Glossary

**Agent / Supervisor:** Specialized stateless system that handles one domain (e.g., Architect for design, Aexis for audits).

**Approval Gate:** Control point where output must be reviewed and approved before proceeding to next stage (e.g., Stefan approval before external action).

**Bus:** SQLite WAL-backed message log enabling async communication between supervisors via topic-based pub/sub.

**Checkpoint:** Timestamp marking when an agent last read the bus; used to determine "unread" messages for that agent.

**Classification Level:** Data sensitivity category (L1 public, L2 internal, L3 strategic, L4 confidential).

**Compliance Boundary:** Logical/technical separation preventing data or actions from crossing security/regulatory lines.

**Context:** Current work state stored in `context.md`; read by most supervisors at loop start.

**Feed:** Permanent activity log in `feed.md`; every supervisor appends summary of work here.

**Fault Isolation:** Design ensuring failure in one component (e.g., supervisor crash) doesn't cascade to others.

**Kairo:** Executive agent coordinating all supervisors; no autonomous external actions.

**Loop:** Single invocation of a supervisor; starts with post, ends with ack.

**OpenClaw:** Claude Code runtime providing file I/O, Git, shell, and MCP tool access.

**Probation:** State entered when supervisor fails 3× on task type; supervisor skipped for that type until cooldown expires.

**Prompt Caching:** Technique to reduce token cost by reusing static prompt templates across calls.

**Registry:** Health/performance metadata for all supervisors stored in `registry.json`.

**Stef / Stefan:** Human authority owner (Stephon Morris); holds all strategic decision power.

**State File:** Per-supervisor `.md` file tracking status, run count, error, and full output of last run.

**Task Type:** Domain of work (e.g., "design", "pipeline", "execution-audit"); used for routing and probation tracking.

**Token Budget:** Expected input + output token count for a task type; used to manage API costs.

**Vault:** Obsidian knowledge base at `/Desktop/kai/`; managed by Stefan with Kairo's read/write authority.

---

## 12. Document Governance

**Document Owner:** Kairo (clawd workspace)  
**Last Updated:** 2026-07-26  
**Next Review:** 2026-10-26 (quarterly)  
**Approval Authority:** Stefan Mundow  
**Status:** ACTIVE — Foundation for system operations  

**Version History:**
- 2.0 (2026-07-26): Initial SAD publication; governance, token efficiency, compliance boundaries added
- 1.0 (2026-07-03): Original ARCHITECTURE.md published

**Change Log:**
| Date | Change | Author |
|---|---|---|
| 2026-07-26 | Separated governance document from technical architecture | Kairo |
| 2026-07-26 | Formalized Stef/Kairo delegation model | Kairo |
| 2026-07-26 | Added token efficiency constraints section | Kairo |
| 2026-07-26 | Documented compliance boundaries and audit trail | Kairo |

---

**END OF SYSTEM ARCHITECTURE DOCUMENT**
