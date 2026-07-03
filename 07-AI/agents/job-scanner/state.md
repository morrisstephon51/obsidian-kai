---
agent: job-scanner
display_name: "JobScout"
emoji: "🔍"
role: "Job Opportunity Scanner · ZipRecruiter"
status: archived
last_run: "2026-06-21T16:30:00Z"
current_task: null
runs_completed: 14
items_processed: 62
last_error: null
color: "#4ECDC4"
house: "watchtower"
---

# Loop Rules

## Loop Start
1. Read `~/Desktop/Context/context.md`
2. Read `~/Desktop/Context/me.md`
3. Check bus for unread messages: `node ~/clawd/.bus/busctl.js unread --agent job-scanner`
4. Read `~/Desktop/kai/07-AI/context/world.md`
5. Read this `state.md`
6. Execute task

## Loop End
1. Update `status`, `last_run`, `current_task`, `items_processed` in this file
2. Post to bus if meaningful work done: `node ~/clawd/.bus/busctl.js post --from job-scanner --topic jobs --msg "<summary>"`
3. Acknowledge bus: `node ~/clawd/.bus/busctl.js ack --agent job-scanner`
4. Write summary message to `~/Desktop/kai/07-AI/chatroom/feed.md`

## Notes
- Scans ZipRecruiter MCP for relevant opportunities.
- Filters for roles aligned with Stefan's Track 1 and Track 2 priorities.

## Archived (2026-07-03)
Correction: real code exists at github.com/morrisstephon51/job_opportunity_scanner (Python, scored real matches as of 2026-06-05 — Greenwood Project 10/10, RSNA 8/10, StrongMind 8/10) — an earlier version of this note wrongly said "zero implementation" because that repo was never cloned locally. The repo is real but dormant (no commits since 2026-06-05) and never wired into this persona's actual loop (run-agents.sh never invokes it). Same category content-pipeline was in before its logic got ported into psychic-bassoon — do that same treatment here before re-activating.
