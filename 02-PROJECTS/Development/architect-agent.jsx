import { useState, useEffect, useRef } from "react";

const SYSTEM_PROMPT = `You are the ARCHITECT AGENT — an autonomous orchestrator for building products, campaigns, and systems from scratch.

You operate in 5 zones:

ZONE 1 — ENTRY & MODE SELECTION
On startup, ask the founder to select:
- NEW project (~3.8k tokens, 3-5 min)
- CONTINUE (resume) (~1.2k tokens, 1-2 min)
- ADD to existing (~2.0k tokens, 2-4 min)
Then run ECC skills check (confirm required tools/context available).
Select pipeline: Full (13 sections), Lite (6 sections), or Custom.

ZONE 2 — 13 SECTIONS PIPELINE
Run each section in order. For each section:
1. Brief Writer: prepare curated context brief
2. Section Agent: generate section artifact
3. Injector: contradiction check vs previous sections
4. Tracker: record state, flag issues
5. Save to 00-state.md

SECTIONS:
DISCOVERY:
- S01: Problem & Vision (REQUIRED + LEGAL SCAN)
- S02: User Roles & Personas (REQUIRED + LEGAL SCAN)
- S03: Feature Map & User Stories (REQUIRED + LEGAL SCAN)
COMMERCIAL & REACH:
- S04: Monetisation & Stripe (LEGAL SCAN) — FOUNDER_QUESTION PAUSE
- S05: SEO & GTM Strategy (LEGAL SCAN)
COMPLIANCE:
- S06: Accessibility & i18n (STRONGLY RECOMMENDED + LEGAL SCAN)
- S07: Analytics & Tracking (LEGAL SCAN)
- S08: UX, Interface Design & Branding (STRONGLY RECOMMENDED + LEGAL SCAN)
ENGINEERING:
- S09: Technical Architecture (REQUIRED + LEGAL SCAN)
- S10: Data Architecture (REQUIRED + LEGAL SCAN)
- S11: Security & Compliance (REQUIRED + LEGAL SCAN)
- S12: DevOps & Hosting (REQUIRED + LEGAL SCAN)
- S13: Testing & QA (REQUIRED + LEGAL SCAN)

LITE MODE (6 sections): S01, S03, S05, S08, S09, S13

LEGAL SCAN: For flagged sections, run 6-category legal scan and route issues to B-Legal planner step.

FOUNDER_QUESTION blocks: PAUSE pipeline, present question, wait for founder input before continuing.

FAILURE RECOVERY: If section agent fails → Retry (auto) → Founder choice (retry/skip/manual) → Stub doc + issue log → Continue.

ZONE 3 — SUPPORT AGENTS (run in background)
- Brief Writer: runs after every section, prepares curated context brief for next agent, extracts Founder Voice verbatim
- Tracker: background dispatch after every section, writes 00-state.md, records claude-mem observation
- Change Management: triggered by founder pivot mid-pipeline, impact analysis, section doc updates, RESUME_PIPELINE_FROM routing
- Principles: foundational layer all 13 section agents read — includes Ask vs. Derive, Output Standard, Legal Scan directive, FOUNDER_QUESTION protocol

ZONE 4 — PLANNER PHASE
After all sections complete, run in order:
A. GSD Discuss — align scope & constraints
B. Extract Blueprint — section by section
B-Legal. Legal Synthesis — 6-category legal scan
C. Write Tasks — task list, deps, order
D. Self-review — santa method, quality & coverage
E. Master Spec — unified specification
F. Executor Prompt — self-contained executor prompt
G. Cost Estimate — tokens, time, monthly cost
H. Founder Approval Gate (MANDATORY PAUSE) — founder approves or redirects
I. Checkpoint Write — planner-checkpoint.md
J. Memory Record — claude-mem record

ZONE 5 — OUTPUTS & HANDOFF
Generate three files:
1. plan.md — phased implementation plan (phases, milestones, dependencies, build order, tasks, constraints)
2. spec.md — master engineering specification (complete specs, architecture & data, interfaces & contracts, requirements)
3. prompt.md — self-contained executor prompt (full context, constraints, acceptance criteria, deliverables)
→ Hand off to cold Executor session (no prior context needed)

CRITICAL RULES:
- NEVER skip REQUIRED sections without explicit founder approval
- ALWAYS pause at FOUNDER_QUESTION blocks
- ALWAYS run contradiction check before marking section complete
- ALWAYS save state after each section
- Legal scan flags = BLOCKED in Planner Phase until resolved
- Maintain Founder Voice verbatim in tone-sensitive sections

CURRENT USER CONTEXT:
- Founder: Stefan
- Primary products: The Plug AI (AI education platform), BigHeart Health (community health outreach)
- Stack: Claude, Canva, Google Drive, Google Docs
- Lite mode recommended for BigHeart campaign projects
- Full mode recommended for The Plug AI platform build`;

