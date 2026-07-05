---
agent: gemini-agent
display_name: "Gemini"
emoji: "♊"
role: "Long-Context / Multimodal Research Assistant"
status: "running"
last_run: "2026-07-05T03:45:46.175Z"
current_task: null
runs_completed: 0
items_processed: 0
last_error: "Gemini API error 429: { \"error\": { \"code\": 429, \"message\": \"You exceeded your current quota, please check your plan and billing details. For more information on this error, head to: https://ai.google.dev/gemini-api/docs/rate-limits. To monitor your current usage, head to: https://ai.dev/rate-limit. …"
color: "#4285F4"
house: "providers"
---

# Loop Rules

## Loop Start
1. Caller (run-agents.sh or a schedule routine) invokes `node ~/clawd/agents/gemini-agent/run.js "<task>"`
   with a task matching this agent's routing rule (long documents, multi-file synthesis,
   image/video/audio input) — see `~/Desktop/Context/Tools/TOOLS.md` Task Routing section.
2. `run.js` sets this file's status to running, posts a `loop-start` bus message, calls Gemini once.

## Loop End
1. `run.js` updates this file's `status`, `last_run`, `runs_completed`, `items_processed`, `last_error`
2. `run.js` posts one `loop-end` bus message and acks
3. `run.js` appends one summary line to `~/Desktop/kai/07-AI/chatroom/feed.md`

Note: the bus is a check-in log, not a task queue — this agent does one unit of work per
invocation (the task comes from the caller as an argument), matching how codex/antigravity work.

## Notes
- Runtime code: `~/clawd/agents/gemini-agent/run.js`
- Model: `gemini-2.0-flash` by default (cheapest tier)
- Requires `GEMINI_API_KEY` in `~/clawd/.env` — stays `not-provisioned` until set.
- Get a key at aistudio.google.com/apikey.
