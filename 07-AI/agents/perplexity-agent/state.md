---
agent: perplexity-agent
display_name: "Perplexity"
emoji: "🔭"
role: "Real-Time Research · Citations"
status: "running"
last_run: "2026-08-10T18:43:42.033Z"
current_task: null
runs_completed: 199
items_processed: 199
last_error: null
color: "#20808D"
house: "providers"
---

# Loop Rules

## Loop Start
1. Caller (run-agents.sh or a schedule routine) invokes `node ~/clawd/agents/perplexity-agent/run.js "<task>"`
   with a task matching this agent's routing rule (current events, prices, "who won",
   anything needing citations) — see `~/Desktop/Context/Tools/TOOLS.md` Task Routing section.
2. `run.js` sets this file's status to running, posts a `loop-start` bus message, calls Perplexity once.

## Loop End
1. `run.js` updates this file's `status`, `last_run`, `runs_completed`, `items_processed`, `last_error`
2. `run.js` posts one `loop-end` bus message and acks
3. `run.js` appends one summary line to `~/Desktop/kai/07-AI/chatroom/feed.md`

Note: the bus is a check-in log, not a task queue — this agent does one unit of work per
invocation (the task comes from the caller as an argument), matching how codex/antigravity work.

## Notes
- Runtime code: `~/clawd/agents/perplexity-agent/run.js`
- Model: `sonar` by default (cheapest tier) — upgrading to `sonar-pro` requires an explicit per-task flag
- Requires `PERPLEXITY_API_KEY` in `~/clawd/.env` — stays `not-provisioned` until set.
- Get a key at perplexity.ai/settings/api (requires a payment method on file — no free tier).

[2026-08-09T21:46:53.687Z] research via sonar: SUCCESS cost_usd=0.005050 billing=api measured=true trace=20260809T214653687Z-kairo-16u7
[2026-08-09T21:53:11.924Z] research via sonar: SUCCESS cost_usd=0.005040 billing=api measured=true trace=20260809T215311924Z-kairo-180i