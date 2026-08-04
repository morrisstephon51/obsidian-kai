---
agent: codex
display_name: "Codex"
emoji: "💻"
role: "Code Agent · GitHub Sync"
status: idle
last_run: "2026-08-04T00:55:00Z"
current_task: "Run 131: Merged forming-paws PR #13 (security fix, issue #12) — squash-merged to main, branch deleted. Verified diff before merge: XSS in admin.html docTags closed via esc(d); list.html checkbox values realigned to full labels matching HEALTH_DOCS_ALL so the Missing-docs panel is now accurate. Checks CLEAN + MERGEABLE, Vercel preview passed. Closed issue #12 completed. Still open in forming-paws: PR #14 (upload redirect, awaiting merge), PR #10 (admin review queue feat), issues #6/#8 blocked on Stef (Supabase SQL + legal filing). ai-video-reel-generator #5 still blocked (Supabase setup)."
runs_completed: 131
items_processed: 341
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
