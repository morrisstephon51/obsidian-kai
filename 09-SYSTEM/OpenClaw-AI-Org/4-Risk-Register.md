# Risk Register
## OpenClaw AI Organization — Known Failure Modes & Mitigation

**Version:** 1.0  
**Date:** 2026-07-26  
**Owner:** Kairo (Risk Orchestration) + Aexis Supervisor (Execution Audit)  
**Review Cadence:** Weekly (Tuesdays 10 AM CT)  
**Status:** ACTIVE

---

## Overview

This register catalogs all identified failure modes in the OpenClaw AI system (topology, delegation, supervisors, infrastructure), their impact, likelihood, and active mitigations. Risks are scored 1-5 (impact × likelihood); risks scoring ≥8 trigger escalation to Stef.

---

## Category 1: Authority & Delegation Risks

### Risk 1.1: Kairo Misinterprets Stef's Intent
**Likelihood:** Medium (3/5)  
**Impact:** High (4/5) — Wasted work, reputational damage if external  
**Score:** 12 (CRITICAL)

**Description:**  
Kairo misreads context.md or standing authorization and executes work Stef didn't actually want, leading to rework or (worse) external damage if Kairo sends communications.

**Existing Mitigations:**
- Rule 0 (prompt contracts) requires clarification for non-trivial tasks
- Rule 1 (context.md gospel) makes intent visible and updatable
- Daily Aexis audit flags decisions outside normal patterns
- External comms require Stef invocation (not autonomous)

**Additional Mitigations (Phase 1-2):**
- Authority Matrix documents who can do what (2026-08-17)
- Kairo escalation protocol: ambiguous tasks → posts to bus, waits for clarification
- Weekly context.md review (Stef + Kairo, Thursdays)

**Owner:** Stef (context clarity), Kairo (clarification discipline)  
**Escalation:** If Kairo feels ambiguous on non-trivial task, post to bus + wait 1 hour

---

### Risk 1.2: Stef Changes Priority Without Updating context.md
**Likelihood:** Medium (3/5)  
**Impact:** High (4/5) — Kairo executes stale instructions, work piles up in wrong direction  
**Score:** 12 (CRITICAL)

**Description:**  
Stef mentions a new priority verbally but doesn't update context.md. Kairo continues executing old priorities. System stays misaligned for hours/days.

**Existing Mitigations:**
- Weekly context.md review (Stef + Kairo, Thursdays)
- Aexis daily audit flags work diverging from context.md

**Additional Mitigations (Phase 1-2):**
- Kairo posts priority changes to message bus (generates notification to Stef)
- Context.md version history (git) shows when last updated
- Stef reminder: "update context.md when priorities shift" (Telegram on Monday mornings)

**Owner:** Stef (discipline), Kairo (visibility)  
**Escalation:** If Aexis detects 3+ consecutive off-target tasks, escalate to Stef immediately

---

## Category 2: Supervisor & Agent Risks

### Risk 2.1: Supervisor Silently Fails
**Likelihood:** Low (2/5)  
**Impact:** High (4/5) — Task hangs indefinitely, Stef unaware  
**Score:** 8 (CRITICAL)

**Description:**  
A supervisor (Architect, Orchestrator, Aeos, etc.) crashes, times out, or enters infinite loop without generating error. Kairo sees no response and assumes work is in progress; Stef thinks task is running but it's actually dead.

**Existing Mitigations:**
- Supervisor registry tracks "last heartbeat" timestamp
- Kairo timeout (5 min for sync agents, 30 min for async workflows)
- Message bus logs all supervisor invocations

**Additional Mitigations (Phase 2):**
- Monitoring stack alerts on supervisor heartbeat gap >10 min
- Runbook: Supervisor Escalation (restart, failover, notify Stef)
- All supervisors must emit heartbeat every 5 min (infrastructure requirement)

