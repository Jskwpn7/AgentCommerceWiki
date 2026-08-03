---
title: "LLM Agent Meets Agentic AI: Can LLM Agents Simulate Customers to Evaluate Agentic-AI-based Shopping Assistants?"
type: summary
date: 2026-08-03
source_url: https://arxiv.org/abs/2509.21501
authors:
  - Lu Sun
  - Shihan Fu
  - Bingsheng Yao
  - Yuxuan Lu
  - Wenbo Li
  - Hansu Gu
  - Jiri Gesi
  - Jing Huang
  - Chen Luo
tags:
  - llm-agent
  - user-simulation
  - evaluation
  - shopping-assistants
  - amazon-rufus
  - digital-twin
  - multi-turn
  - ux-feedback
summary: |
  Evaluates whether LLM agents can simulate real customers to test agentic AI shopping assistants. Compares 40 human participants shopping with Amazon Rufus against digital twins created from their interaction traces. Finds agents explore more diverse choices but action patterns align with humans and yield similar design feedback. First study to quantify how closely LLM agents mirror human multi-turn interaction with agentic AI systems.
concepts:
  - [[user-simulation]]
  - [[llm-as-digital-twin]]
  - [[amazon-rufus]]
  - [[agentic-shopping-assistant]]
---

## Overview

This paper introduces a framework for using LLM agents as digital twins of real customers to evaluate agentic AI shopping assistants. As agentic AI systems evolve rapidly, traditional human evaluation becomes impractical at scale.

## Key Contributions

1. **Human Data Collection**: 40 participants shopped with Amazon Rufus, with personas, interaction traces, and UX feedback recorded
2. **Digital Twin Creation**: LLM agents created from real human data to repeat shopping tasks
3. **Quantitative Comparison**: Pairwise comparison of human and digital-twin traces showing alignment in action patterns and design feedback
4. **Methodology**: First study to quantify how closely LLM agents can mirror human multi-turn interaction

## Findings

- LLM agents often explored more diverse choices than humans
- Action patterns between humans and agents aligned well
- Agents yielded similar design feedback as humans
- Demonstrates potential for scalable evaluation of shopping assistants

## Implications

This research has implications for consumer protection as it enables testing shopping assistants at scale without requiring hundreds of human participants. Digital twin evaluation could identify problematic agent behaviors before deployment.

## Citations

- Paper: [[arXiv:2509.21501]](https://arxiv.org/abs/2509.21501)
- Related: [[ecomagentbench-shopping-agents]](./ecomagentbench-shopping-agents-2606.17698)
