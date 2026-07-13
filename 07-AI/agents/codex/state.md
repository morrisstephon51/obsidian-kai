---
agent: codex
display_name: "Codex"
emoji: "💻"
role: "Code Agent · GitHub Sync"
status: running
last_run: "2026-07-13T14:30:00Z"
current_task: "Fixed double-publish race in ai-video-reel-generator cron queue. processQueue() selected status=queued rows but never claimed them before publishing — overlapping cron GET + manual POST (or an overrunning cron) could upload the same video to YouTube twice. Added a guarded atomic claim (queued->publishing) so only one worker wins; loser skips. Also added publishing badge style + schema comment. tsc clean. Committed 60a237c, pushed branch claude/fix-double-publish-race, opened PR#8."
runs_completed: 58
items_processed: 176
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
