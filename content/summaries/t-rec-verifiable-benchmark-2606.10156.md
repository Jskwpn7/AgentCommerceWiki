---
title: "τ-Rec: A Verifiable Benchmark for Agentic Recommender Systems"
type: summary
date: 2026-08-03
source_url: https://arxiv.org/abs/2606.10156
authors:
  - Bharath Sivaram Narasimhan
  - Karthik R Narasimhan
tags:
  - benchmark
  - recommendation
  - verifiable
  - agentic
  - multi-turn
  - passk-metric
summary: |
  Introduces τ-Rec, a benchmark for agentic recommender systems that replaces subjective "LLM-as-a-judge" evaluation with verifiable rewards and a reveal-tagged elicitation (RTE) mechanism. Tests agents against structured catalog predicates with pass^k reliability metric. Finding: even best models achieve only ~57% at pass^1 and ~35% at pass^4.
concepts:
  - agentic-recommender
  - verifiable-evaluation
  - benchmark
  - llm-judge
---

## Overview

τ-Rec addresses a critical gap in evaluating agentic recommender systems: current benchmarks rely on subjective LLM-as-a-judge evaluations that introduce inconsistency and high costs.

## Key Contributions

1. **Verifiable Rewards**: Replaces subjective scoring with objective, verifiable evaluation criteria
2. **Reveal-Tagged Elicitation (RTE)**: Controls how task constraints surface during dialogue
3. **Pass^k Metric**: Systematic test for consistent reasoning across multiple attempts
4. **Large-Scale Evaluation**: Tests 9 configurations across 5 model families (GPT-5.4, Claude Sonnet 4.6, Gemini 2.5 Flash, DeepSeek V4 Flash, Qwen3-32B, GPT-5 mini)

## Critical Finding

A steep reliability cliff exists in conversational agent deployment:
- Best model: ~57% success at pass^1
- Drops to ~35% at pass^4
- Highlights critical gap in current conversational agent reliability

## Implications

This benchmark reveals that even frontier models struggle with consistent reasoning in multi-turn recommendation dialogues. For consumers, this means agentic recommenders may produce unreliable or inconsistent recommendations across different interactions.

## Citations

- Paper: [[arXiv:2606.10156]](https://arxiv.org/abs/2606.10156)
- Code: [github.com/nbharaths/tau-rec](https://github.com/nbharaths/tau-rec)
