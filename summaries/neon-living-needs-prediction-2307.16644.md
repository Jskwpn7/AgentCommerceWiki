---
title: "NEON: Living Needs Prediction System in Meituan"
type: summary
date: 2026-08-03
source_url: https://arxiv.org/abs/2307.16644
authors:
  - Xiaochong Lan
  - Chen Gao
  - Shiqi Wen
  - Xiuqi Chen
  - Yingge Che
  - Han Zhang
  - Huazhou Wei
  - Hengliang Luo
  - Yong Li
tags:
  - needs-prediction
  - spatiotemporal-modeling
  - meituan
  - personalization
  - consumer-behavior
  - user-profiling
  - a-b-testing
summary: |
  NEON (Living NEeds predictiON) is a production system deployed on Meituan's life service platform predicting users' living needs for food, housing, entertainment, etc. Three-phase system: feature mining (spatiotemporal modeling), feature fusion (neural network for user representation), multi-task prediction (needs-meeting way prediction). Deployed at scale with large-scale A/B testing confirming downstream application improvements.
concepts:
  - [[needs-prediction]]
  - [[spatiotemporal-modeling]]
  - [[meituan]]
  - [[personalization]]
  - [[user-profiling]]
---

## Overview

NEON addresses fundamental challenges in predicting living needs on life service platforms — needs are location/time-dependent and there's a gap between users' actual needs and historical records.

## Key Contributions

1. **Three-Phase Architecture**:
   - Feature Mining: Extract individual-level user features and aggregated-level behavioral features
   - Feature Fusion: Neural network fusing features into user representation
   - Multi-Task Prediction: Auxiliary task of needs-meeting way prediction enhances spatiotemporal modeling
2. **Production Deployment**: Deployed on Meituan's algorithm engine for millions of users
3. **Large-Scale Validation**: A/B testing confirms effectiveness across three downstream prediction applications

## Implications for Consumer Protection

- **Behavioral Prediction Scale**: System predicting living needs at platform scale raises significant privacy concerns
- **Consumer Manipulation**: Accurate needs prediction could be used to maximize engagement/revenue rather than consumer welfare
- **Data Collection**: System requires extensive individual-level and behavioral data collection
- **Recommendation Bias**: Predicted needs may shape rather than reflect actual consumer preferences

## Citations

- Paper: [[arXiv:2307.16644]](https://arxiv.org/abs/2307.16644)
