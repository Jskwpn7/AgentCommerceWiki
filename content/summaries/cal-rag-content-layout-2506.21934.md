---
title: "CAL-RAG: Retrieval-Augmented Multi-Agent Generation for Content-Aware Layout Design"
type: summary
date: 2026-08-03
source_url: https://arxiv.org/abs/2506.21934
authors:
  - Najmeh Forouzandehmehr
  - Reza Yousefi Maragheh
  - Sriram Kollipara
  - Kai Zhao
  - Topojoy Biswas
  - Evren Korpeoglu
  - Kannan Achan
tags:
  - ui-ux-layouts
  - dark-patterns
  - recommendation-manipulation
  - visual-coherence
---

# CAL-RAG: Retrieval-Augmented Multi-Agent Generation for Content-Aware Layout Design

## Paper Details

- **arXiv ID:** 2506.21934
- **Authors:** Najmeh Forouzandehmehr, Reza Yousefi Maragheh, Sriram Kollipara, Kai Zhao, Topojoy Biswas, Evren Korpeoglu, Kannan Achan
- **Source URL:** https://arxiv.org/abs/2506.21934
- **Date:** June 2025

## Summary

CAL-RAG is a retrieval-augmented, agentic framework for content-aware layout generation. It integrates multimodal retrieval, LLMs, and collaborative agentic reasoning to arrange visual elements (text, logos, underlays) on a background canvas. The system:
1. Retrieves relevant layout examples from a structured knowledge base
2. Invokes an LLM-based layout recommender to propose element placements
3. Uses a vision-language grader agent to evaluate layouts with visual metrics
4. A feedback agent provides targeted refinements for iterative improvement

## Consumer Harm Implications

- **Dark patterns in agent-generated layouts:** Automated layout generation could produce UI designs that subtly manipulate user behavior (e.g., hiding pricing, emphasizing misleading features).
- **Lack of visual coherence standards:** No regulatory framework governs agent-generated visual layouts in commerce.
- **Opacity of design choices:** Consumers cannot understand why a layout was presented in a particular way.

## Connection to Other Wiki Entries

- [[agentic-commerce-research-2026]]
- [[dark-pattern]]
- [[recommendation-manipulation]]
- [[platform-agent-asymmetry]]

## Key Findings

- CAL-RAG achieves state-of-the-art performance on PKU PosterLayout dataset.
- Outperforms strong baselines like LayoutPrompter across multiple layout metrics.
- Combines retrieval augmentation with agentic multi-step reasoning for scalable, interpretable layout generation.
