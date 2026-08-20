---
title: "Recommender AI Agent: Integrating Large Language Models for Interactive Recommendations"
type: summary
date: 2026-08-03
source_url: https://arxiv.org/abs/2308.16505
authors:
  - Xu Huang
  - Jianxun Lian
  - Yuxuan Lei
  - Jing Yao
  - Defu Lian
  - Xing Xie
tags:
  - recommender-agent
  - llm-integration
  - interactive-recommendation
  - domain-knowledge
  - conversational-rec
  - fine-tuning
summary: |
  Introduces Recommender AI Agent integrating LLMs with domain-specific recommender models. Addresses the tradeoff between LLM general capabilities and recommender system domain expertise. Proposes approach where LLMs handle conversation and explanation while domain-specific models handle item ranking, avoiding expensive fine-tuning for each domain.
concepts:
  - recommender-agent
  - [[llm-recommender-survey-2502.10050]]
  - interactive-rec
  - domain-knowledge
  - conversational-recommendation
---

## Overview

This paper addresses the complementary strengths and weaknesses of recommender models (domain expertise, lightweight) and LLMs (general intelligence, conversation) by integrating them into a unified Recommender AI Agent.

## Key Contributions

1. **Hybrid Architecture**: Combines domain-specific recommender models with LLM conversational capabilities
2. **Division of Labor**: Recommender models handle item ranking; LLMs handle conversation, explanation, and commonsense reasoning
3. **Efficiency**: Avoids expensive domain-specific fine-tuning by leveraging pre-trained LLMs for interaction
4. **Domain Adaptation**: Framework adaptable to different recommendation domains

## Architecture

- **Recommender Module**: Leverages extensive user behavior data for domain-specific item recommendations
- **LLM Module**: Handles instruction comprehension, commonsense reasoning, and human interaction
- **Integration Layer**: Routes between domain-specific expertise and general intelligence

## Implications for Consumer Protection

- **Transparency**: Hybrid systems make it harder for consumers to understand how recommendations are generated
- **Accountability**: When recommendations are harmful, difficulty determining whether error came from recommender or LLM
- **Data Usage**: Extensive user behavior data collection for recommender module raises privacy concerns
- **Black Box**: Combined systems are more opaque than individual components

## Citations

- Paper: [[arXiv:2308.16505]](https://arxiv.org/abs/2308.16505)
