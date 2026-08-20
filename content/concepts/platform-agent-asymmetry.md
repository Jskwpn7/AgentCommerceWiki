---
title: Platform–Agent Asymmetry
created: 2026-08-16
updated: 2026-08-16
type: concept
tags: [digital-platforms, agentic-ai, choice-architecture, gatekeeping, cross-sector]
sources:
  - summaries/meituan-llm-interaction-2510.13291.md
  - summaries/deepshop-shopping-agents-2506.02839.md
  - summaries/multi-agent-search-framework-2510.20567.md
confidence: medium
---

# Platform–Agent Asymmetry

## Definition

**Platform–agent asymmetry** is the structural information and incentive gap between a commercial platform and the AI agents (on behalf of consumers, or on the platform's own behalf) that interact with it. The platform holds privileged knowledge of its own catalogue, ranking, pricing, and manipulation surface, while an external agent must infer these from opaque signals. This asymmetry lets the platform steer, gatekeep, or manipulate the agent's decisions in ways that are harder for the agent — and therefore for the human behind it — to detect than equivalent manipulation of a human shopper.

## Manifestation in the UK

UK consumer law (DMCCA 2024, CMA unfair-trading guidance) is built on the assumption that the counterparty is a human making bounded-but-visible decisions. When the counterparty is an agent, the asymmetry deepens in three ways:

1. **Opaque search and ranking** — platforms can reorder results, inject sponsored or house-brand items, or throttle third-party listings in ways an agent interprets as "the best option" rather than a cued one.
2. **Asymmetric personalisation** — the platform's model of the user (and thus the agent's effective preferences) is a black box; the agent optimises against a moving target it cannot audit.
3. **Manipulation surface expansion** — content and layout are now "consumed" by a model, creating a new target for [[dark-pattern]]s aimed at the agent rather than the human (see [[agent-dark-pattern-susceptibility]]).

## Examples and Evidence

- **Meituan LLM interaction** (arXiv:2510.13291) — documents how platform-side ranking and reply shaping biases a consumer-facing agent's recommendations, with no human recourse path.
- **DeepShop shopping agents** (arXiv:2506.02839) — shows recommendation and generative-engine manipulation exploiting the agent's lack of platform internals.
- **Multi-agent search framework** (arXiv:2510.20567) — quantifies ranking opacity as a first-order distortion when agents compete for attention on a platform.

## Related Concepts

- [[dark-pattern]]
- [[recommendation-manipulation]]
- [[consumer-autonomy]]
- search manipulation (no dedicated page yet — de-wikilinked in summaries)
- gatekeeping (harm-type tag, see SCHEMA.md)
