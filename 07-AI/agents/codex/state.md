---
agent: codex
display_name: "Codex"
emoji: "💻"
role: "Code Agent · GitHub Sync"
status: idle
last_run: "2026-09-23T10:36:00Z"
current_task: "Run 367 (JobScout / job_opportunity_scanner). Re-surveyed the full open PR+issue surface per-repo across all 5 active agent repos (gh pr list authoritative): every open issue already maps to an open MERGEABLE PR, so the bottleneck is still owner-MERGE (0 merges since R320) — did NOT re-stack any tower or re-certify keystones. Instead shipped the one genuinely-unfiled distinct-class bug from R366 carryover: JobScout AGENCY_BLOCKLIST token 'tek systems' (spaced) never substring-matches the real firm 'TEKsystems' (one word) as it registers on ZipRecruiter/Indeed, so is_agency() let a top-5 US IT staffing agency (Allegis) evade the filter into scored results. Opposite direction from the scorer 'ai'->retail substring class (there substring OVER-matches and word-boundary is the fix; here substring is correct but the token was written in a form the brand never uses). Verified empirically: pre-fix, TEKsystems / ', Inc.' / 'Global Services' all PASSED the filter while every other blocklist entry matches its real brand form. Filed issue #64, shipped PR #65 (branch fix/agency-blocklist-teksystems-spacing, base default claude/clever-cannon-IDh3G): one-line config.py token 'tek systems'->'teksystems' + tests/test_agency_blocklist_teksystems.py (is_agency had ZERO coverage). Full standalone suite 11 files/73 assertions green, 0 regressions. PR #65 MERGEABLE/CLEAN, config-only, DISJOINT from all open scorer PRs (#25/#27/#61/#63) -> independently mergeable in any order. Not self-merged (owner call). Also confirmed avrg PR #27 already fixes BOTH #26 and #28 (persona DELETE guard) despite being titled 'closes #26' only -> commented on avrg #28 so owner closes it alongside #26 on merge (no separate change needed)."
carryover: "CARRYOVER (owner-MERGE still the sole bottleneck; 0 merges since R320). NEW this run: JobScout PR #65 (TEKsystems blocklist spacing, closes #64) merge-ready, config-only, DISJOINT from all scorer PRs -> owner can merge alongside #25/#27/#61/#63 in any order. avrg #28 is already covered by PR #27 (guard removed from persona DELETE too) -> close #28 with #26 when merging #27. Unchanged keystones awaiting owner: JobScout PR #61 (salary-cadence regex superset -> merge + close #30-#59) + PR #63 (keyword whole-word, closes #62, disjoint) + #25/#27 (salary-range/recency). Community Intake PR #38 (intent consolidation superset of #14-#36 except contested #22) -> merge #38 + close issues #14-#36 + tower PRs #15-#37. agent_I_content PR #9 (glob test-runner, merge FIRST) + fix PRs #2/#4/#6/#8 + issues #3/#5/#7. Enrollment_Funnel CSV set #25/#26/#27 + issue #24 (retire stale main). avrg PR #27 (closes #26+#28) + PR #31 (schedule TZ anchor, closes #30); avrg issue #5 (Supabase setup) still blocks all avrg e2e. Uncovered-observation queue now empty: the R366 'tek systems' blocklist bug is SHIPPED (PR #65)."
runs_completed: 367
items_processed: 682
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
