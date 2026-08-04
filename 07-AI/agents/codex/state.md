---
agent: codex
display_name: "Codex"
emoji: "💻"
role: "Code Agent · GitHub Sync"
status: running
last_run: "2026-08-04T03:05:00Z"
current_task: "Run 132: Reviewed forming-paws PR #14 (upload redirect) and found a correctness bug — both upload routes are hit via native <form method=POST> in app/dogs/[id]/page.tsx, but NextResponse.redirect() defaulted to 307, which preserves POST and would re-POST to the GET-only /dogs/[id] page (405). Pushed fix 56b06a7: return 303 See Other (correct Post/Redirect/Get) in both photo/route.ts and health-doc/route.ts; also restored the storagePath template literal. Left a review comment. PR now head=56b06a7, awaiting Vercel rebuild + human merge. Still open: PR #10 (admin review queue). Issues #6 (Supabase profiles/dogs setup) and #8 (IL legal filing) remain blocked on Stef. ai-video-reel-generator #5 still blocked on Supabase setup."
runs_completed: 132
items_processed: 342
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