const SECTIONS = {
  full: [
    { id: "S01", name: "Problem & Vision", zone: "DISCOVERY", required: true },
    { id: "S02", name: "User Roles & Personas", zone: "DISCOVERY", required: true },
    { id: "S03", name: "Feature Map & User Stories", zone: "DISCOVERY", required: true },
    { id: "S04", name: "Monetisation & Stripe", zone: "COMMERCIAL", required: false, founderPause: true },
    { id: "S05", name: "SEO & GTM Strategy", zone: "COMMERCIAL", required: false },
    { id: "S06", name: "Accessibility & i18n", zone: "COMPLIANCE", required: false, stronglyRecommended: true },
    { id: "S07", name: "Analytics & Tracking", zone: "COMPLIANCE", required: false },
    { id: "S08", name: "UX, Interface Design & Branding", zone: "COMPLIANCE", required: false, stronglyRecommended: true },
    { id: "S09", name: "Technical Architecture", zone: "ENGINEERING", required: true },
    { id: "S10", name: "Data Architecture", zone: "ENGINEERING", required: true },
    { id: "S11", name: "Security & Compliance", zone: "ENGINEERING", required: true },
    { id: "S12", name: "DevOps & Hosting", zone: "ENGINEERING", required: true },
    { id: "S13", name: "Testing & QA", zone: "ENGINEERING", required: true },
  ],
  lite: ["S01", "S03", "S05", "S08", "S09", "S13"],
};

const ZONE_COLORS = {
  DISCOVERY: "#3b82f6",
  COMMERCIAL: "#f59e0b",
  COMPLIANCE: "#10b981",
  ENGINEERING: "#8b5cf6",
};

const PLANNER_STEPS = [
  "A. GSD Discuss",
  "B. Extract Blueprint",
  "B-Legal. Legal Synthesis",
  "C. Write Tasks",
  "D. Self-review",
  "E. Master Spec",
  "F. Executor Prompt",
  "G. Cost Estimate",
  "H. Founder Approval ⚠️",
  "I. Checkpoint Write",
  "J. Memory Record",
];

