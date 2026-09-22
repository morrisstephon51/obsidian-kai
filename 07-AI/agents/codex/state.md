---
agent: codex
display_name: "Codex"
emoji: "💻"
role: "Code Agent · GitHub Sync"
status: idle
last_run: "2026-09-22T15:45:00Z"
current_task: "Run 362 (review GitHub repos / fix open issues). Enrollment_Funnel_Agent CSV-parse family: the 3 open PRs (#25 sessions comma-parse, #26 enrollment-csv trim-parity, #27 detect-platform meta-substring; all base=default claude/keen-noether-VED1j) are ONE family = GA4/platform CSV parse robustness. VERIFIED each bug real by reading code: (a) #25 fixes claude-client.ts topUtmSources bare Number(r['Sessions']??..) -> NaN on GA4 '1,024' (duplicated-logic-drift vs reporter.ts which already comma-strips; #25 extracts shared parseSessionCount, both import it so it cannot drift again); (b) #26: GA4 UTM CSV parsed WITHOUT trim:true while csv-normalizer uses it -> ' Sessions' leading-space key -> hasSessionColumn=false -> silent row-count fallback; #26 adds enrollment-csv.ts w/ byte-identical opts; (c) #27 detectPlatform lower.includes('meta') fires inside 'metadata' & (ordered before youtube) hijacks even youtube files -> #27 makes meta a whole-token match. MERGE-SET CERTIFIED locally vs default@0d113c9: #25 & #27 add IDENTICAL glob test line for f in test/*.test.ts -> git auto-resolves, NO conflict in EITHER order (#25->#27->#26 AND #27->#25->#26 both clean). npm test after merging all 3 = 29/29 exit 0 (13 detect-platform + 6 enrollment-csv + 10 sessions) under the glob runner. Caveat: #26 does NOT wire package.json (relies on #25/#27 glob line); if #26 merges alone first, npm test errors 'Missing script: test' & its test is dormant until a glob-line PR lands -> nothing permanently dropped (glob discovers it). This is the CORRECT union-glob pattern (contrast agent_I_content hardcoded-filename conflict class fixed via PR #9). No 4th PR filed (family fully closed by the 3; anti-tower). ACTION: posted merge-recipe certification comment on #26 + short cross-notes on #25/#27; recommended merge #25/#27 then #26 (any order = identical green end state). Did NOT self-merge."
runs_completed: 362
items_processed: 656
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
