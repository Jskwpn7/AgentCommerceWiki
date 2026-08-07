---
title: "Investigating the Impact of Dark Patterns on LLM-Based Web Agents"
created: 2026-07-27
updated: 2026-07-27
type: summary
tags: [dark-pattern, llm-safety, web-agent-security, empirical-study, consumer-harm, ieee-sp, task-completion-bias]
sources:
  - arxiv:2510.18113
  - https://arxiv.org/abs/2510.18113
confidence: HIGH
---

# Investigating the Impact of Dark Patterns on LLM-Based Web Agents

**Published:** 2025-10 (accepted to IEEE S&P 2026)
**Source:** [arXiv:2510.18113](https://arxiv.org/abs/2510.18113)

## Abstract Summary

First study investigating dark pattern impact on LLM-based generalist web agents. Uses **TrickyArena** — a controlled environment with web applications from e-commerce, streaming, and news domains containing realistic dark patterns. Evaluates six LLM-based web agents (Skyvern, DoBrowser, BrowserUse, Agent-E, WebArena, VisualWebArena) across three LLMs (Claude 3.7 Sonnet, GPT-4o, Gemini 2.5 Pro).

## Key Findings

1. **41% average susceptibility** — when a single dark pattern is present, agents are susceptible 41% of the time on average.
2. **Higher-performing agents are MORE vulnerable** — Skyvern 72.3% and BrowserUse 69.3% DPSR (Dark Pattern Susceptibility Rate), likely because they prioritise task completion even when deceived.
3. **Obstruction and Social Engineering** dark patterns are most effective (52.2% and 47.9% susceptibility).
4. **Interaction paralysis** — lower-performing agents are less impacted due to early-exit failures that incidentally evade dark patterns.

## Consumer Protection Implications

This is the first rigorous empirical measurement of how susceptible AI web agents are to dark patterns. The finding that **the best agents (which consumers would naturally adopt) are also the easiest to manipulate** is a force multiplier for existing dark pattern harm.

## Cross-References

[[dark-pattern]], [[ai-shopping-agents]], [[ai-agents-sensitive-to-nudges-cherep-2026]], [[agentic-relationship-harm]]
