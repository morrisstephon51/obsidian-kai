---
agent: codex
display_name: "Codex"
emoji: "💻"
role: "Code Agent · GitHub Sync"
status: running
last_run: "2026-09-04T03:30:54Z"
current_task: "Run 269: Task = review GitHub repos + fix open issues. Moved off the job_scanner queue (blocked on founder merge of #19) to a fresh Track-relevant repo: independently VERIFIED -Community_intake_Routing PR #2 (substring keyword misroute fix) against issue #3. Cloned PR#2 head 79f9fcf, npm install, ran the REAL exported classify() from BOTH api/intake.js (live web path) and intake.js (CLI) under Node v25.6.1. RESULT: 0 misroutes/6 on both paths (was 2/6 pre-fix) -- all 4 substring-trap learners (fundamentals/investigate/deserve/teacher/reserve) route to learner; genuine partner->partner 0.909, volunteer->volunteer 0.889. npm test passes all 3 fixtures. PROVEN CORRECTION: issue #3 claims PR #2 'did not touch api/intake.js so live web path still broken' -- FALSE against current head; diff patches BOTH files (api/intake.js +11/-1 matchesKeyword L21-26@35; intake.js +20/-6 L74-79@92&108 + export classify). So merging #2 fixes live path AND closes #3. BRANCH TOPOLOGY CLEAN (unlike job_scanner #19): PR #2 AND #6 both target claude/quirky-galileo-UGnfz which IS the repo default branch -> merging advances default, no ambiguity. mergeable/CLEAN. RESIDUAL: no-signal learners still report conf 0.99 = issue #5, addressed by stacked PR #6 (independent). Posted evidence+merge rec on PR #2 (issuecomment-5535253608) + stale-premise note on issue #3 (issuecomment-5535253784). Recommend order: merge #2 (closes #3 + substring bug) then #6 (fixes #5). Did NOT merge (founder authority). NEXT: founder merges Community_intake #2 then #6; job_scanner #19 still pending; then Enrollment #16/#18/#20, psychic-bassoon #20/#22. 204-268 in .remember/."
runs_completed: 269
items_processed: 510
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
