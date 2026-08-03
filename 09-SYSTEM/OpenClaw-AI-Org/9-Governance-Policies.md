# Governance Policies
## OpenClaw AI Organization — Decision-Making, Change Control, and Organizational Evolution

**Version:** 1.0  
**Date:** 2026-07-26  
**Owner:** Kairo (Policy Enforcement) + Aexis (Audit)  
**Review Cadence:** Quarterly (every 13 weeks)  
**Status:** ACTIVE

---

## 1. Organizational Governance Model

### 1.1 Decision Authority Matrix

**Who decides what, and how:**

| Decision Type | Authority | Approval Needed | Escalation Path | Deadline |
|---|---|---|---|---|
| **Strategic** (priorities, pivots, funding) | Stef | N/A | N/A | No deadline |
| **Operational** (task routing, budget allocation) | Kairo | Stef (weekly review) | Stef if ambiguous | Daily |
| **Technical** (architecture, specs) | Architect | Kairo | Stef if >$0.01 cost | Per-task |
| **Audit & Compliance** | Aexis | Kairo | Stef if violation | Ongoing |
| **Escalation** (risks ≥8, incidents) | Kairo | N/A (non-discretionary) | Stef immediately | <5 min |
| **External Comms** | Stef | N/A | N/A | Per-request |

### 1.2 Governance Tiers

**Three layers of governance:**

**Tier 1: Strategic Governance (Stef)**
- Sets overall direction + priorities
- Approves roadmaps + budgets
- Makes public commitments
- Veto power on all operations

**Tier 2: Operational Governance (Kairo)**
- Executes strategic decisions
- Allocates resources + routes tasks
- Manages Risk Register + escalations
- Monthly reporting to Stef

**Tier 3: Domain Governance (Supervisors)**
- Execute domain-specific work
- Log decisions to message bus
- Escalate conflicts to Kairo
- Submit to Kairo's routing authority

---

## 2. Change Control Process

### 2.1 What Requires Change Control?

**Major changes (require formal review):**

- **Architecture changes:** SAD modifications, new supervisor roles, system topology changes
- **Policy changes:** Constitution amendments, new compliance rules, governance policies
- **Budget changes:** >10% reallocation of supervisor budgets
- **Integration changes:** New external APIs, third-party tools, infrastructure
- **Process changes:** New workflows, standard runbooks, decision protocols

**Minor changes (log + notify):**

- Supervisor implementation details (code refactoring, optimization)
- Documentation updates (specs, runbooks, guides)
- Context.md updates (project status, team changes)
- Risk Register updates (new risks, mitigations)

### 2.2 Change Control Workflow

**For major changes:**

```
1. PROPOSAL (Author: Kairo or supervisor)
   └─ Document change (what, why, impact)
   └─ Identify risks + dependencies
   └─ Post to message bus + context.md
   └─ Notify Stef (email + Telegram link)

2. REVIEW (Reviewer: Stef + affected supervisors)
   └─ Stef evaluates strategic impact
   └─ Supervisors identify technical conflicts
   └─ Questions/concerns posted to bus
   └─ 3-day review window (unless urgent)

3. APPROVAL (Authority: Stef)
   └─ Approve, approve with conditions, or reject
   └─ Post decision to message bus
   └─ Update context.md with approval date

4. IMPLEMENTATION (Owner: Assigned supervisor)
   └─ Create feature branch (git)
   └─ Implement change + tests
   └─ Submit for peer review (Kairo + related agents)
   └─ Merge when approved

5. ROLLOUT (Owner: Kairo)
   └─ Deploy to production
   └─ Monitor for 24 hours (rollback ready)
   └─ Post rollout summary to message bus
   └─ Update documentation

6. CLOSURE (Owner: Kairo)
   └─ Archive change request (log it)
   └─ Measure impact (did it fix the problem?)
   └─ Update Risk Register (any new risks?)
   └─ Lessons learned (post to bus)
```

### 2.3 Change Review Checklist

**Before approving a change:**

- [ ] Problem is well-defined (why are we doing this?)
- [ ] Solution is sound (will this fix the problem?)
- [ ] Risks are identified + mitigated (what could go wrong?)
- [ ] Impact is understood (who does this affect?)
- [ ] Cost is acceptable (does it fit budget?)
- [ ] Timeline is realistic (when can we rollout?)
- [ ] Rollback plan exists (how do we undo if it breaks?)
- [ ] Audit trail is in place (will we be able to verify this later?)

