---
title: "FaMA: LLM-Empowered Agentic Assistant for Consumer-to-Consumer Marketplace"
type: summary
created: 2026-08-03
updated: 2026-08-16
source_url: https://arxiv.org/abs/2509.03890
authors:
  - Yineng Yan
  - Xidong Wang
  - Jin Seng Cheng
  - Ran Hu
  - Wentao Guan
  - Nahid Farahmand
  - Hengte Lin
  - Yue Li
tags: [academic, agentic-ai, retail, digital-platforms]
confidence: high
---

# FaMA: LLM-Empowered Agentic Assistant for Consumer-to-Consumer Marketplace

arXiv:2509.03890 (cs.AI), 4 September 2025.

FaMA (Facebook Marketplace Assistant) is an LLM-powered agentic assistant that acts as a conversational entry point to a C2C e-commerce marketplace, replacing high-friction GUI workflows with natural-language commands.

## Architecture & capabilities

- **Buyers:** conversational product discovery (search by natural-language description instead of GUI filters/navigation).
- **Sellers:** simplified listing updates and renewals; bulk messaging to interested buyers.
- The agent interprets user intent, plans multi-step actions, and uses tools to execute them against the marketplace — a shift from "user drives the GUI" to "user delegates to the agent."

## Results

- **98% task success rate** on complex marketplace tasks.
- **Up to 2x speedup** in interaction time versus the GUI baseline.

## Relevance to UK Consumer Harms

- Direct evidence of the conversational-commerce paradigm this wiki tracks: when an agent mediates discovery, **what the agent retrieves and how it ranks it becomes the consumer's effective choice set** — the same gatekeeping dynamic analysed in [[ai-shopping-agents]].
- FaMA is a *user-side* assistant (acts for the consumer), which contrasts with merchant-side steering documented in [[llm-travel-agents-consumer-harm]]; the consumer-protection question is whether user-side agents reliably protect the consumer's own interests (price, authenticity, seller conduct) or merely speed up the same GUI process.
- C2C marketplaces are a known area of weak seller accountability (no merchant vetting, informal listings); delegating purchase workflows to an agent raises the stakes for fraud detection — see [[dark-pattern]] on manipulation of agent decision paths.

## Source

- raw/papers/fama-c2c-marketplace-2509.03890.md (re-ingested 2026-08-16)
