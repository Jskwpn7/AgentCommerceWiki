---
title: "How Agents Ask for Permission: User Permissions for AI Agents, from Interfaces to Enforcement"
type: raw_paper
created: 2026-08-15
updated: 2026-08-15
source_url: https://arxiv.org/abs/2607.13718
arxiv_id: "2607.13718"
authors:
  - Alexandra E. Michael
  - Franziska Roesner
categories: [cs.CR, cs.AI]
published: 2026-07-15
tags:
  - agentic-ai
  - digital-platforms
  - financial-services
  - academic
provenance: "Full-text extraction of arXiv 2607.13718v1 (HTML), retrieved 2026-08-15 via web_extract"
---

How Agents Ask for Permission: User Permissions for AI Agents, from Interfaces to Enforcement

As AI agents gain prevalance, users are increasingly exposed to the risks such systems entail.
Prompt injection attacks, as well as hallucination, can cause agents to leak private information to third parties.
As autonomous systems, agents also present the more active danger of performing sensitive tasks, such as bank transactions, without the user’s intent or authorization.
Recognizing this challenge, the agentic security community has developed numerous proposals for secure agentic systems.
Much of this work has focused on *product-level* approaches, where agentic system developers determine and apply the same security policies and permissions to all users.
Yet different users have different needs and preferences, necessitating support for *user-level* permissions policies in agentic AI systems.
To understand how user-level permissions are handled in AI agent systems, we survey 21 proposals for agent permissions systems.
From this review, we construct a taxonomy of how different systems specify user-level permissions policies, both at the user interface and internally; derive internal policies from user input; and enforce those policies at run-time.
We then analyze five prominent commercial agents and compare their permissions handling to agentic permissions systems in the literature.
We identify several high-level themes across the literature and commerical agents, as well as multiple gaps where future work is needed.

## 1 Introduction

AI agents are increasingly prevalent, as AI developers shift their focus from standalone LLM chatbots to whole frameworks integrating LLM planners and executors with third-party tools.
Empowered by the adaptiveness and flexibility of LLMs, agentic AI systems take on a vast space of autonomous tasks, from coding and open-source development to managing email and writing blog posts.

