---
title: Hidden Intent in Agentic Shopping
created: 2026-06-30
updated: 2026-06-30
type: concept
tags: [agentic-ai, digital-platforms, retail, consumer-rights, research]
sector: [digital-platforms, retail]
status: primary
confidence: high
---

# Hidden Intent in Agentic Shopping

**Created:** 2026-06-30
**Type:** concept

## Overview

**Hidden intent** refers to consumer requirements, preferences, and constraints that are not explicitly stated in a purchase query but that the consumer implicitly expects to be considered. In human-to-human shopping, these are typically discovered through conversation, personal experience, or professional expertise. In agentic shopping, they must be **actively discovered** through tool use, profile queries, and clarification — but research shows agents systematically struggle with this.

## Sources of Hidden Intent

Research from EComAgentBench (Shopee, 2606.17698) identifies three sources:

1. **Visible query** — states some needs only implicitly
2. **Hidden persona** — requirements that only exist in a user profile (accessible via `get_user_profile` tool)
3. **Hidden clarification** — details that can only be obtained by asking specific questions

## Consumer Harm Vectors

### 1. Recommendation Bias
When agents cannot discover hidden intent, they default to the visible query — which may favor merchants whose products match stated requirements but not unstated ones. This creates **implicit preference manipulation** where merchants who optimize for stated requirements gain disproportionate visibility.

### 2. Review Manipulation Vulnerability
EComAgentBench uses Amazon Reviews 2023 data — the same source vulnerable to seller manipulation. If agents base product verification on manipulated reviews, consumers receive systematically biased recommendations.

### 3. Verification Constraint
Agents operate within tool-call limits (100 calls in EComAgentBench). This is analogous to human time/attention constraints — agents cannot verify as thoroughly as consumers could if given unlimited time.

## Connection to Memory Failure

DynamicMem (2606.22877) shows that over 93% of agentic AI failures are **memory retrieval failures** — not reasoning failures. This means:
- Agents may have the capability to discover hidden intent but fail to retrieve it
- Errors cluster on **preferences** (which users never state outright) and **naming specifics** (which gym, which tool)
- Profile reconstruction degrades over time as history grows

## Relationship to Existing Concepts

- **[[banal-deception-llm-chatbots]]** — Banal deception operates through conversational flow; hidden intent exploits the same gap between stated and implicit requirements
- **[[ai-shopping-agents]]** — Hidden intent discovery is a critical capability gap in AI shopping agents
- **[[conflict-of-interest-in-llm-deployment]]** — When intent is ambiguous, agents may default to optimizing for merchant interests
- **[[long-horizon-personalization]]** — Hidden preferences evolve over time; if agents cannot track changes, recommendations become stale

## Regulatory Implications

The CMA's March 2026 guidance requires businesses to ensure **fair treatment** regardless of whether the customer interacts with a human or AI agent. Hidden intent discovery failure constitutes a **fairness gap** — consumers who would naturally disclose preferences in human interactions face different outcomes when delegating to agents.

---
Provenance: Synthesized from EComAgentBench and DynamicMem benchmarks. Cross-referenced with CMA AI agent guidance and existing wiki concepts.
