---
agent: codex
display_name: "Codex"
emoji: "💻"
role: "Code Agent · GitHub Sync"
status: running
last_run: "2026-09-15T01:59:51Z"
current_task: "Run 320 (task: review GitHub repos, fix open issues). Surveyed all 5 active repos: every open issue already has a MERGEABLE/CLEAN open PR OR is owner/setup-blocked -> nothing stranded. Instead of piling a 10th PR on the 9 already-open-and-unmerged, did a MERGE-READINESS CERTIFICATION -- the real bottleneck is owner merge action, not more bugs. Key trap: GH reports each PR MERGEABLE vs its CURRENT base, which HIDES the two-PRs-off-same-default-touch-same-file conflict until the 1st merges. PROVED the two non-obvious coexistence cases via real test-merges in throwaway /tmp clones (both orders + combined-tree tests): (1) job_opportunity_scanner #27 recency (edits is_recent ~L40) + #25 salary (edits _location_score ~L89) -- same file scorer.py but DISJOINT functions ~40 lines apart; merge clean in ANY order, combined tests 10/10 GREEN, no rebase needed. (2) agent_I_content 3-PR stack #2 captions -> #4 hashtags(stacked on #2) -> #6 platform: all merge with ZERO conflicts; test script correctly UNIONS caption-limit && hashtag-filter (add/add dodged because #4 stacked on #2, not siblinged). Enrollment_Funnel #26(enrollment-csv.ts) + #25(reporter.ts/claude-client.ts) share NO files -> independent. Community_intake #15 + ai-video-reel #27 are lone PRs, no coexistence risk. FOUND one concrete post-merge follow-up (documented, NOT filed to avoid pile-up + NOT patched now to avoid re-introducing the package.json add/add run-319 deliberately avoided): after #2/#4/#6 merge, #6's platform-validation.test.ts lands as a FILE but is NOT wired into the npm test script -> won't run in CI; owner should append '&& ts-node agents/content-pipeline/platform-validation.test.ts' to package.json test line post-merge. Owner-only items still open: Enrollment #24 (retire stale main = git action), ai-video-reel #5 (needs external Supabase project). Read-only run: no PRs opened, no self-merges; cleaned up /tmp audit clones."
runs_completed: 320
items_processed: 591
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
