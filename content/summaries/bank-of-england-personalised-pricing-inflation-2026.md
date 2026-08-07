---
title: "This Time It's Personal: Dynamic, Personalised Pricing and Inflation — Bank of England (2026)"
created: 2026-07-02
updated: 2026-07-02
type: summary
tags: [personalised-pricing, dynamic-pricing, algorithmic-pricing, inflation-measurement, boe-insights, price-discrimination, inflation-expectations, consumer-harm]
sources:
  - url: https://www.bankofengland.co.uk/bank-insights/2026/this-time-its-personal-the-rise-of-dynamic-personalised-pricing-and-what-it-means-for-inflation
    access: 2026-07-02
authors:
  - Clare Lombardelli, Rupal Patel (Bank of England)
cross_links:
  - [[algorithmic-collusion-pricing]]
  - [[dark-pattern]]
  - [[regulatory-failure]]
  - [[ai-mode-shortlist-gatekeeping]]
  - [[systemic-fragility-in-ai-economies]]
relevance:
  consumer_harm: high
  sector: [e-commerce, energy, financial-services, consumer-tech, retail, transport, hospitality]
---

# This Time It's Personal: Dynamic, Personalised Pricing and Inflation

**Source:** Bank of England Insights, published 2026
**Authors:** Clare Lombardelli, Rupal Patel (Bank of England)
**URL:** https://www.bankofengland.co.uk/bank-insights/2026/this-time-its-personal-the-rise-of-dynamic-personalised-pricing-and-what-it-means-for-inflation
**Reading time:** ~15 min

## Summary

A Bank of England insights article documenting the structural shift in pricing across the UK economy — from static, uniform prices to algorithmically-driven dynamic and personalised pricing. The article covers three tiers of pricing adoption (rules-based, market-responsive AI, personalised), inflation measurement challenges, the impact on consumer welfare and market competition, and psychological channels affecting inflation expectations. It represents the first major central bank publication to directly acknowledge that AI-enabled personalised pricing is creating a world where different consumers face genuinely different prices for identical goods and services.

## Three Tiers of Pricing Adoption

| Tier | Description | Current adoption (DMP Q4 2025) | Planned growth |
|---|---|---|---|
| Rules-based | Pre-set rules: time of day, weekday/weekend, stock levels | Widely used (recreational services, transport) | Stable, being replaced by market-responsive |
| Market-responsive | AI/algorithmic pricing in response to demand, capacity, competitor prices | 21% of consumer-facing firms | 31% in one year (+10pp) |
| Personalised | Prices differ across customers based on characteristics/behaviour (loyalty cards, individual/group data) | "Widely adopted across all sectors" | All sectors planning increases |

- DMP Survey: 1,600+ firms across retail, accommodation, food, recreational services, health, other services
- All sectors are proposing to increase adoption over the coming year
- Electronic shelf labels (widespread in Europe) being experimented with in UK supermarkets

## Key Data Points

### Menu Cost Collapse
- Hotel room rates changing at least once per month: **15% in 2005 → ~80% today**
- This represents a fundamental structural shift — the economic barrier to frequent price changes has essentially disappeared

### Inflation Measurement Challenges
- **ONS March 2026:** Started using bulk weekly grocery scanner data, capturing loyalty card prices and person-specific discounts for ~50% of grocery market
- **Impact on CPI:** Scanner data would have reduced headline CPI by **0.03pp** (Jan 2022–Jun 2025), but **0.1pp higher** during elevated food inflation months
- **Key insight:** "These relatively small overall effects will continue to mask much larger differences between the prices faced by different households"
- ONS household Cost Indices (quarterly, since 2023) show income decile inflation already varies significantly

### Hotel Price Trajectory — The Null Result
- Despite the explosion in dynamic pricing since 2005, cumulative accommodation price increases are **broadly in line** with less-dynamic services
- Dynamic pricing is used more to manage capacity than raise prices overall
- This null result is important: dynamic pricing ≠ inflationary by default

### Psychological Channels — The Hidden Risk
- **44% of households** expect prices will be higher as a result of firms using dynamic pricing
- **29%** expect prices about the same; **8%** expect lower
- When prices fluctuate due to AI-enabled dynamic pricing, people **perceive prices as higher on average** (asymmetric price salience)
- This may cause inflation expectations to drift upwards even if average prices do not

### Food — The High-Risk Sector
- Food has **high frequency of price changes** (weekly/daily) AND **high impact on inflation expectation formation**
- This combination makes food the most vulnerable sector to upward inflation expectation ratcheting
- Supermarket electronic shelf labels could accelerate this further

