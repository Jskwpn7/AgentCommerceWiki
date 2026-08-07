---
title: "RecoAtlas: From Semantic Plausibility to Set-Level Utility in LLM Recommendation Agents"
type: summary
date: 2026-08-03
source_url: https://arxiv.org/abs/2605.18805
authors:
  - Imad Aouali
  - Flavian Vasile
  - Otmane Sakhi
  - Alexandre Gilotte
  - Benjamin Heymann
tags:
  - benchmark
  - recommendation
  - semantic-plausibility
  - set-level-utility
  - tool-use
  - behavior-grounded
  - shopping-agents
summary: |
  Introduces Recommendation Atlas (Agentic Tool-Level Assessment for Shopping), a benchmark evaluating shopping agents with behavior-grounded metrics. Complements held-out interaction metrics with learned utility proxies. Tests agents with semantic, behavior-aligned, or faulty tools. Shows semantic plausibility does not capture behavior-grounded utility.
concepts:
  - [[behavior-grounded]]
  - [[set-level-utility]]
  - [[tool-use]]
  - [[semantic-plausibility]]
---

## Overview

RecoAtlas addresses the gap between semantic plausibility and actual user utility in LLM recommendation agents.

## Key Contributions

1. **Behavior-Grounded Metrics**: Evaluates relevance, complementarity, and diversity derived from interaction data
2. **Controlled Tool Environment**: Tests agents with semantic, behavior-aligned, or faulty tools
3. **Semantic Coherence + Explanation Quality**: Separate measurement of explanation quality
4. **Diagnosis Framework**: Determines whether performance gains come from reasoning, signals, or tool-use policies

## Key Findings

- Semantic plausibility does not capture behavior-grounded utility
- Performance scales with model capacity and test-time compute
- Stronger and better-aligned tools improve performance
- Noisy or misaligned signals degrade performance
- Semantic plausibility alone is insufficient for evaluating recommendation agents

## Implications

This is critical for consumer protection: current evaluation methods may favor agents that produce plausible-sounding recommendations over those that actually deliver utility. Consumers should be aware that "expert" recommendations may be semantically coherent but not behaviorally optimal.

## Citations

- Paper: [[arXiv:2605.18805]](https://arxiv.org/abs/2605.18805)
