---
agent: architect
role: System Design Supervisor
mode: "full"
status: "idle"
last_run: "2026-08-11T14:51:02.699Z"
current_task: null
active_spec: null
runs_completed: 14
last_error: null
---

# Architect — General-Purpose System Design Supervisor

Designs systems before Codex builds them. Produces specs, ADRs, and architectural plans for **any project**.
Token-lean: no context.md injection, max_tokens 1024, concise prompts.

Two modes:
- **Full** — Sonnet, structured spec (What/Key Decisions/Spec/Risks/Done When/Handoff)
- **Lite** — Haiku, numbered steps + done-when bullets only

Invocation:
```
node run.js "<design task>" [--mode lite] [--project "name"]
```

Core question: **"What exactly are we building and why, before a single line of code is written?"**

> v1 (Plug AI / BigHeart scoped, max_tokens 2048, context.md injection) archived to `agents/_archived/architect-agent-v1/`

## Active Spec
<!-- Architect writes the current design here -->

## Last Architecture Decision
*2026-08-11 (full)*

## What We're Building
A Phase 3 audit infrastructure compliance tracking system that provides a unified control library mapped across multiple regulatory frameworks (SOC 2, ISO 27001, HIPAA, PCI-DSS), automates evidence ingestion from integrated systems, tracks audit findings through remediation closure, and produces auditor-ready posture reports — replacing manual spreadsheet-driven audit preparation with a continuous, real-time compliance posture.

---

## Key Decisions

1. **Unified control library over per-framework silos.** Controls from all frameworks are normalized into a single registry with cross-framework mappings (e.g., SOC 2 CC6.1 ↔ ISO 27001 A.9.4.1). This eliminates duplicate evidence collection and lets a single piece of evidence satisfy controls across frameworks simultaneously. The alternative — per-framework tables — causes exponential evidence overhead as frameworks multiply.

2. **Append-only, hash-chained evidence store.** Evidence records are immutable once ingested; updates create new versions linked to the prior record via SHA-256 hash. This produces a tamper-evident chain required for auditor trust and regulatory defensibility. A mutable store would require expensive reconstruction of "what did we have at audit time."

3. **Event-driven ingestion over scheduled polling.** Integrations push evidence via webhooks or stream connectors (not nightly batch jobs). This keeps compliance posture current, enables real-time gap detection, and reduces the 30–90 day "evidence scramble" window before audits. Batch polling is acceptable only as a fallback for systems that cannot push.

---

## Spec

### Data Models / Schema

```
Framework       { id, name, version, effective_date }
Control         { id, framework_id, code, title, description, category, evidence_ttl_days }
ControlMapping  { id, source_control_id, target_control_id, confidence }  -- cross-framework links
Evidence        { id, control_ids[], source_system, collected_at, payload_hash,
                  content_url, status(valid|expired|superseded), prev_evidence_id }
Assessment      { id, framework_id, start_date, end_date, auditor, status }
Finding         { id, assessment_id, control_id, severity(crit|high|med|low),
                  description, evidence_ids[], status(open|in_remediation|closed) }
Remediation     { id, finding_id, owner, due_date, action_plan, closed_at, evidence_id }
AuditEvent      { id, actor, action, resource_type, resource_id, timestamp, payload_hash }
```

---

### API Contracts

| Method | Path | Purpose |
|--------|------|---------|
| `GET` | `/controls?framework=&status=` | List controls with current evidence status |
| `POST` | `/evidence` | Ingest evidence (internal + webhook) |
| `GET` | `/controls/{id}/evidence` | Evidence chain for a control |
| `POST` | `/findings` | Create finding from assessment |
| `PATCH` | `/findings/{id}` | Update finding status |
| `POST` | `/remediations` | Open remediation ticket |
| `GET` | `/posture?framework=&as_of=` | Point-in-time compliance posture report |
| `GET` | `/gaps` | Controls missing valid evidence |
| `POST` | `/integrations/{source}/ingest` | Signed webhook receiver per source |

All mutating endpoints emit to the `AuditEvent` ledger. `GET /posture` accepts an `as_of` timestamp to reconstruct historical state.

---

### Components

