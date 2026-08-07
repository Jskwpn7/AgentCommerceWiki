---
title: "OmniThink: Expanding Knowledge Boundaries in Machine Writing through Thinking"
authors: Zekun Xi, Wenbiao Yin, Jizhan Fang, Jialong Wu, Runnan Fang, Ningyu Zhang, Yong Jiang, Pengjun Xie, Fei Huang, Huajun Chen
date: 2025-01-16
arxiv: 2501.09751
source_url: https://arxiv.org/abs/2501.09751
extraction: arxiv HTML (2501.09751v4)
---

# OmniThink: Expanding Knowledge Boundaries in Machine Writing through Thinking

**Authors:** Zekun Xi (1,2), Wenbiao Yin (2), Jizhan Fang (1), Jialong Wu (2), Runnan Fang (1,2), Ningyu Zhang (1,3), Yong Jiang (2), Pengjun Xie (2), Fei Huang (2), Huajun Chen (1,3)
**Affiliations:** 1 Zhejiang University, 2 Tongyi Lab / Alibaba Group, 3 Zhejiang Key Laboratory of Big Data Intelligent Computing
**Published:** arXiv 2501.09751 (January 16, 2025); EMNLP 2025 acceptance
**arXiv:** https://arxiv.org/abs/2501.09751
**Code:** https://github.com/zjunlp/OmniThink

## Abstract

Machine writing with large language models often relies on retrieval-augmented generation. However, these approaches remain confined within the boundaries of the model's predefined scope, limiting the generation of content with rich information. Specifically, vanilla-retrieved information tends to lack depth, novelty, and suffers from redundancy, which negatively impacts the quality of generated articles, leading to shallow, unoriginal, and repetitive outputs. To address these issues, we propose OmniThink, a slow-thinking machine writing framework that emulates the human-like process of iterative expansion and reflection. The core idea behind OmniThink is to simulate the cognitive behavior of learners as they slowly deepen their knowledge of the topics. Experimental results demonstrate that OmniThink improves the knowledge density of generated articles without compromising metrics such as coherence and depth. Human evaluations and expert feedback further highlight the potential of OmniThink to address real-world challenges in the generation of long-form articles.

## Introduction

### Problem: Limitations of Existing Approaches

Early attempts use Retrieval Augmented Generation (RAG) to expand new information on a given topic. However, vanilla RAG relies on a fixed set of search strategies, which lack diversity in generation, preventing thorough exploration and resulting in fragmented understanding.

STORM and Co-STORM propose role-play approaches to expand perspective — collecting information from multiple perspectives, thus broadening the information space. Yet these approaches still operate within the scope of one's own role, making it difficult to generate deep content and break through knowledge boundaries.

**Key failures:**
- Retrieved information lacks depth, novelty, and suffers from redundancy
- Generated articles are shallow, repetitive, and unoriginal
- Existing systems cannot break through their own knowledge boundaries

### Human Writing as Inspiration

According to reflective practice theory (Osterman, 1990), human writers continuously reflect on previously gathered information and personal experiences, allowing them to reorganize, filter, and refine their cognitive framework. This prompts iterative adjustment of writing direction and mental pathways, ultimately generating more profound, nuanced and original content (Bruce, 1978).

### Proposed Solution: OmniThink

OmniThink emulates the human slow-thinking process to expand knowledge boundaries through:
1. **Information Tree** — simulates the process of collecting and structuring knowledge
2. **Conceptual Pool** — simulates the evolving cognitive framework

These components are iteratively enriched through expansion and reflection. Once a diverse set of information has been gathered and structured, OmniThink transitions to outline construction and article generation.

### Contributions

1. Proposed OmniThink, a novel writing framework that emulates human slow-thinking process
2. Proposed Knowledge Density (KD) metric measuring proportion of useful information in an article
3. Analyzed challenges of current long-form generation methods from a novel knowledge boundary perspective

## Background

### Task Definition: Open-Domain Long-Form Generation

Given an input topic T, the target is to generate a long article A. Standard approach involves two major steps:
1. Use search engine S to retrieve information I = S(T) related to topic T
2. Generate outline O = Generate(I, T) based on retrieved information
3. Generate article A = Generate(O, I) using outline

### Revisiting Previous Methods

- **Co-STORM:** User-participatory roundtable discussion in step (i) to enhance diversity of retrieved information
- **STORM:** Questioning mechanism to improve quality and relevance of generated outlines in step (ii)

Persistent challenge: generated content frequently suffers from redundancy and lacks novelty.

