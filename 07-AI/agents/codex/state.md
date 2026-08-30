---
agent: codex
display_name: "Codex"
emoji: "💻"
role: "Code Agent · GitHub Sync"
status: idle
last_run: "2026-08-30T05:09:00Z"
current_task: "Run 242: STOPPED re-verifying the same frontier and shipped real code instead. Live gh scan = frontier IDENTICAL to Runs 240/241 (4 open issues: psychic #21 [fix PR#22], forming-paws #8 [IL legal], ai-video-reel #5 [Supabase infra], skills-intro #1 [git tutorial] -- only #21 code-actionable, already fixed). Rather than post another re-verification comment (=sprawl Stef warned about), CLOSED A GENUINE GAP: PR#22's toLocalDate fix shipped with ZERO tests and the repo had NO test runner at all -- a silently TZ-dependent bug (#21) is exactly the kind that regresses on a later refactor. Added lib/utils.test.ts using the built-in Node test runner (Node 25, native TS) => ZERO new deps, NO package-lock.json change; added `npm test` -> node --test 'lib/**/*.test.ts'. Test pins TZ=America/Chicago before import for determinism in the west-of-UTC zone where the bug manifests (also the audience). EMPIRICALLY PROVEN both directions: 4/4 PASS on PR#22 branch; same tests FAIL against pre-fix main (render 'Aug 29'/'August 29' for input '2026-08-30'). Also locks toLocalDate's regex boundary: full datetime strings (…T02:00:00Z) still respect explicit UTC time, not coerced to local midnight. Committed 22abe80 to fix/utils-date-off-by-one (strengthens EXISTING PR#22 -- deliberately NOT a new PR, since the founder's 17-PR backlog is the bottleneck), pushed, PR stays MERGEABLE (UNSTABLE = Vercel preview rebuilding only; no CI in repo). Touches only utils.test.ts + package.json, NOT formatShortDate => #1 edit/delete merge resolution unchanged (order still #20->#22->#19->#1-last). Posted 1 factual PR comment (issuecomment-5466847147). Net: highest-priority code PR now has a real regression guard + first test infra in a zero-test repo; frontier still 100% founder-blocked otherwise. [runs 204-241 in .remember/ + prior state.md]."
runs_completed: 242
items_processed: 473
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
