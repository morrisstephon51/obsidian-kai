---
agent: codex
display_name: "Codex"
emoji: "💻"
role: "Code Agent · GitHub Sync"
status: idle
last_run: "2026-09-05T16:24:00Z"
current_task: "Run 277: Task = review GitHub repos + fix open issues. NET-NEW BUG FILED (not re-verify): -Community_intake_Routing issue #7 — how_heard attribution field pollutes intent scoring. classify() joins interest_description + how_heard into scored text (both intake.js AND api/intake.js), but how_heard is marketing-source metadata. Attribution phrases contain partner/volunteer keywords (brand, partner, referral, company, agency, community organization) -> a genuine learner SOURCE contaminates their INTENT. DIFFERENTIAL vs current source: learner 'I want to learn AI for myself' + how_heard='A brand partner referred me' -> CURRENT routes PARTNER @0.8 (founder false-alert, learner never gets welcome email); FIXED (desc-only) -> learner @0.99. Below-threshold cases still corrupt confidence 0.99->0.65. INDEPENDENT of open #3 (substring; offending tokens are whole words, PR #2 whole-token match does NOT fix) and #5 (confidence). One-line fix proposed both files: classify on interest_description only, keep how_heard for logging. Orthogonal to PRs #2/#6. Repro /tmp/howheard_repro.mjs: 1/4 hard-misroute + 2/4 confidence-corrupt. Default branch claude/quirky-galileo-UGnfz (not main). PRIOR: 276 job_scanner #19 canonical (28/28, 11/11 diff); 275 Enrollment #14; 274 Enrollment #20/#19; 273 Enrollment #18; 272 job_scanner #19; 271 Enrollment #16; 270 psychic-bassoon #22; 269 Community_intake #2/#6/#3. STILL OPEN needing founder merge: job_scanner #19 (canonical); Community_intake #2 then #6 (+now #7 needs fix PR); psychic-bassoon #22/#20/#19; Enrollment #14/#16/#18/#20. 204-276 in .remember/."
runs_completed: 277
items_processed: 518
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
