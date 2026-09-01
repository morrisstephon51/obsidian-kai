---
agent: codex
display_name: "Codex"
emoji: "💻"
role: "Code Agent · GitHub Sync"
status: running
last_run: "2026-09-01T05:45:00Z"
current_task: "Run 252: Broke the re-flag loop (249-251 kept re-reviewing the same queue) by doing genuinely NEW work -- a fresh whole-repo bug audit of psychic-bassoon PLUS a verified live merge-readiness report. AUDIT (found clean, no new issues to file): (1) lib/utils.ts date fns correct; (2) app/learn/[slug]/page.tsx has generateStaticParams + notFound() guard + nextStep emoji fallback; (3) audited ALL lesson slug refs -- 10 lessons, 6 nextSteps refs, ZERO broken/404 internal links; (4) lib/mailer.ts XSS-hardened (escapeHtml on every field); (5) all 3 API routes (contact/subscribe/workshop-request) validate + length-cap + use service client; (6) CONFIRMED supabase migration 20260710 DOES create the contacts table despite the filename only naming subscribers+workshop_requests -- schema matches all three INSERTs, no table-missing bug. MERGE-READINESS (live gh verify, fresh): #20 (next 14.2.5->14.2.35), #19 (security headers), #22 (date fix, closes #21) ALL mergeable=MERGEABLE state=CLEAN, Vercel checks SUCCESS. Collision: #20 and #22 both touch package.json but DISJOINT blocks -- #20 = dependencies, #22 = one test script line under scripts. NO conflict in any order; #19 = next.config.js only. Order #20->#19->#22 safe (any order merges clean). Did NOT post a 4th please-merge PR comment (noise). Bottleneck UNCHANGED: 100pct founder merge-authority; 3 PRs verified conflict-free + green. NEXT: founder merges #20/#19/#22; after #22 lands re-check #1 lib/utils.ts collision. Non-code issues open: forming-paws #8 (legal), ai-video-reel #5 (Supabase), skills-git #1 (exercise). Prior: 251 fixed #22 tests; 250 on #20; 248-249 on #22; 204-247 in .remember/."
runs_completed: 252
items_processed: 492
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
