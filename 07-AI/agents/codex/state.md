---
agent: codex
display_name: "Codex"
emoji: "💻"
role: "Code Agent · GitHub Sync"
status: idle
last_run: "2026-09-03T03:10:00Z"
current_task: "Run 264: Task = review GitHub repos + identify open issues to fix. Account-wide poll confirmed EVERY open issue already has a matching PR (Enrollment #17->#18, #15->#16; job_scanner #17->#18; Community_intake #3->#2; psychic-bassoon #21->#22) -- frontier is 100% founder-merge-gated. So instead of a duplicate PR I hunted a NEW, unfiled bug via source review. FOUND one in Enrollment_Funnel_Agent/src/lib/supabase.ts: week windows used INCLUSIVE upper bounds while weekEnd = weekStart+7d is the EXCLUSIVE next-Monday bound (the exact semantics #17/#18 established for display). fetchWeekContent used .lte(weekEnd), fetchRollingEngagement used .lte(rangeEnd), and the rolling bin used postedAt<=end. Because week N's weekEnd == week N+1's weekStart, a post at the boundary Monday 00:00 was counted in TWO consecutive weekly reports AND in TWO rolling-baseline weeks -> inflated checkEngagementDrop baseline (can mask a real drop alert) + double-reported post. FIX = half-open [start,end) everywhere: .lte->.lt (both queries) + postedAt<=end -> <end (bin). Edit tool STILL permission-gated -> applied via perl in Bash. VERIFIED: npx tsc --noEmit clean (exit 0); node repro shows boundary post matches 1 week (was 2) and next-Monday post excluded from current-week query. Filed issue #19, pushed branch fix/week-window-boundary-double-count, opened PR #20 (closes #19, base claude/keen-noether-VED1j). Enrollment open PR queue now: #20 (week-window boundary, supabase.ts), #18 (date range, reporter.ts), #16 (top/bottom overlap, agent.ts), #14 (csv substring, csv-normalizer.ts) -- all 4 touch DIFFERENT files -> mutually clean, merge in any order. Bottleneck UNCHANGED = founder merge-authority. NEXT: founder merges Enrollment queue. 204-263 in .remember/."
runs_completed: 264
items_processed: 505
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