---

## 3. Policy Making & Amendment

### 3.1 Policy Development Process

**To create a new policy (e.g., new compliance rule):**

1. **Identify need:** What problem are we solving? (escalated risk? compliance gap? operational friction?)
2. **Draft policy:** Write the rule + rationale + exceptions
3. **Solicit feedback:** Post to message bus, notify affected agents
4. **Refine:** Incorporate feedback (or explain rejection)
5. **Approve:** Stef signs off
6. **Communicate:** Post to context.md + notify all supervisors
7. **Enforce:** Aexis audit checks compliance (starting next day)
8. **Review:** Monthly check (is the policy working?)

### 3.2 Policy Types

| Policy Type | Examples | Update Frequency |
|---|---|---|
| **Security** | Data classification, secrets management, API approval | Quarterly (or as needed) |
| **Compliance** | Audit logging, incident response, GDPR | Quarterly |
| **Operational** | Task routing, escalation triggers, budget allocation | As needed |
| **Governance** | Decision authority, change control, policy making | Quarterly |

### 3.3 Amendment Process

**To amend an existing policy (e.g., Constitution):**

1. **Propose amendment:** Who wants to change what, and why?
2. **Post to message bus:** Link to current policy + proposed changes
3. **7-day review window:** All supervisors + Stef can comment
4. **Approve:** Stef signs off (or rejects + explains)
5. **Effective date:** Policy goes live (usually immediately after approval)
6. **Communicate:** Email to all supervisors + message bus post
7. **Log:** Git commit + archive old version

---

## 4. Supervisor Roles & Accountability

### 4.1 Supervisor Expectations

**Every supervisor is accountable for:**

1. **Quality:** Work meets specification (no shortcuts, no workarounds)
2. **Transparency:** All decisions logged to message bus + audit trail
3. **Escalation:** Ambiguous or high-risk tasks escalated to Kairo
4. **Deadlines:** Tasks completed within time budget (or escalate delays)
5. **Budget:** Token usage tracked + reported weekly
6. **Compliance:** Data handling + security policies followed
7. **Learning:** Post-incident reviews + process improvements

### 4.2 Supervisor Performance Review (Quarterly)

**Starting 2026-10-26, Stef + Kairo review each supervisor:**

| Metric | Target | Review Basis |
|---|---|---|
| **Quality** | >95% of deliverables meet spec (no rework) | Task review + error logs |
| **Reliability** | >99% uptime (no unplanned downtime >1 hour) | Heartbeat logs |
| **Latency** | <5 min avg per task | Message bus latency metrics |
| **Cost Efficiency** | Actual cost ≤ budget allocation | Weekly cost tracking |
| **Compliance** | 100% of actions audit-logged | Audit trail scan |
| **Escalation Discipline** | Ambiguous tasks escalated | Kairo review + message bus |

**Performance outcomes:**
- **Exceeds:** Increase token budget 20% next quarter
- **Meets:** Maintain current budget
- **Below target:** Root cause analysis + retraining (may reduce budget if needed)

---

## 5. Conflict Resolution

### 5.1 Conflict Types & Resolution

| Conflict | Example | Resolution Authority |
|---|---|---|
| **Supervisory conflict** | Two supervisors claim task ownership | Kairo (routing authority) |
| **Policy interpretation** | Supervisor disagrees with governance policy | Stef (strategic authority) |
| **Resource contention** | Two supervisors need same token budget | Kairo (budget allocation) |
| **Escalation dispute** | Supervisor thinks escalation unnecessary | Kairo (non-discretionary escalation rule) |

### 5.2 Escalation & Dispute Protocol

**If a supervisor disputes Kairo's decision:**

1. **Post to message bus:** Why does the supervisor disagree?
2. **Kairo responds:** Rationale for the decision
3. **If still unresolved:** Escalate to Stef (email + phone call)
4. **Stef arbitrates:** Final authority
5. **Decision logged:** Message bus + context.md

**Principle:** Conflicts are resolved quickly (within 24 hours), decisions are final, but rationale is documented for learning.

---

## 6. Organizational Evolution

### 6.1 Scaling Path (Phases 2-5)

**As OpenClaw grows:**

