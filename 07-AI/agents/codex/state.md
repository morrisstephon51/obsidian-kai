---
agent: codex
display_name: "Codex"
emoji: "💻"
role: "Code Agent · GitHub Sync"
status: idle
last_run: "2026-09-03T15:11:00Z"
current_task: "Run 266: Task = review GitHub repos + identify open issues to fix. Re-confirmed the account-wide pattern (every OPEN issue already has a matching OPEN PR; bottleneck = founder merge-authority, unchanged across 265 runs). Rather than manufacture PR #266 onto a saturated founder-gated queue, did the higher-value unit: VERIFIED the existing consolidated fix in job_opportunity_scanner. PR #19 (fix/scorer-consolidated) targets main, is MERGEABLE/CLEAN, and fixes issues #7,#8,#9,#10,#11,#12,#13,#17 together (IL-substring, ai-substring title, $85k k-notation, trainer title, weeks/months recency, dead-code ISO-date branch, 30+ days, weekly/monthly salary normalization) with a single regression file. KEY STRUCTURAL FINDING: PRs #7-#16 are stuck -- their base is the ORPHAN branch claude/clever-cannon-IDh3G, NOT main, so they can never reach main directly; #19 supersedes all of them and #18 is a strict subset of #19. VERIFIED by cloning fix/scorer-consolidated and running its suite: python3 tests/test_scorer_consolidated.py -> 28/28 PASS (ALL PASSED) on Python 3.14.3. Posted an evidence-backed merge-triage comment on PR #19 (issuecomment-5527859042): merge #19 to clear the whole scorer queue in one reviewed merge, then close #7-16 + #18 as superseded-by-#19 -> job_scanner 12 open PRs + 1 open issue collapse to 0. Attacks the real bottleneck (merge paralysis over a confusing 12-PR queue) instead of adding to it. Did NOT merge -- merge authority remains the founder's. NEXT: founder merges job_scanner #19 then bulk-closes the superseded stack, Enrollment queue (#20/#18/#16/#14), Community_intake #2/#6. 204-265 in .remember/."
runs_completed: 266
items_processed: 507
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
