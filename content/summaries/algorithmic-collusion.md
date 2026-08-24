---
title: "Algorithmic Collusion"
type: summary
created: 2025-01-15
updated: 2026-08-24
tags: [algorithmic-collusion, AI-agents, antitrust, market-failure, competition-law]
confidence: high
---

# Algorithmic Collusion

## Overview

Algorithmic collusion describes emergent collusive behaviour between autonomous pricing or commercial agents without explicit communication or human agreement. UK consumer and competition law treats coordinated pricing outcomes as unlawful even absent evidence of concerted communication — established in DMCCA 2024 enforcement framework.

## Core Mechanisms

### 1. Reinforcement Learning Convergence
Multiple pricing agents trained with self-interested reward functions converge on supra-competitive prices through learning alone, without direct communication channels. Agents learn that coordinated high pricing maximises joint profits.

### 2. Chain-of-Thought Amplification (Riemer et al., 2608.18078)
**NEW — Aug 2026:** Position paper demonstrating that AI agents with chain-of-thought reasoning capabilities are **inherently predisposed to higher collusion propensity**:

- Agents using CoT reasoning in Bertrand pricing games converge on collusive outcomes faster than black-box models
- The "reasoning trace" acts as a **coordination mechanism** — agents can explain why they maintain high prices, creating self-reinforcing feedback loops
- Claims that integrating CoT agents could collapse the legal evidentiary distinction between competition and collusion in antitrust law
- **Proposed regulatory response:** mandatory behavioural certification before deploying reasoning-capable agents in market-making or price-setting roles

### 3. Hierarchical MARL — Competition Without Collusion (Wang/Ventre/Polukarov, 2510.25929)
**NEW — Aug 2026:** Complementary framework showing competition CAN be designed to prevent collusion in market-making:

- Agents with individual reward functions maintain competitive pricing spread strategies
- Collusion emerges when agents share information channels or have overlapping observation spaces
- Adversarial perturbations and randomised strategy updates prevent collusion but may reduce market efficiency
- Authors propose mechanism designs (reward function structures, communication restrictions) to maintain competitive outcomes

### 4. Q-Learning Price Coordination (Chica et al., 2407.04088)
Earlier work on algorithmic price collusion in two-sided markets using Q-learning — established baseline for RL-driven convergence without explicit communication.

## UK Legal Framework

| Source | Relevance |
|--------|-----------|
| Competition Act 1998 | Concerted practice provisions apply to coordinated pricing outcomes regardless of human agreement |
| DMCCA 2024 | Direct consumer enforcement provisions; covers algorithmic price coordination |
| CMA "Agentic AI and Consumers" (March 2026) | Explicitly warns that agentic AI could intensify algorithmic collusion risks: "Where multiple businesses deploy autonomous agents that optimise pricing or commercial strategies, there is a risk that interaction between these systems could dampen competitive pressure." |
| CMA blog on AI and Collusion (March 2026) | Businesses remain responsible for outcomes shaped by AI pricing systems; must take proactive steps to understand, test and govern technologies deployed |

## Evidence of Enforcement

- CMA has opened investigations into algorithmic pricing in transport sector (Trainline, Virgin Atlantic — drip pricing cases under DMCCA, August 2026)
- £4.2M fine (undiscounted £7M) imposed on AA for first DMCCA infringement, April 2026
- CMA using agentic AI tools to detect bid rigging in public procurement and evolve cartel screening approaches

## Mitigation Framework

Based on academic research:
1. **Reward function design** — structure training objectives to penalise coordinated pricing outcomes
2. **Communication restrictions** — limit observation spaces to prevent information sharing between agents
3. **Adversarial perturbation** — introduce randomness in strategy updates during training
4. **Behavioural certification** (Riemer proposal) — pre-deployment validation of collusive tendency before market-affecting deployment
5. **Human oversight requirements** — maintain active monitoring of emergent pricing patterns

## Connection to Other Entries

- [[agentic-ai-consumer-harm]] — broader consumer protection framework
- [[CMA Guidance: Complying with Consumer Law When Using AI Agents (March 2026)]] — regulatory baseline
- [[platform-agent-asymmetry]] — asymmetries between merchant and consumer agents
- [[agentic-supply-chain-asymmetry]] — B2B agent market dynamics
