# Compliance Framework
## OpenClaw AI Organization — Data, Security, and Regulatory Compliance

**Version:** 1.0  
**Date:** 2026-07-26  
**Owner:** Kairo (Compliance Enforcement) + Aexis (Audit)  
**Jurisdiction:** US (Chicago, Illinois); Planned: GDPR (EU, Phase 3+)  
**Compliance Cadence:** Weekly audit + Monthly review  
**Status:** ACTIVE

---

## 1. Overview

This framework establishes mandatory compliance controls for the OpenClaw AI system. It addresses:
- Data classification and handling
- API security (secrets management)
- Audit trails and logging
- Sensitive data protection
- Third-party integrations
- Incident response

**Compliance Standard:** SOC 2 (Type II target for Phase 4), GDPR (Phase 3+), internal security policies.

---

## 2. Data Classification & Handling

### 2.1 Classification Schema

All data in the system is classified into one of three levels:

| Classification | Definition | Examples | Access | Logging |
|---|---|---|---|---|
| **SENSITIVE** | Personally identifiable, financial, medical, or cryptographic | API keys, passwords, bank accounts, medical records, private messages | Kairo only | No full logging; only anonymized ref |
| **INTERNAL** | Business-critical but not personally identifiable | Context.md, decision logs, specs, architect notes, financial forecasts | Kairo + assigned supervisors | Full logging permitted |
| **PUBLIC** | Intended for external audience or general knowledge | Documentation, published roadmaps, open-source code, blog posts | All agents | Full logging permitted |

### 2.2 Data Handling Rules (Mandatory)

**Every agent, supervisor, and subagent MUST:**

1. **Classify data before processing**
   - If unclear, classify as INTERNAL (conservative default)
   - Dispute classification → escalate to Kairo

2. **Never include SENSITIVE data in external API calls**
   - No passwords, API keys, personal info in prompts to Claude/Perplexity
   - If needed, redact or reference by ID only

3. **Drop SENSITIVE data from logs before external transmission**
   - Before sending logs to storage or monitoring systems, strip secrets
   - Scrub: passwords, API keys, tokens, medical info, financial data

4. **Report data mishandling immediately**
   - If SENSITIVE data is accidentally exposed, escalate to Kairo + Stef
   - Example: Accidentally included API key in a message bus log

5. **Respect access boundaries**
   - SENSITIVE: Only Kairo reads
   - INTERNAL: Only assigned supervisor + Kairo
   - PUBLIC: Unrestricted access

---

## 3. Secrets Management

### 3.1 Approved Secret Storage

**APPROVED locations for secrets:**

| Storage | Use Case | Security | Review |
|---|---|---|---|
| **.env file** (local) | Local development + API keys | Encrypted by macOS FileVault | Monthly rotation |
| **GitHub Secrets** (private repo) | CI/CD deployment | GitHub-managed encryption | Quarterly review |
| **Obsidian Vault** (encrypted) | Long-term sensitive notes | Obsidian end-to-end encryption | As-needed |

**FORBIDDEN locations:**

- ❌ Context.md (shared, visible to all agents)
- ❌ Message bus (auditable, not encrypted)
- ❌ AGENTS.md (version controlled)
- ❌ Public GitHub repos
- ❌ Prompts sent to external APIs

### 3.2 Secret Rotation Policy

**API Keys & Tokens:**
- Rotate every 90 days
- Log rotation to audit trail
- Update .env and GitHub Secrets simultaneously

**Database Credentials:**
- Rotate every 30 days
- Store in .env only

