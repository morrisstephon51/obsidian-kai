---
agent: codex
display_name: "Codex"
emoji: "💻"
role: "Code Agent · GitHub Sync"
status: idle
last_run: "2026-09-13T16:25:00Z"
current_task: "Run 312: REVIEW-ONLY run — no new code needed (verified, not manufactured). Cloned + read all 6 active repos and checked every open PR live via gh. Every known bug is already merged or has a CLEAN pending PR; found NO un-fixed provable defect (checked the productive veins: enrollment session-parse family = fully covered by #23 merged + #25 + #26, every Number()/parseInt site handles comma+trim or is covered; community-intake classify() cli/api PARITY holds; job_scanner live branch claude/clever-cannon-IDh3G is SYNCED to main via #24 — no stranded fixes, _keyword_score bare-substring is safe since all SEARCH_KEYWORDS are multi-word; ai-video #27 covers BOTH ADMIN_SECRET outliers incl persona DELETE — not missed). REAL FINDING (new, un-flagged, merge-safety): psychic-bassoon PR#1 and PR#11 BOTH create .env.example as a NEW file (main has none, GET contents ->404); GitHub shows both MERGEABLE only vs current main, but whichever merges SECOND hits an ADD/ADD conflict. Keys are DISJOINT (Formspree vars in #1 vs Supabase/MUTATION_SECRET/Groq/cron/SMTP in #11), so a pick-one-side resolution SILENTLY DROPS the other PR's env vars -> forms die OR grant endpoints 503 on missing MUTATION_SECRET. This corrects the 2026-09-05 triage which named lib/utils.ts as the #1/#11 collision — that file is in NEITHER PR now. ACTION: posted a merge-safety comment with the ready-to-paste UNIONED .env.example on both PRs (#11 comment 5654538945, #1 comment 5654539211); wrote MERGE-TRIAGE-2026-09-13.md. Also VERIFIED enrollment #25 (package.json/claude-client.ts/reporter.ts/sessions.test) and #26 (agent.ts/enrollment-csv.ts/enrollment-csv.test) are DISJOINT — merge either order. NOT self-merged anything. --- REMAINING OWNER-BLOCKED/AWAITING MERGE: Enrollment #25+#26 (both CLEAN, base keen-noether) + #24 (infra, no code); ai-video #27 (CLEAN, base main) + #5 (needs Supabase); psychic-bassoon #1+#11 (merge order free, union .env.example on 2nd); forming-paws #8 (legal, non-code)."
runs_completed: 312
items_processed: 575
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