| Phase | Supervisors | Governance Model | Board |
|---|---|---|---|
| **Phase 1 (Now)** | 6-8 | Single decision-maker (Stef) | N/A |
| **Phase 2** | 10-15 | Kairo + domain supervisors | Stef (advisory) |
| **Phase 3** | 15-20 | Kairo + specialized committees | Stef + 1 external advisor |
| **Phase 4** | 20-30 | Kairo + governance board | Stef + 2-3 board members |
| **Phase 5+** | 30+ | Distributed governance | Formal board + committees |

### 6.2 Onboarding New Supervisors

**Process for adding a new supervisor (Phase 2+):**

1. **Identify capability gap:** What can't we do now that we need to?
2. **Design supervisor:** Role, domain, decision authority, token budget
3. **Implement:** Code + AGENTS.md integration
4. **Train:** Orient on Constitution, governance rules, audit requirements
5. **Deploy:** Add to router + message bus + registry
6. **Monitor:** 2-week trial period (Kairo + Stef watch closely)
7. **Approve:** Formal sign-off if supervisor meets quality bar

---

## 7. Communications & Transparency

### 7.1 Decision Transparency

**Every significant decision must be:**

1. **Logged:** Message bus + audit trail (who, what, when, why)
2. **Rationale explained:** What was the thinking?
3. **Alternatives considered:** What else could we have done?
4. **Stakeholders notified:** Who needs to know? (typically context.md update)
5. **Appealable:** If someone disagrees, they can escalate (process above)

### 7.2 Communication Channels

| Channel | Use | Frequency | Audience |
|---|---|---|---|
| **Message Bus** | Decisions, escalations, incidents | Real-time | All agents + Stef |
| **Context.md** | Strategic decisions, priorities, status | Weekly update | All agents + external (if public) |
| **Weekly Report** | Operational summary + metrics | Thursday 10 AM | Stef + Kairo |
| **Monthly Report** | Audit + compliance + risk review | 1st Friday 2 PM | Stef + Kairo + Aexis |
| **Quarterly Review** | Supervisor performance + governance audit | Q starts + 4 weeks | Stef + Kairo + affected supervisors |

---

## 8. Policy Enforcement & Violations

### 8.1 Violation Types & Response

| Violation Type | Examples | Response |
|---|---|---|
| **Data handling** | SENSITIVE data sent to external API | Immediate halt + incident response |
| **Authority violation** | Agent acts outside assigned domain | Revoke permissions + retraining |
| **Escalation bypass** | High-risk decision made without approval | Halt work + reverse decision |
| **Audit trail gap** | Action not logged to message bus | Retroactive logging + investigation |
| **Policy violation** | Agent ignores documented governance rule | Correction + warning (3 strikes = suspension) |

### 8.2 Response Protocol

**Upon detecting a violation:**

1. **Stop the problem** (isolate, don't escalate further damage)
2. **Investigate** (what happened? who was involved? why?)
3. **Document** (log to message bus + incident report)
4. **Correct** (fix the immediate issue)
5. **Escalate** (notify Stef if severity ≥ HIGH)
6. **Learn** (update Risk Register + governance rules to prevent recurrence)

---

## 9. Governance Roadmap

| Phase | Deliverable | Target Date |
|---|---|---|
| **Phase 1** | Constitution + decision authority matrix | 2026-07-27 (Done) |
| **Phase 2** | Change control process + policy making workflow | 2026-09-08 |
| **Phase 3** | Supervisor performance reviews + evolution roadmap | 2026-09-28 |
| **Phase 4** | Governance board + formal committee structure | 2026-10-12 |
| **Phase 5+** | Multi-team governance + external board | 2027-01-12+ |

---

## Appendix: Governance Checklist

**Phase 1 (2026-07-27):**
- [ ] Constitution ratified
- [ ] Decision authority matrix documented
- [ ] All supervisors understand their roles
- [ ] Context.md reflects authority + policy
- [ ] Message bus logging in place

**Phase 2 (2026-09-08):**
- [ ] Change control workflow operational
- [ ] Change requests documented + reviewed
- [ ] Policy amendment process tested
- [ ] Escalation protocol exercised (at least once)

**Phase 3 (2026-09-28):**
- [ ] Quarterly supervisor review framework ready
- [ ] Performance metrics tracked + analyzed
- [ ] Governance audit completed
- [ ] Scaling roadmap updated

**Phase 4 (2026-10-12):**
- [ ] Governance board established (if adding team members)
- [ ] Formal committee charters drafted
- [ ] External board member onboarded (if applicable)
- [ ] Phase 5 governance plan finalized

