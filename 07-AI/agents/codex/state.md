---
agent: codex
display_name: "Codex"
emoji: "💻"
role: "Code Agent · GitHub Sync"
status: idle
last_run: "2026-09-03T23:30:00Z"
current_task: "Run 268: Task = review GitHub repos + fix open issues. Attacked the biggest bottleneck queue instead of another orphan probe: independently VERIFIED job_opportunity_scanner PR #19 (consolidated scorer fixes, merge once not 8 times; supersedes #7-#13,#18). Cloned + checked out #19, ran its own suite: python3 tests/test_scorer_consolidated.py -> ALL PASSED (18 checks). Confirmed all 8 fixes present & correct line-by-line in scorer.py+config.py (#7 il token, #8 whole-word TITLE_SIGNALS, #9 $85k->85000, #10 trainer, #11 weeks/months recency, #12 ISO dead-code fix, #13 30+ days, #17 weekly/monthly->annual). MERGEABLE/CLEAN. TWO PROVEN CORRECTIONS: (1) PR #19 body FALSELY claims to deliberately exclude public/index.html, vercel.json, .claude/commands/dd.md -- git diff main...head shows the merge delta ADDS all + .claude/skills/remote-control/* + .gitignore (harmless scaffold, mislabeled scope). (2) Ground truth on branch-target ambiguity: repo DEFAULT branch IS claude/clever-cannon-IDh3G but PR #19 TARGETS main, so merging it advances main NOT the default branch. Posted evidence + merge recommendation on PR #19 (issuecomment-5533424793): scorer logic safe; founder decides (a) extra files here vs separate chore PR, (b) confirm main is right target vs retarget to default. PRs #14/#15/#16 report-layer are independent, still need separate merges. Did NOT merge (founder authority). NEXT: founder merges #19 + closes #7-#13,#18; then Enrollment #16/#18/#20, Community_intake #2/#6, psychic-bassoon #20/#22. 204-267 in .remember/."
runs_completed: 268
items_processed: 509
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
