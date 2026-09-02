---
agent: codex
display_name: "Codex"
emoji: "💻"
role: "Code Agent · GitHub Sync"
status: idle
last_run: "2026-09-02T14:40:00Z"
current_task: "Run 260: De-duplicated the Community_intake merge queue instead of filing yet another merge-blocked bug PR (bottleneck is founder merge-authority, not bug supply). Two OVERLAPPING open PRs existed for the same substring-misroute bug (issue #3): PR #2 (fix/classify-substring-misroute, Aug 28) fixes BOTH api/intake.js (serverless endpoint the public form POSTs to) AND intake.js (CLI) with the word-boundary matchesKeyword regex, plus adds export{classify}+isMainModule guard for testability. PR #4 (Sep 2) fixes api/intake.js ONLY with the IDENTICAL matchesKeyword body -- a strict subset; its own description was factually wrong (claimed #2 left api/intake.js untouched, but #2 already includes it). Merging both = overlapping-hunk conflict for zero added coverage. ACTION: closed PR #4 as superseded (diff-proof comment), left recommend-merge comment on PR #2 (CLEAN/MERGEABLE, closes #3). Community_intake queue now 1 clean PR instead of 2 conflicting. Also verified job_opportunity_scanner has 11 open PRs, most touching scorer.py/reporter.py -- all MERGEABLE now but LATENT-CONFLICTING (first merge breaks the rest); PR #18 has scope creep (.claude/, public/index.html, vercel.json beyond the salary fix). Bottleneck UNCHANGED = 100pct founder merge-authority. NEXT: founder merges PR #2 (Community_intake), then sequences scorer PRs in one branch to avoid cascade conflicts. 204-259 in .remember/."
runs_completed: 260
items_processed: 500
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
