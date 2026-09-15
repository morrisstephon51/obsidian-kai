---
agent: codex
display_name: "Codex"
emoji: "💻"
role: "Code Agent · GitHub Sync"
status: idle
last_run: "2026-09-15T02:06:20Z"
current_task: "Run 321 (task: review GitHub repos, fix open issues). Re-surveyed all 5 active repos: every FILED open issue still has an open PR OR is owner/setup-blocked, and NOTHING has merged since run 320 (newest merges all predate 2026-09-14) -> the 9 PRs are still stalled on OWNER MERGE, not on missing fixes. Piling a redundant 10th PR adds review burden, not value. Did non-redundant work: (A) CERTIFIED job_opportunity_scanner default branch GREEN -- cloned claude/clever-cannon-IDh3G to /tmp, built venv, ran full pytest: 59/59 pass. (B) SAME-CLASS SIBLING AUDIT of the recency filter (live #26/#27 hotspot). Empirically probed is_recent() on 16 time-expressions: 'a month ago'(30d) and 'a year ago'(365d) both return INCLUDE(fresh) and slip past MAX_DAYS_OLD=7 -- exact leak class as #26, spelled with an article not a digit ('a week ago'=7d & 'a day ago'=1d correctly stay fresh). CRUCIAL: NOT a clean independent bug -- PR #27's own test file EXPLICITLY asserts test_digitless_year_still_included (a year ago -> include) as a DELIBERATE benefit-of-the-doubt choice; a competing fix would flip that assertion (semantic conflict) + override another agent's just-made decision. Right-sized move: focused REVIEW COMMENT on PR #27 (issuecomment-5675620363) with evidence + minimal disjoint patch (handle a/an as 1 in the week/month/year branches), deferring the call to merge time. Did NOT open a PR / self-merge / file a duplicate issue (avoid pile-up). Owner-only items unchanged: Enrollment #24 (retire stale main = git action), ai-video-reel #5 (needs external Supabase project). Cleaned up /tmp clone + venv + temp files."
runs_completed: 321
items_processed: 597
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
