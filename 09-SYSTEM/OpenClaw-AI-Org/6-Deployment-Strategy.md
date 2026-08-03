# Deployment Strategy
## OpenClaw AI Organization — Infrastructure, Release, & Operational Procedures

**Version:** 1.0  
**Date:** 2026-07-26  
**Owner:** Kairo (Orchestrator) + Architect (Design)  
**Target Environment:** macOS (Stef's machine) + Optional: Cloud (Phase 5)  
**Status:** ACTIVE

---

## 1. Deployment Architecture

### 1.1 Current State (2026-07-26)

**Primary Deployment:**
- **Host:** macOS (Stef's machine, `/Users/abdoulayemundow/clawd/`)
- **Runtime:** OpenClaw CLI + Node.js 25.6.1
- **Storage:** Local filesystem + Git
- **Message Bus:** SQLite (`.bus/busctl.js`) with WAL mode
- **Orchestration:** Kairo process (long-running) + Workflow agent system

**Data Locations:**
- `/clawd/` — Main workspace (agents, routes, registry)
- `/Desktop/Context/` — Shared context (context.md, AGENTS.md, TOOLS.md)
- `/Desktop/kai/` — Obsidian vault (PARA folders, PKB)
- `/Desktop/Context/backups/` — Backup storage (daily snapshots)

**External Integrations:**
- Claude API (via Anthropic SDK)
- Perplexity API (research, external data)
- GitHub (version control, public repos)
- Obsidian (vault sync via Git + iCloud)

### 1.2 Deployment Tiers (Future)

| Tier | Deployment | Use Case | Target |
|------|-----------|----------|--------|
| **Tier 1 (Now)** | Local (macOS) | Development + production execution | 2026-07-27 |
| **Tier 2 (Phase 5)** | Cloud backup (AWS S3) | Backup + disaster recovery | 2026-10-12+ |
| **Tier 3 (Post-MVP)** | Distributed (Multi-region) | Redundancy, multi-team access | 2027-01-12+ |

---

## 2. Deployment Procedure (Tier 1: Local)

### 2.1 Initial Setup (One-Time)

**Prerequisites:**
- macOS (arm64 or x86)
- Node.js ≥25.0
- Git CLI
- Claude API key (set to `ANTHROPIC_API_KEY`)

**Steps:**

```bash
# 1. Clone/setup clawd workspace
cd /Users/abdoulayemundow
git clone <repo> clawd  # or git init if starting fresh

# 2. Install Node dependencies
cd clawd
npm install

# 3. Verify OpenClaw CLI
openclaw --version

# 4. Set up .env (if needed)
touch .env
echo "ANTHROPIC_API_KEY=sk-ant-..." >> .env

# 5. Initialize message bus
node .bus/busctl.js init

# 6. Start Kairo process
openclaw start main  # Starts clawd agent session

# 7. Verify: Check router/subagents-index.txt
wc -l router/subagents-index.txt  # Should have 230+ agents
```

**Validation:**
- [ ] OpenClaw CLI accessible (`which openclaw`)
- [ ] Message bus initialized (`.bus/busctl.js` runs)
- [ ] Kairo session active (`openclaw sessions list | grep main`)
- [ ] Supervisor registry loaded (`cat router/subagents-index.txt | wc -l`)

### 2.2 Daily Startup

**On machine startup or session begin:**

```bash
# 1. Check if Kairo session is running
openclaw sessions list | grep main

# 2. If not running, start Kairo
openclaw start main

# 3. Verify supervisors are responsive
node .bus/busctl.js unread --agent kairo  # Any messages from overnight?

# 4. Check message bus health
sqlite3 .bus/bus.sqlite "PRAGMA integrity_check;"  # Should return "ok"

# 5. Verify token budget hasn't drifted
cat context.md | grep -A5 "Token Budget"
```

### 2.3 Supervisor Deployment

**To add a new supervisor (Phase 2+):**

1. **Create supervisor config** in `router/subagents.json`
   - persona_id, name, tags, model override, token budget
   - Example: 
   ```json
   {
     "persona_id": "aeos-agent",
     "name": "Aeos (Strategic Intelligence)",
     "capability_tags": ["research", "forecasting", "market-analysis"],
     "model": "claude-sonnet-4-6",
     "token_budget_weekly": "$0.02"
   }
   ```

2. **Register in supervisor registry**
   ```bash
   node .bus/busctl.js register --agent aeos-agent --tags research,forecasting
   ```

3. **Test supervisor invocation**
   ```bash
   openclaw spawn runtime="subagent" aeos-agent "Research current market trends in AI"
   ```

4. **Verify heartbeat**
   ```bash
   sleep 30
   node .bus/busctl.js unread --agent aeos-agent
   ```

5. **Update router/subagents-index.txt**
   ```bash
   node .bus/busctl.js index > router/subagents-index.txt
   ```

6. **Commit to Git**
   ```bash
   git add router/subagents.json router/subagents-index.txt
   git commit -m "Add Aeos supervisor (research, forecasting)"
   ```

### 2.4 Workflow Deployment

**To run a multi-agent workflow:**

1. **Create workflow script** (e.g., `workflows/phase-1-build.js`)
2. **Include meta block** (name, description, phases)
3. **Invoke via Workflow tool** in Kairo session
4. **Monitor progress** via `/workflows` in UI
5. **On completion:** Verify artifacts + commit

---

## 3. Release Process

### 3.1 Release Stages

| Stage | Condition | Approval | Duration |
|-------|-----------|----------|----------|
| **Dev** | Local changes on feature branch | None | Ongoing |
| **Test** | Branch pushed, CI passes | Kairo (automated) | 1-2 hours |
| **Stage** | Artifacts reviewed, Risk Register cleared | Kairo | 24 hours (buffer) |
| **Prod** | Stef approval + deployment complete | Stef | Immediate |

### 3.2 Release Checklist (Before Production)

**Before any production deployment:**

- [ ] All artifacts generated + reviewed (SAD, ADRs, etc.)
- [ ] Risk Register ≥8 risks cleared (mitigations in place)
- [ ] Message bus health check passed
- [ ] Supervisor registry updated + verified
- [ ] Token budget confirmed (no overruns forecasted)
- [ ] Backup created + tested (restore from backup)
- [ ] Git branch up-to-date with main
- [ ] Context.md reflects current state
- [ ] Stef approval obtained

**Production Deployment:**

```bash
# 1. Stage work to branch
git checkout -b deploy/phase-1-release-2026-07-27

# 2. Commit artifacts
git add AI-Organization/*.md
git commit -m "Release: Phase 1 OpenClaw AI Org (SAD, ADRs, Constitution, etc.)"

# 3. Create backup pre-deployment
node .bus/busctl.js backup  # Creates snapshot in /Desktop/Context/backups/

# 4. Run deployment script
./scripts/deploy.sh --stage prod  # TBD: Create deployment script

# 5. Verify post-deployment
node .bus/busctl.js health  # All systems green

# 6. Merge to main
git push origin deploy/phase-1-release-2026-07-27
git checkout main
git merge deploy/phase-1-release-2026-07-27

# 7. Tag release
git tag -a v1.0-phase-1 -m "Phase 1: OpenClaw AI Org Foundation"
git push origin --tags
```

---

## 4. Backup & Disaster Recovery

### 4.1 Backup Strategy

**Daily automated backup:**
- Time: 2:00 AM CT (off-hours, minimal impact)
- Source: `/clawd/` + `/Desktop/Context/` + message bus
- Destination: `/Desktop/Context/backups/` (local) + S3 (Phase 2)
- Retention: 30-day rolling window

**Manual backup (before major deployments):**
```bash
node .bus/busctl.js backup --tag "pre-phase-1-release"
```

### 4.2 Recovery Procedure

**If local data is corrupted or lost:**

1. **Identify backup point** (latest clean backup)
2. **Halt all operations** (stop Kairo, stop supervisors)
3. **Restore from backup**
   ```bash
   node .bus/busctl.js restore --from /Desktop/Context/backups/2026-07-25-020000
   ```
4. **Verify data integrity**
   ```bash
   sqlite3 .bus/bus.sqlite "PRAGMA integrity_check;"
   git status  # Check if all files present
   ```
5. **Restart Kairo + supervisors**
   ```bash
   openclaw start main
   ```
6. **Post-recovery audit**
   - Check if any work was lost (compare context.md before/after)
   - Replay manual actions from audit trail
   - Log incident to Risk Register + message bus

---

## 5. Monitoring & Health Checks

### 5.1 Health Check Script (Daily)

```bash
#!/bin/bash
# Daily health check (runs 9:00 AM CT via cron)

echo "=== OpenClaw AI System Health Check ==="
echo "Date: $(date)"

# 1. Check Kairo process
if openclaw sessions list | grep -q "main"; then
  echo "✓ Kairo session: RUNNING"
else
  echo "✗ Kairo session: DOWN (restarting...)"
  openclaw start main
fi

# 2. Check message bus
if sqlite3 /Users/abdoulayemundow/clawd/.bus/bus.sqlite "PRAGMA integrity_check;" | grep -q "ok"; then
  echo "✓ Message bus: HEALTHY"
else
  echo "✗ Message bus: CORRUPTED (escalate!)"
fi

# 3. Check supervisor registry
AGENT_COUNT=$(wc -l < /Users/abdoulayemundow/clawd/router/subagents-index.txt)
echo "✓ Supervisors indexed: $AGENT_COUNT"

# 4. Check token budget
WEEKLY_SPEND=$(grep -A2 "Token Budget" /Users/abdoulayemundow/Desktop/Context/context.md | tail -1)
echo "✓ Weekly token spend: $WEEKLY_SPEND"

# 5. Check disk space
DISK_USAGE=$(df /Users/abdoulayemundow | awk '{print $(NF-1)}' | tail -1)
echo "✓ Disk usage: $DISK_USAGE"

# 6. Check backup freshness
LAST_BACKUP=$(ls -t /Users/abdoulayemundow/Desktop/Context/backups/ | head -1)
echo "✓ Last backup: $LAST_BACKUP"

echo "=== Health Check Complete ==="
```

**Schedule (via cron):**
```bash
# Add to crontab
crontab -e

# Entry (runs daily at 9 AM CT)
0 9 * * * /Users/abdoulayemundow/clawd/scripts/health-check.sh >> /Users/abdoulayemundow/clawd/.logs/health-check.log 2>&1
```

---

## 6. Rollback Procedure

**If a deployment causes issues (crash, data loss, etc.):**

1. **Immediately halt operations**
   ```bash
   openclaw stop main
   ```

2. **Restore from backup (pre-deployment)**
   ```bash
   node .bus/busctl.js restore --from <backup-tag>
   ```

3. **Restart Kairo**
   ```bash
   openclaw start main
   ```

4. **Post-mortem**
   - Log incident (what broke, when, impact)
   - Update Risk Register (add mitigation for future)
   - Notify Stef (Telegram + message bus)
   - Schedule review (why did this deployment cause issues?)

---

## 7. Scaling Deployment (Future)

### 7.1 Phase 5: Cloud Backup + Multi-Region

**Timeline:** 2026-10-12+

**Deployment:**
- AWS S3 for backup (daily snapshots)
- CloudFront CDN for static content (docs, specs)
- Optional: Lambda for scheduled health checks
- Cost: ~$5/month

**Benefits:**
- Disaster recovery (if local machine fails)
- Backup accessible from anywhere
- Audit trail stored off-machine

### 7.2 Post-MVP: Distributed Multi-Team

**Timeline:** 2027-01-12+

**Deployment:**
- Kubernetes cluster (self-hosted or AWS EKS)
- PostgreSQL database (replaces SQLite)
- Message bus becomes centralized queue
- Multiple Kairo instances (one per team)

**Benefits:**
- Scales to 50+ agents
- Team separation (data isolation)
- High availability (redundancy)

---

## Appendix: Deployment Checklist

**Pre-Deployment (Every Release):**
- [ ] All artifacts generated
- [ ] Risk Register cleared (≥8 risks mitigated)
- [ ] Message bus health check
- [ ] Supervisor registry updated
- [ ] Token budget verified
- [ ] Backup created
- [ ] Git status clean
- [ ] Context.md current
- [ ] Stef approval obtained

**Post-Deployment:**
- [ ] All systems running (Kairo + supervisors)
- [ ] Health check passed
- [ ] Message bus operational
- [ ] No error logs
- [ ] Token spend within budget
- [ ] Backup of deployed state

