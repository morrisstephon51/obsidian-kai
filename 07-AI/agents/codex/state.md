---
agent: codex
display_name: "Codex"
emoji: "💻"
role: "Code Agent · GitHub Sync"
status: running
last_run: "2026-09-02T10:35:00Z"
current_task: "Run 259: Found & fixed a NEW uncovered production bug in Enrollment_Funnel_Agent (BigHeart weekly report). agent.ts picked top3=scored.slice(0,3) and bottom3=scored.slice(-3).reverse() from the same score-sorted list; on any week with <6 ranked posts the two slices OVERLAP, so the identical post rendered in BOTH the Top 3 (post more like these) and Bottom 3 (flagged for review) tables -- contradictory client-facing guidance. Reproduced empirically: 4 posts -> 2 posts duplicated across both tables; 3 posts -> all 3 duplicated. Common on light/single-platform weeks. Fix: exclude top3 postIds from the bottom3 selection (topIds Set + filter). Verified npx tsc --noEmit clean and overlap=0 for n=2..8; n>=6 output unchanged. Filed issue #15, opened PR #16 (closes #15) off main. Same-account authorship blocks self-merge -> merge-blocked queue. First check confirmed ALL 5 open issues across repos are already covered by PRs or need founder action: Community_intake #3->PR#4, jobscout #17->PR#18, psychic-bassoon #21->PR#22, avrg #5 (Supabase infra), forming-paws #8 (legal). QUEUE bottleneck UNCHANGED = 100pct founder merge-authority. NEXT: founder merges the independent single-file fix PRs across repos. 204-258 in .remember/."
runs_completed: 259
items_processed: 499
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
