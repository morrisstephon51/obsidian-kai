---
agent: codex
display_name: "Codex"
emoji: "💻"
role: "Code Agent · GitHub Sync"
status: running
last_run: "2026-08-31T08:27:00Z"
current_task: "Run 248: RECONCILED DUPLICATE PRs (cleanup of a mess run 247 created). Swept open ISSUES account-wide: still only 4 (psychic-bassoon #21 = the sole code bug; forming-paws #8, avrg #5, skills-git #1 non-code). Discovered issue #21 had TWO open PRs both 'Closes #21': #22 (run 235) and #24 (run 247, MINE). Run 247 opened #24 without checking for an existing PR -- redundant. Compared diffs: #24 changes only lib/utils.ts; #22 is a STRICT SUPERSET -- identical toLocalDate() helper in lib/utils.ts PLUS a zero-dep regression test (node --test) PLUS an npm test script in package.json. Two PRs closing one issue = merge hazard (first-to-land dangles/conflicts the other). RESOLVED: commented on #24 pointing to #22 as canonical (no work lost, #22 superset), closed #24, deleted branch fix/date-only-utc-offbyone. VERIFIED #24 state=CLOSED. #21 now has exactly ONE canonical open PR (#22) awaiting founder merge -- clean review path restored. Reversible under Operating Rule 5, founder own repo. Prior: run 247 opened the now-closed #24; runs 204-246 in .remember/ + prior state.md."
runs_completed: 248
items_processed: 488
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
