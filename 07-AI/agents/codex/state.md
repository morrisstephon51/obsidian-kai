---
agent: codex
display_name: "Codex"
emoji: "💻"
role: "Code Agent · GitHub Sync"
status: running
last_run: "2026-08-31T16:31:00Z"
current_task: "Run 249: DEEP-REVIEWED canonical PR #22 (psychic-bassoon, closes #21) -- first run to actually read its internal contents rather than compare it file-list-wise vs the now-closed #24. Confirmed run 248 dedup held: #24 CLOSED, #22 is the sole open PR referencing #21, CLEAN/MERGEABLE. Fix is CORRECT: toLocalDate() parses YYYY-MM-DD via numeric Date(y,m-1,d) constructor (local midnight) and passes full datetime strings through untouched -- exactly right for the UTC off-by-one. FOUND a net-new quality issue no prior run caught: PR #22 adds TWO overlapping test files -- lib/utils.test.ts (4 tests, pins TZ=America/Chicago, has the full-datetime passthrough boundary case) AND tests/utils.date.test.ts (3 tests, strict subset, no TZ pin). The npm test script is node --test lib/**/*.test.ts -- glob only matches lib/, so tests/utils.date.test.ts NEVER runs via npm test (verified empirically with a fixture: runner reports tests 1, only lib/utils.test.ts). Orphaned dead weight + false-coverage risk on a UTC CI box. ACTION: posted a precise review comment on #22 (comment 5481370511) recommending deletion of tests/utils.date.test.ts, keep the lib/ superset; fix itself unchanged, then clean to merge. Did NOT push to the byte-frozen PR branch (would reset founder review / recompute mergeability) -- review-comment is the senior-safe move. Account-wide open ISSUES still 4 (psychic #21 sole code bug; forming-paws #8, ai-video-reel #5, skills-git #1 non-code). Bottleneck stays 100pct founder-authority. Prior: run 248 dedup closed #24; runs 204-247 in .remember/ + prior state.md."
runs_completed: 249
items_processed: 489
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
