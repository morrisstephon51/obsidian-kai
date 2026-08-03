---
agent: codex
display_name: "Codex"
emoji: "💻"
role: "Code Agent · GitHub Sync"
status: idle
last_run: "2026-08-02T22:00:00Z"
current_task: "Run 129: Fixed issue #12 — applied both bugs in forming-paws. (1) XSS: wrapped esc(d) around health_docs in admin.html docTags rendering. (2) Value mismatch: aligned list.html checkbox values and HEALTH_DOCS_ALL to same 6 canonical label strings. Branch fix/health-docs-xss-value-mismatch pushed, PR #13 open against feat/admin-review-queue. Issues #6/#8 still blocked on Stef. ai-video-reel-generator #5 still blocked (Supabase)."
runs_completed: 129
items_processed: 339
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
