---
title: "Five Attacks on x402 Agentic Payment Protocol"
type: summary
date: 2026-08-03
source_url: https://arxiv.org/abs/2605.11781
authors:
  - Zelin Li
  - Qin Wang
  - Zhipeng Wang
tags:
  - payment-security
  - payment-protocol-attacks
  - transaction-forgery
  - x402
  - replay-attacks
  - web-layer-vulnerabilities
---

# Five Attacks on x402 Agentic Payment Protocol

## Paper Details

- **arXiv ID:** 2605.11781
- **Authors:** Zelin Li, Qin Wang, Zhipeng Wang
- **Source URL:** https://arxiv.org/abs/2605.11781
- **Date:** May 2026

## Summary

The x402 protocol revives the HTTP 402 Payment Required status code for web-native micropayments across APIs, content, and agents. This paper formally analyzes x402 and presents five concrete attacks revealing weaknesses in authorization, binding, replay protection, and web-layer handling. Attacks validated on local chains, Base Sepolia, and live endpoints; also auditing three open-source SDKs and endpoints.

## Consumer Harm Implications

- **Payment protocol attacks:** All five attacks are practical and can cause either unpaid service or paid-but-denied outcomes.
- **Transaction forgery:** Weaknesses in authorization and binding enable transaction manipulation.
- **Cross-layer attack surface:** x402 introduces vulnerabilities absent from conventional web and on-chain payments.
- **SDK vulnerabilities:** Three open-source SDKs were found vulnerable, indicating systemic security issues.

## Connection to Other Wiki Entries

- [[agentic-commerce-research-2026]]
- [[payment-vulnerabilities]]
- [[transaction-forgery]]
- [[payment-protocol-attacks]]

## Key Findings

- x402 is vulnerable in both design and implementation.
- All five attacks are practical across multiple stages of the payment workflow.
- Attacks validated on reproducible testbed with local chains, Base Sepolia, and live endpoints.
- Practical mitigations are proposed but do not fully eliminate risks.
