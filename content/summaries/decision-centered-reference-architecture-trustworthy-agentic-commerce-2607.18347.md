---
title: "A Decision-Centered Reference Architecture for Trustworthy Agentic Commerce"
type: summary
source_url: https://arxiv.org/abs/2607.18347
authors: [Dimitrios S. Sfiris]
date: 2026-07-20
pages: 23
figures: 3
subjects: [cs.SE, cs.CR, cs.MA]
acm_classes: [D.2.11, K.4.4, I.2.11, K.6.5]
review_status: Published
tags: [agentic-commerce, trustworthy-ai, agent-security, commerce-protocols, consumer-protection, decision-architecture, cryptographic-verification]
---

# A Decision-Centered Reference Architecture for Trustworthy Agentic Commerce

arXiv:2607.18347 (cs.SE / cs.CR / cs.MA), 20 July 2026 | Sfiris | AspectSoft, Xanthi, Greece | 23 pages, 3 figures + ancillary reproducibility materials

## Summary

Presents a design-science study proposing a **protocol-agnostic architecture for trustworthy agentic commerce** — an authentication and verification framework ensuring that when AI agents act on behalf of consumers in e-commerce transactions, every commercial decision can be cryptographically verified, audited, and traced back to authoritative sources.

## Core Architecture: The Canonical Envelope

A single, unified representation containing the authoritative record of all commercial decisions including:
- Commercial eligibility (does the consumer qualify?)
- Actor authority (is the agent authorized to act?)
- Checkout validity (are prices, terms, stock accurate?)
- Payment dispatch (is payment properly authorized?)
- Generated claims (what did the AI decide and why?)
- Evidence (proof supporting each decision)

## Security Mechanisms (6 layers)

1. **Protected dependency and result hashes** — cryptographic binding between inputs and outputs preventing tampering
2. **Ed25519 or HMAC authentication** — verifies agent identity before transactions proceed
3. **Live-request rebinding** — prevents replay attacks by binding decisions to the specific execution context/time
4. **Seven-axis generated-claim gate** — validates AI-generated transaction claims across seven dimensions before execution (prevents autonomous agents from executing unverified decisions)
5. **Execution-time dependency revalidation** — re-checks assumptions at decision time, not just planning time (critical because market conditions change between planning and execution)
6. **Eleven semantic invariants** — business rules that must hold for any transaction to be valid

## Evaluation Results

- Open-source JavaScript implementation tested against **8 deterministic e-commerce scenarios**
- 7 initially valid actions were correctly permitted
- After protected state changed, none could proceed without fresh decisions — demonstrating the live-rebinding mechanism works
- Hostile-accessor case was blocked — unauthorized agents cannot execute transactions
- Each ablation (removing one safeguard) produced the predicted unsafe regression — confirming each component is independently necessary

## Relevance to Agentic Commerce Wiki

This paper provides the most concrete security architecture proposal for trustworthy agentic commerce in the current corpus. The seven-axis claim gate and execution-time revalidation directly address two major consumer protection failures in agent-mediated commerce:
1. Agents executing decisions based on stale or manipulated data
2. Unauthorised agents impersonating legitimate representatives

The paper's approach is protocol-agnostic, meaning it can work across different commerce platforms — a key design choice for interoperable consumer protection infrastructure.

## Source

- raw/papers/decision-centered-reference-architecture-trustworthy-agentic-commerce-2607.18347.md
