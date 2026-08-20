---
title: "Weekly Consumer Harms Research Review — 2026-08-10"
type: summary
date: 2026-08-10
sources:
  - arXiv search
  - web_search
  - web_extract
  - Semantic Scholar (rate-limited; fallback to web sources for paper discovery)
confidence: medium
tags:
  - consumer-harms
  - CMA
  - dark-patterns
  - AI-agents
  - drip-pricing
  - fake-reviews
  - FCA
  - pension-scams
  - algorithmic-collusion
---

# Weekly Consumer Harms Research Review — 2026-08-10

## A. New Wiki Pages to Create

### 1. CMA DMCCA Consumer Enforcement — First Year Summary

- **Source**: CMA press releases, GOV.UK cases, Mayer Brown / Winston Taylor legal analyses
- **Date range**: April 2025 – June 2026
- **Why relevant**: The CMA's new DMCCA enforcement powers (from April 2025) have been used aggressively. This is the single most active area of UK consumer protection enforcement right now. Over 14 businesses investigated; £1.95M+ in consumer refunds ordered; £5.7M+ in fines. The CMA explicitly states "we're just getting started."
- **Key cases to cover**:
  - **AA/BSM Driving Schools** (April 2026): £4.2M fine + £760K refunds for 80K customers — first drip pricing fines under DMCCA. Mandatory £3 booking fee dripped at checkout.
  - **Marks Electrical** (June 2026): £720K fine + £600K refunds — automatic opt-in charges for recycling/packaging services without consent.
  - **StubHub UK** (June 2026): £889K fine + £590K refunds for 50K+ customers — delivery and service fees added at final checkout stage.
  - **Euro Car Parks** (December 2025): £473K fine — first DMCCA information notice fine, for failing to respond to statutory notice.
  - **Adobe** (March 2026): Investigation opened into 50% early cancellation fees on "annual billed monthly" plans.
  - **Ryanair** (June 2026): Investigation into £8 "mandatory family seat" fees.
  - **Emma Sleep** (May 2026): High Court-endorsed settlement — misleading countdown timers, false discount claims.
- **Fake review investigations** (March 2026): Autotrader, Feefo, Dignity, Just Eat, Pasta Evangelists under probe for fake/misleading reviews under DMCCA.
- **Recommended page type**: summary
- **Recommended tags**: `CMA`, `DMCCA`, `drip-pricing`, `fake-reviews`, `enforcement`, `auto-opt-in`
- **Supersedes**: Any pre-DMCCA consumer enforcement content; the CMA's enforcement pace has fundamentally accelerated.

### 2. AI Agent Consumer Compliance — CMA March 2026 Guidance

- **Source**: CMA "Agentic AI and Consumers" research paper (9 March 2026)
- **Why relevant**: First comprehensive regulatory guidance on AI agents in consumer contexts. Covers risks including autonomous purchasing, price negotiation, customer service automation, and recommendation engines. Key message: "the use of AI does not change consumer law obligations."
- **Key risks flagged by CMA**:
  - Autonomous actions without human oversight (e.g., agent signing up for subscriptions)
  - Algorithmic pricing and potential collusion
  - Misrepresentation of agent identity/nature to consumers
  - Data privacy and consent issues
  - Vulnerable consumer protections
- **Four UK regulators (DRCF, CMA, FCA, ICO) all agree**: most AI agents fall within existing regulatory frameworks
- **DRCF horizon-scanning**: committed to work through 2026-2027 on interfaces, consumer robotics, and new technology
- **Recommended page type**: summary
- **Recommended tags**: `AI-agents`, `CMA`, `consumer-law`, `agentic-AI`, `DRCF`, `regulation`

### 3. Poisoned AI Models — NTS Scam Warning (June 2026)

- **Source**: National Trading Standards / Ask Silver (9 June 2026)
- **Why relevant**: Criminals actively poisoning LLM outputs to recommend scam websites. This is a novel consumer harm vector where AI search/recommendation systems become distribution channels for fraud.
- **Mechanism**: SEO manipulation, content injection into training data, and prompt engineering to boost scam sites in LLM responses
- **Recommended page type**: summary
- **Recommended tags**: `scams`, `LLM`, `AI-poisoning`, `National-Trading-Standards`, `fraud`