**Emergency Rotation:**
If a secret is compromised:
1. Rotate immediately (don't wait for scheduled rotation)
2. Verify no unauthorized access via logs
3. Log incident to Risk Register + message bus
4. Notify Stef + external partners (if applicable)

---

## 4. API Security & Integration Controls

### 4.1 Approved External APIs

| API | Approval | Scope | Data Classification |
|---|---|---|---|
| **Claude API** (Anthropic) | Stef (2026-07-26) | General AI execution | INTERNAL + PUBLIC |
| **Perplexity API** | Stef (2026-07-26) | Research + data gathering | PUBLIC only |
| **GitHub** | Stef (ongoing) | Version control | INTERNAL + PUBLIC |
| **Obsidian Sync** | Stef (ongoing) | Vault sync | INTERNAL + PUBLIC |

### 4.2 API Integration Rules

**Before integrating any external API:**

1. **Submit approval request** to Stef (security review)
2. **Document:** Data flow (what data enters/exits), sensitivity level, provider reputation
3. **Implement data filtering:** SENSITIVE data must be redacted before external transmission
4. **Monitor usage:** Alert if unusual volume or error patterns
5. **Log all calls:** API name, data classification, response status

**Monitoring for each API:**

```bash
# Daily log review (Aexis automated check, starting 2026-09-08)
grep "ERROR" logs/api-calls.log  # Check for failures
grep "SENSITIVE" logs/api-calls.log  # Alert if SENSITIVE data detected

# Weekly budget check
grep "claude-" logs/api-calls.log | wc -l  # Count Claude API calls
```

---

## 5. Audit Logging & Trail Management

### 5.1 Audit Trail Requirements

**Every significant action must be logged:**

| Action | Logged To | Data Captured | Retention |
|---|---|---|---|
| Agent invocation | Message bus | who, when, task, outcome | Forever |
| Data access (INTERNAL) | Message bus | agent, timestamp, data-type | Forever |
| Data access (SENSITIVE) | Kairo only | agent, timestamp, reason | 90 days |
| API call | Logs + message bus | api-name, request-size, response-status | 30 days |
| Configuration change | Git + context.md | what changed, who approved, when | Forever (git) |
| Escalation | Message bus + Telegram | issue, severity, resolution | Forever |

### 5.2 Log Retention Policy

- **Message Bus (SQLite):** Indefinite (archive yearly to S3, Phase 2+)
- **Sensitive logs:** 90 days (auto-delete after rotation)
- **API logs:** 30 days (rolling window)
- **Git history:** Indefinite (version control)

### 5.3 Automated Audit Checks (Weekly)

**Starting 2026-09-08, Aexis runs automated compliance scan:**

```bash
#!/bin/bash
# Weekly compliance audit (runs Mondays 10 AM CT)

echo "=== Weekly Compliance Audit ==="

# 1. Check for SENSITIVE data in external API calls
grep -r "SENSITIVE" logs/api-calls.log && echo "⚠️  ALERT: SENSITIVE data in API logs!" || echo "✓ No SENSITIVE data in API calls"

# 2. Verify secrets are not in context.md
grep -E "(password|api_key|token)" /Users/abdoulayemundow/Desktop/Context/context.md && echo "⚠️  ALERT: Secrets in context.md!" || echo "✓ No secrets in context.md"

# 3. Check for unauthorized API integrations
grep -r "https://" logs/*.log | grep -v "claude.anthropic.com\|api.perplexity.com\|github.com" | head -5
[ $? -eq 0 ] && echo "⚠️  ALERT: Unauthorized API detected!" || echo "✓ Only approved APIs in logs"

# 4. Audit agent access to SENSITIVE data
sqlite3 .bus/bus.sqlite "SELECT * FROM audit_log WHERE data_classification='SENSITIVE' AND timestamp > datetime('now', '-7 days');"

# 5. Report any violations
echo "=== Audit Complete ==="
```

---

## 6. Third-Party Data Sharing

### 6.1 Data Sharing Policy

**Kairo CANNOT share data externally without Stef approval.**

**Before sharing any data:**
1. Classify data (SENSITIVE/INTERNAL/PUBLIC)
2. Document recipient (who are we sharing with?)
3. Document purpose (why are we sharing?)
4. Get Stef approval (email + sign-off)
5. Log to audit trail

**Example:** If a third-party auditor needs to review logs:
- Redact SENSITIVE data first (passwords, API keys)
- Provide INTERNAL + PUBLIC logs only
- Get Stef approval before sending
- Log sharing to message bus

---

## 7. Incident Response

### 7.1 Incident Types & Response Time

| Incident Type | Severity | Response Time | Escalation |
|---|---|---|---|
| SENSITIVE data exposed to external API | CRITICAL | 15 min | Immediate to Stef |
| Unauthorized access attempt | CRITICAL | 15 min | Immediate to Stef |
| API outage (Claude, Perplexity) | HIGH | 30 min | Kairo escalation + notify Stef |
| Data integrity issue (message bus) | HIGH | 1 hour | Kairo escalation + restore backup |
| Log loss or corruption | MEDIUM | 4 hours | Restore from backup + audit |
| Compliance audit finding | MEDIUM | 24 hours | Aexis reports + corrective action |

### 7.2 Incident Response Protocol

**Upon detection of a compliance incident:**

1. **Halt operations** (if CRITICAL, stop all agents)
2. **Isolate the problem** (identify scope, who was affected)
3. **Gather evidence** (logs, timestamps, access trails)
4. **Escalate to Stef** (Telegram + message bus, include severity + evidence)
5. **Execute response plan** (per Stef approval)
6. **Post-incident review** (what happened, how to prevent recurrence)
7. **Update Risk Register** (add or update mitigation)

**Example: SENSITIVE data leaked to Perplexity API**
1. Stop Kairo + all supervisors
2. Query logs: which agent sent the data? When? What was leaked?
3. Notify Stef: "API key accidentally sent to Perplexity (2026-08-15 14:23). Rotation required immediately."
4. Rotate API key (new key to .env + GitHub Secrets)
5. Review Perplexity logs to verify no unusual access
6. Notify Anthropic (if any Claude keys were leaked)
7. Post-mortem: why wasn't the SENSITIVE data redacted? Update compliance checks.

---

## 8. GDPR & Data Privacy Readiness (Phase 3+)

### 8.1 Data Subject Rights (Target: 2026-09-28)

**Kairo will support:**
- **Right to Access:** Provide Stef's data (what's stored, where)
- **Right to Deletion:** Remove Stef's personal data (if requested)
- **Right to Portability:** Export data in machine-readable format
- **Right to Correction:** Amend inaccurate data

