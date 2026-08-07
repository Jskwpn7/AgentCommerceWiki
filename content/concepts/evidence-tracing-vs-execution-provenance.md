---
type: concept
title: "Evidence Tracing vs. Execution Provenance"
category: "AI Systems / Agent Architecture"
date: "2026-06-23"
related_papers:
  - "arxiv-2606.04990v1-evidence-tracing-execution-provenance-llm-agents"
tags:
  - "evidence-tracing"
  - "execution-provenance"
  - "agent-traces"
  - "accountability"
---

# Evidence Tracing vs. Execution Provenance

> Two complementary aspects of the agent accountability layer, distinguished by Wang et al. (arXiv:2606.04990v1).

## Definitions

### Evidence Tracing
Mechanisms that **identify, record, and connect the evidence units** that support, contradict, invalidate, or influence agent claims, decisions, and actions.

Focus: *Which evidence justified which claim?*

### Execution Provenance
The broader structured representation of **how an agent execution unfolds** — retrieved documents, tool calls, parameters, observations, memory accesses, intermediate claims, actions, inter-agent messages, and final outputs.

Focus: *What happened, in what order, and what influenced what?*

## Key Differences

| Aspect | Evidence Tracing | Execution Provenance |
|--------|-----------------|---------------------|
| Scope | Evidence-claim relationships | Full execution lifecycle |
| Question | "Which evidence supports this claim?" | "How did this output get produced?" |
| Primary relations | SUPPORT, CONTRADICT, INVALIDATE | DERIVE, DEPEND-ON, TRIGGER, UPDATE |
| Primary units | Documents, passages, tool outputs, memory items | Reasoning steps, tool invocations, actions, messages |
| Downstream use | Verification, attribution | Debugging, audit, recovery |

## Complementary Nature

The two are described as complementary, not competing:
- **Evidence tracing alone** → Know which document supports a claim, but not which tool call produced the evidence or which action used it
- **Execution provenance alone** → Know that a tool was called, but not whether its output actually supported the final answer

Effective provenance requires **both**: evidence tracing provides the semantic grounding, execution provenance provides the procedural chain. Together they connect semantic support with procedural execution.

## Provenance Representation Spectrum

The paper identifies five forms, ranging from basic to advanced:
1. **Structured logs** — Typed execution events (chronological, observable)
2. **Execution graphs** — Dependencies among units (procedural, debuggable)
3. **Evidence graphs** — Links between evidence and claims (semantic, attributable)
4. **Static schemas** — Object/relation types, trust labels (reusable vocabulary)
5. **Runtime provenance** — Concrete source-to-sink dependencies during execution (enforceable)

## Related Concepts
- [[Agent Provenance Taxonomy]] — The five-dimension framework
- [[Provenance Representation Forms]] — How provenance is structured
