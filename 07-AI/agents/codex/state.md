---
agent: codex
display_name: "Codex"
emoji: "💻"
role: "Code Agent · GitHub Sync"
status: running
last_run: "2026-09-05T00:10:00Z"
current_task: "Run 275: Task = review GitHub repos + fix open issues. Independently VERIFIED Enrollment_Funnel_Agent PR #14 (csv platform detect substring misroute, ig/tt/fb/yt). First checked Community_intake #3 (no PR) — found ALREADY covered by PR #2 head 79f9fcf per run 269, so not re-fixed. Pivoted to unverified Enrollment #14. Cloned fix/csv-platform-detect-substring-misroute, npm ci CLEAN. NON-TAUTOLOGY runtime differential: faithful OLD detectPlatform copy vs REAL exported detectPlatform (tsx import from source) over 14 realistic filenames -> OLD 7/14 fail, NEW 0/14. Surfaced NEW misdetects beyond the PR table: 2-char code as raw substring means ig in big/config route innocent files to instagram, yt in analytics routes weekly-analytics.csv to youtube — pre-fix even non-platform files were hard-routed, bypassing the header-signature fallback; post-fix they correctly fall through. Confirmed the silent-drop mechanism at SOURCE (csv-normalizer.ts:142-145: skip row on missing postId); instagram map postId=Post ID but TikTok export header is Video ID -> a mis-routed TikTok file loses EVERY row. E2E: real parseCSV on tiktok-sample.csv copied to tiktok-insights.csv = 5 rows parsed as tiktok (0 pre-fix). tsc --noEmit CLEAN. gh MERGEABLE/CLEAN. Diff isolated to src/lib/csv-normalizer.ts (full-name-first ordering + token-split short codes + export), no scope-creep. Posted evidence on PR #14 (issuecomment-5549249262). Did NOT merge (founder authority). PRIOR: run 274 Enrollment #20/#19(verified); run 273 Enrollment #18; run 272 job_scanner #19; run 271 Enrollment #16; run 270 psychic-bassoon #22; run 269 Community_intake #2/#6/#3. STILL OPEN needing founder merge: Community_intake #2 then #6 (#3 & #5 close on those merges); psychic-bassoon #22 (+ #20 CVE bump, #19 sec headers); Enrollment #16, #18(verified), #20(verified), #14(verified). UNVERIFIED: job_scanner #14/#15/#16/#17. 204-274 in .remember/."
runs_completed: 275
items_processed: 516
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