| Component | Responsibility | Interface |
|-----------|---------------|-----------|
| **Control Registry** | Single source of truth for all controls and cross-framework mappings; seeds from OSCAL-formatted framework definitions | REST + internal SDK |
| **Evidence Collector** | Receives push events (webhooks) and pulls from integrations; validates signatures, hashes payload, writes to evidence store | Webhook endpoints + polling scheduler |
| **Compliance Engine** | Evaluates which controls have valid, non-expired evidence; computes per-control and aggregate posture scores; triggers gap alerts | Internal service, called by Posture API |
| **Finding & Remediation Tracker** | Manages finding lifecycle from open → remediation → closed; links remediation evidence back to finding | REST API + event hooks |
| **Reporting Service** | Generates point-in-time posture snapshots, auditor-export packages (PDF/CSV), and continuous dashboards | REST + scheduled jobs |
| **Integration Hub** | Adapters per source (AWS CloudTrail, Datadog, Jira, GitHub, Okta); normalizes events into canonical evidence format | Plugin architecture; per-adapter config |
| **Notification Service** | Emits alerts on expiring evidence, missed remediation deadlines, new findings, posture drops below threshold | Email / Slack / webhook |
| **Audit Ledger** | Append-only `AuditEvent` log; all writes are hash-chained; exposed read-only to auditors | Write-through from all components |

---

### Integration Points

- **SIEM / Observability**: Datadog, Splunk — push log/metric evidence for operational controls  
- **Cloud Providers**: AWS CloudTrail, Azure Monitor, GCP Audit Logs — IAM, config, and access evidence  
- **Identity Provider**: Okta, Azure AD — access review and MFA evidence  
- **Ticketing**: Jira, ServiceNow — remediation lifecycle sync; bi-directional status updates  
- **SCM**: GitHub/GitLab — code review, branch protection, and SAST scan evidence  
- **OSCAL**: Import/export control catalogs and assessment results in NIST OSCAL JSON format  

---

## Risks

| # | Risk | Mitigation |
|---|------|-----------|
| 1 | **Evidence staleness invalidates posture at audit time** — TTL misconfiguration leaves expired evidence counted as valid | Enforce TTL checks at read time in Compliance Engine, not write time; alert at 80% of TTL, not expiry |
| 2 | **Framework regulatory change breaks existing control mappings** — new ISO 27001:2022 controls silently leave gaps | Version-lock `Framework` records; require explicit migration job when a new version is ingested; diff report surfaced to compliance owner |
| 3 | **Integration webhook authentication failure causes evidence gaps** — misconfigured HMAC secrets let events silently drop | Dead-letter queue for rejected webhooks with ops alert; nightly gap report compares expected evidence frequency to actual receipts |

---

## Done When

1. **Posture API returns a framework-complete compliance score** — given SOC 2 Type II, `GET /posture?framework=soc2` returns per-control evidence status and an aggregate % with zero manual data entry.
2. **End-to-end evidence chain is auditor-verifiable** — an auditor can call `GET /controls/{id}/evidence` and cryptographically verify the hash chain from current evidence back to initial ingestion, with no gaps.
3. **Finding lifecycle closes with linked evidence** — a finding opened from an assessment can be transitioned to `closed` only when a `Remediation` record with a valid `evidence_id` is attached, enforced by the API.

---

## Handoff

**Build the Control Registry first.** Define the `Framework`, `Control`, and `ControlMapping` schema, seed it with SOC 2 Type II controls from the AICPA trust services criteria (in OSCAL JSON), and expose `GET /controls?framework=soc2` returning controls with a placeholder `evidence_status: no_evidence`. Everything else — evidence collection, posture scoring, findings — is blocked on a populated, queryable control library.

<!-- KAIRO-LEDGER -->
## Cost Ledger (appended by Kairo — supervisors must not rewrite below this line)

[2026-08-10T23:32:41.534Z] design via claude-sonnet-4-6: SUCCESS cost_usd=0.175340 billing=subscription measured=true trace=20260810T233241534Z-kairo-s31
[2026-08-11T14:25:33.437Z] design via claude-sonnet-4-6: SUCCESS cost_usd=0.116302 billing=subscription measured=true trace=20260811T142533437Z-kairo-59k
[2026-08-11T14:25:33.435Z] architecture via claude-sonnet-4-6: SUCCESS cost_usd=0.142285 billing=subscription measured=true trace=20260811T142533435Z-kairo-59w
[2026-08-11T14:29:03.065Z] architecture via claude-sonnet-4-6: SUCCESS cost_usd=0.127298 billing=subscription measured=true trace=20260811T142903065Z-kairo-6qf
[2026-08-11T14:29:03.067Z] design via claude-sonnet-4-6: SUCCESS cost_usd=0.282689 billing=subscription measured=true trace=20260811T142903067Z-kairo-6qj
[2026-08-11T14:49:50.527Z] design via claude-sonnet-4-6: SUCCESS cost_usd=0.116213 billing=subscription measured=true trace=20260811T144950527Z-kairo-c35
[2026-08-11T14:49:50.516Z] architecture via claude-sonnet-4-6: TIMEOUT cost_usd=0.000000 billing=subscription measured=false trace=20260811T144950516Z-kairo-c2t