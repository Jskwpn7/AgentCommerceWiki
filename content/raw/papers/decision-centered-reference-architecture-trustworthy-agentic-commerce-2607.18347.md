---
title: "A Decision-Centered Reference Architecture for Trustworthy Agentic Commerce"
source_url: https://arxiv.org/abs/2607.18347
authors: [Dimitrios S. Sfiris]
institution: AspectSoft, Xanthi, Greece
date: 2026-07-20
pages: 23
figures: 3
subjects: [cs.SE, cs.CR, cs.MA]
acm_classes: [D.2.11, K.4.4, I.2.11, K.6.5]
tags: [agentic-commerce, trustworthy-ai, agent-security, decision-architecture, commerce-protocols, consumer-protection]
---

A Decision-Centered Reference Architecture for Trustworthy Agentic Commerce

arXiv:2607.18347 (cs.SE / cs.CR / cs.MA), 20 July 2026. 23 pages, 3 figures. Includes ancillary reproducibility materials.

Author: Dimitrios S. Sfiris
AspectSoft, Xanthi, Greece
info@aspectsoft.gr

## Abstract

Agentic commerce extends agentic shopping into software agents that interpret policy, prepare checkout, generate transaction-facing language, and act under delegated payment authority. Protocols standardize external exchanges, but merchants still need one authoritative representation of commercial eligibility, actor authority, checkout validity, payment dispatch, generated claims, and evidence. This design-science study presents a protocol-agnostic architecture built around a canonical envelope, protected dependency and result hashes, Ed25519 or HMAC authentication, live-request rebinding, a seven-axis generated-claim gate, execution-time dependency revalidation, and eleven semantic invariants. Evaluation used an open-source JavaScript implementation, eight deterministic e-commerce scenarios, and five controlled ablations. Seven initially valid actions were permitted. After protected state changed, none could proceed without a fresh decision; a hostile-accessor case also remained blocked. Action status was consistent across configured surface-bound envelopes, and each scenario contained the three protected hashes and its targeted dependency reference. Each ablation produced the predicted unsafe regression when one safeguard was bypassed.

## Key Contributions

**Canonical Envelope Architecture:**
- Protocol-agnostic architecture for trustworthy agentic commerce
- Single authoritative representation of all commercial decisions (eligibility, authority, checkout validity, payment dispatch, claims, evidence)

**Security Mechanisms:**
1. **Protected dependency and result hashes** — cryptographic binding between inputs and outputs
2. **Ed25519 or HMAC authentication** — agent identity verification
3. **Live-request rebinding** — prevents replay attacks on expired decisions
4. **Seven-axis generated-claim gate** — validates AI-generated transaction claims before execution
5. **Execution-time dependency revalidation** — re-checks assumptions at decision time, not just planning time
6. **Eleven semantic invariants** — business rules that must hold for any transaction

**Evaluation Results:**
- Open-source JavaScript implementation tested against 8 deterministic e-commerce scenarios
- 7 initially valid actions were correctly permitted
- After protected state changed, none could proceed without fresh decisions
- Hostile-accessor case was blocked
- Each ablation (removing one safeguard) produced the predicted unsafe regression — confirming each component is necessary

## Relevance to Agentic Commerce Wiki

This is directly relevant as it addresses the trust and security architecture needed for agentic commerce. It proposes concrete mechanisms for ensuring that when AI agents act on behalf of consumers, every commercial decision can be verified, audited, and traced back to authoritative sources — critical for consumer protection and regulatory compliance.

## Source Files
- raw/papers/decision-centered-reference-architecture-trustworthy-agentic-commerce-2607.18347.md (this file)
- summaries/decision-centered-reference-architecture-trustworthy-agentic-commerce-2607.18347.md
