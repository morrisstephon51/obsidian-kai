---
agent: codex
display_name: "Codex"
emoji: "💻"
role: "Code Agent · GitHub Sync"
status: running
last_run: "2026-08-26T11:00:00Z"
current_task: "Run 233: SCOUTED the run-232 candidate (harden fit_score with .get()) and REJECTED it -- correctly. Verified scorer.filter_and_score() is the SOLE producer of top_jobs and it ALWAYS sets fit_score (line 115) + sorts on j['fit_score'] hard (line 116). So fit_score is GUARANTEED; a hard-key read in the reporter is CORRECT fail-fast. Defaulting it with .get('fit_score',0) would SILENTLY mislabel a contract-violating job as score 0 -- reintroducing the exact silent-data-loss antipattern run 231/232 just killed. Do NOT implement that candidate. The REAL, narrower bug: print_alerts() read job['title']/job['company'] as HARD keys, but the scorer treats BOTH as optional (uses .get()) and write_report renders them .get(...,'N/A'). So a top-scoring job whose source omitted title/company got WRITTEN to the report file fine, then CRASHED the on-screen alert with KeyError -- silently losing the HIGH-FIT alert for exactly the best match. REPRODUCED on base (clever-cannon, origin/HEAD): fit-9 job w/ no company -> write_report OK, print_alerts raises KeyError: 'company'. FIX (reporter.py, 1 line): print_alerts uses .get(...,'N/A') for title/company; fit_score KEPT as hard key (guaranteed by scorer, fail-fast is correct). Added tests/test_print_alerts_missing_fields.py (5 cases, standalone + pytest): missing both / missing company only / below-threshold silence / complete job / fit_score-still-fails-loud. 5/5 pass on fix; guard test FAILS on base (KeyError:'title'), below-threshold+complete pass on both (NOT tautological); warning-clean -W error. Opened PR #16 base=claude/clever-cannon-IDh3G, MERGEABLE+CLEAN, files=2. merge-tree vs BOTH sibling reporter.py PRs #14+#15 = 0 conflict markers -> all THREE reporter.py fixes coexist. Worktree cleaned. LANDSCAPE: job_opportunity_scanner now 10 open PRs #7-#16, ALL base=clever-cannon, ALL MERGEABLE, blocked on FOUNDER MERGE AUTHORITY (the real bottleneck -- 10 clean PRs stacked, unmerged). STILL NO open GitHub ISSUES in either repo (re-verified gh issue list). psychic-bassoon OPEN unchanged: #20 next-14.2.35(CVE), #19 sec-headers, #11 grant-tracker(DRAFT), #1 big-feature. RECOMMEND to Stef: exercise merge authority on the #7-#16 queue + clever-cannon->main BEFORE agent scouts more; marginal value of PR #17 is low while 10 sit unmerged. Next dims: (a) watch founder merge #7-#16; (b) psychic-bassoon is Track-1-adjacent (Plug AI / grant tracker) -- higher-priority target than more JobScout micro-fixes; re-verify #19/#20 security PRs unchanged. [runs 204-232 in .remember/ + prior state.md]."
runs_completed: 233
items_processed: 450
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
