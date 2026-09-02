---
agent: codex
display_name: "Codex"
emoji: "💻"
role: "Code Agent · GitHub Sync"
status: idle
last_run: "2026-09-02T06:25:00Z"
current_task: "Run 258: Fixed an UNCOVERED production bug in Community_intake_Routing. PR #2 fixed the substring-misroute (fund/invest/serve/teach matched as bare substrings) in the CLI intake.js only -- but the actual public web form (public/index.html) POSTs to the Vercel serverless handler api/intake.js, which carries its OWN copy of classify() that was still using text.includes(kw). Reproduced empirically: learner text 'fundamentals of investing ... small business skills' misrouted to PARTNER at 0.857 conf, and 'investigate AI ... fundamentals' to PARTNER at 0.80 -- real learners landing in the founder inbox instead of the learner waitlist. Fix: mirrored PR #2's whole-word matchesKeyword() regex helper into api/intake.js so both classifiers agree. Verified 5/5 routing cases (2 misroutes now->learner; genuine partner/volunteer still correct); node --check clean. Filed issue #3, opened PR #4 (closes #3) off default branch claude/quirky-galileo-UGnfz. Same-account authorship blocks self-merge -- adds to merge-blocked queue. QUEUE bottleneck UNCHANGED = 100pct founder merge-authority. Ready/independent PRs awaiting founder merge: Community_intake_Routing #2(CLI)+#4(api); Enrollment_Funnel_Agent #14(csv substring); job_opportunity_scanner #7-#16,#18; psychic-bassoon #22/#20/#19/#1; ai-video-reel #25+issue#5(Supabase infra); forming-paws #64+issue#8(legal). NEXT: founder merges the independent single-file fix PRs across repos. 204-257 in .remember/."
runs_completed: 258
items_processed: 498
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
