---
title: "Awesome Agentic Commerce — Curated Resource List"
created: 2026-08-04
updated: 2026-08-04
type: summary
tags: [agentic-commerce, academic, research, consumer-harm, protocol-infrastructure, agent-liability]
sources:
  - https://github.com/yifeizhangcs/awesome-agentic-commerce
  - https://www.techrxiv.org/doi/full/10.36227/techrxiv.176972193.39211542/v1
confidence: high
---
# Awesome Agentic Commerce — Curated Resource List

> **Source:** yifeizhangcs/awesome-agentic-commerce (GitHub, 13 stars, 4 forks)
> **Companion Survey:** Zhang, Y., Pan, B., Zhu, M., Pei, J., & Zhao, L. (2026). *Agentic Commerce: A Survey of How AI Agents Are Reshaping Commerce*. TechRxiv. DOI: 10.36227/techrxiv.176972193.39211542/v1
> **License:** Creative Commons Attribution 4.0

---

## Overview

A curated, taxonomically organized list of ~100+ papers, products, protocols, and resources on **agentic commerce (A-Commerce)** — covering agentic e-commerce, multi-agent market systems, conversational commerce, autonomous negotiation, recommendation/search agents, pricing agents, supply chain/logistics agents, and payment agents.

The repository is structured around the companion survey's taxonomy and organizes resources into three parts:
- **Part I:** Commerce Pipeline (survey taxonomy by lifecycle stage × agent role)
- **Part II:** Applications, Infrastructure & Cross-Cutting Research
- **Part III:** Benchmarks, Environments & Evaluation

---

## Part I: Commerce Pipeline Taxonomy

*Organization: Stage → Agent Role. Lifecycle stages: Awareness → Discovery → Engagement → Decision → Transaction → Fulfillment → Service.*

### Awareness (Pre-intent Exposure)

| Stage | Agent Role | Key Papers |
|-------|-----------|------------|
| Awareness | Merchant-Agent | TKDE 2024 (Multi-Agent Meta-RL for Cross-Channel Bidding), EMNLP Industry 2024 (IPL: Multimodal Product Listing), ICLR 2025 FM-Wild (Agentic Multimodal AI for B2B/B2C Advertising), arXiv 2506.21934 (CAL-RAG: Layout Design), WWW Companion 2025 (RTBAgent) |
| Awareness | Platform-Agent | KDD 2023 (NEON: Meituan Needs Prediction), ACL Findings 2025 (PersonaX) |
| Awareness | Consumer-Agent | *Largely unexplored — highlighted as promising future direction* |

**Consumer harm relevance:** MEDIUM — Merchant agents competing for consumer attention via multi-agent bidding; platform agents shaping awareness before consumer intent forms.

### Discovery (Intent-Grounded Exploration)

| Stage | Agent Role | Notable Papers |
|-------|-----------|----------------|
| Discovery | Consumer-Agent | NeurIPS 2022 (WebShop), ACL Findings 2025 (iAgent: "Shield between User and Recommender"), AAAI 2026 (ShoppingBench), ACL Industry 2026 (ProductResearch), arXiv 2603.14864 (Shopping Companion), arXiv 2605.14205 (SimPersona), arXiv 2605.18805 (RecoAtlas) |
| Discovery | Platform-Agent | WWW 2024 (AgentCF), SIGIR 2024 (4 papers: Tool Learning, MACRec, Generative Agents), NAACL Findings 2024 (RecMind), NeurIPS 2025 (AgentRecBench), arXiv 2506.21931 (ARAG), arXiv 2510.20567 (Multi-Agent Cognitive Decision), arXiv 2506.17765 (CARTS), KDD 2025/2026 (LocalGPT, LocalSearchBench), TMLR 2025 (Rec-R1), arXiv 2604.14051 (Enhancing Local Life), arXiv 2606.05671 (QueryAgent-R1), arXiv 2606.28356 (SafeGEO), arXiv 2606.31693 (ShopX) |

**Consumer harm relevance:** HIGH — Platform-agent dominance in discovery creates information asymmetry; consumer agents are significantly underdeveloped. [[ai-shopping-agents]] [[algorithmic-collusion-pricing]]

