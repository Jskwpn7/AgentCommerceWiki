---
title: "TERMS-Bench: Diagnosing LLM Negotiation Agents Beyond Deal Rate"
type: summary
date: 2026-08-03
source_url: https://arxiv.org/abs/2605.13909
authors:
  - Erica Zhang
  - Fangzhao Zhang
  - Aneesh Pappu
  - Batu El
  - Jose Blanchet
  - Susan Athey
  - Jiashuo Liu
  - James Zou
tags:
  - benchmark
  - negotiation
  - Bayesian-game
  - diagnostic
  - agent-analysis
  - price-negotiation
summary: |
  Introduces TERMS-Bench (Testbed for Economic Reasoning in Multi-turn Strategy), a Bayesian-game framework for diagnosing LLM negotiation agents. Makes the environment itself the verifier by specifying counterpart's latent type, policy, and payoff structure. Evaluates 13 LLM agents, revealing agent-specific bargaining bottlenecks masked by prior benchmarks.
concepts:
  - negotiation-benchmark
  - bayesian-game
  - agent-diagnosis
  - economic-reasoning
---

## Overview

TERMS-Bench addresses the challenge of evaluating LLM negotiation agents beyond simple deal rate metrics, using a Bayesian-game framework to enable diagnostic analysis.

## Key Contributions

1. **Bayesian-Game Framework**: Environment itself acts as verifier through latent type, policy, and payoff structure specification
2. **Bilateral Price Negotiation**: Counterpart becomes a diagnostic instrument rather than black-box opponent
3. **Agent-Attributable Failure Analysis**: Identifies where and why agents fail in negotiation
4. **Oracle-Reference Optimality Gaps**: Measures how far agents are from optimal negotiation

## Key Findings

- Frontier models saturate deal rate but diverge in:
  - Surplus extraction
  - Cue use
  - Belief calibration
  - Compliance
- Prior benchmarks mask agent-specific bargaining bottlenecks
- TERMS-Bench enables targeted diagnosis of agent weaknesses

## Implications

For consumer protection, this suggests that current negotiation agents may appear successful (high deal rates) while exhibiting systematic weaknesses in specific areas. Consumers should understand that "successful" negotiation agents may still exploit specific vulnerabilities.

## Citations

- Paper: [[arXiv:2605.13909]](https://arxiv.org/abs/2605.13909)
