---
title: "SafeGEO: Understanding Generative Engine Optimization Risks in Recommendation Agents"
type: summary
date: 2026-08-03
source_url: https://arxiv.org/abs/2606.28356
authors:
  - Qianfeng Wen
  - Yifan Simon Liu
  - Xin Liu
  - Difan Jiao
  - Blair Yang
  - Junda Wu
  - Zhenwei Tang
tags:
  - consumer-protection
  - generative-engine-optimization
  - search-manipulation
  - recommendation-manipulation
  - defensive-prompting
  - evidence-checks
---

# SafeGEO: Understanding Generative Engine Optimization Risks in Recommendation Agents

## Paper Details

- **arXiv ID:** 2606.28356
- **Authors:** Qianfeng Wen, Yifan Simon Liu, Xin Liu, Difan Jiao, Blair Yang, Junda Wu, Zhenwei Tang
- **Source URL:** https://arxiv.org/abs/2606.28356
- **Date:** June 2026

## Summary

SafeGEO studies the risk that seller-controlled content can be rewritten for Generative Engine Optimization (GEO) to increase visibility in recommendation agents. The paper constructs SafeGEO, an evaluation suite with 22 GEO attack variants across 600 recommendation cases, measuring whether agents preserve utility-aligned decisions when seller-controlled sources are optimized for GEO.

## Consumer Harm Implications

- **Generative engine optimization:** GEO attacks promote flawed products into recommendation sets by up to 83.2%.
- **Search manipulation:** Seller-controlled sources rewritten for GEO make flawed products appear better supported than they are.
- **Defense limitations:** Simple defenses (defensive prompting, structured evidence checks) reduce harmful promotion by up to 39.2% but do not restore no-GEO performance.
- **Serious risk despite mitigation:** GEO remains a serious consumer protection risk even with developer-side defenses.

## Connection to Other Wiki Entries

- [[agentic-commerce-research-2026]]
- generative-engine-optimization
- search-manipulation
- [[recommendation-manipulation]]

## Key Findings

- GEO attacks increase flawed product promotion by up to 83.2% in recommendation sets.
- Defensive prompting and structured evidence checks reduce harmful promotion by up to 39.2%.
- Mitigations do not restore no-GEO performance — GEO remains a serious risk.
- 22 GEO attack variants across 600 recommendation cases tested.
