---
agent: codex
display_name: "Codex"
emoji: "💻"
role: "Code Agent · GitHub Sync"
status: running
last_run: "2026-09-23T23:15:00Z"
current_task: "Run 370 (JobScout / job_opportunity_scanner). Found + shipped a genuinely NEW, distinct-class bug OUTSIDE the over-farmed scorer.py towers: the /scan command prompt (.claude/commands/scan.md) re-implements the whole filter+score pipeline inline as hand-scoring instructions, duplicating scorer.py/config.py -- and the copies drifted. Step 4 title table was missing trainer/community/developer vs config.py TITLE_SIGNALS; `trainer` is a DOCUMENTED, unit-tested fix (config.py:71-73 + tests/test_title_trainer_signal.py) added so the literal target query 'healthcare IT trainer' stops scoring zero on the 40%-weighted title dim -- but the prompt copy stayed stale, so if /scan hand-scores per the prompt the exact zeroed-out bug recurs for a query the tool is built to search. Filed issue #66 (documents the duplication + the trainer regression + same-class twins: the 'tek systems' spacing bug #64/PR#65 has an untouched twin at scan.md:49; the entire scorer hardening tower only governs scorer.py not the prompt path). Shipped PR #67 (closes #66): prompt-only, no Python touched -- (1) synced Step 4 title table to config.py TITLE_SIGNALS (exact 17/17 match verified), (2) added source-of-truth notes to Steps 3-4 (filter via scorer.is_agency/is_recent, score via scorer.score_job; code wins on disagreement) to kill future twin-drift. VERIFIED: parity assertion True; full suite 10/10 files, 66 assertions green (unchanged, reran); PR #67 MERGEABLE/CLEAN, touches ONLY scan.md so DISJOINT from all 5 other open JobScout PRs (#61/#63/#65/#27/#25 all touch scorer.py/config.py/tests) -- merges in any order. Deferred to owner (unverifiable w/o live MCP env): fully collapsing scan.md onto scorer.filter_and_score at runtime. Owner-MERGE remains the sole bottleneck (0 merges since R320)."
carryover: "CARRYOVER (owner-MERGE still the sole bottleneck; 0 merges since R320). NEW R370: JobScout issue #66 + PR #67 -- /scan prompt (.claude/commands/scan.md) duplicates scorer.py/config.py and drifted (title table missing trainer/community/developer; trainer = a tested regression fix that never reached the prompt). PR #67 syncs the prompt to config.py + adds source-of-truth notes; prompt-only, tests 10/10 green, MERGEABLE, touches ONLY scan.md so disjoint from #61/#63/#65/#27/#25 (merge in any order). Same-class twin still open: 'tek systems' spacing (PR #65 fixes config.py) needs a twin fix at scan.md:49. JobScout merge plan: PR #61 (salary-cadence regex superset -> close #26-#59) + #63 (keyword whole-word, closes #62) + #65 (TEKsystems blocklist, closes #64) + #25/#27 (salary-range/recency) + NEW #67 (scan-prompt parity, closes #66) -- all MERGEABLE + mutually disjoint. Community Intake: keystone PR #38 (intent-based classify consolidation, supersedes #14-#36) then PR #40 (web /api/intake routing parity, closes #39). agent_I_content: PR #9 (glob test-runner, merge FIRST) + #2/#4/#6/#8 + issues #3/#5/#7. Enrollment_Funnel CSV set #25/#26/#27 + issue #24 (retire stale main). avrg PR #27 + PR #31; avrg issue #5 (Supabase setup) blocks avrg e2e verification."
runs_completed: 370
items_processed: 685
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
