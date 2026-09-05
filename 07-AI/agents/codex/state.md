---
agent: codex
display_name: "Codex"
emoji: "💻"
role: "Code Agent · GitHub Sync"
status: idle
last_run: "2026-09-05T12:30:00Z"
current_task: "Run 276: Task = review GitHub repos + fix open issues. Independently VERIFIED job_opportunity_scanner PR #19 (fix/scorer-consolidated) — the CANONICAL consolidated scorer/config fix covering gh issues #7,#8,#9,#10,#11,#12,#13,#17. base=main (DEFAULT branch, NO split-base trap unlike #7-#16 which target claude/clever-cannon-IDh3G), MERGEABLE/CLEAN, closingIssuesReferences EMPTY. Ran shipped tests/test_scorer_consolidated.py on NEW via git worktree -> 28/28 PASS; py_compile CLEAN scorer.py+config.py. NON-TAUTOLOGY differential: same 11 realistic inputs against OLD main scorer -> 11/11 exhibit bug, NEW 0/11. Worst: \$85k scored 0.0015 (read as \$85/yr) vs 1.0; retAIl/repAIr matched 'ai' (0.333 vs 0.0); Nashville/Philadelphia matched 'il' substring (1.0 vs 0.2); 30+ days/6 weeks/2 months/old-ISO all wrongly included (dead ISO branch: raw[:len(fmt)] slice truncated+always raised). Posted evidence PR #19 (issuecomment-5551760475). Did NOT merge (founder authority). RECOMMEND #19 as canonical merge path: merge once to main, supersedes individual #7-#13/#17, then manually close issues (auto-close will not fire, closes[] EMPTY). PRIOR: run 275 Enrollment #14(verified); 274 Enrollment #20/#19; 273 Enrollment #18; 272 job_scanner #19(now re-verified deeper); 271 Enrollment #16; 270 psychic-bassoon #22; 269 Community_intake #2/#6/#3. STILL OPEN needing founder merge: job_scanner #19 (canonical, verified); Community_intake #2 then #6; psychic-bassoon #22 (+#20 CVE, #19 headers); Enrollment #14/#16/#18/#20 (pick canonical branch first). 204-275 in .remember/."
runs_completed: 276
items_processed: 517
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
