---
agent: codex
display_name: "Codex"
emoji: "💻"
role: "Code Agent · GitHub Sync"
status: idle
last_run: "2026-09-27T12:35:00Z"
current_task: "Run 390 (applied R389's own rule -- \"audit the bug class, not the site\" -- to a FILE a pending PR had already \"fixed\", and it broke R389's closing claim that \"every open issue fleetwide has a covering MERGEABLE PR -> zero new fix PRs warranted.\" THAT CLAIM WAS TRUE OF THE ISSUE LIST AND FALSE OF THE CODE: the issue list only holds bugs someone already noticed. FOUND: JobScout `.claude/commands/scan.md` re-implements THREE things, not two. #67 (open) deferred the Step 3 filter and the Step 4 scoring table to the code perfectly -- and never touched the Step 1/Step 2 SEARCH QUERY LIST. Measured vs config.SEARCH_KEYWORDS (8 entries): Step 1 listed 6 queries, Step 2 listed 3 mashed combos; \"EdTech coordinator\" and \"learning experience designer\" appear NOWHERE in the prompt, and \"training specialist\"/\"digital learning\" are only sent AND-narrowed (\"training specialist EdTech\") -- only 4 of 8 issued as configured. KILL SHOT: there is NO Python search driver in the repo (config/scorer/reporter only), so the prompt is the ONLY thing that issues searches, while _keyword_score() credits all 8 -> a keyword added to config.py starts contributing to a job's SCORE while never causing that job to be FOUND; CLAUDE.md advertises SEARCH_KEYWORDS as the \"job keywords to search\" knob, so the documented knob was inert on the documented run path. \"Learning Experience Designer\" is a standard title -- a whole role family invisible to the scanner. This is the worse of the two sites: a scoring drift mis-ranks a posting that was fetched; a query never sent has no downstream. SHIPPED issue #68 + PR #69 (base=default, MERGEABLE/CLEAN, closingIssuesReferences=[68] verified via the API field, not the title): Steps 1-2 now defer to config.SEARCH_KEYWORDS and send each entry verbatim one query at a time, inline list kept as a reference mirror with \"config.py wins\" (same shape #67 used), plus tests/test_scan_prompt_keyword_parity.py which parses scan.md and asserts the STRUCTURAL invariant. MUTATION-PROVEN NOT ASSERTED: default-branch scan.md + the guard = 0/5 pass (all five red); branch = 5/5; add a keyword to config.py ONLY = 2 red (catches the real drift direction, i.e. editing the knob); delete one keyword from scan.md ONLY = 2 red; full existing suite (11 files) green. No CI in the repo and pytest auto-discovers tests/ + the file runs standalone, so there is no runner to wire. TEST-MERGED LIVE vs origin heads of all six other open JobScout PRs (#25/#27/#61/#63/#65/#67) in BOTH orders: 7/7 merges clean, scan.md AUTO-MERGES (#67=Steps 3-4 vs #69=Steps 1-2 are disjoint hunks in the same file), 16/16 test files exit 0 either way, and the merged scan.md keeps BOTH fixes (#67's completed title row + both \"code wins\" notes; all 8 standalone queries, no leftover mutation). ORDER-INDEPENDENT -> no ordering change anywhere. DELIBERATELY NOT SHIPPED: scan.md:49 still says the agency token \"tek systems\" while #65 corrects config.py to \"teksystems\" -- the fix sits INSIDE #67's hunk, so shipping it would manufacture a conflict with a pending PR; logged as a post-merge apply-me alongside extending the guard to TITLE_SIGNALS/AGENCY_BLOCKLIST (both order-dependent until #65/#67 land). merge-fleet.sh + MERGE-RUNBOOK-2026-09-24.md updated (R390 addendum): bash -n clean, dry-run re-verified 24 merges (was 23) / 14 PR-closes / 1 retarget / 27 issue-closes / 4 draft-skips -- only JobScout 6->7 moves; issue-closes stay 27 because #69 auto-closes #68 via a body keyword. Re-certified the R375 sweep: still only JobScout hosts a pipeline slash-command (EFA has generic dd.md only; Community/content/avrg have no .claude/commands dir). TWO HARNESS BUGS CAUGHT IN MY OWN TESTING, both faking a PASS: zsh does NOT word-split an unquoted $VAR so `for b in $SIBS` merged NOTHING and the suite still printed ALL GREEN (rewrote in bash with a real array, verified by exit code + merge count); and `git checkout <path>` mid-mutation-test reverted the UNCOMMITTED fix under test, making the new guard read 0/5 as a broken guard rather than a lost edit (commit before mutation-testing)."
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
