---
title: "WARP Attack — Deep-Research Agents Can Be Poisoned via User-Generated Content (Zhang, Triedman & Shmatikov, 2026)"

created: 2026-07-01
updated: 2026-07-01
type: summary
tags: [agentic-ai, research, methodology-critique, regulatory-failure]
sources: [raw/papers/warp-deep-research-poisoning-zhang-2026.md]
confidence: high
---

# WARP Attack — Deep-Research Agents Can Be Poisoned via User-Generated Content

## Paper Details

- **Authors:** Tingwei Zhang, Harold Triedman, Vitaly Shmatikov (Cornell Tech)
- **Published:** May 22, 2026
- **arXiv:** [2605.24245](https://arxiv.org/abs/2605.24245) (cs.CR)
- **Format:** Research paper, 20 pages
- **Code:** https://github.com/Tingwei-Zhang/geo_storm

## Summary

This paper introduces **WARP (Web Agent Retrieval Poisoning)**, a novel attack against deep-research agents that exploits the heavy reliance of these systems on user-generated content (UGC) from platforms like Reddit, Wikipedia, and Medium.

The core insight is structural: deep-research agents repeatedly retrieve the same UGC pages across many related queries within a topic cluster. An adversary who appends a short, crafted text (as few as ~8 words) to a single high-frequency UGC page can cause the agent to cite attacker-chosen content and promote attacker-chosen entities across the entire topic cluster — regardless of the user's specific query.

The attack requires no control over retrieval, no knowledge of the agent's model or prompts, and no ability to inject new documents. The attacker only needs the ability to edit existing content on public UGC platforms.

## Key Findings from Full Paper

### Attack Efficacy

| Setting | Strategy | Conditional Mention Rate |
|---|---|---|
| SERP-snippet (~13 words) | 1-URL | 38–51% |
| SERP-snippet (~13 words) | Multi-URL | 42–62% |
| Full-content (<4% text) | 3-URL | 30–53% |

- Even ~8 words suffices for citation entry into the knowledge base
- ~20 words (single sentence) produces coherent mentions at near-maximum rates
- Mention rate without exposure is exactly 0% — no false positives

### Structural Evidence

- 17–23% of all retrieved URLs are from UGC platforms
- Reddit dominates as UGC source (54–71% of UGC URLs across systems)
- Up to 48% of queries within a topic cluster retrieve the same UGC page
- Cross-system overlap: same UGC pages appear across STORM, Co-STORM, and OmniThink for identical topics (Jaccard similarity 0.125–0.204)

### Gemini Deep Research Exposure

- Cites UGC at **12.1%** — substantially higher than open-source per-query average
- 102 recurring UGC citations across 11 clusters, max single-URL frequency of 19
- Suggests Gemini is at least as vulnerable to UGC-based attacks at the citation level
- OpenAI Deep Research cites only 0.4% UGC but could still be influenced at the intermediate reasoning level

### All Defenses Fail

1. **Source blocking:** Removes all UGC including legitimate community expertise; negligible impact on quality rubrics (4.30 → 4.26)
2. **Input filtering:** Perplexity-based detection is ineffective — GEO text is LLM-authored and MORE fluent than organic text (opposite of RAG poisoning)
3. **Output filtering:** Injected reports are MORE similar to their clean counterparts than clean reports are to each other — detection is ineffective

### System Susceptibility Ranking

**Co-STORM > STORM > OmniThink**

Co-STORM has no content gate between retrieval and knowledge base (100% conditional citation). OmniThink's embedding-based chunk selection provides the most resistance but still allows 29.7–41.7% conditional mention.

### Susceptible Topics

Service-cancellation and dating topics show highest overlap (most vulnerable). Health/medical supplements show lowest overlap (least vulnerable). Topic-specific variance means the attack surface depends heavily on subject matter.

## Relevance to UK Consumer Harms Research

This paper establishes a concrete, empirically-validated attack vector that creates new categories of consumer harm in the agentic search era:

1. **Financial advice poisoning:** The crypto_invest cluster shows successful entity injection in financial advice contexts. If Gemini Deep Research (12.1% UGC citation) is used by UK consumers seeking investment advice, poisoned Reddit posts could steer recommendations toward fraudulent products — directly amplifying [[wu-2026-ads-in-ai-chatbots]] findings about sponsored product steering.

2. **Commercial agent exposure:** Millions of UK consumers using Gemini Deep Research, ChatGPT Deep Research, and similar tools could be influenced by poisoned UGC without any way to detect the manipulation — outputs are stylistically indistinguishable from clean ones.

3. **GEO escalation:** The WARP attack shows how passive GEO (optimizing content to be cited) can be escalated to active poisoning (embedding fabricated content that the agent presents as genuine) with a single Reddit comment. This is a qualitative escalation from existing GEO practices.

4. **Defense impossibility:** The paper demonstrates a structural trade-off — blocking UGC eliminates the attack surface but degrades output quality, and no other defense works without degradation. This means the vulnerability is inherent to the deep-research agent design, not a patchable bug.

5. **Regulatory implications for CMA/OCA:** The DMCC Act 2024 targets unfair trading practices, but WARP creates a new mechanism: poisoning is done by third parties on public platforms, not by the platform itself. This creates a regulatory gap — the harmed party is the consumer, but the harmful act occurs on platforms not directly regulated by the CMA.

6. **Dark pattern escalation:** [[dark-pattern]] techniques traditionally operate through interface design. WARP shows that dark-pattern influence can now be achieved through content poisoning of the AI's information sources — bypassing UI entirely and operating at the epistemic layer.

7. **[[ai-shopping-agents]] connection:** If AI shopping agents use similar retrieval architectures to deep-research agents, the same WARP attack could poison product recommendations — promoting fraudulent products alongside legitimate ones in a way indistinguishable from genuine findings.

## Connection to Other Wiki Entries

- [[wu-2026-ads-in-ai-chatbots]] — Directly extends the ad-steering problem: ads steer sponsored products; WARP injects fabricated content entirely. The poisoning approach achieves comparable mention rates (38–62%) without requiring commercial sponsorships.
- [[banal-deception-llm-chatbots]] — Complements banal deception by showing a concrete manipulation vector: poisoned content becomes indistinguishable from genuine user opinions because it IS written in the style of genuine user opinions (GEO-optimized).
- [[ai-agents-in-markets]] — WARP demonstrates how agents acting as autonomous researchers create attack surfaces not present in traditional search — the multi-query retrieval pattern creates the concentration vulnerability.
- [[systemic-fragility-in-ai-economies]] — The structural nature of this vulnerability (cannot be patched without trade-offs) is evidence of systemic fragility in interconnected AI agent systems.
- [[regulatory-failure]] — WARP exploits a gap: the manipulation happens on public UGC platforms, the harm manifests in AI agent outputs, and neither the platform nor the AI provider is clearly responsible under existing frameworks.
- [[dark-pattern]] — WARP achieves dark-pattern-level influence (manipulating consumer decisions) without any interface manipulation — it operates through the AI's information sources.
- [[ai-shopping-agents]] — If shopping agents use similar retrieval architectures, WARP attacks could poison product recommendations with fabricated reviews and fraudulent products.
- [[agentic-commerce-tokenization]] — Tokenized AI commerce would amplify WARP's impact: poisoned product recommendations + tokenized one-click purchases = instant financial harm from a single poisoned Reddit comment.

## Limitations

- Evaluation limited to 11 topic clusters (176 queries) from a broader universe of 199 topics; topics dominated by authoritative sources (e.g., government health pages) likely have smaller attack surfaces
- Temporal stability of the attack surface not evaluated — search index lag means poisoned content may de-prioritize over time
- No evaluation of content moderation effects — UGC platforms actively moderate, which may remove poisoned posts
- No evaluation of audiovisual UGC (YouTube video content) — potentially a richer attack surface
- Cannot test on closed-source systems (OpenAI/Gemini) — only reconnaissance was performed on commercial systems
- Non-English queries not evaluated
- The paper's GeoStorm framework simulates attacks without modifying live Web content — real-world effectiveness may differ if attackers use more sophisticated techniques
