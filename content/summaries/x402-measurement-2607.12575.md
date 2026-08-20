---
title: "How Agentic Is Agentic Commerce? A Population-Scale Measurement of x402 Adoption and Authenticity"
type: summary
date: 2026-08-03
source_url: https://arxiv.org/abs/2607.12575
authors:
  - Shengchen Ling
  - Yajin Zhou
  - Lei Wu
  - Cong Wang
tags:
  - x402
  - measurement
  - adoption
  - authenticity
  - blockchain
  - base
  - settlement
  - manufacturability
summary: |
  First population-scale measurement of x402 protocol on Base blockchain (136.7M settlements, $44.1M over 280 days). Shows settlement count is largely manufactured: 21.2% fictitious, 63.78% internal settlement within linked cluster. Only $187K demonstrably reaches nameable services. 45.92% of value not provably manufactured. Settlement count measures manufacturability, not adoption.
concepts:
  - x402
  - adoption-measurement
  - settlement-analysis
  - blockchain-analytics
  - manufacturability
  - agent-economy
---

## Overview

This paper provides the first population-scale measurement of x402 — the most widely deployed protocol for agentic commerce payments — revealing significant concerns about reported adoption metrics.

## Key Contributions

1. **Population-Scale Analysis**: 136,708,672 settlements worth $44,121,383.81 over 280-day window on Base blockchain
2. **Payment Graph Analysis**: Resolves true payers through meta-transaction layer, sorts by payment trace evidence
3. **Manufacturability Metric**: Demonstrates settlement count can be manufactured almost for free

## Key Findings

- **21.20%** of settlements are fictitious
- **63.78%** are internal settlements within a linked cluster
- **Gini coefficients > 0.98** on every axis (payer, recipient, value) — extreme concentration
- Only **$187,861.35** demonstrably reaches a nameable service
- **$20,258,746.09 (45.92% of value)** not provably manufactured
- Operator-driven economy is: star-shaped, machine-timed, gas-subsidized

## Methodology

- On-chain event identification
- Meta-transaction layer resolution of true payer
- Payment graph analysis proving ownership
- Coarser Solana census supplementing Base analysis

## Implications for Consumer Protection

1. **False Adoption Metrics**: Industry claims about agentic commerce adoption are misleading
2. **Machine-Timed Activity**: Settlements appear machine-generated rather than human-initiated
3. **Gas Subsidization**: Facilitator sponsors gas costs, enabling artificial settlement volume
4. **Lack of Transparency**: No on-chain mechanism to identify who controls payments
5. **Market Manipulation**: Artificial settlement volumes may mislead consumers and regulators about agentic commerce maturity

This paper demonstrates that the "agentic economy" narrative is currently driven by manufactured metrics rather than genuine consumer adoption.

## Citations

- Paper: [[arXiv:2607.12575]](https://arxiv.org/abs/2607.12575)
