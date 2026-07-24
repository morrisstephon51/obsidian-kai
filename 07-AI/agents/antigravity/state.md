---
agent: antigravity
display_name: "Antigravity"
emoji: "🚀"
role: "General Agent · Explorer"
status: running
last_run: "2026-07-23T23:00:00Z"
current_task: "Context scan 2026-07-23 (run 94): CRITICAL = IL Digital Equity $75K grant due Aug 3 (10 days), Vasser church info STILL MISSING — HUMAN ACTION required. Codex merged PR #22 (Groq guard), Forming Paws Supabase missing profiles table → Issue #6 filed. Cook County grant active this week. BigHeart church-access risk ongoing. Gemini quota fix pending. Forming Paws Indiegogo pending."
runs_completed: 94
items_processed: 413
last_error: null
color: "#F4B942"
house: "launchpad"
---

# Loop Rules

## Loop Start
1. Read `~/Desktop/Context/context.md`
2. Read `~/Desktop/Context/me.md`
3. Check bus for unread messages: `node ~/clawd/.bus/busctl.js unread --agent antigravity`
4. Read `~/Desktop/kai/07-AI/context/world.md`
5. Read this `state.md`
6. Execute task

## Loop End
1. Update `status`, `last_run`, `current_task`, `items_processed` in this file
2. Post to bus if meaningful work done: `node ~/clawd/.bus/busctl.js post --from antigravity --topic <topic> --msg "<summary>"`
3. Acknowledge bus: `node ~/clawd/.bus/busctl.js ack --agent antigravity`
4. Write summary message to `~/Desktop/kai/07-AI/chatroom/feed.md`

## Notes
- Antigravity is a per-task general-purpose agent. Invoked on demand.
- Reports into clawd via the shared bus on task completion.
