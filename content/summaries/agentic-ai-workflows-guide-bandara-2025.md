---
title: "A Practical Guide for Production-Grade Agentic AI Workflows — Bandara et al. (2025)"

created: 2026-05-16
updated: 2026-05-16
type: summary
tags: [digital-platforms, corporate-accountability, research, cross-sector]
sources: [raw/papers/agentic-ai-workflows-guide-bandara-2025.md]
confidence: medium
---

# A Practical Guide for Production-Grade Agentic AI Workflows — Bandara et al. (2025)

## Paper Details

- **Authors:** Eranga Bandara, Ross Gore, Peter Foytik, Sachin Shetty, Ravi Mukkamala, Abdul Rahman, Xueping Liang, Safdar H. Bouk, Amin Hass, Sachini Rajapakse, Ng Wee Keong, Kasun De Zoysa, Aruna Withanage, Nilaan Loganathan (14 authors)
- **Affiliations:** Old Dominion University (lead), Deloitte & Touche LLP, Florida International University, Nanyang Technological University, University of Colombo, IcicleLabs.AI, AnaletIQ, Effectz.AI
- **Published:** 2025-12-09
- **arXiv:** [2512.08769v1](https://arxiv.org/abs/2512.08769v1)
- **Categories:** cs.AI
- **Format:** Engineering guide with implemented case study (44 pages, source code at GitLab)

## Summary

This 44-page paper provides a practical, end-to-end guide for designing, developing, and deploying production-grade agentic AI systems, built on the authors' experience implementing a real multimodal news-to-podcast generation workflow. Unlike purely conceptual guides, this paper documents **concrete engineering failure cases** encountered in production and proposes nine best practices derived from those experiences.

The paper's core argument is that building production-grade agentic AI systems requires far more than chaining LLM calls — it demands disciplined engineering, modular design, and operational rigor. The nine best practices address design patterns (tool integration, agent specialization), governance (externalized prompts, model-consortium reasoning), and deployment (containerization, KISS architecture).

## Key Findings from Full Paper

### Engineering Failure Cases

1. **MCP integration instability:** Initial GitHub publishing via MCP caused "flickering, non-reproducible failures" — ambiguous tool selection, inconsistent parameters, unpredictable responses. Replaced with direct tool invocation.
2. **Overloaded agents:** A single agent with two tools (scrape + publish) would often invoke only one, invoke in wrong order, or fail entirely — especially as input size grew.
3. **Hallucinated status messages:** A single agent doing both JSON generation AND video API calls would "hallucinate" file paths and status messages about generation that hadn't occurred.

### Multi-Model Consortium — Empirical Evidence

The workflow uses Gemini, GPT-5, Claude, and Llama in parallel, then a reasoning agent (GPT-oss) consolidates. **Evaluation showed real diversity:**

- **Llama** → concise, structured summaries
- **OpenAI** → detailed, narrative-driven content
- **Gemini** → stylistic flow, contextual framing
- **Problem:** emphasis drift, factual variations, contradictions between models — requiring downstream consolidation

### Nine Best Practices

1. **Tool calls over MCP** — Direct functions eliminate MCP's cognitive load and non-deterministic failures
2. **Pure function calls over tool calls** — Infrastructure tasks executed by orchestrator, not agents
3. **One agent, one tool** — Eliminates tool-selection noise
4. **Single-responsibility agents** — Blurring planning + execution causes hallucination
5. **Externalized prompt management** — Version-controlled, reviewable, rollback-capable
6. **RAI-aligned model-consortium design** — Multiple models + reasoning agent for consolidation
7. **Separation of workflow logic and MCP servers** — REST API + thin MCP adapter
8. **Containerized deployment (Docker + Kubernetes)** — Portability, scalability, resilience, observability
9. **KISS principle** — Flat, readable, function-driven designs; avoid over-engineering

## Relevance to UK Consumer Harms

While not a consumer harm paper per se, it provides several direct connections:

- **Multi-model inconsistency evidence:** The evaluation empirically demonstrates what theoretical papers flag as problematic — different LLMs produce genuinely different outputs. This supports the need for RAI-aligned consortium design as a consumer protection mechanism.

- **Engineering failure modes:** Hallucinated status messages, non-reproducible failures, and overloaded agents are concrete examples of how agentic systems fail — relevant to [[systemic-fragility-in-ai-economies]] and regulatory concerns about production AI systems.

- **MCP security:** The paper documents real MCP failures and cites three papers on MCP security threats (Hou et al., Hasan et al., Ntousakis et al.), connecting engineering practice to security literature.

- **Responsible AI alignment:** The consortium + reasoning agent approach is presented as an RAI mechanism, mapping to concerns about how AI systems should serve (not undermine) user welfare in production.

## Connection to Other Wiki Entries

- Links to [[ai-agents-in-markets]] — agentic systems in production with real-world consequences
- Links to [[systemic-fragility-in-ai-economies]] — engineering failure cases as evidence of fragility
- Links to [[user-welfare-vs-company-incentive]] — multi-model diversity shows model-dependent outputs that may serve different incentives
- Links to [[conflict-of-interest-in-llm-deployment]] — different models produce different results; consortium design as a mitigation
- Links to [[ai-act]] — governance and safety requirements for AI systems in production
- Links to [[hadfield-koh-2025-economy-of-ai-agents]] — theoretical framework for institutional redesign; this paper provides the engineering implementation perspective

## Limitations

- No explicit analysis of consumer harm, UK regulation, or market failures
- Case study is a news-to-podcast workflow (media generation), not a consumer-facing application
- The "Responsible AI" framing is engineering-oriented (accuracy, consistency) rather than consumer-protection oriented
- Does not discuss transparency requirements from a regulatory perspective
