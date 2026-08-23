---
title: "Agentic Web: Weaving the Next Web with AI Agents"
type: summary
source_url: https://arxiv.org/abs/2507.21206
authors: [Yingxuan Yang, Mulei Ma, Yuxuan Huang, Huacan Chai, Chenyu Gong, Haoran Geng, Yuanjian Zhou, Ying Wen, Meng Fang, Muhao Chen, Shangding Gu, Ming Jin, Costas Spanos, Yang Yang, Pieter Abbeel, Dawn Song, Weinan Zhang, Jun Wang]
date: 2025-07-28
subjects: [cs.AI, cs.LG]
authors_affiliations: [Shanghai Jiao Tong University, HKUST Guangzhou, University of Liverpool, UC Berkeley, Shanghai Innovation Institute, UC Davis, Virginia Tech, UCL]
tags: [agentic-web, web-architecture, ai-agents, agent-communication, trust-security, platform-design]
---

# Agentic Web: Weaving the Next Web with AI Agents

arXiv:2507.21206 (cs.AI / cs.LG), 28 July 2025 | Yang et al. | Multi-institutional collaboration across Shanghai Jiao Tong University, UC Berkeley, UCL and others

## Summary

Presents a systematic framework for understanding and designing the **Agentic Web** — a new paradigm where AI agents become primary entities on the Web that actively search, negotiate, transact, and collaborate online. This is a foundational infrastructure paper describing the architectural layers required before agentic commerce can function at scale.

## Four-Layer Agentic Web Architecture

1. **Agent Infrastructure Layer** — foundational networking and routing; how agents discover each other and establish communication channels
2. **Semantics & Standards Layer** — shared ontologies, communication protocols, and data representations that enable cross-system interoperability
3. **Capability & Service Interfaces Layer** — API standards for exposing agent capabilities to other agents and consumers
4. **Intelligence & Autonomy Layer** — reasoning, planning, learning systems that determine agent sophistication

## Key Technical Challenges Identified

- **Agent-to-agent communication protocols:** How agents negotiate, reach agreements, and handle disputes without human mediation
- **Trust and security mechanisms:** Verifying agent identity, intent, and行为的 authenticity in multi-agent environments
- **Decentralized identity management:** Standards for agent identification analogous to but distinct from human digital identity
- **Scalable reasoning architectures:** Architectures that support complex decision-making across multiple agents without central coordination bottlenecks

## Application Domains

The paper surveys implications across:
- E-commerce (direct relevance)
- Education (personalized learning agents)
- Healthcare (diagnostic and treatment coordination agents)
- Smart cities (infrastructure management agents)

## Consumer Protection Implications

- The protocol-level standards discussed in this paper directly shape the consumer protection landscape — who controls the communication protocols between commerce agents matters for whether consumers retain agency
- Decentralized identity standards must account for both human and agent identities to prevent impersonation attacks
- The "seven-axis generated-claim gate" from Sfiris (2607.18347) is one proposed solution to trust challenges this paper identifies broadly

## Source

- raw/papers/agentic-web-weaving-next-web-2507.21206.md
