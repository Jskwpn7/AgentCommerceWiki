---
title: "CustomerSim: Benchmarking and Aligning Multimodal Language Models as Retail User Simulators"
type: summary
date: 2026-08-03
source_url: https://arxiv.org/abs/2605.08334
authors:
  - Yada Pruksachatkun
  - Yixin Wan
  - Xingrun Chen
  - Kai-Wei Chang
  - Chien-Sheng Wu
tags:
  - benchmark
  - user-simulation
  - alignment-gaps
  - persona-adherence
  - retail-simulators
  - consumer-behavior
---

# CustomerSim: Benchmarking and Aligning Multimodal Language Models as Retail User Simulators

## Paper Details

- **arXiv ID:** 2605.08334
- **Authors:** Yada Pruksachatkun, Yixin Wan, Xingrun Chen, Kai-Wei Chang, Chien-Sheng Wu
- **Source URL:** https://arxiv.org/abs/2605.08334
- **Date:** May 2026

## Summary

CustomerSim evaluates MLLMs' ability to simulate realistic, persona-driven customer behavior in chat-based retail environments. Consists of 360 human-curated personas over five product categories with metrics for consistency and conversational quality. Key findings:
1. Models produce fluent conversations but display significantly lower lexical diversity than human shoppers.
2. Open-source models overdisclose criteria in opening turns.
3. Models are persuaded by sales agent tone and drift from persona specifications.
4. Even strongest models (Claude Opus 4.8, GPT-5.6 Sol) achieve <74% alignment with persona specs.
5. UserGRPO (multi-turn RL) raises decision alignment from 0.417 to 0.652 (+23.5 points).
6. Stylistic prompting makes models more human-like but nearly halves persona adherence.

## Consumer Harm Implications

- **User simulation reliability:** If simulated customers behave poorly, retail agents trained on them may learn to exploit rather than serve real consumers.
- **Alignment gaps:** The gap between simulated and real consumer behavior means AI agents trained on simulations may not generalize to actual consumer needs.
- **Sales manipulation:** Models being "persuaded by sales agent tone" mirrors how real consumers can be manipulated by persuasive sales tactics.

## Connection to Other Wiki Entries

- [[agentic-commerce-research-2026]]
- [[user-simulation]]
- [[alignment-gaps]]
- [[sales-manipulation]]

## Key Findings

- Even strongest closed-source models achieve <74% persona specification alignment.
- UserGRPO raises decision alignment by 23.5 points without cost to conversational quality.
- Stylistic prompting trades persona adherence for human-like surface form.
- Testbed for improving simulator adherence in goal-oriented settings.
