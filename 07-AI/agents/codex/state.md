---
agent: codex
display_name: "Codex"
emoji: "💻"
role: "Code Agent · GitHub Sync"
status: running
last_run: "2026-09-26T06:17:47Z"
current_task: "Run 383 (fleet review). Unit of work: turned the R382 prose runbook into a single GUARDED EXECUTABLE -- merge-fleet.sh (codex dir) -- after re-running the authoritative per-repo sweep (all 21 non-archived repos) + a LIVE merge-readiness audit (isDraft+mergeable+mergeStateStatus+base) of every target PR: ZERO drift vs R382 (all agent PRs MERGEABLE/CLEAN/non-draft; Community 10 fix/* non-default stacked bases + content #4/#8 stacking hold; 5 Section-6 drafts psychic#25/Link#5+#6/kai#2+#3 unchanged; still 0 merges fleet-wide). Script is DRY-RUN by default (prints plan, touches nothing); --execute runs the whole runbook in dependency order; before EVERY action it re-checks the PR live and auto-skips any DRAFT or non-MERGEABLE (cant die mid-run, cant merge a draft, cant no-op a stacked base); runs the #61/#38 keystone hand-close loops + auto-retargets content #4 off #2s branch; --only <section> scoping. FOUND+FIXED a real bug while proving it: python json prints True/False (capital) so the first draft-guard let all 4 drafts through as merges -- switched to gh native --jq (lowercase) -> verified dry-run net effect now matches the runbook EXACTLY: 21 merges + 14 PR-closes + 1 retarget + 27 issue-closes + 4 draft-skips. Appended R383 note to MERGE-RUNBOOK-2026-09-24.md linking the script. No merges executed (reserved for owner per governance)."
carryover: "CARRYOVER (owner-MERGE is the SOLE bottleneck; R383 re-confirmed 0 merges since ~Sep 11-12 across all 5 agent repos + Section-6; every agent-fleet code issue has a covering MERGEABLE PR -> DO NOT ship new tower PRs). The runbook is now BOTH prose (MERGE-RUNBOOK-2026-09-24.md) AND a one-command executable (merge-fleet.sh, same codex dir): tell Stef he can run `./merge-fleet.sh` (dry-run, safe) then `./merge-fleet.sh --execute` to clear the ENTIRE fleet queue in one shot -- it self-verifies (auto-skips drafts + non-mergeables), does keystone hand-closes, retargets content #4. Verified net effect: 21 merges + 14 PR-closes + 1 retarget + 27 issue-closes + 4 draft-skips. The 4 draft PRs (psychic #25, Link-inbio #5, kai-vault #2+#3) stay OWNER-ONLY until Stef clicks Mark ready for review; the script skips them by design. Merge order unchanged (JobScout #61 keystone->#63/#25/#27/#65/#67 + hand-close 30/32/34/36/38/41/43/45/47/49/51/53/55/57/59; Community #38 keystone->CLOSE 12 siblings 15-37 odd+even mix->hand-close issues 14-36->merge #40; EFA #25 first->#26/#27/#29/#31; content #2->retarget+merge #4->#6->#9->close #8; avrg #27+#31 auto-close). Owner-only remainders: EFA #30 schema-persist/#24 retire main, avrg #5 Supabase, forming-paws #8 (IL-SOS filing), + the 4 Section-6 drafts. NON-actionable (do NOT re-flag): skills-introduction-to-git #1 (course bot), ----Workspace-notes PR #1 (owner draft). New claude/*-default repos aeos/Stefan-Portfolio/agent-II all 0i/0pr (no new surface). NEXT: nothing to build -- each loop re-run the per-repo sweep of ALL non-archived repos + audit isDraft+mergeable+base on every target (behind_by alone != merge-readiness), and re-run `merge-fleet.sh` dry-run to confirm the plan still matches before nudging owner."
runs_completed: 383
items_processed: 739
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
