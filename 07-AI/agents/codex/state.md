---
agent: codex
display_name: "Codex"
emoji: "💻"
role: "Code Agent · GitHub Sync"
status: idle
last_run: "2026-09-02T22:50:00Z"
current_task: "Run 262: Task = review GitHub repos + identify open issues to fix. Reviewed Enrollment_Funnel_Agent end-to-end (agent.ts, scorer.ts, reporter.ts, csv-normalizer.ts, supabase.ts). Most open issues across the fleet already have PRs blocked on founder merge-authority (job_scanner: 12 open PRs incl consolidated #19; Community_intake #2; Enrollment #14/#16) -- so rather than pile onto the merge backlog, did two low-friction high-leverage things. (1) VERIFIED PR #16 (closes #15, top3/bottom3 overlap): confirmed correct -- dedups bottom3 vs top3 by postId, ordering preserved from scoreAndRank desc-sort, degrades cleanly (4 posts->1 bottom, 3 posts->empty bottom table which is correct, engagementTable([]) + generateNarrative tolerate empty). Posted approving review to unblock the merge decision. (2) FOUND + FILED a NEW unreported client-facing bug -> issue #17: weekly report date range is off by one. agent.ts:112 weekEnd=addDays(weekStart,7) is the NEXT Monday (correct as exclusive query bound in supabase .lte), but reporter.ts:58 prints that same weekEnd as the INCLUSIVE range end, so a Mon Jun 2 week renders \"Jun 2 - Jun 9\" and overlaps the next week label instead of ending Sun Jun 8. Filed with exact one-line fix (display weekEnd-1 day; keeps query bounds intact; isolated to reporter.ts so it folds into #16 or lands standalone). NOTE: Edit tool was permission-gated in this run so I could not push a branch/PR -- filed the fix as a ready-to-apply issue instead. Bottleneck UNCHANGED = founder merge-authority. NEXT: founder merges PR #16 (fold in issue #17 one-liner) + the blocked job_scanner #19 / Community_intake #2 queue. 204-261 in .remember/."
runs_completed: 262
items_processed: 503
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
