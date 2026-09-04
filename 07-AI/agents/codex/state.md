---
agent: codex
display_name: "Codex"
emoji: "💻"
role: "Code Agent · GitHub Sync"
status: idle
last_run: "2026-09-04T11:45:00Z"
current_task: "Run 271: Task = review GitHub repos + fix open issues. Independently VERIFIED Enrollment_Funnel_Agent PR #16 (top3/bottom3 overlap on <6-post weeks, closes #15). Cloned PR head 3a16b6b (base main = repo default), npm ci + npx tsc --noEmit = CLEAN (exit 0). Root cause: scoreAndRank returns posts sorted by normalizedScore desc, postId (content_item_id / CSV Post ID / Video ID) is a unique key; slice(0,3) & slice(-3) intersect when n<6. Ran the EXACT old-vs-new Step-3 selection over n=2..8: OLD duplicates posts (n2->B,A; n3->all3; n4->B,C; n5->C) matching the issue repro precisely; NEW overlap=0 at every size. NON-TAUTOLOGY/no-regression: bottom3 byte-identical old-vs-new for n=6..20 -> fix only touches light weeks, normal weeks untouched. TOPOLOGY: gh MERGEABLE / mergeStateStatus CLEAN, base=default branch. Posted evidence+merge rec on PR #16 (issuecomment-5539997108). Did NOT merge (founder authority). PRIOR: run 270 psychic-bassoon #22; run 269 Community_intake #2/#6 verified. NEXT: founder merges Community_intake #2 then #6, psychic-bassoon #22, Enrollment #16; job_scanner #19 pending; Enrollment #18/#20 unverified. 204-270 in .remember/."
runs_completed: 271
items_processed: 512
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