**Owner:** Kairo (health checks), Aexis (monitoring)  
**Escalation:** Timeout → automatic supervisor restart; 2 restarts in 1 hour → escalate to Stef

---

### Risk 2.2: Subagent Token Budget Exhaustion
**Likelihood:** Medium (3/5)  
**Impact:** Medium (3/5) — Subagent fails mid-task, cost overrun  
**Score:** 9 (CRITICAL)

**Description:**  
A single subagent or supervisor consumes all available token budget in one task, leaving no capacity for other work. Cost spirals; system can't execute other tasks that day.

**Existing Mitigations:**
- Haiku-first routing (99% of tasks use Haiku, not Opus/Sonnet)
- Prompt caching on high-reuse prompts (context.md, AGENTS.md)
- Weekly budget review (Kairo checks token spend vs. cap)

**Additional Mitigations (Phase 2):**
- Token budget allocated per supervisor (e.g., Architect gets $0.02/week, Orchestrator gets $0.01/week)
- Hard cap: if a supervisor hits 80% of weekly budget, Kairo escalates + requests manual approval for further work
- Monitoring alerts when daily spend >$0.01 (2x normal)

**Owner:** Kairo (budget enforcement), Aeos (cost forecasting)  
**Escalation:** 80% budget → escalate to Stef with cost forecast; Stef approves override or postpones work

---

### Risk 2.3: Subagent Data Leakage
**Likelihood:** Very Low (1/5)  
**Impact:** Catastrophic (5/5) — Private data exposed to external API  
**Score:** 5 (MEDIUM, but catastrophic if occurs)

