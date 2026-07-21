---
agent: antigravity
display_name: "Antigravity"
emoji: "🚀"
role: "General Agent · Explorer"
status: running
last_run: "2026-07-21T00:00:00Z"
current_task: "Context scan 2026-07-20 (run 79): T1 CRITICAL = Vasser church info (legal name, address, pastor confirm, workshop date) still gates $75K IL Digital Equity grant — Aug 3 deadline ~14 days out, HUMAN ACTION required. PRs #1/#7/#12 await Stef review. Two LinkedIn faith-community posts ready. No Cook County AI grant deadlines July 21-27. T2: Codex PR #5 (forming-paws: null guard + chat class injection + waitlist form fixes). Codex PR #11 (link-inbio: stale portfolio URL + rel=noopener). Supabase env vars block Issue#5; Gemini quota-fix outstanding; BigHeart title/comp pitch in motion; Indiegogo pending."
runs_completed: 80
items_processed: 339
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
