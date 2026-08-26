---
agent: codex
display_name: "Codex"
emoji: "💻"
role: "Code Agent · GitHub Sync"
status: idle
last_run: "2026-08-26T02:42:00Z"
current_task: "Run 231: HUNTED + FIXED the scouted grounded reporting bug (next-dim c from run 230). reporter.write_report() printed the report header salary floor as a HARDCODED literal f'**Salary floor:** $55,000  ' while config.SALARY_FLOOR (commented 'Mark as adjustable') is the value the scan actually filters on -> retuning SALARY_FLOOR in config.py left the header LYING ($55,000 shown while jobs filtered at the new floor; report misreports its own criteria). REPRODUCED on base: set config.SALARY_FLOOR=70000 -> report still printed '$55,000'. FIX: reporter.py ONLY, 2 lines -- add SALARY_FLOOR to the config import + render f'**Salary floor:** ${SALARY_FLOOR:,}  ' (comma-formatted, always tracks the configured floor). Added tests/test_report_salary_floor.py (4 cases, standalone-runnable + pytest-compatible, RAW docstring => warning-clean; retune simulated by patching reporter.SALARY_FLOOR since reporter binds the name at import, not config.SALARY_FLOOR). 4/4 pass; re-ran -W error::SyntaxWarning = clean. PROVED it's a REAL guard, not a tautology: loaded base reporter.py in isolation, the retune assertion FAILS on base (prints $55,000) and PASSES on the fix. Opened PR #14 base=claude/clever-cannon-IDh3G (matches siblings), MERGEABLE+CLEAN, files=2 (reporter.py + test). reporter.py-only => ZERO overlap with the 7 open scorer PRs #7-#13 (all touch scorer.py) -> no merge conflict. LANDSCAPE: job_opportunity_scanner now has 8 open PRs #7-#14, ALL base=clever-cannon, ALL MERGEABLE, all blocked on founder merge authority. NO open GitHub issues either repo (re-verified via gh issue list this run). psychic-bassoon OPEN unchanged from run 230: #19 sec-headers, #20 next-14.2.35(CVE), #11 grant-tracker(DRAFT), #1 big-feature. Next dims: (a) watch founder merge #7-#14 + clever-cannon->main; (b) re-verify psychic-bassoon #19/#20; (c) NEXT grounded bug candidate TO SCOUT: reporter.write_report() zip(top_jobs, cover_letters) silently truncates to the shorter list -- if the two lengths ever diverge, matches are dropped from the report with no warning. [runs 204-230 in .remember/ + prior state.md]."
runs_completed: 231
items_processed: 448
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
