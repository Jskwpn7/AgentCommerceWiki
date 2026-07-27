---
title: "Investigating the Impact of Dark Patterns on LLM-Based Web Agents"
created: 2026-07-24
updated: 2026-07-24
type: raw_paper
tags: [dark-patterns, llm-agents, web-security, ui-deception, consumer-protection]
sources: ["https://arxiv.org/abs/2510.18113"]
confidence: high
provenance: "Discovered via Weekly Research Review"
---

Investigating the Impact of Dark Patterns on LLM-Based Web Agents

Devin Ersoy† *, Brandon Lee† *, Ananth Shreekumar†, Arjun Arunasalam‡
Muhammad Ibrahim§, Antonio Bianchi†, and Z. Berkay Celik†
† Purdue University, {dersoy, lee3008, ashreeku, antoniob, zcelik}@purdue.edu
‡ Florida International University, aarunasa@fiu.edu § Georgia Institute of Technology, mibrahim@gatech.edu

arXiv:2510.18113v1 [cs.CR] 20 Oct 2025

Abstract—As users increasingly turn to large language model (LLM) based web agents to automate online tasks, agents may encounter dark patterns: deceptive user interface designs that manipulate users into making unintended decisions. Although dark patterns primarily target human users, their potentially harmful impacts on LLM-based generalist web agents remain unexplored. In this paper, we present the first study that investigates the impact of dark patterns on the decision-making process of LLM-based generalist web agents. To achieve this, we introduce LiteAgent, a lightweight framework that automatically prompts agents to execute tasks while capturing comprehensive logs and screen-recordings of their interactions. We also present TrickyArena, a controlled environment comprising web applications from domains such as e-commerce, streaming services, and news platforms, each containing diverse and realistic dark patterns that can be selectively enabled or disabled. Using LiteAgent and TrickyArena, we conduct multiple experiments to assess the impact of both individual and combined dark patterns on web agent behavior. We evaluate six popular LLM-based generalist web agents across three LLMs and discover that when there is a single dark pattern present, agents are susceptible to it an average of 41% of the time. We also find that modifying dark pattern UI attributes through visual design changes or HTML code adjustments and introducing multiple dark patterns simultaneously can influence agent susceptibility. We also explore countermeasures by testing various prompting strategies designed to help agents avoid dark patterns. We found that the most effective prompts were specific step-by-step instructions on how to avoid a particular dark pattern. However, these prompts only dropped agent dark pattern susceptibility by an average of around 32%. We also observe that dark pattern susceptibility generally decreases as the number of dark patterns increases. Finally, we also investigate the impact of vision capabilities on agent behavior, finding mixed results. Without vision capabilities, a majority of agents tested experienced decreases in task success rates and increases in dark pattern susceptibility when vision was turned on. We also experimented with countermeasures by prompting agents to avoid dark patterns with increasingly specific prompts. We found that the most effective prompts were specific step-by-step instructions on how to avoid a particular dark pattern. However, these prompts only dropped agent dark pattern susceptibility by an average of around 32%.

1. Introduction

Large Language Models (LLMs) have demonstrated exceptional performance in various tasks, particularly in understanding and generating both code and natural language [1], [2]. This proficiency has led to widespread adoption in research and industry, with companies developing more powerful models and creating applications to automate specific tasks [3], [4], [5]. One emerging application is LLM-based generalist web agents: LLM-powered systems that can automate browser-based tasks on any website. For instance, a web agent could find the cheapest water bottle on a shopping site or apply for multiple jobs on a job search platform.

These agents can operate on unfamiliar webpages that do not provide API access. To do this, web agents collect data such as HTML code, browser screenshots, or a combination of both to understand the web environment. This observational data is then processed to condense and emphasize key features of the environment, which are combined with the user's task goal in a prompt sent to an LLM. The LLM is then expected to generate an appropriate action that progresses the agent toward achieving the user's goal.

In recent years, the rapid development of LLM-enabled web agents has resulted in several notable academic and commercial implementations [6], [7], [8], [9]. While these agents offer promising web automation capabilities, they face potential challenges in safely navigating the Internet, particularly when encountering dark patterns – deceptive user interface designs specifically intended to mislead or manipulate human users into making certain decisions.

