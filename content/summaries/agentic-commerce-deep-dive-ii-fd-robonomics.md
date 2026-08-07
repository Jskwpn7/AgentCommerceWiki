---
title: "Agentic Commerce Deep Dive (II) — Implications, FD, Robonomics"

created: 2026-06-05
updated: 2026-06-05
type: summary
tags: [digital-platforms, digital-consumer, corporate-accountability, cross-sector, research]
sources: [raw/articles/agentic-commerce-deep-dive-ii-fd-robonomics.md]
confidence: medium
---

# Agentic Commerce Deep Dive (II): Implications for the Internet Economy

**Author:** FD  
**Publication:** Robonomics (independent tech journal)  
**Date:** October 13, 2025  
**Part:** II of "Deep Dive" series (follow-up to Part I)  
**Source:** [[raw/articles/agentic-commerce-deep-dive-ii-fd-robonomics.md]]
**URL:** https://robonomics.substack.com/p/agentic-commerce-deep-dive-ii

## Paper Details

| Field | Value |
|-------|-------|
| Title | Agentic Commerce | Deep Dive (II) — Implications of Agentic Commerce on merchants/platforms, payment stack, ads players and industry |
| Author | FD (independent) |
| Publication | Robonomics |
| Date | October 13, 2025 |
| Format | Newsletter article (follow-up to Part I) |
| URL | https://robonomics.substack.com/p/agentic-commerce-deep-dive-ii |
| Likes/Restacks | 15 likes, 1 comment |

## Summary

This article assumes agentic commerce is viable (established in Part I) and examines the ripple effects across the internet economy across seven domains: ads vs. take-rate economics, merchant/platform dynamics, pure infra vs. traffic-owning platforms, payment infrastructure, and search/ads platforms. The core thesis: agentic commerce represents a "new digital tax" where top-of-funnel networks extract value through a convergence of advertising and e-commerce business models, creating a squeeze on merchants that could be harsher than Apple's 30% App Store fee or Google's CPC toll.

## Key Frameworks and Arguments

### 1. History Lesson: Googl vs. OTAs
**BKNG / EXPE (Hotel Booking Platforms):**
- Roughly 50% of bookings are direct traffic (profitable), 50% indirect via Google (essentially breakeven)
- Unit economics: $300/night hotel, 15% take rate, $1–3 CPC, 3–4% conversion → ~$50 marketing expense per completed booking on indirect traffic
- Direct traffic is monetizable via paid placements (ads account for ~10% of EXPE revenue, ~5% of BKNG)

**ETSY:**
- Marketing runs ~30% of revenue — indirect portion is barely profitable

**Key insight:** Google extracted more total profit from travel than all OTAs combined. Indirect traffic is an "expensive squeeze."

### 2. The New Digital Tax: Ads Expense ≈ Take Rate
The article introduces a powerful analytical framework: **ads expense and take rate are interchangeable forms of digital tax.**

| Platform | "Digital Tax" Rate | Target |
|----------|-------------------|--------|
| YouTube | 45% | Creators |
| META | ~99% | Creators |
| AAPL App Store | 15–30% | App developers |
| OTAs (indirect traffic) | 0–5% effective (headline 15%) | Hotels/travelers |

If ChatGPT charges booking platforms a 10–15% take rate, they'd essentially breakeven compared with getting traffic from Google — making agentic commerce an equivalent "digital tax" to search advertising.

**Prediction:** ChatGPT will start at a low take rate (~2%) and gradually raise toward equilibrium (10–15%). Whether called "take rate" or "ad spend" is semantics — **top-of-funnel networks always get their digital tax.**

This convergence has already happened in China with PDD and BABA, which blur the lines between ads and take rates when charging merchants.

### 3. Impact on Merchants / Platforms
The squeeze operates through multiple channels simultaneously:
1. **Direct vs. indirect traffic mix** — pressure on profitable direct traffic
2. **Unit economics on indirect traffic** — effective take rate convergence
3. **Conversion rates** — agentic commerce may offer higher conversion (6×) but...
4. **Market share displacement** — platform curation replaces merchant discovery
5. **Industry online penetration** — uncertain whether agents increase or decrease online share

**Critical loss for merchants:** Traditional retailers depend on in-site browsing for upsells and cross-sells. Agentic commerce happens off-site — no visit, no pixel, no browsing data. Merchants lose visibility and retargeting power even if they get the buyer's email.

- **Small merchants:** May benefit from higher conversion rates offsetting data loss
- **Big retailers (AOV-optimized):** Likely harmed — they rely on in-site engagement for order value

### 4. Shopify — The Infra Winner
**SHOP** may be the "cleanest structural fit for ChatGPT's agentic world" because:
- Never was the MoR and doesn't "curate" merchants (no direct/indirect traffic conflict)
- ~3 M merchants selling unique, high-quality products that can't afford ad-spend arms race
- Could level the playing field via agent-driven discovery

**Three benefits:**
1. **GMV tilts toward quality SMBs** — agents discover products based on merit, not ad spend
2. **Higher SMB penetration** — merchants lacking data/catalog pipelines migrate to SHOP's stack
3. **Marketing efficiency** — SHOP spends ~$1.4B (16% of revenue) on marketing; its merchants collectively spend ~$20–50B. That duplicated "digital tax" could be streamlined.

