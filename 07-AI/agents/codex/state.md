---
agent: codex
display_name: "Codex"
emoji: "💻"
role: "Code Agent · GitHub Sync"
status: running
last_run: "2026-08-26T19:10:00Z"
current_task: "Run 235: EXECUTED the run-234 recommendation. Took psychic-bassoon ISSUE #21 (repo only open issue, filed by me last run) as the scoped fix. Root cause: lib/utils.ts formatDate/formatShortDate called new Date('YYYY-MM-DD'), which the JS spec parses as UTC midnight -> toLocaleDateString rolled the day BACK for the Central Time (Chicago) audience (formatShortDate('2026-09-15') -> 'Sep 14, 2026' under TZ=America/Chicago; should be Sep 15). FIX: added toLocalDate() helper that parses date-only 'YYYY-MM-DD' as LOCAL midnight; both formatters route through it; full datetime strings still pass through new Date() unchanged. Added tests/utils.date.test.ts using Node BUILT-IN runner (node --test, zero new deps; node 25 strips TS): 4 assertions. VERIFIED before/after: 3 assertions FAIL on origin/main buggy utils.ts (renders Sep 14 / Monday Sep 14), all 4 PASS on fix; datetime pass-through assertion passes on BOTH -> guard NOT tautological. tsc --noEmit clean on changed file (exit 0). Committed 2 files, pushed fix/utils-date-off-by-one, opened PR #22 base=main (production/Vercel branch) with Closes #21. PR #22 = MERGEABLE, files=2, state UNSTABLE only because Vercel preview build still pending (Preview Comments already PASS) -- nothing broken. Logged in PR: stale PR #1 deletes formatShortDate so if #1 revives it needs a trivial rebase; base main correct (bug lives there). LANDSCAPE now: psychic-bassoon 5 open PRs (#22 my fix, #20 Next.js CVE bump, #19 sec-headers, #11 grant-tracker, #1 big-feature); issue #21 auto-closes when #22 merges. JobScout unchanged: 0 open issues, 10 clean PRs #7-#16 blocked on founder merge authority. RECOMMEND Stef: merge #20 (Next.js CVE) -> #22 (this date fix, tests green) -> #19, then JobScout #7-#16 + clever-cannon->main. [runs 204-234 in .remember/ + prior state.md]."
runs_completed: 235
items_processed: 452
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
