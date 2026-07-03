import { useState, useEffect, useRef } from "react";

const SYSTEM_PROMPT = `You are the ARCHITECT AGENT — an autonomous orchestrator for building products, campaigns, and systems from scratch.

You operate in 5 zones: Entry, Pipeline (13 sections across Discovery/Commercial/Compliance/Engineering), Support Agents, Planner Phase (A-J), Outputs (plan.md/spec.md/prompt.md).

CRITICAL: Be concise. Bullets over prose. No preamble. Target 150-300 words per section step unless the founder explicitly requests depth. Quality > length.

For each section, run 4 steps: Brief Writer (curated context), Section Agent (artifact), Injector (contradiction check), Tracker (state save).

Pause at FOUNDER_QUESTION blocks (S04 Monetisation) and Planner Step H (Approval Gate). Run legal scan on flagged sections.

Founder: Stefan. Products: The Plug AI, BigHeart Health. Stack: Claude, Canva, Google Drive.`;

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
  "A. GSD Discuss", "B. Extract Blueprint", "B-Legal. Legal Synthesis",
  "C. Write Tasks", "D. Self-review", "E. Master Spec",
  "F. Executor Prompt", "G. Cost Estimate", "H. Founder Approval ⚠️",
  "I. Checkpoint Write", "J. Memory Record",
];

// ROUGH token estimator: 1 token ≈ 4 chars
const estimateTokens = (text) => Math.ceil((text || "").length / 4);

