---
title: "Intelligent Virtual Assistants with LLM-based Process Automation"
type: summary
date: 2026-08-03
source_url: https://arxiv.org/abs/2312.06677
authors:
  - Yanchu Guan
  - Dong Wang
  - Zhixuan Chu
  - Shiyu Wang
  - Feiyue Ni
  - Ruihua Song
  - Longfei Li
  - Jinjie Gu
  - Chenyi Zhuang
tags:
  - virtual-assistants
  - llm-pa
  - process-automation
  - mobile-apps
  - task-execution
  - natural-language
  - alipay
summary: |
  Introduces LLMPA (LLM-based Process Automation), a virtual assistant that performs multi-step operations within mobile apps based on high-level natural language requests. Modules: instruction decomposition, description generation, interface element detection, action prediction, error checking. First real-world deployment of LLM-based virtual assistant in widely used mobile app (Alipay) with hundreds of millions of users.
concepts:
  - [[virtual-assistants]]
  - [[llm-pa]]
  - [[process-automation]]
  - [[mobile-apps]]
  - [[task-execution]]
---

## Overview

While Siri, Alexa, and Google Assistant are ubiquitous, they struggle with multi-step instructions. LLMPA uses LLMs to enable end-to-end automation of complex mobile app operations.

## Key Contributions

1. **LLMPA Architecture**: End-to-end system for parsing instructions, reasoning about goals, and executing actions
2. **Five Core Modules**:
   - Instruction decomposition
   - Description generation
   - Interface element detection
   - Action prediction
   - Error checking
3. **Production Deployment**: First LLM-based virtual assistant deployed in Alipay (hundreds of millions of users)
4. **Multi-Step Task Completion**: Demonstrates complex mobile operations via natural language

## Architecture

```
User Request → Instruction Decomposition → Description Generation
                                    ↓
                       Interface Element Detection
                                    ↓
                          Action Prediction → Error Checking
```

## Implications for Consumer Protection

- **Automated Actions**: Users may not understand what actions are being executed on their behalf
- **Financial Risk**: Multi-step operations in financial apps (Alipay) could lead to unintended transactions
- **Privacy**: Virtual assistant has access to full mobile app ecosystems and user data
- **Accountability**: When automated actions cause harm, difficulty determining responsibility
- **Scale Impact**: Hundreds of millions of users with automated app operations
- **Transparency**: Users may not realize assistant is making complex decisions, not just executing commands

## Citations

- Paper: [[arXiv:2312.06677]](https://arxiv.org/abs/2312.06677)