**Description:**  
A subagent or Claude API call accidentally includes sensitive data (Stef's personal info, financial data, passwords) in a prompt sent to an external API provider.

**Existing Mitigations:**
- Tier 1C integrations (Claude, Perplexity) are vetted by Stef
- Data classification (sensitive, internal, public) in development
- Subagents instructed to drop secrets before logging/sending

**Additional Mitigations (Phase 3):**
- Compliance Framework includes data scrubbing rules
- Automated scan: all prompts sent to external APIs screened for sensitive keywords
- Hard rule: NEVER include .env files, API keys, or passwords in prompts
- Weekly audit (Aexis) verifies no sensitive data in logs

**Owner:** Kairo (data classification enforcement), Aexis (audit)  
**Escalation:** Any hint of sensitive data in external call → immediate incident response + review

---

## Category 3: Infrastructure & Message Bus Risks

### Risk 3.1: Message Bus Database Corruption
**Likelihood:** Very Low (1/5)  
**Impact:** High (4/5) — Audit trail lost, compliance implications  
**Score:** 4 (LOW)

**Description:**  
SQLite message bus database becomes corrupted (e.g., power loss, concurrent write). Audit logs are lost; compliance auditors can't verify what happened.

**Existing Mitigations:**
- SQLite Write-Ahead Logging (WAL) for durability
- Weekly backup to Desktop/Context/backups/

**Additional Mitigations (Phase 2-3):**
- Daily backup script (automated, 2026-09-01)
- Monitoring alerts on database integrity checks (PRAGMA integrity_check, 2026-09-08)
- Recovery runbook: restore from backup + replay last 24h logs manually

**Owner:** Kairo (backup automation), Aexis (monitoring)  
**Escalation:** Corruption detected → stop all operations, restore backup, notify Stef

---

### Risk 3.2: Message Bus Write Latency >1 Sec
**Likelihood:** Low (2/5)  
**Impact:** Medium (3/5) — Stale decisions, cascading delays  
**Score:** 6 (MEDIUM)

**Description:**  
Message bus writes slow down (disk contention, lock conflicts). Kairo and supervisors see stale data; decisions cascade on outdated state.

**Existing Mitigations:**
- SQLite WAL mode (concurrent readers)
- Message bus runs on SSD (low latency)

**Additional Mitigations (Phase 2):**
- Monitoring alerts: write latency >1 sec (2026-09-08)
- Runbook: cleanup old logs (archive logs >30 days old, 2026-09-15)
- Cost: ~$5/month for S3 backup to reduce local I/O contention

**Owner:** Kairo (monitoring), Infrastructure (disk optimization)  
**Escalation:** Chronic latency >1 sec → upgrade hardware or migrate to PostgreSQL (Phase 5)

---

## Category 4: Process & Operational Risks

### Risk 4.1: Context.md Becomes Out-of-Sync with Reality
**Likelihood:** Medium (3/5)  
**Impact:** Medium (3/5) — Decisions made on stale assumptions  
**Score:** 9 (CRITICAL)

**Description:**  
Context.md describes a state that no longer matches actual project state (e.g., says "Kresge LOI pending" but it's been approved; says "bigHeart partnership active" but it's winding down). Kairo makes decisions based on false state.

**Existing Mitigations:**
- Git history of context.md changes (Stef updates when priorities shift)
- Weekly context.md review (Stef + Kairo, Thursdays)

**Additional Mitigations (Phase 1-2):**
- Aexis audit: flags inconsistencies between context.md claims and observed work
- Rule 4 (AGENTS.md): "Update context.md after every loop if anything changed"
- Monthly context.md "audit sweep" (Stef + Kairo, 1st Thursday of month)

**Owner:** Stef (accuracy), Kairo (consistency checking)  
**Escalation:** If Aexis flags 3+ inconsistencies in 1 week → scheduled 30 min context.md review

---

### Risk 4.2: Workflow Timeouts on Complex Tasks
**Likelihood:** Medium (3/5)  
**Impact:** Medium (3/5) — Task doesn't complete, manual retry required  
**Score:** 9 (CRITICAL)

**Description:**  
A complex multi-agent workflow (e.g., Phase 1-4 artifacts) times out after 2-3 agents complete work, leaving the rest unstarted. Restart is partial, causing duplicates or missed steps.

**Existing Mitigations:**
- Workflow checkpoint: each phase saved after completion
- Manual resume capability (specify which agent to restart from)

**Additional Mitigations (Phase 2):**
- Workflow timeout increased to 60 min (from 30 min) for complex jobs
- Checkpoint saved after every agent completes (fine-grained resume)
- Alert Kairo at 80% of timeout (24 min in, warn Stef if more agents pending)

**Owner:** Kairo (workflow monitoring), Orchestrator (job decomposition)  
**Escalation:** Timeout at >50% completion → save state + notify Stef + resume manually

---

## Critical Risks Summary (Score ≥8)

| Risk ID | Title | Score | Mitigation Phase | Escalation Condition |
|---------|-------|-------|------------------|----------------------|
| 1.1 | Kairo Misinterprets Intent | 12 | Phase 1 | Ambiguous task → clarify before execute |
| 1.2 | Stef Changes Priority (No Update) | 12 | Phase 1 | 3+ off-target tasks → escalate immediately |
| 2.1 | Supervisor Silent Failure | 8 | Phase 2 | 2 restarts in 1 hour → escalate |
| 2.2 | Token Budget Exhaustion | 9 | Phase 2 | 80% budget used → escalate + manual approval |
| 4.1 | Context.md Out-of-Sync | 9 | Phase 1-2 | 3+ inconsistencies/week → scheduled audit |
| 4.2 | Workflow Timeout | 9 | Phase 2 | >50% completion → save + resume manually |

---

## Monthly Risk Review

**Cadence:** 1st Friday of month, 2 PM CT  
**Attendees:** Stef, Kairo, Aexis  
**Agenda:**
1. Review incidents from prior month (if any)
2. Audit risk scores (escalate if Likelihood or Impact changed)
3. Validate mitigations are in place + working
4. Add new risks discovered
5. Plan next month's risk mitigation work

**Output:** Updated register (this file) + summary email to Stef

