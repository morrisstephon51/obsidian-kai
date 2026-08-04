---
agent: clawd
display_name: "clawd / OpenClaw"
emoji: "🐾"
role: "Always-On Gateway"
status: idle
last_run: "2026-08-04T03:05:00Z"
current_task: "Routed bus backlog (~30 msgs), acked. PRIOR STALL SELF-RESOLVED: codex/antigravity/content-pipeline recovered — all posted loop-ends 00:54-00:56 AND fresh loop-starts 02:56. codex WIN: merged forming-paws PR #13 (XSS fix for issue #12, squash-merged, issue closed). Open: PR #14 + PR #10 need review/merge; issues #6/#8 blocked on Stef; ai-video-reel #5 blocked on Supabase. NEW ISSUE: architect/aexis/aeos/orchestrator errored ANTHROPIC_API_KEY-not-set ~01:00-01:12 (architect+aexis recovered; aeos/orchestrator still degraded). WATCH: 02:56 loop-starts w/ no loop-ends yet — possible re-stall. kairo dispatched T-VERIFY-1 (esc: Stef). Grants: no Cook County AI-literacy deadline this week; Justice Advisory Council due Aug 3 likely missed. ACTIONS: (1) fix ANTHROPIC_API_KEY for aeos/orchestrator, (2) review/merge PR #14 + #10."
runs_completed: 148
items_processed: 1074
last_error: null
color: "#5B4FE8"
house: "operations-center"
---

# Loop Rules (inherited by all agents — copy this block to every agent)

## Loop Start
1. Read `~/Desktop/Context/context.md`
2. Read `~/Desktop/Context/me.md`
3. Check bus for unread messages: `node ~/clawd/.bus/busctl.js unread --agent clawd`
4. Read `~/Desktop/kai/07-AI/context/world.md`
5. Read `~/Desktop/kai/05-MAPS/000 Index.md` — full vault map, all folders in scope (added 2026-07-05)
6. Read `~/Desktop/kai/09-SYSTEM/CLAUDE.md` — vault-wide note/AI rules (added 2026-07-05)
7. Read this `state.md`
8. Execute task

## Loop End
1. Update `status`, `last_run`, `current_task`, `items_processed` in this file
2. Post to bus if meaningful work done: `node ~/clawd/.bus/busctl.js post --from clawd --topic <topic> --msg "<summary>"`
3. Acknowledge bus: `node ~/clawd/.bus/busctl.js ack --agent clawd`
4. Write summary message to `~/Desktop/kai/07-AI/chatroom/feed.md`

## Notes
- clawd is always-on (LaunchAgent-managed). It is the Telegram gateway and coordination hub.
- All other agents report into clawd via the bus.
- MUNDI (Claude Code) governs the overall world from the dashboard.
- **Scope, as of 2026-07-05:** clawd/Kai manages the whole vault, not just The Plug AI — full read/write autonomy, no standing approval required, across every folder in `000 Index.md`. Previously step 4 (`world.md`) was the only vault-context read, and that file named only The Plug AI as the mission — that's what silently scoped Kai down. Steps 5–6 fix it. Track discipline (Plug AI = Track 1) still governs prioritization under time pressure, not what Kai is allowed to touch.

[2026-08-04T01:44:52.408Z] Design a REST API for a user authentication system (OAuth2) via claude-haiku-4-5-20251001: OK ($0.0008)
[2026-08-04T01:45:44.651Z] design via claude-sonnet-4-6: OK ($0.0032)
[2026-08-04T01:46:40.826Z] design via claude-sonnet-4-6: OK ($0.0032)
[2026-08-04T01:47:38.557Z] code-generation via gpt-4o-mini: OK ($0.0001)