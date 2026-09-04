---
agent: codex
display_name: "Codex"
emoji: "💻"
role: "Code Agent · GitHub Sync"
status: idle
last_run: "2026-09-04T15:50:00Z"
current_task: "Run 272: Task = review GitHub repos + fix open issues. Independently VERIFIED job_opportunity_scanner PR #19 (consolidated scorer/config fixes, closes #7-#13,#17, supersedes #18). Cloned head 28d82f5, base main HEAD bd6388d, merge-base f0d9813. Bundled tests/test_scorer_consolidated.py green under python3 3.14. NON-TAUTOLOGY differential: imported OLD main scorer.py+config.py vs NEW pr19 in isolated procs -- every fix flips as claimed: #13 '30+ days ago' kept->filtered; #11 6wk/2mo kept->filtered; #12 ISO date dead-branch kept->filtered; #9 '$85k' 0.002->1.0; #17 '$5000/month' 0.091->1.0; #8 'Retail'(ai in retAIl) 0.333->0.0; #7 'Nashville'(il) 1.0->0.2; #10 'AI Trainer' 0.333->0.667. No-regression pass-through identical old->new (''/'3 days ago'/'today'/'garbage', Illinois/Remote->1.0, $90k-range->1.0, no-salary->0.5). TOPOLOGY: gh MERGEABLE/CLEAN, base=main. FINDING: two-dot main..pr19 adds 4 UNRELATED .claude files not on main & not part of any issue (.claude/commands/dd.md +61, .claude/skills/remote-control/* +222) carried from old fork point -- contradicts PR body's 'deliberately excluded .claude/dd.md' claim; public/index.html+vercel.json show in 3-dot view but byte-identical to main (net-zero). Recommended merge + drop the 4 .claude files first. Posted evidence+rec on PR #19 (issuecomment-5543043125). Did NOT merge (founder authority). PRIOR: run 271 Enrollment #16; run 270 psychic-bassoon #22; run 269 Community_intake #2/#6. NEXT: founder merges Community_intake #2 then #6, psychic-bassoon #22, Enrollment #16, job_scanner #19 (optionally drop .claude scope-creep); Enrollment #18/#20 unverified. 204-271 in .remember/."
runs_completed: 272
items_processed: 513
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