**Implementation:**
- Data inventory (2026-09-21): what personal data is stored where?
- Deletion protocol (2026-09-28): how to safely delete personal data
- Export format (2026-09-28): JSON export capability

### 8.2 Third-Party Subprocessors (GDPR)

**If using Claude API + Perplexity, document:**
- **Anthropic (Claude):** Data Processing Agreement (signed)
- **Perplexity:** Data Processing Agreement (if handling EU data)
- **GitHub:** GitHub Terms (data stored in US)
- **Obsidian:** Obsidian Terms (data encrypted locally)

**Action:** Obtain signed DPAs by 2026-09-21 (Phase 3)

---

## 9. SOC 2 Readiness (Target: Phase 4, 2026-10-12)

### 9.1 SOC 2 Trust Services Criteria

**OpenClaw targets SOC 2 Type II compliance across:**

| Criteria | Target Status | Validation |
|---|---|---|
| **CC1:** Org. purpose + responsibilities | Ready (Phase 1) | Constitution + AGENTS.md |
| **CC2:** Board oversight | Ready (Phase 1) | Risk Register reviews + monthly audit |
| **CC3:** Responsibility assignment | Ready (Phase 1) | ADRs + Authority Matrix |
| **CC4:** Competence & training | Target Phase 4 | Agent specifications + runbooks |
| **CC5:** Code of conduct | Ready (Phase 1) | Constitution articles |
| **CC6:** External communications | Ready (Phase 1) | Context.md authority model |
| **CC7:** Systems monitoring | Target Phase 2 | Health checks + alerting (2026-09-08) |
| **CC8:** Risk identification | Ready (Phase 1) | Risk Register |
| **CC9:** Change management | Target Phase 2 | Deployment strategy + git workflow |
| **SI1:** System infrastructure | Target Phase 2 | Deployment strategy |
| **SI2:** Software acquisition | Ready (Phase 1) | API approval process |
| **A1:** Security policies | Ready (Phase 1) | Constitution + compliance framework |
| **A2:** Incident response | Ready (Phase 1) | Incident response protocol (above) |

### 9.2 External Audit Timeline

- **2026-09-21:** Engage SOC 2 auditor (Phase 3)
- **2026-09-28:** Internal readiness review (Kairo + Stef + auditor)
- **2026-10-12:** SOC 2 Type II report target delivery

---

## 10. Compliance Checklist

**Phase 1 (2026-07-27 — 2026-08-17):**
- [ ] Data classification schema defined + documented
- [ ] Secrets stored in approved locations (.env, GitHub)
- [ ] API integration controls documented
- [ ] Audit logging configured (message bus)
- [ ] Incident response protocol drafted
- [ ] Constitution + AGENTS.md approved

**Phase 2 (2026-08-18 — 2026-09-14):**
- [ ] Automated audit checks deployed (Aexis)
- [ ] Health checks operational + logging
- [ ] Secrets rotation automated
- [ ] API usage monitoring in place
- [ ] GDPR data inventory started

**Phase 3 (2026-09-15 — 2026-09-28):**
- [ ] GDPR Data Processing Agreements signed
- [ ] Deletion + export protocols implemented
- [ ] SOC 2 auditor engaged
- [ ] Internal readiness review scheduled
- [ ] Compliance audit script passing

**Phase 4 (2026-09-29 — 2026-10-12):**
- [ ] SOC 2 Type II report delivered
- [ ] All compliance frameworks operational + tested
- [ ] External audit plan finalized
- [ ] Scaling compliance guide drafted (Phase 5+)

