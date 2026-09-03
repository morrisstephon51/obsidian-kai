---
agent: codex
display_name: "Codex"
emoji: "💻"
role: "Code Agent · GitHub Sync"
status: idle
last_run: "2026-09-03T19:20:00Z"
current_task: "Run 267: Task = review GitHub repos + identify open issues to fix. Re-confirmed account-wide: EVERY open issue across job_opportunity_scanner(#17), Enrollment(#19/#17/#15), Community_intake(#5/#3), psychic-bassoon(#21), forming-paws(#8), ai-video-reel(#5) already has a matching open PR -> bottleneck stays founder merge-authority. CORRECTED prior mental model: job_scanner default branch is claude/clever-cannon-IDh3G (NOT main) and Enrollment default is claude/keen-noether-VED1j, so PRs targeting those ARE hitting repo-default; #19-to-main is the odd one out. The real merge-paralysis driver is branch-target AMBIGUITY, not orphan branches. NEW UNIT (not a repeat, not a new PR): chased the uninvestigated lead sitting in psychic-bassoon issue #21 since run 234 -- the sibling content-engine/client/src/lib/utils.ts formatDate/formatDateTime. Traced end-to-end via clone+grep: formatDate = 0 callers; formatDateTime = imported once (ScheduleCalendar.tsx:5) but 0 call sites (dead import; noUnusedLocals=false so not build-breaking; real render at :79 uses inline Date().toLocaleTimeString); ALL client date fields (scheduledAt/publishedAt/createdAt/updatedAt) are full ISO timestamps from DB cols so the UTC date-only off-by-one cannot trigger. VERDICT: latent/safe, no active bug, no fix needed now -> recommended a defensive toLocalDate guard whenever PR #11/content-engine work lands. Posted evidence comment on issue #21 (issuecomment-5530917686), closing the open worth-a-glance thread. Did NOT open a PR (queue saturated) and did NOT merge (founder authority). NEXT: founder merges saturated queues (job_scanner #19; Enrollment #18/#16/#20/#14; Community_intake #6/#2; psychic-bassoon #22/#20/#19). 204-266 in .remember/."
runs_completed: 267
items_processed: 508
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
