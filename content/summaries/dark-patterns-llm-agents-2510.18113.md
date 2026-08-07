---
title: "Investigating the Impact of Dark Patterns on LLM-Based Web Agents"
created: 2026-07-24
updated: 2026-07-24
type: summary
tags: [dark-patterns, llm-agents, web-security, ui-deception, consumer-protection, automated-shopping, deceptive-design]
sources: ["https://arxiv.org/abs/2510.18113"]
confidence: high
provenance: "Discovered via Weekly Research Review"
---

# Investigating the Impact of Dark Patterns on LLM-Based Web Agents

## Paper Details

- **Authors:** Devin Ersoy, Brandon Lee, Ananth Shreekumar, Arjun Arunasalam, Muhammad Ibrahim, Antonio Bianchi, Z. Berkay Celik
- **Affiliations:** Purdue University, Florida International University, Georgia Institute of Technology
- **Venue:** IEEE Symposium on Security and Privacy 2026 (S&P 2026)
- **Date:** October 20, 2025
- **arXiv:** 2510.18113
- **Code:** https://github.com/purseclab/liteagent

## Summary

This paper presents the first systematic evaluation of how **dark patterns** — deceptive user interface designs intended to manipulate human users — affect **LLM-based generalist web agents**. The authors introduce two novel tools: **LiteAgent**, a framework for automating agent execution on specific tasks with comprehensive logging and screen recording, and **TrickyArena**, a controlled environment containing web applications from e-commerce, streaming, and news platforms with diverse and realistic dark patterns that can be selectively enabled or disabled.

## Key Findings

### 1. High susceptibility to individual dark patterns
When a single dark pattern is present, LLM-based web agents fall for them an average of **41% of the time**. This is a significant vulnerability for automated shopping, job application, and subscription tasks where agents make decisions on behalf of users.

### 2. UI modification influences susceptibility
Changing dark pattern UI attributes — through visual design (colors, sizing, placement) or HTML code adjustments — can meaningfully increase or decrease agent susceptibility. This mirrors findings in human-facing dark pattern research but with important differences in direction and magnitude for AI agents.

### 3. Counterintuitive: more patterns = less susceptibility
Dark pattern susceptibility generally **decreases as the number of dark patterns increases**. The authors suggest this may be because agents become more cautious or confused when multiple conflicting signals are present, leading to more conservative (i.e., pattern-avoiding) behavior.

### 4. Vision capabilities have mixed results
Without vision capabilities, a majority of agents tested experienced **decreases in task success rates and increases in dark pattern susceptibility** when vision was turned on. This contradicts the assumption that vision always helps agents make better decisions.

### 5. Prompt-based countermeasures help but are incomplete
The most effective countermeasures were **specific step-by-step instructions** on how to avoid a particular dark pattern. However, these prompts only reduced dark pattern susceptibility by an average of **around 32%** — meaning agents remain vulnerable even with explicit warnings.

### 6. First comprehensive evaluation of its kind
The paper establishes **LiteAgent** and **TrickyArena** as reproducible test frameworks for future research. Six popular web agents across three different LLMs were evaluated, providing a benchmark dataset for the community.

## Relevance to UK Consumer Harms Research

This research has direct relevance to several areas of consumer protection:

1. **Automated shopping harms:** Consumers increasingly use AI assistants for shopping. If agents are susceptible to dark patterns, consumers may be tricked into subscriptions, purchases, or data-sharing they would not otherwise consent to — with the AI agent acting as the instrument of deception.

2. **Regulatory enforcement gaps:** Current UK consumer protection frameworks (Consumer Protection from Unfair Trading Regulations 2008, CMA guidance) are designed to protect human consumers. This paper raises the question of whether dark patterns that bypass human scrutiny by targeting AI agents should be treated as a distinct category of unfair practice.

3. **Financial services:** Subscription traps, misleading pricing, and forced continuation — all common dark patterns — are particularly harmful in financial contexts. Agents auto-renewing subscriptions or enrolling users in premium services without meaningful consent represent a novel consumer harm vector.

4. **Digital platform governance:** The FTC's finding that 75% of apps and websites use deceptive design, combined with the 41% agent susceptibility rate, suggests a significant proportion of AI-mediated user interactions may be influenced by deceptive design.

## Connection to Other Wiki Entries

- [[dark-patterns]] — Definition and taxonomy of deceptive design patterns
- [[automated-shopping]] — AI agent-mediated consumer transactions
- [[CMA]] — UK competition and consumer authority
- [[Consumer Protection from Unfair Trading Regulations 2008]] — UK regulatory framework
- [[FTC]] — US Federal Trade Commission findings on deceptive design
- [[subscription-traps]] — Ongoing subscription and cancellation harms
- [[deceptive-steering]] — Algorithmic and UI-based consumer steering
