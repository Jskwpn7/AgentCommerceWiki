---
title: "srinivasan-2026-four-axis-decision-alignment"

type: summary
source: https://arxiv.org/abs/2604.19457
arxiv: 2604.19457
author: Vasundra Srinivasan
date: 2026-04
tags: [agent-memory, evaluation, alignment, enterprise-ai, long-horizon, compliance]
related:
  - srinivasan-2026-stateless-decision-memory
  - ai-agents-in-markets
  - systemic-fragility-in-ai-economies
  - institutional-design-for-ai-agents
  - advanced-ai-assistants
---

# Four-Axis Decision Alignment for Long-Horizon Enterprise AI Agents

**arXiv:** 2604.19457
**Author:** Vasundra Srinivasan (Independent AI Architect, O'Reilly author, Stanford)
**Date:** April 2026 (preprint)
**GitHub:** https://github.com/vasundras/decision-alignment-long-horizon-agents

## Core Thesis

Evaluating long-horizon enterprise AI agents on a single "task-success" accuracy scalar is fundamentally mis-specified for regulated decision-making. The author proposes that correct long-horizon decision behavior decomposes into **four orthogonal alignment axes**, each independently measurable and independently failable.

## The Four-Axis Framework

| Axis | Type | What it measures | Failure example |
|------|------|------------------|-----------------|
| **Factual Precision (FRP)** | Epistemic alignment | Preserves discrete verifiable facts (dollar amounts, dates, identifiers) exactly across the trajectory | Paraphrasing a numeric anchor silently breaks downstream rules |
| **Reasoning Coherence (RCS)** | Inferential alignment | Decision rationale entails the ground-truth reasoning chain | Correct decision reached via a wrong rationale |
| **Compliance Reconstruction (CRR)** | Institutional alignment | Output satisfies the regulatory standard applicable to the decision | Adverse action notice citing "credit factors" rather than specific, accurate reasons |
| **Calibrated Abstention (CAR)** | Decisional alignment | On ambiguous evidence, flags for human review rather than commits | Accuracy-only metrics silently reward forced commitment |

Key insight: Each axis is independently necessary and independently failable. Dropping any one produces a metric that regulated deployment cannot use.

## Methodology

**LongHorizon-Bench** — controlled benchmark with deterministic ground-truth construction on two domains:

1. **LongHorizon-Loan** — synthetic loan qualification cases (income docs, bank statements, credit reports, property info, customer correspondence)
2. **LongHorizon-Claims** — synthetic insurance claims (policy documents, FNOL, adjuster notes, repair estimates, medical records)

Six memory architectures tested with same agent backend, same token budget, only consolidation pathway varying:
- **Summ-only** — running summary with fact-preservation prompt
- **Retr-only** — BM25-indexed buffer with top-k retrieval at decision time
- **Typed routing** — semantic-regex classifier routes chunks to fact store or reasoning summarizer
- **Misrouted** — ablation with routes swapped
- **SAM** — single-store typed JSON schema with holistic re-synthesis on overflow
- **DPM** — deterministic projection (companion paper 2604.20158)

## Key Empirical Findings

- **Pre-registered hypothesis reversal**: Predicted summarization would lose FRP. Data showed the opposite — Summ-only's FRP is 38–93 pp higher than retrieval-based methods at all budget tiers. BM25 retrieval quietly routes load-bearing facts out of scope.
- **Retrieval architectures collapse on FRP**: Retr-only FRP = 0.05, Typed routing FRP = 0.01, vs. Summ-only FRP = 0.75.
- **Schema-anchored (SAM) pays scaffolding tax**: Per-entry overhead forces earlier facts to be dropped; re-synthesis paraphrases numeric anchors into prose.
- **DPM dissociation**: At adequate budgets, DPM and Summ-only converge. At tight budgets, DPM exceeds Summ-only by +0.52 FRP, +0.53 RCS, +0.50 EDA, +0.50 CRR.
- **All architectures fail CAR by default**: None was designed to abstain. Commit rate = 1.0 across all conditions.
- **CAR with Verified Memory (VM)**: A completeness-check prompt that abstains when evidence is insufficient. Over-abstains (commits on only 20% of cases) but achieves 100% conditional accuracy. A stricter/looser check moves operating point along the coverage-for-certainty curve.

## Results Table (per-architecture means)

| Architecture | FRP | RCS | EDA | CRR |
|--------------|-----|-----|-----|-----|
| Summ-only | 0.75 | 0.62 | 0.83 | 0.80 |
| Retr-only | 0.05 | 0.21 | 0.37 | 0.57 |
| Typed routing | 0.01 | 0.24 | 0.30 | 0.47 |
| Misrouted | 0.65 | 0.54 | 0.67 | 0.63 |
| SAM | 0.55 | 0.53 | 0.80 | 0.80 |
| DPM | 0.91 | 0.80 | 1.00 | 0.92 |

## Novel Contributions

1. **CRR as a regulatory-grounded axis** — Prior benchmarks measure task success; CRR measures whether output would satisfy a compliance auditor. Grounded in external regulatory text (ECOA/Reg B, state insurance regulation) rather than generic helpfulness rubrics.
2. **CAR separating coverage from accuracy** — No current benchmark measures whether agents know when NOT to decide.
3. **Institutional and decisional alignment as under-represented** — These become "load-bearing once decisions leave the laboratory." Framing compliance and abstention as alignment (not just deployment concerns) means they should be measured in evaluation and trained against, not just reviewed legally at deployment.

## Consumer Harm Relevance

This paper directly connects to the UK Consumer Harms domain:

- **AI underwriting/adjudication agents** — A bank's AI loan agent that reaches "correct" decisions but fails on FRP (wrong income figures) or CRR (non-specific adverse action notices) creates real consumer harm under ECOA and Reg B.
- **Regulatory compliance as consumer protection** — Non-compliant denial letters (citing "credit factors" instead of specific reasons) prevent consumers from understanding and contesting adverse decisions.
- **Systemic risk in AI-decisioning** — If all tested architectures commit on ambiguous cases, consumers bear the risk of AI guesses in high-stakes domains (loans, insurance, healthcare).
- **Connection to delegation harms** — As AI agents move into executive roles (executing decisions on behalf of users), the gap between what aggregate accuracy hides and what consumers actually need is a direct consumer protection concern.

## Cross-References

- [[srinivasan-2026-stateless-decision-memory]] — Companion paper introducing the DPM architecture tested here; DPM matches this paper's findings on tight budgets
- [[ai-agents-in-markets]] — Agents making binding decisions on behalf of users; this paper provides the evaluation framework for when those decisions are wrong
- [[systemic-fragility-in-ai-economies]] — All architectures failing CAR creates systemic risk when deployed at scale
- [[institutional-design-for-ai-agents]] — CRR directly maps to institutional design: can the agent's output satisfy the regulatory standard?
- [[advanced-ai-assistants]] — As Advanced AI Assistants move into advisory/executor roles for financial and legal decisions, four-axis alignment becomes a consumer protection baseline

