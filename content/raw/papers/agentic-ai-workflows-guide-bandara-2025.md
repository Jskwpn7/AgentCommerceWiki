---
source_url: https://arxiv.org/abs/2512.08769
ingested: 2026-05-16
sha256: pending
tags:
  - agentic
  - Artificial_Intelligence
  - LLM
  - MCP
  - orchestration
---
# A Practical Guide for Designing, Developing, and Deploying Production-Grade Agentic AI Workflows

**Authors:** Eranga Bandara, Ross Gore, Peter Foytik, Sachin Shetty, Ravi Mukkamala, Abdul Rahman, Xueping Liang, Safdar H. Bouk, Amin Hass, Sachini Rajapakse, Ng Wee Keong, Kasun De Zoysa, Aruna Withanage, Nilaan Loganathan
**Affiliations:** Old Dominion University (lead), Deloitte & Touche LLP, Florida International University, Nanyang Technological University, University of Colombo, IcicleLabs.AI, AnaletIQ, Effectz.AI
**Published:** 2025-12-09 (arXiv ID: 2512.08769v1)
**Categories:** cs.AI
**Format:** Engineering guide with implemented case study (44 pages)

## Abstract

Agentic AI marks a major shift in how autonomous systems reason, plan, and execute multi-step tasks. Unlike traditional single model prompting, agentic workflows integrate multiple specialized agents with different Large Language Models (LLMs), tool-augmented capabilities, orchestration logic, and external system interactions to form dynamic pipelines capable of autonomous decision-making and action. As adoption accelerates across industry and research, organisations face a central challenge: how to design, engineer, and operate production-grade agentic AI workflows that are reliable, observable, maintainable, and aligned with safety and governance requirements. This paper provides a practical, end-to-end guide for designing, developing, and deploying production-quality agentic AI systems.

## Key Findings from Full Text

### Engineering Failure Cases Documented

1. **MCP integration instability:** When the podcast workflow initially used MCP integration for GitHub publishing, agents exhibited "flickering, non-reproducible failures" — ambiguous tool-selection decisions, inconsistently inferred parameters, and unpredictable MCP responses. The cognitive load of interpreting MCP metadata caused variability. Replaced with direct tool invocation to eliminate ambiguity.

2. **Overloaded agents:** A single agent given two tools (scrape markdown + publish markdown) would often invoke only one tool, invoke them in the wrong order, or fail entirely — especially as input size increased. Decomposed into two independent agents, each responsible for exactly one tool.

3. **Planning-execution blurring:** A single agent tasked with both generating Veo-3 JSON specifications AND calling the video generation API would sometimes produce malformed JSON, sometimes mix natural language with JSON, and sometimes "hallucinate" file paths or status messages about video generation that had not actually occurred. Split into a JSON Builder Agent + a non-agent function.

### Multi-Model Consortium Evaluation

The workflow uses a consortium of LLMs (Gemini, GPT-5, Claude, Llama) for podcast script generation, then a reasoning agent (GPT-oss) consolidates outputs. **Empirical evaluation showed real diversity and problems:**

- **Llama:** Concise, structured summaries
- **OpenAI (GPT-5):** Detailed, narrative-driven content
- **Gemini:** Emphasizes stylistic flow and contextual framing
- **Resulting inconsistencies:** Emphasis drift, factual variations, and occasional contradictions between models — highlighting the need for downstream consolidation

The reasoning agent improves clarity, factual stability, and narrative coherence by retaining only information consistently supported across drafts, removing speculation, and correcting contradictions. This consensus-driven approach grounds outputs in multi-model agreement.

### Case Study Architecture

The implemented workflow has these agents:
1. **Web Search Agent** — discovers news via RSS feeds and MCP-based search endpoints
2. **Topic Filtering Agent** — evaluates relevance of articles to user-specified topic
3. **Web Scrape Agent** — extracts full content, converts to clean Markdown
4. **Podcast Script Generation Agents** — multiple LLM providers generate parallel drafts
5. **Reasoning Agent** — consolidates drafts, resolves inconsistencies, removes speculation
6. **PR Agent** — publishes results to GitHub via MCP-integrated GitHub server

