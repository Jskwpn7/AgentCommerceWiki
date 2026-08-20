---
title: "Iterating Toward Better Search: A Two-Agent Simulation Framework for Evaluating Agentic Search Architectures in E-Commerce"
type: summary
date: 2026-08-03
source_url: https://arxiv.org/abs/2606.12924
authors:
  - Jetlir Duraj
  - Jayanth Yetukuri
  - Shuang Zhou
  - Dhruv Varma
  - Rui Kong
  - Ishita Khan
  - Qunzhi Zhou
tags:
  - simulation
  - search
  - agentic
  - e-commerce
  - buyer-agent
  - memory
  - persona
summary: |
  Introduces a modular two-agent simulation framework for evaluating conversational shopping assistant architectures. Uses 2011 conversations across 14 persona buckets. Finds rolling-window memory outperforms intent-extraction memory (35% faster). Reduces failure rates by 62% through targeted fixes. Documents systematic disagreement between LLM judges (Gemini rewards process, Claude demands outcomes).
concepts:
  - simulated-search
  - buyer-agent
  - memory-mechanisms
  - llm-judge
---

## Overview

This paper presents a framework for systematically evaluating conversational shopping assistant architectures through controlled two-agent simulation.

## Key Contributions

1. **Modular Two-Agent Framework**: Independent buyer agent (with personas, missions, patience levels) paired with interchangeable responder agents
2. **Controlled Comparison**: Holding buyer constant enables testing different responder designs on identical scenarios
3. **Real E-commerce Integration**: Responder integrates with actual e-commerce search APIs

## Key Findings (from 2011 conversations, 14 personas)

1. **Memory Architecture**: Rolling-window memory outperforms intent-extraction memory on all quality metrics, 35% faster per query
2. **Failure Analysis**: Systematic failure analysis reduced failure/near-failure rates by 62%
3. **LLM Backbone Impact**: Swapping from Gemini 2.5 to Llama 3.3 70B costs only 0.16-0.45 points despite identical architecture
4. **Judge Disagreement**: Gemini rewards process correctness while Claude demands concrete outcomes, despite identical evaluation prompts

## Implications

The framework enables rapid iteration on shopping assistant designs. The finding about judge disagreement suggests evaluation methods may bias toward certain architectural patterns, potentially affecting which systems get deployed.

## Citations

- Paper: [[arXiv:2606.12924]](https://arxiv.org/abs/2606.12924)