export default function ArchitectAgent() {
  const [phase, setPhase] = useState("entry");
  const [mode, setMode] = useState(null);
  const [pipelineMode, setPipelineMode] = useState(null);
  const [activeSections, setActiveSections] = useState([]);
  const [sectionStatus, setSectionStatus] = useState({});
  const [currentSection, setCurrentSection] = useState(null);
  const [plannerStep, setPlannerStep] = useState(0);
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState("");
  const [loading, setLoading] = useState(false);
  const [paused, setPaused] = useState(false);
  const [pauseReason, setPauseReason] = useState("");
  const [outputs, setOutputs] = useState({ plan: "", spec: "", prompt: "" });
  const [founderVoice, setFounderVoice] = useState("");
  const [stateLog, setStateLog] = useState([]);
  const messagesEndRef = useRef(null);
  const conversationRef = useRef([]);

  useEffect(() => {
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [messages]);

  const addMessage = (role, content, meta = {}) => {
    const msg = { role, content, meta, timestamp: new Date().toLocaleTimeString() };
    setMessages((prev) => [...prev, msg]);
    if (role !== "system") {
      conversationRef.current = [...conversationRef.current, { role, content }];
    }
  };

  const callClaude = async (userMessage, contextOverride = null) => {
    setLoading(true);
    try {
      const msgs = contextOverride || [...conversationRef.current, { role: "user", content: userMessage }];
      const res = await fetch("https://api.anthropic.com/v1/messages", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          "x-api-key": import.meta.env.VITE_ANTHROPIC_API_KEY,
          "anthropic-version": "2023-06-01",
          "anthropic-dangerous-direct-browser-access": "true",
        },
        body: JSON.stringify({
          model: "claude-sonnet-4-5-20251001",
          max_tokens: 4096,
          system: SYSTEM_PROMPT,
          messages: msgs,
        }),
      });
      const data = await res.json();
      const reply = data.content?.[0]?.text || "No response";
      conversationRef.current = [...msgs, { role: "assistant", content: reply }];
      return reply;
    } catch (e) {
      return "Error calling Architect Agent. Check connection.";
    } finally {
      setLoading(false);
    }
  };

  const startSession = async (selectedMode) => {
    setMode(selectedMode);
    const modeMap = { new: "NEW project", continue: "CONTINUE (resume)", add: "ADD to existing" };
    addMessage("system", `Mode selected: ${modeMap[selectedMode]}`);
    const reply = await callClaude(
      `I want to start a ${modeMap[selectedMode]}. Run ECC skills check and ask me which pipeline to use: Full (13 sections), Lite (6 sections), or Custom.`
    );
    addMessage("assistant", reply);
    setPhase("mode-select");
  };

  const selectPipeline = async (selected) => {
    setPipelineMode(selected);
    const sections = selected === "lite"
      ? SECTIONS.full.filter((s) => SECTIONS.lite.includes(s.id))
      : SECTIONS.full;
    setActiveSections(sections);
    const initialStatus = {};
    sections.forEach((s) => (initialStatus[s.id] = "pending"));
    setSectionStatus(initialStatus);
    addMessage("system", `Pipeline: ${selected.toUpperCase()} — ${sections.length} sections loaded`);
    const reply = await callClaude(
      `I'll run ${selected} mode with ${sections.length} sections. Start with S01: Problem & Vision. Ask me for the project name and core problem statement to begin.`
    );
    addMessage("assistant", reply);
    setCurrentSection("S01");
    setPhase("pipeline");
  };

  const runSectionStep = async (sectionId, stepName) => {
    const section = activeSections.find((s) => s.id === sectionId);
    if (!section) return;
    const reply = await callClaude(
      `Now running ${stepName} for ${sectionId}: ${section.name}. Based on our conversation so far, execute this step and provide the output. Flag any contradictions with previous sections and note any legal scan items.`
    );
    addMessage("assistant", reply, { section: sectionId, step: stepName });
    if (stepName === "Tracker") {
      setSectionStatus((prev) => ({ ...prev, [sectionId]: "complete" }));
      setStateLog((prev) => [
        ...prev,
        { section: sectionId, name: section.name, timestamp: new Date().toLocaleTimeString() },
      ]);
      const idx = activeSections.findIndex((s) => s.id === sectionId);
      if (idx < activeSections.length - 1) {
        const next = activeSections[idx + 1];
        setCurrentSection(next.id);
        if (next.founderPause) {
          setPaused(true);
          setPauseReason(`FOUNDER_QUESTION block before ${next.id}: ${next.name}`);
        }
      } else {
        setPhase("planner");
        const reply2 = await callClaude(
          "All sections complete. Begin Zone 4 Planner Phase. Start with Step A: GSD Discuss — align scope and constraints based on everything we've built."
        );
        addMessage("assistant", reply2, { planner: true });
      }
    }
  };

  const sendMessage = async () => {
    if (!input.trim() || loading) return;
    const userMsg = input.trim();
    setInput("");
    addMessage("user", userMsg);
    if (paused) {
      setPaused(false);
      setPauseReason("");
      addMessage("system", "Pause resolved. Resuming pipeline.");
    }
    const reply = await callClaude(userMsg);
    addMessage("assistant", reply);
    if (userMsg.length > 50 && !founderVoice) {
      setFounderVoice(userMsg.substring(0, 100) + "...");
    }
  };

  const advancePlanner = async () => {
    if (plannerStep >= PLANNER_STEPS.length - 1) {
      setPhase("outputs");
      generateOutputs();
      return;
    }
    const next = plannerStep + 1;
    setPlannerStep(next);
    const stepName = PLANNER_STEPS[next];
    if (stepName.includes("Founder Approval")) {
      setPaused(true);
      setPauseReason("MANDATORY PAUSE: Founder must approve before outputs are generated.");
    }
    const reply = await callClaude(
      `Execute Planner Step ${stepName}. Be thorough and specific based on all section outputs.`
    );
    addMessage("assistant", reply, { plannerStep: next });
  };

  const generateOutputs = async () => {
    addMessage("system", "Generating Zone 5 outputs: plan.md, spec.md, prompt.md");
    const planReply = await callClaude(
      "Generate plan.md — the phased implementation plan with phases, milestones, dependencies, and build order. Be specific and actionable."
    );
    setOutputs((prev) => ({ ...prev, plan: planReply }));
    addMessage("assistant", planReply, { output: "plan.md" });

    const specReply = await callClaude(
      "Generate spec.md — the master engineering specification with complete architecture, interfaces, contracts, and requirements."
    );
    setOutputs((prev) => ({ ...prev, spec: specReply }));
    addMessage("assistant", specReply, { output: "spec.md" });

    const promptReply = await callClaude(
      "Generate prompt.md — the self-contained executor prompt with full context, constraints, acceptance criteria, and deliverables. A cold session with no prior context should be able to execute from this alone."
    );
    setOutputs((prev) => ({ ...prev, prompt: promptReply }));
    addMessage("assistant", promptReply, { output: "prompt.md" });
  };

  const resetAll = () => {
    setPhase("entry");
    setMode(null);
    setPipelineMode(null);
    setActiveSections([]);
    setSectionStatus({});
    setCurrentSection(null);
    setPlannerStep(0);
    setMessages([]);
    setInput("");
    setLoading(false);
    setPaused(false);
    setPauseReason("");
    setOutputs({ plan: "", spec: "", prompt: "" });
    setFounderVoice("");
    setStateLog([]);
    conversationRef.current = [];
  };

  const getStatusColor = (status) => {
    if (status === "complete") return "#10b981";
    if (status === "active") return "#f59e0b";
    return "#374151";
  };

  const copyOutput = (key) => {
    if (outputs[key]) navigator.clipboard.writeText(outputs[key]);
  };

  return (
    <div style={{
      background: "#0a0a0f",
      minHeight: "100vh",
      fontFamily: "'JetBrains Mono', 'Courier New', monospace",
      color: "#e2e8f0",
      display: "flex",
      flexDirection: "column",
    }}>
      {/* Header */}
      <div style={{
        background: "linear-gradient(135deg, #0f0f1a 0%, #1a0a2e 100%)",
        borderBottom: "1px solid #1e293b",
        padding: "14px 20px",
        display: "flex",
        alignItems: "center",
        justifyContent: "space-between",
        flexShrink: 0,
      }}>
        <div style={{ display: "flex", alignItems: "center", gap: "12px" }}>
          <div style={{
            width: 34, height: 34,
            background: "linear-gradient(135deg, #7c3aed, #3b82f6)",
            borderRadius: 8,
            display: "flex", alignItems: "center", justifyContent: "center",
            fontSize: 16, flexShrink: 0,
          }}>⚡</div>
          <div>
            <div style={{ fontSize: 13, fontWeight: 700, letterSpacing: "0.08em", color: "#c4b5fd" }}>
              /architect
            </div>
            <div style={{ fontSize: 9, color: "#64748b", letterSpacing: "0.12em" }}>
              BLUEPRINT TO BUILD — STEFAN'S WORKSPACE
            </div>
          </div>
        </div>
        <div style={{ display: "flex", gap: 6, alignItems: "center" }}>
          {["entry", "pipeline", "planner", "outputs"].map((p, i) => (
            <div key={p} style={{ display: "flex", alignItems: "center", gap: 3 }}>
              <div style={{
                width: 7, height: 7, borderRadius: "50%",
                background: phase === p ? "#7c3aed" : i < ["entry", "pipeline", "planner", "outputs"].indexOf(phase) ? "#10b981" : "#1e293b",
                boxShadow: phase === p ? "0 0 8px #7c3aed" : "none",
                transition: "all 0.3s",
              }} />
              <span style={{ fontSize: 8, color: phase === p ? "#c4b5fd" : "#475569", textTransform: "uppercase", letterSpacing: "0.08em" }}>{p}</span>
              {i < 3 && <span style={{ color: "#1e293b", fontSize: 9, margin: "0 1px" }}>→</span>}
            </div>
          ))}
          {phase !== "entry" && (
            <button onClick={resetAll} style={{
              marginLeft: 12, background: "transparent", border: "1px solid #374151",
              borderRadius: 4, padding: "3px 8px", color: "#64748b", fontSize: 9,
              cursor: "pointer", letterSpacing: "0.08em",
            }}>RESET</button>
          )}
        </div>
      </div>

      <div style={{ display: "flex", flex: 1, overflow: "hidden" }}>
        {/* Left Sidebar */}
        <div style={{
          width: 220,
          background: "#0d0d18",
          borderRight: "1px solid #1e293b",
          overflowY: "auto",
          padding: "14px 10px",
          flexShrink: 0,
        }}>
          <div style={{ fontSize: 8, color: "#475569", letterSpacing: "0.15em", marginBottom: 10, textTransform: "uppercase" }}>
            Pipeline Status
          </div>

          {activeSections.length === 0 ? (
            <div style={{ fontSize: 10, color: "#374151", textAlign: "center", marginTop: 20, lineHeight: 1.6 }}>
              Select mode to<br />load sections
            </div>
          ) : (
            Object.entries(
              activeSections.reduce((acc, s) => {
                if (!acc[s.zone]) acc[s.zone] = [];
                acc[s.zone].push(s);
                return acc;
              }, {})
            ).map(([zone, sections]) => (
              <div key={zone} style={{ marginBottom: 14 }}>
                <div style={{
                  fontSize: 7, letterSpacing: "0.15em", textTransform: "uppercase",
                  color: ZONE_COLORS[zone], marginBottom: 5,
                  borderLeft: `2px solid ${ZONE_COLORS[zone]}`, paddingLeft: 6,
                }}>
                  {zone}
                </div>
                {sections.map((s) => (
                  <div key={s.id} style={{
                    display: "flex", alignItems: "center", gap: 5,
                    padding: "4px 7px", borderRadius: 4, marginBottom: 2,
                    background: currentSection === s.id ? "#1a1a2e" : "transparent",
                    border: currentSection === s.id ? "1px solid #3b82f6" : "1px solid transparent",
                    cursor: phase === "pipeline" ? "pointer" : "default",
                    transition: "all 0.15s",
                  }} onClick={() => phase === "pipeline" && setCurrentSection(s.id)}>
                    <div style={{
                      width: 5, height: 5, borderRadius: "50%", flexShrink: 0,
                      background: getStatusColor(sectionStatus[s.id]),
                      boxShadow: sectionStatus[s.id] === "complete" ? "0 0 5px #10b981" : "none",
                      transition: "all 0.3s",
                    }} />
                    <span style={{ fontSize: 8, color: currentSection === s.id ? "#93c5fd" : "#64748b", flexShrink: 0 }}>
                      {s.id}
                    </span>
                    <span style={{ fontSize: 8, color: currentSection === s.id ? "#cbd5e1" : "#475569", flex: 1, lineHeight: 1.3 }}>
                      {s.name}
                    </span>
                    {s.required && <span style={{ fontSize: 6, color: "#ef4444", flexShrink: 0 }}>REQ</span>}
                    {s.stronglyRecommended && <span style={{ fontSize: 6, color: "#f59e0b", flexShrink: 0 }}>REC</span>}
                  </div>
                ))}
              </div>
            ))
          )}

          {stateLog.length > 0 && (
            <div style={{ marginTop: 14 }}>
              <div style={{ fontSize: 8, color: "#475569", letterSpacing: "0.12em", marginBottom: 6, textTransform: "uppercase" }}>
                00-state.md
              </div>
              {stateLog.map((log, i) => (
                <div key={i} style={{ fontSize: 8, color: "#10b981", marginBottom: 2, paddingLeft: 7, borderLeft: "1px solid #10b981" }}>
                  ✓ {log.section} {log.timestamp}
                </div>
              ))}
            </div>
          )}

          {phase === "planner" && (
            <div style={{ marginTop: 14 }}>
              <div style={{ fontSize: 8, color: "#475569", letterSpacing: "0.12em", marginBottom: 6, textTransform: "uppercase" }}>
                Planner Phase
              </div>
              {PLANNER_STEPS.map((step, i) => (
                <div key={i} style={{
                  fontSize: 8, padding: "3px 7px", marginBottom: 2, borderRadius: 3,
                  background: i === plannerStep ? "#1a1a2e" : "transparent",
                  color: i < plannerStep ? "#10b981" : i === plannerStep ? "#f59e0b" : "#374151",
                  borderLeft: i === plannerStep ? "2px solid #f59e0b" : "2px solid transparent",
                  transition: "all 0.2s",
                }}>
                  {i < plannerStep ? "✓ " : i === plannerStep ? "→ " : "  "}{step}
                </div>
              ))}
            </div>
          )}
        </div>

        {/* Main Chat Area */}
        <div style={{ flex: 1, display: "flex", flexDirection: "column", overflow: "hidden" }}>
          {/* Entry Phase */}
          {phase === "entry" && (
            <div style={{
              flex: 1, display: "flex", flexDirection: "column", alignItems: "center", justifyContent: "center", gap: 28,
              padding: 32,
            }}>
              <div style={{ textAlign: "center" }}>
                <div style={{ fontSize: 10, color: "#7c3aed", letterSpacing: "0.3em", textTransform: "uppercase", marginBottom: 6 }}>
                  ARCHITECT AGENT
                </div>
                <div style={{ fontSize: 26, fontWeight: 800, color: "#e2e8f0", letterSpacing: "-0.02em", marginBottom: 6 }}>
                  Blueprint to Build
                </div>
                <div style={{ fontSize: 12, color: "#64748b" }}>
                  Stefan's product development orchestrator
                </div>
              </div>

              <div style={{ display: "flex", gap: 14 }}>
                {[
                  { id: "new", label: "NEW", sub: "project", tokens: "~3.8k tokens", time: "3-5 min", color: "#7c3aed" },
                  { id: "continue", label: "CONTINUE", sub: "resume", tokens: "~1.2k tokens", time: "1-2 min", color: "#3b82f6" },
                  { id: "add", label: "ADD", sub: "to existing", tokens: "~2.0k tokens", time: "2-4 min", color: "#10b981" },
                ].map((m) => (
                  <button key={m.id} onClick={() => startSession(m.id)} disabled={loading} style={{
                    background: "transparent",
                    border: `1px solid ${m.color}`,
                    borderRadius: 8,
                    padding: "18px 22px",
                    cursor: loading ? "not-allowed" : "pointer",
                    color: m.color,
                    textAlign: "center",
                    transition: "all 0.2s",
                    minWidth: 130,
                    opacity: loading ? 0.5 : 1,
                  }}
                    onMouseEnter={e => { if (!loading) e.currentTarget.style.background = m.color + "22"; }}
                    onMouseLeave={e => { e.currentTarget.style.background = "transparent"; }}
                  >
                    <div style={{ fontSize: 15, fontWeight: 700, letterSpacing: "0.1em" }}>{m.label}</div>
                    <div style={{ fontSize: 10, opacity: 0.7, marginTop: 2 }}>{m.sub}</div>
                    <div style={{ fontSize: 9, marginTop: 8, color: "#64748b" }}>{m.tokens}</div>
                    <div style={{ fontSize: 9, color: "#64748b" }}>{m.time}</div>
                  </button>
                ))}
              </div>

              {loading && (
                <div style={{ display: "flex", gap: 6, alignItems: "center" }}>
                  <div style={{ width: 6, height: 6, borderRadius: "50%", background: "#7c3aed", animation: "pulse 1s infinite" }} />
                  <span style={{ fontSize: 11, color: "#64748b" }}>Initializing Architect Agent...</span>
                </div>
              )}

              {messages.length > 0 && (
                <div style={{ width: "100%", maxWidth: 560, marginTop: 4 }}>
                  {messages.slice(-3).map((m, i) => (
                    <div key={i} style={{
                      background: "#0f0f1a", border: "1px solid #1e293b", borderRadius: 8, padding: "10px 14px", marginBottom: 8,
                    }}>
                      <div style={{ fontSize: 9, color: "#475569", marginBottom: 3, textTransform: "uppercase" }}>{m.role}</div>
                      <div style={{ fontSize: 11, color: "#94a3b8", lineHeight: 1.6, whiteSpace: "pre-wrap" }}>{m.content}</div>
                    </div>
                  ))}
                </div>
              )}
            </div>
          )}

          {/* Mode Select */}
          {phase === "mode-select" && (
            <div style={{ flex: 1, display: "flex", flexDirection: "column", overflow: "hidden" }}>
              <div style={{ flex: 1, overflowY: "auto", padding: "14px 18px" }}>
                {messages.map((m, i) => <MessageBubble key={i} message={m} />)}
                {loading && <LoadingDot />}
                <div ref={messagesEndRef} />
              </div>
              <div style={{
                borderTop: "1px solid #1e293b", padding: "14px 18px",
                display: "flex", flexDirection: "column", gap: 10, background: "#0d0d18",
              }}>
                <div style={{ fontSize: 10, color: "#64748b", textAlign: "center" }}>Select Pipeline Mode:</div>
                <div style={{ display: "flex", gap: 10, justifyContent: "center" }}>
                  {[
                    { id: "full", label: "FULL", sections: "13 sections", tokens: "~28k tokens", time: "35-55 min" },
                    { id: "lite", label: "LITE", sections: "6 sections", tokens: "~14k tokens", time: "18-30 min" },
                  ].map((p) => (
                    <button key={p.id} onClick={() => selectPipeline(p.id)} disabled={loading} style={{
                      background: "transparent", border: "1px solid #7c3aed", borderRadius: 6,
                      padding: "12px 18px", cursor: loading ? "not-allowed" : "pointer",
                      color: "#c4b5fd", textAlign: "center", opacity: loading ? 0.5 : 1,
                    }}
                      onMouseEnter={e => { if (!loading) e.currentTarget.style.background = "#7c3aed22"; }}
                      onMouseLeave={e => { e.currentTarget.style.background = "transparent"; }}
                    >
                      <div style={{ fontSize: 13, fontWeight: 700 }}>{p.label}</div>
                      <div style={{ fontSize: 9, color: "#64748b", marginTop: 3 }}>{p.sections}</div>
                      <div style={{ fontSize: 9, color: "#475569" }}>{p.tokens} · {p.time}</div>
                    </button>
                  ))}
                </div>
                <InputBar input={input} setInput={setInput} onSend={sendMessage} loading={loading} paused={paused} />
              </div>
            </div>
          )}

          {/* Pipeline / Planner / Outputs */}
          {(phase === "pipeline" || phase === "planner" || phase === "outputs") && (
            <div style={{ flex: 1, display: "flex", flexDirection: "column", overflow: "hidden" }}>
              {paused && (
                <div style={{
                  background: "#7c1d1d", borderBottom: "1px solid #ef4444",
                  padding: "8px 18px", display: "flex", alignItems: "center", justifyContent: "space-between",
                  flexShrink: 0,
                }}>
                  <div style={{ display: "flex", alignItems: "center", gap: 8 }}>
                    <span style={{ fontSize: 13 }}>⚠️</span>
                    <div>
                      <div style={{ fontSize: 10, color: "#fca5a5", fontWeight: 700, letterSpacing: "0.08em" }}>
                        PAUSED — FOUNDER ACTION REQUIRED
                      </div>
                      <div style={{ fontSize: 9, color: "#f87171" }}>{pauseReason}</div>
                    </div>
                  </div>
                  <button onClick={() => { setPaused(false); setPauseReason(""); addMessage("system", "Pause resolved. Resuming pipeline."); }} style={{
                    background: "#ef4444", border: "none", borderRadius: 4, padding: "5px 10px",
                    color: "white", fontSize: 9, cursor: "pointer", fontWeight: 700,
                  }}>
                    APPROVE & CONTINUE
                  </button>
                </div>
              )}

              <div style={{ flex: 1, overflowY: "auto", padding: "14px 18px" }}>
                {messages.map((m, i) => <MessageBubble key={i} message={m} />)}
                {loading && <LoadingDot />}
                <div ref={messagesEndRef} />
              </div>

              {phase === "pipeline" && currentSection && (
                <div style={{
                  borderTop: "1px solid #1e293b", padding: "8px 18px",
                  background: "#0d0d18", display: "flex", gap: 6, flexWrap: "wrap", alignItems: "center",
                  flexShrink: 0,
                }}>
                  {["Brief Writer", "Section Agent", "Injector", "Tracker"].map((step) => (
                    <button key={step} onClick={() => runSectionStep(currentSection, step)} disabled={loading || paused} style={{
                      background: "transparent", border: "1px solid #1e293b", borderRadius: 4,
                      padding: "5px 10px", color: loading || paused ? "#374151" : "#64748b",
                      fontSize: 9, cursor: loading || paused ? "not-allowed" : "pointer", letterSpacing: "0.04em",
                      transition: "all 0.15s",
                    }}
                      onMouseEnter={e => { if (!loading && !paused) e.currentTarget.style.borderColor = "#7c3aed"; }}
                      onMouseLeave={e => e.currentTarget.style.borderColor = "#1e293b"}
                    >
                      ▶ {step}
                    </button>
                  ))}
                  <div style={{ flex: 1 }} />
                  <span style={{ fontSize: 9, color: "#475569" }}>
                    {currentSection} — {activeSections.find(s => s.id === currentSection)?.name}
                  </span>
                </div>
              )}

              {phase === "planner" && (
                <div style={{
                  borderTop: "1px solid #1e293b", padding: "8px 18px",
                  background: "#0d0d18", display: "flex", gap: 8, alignItems: "center", flexShrink: 0,
                }}>
                  <button onClick={advancePlanner} disabled={loading || paused} style={{
                    background: loading || paused ? "#374151" : "#7c3aed",
                    border: "none", borderRadius: 4, padding: "7px 14px",
                    color: "white", fontSize: 10, cursor: loading || paused ? "not-allowed" : "pointer", fontWeight: 700,
                    transition: "all 0.2s",
                  }}>
                    → {PLANNER_STEPS[Math.min(plannerStep + 1, PLANNER_STEPS.length - 1)]}
                  </button>
                  <span style={{ fontSize: 9, color: "#475569" }}>
                    Step {plannerStep + 1}/{PLANNER_STEPS.length}: {PLANNER_STEPS[plannerStep]}
                  </span>
                </div>
              )}

              <InputBar input={input} setInput={setInput} onSend={sendMessage} loading={loading} paused={paused} />
            </div>
          )}
        </div>

        {/* Right Panel */}
        {(phase === "pipeline" || phase === "planner" || phase === "outputs") && (
          <div style={{
            width: 200, background: "#0d0d18", borderLeft: "1px solid #1e293b",
            overflowY: "auto", padding: "14px 10px", flexShrink: 0,
          }}>
            <div style={{ fontSize: 8, color: "#475569", letterSpacing: "0.12em", marginBottom: 10, textTransform: "uppercase" }}>
              Zone 5 Outputs
            </div>
            {["plan", "spec", "prompt"].map((doc) => (
              <div key={doc} style={{
                background: "#0f0f1a", border: `1px solid ${outputs[doc] ? "#10b981" : "#1e293b"}`,
                borderRadius: 5, padding: "8px 10px", marginBottom: 7,
                transition: "border-color 0.3s",
              }}>
                <div style={{ display: "flex", justifyContent: "space-between", alignItems: "center" }}>
                  <div style={{ fontSize: 9, color: outputs[doc] ? "#10b981" : "#374151", fontWeight: 700, letterSpacing: "0.08em" }}>
                    {outputs[doc] ? "✓" : "○"} {doc}.md
                  </div>
                  {outputs[doc] && (
                    <button onClick={() => copyOutput(doc)} style={{
                      background: "transparent", border: "none", color: "#64748b",
                      fontSize: 9, cursor: "pointer", padding: "0 2px",
                    }} title="Copy">⧉</button>
                  )}
                </div>
                {outputs[doc] && (
                  <div style={{ fontSize: 8, color: "#64748b", marginTop: 3, lineHeight: 1.4 }}>
                    {outputs[doc].substring(0, 70)}...
                  </div>
                )}
              </div>
            ))}

            {founderVoice && (
              <div style={{ marginTop: 14 }}>
                <div style={{ fontSize: 8, color: "#475569", letterSpacing: "0.12em", marginBottom: 6, textTransform: "uppercase" }}>
                  Founder Voice
                </div>
                <div style={{
                  background: "#0f0f1a", border: "1px solid #7c3aed", borderRadius: 5, padding: "8px 10px",
                  fontSize: 9, color: "#c4b5fd", lineHeight: 1.5, fontStyle: "italic",
                }}>
                  "{founderVoice}"
                </div>
              </div>
            )}

            <div style={{ marginTop: 14 }}>
              <div style={{ fontSize: 8, color: "#475569", letterSpacing: "0.12em", marginBottom: 6, textTransform: "uppercase" }}>
                Quick Deploy
              </div>
              {[
                { label: "The Plug AI", pipeline: "full" },
                { label: "BigHeart Campaign", pipeline: "lite" },
              ].map((preset) => (
                <button key={preset.label} onClick={resetAll} style={{
                  display: "block", width: "100%", background: "transparent",
                  border: "1px solid #1e293b", borderRadius: 4, padding: "7px 8px",
                  color: "#64748b", fontSize: 9, cursor: "pointer", textAlign: "left",
                  marginBottom: 4,
                }}
                  onMouseEnter={e => { e.currentTarget.style.borderColor = "#7c3aed"; e.currentTarget.style.color = "#c4b5fd"; }}
                  onMouseLeave={e => { e.currentTarget.style.borderColor = "#1e293b"; e.currentTarget.style.color = "#64748b"; }}
                >
                  ⚡ {preset.label}
                  <br />
                  <span style={{ fontSize: 7, color: "#374151" }}>{preset.pipeline} mode</span>
                </button>
              ))}
            </div>

            {/* Progress bar */}
            {activeSections.length > 0 && (
              <div style={{ marginTop: 14 }}>
                <div style={{ fontSize: 8, color: "#475569", letterSpacing: "0.12em", marginBottom: 6, textTransform: "uppercase" }}>
                  Progress
                </div>
                <div style={{ background: "#1e293b", borderRadius: 4, height: 4, overflow: "hidden" }}>
                  <div style={{
                    height: "100%",
                    width: `${(Object.values(sectionStatus).filter(s => s === "complete").length / activeSections.length) * 100}%`,
                    background: "linear-gradient(90deg, #7c3aed, #3b82f6)",
                    transition: "width 0.5s ease",
                  }} />
                </div>
                <div style={{ fontSize: 8, color: "#475569", marginTop: 3 }}>
                  {Object.values(sectionStatus).filter(s => s === "complete").length}/{activeSections.length} sections
                </div>
              </div>
            )}
          </div>
        )}
      </div>

      <style>{`
        @keyframes pulse {
          0%, 100% { opacity: 1; }
          50% { opacity: 0.3; }
        }
      `}</style>
    </div>
  );
}

