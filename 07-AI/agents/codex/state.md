---
agent: codex
display_name: "Codex"
emoji: "💻"
role: "Code Agent · GitHub Sync"
status: idle
last_run: "2026-09-15T10:25:00Z"
current_task: "Run 322 (review GitHub repos / fix open issues). Confirmed the standing bottleneck: 9 open PRs across 5 repos, all CLEAN and stalled on OWNER MERGE (nothing merged since run 320); every filed issue has an open PR or is owner-only. Did NOT pile a redundant 10th PR. Non-redundant work: (A) TEST-MERGED every multi-PR set locally in BOTH orders -- agent_I_content stack #2->#4->#6 CLEAN (verified #2 is ancestor of #4 = true stack, #4 based on #2 head not default); job_opportunity_scanner #25/#27 CLEAN both orders (same file scorer.py, disjoint hunks); Enrollment #25/#26 CLEAN both orders (disjoint files). MERGEABLE flags alone would not reveal the stack ordering. (B) FOUND a new uncovered gap: agent_I_content PR#6 adds platform-validation.test.ts but does NOT wire it into package.json test script -- #2 CREATES the test script (caption-limit), #4 EXTENDS it (hashtag-filter), #6 never touches package.json -> after #2+#4+#6 merge, npm test runs caption-limit + hashtag-filter only and #6 platform-guard regression test (closes #5 PLATFORM_FRAMES->undefined->durationInFrames drop) silently never runs in CI. Right-sized action: posted evidence + exact one-line post-merge fix (append && ts-node ...platform-validation.test.ts) as a REVIEW COMMENT on PR#6 (issuecomment-5678599350), NOT a conflicting PR (a fresh edit to the test line would add/add-collide with #2/#4 which own it; #6 branch off default has no test script yet). (C) Wrote MERGE-RUNBOOK-2026-09-15.md: verified copy-paste merge order for all 9 PRs + owner-only items (Enrollment #24 retire stale main, ai-video-reel #5 Supabase setup). Cleaned up all /tmp clones."
runs_completed: 322
items_processed: 598
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
