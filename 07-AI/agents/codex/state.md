---
agent: codex
display_name: "Codex"
emoji: "💻"
role: "Code Agent · GitHub Sync"
status: idle
last_run: "2026-09-14T00:56:16Z"
current_task: "Run 314 (task: review GitHub repos, fix an open issue). Swept all active repos. Enrollment_Funnel_Agent CERTIFIED clean: all 3 orphan fix branches (date-range #17, top/bottom overlap, narrative+UTM #8/#9) already on default; the reporter.ts/claude-client.ts comma-parse sibling-drift is already handled by open PR #25 which touches BOTH files; only pending items are owner-merge PRs #25/#26. -Community_intake_Routing CERTIFIED clean: intake.js and api/intake.js classify() are in lockstep (identical SIGNALS + confidence logic), 5 orphan fix branches (#3 word-boundary, #5 neutral-learner, #7 how_heard, #9 evidence-denominator, #12 reasoning-parity) all already on default, and the test suite enforces cross-impl reasoning parity. SHIPPED NEW FIX -> job_opportunity_scanner _salary_score(): it read only the FIRST number in a salary string, so \"$0 - $200k DOE\" scored 0.000 (placeholder-0 low buried a $200k role) and \"$85 - $110k\" scored 0.002 (shared k on the upper bound ignored). Fix parses every figure with optional k, applies a range shared-k to a bare sub-1000 bound, and uses the first figure as the conservative low with fallback to the next POSITIVE figure only when the low is a placeholder 0 (a real low is never overridden, so 401k/PTO/stray-year cannot hijack the amount; pre-existing test_401k_does_not_hijack_the_amount stays green). Added tests/test_salary_range_parsing.py; ran FULL suite 11/11 green + py_compile OK. Opened PR #25 base=default claude/clever-cannon-IDh3G (NOT main), MERGEABLE/CLEAN, +111/-8, 2 files. Did NOT self-merge, left to owner. Note: inert git clone left at ~/Desktop/.codex-work/jos (rm blocked by workspace guard)."
runs_completed: 314
items_processed: 577
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
