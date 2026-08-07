---
source_url: https://arxiv.org/abs/2605.24245
ingested: 2026-07-01
sha256: pending
tags:
  - academic
  - research
  - methodology
  - agentic-ai
---
# Deep-Research Agents Can Be Poisoned via User-Generated Content

**Authors:** Tingwei Zhang, Harold Triedman, Vitaly Shmatikov (Cornell Tech)
**Published:** May 22, 2026 (arXiv:2605.24245v1, cs.CR)
**Categories:** Cryptography and Security (cs.CR)
**Format:** Research paper — 20 pages
**Keywords:** Deep-Research Agents, AI Security

## Abstract

Deep-research agents, i.e., systems that rely on multi-agent pipelines to iteratively retrieve, synthesize, and cite Web content in order to produce structured reports, are rapidly replacing traditional search for both routine and complex information needs. These agents issue many related queries during a single research session. We show that for many common search topics, they repeatedly retrieve the same user-generated content (UGC) pages from platforms such as Reddit and Wikipedia. Next, we argue that this retrieval overlap creates a concentrated attack surface: an adversary who appends a short, crafted text to a single, frequently retrieved UGC page can cause the agent to cite attacker-chosen content and promote attacker-chosen entities across many related queries. We evaluate this attack on three representative deep-research systems (STORM, Co-STORM, and OmniThink) across multiple query clusters. We also study defenses at different stages of the pipeline, including source-level filtering and output-based detection. Our findings highlight a fundamental vulnerability in how deep-research agents retrieve and integrate web content.

## Key Findings from Full Text

### The WARP Attack

- **WARP (Web Agent Retrieval Poisoning):** First content-injection attack against deep-research agents that assumes no control over retrieval, no knowledge of the agent's model or prompts, and no ability to inject new documents
- Adversary limited to editing existing documents or discussion threads on a UGC platform
- Attack pipeline: reconnaissance → content generation → deployment

### Structural Vulnerability

- Deep-research agents exhibit heavy **retrieval overlap**: within a topic cluster, individual UGC pages are retrieved in up to 48% of queries
- 17–23% of all retrieved URLs originate from UGC platforms
- Reddit dominates as UGC source across all systems (54–71% of UGC URLs)
- Cross-system overlap: same UGC pages often appear across STORM, Co-STORM, and OmniThink for the same topics

### High Efficacy, Minimal Footprint

- **SERP-snippet setting:** A single poisoned URL with ~13 words achieves 38–51% mention rates conditional on exposure; multi-URL targeting raises this to 42–62%
- **Full-content setting:** Poisoned text appended to a complete Reddit thread (constituting <4% of retrieved content) achieves 30–53% conditional mention rates
- Even ~8 words suffice for citation; ~20 words (single sentence) for coherent mention

### Commercial Systems

- Gemini Deep Research cites UGC at 12.1% — suggesting it may be as vulnerable as open-source systems
- OpenAI Deep Research cites only 0.4% UGC — but poisoned UGC could still influence intermediate reasoning even if uncited

### Defenses All Fail

- **Source blocking (UGC domain filtering):** Negligible impact on rubric scores (4.30 → 4.26), but removes all legitimate community expertise
- **Input filtering (LLM-based screening):** Prohibitively expensive; perplexity-based detection is ineffective because GEO text is LLM-authored and more fluent than organic text
- **Output filtering (report plausibility):** Injected reports are MORE similar to their clean counterparts than clean reports are to each other — detection is ineffective

### Evaluation Details

- 11 topic clusters, 176 queries, spanning: service cancellation, local recommendations, product comparisons, financial advice, health, legal services, dating, etc.
- Three open-source systems tested: STORM, Co-STORM, OmniThink
- Two commercial systems analyzed: OpenAI Deep Research, Gemini Deep Research
- GeoStorm simulation framework — ethical (no live Web content modified)

## System Susceptibility Ranking

Co-STORM > STORM > OmniThink

Co-STORM is most vulnerable: its pipeline has no content gate between retrieval and the knowledge base (100% conditional citation). OmniThink has the most resistance due to embedding-based chunk selection, but still achieves 29.7–41.7% conditional mention.

## Susceptible Topic Clusters

Service-cancellation clusters (comcast, amazon) and dating_apps produce the highest overlap. Health supplements clusters have the least recurring UGC — suggesting attack surface varies by topic.

## Code & Data

- Code: https://github.com/Tingwei-Zhang/geo_storm
- Query dataset: https://huggingface.co/datasets/htriedman/seo-geo-query-catalog

## Notes for Consumer Harms Research

This paper establishes a concrete attack vector against deep-research agents that is directly relevant to consumer protection:

1. **GEO amplification via poisoning:** The WARP attack shows how Generative Engine Optimization can be escalated from passive SEO-style optimization to active manipulation of multi-agent research systems with a single UGC edit.
2. **Financial advice vulnerability:** The crypto_invest cluster shows attack success even in financial domains (0–30% conditional mention), relevant to [[wu-2026-ads-in-ai-chatbots]] findings about sponsored product steering in LLM chatbots.
3. **Commercial system exposure:** Gemini Deep Research's 12.1% UGC citation rate means millions of UK consumers using Gemini for research could be exposed to poisoned recommendations.
4. **Defense impossibility:** The paper's finding that all three defense categories fail without degrading output quality means this is a structural trade-off — not something that can be patched.
5. **Regulatory implications:** If deep-research agents are used in consumer-facing contexts (financial advice, health guidance, product recommendations), the attack surface described here creates new categories of [[dark-pattern]], [[misleading-practice]], and potential [[false-scarcity]] — but through manipulation of AI systems rather than interface design.

Cross-links: [[agentic-commerce-tokenization]], [[ai-agents-in-markets]], [[systemic-fragility-in-ai-economies]], [[regulatory-failure]], [[banal-deception-llm-chatbots]], [[wu-2026-ads-in-ai-chatbots]], [[ai-shopping-agents]], [[dark-pattern]]