export default function ArchitectAgent() {
  const [phase, setPhase] = useState("entry");
  const [mode, setMode] = useState(null);
  const [pipelineMode, setPipelineMode] = useState(null);
  const [activeSections, setActiveSections] = useState([]);
  const [sectionStatus, setSectionStatus] = useState({});
  const [sectionOutputs, setSectionOutputs] = useState({}); // { S01: { briefWriter: "...", sectionAgent: "...", injector: "...", tracker: "..." } }
  const [currentSection, setCurrentSection] = useState(null);
  const [plannerStep, setPlannerStep] = useState(0);
  const [plannerOutputs, setPlannerOutputs] = useState({});
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState("");
  const [loading, setLoading] = useState(false);
  const [paused, setPaused] = useState(false);
  const [pauseReason, setPauseReason] = useState("");
  const [outputs, setOutputs] = useState({ plan: "", spec: "", prompt: "" });
  const [stateLog, setStateLog] = useState([]);
  const [tokensUsed, setTokensUsed] = useState(0);
  const [viewingSection, setViewingSection] = useState(null); // For navigating back to a previous section
  const [showDownloadPanel, setShowDownloadPanel] = useState(false);
  const messagesEndRef = useRef(null);

  useEffect(() => {
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [messages]);

  const addMessage = (role, content, meta = {}) => {
    const msg = { role, content, meta, timestamp: new Date().toLocaleTimeString(), id: Date.now() + Math.random() };
    setMessages((prev) => [...prev, msg]);
    return msg;
  };

  /**
   * TOKEN-OPTIMIZED CALL
   * Instead of sending full conversation history, we build a minimal context:
   * - System prompt (always)
   * - Summary of completed sections (compressed)
   * - Current section's prior steps only
   * - User message
   */
  const callClaude = async (userMessage, options = {}) => {
    setLoading(true);
    try {
      const { sectionId, stepName, isFreeChat, isPlanner } = options;
      const msgs = [];

      // For freeform chat, send recent context window only (last 6 messages)
      if (isFreeChat) {
        const recent = messages.slice(-6).filter(m => m.role !== "system");
        recent.forEach(m => msgs.push({ role: m.role, content: m.content }));
        msgs.push({ role: "user", content: userMessage });
      }
      // For section step execution, send compressed prior-section summaries + current section's prior steps
      else if (sectionId) {
        const priorSummary = buildPriorSectionSummary(sectionId);
        const currentSectionContext = buildCurrentSectionContext(sectionId);
        const contextBlock = `PRIOR SECTIONS (summary):\n${priorSummary}\n\nCURRENT SECTION (${sectionId}) progress:\n${currentSectionContext}`;
        msgs.push({ role: "user", content: `${contextBlock}\n\n---\n\nTASK: ${userMessage}` });
      }
      // For planner phase, send all section trackers (already compressed) only
      else if (isPlanner) {
        const allTrackers = activeSections
          .map(s => sectionOutputs[s.id]?.tracker ? `${s.id} ${s.name}:\n${sectionOutputs[s.id].tracker}` : null)
          .filter(Boolean)
          .join("\n\n");
        msgs.push({ role: "user", content: `SECTION TRACKERS:\n${allTrackers}\n\n---\n\nTASK: ${userMessage}` });
      } else {
        msgs.push({ role: "user", content: userMessage });
      }

      // Track input tokens (rough)
      const inputTokens = msgs.reduce((sum, m) => sum + estimateTokens(m.content), 0) + estimateTokens(SYSTEM_PROMPT);

      const res = await fetch("https://api.anthropic.com/v1/messages", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          model: "claude-sonnet-4-20250514",
          max_tokens: 1000,
          system: SYSTEM_PROMPT,
          messages: msgs,
        }),
      });
      const data = await res.json();
      const reply = data.content?.[0]?.text || "No response";
      const outputTokens = estimateTokens(reply);
      setTokensUsed(prev => prev + inputTokens + outputTokens);
      return reply;
    } catch (e) {
      return "Error calling Architect Agent. Check connection.";
    } finally {
      setLoading(false);
    }
  };

  // Build a compressed summary of completed sections (Tracker output only — that IS the compressed state)
  const buildPriorSectionSummary = (currentId) => {
    const currentIdx = activeSections.findIndex(s => s.id === currentId);
    if (currentIdx <= 0) return "(none — this is the first section)";
    return activeSections.slice(0, currentIdx)
      .map(s => {
        const tracker = sectionOutputs[s.id]?.tracker;
        if (!tracker) return `${s.id} ${s.name}: (skipped)`;
        // Truncate tracker to ~80 words
        const words = tracker.split(/\s+/).slice(0, 80).join(" ");
        return `${s.id} ${s.name}: ${words}${tracker.split(/\s+/).length > 80 ? "..." : ""}`;
      })
      .join("\n");
  };

  // Build context for the current section: include prior steps within this section
  const buildCurrentSectionContext = (sectionId) => {
    const out = sectionOutputs[sectionId];
    if (!out) return "(no prior steps yet)";
    const steps = [];
    if (out.briefWriter) steps.push(`Brief Writer:\n${out.briefWriter}`);
    if (out.sectionAgent) steps.push(`Section Agent:\n${out.sectionAgent}`);
    if (out.injector) steps.push(`Injector:\n${out.injector}`);
    return steps.length ? steps.join("\n\n") : "(no prior steps yet)";
  };

  const startSession = async (selectedMode) => {
    setMode(selectedMode);
    const modeMap = { new: "NEW project", continue: "CONTINUE (resume)", add: "ADD to existing" };
    addMessage("system", `Mode selected: ${modeMap[selectedMode]}`);
    const reply = await callClaude(
      `Founder selected ${modeMap[selectedMode]}. Run ECC skills check (one line) and ask which pipeline: Full (13), Lite (6), or Custom. Keep response under 80 words.`,
      { isFreeChat: true }
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
      `Pipeline ${selected} loaded. Start S01: Problem & Vision. Ask Stefan for project name and core problem statement. Under 60 words.`,
      { isFreeChat: true }
    );
    addMessage("assistant", reply);
    setCurrentSection("S01");
    setViewingSection("S01");
    setPhase("pipeline");
  };

  const STEP_KEY = {
    "Brief Writer": "briefWriter",
    "Section Agent": "sectionAgent",
    "Injector": "injector",
    "Tracker": "tracker",
  };

  const runSectionStep = async (sectionId, stepName, isRerun = false) => {
    const section = activeSections.find((s) => s.id === sectionId);
    if (!section) return;

    const stepPrompts = {
      "Brief Writer": `Prepare a brief context summary for ${sectionId} ${section.name}. List: scope, key questions to resolve, dependencies on prior sections. Bullets only. Under 120 words.`,
      "Section Agent": `Generate the section artifact for ${sectionId} ${section.name}. Output structured deliverable with clear headings. Concise. Target 200-300 words.`,
      "Injector": `Run contradiction check for ${sectionId} against prior sections. Flag any conflicts. If none: "No contradictions detected." Under 80 words.`,
      "Tracker": `Record final state for ${sectionId}. Output: (1) key decisions (3-5 bullets), (2) artifacts produced, (3) legal scan flags if any, (4) open questions. THIS BECOMES THE COMPRESSED STATE for future sections — be precise and tight. Under 150 words.`,
    };

    const reply = await callClaude(stepPrompts[stepName], { sectionId, stepName });
    addMessage("assistant", reply, { section: sectionId, step: stepName, rerun: isRerun });

    // Save step output
    setSectionOutputs(prev => ({
      ...prev,
      [sectionId]: { ...prev[sectionId], [STEP_KEY[stepName]]: reply },
    }));

    if (stepName === "Tracker" && !isRerun) {
      setSectionStatus((prev) => ({ ...prev, [sectionId]: "complete" }));
      setStateLog((prev) => [...prev, { section: sectionId, name: section.name, timestamp: new Date().toLocaleTimeString() }]);
      const idx = activeSections.findIndex((s) => s.id === sectionId);
      if (idx < activeSections.length - 1) {
        const next = activeSections[idx + 1];
        setCurrentSection(next.id);
        setViewingSection(next.id);
        if (next.founderPause) {
          setPaused(true);
          setPauseReason(`FOUNDER_QUESTION block before ${next.id}: ${next.name}`);
        }
      } else {
        setPhase("planner");
        const reply2 = await callClaude(
          "All sections complete. Begin Zone 4 Planner Step A: GSD Discuss — align scope and constraints. Under 200 words.",
          { isPlanner: true }
        );
        addMessage("assistant", reply2, { planner: true, plannerStep: 0 });
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
    const reply = await callClaude(userMsg, { isFreeChat: true });
    addMessage("assistant", reply);
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
      `Execute Planner Step ${stepName}. Be specific. Under 250 words.`,
      { isPlanner: true }
    );
    setPlannerOutputs(prev => ({ ...prev, [stepName]: reply }));
    addMessage("assistant", reply, { plannerStep: next, planner: true });
  };

  const generateOutputs = async () => {
    addMessage("system", "Generating Zone 5 outputs...");
    const planReply = await callClaude(
      "Generate plan.md — phased implementation plan: phases, milestones, dependencies, build order. Markdown. Under 600 words.",
      { isPlanner: true }
    );
    setOutputs((prev) => ({ ...prev, plan: planReply }));
    addMessage("assistant", planReply, { output: "plan.md" });

    const specReply = await callClaude(
      "Generate spec.md — master engineering specification: architecture, data, interfaces, contracts, requirements. Markdown. Under 800 words.",
      { isPlanner: true }
    );
    setOutputs((prev) => ({ ...prev, spec: specReply }));
    addMessage("assistant", specReply, { output: "spec.md" });

    const promptReply = await callClaude(
      "Generate prompt.md — self-contained executor prompt: full context, constraints, acceptance criteria. A cold session executes from this alone. Markdown. Under 700 words.",
      { isPlanner: true }
    );
    setOutputs((prev) => ({ ...prev, prompt: promptReply }));
    addMessage("assistant", promptReply, { output: "prompt.md" });
  };

  const resetAll = () => {
    if (!confirm("Reset everything? All session data will be lost.")) return;
    setPhase("entry"); setMode(null); setPipelineMode(null);
    setActiveSections([]); setSectionStatus({}); setSectionOutputs({});
    setCurrentSection(null); setViewingSection(null); setPlannerStep(0); setPlannerOutputs({});
    setMessages([]); setInput(""); setLoading(false);
    setPaused(false); setPauseReason("");
    setOutputs({ plan: "", spec: "", prompt: "" });
    setStateLog([]); setTokensUsed(0); setShowDownloadPanel(false);
  };

  const getStatusColor = (status) => {
    if (status === "complete") return "#10b981";
    if (status === "active") return "#f59e0b";
    return "#374151";
  };

  // === DOWNLOAD HELPERS ===
  const download = (filename, content) => {
    const blob = new Blob([content], { type: "text/markdown" });
    const url = URL.createObjectURL(blob);
    const a = document.createElement("a");
    a.href = url; a.download = filename; a.click();
    URL.revokeObjectURL(url);
  };

  const buildSectionMd = (sectionId) => {
    const section = activeSections.find(s => s.id === sectionId);
    const out = sectionOutputs[sectionId] || {};
    return `# ${sectionId} — ${section?.name}\n\nZone: ${section?.zone}\nStatus: ${sectionStatus[sectionId] || "pending"}\n\n## Brief Writer\n${out.briefWriter || "(not run)"}\n\n## Section Agent\n${out.sectionAgent || "(not run)"}\n\n## Injector\n${out.injector || "(not run)"}\n\n## Tracker\n${out.tracker || "(not run)"}\n`;
  };

  const buildStateMd = () => {
    const lines = ["# 00-state.md", "", `Generated: ${new Date().toISOString()}`, `Pipeline: ${pipelineMode}`, `Tokens used (approx): ${tokensUsed.toLocaleString()}`, "", "## Section Status", ""];
    activeSections.forEach(s => {
      lines.push(`- ${s.id} ${s.name}: ${sectionStatus[s.id] || "pending"}`);
    });
    lines.push("", "## Completion Log", "");
    stateLog.forEach(l => lines.push(`- ${l.timestamp} — ${l.section} ${l.name}`));
    return lines.join("\n");
  };

  const buildTranscriptMd = () => {
    return `# Conversation Transcript\n\n${messages.map(m => `**${m.role.toUpperCase()}** [${m.timestamp}]${m.meta?.section ? ` (${m.meta.section}${m.meta.step ? ` · ${m.meta.step}` : ""})` : ""}${m.meta?.output ? ` (${m.meta.output})` : ""}\n\n${m.content}\n\n---\n`).join("\n")}`;
  };

  const buildBundle = () => {
    let bundle = "# Architect Agent — Full Session Bundle\n\n";
    bundle += buildStateMd() + "\n\n---\n\n";
    activeSections.forEach(s => {
      if (sectionOutputs[s.id]) {
        bundle += buildSectionMd(s.id) + "\n---\n\n";
      }
    });
    if (Object.keys(plannerOutputs).length) {
      bundle += "# Planner Phase\n\n";
      Object.entries(plannerOutputs).forEach(([k, v]) => {
        bundle += `## ${k}\n\n${v}\n\n`;
      });
      bundle += "---\n\n";
    }
    if (outputs.plan) bundle += `# plan.md\n\n${outputs.plan}\n\n---\n\n`;
    if (outputs.spec) bundle += `# spec.md\n\n${outputs.spec}\n\n---\n\n`;
    if (outputs.prompt) bundle += `# prompt.md\n\n${outputs.prompt}\n\n`;
    return bundle;
  };

  // What's currently being viewed (when navigating back)
  const viewingIsLive = viewingSection === currentSection;
  const viewingData = viewingSection ? sectionOutputs[viewingSection] : null;
  const viewingMeta = viewingSection ? activeSections.find(s => s.id === viewingSection) : null;

  return (
    <div style={{
      background: "#0a0a0f", minHeight: "100vh",
      fontFamily: "'JetBrains Mono', 'Courier New', monospace",
      color: "#e2e8f0", display: "flex", flexDirection: "column",
    }}>
      {/* Header */}
      <div style={{
        background: "linear-gradient(135deg, #0f0f1a 0%, #1a0a2e 100%)",
        borderBottom: "1px solid #1e293b", padding: "12px 18px",
        display: "flex", alignItems: "center", justifyContent: "space-between", flexShrink: 0,
      }}>
        <div style={{ display: "flex", alignItems: "center", gap: 12 }}>
          <div style={{
            width: 32, height: 32, background: "linear-gradient(135deg, #7c3aed, #3b82f6)",
            borderRadius: 8, display: "flex", alignItems: "center", justifyContent: "center",
            fontSize: 15, flexShrink: 0,
          }}>⚡</div>
          <div>
            <div style={{ fontSize: 13, fontWeight: 700, letterSpacing: "0.08em", color: "#c4b5fd" }}>/architect</div>
            <div style={{ fontSize: 9, color: "#64748b", letterSpacing: "0.12em" }}>BLUEPRINT TO BUILD · STEFAN'S WORKSPACE</div>
          </div>
        </div>
        <div style={{ display: "flex", gap: 12, alignItems: "center" }}>
          {/* Token meter */}
          <div style={{
            background: "#0f0f1a", border: "1px solid #1e293b", borderRadius: 4,
            padding: "4px 10px", display: "flex", alignItems: "center", gap: 6,
          }}>
            <span style={{ fontSize: 8, color: "#475569", letterSpacing: "0.1em" }}>TOKENS</span>
            <span style={{ fontSize: 11, color: tokensUsed > 20000 ? "#f59e0b" : "#10b981", fontWeight: 700 }}>
              {tokensUsed.toLocaleString()}
            </span>
          </div>
          {/* Phase pips */}
          <div style={{ display: "flex", gap: 4, alignItems: "center" }}>
            {["entry", "pipeline", "planner", "outputs"].map((p, i) => (
              <div key={p} style={{ display: "flex", alignItems: "center", gap: 3 }}>
                <div style={{
                  width: 7, height: 7, borderRadius: "50%",
                  background: phase === p ? "#7c3aed" : i < ["entry", "pipeline", "planner", "outputs"].indexOf(phase) ? "#10b981" : "#1e293b",
                  boxShadow: phase === p ? "0 0 8px #7c3aed" : "none",
                }} />
                <span style={{ fontSize: 8, color: phase === p ? "#c4b5fd" : "#475569", textTransform: "uppercase", letterSpacing: "0.08em" }}>{p}</span>
                {i < 3 && <span style={{ color: "#1e293b", fontSize: 9 }}>→</span>}
              </div>
            ))}
          </div>
          {/* Downloads always available */}
          {messages.length > 0 && (
            <button onClick={() => setShowDownloadPanel(true)} style={{
              background: "#10b981", border: "none", borderRadius: 4,
              padding: "5px 12px", color: "white", fontSize: 9,
              cursor: "pointer", fontWeight: 700, letterSpacing: "0.08em",
            }}>
              ⬇ DOWNLOAD
            </button>
          )}
          {phase !== "entry" && (
            <button onClick={resetAll} style={{
              background: "transparent", border: "1px solid #374151", borderRadius: 4,
              padding: "5px 10px", color: "#64748b", fontSize: 9,
              cursor: "pointer", letterSpacing: "0.08em",
            }}>RESET</button>
          )}
        </div>
      </div>

      <div style={{ display: "flex", flex: 1, overflow: "hidden" }}>
        {/* Left Sidebar — Navigable */}
        <div style={{
          width: 230, background: "#0d0d18", borderRight: "1px solid #1e293b",
          overflowY: "auto", padding: "12px 10px", flexShrink: 0,
        }}>
          <div style={{ fontSize: 8, color: "#475569", letterSpacing: "0.15em", marginBottom: 8, textTransform: "uppercase" }}>
            Pipeline · Click to View
          </div>

          {activeSections.length === 0 ? (
            <div style={{ fontSize: 10, color: "#374151", textAlign: "center", marginTop: 20 }}>
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
              <div key={zone} style={{ marginBottom: 12 }}>
                <div style={{
                  fontSize: 7, letterSpacing: "0.15em", textTransform: "uppercase",
                  color: ZONE_COLORS[zone], marginBottom: 4,
                  borderLeft: `2px solid ${ZONE_COLORS[zone]}`, paddingLeft: 6,
                }}>
                  {zone}
                </div>
                {sections.map((s) => {
                  const isViewing = viewingSection === s.id;
                  const isCurrent = currentSection === s.id;
                  const hasData = sectionOutputs[s.id];
                  return (
                    <div key={s.id} style={{
                      display: "flex", alignItems: "center", gap: 5,
                      padding: "4px 7px", borderRadius: 4, marginBottom: 2,
                      background: isViewing ? "#1a1a2e" : "transparent",
                      border: isViewing ? "1px solid #7c3aed" : isCurrent ? "1px solid #3b82f6" : "1px solid transparent",
                      cursor: hasData ? "pointer" : "default",
                      transition: "all 0.15s",
                      opacity: hasData || isCurrent ? 1 : 0.6,
                    }} onClick={() => hasData && setViewingSection(s.id)}>
                      <div style={{
                        width: 5, height: 5, borderRadius: "50%", flexShrink: 0,
                        background: getStatusColor(sectionStatus[s.id]),
                        boxShadow: sectionStatus[s.id] === "complete" ? "0 0 5px #10b981" : "none",
                      }} />
                      <span style={{ fontSize: 8, color: isViewing ? "#c4b5fd" : "#64748b", flexShrink: 0 }}>{s.id}</span>
                      <span style={{ fontSize: 8, color: isViewing ? "#cbd5e1" : "#475569", flex: 1, lineHeight: 1.3 }}>
                        {s.name}
                      </span>
                      {isCurrent && <span style={{ fontSize: 7, color: "#3b82f6" }}>●</span>}
                      {s.required && <span style={{ fontSize: 6, color: "#ef4444" }}>REQ</span>}
                      {s.stronglyRecommended && <span style={{ fontSize: 6, color: "#f59e0b" }}>REC</span>}
                    </div>
                  );
                })}
              </div>
            ))
          )}

          {stateLog.length > 0 && (
            <div style={{ marginTop: 12 }}>
              <div style={{ fontSize: 8, color: "#475569", letterSpacing: "0.12em", marginBottom: 5, textTransform: "uppercase" }}>
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
            <div style={{ marginTop: 12 }}>
              <div style={{ fontSize: 8, color: "#475569", letterSpacing: "0.12em", marginBottom: 5, textTransform: "uppercase" }}>
                Planner Phase
              </div>
              {PLANNER_STEPS.map((step, i) => (
                <div key={i} style={{
                  fontSize: 8, padding: "3px 7px", marginBottom: 2, borderRadius: 3,
                  background: i === plannerStep ? "#1a1a2e" : "transparent",
                  color: i < plannerStep ? "#10b981" : i === plannerStep ? "#f59e0b" : "#374151",
                  borderLeft: i === plannerStep ? "2px solid #f59e0b" : "2px solid transparent",
                }}>
                  {i < plannerStep ? "✓ " : i === plannerStep ? "→ " : "  "}{step}
                </div>
              ))}
            </div>
          )}
        </div>

        {/* Main Area */}
        <div style={{ flex: 1, display: "flex", flexDirection: "column", overflow: "hidden" }}>
          {/* Entry */}
          {phase === "entry" && (
            <div style={{ flex: 1, display: "flex", flexDirection: "column", alignItems: "center", justifyContent: "center", gap: 24, padding: 28 }}>
              <div style={{ textAlign: "center" }}>
                <div style={{ fontSize: 10, color: "#7c3aed", letterSpacing: "0.3em", textTransform: "uppercase", marginBottom: 6 }}>
                  ARCHITECT AGENT v2
                </div>
                <div style={{ fontSize: 26, fontWeight: 800, color: "#e2e8f0", letterSpacing: "-0.02em", marginBottom: 4 }}>
                  Blueprint to Build
                </div>
                <div style={{ fontSize: 11, color: "#64748b" }}>
                  Token-optimized · Navigable · Downloadable anytime
                </div>
              </div>
              <div style={{ display: "flex", gap: 14 }}>
                {[
                  { id: "new", label: "NEW", sub: "project", tokens: "~3.8k tokens", time: "3-5 min", color: "#7c3aed" },
                  { id: "continue", label: "CONTINUE", sub: "resume", tokens: "~1.2k tokens", time: "1-2 min", color: "#3b82f6" },
                  { id: "add", label: "ADD", sub: "to existing", tokens: "~2.0k tokens", time: "2-4 min", color: "#10b981" },
                ].map((m) => (
                  <button key={m.id} onClick={() => startSession(m.id)} disabled={loading} style={{
                    background: "transparent", border: `1px solid ${m.color}`, borderRadius: 8,
                    padding: "16px 22px", cursor: loading ? "not-allowed" : "pointer",
                    color: m.color, textAlign: "center", transition: "all 0.2s", minWidth: 130,
                    opacity: loading ? 0.5 : 1,
                  }}
                    onMouseEnter={e => { if (!loading) e.currentTarget.style.background = m.color + "22"; }}
                    onMouseLeave={e => { e.currentTarget.style.background = "transparent"; }}
                  >
                    <div style={{ fontSize: 15, fontWeight: 700, letterSpacing: "0.1em" }}>{m.label}</div>
                    <div style={{ fontSize: 10, opacity: 0.7, marginTop: 2 }}>{m.sub}</div>
                    <div style={{ fontSize: 9, marginTop: 6, color: "#64748b" }}>{m.tokens}</div>
                    <div style={{ fontSize: 9, color: "#64748b" }}>{m.time}</div>
                  </button>
                ))}
              </div>
              {loading && <LoadingDot />}
            </div>
          )}

          {/* Mode select */}
          {phase === "mode-select" && (
            <div style={{ flex: 1, display: "flex", flexDirection: "column", overflow: "hidden" }}>
              <div style={{ flex: 1, overflowY: "auto", padding: "12px 18px" }}>
                {messages.map((m) => <MessageBubble key={m.id} message={m} />)}
                {loading && <LoadingDot />}
                <div ref={messagesEndRef} />
              </div>
              <div style={{ borderTop: "1px solid #1e293b", padding: "12px 18px", display: "flex", flexDirection: "column", gap: 10, background: "#0d0d18" }}>
                <div style={{ fontSize: 10, color: "#64748b", textAlign: "center" }}>Select Pipeline Mode:</div>
                <div style={{ display: "flex", gap: 10, justifyContent: "center" }}>
                  {[
                    { id: "full", label: "FULL", sections: "13 sections", tokens: "~28k tokens", time: "35-55 min" },
                    { id: "lite", label: "LITE", sections: "6 sections", tokens: "~14k tokens", time: "18-30 min" },
                  ].map((p) => (
                    <button key={p.id} onClick={() => selectPipeline(p.id)} disabled={loading} style={{
                      background: "transparent", border: "1px solid #7c3aed", borderRadius: 6,
                      padding: "10px 16px", cursor: loading ? "not-allowed" : "pointer", color: "#c4b5fd",
                      opacity: loading ? 0.5 : 1,
                    }}>
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
                  padding: "8px 18px", display: "flex", alignItems: "center", justifyContent: "space-between", flexShrink: 0,
                }}>
                  <div style={{ display: "flex", alignItems: "center", gap: 8 }}>
                    <span style={{ fontSize: 13 }}>⚠️</span>
                    <div>
                      <div style={{ fontSize: 10, color: "#fca5a5", fontWeight: 700, letterSpacing: "0.08em" }}>PAUSED — FOUNDER ACTION REQUIRED</div>
                      <div style={{ fontSize: 9, color: "#f87171" }}>{pauseReason}</div>
                    </div>
                  </div>
                  <button onClick={() => { setPaused(false); setPauseReason(""); addMessage("system", "Pause resolved."); }} style={{
                    background: "#ef4444", border: "none", borderRadius: 4, padding: "5px 10px",
                    color: "white", fontSize: 9, cursor: "pointer", fontWeight: 700,
                  }}>APPROVE & CONTINUE</button>
                </div>
              )}

              {/* Navigation banner — when viewing a non-current section */}
              {viewingSection && !viewingIsLive && phase === "pipeline" && (
                <div style={{
                  background: "#1a1a2e", borderBottom: "1px solid #7c3aed",
                  padding: "8px 18px", display: "flex", alignItems: "center", justifyContent: "space-between", flexShrink: 0,
                }}>
                  <div style={{ fontSize: 10, color: "#c4b5fd" }}>
                    👁 Viewing <strong>{viewingSection} · {viewingMeta?.name}</strong> (read-only)
                  </div>
                  <div style={{ display: "flex", gap: 6 }}>
                    <button onClick={() => download(`${viewingSection}.md`, buildSectionMd(viewingSection))} style={{
                      background: "transparent", border: "1px solid #10b981", borderRadius: 3,
                      padding: "3px 8px", color: "#10b981", fontSize: 9, cursor: "pointer", fontWeight: 700,
                    }}>⬇ {viewingSection}.md</button>
                    <button onClick={() => setViewingSection(currentSection)} style={{
                      background: "#7c3aed", border: "none", borderRadius: 3,
                      padding: "3px 8px", color: "white", fontSize: 9, cursor: "pointer", fontWeight: 700,
                    }}>→ BACK TO LIVE ({currentSection})</button>
                  </div>
                </div>
              )}

              {/* Content area — either live chat OR section view */}
              <div style={{ flex: 1, overflowY: "auto", padding: "14px 18px" }}>
                {viewingSection && !viewingIsLive && phase === "pipeline" ? (
                  <SectionView sectionId={viewingSection} sectionMeta={viewingMeta} data={viewingData} onRerun={(step) => runSectionStep(viewingSection, step, true)} loading={loading} />
                ) : (
                  <>
                    {messages.map((m) => <MessageBubble key={m.id} message={m} />)}
                    {loading && <LoadingDot />}
                  </>
                )}
                <div ref={messagesEndRef} />
              </div>

              {/* Pipeline action bar */}
              {phase === "pipeline" && currentSection && viewingIsLive && (
                <div style={{
                  borderTop: "1px solid #1e293b", padding: "8px 18px",
                  background: "#0d0d18", display: "flex", gap: 6, flexWrap: "wrap", alignItems: "center", flexShrink: 0,
                }}>
                  {["Brief Writer", "Section Agent", "Injector", "Tracker"].map((step) => {
                    const done = sectionOutputs[currentSection]?.[STEP_KEY[step]];
                    return (
                      <button key={step} onClick={() => runSectionStep(currentSection, step)} disabled={loading || paused} style={{
                        background: done ? "#052e16" : "transparent",
                        border: `1px solid ${done ? "#10b981" : "#1e293b"}`,
                        borderRadius: 4, padding: "5px 10px",
                        color: loading || paused ? "#374151" : done ? "#10b981" : "#64748b",
                        fontSize: 9, cursor: loading || paused ? "not-allowed" : "pointer", letterSpacing: "0.04em",
                      }}>
                        {done ? "✓ " : "▶ "}{step}
                      </button>
                    );
                  })}
                  <div style={{ flex: 1 }} />
                  <span style={{ fontSize: 9, color: "#475569" }}>
                    {currentSection} — {activeSections.find(s => s.id === currentSection)?.name}
                  </span>
                </div>
              )}

              {/* Planner action bar */}
              {phase === "planner" && (
                <div style={{
                  borderTop: "1px solid #1e293b", padding: "8px 18px",
                  background: "#0d0d18", display: "flex", gap: 8, alignItems: "center", flexShrink: 0,
                }}>
                  <button onClick={advancePlanner} disabled={loading || paused} style={{
                    background: loading || paused ? "#374151" : "#7c3aed", border: "none", borderRadius: 4,
                    padding: "7px 14px", color: "white", fontSize: 10,
                    cursor: loading || paused ? "not-allowed" : "pointer", fontWeight: 700,
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
            width: 210, background: "#0d0d18", borderLeft: "1px solid #1e293b",
            overflowY: "auto", padding: "12px 10px", flexShrink: 0,
          }}>
            <div style={{ fontSize: 8, color: "#475569", letterSpacing: "0.12em", marginBottom: 8, textTransform: "uppercase" }}>
              Zone 5 Outputs
            </div>
            {["plan", "spec", "prompt"].map((doc) => (
              <div key={doc} style={{
                background: "#0f0f1a", border: `1px solid ${outputs[doc] ? "#10b981" : "#1e293b"}`,
                borderRadius: 5, padding: "8px 10px", marginBottom: 6,
              }}>
                <div style={{ display: "flex", justifyContent: "space-between", alignItems: "center" }}>
                  <div style={{ fontSize: 9, color: outputs[doc] ? "#10b981" : "#374151", fontWeight: 700, letterSpacing: "0.08em" }}>
                    {outputs[doc] ? "✓" : "○"} {doc}.md
                  </div>
                  {outputs[doc] && (
                    <button onClick={() => download(`${doc}.md`, outputs[doc])} style={{
                      background: "transparent", border: "1px solid #10b981", borderRadius: 3,
                      padding: "1px 5px", color: "#10b981", fontSize: 8, cursor: "pointer",
                    }}>⬇</button>
                  )}
                </div>
                {outputs[doc] && (
                  <div style={{ fontSize: 8, color: "#64748b", marginTop: 3, lineHeight: 1.4 }}>
                    {outputs[doc].substring(0, 70)}...
                  </div>
                )}
              </div>
            ))}

            {/* Progress */}
            {activeSections.length > 0 && (
              <div style={{ marginTop: 14 }}>
                <div style={{ fontSize: 8, color: "#475569", letterSpacing: "0.12em", marginBottom: 5, textTransform: "uppercase" }}>
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
                  {Object.values(sectionStatus).filter(s => s === "complete").length}/{activeSections.length} sections · {tokensUsed.toLocaleString()} tokens
                </div>
              </div>
            )}
          </div>
        )}
      </div>

      {/* Download Panel Modal */}
      {showDownloadPanel && (
        <div style={{
          position: "fixed", inset: 0, background: "rgba(0,0,0,0.8)",
          display: "flex", alignItems: "center", justifyContent: "center", zIndex: 100,
        }} onClick={() => setShowDownloadPanel(false)}>
          <div style={{
            background: "#0d0d18", border: "1px solid #7c3aed", borderRadius: 8,
            padding: "20px", maxWidth: 560, width: "90%", maxHeight: "80vh", overflowY: "auto",
          }} onClick={e => e.stopPropagation()}>
            <div style={{ display: "flex", justifyContent: "space-between", alignItems: "center", marginBottom: 16 }}>
              <div>
                <div style={{ fontSize: 14, fontWeight: 700, color: "#c4b5fd", letterSpacing: "0.08em" }}>DOWNLOAD CENTER</div>
                <div style={{ fontSize: 9, color: "#64748b", marginTop: 2 }}>Anything available at this moment in the session</div>
              </div>
              <button onClick={() => setShowDownloadPanel(false)} style={{
                background: "transparent", border: "1px solid #374151", borderRadius: 4,
                padding: "4px 10px", color: "#64748b", fontSize: 10, cursor: "pointer",
              }}>✕ CLOSE</button>
            </div>

            {/* Bundle */}
            <div style={{ marginBottom: 14 }}>
              <div style={{ fontSize: 9, color: "#475569", letterSpacing: "0.12em", marginBottom: 6, textTransform: "uppercase" }}>Full Bundle</div>
              <button onClick={() => download("architect-session-bundle.md", buildBundle())} style={{
                width: "100%", background: "#7c3aed", border: "none", borderRadius: 5,
                padding: "10px", color: "white", fontSize: 11, cursor: "pointer", fontWeight: 700,
                textAlign: "left",
              }}>
                ⬇ architect-session-bundle.md
                <div style={{ fontSize: 8, opacity: 0.8, marginTop: 2, fontWeight: 400 }}>Everything: state + all sections + planner + outputs</div>
              </button>
            </div>

            {/* State */}
            {activeSections.length > 0 && (
              <div style={{ marginBottom: 14 }}>
                <div style={{ fontSize: 9, color: "#475569", letterSpacing: "0.12em", marginBottom: 6, textTransform: "uppercase" }}>State</div>
                <button onClick={() => download("00-state.md", buildStateMd())} style={downloadRowStyle}>
                  <span>⬇ 00-state.md</span>
                  <span style={{ fontSize: 8, color: "#64748b" }}>{stateLog.length} entries</span>
                </button>
                <button onClick={() => download("transcript.md", buildTranscriptMd())} style={downloadRowStyle}>
                  <span>⬇ transcript.md</span>
                  <span style={{ fontSize: 8, color: "#64748b" }}>{messages.length} messages</span>
                </button>
              </div>
            )}

            {/* Sections */}
            {activeSections.some(s => sectionOutputs[s.id]) && (
              <div style={{ marginBottom: 14 }}>
                <div style={{ fontSize: 9, color: "#475569", letterSpacing: "0.12em", marginBottom: 6, textTransform: "uppercase" }}>Section Docs</div>
                {activeSections.filter(s => sectionOutputs[s.id]).map(s => (
                  <button key={s.id} onClick={() => download(`${s.id}.md`, buildSectionMd(s.id))} style={downloadRowStyle}>
                    <span>⬇ {s.id}.md — {s.name}</span>
                    <span style={{ fontSize: 8, color: sectionStatus[s.id] === "complete" ? "#10b981" : "#f59e0b" }}>
                      {sectionStatus[s.id] === "complete" ? "✓ complete" : "partial"}
                    </span>
                  </button>
                ))}
              </div>
            )}

            {/* Zone 5 outputs */}
            {Object.values(outputs).some(v => v) && (
              <div style={{ marginBottom: 14 }}>
                <div style={{ fontSize: 9, color: "#475569", letterSpacing: "0.12em", marginBottom: 6, textTransform: "uppercase" }}>Zone 5 Outputs</div>
                {["plan", "spec", "prompt"].filter(d => outputs[d]).map(d => (
                  <button key={d} onClick={() => download(`${d}.md`, outputs[d])} style={downloadRowStyle}>
                    <span>⬇ {d}.md</span>
                    <span style={{ fontSize: 8, color: "#10b981" }}>✓</span>
                  </button>
                ))}
              </div>
            )}

            <div style={{ fontSize: 8, color: "#475569", textAlign: "center", marginTop: 14, paddingTop: 10, borderTop: "1px solid #1e293b" }}>
              Tokens used (approx): {tokensUsed.toLocaleString()}
            </div>
          </div>
        </div>
      )}

      <style>{`
        @keyframes pulse { 0%, 100% { opacity: 1; } 50% { opacity: 0.3; } }
      `}</style>
    </div>
  );
}

