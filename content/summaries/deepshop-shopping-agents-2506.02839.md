---
title: "DeepShop: A Benchmark for Deep Research Shopping Agents"
type: summary
date: 2026-08-03
source_url: https://arxiv.org/abs/2506.02839
authors:
  - Yougang Lyu
  - Xiaoyu Zhang
  - Lingyong Yan
  - Maarten de Rijke
  - Zhaochun Ren
  - Xiuying Chen
tags:
  - benchmark
  - shopping-agents
  - recommendation-manipulation
  - platform-agent-asymmetry
---

# DeepShop: A Benchmark for Deep Research Shopping Agents

## Paper Details

- **arXiv ID:** 2506.02839
- **Authors:** Yougang Lyu, Xiaoyu Zhang, Lingyong Yan, Maarten de Rijke, Zhaochun Ren, Xiuying Chen
- **Source URL:** https://arxiv.org/abs/2506.02839
- **Date:** June 2025

## Summary

Web agents for online shopping have shown promise in automating user interactions across e-commerce platforms, but existing benchmarks oversimplify the complexity of real-world shopping. DeepShop addresses this gap with a benchmark designed to evaluate web agents in complex, realistic online shopping environments.

## Key Contributions

1. **Query diversity evolution:** Starting from real user queries, generates diverse queries across five popular online shopping domains.
2. **Query complexity evolution:** Evolves queries to increase complexity considering product attributes, search filters, and sorting preferences, classified into three levels: easy, medium, and hard.
3. **Fine-grained and holistic evaluation:** Automated evaluation framework assessing agent performance on fine-grained aspects (product attributes, search filters, sorting preferences) and overall success rates.

## Consumer Harm Implications

- **Recommendation manipulation:** Agents operating on complex, multi-dimensional queries may be more easily manipulated by sellers who understand agent behavior patterns.
- **Platform-agent asymmetry:** The gap between agent capabilities and platform design creates information asymmetry that sellers can exploit.
- **Filter and sorting exploitation:** Low success rates on filters and sorting preferences suggest consumers relying on agents may receive suboptimal results without awareness.

## Connection to Other Wiki Entries

- [[agentic-commerce-research-2026]]
- [[platform-agent-asymmetry]]
- [[recommendation-manipulation]]
- generative-engine-optimization

## Key Findings

- RAG-based approaches struggle with complex queries due to lack of web interaction capabilities.
- Other methods face significant challenges with filters and sorting preferences, leading to low overall success rates.
- Cross-category and complexity-based evaluations reveal systematic gaps in agent performance.
