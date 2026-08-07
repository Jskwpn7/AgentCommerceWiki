---
title: "Only 25% of cited sources overlap between ChatGPT's different reasoning modes [Study]"
authors: Margarita Loktionova, Christine Skopec
date: 2026-06-30
source_url: https://www.semrush.com/blog/chatgpt-reasoning-ai-visibility/
extraction: web_extract (Semrush blog)
tags: [chatgpt, reasoning-modes, ai-visibility, source-divergence, semrush-study]
---

# Only 25% of cited sources overlap between ChatGPT's different reasoning modes [Study]

**Authors:** Margarita Loktionova, Christine Skopec (Semrush)
**Contributor:** Kevin Indig (Growth Advisor, Growth Memo)
**Published:** June 30, 2026
**URL:** https://www.semrush.com/blog/chatgpt-reasoning-ai-visibility/
**Reading time:** ~10 min

## Abstract / Key Thesis

Most AI visibility strategies treat ChatGPT as a single system. This study shows that high-reasoning mode (Thinking) and minimal-reasoning mode (Instant) cite fundamentally different sources — only 25.6% of cited domains overlap for the same prompts. Nearly three-quarters of cited sources are entirely different. The choice of reasoning mode determines not just the volume but the identity of sources presented to consumers.

## Methodology

- **Model:** ChatGPT 5.2
- **Prompts:** 100 prompts across 20 buyer journeys in 4 categories
- **Response pairs:** 200 total (each prompt × 2 modes)
- **Categories:** B2B SaaS, Finance, Consumer Tech, Health and Lifestyle
- **Buyer journey stages:** Problem, Exploration, Comparison, Validation, Selection (5 stages each)
- **Minimal reasoning** = Instant mode (default fast-response)
- **High reasoning** = Thinking mode (deeper, multi-step research)
- **Tracked metrics:** Citation rate, average citations per response, fan-out queries, domain overlap, source type composition, brand persistence

## Key Findings

### 1. High reasoning cites sources and uses web searches much more
- Citation rate: 50% (Instant) → 68% (Thinking), +18pp
- Average citations: 2.6 → 4.5 (nearly double)
- Fan-out sub-queries: 4.6× higher in Thinking mode (1,130 total vs 245)
- Response length increases only slightly — more citations packed into same-length output
- 173 unique domains in Thinking vs 127 in Instant; 99 domains appear exclusively in Thinking
- Complex prompts (comparisons, evaluations, regulatory questions) trigger high-reasoning mode automatically even for free-tier users

### 2. Each reasoning mode cites different domains
- Only 25.6% of cited domains shared between modes
- Source composition shifts dramatically:
  - Reddit: 15% → 7% (−53%)
  - UGC / review sites: 14.3% → 6% (−58%)
  - Government / academic: 1.9% → 8.8% (+363%)
  - Official documentation: 12.4% → 17.5% (+41%)
  - Brands: 62.4% → 60.6% (−3%)
- "The brand that wins under minimal reasoning is not the brand that wins under high reasoning. The mix of source types is different. The stages where citations appear are different. These are two different systems." — Kevin Indig

### 3. The biggest mode gap shows up early in the buyer journey
- Problem stage: citation rate gap = 35pp (highest)
- Comparison stage: where high reasoning does the most research — 24 sub-queries per response vs 5.5; average citations peak at 9.8 vs 5.8
- Selection stage: high reasoning still cites more (4.7 vs 2.6 on average)
- Minimal reasoning often answers early-funnel questions without citing external sources

### 4. Under high-reasoning mode, brands persist across the journey
- Minimal reasoning: zero journeys show full-funnel brand persistence (Problem → Selection)
- High reasoning: brand continuity maintained in 4 of 20 journeys
- Same domain cited multiple times within a single response: 51 of 100 (high) vs 26 of 100 (minimal)

### 5. Reasoning lift varies sharply by category
| Category | Citation Rate Increase |
|---|---|
| Finance | +28pp |
| Health and Lifestyle | +24pp |
| B2B SaaS | +16pp |
| Consumer Tech | +4pp |

- Consumer Tech is a striking outlier: despite running the most sub-queries per prompt (13.4, highest of all categories), high reasoning cites nearly the same brands as minimal reasoning — the model already has strong internal knowledge for common Consumer Tech topics

## Consumer Harm Analysis

### Inconsistent Consumer Advice
Same question → different sources → different brand recommendations depending on reasoning mode. Consumers cannot control which mode their query hits, and complex queries are automatically routed to high reasoning even for free-tier users.

### Source Composition Bias
High reasoning systematically downweights UGC/review-site content (which consumers often trust most), replacing it with institutional sources. This may improve factual accuracy but disadvantages:
- Niche products and emerging brands without institutional backing
- Non-English content and international sources
- Consumer-generated reviews that are often the most trusted by consumers

### Opaque Ranking Mechanics
Consumers have no visibility into:
- Which reasoning mode was used for their query
- Which sub-searches were made
- What sources were found and discarded
- Why a particular brand or source was recommended

### Top-of-Funnel Compounding
Under high reasoning, early-stage citations persist through decision stages. This creates a structural advantage for established brands that have strong Problem-stage content and makes it harder for new entrants to gain footing in consumer-facing AI recommendations.

### Highest-Stakes Categories Most Affected
Finance (+28pp) and Health (+24pp) show the largest reasoning lift — categories where consumer decisions are highest-stakes. Consumers asking financial or health questions are most likely to receive divergent advice based on opaque mode selection.

### Kevin Indig's "Reasoning Lift" as a Consumer Protection Concern
The concept of "reasoning lift" — the gap between outputs in one mode versus another — is itself a consumer protection issue. If the same model produces fundamentally different outputs for the same question based on an opaque internal routing mechanism, consistency and fairness obligations are implicated.

## Connections to Other Wiki Entries

- **[[omnithink-slow-thinking-writing]]** — OmniThink is one of three deep-research systems in the WARP attack paper; the reasoning-mode divergence demonstrated here would affect OmniThink's poisoning vulnerability differently depending on mode
- **[[wu-2026-ads-in-ai-chatbots]]** — 18/23 LLMs recommend sponsored products; reasoning mode divergence means sponsored product recommendations would also differ between modes, compounding consumer confusion
- **[[banal-deception-llm-chatbots]]** — Source composition shifts (less UGC, more institutional) may make AI recommendations appear more authoritative without consumers understanding the basis for source selection
- **[[regulatory-failure]]** — Current consumer protection frameworks have no mechanism to evaluate or mandate consistency across reasoning modes of the same model
- **[[systemic-fragility-in-ai-economies]]** — Reasoning-mode divergence as an additional mechanism of correlated behavior — brands optimize for one mode and lose visibility when mode selection shifts
- **[[ai-agents-in-markets]]** — AI agents mediating consumer choices must navigate mode-variant source landscapes, creating additional opacity in their recommendations
- **[[conflict-of-interest-in-llm-deployment]]** — High-reasoning mode's preference for institutional sources may align with LLM providers' incentives (more authoritative, less controversial sources)

## Cross-References in Wiki

- Kevin Indig also cited in:
  - [[warp-deep-research-poisoning-zhang-2026]] — reasoning mode affects which deep-research systems are vulnerable to UGC poisoning
  - [[omnithink-2501.09751]] — OmniThink is a deep-research system evaluated in the WARP attack paper
