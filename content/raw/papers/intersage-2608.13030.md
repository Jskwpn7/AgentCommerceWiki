---
title: "InterSAGE: The Secure and Verifiable Interoperability Protocol for An Internet of Agents"
type: raw
source_url: https://arxiv.org/abs/2608.13030
ingested: 2026-08-17
tags:
  - agentic-ai
  - academic
  - agentic-commerce
---

# InterSAGE: The Secure and Verifiable Interoperability Protocol for An Internet of Agents

arXiv:2608.13030 — 13 Aug 2026 (v1), last revised 14 Aug 2026 (this version, v2)

**Authors:** Zou, Zhenhua, Guo, Sheng, Zhan, Qiuyang, Zhao, Lepeng, Li, Shuo, Liu, Zhuotao

## Abstract (verbatim from arXiv)

The emerging Internet of Agents enables LLM-powered agents to discover peers, invoke tools, and delegate tasks across organizational boundaries. Existing protocols increasingly define how agents exchange messages, but not how an agent proves its identity, authorization, advertised capabilities, or accountability after delegation. We present InterSAGE, a trust-native protocol suite that supplies this missing security substrate alongside, rather than in place of, communication protocols. InterSAGE comprises four layers: Persistent Identity, Discovery, Trust Negotiation, and Accountability. Its four core primitives are: (1) Agent Identity Cards that bind developer, code package, operator, and deployment context; (2) capability-aware discovery using DID-bound Verifiable Credential manifests; (3) trust negotiation combining monotonic capability attenuation with two-tier access control; and (4) kernel-mediated cryptographic audit trails that bind usage, delegation, and execution traces to agent identity without a consensus ledger. InterSAGE is designed to complement MCP, A2A, ANP, and AG-UI, allowing communication protocols to evolve independently while keeping trust semantics explicit, portable, and verifiable. We compare InterSAGE with more than 50 efforts spanning agent protocols, decentralized identity, OAuth/OIDC extensions, zero-trust governance, delegation, and audit architectures. We show that no prior architecture jointly enforces persistent identity, capability-aware discovery, trust negotiation, and accountability as a unified four-layer trust substrate for secure agent interoperability.
