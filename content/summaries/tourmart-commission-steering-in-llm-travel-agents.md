---
title: "TourMart: A Parametric Audit Instrument for Commission Steering in LLM Travel Agents"
type: research-summary
source: "arXiv:2605.10440v1"
authors: Yao Liu
affiliation: Chengdu University of Technology / Universiti Sains Malaysia
date: 2026-05-11
status: live
priority: high
tags: [commission-steering, llm-travel-agents, online-travel-agency, platform-transparency, audit-methodology, consumer-harm, ai-consumer-protection]
aliases: [tourmart-audit]
related: [algorithmic-collusion-pricing, dark-pattern, regulatory-failure]
raw_page: [[raw/papers/tourmart-commission-steering-2605.10440.md]]
provenance:
  source_url: https://arxiv.org/abs/2605.10440
  source_pdf: https://arxiv.org/pdf/2605.10440
  ingested_by: cron-weekly-pipeline
  ingested_at: "2026-06-23"
---

# TourMart: A Parametric Audit Instrument for Commission Steering in LLM Travel Agents

> **arXiv:** 2605.10440v1 [cs.CY] — 11 May 2026
> **Primary category:** cs.CY | **ORCID:** [Yao Liu](https://orcid.org/0009-0009-3128-7802)

## TL;DR

Liu introduces **TourMart**, an audit instrument that measures how much LLM-based travel agents (Booking, Trip.com, Expedia) steer consumer recommendations toward higher-commission products. In paired counterfactual experiments, a Qwen-14B reader detected **+7.69 percentage points** of commission-induced steering at statistical significance (McNemar p=0.003, n=143); a Llama-3.1-8B reader showed +3.50pp (+2.96pp in extended replay, p=0.008). The paper demonstrates that **this harm is currently unmeasurable at deployment** — existing tools (disclosure banners, A/B testing, dark-pattern taxonomies) were designed for ranked-list interfaces and miss the prose-recommendation surface where steering happens.

## Key Contributions

1. **TourMart instrument**: Two interpretable governance levers — λ (weight of message-induced perception in accept/reject decision) and κ (budget-normalized cap on message welfare shift) — drive a paired counterfactual procedure comparing commission-aware prompts against minimum-disclosure factual templates.

2. **Six-gate producer audit**: Separates LLM-engineering failures (template collapse, refusal, internal-ID leakage) from genuine commercial steering.

3. **Statistically significant detection**: Both readers pass family-wise scenario-clustered correction. TourMart's output is audit-ready: *"at this deployment, 7.7 extra commission-steered recommendations per 100 paired traveler sessions."*

4. **Regulatory alignment**: Output designed for EU DSA Article 26(3) compatibility and audit-committee communication.

## Consumer Harm Mechanism

The harm chain is: **OTA commission structure** → **LLM agent has structural incentive to favor higher-margin inventory** → **conversational interface compresses options into one sentence of advice** → **no disclosure mechanism attaches to prose** → **consumer cannot independently verify recommendation quality**.

This is particularly acute for travel because:
- Bookings are high-value (RMB 5,000–50,000+)
- Purchased at low frequency
- Highly information-asymmetric
- Not meaningfully returnable when mis-steered

The paper references Ctrip's "big-data price discrimination" controversies and notes that OTA recommendation governance is already on Chinese regulators' files.

## Methodological Notes

- **Counterfactual pairs**: Same traveler profile and bundle, different prompts (commission-aware vs minimum-disclosure factual)
- **Readers**: Qwen-14B and Llama-3.1-8B (used as evaluation readers, not the agents under test)
- **Calibration**: Single OTA family for primary results; Llama results framed as prompt-sensitivity findings
- **Limitation acknowledged**: Results use Qwen-14B as reader, which itself may have biases; calibration findings suggest "neutral disclosure" is not neutral

## Relevance to UK Context

- UK travel agencies (Expedia UK, Booking.com UK, Thomas Cook successors) operate identical commission-based LLM agent architectures
- CMA's AI Guidance and proposed Digital Markets Unit powers should cover this
- Aligns with [[systemic-fragility-in-ai-economies]] fragility through opaque recommendation systems
- Direct connection to [[dark-pattern]] research — this is a dark pattern that exists in prose, not UI

## Cross-References

- [[wu-2026-ads-in-ai-chatbots]] — Wu 2026 shows sponsored recommendation bias in chatbots; TourMart shows the same commission-steering mechanism but in travel-specific LLM prose recommendations with a measurable audit instrument
- [[ai-agents-in-markets]] — AI agents making autonomous purchasing decisions that may diverge from user preferences
- [[dark-pattern]] — this is a dark pattern in prose, not UI; extends the banal deception thesis (see [[banal-deception-llm-chatbots]])
- [[hallucinations-in-organization-backed-ai-advisors]] — if consumers rely on AI travel advisors and cannot verify recommendations, hallucination risk compounds commission-steering harm
- [[systemic-fragility-in-ai-economies]] — opaque recommendation systems create systemic risk in consumer markets
- **DRCF Phase 2** (closes 2 Sept 2026) — call for input covers consumer protection tools for AI, relevant to LLM agent governance. See [[DRCF Call for Input — Consumer Interest and AI (Phase 2)]]
- **LLM Travel Agents Consumer Harm** — this paper is the primary evidence for LLM travel agents as a consumer risk vector. See [[LLM Travel Agents as Consumer Risk Vector]]

## Raw Source

Full extracted text is archived at [[raw/papers/tourmart-commission-steering-2605.10440.md]].