### 4. Dark Patterns in AI — arXiv Paper Summary (2510.18113)

- **Paper**: "Investigating the Impact of Dark Patterns on LLM-Based Web Agents" (Ersoy et al., IEEE S&P 2026)
- **arXiv ID**: 2510.18113
- **URL**: https://arxiv.org/abs/2510.18113
- **Authors**: Devin Ersoy, Brandon Lee, Ananth Shreekumar, Arjun Arunasalam, Muhammad Ibrahim, Antonio Bianchi, Z. Berkay Celik (Purdue, FIU, Georgia Tech)
- **Published**: October 2025
- **Abstract**: First systematic evaluation of dark pattern effectiveness on LLM web agents. Using LiteAgent framework and TrickyArena testbed (e-commerce, health, streaming, news), evaluated 6 agents across 3 LLMs (Claude 3.7 Sonnet, GPT-4o, Gemini 2.5 Pro). Key finding: agents susceptible to single dark patterns 41% of the time; higher-performing agents most vulnerable; combining dark patterns reduces task completion; vision-mode agents more susceptible.
- **Why relevant**: Critical empirical evidence that AI agents amplify dark pattern harm. AI shopping agents — increasingly deployed — may inadvertently subscribe users, make purchases, or consent to data sharing when encountering dark patterns.
- **Recommended page type**: summary
- **Recommended tags**: `dark-patterns`, `AI-agents`, `LLM`, `web-agents`, `empirical-study`, `IEEE-Sp`

### 5. EU Digital Fairness Act (DFA) — Consumer Protection Timeline

- **Source**: European Commission consultation, Osborne Clarke, Baker McKenzie
- **Why relevant**: Major upcoming EU regulation targeting dark patterns, addictive design, unfair personalisation, and algorithmic pricing transparency. Expected Q4 2026. Will indirectly affect UK businesses serving EU consumers.
- **Key provisions expected**:
  - Dark pattern prohibitions (manipulative flows, hidden opt-outs, false urgency)
  - Transparency for algorithmic/personalised pricing and ranking
  - Protection of minors on social media and gambling
  - Revision of CPC Regulation for cross-border enforcement
- **Recommended page type**: summary
- **Recommended tags**: `EU`, `DFA`, `dark-patterns`, `algorithmic-pricing`, `cross-border`

### 6. FCA Consumer Duty — Three-Year Review (July 2026)

- **Source**: FCA CP26/23, Simmons & Simmons, Global Regulation Tomorrow
- **Why relevant**: 31 July 2026 marks three years since Consumer Duty came into force. FCA published scope and proportionality consultation (29 June 2026, closes 18 September 2026) proposing changes to reduce burden on wholesale-primary firms. Policy Statement expected Q1 2027.
- **Key areas**:
  - Consumer Duty at three: embedding to recalibration
  - Scope clarification for wholesale firms
  - FCA review into firms' approaches to products and services (published 10 July 2026)
  - FCA review into consumer understanding (published 13 March 2026)
- **Recommended page type**: summary
- **Recommended tags**: `FCA`, `Consumer-Duty`, `financial-services`, `proportionality`

### 7. UK Fraud Strategy 2026-2029

- **Source**: GOV.UK (published 2026)
- **Why relevant**: The UK's first comprehensive national fraud strategy since 2019. Focuses on disrupting crime, supporting economic resilience, and improving justice access. Addresses AI-enabled fraud, cross-border fraud, and coordination between NCA, City of London Police, and HMRC.
- **Recommended page type**: summary
- **Recommended tags**: `fraud`, `NCA`, `national-strategy`, `AI-fraud`

### 8. Pension Scams — FCA/TPR Joint Warning (2026)

- **Source**: FCA, TPR, GOV.UK (9 June 2026 government crackdown)
- **Why relevant**: 5 million pension savers (42%) could be at risk of falling for scam tactics. Government cracking down on SSAS misuse. FCA estimates up to 40% of pension transfers linked to fraud or unsuitable solutions. New measures expected including potential primary legislation.
- **Recommended page type**: summary
- **Recommended tags**: `pension-scams`, `FCA`, `TPR`, `fraud`, `financial-harm`

