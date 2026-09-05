---
agent: codex
display_name: "Codex"
emoji: "💻"
role: "Code Agent · GitHub Sync"
status: idle
last_run: "2026-09-05T20:35:00Z"
current_task: "Run 278: Task = review GitHub repos + fix open issues. FIX SHIPPED for the bug run 277 filed: -Community_intake_Routing #7 (how_heard attribution pollutes intent scoring) -> PR #8 opened (branch fix/howheard-attribution-pollution, base claude/quirky-galileo-UGnfz), closes #7. One-line fix in BOTH intake.js + api/intake.js: classify on interest_description only; how_heard still logged, not routed. Verified 10/10 via /tmp/verify7.mjs (differential, real classify() from each file): 4 learner-with-partner-source cases now learner@0.99 (were partner@0.8 misroute / 0.65 corrupted); control genuine partner still partner@0.909. Orthogonal to #2 (substring) and #5/#6 (no-signal confidence). Community_intake open PRs now #2,#6,#8 awaiting founder merge (all independent). STILL OPEN needing founder merge: job_scanner #19 (canonical); Community_intake PRs #2,#6,#8; psychic-bassoon #22/#20/#19; Enrollment #14/#16/#18/#20. 204-277 in .remember/."
runs_completed: 278
items_processed: 519
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
