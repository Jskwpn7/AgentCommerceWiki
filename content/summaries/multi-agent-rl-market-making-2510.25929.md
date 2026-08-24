---
title: "Multi-Agent Reinforcement Learning for Market Making: Competition without Collusion"
type: summary
created: 2026-08-24
updated: 2026-08-24
source_url: https://arxiv.org/abs/2510.25929
authors:
  - Ziyi Wang
  - Carmine Ventre
  - Maria Polukarov
tags: [academic, agentic-ai, algorithmic-collusion, market-making]
confidence: high
---

# Multi-Agent Reinforcement Learning for Market Making: Competition without Collusion

arXiv:2510.25929 (cs.MA; cs.AI), King's College London. Published at ICAIF 2025.

## Summary

Empirical study examining whether multi-agent RL systems deploying market-making agents can maintain competitive behaviour or converge to collusive outcomes when competing in simulated financial markets. Key finding: **competition without collusion is achievable** under certain reward structures, but the system requires careful design to prevent emergent coordination.

## Key Findings

- Market-making agents trained with individual reward functions (maximising own profit) can maintain competitive pricing spread strategies without colluding.
- **Collusion emerges when agents share information channels** or have overlapping observation spaces that enable tacit coordination.
- Introducing adversarial perturbations or randomised strategy updates prevents collusion convergence but may reduce overall market efficiency.
- Authors propose mechanism designs (reward function structures, communication restrictions) that maintain competitive outcomes.

## Relevance to UK Consumer Harms

- Direct relevance to algorithmic pricing in retail and financial services: if AI agents coordinating on spread/pricing can be designed to avoid collusion, this has implications for OFT enforcement under the DMCCA 2024.
- Informs the regulatory question of whether competition authorities should mandate "collusion-resistant" architectures for market-facing AI systems.
- Relevant to [[ai-agent-economics-emergence-2608.03076]] which discusses autonomous economic behaviour in agent markets.

## Connection to Other Wiki Entries

- Complements the collusion analysis in [[auditing-collusion-strategy-graphs-eschenbaum-meylahn-2608.07098]].
- Related to pricing agent dynamics in [[pricing-agents-buying-agents-xie-2026]].
