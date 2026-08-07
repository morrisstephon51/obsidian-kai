---
agent: codex
display_name: "Codex"
emoji: "💻"
role: "Code Agent · GitHub Sync"
status: idle
last_run: "2026-08-07T10:20:00Z"
current_task: "Run 148: Re-audited job_opportunity_scanner PR#3 (Stefan Build Hub landing page, static public/index.html + vercel.json, +323). Prior 2026-08-05 link audit found 2 of 6 showcase cards broken; today (2026-08-07) re-ran deterministic curl -I audit and found the picture WORSENED: 2 previously-GREEN cards regressed behind the Vercel Deployment-Protection auth wall (302 -> vercel.com/sso-api, same mechanism as psychic-bassoon #12): The Plug AI (psychic-bassoon-cam6stef) was 200 on 08-05, now 302; Content Machine (content-machine-cam6stef) was 200, now 302. The two prior breakages persist: AI Video Reel (ai-video-reel-generator.vercel.app) still 307 dead-end (fix = ai-video-reel #23, now open+MERGEABLE), Community Intake (community-intake-routing.vercel.app) still 404 NOT_FOUND (fix = -Community_intake_Routing #1, still draft/unmerged). Net: only 2 of 6 cards (Portfolio, Psychic Octo Engine) resolve for a logged-out visitor. PR code itself is clean (vanilla HTML + catch-all rewrite, no defect) -- every breakage is upstream deploy state. Posted updated audit comment #5215760757 with before/after table; the 08-05 \"hide 2 dead cards, ship with 4\" recommendation is now obsolete (4 broken), revised to HOLD merge until the two auth-wall toggles + two link fixes land, or ship with only the 2 verified-live cards + GitHub. No merge/push -- auth-wall toggles are Vercel-dashboard-only, flagged for human. Frontier otherwise unchanged from Run 147 (forming-paws #10/#14/#15, psychic-bassoon #11/#12, ai-video-reel #23, community-intake #1, Link-inbio #11 all human-merge/decision-pending). Earlier runs in git history / bus."
runs_completed: 148
items_processed: 358
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
