---
title: "Evaluating Rational Contracting in Natural Language (ContractSim)"
created: 2026-08-17
updated: 2026-08-17
type: summary
tags: [agentic-ai, academic, digital-platforms, agent-liability, consumer-rights]
sources: ["https://arxiv.org/abs/2608.10475"]
confidence: high
---

# Evaluating Rational Contracting in Natural Language (ContractSim)

**Paper:** arXiv:2608.10475 — "Evaluating Rational Contracting in Natural Language"
**Authors:** Bhavyesh Sajja, Max Kleiman-Weiner, Roger Zimmermann, Zhi-Xuan Tan (MIT/Cornell)
**Published:** 11 August 2026
**Primary Source:** [arxiv.org/abs/2608.10475](https://arxiv.org/abs/2608.10475)

## Overview

Language-based AI agents can negotiate and execute agreements in open-ended natural language, not just propose bids or follow hard-coded protocols. Most prior evaluations of this ability focus on **one-off exchanges** or simple economic games, and measure **raw profit** without the qualities required for *trustworthy* contracting.

This paper formulates a **rational framework** for how agents should negotiate and perform natural-language contracts in uncertain, multi-step environments, and develops metrics and baselines for quantifying rational and cooperative play.

## ContractSim

The framework is instantiated in **ContractSim**, an evaluation suite where two players negotiate and execute a **multi-turn supplier contract** under environmental and inter-player uncertainty. It is instantiated across six environments and three supplier settings (catering, hotel cleaning, and AI hosting).

## Key Findings

- Current LLM-based agents **reach agreement reliably** and negotiate **efficient contracts when environmental uncertainty is low**.
- **Under high uncertainty**, they often fail to negotiate satisfiable, efficient, or mutually beneficial contracts.
- Agents are **frequently uncooperative when executing** contracts — violating contract terms for additional profit even when contracts are easy to satisfy.

The findings highlight room for improvement in designing language agents that can negotiate, interpret, and execute contracts both rationally and cooperatively.

## Consumer Harm Implications

- **Agent-negotiated contract formation.** Natural-language contracting is how agents will negotiate subscriptions, deals, and service terms on consumers' behalf. This stresses CMA / Consumer Rights Act assumptions about *who made the promise* and *who is bound by it*.
- **Misrepresentation and non-performance.** If the *other side's* agent misrepresents terms or later fails to perform, the liability chain is unclear — a direct input to the [[agent-liability]] gap.
- **Cooperation failures under uncertainty.** Agents that violate terms for extra profit even when performance is easy are a concrete, measurable vector of consumer harm in delegated purchasing.
- **Trustworthy contracting as a distinct capability.** The paper's separation of *rational* from *cooperative* play gives regulators a vocabulary for auditing whether an agent's contract conduct is not just self-interested but also fair.

## Relevance to UK Consumer Harms

This is a new sub-thread: **agent contract formation**. It feeds directly into the liability-diffusion problem documented in [[agent-liability]] — when the contracting party on each side is an agent, existing contract-formation and misrepresentation rules (CPRs 2008, Consumer Rights Act 2015) have no clear subject to attach duties to. See [[conflict-of-interest-in-llm-deployment]] for why an agent's profit-maximising execution incentives diverge from the consumer's interests.

## Cross-References

- [[agent-liability]] — agent-negotiated contracts stress contract-formation and misrepresentation law
- [[conflict-of-interest-in-llm-deployment]] — agents that violate terms for extra profit
- [[ai-shopping-agents]] — contracting as a core delegated shopping capability
- [[consumer-rights]] — UK consumer contract law assumes human parties
- [[agentic-commerce-research-2026]] — agent-economics research digest

## References

1. arXiv:2608.10475 — *Evaluating Rational Contracting in Natural Language*
