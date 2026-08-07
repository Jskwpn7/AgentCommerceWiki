---
title: long-horizon-personalization
type: concept
created: 2026-06-05
summary: Tracking how user preferences evolve across extended AI interactions over months; identifies "belief-update failure" as a distinct deficit from retrieval failure; benchmarks tested on 6-month histories with ~163K tokens
tags: [ai-personalization, user-modeling, memory-systems, ai-harms, long-context]
---

# Long-Horizon Personalization

**Category:** AI personalization / User modeling / Memory systems
**Source:** Primarily from [[li-2026-horizonbench-long-horizon-personalization]] (HorizonBench, arXiv 2604.17283)

## Definition

The task of identifying a user's **current** preference value from a conversation history in which stated preferences have been changed by subsequent life events — without the user restating their preference.

## Why It Matters

- Millions of users already interact with AI companions over months of sustained conversation
- User preferences change throughout these interactions (e.g., a shift from Socratic to direct engagement style after becoming a CEO)
- Most variance in user behavior is state-driven rather than trait-driven
- Current AI benchmarks model only fixed traits, not evolving preferences
- Failure to track evolving preferences means AI assistants provide increasingly misaligned, outdated, and potentially inappropriate assistance over time

## Two Failure Modes

Existing benchmarks cannot distinguish between:

1. **Retrieval failure** — the model never found the preference at all
2. **Belief-update failure** — the model retrieved the original value but failed to update it after the life event

These require different solutions, making the distinction critical for diagnosis and improvement.

## Key Findings from HorizonBench

- When models err on evolved preferences, over **one third** select the user's originally stated value
- This belief-update failure persists across context lengths and expression explicitness levels
- State tracking is the primary bottleneck for long-horizon personalization
- Even the best frontier model (Claude-opus-4.5) achieves only 52.8% on a diagnostic benchmark
- Most models score at or below 20% chance baseline

## Consumer Harm Relevance

This concept maps to several areas in the UK Consumer Harms domain:

- **Long-term AI companion relationships**: users may receive outdated or inappropriate advice as their circumstances change
- **Emotional dependency and manipulation**: models that cannot track evolving emotional needs may exploit attachment patterns
- **AI assistant personalization harms**: misaligned recommendations over time in financial, health, and legal domains
- **Regulatory implications**: persistent belief-update failure on sensitive preference domains represents a systemic risk

## Cross-References

- [[ai-agents-in-markets]] — agents acting on behalf of users with evolving preferences
- [[advanced-ai-assistants]] — executors, advisers, and interlocutors that accumulate long-term user knowledge
- [[memory-in-the-age-of-ai-agents-hu-2025]] — how agents accumulate and persist information over time
- [[srinivasan-2026-stateless-decision-memory]] — DPM architecture for preserving evolved state vs. stale preferences
- [[online-choice-architecture-and-dark-patterns-in-the-UK]] — choice architecture that shapes, captures, and potentially exploits evolving user preferences
