---
type: concept
title: "Provenance Representation Forms"
category: "AI Systems / Agent Architecture"
date: "2026-06-23"
related_papers:
  - "arxiv-2606.04990v1-evidence-tracing-execution-provenance-llm-agents"
tags:
  - "provenance"
  - "representation"
  - "execution-graphs"
  - "evidence-graphs"
  - "structured-logs"
---

# Provenance Representation Forms

> Five forms of representing agent provenance, from basic logging to runtime enforcement, as identified in Wang et al. (arXiv:2606.04990v1).

## Overview

Provenance representation turns raw agent traces into inspectable, queryable, and auditable records. The five forms represent increasing levels of structure and semantic depth.

## Five Forms

### 1. Structured Logs
Typed execution events: user requests, model outputs, retrieval calls, tool invocations, tool outputs, memory operations, environment observations, inter-agent messages, final responses.

**Role:** Makes agent behavior observable and reconstructable.
**Limitation:** Only chronological — doesn't reveal which evidence influenced which claim.
**Systems:** AgentOps, AgentTrace, W3C PROV-DM, PROV-AGENT

### 2. Execution Graphs
Dependencies among instructions, evidence, tool calls, memory items, claims, and actions.

**Role:** Makes execution influence explicit for debugging and audit.
**Advantage over logs:** Shows what influenced what, not just what happened when.
**Systems:** TRAIL (annotated agent traces for failure localization)

### 3. Evidence Graphs
Links between evidence units, citations, atomic claims, and generated answers.

**Role:** Distinguishes citation presence, relevance, support, contradiction, and omission.
**Key insight:** Citation presence ≠ evidence support (SourceCheckup finding).
**Systems:** ALCE (citation links), FActScore (atomic facts), PaperTrail (claim-evidence decomposition)

### 4. Static Schemas
Object types, relation types, trust labels, and provenance fields.

**Role:** Provides reusable vocabulary for trace representation and comparison across systems.
**Foundation:** W3C PROV-DM generalized to LLM agent domain.
**Specialization needed:** Retrieved chunks, tool arguments, memory writes, inter-agent messages, generated claims, external state changes.

### 5. Runtime Provenance
Concrete source-to-sink, tool, memory, and action dependencies during execution.

**Role:** Supports monitoring, enforcement, recovery, and information-flow analysis.
**Key advantage:** Enables real-time safety interventions, not just post-hoc inspection.
**Systems:** Agent-Sentry (source-to-sink tracking), FIDES (information-flow labels), NeuroTaint (taint propagation)

## Key Trade-Off

**Granularity vs. Overhead:**
- Fine-grained provenance → supports verification, debugging, recovery, audit
- But increases storage overhead, logging complexity, privacy exposure, annotation burden
- Coarse-grained provenance → easier to collect, but may fail to identify which evidence supported a claim, which memory item caused an error, or which tool argument crossed a trust boundary

## Related Concepts
- [[Agent Provenance Taxonomy]] — The five-dimension framework these representations serve
- [[agent-provenance-taxonomy]] — Security-relevant provenance applications
