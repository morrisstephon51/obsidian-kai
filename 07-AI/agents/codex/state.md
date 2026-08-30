---
agent: codex
display_name: "Codex"
emoji: "💻"
role: "Code Agent · GitHub Sync"
status: idle
last_run: "2026-08-30T23:52:00Z"
current_task: "Run 246: Actioned last run's flagged backlog -- job_opportunity_scanner's 10 open PRs (#7-#16, all non-draft, all shown MERGEABLE, ZERO open issues). Cloned depth-1 and did an independent review against main rather than trusting the 10 PR bodies. FINDINGS: (A) All bugs are REAL on main: #7 `'il' in loc` bare-substring (matches email/Wilmington); #8 TITLE_SIGNALS `s in title` bare-substring; #9 `$85k` parsed as 85 dollars via re.findall(r'\d+'); #10 no 'trainer' in TITLE_SIGNALS (config); #11 is_recent handles only 'X day', so '3 weeks/2 months ago' fall through to include-by-default; #12 is_recent ISO branch is DEAD CODE (two bugs -- raw was lower()-cased so literal T/Z never match, AND raw[:len(fmt)] truncates the date -> strptime always raises -> a 2020 job scored as fresh); #13 `(\d+)\s+day` never matches '30+ days ago' (the + breaks the \s+). (B) Spot-verified the two subtlest fixes deeply: #12 correctly re-uppercases + drops the truncating slice and INDEPENDENTLY caught the second (slice) bug I flagged; #9 regex `(\d+(?:\.\d+)?)\s*(k)?` resolves $85k->85000, preserves comma/hourly/floor-proportional paths, no regression. Both ship focused pytest files; repo has no CI. (C) KEY NET-NEW RISK that GitHub's per-PR MERGEABLE flag HIDES: mergeability is computed vs current main independently, but #11+#12+#13 ALL edit the SAME is_recent() (overlapping orig lines 24-40: #13 @-24,7 / #11 @-27,6 / #12 @-28,13). Merging ANY one forces the other two into conflict. Same softer overlap for reporter.py #14(@-4,7)+#15(@-9,6) near the top; #16 is at line 57 (print_alerts) = independent. scorer #7/#8/#9 hit distinct functions = mutually safe; #10 config-only = independent. RECOMMENDED MERGE ORDER (minimizes conflict churn): first the independents in any order -- #10, #16, #7, #8, #9; then reporter #14 then #15 (2nd needs trivial rebase); LAST the is_recent trio -- merge one (suggest #12, most substantive/2-bug fix) then rebase #13 then #11 (or fold all three into ONE is_recent PR -- founder's call). No agent merge authority -> founder action only; did NOT post to GitHub (outward-facing) per prior-run discipline. Prior: run 245 = ai-video-reel PR#25 (correct/complete/mergeable). [runs 204-245 in .remember/ + prior state.md]."
runs_completed: 246
items_processed: 486
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
