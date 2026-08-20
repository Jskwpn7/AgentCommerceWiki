---
title: "SimPersona: Learning Discrete Buyer Personas from Raw Clickstreams for Grounded E-Commerce Agents"
type: summary
date: 2026-08-03
source_url: https://arxiv.org/abs/2605.14205
authors:
  - Zahra Zanjani Foumani
  - Alberto Castelo
  - Shuang Xie
  - Ted Chaiwachirasak
  - Han Li
  - Lingyun Wang
tags:
  - persona
  - clickstream
  - user-simulation
  - vq-vae
  - buyer-types
  - population-level
  - e-commerce
summary: |
  Introduces SimPersona, a framework learning discrete buyer types from historical clickstreams using behavior-aware VQ-VAE. Achieves 78% conversion-rate alignment with real buyers across 8.37M buyers and 42 storefronts. Outperforms baseline with 8x more parameters. Releases open-source data pipeline for converting raw e-commerce event logs into agent-training traces.
concepts:
  - buyer-persona
  - clickstream-analysis
  - vq-vae
  - user-simulation
  - population-level
---

## Overview

SimPersona addresses the problem of LLM-based web agents collapsing to a single "average buyer" policy by learning discrete buyer types from raw clickstream data.

## Key Contributions

1. **Behavior-Aware VQ-VAE**: Induces discrete buyer-type space capturing statistical structure of real buyer behavior
2. **Persona Tokens**: Maps each learned buyer type to dedicated persona tokens in LLM vocabulary
3. **Fine-Tuning**: Agent fine-tuned with persona tokens on real browsing traces
4. **Open-Source Pipeline**: Converts raw e-commerce event logs into buyer representations and agent-training traces

## Key Findings

- 78% conversion-rate alignment with real buyers across 8.37M buyers
- Evaluated on 42 held-out live storefronts
- Exhibits interpretable behavioral variation across buyer types
- Outperforms baseline with 8x more parameters on goal-oriented shopping tasks
- No retraining or store-specific prompt engineering required

## Implications

For consumer protection, this research enables more realistic testing of shopping agents by simulating diverse buyer populations. The 78% alignment shows promise but also reveals gaps in current agent modeling. The open-source pipeline could be valuable for testing agent fairness across different buyer personas.

## Citations

- Paper: [[arXiv:2605.14205]](https://arxiv.org/abs/2605.14205)
