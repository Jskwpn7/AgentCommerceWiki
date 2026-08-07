---
title: Accelerating the Adoption of Software and AI Agent Identity and Authorization (NCCoE Concept Paper, February 2026)
created: 2026-07-13
updated: 2026-07-13
type: summary
tags: [nist, nccoe, agent-identity, authorization, zero-trust, oauth, identity-management]
sources: [raw/articles/nist-nccoe-2026-agent-identity-authorization.md]
url: https://www.nccoe.nist.gov/projects/software-and-ai-agent-identity-and-authorization
---
# NIST NCCoE: Software and AI Agent Identity and Authorization

**Source**: [[nist-nccoe-2026-agent-identity-authorization|Raw source]] • **Authors**: Booth, Fisher, Galluzzo, Roberts (NIST NCCoE) • **Published**: February 2026 • **Comment deadline**: April 2, 2026

## Overview
NIST NCCoE concept paper seeking stakeholder input for a demonstration project applying existing identity standards and best practices to AI agents. Public comment period: Feb 5 – April 2, 2026.

## Scope
Focus on applying identity standards to **agentic architectures** (instruct → acquire context → process → act → respond). RAG-only and training-data-only architectures are **out of scope**.

## Four Areas of Interest
1. **Identification**: distinguishing AI agents from human identities, managing metadata (ephemeral vs fixed)
2. **Authorization**: OAuth 2.0/2.1, policy-based access control, zero-trust principles
3. **Access Delegation**: linking user identities to agents for accountability, "on behalf of" scenarios
4. **Logging and Transparency**: tamper-proof audit logs, non-repudiation, human-in-the-loop authorizations

## Use Cases Considered
- Enterprise AI agents for personal productivity (calendars, policy documents)
- Security AI agents (analysis + action/recommendation on security data)
- Development/deployment AI agents (automated pipelines with AI agents)

## Standards Referenced
OAuth 2.0/2.1, OpenID Connect, SPIFFE/SPIRE, SCIM, NIST SP 800-207 (Zero Trust), SP 800-63-4 (Digital Identity), Model Context Protocol (MCP)

## Relevance
Directly addresses agent identity, authorization, and accountability — core KYA concerns. NCCoE project would produce practical implementation guides using commercially available technologies.
