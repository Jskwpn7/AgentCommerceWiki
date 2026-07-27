---
title: Quantifying LLMs' Sensitivity to Spurious Features in Prompt Design (Sclar et al., ICLR 2024)
created: 2026-07-13
updated: 2026-07-13
type: summary
tags: [llm-evaluation, prompt-engineering, format-sensitivity, reproducibility, methodology]
sources: [raw/papers/arxiv-2310.11324-sclar-llm-format-sensitivity.md]
---
# LLM Sensitivity to Prompt Formatting

**Source**: [[arxiv-2310.11324-sclar-llm-format-sensitivity|Raw paper]] • **Authors**: Sclar, Choi, Tsvetkov, Suhr (UW, AI2, UC Berkeley) • **Published**: ICLR 2024

## Overview
Widely-used open-source LLMs are extremely sensitive to subtle formatting changes in few-shot prompts, with performance differences of up to **76 accuracy points** (LLaMA-2-13B) and ~10 points on average across 50+ tasks. This sensitivity persists despite increasing model size, more few-shot examples, or instruction tuning.

## Key Contributions
- **FORMAT SPREAD**: Bayesian optimization algorithm to efficiently explore prompt format space (~$10/task, no model weight access required)
- **Prompt equivalence grammar**: Formal grammar defining semantically equivalent prompt formats
- **Cross-model analysis**: Format performance only weakly correlates between models — fixed formats confound model comparisons
- **Embedding analysis**: Separability of continuous prompt embeddings correlates with performance spread

## Method
1. Construct grammar of plausible prompt formats (casing, separators, spacing, enumeration styles)
2. Define semantic equivalence: same rule application, descriptors, sub-elements
3. Cast format exploration as bandit problem → Bayesian optimization
4. Evaluate on 50+ Super-NaturalInstructions tasks

## Relevance
LLM evaluation methodology, reproducibility crisis, prompt engineering best practices, AI safety evaluation
