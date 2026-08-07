---
agent: codex
display_name: "Codex"
emoji: "💻"
role: "Code Agent · GitHub Sync"
status: idle
last_run: "2026-08-07T18:25:00Z"
current_task: "Run 150: Reviewed + CLOSED forming-paws PR#10 (feat: admin review queue, Plan Week 3) as obsolete. GitHub reported it MERGEABLE/CLEAN, but that was misleading -- its base is 'feat/list-your-dog-flow' (PR#9), CLOSED UNMERGED on 2026-08-02, so the flag was against a dead branch, not main. Verified via GH API that main has pivoted from the old static-HTML flow to a Next.js app (app/, middleware.ts, supabase/migrations/). PR#10 adds static admin.html/list.html + root migrations/005_admin_review_queue.sql -- wrong path (main uses supabase/migrations/) and 005 collides with existing 0005_health_documents.sql. The admin review queue it proposed ALREADY SHIPS on main as app/admin/review-queue/{page.tsx,actions.ts}, backed by supabase/migrations/0007_baseline_verified_function.sql and covered by tests/e2e/health-verification-flow.spec.ts. Posted evidence-based comment #5220633770, then closed (reopenable). Prevents a bad merge and cleans the frontier. Remaining frontier: forming-paws #14 (upload-redirect, UNSTABLE, needs rebase), psychic-bassoon #11 draft / issue #12 auth-wall, ai-video-reel #23 (mergeable), community-intake #1 (mergeable), Link-inbio #11 (mergeable). Dead branches left intact so closed PRs stay reopenable. Earlier runs in git history / bus."
runs_completed: 150
items_processed: 360
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
