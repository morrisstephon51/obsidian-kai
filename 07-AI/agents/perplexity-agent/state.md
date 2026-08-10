---
agent: perplexity-agent
display_name: "Perplexity"
emoji: "🔭"
role: "Real-Time Research · Citations"
status: "running"
last_run: "2026-08-10T23:32:46.391Z"
current_task: "Find open AI-literacy / digital-equity grants for nonprofits in Illinois or nationally with application deadlines more than 7 days out. Exclude the Cook County Digital Equity IMPACT grant and any CVI NOFOs (both closed/out of scope)."
runs_completed: 200
items_processed: 200
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

<!-- KAIRO-LEDGER -->
## Cost Ledger (appended by Kairo — supervisors must not rewrite below this line)

[2026-08-10T23:32:41.534Z] research via sonar: SUCCESS cost_usd=0.005280 billing=api measured=true trace=20260810T233241534Z-kairo-s2x