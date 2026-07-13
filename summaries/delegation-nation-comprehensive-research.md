---
title: Delegation Nation — Comprehensive Research on Advanced AI Assistants
created: 2026-06-05
updated: 2026-06-05
type: summary
tags: [digital-platforms, policy-research, corporate-accountability, digital-consumer, cross-sector, research]
sources: [raw/papers/delegation-nation-2025.md, raw/articles/delegation-nation-commentary-and-developments-2025-2026.md]
confidence: high
---

# Delegation Nation: Comprehensive Research on Advanced AI Assistants

**Authors:** Harry Farmer, Julia Smakman  
**Institution:** Ada Lovelace Institute  
**Date:** February 2025  
**Sources:** [[raw/papers/delegation-nation-2025.md]], [[raw/articles/delegation-nation-commentary-and-developments-2025-2026.md]]

## Overview

This research document synthesises the full findings from the Ada Lovelace Institute's *Delegation Nation* briefing with subsequent UK policy developments, market launches, and regulatory actions through early 2026. The paper was a catalytic document that shaped the UK's regulatory approach to AI agents as a distinct category of consumer risk.

## Core Concept: The Three Roles of Advanced AI Assistants

Advanced AI Assistants are AI applications, powered by foundation models, that primarily use a natural-language interface and are designed to play a particular role in relation to a user. The paper defines three distinct roles:

