---
title: Know Your Agent — NIST RFI and RFI Commentary (February 2026)
created: 2026-07-13
updated: 2026-07-13
type: raw
url: https://knowyouragent.network/nist-rfi-ai-agent-identity-march-2026
url_title: KnowYourAgent Network Commentary
extracted: 2026-07-13
sha256: [REDACTED]
license: © KnowYourAgent Network
---

# Know Your Agent — NIST RFI and RFI Commentary

**KnowYourAgent Network (KYA)** — February 13, 2026

## Abstract

On January 8, 2026, NIST's Center for AI Standards and Innovation (CAISI) published a Request for Information titled "Security Considerations for Artificial Intelligence Agents." The comment deadline is March 9, 2026. As of mid-February, only 54 comments had been submitted — far fewer than a routine FDA food labeling rule would attract.

A month later, NCCoE released a companion concept paper: "Accelerating the Adoption of Software and Artificial Intelligence Agent Identity and Authorization." Comments due April 2, 2026.

This commentary argues that the voices of independent developers, open-source communities, startups, and researchers are underrepresented in the NIST comment process, and that decentralized identity approaches (DIDs, verifiable credentials, soulbound tokens) are not yet in the record despite academic and industry support.

## Key Points from the Commentary

### What NIST Is Asking

The RFI covers 5 categories:

1. **Security threats and risks**: Unique threats to AI agent systems, evolving risk profiles
2. **Security practices**: Technical controls at model, system, and human-oversight levels
3. **Assessing security**: Threat anticipation and incident detection
4. **Deployment environments**: Identity, access constraints, monitoring in production
5. **Additional considerations**: Government collaboration priorities

### The Second Document Nobody's Talking About

The NCCoE concept paper is more specific than the RFI. It proposes a demonstration project across 4 areas:

1. **Identification**: Distinguishing AI agents from humans, managing metadata
2. **Authorization**: OAuth 2.0, policy-based access control
3. **Access delegation**: Linking user identities to agents for accountability
4. **Logging and transparency**: Auditability of agent actions

### Regulatory Landscape Beyond NIST

- **Singapore**: World's first agentic AI governance framework (IMDA, January 2026) — requires agent identity management
- **EU AI Act**: Article 50 transparency requirements take effect August 2, 2026
- **UK AISI**: Agentic safety rates significantly lower than conversational tasks (57% vs 99%)
- **ITU**: New working group on AI security and digital identity for agentic AI

### Private Sector Infrastructure Already Built

- **Visa Trusted Agent Protocol (TAP)**: Agent-specific cryptographic signatures (October 2025)
- **Mastercard Agent Pay**: Registered and verified agents (April 2025)
- **Google Agent Payments Protocol (AP2)**: 60+ organizations including Amex, PayPal, Coinbase
- **CrowdStrike acquired SGNL**: $740M acquisition for AI agent identity security
- **Trulioo Know Your Agent framework**: Digital Agent Passport (DAP) with 5 verification steps
- **Microsoft Entra Agent ID**: Unique identity profiles with conditional access
- **Okta Agent Discovery**: OAuth consent event detection for shadow agents

### Academic Foundation

- **"Authenticated Delegation and Authorized AI Agents"** (South et al., MIT Media Lab, ICML 2025 Oral): Extends OAuth 2.0/OpenID Connect with agent-specific credentials
- **"Know Your Agent: Governing AI Identity on the Agentic Web"** (Chaffer, February 2025): Blockchain, smart contracts, DAOs, soulbound tokens, ZKPs for decentralized agent governance
- **"A Novel Zero-Trust Identity Framework for Agentic AI"** (Cloud Security Alliance, AWS, MIT, Salesforce): DIDs, VCs, Agent Naming Service
- **"Multi-Agent Risks from Advanced AI"** (Cooperative AI Foundation, 30+ researchers): Failure modes — miscoordination, conflict, collusion

### Why 54 Comments Isn't Enough

The commentary argues that the conversation is dominated by large enterprises and law firms, while independent developers, open-source communities, and decentralized identity researchers are underrepresented. The NCCoE concept paper references OAuth 2.0, OpenID Connect, SPIFFE/SPIRE but does not mention DIDs, verifiable credentials, soulbound tokens, or on-chain identity — despite academic literature supporting these approaches.

## Implications for Consumer Protection

- **Agent Identity Gaps**: Without comprehensive identity frameworks, consumers cannot verify which agents are acting on their behalf or with what authority
- **Decentralized Identity Opportunity**: DIDs and verifiable credentials offer a more decentralized, user-controlled alternative to centralized identity systems — but only if they're included in the standards conversation
- **Private Sector Leadership**: Payment networks and cloud providers are building agent identity infrastructure ahead of regulators, creating de facto standards that may not prioritize consumer interests

## Comment Submission

- **CAISI RFI**: regulations.gov/document/NIST-2025-0035-0001 (deadline: March 9, 2026)
- **NCCoE Concept Paper**: Email AI-Identity@nist.gov (deadline: April 2, 2026)

## Related Pages

- [[nist-nccoe-2026-agent-identity-authorization]] — NCCoE concept paper
- [[w3c-vc-data-model-v2]] — W3C Verifiable Credentials Data Model v2.0
- [[w3c-did-1]] — W3C Decentralized Identifiers v1.0

[[#top]]