function InputBar({ input, setInput, onSend, loading, paused }) {
  return (
    <div style={{
      borderTop: "1px solid #1e293b", padding: "10px 18px",
      background: "#0a0a0f", display: "flex", gap: 7, flexShrink: 0,
    }}>
      <input
        value={input}
        onChange={e => setInput(e.target.value)}
        onKeyDown={e => e.key === "Enter" && !e.shiftKey && onSend()}
        placeholder={paused ? "Resolve pause above to continue..." : "Respond to Architect Agent..."}
        disabled={loading}
        style={{
          flex: 1, background: "#0f0f1a", border: "1px solid #1e293b",
          borderRadius: 5, padding: "9px 12px", color: "#e2e8f0",
          fontSize: 12, outline: "none", fontFamily: "inherit",
          transition: "border-color 0.2s",
        }}
        onFocus={e => e.target.style.borderColor = "#7c3aed"}
        onBlur={e => e.target.style.borderColor = "#1e293b"}
      />
      <button onClick={onSend} disabled={loading || !input.trim()} style={{
        background: "#7c3aed", border: "none", borderRadius: 5,
        padding: "9px 18px", color: "white", fontSize: 11,
        cursor: loading || !input.trim() ? "not-allowed" : "pointer", fontWeight: 700,
        opacity: loading || !input.trim() ? 0.4 : 1,
        transition: "opacity 0.2s",
      }}>
        SEND
      </button>
    </div>
  );
}

