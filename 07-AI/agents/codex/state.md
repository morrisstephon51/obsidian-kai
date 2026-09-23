---
agent: codex
display_name: "Codex"
emoji: "💻"
role: "Code Agent · GitHub Sync"
status: idle
last_run: "2026-09-23T18:55:00Z"
current_task: "Run 369 (Community Intake / -Community_intake_Routing). Converted last run's well-analyzed-but-PR-less issue #39 into a SHIPPED PR (#40) -- per the standing rule: don't stall on owner-blocked bugs, ship the non-forking part as a PR and reserve "hold for owner" for the merge. Read the actual code both paths: CLI intake.js main does parse->classify->buildEmail->sendEmail(__GMAIL_ACTION__)->log, but the PUBLIC web handler api/intake.js only classifies+logs (status:routed) and produces NO routing action -- confirming #39 (every public-form submission silently un-routed). Shipped the provably-correct, NON-forking, SCHEMA-SAFE slice: (1) extracted buildEmail into shared lib/email.js (single source, kills classify()-style twin-drift), imported by BOTH paths; (2) web handler now computes the routing action and emits the SAME __GMAIL_ACTION__ envelope the CLI emits (recoverable from function logs, matching the handler's own no-Supabase recoverability contract) so partner->founder + learner/volunteer->submitter is recorded per submission instead of dropped; (3) test/routing.test.mjs locks routing targets, wired into npm test. Deliberately did NOT change the persisted status off 'routed' or add columns: community_intake schema is unverifiable this run (Supabase MCP perm not granted; no SQL in repo), so touching the record risks regressing the insert -- that + the actual serverless delivery mechanism (Resend/SendGrid vs downstream poller) stay the owner infra decision tracked in #39. VERIFIED before shipping: npm test = unit 8/8 (routing) + smoke learner/partner/volunteer green; mock req/res harness shows handler emits __GMAIL_ACTION__ with to=FOUNDER (partner) / to=submitter (learner) at HTTP 200; and #38 (keystone classify consolidation) test-merged BOTH orders CLEAN with the merged tree passing 94 classify + 8 routing + smoke -- so PR#40 is disjoint from #38, based off DEFAULT (independent, not stacked). Owner-MERGE remains the sole bottleneck (0 merges since R320); PR#40 adds one concrete, verified, distinct-class fix to the queue."
carryover: "CARRYOVER (owner-MERGE still the sole bottleneck across the 4 claude/* repos; 0 merges since R320; avrg main actively merges). NEW this run: Community Intake PR #40 ships the non-forking slice of #39 -- web /api/intake now computes+emits the routing action via shared lib/email.js (closes #39 on merge); based off DEFAULT, verified disjoint from #38 (both-order test-merge clean, 94+8 pass). Still owner-deferred inside #39: real serverless delivery mechanism (Resend/SendGrid vs poller) + flipping status off 'routed' (needs community_intake status-constraint confirmed -- Supabase inspection was perm-blocked this run). Unchanged keystones awaiting owner MERGE: Community Intake PR #38 (intent-based classify consolidation, supersedes #14-#36; merge #38 -> close issues #14-#36 + tower PRs #15-#37; PR#40 auto-retargets to default after) then PR #40. JobScout PR #61 (salary-cadence regex superset -> merge + close #30-#59) + PR #63 (keyword whole-word, closes #62) + PR #65 (TEKsystems blocklist spacing, closes #64) + #25/#27 (salary-range/recency) -- all MERGEABLE + mutually disjoint. agent_I_content PR #9 (glob test-runner, merge FIRST) + fix PRs #2/#4/#6/#8 + issues #3/#5/#7. Enrollment_Funnel CSV set #25/#26/#27 + issue #24 (retire stale main). avrg PR #27 (persona/upload auth, closes #26+#28) + PR #31 (schedule TZ anchor, closes #30); avrg issue #5 (Supabase setup) still blocks ALL avrg e2e verification."
runs_completed: 369
items_processed: 684
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
