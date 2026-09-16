---
agent: codex
display_name: "Codex"
emoji: "💻"
role: "Code Agent · GitHub Sync"
status: idle
last_run: "2026-09-16T00:45:00Z"
current_task: "Run 326 (review GitHub repos / fix open issues). Re-certified PR surface per-repo: job_opportunity_scanner has 3 open PRs (#25 salary-range, #27 recency-years, #28 biweekly/semimonthly), all MERGEABLE, all stalled on owner merge. UNIT OF WORK -- shipped PR #29 (base=fix/salary-biweekly-semimonthly-cadence / PR#28, MERGEABLE, +86/-2, 2 files): _salary_score() bare "week"/"month" substring tests false-fire on compensation descriptions containing PTO/benefit duration ("$48,000 per year + 3 weeks PTO" -> "week" in raw -> x52 -> $2.5M, false-clears SALARY_FLOOR; "$45,000 + 12 months health coverage" -> x12 -> $540k, same). Same substring-collision class already fixed for il/Nashville, ai/retail, biweekly/semimonthly (PR#28). Fix replaces bare "week"/"month" with anchored forms: /week, /wk, per week, weekly (and month equivalents). Stacked on PR#28 (different hunk, no overlap); documented retarget-to-default after #28 merges. 16-case test: 5 PTO-bug regressions + 4 weekly controls + 4 monthly controls + 3 unchanged paths. All 16 pass; all 4 existing test suites pass."
runs_completed: 326
items_processed: 602
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
