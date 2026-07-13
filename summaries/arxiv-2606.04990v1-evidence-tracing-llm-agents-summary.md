---
type: summary
title: "Evidence Tracing and Execution Provenance in LLM Agents — Survey Summary"
source_paper: "arxiv-2606.04990v1-evidence-tracing-execution-provenance-llm-agents"
date: "2026-06-23"
tags:
  - "llm-agents"
  - "provenance"
  - "traceability"
  - "trustworthy-ai"
---

# Evidence Tracing and Execution Provenance in LLM Agents — Survey Summary

> **Source:** Wang et al., "From Agent Traces to Trust: Evidence Tracing and Execution Provenance in LLM Agents," arXiv:2606.04990v1, June 2026
> **Type:** Systematic survey/review paper

## Overview

This survey identifies a critical gap in LLM agent research: **final-answer accuracy is insufficient for trustworthiness**. As agents increasingly interact with tools, retrieval systems, memory, environments, and other agents, the field needs systematic ways to trace *how* outputs are produced — not just *what* was produced. The paper proposes **evidence tracing and execution provenance** as a unified accountability layer for trustworthy LLM agent systems.

## Core Problem: The Accountability Gap

Modern LLM agents perform heterogeneous execution across multiple dimensions:
- Reasoning chains and plans
- External tool/API calls with parameters
- Document retrieval and evidence gathering
- Memory reads/writes across sessions
- Environment observation and state changes
- Multi-agent communication and delegation

When an agent succeeds, the supporting evidence path may remain opaque. When it fails, the failure origin (retrieval error, tool misuse, stale memory, prompt injection, miscommunication) is hard to pinpoint. This is the **process-level accountability gap**.

## Key Framework: 5-Dimension Taxonomy (Table 2)

| Dimension | Categories | Key Insight |
|-----------|-----------|-------------|
| **Trace Sources** | Reasoning, retrieval, tool use, memory, environment, multi-agent | Each source generates different evidence types with different failure modes |
| **Evidence & Execution Units** | Evidence (semantic support) vs. Execution (procedural steps) | Both must be linked; neither alone is sufficient |
| **Provenance Relations** | SUPPORT, DERIVE, DEPEND-ON, CONTRADICT, INVALIDATE, TRIGGER, UPDATE | Typed graphs > flat chronological logs |
| **Granularity & Timing** | Run-level → Token-level; Pre-execution → Runtime → Post-hoc → Continuous | Trade-off: granularity vs. overhead |
| **Trust Functions** | Verification, Attribution, Debugging, Safety, Audit, Recovery | Provenance serves 6 distinct purposes |

## Five Methodological Contributions

1. **Provenance Representation** (Section 4): Structured logs → execution graphs → evidence graphs → runtime provenance. The paper argues for moving beyond flat chronological logs to dependency-aware representations that make influence paths explicit.

2. **Tool-Use Provenance** (Section 5): The most security-relevant section. Covers indirect prompt injection, information-flow control (taint tracking), access boundaries, and runtime guardrails. Key systems: Agent-Sentry (argument provenance), FIDES (information-flow labels), NeuroTaint (semantic taint), AgentSpec (runtime constraints).

3. **Memory Provenance** (Section 6): Memory is not passive storage — it's evidence-bearing. Key problems: source attribution for memory writes, temporal validity, contamination/poisoning risks, downstream influence tracking. References AgentPoison, InjecMEM, sleeper poisoning attacks.

4. **Benchmark Mapping** (Section 7): Systematic review of 18+ benchmarks across evidence tracing, tool-use, memory, multi-agent, safety, and debugging categories. **Critical finding**: no existing benchmark provides strong end-to-end coverage across all provenance dimensions. The paper includes a heatmap (Figure 5) and detailed comparison table (Table 7).

5. **Open Problems** (Section 8): Unified trace schemas, claim-level provenance, provenance-aware recovery, privacy-aware audit infrastructure, realistic execution-trace benchmarks.

## Key Systems Referenced

| Category | Systems |
|----------|---------|
| Observability | AgentOps, AgentTrace |
| Tool Safety | Agent-Sentry, FIDES, NeuroTaint, AgentSpec, AgentBound |
| Prompt Injection | InjecAgent, AgentDojo, ToolEmu |
| Memory | MemGPT, A-MEM, MemoryBank, Mem0, Generative Agents |
| Evidence/Factuality | FActScore, ALCE, RAGAS, RAGChecker, FEVER, RAGTruth, SourceCheckup, PaperTrail |
| Debugging | TRAIL, LADYBUG |
| Multi-Agent | AutoGen, CAMEL, MAST |

## Critical Gap Analysis

The survey identifies a **fragmentation problem**: RAG evaluation, tool-use safety, memory research, graph-based reasoning, observability, and debugging each advance independently but use different terminology, representations, and evaluation protocols. No unified framework connects retrieval grounding → claim support → tool justification → memory validity → multi-agent attribution → recovery.

## Consumer Harm Relevance

This paper is directly relevant to the UK consumer harms domain for:
- **Financial services agents**: Provenance tracking for advice generation, tool-use justification, memory validity (e.g., outdated client risk profiles)
- **Regulatory compliance**: Audit trails for automated decision-making under UK financial regulations
- **Algorithmic accountability**: Understanding how AI agents make decisions that affect consumers
- **Prompt injection in customer service**: Protecting against malicious instructions injected through customer interactions
- **Memory poisoning**: Risks of contaminated customer data influencing future agent behavior

## Novel Contributions

1. **Unified provenance taxonomy** — First paper to systematically organize evidence tracing and execution provenance across all agent execution dimensions
2. **Seven provenance relation types** — Formalizes semantic (SUPPORT, CONTRADICT, INVALIDATE) and procedural (DERIVE, DEPEND-ON, TRIGGER, UPDATE) relations
3. **Trust function taxonomy** — Links provenance to 6 concrete downstream purposes
4. **Comprehensive benchmark mapping** — Systematic comparison of 18+ benchmarks across provenance dimensions with heatmap visualization
5. **Memory as provenance-bearing evidence** — Shifts perspective on agent memory from "capability mechanism" to "auditable basis for accountability"