### Engagement (Interactive Preference Elicitation)

| Stage | Agent Role | Notable Papers |
|-------|-----------|----------------|
| Engagement | Consumer-Agent | arXiv 2024 (ChatShop), PNAS 2026 (Autonomous Negotiation Competition), NLLP 2025 (Agent-to-Agent Negotiations in Consumer Markets) |
| Engagement | Merchant-Agent | arXiv 2511.12133 (AI-Salesman), EMNLP 2025 (ASTRA), IWSDS 2025 (Personality-Aware Sales), WWW Companion 2025 (FishBargain), CVPR 2026 (VerbalValue: Live Commerce) |
| Engagement | Platform-Agent | KDD 2025 (DiMA: DiDi Ride-Hailing), ACM TOIS 2025 (Recommender AI Agent), ACL Findings 2025 (Expectation Confirmation Preference Optimization) |

**Consumer harm relevance:** HIGH — Autonomous negotiation agents (PNAS 2026) create new asymmetries in bargaining power. [[commercial-persuasion-salvi-2026]]

### Decision (Evaluation & Commitment)

| Stage | Agent Role | Notable Papers |
|-------|-----------|----------------|
| Decision | Consumer-Agent | ACL 2025 (Personal Travel Solver), Amazon 2024 (Help Me Decide), arXiv 2606.17698 (EComAgentBench) |

**Consumer harm relevance:** MEDIUM — Platform-side decision tools may encode merchant interests over consumer welfare.

### Transaction (Authorization, Payment, Settlement)

| Stage | Agent Role | Notable Papers |
|-------|-----------|----------------|
| Transaction | Payment-Agent | IEEE BigData 2025 (CASE: Scam Intelligence in Digital Payments), GitHub (Zen7 Payment Agent) |

**Consumer harm relevance:** HIGH — Payment agents execute financial commitments; security frameworks are critical. [[x402-agentic-commerce-audit-ling-2026]] [[agentic-commerce-protocols]]

### Fulfillment (Supply Chain, Logistics, Delivery)

| Stage | Agent Role | Notable Papers |
|-------|-----------|----------------|
| Fulfillment | Supply-Side Agent | IROS 2023 (L3MVN), CoRL 2023 (RT-2), RSS 2024 (RoboCasa), arXiv 2411.10184 (Agentic LLMs in Supply Chain), arXiv 2511.23366 (Smart Inventory), arXiv 2508.11416 (AIM-Bench), CoRL 2025 (Mobility VLA), ICCV 2025 (RoboFactory), Amazon Robotics (>1M robots) |

### Service (Post-Purchase Support)

| Stage | Agent Role | Notable Papers |
|-------|-----------|----------------|
| Service | Consumer-Agent | *No canonical benchmark/paper list yet* |
| Service | Platform-Agent | arXiv 2510.13291 (Meituan Intelligent Interaction), arXiv 2507.18884 (MindFlow+: Self-Evolving CS Agent) |

**Notable gap:** No established benchmarks for consumer-agent service — identified as contribution opportunity.

---

## Part II: Applications, Infrastructure & Cross-Cutting Research

### Retail Shopping & Personal Assistants

Notable entries: OpenAI Shopping Research (ChatGPT), OpenAI Buy it (ChatGPT), Perplexity Shop like a Pro, Amazon Rufus, Amazon "Buy for Me" (2025), WebShop (NeurIPS 2022), ICML 2025 Position: "Build Agent Advocates, Not Platform Agents", KDD 2026 DeepTravel, REALM 2025 PAARS.

### Marketplaces (C2C / P2P)

- arXiv 2025 (FaMA: LLM Consumer-to-Consumer Marketplace)
- WWW Companion 2025 (FishBargain: Fleamarket Bargaining)
- NLLP 2025 (Agent-to-Agent Negotiations in Consumer Markets)

### Advertising, Bidding & Merchant Growth

- TKDE 2024 (Cross-Channel Bidding), SIGIR 2025 (Insight Agents), CVPR 2026 (E-comIQ-ZH: E-commerce Poster Evaluation)

### Sales & Customer Service

- Amazon Seller Assistant, AI-Salesman, MindFlow+, SalesRLAgent, VerbalValue (Live Commerce)