const downloadRowStyle = {
  width: "100%", background: "#0f0f1a", border: "1px solid #1e293b", borderRadius: 4,
  padding: "8px 10px", color: "#cbd5e1", fontSize: 10, cursor: "pointer",
  display: "flex", justifyContent: "space-between", alignItems: "center",
  marginBottom: 3, fontFamily: "inherit",
};

function SectionView({ sectionId, sectionMeta, data, onRerun, loading }) {
  const steps = [
    { name: "Brief Writer", key: "briefWriter" },
    { name: "Section Agent", key: "sectionAgent" },
    { name: "Injector", key: "injector" },
    { name: "Tracker", key: "tracker" },
  ];
  return (
    <div>
      <div style={{ marginBottom: 14 }}>
        <div style={{ fontSize: 9, color: "#475569", letterSpacing: "0.12em", textTransform: "uppercase" }}>
          {sectionMeta?.zone}
        </div>
        <div style={{ fontSize: 18, fontWeight: 700, color: "#c4b5fd", marginTop: 2 }}>
          {sectionId} — {sectionMeta?.name}
        </div>
      </div>
      {steps.map(step => {
        const content = data?.[step.key];
        return (
          <div key={step.key} style={{
            background: "#0f0f1a", border: `1px solid ${content ? "#2d1b4e" : "#1e293b"}`,
            borderRadius: 6, padding: "12px 14px", marginBottom: 10,
          }}>
            <div style={{ display: "flex", justifyContent: "space-between", alignItems: "center", marginBottom: 8 }}>
              <div style={{ fontSize: 10, color: content ? "#c4b5fd" : "#374151", fontWeight: 700, letterSpacing: "0.1em" }}>
                {content ? "✓ " : "○ "}{step.name}
              </div>
              {content && (
                <button onClick={() => onRerun(step.name)} disabled={loading} style={{
                  background: "transparent", border: "1px solid #7c3aed", borderRadius: 3,
                  padding: "3px 8px", color: "#c4b5fd", fontSize: 9,
                  cursor: loading ? "not-allowed" : "pointer", opacity: loading ? 0.5 : 1, fontWeight: 700,
                }}>↻ RE-RUN</button>
              )}
            </div>
            <div style={{ fontSize: 11, color: content ? "#94a3b8" : "#374151", lineHeight: 1.7, whiteSpace: "pre-wrap" }}>
              {content || "(not run yet)"}
            </div>
          </div>
        );
      })}
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
          flex: 1, background: "#0f0f1a", border: "1px solid #1e293b", borderRadius: 5,
          padding: "9px 12px", color: "#e2e8f0", fontSize: 12, outline: "none", fontFamily: "inherit",
        }}
        onFocus={e => e.target.style.borderColor = "#7c3aed"}
        onBlur={e => e.target.style.borderColor = "#1e293b"}
      />
      <button onClick={onSend} disabled={loading || !input.trim()} style={{
        background: "#7c3aed", border: "none", borderRadius: 5,
        padding: "9px 18px", color: "white", fontSize: 11,
        cursor: loading || !input.trim() ? "not-allowed" : "pointer", fontWeight: 700,
        opacity: loading || !input.trim() ? 0.4 : 1,
      }}>SEND</button>
    </div>
  );
}

