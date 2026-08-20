---
title: "ComboShoppingBench: Budget-Constrained Basket Shopping with Coupons"
created: 2026-08-17
updated: 2026-08-17
type: summary
tags: [agentic-ai, academic, digital-platforms, retail, methodology]
sources: ["https://arxiv.org/abs/2608.09282"]
confidence: high
---

# ComboShoppingBench: Budget-Constrained Basket Shopping with Coupons

**Paper:** arXiv:2608.09282 — "ComboShoppingBench: Evaluating LLM Agents for Budget-Constrained Basket Shopping with Coupons"
**Authors:** Adrian Li, Kelong Mao, Yudong Guo, Heming Xia, Xinwei Yang, Lirui Luo, Jace Wong, Pu Yao, Sulong Xu, Simiu Gu
**Published:** 10 August 2026
**Primary Source:** [arxiv.org/abs/2608.09282](https://arxiv.org/abs/2608.09282)

## Overview

Real-world shopping often requires constructing a *basket* of complementary items rather than retrieving a single product — device setup, meal preparation, event planning, group takeout. Such "combo-shopping" tasks require joint reasoning about item compatibility, availability, store-level requirements, delivery fees, coupons, and budgets.

Evaluation is hard for two reasons: (a) **multiple baskets may satisfy the same request**, so exact-match metrics are unsuitable; and (b) semantic evaluation alone cannot detect infeasible orders, invalid coupon combinations, or incorrect payments.

## The Benchmark

**ComboShoppingBench** is an agentic shopping benchmark for open-ended yet verifiable basket construction in a simulated commerce and takeout environment.

- **Task synthesis.** An exploration agent first constructs a feasible, semantically coherent basket of purchasable products. This *witness* guides generation of coupons, budget constraints, user queries, and aligned evaluation rubrics.
- **Two-pronged evaluation.** LLM judges assess semantic satisfaction, response quality, and claim faithfulness; deterministic validation checks product-ID validity, budget compliance, and coupon optimality.

Experiments with diverse LLM agents show that even strong agents struggle on ComboShoppingBench, highlighting substantial room for improvement in reliable, constraint-aware combo shopping.

## Consumer Harm Implications

- **Measuring how well agents spend consumer money.** This is the first dedicated benchmark for the competence of agents that would actually *spend a consumer's money* on a multi-item basket. Competence gains and liability exposure rise together: as agents become more competent at building "reasonable" baskets, those baskets become legally harder to challenge.
- **Coupon/bundle optimisation risk.** Automated optimisation across coupons, bundles, and store minimums raises the risk of exploiting merchant pricing errors (cf. the Reg E error-pricing scenario) and of steering consumers into higher-margin basket configurations.
- **Constraint-awareness failures.** Infeasible or invalid-basket failures (wrong product IDs, broken coupon combos, budget breaches) are exactly the class of error that, when it occurs at scale in production, produces unauthorised or disputed charges.

## Relevance to UK Consumer Harms

ComboShoppingBench provides the empirical baseline for judging whether a delegated basket purchase was "reasonable" — a question the Consumer Rights Act 2015 and CPRs 2008 have not been designed to answer for agent-mediated purchases. It directly extends the benchmarking thread in [[ai-shopping-agents]] and connects to [[agentic-commerce-protocols]] (the protocols that would execute these baskets) and to [[agent-liability]] (who is responsible when the basket is wrong).

## Cross-References

- [[ai-shopping-agents]] — first benchmark for basket-shopping competence
- [[agentic-commerce-protocols]] — protocols that execute agent-built baskets
- [[agent-liability]] — competence gains and liability exposure rise together
- [[conflict-of-interest-in-llm-deployment]] — bundle optimisation can steer toward higher-margin configurations
- [[agentic-commerce-research-2026]] — shopping-agent research digest

## References

1. arXiv:2608.09282 — *ComboShoppingBench: Evaluating LLM Agents for Budget-Constrained Basket Shopping with Coupons*
