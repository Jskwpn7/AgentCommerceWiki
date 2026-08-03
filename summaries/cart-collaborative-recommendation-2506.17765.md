---
title: "CARTS: Collaborative Agents for Recommendation Textual Summarization"
type: summary
date: 2026-08-03
source_url: https://arxiv.org/abs/2506.17765
authors:
  - Jiao Chen
  - Kehui Yao
  - Reza Yousefi Maragheh
  - Kai Zhao
  - Jianpeng Xu
  - Jason Cho
  - Evren Korpeoglu
tags:
  - recommendation-agents
  - multi-agent-systems
  - recommendation-manipulation
  - hidden-preferences
---

# CARTS: Collaborative Agents for Recommendation Textual Summarization

## Paper Details

- **arXiv ID:** 2506.17765
- **Authors:** Jiao Chen, Kehui Yao, Reza Yousefi Maragheh, Kai Zhao, Jianpeng Xu, Jason Cho, Evren Korpeoglu
- **Source URL:** https://arxiv.org/abs/2506.17765
- **Date:** June 2025

## Summary

CARTS (Collaborative Agents for Recommendation Textual Summarization) is a multi-agent LLM framework designed for structured summarization in recommendation systems. It decomposes the task into three stages: Generation Augmented Generation (GAG), refinement circle, and arbitration, with successive agent roles responsible for extracting salient item features, iteratively refining candidate titles, and selecting final titles through collaborative arbitration.

## Consumer Harm Implications

- **Hidden preferences:** Agent-generated summaries may obscure product differences that human review would reveal.
- **Recommendation manipulation:** The collaborative arbitration process is not transparent to consumers — they cannot understand how final recommendations were selected from candidate sets.
- **Consumer deception:** A/B testing showed improved engagement metrics, but this may reflect persuasive rather than informative summaries.

## Connection to Other Wiki Entries

- [[agentic-commerce-research-2026]]
- [[recommendation-manipulation]]
- [[hidden-preferences]]
- [[platform-agent-asymmetry]]

## Key Findings

- CARTS significantly outperforms single-pass and chain-of-thought LLM baselines.
- Live A/B testing on large-scale e-commerce data showed higher title relevance and improved user engagement metrics.
- The three-stage decomposition (GAG, refinement, arbitration) enables iterative improvement over single-pass approaches.
