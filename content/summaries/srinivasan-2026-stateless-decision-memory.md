---
title: "Stateless Decision Memory for Enterprise AI Agents"

created: 2026-06-05
updated: 2026-06-05
type: summary
tags: [digital-platforms, policy-research, digital-consumer, corporate-accountability, research]
sources: [raw/papers/stateless-decision-memory-2604.20158.md]
confidence: medium
---

# Stateless Decision Memory for Enterprise AI Agents

**Author:** Vasundra Srinivasan (Independent, AI Architect; Author, Data Engineering for Multimodal AI (O'Reilly); Stanford School of Engineering)  
**Date:** April 22, 2026  
**arXiv ID:** 2604.20158v1 [cs.AI]  
**Source:** [[raw/papers/stateless-decision-memory-2604.20158.md]]  
**URL:** https://arxiv.org/abs/2604.20158  

## Paper Details

| Field | Value |
|-------|-------|
| Title | Stateless Decision Memory for Enterprise AI Agents |
| Author | Vasundra Srinivasan |
| Date | April 22, 2026 |
| Venue | arXiv preprint 2604.20158v1 |
| Pages | 16 |
| Companion paper | [[memory-in-the-age-of-ai-agents-hu-2025]] (also by Srinivasan — four-axis decision alignment framework) |

## Summary

This paper identifies and quantifies the gap between academic agent-memory research and enterprise deployment in regulated domains (mortgage underwriting, claims adjudication, clinical review, tax examination). The author argues this gap is explained by four **enterprise systems properties** that academic evaluations underweight: deterministic replay, auditable rationale, multi-tenant isolation, and statelessness for horizontal scale.

The paper proposes **Deterministic Projection Memory (DPM)** — an append-only event log plus one task-conditioned projection at decision time — and demonstrates it matches summarization-based memory at generous budgets while strictly improving at tight budgets (20× compression), with large effect sizes on factual precision (Cohen's h=1.17) and reasoning coherence (h=1.13).

DPM is 7–15× faster than stateful baselines and reduces the audit surface from 83–97 LLM calls per decision to just 2.

## Key Contributions

### 1. Four Enterprise Properties Framework
The paper defines four load-bearing properties that regulated decisioning systems require:
- **Deterministic replay** — a denied applicant can be re-scored and the same decision justified
- **Auditable rationale** — reasoning chain maps back to specific events in the input
- **Multi-tenant isolation** — one applicant's documents cannot leak into another's decision
- **Statelessness for horizontal scale** — thousands of concurrent decisions cannot bottleneck on shared mutable memory

These are standard in enterprise software (SOC 2, ISO 27001) but novel as explicit architectural constraints on agent memory systems.

### 2. Deterministic Projection Memory (DPM)
An architecture that treats agent memory as an **append-only event log** plus a **single task-conditioned projection** at decision time. The projection is a pure function — a structured extraction of facts, reasoning points, and compliance notes at temperature zero, within a character budget.

### 3. Empirical Results (10 cases, 3 budgets, paired permutation)
| Metric | Budget | DPM | Summ-only | Δ | p-value | Cohen's h |
|--------|--------|-----|-----------|------|---------|-----------|
| FRP | Tight | 0.907 | 0.392 | +0.515 | 0.001 | +1.17 |
| RCS | Tight | 0.800 | 0.267 | +0.533 | 0.003 | +1.13 |
| Cost at tight budget | — | $0.014 | $0.165 | — | — | 7.4× speedup |
| Audit surface | — | 2 LLM calls | 83–97 LLM calls | — | — | 40–48× reduction |

**Key finding:** The DPM advantage appears specifically in the tight-budget regime where memory compression binds — a "scale effect" not a uniform improvement.

### 4. Determinism Study
Both architectures inherit residual API-level nondeterminism at temperature zero (live Anthropic API produces distinct SHA-256 hashes across replays). However, DPM exposes **one** nondeterministic call per replay vs. **N** (≈82) for summarization-based memory. If each call contributes drift ϵ, DPM's expected drift is O(ϵ) vs. Summ-only's O(ϵn).

### 5. TAMS Heuristic
Task-Adaptive Memory Selection — a binary rule:
1. If deployment requires deterministic replay, audit-ready rationale, or multi-tenant isolation → **use DPM**
2. Else if compression ratio exceeds ~10× → **use DPM**
3. Else → **either architecture is acceptable**

### 6. Failure Analysis
Concrete failure modes of stateful memory in production: state drift under concurrency (non-associative/commutative merge semantics), replay complexity compounding (exponential byte-identity probability decline), cross-tenant leakage in shared caches, and audit surface area (n+1 vs. 2 LLM calls).

## Relevance to UK Consumer Harms

This paper has direct and significant relevance to UK Consumer Harms Research:

### 1. Consumer Redress and Deterministic Replay
When an enterprise AI agent denies a mortgage application, claims an insurance policy, or rejects a prior-authorization request, the consumer has a legal right (under ECOA/Regulation B, FCA rules, PRA requirements) to understand **why** and to **contest** the decision. The paper's first enterprise property — deterministic replay — is precisely the technical requirement that enables consumer redress. If the memory architecture cannot reproduce the same decision when replayed, the consumer cannot get a fair re-assessment. The paper demonstrates that stateful memory architectures **structurally violate** this property while DPM satisfies it by construction.

### 2. Audit Trail and Explainability
The "auditable rationale" property is critical for consumer-facing AI systems. Under UK regulatory frameworks (FCA, PRA, ICO), decisions affecting consumers must be explainable. The paper quantifies the audit surface asymmetry: DPM requires capturing 2 LLM calls per decision vs. 83–97 for stateful memory. This has implications for the **practical cost of explainability** — stateful architectures make comprehensive audit trails materially more expensive to implement, potentially creating a disincentive for regulated firms to invest in proper consumer-facing explainability.

### 3. Multi-Tenant Isolation and Data Protection
The paper's multi-tenant isolation property maps directly to **UK GDPR requirements** for data segregation. If one consumer's documents leak into the AI agent's decision on another consumer, this constitutes a data breach under Article 33 notification requirements. The paper argues isolation is the "default" for stateless architectures but must be "retrofitted" for stateful ones — suggesting that enterprises choosing sophisticated stateful memory may accept higher data-breach risk.

### 4. The Accuracy vs. Auditability Trade-off
The paper documents that RAG (the enterprise standard) is "straightforwardly weaker" than academic memory architectures on decision accuracy, yet enterprises prefer it because of its operational properties. This reveals a fundamental tension: **the architectures that deliver the best consumer outcomes (decision accuracy) are the hardest to make compliant**. This connects to [[conflict-of-interest-in-llm-deployment]] where provider incentives may not align with consumer welfare — in this case, the tension is between what is best for the consumer (accurate decisions) and what is easiest for the enterprise (compliant operations).

### 5. Enterprise Adoption Patterns and Consumer Protection
The paper explains **why** enterprises under-deploy sophisticated AI memory in regulated domains — not because they don't want accuracy, but because they can't satisfy the four enterprise properties with stateful architectures. This has implications for UK regulators: if enterprises are structurally incentivized to choose simpler (weaker) AI systems for compliance reasons, consumers may systematically receive **less sophisticated AI assistance** in high-stakes regulated domains (mortgages, insurance, healthcare) than in consumer-facing applications where compliance requirements are lighter.

### 6. TAMS Heuristic and Consumer Risk
The TAMS rule provides a decision framework that enterprises can use to justify their memory architecture choices. However, it is derived from only 10 cases across 2 domains with one model family. The paper acknowledges TAMS should be "re-derived under" different conditions. For UK consumer protection, this means the heuristic's guidance may not transfer to the specific regulatory contexts that matter most for consumer welfare (UK-specific frameworks like FCA Consumer Duty, PRA rules, ICO guidance).

### 7. Statelessness and Consumer Agency
The paper's broader argument — that **statelessness is the load-bearing property** for enterprise AI — connects to the concept of consumer **agency and contestability**. A stateless, deterministic architecture makes it possible for consumers to understand and challenge AI decisions. A stateful, path-dependent architecture renders the decision process opaque and unchallengeable. This is a form of **information asymmetry** that disadvantages consumers — they cannot contest what they cannot understand.

## Connection to Other Wiki Entries

- [[memory-in-the-age-of-ai-agents-hu-2025]] — Companion paper (also by Srinivasan) defines the four-axis decision-alignment framework (FRP, RCS, EDA, CRR) used in this paper's experiments
- [[conflict-of-interest-in-llm-deployment]] — The tension between decision accuracy and auditability reveals a structural conflict between what is best for consumers and what is easiest for enterprises to deploy
- [[systemic-fragility-in-ai-economies]] — The state drift and cross-tenant leakage failure modes demonstrate how interconnected AI systems create new failure modes that can harm consumers
- [[advanced-ai-assistants]] — The paper addresses executor-role AI agents in regulated enterprise contexts
- [[ai-agents-in-markets]] — The paper provides concrete architectural analysis of how AI agents make decisions in regulated markets (mortgage, insurance)
- [[user-welfare-vs-company-incentive]] — The trade-off between decision accuracy (consumer welfare) and auditability/operational cost (company incentive) is central to this paper
- [[delegation-nation-comprehensive-research]] — Delegation of regulated decisions to AI agents raises the same questions about explainability and contestability that this paper addresses at the architectural level
- [[notes/Online-Choice-Architecture-and-Dark-Patterns-in-the-UK]] — If stateful memory architectures make explainability too expensive to implement, consumers face AI decisions they cannot contest — a form of information-dark-pattern choice architecture
- [[agentic-ai-workflows-guide-bandara-2025]] — This paper's DPM architecture provides a concrete alternative to the agentic AI workflow patterns described in the Bandara guide, specifically optimized for regulated environments
- [[agentic-commerce-deep-dive-fd-robonomics]] — The TAMS heuristic parallels the "digital tax" framework: both provide practical rules for how enterprises choose between competing AI architecture approaches

## Methodology Notes

- 10 cases per cell on two regulated domains (mortgage qualification under ECOA/Regulation B, insurance claims adjudication)
- 26,000–28,000 characters per case, 82–96 discrete events per case
- claude-haiku-4-5-20251001 at temperature 0, fixed seed 20260420
- Paired permutation tests with 10,000 resamples
- Companion paper [[memory-in-the-age-of-ai-agents-hu-2025]] by the same author defines the decision-alignment framework used for evaluation
- Reproducibility harness released at https://github.com/vasundras/stateless-decision-memory-enterprise-ai-agents
- Author disclaimer: independent research, no employer sponsorship, no proprietary information disclosed
- Code and evaluation harness released for reproducibility
