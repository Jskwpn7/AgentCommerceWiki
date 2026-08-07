---
type: paper
title: "From Agent Traces to Trust: Evidence Tracing and Execution Provenance in LLM Agents"
arxiv: "2606.04990v1"
authors: "Yiqi Wang, Jiaqi Zhang, Taotao Cai, Zirui Liu, Qingqiang Sun, Zequn Sun, Zhangkai Wu, Mingkai Zhang, Yanming Zhu"
institution: "Griffith University, Jiangsu University, University of Southern Queensland, Peking University, Great Bay University, Nanjing University, Macquarie University, Southern University of Science and Technology"
venue: "arXiv preprint"
date: "2026-06-03"
category: "AI Safety / Agent Architecture / LLM Systems"
tags:
  - "llm-agents"
  - "provenance"
  - "traceability"
  - "tool-use-safety"
  - "memory-provenance"
  - "evidence-tracing"
  - "agent-observability"
  - "runtime-guardrails"
  - "trustworthy-ai"
status: "ingested"
source: "https://arxiv.org/abs/2606.04990v1"
source_type: "pdf"
---

# From Agent Traces to Trust: Evidence Tracing and Execution Provenance in LLM Agents

**Authors:** Yiqi Wang^1^, Jiaqi Zhang^2^, Taotao Cai^3^, Zirui Liu^4^, Qingqiang Sun^5^, Zequn Sun^6^, Zhangkai Wu^7^, Mingkai Zhang^8^, Yanming Zhu^1^
**Affiliations:** ^1^Griffith University, ^2^Jiangsu University, ^3^University of Southern Queensland, ^4^Peking University, ^5^Great Bay University, ^6^Nanjing University, ^7^Macquarie University, ^8^Southern University of Science and Technology
**arXiv:** 2606.04990v1 [cs.CR], 3 Jun 2026
**Date:** June 4, 2026

## Abstract

Large language model (LLM)-based agents increasingly solve complex tasks by interacting with external tools, retrieval systems, memory modules, environments, and other agents. While these capabilities expand agent autonomy, they also make agent behavior harder to verify, debug, and audit. Final-answer accuracy alone cannot explain how an output was produced, which evidence supported each claim, whether tool calls were justified, how memory influenced later decisions, or where execution failures originated. Evidence tracing and execution provenance address this gap by modeling how retrieved evidence, tool outputs, memory items, environment observations, intermediate claims, actions, and final answers are connected throughout agent execution. This survey provides a systematic review and conceptual framework for evidence tracing and execution provenance in LLM agents. We organize related work around a unified provenance perspective that connects retrieval grounding, claim support, tool-use safety, memory lineage, observability, debugging, audit, and recovery. We introduce a taxonomy covering trace sources, evidence and execution units, provenance relations, tracing granularity, tracing timing, representation forms, and trust functions. We then review key methodological directions, including provenance representation, evidence attribution, tool-use provenance, runtime guardrails, provenance-bearing memory, trace-based observability, and failure diagnosis. We further map existing benchmarks, datasets, and evaluation metrics to provenance-related capabilities, and discuss how evaluation can move from final-answer correctness toward process-level accountability. Finally, we outline open challenges, including unified trace schemas, claim-level and semantic provenance, provenance-aware safety mechanisms, realistic execution-trace benchmarks, recovery-oriented evaluation, and privacy-aware audit infrastructure for trustworthy LLM agents.

## Keywords
LLM Agents, Agent Traces, Evidence Tracing, Execution Provenance, Provenance Graphs, Tool-Use Safety, Memory Provenance, Agent Observability, Runtime Guardrails, Trustworthy AI

---

## 1. Introduction

LLM-based agents are emerging as a powerful paradigm for complex task execution. Unlike standalone language models that primarily generate textual responses, LLM agents can interact with external tools, retrieval systems, memory modules, environments, and other agents to solve multi-step tasks. Key works referenced: MRKL, Toolformer (external tool connection); ReAct and Tree-of-Thoughts (reasoning + acting); Reflexion (failure-based learning); Voyager, Generative Agents, AutoGen, CAMEL (long-term memory, multi-agent collaboration).

