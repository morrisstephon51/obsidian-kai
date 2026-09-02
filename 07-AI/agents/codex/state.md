---
agent: codex
display_name: "Codex"
emoji: "💻"
role: "Code Agent · GitHub Sync"
status: idle
last_run: "2026-09-01T22:40:00Z"
current_task: "Run 257: FIXED a genuine untracked bug (not just a review). Widened the repo sweep beyond the usual queue and found job_opportunity_scanner had 10 un-tracked open PRs (#7-#16, all scorer/report fixes) plus other repos with untriaged PRs the state never captured. Rather than a 257th re-review of the merge-blocked psychic-bassoon/forming-paws/ai-video queue (bottleneck is 100pct founder merge-authority, unchanged), hunted for an UNCOVERED bug. Verified psychic-bassoon main is already clean (earlier stale-branch reads were behind main: subscribe-route EMAIL_RE+slice(254) and sitemap SITE_URL import already present). Found in job_opportunity_scanner/scorer.py _salary_score: only HOURLY pay was normalized to annual (*2080); WEEKLY and MONTHLY salaries were compared to SALARY_FLOOR as-is, so \"$5,000/month\" ($60k/yr) scored 0.091 and \"$1,500/week\" ($78k/yr) scored 0.027 -- qualified jobs sank in ranking. NOT covered by any of the 10 open PRs (k-notation #9, salary-floor-literal #14, recency #11/#13, title/location tokens #7/#8). Fix: mirror the hourly branch (week*52, month*12); annual/hourly/unlisted paths unchanged. Verified empirically (monthly & weekly now 1.0; annual/hourly/DOE unchanged; py_compile clean). Filed issue #17, opened PR #18 (closes #17), branch fix/salary-score-monthly-weekly-periods off main -- independent of #7-#16. Same-account authorship blocks formal gh approve/self-merge. Queue UNCHANGED bottleneck: psychic-bassoon PRs #22/#20/#19/#11(draft)/#1 + issue#21(->#22); ai-video-reel PR#25+issue#5(Supabase infra); forming-paws PR#64+issue#8(legal); job_opportunity_scanner PRs #7-#16 + new #18; skills-git issue#1(exercise). NEXT: founder merges the ready scorer/report PRs #7-#18 in job_opportunity_scanner (many are independent single-file fixes) and the psychic-bassoon/ai-video/forming-paws queue. 204-256 in .remember/."
runs_completed: 257
items_processed: 497
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
