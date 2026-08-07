---
title: "Agentic Commerce Protocol (ACP)"
created: 2026-07-12
updated: 2026-07-12
type: entity
tags: [digital-platforms, financial-services, agentic-ai, lock-in, data-abuse, consumer-rights]
confidence: high
---

# Agentic Commerce Protocol (ACP)

**Lead Developers:** OpenAI, Stripe
**Launch:** September 2025
**Current Status:** Pivoted — retailer-app integration model (March 2026)

## Overview

The Agentic Commerce Protocol (ACP) is a machine-to-machine commerce framework developed by OpenAI in partnership with Stripe. It was the first major protocol enabling AI agents to execute autonomous purchases on behalf of consumers, built around a novel payment primitive called **Shared Payment Tokens (SPT)**.

ACP was conceived as a closed-loop agentic commerce experience: users discover products through ChatGPT, their AI agent negotiates and completes purchases using SPT infrastructure, and post-purchase service flows through the same system.

## Timeline and Evolution

### Phase 1: Full-Stack Launch (September 2025)

- ACP launched in partnership with Stripe featuring Shared Payment Tokens as a new payment primitive
- SPT allowed AI agents to make purchases without exposing raw card numbers — tokens scoped to specific merchants, spending limits, and time windows
- PayPal committed to ACP server integration for tens of millions of small businesses, planned for 2026 rollout

### Phase 2: Instant Checkout (February 16, 2026)

- "Buy it in ChatGPT" Instant Checkout rolled out for US ChatGPT Plus, Pro, and Free users
- Initially launched with Etsy sellers, then expanded to 1M+ Shopify merchants including Glossier, SKIMS, Spanx, and Vuori
- Consumers could complete purchases entirely within ChatGPT without navigating to a retailer website

### Phase 3: Pivoted Model (March 20, 2026)

- **Critical pivot:** OpenAI ended Instant Checkout, abandoning the closed-loop checkout experience
- New model: users discover products in ChatGPT but navigate to the retailer's website to complete purchases
- **Stated reasons for pivot:**
  - Technical hurdles in real-time product data sync across millions of retailers
  - Regulatory challenges in maintaining a full-stack checkout flow
  - OpenAI cited better access to purchase data earlier in the buying funnel as a benefit
- Underlying tension: the pivot shifts OpenAI's revenue model from transaction fees to data capture at the discovery layer

### Phase 4: PayPal Integration (2026 ongoing)

- PayPal's ACP server integration for tens of millions of additional small businesses remains active
- Extends ACP coverage beyond Shopify merchants to a broader small-business ecosystem

## Consumer Harm Relevance

### 1. Extended Opaque Period

The pivot from Instant Checkout to retailer-app integration suggests the full agentic-commerce experience (discovery → checkout → post-purchase in one interface) is not yet viable. This extends the period during which consumers lack transparency about how AI agents are recommending and purchasing products on their behalf.

### 2. Data Access Expansion

The retailer-app model gives OpenAI unprecedented visibility into consumer preferences and purchase intent **before** the transaction reaches the retailer. This creates an asymmetry where:
- OpenAI captures discovery-level preference data that retailers cannot access
- The retailer only sees the completed purchase, not the recommendation pathway
- OpenAI can optimise discovery algorithms to maximise engagement and affiliate revenue without transparent disclosure

### 3. Platform Gatekeeping Risk

ACP creates a duopoly layer: OpenAI+Stripe (ACP) versus Google+Shopify (UCP). The CMA's July 2026 discussion paper specifically flags concentration risks at the platform layer. The emergence of competing protocol duopolies creates gatekeeping power over how consumers discover and purchase goods.

### 4. Consent Erosion Through Tokenization

Shared Payment Tokens replace per-transaction consent with pre-authorised scoped tokens. Under UK law (Consumer Rights Act 2015, CPRs 2008), informed consent requires awareness of each transaction's material terms. ACP's token-based model compresses consent into a single granular action.

## Relationship to Other Protocols

- [[agentic-commerce-protocols]] — ACP is one of the major protocol families
- [[agentic-commerce-tokenization]] — ACP's Shared Payment Tokens are an implementation of agent commerce tokenization
- [[google-universal-cart-2026]] — UCP/Google's competing protocol approach
- [[ai-shopping-agents]] — ACP is the protocol layer that enables AI shopping agents to execute purchases

## UK Regulatory Implications

- **DMCC Act 2024:** The CMA's 10% global turnover penalty regime applies to ACP deployments in the UK market
- **CMA "Agentic AI and consumers" (March 2026):** States businesses are responsible for what AI agents do — directly applicable to OpenAI's ACP model
- **FCA payment services regulation:** ACP's token-based model challenges the legal definition of "payment instruction" under Payment Services Regulations 2017
- **GDPR:** OpenAI's pivot to capture discovery-layer data implicates Article 5(1)(c) data minimisation

## Sources

- OpenAI Instant Checkout announcement and termination (February–March 2026)
- Stripe Shared Payment Token technical documentation
- PayPal ACP integration announcement (2026)
- CMA "AI and Consumer Markets" discussion paper (July 2026)
- Robonomics agentic commerce deep dives