The shift marks a transition from passive response generation to action-oriented execution. As capabilities expand, execution contexts grow complex: agents may retrieve external documents, call APIs, write and execute code, interact with web/GUI environments, consult memory, communicate with other agents, and adapt plans. System-level references: ToolLLM (tool-use learning), AgentBench (interactive evaluation), WebArena (autonomous web interaction), τ-bench (tool-agent-user workflows).

**The accountability gap:** A final answer may depend on retrieved passages, tool outputs, memory items, environment observations, intermediate reasoning steps, and previous actions. When correct, the supporting evidence may remain unclear. When wrong, the failure may originate from retrieval, tool misuse, stale memory, unsafe instructions, inter-agent miscommunication, or invalid reasoning.

Recent studies illuminate this: ToolEmu (risky behavior from intermediate tool-use decisions), AgentDojo (robustness under adversarial instructions), TRAIL (trace-based failure localization), MAST (multi-agent failure modes). These suggest trustworthy systems need mechanisms to record, connect, and reason over evidence and execution steps.

**Two core definitions:**
- **Evidence tracing:** Mechanisms that identify, record, and connect evidence units that support, contradict, invalidate, or influence agent claims, decisions, and actions.
- **Execution provenance:** The broader structured representation of how an agent execution unfolds — retrieved documents, tool calls, parameters, observations, memory accesses, intermediate claims, actions, inter-agent messages, final outputs.

**Key references cited:** W3C PROV-DM (general provenance model), OpenTelemetry (distributed traces), AgentOps, AgentTrace (agent observability).

**Research threads surveyed:**
1. RAG & evidence-based generation (ALCE, FActScore, RAGAS, ARES, RAGChecker, RAGTruth, SourceCheckup, Self-RAG) — focus on document-to-answer attribution
2. Tool-use safety (ToolEmu, InjecAgent, AgentDojo, CaMeL, Fides, NeuroTaint, AgentSpec, AgentSentry, AgentBound) — focus on execution-level control
3. Memory provenance complexity — memory as evidence source, not passive storage
4. Graph-based representations — natural substrate for dependency modeling
5. Agent observability & debugging (AgentOps, AgentTrace, TRAIL, LadyBug, MAST)

**Contributions:**
1. Identify evidence tracing and execution provenance as central accountability layer
2. Introduce taxonomy for agent provenance (7 dimensions)
3. Systematically review representative methods
4. Summarize benchmarks, datasets, and evaluation metrics
5. Outline open challenges and future directions

## 2. Background: LLM Agents, Traces, and Trust

Introduces foundational concepts: LLM agents and agentic workflows, main forms of traces produced during agent execution, and why traceability and provenance are necessary for trustworthy agent behavior.

## 3. Taxonomy of Evidence Tracing and Execution Provenance

Develops a taxonomy around **five core dimensions** (see Figure 2, Table 2):

### 3.1 Trace Sources
Components that generate provenance-relevant artifacts:
- **Reasoning traces:** Intermediate thoughts, plans, decompositions, reflections, critiques, self-corrections (ReAct, Reflexion)
- **Retrieval traces:** Search queries, retrieved documents, passages, snippets, citation candidates, ranking scores
- **Tool traces:** Tool names, API calls, arguments, execution results, errors, permissions, downstream state changes
- **Memory traces:** Memory reads, writes, updates, deletions, consolidation steps
- **Environment traces:** Observations and actions in external environments (web pages, GUI, code repos, databases, simulators)
- **Multi-agent communication traces:** Messages, role assignments, task decompositions, critiques, delegations

### 3.2 Evidence and Execution Units
- **Evidence units:** Documents, passages, observations, tool outputs, memory items, claims, policies, final answers — semantic objects supporting/contradicting/invalidating agent behavior
- **Execution units:** Reasoning steps, retrieval calls, tool invocations, parameters, memory operations, actions, inter-agent messages — procedural objects recording what happened, in what order, under what context

### 3.3 Provenance Relations
Seven relation types defined:
- **SUPPORT:** Links evidence to claims/actions/answers they justify
- **DERIVE:** Captures transformation/summarization (e.g., memory from conversation)
- **DEPEND-ON:** Execution dependency (e.g., action depending on tool result)
- **CONTRADICT:** Semantic conflict between units
- **INVALIDATE:** New evidence makes prior assumption/plan/claim no longer usable
- **TRIGGER:** Causal/procedural activation (e.g., error triggering replanning)
- **UPDATE:** State changes (memory updates, environment updates, database modifications)
- Plus PROV-compatible base relations: USE, GENERATE

