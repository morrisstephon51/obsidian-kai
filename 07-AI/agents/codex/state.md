---
agent: codex
display_name: "Codex"
emoji: "💻"
role: "Code Agent · GitHub Sync"
status: running
last_run: "2026-09-02T19:05:00Z"
current_task: "Run 261: Executed the NEXT action from run 260 -- consolidated the cascade-conflicting job_opportunity_scanner scorer PRs into ONE mergeable branch so the founder merges once instead of resolving 7+ sequential rebase conflicts. Verified the conflict claim by diff: PRs #11/#12/#13 ALL edit is_recent() (line-offset collisions on sequential merge); PRs #9 and #18 BOTH rewrite _salary_score() (direct overlapping-hunk conflict). Built branch fix/scorer-consolidated integrating 8 fixes coherently: #7 IL whole-token location match, #8 title whole-word match (stops 'ai' matching retAIl/repAIr), #9 $85k thousands notation, #10 add 'trainer' to TITLE_SIGNALS, #11 weeks/months recency, #12 ISO posted_date honored (was dead code -- truncated slice + lowercased T/Z), #13 30+ days ago filter, plus #17 weekly/monthly salary-period normalization pulled from PR #18 MINUS its .claude/public/vercel.json scope-creep files. Added tests/test_scorer_consolidated.py: 28 self-contained checks (pytest OR plain python3, no deps since repo has no CI) -- ALL GREEN. End-to-end filter_and_score smoke test confirms stale 30+ days ago job filtered + $85k Chicago AI-training role scores 8. Pushed + opened PR #19 (supersedes #7-#13+#18, closes #17) with full mapping table; commented on PR #18 (scope-creep files excluded) and issue #17. Bottleneck UNCHANGED = founder merge-authority, but merge burden for scorer queue cut from ~8 conflict-prone merges to 1 clean merge. NEXT: founder merges PR #19 (job_scanner) + PR #2 (Community_intake); reporter PRs #14/#15/#16 remain separately mergeable. 204-260 in .remember/."
runs_completed: 261
items_processed: 501
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
