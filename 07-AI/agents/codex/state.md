---
agent: codex
display_name: "Codex"
emoji: "💻"
role: "Code Agent · GitHub Sync"
status: idle
last_run: "2026-08-06T13:55:00Z"
current_task: "Run 142: Advanced the last live-broken, non-draft-blocked frontier item — the community-intake 404. -Community_intake_Routing PR #1 (draft since 2026-06-28) already contained a complete, sound fix (public/index.html + api/intake.js Vercel zero-config layout) but had sat unmerged. Verified it end-to-end: live site still returns HTTP 404 (x-vercel-error NOT_FOUND); package.json declares @supabase/supabase-js ^2.45.0 so the serverless import resolves; api/intake.js passes node --check; and the Supabase insert is env-guarded so the 404 is fixed even before Supabase is provisioned. Found + fixed one real gap: with Supabase unconfigured (current state) a submission was silently discarded while the user still saw \"You're in!\" — permanent data loss for every early signup. Pushed commit d8fd798 to the PR branch adding an else-branch that logs the classified record to Vercel function logs so submissions are recoverable until the DB lands (node --check clean, minimal diff). Marked PR #1 ready for review (out of draft) and posted evidence review comment #5205625446 recommending merge — which also unblocks the broken community-intake card in job_opportunity_scanner PR #3 (Build Hub). Flagged for human merge; no auto-merge, no push to main. PREVIOUS Run 141: forming-paws PR #15 (vercel.json framework:nextjs) fixes repo-wide deploy failure; verified preview deploy passes; unblocks PRs #14/#10/main. Earlier runs (140-137) detailed in git history / bus."
runs_completed: 142
items_processed: 352
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
