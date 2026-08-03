# Architecture Decision Records (ADRs)
## OpenClaw AI Organization — Stefan Mundow's Kairo System

**Document ID:** 2-ADRs.md  
**Version:** 1.0  
**Date:** 2026-07-26  
**Organization:** Stefan AI (Kairo/Clawd)  
**Related:** 1-SAD.md (System Architecture Document)  
**Status:** ACTIVE

---

## ADR-001: Multi-Identity Delegation Model (Stef ↔ Kairo)

### Title
Multi-Identity Delegation: Stef as Human Decision Authority; Kairo as AI Executor

### Context

Stefan Mundow operates across multiple concurrent tracks (Plug AI, Puppy Power, BigHeart Health) with finite attention. No single AI agent can make legitimate decisions on his behalf. However, delegating *execution* to trustworthy AI is unavoidable if the system is to move at necessary speed.

**Constraints:**
- Stefan retains veto power on all external communications and strategic moves
- Kairo must operate under explicit standing authorization for certain domains
- Risk: Kairo makes a decision Stef didn't actually authorize
- Precedent: AGENTS.md Rule 4 (Kai's vault autonomy, 2026-07-05) already established this pattern

### Decision

**Adopt a two-tier delegation model:**

1. **Stef's Tier (Authority):**
   - All strategic decisions (priorities, funding, pivots)
   - All external communications (email, GitHub issues, Telegram posts)
   - All legal/financial commitments
   - Approval on public work or reputational moves
   - **Default stance:** Explicit approval required

2. **Kairo's Tier (Delegated Autonomy):**
   - Full read/write access to `/Users/abdoulayemundow/Desktop/kai/` (Obsidian vault) — PARA folders + personal PKB
   - Orchestration of task routing (which agent handles which work)
   - Internal documentation (ADRs, specs, audit trails)
   - Updating context.md and state files
   - Posting to internal message bus (.bus/bus.sqlite)
   - **Standing authorization:** No per-action approval needed (but must update context.md after)
   - **Exception:** External APIs or side-effects still require explicit invocation

### Consequences

**Positive:**
- System moves at human speed (Stef decides at 9 AM, work is decomposed/executed by 10 AM)
- Clear boundary between authority (Stef) and execution (Kairo)
- Audit trail in context.md captures what Kairo did and why
- Extensible: New supervisors inherit same delegation pattern

**Negative:**
- Kairo must accurately understand Stef's intent (requires good prompt contracts)
- If context.md drifts, Kairo can make mistakes that seem authorized but aren't
- Requires discipline: Stef must update context.md when priorities shift
- Single point of failure: If Kairo misinterprets a standing authorization, work could be wasted

**Mitigation:**
- Rule 0 (prompt contracts) ensures non-trivial tasks are clarified before execution
- Rule 1 (context.md is gospel) makes drift visible
- Daily audit (Aexis supervisor) flags unexpected decisions
- Escalation protocol: If Kairo feels ambiguous, it asks for clarification (posts to bus)

### Alternatives

**A1: Full Kairo Autonomy**
- Kairo makes all decisions without approval
- Risk: Kairo optimizes for the wrong goal
- Rejected: Violates Stef's authority principle

**A2: Full Stef Approval**
- Every action requires explicit Stefan approval
- Risk: Severe bottleneck; system can't move
- Rejected: Defeats the purpose of having AI

**A3: Role-Based Committee**
- Multiple humans (Stefan + others) vote on decisions
- Risk: Overkill for single-human operation; scaling problem later
- Rejected: Not applicable until Stef adds team members

### Owner
Kairo (delegated by Stefan Mundow, 2026-07-05 via AGENTS.md Rule 4)

### Status
ACCEPTED — Foundation of system

---

## ADR-002: 8-Supervisor Specialized Network vs. Monolithic LLM

### Title
Supervisor Specialization: 8-Supervisor Hierarchy vs. Single Generalist Agent

### Context

OpenClaw AI can invoke Claude directly for any task (monolithic), or route work to specialized supervisors (modular). Single-agent approach is simpler; multi-supervisor approach enables:
- Cost optimization (use Haiku for cheap tasks, Sonnet for hard ones)
- Task-specific prompt optimization
- Health monitoring (track success rate per domain)
- Horizontal scaling (add supervisors in parallel if needed)

**Current Design:**
- 8 active supervisors: Claude, Architect, Orchestrator, Aexis, Aeos, Perplexity, Antigravity, Codex
- Each has single domain: design, pipeline decomposition, audit, synthesis, research, content, code
- Stateless: operate via request-response, no persistent connections
- Subprocess-based: invoked on-demand via Node.js, exit after task

### Decision

**Adopt 8-supervisor specialized network with optional Haiku/Sonnet model selection per domain.**

**Routing Logic:**
```
IF task = design_spec THEN Architect (Sonnet full, or Haiku lite)
ELSE IF task = pipeline_decomposition THEN Orchestrator (Haiku)
ELSE IF task = execution_audit THEN Aexis (Haiku)
ELSE IF task = strategic_synthesis THEN Aeos (Haiku)
ELSE IF task = realtime_research THEN Perplexity (API)
ELSE IF task = content_creation THEN Antigravity (TBD)
ELSE IF task = code_generation THEN Codex (TBD)
ELSE task = general THEN Claude (Haiku default)
```

**Supervisor Manifest:**

| Supervisor | Domain | Model | Cost | Status |
|------------|--------|-------|------|--------|
| Architect | System design, ADRs, specs | Haiku (lite) / Sonnet (full) | $0.0005–0.003 | Active |
| Orchestrator | Goal decomposition, pipelines | Haiku | $0.002 | Active |
| Aexis | Execution audit, open loops | Haiku | $0.002 | Active |
| Aeos | Strategic synthesis, intelligence | Haiku | $0.003 | Active |
| Perplexity | Real-time research, citations | Perplexity API | $0.005 | Active |
| Antigravity | Marketing content, LinkedIn | TBD | $0 | Planned |
| Codex | Code generation, bug fixes, PRs | TBD | $0 | Planned |
| Claude | Fallback general purpose | Haiku | $0 | Active |

### Consequences

**Positive:**
- **Cost optimization:** 80% cheaper than using Sonnet for all tasks
- **Quality:** Prompt optimization per domain (Architect prompt ≠ Audit prompt)
- **Health visibility:** Success rate per task type in registry.json
- **Scaling:** Easy to add more supervisors (e.g., Security Auditor, Compliance Checker)
- **Modularity:** Can swap Claude for Claude Next, or add Gemini, without rewriting all logic
- **Predictability:** Output format is consistent per supervisor

**Negative:**
- **Routing overhead:** Must decide which supervisor handles which task (small overhead, ~50 ms)
- **Cold start:** Each supervisor subprocess startup takes ~100 ms (vs. direct API call)
- **Code duplication:** Each supervisor has similar boilerplate (mitigated by shared template)
- **Failure isolation:** If one supervisor breaks (e.g., Architect probation), must route around it (registry probation logic handles this)

**Mitigation:**
- Supervisor templates enforce consistency
- Registry tracks health; bad supervisors are automatically skipped
- Fallback chain: If specialist unavailable, route to Claude
- Caching: Prompt templates use Claude prompt caching to reduce token cost

### Alternatives

**A1: Monolithic Claude for Everything**
- Single API call, no routing
- Pros: Simple, predictable latency
- Cons: 5-10x more expensive; no domain-specific optimization; harder to debug
- Rejected: Violates cost-first principle

**A2: Cloud Orchestration (AWS Step Functions, etc.)**
- Managed routing, distributed agents
- Pros: Scales to 1000+ supervisors
- Cons: Adds $50–200/month overhead; overkill for current scale
- Rejected: Not needed yet; revisit if scale > 20 tasks/day

**A3: Single Supervisor with Role-Based Prompting**
- One agent that role-plays (Architect mode, Auditor mode, etc.)
- Pros: Simpler setup, easier to modify
- Cons: Role-play is less reliable than specialized code; harder to track per-domain success
- Rejected: Less robust than specialization

### Owner
Kairo (system designer)

### Status
ACCEPTED — Core to current architecture; proven in early runs

---

## ADR-003: Token-Efficiency-First Context Management

### Title
Context Injection: Selective Read-Only Access vs. Full-Context Omniscience

### Context

LLM API costs scale with token count. Total cost = (input_tokens + output_tokens) × rate.

**Current Spend:**
- ~50 tokens/call setup + prompt
- ~1000–3000 tokens context.md per call
- ~500–800 tokens output per call
- = ~2000 tokens avg per task × 50 tasks/month = 100K tokens/month ≈ $0.20–0.30

**Tension:**
- More context → better decisions (Aeos needs full project state)
- More context → higher token cost (context.md is 2000+ tokens)
- Architects don't need context (intentional fresh eyes on design)
- Orchestrators must read context (need to understand current state to route)

### Decision

**Adopt selective context injection with three tiers:**

**Tier 1 — Context Required (read context.md at loop start):**
- Orchestrator (needs to route based on current state)
- Aexis (needs to find open loops)
- Aeos (needs to synthesize strategically)
- **Token cost:** ~2000 per call, acceptable for these domains

**Tier 2 — Context Optional (read only on explicit request):**
- Architect (intentionally works from fresh perspective; read context only for full design, not lite)
- Perplexity (only reads query, not context)
- **Token cost:** ~300–500 per call

**Tier 3 — No Context (task description only):**
- Claude (fallback general use)
- Antigravity (given brief from Orchestrator pipeline)
- Codex (given brief from Orchestrator pipeline)
- **Token cost:** ~50–100 per call

**Implementation:**
```javascript
// Tier 1: Orchestrator
const context = readFileSync('/Users/abdoulayemundow/Desktop/Context/context.md', 'utf-8')
const response = await callClaude(orchestratorPrompt(task, context))

// Tier 2: Architect (lite mode)
const response = await callClaude(architectPromptLite(task))  // no context

// Tier 2: Architect (full mode)
const context = readFileSync('/Users/abdoulayemundow/Desktop/Context/context.md', 'utf-8')
const response = await callClaude(architectPromptFull(task, context))

// Tier 3: Claude
const response = await callClaude(generalPrompt(task))  // no context
```

**Cache Strategy:**
- Prompt templates: Use Claude prompt caching API (one-time ~10% cost, then cached)
- Context.md: Cache in memory for 5 minutes across supervisor calls
- Registry.json: Cache for 5 minutes (doesn't change often)

### Consequences

**Positive:**
- **Cost reduction:** ~30–40% cheaper than full-context for all tasks
- **Latency:** Smaller prompts = slightly faster API response
- **Quality:** Architects think better with fresh eyes; Aexis finds open loops with full picture
- **Modularity:** New supervisors can choose context needs independently

**Negative:**
- **Complexity:** Must maintain mapping of {supervisor → context_tier}
- **Inconsistency:** Different supervisors see different "truth"
- **Bug risk:** If context.md has stale info, Tier 1 supervisors make stale decisions
- **Mitigation:** Rule 4 (AGENTS.md) requires context.md update after every loop

**Mitigation:**
- Document context tier in registry.json
- Add assertion: if context.md is >1 day old, Orchestrator flags it
- Caching layer validates freshness (mtime check)

### Alternatives

**A1: Full Context for All Tasks**
- Every supervisor reads entire context.md
- Pros: Uniform view of truth
- Cons: 2x token cost; wastes tokens on tasks that don't need context
- Rejected: Violates cost-first principle

**A2: No Context for Any Task**
- All supervisors work from task description only
- Pros: Minimal tokens; maximum speed
- Cons: Aexis can't find open loops; Aeos can't synthesize; quality drops
- Rejected: Unacceptable quality loss

**A3: Context Compression (Summarization)**
- LLM summarizes context.md to 500 tokens before passing to other supervisors
- Pros: Smaller size, preserve semantic content
- Cons: Adds extra API call (~$0.001); one more failure point
- Rejected: ROI not worth it at current scale

### Owner
Kairo (system designer)

### Status
ACCEPTED — Implemented and tuned

---

## ADR-004: Mandatory Compliance Enforcement via AGENTS.md

### Title
Compliance as Code: Binding Agent Rules via AGENTS.md (Not Guidance, Not Suggestions)

### Context

Multi-agent systems need coordination rules. Without them:
- Agents re-read context.md redundantly (wasted tokens)
- Agents forget to post to bus (silent work, hard to debug)
- Agents skip context updates (stale information spreads)
- New agents (Codex, Antigravity) repeat mistakes of earlier agents

**Current State:**
- AGENTS.md exists at `/Users/abdoulayemundow/Desktop/Context/Agents/AGENTS.md`
- Contains 12 binding rules (Rule 0–12)
- All agents read it at loop start (Rule 1B)
- Rules cover: prompt contracts, context reading, bus check-in, loop sequence, memory management

**Problem:**
- Rules are documented but not enforced (no active linter/validator)
- Agent could skip Rule 1 (read context) and nobody knows
- Compliance audit requires manual review of bus logs

### Decision

**Adopt AGENTS.md as the binding specification for every agent. Make non-compliance visible and escalate.**

**The 12 Rules (binding, not optional):**
1. **Rule 0:** Establish prompt contract before non-trivial work (defines GOAL, CONSTRAINTS, FORMAT, FAILURE)
2. **Rule 1B:** Read TOOLS.md and SKILLS.md, check bus every loop
3. **Rule 1:** Read context.md at start of loop (single source of truth)
4. **Rule 3:** Define "loop" as task boundary or heartbeat cycle
5. **Rule 4:** Update context.md after every loop if anything changed
6. **Rule 5:** Resolve conflicts (don't duplicate stale info)
7. **Rule 6:** Memory is files, not headspace (write to files)
8. **Rule 1C:** Subagent lookup via index first (not full file)
9. **Rule 7:** Safety (no exfiltration, ask before destructive ops)
10. **Rule 8:** Know when to speak (quality over noise)
11. **Rule 9:** Match format to platform (Discord/WhatsApp/Telegram formatting)
12. **Rule 10:** Tools and Skills (check SKILLS.md before executing)
13. **Rule 11:** Explicit loop sequence (startup → work → checkpoint)
14. **Rule 12:** Inheritance (new agents inherit rules unless explicitly exempted)

**Enforcement Mechanism:**

At loop start, every agent must:
1. Load AGENTS.md
2. Check its agent_name against the signature
3. Validate that previous loop had context.md update (if non-trivial work occurred)
4. Post a loop-start message to bus with checklist (context read? ✓, contract established? ✓, etc.)

If compliance check fails:
- Agent logs `COMPLIANCE_VIOLATION: [rule] not met` to bus
- Kairo receives alert on next bus check
- Escalate to Stef if repeated violations

**Exemptions:**
- Trivial operations (single-line fixes, direct factual answers) don't need full contract
- Read-only operations don't need context.md write-back
- Boundary defined in TOOLS.md (each workspace can tune this)

### Consequences

**Positive:**
- **Consistency:** Every agent follows same sequence; no outliers
- **Auditability:** Bus log shows compliance status per agent per loop
- **Onboarding:** New agents (Codex, Antigravity) have clear rules; less guesswork
- **Scaling:** Rules scale to multi-human teams without change
- **Quality:** Prompt contracts reduce ambiguity; fewer rework cycles

**Negative:**
- **Overhead:** Loop startup takes ~500 ms extra (read files, validate rules)
- **Strictness:** Some agents might chafe at mandatory context reads (mitigated by Rule 1B bus check)
- **False Positives:** If context.md is unchanged, write-back is wasted (mitigated: check before writing)
- **Maintenance:** Rules must evolve with system; require quarterly review

**Mitigation:**
- Compliance check is cached (only run at actual loop start, not per-sub-task)
- Context.md write is idempotent (no harm if unchanged content re-written)
- Exemption list (TOOLS.md) prevents over-enforcement on trivial work
- Quarterly rule review (aligned with system SAD update)

### Alternatives

**A1: Guidance Only (Current)**
- Rules documented but not enforced
- Pros: Flexible; less overhead
- Cons: Agents skip rules silently; hard to debug; repeating mistakes
- Rejected: Doesn't scale to multi-agent

**A2: External Compliance Checker**
- Separate agent audits other agents' compliance
- Pros: Decoupled; can run in background
- Cons: Adds 1–2 seconds latency; overhead of extra agent
- Rejected: Too complex for current scale

**A3: Machine-Readable Rules (AGENTS.yaml)**
- Rules in structured format with validation schema
- Pros: Can auto-lint against schema
- Cons: Overkill overhead; makes rules harder to read
- Rejected: Plain text AGENTS.md is working fine

### Owner
Stefan Mundow (authority), Kairo (enforcement)

### Status
ACCEPTED — Implemented via AGENTS.md; enforcement via Rule 1B bus check-in

---

## ADR-005: Telegram Gateway Integration Strategy

### Title
Telegram as Async Task Inbox: Sync vs. Native API vs. Webhook

### Context

Stefan works on-the-go (field work, meetings, travel). Telegram is his primary communication channel. Current system is desktop-only (Obsidian, Claude Code).

**Use Cases:**
1. Stefan sends task: "@kairo redesign homepage" → Kairo routes to Architect, posts result back
2. Stefan asks question: "What's the status?" → Kairo runs Aexis audit, returns summary
3. Kairo posts urgent alert: "Deadline tomorrow on grant deadline" → Stefan sees notification
4. Stefan approves work: "👍 looks good" → triggers external action (GitHub push, email send)

**Integration Options:**

1. **Native Telegram Bot (webhooks):**
   - Kairo runs a bot; Telegram sends updates to webhook
   - Pros: Real-time, low latency, native experience
   - Cons: Requires public server (security risk), harder to debug

2. **Polling (every 30 seconds):**
   - Kairo checks Telegram inbox via API, pulls new messages
   - Pros: No public server, simpler, works behind NAT
   - Cons: 30-second latency, wastes API calls

3. **Native Sync (monthly):**
   - Manual: Stefan opens Telegram, checks, runs tasks on desktop
   - Pros: Zero new complexity
   - Cons: Defeats the purpose (not async, not urgent)

### Decision

**Adopt hybrid Telegram strategy:**

**Phase 1 (Immediate: polling):**
- Kairo runs polling loop every 5 minutes (via schedule skill)
- Checks Telegram inbox for new messages to `@kairo_ai_bot`
- Messages format: `@kairo [task description]` or `@kairo [supervisor] [task]`
- Routes to appropriate supervisor (parse message for routing hints)
- Posts result back to Telegram (text, or link to full output if >4096 chars)
- Posts to internal bus for audit trail

**Phase 2 (Q3 2026: native webhooks):**
- If polling latency becomes issue, move to webhook-based architecture
- Requires: public server, SSL cert, firewall rules
- Only then if Stef explicitly requests it

**Message Format Examples:**
```
@kairo audit                           → Aexis runs, returns summary
@kairo architect design homepage       → Architect runs full spec
@kairo architect --lite homepage       → Architect lite mode
@kairo research funding rounds health  → Perplexity search, returns link
@kairo 👍                              → Stefan approval signal (context-dependent)
```

**Architecture:**

```
┌─────────────────────────────────────────────────────────┐
│ Telegram: Stefan sends message to @kairo_ai_bot         │
└─────────────────────────────────────────────────────────┘
                     │
                     v (every 5 minutes)
┌─────────────────────────────────────────────────────────┐
│ Schedule Task (Node.js): Poll Telegram API              │
│  - Get updates since last checkpoint                    │
│  - Filter for messages to @kairo_ai_bot                 │
└─────────────────────────────────────────────────────────┘
                     │
                     v
┌─────────────────────────────────────────────────────────┐
│ Kairo Telegram Agent (clawd agent)                      │
│  - Parse message, extract task                          │
│  - Route to appropriate supervisor (Architect, Aexis)   │
│  - Call supervisor subprocess                           │
└─────────────────────────────────────────────────────────┘
                     │
                     v
         ┌───────────┴─────────────────┐
         │                             │
    ┌────v────┐                   ┌────v────┐
    │Architect│                   │  Aexis  │ (etc.)
    └────┬────┘                   └────┬────┘
         │                             │
         v                             v
    (produces spec)              (produces audit)
         │                             │
         └─────────────┬───────────────┘
                       │
                       v
    ┌──────────────────────────────────┐
    │Post Result to Telegram           │
    │ - If <4096 chars: full text      │
    │ - If >4096 chars: link to vault  │
    └──────────────────────────────────┘
                       │
                       v
    ┌──────────────────────────────────┐
    │Post to Internal Bus (audit trail)│
    └──────────────────────────────────┘
```

**Configuration:**
- Store Telegram bot token in `.env` (never commit)
- Store last_message_id in state file (idempotency)
- Poll every 5 minutes via schedule skill (`schedule "*/5 * * * * kairo-telegram-poll"`)

### Consequences

**Positive:**
- **Async mobility:** Stefan can task from anywhere, get results on Telegram
- **Speed:** 5-minute latency is acceptable for most tasks
- **Simplicity:** Polling is easier than webhooks (no public server needed)
- **Audit trail:** All Telegram activity logged to bus and context.md
- **Separation:** Telegram is just a UI; core logic remains in clawd

**Negative:**
- **Latency:** 5-minute polls mean task won't start for up to 5 minutes
- **Message ordering:** Multiple rapid messages might batch into one poll cycle
- **Formatting:** 4096-char limit on Telegram means some outputs won't fit (redirect to vault)
- **Security:** Bot token in `.env` is sensitive (use secrets management in future)

**Mitigation:**
- Decrease polling interval to 1 minute if latency becomes issue
- Queue mechanism: supervisor bumped to front of queue if urgent
- Markdown link: "Full output here: [link to vault]"
- Rotate bot token quarterly (manual reminder in Heartbeat)

### Alternatives

**A1: Telegram Webhooks (Real-Time)**
- Telegram sends events to public webhook
- Pros: <1 second latency, feels native
- Cons: Requires public server; higher security risk; harder to debug behind NAT
- Rejected for Phase 1: Not needed yet; too much infrastructure
- Accepted for Phase 2: Revisit if polling latency becomes bottleneck

**A2: Discord/Slack Instead**
- Use Discord bot or Slack bot instead
- Pros: Similar capabilities; different UX
- Cons: Doesn't match Stefan's actual workflow (he lives in Telegram)
- Rejected: Must match user's communication preference

**A3: No Integration (Desktop Only)**
- Stick with clawd/OpenClaw on desktop
- Pros: Zero new complexity; no new security surface
- Cons: Not async; requires Stefan to manually invoke; defeats productivity goal
- Rejected: Undermines goal of mobile tasking

### Owner
Kairo (system designer), Stefan (user experience owner)

### Status
PENDING → ACCEPTED (Phase 1 approved for Q3 2026)

---

## ADR-006: Workspace Vault Consolidation Strategy

### Title
Vault Unification: Single Obsidian Vault vs. Split (Workspace + Personal)

### Context

Stefan currently maintains two knowledge bases:
1. **Desktop/kai/** (Obsidian vault): Personal PKB, projects, PARA structure — Kairo's primary authority
2. **clawd/ workspace:** System architecture, agent registry, bus — Kairo's secondary authority

**Current State:**
- ARCHITECTURE.md lives in clawd/
- Agent state files live in Desktop/kai/07-AI/agents/
- Feed.md lives in Desktop/kai/07-AI/chatroom/
- Context.md lives in Desktop/Context/ (external to both vaults)

**Problem:**
- Three sources of truth (clawd, Desktop/kai/, Desktop/Context/)
- Agent output splits across Desktop/kai/ and clawd/
- Makes it harder to reason about full system state
- Sync points are manual and error-prone

### Decision

**Adopt vault consolidation: All Kairo/system output lives in Desktop/kai/. Clawd is source control only (git history), not source of truth.**

**New Structure:**
```
Desktop/kai/
├── _INDEX.md                    (updated daily)
├── Projects/
│   ├── plug-ai/
│   │   ├── spec.md
│   │   ├── roadmap.md
│   │   └── adrs/
│   │       ├── ADR-001.md       (written by Architect)
│   │       └── ADR-002.md
│   └── puppy-power/
│       └── ...
├── Areas/
│   ├── BigHeart-Health/
│   │   ├── status.md
│   │   └── financial.md
│   └── AI-Operations/
│       ├── agents-status.md     (written by Aexis every 24h)
│       ├── registry-snapshot.md (written by Router)
│       └── vault-integrity.md
├── Resources/
│   ├── system-architecture/
│   │   ├── ARCHITECTURE.md      (copied from clawd by Kairo)
│   │   ├── ADRs/                (symlink or copy from clawd)
│   │   └── agent-registry/
│   │       ├── supervisor-specs.md
│   │       └── routing-logic.md
│   └── design-patterns/
├── Archive/
│   └── (completed work)
├── 07-AI/
│   ├── agents/
│   │   ├── orchestrator/
│   │   │   └── state.md         (output of last run)
│   │   ├── architect/
│   │   │   └── state.md
│   │   ├── aexis/
│   │   │   └── state.md
│   │   └── ...
│   ├── chatroom/
│   │   └── feed.md              (permanent activity log)
│   └── vault-sync/
│       └── last-sync.md         (timestamp, status)
└── (Personal PKB: Identity, Psychology, etc.)

clawd/ (git repo)
├── AGENTS.md                    (redirect stub to Desktop/Context/Agents/AGENTS.md)
├── ARCHITECTURE.md              (link to or managed copy)
├── 2-ADRs.md                    (managed copy, source of truth is vault)
├── .bus/
│   ├── busctl.js                (active)
│   └── bus.sqlite               (transient; not synced)
├── agents/
│   ├── orchestrator-agent/
│   ├── architect-agent/
│   └── (runtime-only; don't edit here)
└── router/
    ├── registry.json            (transient health data)
    └── subagents-index.txt      (managed copy)
```

**Sync Strategy:**

1. **Daily Sync (via schedule or heartbeat):**
   - Kairo reads `/clawd/ARCHITECTURE.md` (clawd is git repo)
   - Copies or links to `Desktop/kai/Resources/system-architecture/ARCHITECTURE.md`
   - Kairo reads `/clawd/2-ADRs.md`, links in vault
   - Kairo reads `router/registry.json` snapshot, writes summary to `Areas/AI-Operations/registry-snapshot.md`

2. **Event-Driven Sync:**
   - Every agent run: write state.md to `Desktop/kai/07-AI/agents/[supervisor]/`
   - Every Aexis audit: write output to `Areas/AI-Operations/agents-status.md`
   - Every design task: copy final Architect output to `Projects/[project]/adrs/` (if approved by Stefan)

3. **No Bi-Directional Sync of Code:**
   - clawd/ remains the source control repo (GitHub)
   - Desktop/kai/ mirrors key docs (for reference, not editing)
   - Rule: Edit `.js` files in clawd/, doc files in Desktop/kai/

### Consequences

**Positive:**
- **Single source of truth:** Desktop/kai/ is Kairo's vault; clawd/ is source control
- **Faster context reading:** Agents read from vault (organized by PARA) instead of scattered files
- **Better discovery:** Stefan can browse vault and see all Kairo work in one place
- **Scalability:** Easy to add new projects; PARA structure handles growth
- **Obsidian UX:** Full search, backlinking, daily notes — only in vault

**Negative:**
- **Sync overhead:** Must maintain daily copy/symlink logic (~100 ms extra per loop)
- **Storage duplication:** Some files appear in both clawd/ and vault (mitigated: use symlinks)
- **Coordination:** New agents must know to write to vault, not clawd/
- **Git history:** Code changes in clawd/; documentation changes in vault (separate histories)

**Mitigation:**
- Use symlinks (from clawd/ to vault/) to avoid duplication
- Automate sync via schedule task (cheap, runs once daily)
- Document file ownership: which agent writes which file
- Quarterly: resolve broken symlinks, audit sync integrity

### Alternatives

**A1: Dual Vaults (Current State)**
- Keep both clawd/ and Desktop/kai/; accept duplication
- Pros: No sync overhead; clear separation (code vs. docs)
- Cons: Confusion about source of truth; wasted tokens reading scattered files
- Rejected: Scales poorly

**A2: Merge Into Clawd Git Repo**
- Make clawd/ the single repo; drop Obsidian vault
- Pros: Single history; no sync needed
- Cons: Loses Obsidian UX (search, dailies, backlinks); clawd/ becomes 1000+ files
- Rejected: Obsidian is Stefan's primary knowledge tool; can't abandon it

**A3: Cloud Sync (Notion, Roam, etc.)**
- Use cloud-based PKB instead of Obsidian
- Pros: Sync is automatic; accessible from phone
- Cons: Privacy risk; cloud cost; slower than local Obsidian
- Rejected: Stefan's vault is sensitive; prefer local storage

### Owner
Kairo (system designer), Stefan (vault owner)

### Status
ACCEPTED — Implement Phase 1 (manual daily sync); Phase 2 (automated schedule)

---

## ADR-007: Subagent Indexing and Discovery Strategy

### Title
Agent Discovery: Fast Index vs. Full Registry Scan for Supervisor Routing

### Context

OpenClaw has a growing agent fleet:
- Core supervisors: Architect, Orchestrator, Aexis, Aeos, Perplexity (5)
- Planned agents: Codex, Antigravity, Compliance Checker, Security Auditor (4+)
- External subagents: Gemini (archived), Groq (potential), Claude Next (future)
- Total manifest: 12,000+ words in `router/subagents.json`

**Current Problem:**
- AGENTS.md Rule 1C warns against loading full `subagents.json` at loop start (burns tokens)
- But routing decisions need to know: "Which agent handles `task_type=code_review`?"
- Current workaround: Hardcoded routing in supervisor code (doesn't scale)

**Scaling Tension:**
- If 100 subagents exist, can't hardcode route all of them
- Full manifest read costs 5000+ tokens per loop (unacceptable)
- Index is small (1600 words) but loses detail (agent capabilities, cost, latency)

### Decision

**Adopt two-tier agent discovery: Index-first for routing decisions, full manifest only on match.**

**Tier 1: Subagent Index** (`router/subagents-index.txt`)

```
Format (tab-separated, one agent per line):
persona_id | name | capability_tags | status | cost_per_call

ae7d3b29 | architect-agent | design,spec,adr,system-architecture | active | 0.005
c4f2a8e1 | orchestrator-agent | pipeline,decomposition,workflow,planning | active | 0.002
d9e5f1c6 | aexis-agent | audit,open-loops,accountability,status | active | 0.002
f2g6h9k2 | aeos-agent | synthesis,strategy,intelligence,brief | active | 0.003
...
```

**Advantages:**
- Size: ~1600 words (100x smaller than full manifest)
- Fast: Can scan all agents in <100 ms
- Token cost: ~0.0002 (negligible)
- Format: Human-readable tab-separated for easy parsing

**Tier 2: Supervisor Manifest** (`router/subagents.json`)

Full detail per agent:
- Model, prompt template
- Input constraints, output format
- Cost, latency, success rate
- State (active, probation, archived)
- Links to code, docs

**Only loaded if index match found.**

**Routing Algorithm:**

```javascript
async function routeTask(task) {
  // 1. Load index (cheap)
  const index = readFileSync('./router/subagents-index.txt', 'utf-8')
  
  // 2. Parse index, find matches
  const matches = parseIndex(index).filter(agent => 
    agent.capability_tags.includes(task.type)
  )
  
  if (matches.length === 0) {
    // No match found; escalate to Kairo
    return { router: 'kairo', task, reason: 'no-agent-found' }
  }
  
  // 3. Load full manifest for top 3 matches (cheap: 3K tokens max)
  const fullManifests = await Promise.all(
    matches.slice(0, 3).map(m => 
      loadManifest('./router/subagents.json', m.persona_id)
    )
  )
  
  // 4. Rank by success_rate, latency, cost
  const best = rankAgents(fullManifests, task)
  
  // 5. Check probation status from registry
  if (best.on_probation[task.type]) {
    return fallback(task, reason='on-probation')
  }
  
  // 6. Route to best agent
  return invokeAgent(best, task)
}
```

**File Manifest:**

| File | Purpose | Owner | Update Cadence |
|------|---------|-------|-----------------|
| `router/subagents-index.txt` | Fast discovery index | Kairo | After new agent added |
| `router/subagents.json` | Full manifest (detailed specs) | Kairo | After new agent added |
| `router/registry.json` | Health + probation data | Router | Every agent run (append only) |
| `.bus/bus.sqlite` | Message log | Bus | Every post |

**Discovery Flow (at task routing time):**

```
Task arrives: "redesign homepage"
    ↓
Router checks index: what capability_tags match "design"?
    ↓
Found: architect-agent (design,spec,adr,...)
    ↓
Router loads architect details from subagents.json
    ↓
Router checks registry: architect on probation?
    ↓
No → invoke architect-agent
Yes → route to fallback (claude-base)
```

### Consequences

**Positive:**
- **Scalability:** Supports 1000+ agents without token blowup (index is constant size)
- **Speed:** Index scan is ~50 ms; full manifest load is lazy (only on match)
- **Simplicity:** Single hardcoded routing algorithm; easy to test
- **Extensibility:** New agents just need one line in index (no code change)
- **Transparency:** Stefan can see all agents via index without token cost

**Negative:**
- **Maintenance:** Must keep index and manifest in sync (risk: outdated index)
- **Partial info:** Index doesn't capture full capability (only tags)
- **Two-file dependency:** Router must read both files (failure point if one is stale)
- **Tag explosion:** If tags aren't standardized, routing becomes fuzzy

**Mitigation:**
- Validation script: Check that index and manifest have same persona_ids
- Quarterly: Audit index and manifest for drift
- Standard tags: Define fixed set (design, code, audit, synthesis, research, etc.)
- Fallback: If manifest load fails, route to claude-base with full context

### Alternatives

**A1: Full Manifest Always**
- Load subagents.json at every route decision
- Pros: Complete information; no sync risk
- Cons: 5000+ tokens per loop × 50 tasks/month = expensive; 2x token cost
- Rejected: Violates cost-first principle

**A2: Hardcoded Routing (Current)**
- Route decisions hardcoded in supervisor code
- Pros: Fast, predictable
- Cons: New agent requires code change; doesn't scale beyond 10 agents
- Rejected: Can't scale to 100+ agents

**A3: Redis Cache (Distributed)**
- Cache manifest in Redis; TTL 5 min
- Pros: Scales to multiple machines; shared cache
- Cons: Adds Redis dependency; overkill for current scale; $10/month overhead
- Rejected: Not needed yet; revisit if multi-machine

**A4: Hierarchical Fallback**
- Index → if miss, ask Kairo → if still miss, escalate to Claude
- Pros: Graceful degradation; supports dynamic agent discovery
- Cons: Slower (3 round-trip potential); more complex logic
- Rejected: Overkill for current stable agent roster

### Owner
Kairo (router), Stefan (agent oversight)

### Status
ACCEPTED — Implement two-tier discovery with index-first strategy

---

## Summary & Cross-ADR Dependencies

| ADR | Decision | Key Dependencies | Implementation Status |
|-----|----------|------------------|----------------------|
| ADR-001 | Multi-identity (Stef ↔ Kairo) | None (foundation) | ACTIVE |
| ADR-002 | 8-supervisor hierarchy | ADR-001 | ACTIVE |
| ADR-003 | Token-efficient context | ADR-002 | ACTIVE |
| ADR-004 | AGENTS.md compliance | ADR-001, ADR-003 | ACTIVE (via Rule 1B) |
| ADR-005 | Telegram gateway | ADR-001, ADR-002, ADR-004 | PENDING (Phase 1 Q3) |
| ADR-006 | Vault consolidation | ADR-001, ADR-002, ADR-004 | ACCEPTED (Phase 1 manual) |
| ADR-007 | Subagent discovery | ADR-002, ADR-003 | ACCEPTED (implement next) |

**Implementation Roadmap:**
- **Now (2026-07-26):** ADR-001–004 active; ADR-006 Phase 1 (manual sync); ADR-007 planning
- **Q3 2026:** ADR-005 Phase 1 (Telegram polling); ADR-007 automated indexing
- **Q4 2026:** ADR-005 Phase 2 (webhooks if needed); ADR-006 Phase 2 (auto-sync)

---

## Document Governance

**Author:** Kairo (AI system designer)  
**Reviewed By:** Stefan Mundow (2026-07-26)  
**Status:** APPROVED — Foundation for ADR-based architecture decisions  
**Next Review:** 2026-10-26 (quarterly, or after major system change)  
**Modification Process:** New ADRs require Stefan approval; existing ADRs updated by Kairo (with summary to context.md)

---

**END OF ARCHITECTURE DECISION RECORDS**
