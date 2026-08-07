---
title: "Shopping Agent Benchmarks: EComAgentBench and DynamicMem"
created: 2026-06-30
updated: 2026-06-30
type: summary
tags: [agentic-ai, digital-platforms, retail, methodology, research]
sector: [digital-platforms, retail]
sources: [raw/articles/ecomagentbench-shopee-2026.md, raw/articles/dynamicmem-memory-benchmark-2026.md]
confidence: high
---

# Shopping Agent Benchmarks: EComAgentBench and DynamicMem

**Date:** 2026-06-30
**Sources:** arXiv 2606.17698 (Shopee), arXiv 2606.22877

## Executive Summary

Two June 2026 benchmark papers reveal systematic capability gaps in AI shopping agents that translate directly to consumer harm vectors. EComAgentBench shows agents struggle with hidden intent discovery; DynamicMem shows memory retrieval failures account for over 93% of all failures.

## EComAgentBench: Hidden Intent Discovery

A benchmark of 662 tasks using real Amazon Reviews 2023 catalog data that tests whether agents can handle **distributed hidden intent** — where requirements are scattered across multiple sources a consumer would naturally consult but an agent must actively discover.

### The Challenge
- **Visible query** — states some needs only implicitly
- **Hidden persona** — read only via a `get_user_profile` tool
- **Hidden clarification** — obtained only by asking specific questions

### Consumer Harm Implications
- If agents cannot discover hidden requirements, they recommend unsuitable products
- Review-based verification is itself vulnerable to manipulation
- The 100 tool-call limit constrains verification depth — analogous to human time/attention constraints

## DynamicMem: Memory Retrieval Failure

A long-horizon memory benchmark testing whether AI systems can maintain accurate user profiles over months as preferences and situations change.

### Key Finding
**Over 93% of failures trace to memory retrieval, not to the model that writes the final answer.**

This means:
- Memory systems are the largest room for improvement in agentic AI
- Errors cluster on preferences (which users never state outright) and naming specifics (which gym, which tool)
- Profile reconstruction degrades with history length while service-task accuracy stays flat
- No system manages to keep facts that stay true AND replace facts that change

### Consumer Harm Implications
- Shopping agents making decisions based on stale preference profiles systematically misrepresent consumer interests
- Long-horizon memory systems accumulate vast personal data — GDPR data minimization questions
- If preference tracking is error-prone, malicious actors could potentially influence agents' models

## Connection to Existing Wiki Content

- **[[ai-shopping-agents]]** — Both benchmarks validate capability gaps in AI shopping agents
- **[[long-horizon-personalization]]** — DynamicMem confirms HorizonBench's "belief-update failure" finding; all major failures are retrieval-related
- **[[affonso-2026-vertical-tacit-collusion]]** — If agents cannot detect hidden intent, platforms can exploit this more easily
- **[[conflict-of-interest-in-llm-deployment]]** — When intent is ambiguous, agents may optimize for merchant interests
- **[[banal-deception-llm-chatbots]]** — Agents with poor memory are more susceptible to manipulation

## Benchmark Comparison

| Dimension | EComAgentBench | DynamicMem |
|---|---|---|
| **Focus** | Hidden intent discovery | Long-horizon memory accuracy |
| **Task type** | Shopping/product choice | User profile maintenance |
| **Key failure mode** | Missing hidden requirements | Memory retrieval errors |
| **Data source** | Amazon Reviews 2023 | Real-world settings |
| **Consumer harm** | Wrong product recommendations | Stale preference profiles |
| **Tool constraint** | 100 tool-call limit | Information accumulation over time |

---
Provenance: Synthesized from arXiv 2606.17698 and 2606.22877. Cross-referenced with agentic-commerce-monitor cron report 2026-06-30.
