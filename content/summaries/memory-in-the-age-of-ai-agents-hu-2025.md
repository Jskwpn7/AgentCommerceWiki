---
title: "Memory in the Age of AI Agents: A Survey"

created: 2026-05-20
updated: 2026-05-20
type: summary
tags: [academic, research]
sources: [raw/papers/memory-in-the-age-of-ai-agents-2025.md]
confidence: high
---

# Memory in the Age of AI Agents: A Survey — Forms, Functions and Dynamics

## Paper Details

| Field | Value |
|-------|-------|
| **Authors** | Yuyang Hu, Shichun Liu, Yanwei Yue, Guibin Zhang et al. (46 authors) |
| **Affiliations** | NUS, Renmin University, Fudan, Peking, NTU, Tongji, UCSD, HKUST(GZ), Griffith, Georgia Tech, OPPO, Oxford |
| **Published** | Submitted 15 Dec 2025; revised 13 Jan 2026 (v2) |
| **arXiv** | [2512.13564](https://arxiv.org/abs/2512.13564) [cs.CL; cs.AI] |
| **Length** | 76 pages |
| **GitHub** | https://github.com/Shichun-Liu/Agent-Memory-Paper-List |

## Summary

This is a comprehensive 76-page survey mapping the rapidly expanding field of agent memory — the mechanisms by which foundation-model-based AI agents store, manage, and retrieve information across interactions. The paper argues that existing taxonomies (long/short-term, declarative/episodic/semantic) are insufficient for the diversity of contemporary agent memory systems, and proposes a unified three-dimensional taxonomy organized around **forms**, **functions**, and **dynamics**.

### The Forms–Functions–Dynamics Taxonomy

**Forms (what carries memory):**

1. **Token-level memory** — information encoded in the token sequence (context window). Subdivided into flat (1D), planar (2D), and hierarchical (3D) structures.

2. **Parametric memory** — information internalized into model parameters. Divided into internal (fine-tuning, prompt-tuning) and external (knowledge bases, retrieval systems).

3. **Latent memory** — information encoded in the model's hidden states or learned representations. Includes generation (memory generation during generation), reuse (memory reuse across tasks), and transform (memory transformation).

**Functions (why agents need memory):**

1. **Factual memory** — records knowledge from agent interactions with users and the environment. Subdivided into user factual memory (user preferences, profiles) and environment factual memory (environment state, rules).

2. **Experiential memory** — incrementally enhances problem-solving capabilities through task execution. Includes case-based, strategy-based, skill-based, and hybrid memory.

3. **Working memory** — manages workspace information during individual task instances. Subdivided into single-turn and multi-turn working memory.

**Dynamics (how memory operates):**

1. **Memory formation** — semantic summarization, knowledge distillation, structured construction, latent representation, parametric internalization.

2. **Memory evolution** — consolidation, updating, forgetting.

3. **Memory retrieval** — retrieval timing and intent, query construction, retrieval strategies, post-retrieval processing.

### Key Distinctions

The paper formalizes agent memory and distinguishes it from related concepts:

- **Agent memory vs. LLM memory**: Agent memory is external to model parameters and designed for continual adaptation; LLM memory refers to information encoded within or directly affecting model weights.
- **Agent memory vs. RAG**: RAG retrieves from a static knowledge base; agent memory is dynamic, evolving through interaction and supporting both inside-trial and cross-trial memory.
- **Agent memory vs. context engineering**: Context engineering optimizes prompt composition; agent memory is a persistent, evolving state that survives across sessions.

### Seven Emerging Research Frontiers

1. **Memory retrieval vs. memory generation** — moving from retrieval-based to generation-based memory
2. **Automated memory management** — transitioning from hand-crafted to automatically constructed memory systems
3. **Reinforcement learning meets agent memory** — RL internalizing memory management abilities
4. **Multimodal memory** — integrating vision, audio, and other modalities
5. **Shared memory in multi-agent systems** — moving from isolated memories to shared cognitive substrates
6. **Memory for world models** — using memory to build and maintain models of the environment
7. **Trustworthy memory** — addressing security, privacy, and reliability concerns

### Resources

The paper compiles representative benchmarks for memory/lifelong/self-evolving agents and catalogues open-source frameworks including Zep, AriGraph, Ella, M+, MemoryLLM, and others.

## Relevance to UK Consumer Harms

While this is a general technical survey rather than a consumer harms paper, several dimensions are relevant:

**Memory architectures shape consumer protection risks.** The paper's formalization of agent memory (Section 2) establishes the technical basis for understanding how autonomous agents accumulate information about users, learn preferences over time, and persistently adapt — all of which underpin the [[ai-agents-in-markets]] framework. Agents with robust factual memory (Section 4.1) can build detailed user profiles that enable preference distortion at scale.

**Multi-agent shared memory is a regulatory blind spot.** The frontier on shared memory in multi-agent systems (Section 7.5) describes agents sharing "cognitive substrates" — this directly relates to [[systemic-fragility-in-ai-economies]], as shared memory between agents deployed by competing firms could enable implicit coordination that is opaque to regulators.

**Trustworthiness memory (Section 7.7) is underdeveloped.** The paper identifies trustworthiness as an emerging frontier — the fact that this is *emerging* rather than solved is itself a consumer protection concern. Agents with memory capabilities that cannot be audited, forgotten, or corrected pose novel risks for [[conflict-of-interest-in-llm-deployment]].

**Memory automation (Section 7.2) has implications for consumer control.** If memory formation and evolution become fully automated, consumers may have no visibility into what information agents collect, retain, or use — a significant gap for regulatory frameworks like GDPR's right to erasure and [[user-welfare-vs-company-incentive]].

## Connection to Other Wiki Entries

- [[ai-agents-in-markets]] — The memory architectures surveyed here are the technical mechanisms through which AI agents accumulate market intelligence, learn user preferences, and persistently adapt — core drivers of the consumer harms described in this concept page.
- [[systemic-fragility-in-ai-economies]] — Shared memory between agents (Section 7.5) provides the technical substrate for correlated behavior and opaque coordination across firm boundaries.
- [[agentic-ai-workflows-guide-bandara-2025]] — A companion technical survey; while Bandara focuses on engineering best practices, Hu et al. provides the comprehensive taxonomy of memory systems that underpin those workflows.
- [[wu-2026-ads-in-ai-chatbots]] — Both papers document the growing gap between what AI agents *can* do (with memory systems) and whether those capabilities are aligned with consumer welfare.
- [[conflict-of-interest-in-llm-deployment]] — The paper's trustworthiness frontier (Section 7.7) directly addresses how memory systems amplify existing conflicts between LLM provider incentives and user welfare.
