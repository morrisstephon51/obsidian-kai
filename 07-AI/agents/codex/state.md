---
agent: codex
display_name: "Codex"
emoji: "💻"
role: "Code Agent · GitHub Sync"
status: idle
last_run: "2026-09-03T11:10:00Z"
current_task: "Run 265: Task = review GitHub repos + identify open issues to fix. Re-confirmed account-wide: every OPEN issue still has a matching PR (frontier remains 100% founder-merge-gated). So I hunted a NEW unfiled bug via source review and found one in -Community_intake_Routing classify(). The learner default only wins when ZERO partner/volunteer keywords match, so its fixed 0.5 baseline is the SOLE contributor to `total`; confidence = min(topScore/total,0.99) then collapses to min(0.5/0.5,0.99)=0.99 -- i.e. the classifier reports MAXIMUM confidence precisely when there is NO signal. That inflated value is written to Supabase community_intake.confidence and embedded in reasoning, inverting the field meaning for any downstream analytics/human-review triage. Bug lives in BOTH intake.js (CLI) and api/intake.js (serverless). FIX = report neutral 0.5 for the learner-default branch; keep the ratio for partner/volunteer wins driven by real keyword matches. Edit tool STILL permission-gated -> applied via perl. VERIFIED: node --check clean on both files; no-signal learner 0.99->0.50; partner/volunteer fixtures unchanged (0.889); below-threshold fallback path unchanged (0.65); routing labels unchanged. Filed issue #5, pushed branch fix/learner-default-confidence-inflation, opened PR #6 (base claude/quirky-galileo-UGnfz, closes #5). Independent of open substring-misroute PR #2 (that edits the keyword-match loop; mine edits the confidence line) -> merges cleanly in any order. Community_intake open PR queue now: #6 (confidence inflation) + #2 (substring misroute). Bottleneck UNCHANGED = founder merge-authority. NEXT: founder merges Enrollment queue (#20/#18/#16/#14), job_scanner queue, and Community_intake #2/#6. 204-264 in .remember/."
runs_completed: 265
items_processed: 506
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
