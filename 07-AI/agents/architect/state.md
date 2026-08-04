---
agent: architect
role: System Design Supervisor
mode: "full"
status: "running"
last_run: "2026-08-04T01:07:53.055Z"
current_task: "Design a REST API for OAuth2"
active_spec: "Design a REST API for OAuth2"
runs_completed: 1
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
*2026-08-04 (lite)*

To design this task effectively, I need a few clarifications:

1. **What system does this relate to?** Is this for an API, database, microservice, frontend testing, deployment pipeline, or something else?

2. **What does "lite" mean?** Is it:
   - A simplified/minimal version of full health checks?
   - Only retesting failed checks from a previous run?
   - Fast-path checks without deep diagnostics?

3. **What are you retesting?** What did the original health check do, and what failed?

4. **What's the output format?** Do you need a report, metrics, pass/fail status, or detailed logs?

Once I understand the context, I can give you a proper design with the three-section format:
- **What** (one sentence)
- **Steps** (numbered concrete actions)
- **Done When** (3 testable bullets)
