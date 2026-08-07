---
title: "Enhancing Local Life Service Recommendation with Agentic Reasoning in Large Language Model"
type: summary
date: 2026-08-03
source_url: https://arxiv.org/abs/2604.14051
authors:
  - Shiteng Cao
  - Xiaochong Lan
  - Yuwei Du
  - Jie Feng
  - Yinxing Liu
  - Xinlei Shi
  - Yong Li
tags:
  - local-life
  - recommendation
  - need-prediction
  - curriculum-learning
  - rl-verifiable-rewards
  - behavioral-clustering
  - long-tail
summary: |
  Proposes LLM-based framework jointly performing living need prediction and service recommendation for local life services. Introduces behavioral clustering to filter noise from raw consumption data. Uses curriculum learning + RL with verifiable rewards to navigate need-to-merchant mapping. Enhances both need prediction performance and recommendation accuracy, with gains in long-tail scenarios.
concepts:
  - [[local-life-service]]
  - [[need-prediction]]
  - [[curriculum-learning]]
  - [[verifiable-rewards]]
  - [[behavioral-clustering]]
  - [[long-tail-recommendation]]
---

## Overview

Local life service recommendation differs from general recommendation due to its strong living-need-driven nature. This paper proposes unified modeling of need prediction and service recommendation.

## Key Contributions

1. **Unified Framework**: Jointly performs living need prediction and service recommendation
2. **Behavioral Clustering**: Filters accidental factors from raw consumption data, preserves typical patterns
3. **Curriculum Learning + RL**: Guides model sequentially through need generation → category mapping → specific service selection
4. **Verifiable Rewards**: RL process uses verifiable reward signals for training

## Key Findings

- Jointly modeling living needs and user behaviors significantly enhances both prediction and recommendation
- Behavioral clustering improves model robustness to noisy data
- Curriculum learning helps navigate vast search space of needs-merchants-mappings
- Model generalizes well to long-tail scenarios

## Implications for Consumer Protection

- **Need Manipulation**: If models can predict and influence living needs, they could create artificial demand
- **Long-Tail Vulnerability**: Long-tail merchants may be underrepresented in recommendations despite model claims
- **Privacy**: Behavioral clustering requires detailed consumption data
- **Transparency**: Consumers unaware their "needs" are being algorithmically predicted and potentially shaped

## Citations

- Paper: [[arXiv:2604.14051]](https://arxiv.org/abs/2604.14051)
