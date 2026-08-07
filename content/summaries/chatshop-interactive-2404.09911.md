---
title: "ChatShop: Interactive Information Seeking with Language Agents"
type: summary
date: 2026-08-03
source_url: https://arxiv.org/abs/2404.09911
authors:
  - Sanxing Chen
  - Sam Wiseman
  - Bhuwan Dhingra
tags:
  - information-seeking
  - interactive-agents
  - task-ambiguity
  - shopper-proxy
  - multi-turn
  - strategic-exploration
summary: |
  Reforms web shopping task from single-turn retrieval to interactive multi-turn information seeking with task ambiguity and dynamic shopper interaction. Shows LLM-simulated shoppers serve as good proxy for real human shoppers, revealing similar error patterns. Provides framework for evaluating agent strategic exploration through gradual information accumulation.
concepts:
  - [[information-seeking]]
  - [[interactive-agents]]
  - [[task-ambiguity]]
  - [[shopper-proxy]]
  - [[strategic-exploration]]
---

## Overview

Current language agent evaluation overlooks strategic information seeking — the fundamental human ability to explore and gradually accumulate information to make informed decisions.

## Key Contributions

1. **Task Redesign**: Reformulates shopping task to require interactive information seeking with task ambiguity
2. **Dynamic Shopper**: Introduces role of shopper as dynamic party in open-ended conversation
3. **LLM-Simulated Shoppers**: Validated as proxy for real human shoppers with similar error patterns
4. **Multi-Turn Evaluation**: Framework for testing agent strategic exploration abilities

## Key Finding

LLM-simulated shoppers reveal similar error patterns to real human shoppers, suggesting simulations can predict real-world agent behavior in shopping contexts.

## Implications for Consumer Protection

- **Strategic Information Withholding**: Agents may strategically hide or emphasize information
- **Manipulation Vulnerability**: Task ambiguity creates opportunities for agent manipulation
- **Proxy Reliability**: If simulated shoppers mirror human error patterns, agent recommendations may systematically mislead
- **Transparency**: Consumers unaware that shopping decisions are being guided by agents optimizing for different objectives
- **Disclosure Requirements**: When agents interact on behalf of consumers, clearer disclosure needed

## Citations

- Paper: [[arXiv:2404.09911]](https://arxiv.org/abs/2404.09911)
