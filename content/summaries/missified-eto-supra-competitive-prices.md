---
title: "Misspecified Estimate-then-Optimize Leads to Supra-Competitive Prices"
type: research-summary
source: arXiv:2605.16064v2
authors: Jackie Baek, Vivek F. Farias, Farrell Wu
affiliation: Stanford GSB
date: 2026-05-15
status: live
priority: medium-lower
tags: [algorithmic-pricing, estimate-then-optimize, supra-competitive-prices, misspecified-demand, algorithmic-collusion, multi-firm-markets, pricing-dynamics]
aliases: [missified-eto]
related: [algorithmic-collusion-pricing, ai-agents-in-markets, systemic-fragility-in-ai-economies]
raw_page: [[raw/papers/missified-eto-supra-competitive-prices-2605.16064.md]]
provenance:
  source_url: https://arxiv.org/abs/2605.16064
  source_pdf: https://arxiv.org/pdf/2605.16064
  ingested_by: cron-weekly-pipeline
  ingested_at: "2026-06-23"
---

# Misspecified Estimate-then-Optimize Leads to Supra-Competitive Prices

> **arXiv:** 2605.16064v2 [cs.GT, cs.AI, econ.TH] — 15 May 2026
> **Authors:** Jackie Baek, Vivek F. Farias, Farrell Wu (Stanford GSB)

## TL;DR

Firms that price using a **simple algorithmic rule** — estimating demand from their own price/sales history and optimizing prices to maximize estimated profit — can systematically produce **collusive-like prices even without any communication or explicit agreement**. The key mechanism is demand model misspecification: when firms omit competitors' prices from their demand model, their pricing dynamics converge to supra-competitive prices. This is a form of **non-collusive collusion** — prices are high without any human cartel formation.

## Core Mechanism

The paper models firms using a **myopic estimate-then-optimize rule**:

1. Each firm fits a demand model to its own price and sales history
2. The demand model is **misspecified** — it omits competitors' prices
3. Firms set the price that maximizes estimated profit based on this misspecified model
4. After an initial exploration phase of random prices, the rule drives prices toward supra-competitive levels

## Key Findings

- **Convergence to supra-competitive prices**: The misspecified demand model systematically overestimates demand elasticity at competitive prices and underestimates it at high prices, creating a self-reinforcing dynamic that pushes prices upward
- **No communication required**: This outcome emerges purely from each firm's independent use of a simple, common pricing algorithm — no explicit agreement or communication between firms
- **Initialization matters**: The process requires an initial exploration phase of independent random prices to get started, but once initiated, the convergence is stable
- **Real-world relevance**: This mechanism is directly relevant to modern online pricing systems that use simple ML models to set prices based on historical sales data

## Consumer Harm Implications

- **Prices can be higher without anyone breaking the law**: Traditional antitrust frameworks require evidence of communication or agreement; this paper shows supra-competitive prices can emerge without either
- **Simple algorithms, big impact**: The pricing rule is very simple — firms don't need sophisticated AI to produce consumer-harmful outcomes
- **Systematic and predictable**: The paper provides theoretical analysis showing this is not a偶然 outcome but a systematic property of the misspecified model class
- **Monitoring challenge**: Regulators cannot detect this by looking for communication or price-matching signals — the harm emerges from algorithmic decision-making alone

## Connection to Related Research

- Links to [[algorithmic-collusion-pricing]] (which studies similar mechanisms in broader contexts)
- Relevant to [[ai-agents-in-markets]] (autonomous pricing agents face similar dynamics)
- Connects to [[systemic-fragility-in-ai-economies]] (systemic price fragility through simple algorithmic rules)
- The [[voluntary-collusion-with-secret-tools-in-competing-llm-agents]] paper shows the complementary case where agents *choose* to collude, whereas this shows they can produce collusive prices *without choosing to*

## Relevance to UK Context

- UK CMA should monitor pricing algorithms in retail, energy, and telecoms for convergence to supra-competitive prices
- The "misspecified model" mechanism is particularly concerning because it arises from simple, commonly-deployed pricing rules
- CMA's existing work on algorithms and competition should be extended to cover this non-communication-based mechanism
- Relevant to UK competition law's approach to "concerted practice" — current frameworks may not capture algorithm-driven price convergence

## Limitations

- The model is simplified (symmetric firms, homogeneous products, myopic optimization)
- Real-world pricing systems are more complex than the model assumes
- The paper focuses on theoretical analysis rather than empirical validation
- The initial random price phase may not reflect real-world deployment scenarios

## Raw Source

Full extracted text is archived at [[raw/papers/missified-eto-supra-competitive-prices-2605.16064.md]].
