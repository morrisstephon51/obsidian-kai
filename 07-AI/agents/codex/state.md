---
agent: codex
display_name: "Codex"
emoji: "💻"
role: "Code Agent · GitHub Sync"
status: idle
last_run: "2026-08-29T19:40:00Z"
current_task: "Run 241: VERIFY-DON'T-TRUST-THE-BUS on my OWN prior claim -- caught and corrected a factual error propagating across the fleet about what psychic-bassoon PR#22 actually fixes. Fresh account-wide scan: issue frontier IDENTICAL to Run 240 (4 open issues: psychic #21 [has fix PR#22], forming-paws #8 [IL legal filing], ai-video-reel #5 [Supabase infra], skills-intro #1 [git tutorial bot] -- only #21 code-actionable, already fixed). Nothing merged/closed since Run 240; #21 still OPEN, PR#22 MERGEABLE/CLEAN. Instead of re-running the (already-done) #22 regression suite = sprawl, resolved a genuine CONTRADICTION in the agents' bus reports: Run 240 said '#22 substantive fix lives on formatDate which #1 never touches'; clawd Run 254 said '#22 rewrites formatShortDate'; antigravity Run 229 said '#22 fixes formatShortDate+formatDate'. Pulled the actual PR#22 diff = GROUND TRUTH: #22 applies new toLocalDate() to BOTH formatDate AND formatShortDate (both new Date(dateStr)->toLocalDate). So issue #21 (names both fns) is FULLY resolved by #22 alone; antigravity Run 229 was the accurate report, my own Run 240 was WRONG. The error mattered: Run 240 merge-note comment on PR#22 (issuecomment-5460658645) told the founder '#22 fix lives on formatDate... so it survives' -- misleading, since #22 ALSO patches formatShortDate and #1 DELETES it => real edit/delete conflict on formatShortDate (both PRs branch same base blob 8d9f682) that git WILL flag; a reader trusting 'it survives' could resolve it wrong (keep #22 formatShortDate, silently reverting #1 dead-code deletion). Verified formatShortDate is genuinely dead (0 callers across all 114 .ts/.tsx on main; only occurrence = its own def). Posted ONE corrective comment on PR#22 (issuecomment-5464461610): order unchanged #20->#22->#19->#1-last, but the correct reason = keep #1 deletion of dead formatShortDate (costs nothing), formatDate fix + toLocalDate survive automatically; the one manual edit/delete resolve happens at #1, not #22. No new files, no speculative PR. Frontier still 100% founder-blocked, 0 code work outstanding. PRIOR run 240: empirically verified #22 resolves #21 via TZ=America/Chicago regression suite (3-fail->4-pass). [runs 204-240 in .remember/ + prior state.md]."
runs_completed: 241
items_processed: 472
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
