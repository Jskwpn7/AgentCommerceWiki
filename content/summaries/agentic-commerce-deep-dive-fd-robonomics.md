---
title: "Agentic Commerce Deep Dive (I) — FD, Robonomics"

created: 2026-06-05
updated: 2026-06-05
type: summary
tags: [digital-platforms, digital-consumer, corporate-accountability, cross-sector, research]
sources: [raw/articles/agentic-commerce-deep-dive-fd-robonomics.md]
confidence: medium
---

# Agentic Commerce Deep Dive (I)

**Author:** FD  
**Publication:** Robonomics (independent tech journal)  
**Date:** October 09, 2025  
**Source:** [[raw/articles/agentic-commerce-deep-dive-fd-robonomics.md]]

## Paper Details

| Field | Value |
|-------|-------|
| Title | Agentic Commerce | Deep Dive (I) |
| Author | FD (independent) |
| Publication | Robonomics |
| Date | October 09, 2025 |
| Format | Newsletter article |
| URL | https://robonomics.substack.com/p/agentic-commerce-deep-dive-i |
| Likes/Restacks | 31 likes, 6 comments, 2 restacks |

## Summary

This article provides a structured analysis of "agentic commerce" — the emerging paradigm where AI agents autonomously complete purchases on behalf of users. The author (FD) argues that meaningful discussion of agentic commerce requires understanding three foundational questions: what kind of commerce we're talking about, why Google and Meta previously failed at it, and which business model for third-party (3P) e-commerce is most likely to win.

The article examines two competing approaches to agentic commerce architecture:
1. **OpenAI's Agentic Commerce Protocol (ACP)** — works with any payment service provider (PSP); merchants remain the merchant of record (MoR)
2. **Perplexity's "Buy with Pro"** — Perplexity acts as the MoR, Walmart is merely the fulfiller

The author argues OpenAI's approach is preferable because it preserves merchant ownership of payments, tax, refunds, fraud, CRM, and first-party data.

## Key Frameworks and Arguments

### 1. Commerce Taxonomy
Drawing on Alex Rampell's framework, the article categorizes commerce into:
- **Impulse Buys** — low deliberation, fast decision
- **Routine Essentials** — habitual, low engagement
- **Life Purchases** — high deliberation, high trust required

For agentic commerce, **Lifestyle** and **Functional Purchases** are the most promising initial categories because they require research, opinions, and trust. The online TAM for these three categories alone is approximately **$3 trillion**.

### 2. 3P E-Commerce Spectrum
The article argues that third-party commerce exists on a spectrum, not as a binary:

| Model | Merchant of Record | Customer Relationships | Merchant Control |
|-------|-------------------|----------------------|------------------|
| **AMZN** | Platform | Platform owns | None |
| **ETSY/EBAY** | Platform (payment) | Shared | Partial (returns mediation) |
| **Taobao/PDD** | Merchant (escrow) | Shared | Moderate |
| **SHOP** | Merchant | Merchant owns 100% | Full |

**Why this matters for consumers:** Where agentic commerce platforms sit on this spectrum determines how much control merchants retain over data, how much disruption hits payment providers like Stripe, and ultimately how consumer data flows through the system.

### 3. ACP vs. Buy with Pro
The article provides detailed comparison of two agentic commerce architectures:

**ACP (OpenAI + Stripe):**
- ACP is agnostic to who the PSP is
- Works with any PSP and any agent
- OpenAI packages payment credential in shared token → merchant receives token → merchant's PSP processes payment
- Merchants pay processing fees + take rate to OpenAI

**Perplexity "Buy with Pro":**
- Perplexity is the MoR (appears on credit card bill)
- Walmart is just the fulfiller
- Funds go through Perplexity first; Stripe via Link processes checkout
- Perplexity carries more liability but also more control

The author's judgment: OpenAI's approach "passes the first test" and is preferable. Becoming the MoR would be "very concerning."

### 4. Why Google and Meta Failed
Both GOOGL and META avoided being the MoR, but that wasn't the reason their 3P commerce failed:
- Both realized ads are far more profitable than ecommerce
- META's payment UX was described as "a mess": 8+ steps, forced logins, endless redirects
- Meta Pay never reached adoption
- Meta Shops (FB/IG) defaulted back to link-out checkout by Sept 2025 — "Meta Commerce is officially dead"

### 5. Implications Preview
The article previews "Part II" which will cover winners vs. losers of agentic commerce, but does not elaborate further in this installment.

## Relevance to UK Consumer Harms

This article is relevant to UK Consumer Harms Research for several reasons:

- **Choice architecture in AI agents:** Agentic commerce represents an extreme form of choice architecture where the AI agent — not the consumer — makes the purchase decision. This raises questions about who sets the parameters of that choice and whether the agent's training data and commercial incentives influence which products it selects.

- **Data flow and privacy:** In ACP, merchants retain CRM and first-party data, but in Perplexity's model, the platform (MoR) controls the data pipeline. This has implications for how UK consumer data protection (UK GDPR) applies when AI agents are making purchases — who is the data controller?

- **Platform power concentration:** If agentic commerce platforms (like ChatGPT) become the primary way consumers shop, they effectively become digital gatekeepers in the retail space — echoing concerns raised in the [[delegation-nation-comprehensive-research]] paper about AI Assistants as gatekeepers.

- **Merchant vs. platform power:** The spectrum analysis (AMZN vs. SHOP models) shows how the architecture of agentic commerce determines where value accrues — to merchants, platforms, or payment providers. This connects to [[conflict-of-interest-in-llm-deployment]] where provider incentives may not align with consumer welfare.

- **Dark patterns in agency:** If an AI agent's recommendations are influenced by sponsored content or revenue-sharing arrangements, the resulting purchase decisions represent an even more opaque form of dark-pattern choice architecture than traditional UI-based manipulation.

- **Regulatory uncertainty:** The article highlights that agentic commerce is still in early stages, but the regulatory framework (CMA, FCA, ICO) has not yet addressed the specific consumer harms that arise when AI agents autonomously spend money on behalf of consumers. This connects to [[user-welfare-vs-company-incentive]].

## Connection to Other Wiki Entries

- [[advanced-ai-assistants]] — Agentic commerce is the executor role of AI assistants applied to the retail/consumer domain
- [[conflict-of-interest-in-llm-deployment]] — If LLMs recommend sponsored products during agentic commerce, this creates direct financial harm
- [[ai-agents-in-markets]] — Hadfield & Koh's framework applies directly to AI agents acting as autonomous purchasers in markets
- [[user-welfare-vs-company-incentive]] — The tension between merchants wanting data ownership vs. platforms wanting MoR control
- [[delegation-nation-comprehensive-research]] — Delegation of purchasing decisions to AI agents is a specific instance of "delegation of decision-making"; the 3P commerce spectrum maps directly to gatekeeper risks
- [[systemic-fragility-in-ai-economies]] — Correlated agent purchasing behaviour could create new systemic risks in retail markets
- [[wu-2026-ads-in-ai-chatbots]] — Empirical evidence that LLMs recommend sponsored products at high rates, directly relevant to agentic commerce integrity
- [[gpt-5-1-openai]] — OpenAI's model has been documented as surfacing sponsored options in purchasing contexts