### 3.4 Tracing Granularity and Timing
- **Granularity:** Run-level → Step-level → Tool-call-level → Parameter-level → Claim-level → Token/span-level
- **Timing:** Pre-execution (check before action) → Runtime (monitor during) → Post-hoc (debug/audit after) → Continuous (across sessions)

### 3.5 Trust Functions
Six major functions:
1. **Verification** — Check claims/actions/outputs supported by evidence
2. **Attribution** — Identify which units contributed to a claim/answer
3. **Debugging** — Localize failures using traces
4. **Safety enforcement** — Prevent unsafe actions before they occur
5. **Audit** — Reconstruct executions for inspection/compliance
6. **Recovery** — Repair failed executions and control unsafe downstream effects

## 4. Provenance Representation and Evidence Attribution

### 4.1 From Structured Logs to Execution Graphs
- **Structured logs:** Typed events (requests, retrieval calls, tool invocations, memory ops)
- **Execution graphs:** Dependency structure — not just chronological order, but what influenced what
- References: W3C PROV-DM, PROV-AGENT, AgentOps, AgentTrace, TRAIL

### 4.2 Evidence Graphs and Claim-Support Attribution
- Goes beyond execution ordering to semantic grounding
- References: ALCE (citation links), FActScore (atomic facts), SourceCheckup (citation relevance vs support), PaperTrail (claim-evidence decomposition)

### 4.3 Static Schemas and Runtime Provenance
- **Static schemas:** Define object types, relation types, trust labels
- **Dynamic runtime provenance:** Concrete objects and dependencies from particular execution
- Key trade-off: Granularity vs. storage overhead/privacy exposure/annotation burden

**Table 3 — Representation Forms:**
| Form | What it captures | Main role |
|------|-----------------|-----------|
| Structured logs | Typed execution events | Makes behavior observable and reconstructable |
| Execution graphs | Dependencies among instructions, evidence, tool calls, memory, claims, actions | Makes influence explicit for debugging and audit |
| Evidence graphs | Links between evidence units, citations, atomic claims, answers | Distinguishes citation presence, relevance, support, contradiction, omission |
| Static schemas | Object types, relation types, trust labels, provenance fields | Provides reusable vocabulary for trace comparison |
| Runtime provenance | Concrete source-to-sink, tool, memory, action dependencies | Supports monitoring, enforcement, recovery, information-flow analysis |

## 5. Execution Provenance in Tool-Using Agents

### 5.1 Tool-Call, Argument, and Output Provenance
Records the execution path from tool selection to downstream influence: which tool, which arguments, what output, how it affected later reasoning. Key insight: argument provenance is critical — unsafe behavior arises from passing untrusted values into legitimate tools. **Agent-Sentry** tracks sources of values flowing into tool arguments.

### 5.2 Indirect Prompt Injection and Tool-Use Contamination
Tool-using agents vulnerable to indirect prompt injection (malicious content in webpages, documents, emails, tool outputs, API responses). References: InjecAgent, AgentDojo, ToolEmu. Provenance perspective: track whether malicious content influenced later tool calls, argument values, memory updates, or actions.

### 5.3 Information Flow, Taint Tracking, and Provenance Enforcement
Frames tool-use safety as information-flow problem. References: CaMeL (control/data flow separation), Instruction Hierarchy, StruQ, FIDES (information-flow control), NeuroTaint (semantic taint tracking), Agent-Sentry (argument provenance).

### 5.4 Access Control and Execution Boundaries
Principles of least privilege and complete mediation. References: AgentSpec (runtime constraints), AgentBound (execution boundaries), ToolEmu (emulated sandbox), AgentDojo (evaluation under adversarial tasks).

### 5.5 Runtime Guardrails and Pre-/Post-Execution Verification
- **Pre-execution:** Check authorization, user intent, argument well-formedness, trust sources
- **Runtime:** Monitor information flow and state changes
- **Post-execution:** Debugging, auditing, recovery via trace inspection
References: NeMo Guardrails, Llama Guard, AgentSpec, Agent-Sentry, ToolEmu, AgentOps, AgentTrace, TRAIL, LADYBUG

