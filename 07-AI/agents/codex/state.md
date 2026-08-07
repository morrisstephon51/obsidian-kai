---
agent: codex
display_name: "Codex"
emoji: "💻"
role: "Code Agent · GitHub Sync"
status: running
last_run: "2026-08-07T14:20:00Z"
current_task: "Run 149: Reviewed + MERGED forming-paws PR#15 (fix: pin Vercel framework to nextjs), squash-merged at 2026-08-07T14:20:22Z, branch deleted. Clean +4/-0 single-file fix adding vercel.json {\"framework\":\"nextjs\"}. Independently verified all three PR claims before merging: (1) no pre-existing vercel.json on base (GH API 404), (2) next.config.ts has NO output:'export' so .next serverless is the correct target and 'nextjs' preset is right, (3) confirmed Next.js 15 / React 19 in package.json. Root cause was Vercel framework-detection falling back to the static preset and erroring 'No Output Directory named public found' even though next build compiles 14/14 pages -- vercel.json now forces the Next.js builder, no dashboard access needed. Unblocks Forming Paws (Track 2 / Puppy Power) deploys. Follow-through: posted comment #5218222725 on forming-paws PR#14 (upload-redirect, was UNSTABLE) noting its red Vercel check shares the same root cause and will go green once rebased onto main -- flagged for rebase. Remaining frontier: forming-paws #10 (admin queue, mergeable) + #14 (needs rebase), psychic-bassoon #11 draft / issue #12 auth-wall, ai-video-reel #23 (mergeable), community-intake #1, Link-inbio #11, job_opportunity_scanner PR#3 (HOLD, 4 of 6 cards broken upstream). Earlier runs in git history / bus."
runs_completed: 149
items_processed: 359
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
