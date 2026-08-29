---
agent: codex
display_name: "Codex"
emoji: "💻"
role: "Code Agent · GitHub Sync"
status: running
last_run: "2026-08-28T17:20:00Z"
current_task: "Run 239: MERGE-READINESS AUDIT of the founder-blocked PR queue instead of a 19th speculative PR. Frontier is 100% founder-authority-blocked -- 18 open PRs across 5 repos, 0 code-actionable open issues (psychic#21 has fix PR#22; forming-paws#8 = IL-SOS filing; avrg#5 = Supabase; skills-intro#1 = git tutorial, not a real project). Rather than pile on another found-and-fixed PR, I empirically de-risked the merge queue with REAL local git merges (clone + fetch pull/N/head + git merge), because GitHub's per-PR 'mergeable' flag only checks each PR vs base IN ISOLATION and lies about how PRs interact once earlier ones land. (1) job_opportunity_scanner 10-PR stack (#7-#16, all base clever-cannon, 6 touch scorer.py / 3 touch reporter.py): sequential merge sim 7->16 = 10/10 CLEAN, 0 conflicts; built the full merged tree, venv + pytest 9.1.1 -> 58 tests pass. Independently re-confirms codex Run 236; safe to batch-merge in any order, no rebases. (2) psychic-bassoon 5-PR stack: NEW HAZARD not in FOUNDER-ACTION-QUEUE.md -- queue lists #1 as CLEAN with only an .env.example clash vs draft #11, but sim 20->19->22->1 shows #1 CONFLICTS on lib/utils.ts once #22 lands: #22 rewrites formatShortDate via a new toLocalDate() (the issue-#21 off-by-one fix) AND fixes formatDate; #1 DELETES formatShortDate -> edit/delete collision git cannot auto-resolve. Verified SAFE resolution: keep #1's deletion (formatShortDate has ZERO callers on main and in #1's tree -- dead code), and #22's substantive fix is on formatDate which #1 never touches, so it survives. Recommended merge order: #20 (CVE) -> #22 (closes #21) -> #19 (headers) -> #1 LAST with one manual keep-the-deletion resolution + concatenate .env.example vs draft #11. Deliverables: durable artifact agents/codex/MERGE-READINESS-2026-08-28.md + high-signal warning comment on psychic-bassoon PR#1 (issuecomment-5455856070). No code blockers introduced; everything remains one founder click / one safe manual resolve from done. RECOMMEND Stef: batch-merge jobscout #7-#16 (proven green), merge psychic trio #20->#22->#19, then #1 (expect the flagged lib/utils.ts conflict), avrg #25, sign Week-1 gate, file forming-paws #8. PRIOR run 238: fixed CSV platform-detect substring misroute in Enrollment_Funnel_Agent, shipped PR#14 (still open/mergeable; clawd#252 independently verified REAL). [runs 204-238 in .remember/ + prior state.md]."
runs_completed: 239
items_processed: 470
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
