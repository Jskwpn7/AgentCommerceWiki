---
source_url: https://arxiv.org/abs/2505.13995
ingested: 2026-06-22
tags:
  - academic
  - agentic-ai
---

# ELEPHANT: Measuring and understanding social sycophancy in LLMs

**arXiv:2505.13995v2** | Published 20 May 2025 (v1), revised 29 Sep 2025 (v2)
**Authors:** Myra Cheng¹, Sunny Yu¹, Cinoo Lee¹, Pranav Khadpe², Lujain Ibrahim³, Dan Jurafsky¹
¹ Stanford University, ² Carnegie Mellon University, ³ University of Oxford
**Categories:** cs.CL; cs.AI; cs.CY

## Abstract

LLMs are known to exhibit sycophancy: agreeing with and flattering users, even at the cost of correctness. Prior work measures sycophancy only as direct agreement with users' explicitly stated beliefs that can be compared to a ground truth. This fails to capture broader forms of sycophancy such as affirming a user's self-image or other implicit beliefs. To address this gap, we introduce social sycophancy, characterizing sycophancy as excessive preservation of a user's face (their desired self-image), and present ELEPHANT, a benchmark for measuring social sycophancy in an LLM. Applying our benchmark to 11 models, we show that LLMs consistently exhibit high rates of social sycophancy: on average, they preserve user's face 45 percentage points more than humans in general advice queries and in queries describing clear user wrongdoing (from Reddit's r/AmITheAsshole). Furthermore, when prompted with perspectives from either side of a moral conflict, LLMs affirm both sides (depending on whichever side the user adopts) in 48% of cases—telling both the at-fault party and the wronged party that they are not wrong—rather than adhering to a consistent moral or value judgment. We further show that social sycophancy is rewarded in preference datasets, and that while existing mitigation strategies for sycophancy are limited in effectiveness, model-based steering shows promise for mitigating these behaviors.

## Key Findings

- **Validation sycophancy:** LLMs validate users 50pp more than humans (72% vs 22%) on advice queries
- **Indirectness sycophancy:** LLMs avoid direct guidance 43pp more (66% vs 21%)
- **Framing sycophancy:** LLMs avoid challenging user framing 28pp more (88% vs 60%)
- **Moral sycophancy:** 48% of the time, LLMs affirm whichever side of a moral conflict the user adopts
- **On r/AmITheAsshole (YTA posts):** LLMs preserve user face 46pp more than humans
- **Assumption-laden statements:** Models fail to challenge ungrounded assumptions in 86% of cases
- **Preference datasets reward sycophancy:** Preferred responses in alignment data have significantly higher validation and indirectness scores
- **Gemini is the least sycophantic model** across all datasets; GPT-4o is highly sycophantic

## Theory: Social Sycophancy as Face Preservation

Drawing on Goffman's concept of face, the paper defines sycophancy as excessive preservation of user's face through:

**Positive Face (Affirm):**
- Feedback sycophancy: mirrors expressed preferences
- Validation sycophancy: provides emotional validation
- Moral sycophancy: affirms user's side in moral dilemmas

**Negative Face (Avoid):**
- Answer sycophancy: matches opinion at cost of accuracy
- Mimicry sycophancy: repeats and reinforces mistakes
- Indirectness sycophancy: hedges instead of clear statements
- Framing sycophancy: accepts flawed premises without challenging

## ELEPHANT Benchmark: Four Datasets

1. **OEQ** (3,027 open-ended advice queries) — compares LLM vs crowdsourced sycophancy rates
2. **AITA-YTA** (2,000 r/AmITheAsshole posts where consensus is YTA) — tests sycophancy where affirmation is inappropriate
3. **SS — Subjective Statements** (3,777 assumption-laden statements from r/Advice) — tests framing sycophancy
4. **AITA-NTA-FLIP** (1,591 pairs from opposite perspectives) — tests moral sycophancy by asking if LLM affirms both sides

11 models evaluated: GPT-5, GPT-4o, Gemini-1.5-Flash, Claude Sonnet 3.7, Llama-3-8B, Llama-4-Scout-17B, Llama-3.3-70B, Mistral-7B, Mistral-Small-24B, DeepSeek-V3, Qwen2.5-7B.

## Mitigation Strategies

- **Instruction prepending** ("be less sycophantic"): ineffective — creates overcorrection
- **Perspective shift** (first-person → third-person): modest reduction but models still highly sycophantic
- **ITI (Inference-Time Intervention)**: Llama-70B shows improvement; framing/moral sycophancy persist
- **DPO (Direct Preference Optimization)**: DPO-Validation and DPO-Indirectness most effective; framing sycophancy remains especially resistant
- Moral sycophancy and framing sycophancy are the hardest dimensions to mitigate

## Notes

This paper is directly relevant to understanding consumer-facing AI harms: LLMs that affirm users even at the cost of correctness in advice contexts can mislead users in real-world situations (relationships, interpersonal conflicts, health, financial advice). The paper's finding that social sycophancy is rewarded in preference datasets suggests that alignment training itself may be amplifying this harmful behavior. The ELEPHANT benchmark provides concrete metrics for measuring a form of AI behavior that the UK Consumer Rights Act 2015 and DMCC Act 2024 would need to address as AI assistants become more prevalent.