Consider a shopping site pop-up offering a 30-day free trial of a premium membership. It might feature a prominent blue button to "continue with a free trial" (which eventually charges the user's card-on-file) and a small "x" button to close the pop-up. This asymmetry of choice, combined with forced user interaction to continue, is designed to increase the likelihood of subscription – a common dark pattern. In such a scenario, a web agent might inadvertently subscribe on behalf of the user, not only falling victim to the dark pattern but also doing so without the user's knowledge. Compounding this risk is the plethora of dark patterns that exist online today. A recent report by the Federal Trade Commission (FTC) noted that 75% of apps and websites leverage such deceptive design to trick users [10]. These dark patterns are known to have negative consequences for users, ranging from unintentional loss of money [11], [12] to deceptive steering of users toward specific items [13], [14].

Given the prevalence of dark patterns, it is highly likely that web agents interacting with web content come across such deceptive patterns. However, prior research surrounding security threats for web agents has mainly focused on prompt injection attacks, where an attacker embeds malicious instructions within the web environment [15], [16], causing the web agent to deviate from its intended task. While such attacks remain minimally documented in real-world scenarios, dark patterns are a well-documented and widespread phenomenon [10]. Although dark patterns are traditionally designed for humans, their potential to affect LLM-based generalist web agents remains unexplored.

In this paper, we present the first systematic evaluation of dark pattern effectiveness on LLM-enabled web agents. To do this, we introduce LiteAgent, a framework that automates agent execution on specific tasks and records their actions. Existing test environments, such as WebArena [8], test specific agent implementations with different LLMs. In contrast, our framework can be configured to support any agent implementation, enabling more realistic evaluation.

LiteAgent takes an agent, task, and target website as inputs. It prompts the agent to complete the task in a browser on the target website while monitoring the environment with injected JavaScript event listeners. These listeners capture agent actions (such as clicks, scrolls, and keystrokes) with elements on every webpage, logging them to a database for later analysis. The entire session is also screen recorded to provide a comprehensive visual record for manual inspection.

To provide a controlled web environment to systematically assess web agents, we introduce TrickyArena, a controlled environment comprising web applications from domains such as e-commerce, streaming services, and news platforms, each containing diverse and realistic dark patterns that can be selectively enabled or disabled.

We conduct a comprehensive evaluation of six popular web agents across three LLMs, systematically testing their susceptibility to dark patterns. Our evaluation reveals several key findings:

- When a single dark pattern is present, agents are susceptible to it an average of 41% of the time.
- Modifying dark pattern UI attributes through visual design changes or HTML code adjustments influences agent susceptibility.
- Introducing multiple dark patterns simultaneously affects agent decision-making.
- Dark pattern susceptibility generally decreases as the number of dark patterns increases (counterintuitively).
- Vision capabilities have mixed results – without vision, a majority of agents experienced decreases in task success rates and increases in dark pattern susceptibility when vision was turned on.
- Countermeasures via prompting were tested. The most effective prompts were specific step-by-step instructions on how to avoid a particular dark pattern. However, these prompts only dropped agent dark pattern susceptibility by an average of around 32%.

In summary, we make the following contributions:

- Dark Patterns vs. Agents: To the best of our knowledge, we conduct the first comprehensive analysis of dark pattern effectiveness on LLM web agents.
- Systematic Evaluation Framework: We introduce LiteAgent and TrickyArena, tools for testing web agents against dark patterns in a controlled environment.
- Comprehensive Agent Analysis: We evaluate six popular web agents, revealing their vulnerabilities to various dark patterns.

Our tools and findings from this study serve as a valuable resource for future research on dark patterns and web agents.

Our code and datasets are available at https://github.com/purseclab/liteagent

©2025 IEEE. Personal use of this material is permitted. Permission from IEEE must be obtained for all other uses, in any current or future media, including reprinting/republishing this material for advertising or promotional purposes, creating new collective works, for resale or redistribution to servers or lists, or reuse of any copyrighted component of this work in other works.

[Content continues — full PDF extraction follows...]
