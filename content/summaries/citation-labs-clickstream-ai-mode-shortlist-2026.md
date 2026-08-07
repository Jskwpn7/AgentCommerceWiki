---
title: "BOFU Shortlists in Google AI Mode: 48-Participant Behavioral Study — Citation Labs / Clickstream (2026)"
created: 2026-07-02
updated: 2026-07-02
type: summary
tags: [google-ai-mode, shortlist-bias, behavioral-study, ai-visibility, consumer-harm, clickstream, citation-labs]
sources:
  - url: https://citationlabs.com/funnels-new-gatekeeper-google-search-ai-mode-shortlisting-behavioral-study/
    access: 2026-07-02
authors:
  - Citation Labs / Clickstream Solutions
  - Eric Van Buskirk (Clickstream)
  - Kevin Indig (Growth Memo, sponsoring author)
cross_links:
  - [[agentic-commerce-tokenization]]
  - [[ai-shopping-agents]]
  - [[banal-deception-llm-chatbots]]
  - [[conflict-of-interest-in-llm-deployment]]
  - [[reasoning-lift]]
  - [[systemic-fragility-in-ai-economies]]
  - [[wu-2026-ads-in-ai-chatbots]]
relevance:
  consumer_harm: high
  sector: [e-commerce, digital-platforms, financial-services, consumer-tech, insurance]
---

# BOFU Shortlists in Google AI Mode: 48-Participant Behavioral Study

**Source:** Citation Labs / Clickstream Solutions, published March 2026 (blog post 2026-06-30)
**URL:** https://citationlabs.com/funnels-new-gatekeeper-google-search-ai-mode-shortlisting-behavioral-study/
**Reading time:** ~20 min

## Summary

