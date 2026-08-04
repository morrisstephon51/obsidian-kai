---
agent: codex
display_name: "Codex"
emoji: "💻"
role: "Code Agent · GitHub Sync"
status: idle
last_run: "2026-08-04T07:05:00Z"
current_task: "Run 133: Full code review of forming-paws PR #10 (admin review queue — admin.html, list.html, migrations/005). Verified end-to-end: (1) every column the admin UI PATCHes (status/reviewer_note/reviewed_at/submitted_at/health_docs) exists in migration 004, so no missing-column failures; (2) health_docs strings now match EXACTLY between list.html checkbox values and admin.html HEALTH_DOCS_ALL (all 6) — the #13 value-mismatch fix is consistent; (3) RLS sound — admin_users default-deny (no client policies, service_role only), select/update gated on auth.email() in admin_users; (4) XSS clean — esc() on all user fields, missingTags only interpolates the constant list; (5) submit path maps checked health boxes into health_docs correctly; 401 triggers doLogout. CI green (Vercel preview SUCCESS), mergeable=CLEAN. No blocking issues. Posted review comment (#5175686524) with pre-merge action for Stef: run migration 005 + insert admin_users row, else queue loads empty. Earlier local no-merge-base was a shallow-clone artifact — GitHub reports MERGEABLE. Still open: issues #6 (Supabase profiles/dogs), #8 (IL legal filing) blocked on Stef; ai-video-reel #5 blocked on Supabase. PR #14 (upload redirect) awaiting human merge."
runs_completed: 133
items_processed: 343
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
