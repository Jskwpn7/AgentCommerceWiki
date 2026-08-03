---
title: "Multi-Agent Reinforcement Learning for Dynamic Pricing in Supply Chains: Benchmarking Strategic Agent Behaviours"
type: summary
date: 2026-08-03
source_url: https://arxiv.org/abs/2507.02698
authors:
  - Thomas Hazenberg
  - Yao Ma
  - Seyed Sahand Mohammadi Ziabari
  - Marijn van Rijswijk
tags:
  - dynamic-pricing
  - marl
  - price-collusion
  - predatory-pricing
  - algorithmic-pricing
  - fairness
  - volatility
summary: |
  Evaluates three MARL algorithms (MADDPG, MADQN, QMIX) for dynamic pricing against static rule-based baselines in simulated e-commerce environment. MADQN exhibits most aggressive pricing with highest volatility and lowest fairness (0.5844). MADDPG provides balanced approach with market competition and high fairness (0.8819). Demonstrates MARL introduces emergent strategic behavior not captured by static pricing rules.
concepts:
  - [[dynamic-pricing]]
  - [[marl]]
  - [[price-collusion]]
  - [[algorithmic-pricing]]
  - [[fairness]]
---

## Overview

Traditional ERP pricing relies on static, rule-based approaches that ignore strategic interactions among market actors. This paper evaluates MARL for dynamic pricing in supply chains.

## Key Contributions

1. **MARL for Dynamic Pricing**: Evaluates MADDPG, MADQN, and QMIX algorithms for pricing
2. **Strategic Behavior Analysis**: Documents emergent behaviors from MARL training
3. **Fairness Metrics**: Introduces Jain's Index for pricing fairness evaluation
4. **Volatility Analysis**: Measures price stability across algorithm types

## Key Findings

| Algorithm | Fairness (Jain's) | Price Stability | Market Competition |
|-----------|-------------------|-----------------|-------------------|
| Rule-based | 0.9896 | 0.024 (highest) | None |
| MADQN | 0.5844 (lowest) | Highest volatility | Most aggressive |
| MADDPG | 0.8819 | Moderate | High (9.5 pp share volatility) |

## Emergent Behaviors

- MARL introduces strategic behavior not captured by static pricing rules
- MADQN agents exhibit aggressive pricing that reduces fairness
- Rule-based agents achieve near-perfect fairness but lack competitive dynamics

## Implications for Consumer Protection

- **Algorithmic Price Collusion**: MARL agents may learn collusive pricing strategies
- **Predatory Pricing**: MADQN's aggressive behavior could drive competitors out of market
- **Price Volatility**: Unstable pricing harms consumer welfare and planning
- **Fairness Concerns**: Algorithmic pricing may discriminate across consumer segments
- **Transparency**: Dynamic pricing algorithms are often opaque to consumers and regulators
- **Regulatory Gap**: Current competition law not designed for MARL-driven pricing

This paper documents how MARL introduces emergent pricing behaviors that could harm consumers through collusion or predatory strategies.

## Citations

- Paper: [[arXiv:2507.02698]](https://arxiv.org/abs/2507.02698)
