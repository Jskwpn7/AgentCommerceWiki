---
type: concept
title: "Agent Provenance Taxonomy"
category: "AI Systems / Agent Architecture"
date: "2026-06-23"
related_papers:
  - "arxiv-2606.04990v1-evidence-tracing-execution-provenance-llm-agents"
tags:
  - "provenance"
  - "agent-traces"
  - "taxonomy"
  - "traceability"
---

# Agent Provenance Taxonomy

> Taxonomy of evidence tracing and execution provenance for LLM agents, as defined by Wang et al. (arXiv:2606.04990v1).

## Definition

A structured framework for describing and comparing provenance-aware LLM agent systems along five core dimensions. It moves beyond flat chronological logging to a typed, graph-based representation of how agent behavior is produced and can be traced.

## Five Dimensions

### 1. Trace Sources
Where provenance-relevant artifacts originate in agent systems:
- **Reasoning** — Thoughts, plans, decompositions, reflections, self-corrections
- **Retrieval** — Queries, documents, passages, snippets, citations, ranking scores
- **Tool use** — Tool names, API calls, arguments, results, errors, permissions
- **Memory** — Reads, writes, updates, deletions, consolidation steps
- **Environment** — Observations and actions in web, GUI, databases, simulators
- **Multi-agent communication** — Messages, role assignments, task decompositions, delegations

### 2. Evidence and Execution Units
- **Evidence units** — Objects providing semantic support/contradiction/context (documents, passages, tool outputs, memory items, claims, policies)
- **Execution units** — Procedural steps recording what the agent did, in what order, under what context (reasoning steps, retrieval calls, tool invocations, memory operations, actions, messages)

### 3. Provenance Relations
Typed connections between trace units:
- **SUPPORT** — Evidence supports a claim/answer
- **DERIVE** — Transformation/summarization (e.g., memory from conversation)
- **DEPEND-ON** — Execution dependency (e.g., action depends on tool result)
- **CONTRADICT** — Semantic conflict between units
- **INVALIDATE** — New evidence makes prior assumption/plan no longer usable
- **TRIGGER** — Causal/procedural activation (e.g., error triggers replanning)
- **UPDATE** — State changes (memory, environment, database)
- **USE / GENERATE** — PROV-compatible base relations

### 4. Granularity and Timing
- **Granularity:** Run-level → Step-level → Tool-call-level → Parameter-level → Claim-level → Token/span-level
- **Timing:** Pre-execution → Runtime → Post-hoc → Continuous

### 5. Trust Functions
Provenance serves 6 downstream purposes:
1. **Verification** — Claims supported by appropriate evidence
2. **Attribution** — Which units contributed to a claim/answer
3. **Debugging** — Localize failures
4. **Safety enforcement** — Prevent unsafe actions before they occur
5. **Audit** — Reconstruct executions for inspection/compliance
6. **Recovery** — Repair failed executions and control unsafe downstream effects

## Key Distinction

The taxonomy distinguishes between **evidence tracing** (identifying which evidence supports/contradicts claims) and **execution provenance** (recording how the agent execution unfolds — the causal/procedural chain from input to output).

## Related Concepts
- [[Provenance Representation Forms]] — How provenance is structured (logs, graphs, schemas)
- [[Agent Observability]] — Systems for recording and inspecting agent executions
- [[Tool-Use Safety]] — Security concerns in tool-using agents
