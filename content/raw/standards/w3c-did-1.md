---
title: "Decentralized Identifiers (DIDs) v1.0 (W3C Recommendation, July 2022)"

created: 2026-07-13
updated: 2026-07-13
type: raw
url: https://www.w3.org/TR/did-1.0/
url_title: W3C Decentralized Identifiers v1.0
extracted: 2026-07-13
sha256: [REDACTED]
license: W3C Software and Document Notice and License
---

# Decentralized Identifiers (DIDs) v1.0

**Standard**: W3C Recommendation 19 July 2022 • **Working Group**: Decentralized Identifier Working Group

## Abstract

Decentralized identifiers (DIDs) are a new type of identifier that enables verifiable, decentralized digital identity. A DID refers to any subject (e.g., a person, organization, thing, data model, abstract entity, etc.) as determined by the controller of the DID. In contrast to typical, federated identifiers, DIDs have been designed so that they may be decoupled from centralized registries, identity providers, and certificate authorities.

## Design Goals

| Goal | Description |
| --- | --- |
| Decentralization | Eliminate the requirement for centralized authorities or single point of failure |
| Control | Give entities power to directly control their digital identifiers |
| Privacy | Enable entities to control privacy — minimal, selective, progressive disclosure |
| Security | Enable sufficient security for requesting parties to depend on DID documents |
| Proof-based | Enable DID controllers to provide cryptographic proof |
| Discoverability | Make it possible for entities to discover DIDs for other entities |
| Interoperability | Use interoperable standards |
| Portability | System- and network-independent |
| Simplicity | Reduced set of simple features |
| Extensibility | Enable extensibility without hindering interoperability |

## Architecture

- **DID**: URI scheme `did:method:specific-id` — three parts (scheme, method, method-specific string)
- **DID document**: Contains cryptographic material, verification methods, and services
- **Verifiable Data Registry**: Where DIDs and DID documents are recorded
- **DID resolution**: DIDs resolve to DID documents without relying on centralized registries

At time of publication, 103 experimental DID Method specifications, 32 experimental driver implementations, and 46 implementations submitted to the conformance test suite.

## Relevance to KYA

Foundational standard for decentralized agent identity. Provides the identifier scheme and resolution mechanism that can underpin Know Your Agent (KYA) systems, enabling agents to prove control over their identity without reliance on centralized registries. Critical complement to W3C VC-DM v2.0 for agent identity infrastructure.

## Referenced In

- [[w3c-vc-data-model-v2]] — W3C Verifiable Credentials Data Model v2.0 (complementary VC standard)
- [[nist-nccoe-2026-agent-identity-authorization]] — NCCoE concept paper

[[#top]]
