---
title: "Learning from Online User Feedback for Shopping Agents (LOFA)"
created: 2026-08-17
updated: 2026-08-17
type: summary
tags: [agentic-ai, academic, digital-platforms, retail, data-abuse, digital-consumer]
sources: ["https://arxiv.org/abs/2608.11604"]
confidence: high
---

# Learning from Online User Feedback for Shopping Agents (LOFA)

**Paper:** arXiv:2608.11604 — "Learning from Online User Feedback for Shopping Agents"
**Authors:** Haobo Zhang, Kelong Mao, Sulong Xu, Simiu Gu, Zhicheng Dou (NUS and industry collaborators)
**Published:** 12 August 2026
**Primary Source:** [arxiv.org/abs/2608.11604](https://arxiv.org/abs/2608.11604)

## Overview

LLM-based shopping agents are now deployed in real-world e-commerce platforms, where they generate large volumes of user-interaction logs. Most existing training approaches rely on **offline** supervision signals — user-item interaction histories or synthetic preference data — while ignoring the richer supervision embedded in users' natural **conversational** feedback. That feedback is also heterogeneous, sparse, and noisy, making it hard to convert into reliable learning signals automatically.

The paper proposes **LOFA** (Learning from Online Feedback for Agents), a framework that lets shopping agents learn directly from real online interaction logs without human annotation.

## Mechanism

LOFA combines two complementary objectives:

1. **Reinforcement learning over verifiable purchase outcomes** — the agent is rewarded on purchase outcomes that can be objectively checked, capturing collaborative behavioural patterns (what tends to lead to a completed, satisfactory purchase).
2. **Feedback-aware on-policy distillation** — the framework identifies users' in-dialogue directives (natural-language corrections, preferences, constraints stated mid-conversation) and converts them into dense token-level supervision, capturing user-specific preferences.

The two objectives jointly capture collaborative behaviour and individual preference. Experiments on real-world e-commerce logs show LOFA consistently improves recommendation quality, response helpfulness, and user-satisfaction alignment over strong baselines.

## Consumer Harm Implications

- **Preference drift via third-party data.** The agent's purchasing policy is optimised on *other users'* interaction logs. This is a structural source of recommendation bias and preference drift that the individual consumer cannot inspect or contest.
- **First-party intent data monopoly.** Continuous learning from live shopping logs creates a large, proprietary first-party dataset on consumer intent — a data-concentration and [[gdpr-data-minimisation]] vector.
- **Opaque learning loop.** As the agent improves from opaque log-derived signals, the reasoning behind a specific recommendation becomes harder to audit, complicating ex-post complaint handling.
- **UK angle.** Feeds the CMA's "monitor and refine" expectation: autonomous agent learning loops make it harder for consumers to understand or challenge a recommendation after the fact, and harder for regulators to attribute a harmful steering decision to a specific input.

## Relevance to UK Consumer Harms

This paper documents the *execution layer* of shopping agents improving from consumer behaviour at scale. It directly extends [[ai-shopping-agents]]: the competence gains that make delegated purchasing more reliable also deepen the opacity and data asymmetries that underpin recommendation-manipulation and misaligned-incentive harms. See [[conflict-of-interest-in-llm-deployment]] for the provider-side commercial incentives that log-derived optimisation can reinforce.

## Cross-References

- [[ai-shopping-agents]] — live-log training improves the shopping-agent execution layer
- [[conflict-of-interest-in-llm-deployment]] — optimised recommendation surfaces amplify commercial steering incentives
- [[recommendation-manipulation]] — opaque log-derived optimisation as a manipulation surface
- [[gdpr-data-minimisation]] — first-party intent data concentration
- [[agentic-commerce-research-2026]] — shopping-agent research digest

## References

1. arXiv:2608.11604 — *Learning from Online User Feedback for Shopping Agents*
