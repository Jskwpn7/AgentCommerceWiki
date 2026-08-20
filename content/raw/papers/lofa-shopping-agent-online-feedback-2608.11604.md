---
title: "Learning from Online User Feedback for Shopping Agents"
type: raw
source_url: https://arxiv.org/abs/2608.11604
ingested: 2026-08-17
tags:
  - agentic-ai
  - academic
  - agentic-commerce
---

# Learning from Online User Feedback for Shopping Agents

arXiv:2608.11604 — 12 Aug 2026

**Authors:** Zhang, Haobo, Mao, Kelong, Xu, Sulong, Gu, Simiu, Dou, Zhicheng

## Abstract (verbatim from arXiv)

Large language model-based shopping agents are increasingly deployed in real-world e-commerce platforms, generating massive amounts of user interaction logs that provide valuable supervision for improving these agents. However, existing approaches primarily rely on offline training signals, such as user-item interactions or synthetic preference data, while largely overlooking the rich supervision contained in users' natural conversational feedback. Moreover, the available online feedback is heterogeneous, sparse, and noisy, making it difficult to transform into reliable learning signals automatically. To address these challenges, we propose LOFA, a framework that enables shopping agents to learn directly from real online interaction logs without human annotation. LOFA combines reinforcement learning over verifiable purchase outcomes with feedback-aware on-policy distillation, which identifies users'in-dialogue directives and converts them into dense token-level supervision. These complementary objectives capture both collaborative behavioral patterns and user-specific preferences. Extensive experiments on real-world e-commerce logs demonstrate that LOFA consistently improves recommendation quality, response helpfulness, and user-satisfaction alignment over strong baselines, highlighting the effectiveness of learning shopping agents from real online user feedback.