### Recommendation & Search Systems

*Extensive section: ~25+ entries covering AgentCF, MACRec, AgentRecBench, ARAG, CARTS, Rec-R1, LORE, ShopX, and more. Largely overlaps with Part I Discovery Platform-Agent entries.*

### Platform Services & Enterprise Solutions

- OpenAI Operator, Adobe Experience Platform Agent Orchestrator, Salesforce AI

### Mobility & On-demand Services

- Transportation Research Part C 2025 (LLMTraveler), KDD 2025 (DiMA), IEEE TASE 2026 (RideAgent)

### Unmanned Stores & Autonomous Retail

- Amazon Go, Nature Scientific Reports 2024 (LLM in Unmanned Retail), arXiv 2025 (Autonomous Retail Survey)

### Intelligent Cockpit & In-Vehicle Commerce

- SoundHound 2025 (In-Vehicle Voice Assistant), Alibaba Cloud 2025 (Intelligent Cockpits)

### Supply Chain, Warehousing & Embodied Commerce

- RT-2, RoboCasa, Agentic LLMs in Supply Chain, Amazon Robotics (1M+ robots)

### Negotiation & Pricing

- ICML 2024 (CompeteAI, NegotiationArena), PNAS 2026 (Autonomous Negotiation Competition), arXiv 2026 (TERMS-Bench)

### Protocols & Standards

| Protocol | Source | Significance |
|----------|--------|--------------|
| MCP (Model Context Protocol) | Anthropic | Tool interface standard |
| A2A (Agent-to-Agent) | Google | Delegation protocol (150+ orgs) |
| ACP (Agentic Commerce Protocol) | OpenAI | Checkout execution |
| Verifiable Credentials 2.0 | W3C 2025 | W3C Recommendation |
| Agent TCP/IP | arXiv 2025.01.06243 | Agent-to-Agent transaction system |

**Existing wiki entries:** [[universal-commerce-protocol-ucp]] [[agentic-commerce-protocol-acp]] [[the-dmcca]]

### Payment & Transaction Protocols

| Protocol/Entity | Source | Function |
|-----------------|--------|----------|
| AP2 (Agent Payments Protocol) | Google Cloud | AI commerce payments |
| KYA & Payments for Agents | Skyfire | Agent payments |
| MachinePal (x402) | GitHub/skalenetwork | AI Payment Agent |
| Zen7 Payment Agent | GitHub | Dedicated payment network |
| arXiv 2025.11.15712 | Secure Agent Payments | Trustless verification |
| arXiv 2026.06.08790 | RAILS | Verification-Native Clearing |

### User Simulation & Behavioral Modeling

- SIGIR 2025 (Agentic Feedback Loop), ACL Industry 2025 (SimUSER), arXiv 2509.21501 (LLM Customer Simulation), arXiv 2605.14205 (SimPersona), arXiv 2605.08334 (SalesSim)

### Trust, Safety & Ecosystem Measurement

| Entry | Source | Harm Relevance |
|-------|--------|----------------|
| iAgent | ACL Findings 2025 | HIGH — "Shield between User and Recommender" |
| CASE | IEEE BigData 2025 | HIGH — Scam intelligence in payments |
| Five Attacks on x402 | arXiv 2605.11781 | HIGH — Payment protocol vulnerabilities |
| SafeGEO | arXiv 2606.28356 | HIGH — Generative Engine Optimization risks |
| How Agentic Is A-Commerce? | arXiv 2607.12575 | MEDIUM — Population-scale x402 adoption measurement |

---

## Part III: Benchmarks & Evaluation

*Cross-cutting benchmarks covering multiple commerce stages and agent roles:*

Notable benchmarks: WebShop (NeurIPS 2022), NegotiationArena (ICML 2024), AgentRecBench (NeurIPS 2025), AIM-Bench, τ²-Bench, DeepShop, EcomBench, LocalGPT, LocalSearchBench, Magentic Marketplace, ShoppingBench (AAAI 2026), EComAgentBench (arXiv 2606.17698), TERMS-Bench (arXiv 2605.13909), τ-Rec (arXiv 2606.10156), SalesSim (arXiv 2605.08334), ShopX (arXiv 2606.31693).