## Consumer Harm Analysis

### 1. Perfect Price Discrimination — The Fundamental Shift
The article explicitly states firms are moving toward textbook "perfect price discrimination" — charging close to the maximum price each consumer is willing to pay. This represents a fundamental change in the consumer-seller relationship:

- **Pre-AI:** Consumers at least had the possibility of finding the same price others paid (uniform or time-based pricing)
- **AI-era:** The price one consumer sees may be unknowingly different from what everyone else pays for the same product

### 2. Invisibility of Personalised Pricing
There is no mechanism for consumers to detect whether they are being personalised-priced. Unlike peak/off-peak rail pricing (which the Bank notes is "well communicated and widely understood"), personalised pricing through loyalty cards and ML models is opaque. Consumers cannot:
- Compare their price to the reference price
- Know what a "fair" price would be
- Exercise meaningful price elasticity when they don't know the alternative

### 3. Inflation Measurement Breakdown
When prices differ for the same thing across consumers, the concept of a "representative price" becomes meaningless. This has cascading effects:
- CPI becomes less informative about any individual household's experience
- MPC monetary policy decisions are based on an aggregate measure that may not reflect lived reality
- The ONS scanner data improvement is a step forward but remains aggregate-level, not personalised

### 4. Algorithmic Collusion — The Article's Acknowledgment
The Bank explicitly references the academic literature on algorithmic collusion (Calvano et al 2020, Brown and MacKay 2022, Fish et al 2026, CMA pricing algorithms report):

> "In some unsettling experiments, algorithms have learnt over time to charge above competitive and static prices and drifted into tacit, collusive behaviour after discovering that constant undercutting is bad for profits."

- Algorithmic collusion is described as "still rare, but regulators are alert"
- This is the same mechanism that drives the wiki's `[[algorithmic-collusion-pricing]]` concept
- The fact that a central bank publication acknowledges this is significant

### 5. Inflation Expectations as a Self-Fulfilling Mechanism
The asymmetry in price salience (people notice rises more than falls) combined with more frequent price changes creates a psychological channel:
- More volatile prices → higher perceived inflation → higher inflation expectations
- Higher expectations → wage/price dynamics that may push actual inflation up
- Food, as the high-frequency/high-impact sector, is the primary transmission channel

### 6. Regulatory Fragmentation
The article references:
- **CMA guidance** on price transparency and competition law for pricing algorithms (Nov 2024)
- **FTC surveillance pricing study** (Jan 2025) — wide range of personal data used to set individualized prices
- **EU competition authorities** investigating antitrust risks of algorithmic pricing
- No single framework currently addresses the full scope of personalised pricing harms

## Connections to Other Wiki Entries

- **`[[algorithmic-collusion-pricing]]`** — The Bank's explicit acknowledgment of algorithmic tacit collusion connects directly to this concept. The pricing adoption data (21%→31% planned) provides the adoption curve for the mechanism described in the wiki.
- **`[[ai-mode-shortlist-gatekeeping]]`** — Both studies show the same underlying dynamic: AI systems determining what different consumers see/face. AI Mode determines what brands consumers consider; personalised pricing determines what prices consumers face. Both are opaque and mode-dependent.
- **`[[dark-pattern]]`** — Personalised pricing without disclosure functions as a dark pattern — a choice architecture manipulation where consumers cannot exercise informed consent because they lack the reference information needed to evaluate the price.
- **`[[systemic-fragility-in-ai-economies]]`** — Personalised pricing at scale creates correlated pricing behavior across firms using similar ML models, with the potential for economy-wide upward price pressure through expectation channels.

## Methodology Note

This is a Bank of England insights article, not a peer-reviewed academic paper. It is:
- Written by BoE staff economists (Lombardelli and Patel)
- Based on DMP Survey data, ONS scanner data, Bank's own surveys (Inflation Attitudes Survey)
- Acknowledges multiple external academic sources (Calvano, Brown/MacKay, Ellison, etc.)
- Represents institutional central bank analysis, not independent research

## Key Policy Implications (This Wiki's Analysis)

1. **DMCC Act 2024:** Personalised pricing without price transparency may constitute an unfair trading practice under the Act's "intermediation" and "dark pattern" provisions
2. **CPRs 2008:** Material information requirements may apply to pricing — if a consumer pays more than another for identical goods, is the price difference a "material omission"?
3. **CMA market study power:** Personalised pricing adoption curve (21%→31% in one year) suggests potential for a market investigation
4. **Bank's own inflation measurement:** If the CPI is becoming less representative of household experience, monetary policy transmission may be weakening
