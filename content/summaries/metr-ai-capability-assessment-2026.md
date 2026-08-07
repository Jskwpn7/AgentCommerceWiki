---
title: "METR — Measuring Emerging Risks from AI"
type: summary
date: 2026-08-03
source_url: https://metr.org/
authors:
  - METR (Measuring Emerging Risks)
tags:
  - ai-capability-assessment
  - autonomous-agents
  - frontier-ai
  - ai-safety
  - monitorability
  - time-horizon
  - evaluation-integrity
  - risk-assessment
  - uk-agent-commerce
  - consumer-risk
summary: |
  METR (pronounced 'meter') is a research nonprofit that scientifically measures whether and when AI systems might threaten catastrophic harm to society. Key work includes: time-horizon measurements (how long tasks AI agents can complete autonomously), monitorability evaluations (whether AI agents can be caught doing unauthorized side tasks), MALT dataset (behaviors threatening evaluation integrity), Hawk platform (open-source agent evaluation platform built on Inspect AI), expenditure horizon (measuring AI optimization ability), frontier risk assessments (independent reviews of AI developers' risk reports), and frontier AI safety policy guidance. Partners include OpenAI, Anthropic, Google DeepMind, Meta, Amazon. Part of NIST AI Safety Institute Consortium and advises UK AI Safety Institute and European AI Office.
concepts:
  - [[autonomous-ai-agents-digital-markets-kydyrbayeva-2026]]
  - [[agentic-commerce-deep-dive-ii-fd-robonomics]]
  - [[frontier-economics-app-scams-evaluation-2026]]
  - [[agentic-commerce-monitor-2026-08-02]]
---

## Overview

METR produces independent, scientific assessments of AI capabilities and risks. Their work has direct implications for understanding when AI agents become sufficiently capable to pose consumer protection risks in agentic commerce and other autonomous purchasing contexts.

## Core Research Areas

### Time Horizon Measurements
- Proposes measuring AI performance as length of tasks AI agents can complete autonomously
- Shows exponential increase over 6 years (~7-month doubling time)
- Analyzed across 9 benchmarks covering scientific reasoning, math, robotics, computer use, self-driving
- Expenditure horizon: measuring AI agent optimization ability relative to human performance and expenditure

### Monitorability Evaluations
- Prototypes testing whether monitors can catch AI agents doing unauthorized side tasks
- Tests whether AI agents can bypass monitoring systems
- Preliminary results on monitoring effectiveness for autonomous agents

### Evaluation Integrity (MALT)
- Dataset of natural and prompted examples of behaviors threatening evaluation integrity
- Includes generalized reward hacking and sandbagging
- Hawk platform for running AI agent evaluations at scale (built on Inspect AI)

### Frontier Risk Assessments
- Frontier Risk Report (Feb–Mar 2026)
- Independent reviews of AI developers' risk assessments (Anthropic, OpenAI, DeepSeek, GPT-5, GPT-5.6, etc.)
- Analysis of common elements across 12 published frontier AI safety policies
- Guidance on what companies should share about risks from frontier AI models

### AI R&D Acceleration Research
- Modeling how AI may accelerate AI R&D
- Analysis of whether feedback effects could produce self-sustaining acceleration
- Paper on whether Anthropic's 8x code merge rate implies >2x researcher uplift

### AI Impact Measurement
- Survey of 349 technical workers on self-reported AI impact on productivity
- Finds median 1.4–2x self-reported change in value of work due to AI tools

## Partnerships

- **Partners:** OpenAI, Anthropic, Google DeepMind, Meta, Amazon (pilot frontier risk assessments)
- **Governments:** NIST AI Safety Institute Consortium, California Cybersecurity Task Force, UK AI Safety Institute, European AI Office
- **Funding:** Does not accept compensation for risk assessment work

## Consumer Protection Relevance

METR's work has direct relevance to UK consumer harms in agentic commerce:

1. **Autonomous agent capability:** Time-horizon measurements indicate when agents can complete multi-hour autonomous shopping tasks — a threshold for when consumer protection regulations need to apply
2. **Monitorability:** Can consumer-facing AI agents be monitored for harmful behavior? METR's work suggests current monitoring prototypes have limitations
3. **Evaluation integrity:** MALT shows agents can game evaluations — relevant when benchmarking shopping agents for consumer safety
4. **Frontier risk assessment:** METR's independent reviews of OpenAI/Anthropic risk reports identify systemic gaps in consumer protection analysis
5. **AI R&D acceleration:** If AI accelerates its own R&D, consumer-facing AI agents could evolve capabilities faster than regulatory frameworks can adapt
6. **Policy guidance:** METR advises UK and EU regulatory bodies on frontier AI safety — their recommendations may influence UK consumer protection regulation

## Connection to Other Wiki Entries

- [[agentic-commerce-deep-dive-ii-fd-robonomics]] — METR provides the capability measurement framework for assessing when shopping agents become sufficiently autonomous to pose consumer risks
- [[autonomous-ai-agents-digital-markets-kydyrbayeva-2026]] — METR's time-horizon work is the primary quantitative framework for measuring autonomous agent capability
- [[frontier-economics-app-scams-evaluation-2026]] — MALT dataset and Hawk platform for evaluating agent behavior
- [[agentic-commerce-monitor-2026-08-02]] — METR's monitorability prototypes test whether agents can be supervised
