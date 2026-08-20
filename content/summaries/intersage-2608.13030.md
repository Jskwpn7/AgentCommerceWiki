---
title: "InterSAGE: Secure & Verifiable Interoperability Protocol for an Internet of Agents"
created: 2026-08-17
updated: 2026-08-17
type: summary
tags: [agentic-ai, academic, digital-platforms, protocol-competition, agent-liability]
sources: ["https://arxiv.org/abs/2608.13030"]
confidence: high
---

# InterSAGE: Secure & Verifiable Interoperability Protocol for an Internet of Agents

**Paper:** arXiv:2608.13030 — "InterSAGE: The Secure and Verifiable Interoperability Protocol for An Internet of Agents"
**Authors:** Zhenhua Zou, Sheng Guo, Qiuyang Zhan, Lepeng Zhao, Shuo Li, Zhuotao Liu
**Published:** 13 August 2026 (v2: 14 August 2026)
**Primary Source:** [arxiv.org/abs/2608.13030](https://arxiv.org/abs/2608.13030)

## Overview

The emerging "Internet of Agents" enables LLM-powered agents to discover peers, invoke tools, and delegate tasks **across organizational boundaries**. Existing protocols increasingly define how agents *exchange messages*, but not how an agent **proves its identity, authorization, advertised capabilities, or accountability after delegation**.

**InterSAGE** is a trust-native protocol suite that supplies this missing security substrate **alongside** (not in place of) communication protocols. It is designed to complement MCP, A2A, ANP, and AG-UI, letting communication protocols evolve independently while keeping trust semantics explicit, portable, and verifiable.

## Four Layers / Four Core Primitives

InterSAGE comprises four layers — **Persistent Identity, Discovery, Trust Negotiation, and Accountability** — with four core primitives:

1. **Agent Identity Cards** that bind developer, code package, operator, and deployment context.
2. **Capability-aware discovery** using DID-bound Verifiable Credential manifests.
3. **Trust negotiation** combining monotonic capability attenuation with two-tier access control.
4. **Kernel-mediated cryptographic audit trails** that bind usage, delegation, and execution traces to agent identity **without a consensus ledger**.

## Positioning

The authors compare InterSAGE with **more than 50 efforts** spanning agent protocols, decentralized identity, OAuth/OIDC extensions, zero-trust governance, delegation, and audit architectures, and show that **no prior architecture jointly enforces persistent identity, capability-aware discovery, trust negotiation, and accountability** as a unified four-layer trust substrate for secure agent interoperability.

## Consumer Harm Implications

- **"Who authorised this agent?"** InterSAGE directly targets the core liability/audit gap in agentic commerce. Without a verifiable authorization and accountability layer, "unauthorised purchase" disputes default to a he-said/she-said between agent platforms.
- **Audit trail as consumer protection.** The kernel-mediated audit trails are the evidence UK regulators keep citing as missing for tracing a delegated action back to its authorising human.
- **Protocol layer, not a competitor.** Because InterSAGE sits *alongside* ACP/AP2/UCP/TAP/x402 rather than replacing them, it could in principle supply the shared trust substrate that the currently fragmented protocol stack ([[agentic-commerce-protocols]]) lacks.

## Relevance to UK Consumer Harms

InterSAGE is the strongest candidate yet for closing the authorization/accountability gap at the heart of the [[agent-liability]] problem and of the [[agent-identity-and-authorization]] concept. It also maps onto the UK's audit-trail expectations under the CMA's agentic-AI guidance and the DMCC Act's transparency duties. See also the protocol-competition context in [[agentic-commerce-protocols]] and the existing protocol entities [[universal-commerce-protocol-ucp]] and [[agentic-commerce-protocol-acp]].

## Cross-References

- [[agent-liability]] — closes the "who authorised this agent" audit gap
- [[agentic-commerce-protocols]] — sits alongside ACP/AP2/UCP/TAP/x402 as a trust substrate
- [[agent-identity-and-authorization]] — the missing trust layer across protocol stacks
- [[universal-commerce-protocol-ucp]] — a protocol InterSAGE would complement
- [[agentic-commerce-protocol-acp]] — a protocol InterSAGE would complement

## References

1. arXiv:2608.13030 — *InterSAGE: The Secure and Verifiable Interoperability Protocol for An Internet of Agents*
