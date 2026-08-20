---
title: "EU AI Act Rules for Building AI Agents — AAIF Guidance"
type: summary
created: 2026-08-19
updated: 2026-08-19
tags: [regulation, eu-ai-act, ai-agents, corporate-accountability]
sources:
  - url: https://aaif.io/blog/the-eu-ai-act-and-the-new-rules-for-building-ai-agents
    title: "The EU AI Act and the New Rules for Building AI Agents"
    date: 2026-08-02
confidence: high
sectors: [digital-platforms, regulatory-compliance]
concepts:
  - [[ai-act]]
  - [[ai-agents-in-markets]]
  - [[dark-pattern]]
---

# EU AI Act Rules for Building AI Agents — AAIF Guidance

## Paper Details

- **Source:** Agentic AI Foundation (AAIF) blog
- **Author:** Angie Jones (VP, Agentic AI Foundation; Master Inventor with 27 patents)
- **Published:** August 2, 2026
- **URL:** https://aaif.io/blog/the-eu-ai-act-and-the-new-rules-for-building-ai-agents
- **Context:** Published on the EU AI Act's transparency deadline (August 2, 2026); covers agent-specific compliance obligations

## Summary

This article provides practical guidance from the Agentic AI Foundation on how the EU AI Act's regulatory framework applies to AI agents — autonomous or semi-autonomous systems built on top of general-purpose foundation models. It clarifies that while the Act creates separate categories for general AI models and AI systems, it does not create a distinct legal category for agents themselves; instead, agents are treated as AI systems whose obligations depend on their intended use, risk level, and whether they interact with humans.

Key themes: (1) risk classification is use-dependent, not model-dependent — the same model can produce both low-risk and high-risk agents depending on what they do; (2) a company using a compliant foundation model still bears duties as agent provider or deployer; (3) transparency obligations for human-facing AI started August 2, 2026 (must disclose AI interaction); (4) high-risk systems require automatic logging, risk management, post-market monitoring, and written value-chain agreements; (5) the Digital Omnibus proposal delayed standalone high-risk rules to December 2027 but did not delay transparency requirements.

## Key Findings / Arguments

- **No separate agent category:** The AI Act does not create a distinct legal classification for AI agents. Agents are covered under the broad definition of "AI system" — systems operating with varying levels of autonomy that produce decisions affecting digital or physical environments.
- **Risk is use-dependent, not model-dependent:** Using a powerful general-purpose model does not make an agent high risk. An internal document summarizer has few duties; the same model connected to hiring records and ranking applicants may be high risk. Teams must reclassify whenever purpose, data access, tools, or affected users change.
- **Extraterritorial reach applies:** The Act applies when a system's output is used in the EU, even if the provider/deployer is based outside Europe. UK companies selling to EU customers building AI agents are within scope.
- **Prohibited uses matter:** Harmful manipulation, social scoring, and emotion recognition in workplaces/schools are prohibited. Companies must check these before any other compliance work.
- **Transparency deadline passed (Aug 2, 2026):** Providers of interactive AI systems must design them so people know they're talking to AI at the start of first interaction, unless obvious. AI agents and chatbots are named as examples. This deadline was not delayed by the Digital Omnibus.
- **Model compliance ≠ agent compliance:** OpenAI, Anthropic, Google, Microsoft, Amazon, Mistral, and Cohere signed the EU's voluntary General Purpose AI Code of Practice. But this does not absolve downstream companies — a company deploying an agent under its own name is the agent system provider with independent obligations.
- **Deployer-to-provider escalation:** A deployer becomes a provider (and faces full provider obligations) when it substantially modifies a high-risk system or changes its purpose to make it high risk.
- **Value-chain documentation required:** High-risk systems require written agreements across the supply chain specifying what information and technical support the system provider needs for compliance.
- **Record-keeping is an agent-specific challenge:** Unlike chatbots where the event is an answer, agents take actions. Evidence must show tool requests, results, active model versions, and policy versions at time of action — plus protections against later tampering.
- **Human approval requirement for high-risk actions:** Actions affecting a person's rights, money, employment, or access to services require human approval before execution.
- **Digital Omnibus schedule changes:** Standalone high-risk system rules delayed to December 2, 2027. High-risk AI in regulated products: August 2, 2028. Transparency and generative content marking rules not delayed (transparency already active as of Aug 2, 2026).