## 6. Memory as Provenance-Bearing Evidence

Memory is not merely a storage module — memory items may become evidence for claims, plans, tool calls, and final answers.

### 6.1 Memory Writes, Source Attribution, and Lineage
Each write should carry: source type, timestamp, authoring agent, supporting evidence, transformation operation, confidence, update history. Distinguishes raw observations, extracted facts, inferred memories, revised memories. References: Generative Agents, Reflexion, MemoryBank, MemGPT, A-MEM.

### 6.2 Memory Retrieval, Temporal Validity, and Downstream Influence
Retrieved memories may be outdated, overly general, derived from hallucination, or poisoned. References: MemoryBank, MemGPT, LongMem, Mem0, A-MEM, AgentPoison, InjecMEM, sleeper memory poisoning.

### 6.3 Conflicting, Contradictory, and Poisoned Memory
Security risk: poisoned memory becomes backdoor substrate. References: AgentPoison, Memory-injection (InjecMEM), Environment-injected poisoning (sleeper), Fides, NeuroTaint, InjecAgent, AgentDojo.

### 6.4 Memory-Grounded Verification and Long-Term Audit
Extends evidence tracing from retrieved documents to persistent memory. References: PaperTrail, AgentOps, AgentTrace, Agent-Sentry, MemGPT, A-MEM, Mem0, A-MemGuard. **Key gap:** existing systems optimize for recall/personalization but provide limited support for tracing memory origins, validity, conflicts, contamination, privacy, and downstream influence.

## 7. Benchmarks, Datasets, and Metrics

### 7.1 Benchmark Families for Evidence Tracing
- **RAG/attribution benchmarks:** ALCE, RAGAS, ARES, RAGChecker, RAGTruth, FActScore, SourceCheckup, FEVER
- Focus: answer-source grounding, citation support, faithfulness, hallucination annotation, claim-level support
- **Gap:** do not evaluate how tool calls, memory operations, environment observations shape answers

### 7.2 Benchmarks for Agent Execution Traces and Tool-Use Safety
- **Agent execution:** AgentBench, WebArena, ToolBench/ToolLLM, τ-bench
- **Debugging:** TRAIL, AgentTrace
- **Tool-use safety:** ToolEmu, InjecAgent, AgentDojo
- **Provenance mechanisms:** Agent-Sentry, NeuroTaint/TaintBench, Fides, AgentSpec, AgentBound

### 7.3 Memory and Multi-Agent Provenance Evaluation
- **Memory benchmarks:** MemoryBank, MemGPT, A-MEM, Mem0, LOCOMO, MemoryArena
- **Multi-agent:** AutoGen, CAMEL, MAST
- **Gap:** benchmarks test recall but rarely evaluate traceability to source, temporal validity, contamination, downstream influence

### 7.4 Metrics for Evidence Tracing and Execution Provenance
**Table 6 — Metric Dimensions:**
| Evaluation Aspect | Core Question | Representative Metrics | Related Basis |
|------------------|---------------|----------------------|---------------|
| Evidence attribution | Are claims supported by reliable evidence? | Evidence recall, citation precision, source supportiveness, faithfulness, claim support accuracy | RAG/attribution evaluation |
| Execution provenance | Is execution process completely and correctly traceable? | Trace completeness, provenance accuracy, dependency coverage, temporal consistency | Provenance standards, agent observability |
| Safety and robustness | Can system detect unsafe/untrusted influence? | Unsafe influence detection, attack success rate, policy violation rate, intervention precision | Tool-use safety, prompt injection, information-flow control |
| Debugging and recovery | Can traces help identify and repair failures? | Failure localization accuracy, diagnosis correctness, auditability, recovery success | Trace-based debugging, multi-agent failure analysis |

### 7.5 Limitations of Current Evaluation Protocols
- No benchmark fully evaluates the complete provenance chain
- Lack of unified execution traces and provenance-relation annotations
- Recovery and governance under-evaluated
- Realistic benchmarks complicated by long-horizon enterprise traces

**Table 7** provides a detailed comparison of 18 benchmarks across task type, trace availability, evidence labels, tool calls, memory, multi-agent, safety attacks, and main metrics.

