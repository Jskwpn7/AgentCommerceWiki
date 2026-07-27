---
title: Verifiable Credentials Data Model v2.0 (W3C Recommendation, May 2025)
created: 2026-07-13
updated: 2026-07-13
type: raw
url: https://www.w3.org/TR/vc-data-model/
url_title: W3C Verifiable Credentials Data Model v2.0
extracted: 2026-07-13
sha256: [REDACTED]
license: W3C Software and Document Notice and License
---

# Verifiable Credentials Data Model v2.0

**Standard**: W3C Recommendation 15 May 2025 • **Working Group**: Verifiable Credentials Working Group

## Abstract

A verifiable credential is a specific way to express a set of claims made by an issuer, such as a driver's license or an education certificate. This specification describes the extensible data model for verifiable credentials, how they can be secured from tampering, and a three-party ecosystem for the exchange of these credentials that is composed of issuers, holders, and verifiers.

## Status

W3C Recommendation. W3C recommends wide deployment as a standard for the Web. After extensive consensus-building, endorsed by W3C and its Members, with commitments from Working Group members to royalty-free licensing for implementations.

## Core Concepts

### Verifiable Credential
Cryptographic expression of claims by an issuer. More tamper-evident and trustworthy than physical counterparts when secured with digital signatures.

### Verifiable Presentation
Holder-generated proof that they possess credentials with specific characteristics, shared with verifiers.

### Three-Party Ecosystem
- **Issuers**: Create and sign verifiable credentials
- **Holders**: Possess and present verifiable credentials
- **Verifiers**: Validate credentials and presentations

This contrasts with typical two-party or federated identity provider models, which tightly bind holders to identity providers. This specification decouples identity provider into two distinct concepts: issuer and holder.

### Security and Privacy
- Secured by at least one securing mechanism (Section 4.12)
- Conforming documents MUST be compacted JSON-LD with media type `application/vc` (credentials) or `application/vp` (presentations)
- Privacy-preserving: zero-knowledge proofs, selective disclosure, subject-holder separation
- Verifiability does not imply truth of claims — verifiers validate against their own business rules

## Relevance to KYA

Provides the foundational data model for verifiable credentials, serving as technical basis for Know Your Agent (KYA) credential issuance. Supports cryptographic verification of agent identity, selective disclosure of agent capabilities, and machine-verifiable delegation.

## Referenced In

- [[w3c-did-1]] — W3C Decentralized Identifiers v1.0 (complementary DID standard)
- [[nist-nccoe-2026-agent-identity-authorization]] — NCCoE references VCs for agent authorization

[[#top]]
