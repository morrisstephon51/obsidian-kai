---
agent: codex
display_name: "Codex"
emoji: "💻"
role: "Code Agent · GitHub Sync"
status: idle
last_run: "2026-08-06T22:05:00Z"
current_task: "Run 145: Advanced psychic-bassoon issue #12 (The Plug AI prod URL behind Vercel auth wall — Track-1 flagship). Re-verified the wall is live (GET psychic-bassoon-cam6stef.vercel.app -> 302 vercel.com/sso-api) and confirmed resume.html links this exact slug TWICE (header + projects). Cloned the repo and confirmed it IS The Plug AI (app/layout.tsx title The Plug AI — AI Is For You. Not Just Them.; hero Get Connected/Skilled/Into AI; vercel.json clean framework:nextjs). KEY NEW EVIDENCE: the bare psychic-bassoon.vercel.app returns 200 but serves a STRANGER'S HackMerced project — a global *.vercel.app namespace collision, which is why this project deploys under the -cam6stef suffix. So dropping the suffix is a TRAP (points reviewers at unrelated third-party content, worse than a login wall). Posted verification comment #5209432397 sharpening the fix to two dashboard/DNS options: (1) fastest — Vercel Deployment Protection > Vercel Authentication > Off then re-verify 200; (2) durable — attach a public custom domain and repoint all links. No code change needed; flagged for human dashboard action (Vercel MCP settings-write needs interactive permission unavailable in the autonomous loop; no unauthorized changes made). PREVIOUS Run 144: Reviewed Link-inbio PR #11 (resume.html: stale portfolio URL + rel=noopener) with live verification of every URL it touches. (1) SOUND — rel=noopener noreferrer added to all 9 target=_blank anchors (reverse-tabnabbing fix); ai-video-reel-generator.vercel.app reproduced dead-end 307 and community-intake-routing.vercel.app reproduced 404, so swapping both to GitHub repo links is justified. (2) INACCURATE claim corrected — PR calls stefan-portfolio-eight.vercel.app stale but it returns live 200 (as does the new cam6stef slug); this is canonicalization, not a dead-link repair. (3) NEW HIGH-PRIORITY issue discovered — The Plug AI link psychic-bassoon-cam6stef.vercel.app returns 302 -> vercel.com/sso-api (Vercel Deployment Protection ON), so a fellowship reviewer clicking The Plug AI link from the resume hits a Vercel login wall, not the site; appears twice in resume.html and PR #11 does NOT fix it. Posted evidence review comment #5208027512 recommending merge of the sound resume.html changes (flagged for human merge, no auto-merge/push). Filed psychic-bassoon issue #12 to track the auth-wall (fix: disable Deployment Protection on Production, then re-verify 200). PREVIOUS Run 143: Verified the freshest live-broken frontier item — ai-video-reel-generator PR #23 (bare-domain dead-end 307). Reproduced live: GET / returns 307 with NO Location header and x-vercel-cache: HIT (a cached dead end), while GET /dashboard returns 200 (redirect destination healthy). Isolated root cause: no middleware.ts and no redirects block in vercel.json, so the ONLY origin of the / 307 is the component-level redirect(/dashboard) in src/app/page.tsx, which Next 14.2.5 statically prerenders and Vercel edge-caches without a Location header. Validated the PR fix on its branch via node --input-type=module: next.config.mjs redirects() returns exactly [{source:/,destination:/dashboard,permanent:false}] — a routing-layer redirect that runs before render and always emits a correct Location; vercel.json already pins framework:nextjs so the rules compile; both config redirect and leftover page.tsx fallback target /dashboard, so no loop. PR is complete and sound (single-file, +10, independent of the Supabase blocker #5). Posted evidence review comment #5207691719 recommending merge to restore the sites front door; flagged for human merge — no auto-merge, no push to main. PREVIOUS Run 142: community-intake PR #1 (404 fix + data-loss else-branch d8fd798), out of draft, comment #5205625446. Run 141: forming-paws PR #15 vercel.json framework:nextjs. Earlier runs in git history / bus."
runs_completed: 145
items_processed: 355
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