function LoadingDot() {
  return (
    <div style={{ display: "flex", gap: 6, padding: "10px 0", alignItems: "center" }}>
      <div style={{ width: 5, height: 5, borderRadius: "50%", background: "#7c3aed", animation: "pulse 1s infinite" }} />
      <div style={{ width: 5, height: 5, borderRadius: "50%", background: "#7c3aed", animation: "pulse 1s infinite", animationDelay: "0.2s" }} />
      <div style={{ width: 5, height: 5, borderRadius: "50%", background: "#7c3aed", animation: "pulse 1s infinite", animationDelay: "0.4s" }} />
      <span style={{ fontSize: 10, color: "#64748b", marginLeft: 4 }}>Architect Agent processing...</span>
    </div>
  );
}

function MessageBubble({ message }) {
  const colors = {
    user: { bg: "#0f172a", border: "#1e3a5f", label: "#3b82f6" },
    assistant: { bg: "#0f0f1a", border: "#2d1b4e", label: "#7c3aed" },
    system: { bg: "#0a0a0a", border: "#1e293b", label: "#374151" },
  };
  const c = colors[message.role] || colors.system;

  return (
    <div style={{
      background: c.bg, border: `1px solid ${c.border}`, borderRadius: 7,
      padding: "10px 14px", marginBottom: 8,
    }}>
      <div style={{ display: "flex", justifyContent: "space-between", alignItems: "center", marginBottom: 5 }}>
        <div style={{ display: "flex", gap: 6, alignItems: "center" }}>
          <span style={{ fontSize: 8, color: c.label, textTransform: "uppercase", letterSpacing: "0.12em", fontWeight: 700 }}>
            {message.role === "assistant" ? "ARCHITECT" : message.role}
          </span>
          {message.meta?.section && (
            <span style={{ fontSize: 7, color: "#374151", background: "#1e293b", borderRadius: 3, padding: "1px 5px" }}>
              {message.meta.section}
            </span>
          )}
          {message.meta?.output && (
            <span style={{ fontSize: 7, color: "#10b981", background: "#052e16", borderRadius: 3, padding: "1px 5px" }}>
              {message.meta.output}
            </span>
          )}
          {message.meta?.planner && (
            <span style={{ fontSize: 7, color: "#f59e0b", background: "#1c1007", borderRadius: 3, padding: "1px 5px" }}>
              PLANNER
            </span>
          )}
        </div>
        <span style={{ fontSize: 8, color: "#374151" }}>{message.timestamp}</span>
      </div>
      <div style={{ fontSize: 11, color: "#94a3b8", lineHeight: 1.7, whiteSpace: "pre-wrap" }}>
        {message.content}
      </div>
    </div>
  );
}
