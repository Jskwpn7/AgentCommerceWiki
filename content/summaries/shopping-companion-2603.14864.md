---
title: "Shopping Companion: Benchmarking and Training LLM Agents for Long-Horizon Preference-Grounded E-Commerce Tasks"
type: summary
date: 2026-08-03
source_url: https://arxiv.org/abs/2603.14864
authors:
  - Zijian Yu
  - Kejun Xiao
  - Huaipeng Zhao
  - Tao Luo
  - Xiaoyi Zeng
tags:
  - benchmark
  - preference
  - long-horizon
  - shopping
  - preference-hallucination
  - reward-design
  - fine-tuning
summary: |
  Introduces Shopping Companion Bench, a benchmark for long-term preference-aware shopping tasks with 1.2M real-world items. Identifies two failure modes: cascading errors from preference hallucination and insufficient product attribute verification. Designs annotation-free, tool-wise rewards for process supervision. Fine-tuned 4B model outperforms strong baselines.
concepts:
  - [[preference-memory]]
  - [[long-horizon]]
  - [[preference-hallucination]]
  - [[tool-wise-rewards]]
---

## Overview

Shopping Companion Bench addresses two critical challenges in e-commerce: evaluating long-term preference-aware shopping tasks and training agents with fine-grained supervision.

## Key Contributions

1. **Shopping Companion Bench**: Two shopping tasks requiring cross-session preference memory
2. **1.2M Item Pool**: Grounded in real-world product catalog
3. **Failure Mode Analysis**: Identifies cascading preference hallucination and insufficient verification
4. **Annotation-Free Rewards**: Tool-wise rewards provide process supervision without manual annotation

## Key Findings

- Even GPT-5 achieves below 70% success rate on the benchmark
- Two major failure modes:
  - Cascading errors from preference hallucination
  - Insufficient verification of product attributes against user requirements
- Fine-tuned 4B model consistently outperforms stronger baselines in preference capture and task performance
- Reward design is critical for long-horizon task success

## Implications

For consumers, this shows that even state-of-the-art models struggle with long-horizon shopping tasks. Preference hallucination is a key failure mode that could lead to recommendations that drift from user needs over extended interactions.

## Citations

- Paper: [[arXiv:2603.14864]](https://arxiv.org/abs/2603.14864)
