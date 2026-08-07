---
source_url: https://arxiv.org/abs/2310.11324
title: Quantifying Language Models' Sensitivity to Spurious Features in Prompt Design
ingested: 2026-07-13
sha256: arxiv-2310.11324
tags: [llm-evaluation, prompt-engineering, format-sensitivity, reproducibility, methodology]
---
# Quantifying Language Models' Sensitivity to Spurious Features in Prompt Design (arXiv:2310.11324)

## Source
- **Authors**: Melanie Sclar¹, Yejin Choi¹², Yulia Tsvetkov¹, Alane Suhr³
- **Affiliations**: ¹University of Washington, ²Allen Institute for AI, ³UC Berkeley
- **Published**: ICLR 2024 (Camera Ready)
- **arXiv**: 2310.11324v2 [cs.CL]

## Abstract
As large language models (LLMs) are adopted as a fundamental component of language technologies, it is crucial to accurately characterize their performance. Choices in prompt design can strongly influence model behavior. This work focuses on LLM sensitivity to a quintessential class of meaning-preserving design choices: **prompt formatting**.

## Key Findings
- Several widely used open-source LLMs are extremely sensitive to subtle changes in prompt formatting in few-shot settings
- Performance differences of up to **76 accuracy points** when evaluated using LLaMA-2-13B
- Sensitivity remains even when increasing model size, number of few-shot examples, or performing instruction tuning
- Average variance: ~10 accuracy points across 50+ tasks and several models
- Format performance only weakly correlates between models

## Format Spread (selected examples from the paper)
- LLaMA-2-7B on StereoSet task: 0.036 accuracy at one format, 0.804 at another (spread of 0.768)
- GPT-3.5: spread up to 56 accuracy points across 320 formats and 53 tasks
- Cost: under $10 USD per task to evaluate
- Median spread: 6.4 accuracy points

## FORMAT SPREAD
The authors propose FORMAT SPREAD, an algorithm that:
- Rapidly evaluates a sampled set of plausible prompt formats for a given task
- Reports the interval of expected performance without accessing model weights
- Uses Bayesian optimization to efficiently explore the space of prompt formats
- Can be applied to API-gated models (e.g., GPT-3.5)
- Cost: under $10 USD per task

## Prompt Grammar
The paper defines a grammar for generating semantically equivalent prompt formats:
- Basic fields: `B1(d, s, f) := f(d)s<text>` where d=descriptor, s=separator, f=casing function
- Joined fields: `B2(X1, ..., Xn, c) := X1 c ... cXn`
- Enumeration: `B3(d, j1, ..., jn, s1, s2, c, f1, f2)`
- Two formats are equivalent if they represent the same rule, same descriptors, and same sub-elements

## Implications
- Research evaluating LLMs with prompting-based methods should report a range of performance across plausible prompt formats, not just one format
- Methodological validity of comparing models with an arbitrarily chosen, fixed prompt format is questionable
- Performance variance across formats may confound conclusions about model improvements
- User experience may be negatively affected if users inadvertently choose formats the LLM performs poorly on

## Key Results
- Separability of continuous prompt embeddings correlates with spread observed in task performance
- Individual feature choices (separator, spacing, casing) contribute significantly to performance variance
