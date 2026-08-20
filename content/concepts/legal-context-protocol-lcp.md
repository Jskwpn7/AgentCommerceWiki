---
title: "Legal Context Protocol (LCP) — Open Standard for Agentic Commerce"
created: 2026-08-18
updated: 2026-08-18
type: concept
tags: [agentic-commerce, legal-infrastructure, settlement, dispute-resolution, consumer-harm]
sector: [cross-sector]
status: primary
confidence: high
---

# Legal Context Protocol (LCP)

**Also known as:** LCP, AAA Legal Context Protocol, Agentic Commerce Legal Infrastructure

## Definition

The **Legal Context Protocol (LCP)** is an open standard launched June 24, 2026 by the American Arbitration Association (AAA) and Integra Ledger. It makes legal terms, consent records, and dispute resolution provisions discoverable before a transaction and verifiable afterward — via cryptographic fingerprint bound to payment and tied to the parties' chosen jurisdiction's law. Published under Apache 2.0 with governance designed for transfer to a neutral foundation.

## Consumer Harm Context

The existence of LCP reveals an **infrastructure asymmetry**: enterprise B2B agentic commerce has a formal legal infrastructure layer (terms discoverability, cryptographic proof, dispute resolution), while consumer-facing agentic commerce has no equivalent overlay. Every infrastructure layer in the agent commerce stack — legal terms, identity, settlement, escrow — is enterprise-first with no mandated consumer protection component.

## Key Technical Elements

- **Pre-transaction discoverability** — Legal context available before deal execution
- **Post-transaction provability** — Cryptographic fingerprint bound to payment creates audit trail
- **Jurisdictional anchoring** — Tied to chosen law, not a single standard
- **Neutral governance** — Designed for eventual transfer from AAA/Integra Ledger to independent foundation

## Consumer Protection Implications

The absence of a consumer-oriented legal context layer means:
1. Consumers have no way to verify what terms govern their agent-mediated purchases before execution
2. No cryptographic proof exists when disputes arise over agent actions
3. Dispute resolution mechanisms are designed for B2B, not consumer-scale transactions
4. The LCP coalition's founding members (Google, IBM, Circle, Wayfair, etc.) are all enterprise entities — no consumer advocacy organizations involved

## Cross-References

- [[legal-context-protocol-adr-2026]] — Summary of the AAA/Integra Ledger launch announcement
- [[adyen-agentic-2026]] — Payment infrastructure context; LCP adds missing legal/terms layer
- [[a2a-settlement-protocols-agentlux-2026]] — Technical escrow (ERC-8183) + LCP's legal terms layer = enterprise stack, but no consumer equivalent
