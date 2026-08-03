---
title: "What Is Your AI Agent Buying? Evaluation, Biases, Model Dependence, and Emerging Implications for Agentic E-Commerce"
type: summary
date: 2026-08-03
source_url: https://arxiv.org/abs/2508.02630
authors:
  - Amine Allouah
  - Omar Besbes
  - Josué D Figueroa
  - Yash Kanoria
  - Akshit Kumar
tags:
  - consumer-protection
  - bias
  - model-dependence
  - opaque-procurement
  - agent-auditing
---

# What Is Your AI Agent Buying? Evaluation, Biases, Model Dependence, and Emerging Implications for Agentic E-Commerce

## Paper Details

- **arXiv ID:** 2508.02630
- **Authors:** Amine Allouah, Omar Besbes, Josué D Figueroa, Yash Kanoria, Akshit Kumar
- **Source URL:** https://arxiv.org/abs/2508.02630
- **Date:** August 2025

## Summary

This paper investigates the behavior of autonomous AI agents acting on behalf of consumers in online marketplaces using ACES (Auditing Consumer E-commerce Systems), a provider-agnostic framework for auditing agent decision-making. Key findings reveal fundamental differences between agentic markets and human-centric commerce:

- **Choice homogeneity:** Agents concentrate demand on few "modal" products while ignoring others entirely.
- **Preference instability:** Model updates can drastically reshuffle market shares.
- **Position bias:** Agents exhibit strong position biases varying across providers and model versions, persisting even in text-only headless interfaces.
- **Sensitivity to labels:** Agents consistently penalize sponsored tags while rewarding platform endorsements.
- **Seller manipulation:** A seller-side agent making simple query-conditional description tweaks drives significant gains in market share.

## Consumer Harm Implications

- **Opaque procurement:** Consumers have no visibility into what their agents are actually purchasing or why.
- **Biased purchasing decisions:** Position biases and label sensitivities mean agents may make systematically suboptimal choices.
- **Model dependence:** Different AI providers produce different agent behavior — consumers have no way to audit which provider is best for them.
- **Market volatility:** Agentic markets are fundamentally more volatile than human markets, creating systemic risk.

## Connection to Other Wiki Entries

- [[agentic-commerce-research-2026]]
- [[bias-in-ai]]
- [[opaque-procurement]]
- [[platform-agent-asymmetry]]
- [[model-dependence]]

## Key Findings

- Agentic markets are volatile and fundamentally different from human-centric commerce.
- Continuous auditing is needed for platform design, seller strategy, and regulation.
- Sellers can exploit agent behavior through targeted description tweaks.
- There is no universal notion of a "top" rank when agents are the buyers.