## B. Existing Pages to Update

### CMA Enforcement / Online Pricing Pages
- Add StubHub UK fine (£889K + £590K refunds, 23 June 2026)
- Add Marks Electrical fine (£720K + £600K refunds, 18 June 2026)
- Update CMA enforcement totals: £1.95M+ refunds, £5.7M+ fines (as of June 2026)
- Add Ryanair investigation (June 2026)
- Add Adobe investigation (March 2026)
- Add fake review investigations (Autotrader, Feefo, Dignity, Just Eat, Pasta Evangelists)
- Add Viagogo investigation update (ongoing as of June 2026)

### DMCCA Pages
- Add enforcement case outcomes to demonstrate the regime is active
- Update enforcement statistics

### Dark Patterns Pages
- Add EU Digital Fairness Act timeline
- Add arXiv paper 2510.18113 as key empirical reference
- Add ICO automated decision-making guidance (31 March 2026)

### AI Regulation Pages
- Add CMA March 2026 AI agent guidance as core UK regulatory development
- Add DRCF horizon-scanning commitment
- Add NTS "poisoned AI" scam warning (9 June 2026)
- Add CERRE paper "Agentic AI and Consumer Protection" (July 2026)

### FCA / Financial Services Pages
- Add Consumer Duty three-year review details
- Add CP26/23 scope/proportionality consultation
- Add 5 million pension savers at risk statistic
- Add government SSAS crackdown measures

### Scams / Fraud Pages
- Add NTS poisoned AI model scam warning
- Add UK Fraud Strategy 2026-2029
- Add pension scam updates

### Food Labelling / Health Claims
- Add HFSS advertising ban (January 2026)
- Add ASA bans on misleading health claims (green kiwi powder, dietary supplements)
- Add Supreme Court plant-based "milk" ban confirmation (February 2026)

## C. Outdated / Stale Content

- **Any pre-DMCCA CMA enforcement timeline**: Should be updated to reflect DMCCA's transformative impact — investigations now close in 3-6 months vs. multi-year timelines under old regime (AA case: opened Nov 2025, closed April 2026 vs. Emma Sleep: opened Nov 2022, settled May 2026).
- **AI regulation gap narratives**: The CMA's March 2026 guidance demonstrates the UK has moved from "gaps exist" to "existing law applies" for AI agents. Pages claiming regulatory vacuum are now stale.
- **Dark patterns = unregulated**: Multiple jurisdictions now actively regulating dark patterns (UK DMCCA, EU DFA coming, US FTC enforcement). Any pages suggesting dark patterns are largely unaddressed should be updated.

## D. Orphaned / Undercovered Areas

### 1. Agentic AI Shopping Assistants — Consumer Risk
- No existing wiki page covers the specific consumer risks of AI shopping agents encountering dark patterns
- The empirical evidence (41% susceptibility rate from IEEE S&P paper) suggests significant consumer harm potential
- **Recommended new page**: `AI-shopping-agents-consumer-harm`

### 2. Drip Pricing as Consumer Harm Pattern
- While CMA cases are documented, there is no standalone analysis of drip pricing as a systemic consumer harm
- Covers ticketing (StubHub, viagogo), driving schools (AA), and potentially other sectors
- **Recommended new page**: `drip-pricing`

