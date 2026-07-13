---
type: concept
title: "Memory Provenance"
category: "AI Systems / Agent Architecture"
date: "2026-06-23"
related_papers:
  - "arxiv-2606.04990v1-evidence-tracing-execution-provenance-llm-agents"
tags:
  - "memory-provenance"
  - "agent-memory"
  - "provenance"
  - "agent-poisoning"
---

# Memory Provenance

> Treating agent memory as evidence-bearing objects with traceable origins, transformations, temporal validity, and downstream influence, as defined by Wang et al. (arXiv:2606.04990v1).

## Core Premise

Agent memory is **not a passive storage module**. Memory items may later become evidence for claims, plans, tool calls, and final answers. Their origin, transformation, retrieval context, temporal validity, conflicts, and downstream influence therefore become part of the agent's provenance chain.

## Four Dimensions

### 1. Memory Writes — Source Attribution and Lineage
Each memory write should carry:
- Source type (user input, retrieved document, tool output, environment observation, reflection, inter-agent message)
- Timestamp, authoring agent
- Supporting evidence, transformation operation
- Confidence, update history
- Lineage: raw observations → extracted facts → inferred memories → revised memories

**Key systems:** Generative Agents, Reflexion, MemoryBank, MemGPT, A-MEM

### 2. Memory Retrieval — Temporal Validity and Downstream Influence
Retrieved memories may be:
- Partially relevant, outdated, overly general
- Derived from a previous hallucination
- Poisoned by adversarial interaction
- No longer valid in the current environment

**Provenance-aware retrieval should track:** triggering query/context, retrieved items, original sources, relevance signals, validity status, downstream links to claims/actions.

**Key systems:** MemoryBank, MemGPT, LongMem, Mem0, A-MEM

### 3. Conflict, Contradiction, and Poisoning
- **AgentPoison:** Poisoned long-term memory/RAG knowledge bases as backdoor substrates
- **InjecMEM:** Targeted memory injection through ordinary agent interactions
- **Sleeper memory poisoning:** Adversarial external context implants fabricated memories that remain dormant
- **Memory privacy:** Sensitive stored information exposed through adversarial interactions

### 4. Memory-Grounded Verification and Long-Term Audit
Extends evidence tracing from retrieved documents to persistent memory. Requires:
- Source attribution across memory writes, retrieval events, updates, conflicts, invalidations
- Persistent lineage across sessions
- Selective invalidation: identify affected claims, actions, and derived memories when memory is stale/contaminated
- Self-checking and self-correction mechanisms

**Key gap:** Existing systems (MemGPT, A-MEM, Mem0) optimize for recall/personalization/efficiency but provide limited support for tracing memory origins, validity, conflicts, contamination, privacy, and downstream influence.

## Defense Mechanisms
- **Fides:** Information-flow control with confidentiality/integrity labels
- **NeuroTaint:** Semantic taint tracking through memory
- **A-MemGuard:** Self-checking and self-correction for agent memory

## Related Concepts
- [[Agent Provenance Taxonomy]] — Memory provenance as part of the 5-dimension framework
- [[Agent Provenance Taxonomy]] — Memory traces as one of the 6 trace source types
