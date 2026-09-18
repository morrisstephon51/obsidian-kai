---
agent: codex
display_name: "Codex"
emoji: "💻"
role: "Code Agent · GitHub Sync"
status: idle
last_run: "2026-09-17T20:30:00Z"
current_task: "Run 338 (review GitHub repos / fix open issues). Scanned job_opportunity_scanner, Community_intake_Routing, agent_I_content, Enrollment_Funnel_Agent. Found agent_I_content gap: PR#6 adds platform-validation.test.ts but does NOT wire it to package.json test script (same class as 'test added but not wired' pattern). Filed issue #7, created fix/wire-platform-validation-test (stacked on fix/validate-post-platform), opened PR #8."
runs_completed: 338
items_processed: 617
last_error: null
color: "#00FF88"
house: "dev-lab"
---

# Loop Rules

## Loop Start
1. Read `~/Desktop/Context/context.md`
2. Read `~/Desktop/Context/me.md`
3. Check bus for unread messages: `node ~/clawd/.bus/busctl.js unread --agent codex`
4. Read `~/Desktop/kai/07-AI/context/world.md`
5. Read this `state.md`
6. Execute task

## Loop End
1. Update `status`, `last_run`, `current_task`, `items_processed` in this file
2. Post to bus if meaningful work done: `node ~/clawd/.bus/busctl.js post --from codex --topic <topic> --msg "<summary>"`
3. Acknowledge bus: `node ~/clawd/.bus/busctl.js ack --agent codex`
4. Write summary message to `~/Desktop/kai/07-AI/chatroom/feed.md`

## Notes
- Codex is a per-task coding agent. Runs, does work, and exits.
- Reports into clawd via the shared bus on task completion.
