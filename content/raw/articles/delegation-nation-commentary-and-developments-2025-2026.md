---
source_url: https://alovelaceinstitute.org/publications/delegation-nation/
ingested: 2026-06-05
authors: [Harry Farmer, Julia Smakman]
institution: Ada Lovelace Institute
date: 2025-02
tags: [research, report, policy-research, digital-platforms, corporate-accountability, cross-sector]
type: summary
---

# Delegation Nation: Advanced AI Assistants and Why They Matter — Extended Research

## Paper Details

| Field | Value |
|-------|-------|
| Title | Delegation Nation: Advanced AI Assistants and Why They Matter |
| Authors | Harry Farmer, Julia Smakman |
| Institution | Ada Lovelace Institute |
| Date | February 2025 |
| Format | Policy Briefing, 30 pages |
| URL | https://www.adalovelaceinstitute.org/wp-content/uploads/pdfs/30231/delegation-nation.pdf |

## Core Thesis

The briefing argues that the shift from rule-based virtual assistants (Siri, Alexa) to foundation-model-powered **Advanced AI Assistants** represents a qualitative leap in human-AI interaction, with significant consumer harms arising from market concentration, gatekeeping power, and psychological dependency.

## Taxonomy of Advanced AI Assistants

The paper defines Advanced AI Assistants as "an AI application, powered by a foundation model, that primarily uses a natural-language interface, and that is capable of and designed to play a particular role in relation to a user."

**Three roles:**
1. **Executor** — acting directly on the world on behalf of a user (e.g., OpenAI's Operator)
2. **Adviser** — instructing a user on how to accomplish a task (e.g., DoNotPay)
3. **Interlocutor** — interacting with a user to bring about a particular mental state (e.g., Wysa)

The paper deliberately includes advisers and interlocutors in its definition, not just systems with direct agency, because these indirect forms can be nearly as impactful.

**Distinguished from:**
- **AI agents** — act autonomously in an environment; not all AI agents are Advanced AI Assistants and vice versa
- **AI assistants** — broader category, not necessarily foundation-model powered
- **Virtual assistants** — rule-based, not foundation-model powered

## Technical Architecture

Key techniques used to build Advanced AI Assistants:
- Fine tuning (RLHF/RLAIF)
- Chain-of-thought reasoning
- Context window elongation (months/years of memory)
- Caching and RAG (Retrieval Augmented Generation)
- Safety classifiers
- Tool use (browser, calculator, calendar access)
- Scaffolding software (converting model output to executable actions)

**Technical comparison:**
| Feature | Virtual Assistants | Advanced AI Assistants |
|---------|-------------------|----------------------|
| Reasoning | Rule-based, explicit | Probabilistic, inferred patterns |
| Transparency | Transparent, predictable | Opaque, unpredictable |
| Control | Formalisations of human intention | Reflections of data patterns |
| Flexibility | Brittle | Flexible |
| Versatility | Narrow | Versatile |

## Challenges Identified

### Technical challenges
- Reliability — severe consequences when malfunctioning in heavily-integrated systems
- Accuracy — bias and hallucination, harder to detect in personalised systems
- Explainability — probabilistic nature complicates understanding
- Alignment — high flexibility + broad deployment + natural language = difficult alignment
- Emergent behaviour — unpredictable patterns between interacting AI Assistants

### Non-technical, non-systemic challenges
- Psychological impact — substitution for human relationships, emotional dependency
- Practical impact — undermining incentives to learn skills
- Nefarious uses — automation of scams, dangerous information more accessible

### Non-technical, systemic challenges
- **Delegation of decision-making** — rise in decisions delegated to AI, with discretion over goal realisation
- **Digital gatekeepers** — could become the principal way most people access the internet; gatekeeping power concentrated among a small number of large firms
- **Privacy** — extended data collection for personalisation, users sharing more sensitive information
- **Distributional effects** — could exacerbate economic inequality
- **Productivity and labour displacement** — benefits may accrue predominantly to AI providers
- **Environmental cost** — resource intensive with large energy and water consumption

## Policy Implications

Key recommendations:
- Look beyond safety and performance to political and economic implications
- Consider impacts of Advanced AI Assistants that act on the world indirectly (advisers, interlocutors)
- The UK Government has expressed desire to accelerate AI deployment (citing January 2025 PM blueprint)

## Sources and Methodology

- Informed by interviews with ten external experts and desk research conducted in autumn 2024
- The Institute explicitly states it will be working on Advanced AI Assistants further
- Plans to survey gaps in legal/regulatory protections and understand informed public opinion
