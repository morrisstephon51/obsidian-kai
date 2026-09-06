---
agent: codex
display_name: "Codex"
emoji: "💻"
role: "Code Agent · GitHub Sync"
status: idle
last_run: "2026-09-05T21:05:00Z"
current_task: "Run 279: NEW distinct bug found+fixed in Community_intake_Routing. Filed #9 + shipped PR #10 (branch fix/single-keyword-partner-volunteer-misroute, base claude/quirky-galileo-UGnfz, closes #9). Bug: learner 0.5 baseline sat in the confidence DENOMINATOR (total), so a lone partner/volunteer keyword computes 1.0/1.5=0.667 < 0.7 threshold -> hard-fallback to learner. Every single-line sponsor/partner/mentor inquiry was silently downgraded to the learner waitlist, starving the founder-notification path. Fix: score a real winner against matched-signal evidence only (scores.partner+scores.volunteer); learner-default path unchanged. Applied to BOTH intake.js + api/intake.js. Verified 18/18 differential (real classify() per file): 5 single-keyword partner/volunteer cases now route right; genuine-learner@0.99, ambiguous 1v1 tie@0.65, strong multi-kw controls all unchanged. Orthogonal to #3/#7 (substring/how_heard) and #5 (no-signal confidence). Community_intake open PRs now #2,#6,#8,#10 (all independent off base, awaiting founder merge). STILL OPEN needing founder merge: job_scanner #19; Community_intake #2/#6/#8/#10; psychic-bassoon #22/#20/#19; Enrollment #14/#16/#18/#20. 204-278 in .remember/."
runs_completed: 279
items_processed: 520
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
