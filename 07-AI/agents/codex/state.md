---
agent: codex
display_name: "Codex"
emoji: "💻"
role: "Code Agent · GitHub Sync"
status: idle
last_run: "2026-08-27T19:15:00Z"
current_task: "Run 238: swept a repo prior runs never code-audited -- Enrollment_Funnel_Agent (BigHeart bridge, TS; the weekly short-form performance report agent). All 3 currently-open issues across the fleet remain founder-blocked (avrg#5 needs Supabase; psychic-bassoon#21 already has mergeable PR#22; forming-paws#8 needs IL-SOS filing), so per the run-237 pattern I audited fresh code. Found + FIXED a real silent-corruption defect in src/lib/csv-normalizer.ts detectPlatform(): the 2-letter platform short codes (ig/tt/fb/yt) were matched as RAW SUBSTRINGS in the same ||-condition as the full name, and Instagram's 'ig' branch runs first -- so a file literally named 'tiktok-insights.csv' routes to INSTAGRAM because 'insights' contains 'ig'. The Instagram column map then looks for 'Post ID' (TikTok exports use 'Video ID'), so every row is dropped as 'missing post ID' -> the whole platform silently vanishes from the BigHeart leadership report (or partially zeroes out and corrupts the within-platform z-score rankings, platforms list, and totalEngagement). Fix: check unambiguous full names first, then match short codes only as whole filename TOKENS (split on non-alphanumeric), and exported detectPlatform for testability -- one function, display/scoring-independent, low risk, matches codebase style. EMPIRICALLY proven (Node 25 / tsx, importing the REAL exported fn): pre-fix 4/7 realistic filenames misdetect; post-fix 0/15 incl. hyphen+underscore short codes (ig-june / ig_june / tt-week / fb-report / yt-shorts) AND negative cases that must NOT match (big/config/output/analytics). tsc --noEmit PASSES; end-to-end real parseCSV on a 'tiktok-insights.csv' copy of the sample now yields 5 tiktok rows (0 pre-fix). Shipped PR #14 (fix/csv-platform-detect-substring-misroute) with the full pre/post evidence table. RECOMMEND Stef: merge EFA PR #14 (low-risk correctness fix) alongside the still-pending queue -- avrg PR#25, psychic-bassoon #22->#20(CVE)->#19, JobScout #7-#16. [runs 204-237 in .remember/ + prior state.md]."
runs_completed: 238
items_processed: 469
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
