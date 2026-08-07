---
title: "GDPR Data Minimisation"

created: 2026-06-22
updated: 2026-06-22
type: concept
tags: [data-protection, gdpr, cross-sector, regulatory-failure]
sector: [cross-sector]
status: primary
confidence: high
---

# GDPR Data Minimisation

## Overview

**Data minimisation** is a core principle of the EU General Data Protection Regulation (GDPR), Article 5(1)(c): personal data must be "adequate, relevant and limited to what is necessary in relation to the purposes for which they are processed."

## Relevance to AI Consumer Harm

AI systems often collect far more data than is necessary for their stated purpose. This creates multiple consumer protection risks:

- **Function creep:** Data collected for one purpose is later used for another (e.g., training, profiling)
- **Inference attacks:** Excessive data enables derivation of sensitive attributes not originally collected
- **Opaque processing:** Consumers cannot understand what data is collected when the process is automated and non-transparent

## Interaction with AI Systems

AI agents that mediate consumer interactions may collect data beyond what is necessary, violating the data minimisation principle. The [[ai-shopping-agents]] concept documents how AI shopping agents collect extensive user data to make purchasing decisions — raising questions about whether this data collection is proportionate.

The [[ai-act]] transparency requirements partially address this, but the GDPR remains the primary data protection framework.

## Cross-References

- [[ai-act]] — Complementary regulation for AI systems
- [[ai-shopping-agents]] — AI agents that may collect excessive data
- [[conflict-of-interest-in-llm-deployment]] — LLM providers may be incentivised to collect and process excessive data
