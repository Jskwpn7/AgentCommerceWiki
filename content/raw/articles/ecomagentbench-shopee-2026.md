---
title: "EComAgentBench — Benchmarking Shopping Agents on Long-Horizon Tasks"

created: 2026-06-30
updated: 2026-06-30
type: raw-article
tags: [agentic-ai, digital-platforms, retail, research, methodology]
sector: [digital-platforms, retail]
status: primary
confidence: high
---

# EComAgentBench: Benchmarking Shopping Agents on Long-Horizon Tasks with Distributed Hidden Intent

**Source:** arXiv (Shopee research team)
**Date:** June 17, 2026
**ID:** 2606.17698
**URL:** https://arxiv.org/abs/2606.17698
**HTML:** https://arxiv.org/html/2606.17698v1

## Overview

A benchmark of 662 tasks grounded in real Amazon Reviews 2023 catalog data that tests whether LLM-based shopping agents can handle **distributed hidden intent** — where a shopper's requirements are scattered across multiple sources rather than stated explicitly.

## Key Innovation

Existing benchmarks expose full intent upfront and grade only the final product choice. EComAgentBench instead scatters requirements across three sources that an agent must discover:

1. **Visible query** — states some needs only implicitly
2. **Hidden persona** — read only via a `get_user_profile` tool (like a user account/profile)
3. **Hidden clarification** — obtained only by asking a question the `ask_user` tool recognizes

An agent must uncover hidden intent, verify candidates against attributes and review evidence, and commit to a single product **within 100 tool calls**.

## Evaluation Framework

Each task has **typed, source-tagged rubrics** that grade every failure by attributing it to a specific requirement and its source. This allows detailed diagnosis of which type of hidden information agents struggle with most.

Construction is automated yet reliable — every answer is fixed in code before any text is generated, and every sample is validated.

## Relevance to UK Consumer Harms

| Vector | Description |
|---|---|
| **Hidden intent exploitation** | The benchmark demonstrates that even sophisticated agents struggle with distributed hidden intent — a capability that e-commerce platforms already exploit through hidden fees, dynamic pricing, and undisclosed preferences |
| **Review manipulation** | The benchmark uses real Amazon Reviews data; the same data sources are vulnerable to review manipulation by sellers |
| **Agent capability gap** | If AI shopping agents cannot reliably uncover hidden requirements, consumers delegating purchases to agents face higher risk of unsuitable purchases |
| **Tool-call limits** | The 100 tool-call limit constrains how thoroughly agents can verify information — analogous to time/attention constraints on human consumers |
| **Verification gap** | Agents must verify candidates against attributes and review evidence — but reviews themselves may be manipulated |

## Connection to Existing Wiki Content

- Extends [[ai-shopping-agents]] with a concrete benchmark showing capability gaps
- Validates concerns in [[affonso-2026-vertical-tacit-collusion]] — if agents cannot detect hidden intent, platforms and sellers can exploit this more easily
- Related to [[conflict-of-interest-in-llm-deployment]] — agents may optimize for platform interests rather than consumer interests when intent is ambiguous

---
Provenance: arXiv 2606.17698 (Shopee, June 2026). Cross-referenced with cron report findings from agentic-commerce-monitor 2026-06-30.