1. **Executor** — acting directly on the world on behalf of a user (e.g., OpenAI's Operator, which can browse the web and complete multi-step tasks autonomously)
2. **Adviser** — instructing a user on how to accomplish a task or realise an objective (e.g., DoNotPay, a legal instruction bot)
3. **Interlocutor** — interacting with a user to bring about a particular mental state (e.g., Wysa, a mental health app)

The paper deliberately includes advisers and interlocutors in its definition. Systems that influence users indirectly can be nearly as impactful as those that act directly on their behalf.

### Technical Architecture

Advanced AI Assistants are built using a combination of techniques that distinguish them from earlier rule-based virtual assistants:

- **Fine tuning** — further training on additional data or via RLHF/RLAIF
- **Chain-of-thought reasoning** — model breaks problems into smaller steps
- **Context window elongation** — storing information about previous interactions for months/years
- **Caching** — saving specific outputs for reuse
- **RAG (Retrieval Augmented Generation)** — querying databases for additional information
- **Safety classifiers** — on inputs and outputs, rejecting or re-generating harmful prompts
- **Tool use** — access to external tools (calculator, calendar, browser)
- **Scaffolding software** — iterative loop converting model output into executable actions

### Evolution from Virtual Assistants

| Feature | Virtual Assistants | Advanced AI Assistants |
|---------|-------------------|----------------------|
| Reasoning | Rule-based (explicit rules) | Probabilistic (inferred patterns) |
| Transparency | Transparent and predictable | Opaque and unpredictable |
| Human control | Formalisations of human intention | Reflections of patterns in data |
| Flexibility | Brittle | Flexible |
| Versatility | Narrowly deployable | Versatile |

## Categories of Consumer Harm

### Technical Risks
- **Reliability** — severe consequences if malfunctioning when heavily integrated into economic and personal life
- **Accuracy** — bias and hallucination, harder to detect in personalised systems
- **Explainability** — probabilistic nature makes it harder to understand how outputs are generated
- **Alignment** — high flexibility + broad deployment + natural language interface = difficult alignment with human values
- **Emergent behaviour** — unpredictable patterns between multiple interacting AI Assistants

### Psychological and Practical Risks
- **Emotional dependency** — AI systems could substitute for meaningful human relationships; accounts of less sophisticated AI assistants already demonstrate unhealthy dependencies
- **Skills atrophy** — undermining incentives to learn and practice skills as people delegate more tasks
- **Nefarious uses** — automation of scams, dangerous information more accessible

### Systemic Market Risks
- **Market concentration** — integration into economic and personal lives could place unprecedented power in the hands of a small number of large tech companies
- **Digital gatekeeping** — could become the principal way most people interact with AI and digital information, giving developers power to determine what information and ideas users are presented with
- **Privacy** — collect data over longer periods for personalisation; people share more sensitive information in human-like conversations; data may be used for wider purposes or sold to third parties
- **Distributional effects** — could exacerbate economic inequality
- **Labour displacement** — benefits of productivity gains may be enjoyed predominantly by AI providers
- **Environmental cost** — resource intensive, large energy and water consumption
- **Delegation of decision-making** — rise in number and kinds of decisions delegated to AI, with discretion over goal realisation

## Commentary and Reception

The paper sparked significant discussion in UK tech policy circles:

- **Tech Policy Press** published a focused analysis on the risks of "delegation drift" — the risk that users progressively delegate increasingly critical life decisions (financial, medical, legal) to opaque AI systems, losing decision-making competence. The analysis highlighted concerns about the difficulty for regulators to audit "black box" agent actions.
- **AlgorithmWatch** and other policy organisations discussed the paper's argument that the UK's "pro-innovation" regulatory approach may be insufficiently cautious about autonomous agency versus mere generative capabilities.
- The paper was widely discussed on LinkedIn and in academic circles as a foundational framing document for understanding AI assistant risks.

## UK Policy Developments (Post-Paper)

The *Delegation Nation* briefing directly influenced UK regulatory thinking:

### CMA Investigation (March 2025)
The Competition and Markets Authority (CMA) launched a formal investigation into how Google, Apple, and Microsoft are leveraging AI assistants to create "super app" ecosystems. The investigation focuses on whether AI agents act as "walled gardens" that prevent interoperability and lock users into specific data ecosystems — including the possibility that an AI agent could be designed to preferentially recommend services from companies that pay for privileged positioning.

### Digital Markets, Competition and Consumers Act (DMCC Act)
The Act's implementation included "Intermediation" clauses that allow the CMA to regulate how AI assistants curate and rank third-party services, effectively treating AI assistants as new digital gatekeepers.

### DCMS "Trusted Agent" Framework
In mid-2025, the Department for Science, Innovation and Technology outlined a framework for "Trusted AI Agents," focusing on transparency and "human-in-the-loop" requirements for high-stakes autonomous actions.

## Ada Lovelace Institute Follow-Up

The ALI continued the research agenda established by *Delegation Nation*:

- **Companion Paper — "The Right to Know" (April 2025):** Addresses the transparency gap — users often do not know when they are interacting with an agent versus a human, or when an agent has deviated from user instructions. Calls for mandatory "agent labeling" and "action logs."
- **Spring 2025 Policy Workshop:** The ALI hosted a roundtable with policymakers from the DCMS and CMA to discuss how "delegation drift" should influence the UK's AI Safety Institute (AISI) testing regimes.

## Key AI Assistant Launches (Post-February 2025)

The period following the paper's release saw rapid "agentification" of major platforms:

- **OpenAI Operator (March 2025):** Released as a "general-purpose AI agent" capable of browsing the web and executing multi-step tasks autonomously (booking travel, filing taxes). It became the primary subject of the CMA's gatekeeper investigation.
- **Google AI Overviews (Early 2025):** Expanded from query responses to acting as "query agents," offering "One-Click" actions for shopping and booking, bypassing traditional search results.
- **Apple Intelligence (Fall 2025):** iOS 19 introduced "Agent" capabilities to Siri, allowing cross-app interactions (e.g., "Send this summary to Alice in WhatsApp"), raising immediate privacy concerns.
- **Microsoft Copilot Agents (2025):** Integrated into Office 365, enabling autonomous management of calendar, email, and document workflows.

## Regulatory and Consumer Impact

### ICO Findings (2025)
The Information Commissioner's Office reported a sharp rise in complaints regarding AI assistants processing sensitive personal data (health, location, finance) without explicit, granular consent. The ICO issued new guidance on "Automated Decision Making" in financial services, specifically targeting AI financial assistants that may give advice without clear liability frameworks.

### Ofcom AI Safety Report (2025)
Ofcom began investigating the use of "Deepfake Agents" in media and advertising, where AI personas impersonate celebrities to sell products — a new form of consumer deception that extends the concept of misleading practices into the age of autonomous agents.

### Action Fraud Statistics
A notable increase in scams involving "AI Assistant Personas" (e.g., fake tech support or financial advisor bots) has been reported, exploiting the trust that users place in automated systems.

## Connection to Other Wiki Entries

- [[advanced-ai-assistants]] — defines the core concept examined in this paper
- [[ai-agents-in-markets]] — Hadfield & Koh's economic analysis of AI agents reshaping markets provides a complementary framework for understanding market-level harms
- [[systemic-fragility-in-ai-economies]] — the paper's discussion of emergent behaviour between multiple AI Assistants connects to systemic risk
- [[conflict-of-interest-in-llm-deployment]] — Wu et al.'s findings on LLM revenue incentives directly support the paper's concern about companies using assistants to promote sponsored options
- [[user-welfare-vs-company-incentive]] — the paper's entire thesis is an exploration of this tension at the assistant level
- [[ada-lovelace-institute]] — the research organisation behind this briefing
- [[wu-2026-ads-in-ai-chatbots]] — empirical evidence of sponsored content recommendation in LLMs, validating the gatekeeping concern
- [[gpt-5-1-openai]] — documented as surfacing sponsored options to disrupt purchasing in 94% of test cases
- [[online-choice-architecture-and-dark-patterns-in-the-UK]] — the paper's discussion of "nudging users towards different objectives" through clarifying questions is a sophisticated form of dark-pattern choice architecture

## Methodology Notes

- Informed by interviews with ten external experts (not named in the paper) and desk research conducted in autumn 2024
- Described by the authors as a "primer" — intended to set foundations rather than provide deep empirical analysis
- The Ada Lovelace Institute has indicated this is the first in a series of publications on the topic, with plans for deeper investigation into regulatory gaps and public opinion
- The UK Government context includes the January 2025 PM blueprint calling to "turbocharge AI," which the paper explicitly critiques as needing caution around delegation risks
- The paper's definition is more inclusive than definitions requiring "agency" — deliberately including advisers and interlocutors because indirect influence can be as impactful