Built with OpenAI Agents SDK, Docker, Kubernetes, REST API. Source code at GitLab (rahasak-labs/podcast-workflow).

### Nine Best Practices (detailed)

1. **Tool calls over MCP** — Direct function calls eliminate MCP's additional abstraction layer that caused cognitive load and non-deterministic failures. MCP should be a thin adapter, not the primary integration mechanism.
2. **Pure function calls over tool calls** — Infrastructure tasks (API calls, file writes, timestamps) should be pure functions executed by the orchestrator, not agent-invoked tools. Eliminates ambiguous tool formatting, unnecessary LLM reasoning, and reduces token usage.
3. **One agent, one tool** — Avoid overloading agents with multiple tools. Each agent should have a single well-defined tool to eliminate tool-selection noise and ensure deterministic behavior.
4. **Single-responsibility agents** — Each agent should do one thing well. Blurring planning and execution (e.g., JSON generation + API calls) causes hallucination of status messages and malformed outputs.
5. **Externalized prompt management** — Store prompts as Markdown/text in a separate repo. Enables non-technical stakeholders to update agent behavior without code changes, supports version pinning, rollback, and controlled access.
6. **RAI-aligned model-consortium design** — Use multiple LLMs in parallel with a reasoning agent for consolidation. Improves accuracy through cross-model agreement, reduces bias via diverse training distributions, increases robustness to model drift.
7. **Separation of workflow logic and MCP servers** — Expose workflows via REST API, MCP server acts as a thin forwarding layer. Keeps MCP simple/stable while allowing backend to iterate rapidly.
8. **Containerized deployment (Docker + Kubernetes)** — Provides portability, scalability, resilience, security (RBAC, network policies), observability (Prometheus, Grafana, OpenTelemetry), and CI/CD integration.
9. **KISS principle** — Flat, readable, function-driven designs. Avoid over-engineering, deep inheritance, or microservice-like decomposition. Simple workflows are easier for LLMs to reason about, easier for AI-assisted coding tools, and more adaptable to new models.

### References to MCP Security Literature

The paper cites three papers on MCP security and maintainability:
- **[10]** Hou et al. — MCP landscape, security threats, and future research directions
- **[25]** Hasan et al. — Security and maintainability of MCP servers
- **[27]** Ntousakis et al. — Securing MCP-based agent workflows

### Broader Research Context

The authors have a portfolio of related papers:
- Agentsway: software development methodology for AI agent teams (arXiv 2510.23664)
- Model Context Contracts: MCP framework for blockchain smart contracts (arXiv 2510.19856)
- Deep-Stride: automated security threat modeling with VLMs
- Proof-of-TBI: fine-tuned VLM consortium for medical diagnosis
- Standardization of psychiatric diagnoses using LLM consortium
- SRE-LLaMA: fine-tuned LLM for site reliability engineering

### Conclusion

The paper concludes that agentic AI "represents a fundamental shift in how autonomous systems are engineered" and that achieving production-grade reliability "demands disciplined engineering, modular design, and operational rigor." Future work includes adaptive evaluation pipelines, workflow self-monitoring, and tighter safety/guardrail integrations.

## Notes for Consumer Harms Research

This is an engineering guide, not a consumer harm analysis. Its value to the wiki lies in:

1. **Concrete evidence of multi-model inconsistency** — the evaluation shows that different LLMs produce genuinely different outputs (emphasis drift, factual variations) which is exactly the problem that [[user-welfare-vs-company-incentive]] and [[conflict-of-interest-in-llm-deployment]] identify at a theoretical level. The consortium + reasoning agent approach is presented as a mitigation.

2. **MCP security concerns** — the paper documents real failures from MCP integration and cites MCP security literature, connecting to concerns about how agentic systems interact with external tools in production.

3. **Engineering failure modes** — the documented failures (hallucinated status messages, non-reproducible MCP failures, overloaded agents) are relevant to [[systemic-fragility-in-ai-economies]] as concrete examples of how agentic systems can fail in production.

4. **Responsible AI alignment** — the paper's emphasis on RAI-aligned design maps to regulatory concerns about consumer protection in agentic AI systems.