---

## Consumer Harm Relevance

### Cross-Referenced Wiki Concepts

This resource list directly relates to or reinforces multiple existing wiki pages:

| Wiki Entry | Connection |
|-----------|------------|
| [[ai-shopping-agents]] | Discovery and engagement stage papers (WebShop, ShoppingBench, ProductResearch) |
| [[algorithmic-collusion-pricing]] | Negotiation & pricing section (CompeteAI, NegotiationArena, TERMS-Bench) |
| [[commercial-persuasion-salvi-2026]] | Merchant-agent engagement, AI-Salesman, sales conversion agents |
| [[dark-patterns-choice-architecture]] | iAgent (consumer shield), SafeGEO (generative engine optimization risks) |
| [[agentic-commerce-protocols]] | Protocols section: MCP, A2A, ACP, Verifiable Credentials |
| [[universal-commerce-protocol-ucp]] | Companion protocol to ACP |
| [[agentic-commerce-protocol-acp]] | Listed alongside MCP and A2A |
| [[x402-agentic-commerce-audit-ling-2026]] | Payment protocols section, x402 security |
| [[the-dmcca]] | Protocol standards and regulatory framework context |
| [[dissociative-agent-identity]] — Reputation mechanisms and identity grounding in agent-to-agent commerce | Reputation and identity challenges in agent-mediated commerce |
| [[evidence-tracing-vs-execution-provenance]] | Benchmarks section: verifiable evaluation frameworks |
| [[hidden-intent-agentic-shopping]] | EComAgentBench (hidden intent shopping tasks) |
| [[agent-dark-pattern-susceptibility]] | iAgent consumer protection, dark patterns for LLM agents |
| [[user-welfare-vs-company-incentive]] | ICML 2025 position paper: "Build Agent Advocates, Not Platform Agents" |
| [[the-mills-review]] | UK regulatory context (FCA Mills Review) |

### Identified Consumer Harm Vectors

| # | Vector | Source Coverage | Priority |
|---|--------|----------------|----------|
| 1 | Platform-agent information asymmetry | Discovery Platform-Agent (~25 entries), Recommendation section | HIGH |
| 2 | Autonomous negotiation power imbalances | PNAS 2026, FishBargain, CompeteAI | HIGH |
| 3 | Payment security vulnerabilities | x402 Five Attacks, CASE scam intelligence | HIGH |
| 4 | Merchant-agent competitive bidding | Awareness Merchant-Agent, RTBAgent | MEDIUM |
| 5 | Recommendation manipulation | iAgent, SafeGEO, Insight Agents | HIGH |
| 6 | Consumer-agent underdevelopment | Explicitly noted gap in Awareness and Service stages | MEDIUM |
| 7 | Embodied commerce safety | RoboFactory, Safe Human Robot Navigation | LOW-MEDIUM |
| 8 | Generative engine optimization | SafeGEO (arXiv 2606.28356) | HIGH |

### Notable Gaps (Contributions Welcome)

- **Consumer-Agent service benchmarks** — No canonical list yet in Part I Service stage
- **UK-specific agentic commerce research** — Repository is globally oriented; limited UK regulatory context beyond protocol standards
- **Long-horizon consumer agent evaluation** — Most benchmarks focus on single-task or short-horizon interactions

---

## Repository Metadata

| Attribute | Value |
|-----------|-------|
| GitHub | yifeizhangcs/awesome-agentic-commerce |
| Stars | 13 |
| Forks | 4 |
| Commits | 38 |
| License | CC-BY-4.0 |
| Contributor format | `[Venue Year] Paper Title. [link](url)` |
| Companion survey | Zhang et al. (2026), TechRxiv DOI: 10.36227/techrxiv.176972193.39211542/v1 |
| Coverage | ~100+ papers, products, protocols, benchmarks |
| Taxonomy basis | 7-stage commerce pipeline × agent roles (Merchant/Consumer/Platform/Supply/Payment) |

---

*Page generated from GitHub awesome list — not a primary research paper. Provides structured taxonomy and navigation for the agentic commerce research landscape. Cross-references existing wiki pages where applicable.*
