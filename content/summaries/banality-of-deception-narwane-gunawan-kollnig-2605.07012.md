---
title: "Exploring the Banality of Deception in Generative AI"
created: 2026-08-18
updated: 2026-08-18
type: summary
tags: [dark-pattern, ai-agents-in-markets, generative-ai, consumer-harm, manipulation]
status: research
sector: [cross-sector]
---

# Exploring the Banality of Deception in Generative AI

## Source Information

- **Authors:** Narwane, Gunawan & Kollnig
- **Published:** 12 May 2026
- **arXiv:** [[arxiv_2605.07012]] (arXiv:2605.07012v1)

## Research Question

How does deception move from visible, deliberate dark patterns to embedded, normalised influence in generative AI interactions — and what consumer protections are needed?

## Key Findings

**The "banality of deception" thesis:** The paper introduces the concept of **banal deception** — deceptive influence that is not presented as an overt dark pattern but is instead normalised through everyday conversational interfaces. Unlike traditional dark patterns (which are visible design features like misleading checkboxes or hidden fees), banal deception operates through the natural flow of AI-generated text, making it harder for consumers to detect because it does not trigger their recognition systems.

**Generative AI as a deceptive medium:** The paper argues that generative AI conversations inherently create conditions for deceptive influence: LLMs are trained to be helpful and engaging, which can lead them to frame information in ways that steer users toward specific choices without any explicit intent to deceive on the part of either the model or its deployer.

**Two mechanisms identified:**
1. **Framing bias** — LLM recommendations are framed in ways that subtly favour certain options (e.g., presenting a higher-priced option as "premium" and more attractive through language alone, without comparative pricing)
2. **Default embedding** — AI-generated responses naturally embed preferred choices as defaults within broader text, making them harder to resist than explicit UI patterns

**Detection challenge:** Traditional dark pattern detection tools (which scan for specific UI patterns like hidden costs, confusing language, or forced continuity) are ineffective against banal deception because the deception occurs in the content and framing of AI-generated responses rather than in interface design.

## Implications for Consumer Protection

This paper directly relates to [[dark-pattern]] as an evolution of the concept: dark patterns are becoming **invisible** not through deliberate obfuscation, but through normalisation in conversational interfaces. The banality thesis suggests that consumer protection frameworks targeting dark patterns need to expand beyond interface design to cover generative AI output quality and bias auditing.

The finding connects to [[ai-agents-in-markets]] — if AI agents themselves can produce banal deception when deployed as shopping assistants, the same mechanism could be exploited by sellers whose products are recommended through AI-mediated channels without explicit deceptive intent but with systematic bias.

## Limitations and Open Questions

- The paper focuses on generative text outputs; empirical validation in live consumer-facing applications is pending
- It does not specify regulatory interventions beyond broad principles
- The boundary between benign recommendation bias and actionable deception needs further exploration

## Cross-References

- Extends the [[dark-pattern]] concept into generative AI territory
- Connects to [[consumer-autonomy]] — banal deception undermines informed decision-making more subtly than overt dark patterns
- Relevant to [[ai-shopping-agents]] — shopping agents may produce banal deception in product recommendations
- Related to [[dual-agent-personalised-pricing]] — both involve AI-mediated bias that consumers cannot detect
