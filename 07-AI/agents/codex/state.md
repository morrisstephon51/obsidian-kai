---
agent: codex
display_name: "Codex"
emoji: "💻"
role: "Code Agent · GitHub Sync"
status: running
last_run: "2026-09-13T20:40:00Z"
current_task: "Run 313: RESOLVED the predicted merge landmine — psychic-bassoon PR #1 went CONFLICTING/DIRTY because main gained .env.example (from merged grant-tracker PR #11) while PR #1 also creates it (add/add). Fixed it for real (not just commented as run 312 did): merged origin/main into head branch claude/amazing-mccarthy-zZl3L and resolved .env.example by UNION not pick-one — kept PR#1 Formspree keys + richer setup comments AND all of main keys (Supabase/MUTATION_SECRET+NEXT_PUBLIC_/GROQ/CRON/SITE_URL/SMTP). Verified ZERO env vars dropped via key-diff vs BOTH parents (14 keys); no conflict markers anywhere; only .env.example needed manual resolution, all code auto-merged clean. Pushed merge commit b2233ea -> PR #1 now MERGEABLE (was CONFLICTING; UNSTABLE = pending Vercel preview only, non-blocking). Did NOT self-merge; posted resolution comment (issuecomment-5655962196), left merge to owner. Note main .env.example was already a superset of PR#1 env keys, so union dropped nothing. Also observed since run 312: PR #11 merged; new PR #25 (feature/websites-page, app/websites/page.tsx +297, CLEAN/MERGEABLE, base main) awaiting owner merge. REMAINING OWNER-BLOCKED/AWAITING MERGE: psychic-bassoon #1 (now clean) + #25; Enrollment #25+#26 (both MERGEABLE, base claude/keen-noether-VED1j, disjoint) + issue #24 (infra); ai-video #27 (MERGEABLE, base main, closes #26) + issue #5 (Supabase setup); forming-paws issue #8 (legal, non-code). No open PRs/issues on job_opportunity_scanner or -Community_intake_Routing."
runs_completed: 313
items_processed: 576
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
