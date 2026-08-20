---
title: "EComAgentBench: Benchmarking Shopping Agents on Long-Horizon Tasks with Distributed Hidden Intent"
type: summary
date: 2026-08-03
source_url: https://arxiv.org/abs/2606.17698
authors:
  - Zeyao Du
  - Tong Li
  - Yanci Zhang
  - Haibo Zhang
tags:
  - benchmark
  - hidden-intent
  - long-horizon
  - decision-chains
  - shopping-agents
  - amazon
---

# EComAgentBench: Benchmarking Shopping Agents on Long-Horizon Tasks with Distributed Hidden Intent

## Paper Details

- **arXiv ID:** 2606.17698
- **Authors:** Zeyao Du, Tong Li, Yanci Zhang, Haibo Zhang
- **Source URL:** https://arxiv.org/abs/2606.17698
- **Date:** June 2026

## Summary

EComAgentBench is a benchmark of 662 tasks grounded in real Amazon products and reviews. Each task scatters requirements across:
1. A visible query
2. A tool-gated profile
3. Scripted clarification

An agent must uncover hidden intent, verify candidates against attributes and review evidence, and commit to a single product within 100 tool calls. Typed, source-tagged rubrics grade every task, attributing each failure to a requirement and its source.

## Consumer Harm Implications

- **Hidden intent:** Agents may fail to uncover all consumer requirements, leading to purchases that don't match actual needs.
- **Opaque long-horizon decision chains:** Complex multi-step reasoning makes it impossible for consumers to audit agent decisions.
- **Low accuracy:** Even the strongest models attain only 57.1% overall accuracy — meaning most consumer-facing shopping agents are wrong more than half the time on complex tasks.
- **Rubric satisfaction degradation:** Performance drops significantly when requirements are hidden (e.g., in user profiles).

## Connection to Other Wiki Entries

- [[agentic-commerce-research-2026]]
- [[hidden-intent-agentic-shopping]]
- opaque-long-horizon-decisions
- shopping-agent-reliability

## Key Findings

- Even strongest models attain only 57.1% overall accuracy on long-horizon shopping tasks.
- Rubric satisfaction degrades from visible to hidden requirement sources.
- 662 tasks grounded in real Amazon products and reviews provide realistic evaluation.
- Construction is automated yet reliable with every answer fixed in code before text generation.
