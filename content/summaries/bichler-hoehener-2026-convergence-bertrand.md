---
title: "Convergence of Stochastic First-Order Algorithms in Bertrand Competition Under Incomplete Information"
date: 2026-05-22
type: summary
tags: [algorithmic-pricing, bertrand-competition, bayes-nash-equilibrium, multi-agent-learning, convergence-theory]
sector: [cross-sector]
status: primary
confidence: high
sources: [raw/papers/bichler-hoehener-2026-convergence-bertrand.md]
---

# Convergence of Stochastic First-Order Algorithms in Bertrand Competition Under Incomplete Information

## Source Metadata

- **Authors:** Martin Bichler, Jan-Sebastian Höhener
- **Affiliation:** Chair of Decision Sciences and Systems, Technical University of Munich
- **Published:** 22 May 2026
- **arXiv:** [2605.17607](https://arxiv.org/abs/2605.17607) [cs.AI]
- **License:** CC BY 4.0
- **Cited by:** —

## Overview

This paper provides a **rigorous counterpoint** to widespread claims of algorithmic collusion by proving that stochastic first-order learning algorithms (Regularized Robbins–Monro algorithms) converge to the efficient Bayes–Nash equilibrium in Bayesian Bertrand competition with private costs. Unlike prior experimental evidence suggesting collusive outcomes, this work establishes **convergence guarantees** for a class of learning algorithms widely used in real-world pricing agents.

## Key Findings

### 1. Convergence to Bayes–Nash Equilibrium

Despite violating standard stability conditions:

- The setting violates **monotonicity** and the **Minty variational inequality**
- Classical convergence results for gradient-based learning are inapplicable
- Nevertheless, Euclidean RRM algorithms **converge almost surely** to the unique, efficient Bayes–Nash equilibrium
- The proof uses a projected dynamical system framework with a global Lyapunov function

### 2. Critique of Prior Collusion Evidence

The paper identifies key limitations in prior algorithmic collusion evidence:

| Limitation | Detail |
|---|---|
| Q-learning bias | Prior evidence relies on tabular Q-learning, which scales poorly and lacks vanishing regret guarantees |
| Complete information | Prior work uses complete-information environments, unlike real-world pricing where costs are private |
| Hyperparameter sensitivity | Collusive outcomes may depend on specific hyperparameter choices rather than fundamental dynamics |
| Theoretical gap | Lack of rigorous convergence guarantees for the algorithms actually used in production |

### 3. Real-World Algorithmic Pricing

The paper argues that the algorithms deployed in real-world online marketplaces are **stochastic first-order methods** (stochastic gradient ascent, optimistic gradient, extra-gradient) — not tabular Q-learning. These:

- Are well suited for **continuous action spaces**
- Satisfy **minimal rationality requirements** (vanishing regret)
- Are the natural choice for algorithmic pricing in production
- **Converge to equilibrium** in the Bayesian setting with private costs

### 4. Bayesian Bertrand Competition Model

The model captures key features of online pricing:

- Firms have **privately known costs** drawn from a common distribution
- Learning agents don't even know the cost distribution ex-ante
- The Bayes–Nash equilibrium serves as the clear benchmark
- Piecewise-linear pricing strategies in a duopoly setting provide explicit construction

## Implications for the Wiki

This paper provides an important **nuance** to the algorithmic collusion narrative:

- While [[systemic-fragility-in-ai-economies]] and [[affonso-2026-vertical-tacit-collusion]] demonstrate real collusion risks, this paper shows that the **most widely deployed class of algorithms** (stochastic first-order methods) actually **converges to competitive equilibrium**
- The collusion evidence from prior work relies on **Q-learning**, which is not representative of production systems
- This creates a more balanced picture: collusion risks exist but may be concentrated in specific algorithm classes

### Tension with Collusion Literature

| Finding | Collusion Literature | This Paper |
|---|---|---|
| Core claim | LLM/RL agents reach supracompetitive prices | Stochastic first-order agents converge to BNE |
| Method | Q-learning, RL | RRM (SGA, optimistic gradient) |
| Information | Complete information | Bayesian (private costs) |
| Real-world relevance | Questionable (Q-learning doesn't scale) | High (matches production algorithms) |
| Outcome | Collusion | Efficient equilibrium |

## Critical Assessment

| Strength | Detail |
|---|---|
| Rigorous proof | Establishes convergence guarantees, not just empirical observations |
| Realistic algorithm class | Analyzes the actual algorithms used in production pricing agents |
| Bayesian setting | Captures the incomplete information that characterizes real markets |
| Counter-narrative | Provides important nuance to the collusion literature |

| Limitation | Detail |
|---|---|
| Model simplicity | Piecewise-linear pricing in duopoly — may not capture complex multi-product markets |
| Theoretical framework | Convergence guarantees apply to a specific algorithm class, not all agents |
| No LLM focus | Doesn't address LLM-based agents specifically |
| No empirical validation | Purely theoretical — no market data tested |

## Cross-References

- Provides the strongest theoretical counterpoint to [[systemic-fragility-in-ai-economies]] — shows that production algorithms converge to equilibrium
- Important complement to [[affonso-2026-vertical-tacit-collusion]] — differentiates between algorithm classes and their convergence properties
- Relevant to [[ai-agents-in-markets]] — shows that not all AI-mediated pricing leads to harm
- **Calvano et al. (2020):** The foundational paper showing RL pricing algorithms learn supracompetitive prices — Tian's paper extends this by showing prompt optimization enables even more stable collusion
- Relates to [[tian-2026-prompt-optimization-collusion]] — shows that the specific algorithm/prompt paradigm matters enormously for collusion risk
