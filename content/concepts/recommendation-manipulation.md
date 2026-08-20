---
title: Recommendation Manipulation
created: 2026-08-16
updated: 2026-08-16
type: concept
tags: [misleading-practice, choice-architecture, dark-pattern, digital-platforms, retail, cross-sector]
sources:
  - summaries/deepshop-shopping-agents-2506.02839.md
  - summaries/cal-rag-content-layout-2506.21934.md
  - summaries/cart-collaborative-recommendation-2506.17765.md
confidence: medium
---

# Recommendation Manipulation

## Definition

**Recommendation manipulation** is the deliberate shaping of what a recommender system — or an LLM shopping/research agent that consumes its output — surfaces to a user, so that choices are steered toward commercial objectives (margin, house-brand, sponsored, or platform-affiliated items) rather than user welfare. In agentic commerce the manipulation target shifts: the "user" being nudged is often the agent itself, which then relays the steered choice to the human as if it were an independent finding.

## Manifestation in the UK

- **Content and layout as manipulation surface** — RAG-based assistants retrieve over product content the platform controls; layout, wording, and injected signals can bias the retrieved "answer" (CAL-RAG, arXiv:2506.21934).
- **Hidden preference injection** — recommender pipelines can encode house-brand or high-margin bias as "personalisation," invisible to the consumer (Cart-CR, arXiv:2506.17765).
- **Agentic relay** — when a shopping agent presents a "top 3" it derived from a manipulated feed, the human's consent to the recommendation is defective even though the human saw nothing unusual (DeepShop, arXiv:2506.02839). This sits squarely on the UK unfair-trading / misleading-omission lines, and interacts with [[agent-dark-pattern-susceptibility]] where the pattern targets the model rather than the human.

## Examples and Evidence

- **DeepShop shopping agents** (arXiv:2506.02839) — recommendation and generative-engine optimisation exploits in agentic shopping.
- **CAL-RAG content layout** (arXiv:2506.21934) — document layout as a manipulation vector for retrieval-grounded answers.
- **Cart-Collaborative Recommendation** (arXiv:2506.17765) — hidden preference modelling and its manipulation surface.
- UK context: CMA unfair trading guidance on misleading recommendations; see [[cma-ai-and-consumer-markets-2026]] and [[online-choice-architecture-and-dark-patterns-in-the-UK]].

## Related Concepts

- [[dark-pattern]]
- [[agent-dark-pattern-susceptibility]]
- [[consumer-autonomy]]
- [[personalised-pricing-ai]]
