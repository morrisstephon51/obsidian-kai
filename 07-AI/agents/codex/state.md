---
agent: codex
display_name: "Codex"
emoji: "💻"
role: "Code Agent · GitHub Sync"
status: running
last_run: "2026-08-06T17:10:00Z"
current_task: "Run 143: Verified the freshest live-broken frontier item — ai-video-reel-generator PR #23 (bare-domain dead-end 307). Reproduced live: GET / returns 307 with NO Location header and x-vercel-cache: HIT (a cached dead end), while GET /dashboard returns 200 (redirect destination healthy). Isolated root cause: no middleware.ts and no redirects block in vercel.json, so the ONLY origin of the / 307 is the component-level redirect(/dashboard) in src/app/page.tsx, which Next 14.2.5 statically prerenders and Vercel edge-caches without a Location header. Validated the PR fix on its branch via node --input-type=module: next.config.mjs redirects() returns exactly [{source:/,destination:/dashboard,permanent:false}] — a routing-layer redirect that runs before render and always emits a correct Location; vercel.json already pins framework:nextjs so the rules compile; both config redirect and leftover page.tsx fallback target /dashboard, so no loop. PR is complete and sound (single-file, +10, independent of the Supabase blocker #5). Posted evidence review comment #5207691719 recommending merge to restore the sites front door; flagged for human merge — no auto-merge, no push to main. PREVIOUS Run 142: community-intake PR #1 (404 fix + data-loss else-branch d8fd798), out of draft, comment #5205625446. Run 141: forming-paws PR #15 vercel.json framework:nextjs. Earlier runs in git history / bus."
runs_completed: 143
items_processed: 353
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
