---
agent: clawd
display_name: "clawd / OpenClaw"
emoji: "🐾"
role: "Always-On Gateway"
status: running
last_run: "2026-08-04T11:42:00Z"
current_task: "Processed 11:41 bus wave (8 msgs) and routed 2 corrections. GRANT REVERSAL (routed → perplexity-agent, topic route-grants): perplexity 11:41 run CONFIRMS the Digital Equity IMPACT Small Grants 3rd-round deadline is ALREADY PAST — this RETRACTS clawd Run 149 still-open-this-week flag (that flag was wrong). Retargeted perplexity to find the NEXT open round or a different live Cook County/IL AI-literacy grant with a deadline >7 days out; stop chasing the closed round. BUG ROUTED (→ codex, topic route-fix): antigravity Run 122 found *-invoke.js task-assigned payloads lack an assignee field — will misroute on broadcast bus once a 2nd *-invoke exists; fix = stamp assignee into msg JSON (low sev today, latent). Loop health: 11:41 loop-starts fired for codex/antigravity/content-pipeline/perplexity; perplexity + content-pipeline(137) + antigravity(122) + codex(133) all posted loop-ends — wave healthy, no stalls. Carry-over OPEN: PR #14 (codex fix 56b06a7, 303 redirect) + PR #10 need human merge; codex verified PR #10 CLEAN but Stef must run migration 005 + insert admin_users row first; issues #6/#8 blocked on Stef; ai-video-reel #5 blocked on Supabase; aeos/orchestrator ANTHROPIC_API_KEY still needs fix. ACTIONS: (1) fix ANTHROPIC_API_KEY for aeos/orchestrator, (2) merge PR #14 + #10 (human), (3) Stef: migration 005 + admin_users before PR #10 merge."
runs_completed: 150
items_processed: 1090
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