## Relevance to UK Consumer Harms

This source is directly relevant to UK consumer harms research on multiple fronts:

1. **Extraterritorial overlap with DMCCA 2024:** The EU AI Act's extraterritorial scope (applying when outputs are used in the EU) means UK companies deploying AI agents — especially those serving EU customers — must comply with both EU and UK frameworks. The Digital Markets, Competition and Consumer Act 2024 addresses misleading commercial practices; if an agent is manipulated via GEO techniques or dark patterns while appearing to give impartial advice to consumers, this could trigger obligations under both regimes simultaneously.

2. **Prohibited manipulation maps to consumer harm:** The AI Act's prohibited uses — harmful manipulation and social scoring — are directly relevant to consumer protection. If AI agents used in financial services, healthcare, or other regulated sectors apply manipulative techniques to steer consumer choices, this constitutes a form of unfair trading practice that UK regulators (CMA, FCA) would also scrutinize under DMCCA 2024 and sectoral rules.

3. **Transparency obligation as consumer right:** The August 2, 2026 transparency requirement (disclosing AI interaction at the start of first contact) parallels UK concerns about undisclosed automated decision-making. UK consumers have a right to know when they're interacting with an AI agent rather than a human — especially in regulated sectors like financial services where misrepresentation can cause material harm.

4. **Model-compliance ≠ service-compliance creates enforcement gaps:** The article's distinction between foundation model compliance and downstream agent deployment mirrors the UK's challenge of regulating deployed AI systems when the underlying models come from external providers (often US companies). If an EU company uses a compliant Anthropic or OpenAI model but deploys it as a high-risk consumer-facing agent, the model provider has done nothing wrong — yet the consumer-facing harms still occur. This is the exact enforcement gap the UK's "pro-innovation" AI approach struggles to address.

5. **Value-chain accountability gaps:** The AI Act's requirement for written value-chain agreements for high-risk systems could inform UK regulatory thinking on where accountability sits when a consumer is harmed by an AI agent built from multiple components (foundation model + middleware + custom tools). Who is liable — the model provider, the integrator, or the deployer?

6. **Connection to SafeGEO and agentic commerce:** The article's discussion of agent classification, transparency, and action logging has direct implications for consumer-facing AI agents that research products, make purchases, or recommend services on behalf of users. If an agent cannot produce verifiable records of its actions and reasoning, consumers have no way to challenge harmful decisions — a core consumer harm vector in [[agentic-commerce-research-2026]].

## Connection to Other Wiki Entries

- [[ai-act]] — EU AI Act overview; this article provides practical agent-specific guidance under the Act
- [[the-dmcca]] — UK's DMCCA 2024 overlaps with EU AI Act on manipulation and misleading practices
- [[digital-omnibus-proposal]] — the Digital Omnibus proposal that delayed high-risk AI rules to December 2027
- [[agentic-commerce-research-2026]] — consumer harms from agentic AI commerce; this article addresses accountability gaps in deployed agent systems
- [[ai-agents-in-markets]] — AI agents operating in commercial contexts
- [[dark-pattern]] — EU AI Act prohibited uses (harmful manipulation, social scoring) overlap with UK dark pattern and unfair trading concerns
- [[platform-agent-asymmetry]] — information asymmetry between platform/deployer and consumer regarding agent behavior
- [[dark-patterns-choice-architecture]] — if agents are used to deploy dark patterns on behalf of consumers, transparency and prohibition rules apply
