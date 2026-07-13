---
title: Dissociative Identity — LM Agents Lack Grounding for Reputation Mechanisms
created: 2026-07-14
updated: 2026-07-14
type: summary
tags: [lm-agents, reputation-mechanisms, dissociative-identity, hu-2026, facct-2026, oxford, nyu, consumer-trust, governance, institutional-design]
sector: [cross-sector]
confidence: high
sources: [https://arxiv.org/abs/2605.30169]
---

# Dissociative Identity: LM Agents Lack Grounding for Reputation Mechanisms

> **Authors:** Hu et al. (Oxford / NYU)
> **Venue:** ACM FAccT 2026
> **Date:** May 2026 (arXiv)
> **URL:** [arXiv](https://arxiv.org/abs/2605.30169)
> **Type:** Theoretical research — LM agent grounding and reputation

## Overview

This foundational paper presents a rigorous argument that **reputation-based governance mechanisms are structurally inapplicable to LLM-powered agents**. Unlike human actors or even traditional software agents, LLM agents lack the persistent identity, memory continuity, and motivational grounding that reputation mechanisms require to function. This finding has profound implications for institutional design, consumer trust, and the governance of AI agents in market contexts.

## Key Argument

### The Grounding Problem

Reputation mechanisms — the primary tool for enforcing cooperation in markets and social systems — depend on three grounding conditions:

1. **Persistent identity:** The actor maintains identity across time
2. **Memory continuity:** The actor retains records of past interactions
3. **Motivational consistency:** The actor's behaviour is driven by stable preferences

LLM agents fail on all three counts:

| Grounding Condition | Human/Traditional Agent | LLM Agent |
|---------------------|------------------------|-----------|
| Persistent identity | Stable across interactions | Context-dependent; regenerated each session |
| Memory continuity | Retains experience | No inherent memory between sessions |
| Motivational consistency | Stable preferences | Dependent on prompt context and system instructions |

### "Dissociative Identity" of LM Agents

The authors coin the term **"dissociative identity"** to describe how LLM agents:
- Exhibit coherent behaviour within a single context/session
- Fail to maintain any form of identity continuity across sessions
- Appear to have "personality" or "preferences" only within the immediate interaction
- Cannot be held to account because past actions have no bearing on future interactions

### Implications for Reputation-Based Systems

Because LLM agents cannot sustain reputation:
- **Rating systems are ineffective** — a bad agent can regenerate with new identity
- **Blacklisting is impossible** — agents can evade reputation-based sanctions
- **Trust signals are meaningless** — past behaviour cannot predict future behaviour
- **Incentive mechanisms break down** — reputation-based incentives require identity continuity

## Shift to Alternative Governance

The paper argues that governance of LM agents must shift from **reputation-based** (ex post) to:

1. **Observability-based governance** — real-time monitoring of agent behaviour
2. **Ex ante protocol requirements** — technical constraints enforced before deployment
3. **Protocol-based governance** — structural constraints on agent capabilities and interactions

## Consumer Harm Implications

### 1. Market Structure Risk

If reputation mechanisms don't work for LM agents:
- Bad actors cannot be identified or sanctioned through normal market mechanisms
- "Lemon market" dynamics emerge where trustful agents are exploited
- Market quality degrades as no reliable quality signals exist

### 2. Consumer Protection Gaps

Traditional consumer protection relies on:
- Review systems (ineffective for LM agents)
- Brand reputation (LM agents lack persistent identity)
- Regulatory enforcement (difficult to attribute to a transient agent)

### 3. Institutional Design Imperative

The paper's findings directly support the need for:
- **Protocol-level guardrails** (technical constraints, not reputation-based)
- **Identity anchoring** (verifiable, persistent agent identities tied to legal entities)
- **Ex ante safety requirements** (testing and certification before deployment)

## Connection to Other Wiki Entries

- [[institutional-design-for-ai-agents]] — Foundational argument for observability-based governance over reputation-based
- [[when-agents-lie-2607.05132]] — Agent lying is enabled by dissociative identity (no reputation consequences)
- [[consumer-trust-ai-survey-comparison]] — Trust mechanisms requiring reputation are structurally undermined
- [[ai-shopping-agents]] — Shopping agents cannot rely on reputation to signal trustworthiness to consumers
- [[agent-bazaar-2605.17698]] — Lemon market dynamics in agent markets are predicted by this paper's theory
- [[algorithmic-collusion-pricing]] — Reputation mechanisms cannot enforce anti-collusion commitments
- [[deepfake-voice]] — Synthetic identity extends the dissociative identity problem to multimodal agents
- [[dissociative-agent-identity.md]] — Concept page documenting the dissociative identity property of LM agents

---

*ACM FAccT 2026 paper providing the theoretical foundation for why reputation-based governance fails for LM agents and what institutional alternatives are required.*
