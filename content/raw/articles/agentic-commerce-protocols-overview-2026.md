---
source_url: https://www.linkedin.com/posts/rakeshgohel01_traditional-checkout-flows-werent-built-activity-7401598475601444864-gVLK
ingested: 2026-06-26
tags: [digital-platforms, financial-services, agentic-ai, choice-architecture]
---

# Emerging Agent Commerce Protocols (June 2026)

As AI agents evolve from answering questions to executing transactions, traditional checkout flows (designed for humans clicking buttons) are being replaced by machine-readable protocols.

## Key Protocols

### 1. ACP (Agent Commerce Protocol)
- **Developers:** OpenAI & Stripe
- **Mechanism:** Enables agent checkout through **Shared Payment Tokens (SPT)**.
- **Workflow:**
    1. Agent initiates purchase flow.
    2. User reviews and approves selections.
    3. Agent shares SPT with merchant.
    4. Merchant charges via existing processors.
- **Focus:** Delegated shopping with explicit user approval.

### 2. AP2 (Agent Payment Protocol)
- **Developer:** Google
- **Mechanism:** Uses **Intent Mandates** and verifiable credentials.
- **Workflow:**
    1. Capture user intent (Intent Mandate).
    2. User signs mandate with payment constraints.
    3. Payment method linked to verified mandate.
    4. Execution happens automatically within signed rules.
- **Focus:** Pre-authorized, recurring, or rule-based agent spending.

### 3. TAP (Trusted Agent Protocol)
- **Developer:** VISA
- **Mechanism:** Cryptographically signed intent and agent identity verification.
- **Workflow:**
    1. Agent sends signed intent to merchant.
    2. Merchant verifies signature using Visa's public keys.
    3. Proceed with normal checkout.
- **Focus:** A rail-agnostic trust layer for identity and intent.

### 4. x402 (Coinbase Protocol)
- **Developer:** Coinbase
- **Mechanism:** HTTP-based on-chain pay-per-use via USDC on Base (EIP-712).
- **Workflow:**
    1. Server returns HTTP 402 status with payment terms.
    2. Client pays via facilitator using stablecoins.
    3. Payment verified on-chain.
- **Focus:** Microtransactions and API monetization.

### 5. UCP (Universal Commerce Protocol)
- **Status:** Open standard, donated to FIDO Alliance (April 2026).
- **Architecture:** Layered (Services $\rightarrow$ Capabilities $\rightarrow$ Extensions $\rightarrow$ Transport).
- **Goal:** Solve fragmentation in agentic shopping.

## Implications for Consumer Harms

- **Invisible Spending:** AP2's "automatic execution within signed rules" can lead to spending without real-time awareness.
- **Consent Erosion:** The shift from "approve each item" (ACP) to "sign a mandate" (AP2) reduces the granularity of consumer consent.
- **Platform Lock-in:** If merchants only support ACP or AP2, consumers may be forced into specific AI ecosystems (OpenAI/Google) to access certain goods.
- **Data Concentration:** These protocols centralize transaction intent and execution data within a few mega-platforms (Stripe, Google, Visa).

## Notes
The shift toward "Human-Not-Present" support (UCP v0.2) represents a critical transition in consumer agency.
