---
title: "LORE: A Large Generative Model for Search Relevance"
type: summary
date: 2026-08-03
source_url: https://arxiv.org/abs/2512.03025
authors:
  - Chenji Lu
  - Zhuo Chen
  - Hui Zhao
  - Zhiyuan Zeng
  - Gang Zhao
  - Junjie Ren
  - Ruicong Xu
  - Haoran Li
  - Songyan Liu
tags:
  - search-relevance
  - search-manipulation
  - search-optimization
  - chain-of-thought
  - rl-alignment
---

# LORE: A Large Generative Model for Search Relevance

## Paper Details

- **arXiv ID:** 2512.03025
- **Authors:** Chenji Lu, Zhuo Chen, Hui Zhao, Zhiyuan Zeng, Gang Zhao, Junjie Ren, Ruicong Xu, Haoran Li, Songyan Liu
- **Source URL:** https://arxiv.org/abs/2512.03025
- **Date:** December 2025

## Summary

LORE is a systematic framework for Large Generative Model-based relevance in e-commerce search. Deployed over three years, achieving cumulative +27% improvement in online GoodRate metrics. Key insights:
1. Relevance comprises distinct capabilities: knowledge/reasoning, multi-modal matching, and rule adherence.
2. Two-stage training: progressive CoT synthesis via SFT + human preference alignment via RL.
3. Comprehensive benchmark (RAIR) for evaluating core capabilities.
4. Query frequency-stratified deployment strategy.

## Consumer Harm Implications

- **Search result manipulation:** LLM-based relevance optimization creates new attack surfaces for search manipulation beyond traditional SEO.
- **Rule adherence opacity:** When search relevance is optimized via RL and human preference alignment, consumers cannot audit why certain results rank higher.
- **Feedback loop risk:** Query frequency-stratified deployment may create visibility bias where popular queries get better relevance, reinforcing existing inequalities.

## Connection to Other Wiki Entries

- [[agentic-commerce-research-2026]]
- search-manipulation
- search-optimization
- ranking-opacity

## Key Findings

- +27% cumulative improvement in online GoodRate metrics over 3 years.
- Qualitative-driven decomposition of relevance breaks through CoT performance ceilings.
- LORE provides complete blueprint for LLM relevance lifecycle in e-commerce.
