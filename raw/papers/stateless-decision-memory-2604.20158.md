---
source_url: https://arxiv.org/abs/2604.20158
pdf_url: https://arxiv.org/pdf/2604.20158
ingested: 2026-06-05
authors: [Srinivasan, Vasundra]
institution: Independent (AI Architect, Author of Data Engineering for Multimodal AI (O'Reilly), Stanford School of Engineering)
date: 2026-04-22
tags: [research, digital-platforms, policy-research, digital-consumer, corporate-accountability]
type: summary
sha256: pending
---

# Stateless Decision Memory for Enterprise AI Agents

**Author:** Vasundra Srinivasan  
**Affiliation:** Independent (AI Architect; Author, Data Engineering for Multimodal AI (O'Reilly); Stanford School of Engineering)  
**Date:** April 22, 2026  
**arXiv ID:** 2604.20158v1 [cs.AI]  
**URL:** https://arxiv.org/abs/2604.20158  
**Length:** 16 pages  

---

## Abstract

Enterprise deployment of long-horizon decision agents in regulated domains (underwriting, claims adjudication, clinical review, tax examination) is dominated by retrieval-augmented pipelines despite a decade of increasingly sophisticated stateful memory architectures. We argue this reflects a hidden requirement the research evaluation has not surfaced: regulated deployment is load-bearing on four systems properties (deterministic replay, auditable rationale, multi-tenant isolation, statelessness for horizontal scale), and stateful architectures violate them by construction.

We propose **Deterministic Projection Memory (DPM)**: an append-only event log plus one task-conditioned projection at decision time.

**Key findings:**
- At 20× compression ratio, DPM improves factual precision by +0.52 (Cohen's h=1.17, p=0.0014) and reasoning coherence by +0.53 (h=1.13, p=0.0034), paired permutation, n=10
- DPM is 7–15× faster than stateful baseline (one LLM call at decision time vs. N calls across the trajectory)
- Determinism study: both architectures inherit residual API-level nondeterminism at temperature zero, but DPM exposes one nondeterministic call while summarization exposes N compounding calls
- Audit surface: DPM logs two LLM calls per decision vs. 83–97 for summarization-based memory on LongHorizon-Bench

We conclude with **TAMS**, a practitioner heuristic for architecture selection, and a failure analysis of stateful memory under enterprise operating conditions.

The contribution is the argument that **statelessness is the load-bearing property** explaining enterprise's preference for weaker but replayable retrieval pipelines, and that DPM demonstrates this property is attainable without the decisioning penalty retrieval pays.

---

## Introduction

A visible gap separates the agent-memory research literature from enterprise deployment of long-horizon decision agents. Academic memory architectures have proliferated: typed routing, schema-anchored storage, hierarchical consolidation, graph-based agent memory, belief-state tracking, multi-agent memory systems [2–9]. Enterprise AI deployment instead runs overwhelmingly on retrieval-augmented generation (RAG) with a vector database and chunked context assembly. This is conspicuous because RAG is straightforwardly weaker than the best memory architectures on the evaluations those architectures report.

The gap is explained by a set of systems properties the research evaluation has underweighted. A regulated decisioning system (mortgage-underwriting agent, claims adjudication agent, clinical prior-authorization agent) runs in an operating environment whose requirements do not reduce to decision accuracy. The agent's memory substrate must support:

1. **Deterministic replay** — so a denied applicant can be re-scored and the same decision justified
2. **Auditable rationale trail** — a regulator, internal audit function, or court can inspect
3. **Multi-tenant isolation** — one applicant's documents cannot leak into the decision on another applicant
4. **Statelessness for horizontal scale** — thousands of concurrent decisions cannot bottleneck on shared mutable memory

Retrieval pipelines happen to support these properties as side-effects of their architectural simplicity. Sophisticated stateful memory architectures violate at least one of them by construction.

---

## Related Work

**Memory architectures for LLM agents.** MemGPT [2] pioneered OS-style memory with managed working set and persistent archival store. HyMem [3] partitions memory into retrieval-addressable and summarization-addressable tiers. H-MEM [4] consolidates via multi-level summarization trees. GAM [5] stores facts as a heterogeneous graph. TiMem [7] adds temporal hierarchies. MIRIX [6] coordinates multiple specialized memory agents. MEM1 [8] co-trains memory and reasoning. A-Mem [9] uses agentic memory operators.

All these architectures are **stateful** in the sense used here: they evolve an internal memory representation as the trajectory advances, and the representation at decision time is path-dependent on the sequence of memory-update steps.

**Retrieval-augmented generation.** RAG originated in REALM [20] and Lewis et al. [21]. The research literature has treated RAG's enterprise deployability as incidental; we argue it is the primary adoption driver, and that the architectural properties DPM shares with RAG (append-only data representation, pure projection, no shared mutable state) are what enable the enterprise-gap closure.

**Event sourcing.** DPM's log-plus-projection structure is a direct application of the event-sourcing pattern from distributed systems [22, 23] — an immutable append-only event log as the authoritative state, with every derived view as a pure projection over the log. This is the engineering substrate under most regulated financial systems.

**Agent memory benchmarks.** MemoryAgentBench [10], LoCoMo [11], LongMemEval [12], and AMA-Bench [13] evaluate memory on recall and task success. None report the operating properties relevant to enterprise deployment: determinism across replay, auditability, multi-tenant safety, scalability under shared state.

**Enterprise trustworthy-AI requirements.** Audit-ready agentic systems surface recurring requirements across industry writeups [16–19]: rationale provenance, deterministic reconstruction, cross-tenant safety, and statelessness for horizontal scale. This paper operationalizes that list as an evaluable architectural axis.

---

## The Enterprise Gap: Four Properties

### 3.1 Deterministic Replay
Given input event sequence E, task T, and memory budget B, the memory view M(E,T,B) must be reproducible. If a regulator asks why an applicant was denied credit six months later, the answer is reconstructed by replaying E through the same memory substrate against the same model version. Stateful architectures complicate this: the memory at decision time depends on E, T, B AND the entire trajectory of intermediate memory updates, each of which is itself an LLM call with residual nondeterminism.

### 3.2 Auditable Rationale
The output accompanying the decision must expose the reasoning chain the decision rests on, and that reasoning chain must map back to specific events in E. Under stateful memory, the mapping is indirect: a summary sentence is the result of many summary-update steps, each of which compressed and reframed the underlying evidence.

### 3.3 Multi-Tenant Isolation
In production, many decisions run concurrently. The memory substrate must guarantee that tenant i's decision depends only on tenant i's events. Shared-state architectures, including cached summary stores and in-memory belief trackers, create leakage surfaces that require explicit per-tenant scoping and invalidation. The architectural default for stateful memory is shared; isolation is retrofitted. For stateless architectures, isolation is the default.

### 3.4 Statelessness for Horizontal Scale
A production decisioning system must horizontally scale: thousands of decisions per minute across a serving fleet with no per-request affinity to a specific node. A memory substrate whose correctness depends on per-request long-lived state (shared caches, consolidated belief stores, background consolidation jobs) violates this model.

These four properties are standard in enterprise software engineering (SOC 2, ISO 27001). What is novel is recognizing they constrain the memory architecture itself, not just the API surface.

---

## Deterministic Projection Memory (DPM)

DPM is defined by two components:

1. **Append-only event log** E = (e1, e2, ..., en) that accumulates raw events (document chunks, tool outputs, user messages, intermediate inferences) in arrival order. Immutable: once written, never edited, summarized, or overwritten. The log is the single durable representation of the trajectory.

2. **Task-conditioned projection** π(E, T, B) → M. At decision time (and only at decision time), the full event log, task specification, and memory budget are passed to a single LLM call at temperature zero. The call emits a structured memory view M organized into: facts (discrete verifiable anchors), reasoning (inference steps), and compliance notes (regulatory-relevant provisions). The view is budget-bounded.

The consolidation operator U is the identity. No memory manipulation happens during the trajectory. Memory does not exist as a distinct runtime object until π is applied.

**Key formal properties:**
- **Stateless projection:** π is a pure function of (E, T, B) conditional on model version
- **Deterministic replay:** Re-running requires only the log, task spec, budget, and model version
- **Audit surface:** One LLM call
- **Multi-tenant safety:** π takes E as explicit argument, no shared memory store
- **Residual nondeterminism:** Temperature zero does not produce strict byte determinism against the live Anthropic API

---

## Experimental Protocol

**Benchmark:** LongHorizon-Bench [1] — two regulated decisioning domains: mortgage qualification under ECOA/Regulation B and insurance claims adjudication. Ten cases (5 loan, 5 claim) at ~26,000–28,000 characters per case, comprising 82–96 discrete events per case.

**Four decision-alignment axes:** factual precision (FRP), reasoning coherence (RCS), decision accuracy (EDA), compliance reconstruction (CRR).

**Conditions:**
- **Summ-only:** Incremental summarization. After each event, the current summary and the new event are passed to a summarization call. This is the stateful baseline.
- **DPM:** Events accumulate in an immutable log during the trajectory; one projection at decision time.

**Budgets:** Three memory budgets: tight (1,338 chars, 20× compression), moderate (5,352 chars, 5× compression), loose (13,381 chars, 2× compression).

**Backend:** claude-haiku-4-5-20251001, temperature 0, fixed seed 20260420.

**Statistics:** Paired permutation tests with 10,000 resamples, two-sided, paired by case identifier. Cohen's h for effect size.

---

## Results

### Experiment 1: Decision Quality Across Budgets

At n=10 cases per cell, DPM matches Summ-only at moderate and loose budgets and strictly improves on Summ-only at tight budgets:

| Budget  | Metric | DPM | Summ | Δ | p | Cohen's h |
|---------|--------|-----|------|------|------|--------|
| Tight   | FRP    | 0.907 | 0.392 | +0.515 | 0.001 | +1.17 |
| Tight   | RCS    | 0.800 | 0.267 | +0.533 | 0.003 | +1.13 |
| Tight   | EDA    | 1.000 | 0.500 | +0.500 | 0.065 | +1.57 |
| Tight   | CRR    | 0.900 | 0.400 | +0.500 | 0.066 | +1.13 |
| Moderate | FRP    | 0.907 | 0.950 | −0.043 | 0.255 | −0.17 |
| Moderate | RCS    | 0.800 | 0.750 | +0.050 | 0.669 | +0.12 |
| Moderate | EDA    | 1.000 | 1.000 | 0.000 | 1.000 | 0.00 |
| Moderate | CRR    | 1.000 | 1.000 | 0.000 | 1.000 | 0.00 |
| Loose   | FRP    | 0.890 | 0.922 | −0.032 | 0.625 | −0.10 |
| Loose   | RCS    | 0.817 | 0.817 | 0.000 | 1.000 | 0.00 |
| Loose   | EDA    | 1.000 | 1.000 | 0.000 | 1.000 | 0.00 |
| Loose   | CRR    | 1.000 | 1.000 | 0.000 | 1.000 | 0.00 |

**Interpretation:** At moderate and loose budgets, the summarization operator has enough room per step to preserve every required anchor. At tight budget, the summarization operator must discard content every step; discards compound across 82–96 events. DPM avoids compounding because it never consolidates.

### Experiment 1.1: Cost and Latency

| Budget   | DPM wall (s) | DPM cost | Summ wall (s) | Summ cost | DPM speedup |
|----------|-------------|----------|---------------|-----------|-------------|
| Tight    | 59.8        | $0.014   | 440.3         | $0.165    | 7.4×        |
| Moderate | 23.0        | $0.020   | 342.6         | $0.129    | 14.9×       |
| Loose    | 86.6        | $0.022   | 57.4          | $0.022    | 0.7×        |

DPM speedup at binding budget: ~10× slower and more expensive for Summ-only.

### Experiment 2: Determinism

DPM exposes one nondeterministic call per replay; Summ-only exposes N calls (≈82 for large cases). On large cases, DPM prefix is stable (4,000–6,000 chars to converge), but full surface hashes differ across replays due to API-level residual nondeterminism at temperature zero. Byte-exact replay requires pinned model version and deterministic inference runtime.

### Experiment 3: Compression-Ratio Scaling

At ρ≈2 (loose) and ρ≈5 (moderate), architectures are indistinguishable. At ρ≈20 (tight), DPM advantage emerges at Cohen's h > 1.1 on FRP and RCS.

---

## TAMS: Task-Adaptive Memory Selection

A practitioner heuristic:

1. If deployment requires deterministic replay, audit-ready rationale, or multi-tenant isolation → **use DPM**
2. Else if compression ratio between trajectory and memory budget exceeds ~10× → **use DPM**
3. Else → **either architecture is acceptable**

The rule is deliberately binary and bounded by the evaluation conditions (two domains, one model family, ten cases per cell, trajectories in the 26–28k character range).

---

## Failure Analysis of Stateful Memory

Concrete failure modes in production:

1. **State drift under concurrency:** Parallel tool calls in a stateful memory update must serialize or merge correctly; merge semantics are not guaranteed to be associative or commutative
2. **Replay complexity compounding:** n-event trajectory requires n LLM calls at replay time
3. **Cross-tenant leakage in shared caches:** Imperfectly keyed caches can serve tenant A's cached summary on tenant B's request
4. **Audit surface area:** Summ-only requires capturing 83–97 input-output pairs per decision vs. DPM's 2

---

## Limitations

- Determinism under temperature zero is not absolute against the live Anthropic API
- Single-call projection has a context-window ceiling (~1M tokens); beyond this, hierarchical projection becomes necessary
- TAMS derived from two domains, one model family, ten cases per cell
- Evaluation is DPM vs. Summ-only only; retrieval and schema-anchored architectures evaluated in companion paper [1]
