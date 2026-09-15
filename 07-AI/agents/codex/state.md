---
agent: codex
display_name: "Codex"
emoji: "💻"
role: "Code Agent · GitHub Sync"
status: idle
last_run: "2026-09-15T23:20:00Z"
current_task: "Run 325 (review GitHub repos / fix open issues). Re-certified PR surface per-repo (gh pr list authoritative): 11 open PRs still stalled on OWNER MERGE, all MERGEABLE, nothing merged since run 320. Did NOT pile redundant PRs. First hunted EFA \"duplicated logic drifts\": found claude-client.ts:116 topUtmSources does bare Number(r['Sessions']) with no comma-strip (twin of reporter.ts:80) -- but memory-checked and open PR#25 ALREADY fixes it (shared parseSessions), so left it (would have been redundant). UNIT OF WORK -- shipped a NEW uncovered bug in Enrollment_Funnel_Agent (PR #27, base=default claude/keen-noether-VED1j, MERGEABLE, +76/-6, 3 files): detectPlatform() in csv-normalizer.ts routed ANY filename containing substring \"meta\" to facebook via lower.includes('meta'); \"meta\" is a substring of \"metadata\" (common export word) and the facebook check is ordered before youtube, so it silently re-routed even files naming \"youtube\". SAME substring-collision class this file already tokenized for ig/tt/fb/yt. PROVEN vs live code: youtube-video-metadata.csv, content-metadata.csv (ig hdrs), post-metadata-2026.csv (yt hdrs) all -> facebook (wrong); wrong platform -> wrong PLATFORM_MAPS col map -> all metrics 0 + rows dropped as \"missing post ID\" (silent report corruption). Fix moves 'meta' into the whole-token check (tokens.includes('fb')||'meta'); meta-week.csv / Meta_Business_Suite_*.csv still -> facebook. Added self-contained test/detect-platform.test.ts (13 cases: fix + meta-alias preservation + ig/tt/fb/yt guards + header fallback); tsc --noEmit clean. Repo has NO test runner, so wired npm test to a GLOB over test/*.test.ts (not a hardcoded file). SET-LEVEL CONFLICT flagged+neutralized: open PR#25 also adds a package.json \"test\" key hardcoded to test/sessions.test.ts -> add/add conflict on that one line (verified: #25 merges clean, then #27 conflicts). Made #27 union-safe via the glob and documented the exact resolution in the PR (keep the glob line, drop #25's single-file line); proven on the fully-merged set both run: detect-platform 13/13 AND sessions 10/10. Code hunks disjoint from #25 (reporter/claude-client) and #26 (agent/enrollment-csv). Owner-only items unchanged (Enrollment #24 retire stale main, ai-video-reel #5 Supabase)."
runs_completed: 325
items_processed: 601
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
