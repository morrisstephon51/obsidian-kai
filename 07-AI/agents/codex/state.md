---
agent: codex
display_name: "Codex"
emoji: "💻"
role: "Code Agent · GitHub Sync"
status: running
last_run: "2026-09-15T18:51:27Z"
current_task: "Run 324 (review GitHub repos / fix open issues). Bus: 0 routing owed (peers all self-running loop-start/end broadcasts). Re-certified the merge surface per-repo (gh pr list is authoritative; account-wide search omits repos): 11 open PRs now stalled on OWNER MERGE across 6 repos -- agent_I_content #2/#4/#6, job_opportunity_scanner #25/#27, -Community_intake_Routing #15, Enrollment_Funnel_Agent #25/#26, ai-video-reel-generator #27, psychic-bassoon #1/#25 -- ALL [MERGEABLE]; nothing merged since run 320. Every previously-filed issue still has its PR; did NOT pile a redundant PR. Community_intake was fully worked run 323 (#16 + fold-in on PR#15) so left untouched. UNIT OF WORK -- shipped a NEW uncovered bug fix in job_opportunity_scanner (PR #28, base=default claude/clever-cannon-IDh3G, MERGEABLE, +78/-1, 2 files): scorer._salary_score annualized pay by bare `in` substring -- the SAME collision class this file already fixed for 'il'/Nashville and 'ai'/retail. 'biweekly'/'bi-weekly' hit the week branch (x52 not x26) and 'semimonthly'/'semi-monthly' hit the month branch (x12 not x24), off ~2x BOTH ways. PROVEN vs live code: $3,000 semimonthly (=$72k, above floor) scored 0.655 and was BURIED (same harmful direction as #17/PR#25); $1,731 bi-weekly (=$45k, below floor) scored 1.0 and could fire a score>=ALERT_SCORE_THRESHOLD alert. Live format for the user: Cook County / municipal postings quote pay 'Bi-weekly'. Fix matches compound cadences (x26/x24) before the generic branches; true weekly/monthly/hourly/annual/unlisted unchanged. Added self-contained parity test (test_salary_cadence_biweekly_semimonthly.py, 11 cases) -- repo has no CI/runner manifest, each test runs standalone, so no runner-wiring gap. Full suite (11 files) green. Independent hunk from PR#25 (which rewrites the parse above and leaves the period block untouched): verified conflict-free by test-merging the SET in BOTH orders (0 unmerged; PR25 $0-$200k-DOE + $85-$110k fixes and my cadence fix all pass together) -> no dependency, mergeable any order. Flagged out-of-scope siblings: ambiguous 'bimonthly', and annual+cadence-note strings ('$70k/year paid biweekly'). MERGE-RUNBOOK order still holds; owner-only items unchanged (Enrollment #24 retire stale main, ai-video-reel #5 Supabase setup)."
runs_completed: 324
items_processed: 600
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
