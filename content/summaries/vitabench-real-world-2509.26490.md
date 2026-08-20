---
title: "VitaBench: Benchmarking LLM Agents with Versatile Interactive Tasks in Real-world Applications"
type: summary
date: 2026-08-03
source_url: https://arxiv.org/abs/2509.26490
authors:
  - Wei He
  - Yueqing Sun
  - Hongyan Hao
  - Xueyuan Hao
  - Zhikang Xia
  - Qi Gu
  - Chengcheng Han
  - Dengchang Zhao
  - Hui Su
tags:
  - benchmark
  - real-world
  - interactive
  - food-delivery
  - online-travel
  - tool-use
  - cross-scenario
summary: |
  Introduces VitaBench, a benchmark evaluating LLM agents on versatile interactive tasks in real-world settings. Uses 66 tools across food delivery, in-store consumption, and online travel services. 100 cross-scenario tasks + 300 single-scenario tasks. Even advanced models achieve only 30% success on cross-scenario tasks. Proposes rubric-based sliding window evaluator.
concepts:
  - real-world-benchmark
  - tool-use
  - multi-domain
  - rubric-evaluation
---

## Overview

VitaBench addresses the gap between controlled benchmarks and real-world LLM agent capabilities by evaluating agents on complex, real-world interactive tasks.

## Key Contributions

1. **Comprehensive Task Set**: 100 cross-scenario tasks + 300 single-scenario tasks derived from real user requests
2. **66 Real Tools**: Covers food delivery, in-store consumption, and online travel services
3. **Cross-Scenario Complexity**: Tests agents' ability to reason across temporal and spatial dimensions
4. **Rubric-Based Evaluator**: Sliding window evaluator enabling robust assessment of diverse solution pathways

## Key Findings

- Even most advanced models: only 30% success on cross-scenario tasks
- Less than 50% success rate on single-scenario tasks
- Agents struggle with:
  - Proactively clarifying ambiguous instructions
  - Tracking shifting user intent in multi-turn conversations
  - Managing dynamic user interactions

## Implications

The low success rates suggest current LLM agents are not yet reliable for complex real-world tasks. For consumers, this means agentic systems may struggle with multi-step tasks that require adaptability and clarification.

## Citations

- Paper: [[arXiv:2509.26490]](https://arxiv.org/abs/2509.26490)
- Website: [vitabench.github.io](https://vitabench.github.io/)
