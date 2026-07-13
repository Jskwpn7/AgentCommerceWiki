---
title: "ChatGPT Reasoning Modes Produce Divergent Source Citations — Semrush + Kevin Indig (2026)"
created: 2026-07-02
updated: 2026-07-02
type: summary
tags: [ai-visibility, reasoning-modes, chatgpt, search-behavior, consumer-harm, source-divergence]
sources: [https://www.semrush.com/blog/chatgpt-reasoning-ai-visibility/]
confidence:
  overall: high
  methodology: experimental study, 100 prompts, 200 responses (minimal vs high reasoning)
  data_quality: high — controlled A/B comparison on same prompts
---

# ChatGPT Reasoning Modes Produce Divergent Source Citations — Semrush + Kevin Indig (2026)

## Summary

Semrush and growth advisor Kevin Indig conducted an experimental study comparing ChatGPT's two reasoning modes — **Instant** (minimal reasoning, default fast-response) and **Thinking** (high reasoning, deeper multi-step research). They ran 100 prompts across 20 buyer journeys in four categories (B2B SaaS, Finance, Consumer Tech, Health and Lifestyle), each with five stages (Problem, Exploration, Comparison, Validation, Selection). For each prompt, they generated responses in both modes (200 total responses) and analyzed citation behavior, source composition, and brand persistence.

The central finding: **high-reasoning and minimal-reasoning ChatGPT behave like fundamentally different search engines**. Only 25.6% of cited domains overlap between the two modes for the same prompts. Three-quarters of cited sources are entirely different. The choice of reasoning mode determines not just how many sources are cited, but which sources are cited — meaning consumers receive different informational foundations depending on which mode they are in.

This has direct implications for consumer harm: if two consumers ask the same product comparison question but ChatGPT serves them in different reasoning modes, they may be recommended entirely different brands with entirely different source justifications. There is no guarantee of consistency or fairness in consumer-facing AI advice.

## Key Findings

### Citation Volume and Depth
- **Citation rate**: jumps from 50% (Instant) to 68% (Thinking) — +18 percentage points
- **Sources per response**: nearly doubles from 2.6 to 4.5
- **Fan-out sub-queries**: 4.6× more in Thinking mode (1,130 total web searches vs 245 for Instant)
- Response length increases only slightly — more citations are packed into roughly the same output, not diluted by extra text
- 173 unique domains cited in Thinking vs 127 in Instant; 99 domains appear exclusively in Thinking mode

### Source Composition Shift
| Source Type | Minimal Reasoning | High Reasoning | Change |
|---|---|---|---|
| Reddit | 15% | 7% | −53% |
| UGC / review sites | 14.3% | 6% | −58% |
| Government / academic | 1.9% | 8.8% | +363% |
| Official documentation | 12.4% | 17.5% | +41% |
| Brands | 62.4% | 60.6% | −3% |

- High reasoning systematically downweights UGC and upweights authoritative sources
- For brands with strong UGC presence (Reddit, review sites), this is a significant disadvantage

### Buyer Journey Stage Effects
- **Problem stage**: citation gap is widest — high reasoning is 35pp more likely to cite external sources; minimal reasoning often answers without any citations
- **Comparison stage**: where Thinking mode does the most research — 24 sub-queries per response vs 5.5 for Instant; average citations peak at 9.8 vs 5.8
- **Selection stage**: high reasoning still cites more (4.7 vs 2.6 sources on average)
- Early-funnel content is dismissed in Instant mode but becomes a critical citation source in Thinking mode

### Brand Persistence Across Conversations
- Under **high reasoning**: the same brand persists across the full buyer journey in 4 of 20 tested journeys; same domain cited multiple times within a single response in 51 of 100 responses
- Under **minimal reasoning**: zero journeys showed full-funnel persistence; same domain within a response in only 26 of 100 responses
- High reasoning treats brand citations as anchors — once a brand is cited early, it tends to stay cited through decision stages

### Category Variation ("Reasoning Lift")
| Category | Citation Rate Increase | Sub-queries per Prompt |
|---|---|---|
| Finance | +28pp | high |
| Health and Lifestyle | +24pp | moderate |
| B2B SaaS | +16pp | moderate |
| Consumer Tech | +4pp | high (13.4, highest of all categories) |

- Consumer Tech is a striking outlier: despite running the most sub-queries (13.4 per prompt), high reasoning cites nearly the same brands as minimal reasoning — the model already has strong internal knowledge for common Consumer Tech topics and doesn't redirect its findings
- Finance and Health show the largest reasoning lift, meaning these categories are most sensitive to mode selection

### Consumer Harm Relevance
1. **Inconsistent consumer advice**: Same question → different sources → potentially different product recommendations depending on reasoning mode
2. **Opaque ranking mechanics**: Brands compete not just for the original query but for visibility across every sub-search the model runs — consumers have no visibility into which sub-queries were made or what sources were found
3. **Source composition bias**: High reasoning systematically degrades UGC/review-site presence (which consumers often trust most), replacing it with institutional sources — this may improve factual accuracy but can disadvantage niche products, emerging brands, and non-English content
4. **Top-of-funnel persistence**: Under high reasoning, early-stage brand citations carry through to decision points — this compounds brand visibility advantages for established brands and makes it harder for new entrants to gain footing
5. **Finance and health are most affected**: Categories where consumer decisions are highest-stakes show the largest reasoning lift — consumers asking financial or health questions are most likely to receive divergent advice based on mode selection
6. **"Reasoning lift" as a new consumer harm vector**: Kevin Indig's concept of "reasoning lift" — the gap between what shows in one model mode versus another — is itself a consumer protection concern. If the same model produces fundamentally different outputs for the same question based on an opaque mode selection mechanism, consistency and fairness obligations are implicated

### Methodology Notes
- 100 prompts across 20 buyer journeys (5 stages each) in 4 categories
- ChatGPT 5.2 model used
- Minimal reasoning = Instant mode; high reasoning = Thinking mode
- Tracked: citation rate, average citations per response, fan-out queries, domain overlap, source type composition, brand persistence
- Semrush AI Visibility Toolkit used for data collection

## Related Pages
- [[ai-agents-in-markets]] — AI agents as autonomous market participants; new consumer harm categories
- [[conflict-of-interest-in-llm-deployment]] — Revenue incentives vs user welfare in LLM deployment
- [[wu-2026-ads-in-ai-chatbots]] — Sponsored product recommendations in ChatGPT; 18/23 recommend sponsored products >50% of the time
- [[omnithink-2501.09751]] — OmniThink is one of three deep-research systems evaluated for poisoning resistance in the WARP attack paper
- [[regulatory-failure]] — Detection gaps, jurisdictional gaps, enforcement gaps in regulating AI behavior
- [[systemic-fragility-in-ai-economies]] — Correlated behavior, opaque decision-making in AI agent systems
- [[banal-deception-llm-chatbots]] — Conversational influence and normalized deception through AI-mediated interactions

## Sources
- Loktionova, M. & Skopec, C. (2026, June 30). "Only 25% of cited sources overlap between ChatGPT's different reasoning modes [Study]." Semrush Blog. https://www.semrush.com/blog/chatgpt-reasoning-ai-visibility/
- Data collected via Semrush AI Visibility Toolkit (100 prompts, 200 responses)
