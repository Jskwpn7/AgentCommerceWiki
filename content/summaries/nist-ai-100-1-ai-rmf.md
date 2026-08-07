---
title: "NIST AI Risk Management Framework (AI RMF 1.0)"

created: 2026-07-04
updated: 2026-07-04
type: summary
tags: [policy-research, report, cross-sector, regulatory-failure]
sources: [raw/papers/nist-ai-100-1-ai-rmf.md]
confidence: high
---

# NIST AI Risk Management Framework (AI RMF 1.0)

## Paper Details

| Field | Value |
|-------|-------|
| Title | Artificial Intelligence Risk Management Framework (AI RMF 1.0) |
| Publication | NIST AI 100-1 |
| Publisher | National Institute of Standards and Technology (NIST), U.S. Department of Commerce |
| Date | January 2023 |
| DOI | https://doi.org/10.6028/NIST.AI.100-1 |
| Version | 1.0 (living document; formal review expected by 2028) |
| Pages | ~42 + appendices |
| URL | https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-1 |

## Summary

The NIST AI Risk Management Framework (AI RMF 1.0) is the first comprehensive, voluntary, non-sector-specific framework for managing AI risks. Directed by the National Artificial Intelligence Initiative Act of 2020, it provides a structured approach for organizations designing, developing, deploying, or using AI systems to promote trustworthy and responsible AI.

The framework is divided into two parts. **Part 1** (Foundational Information) establishes the conceptual foundation: how to frame AI risks, the intended audience (AI actors per OECD definition), and the characteristics of trustworthy AI systems. **Part 2** (Core and Profiles) presents the operational Core consisting of four functions — **GOVERN, MAP, MEASURE, MANAGE** — each broken into categories and subcategories, plus Profiles for tailoring the framework to specific organizational contexts.

The AI RMF defines an AI system as "an engineered or machine-based system that can, for a given set of objectives, generate outputs such as predictions, recommendations, or decisions influencing real or virtual environments" and recognizes AI systems as "inherently socio-technical in nature."

## Key Findings and Framework Structure

### Trustworthy AI Characteristics (7 dimensions)
The AI RMF identifies seven characteristics of trustworthy AI systems:
1. **Valid & Reliable** — performs as intended with appropriate accuracy and robustness
2. **Safe** — does not cause physical, psychological, or economic harm
3. **Secure and Resilient** — protected against adversarial attacks and failures
4. **Accountable and Transparent** — organizations accountable for outcomes; operations transparent to affected parties
5. **Explainable and Interpretable** — behavior can be explained to stakeholders
6. **Privacy-Enhanced** — protects personal data and respects privacy rights
7. **Fair with Harmful Bias Managed** — does not produce discriminatory outcomes

### The Four Core Functions

**GOVERN** (cross-cutting function, infused throughout all other functions):
- *Map*: Organizational coherence, stakeholder preferences, lifecycle processes, risk management plans, documentation
- *Measure*: Assess risk performance, report findings to stakeholders

**MAP** (understand context and plans):
- *Context*: Environment, data, capabilities, outcomes
- *Plan*: Understand plan, resources, governance structures, metrics

**MEASURE** (assess risk performance):
- *Assess*: Metrics, testing, validation, verification
- *Monitor*: Continuous monitoring of performance and risk indicators

**MANAGE** (make decisions about risk):
- *Treat*: Mitigate, accept, transfer, or avoid risk
- *Respond*: Respond to emerging risks, learn from events

### Key Challenges Identified
- **Risk Measurement**: Third-party dependencies, emergent risks, lack of consensus metrics, inscrutability of AI systems, difficulty establishing human baselines
- **Risk Tolerance**: Contextual and use-case specific, influenced by legal/regulatory requirements, likely to change over time
- **Risk Prioritization**: Eliminating all risk is counterproductive; residual risk directly impacts end users
- **Organizational Integration**: AI risks should be integrated into broader enterprise risk management; requires senior-level commitment and potentially cultural change

### Key Attributes (Appendix D)
The AI RMF strives to be: risk-based, resource-efficient, pro-innovation, voluntary, consensus-driven, written in clear plain language, providing common language/taxonomy, easily usable, useful across sectors/outcomes-focused, law-agnostic, and a living document.

## Relevance to UK Consumer Harms

This is a **foundational reference document** for the UK consumer harms wiki. While US-published, its value lies in:

1. **Comprehensive harm taxonomy** — the seven trustworthy AI characteristics map directly to UK consumer protection concerns: fairness/bias (discrimination in credit scoring, pricing), safety (physical and economic harm), privacy (GDPR alignment), accountability (consumer redress), explainability (right to explanation under UK GDPR).

2. **GOVERN function as regulatory template** — The GOVERN function's emphasis on organizational coherence, stakeholder analysis, and lifecycle processes provides a structured approach that UK regulators (CMA, FCA, Ofcom, Ofgem) could adapt for sector-specific AI oversight.

3. **Regulatory gap analysis** — The framework's recognition that "risks posed by AI systems are in many ways unique" compared to traditional software — particularly regarding data drift, emergent behavior, and socio-technical complexity — validates existing wiki entries on [[regulatory-failure]] and the need for AI-specific regulatory frameworks.

4. **Cross-sector applicability** — Its non-sector-specific, use-case agnostic design means it applies to all wiki-relevant sectors: financial services (AI credit scoring, algorithmic trading), energy (dynamic pricing), telecoms (recommendation algorithms), digital platforms (content moderation, search ranking), and housing (valuation algorithms).

5. **Informing UK policy development** — The voluntary, principles-based approach mirrors the UK government's current AI regulatory stance (pro-innovation, sector-led regulation). The framework could inform the UK's development of AI governance standards, potentially serving as a reference point for CMA guidance on AI-enabled consumer harms.

6. **Residual risk concept** — The framework's explicit treatment of residual risk (risk remaining after mitigation) is directly relevant to consumer protection: even after regulatory compliance, some AI risks remain, and documenting these is critical for stakeholder transparency.

## Connection to Other Wiki Entries

- [[regulatory-failure]] — The AI RMF's identification of measurement gaps and inscrutability as key challenges directly supports the wiki's analysis of regulatory detection and temporal gaps
- [[ai-agents-in-markets]] — The framework's lifecycle-based approach and emphasis on AI actors provides a structured lens for understanding autonomous agent deployment
- [[systemic-fragility-in-ai-economies]] — The AI RMF's recognition that AI risks can be systemic and interconnected, and that risk measurement at different lifecycle stages yields different results
- [[dark-pattern]] — Accountability and transparency requirements in the AI RMF directly address dark pattern concerns
- [[ai-act]] — While the EU AI Act is regulatory and prescriptive, the AI RMF is voluntary and principles-based; the two represent different governance philosophies that could be compared
- [[algorithmic-collusion-pricing]] — The framework's treatment of emergent behavior and third-party risk is relevant to understanding how algorithmic collusion arises
