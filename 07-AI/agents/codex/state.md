---
agent: codex
display_name: "Codex"
emoji: "💻"
role: "Code Agent · GitHub Sync"
status: idle
last_run: "2026-08-29T05:50:00Z"
current_task: "Run 240: CLOSED THE LOOP on the one real open code bug in the whole account -- psychic-bassoon #21 (formatDate/formatShortDate off-by-one for date-only strings). Fresh account-wide scan reconfirms the frontier is 100% founder-blocked: 18 open PRs across 5 repos + exactly 4 open issues, all non-code-actionable except #21 which already has fix PR#22 -- (avrg/ai-video-reel #5 = Supabase project setup; forming-paws #8 = IL SOS legal filing; skills-intro #1 = GitHub tutorial bot). Prior runs verified the MERGE MECHANICS of the jobscout(10) and psychic(5) stacks but never verified that #22 actually RESOLVES #21 end-to-end. Did that empirically: cloned psychic-bassoon, ran PR#22 own regression suite (tests/utils.date.test.ts, Node built-in --test runner) against BOTH trees under TZ=America/Chicago. On main (buggy bare new Date(dateStr)): 3 fail / 1 pass -- reproduced 2026-09-15 -> Monday September 14 2026 (a Tuesday) off-by-one. On PR#22 (new toLocalDate() helper parsing YYYY-MM-DD as local midnight, datetime strings pass through): 4/4 pass. The single test passing on main is the datetime-passthrough case, proving the suite is a real regression guard not a tautology. VERDICT: #21 is a real CT-timezone bug, #22 is correct as-is and merge-ready, no code changes needed. Left before/after evidence comment on PR#22 (issuecomment-5460658645) reiterating the Run 239 merge-order caveat: land #20->#22->#19->#1 (#1 deletes dead formatShortDate and edit/delete-collides with #22 if #1 lands first; #22 substantive fix is on formatDate which #1 never touches -> survives). No new speculative PR, no artifact sprawl. Frontier still one founder click from clearing. PRIOR run 239: merge-readiness audit (jobscout #7-#16 batch-merge proven green via real git replay + pytest 58 pass; psychic #1<->#22 lib/utils.ts edit/delete hazard found + warned). [runs 204-239 in .remember/ + prior state.md]."
runs_completed: 240
items_processed: 471
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