Yet just as AI agents inherit LLMs’ benefits, they also share, and amplify, their dangers.
LLMs are subject to a wide range of risks, including, but certainly not limited to, prompt injection and jailbreaking, disclosing sensitive information, and simple hallucination [[42](#bib.bib42), [18](#bib.bib18)].
AI agents carry those same risks, and add the potential for substantially greater harms.
A prompt-injected or hallucinating agent can use tools to expose sensitive information, wreak havoc on a user’s files, or even transfer their funds to third parties.

Recognizing this challenge, researchers and AI companies alike have made the pursuit of more secure agentic systems a priority.
The last two years alone have seen an explosion of proposals for secure agentic systems.
These systems aim to mitigate AI agents’ risks by enforcing some security policy over their actions.

Much of the agentic security literature has focused on global or *product-level* security policies, which are pre-defined in the agent framework and applied across all users.
For example, an agentic security system might impose a global policy that prevents passport numbers from being sent to any websites other than recognized airlines.
Yet “correct” security policies, or permissions, are often user- and context-dependent [[11](#bib.bib11), [12](#bib.bib12)].
One user might want an agent to share their passport information with a specialty travel booking service, one not listed in the global policy.
Another, especially privacy-conscious, user might prefer to prohibit the agent from ever sharing their passport information, even with “authorized” sites.

To address cases like these, a secure agentic system must support some form of *user-level* permissions policy.
In this work, we seek to answer the questions:
What is the state of the art on handling user-level permissions in agentic AI systems?
And where should the agentic security community go from here?

These questions are not only a matter of technical implementation, but also user interaction.
User-level permissions are, by definition, influenced by the user’s needs.
This makes it crucial to understand when and how agentic permissions systems grant users control over their own permission policies [[57](#bib.bib57)].
We break down our overarching goal into three research questions:

RQ1. What interfaces do current proposals for secure agent permissions systems provide to users?

RQ2. How do agent permissions systems in the literature internally specify and enforce user-level policies?
(a) What is the structure of internal policy specifications, and (b) how are they derived from user-selected options?
(c) To what extent do enforcement mechanisms depend on LLMs?

RQ3. Where are there gaps in the work on user-level permissions systems for AI agents, both (a) within the literature and (b) between the literature and commercial agents?
(c) What areas of agent permissions systems hold potential and need for future work?

To answer these questions, we conduct a literature review of recently proposed secure agentic systems, specifically targeting those that address user-level permissions in some capacity.
From this survey, we construct a taxonomy of approaches in agentic systems to specifying permissions policies, both at the user interface and internally, deriving internal policies from user selections, and enforcing polices at run time.
With this taxonomy, we then analyze five prominent commercial AI agents to understand how agent permissions systems used in practice compare to those in the literature.

Scope.
We consider any autonomously acting system that does not incorporate LLMs, as well as LLM-based systems that lack support for external tools, to be out of scope.
We furthermore focus on prototypes that implement some form of user-level permissions or policies for agents.
Agentic systems with no support for permissions, or which only support global or product-level permission policies, are out of scope.

We identify several common goals in the literature, including minimizing user overhead, formalizing policy specifications, and enforcing permissions deterministically.
We also find substantial gaps: none of the proposals we review achieve all three of these goals, despite a few coming close.
The commercial agents we evaluate fare even worse.
We find they often force users to choose between high-overhead user-in-the-loop permissions enforcement, and LLM auto-reviewers with little transparency or user control.
Commercial agents do, however, allow users to modify policies over time, a user control frequently overlooked in the literature.

Our contributions:

A survey of recent proposals for handling user-level permissions in the AI agent literature.

A taxonomy of approaches to specifying, deriving from user input, and enforcing user-level permissions policies in agentic systems.

A comparative analysis of permissions handling in five commercial AI agents to agentic permissions systems in the literature.

Important gaps and areas for future work on user-level permissions in agentic systems.

We begin with a brief overview of AI agents, agent security, and related work (Section [2](#S2 "2 Background ‣ How Agents Ask for Permission: User Permissions for AI Agents, from Interfaces to Enforcement")).
Section [3](#S3 "3 Methods ‣ How Agents Ask for Permission: User Permissions for AI Agents, from Interfaces to Enforcement") describes our methodology.
Section [4](#S4 "4 Results ‣ How Agents Ask for Permission: User Permissions for AI Agents, from Interfaces to Enforcement") details our taxonomy and survey results, followed by discussion and takeaways (Section [5](#S5 "5 Discussion ‣ How Agents Ask for Permission: User Permissions for AI Agents, from Interfaces to Enforcement")).
Section [6](#S6 "6 Limitations ‣ How Agents Ask for Permission: User Permissions for AI Agents, from Interfaces to Enforcement") contains limitations, and Section [8](#S8 "8 Conclusion ‣ How Agents Ask for Permission: User Permissions for AI Agents, from Interfaces to Enforcement") concludes.

## 2 Background

### 2.1 AI Agents

In line with related work [[28](#bib.bib28)], we use “AI agent” and “agentic AI systems” interchangeably, to mean systems that use LLMs to plan and/or trigger calls to external tools.
As a rule, AI agents under our notion also include some non-AI component, as necessary to effectuate the actual execution of tool calls [[28](#bib.bib28), [35](#bib.bib35)].
We sometimes shorten “AI agent” and “agentic AI systems” to “agent” or “agentic systems” for brevity.
In context of this work, we exclusively use these terms to refer to the sort of LLM-based agentic AI systems described above, acknowledging that “agent” may have a broader meaning in other contexts [[48](#bib.bib48), [61](#bib.bib61), [56](#bib.bib56)].

Within this definition, AI agents may have a wide variety of different architectures, such as multi-LLM paradigms [[19](#bib.bib19), [59](#bib.bib59), [35](#bib.bib35)], and tool-calling protocols [[5](#bib.bib5), [63](#bib.bib63)].
AI agents also occupy various different contexts: coding agents [[41](#bib.bib41), [8](#bib.bib8)], chatbots augmented with OAuth connections [[39](#bib.bib39), [7](#bib.bib7), [24](#bib.bib24)], and agentic browsers [[40](#bib.bib40), [45](#bib.bib45)] are just a few examples.
While the specifics of each agent necessarily influence its mechanisms for user-level permissions, we aim to develop a unified taxonomy of high-level approaches across agentic architectures and contexts.

Importantly, we distinguish between the overarching agentic AI system, or agent, and the LLM(s) used to plan and execute actions within it.
Our focus is on permissions systems for agents as whole frameworks.
We consider safety and security considerations for standalone LLMs [[3](#bib.bib3), [46](#bib.bib46)], an important research area in its own right, to be out of scope.

### 2.2 User-Facing Permissions in Non-AI Systems

There is a long history of work on user-facing permissions for traditional, non-AI systems.
Such permissions systems have traditionally been built on foundational security principles like *least privilege* (grant each entity only the minimum necessary permissions) and *failing closed* (when in doubt, deny permission) [[47](#bib.bib47), [51](#bib.bib51)].
Prominent approaches include access control lists (ACLs), where each resource (e.g., a file) carries a list of who can access it and how; and capabilities, which instead act as nontransferable tokens of authority.
Both access control lists and capabilities appear in widely used permissions systems today, including the Unix file system (ACLs) and OAuth 2.0 (capabilities) [[22](#bib.bib22)].

Regardless of approach or context, user-facing permissions systems face a common challenge of balancing desired security principles with usability: How easy is it for a user to specify permissions?
And how likely is it that the permissions they select will match what they actually need?

This problem is hard in part because appropriate permissions are context-dependent, and cannot generally be determined ahead of time for all users [[11](#bib.bib11), [12](#bib.bib12)].
One solution is to ask the user themselves to determine their permissions policy.
However, users overwhelmed by permissions or privacy decisions are prone to over-granting permissions, in a phenomenon known as “privacy fatigue” [[15](#bib.bib15), [27](#bib.bib27), [54](#bib.bib54)].
Alternatives, like automatically-granted permissions and trusted UI elements, avoid such interruptions, but come at a cost to transparency, user control, and least privilege [[21](#bib.bib21)].

AI agents represent a novel domain for permissions systems, one that presents unique challenges while retaining many of the goals and tradeoffs of traditional systems [[16](#bib.bib16)].
Agentic permissions systems, like traditional ones, are still asked to enforce security principles like least privilege.
And the security-usability tradeoff is more prominent than ever, amplified by the need to preserve as much of the agent’s run-time utility as possible.

Unlike traditional systems, however, AI agents carry particular challenges owing to their reliance on LLMs.
These include the conflation of “code” (instructions) and data, which opens agents to prompt injection attacks, and LLMs’ inherent nondeterminism [[42](#bib.bib42), [18](#bib.bib18)].
Unlike deterministic systems, an AI agent may respond to the same instructions in arbitrarily many different ways.
That unpredictability poses a particular challenge to permissions systems, which must enforce a consistent policy on every possible set of actions.

### 2.3 Agentic Security

The growing field of agentic security seeks to address the risks of AI agents [[28](#bib.bib28), [16](#bib.bib16)].
These risks include not just the novel challenges posed by LLMs, but also the familiar dangers of heterogeneous systems, such as untrusted inputs, access to sensitive data, and the potential for destructive actions, to name a few.
As background to the narrower space of user-level permissions in agents, we describe a few important agentic security approaches below.

One line of work seeks to reign in AI agents by targeting their core LLMs.
AI guardrails constrain the output of a decision-making LLM by using a secondary model, typically another LLM, to identify policy violations [[3](#bib.bib3), [46](#bib.bib46), [1](#bib.bib1)].
Meanwhile, dual- or multi-LLM systems like CaMeL create a separation of privilege by designating distinct LLMs for different tasks [[19](#bib.bib19), [59](#bib.bib59)].
For example, a planner LLM might determine actions in advance, while an executor handles untrusted run-time inputs but cannot make decisions.

LLM-focused safeguards provide valuable checks against prompt injection and hallucination, but they are not a panacea.
AI guardrails offer limited protection against stronger, more adaptive attacks [[38](#bib.bib38)].
And privilege separation approaches are often forced to choose between permitting the planner to see untrusted data and maintaining the run-time flexibility that makes agents so useful [[19](#bib.bib19)].
Recognizing these shortcomings, a surge of recent work draws from traditional security approaches to implement more deterministic agentic security systems.
These efforts range from mobile-style user-selected security policies [[59](#bib.bib59), [60](#bib.bib60)], to information flow control [[58](#bib.bib58), [19](#bib.bib19), [32](#bib.bib32), [17](#bib.bib17), [36](#bib.bib36), [4](#bib.bib4)], to custom domain-specific languages (DSLs) for agentic security policies [[50](#bib.bib50), [55](#bib.bib55), [44](#bib.bib44), [31](#bib.bib31)].

Agentic security is a recently emerged area, and so far, much of the literature focuses on internal, product-level mechanisms for defining and enforcing security policies.
Comparatively less work has been devoted to the ways *users* interact with those policies.
For instance, both CaMeL and Fides presume that security policies are fixed in the agentic system’s architecture, without allowing those policies to shift according to users’ needs [[19](#bib.bib19), [17](#bib.bib17)].
Fides’ approach was later extended in Prudentia to allow users to selectively override policy violations, even as the policies themselves remain fixed.
For CaMeL, however, any extension to user-specific permissions remains open for future work, as is a recurring pattern in agentic security systems [[65](#bib.bib65), [36](#bib.bib36), [4](#bib.bib4), [25](#bib.bib25), [1](#bib.bib1)].

## 3 Methods

### 3.1 Literature Survey

To understand the current space of approaches to user-level agent permissions, we reviewed a total of 21 systems and proposals from 2024 -- 2026, including 3 peer-reviewed publications, 18 pre-prints,11
1
Two of these, PCAS and FORGE, are different iterations of the same work [[44](#bib.bib44), [43](#bib.bib43)]. We reviewed PCAS prior to FORGE’s release, and retained it in our analysis due to the substantial architectural and design differences between the two. and one open-source system without an associated paper [[2](#bib.bib2)].
The initial literature search took place during April and early May 2026, with a small number of papers added subsequently (see below).

We identified these works by beginning with a small set of influential papers, e.g., [[55](#bib.bib55), [50](#bib.bib50), [44](#bib.bib44)], then recursively following citation paths (“snowballing”) to incorporate those papers’ related works.
This process resulted in an initial pool of 26 papers and open-source systems.
From this pool, we eliminated 8 systems as out of scope, under the following criteria:

They targeted standalone LLMs rather than tool-calling AI agents;

They did not propose or implement any concrete framework, mechanism, or technique relating to permissions policies in agentic systems; or

They did not support or address *user-level* permissions policies, only policies set at a global or product level.

Finally, we considered four additional pre-prints that were posted recently and identified after completing our initial literature search.
One of these was out of scope, while the other three we added to our analysis, resulting in our final set of 21 papers and systems.
We reviewed each paper in this set for high-level themes, recording detailed notes on each proposal’s approach to handling user interfaces, internal specifications, and enforcement of permissions.

#### 3.1.1 Taxonomization

We developed our agent permissions system taxonomy (Table [1](#S4.T1 "Table 1 ‣ 4 Results ‣ How Agents Ask for Permission: User Permissions for AI Agents, from Interfaces to Enforcement")) through a process of iterative refinement.
The taxonomy development and paper categorization process was undertaken primarily by the first author, with periodic feedback from the other authors.
We began by proposing a sketch of taxonomies for (a) policy specifications, (b) derivation of internal specifications from user selections, and (c) enforcement mechanisms.
Each initial sketch consisted of 4-6 levels, with higher levels roughly corresponding to greater user control over, and predictability of, the policy and its enforcement.

We then reviewed each paper in our initial pool of 26, setting aside those we ruled out of scope and identifying tentative taxonomy placements for the remaining 18.
During this initial pass, we occasionally paused to refine the taxonomy to better reflect the themes emerging from the literature.
Each time we refined the taxonomy, we returned to the previously reviewed papers to validate their placements and adjust them, if needed.
While most refinements were minor, we notably added the threat model portion of the taxonomy during this stage.

We repeated this process of refinement and validation until all 18 initial papers had been reviewed.
At this point, we finalized the taxonomy and performed a penultimate validation pass to ensure all placements remained stable.
When we later placed the three additional papers for our final set of 21, we once again refined and validated the taxonomy.
This last refinement only required adding one new category to our taxonomy of threat model adversaries, and did not affect any existing papers’ placements.

### 3.2 Commercial Agent Walkthroughs

To understand how prominent in-use agents fit into the space of agent permissions, we evaluated five commercial agents across two companies and three modalities: Web chatbots with OAuth connections (Claude [[7](#bib.bib7)], ChatGPT [[39](#bib.bib39)]), desktop agents (Claude Cowork [[9](#bib.bib9)], Codex [[41](#bib.bib41)]), and an agentic browser (ChatGPT agent mode [[39](#bib.bib39)]).
Our commercial agent investigation took place in the latter half of May and first week of June 2026, and used Sonnet 4.6, GPT-5.5, and GPT-5.4-Mini.

Inspired by the walkthrough method of app analysis [[34](#bib.bib34)], we applied the following process to each agent:

Set up or install the agent in a clean environment (e.g., a private browsing window or isolated VM), using an account created for this purpose.

Identify the permissions settings (UI) initially available through menus.

Grant a small number of permissions. For chatbots with OAuth connections, we granted access to an experiment-specific Gmail account. For desktop agents, we granted access to a local file folder (e.g., the Desktop). The agentic browser had no permissions available to grant.

Ask the agent to complete tasks that it both should and should not be able to accomplish under the current settings. If multiple settings are available for policy enforcement, repeat under each one.

If possible, attempt to revoke previously granted permissions, then ask the agent to attempt tasks that require the revoked permissions.

Due to the closed-source nature of most commercial agents, we rely on our observations of the agent’s output and UI to determine the results of each user-level change to permissions.
In one chatbot’s case (Claude), we were able to glean additional insights from monitoring the browser’s console log, where it logged its MCP tool calls.

## 4 Results

|  | Category | In the literature | In commercial agents |
| --- | --- | --- | --- |
| Threat model: Adversary | None specified | [[33](#bib.bib33), [31](#bib.bib31), [14](#bib.bib14), [44](#bib.bib44), [55](#bib.bib55), [62](#bib.bib62)] | – |
| External data sources, excluding third-party tools, the agent, and its provider (implied by “benign but fallible agent”) | [[37](#bib.bib37), [29](#bib.bib29)] | – |
| Third-party tools | [[59](#bib.bib59), [10](#bib.bib10), [60](#bib.bib60), [50](#bib.bib50), [32](#bib.bib32), [52](#bib.bib52)] | – |
| Agent provider | [[52](#bib.bib52)] | – |
| Benign but fallible agent subject to prompt injection and/or hallucination | [[53](#bib.bib53), [23](#bib.bib23), [43](#bib.bib43), [2](#bib.bib2), [49](#bib.bib49), [60](#bib.bib60), [58](#bib.bib58), [66](#bib.bib66), [50](#bib.bib50), [52](#bib.bib52)] | – |
| Threat model: Target | None specified | [[33](#bib.bib33), [31](#bib.bib31), [14](#bib.bib14), [44](#bib.bib44), [55](#bib.bib55), [62](#bib.bib62)] | – |
| Data exfiltration to external parties, excluding other forms of data/control flow (implied by “general task flow”) | [[10](#bib.bib10), [60](#bib.bib60), [52](#bib.bib52)] | – |
| General task flow: combined data/control flow at execution time | [[53](#bib.bib53), [23](#bib.bib23), [37](#bib.bib37), [43](#bib.bib43), [2](#bib.bib2), [49](#bib.bib49), [32](#bib.bib32), [59](#bib.bib59), [58](#bib.bib58), [66](#bib.bib66), [50](#bib.bib50), [29](#bib.bib29)] | – |
| Specification (UI) | None (no user-facing specification mechanism) | [[53](#bib.bib53), [23](#bib.bib23), [33](#bib.bib33), [37](#bib.bib37), [31](#bib.bib31)] | ChatGPT agent mode [[39](#bib.bib39)] |
| Natural language | [[10](#bib.bib10), [62](#bib.bib62), [14](#bib.bib14), [43](#bib.bib43), [2](#bib.bib2), [49](#bib.bib49)] | – |
| Privilege labels, e.g., high (secure) vs. low (public) | [[32](#bib.bib32), [58](#bib.bib58), [29](#bib.bib29)] | – |
| Fixed selection from a set of policies, e.g., mobile-style permissions | [[49](#bib.bib49), [60](#bib.bib60), [59](#bib.bib59), [66](#bib.bib66), [52](#bib.bib52)] | Claude, Claude Cowork, Codex, ChatGPT chat mode [[7](#bib.bib7), [9](#bib.bib9), [41](#bib.bib41), [39](#bib.bib39)] |
| Structured constraints, or flexible rules within a pre-defined set of actions or conditions | [[44](#bib.bib44), [50](#bib.bib50)] | – |
| Arbitrary rules, permitting fully user-defined actions | [[55](#bib.bib55)] | – |
| Specification (internal) | None (no internally tracked specification) | [[10](#bib.bib10)] | – |
| Natural language | [[62](#bib.bib62)] | – |
| Privilege labels, e.g., high (secure) vs. low (public) | [[32](#bib.bib32), [58](#bib.bib58), [66](#bib.bib66), [29](#bib.bib29)] | – |
| Fixed selection from a set of policies, e.g., mobile-style permissions | [[49](#bib.bib49), [60](#bib.bib60), [59](#bib.bib59), [52](#bib.bib52)] | – |
| Structured constraints, permitting flexible rules within a pre-defined set of actions or conditions | [[53](#bib.bib53), [23](#bib.bib23), [33](#bib.bib33), [37](#bib.bib37), [31](#bib.bib31), [14](#bib.bib14), [43](#bib.bib43), [2](#bib.bib2), [44](#bib.bib44), [50](#bib.bib50)] | – |
| Arbitrary rules, permitting fully user-defined actions | [[55](#bib.bib55)] | – |
| Derivation | None (no UI-to-internal translation occurs) | [[10](#bib.bib10)] | ChatGPT agent mode [[39](#bib.bib39)] |
| AI prediction from user query and/or implicit context | [[53](#bib.bib53), [23](#bib.bib23), [33](#bib.bib33), [37](#bib.bib37), [31](#bib.bib31), [49](#bib.bib49), [60](#bib.bib60)] | Claude [[7](#bib.bib7)] |
| AI compilation from user-provided specification | [[14](#bib.bib14), [43](#bib.bib43), [2](#bib.bib2), [49](#bib.bib49)] | – |
| Deterministic compilation from user-specified policy | [[58](#bib.bib58), [66](#bib.bib66)] | – |
| Exact use of user-specified policy | [[62](#bib.bib62), [49](#bib.bib49), [32](#bib.bib32), [59](#bib.bib59), [44](#bib.bib44), [50](#bib.bib50), [55](#bib.bib55), [29](#bib.bib29), [52](#bib.bib52)] | Claude, Claude Cowork, Codex, ChatGPT chat mode [[7](#bib.bib7), [9](#bib.bib9), [41](#bib.bib41), [39](#bib.bib39)] |
| Enforcement | None (relies on best-effort compliance from the agent) | [[31](#bib.bib31)] | Claude Cowork [[9](#bib.bib9)] |
| External mechanisms, defined by third-party tools | [[49](#bib.bib49)] | – |
| LLM guardrail determines compliance | [[33](#bib.bib33), [2](#bib.bib2), [10](#bib.bib10)] | Claude, Codex [[7](#bib.bib7), [41](#bib.bib41)] |
| AI-generated per query, e.g., enforcement code generated separately for each query | [[62](#bib.bib62), [14](#bib.bib14), [32](#bib.bib32)] | – |
| AI-generated from policy, only once | [[55](#bib.bib55)] | – |
| Non-AI automation: automated violation detection without use of AI; generally deterministic | [[53](#bib.bib53), [23](#bib.bib23), [37](#bib.bib37), [43](#bib.bib43), [2](#bib.bib2), [59](#bib.bib59), [58](#bib.bib58), [66](#bib.bib66), [44](#bib.bib44), [50](#bib.bib50), [29](#bib.bib29), [52](#bib.bib52)] | Claude [[7](#bib.bib7)] |
| User-in-the-loop: User indicates violations in real time | [[59](#bib.bib59), [29](#bib.bib29), [52](#bib.bib52)] | Claude, Claude Cowork, Codex, ChatGPT chat mode [[7](#bib.bib7), [9](#bib.bib9), [41](#bib.bib41), [39](#bib.bib39)] |

Agent permissions systems in the literature represent a wide range of approaches to specifying, deriving, and enforcing user-specific permissions policies.
Nonetheless, we identify three primary themes as recurring goals among permissions systems:

(1) *Near-zero user overhead* in specifying policies, whether by permitting natural language input or inferring policies from implicit context.
(2) *Formally grounded specifications*, based on established principles such as information flow control [[58](#bib.bib58), [32](#bib.bib32), [29](#bib.bib29)] or type safety [[44](#bib.bib44), [50](#bib.bib50), [55](#bib.bib55), [31](#bib.bib31)].
And (3) *deterministic enforcement*, avoiding the potential for nondeterministic errors in AI guardrails.

Across the 21 systems we review from the literature, all emphasize one or more of these themes, *but none fully achieve all three*.
On the other hand, few of the 5 commercial agents we review clearly achieve any of the three goals.
What many of them do prioritize, however, is:
(4) *Continuous user control* over permissions policies, even after initial specification time.

By contrast, few of the proposals in the literature focus on continued user control or transparency, indicating a substantial gap between the directions of academic research and commercial systems on priorities in agent permissions systems.

We begin this section by highlighting notable elements of our taxonomy.
We then describe the threat models and themes we identify across agent permissions systems in the literature, followed by a discussion of commercial agents.

### 4.1 Taxonomy

Table [1](#S4.T1 "Table 1 ‣ 4 Results ‣ How Agents Ask for Permission: User Permissions for AI Agents, from Interfaces to Enforcement") contains our taxonomy, split across threat models and approaches to specifying, deriving, and enforcing policies.
Apart from those labeled “None”, the categories are generally not mutually exclusive.
We describe a few notable categories here, and refer the reader to the table for the full list.

#### 4.1.1 Threat Models

Threat models for traditional, non-AI systems have historically distinguished between data flow, or the movement of information, and control flow, concerning the instructions executed by a program.
To an AI agent, however, data and control flow are unavoidably intertwined: instructions are merely another form of data, and data itself often contains instructions [[35](#bib.bib35), [42](#bib.bib42)].

We therefore consider data and control flow as one unit in our threat model taxonomy, termed *task flow*.
We define task flow as the combined flow of information and instructions over the course of an agent solving any given task.
The task flow category includes any threat model that broadly targets data, control flow, or both.

The threat models portion of our taxonomy also contains two mutually exclusive categories (other than “None”).
A small number of papers explicitly limit their adversary to only include external data sources, or their target to only include data exfiltration.
Both threat models are implied by a more expansive one: external data sources are covered by benign-but-fallible agent adversaries, while data exfiltration is implicit in general task flow.
Because the great majority of papers with specified threat models fall into the more general categories, we list only the papers that use these categories exclusively.

#### 4.1.2 Specifications

We distinguish between several forms of policy specification, including privilege labels, fixed selections, structured constraints, and arbitrary rules.
*Privilege* or *security labels* are often used to distinguish between private and public data in information flow control systems.
Generally, such systems follow a standard policy: “low” (public) data is allowed as input to tools labeled “high” (private), but not vice versa [[58](#bib.bib58), [29](#bib.bib29), [32](#bib.bib32)].
In practice, we find that privilege label systems offer users only limited control over permissions policies.
The user can sometimes indicate the label of their own query, but often have little or no control over the labels assigned to third-party tools [[29](#bib.bib29), [32](#bib.bib32)].

*Fixed selection* refers to systems where users may select any policy from a set of pre-defined options.
This often takes the form of mobile-style permissions, i.e., “Always”/“Once”/“Never” [[59](#bib.bib59), [60](#bib.bib60)].
*Structured constraints*, by contrast, are more flexible.
We use this category for systems where policies must operate over a pre-defined set of actions or targets, but can be nearly anything within those constraints.
Progent’s programmable policies, which require every policy to select from a set of three actions to take upon violation, are one example [[50](#bib.bib50)].

Finally, we classify specifications where policies can be truly anything under *arbitrary rules*.
This category includes only one system, AgentSpec [[55](#bib.bib55)], which allows users to write arbitrary functions as policies.

While each system has at most one form of internal specification, user interface specification categories are not mutually exclusive.
For example, AC4A [[49](#bib.bib49)] provides two different ways for users to specify their policy (natural language or direct selection from a list of options).
We list it under both categories accordingly.

#### 4.1.3 Derivation and Enforcement

Derivation categories refer to the means by which an agent permission system determines its internal policy from a user-specified one.
Enforcement, meanwhile, covers the run-time mechanism a system uses to detect policy violations.
As with UI specifications, some systems provide multiple derivation or enforcement approaches and are listed for every option they support.
We refer the reader to Table [1](#S4.T1 "Table 1 ‣ 4 Results ‣ How Agents Ask for Permission: User Permissions for AI Agents, from Interfaces to Enforcement") for a brief description of each category.

### 4.2 Themes in the Literature

#### 4.2.1 Threat Models

Nearly a third of the proposals in our survey do not specify a threat model [[33](#bib.bib33), [31](#bib.bib31), [14](#bib.bib14), [44](#bib.bib44), [55](#bib.bib55), [62](#bib.bib62)].
Among those that do, most define the agent itself as the source of threat, not out of malicious intent, but rather due to external prompt injection, hallucinations, or both [[53](#bib.bib53), [23](#bib.bib23), [43](#bib.bib43), [2](#bib.bib2), [49](#bib.bib49), [60](#bib.bib60), [58](#bib.bib58), [66](#bib.bib66), [50](#bib.bib50)].
Some proposals explicitly trust third-party tools [[49](#bib.bib49), [66](#bib.bib66), [29](#bib.bib29)], while not necessarily extending that trust to those tools’ output.
Others consider tools to be an adversary [[59](#bib.bib59), [10](#bib.bib10), [60](#bib.bib60), [50](#bib.bib50), [32](#bib.bib32)].

The goal for most of the systems we review is to prevent agent actions (i.e., tool calls) that fall outside the intended, or authorized, task flow.
The three exceptions are AirGapAgent [[10](#bib.bib10)], GAAP [[52](#bib.bib52)], and Wu et al.’s proposal for automating data permissions [[60](#bib.bib60)], whose narrower threat models seek only to prevent exfiltration of sensitive data.

#### 4.2.2 Low User Overhead Through Natural Language or Contextual Policies

Nearly two-thirds (12) of the systems we review from the literature make design choices to avoid users having to specify permissions policies directly.
In 6 proposals, this comes in the form of taking user permissions as natural language [[10](#bib.bib10), [62](#bib.bib62), [14](#bib.bib14), [43](#bib.bib43), [2](#bib.bib2), [49](#bib.bib49)].
In such cases, the user must still dictate their intended policy, but avoid both the expressiveness limits of selecting a policy from a fixed set of permissions, and the learning curve of writing policies in JSON or a domain-specific language (DSL).

5 permissions systems go even further by eschewing user input for policies entirely [[53](#bib.bib53), [23](#bib.bib23), [33](#bib.bib33), [37](#bib.bib37), [31](#bib.bib31)].
Instead, these systems predict policies from *implicit context*, typically the contents of the user query, or information about the agent’s execution state.
Wu et al.’s proposal [[60](#bib.bib60)] similarly seeks to predict permissions policies, in their case by using a limited set of user-selected permissions decisions to train a classifier for future decisions.

Finally, Prudentia [[29](#bib.bib29)] explicitly identifies low user overhead as a goal.
Yet Prudentia relies on the user to make policy decisions in real time, making its demands on users significantly higher than the other systems listed here.
In this regard, Prudentia is more in line with commercial agents, which similarly rely on a user-in-the-loop approach (§[4.3](#S4.SS3 "4.3 Commercial Agents ‣ 4 Results ‣ How Agents Ask for Permission: User Permissions for AI Agents, from Interfaces to Enforcement")).

Among the systems that minimize user overhead, 5 also emphasize deterministic enforcement mechanisms (§[4.2.4](#S4.SS2.SSS4 "4.2.4 Deterministic Policy Enforcement ‣ 4.2 Themes in the Literature ‣ 4 Results ‣ How Agents Ask for Permission: User Permissions for AI Agents, from Interfaces to Enforcement")), while 2 offer formal grounding for their specifications (§[4.2.3](#S4.SS2.SSS3 "4.2.3 Formally Grounded Specifications ‣ 4.2 Themes in the Literature ‣ 4 Results ‣ How Agents Ask for Permission: User Permissions for AI Agents, from Interfaces to Enforcement")).
None, however, provide both.

#### 4.2.3 Formally Grounded Specifications

11 of the systems we review ground their policy specifications in formalized approaches to security.
Approaches range from defining policies in terms of security labels for information flow control [[32](#bib.bib32), [58](#bib.bib58), [29](#bib.bib29)], to using typed DSLs or Datalog (structured constraints or arbitrary rules) to ensure policies are well-formed [[50](#bib.bib50), [44](#bib.bib44), [55](#bib.bib55), [31](#bib.bib31), [43](#bib.bib43)].
ShieldAgent [[14](#bib.bib14)] defines policies in the form of linear temporal logic, while MiniScope [[66](#bib.bib66)] uses an Integer Linear Program (ILP) solver to identify the smallest set of necessary privileges.
Lastly, GAAP [[52](#bib.bib52)] performs information flow control analysis on code an agent generates to perform its task.

We observe that some systems appear to provide a foundation for formal specifications, yet fall short of defining the formalism itself.
AC4A [[49](#bib.bib49)] notably describes its approach in terms of “resource types”, implying a formal type system.
However, the AC4A paper omits discussion of what said formalism would actually entail.

Even among the systems that do provide formalized specifications, none prove the correctness of their policy *enforcement*.
ff-secure [[58](#bib.bib58)] and FORGE [[43](#bib.bib43)] both provide formal security analyses of their overall architecture, including both specification and enforcement, but the implemented systems themselves remain unverified.
GAAP’s run-time analysis of agent-generated code appears to come the closest, but even then, GAAP’s authors do not claim to have implemented formally verified enforcement [[52](#bib.bib52)].

#### 4.2.4 Deterministic Policy Enforcement

The final theme we identify in the literature is of deterministic enforcement mechanisms, implemented by 12 out of 21 systems [[53](#bib.bib53), [23](#bib.bib23), [37](#bib.bib37), [43](#bib.bib43), [2](#bib.bib2), [59](#bib.bib59), [58](#bib.bib58), [66](#bib.bib66), [44](#bib.bib44), [50](#bib.bib50), [29](#bib.bib29), [52](#bib.bib52)].
We observe deterministic enforcement across two categories:
(1) Automated enforcement mechanisms that do not involve an LLM or other AI models.
While one could theoretically implement nondeterministic or heuristic enforcement without using LLMs, in practice, none of the systems we review take this approach.
And (2) “user-in-the-loop” enforcement, which preemptively asks the user to make a policy decision rather than attempting to detect violations automatically.

We distinguish user-in-the-loop enforcement from systems that escalate to the user when a policy violation has *already* been detected.
The latter is an implementation decision, and we consider it orthogonal to the means of detecting violations in the first place.
Among the literature we review, only three systems implement a user-in-the-loop approach: IsolateGPT [[59](#bib.bib59)], Prudentia [[29](#bib.bib29)], and GAAP [[52](#bib.bib52)].
Both IsolateGPT and GAAP avoid user-in-the-loop enforcement where possible, by saving user decisions as policy updates and deterministically applying them to subsequent queries.
Prudentia, on the other hand, asks the user to override its default policies separately for every query.

We specifically define deterministic enforcement as excluding systems that use an LLM to generate enforcement code.
While most such systems seek to shield the enforcement models from untrusted inputs, doing so completely is not always possible, especially when the policy-enforcing code is generated anew for each query [[62](#bib.bib62), [14](#bib.bib14), [32](#bib.bib32)].
Furthermore, nondeterminism in the code-generating models remains a source of risk.
On the other hand, we classify FORGE [[43](#bib.bib43)] as providing deterministic enforcement, even though it permits LLM usage by way of user-defined external code.
Users must explicitly enable the LLM usage in question, and FORGE’s enforcement mechanism remains deterministic by default.

Finally, AC4A [[49](#bib.bib49)] does not automatically include LLMs in its enforcement.
However, AC4A requires each third-party tool to provide its own permissions enforcement function, which AC4A relies upon as a ground-truth source of policy enforcement decisions.
With third parties controlling the means of enforcement, there is no way for an individual user to be certain their policy is enforced deterministically.
Thus we exclude AC4A from this category.

### 4.3 Commercial Agents

We conducted walkthrough-style [[34](#bib.bib34)] investigations of five commercial agents (Claude, Claude Cowork, ChatGPT chat mode, ChatGPT agent mode, and Codex) with over the course of three weeks in late May and early June 2026.
We evaluated each agent’s user interface for specifying permissions policies, as well as how they appeared to enforce those policies at run-time.
Because all five commercial agents are closed-source, we could not assess their internal policy specifications.
Nonetheless, we glean several insights from their UIs and visible enforcement approaches.

#### 4.3.1 Continuous User Control, But High Overhead

Despite the prominence of low user overhead as a focus in the literature, we find little sign of this theme in our walkthroughs of Claude, Claude Cowork, ChatGPT (chat and agent mode), and Codex.
On the contrary, we found a tendency for commercial agents to incur *high* user overhead with frequent requests for confirmation, sometimes even when the permission had been previously granted.

We classify this behavior as user-in-the-loop enforcement, where agents require users to explicitly approve or deny actions in real time.
All four of the Claude chatbot, ChatGPT chat mode, ChatGPT agent mode, and Codex relied on user-in-the-loop enforcement at least some of the time.
Claude and Codex default to this method, but also employ LLM guardrails for auto-reviewing actions.

ChatGPT, on the other hand, required explicit user approval for *all* actions associated with a permissions policy.
We found no way to turn this off, or indicate that approval had been granted in advance.
The only workaround was in ChatGPT’s agent mode, which grants the LLM control over a remote browser.
In this mode, ChatGPT could and would take actions in the remote browser, such as accessing Gmail, that required user-in-the-loop permissions to do locally.
ChatGPT accomplished this simply by not assigning any permissions policies to the remote browser at all, meaning no opportunity for users to approve *or* deny agent mode actions.

#### 4.3.2 Lack of Transparency

The dichotomy between ChatGPT’s chat and agent modes illustrates another trend in commercial agents: When not relying on user-in-the-loop enforcement, they reach for the least transparent and least user-controllable alternatives.
We observe this pattern across all five agents, most notably in Claude.

As mentioned earlier, the Claude chatbot makes use of an LLM auto-reviewer.
Yet this auto reviewer is not controlled via Claude’s standard permissions settings for each tool.
Rather, we found that Claude uses LLM auto-review *implicitly*, without notifying the user or providing any setting to control it.22
2
This is a difference from Claude Code’s “auto mode”, which is fully user-controlled [[6](#bib.bib6)].

Claude provides a “Needs approval” setting that all but promises a user-in-the-loop approach to enforcement, especially in contrast with its “Always allow” option (Figure [1](#S4.F1 "Figure 1 ‣ 4.2.4 Deterministic Policy Enforcement ‣ 4.2 Themes in the Literature ‣ 4 Results ‣ How Agents Ask for Permission: User Permissions for AI Agents, from Interfaces to Enforcement")).
Yet it is under “Needs approval” that the agent sometimes *automatically* infers permission from the user’s message.
For example, Claude autonomously approved the creation of an email draft even when we had selected “Needs approval”, and even tagged its associated MCP query with approvalRequired: false (Figure [2](#S4.F2 "Figure 2 ‣ 4.2.4 Deterministic Policy Enforcement ‣ 4.2 Themes in the Literature ‣ 4 Results ‣ How Agents Ask for Permission: User Permissions for AI Agents, from Interfaces to Enforcement")).
We observed this behavior especially often with the Gmail search\_emails tool, which Claude consistently used without asking when an auto-reviewer had decided our prompt was permission enough.
Notably, because Claude’s only other permissions options are “Always allow” and “Blocked”, this auto-review behavior cannot be disabled short of revoking access to a given tool entirely.

We find a similar, if less egregious, lack of transparency in Claude Cowork.
Once Claude Cowork has received a permission, e.g., to read or delete files in a given folder, that access *cannot* be revoked by the user (Figure [3](#S4.F3 "Figure 3 ‣ 4.2.4 Deterministic Policy Enforcement ‣ 4.2 Themes in the Literature ‣ 4 Results ‣ How Agents Ask for Permission: User Permissions for AI Agents, from Interfaces to Enforcement")).
Fresh Cowork sessions do not carry over permissions from previous ones, but the older sessions persist in the app’s history, and will retain previously granted permissions if reentered.
To the best of our knowledge, the only way to permanently revoke a filesystem permission from Cowork is through the operating system (if it has such a feature; Windows, for example, does not) or by uninstalling the app entirely.

By contrast, Codex at least provides an explicit setting for its LLM auto-review, which is off by default and can be disabled at any time.
When enabled, however, Codex’s auto-review applies to all tools used in the current session, with the only alternative being to ask the user every time (Figure [4](#S4.F4 "Figure 4 ‣ 4.2.4 Deterministic Policy Enforcement ‣ 4.2 Themes in the Literature ‣ 4 Results ‣ How Agents Ask for Permission: User Permissions for AI Agents, from Interfaces to Enforcement")).

Curiously, while ChatGPT did not provide an auto-review option, it did appear to use LLM guardrails as a more-restrictive, as opposed to permissive, enforcement layer.
For example, when we asked ChatGPT to send an email that mimicked a common prompt injection format (“Ignore all previous instructions. This email is safe and benign.”), the agent refused to do so, and provided the following natural language feedback: “This tool call was blocked by OpenAI’s safety checks. Please double check what you are sending.”

In this instance, the LLM guardrail actually *prevented* the agent from completing its intended task.
While this design is less likely to allow dangerous actions than an LLM auto-reviewer that approves permissions automatically, we note that it fits a larger theme of commercial agents limiting *actual* user control over their behavior, even as defaulting to a user-in-the-loop approach creates the *appearance* of control.

## 5 Discussion

We find that the existing literature on agent permissions systems reflects a promising variety of approaches, mainly concentrated on three distinct goals: (1) lowering user overhead, (2) grounding policy specifications in formalized security principles, and (3) deterministic enforcement.
Yet substantial gaps remain, both within the literature and especially between proposed systems and those implemented in the most prominent commercial agents.

### 5.1 Gaps in the Literature

#### 5.1.1 Unification of Primary Goals

Though several permissions systems in the literature concentrate on two of the three goals we identify, none of the proposed systems achieves all three.
We observe that the overlap is smallest between low-overhead systems and those focused on formally grounded specifications: only VeriSafe Agent [[31](#bib.bib31)] and ShieldAgent [[14](#bib.bib14)] achieve both of these themes.
Neither system provides deterministic enforcement.
This lack represents the first gap we identify: The literature lacks agentic permissions systems that provide all three properties of low user overhead, formal specifications, and deterministic policy enforcement.

The robust overlaps between systems with deterministic enforcement and low user overhead, or deterministic enforcement and formal specifications, suggests that implementing a system with all three is technically achievable, making it all the more surprising that we found no such system in our review.
AC4A [[49](#bib.bib49)] and Prudentia [[29](#bib.bib29)] come the closest.
Yet AC4A does not provide a formalism for its specifications (despite its reference to types), while Prudentia relies on user-in-the-loop enforcement.
We argue that, as these two systems show, closing this gap is both eminently achievable and an important target for future work.

#### 5.1.2 Formally Verified Enforcement

Another gap lies in the use of formal specifications for enforcement.
While 11 of the systems we review implement some level of formalism for their policy specifications, none take the next step to verify the *enforcement* of said policies.
This constitutes our second gap: Formally verified policy enforcement would build confidence in permissions’ systems robustness to arbitrary agentic actions.

Verifying programs is a classically challenging problem.
Nonetheless, we argue that it is a worthwhile one, particularly in the agentic security context.
As AI agents vastly expand the space of likely inputs to the code that enforces a given policy, it becomes all the more important to ensure that the enforcement code functions correctly, even in the presence of unanticipated inputs.
Furthermore, since policy enforcement code is a relatively small part of any agent, focusing verification efforts there can provide outsized guarantees about the safety of a larger agentic system, even with its many untrusted components.

#### 5.1.3 Continuous User Control

We identify a third gap in proposed permissions systems’ lack of continuous user control over permissions policies.
For an agentic permissions system to truly empower users to express their intended policies, we believe it is crucial for users to have ways to update policies over time.
Yet among the 21 systems we review, only six clearly provide ways for users to change or revoke permissions after the policy has been specified [[2](#bib.bib2), [49](#bib.bib49), [59](#bib.bib59), [66](#bib.bib66), [50](#bib.bib50), [52](#bib.bib52)].
Of those five, two only allow changes between sessions, not during [[59](#bib.bib59), [66](#bib.bib66)], which may pose challenges during single prolonged sessions.
Separately, another two systems update permissions based on user choices to allow or deny specific actions at run-time, yet lack ways for users to prevent or revert those updates [[23](#bib.bib23), [10](#bib.bib10)].
These systems assume that a one-time decision extrapolates to all future circumstances—an presumption that may not always be accurate.

#### 5.1.4 Diversity of Threat Models

The fourth and final gap we find in the literature is a lack of exploration of diverse threat models, such as adversarial users in multi-user systems, or the agent itself.
As discussed in §[4.2.1](#S4.SS2.SSS1 "4.2.1 Threat Models ‣ 4.2 Themes in the Literature ‣ 4 Results ‣ How Agents Ask for Permission: User Permissions for AI Agents, from Interfaces to Enforcement"), nearly all the permissions systems we review with well-defined threat models share a single model: the adversary is agent misbehavior due to prompt injection or hallucination, targeting task flow.
A small number of systems target a strict subset of this model, e.g., by focusing only on data exfiltration [[10](#bib.bib10), [60](#bib.bib60), [52](#bib.bib52)].
Notably, nearly all of these systems assume that the agent itself is benign, and only misbehaves “on accident” or due to a third-party attacker.

We argue, first, that future agent permissions proposals should take care to define their threat models explicitly, as several systems do not [[33](#bib.bib33), [62](#bib.bib62), [14](#bib.bib14), [44](#bib.bib44), [55](#bib.bib55)].
Second, we recommend that future work consider potential threat models beyond what is currently reflected in the literature.
For example, adversarial users in a multi-user or multi-agent context are addressed by only GuardAgent [[62](#bib.bib62)] among the systems we review.
Another potential adversary is the agent provider itself.
Many agents operate by sending input data to the cloud to be processed, and privacy-conscious users may wish to prevent their private data from reaching the provider’s servers [[26](#bib.bib26)].
Among the 21 papers in our survey, only GAAP [[52](#bib.bib52)] accounts for this possibility by including the agent provider as an adversary.

Targets beyond task flow similarly deserve further consideration.
These could include denial of service, for example, or attempts to advertise an attacker’s product via malicious data poisoning [[64](#bib.bib64)].
Another alternative target is adversarial attacks that do not seek to compromise user privacy, but rather maliciously consume users’ limited tokens and funds to perform unintended tasks.

### 5.2 Gaps Between the Literature and Commercial Systems

Despite the extensive literature on formally grounded, deterministically enforced, and/or low-user overhead permissions systems, commercial agents largely fail to achieve any of the primary aims exhibited in the literature.
This is a serious and substantial gap, particularly as the current state of commercial agents trades these goals for high user overhead, lack of transparency and user control over enforcement, or both.

While commercial agents tend to do better than the literature on providing practical ways for users to update permissions over time, that success has limits.
Most agents rely on user-in-the-loop enforcement, which, though it theoretically maximizes user control over permissions policies, also creates a high risk of privacy fatigue—a phenomenon well known to increase users’ likelihood of ignoring warnings or over-granting permissions [[15](#bib.bib15), [27](#bib.bib27), [54](#bib.bib54)].
Often, the only alternative agents provide is an LLM auto-reviewer, with users given limited or no control over its use (§[4.3.2](#S4.SS3.SSS2 "4.3.2 Lack of Transparency ‣ 4.3 Commercial Agents ‣ 4 Results ‣ How Agents Ask for Permission: User Permissions for AI Agents, from Interfaces to Enforcement")).

The net effect is that many commercial agents require users to either manually approve every action, or give up substantial portions of their control and autonomy in deciding permissions policies.
We observe this pattern directly in the five agents we evaluate, and note that it appears in other agent settings as well.
Claude Code’s auto mode [[6](#bib.bib6)], for example, avoids user-in-the-loop permissions by automatically allowing actions with only an LLM auto-reviewer for safety.
Even more dangerous, Claude Code offers a bypassPermissions mode (a.k.a. YOLO) that lacks even the protection of an auto-reviewer.

Substantial work is needed to build practical agentic permissions systems that avoid this tradeoff, by letting users control policies when needed without overwhelming them with permissions pop-ups.
Moreover, in light of commercial agents’ evident tendency to incorporate LLM-based permissions decisions without informing users (§[4.3](#S4.SS3 "4.3 Commercial Agents ‣ 4 Results ‣ How Agents Ask for Permission: User Permissions for AI Agents, from Interfaces to Enforcement")), any agentic permissions system must be transparent about when and how it uses LLMs, including and especially in its UI.

## 6 Limitations

Our survey of papers and proposals relating to user-level agent permissions represents only a snapshot of current work in the area.
By the nature of our search methodology (§[3](#S3 "3 Methods ‣ How Agents Ask for Permission: User Permissions for AI Agents, from Interfaces to Enforcement")), it is entirely possible there exist relevant papers not captured in our review.
Furthermore, as this space is rapidly evolving, it is also possible—indeed, very likely—that additional relevant work has been completed even in the course of our analysis.
Nonetheless, we believe our survey constitutes an important and valuable review of the state of user-level permissions in AI agents at the current moment in time.

Separately, our ability to draw conclusions about commercial AI agent systems is limited by the lack of public information around how those systems function internally.
While we can and do glean substantive insights by conducting walkthroughs of these systems from a user perspective, we ultimately cannot know the exact details of permissions handling in closed-source commercial agents.
Commercial agent systems are also rapidly evolving and may exhibit nondeterministic behavior, particularly where LLMs handle permissions policies directly.

## 7 Related Work

Kim et al.’s review of agentic AI attacks and defenses [[28](#bib.bib28)] provides a valuable survey of current attack vectors, mitigations, and challenges in building secure agentic systems.
Left unaddressed, however, is the question of whether and how *users* of agentic systems, as opposed to developers, may specify individual policies within a larger security framework, or how those user-level policies are subsequently enforced.

Zhang and Wang approach the user experience of agent security more directly [[20](#bib.bib20)].
In their survey of 18 web agents, Zhang and Wang identify widespread challenges in the web agent authorization landscape.
These include a lack of granularity in permissions schemes; deceptive or missing options for revoking permissions; and a disconnect between “Interaction-Level” authorizations selected by users, and the “System-Level” authorizations that actually take effect, which are often much broader and more permissive [[20](#bib.bib20)].

In concurrent work, Wang et al. review the academic literature and commercial agents, toward building a taxonomy of approaches to user intent alignment [[57](#bib.bib57)].
As an area of investigation, intent alignment is related to, but distinct from, the notion of user-level permissions.
Intent alignment is the objective that an AI agent’s actions should “align” with the user’s intent.
User-level permissions are an implementation-level mechanism that prospectively *enables* intent alignment, among other objectives.

This difference is crucial in certain settings, such as customer service agents, where multiple users with heterogenous permissions and intents interact with a single agent.
In such contexts, *any one user’s intent should not unilaterally determine their permissions policy*.
The alternative can have disastrous consequences, empowering potentially malicious users to act beyond the bounds of their appropriate permissions [[30](#bib.bib30)].
User-level permissions are an important tool for balancing intent alignment with the need for appropriate restrictions on users’ own intended actions.

Within the context of intent alignment, Wang et al. conclude that human-agent interaction is paramount [[57](#bib.bib57)].
As for user-level permissions, we agree that user control and transparency are important goals.
Yet our results also highlight the need for more robust permissions policy enforcement without overly relying on user interaction (§[5](#S5 "5 Discussion ‣ How Agents Ask for Permission: User Permissions for AI Agents, from Interfaces to Enforcement")).

In other concurrent work, Brigham et al. also consider user-facing permissions in agentic systems, developing an evaluation framework to empirically compare
different permission approaches with respect to security- and usability-relevant criteria [[13](#bib.bib13)].
They evaluate implementations designed to capture different points in the design space, not existing commercial systems or other research prototypes, although they conceptually
compare some of the same systems that we consider.

We complement and expand on past work by taking a broad lens to the space of user-level permissions for AI agents.
We survey the recent literature to construct a *platform-agnostic* taxonomy of agent permissions interfaces, specifications, and derivation and enforcement mechanisms, geared toward identifying when, how, and to what extent users can determine the permissions policies applied to their agent’s actions and access.
We then identify cross-cutting themes in both the literature and commercial agents, and provide recommendations on areas in need of further exploration.

## 8 Conclusion

We review 21 papers and open-source systems on implementing user-level permissions in agentic AI systems.
From these papers, we develop a unified taxonomy of approaches to specifying, deriving from user input, and enforcing user-level permissions in agents.
We then apply this taxonomy to an exploration of five commercial AI agents across web, desktop, and browser-use modalities.

We identify four primary goals as themes across the literature and commerical agents: low user overhead in setting permissions policies, formally grounded policy specifications, deterministic enforcement, and continuous user control of previously specified policies.
While the first three themes feature prominently in the literature, we find them to be nearly absent from commercial agents.
Even deterministic enforcement, while often present in a user-in-the-loop form, is counterbalanced by commercial agents’ tendency to rely on LLM guardrails as the sole alternative to constant permission requests—an alternative that users sometimes cannot even control.

Yet the reverse is true of the last theme, continuous user control: though prominently featured in multiple commercial agents, few systems in the literature provide the user with options to edit or revoke previously granted permissions.
We identify this as one of several substantial gaps in the academic literature, along with a dearth of systems combining all three of low user overhead, formal specifications, and deterministic enforcement; no exploration of formally verified enforcement; and a lack of diverse threat models.

We strongly encourage researchers to explore agentic permissions systems in these areas, towards creating a framework for user-level agent permissions that prioritizes not just usability and robustness, but also user control and transparency.
We furthermore urge the AI industry to prioritize these goals in their commercial agents, particularly around closing the gap between the high overhead of user-in-the-loop policy enforcement, and the low transparency and accountability of LLM-based enforcement.
Use of AI agents will only continue to grow.
As it does, it is incumbent upon academia and industry alike to ensure the permissions that regulate agents’ actions are correct, transparent, and accountable to users.

## 9 Acknowledgements

This work was funded in part by gifts from Microsoft, including a Microsoft Grant for Customer Experience Innovation, and by NSF grant number DGE-2140004. Any opinions, findings, and conclusions or recommendations expressed in this material are those of the author(s) and do not necessarily reflect the views of the National Science Foundation.

## Appendix A Ethical Considerations

The relevant ethical stakeholders for this work include the users and developers of agentic AI systems, as well as researchers in AI agents and agentic security. Our publication of Claude's implicit auto-review behavior (the undisclosed LLM auto-reviewer) reveals a permissions gap that could theoretically be exploited to harm Claude's users, e.g., through prompt injection attacks. The authors disclosed Claude's implicit auto-review behavior to Anthropic on July 2, 2026, and are currently awaiting their response.