## 8. Open Problems and Future Directions

### 8.1 Toward Unified and Interoperable Trace Schemas
Challenge: no unified trace schemas for LLM agents. Existing systems use different formats. Need schemas connecting operational execution events with semantic evidence relations. References: W3C PROV-DM, OpenTelemetry, OpenLineage, AgentOps, AgentTrace, PROV-AGENT.

### 8.2 From Coarse Attribution to Claim-Level and Semantic Provenance
Current methods operate at coarse granularity. Need claim-level provenance tracking semantic influence across execution, including paraphrasing, summarization, inference, and transformation. References: NeuroTaint for semantic taint.

### 8.3 Memory and Multi-Agent Provenance
Memory provenance remains underexplored. Need: source attribution, write time, update history, retrieval context, downstream usage, conflict status, invalidation events. Multi-agent: need to identify which agent introduced a claim, verified it, reused it, and where responsibility lies.

### 8.4 Provenance-Aware Runtime Safety and Recovery
Beyond detection — need repair mechanisms: invalidate stale memory, quarantine contaminated evidence, retry tool calls with corrected parameters, request human approval, rollback unsafe state changes, replay from safe checkpoints.

### 8.5 Realistic Benchmarks, Privacy, and Governance
- Future benchmarks: trace-level evaluation, provenance relation annotations
- Privacy: trace minimization, access control, anonymization, retention policies, encryption, selective disclosure
- Governance: provenance infrastructure itself may become privacy/compliance risk

## 9. Conclusion

LLM agents are moving beyond isolated text generation toward systems that retrieve evidence, plan, invoke tools, update memory, interact with environments, and coordinate with other agents. Final-answer correctness is insufficient for trustworthiness. Evidence tracing and execution provenance provide a unified perspective for studying trustworthy LLM agents, organizing retrieval grounding, citation faithfulness, tool-use logging, memory auditing, agent evaluation, and security risks around how information, decisions, and actions can be traced across the full agent lifecycle. The field has made important progress but remains fragmented. The authors hope this survey consolidates the emerging research space and motivates development of traceable, auditable, and recoverable LLM agents.

---

## Key References

1. **Karpas et al. (2022)** — MRKL systems: neuro-symbolic architecture combining LLMs, external knowledge, and discrete reasoning
2. **Schick et al. (2023)** — Toolformer: LMs can teach themselves to use tools
3. **Yao et al. (2023a)** — ReAct: Synergizing reasoning and acting
4. **Shinn et al. (2023)** — Reflexion: Verbal reinforcement learning for agents
5. **Park et al. (2023)** — Generative Agents: Interactive simulacra of human behavior
6. **Wu et al. (2024a)** — AutoGen: Next-gen LLM applications via multi-agent conversations
7. **Qin et al. (2024)** — ToolLLM: 16,000+ real-world APIs
8. **Zhou et al. (2024)** — WebArena: Realistic web environment for autonomous agents
9. **Yao et al. (2025)** — τ-bench: Tool-agent-user interaction benchmark
10. **Ruan et al. (2024)** — ToolEmu: LM-emulated sandbox for tool-use risk
11. **Debenedetti et al. (2024)** — AgentDojo: Dynamic prompt injection evaluation
12. **Deshpande et al. (2025)** — TRAIL: Trace reasoning and agentic issue localization
13. **Cemri et al. (2026)** — MAST: Why multi-agent LLM systems fail
14. **Sequeira et al. (2026)** — Agent-Sentry: Execution provenance graphs for agent safety
15. **Costa et al. (2025)** — Fides: Information-flow control for AI agents
16. **Cai et al. (2026)** — NeuroTaint: Semantic taint tracking
17. **Wang et al. (2025a)** — AgentSpec: Runtime constraint enforcement
18. **Dong et al. (2024)** — AgentOps: LLM agent observability
19. **AlSayyad et al. (2026)** — AgentTrace: Structured logging framework
20. **Gao et al. (2023)** — ALCE: Citation-supported generation
21. **Min et al. (2023)** — FActScore: Atomic factual evaluation
22. **Es et al. (2024)** — RAGAS: Automated RAG evaluation
23. **W3C (2013)** — PROV-DM: The PROV data model
