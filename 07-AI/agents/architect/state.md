---
agent: architect
role: System Design Supervisor
mode: "full"
status: "running"
last_run: "2026-08-09T20:39:32.331Z"
current_task: "Design an audit logging system for compliance"
active_spec: "Design an audit logging system for compliance"
runs_completed: 8
last_error: null
---

# Architect — General-Purpose System Design Supervisor

Designs systems before Codex builds them. Produces specs, ADRs, and architectural plans for **any project**.
Token-lean: no context.md injection, max_tokens 1024, concise prompts.

Two modes:
- **Full** — Sonnet, structured spec (What/Key Decisions/Spec/Risks/Done When/Handoff)
- **Lite** — Haiku, numbered steps + done-when bullets only

Invocation:
```
node run.js "<design task>" [--mode lite] [--project "name"]
```

Core question: **"What exactly are we building and why, before a single line of code is written?"**

> v1 (Plug AI / BigHeart scoped, max_tokens 2048, context.md injection) archived to `agents/_archived/architect-agent-v1/`

## Active Spec
<!-- Architect writes the current design here -->

## Last Architecture Decision
*2026-08-09 (lite)*

## What
Cache-aside pattern: application checks cache first, loads from source on miss, then populates cache.

## Steps
1. Query cache for key
2. On hit, return value
3. On miss, fetch from database/source
4. Write result to cache with optional TTL
5. Return value to caller

## Done When
- Cache hit returns data without source query
- Cache miss fetches fresh data and stores it
- Stale data can exist until TTL expires or manual eviction

[2026-08-09T21:19:37.015Z] design via claude-sonnet-4-6: TIMEOUT cost_usd=0.000000 billing=subscription measured=false trace=20260809T211937015Z-kairo-so2
[2026-08-09T21:20:38.210Z] design via claude-sonnet-4-6: TIMEOUT cost_usd=0.000000 billing=subscription measured=false trace=20260809T212038210Z-kairo-wck