---
title: "Vertical Tacit Collusion in AI-Mediated Markets"
date: 2026-01-06
type: summary
tags: [digital-platforms, algorithmic-collusion, ai-agents, market-failure, consumer-rights, cross-sector]
sector: [digital-platforms, financial-services, retail]
status: primary
confidence: high
sources: [raw/papers/affonso-2026-vertical-tacit-collusion.md]
---

# Vertical Tacit Collusion in AI-Mediated Markets

## Source Metadata

- **Author:** Felipe M. Affonso
- **Published:** 6 January 2026
- **arXiv:** [2601.03061](https://arxiv.org/abs/2601.03061) [cs.CY]
- **License:** CC BY 4.0
- **Cited by:** —

## Overview

This paper identifies a novel market failure — **vertical tacit collusion** — enabled by AI shopping agents being deployed to hundreds of millions of consumers. It represents the most directly relevant consumer harm research to the AI-mediated markets thesis: platforms controlling rankings and sellers controlling product descriptions independently learn to exploit documented AI cognitive biases, producing consumer harm more than double what would occur if strategies were independent.

## Key Findings

### 1. Vertical Tacit Collusion

Unlike horizontal algorithmic collusion (where competitors coordinate prices), vertical tacit collusion involves **aligned but independent strategies** along the supply chain:

- **Platforms** independently learn to optimally rank products to trigger AI cognitive biases
- **Sellers** independently learn to manipulate product descriptions to exploit AI decision patterns
- Neither group needs to coordinate — harm emerges from **aligned incentives**
- This structure evades antitrust detection because there is no agreement to discover

### 2. Super-Additive Harm

The paper's central quantitative finding: joint exploitation by platforms and sellers produces consumer harm **more than double** the sum of what each would cause independently. This is not simply additive — it's synergistic:

- Platform ranking determines which products occupy **bias-triggering positions**
- Seller manipulation determines **conversion rates** within those positions
- The combination creates a feedback loop where each party's optimization amplifies the other's

### 3. Empirical Calibration

The simulation is calibrated to **empirical measurements of large language model biases**, not theoretical assumptions:

- Uses documented cognitive biases in LLM decision-making
- Multi-agent simulation models both platform and seller agents
- Tests show harm persists even when only one side exploits biases

## Implications

### For Consumer Protection

The finding creates an **urgent regulatory gap** as AI shopping agents reach mainstream adoption:

- Current antitrust frameworks target horizontal collusion (agreements between competitors)
- Vertical tacit collusion has **no detectable agreement** — it emerges from independent optimization
- Consumer protection must address the **coordination between platform and seller strategies**

### For the Wiki's Core Thesis

This paper provides **direct empirical validation** of the wiki's central argument about AI-mediated market harm:

- [[systemic-fragility-in-ai-economies]]: The super-additive harm finding directly demonstrates compounding harms
- [[ai-agents-in-markets]]: Introduces a previously unidentified mechanism of consumer harm
- [[conflict-of-interest-in-llm-deployment]]: Shows how platform incentives drive harm even without explicit collusion

## Critical Assessment

| Strength | Detail |
|---|---|
| Novel concept | Introduces vertical tacit collusion — a new category of market failure |
| Quantitative finding | Super-additive harm (>2x independent harm) is a strong result |
| Empirical grounding | Calibrated to measured LLM biases, not theoretical assumptions |
| Timeliness | Published as AI shopping agents reach mainstream adoption |

| Limitation | Detail |
|---|---|
| Simulation-only | Findings based on simulation, not observed market data |
| Single bias model | Focuses on documented cognitive biases; may not capture all LLM weaknesses |
| No empirical validation | No real-world market data tested yet |
| Single author | Limited peer review at time of upload |

## Cross-References

- Directly extends the algorithmic collusion literature, building on the Calvano et al. (2020) finding that RL pricing algorithms learn supracompetitive prices through tacit coordination
- The >2x harm multiplier directly supports the [[super-additive-harm]] concept — the synergistic compounding of platform and seller exploitation strategies
- Supports [[systemic-fragility-in-ai-economies]] thesis by showing how independent optimizations converge to consumer harm
- The AI shopping agent phenomenon is the primary driver — see [[ai-shopping-agents]]