**Example case (STORM with GPT-4o):** "AlphaFold was developed by DeepMind" appears multiple times in generated article, when it could be stated only once in initial mention.

### Limitation Analysis: Boundary Perspective

Two knowledge boundary issues:
1. **Knowledge Information Boundary:** When retrieved content contains limited factual knowledge, available information for generating text is constrained → leads to redundancy
2. **Knowledge Cognition Boundary:** Even when large amount of non-redundant factual knowledge is retrieved, model cannot organize and structure knowledge as humans do → results in limited usable information and consequently redundancy

Similarly, lack of novelty attributed to either failure to collect novel knowledge OR inability to use retrieved novel knowledge effectively.

### Comparative Features

| Feature | STORM | Co-STORM | OmniThink |
|---|---|---|---|
| Dynamic retrieval | ✗ | ✗ | ✓ |
| Structured memory | ✗ | ✓ | ✓ |
| Reflective thinking | ✗ | ✗ | ✓ |

## OmniThink Framework

### Information Acquisition

While LLMs have learned vast amounts of human knowledge through training, they may struggle to capture the spontaneous processes by which humans organize useful information and update cognitive frameworks when learning new knowledge.

Two novel components:
1. **Information Tree (T)** — hierarchical organization of retrieved knowledge
2. **Conceptual Pool (P)** — evolving representation of LLM's understanding

#### Initialization

Interactive process begins with initialization of root node based on input topic T. OmniThink uses search engines (Google/Bing) to retrieve information related to T, using retrieved information to construct initial root node Nr. Initial information in Nr is analyzed and extracted to form preliminary conceptual pool P0, serving as foundational cognition and guiding subsequent expansion.

#### Expansion of Information Tree

At time step m, OmniThink analyzes all leaf nodes Lm = {N0, N1, ..., Nn} of information tree Tm. For nodes needing expansion, OmniThink uses current conceptual pool Pm to identify areas for deeper expansion.

For each leaf node Ni, OmniThink generates k_Ni sub-nodes: SUB(Ni) = {S0, S1, ..., S_k_Ni}. Each sub-node represents a specific aspect or subtopic identified from current node Ni. For each sub-node, OmniThink retrieves relevant information and stores it within the node, subsequently adding sub-nodes to updated tree T_{m+1}:

```
T_{m+1} = Combine(T_m, SUB(N_0), ..., SUB(N_n))
```

This targeted retrieval ensures comprehensive and in-depth knowledge for each sub-node, enriching the hierarchical structure.

#### Reflection of Conceptual Pool

OmniThink reflects newly retrieved information in all leaf nodes L_{m+1} = {N0, ..., Nn} to update cognitive framework (conceptual pool). Information from leaf nodes is analyzed, filtered, and synthesized to distill core insights I_{m+1} = {INS_0, ..., INS_n}. These distilled insights are incorporated into conceptual pool Pm:

```
P_{m+1} = Merge(I_{m+1}, P_m)
```

Using updated conceptual pool P_{m+1}, OmniThink further expands leaf nodes of the information tree iteratively.

The iterative cycle of expansion and reflection continues until sufficient information is acquired or predefined maximum retrieval depth K is reached. During this process, as Information Tree and Conceptual Pool are continuously expanded, both Information Boundary and Cognition Boundary are progressively expanded.

### Concept-Guided Outline Structuring

The outline determines content direction, structural hierarchy, and logical progression. OmniThink first creates draft outline O_D, then asks the LLM to refine and link content from the conceptual pool P, ultimately forming final outline:

```
O = Polish(O_D, P)
```

### Article Composition

After completing outline O, writing proceeds for each section S. LLM works in parallel for each section. Section content generation uses section titles and hierarchical subsections to retrieve the most relevant K documents from the information tree via Sentence-BERT embeddings. After obtaining relevant information, LLM generates section content with citations. Once all sections generated, they are concatenated into complete draft article, then LLM processes to remove redundant information and form final article.

## Experiments

### Dataset and Baseline

**Evaluation dataset:** WildSeek (Jiang et al., 2024) — 100 data points across 24 different domains, each consisting of specific topic and user intent.

**Baselines:** RAG, oRAG, STORM, Co-STORM (reproduced from STORM repository)

### Knowledge Density Metric

Previous works focus on relevance and correctness but do not consider conciseness and redundancy. OmniThink introduces **Knowledge Density (KD)**:

```
KD = Σ_{i=1}^{N} U(k_i) / L
```

Where N is total number of atomic knowledge units, U(k_i) indicates whether i-th unit information is unique, and L is total text length.

