---
agent: codex
display_name: "Codex"
emoji: "💻"
role: "Code Agent · GitHub Sync"
status: idle
last_run: "2026-09-01T17:57:00Z"
current_task: "Run 255: REVIEWED psychic-bassoon flagship end-to-end + independently VERIFIED PR #22 (fix/utils-date-off-by-one, closes #21) merge-ready. Full clean-sweep code review of main first: subscribe/contact/workshop-request API routes (validation + length-caps solid), mailer.ts (XSS-hardened escapeHtml on all HTML fields, raw values only in non-HTML subject/text), supabase server client, sitemap/robots, learn+resources listings, learn/[slug] detail + generateMetadata/JSON-LD. Conclusion: codebase clean; ONLY known real bug (issue #21 date off-by-one) still on main in lib/utils.ts (new Date(dateStr) UTC-parses date-only) and already covered by PR #22 -- so verified that PR vs manufacturing a marginal issue. Node v25.6.1, TZ=America/Chicago: (1) REPRODUCED on main -- formatShortDate(2026-08-30)=>Aug 29,2026 and 2026-01-01=>Dec 31,2025 (month+YEAR rollback, not just a day); (2) fix toLocalDate() parses ^YYYY-MM-DD$ at LOCAL midnight -> corrects both; (3) datetime pass-through preserved (2026-08-30T02:00:00Z=>Aug 29 correctly); (4) ran exact configured npm test (node --test lib globstar) => 5 tests/5 pass/0 fail/exit 0, glob matches lib/utils.test.ts (5 discovered not silently 0). NOTE: first test run showed 0 tests -- STALE local branch artifact, had to git reset --hard origin/fix/utils-date-off-by-one @ a41fc91, re-ran green. Posted verification PR comment (issuecomment-5498206135); same-account authorship blocks formal gh approve. Queue UNCHANGED: psychic-bassoon PRs #22(verified)/#20/#19/#11(draft)/#1; ai-video-reel PR#25(verified run-254)+issue#5(Supabase infra); forming-paws issue#8(legal,non-code); skills-git issue#1(exercise). Bottleneck UNCHANGED: 100pct founder merge-authority, 0 code blockers. NEXT: founder merges psychic-bassoon #22->#20->#19 + ai-video-reel #25. 204-254 in .remember/."
runs_completed: 255
items_processed: 495
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
