---
agent: antigravity
display_name: "Antigravity"
emoji: "🚀"
role: "General Agent · Explorer"
status: idle
last_run: "2026-08-13T03:32:12Z"
current_task: "Run 165: TASK = scan context + summarize active priorities + one meaningful unit of work. UNIT OF WORK = closed Run-164 handoff item #2 (the two run-agents.sh copies), with a correction: ~/clawd/scripts/run-agents.sh is NOT an accidental stale duplicate -- it is a DELIBERATE git-tracked disaster-recovery backup (committed 2026-08-06 because the fleet runner existed in NO repo; scripts/README.md documents it as a mirror of canonical ~/Desktop/run-agents.sh). ai.mundi.sync (launchd, every 5min) is unrelated (syncs agent-dashboard state to Vercel edge config), so there is NO automated copy mechanism -- divergence is purely manual edits. LIVE LIABILITY FOUND: the COMMITTED git backup still held the LIVE perplexity grant query (Run 163 edited only the working tree, never committed; Run 164 edited only the Desktop canonical), so a disaster-recovery restore would have RESURRECTED the billing loop Runs 160-164 fought. FIX (README's prescribed way, NOT a symlink): re-copied canonical Desktop -> clawd/scripts mirror (byte-identical, bash -n clean), committed as clawd 4a1f137 'Sync fleet backup mirror: retire perplexity grant query'. CORRECTION to Run-164 handoff: the 'consolidate to a symlink' idea is HARMFUL and RETRACTED -- a symlink shares one inode, so if the Desktop file is lost the backup becomes a dangling link and the content is gone; independence is the whole point of the mirror. Keep two REAL files + re-copy after edits. ACTIVE PRIORITIES (canonical, unchanged): P1 = OpenClaw Phase 1-4 (target 2026-10-12); Phase 2 Week-1 -- sign-off Aug 13 (6/6 criteria, DUE NOW), go/no-go Aug 17 EOD, formal gate Aug 18. P2 (after OpenClaw) = Track 1 Plug AI exec starts Oct 13 (grant loop CLOSED by choice 2026-07-29); Track 2 = BigHeart content-automation title/comp ask + Forming Paws live; Track 3 = AI consulting (built, not launched). Ongoing = vault upkeep. HANDOFF: (1) fleet backup drift CLOSED the right way -- git backup + canonical + mirror now all byte-identical with perplexity retired; committed so a restore is safe. (2) tried to add an anti-symlink guard + drift checklist to clawd/scripts/README.md but the write was PERMISSION-DENIED this run -- next run/founder should add it so nobody re-attempts the symlink. (3) Founder decision still open: fund OpenAI leg for Phase 2 or stay Claude-only. (4) Next antigravity loop: confirm Aug 13 Week-1 sign-off (6/6) + Aug 17 EOD go/no-go."
runs_completed: 165
items_processed: 674
last_error: null
color: "#F4B942"
house: "launchpad"
---

# Loop Rules

## Loop Start
1. Read `~/Desktop/Context/context.md`
2. Read `~/Desktop/Context/me.md`
3. Check bus for unread messages: `node ~/clawd/.bus/busctl.js unread --agent antigravity`
4. Read `~/Desktop/kai/07-AI/context/world.md`
5. Read this `state.md`
6. Execute task

## Loop End
1. Update `status`, `last_run`, `current_task`, `items_processed` in this file
2. Post to bus if meaningful work done: `node ~/clawd/.bus/busctl.js post --from antigravity --topic <topic> --msg "<summary>"`
3. Acknowledge bus: `node ~/clawd/.bus/busctl.js ack --agent antigravity`
4. Write summary message to `~/Desktop/kai/07-AI/chatroom/feed.md`

## Notes
- Antigravity is a per-task general-purpose agent. Invoked on demand.
- Reports into clawd via the shared bus on task completion.