function LoadingDot() {
  return (
    <div style={{ display: "flex", gap: 6, padding: "10px 0", alignItems: "center" }}>
      <div style={{ width: 5, height: 5, borderRadius: "50%", background: "#7c3aed", animation: "pulse 1s infinite" }} />
      <div style={{ width: 5, height: 5, borderRadius: "50%", background: "#7c3aed", animation: "pulse 1s infinite", animationDelay: "0.2s" }} />
      <div style={{ width: 5, height: 5, borderRadius: "50%", background: "#7c3aed", animation: "pulse 1s infinite", animationDelay: "0.4s" }} />
      <span style={{ fontSize: 10, color: "#64748b", marginLeft: 4 }}>Architect processing...</span>
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
              {message.meta.section}{message.meta.step ? ` · ${message.meta.step}` : ""}
            </span>
          )}
          {message.meta?.rerun && (
            <span style={{ fontSize: 7, color: "#f59e0b", background: "#1c1007", borderRadius: 3, padding: "1px 5px" }}>RE-RUN</span>
          )}
          {message.meta?.output && (
            <span style={{ fontSize: 7, color: "#10b981", background: "#052e16", borderRadius: 3, padding: "1px 5px" }}>
              {message.meta.output}
            </span>
          )}
          {message.meta?.planner && (
            <span style={{ fontSize: 7, color: "#f59e0b", background: "#1c1007", borderRadius: 3, padding: "1px 5px" }}>PLANNER</span>
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
