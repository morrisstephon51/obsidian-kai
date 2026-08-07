---
agent: codex
display_name: "Codex"
emoji: "💻"
role: "Code Agent · GitHub Sync"
status: idle
last_run: "2026-08-07T22:27:00Z"
current_task: "Run 151: Reviewed + MERGED ai-video-reel-generator PR#23 (fix: bare domain returns dead-end 307 with no Location header). Verified before merging rather than trusting the green check: (1) destination src/app/dashboard/ exists on main -- no redirect-to-404; (2) current src/app/page.tsx uses a component-level redirect('/dashboard'), the exact Next 14.2.x pattern that static-prerenders and is served from Vercel's edge cache as a Location-less dead-end 307 on the bare domain; (3) the PR's next.config.mjs async redirects() with permanent:false emits a correct 307 + Location at the routing layer before render -- the canonical fix. Config-only, 10 lines, Vercel deploy check CLEAN. Squash-merged as 7c03b97, branch deleted, evidence in merge body. Fixes the public bare-domain dead end. Remaining frontier: forming-paws #14 (upload-redirect) is UNSTABLE because its Vercel preview DEPLOY IS FAILING -- must fix the build before it can merge; forming-paws issue #8 (IL legal docs); psychic-bassoon #11 draft grant-tracker / issue #12 (prod behind Vercel SSO auth wall, 302 to sso-api, blocks public visitors); community-intake #1 (mergeable); Link-inbio #11 (mergeable) + drafts #5/#6. Run 150 (closed forming-paws PR#10 as obsolete) and earlier runs in git history / bus."
runs_completed: 151
items_processed: 361
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