This is the third in a series of usability studies (sponsored by Citation Labs, previously published on Kevin Indig's Growth Memo) examining how consumers behave in Google Search vs. Google AI Mode. The study focuses on bottom-of-funnel (BOFU) purchase research, comparing how buyers build a candidate set for major purchases in Google AI Mode versus Google's standard Search experience.

**Core thesis:** Google AI Mode intensifies shortlist acceptance behavior. The default state in AI Mode is acceptance, not construction. Brands absent from the AI-generated shortlist become invisible at the decision stage.

## Methodology

- **Design:** Remote, unmoderated think-aloud usability study (UXtweak platform)
- **Participants:** 48 U.S.-based consumers (from Prolific panel)
  - 21 excluded (7 technical issues, 14 insufficient engagement)
- **Tasks:** 185 major-purchase tasks across 4 categories
  - Insurance (n=27 AI Mode), Television (n=46), Laptop (n=29), Washer/Dryer (n=47)
- **Duration:** 23 hours total, ~30 min per participant
- **Data:** Screen recordings + speak-aloud audio + post-task surveys + 275+ pages of transcribed audio
- **Analysis:** Trained analysts coded micro/macro behaviors; statistical confidence noted as directional (wider CIs than large-scale surveys)

**Task protocol:** For each task, participants completed a major-purchase research session in either AI Mode or standard Search, then reported their final shortlist and confidence.

## Key Findings

### 1. Shortlist Origin — AI Mode Is Acceptance, Not Construction

| Shortlist Origin | AI Mode | Search |
|---|---|---|
| AI Adopted (direct from AI, no external check) | **88%** of 149 AI Mode tasks | — |
| AI Verified (checked externally) | — | — |
| User Built (independent, multi-source) | **8 of 147** codeable tasks | Nearly 50% built from multiple sources |
| Hybrid | — | — |

- **64% of AI Mode participants clicked nothing at all** during the task (read AI output, declared finalists)
- In Search, ~89% clicked on something; half built independent shortlists
- For insurance tasks: **85% of AI Mode participants clicked nothing**
- Among the 117 AI Adopted tasks, ~85% showed no internal verification; ~15% verified inline (opened product cards without leaving the page)

### 2. Position in AI Output Strongly Predicts Final Choice

- **74% chose the first-ranked item** in the AI response as their top pick
- Mean rank of first choice: **1.35** (across all AI Mode tasks)
- Only **10% chose something ranked 3rd or lower**
- **26% overrode rank** (typically based on brand recognition), but 81% of those overrides still kept the AI-generated shortlist — they picked a different item *from* the AI's list, not from outside it

### 3. AI Framing Dominates Trust in AI Mode; Multi-Source Convergence Dominates in Search

| Trust Signal | All AI Mode | Insurance | Search (laptop+insurance) |
|---|---|---|---|
| AI framing | **37%** | **59%** | **6%** |
| Brand recognition | 34% | 26% | 23% |
| AI trust (general) | 26% | 22% | 11% |
| Source trust | 17% | 4% | 23% |
| Multi-source convergence | **5%** | 7% | **37%** |

- AI framing (the AI's description itself driving the decision) was the dominant trust signal in AI Mode — especially for insurance (59%) and categories with less prior brand knowledge
- In Search, participants built trust through corroboration across multiple sources (37%)

### 4. Brand Outcomes Highly Concentrated in AI Mode

| Category | Top Choice | 2nd | 3rd | Top-3 Share |
|---|---|---|---|---|
| Insurance (n=25) | Geico (52%) | Travelers (48%) | State Farm (28%) | ~64% |
| Laptop (n=29) | Lenovo ThinkPad (~52%) | Apple MacBook (~34%) | Dell XPS (~7%) | ~93% |
| Television (n=42) | LG (~21%) | Samsung (~14%) | Sony (~10%) | ~45% |
| Washer/Dryer (n=46) | LG (~33%) | Electrolux (~11%) | Whirlpool (~4%) | ~48% |

- Insurance: top 3 brands accounted for ~64% of AI Mode choices vs ~30% in Search
- Laptops: Lenovo ThinkPad + MacBook variants captured most AI Mode choices, no other brand appearing more than once
- Search distributed more broadly; HP EliteBook appeared 3×, ASUS once (vs. ThinkPad/MacBook dominance in AI Mode)

### 5. External Visits — Verification, Not Exploration

- Only **23% of AI Mode tasks** involved visiting an external website (vs. **67% in Search**)
- External visits in AI Mode were for **verification** of a candidate already under consideration (Best Buy, Dell, Lenovo, LendingTree, WalletHub)
- External visits in Search were for **discovery and comparison**

### 6. Reading Behavior — Deep Readers Still Adopt

- **70% skimmed**, 18% scanned, **<7% read comprehensively** in AI Mode
- Among the rare deep readers, **88% still adopted the AI shortlist** — deep reading produced more confident acceptance, not rejection

### 7. Narrowness Frustration Surprisingly Low

- Narrowness frustration (explicit signaling the option set was too limited): **15% in AI Mode, 11% in Search** — no statistically meaningful difference
- Participants delegated to AI without feeling constrained

## Consumer Harm Analysis

### Structural Brand Visibility Bias
Brands missing from the AI-generated shortlist become invisible at the decision stage. In AI Mode, 88% of shortlists came directly from the AI output. The "gatekeeper" function has moved upstream to Google's recommendation layer. This creates:
- **Barrier to entry** for challenger brands and newer entrants
- **Consolidation risk** — top 3 brands capture 64–93% of outcomes depending on category
- **Opaque selection** — consumers have no visibility into what was considered and discarded

### Trust Signal Manipulation Risk
When AI framing (not independent corroboration) becomes the dominant trust signal (59% for insurance in AI Mode), the mechanism that determines brand preference is Google's prompt engineering and knowledge synthesis, not consumer evaluation of evidence. This means:
- Brands can (and are) optimizing for AI visibility through structured data, content patterns, and citation strategy
- Consumer "trust" in AI recommendations is based on persuasive framing, not verified product comparison

### Opaque Ranking in AI Output
The AI output ranking is not a search ranking — it is a recommendation ranking. The study shows 74% of consumers choose rank 1. This is functionally equivalent to a sponsored placement with no disclosure. No regulatory framework currently treats this as a disclosure issue.

### Insurance Sector — Highest Risk Category
Insurance showed the most extreme AI Mode effects: 85% no-click rate, 59% AI framing as trust signal, top 3 brands capturing 64% of choices. Insurance is a regulated sector where consumers should have access to transparent comparison mechanisms. AI Mode effectively replaces comparison shopping with a recommendation shortcut.

### Kevin Indig's Three Takeaways (Consumer Harm Framing)

1. **"If your brand is not in the AI's output, it's invisible"** — structural barrier to consideration
2. **"How the AI presents your brand matters as much as whether it appears"** — framing is the new ranking signal
3. **"Challenger brands need recognition before the AI moment"** — pre-AI awareness campaigns become mandatory, increasing marketing costs for newer/smaller entrants

## Connections to Other Wiki Entries

- **[[reasoning-lift]]** — Same underlying mechanism: the mechanism determining which brands/surfaces consumers see is opaque and mode-dependent. AI Mode amplifies this effect further (88% acceptance vs. 50% citation rate for ChatGPT Instant)
- **[[conflict-of-interest-in-llm-deployment]]** — Google's AI Mode creates the same conflict: the recommendation layer benefits from brands that optimize for AI visibility (Citation Labs' business model), not from unbiased consumer outcomes
- **[[banal-deception-llm-chatbots]]** — The 7% who read comprehensively but still adopted the AI shortlist exemplifies how AI-generated content produces co-produced deception through truth-default exploitation
- **[[wu-2026-ads-in-ai-chatbots]]** — Both studies show that AI systems are optimized for commercial outcomes; AI Mode narrows choices to a smaller set of brands, while ChatGPT recommends sponsored products at high rates
- **[[systemic-fragility-in-ai-economies]]** — AI Mode as a systemic fragility mechanism: when a single recommendation layer determines brand outcomes for millions of consumers, correlated behavior and limited risk-bearing become structural features
- **[[agentic-commerce-tokenization]]** — Both address the same question: what happens when AI systems sit between consumers and purchasing decisions?
- **[[ai-shopping-agents]]** — AI Mode functions as an AI shopping agent for the majority of users (88% acceptance rate). The study provides behavioral evidence for the preference distortion mechanisms described in the AI shopping agents literature

## Study Limitations (As Reported by Authors)

- Sample size (48 participants) means wider confidence intervals than large-scale surveys
- Findings are directional, not population-level estimates
- U.S.-only participants (not generalizable to other markets)
- Only 4 product categories studied (not comprehensive across all purchase types)
- No systematic coding of whether every external destination first appeared in the AI answer

## Author Bias Note

This study was sponsored by Citation Labs (a firm that helps brands improve AI visibility) and published through Kevin Indig (Growth Memo). The authors have a clear commercial interest in demonstrating AI Mode's narrowing effects, as this finding validates their business proposition. Consumers should treat the magnitude of effects (percentages) with caution, though the directional findings are consistent with related research.
