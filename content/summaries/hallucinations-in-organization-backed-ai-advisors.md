---
title: "Hallucinations in Organization-backed AI advisors: Evidence about Skepticism, Verification, and Reliance"
type: research-summary
source: "arXiv:2606.23491v1"
authors: Simon J. Blanchard, Aaron M. Garvey, Laura O'Laughlin
affiliation: Georgetown, U. Tennessee, Analysis Group
date: 2026-06-22
status: live
priority: medium-high
tags: [hallucinations, ai-advisors, skepticism, verification, reliance, consumer-deception, organization-backed-ai]
aliases: [hallucinations-advisors]
related: [regulatory-failure, dark-pattern, banal-deception-llm-chatbots]
raw_page: [[raw/papers/hallucinations-ai-advisors-blanchard-2026.md]]
provenance:
  source_url: https://arxiv.org/abs/2606.23491
  source_pdf: https://arxiv.org/pdf/2606.23491
  ingested_by: cron-weekly-pipeline
  ingested_at: "2026-06-23"
---

# Hallucinations in Organization-backed AI advisors: Evidence about Skepticism, Verification, and Reliance

> **arXiv:** 2606.23491v1 [cs.HC, cs.CY] — 22 June 2026
> **Authors:** Simon J. Blanchard (Georgetown), Aaron M. Garvey (U. Tennessee), Laura O'Laughlin (Analysis Group)

## TL;DR

This review distinguishes three constructs that existing studies often conflate in organization-backed AI advisor interactions: **(1) skepticism** (recognizing that a response may require verification), **(2) verification** (the act of checking accuracy against other sources), and **(3) reliance** (whether the response affects the user's decision). Nearly all existing studies measure reliance, while skepticism and verification are more often targeted by interventions than measured directly. General and specific warnings about hallucination risk show the **weakest and most mixed effects** of any interventions reviewed.

## Conceptual Framework

The paper defines three distinct constructs:

| Construct | Definition | Distinct From |
|-----------|-----------|---------------|
| **Skepticism** | Recognizing that a response may be inaccurate or require verification | Verification — users can be skeptical without checking |
| **Verification** | The act of checking accuracy against other sources | Reliance — verification may or may not change reliance |
| **Reliance** | Whether the response affects the user's decision | Skepticism — users can rely on unverified responses |

Skepticism arises through two pathways:
- **Output-based**: Implausibility, inconsistency, conflict with prior knowledge
- **Category-based**: Knowledge that certain content types (numerical claims, policy provisions, medical guidance, citations) are more error-prone

## Key Findings

1. **Cognitive surrender**: Consistent use of GenAI for task completion may lead users to delegate metacognitive oversight to the system — users stop questioning AI outputs

2. **Weak intervention effects**: General warnings ("this AI may hallucinate") and specific warnings ("numerical claims may be inaccurate") show the weakest effects of any AI output interventions reviewed

3. **Most studies measure reliance, not skepticism/verification**: The literature overwhelmingly focuses on whether users accept AI responses, not whether they recognize the need to check

4. **Content category matters (but unstudied)**: Existing literature posits users scrutinize certain content categories more, but no study has varied content category — this is an open research question

5. **Task completion vs. accuracy evaluation**: Users of AI advisors are typically trying to complete a task rather than explicitly evaluate accuracy — this changes the verification incentive structure

## Consumer Harm Implications

- **Organization-backed AI advisors** (service chatbots, medical assistants, employer knowledge tools) present heightened risk because users reasonably treat the system as providing information **on the organization's behalf**
- **Cognitive surrender** creates a persistent reliance pattern that is resistant to simple warning interventions
- **Task-completion context** means users will not spontaneously detect hallucinations — they're trying to complete a booking, find a policy, or get medical guidance, not fact-check the AI
- **Weak detection cues**: Source citations and other AI output interventions are the most common but least effective at prompting scrutiny

This paper is a **systematic review of existing evidence** rather than a new empirical study — it synthesizes patterns across product search, medical decision-making, content generation, and chatbot-assisted task studies.

## Relevance to UK Context

- UK organizations increasingly deploy AI advisors for customer service, health guidance (NHS), and consumer information
- CMA's AI Guidance should address hallucination risks in organization-backed systems
- Relevant to UK Consumer Protection from Unfair Trading Regulations 2008 (misleading omissions)
- Connects to [[regulatory-failure]] (regulatory frameworks haven't caught up with organization-backed AI)
- Links to [[banal-deception-llm-chatbots]] (banal deception through AI outputs presented as organizational information)

## Raw Source

Full extracted text is archived at [[raw/papers/hallucinations-ai-advisors-blanchard-2026.md]].
