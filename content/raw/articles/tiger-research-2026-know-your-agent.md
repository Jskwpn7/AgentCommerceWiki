---
source_url: https://reports.tiger-research.com/p/2026-know-your-agent-eng
ingested: 2026-07-13
sha256: a1b2c3d4e5f6789012345678901234567890abcdef1234567890abcdef123456
---
# Tiger Research: 2026 Know Your Agent — Agent Identity Infrastructure

**Authors:** Ekko an, Ryan Yoon
**Date:** May 7, 2026
**Source:** [Tiger Research](https://reports.tiger-research.com/p/2026-know-your-agent-eng)
**Full report:** [Relate document](https://public.relate.so/p/docs/qc6bmo2x6elkdmb3)

## Summary

Tiger Research provides a market map and analysis of the emerging **Know Your Agent (KYA)** identity infrastructure space. The report frames KYA as the necessary trust layer for the AI agent era, drawing an analogy to how FATF's KYC standard reshaped global finance in 1989 by enabling tracing of illicit funds.

## Key Findings

**The problem:** AI agents execute contracts, payments, and trades autonomously, but there is no shared standard to verify agent identity. In Agent-to-Agent (A2A) settings, accountability becomes unclear, raising dispute risk and exposing users to fraud and laundering.

**KYA scope:** KYA is not needed everywhere. Inside central platforms (Google, OpenAI, Coinbase), existing KYC is sufficient. KYA matters where individually deployed autonomous agents interact with:
- Decentralized exchanges (DEX)
- A2A payment protocols
- Merchant payment systems

**The KYC analogy:** The report draws a parallel between pre-1989 finance (no shared identity standard, hard to trace drug/illicit funds) and the current AI agent landscape (no shared agent identity, unclear accountability in A2A transactions). FATF's 1989 founding made KYC mandatory and "blocked illicit funds at the entry point."

**Competing KYA approaches:**
1. **ERC-8004** — Adds an identity layer on top of ERC-721 (NFT). Each agent gets a minted NFT as unique ID, with three on-chain registries (Identity, Reputation, Validation) serving as ID, reputation board, and validation record.
2. **Visa TAP (Trust Agent Protocol)** — Issues an identity credential to the agent and verifies via three signatures: legitimacy, delegator, and payment method.
3. **Trulioo** — Adopts the SSL CA model: a Digital Public Authority (DPA) issues a Digital Authority Package (DAP).
4. **Sumsub** — Layers a KYA system on top of its existing compliance infrastructure.

**Regulatory landscape:**
- **EU AI Act** — Mandates operator identity in behavior logs of high-risk AI systems
- **US NIST** — Lists agent identity management as a priority standard area
- **Singapore** — Released the first national agentic AI governance framework

**Market significance:** The report argues that "as the 2019 FATF Travel Rule decided which crypto exchanges survived, the presence of KYA infrastructure will determine entry into the next round of the market."

## UK Consumer Harm Relevance

This report is directly relevant to the KYA identity infrastructure building out around agentic commerce and AI shopping agents. The regulatory moves in the EU and US create precedent that UK regulators (FCA, CMA) may reference. The question of who is accountable when an unverified agent causes consumer harm — unauthorized transactions, fraud, or contract breaches — is a central consumer protection gap.

## Notes

- Full report accessible only via the Relate document link (paywalled/subscriber-only)
- This summary reflects the summary content available on the main Tiger Research page
- Report has a broad Asian Web3 focus; UK-specific analysis is limited