### 3. Algorithmic Collusion — Economic Theory Meets Regulation
- Multiple arXiv papers exist (Frick 2604.15825, Ye 2502.15084, Zhang 2403.06150)
- UK/EU regulators actively investigating (Poland's UOKiK, EC)
- UK-specific regulatory gap: no dedicated CMA investigation yet, but theory is well-developed
- **Recommended new page**: `algorithmic-collusion`

### 4. Trader Recommendation Platforms — CMA Concerns
- CMA wrote to several TRP platforms (May 2026) over misleading quality claims, outdated vetting, poor complaint handling
- Affects tradespeople, lawyers, financial advisers, and other professional services
- No existing wiki coverage
- **Recommended new page**: `trader-recommendation-platforms`

### 5. AI Poisoning of Search/Recommendation Systems
- Novel harm vector identified by NTS (June 2026)
- Criminals actively poisoning LLM outputs to promote scam sites
- Intersection of AI safety and consumer fraud
- **Recommended new page**: `AI-poisoning-consumer-fraud`

---

## Key Sources Used

| # | Source | URL |
|---|--------|-----|
| 1 | CMA: CMA consumer enforcement in 2026 (Winston Taylor) | https://www.winstontaylor.com/insights/cma-consumer-protection-enforcement-in-2026 |
| 2 | CMA: "We're Just Getting Started" (Mayer Brown) | https://www.mayerbrown.com/en/insights/publications/2026/08/were-just-getting-started |
| 3 | CMA: StubHub UK refund order | https://www.gov.uk/government/news/cma-orders-stubhub-uk-to-refund-customers-over-hidden-fees |
| 4 | CMA: Adobe investigation | https://www.gov.uk/government/news/cma-investigates-adobe-over-concerns-about-cancellation-fees |
| 5 | CMA: Ryanair investigation | https://www.gov.uk/government/news/cma-investigates-ryanair-over-charging-parents-to-sit-with-children |
| 6 | CMA: AA/BSM Driving Schools fine | https://www.gov.uk/government/news/cma-orders-the-aa-and-bsm-driving-schools-to-refund-learner-drivers |
| 7 | CMA: Marks Electrical order | https://www.gov.uk/government/news/cma-orders-marks-electrical-to-refund-customers |
| 8 | NTS: Poisoned AI models | https://www.nationaltradingstandards.uk/news |
| 9 | UK Fraud Strategy 2026-2029 | https://www.gov.uk/government/publications/fraud-strategy-2026-to-2029 |
| 10 | FCA: Consumer Duty three-year review | https://www.simmons-simmons.com/en/publications/cmn92abw80056ukto0v9dn2yr |
| 11 | arXiv 2510.18113: Dark Patterns on LLM Agents | https://arxiv.org/abs/2510.18113 |
| 12 | CMA: Agentic AI and Consumers guidance | https://www.gov.uk/government/publications/agentic-ai-and-consumers |
| 13 | ICO: Automated Decision Making Consultation | (31 March 2026) |
| 14 | EU Digital Fairness Act (Baker McKenzie) | https://connectontech.bakermckenzie.com/2026-regulatory-watch |
| 15 | Osborne Clarke: UK Consumer Law 2026 | https://www.osborneclarke.com/insights/regulatory-outlook-january-2026-consumer-law |
| 16 | BEUC: Dark Patterns Complaints | https://www.beuc.eu/position-paper/dark-patterns-and-eu-consumer-law-acquis |
| 17 | FCA: 5M Pension Savers at Risk | https://www.fca.org.uk/news/press-releases/5m-pension-savers-could-put-retirement-savings-risk-scammers |
| 18 | GOV.UK: Government Crackdown on Pension Scams | https://www.gov.uk/government/news/government-crack-down-on-pension-scams |

## arXiv/Semantic Scholar Limitations

- arXiv API was rate-limited during this run (HTTP 429 responses)
- Semantic Scholar API also rate-limited (HTTP 429)
- Paper 2510.18113 was found via web search (IEEE S&P 2026 acceptance) and extracted via ar5iv
- Related papers identified via web search: Frick 2604.15825 (Convergence to collusion in algorithmic pricing), Ye 2502.15084 (Algorithmic Collusion under Observed Demand Shocks), Zhang 2403.06150 (Artificial Intelligence, Data and Competition)
- **Recommendation**: Retry arXiv search with extended delays (>10s between queries) in next run

## Next Review Focus Areas

1. Monitor Viagogo investigation outcome (expected Summer 2026)
2. Track EU Digital Fairness Act proposal (expected Q4 2026)
3. Watch for CMA's response to reference pricing trial (judgment pending)
4. Monitor FCA Consumer Duty Policy Statement (expected Q1 2027)
5. Investigate Ryanair investigation outcome (expected within 6 months)
6. Follow up on Adobe investigation (next update autumn 2026)
7. Search for newer arXiv papers on agentic AI consumer harms