### 5. Payments: Stripe's Quiet Leverage
Both ACP (OpenAI) and Perplexity's model let merchants keep existing PSPs — and **Stripe powers both.** As agentic checkout spreads, Stripe's role as the neutral connective tissue likely strengthens.

### 6. Impact on Google / Ads
**Bull case:** GOOGL has a near-perfect "T-shaped" value proposition — vertically integrated (apps → cloud → chips) and horizontally positioned (Google Suite, YouTube, Google Home).

**Concern:** GOOGL could theoretically lose 95% of search volume and still grow revenue (as long as valuable commerce queries remain). But whether the ads model survives the agentic era intact is unresolved.

### 7. The Road Ahead
**Key requirements for mature agentic commerce:**
- **Universal product catalog** (Patrick Collison/Tobi Lütke) — standardized product data powering AI agents
- **Product-specific models** — agents must parse "a black-and-white mohair sweater with a big letter G"
- **Feedback-driven review layer** — to close the loop on agent recommendations

## Relevance to UK Consumer Harms

This article provides significant UK consumer harms relevance across several dimensions:

### 1. The "Digital Tax" as Economic Harm
The article's "ads expense = take rate" framework reveals how agentic commerce could impose a **new layer of economic extraction** on merchants, consumers, and the broader digital economy. If top-of-funnel AI platforms charge 10–15% on all agent-mediated purchases, this represents a structural shift in value extraction that parallels concerns about platform monopolies and pricing power — directly relevant to UK CMA and consumer-rights investigations into digital gatekeepers.

### 2. Merchant Squeeze and Market Concentration
The analysis of how agentic commerce squeezes merchants through the loss of direct traffic, browsing data, and upsell opportunities connects to [[conflict-of-interest-in-llm-deployment]] — when AI agents mediate purchases, merchants lose the ability to optimize their customer relationship. This concentration of data and relationship power at the agent/platform layer creates new vulnerabilities for small businesses that cannot compete in ad-spend arms races.

### 3. Data Privacy and Consumer Protection
The article explicitly notes that agentic commerce happens **off-site, with no visit, pixel, or browsing data** — yet merchants may still receive the buyer's email. This creates a novel data asymmetry: the platform controls the full interaction data while the merchant only gets minimal contact information. Under UK GDPR, this raises questions about:
- Who is the data controller/processor in agent-mediated transactions?
- What consent mechanisms exist when an AI agent acts on behalf of a consumer?
- How does the ICO regulate the data flows in agentic commerce?

### 4. Choice Architecture and Consumer Welfare
The progression from "find me women's running shoes" to "a black-and-white mohair sweater with a big letter G" represents increasingly sophisticated **choice architecture** — exactly the kind of influence the [[online-choice-architecture-and-dark-patterns-in-the-UK]] wiki page examines. When AI agents make purchasing decisions, the "choice architecture" is embedded in:
- The agent's training data and prompt design
- The product catalog metadata that the agent can access
- The recommendations generated by the agent (potentially influenced by sponsored content per [[wu-2026-ads-in-ai-chatbots]])

### 5. Systemic Risk in the Payment Stack
The article's observation that Stripe strengthens as the "neutral connective tissue" raises questions about **single points of failure** in the payment infrastructure for agentic commerce. If all AI-mediated purchases flow through a single PSP, this creates systemic risk — relevant to [[systemic-fragility-in-ai-economies]].

### 6. Cross-Sector Comparison
The analogy between Google's extraction from OTAs and future AI agent extraction from merchants provides a **historical precedent** for understanding how top-of-funnel platforms can extract disproportionate value. The UK's FCA and consumer-rights regulators could draw parallels between the OTA situation and agentic commerce to build regulatory responses.

## Connection to Other Wiki Entries

- [[delegation-nation-comprehensive-research]] — AI agents as executors of purchasing decisions extends the delegation-of-decision-making concern; the "digital tax" framework maps to the paper's market concentration warnings
- [[agentic-commerce-deep-dive-fd-robonomics]] — This is Part II of the same series, covering economic implications after Part I established technical feasibility
- [[conflict-of-interest-in-llm-deployment]] — When AI agents influence purchasing, revenue incentives directly affect consumer outcomes
- [[systemic-fragility-in-ai-economies]] — Centralization of agentic commerce through single PSPs and top-of-funnel platforms creates systemic risk
- [[user-welfare-vs-company-incentive]] — The "digital tax" framework shows how platform incentives (extracting value from traffic) conflict with merchant and consumer welfare
- [[ai-agents-in-markets]] — AI agents as autonomous market participants reshaping distribution and merchant economics
- [[advanced-ai-assistants]] — Agentic commerce is the executor role of AI assistants applied to retail
- [[wu-2026-ads-in-ai-chatbots]] — Empirical evidence of sponsored product recommendations is directly relevant when agents mediate purchases
- [[gpt-5-1-openai]] — OpenAI's GPT models documented as surfacing sponsored options, relevant to agentic commerce integrity
