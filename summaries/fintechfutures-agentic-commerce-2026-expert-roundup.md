---
title: "Agentic Commerce in 2026 — Expert Roundup (FinTech Futures)"
created: 2026-07-14
type: summary
tags: [agentic-commerce, ai-shopping-agents, open-protocols, ucp, ap2, aep, leo, consumer-rights, cross-sector]
sector: [retail, travel, financial-services, payments, cross-sector]
source: [[fintechfutures-agentic-commerce-2026-where-we-stand-and-what-lies-ahead]]
---
# Agentic Commerce in 2026 — Expert Roundup (FinTech Futures)

**Source:** Cameron Emanuel-Burns, FinTech Futures, April 1, 2026
**URL:** https://www.fintechfutures.com/ai-in-fintech/agentic-commerce-in-2026-where-we-stand-and-what-lies-ahead

## Overview

Expert-roundup article surveying the state of agentic commerce in 2026 through interviews with five industry leaders across AWS, Microsoft, Google, First Digital, and Mastercard. Covers definition, technology stack, current deployments, scaling challenges, and 5–10 year outlook.

## Key Definitions

**Agentic commerce** (AWS's John Kain): "A system where software agents (acting for consumers or merchants) can discover, decide, and transact — including executing multi-step workflows like comparing options, applying preferences/constraints, authenticating identity, arranging payment, and handling post-purchase service — while operating within explicit guardrails."

**Distinction from AI shopping assistants:** Agency — the system doesn't just recommend; it can complete a purchase or resolve a service workflow via tools and APIs.

**Business shift:** From search engine optimisation (SEO) to Answer Engine Optimisation (AEO) and LLM Engine Optimisation (LEO) — structuring product data so AI systems and agents can easily understand, evaluate, and recommend products.

## Expert Perspectives by Organization

### AWS — John Kain (Director, Financial Services Market Development)
- Defines agentic commerce architecture: agents execute multi-step workflows within guardrails
- Investment in building blocks: enterprise identity management, runtime orchestration, tool/data access controls, memory, evaluation, and end-to-end observability
- Platform: Amazon Bedrock AgentCore (adopted by Chime, Robinhood)
- Prediction: Single-threaded assistants will evolve into teams of specialised agents coordinated by a supervisor (planning, retrieval, risk, payments, service)
- E-commerce will shift toward intent-based purchasing ("get me the best option under these constraints") and continuous service (proactive returns, disputes, subscriptions)

### Microsoft — Keith Mercier (VP, Worldwide Retail and Consumer Goods)
- Retail is the most impactful sector; travel/hospitality close behind; financial services a major adopter
- Copilot Checkout (launched US January): shoppers complete purchases directly within Copilot, no external site visit
- Brand Agents deployed on retailer websites, trained on brand/product catalogue/business rules
- Emphasis on open protocols and shared business context for agent reasoning
- Trust: agents must explain recommendations, surface trade-offs, act only with appropriate consent

### Google — Deniz Oran (Head of Payments Partnerships, EMEA)
- UCP: "creates the common language to address disjointed shopping journeys"
- AP2: "provides the secure handshake for payments to establish trust and accountability across the ecosystem"
- Biggest scaling challenge: "everyone is building custom plugs for custom sockets, which is slow and expensive"
- Near-term: UCP will add related products at checkout, loyalty rewards application
- Still in "early stages of agentic commerce"

### First Digital — Vincent Chok (Founder & CEO)
- Blockchain as "programmable, fully transparent and immutable settlement layer that AI agents require for machine-to-machine interactions"
- Trust barrier: "In the US alone, only 10% of population trusts AI with financial decisions"
- Long-term vision: "commercial transactions are negotiated and settled between algorithms before a human ever sees a receipt"
- Building blocks already in construction: stablecoins, verifiable agent identity, 24/7 payment infrastructures

### Mastercard (former) — Sushma Daggubati (Payments & AI Product Expert)
- Agentic model: consumer specifies intent, agent handles discovery, evaluation, checkout, and post-purchase
- Biggest hurdles: trust, identity, regulatory complexity
- Regulatory patchwork: EU AI Act, data residency laws, eIDAS 2.0 create fragmented requirements
- Proposals: KYA (Know Your Agent) frameworks, cryptographic signing, Web Bot Auth standards, graded permissions, spending limits, human-in-the-loop checks, enhanced dispute/recovery flows
- Policy-aware routing and compliance logic embedded in agent workflows

## Current Deployments Documented

| Entity | Initiative | Status |
|--------|-----------|--------|
| Visa | VIC (Visa Intelligent Commerce) platform | Pilots with DBS Bank, Banco Santander |
| Visa | Visa Agentic Ready programme | Launching in Europe with Revolut, Barclays, Commerzbank |
| Mastercard + Santander | Europe's first live end-to-end AI-agent payment | Completed |
| Microsoft | Copilot Checkout | Live in US (January 2026) |
| Microsoft | Brand Agents on retailer sites | Active |
| AWS | Amazon Bedrock AgentCore | Adopted by Chime, Robinhood |
| Google | UCP + AP2 | Platform-agnostic; compatible with ACP, TAP, AP4M |
| First Digital | FDUSD stablecoin for agent settlement | Building blocks in construction |

## Scaling Challenges Identified

1. **Fragmentation:** Custom plugs for custom sockets; slow, expensive to integrate
2. **Infrastructure complexity:** No standardised execution environments; identity management across disparate systems; no comprehensive audit trails
3. **Context maintenance:** Sub-millisecond state access and real-time coordination for multi-step workflows; traditional databases inadequate
4. **Regulatory patchwork:** EU AI Act, data residency, eIDAS 2.0 create compliance complexity; privacy-preserving models reduce fraud monitoring visibility
5. **Trust deficit:** 10% US population trust AI with financial decisions; verifying agent legitimacy and liability allocation are unresolved
6. **Legacy system integration:** Existing financial infrastructure not designed for agent-driven transactions

## Consumer Harm Relevance

This article provides a rare cross-industry synthesis that validates several consumer harm vectors already documented in the wiki:

- **Protocol fragmentation → invisible spending:** Multiple competing protocols (ACP, AP2, UCP, TAP, x402, AP4M) with no standardised consumer-facing interface creates risk of invisible spending across incompatible rails
- **Trust gap validation:** The 10% US trust figure and "trust is necessary for mainstream adoption" aligns with the wiki's documented trust gap (19% UK trust for purchasing agents, 60% one-mistake tolerance)
- **KYA identity frameworks:** Daggubati's proposal for "Know Your Agent" frameworks directly addresses the wiki's documentation of agent identity and reputation problems (see [[agentic-commerce-protocols]], [[ai-shopping-agents]])
- **Liability gaps:** "Defining responsibility when an agent makes an unauthorised or harmful decision" — this is the core liability attribution problem the wiki tracks (see [[agentic-relationship-harm]], [[institutional-design-for-ai-agents]])
- **AEO/LEO shift:** The article's emphasis on Answer Engine Optimisation and LLM Engine Optimisation reflects the structural gatekeeping risk documented in [[ai-mode-shortlist-gatekeeping]] — businesses structuring data for agent retrieval rather than human discovery

## Connection to UK Policy

- The regulatory patchwork cited (EU AI Act, eIDAS 2.0) directly affects UK businesses operating in EU markets
- Visa Agentic Ready's European launch with UK banks (Barclays, Revolut, Commerzbank) means UK consumers will encounter agent-initiated transactions
- The KYA proposal aligns with UK FCA expectations under the Mills Review for agent identity and accountability frameworks
- Daggubati's call for "human-in-the-loop checks for high-risk actions" maps to KPMG's "right to human" and "right to appeal" framework