Low KD content causes reader fatigue, frustration, or disengagement. High-density content provides streamlined experience enabling efficient knowledge transfer.

### Evaluation Setup

- **Automatic scoring:** Prometheus2 — scores articles 0-5 on Relevance, Breadth, Depth, Novelty
- **Information diversity:** cosine similarity differences between web pages
- **Knowledge density:** as defined above
- **Human evaluation:** detailed evaluation (see Appendix C)

### Results (GPT-4o backbone)

| Method | Rubric | Relevance | Breadth | Depth | Novelty | Info Diversity | Knowledge Density |
|---|---|---|---|---|---|---|---|
| RAG | 4.65 | 4.55 | 4.59 | 4.22 | 0.1042 | 22.11 | — |
| oRAG | 2.38 | 3.63 | 2.56 | 2.27 | 0.0963 | 19.70 | — |
| STORM | 4.34 | 4.21 | 4.21 | 3.80 | 0.6342 | 19.33 | — |
| Co-STORM | 4.37 | 4.66 | 4.65 | 3.89 | 0.6285 | 19.53 | — |
| **OmniThink** | **4.77** | **4.71** | **4.66** | **4.31** | **0.6642** | **22.31** | **22.31** |

### Qwen-Plus backbone (similar pattern)

OmniThink consistently outperforms all baselines across all metrics when using Qwen-Plus as backbone.

### Reasoning Model backbone (O1-preview)

Similar pattern — OmniThink leads on all metrics when using reasoning models.

### Robustness to Model Degradation

Replacing expansion/reflection models from Qwen-Plus to Qwen2.5-7b-instruct shows measurable decline in evaluation metrics, demonstrating that expansion/reflection quality is critical.

## Appendices

### Appendix G: Feature Comparison

- **Dynamic retrieval:** OmniThink dynamically adjusts retrieval based on problem difficulty, constantly reflecting on whether further retrieval is necessary. STORM/Co-STORM rely on max conversation count.
- **Structured memory:** OmniThink records retrieved pages in progressive knowledge manner AND uses conceptual pool for understanding changes. Co-STORM only records mind map during conversation.
- **Reflective thinking:** OmniThink continuously reflects on retrieved content to fill conceptual pool. STORM/Co-STORM do not reflect.

### Appendix H: Effectiveness of Knowledge Density

Experiment: constructed 50 unique atomic facts → asked GPT-4o to generate 500-word article → gradually reduced facts while keeping length constant → invited 3 human + 3 LLM evaluators to score.

| Evaluator | 20 Facts | 30 Facts | 40 Facts | 50 Facts |
|---|---|---|---|---|
| GPT-4o | 1.0 | 2.0 | 3.0 | 3.6 |
| DeepSeek-R1 | 1.0 | 2.6 | 2.8 | 3.6 |
| O3-mini-high | 1.0 | 2.4 | 3.2 | 3.4 |
| Humans | 1.0 | 2.1 | 3.1 | 3.8 |

Result: all evaluators consistently prefer higher factual density, confirming KD's validity as a quality metric.

### Appendix J: Decision Process of Expansion

At each step: check if tree reached max depth. If not, LLM decides next steps for each leaf node. If expansion needed, model generates sub-node categories and retrieval keywords. Otherwise, produces no output (node is complete). Sub-node categories and keywords extracted via regex and used to query search engines. Retrieved content forms new information nodes.

### Appendix K: Clarification of Reflection

Reflection = LLM reflects on retrieved information based on current Conceptual Pool, evaluating which parts can enrich existing pool. Usable information extracted as insights and added to Conceptual Pool.

## Case Studies

### AGI Generated by OmniThink with GPT-4o

Language is more concise compared to other methods, contains more information per unit of text length.

### AGI Generated by OmniThink with DeepSeek-R1

Uses reasoning model — cites significantly more content per chapter, indicating improved ability to utilize information through reflection.

## Citation

```bibtex
@misc{xi2025omnithinkexpandingknowledgeboundaries,
  title={OmniThink: Expanding Knowledge Boundaries in Machine Writing through Thinking},
  author={Zekun Xi and Wenbiao Yin and Jizhan Fang and Jialong Wu and Runnan Fang and Ningyu Zhang and Jiang Yong and Pengjun Xie and Fei Huang and Huajun Chen},
  year={2025},
  eprint={2501.09751},
  archivePrefix={arXiv},
  primaryClass={cs.CL},
  url={https://arxiv.org/abs/2501.09751},
}
```
