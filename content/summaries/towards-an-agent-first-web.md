---
title: "Towards an Agent-First Web: Redesigning the Web for AI Agents"
type: research-summary
source: "arXiv:2606.19116v1"
authors: Eranga Bandara, Ross Gore, Ravi Mukkamala, et al. (20 authors)
affiliation: Multi-institutional (Sri Lanka, Australia, India, etc.)
date: 2026-06-17
status: live
priority: medium-lower
tags: [agent-first-web, web-architecture, ai-agents, web-protocols, machine-readable-content, web-modernization]
aliases: [agent-first-web]
related: [agentic-web-requires-new-normative-infrastructure, ai-agents-in-markets]
raw_page: [[raw/papers/agent-first-web-redesign-2606.19116.md]]
provenance:
  source_url: https://arxiv.org/abs/2606.19116
  source_pdf: https://arxiv.org/pdf/2606.19116
  ingested_by: cron-weekly-pipeline
  ingested_at: "2026-06-23"
---

# Towards an Agent-First Web: Redesigning the Web for AI Agents

> **arXiv:** 2606.19116v1 [cs.AI, cs.CY] — 17 June 2026
> **Authors:** Eranga Bandara, Ross Gore, Ravi Mukkamala, Asanga Gunaratna, Safdar H. Bouk, Xueping Liang, Peter Foytik, Abdul Rahman, Sachini Rajapakse, Isurunima Kularathna, Pramoda Karunarathna, Chalani Rajapakse, Ng Wee Keong, Kasun De Zoysa, Tharaka Hewa, Amin Hass, Wathsala Herath, Aruna Withanage, Nilaan Loganathan, Atmaram Yarlagadda, Sachin Shetty (20 authors)

## TL;DR

The World Wide Web was built for a **human primary consumer** over three decades — its access model, economics, and content all target human perception. AI agents as intermediaries between humans and web content **invalidate this assumption**, yet the web resists agents through blanket blocking, CAPTCHA-based exclusion, and economic models that treat agent traffic as unwanted. This paper proposes an **agent-first web architecture** that redesigns web protocols, content formats, and access models to natively support AI agents as first-class consumers.

## Key Arguments

1. **Web architecture is human-centric**: The web's 30-year legacy assumes human visitors. Every layer — access model, economics, content presentation — targets human perception.

2. **The web resists agents**: Platforms employ blanket blocking, CAPTCHA-based exclusion, and economic models that penalize agent traffic. This creates an adversarial relationship.

3. **Agent-first is different from agent-friendly**: The paper argues for fundamental redesign, not just adding agent-friendly headers or APIs. Agents need their own protocols and content formats.

4. **Economic model needs revision**: The current attention-based web economy (ad revenue, click-through) doesn't translate to agent-mediated browsing where agents consume content on behalf of users.

## Proposed Architecture

The paper outlines several design principles for an agent-first web:

- **Machine-readable content formats**: Standardized formats for structured information that agents can process without HTML parsing and scraping
- **Agent authentication and delegation protocols**: Clear standards for agents to identify themselves and prove they act with user authorization
- **Agent-appropriate pricing models**: Economic models that value agent-mediated traffic rather than treating it as a cost
- **Content metadata for agents**: Rich metadata that agents can use to make informed decisions about content relevance and quality

## Consumer Harm Implications

This paper is primarily about enabling beneficial agent capabilities rather than identifying harms, but several consumer protection angles exist:

- **Access equity**: Without agent-first redesign, only well-resourced platforms can support agents, creating a two-tier system where consumer agency is limited by platform generosity
- **Data extraction**: Current agent access models often require platforms to expose APIs that may extract consumer data
- **Interoperability**: An agent-first web could improve consumer choice by making it easier to compare across platforms (if platforms cooperate)
- **Platform gatekeeping**: Platforms that resist agent access effectively gatekeep consumer choice between human-mediated and agent-mediated interactions

## Connection to Related Research

- Complements [[the-agentic-web-requires-new-normative-infrastructure]] (which focuses on policy/normative dimensions) with technical architecture proposals
- Both papers agree the current state is unsustainable and requires fundamental change
- The [[the-agentic-web-requires-new-normative-infrastructure]] normative triad (delegation, transparency, proportional restriction) could inform agent-first protocol design

## Relevance to UK Context

- UK web accessibility and digital infrastructure policy should consider agent-first principles
- CMA's Digital Markets Unit may want to mandate agent access for designated straddle platforms
- Relevant to UK open data and government digital services policy
- The paper's technical proposals could inform UK participation in international web standards bodies

## Limitations

- This is a **position/proposal paper** with a large author group — the technical proposals are broad rather than detailed
- No implementation or empirical validation of proposed architecture
- The paper doesn't address specific consumer harm scenarios or harm quantification
- 20 authors suggest this is a community vision document rather than a focused research contribution

## Future Work Needed

- Implementation prototypes of agent-first protocols
- Empirical studies comparing human-vs-agent access experiences
- Economic modeling of agent-first web revenue models
- Security analysis of agent authentication and delegation mechanisms

## Raw Source

Full extracted text is archived at [[raw/papers/agent-first-web-redesign-2606.19116.md]].
