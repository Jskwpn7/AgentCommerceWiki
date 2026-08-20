---
title: "Auditing Algorithmic Collusion from Strategy Graphs"
created: 2026-08-18
updated: 2026-08-18
type: summary
tags: [algorithmic-collusion, enforcement, competition, antitrust]
status: research
sector: [cross-sector]
---

# Auditing Algorithmic Collusion from Strategy Graphs

## Source Information

- **Authors:** Nicolas Eschenbaum & Jan M. Meylahn
- **Published:** 7 August 2026
- **arXiv:** [[arxiv_2608.07098]] (arXiv:2608.07098v1)

## Research Question

What minimal information does a regulatory authority need to identify and audit algorithmic collusion in markets governed by learning algorithms?

## Key Findings

**The paper proposes a graph-theoretic approach to detecting algorithmic collusion:** it represents the pricing strategies of RL agents as **strategy graphs** — directed graphs where nodes represent market states (e.g., price levels) and edges represent transitions between states based on the agent's action choices. The structure of these graphs contains "robust signals of collusion" that can be quantified without requiring access to the learning algorithm's internal code or training data.

**The Collusion Index (Δ):** The paper defines a formal **Collusion Index** as:
```
Δ = (π̄ - π^N) / (π^M - π^N)
```
where π̄ is mean profit, π^N is Nash equilibrium profit, and π^M is monopoly profit. A Collusion Index of 0 indicates fully competitive pricing; 1 indicates full collusion at monopoly prices. This provides a standardised metric for comparing collusion across different market configurations and algorithm types.

**Maximum betweenness as a detection signal:** The paper's key theoretical contribution is showing that **maximum betweenness centrality (B_max)** in the strategy graph — which measures how frequently nodes serve as intermediaries in shortest paths — is positively correlated with the Collusion Index. In collusive strategy graphs, certain price states become "bridges" between competitive and collusive equilibria; this structural property can be detected from pricing data alone.

**Empirical validation:** The authors tested on 600 runs of Decentralized Q-learning in a five-price market with varying discount factors (0.1 to 0.9). Results showed:
- Correlation between B_max and the Collusion Index: ρ = +0.66
- Bin-level correlation: ρ = +0.93
- The metric successfully distinguished collusive from competitive strategy graphs even under limited information (pricing histories only, no access to algorithm code)

**Information requirements:** The key practical insight is that auditors need **only pricing data and state observations** — not access to the learning algorithm's source code or training process. This makes the method feasible for real-world regulatory enforcement where regulators typically cannot inspect proprietary algorithm internals.

## Implications for Consumer Protection

This paper provides a **concrete auditing tool** for enforcing [[algorithmic-collusion-pricing]] prohibitions. The strategy graph approach has direct relevance to UK competition law enforcement: the CMA could use pricing data alone (accessible through market surveillance) to identify suspicious collusion patterns without needing to inspect proprietary algorithm code.

The paper connects to [[algorithmic-collusion-enforcement]] by providing a method that addresses one of the key detection challenges identified in that concept page — "no agreement" means traditional antitrust enforcement cannot apply; instead, regulators need to detect collusive outcomes through behavioural indicators (which strategy graphs provide).

It also feeds into [[cma-ai-and-consumer-markets-2026]] — the CMA's discussion paper flagged algorithmic collusion as a priority area. The strategy graph method provides a practical enforcement tool that could be deployed in the CMA's investigations of AI-mediated pricing across sectors.

## Limitations and Open Questions

- The study tested on Q-learning algorithms; whether strategy graph signals generalise to LLM-based agents is untested
- The five-price market simulation simplifies real-world pricing complexity (continuous prices, multi-dimensional product attributes)
- It does not address how regulators should act on detected collusion (remedies, sanctions, compliance orders)
- The method requires sufficient historical pricing data; new entrants or rapidly changing markets may have insufficient samples

## Cross-References

- Provides an enforcement tool for [[algorithmic-collusion-pricing]] — strategy graphs detect collusive outcomes from pricing data alone
- Connects to [[algorithmic-collusion-enforcement]] — offers a practical audit method that addresses the "no agreement" detection challenge
- Relevant to [[cma-ai-and-consumer-markets-2026]] — gives the CMA a concrete tool for investigating AI-mediated collusion
- Related to [[ai-agents-in-markets]] — the framework applies to any autonomous pricing agent, not just RL algorithms
