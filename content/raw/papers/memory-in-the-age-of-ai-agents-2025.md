---
title: "Memory in the Age of AI Agents: A Survey"

source_url: https://arxiv.org/abs/2512.13564
ingested: 2026-05-20
pdf: raw/papers/memory-in-the-age-of-ai-agents-2025.pdf
arxiv_id: 2512.13564
authors:
  - Yuyang Hu (Core Supervisor, Renmin University)
  - Shichun Liu (Core Contributor, Fudan University)
  - Yanwei Yue (Core Contributor, Peking University)
  - Guibin Zhang (Project Organizer, NUS)
  - Boyang Liu
  - Fangyi Zhu
  - Jiahang Lin
  - Honglin Guo
  - Shihan Dou
  - Zhiheng Xi
  - Senjie Jin
  - Jiejun Tan
  - Yanbin Yin
  - Jiongnan Liu
  - Zeyu Zhang
  - Zhongxiang Sun
  - Yutao Zhu
  - Hao Sun
  - Boci Peng
  - Zhenrong Cheng
  - Xuanbo Fan
  - Jiaxin Guo
  - Xinlei Yu
  - Zhenhong Zhou
  - Zewen Hu
  - Jiahao Huo
  - Junhao Wang
  - Yuwei Niu
  - Yu Wang
  - Zhenfei Yin
  - Xiaobin Hu
  - Yue Liao
  - Qiankun Li
  - Kun Wang
  - Wangchunshu Zhou
  - Yixin Liu
  - Dawei Cheng
  - Qi Zhang
  - Tao Gui (Core Supervisor)
  - Shirui Pan
  - Yan Zhang (Core Supervisor)
  - Philip Torr (Oxford University)
  - Zhicheng Dou (Core Supervisor)
  - Ji-Rong Wen
  - Xuanjing Huang (Core Supervisor)
  - Yu-Gang Jiang
  - Shuicheng Yan (Core Supervisor)
categories: [cs.CL, cs.AI]
submitted: 2025-12-15
revised: 2026-01-13
affiliations:
  - National University of Singapore
  - Renmin University of China
  - Fudan University
  - Peking University
  - Nanyang Technological University
  - Tongji University
  - UC San Diego
  - HKUST (Guangzhou)
  - Griffith University
  - Georgia Institute of Technology
  - OPPO
  - Oxford University
total_authors: 46
pages: 76
---

Memory in the Age of AI Agents: A Survey
Forms, Functions and Dynamics
Yuyang Hu† , Shichun Liu† , Yanwei Yue† , Guibin Zhang†ò , Boyang Liu , Fangyi Zhu , Jiahang Lin ,
Honglin Guo , Shihan Dou , Zhiheng Xi , Senjie Jin , Jiejun Tan , Yanbin Yin , Jiongnan Liu , Zeyu Zhang ,
Zhongxiang Sun , Yutao Zhu , Hao Sun , Boci Peng , Zhenrong Cheng , Xuanbo Fan , Jiaxin Guo , Xinlei Yu ,
Zhenhong Zhou , Zewen Hu , Jiahao Huo , Junhao Wang , Yuwei Niu , Yu Wang , Zhenfei Yin , Xiaobin Hu ,
Yue Liao , Qiankun Li , Kun Wang , Wangchunshu Zhou , Yixin Liu , Dawei Cheng , Qi Zhang , Tao Gui‡ ,
Shirui Pan , Yan Zhang‡ , Philip Torr , Zhicheng Dou‡ , Ji-Rong Wen , Xuanjing Huang‡ , Yu-Gang Jiang ,
Shuicheng Yan‡

arXiv:2512.13564v2 [cs.CL] 13 Jan 2026

†

Core Contributors with Names Listed Alphabetically. ò Project Organizer. ‡ Core Supervisors.

Affiliations: National University of Singapore, Renmin University of China, Fudan University,

Peking University, Nanyang Technological University, Tongji University, University of California
San Diego, Hong Kong University of Science and Technology (Guangzhou), Griffith University,
Georgia Institute of Technology, OPPO, Oxford University
Memory has emerged, and will continue to remain, a core capability of foundation model-based agents.
It underpins long-horizon reasoning, continual adaptation, and effective interaction with complex
environments. As research on agent memory rapidly expands and attracts unprecedented attention,
the field has also become increasingly fragmented. Existing works that fall under the umbrella of
agent memory often differ substantially in their motivations, implementations, assumptions, and
evaluation protocols, while the proliferation of loosely defined memory terminologies has further
obscured conceptual clarity. Traditional taxonomies such as long/short-term memory have proven
insufficient to capture the diversity and dynamics of contemporary agent memory systems. This
survey aims to provide an up-to-date and comprehensive landscape of current agent memory research.
We begin by clearly delineating the scope of agent memory and distinguishing it from related concepts
such as LLM memory, retrieval augmented generation (RAG), and context engineering. We then
examine agent memory through the unified lenses of forms, functions, and dynamics. From the
perspective of forms, we identify three dominant realizations of agent memory, namely token-level,
parametric, and latent memory. From the perspective of functions, we move beyond coarse temporal
categorizations and propose a finer-grained taxonomy that distinguishes factual, experiential, and
working memory. From the perspective of dynamics, we analyze how memory is formed, evolved, and
retrieved over time as agents interact with their environments. To support empirical research and
practical development, we compile a comprehensive summary of representative benchmarks and open
source memory frameworks. Beyond consolidation, we articulate a forward-looking perspective on
emerging research frontiers, including automation-oriented memory design, the deep integration of
reinforcement learning with memory systems, multimodal memory, shared memory for multi-agent
systems, and trustworthiness issues. We hope this survey serves not only as a reference for existing
work, but also as a conceptual foundation for rethinking memory as a first-class primitive in the design
of future agentic intelligence.
# Main Contact: guibinz@u.nus.edu, yuyang.hu@ruc.edu.cn, liusc24@m.fudan.edu.cn, ywyue25@stu.pku.edu.cn
Github: https://github.com/Shichun-Liu/Agent-Memory-Paper-List

Note: If you identify your own or other papers relevant to this survey that have not been discussed (we apologize for any
such omissions due to the rapidly expanding literature), please feel free to contact us via email or raise an issue on GitHub.

1

Contents
1 Introduction

4

2 Preliminaries: Formalizing Agents and Memory
2.1 LLM-based Agent Systems . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
2.2 Agent Memory Systems . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
2.3 Comparing Agent Memory with Other Key Concepts . . . . . . . . . . . . . . . . . . . . . . .
2.3.1 Agent Memory vs. LLM Memory . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
2.3.2 Agent Memory vs. RAG . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
2.3.3 Agent Memory vs. Context Engineering . . . . . . . . . . . . . . . . . . . . . . . . . .

6
6
7
8
9
10
11

3 Form: What Carries Memory?
3.1 Token-level Memory . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
3.1.1 Flat Memory (1D) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
3.1.2 Planar Memory (2D) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
3.1.3 Hierarchical Memory (3D) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
3.2 Parametric Memory . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
3.2.1 Internal Parametric Memory . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
3.2.2 External Parametric Memory . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
3.3 Latent Memory . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
3.3.1 Generate . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
3.3.2 Reuse . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
3.3.3 Transform . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
3.4 Adaptation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

12
13
15
20
21
22
22
24
26
26
28
28
30

4 Functions: Why Agents Need Memory?
4.1 Factual Memory . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
4.1.1 User factual memory . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
4.1.2 Environment factual memory . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
4.2 Experiential Memory . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
4.2.1 Case-based Memory . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
4.2.2 Strategy-based Memory . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
4.2.3 Skill-based Memory . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
4.2.4 Hybrid memory . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
4.3 Working Memory . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
4.3.1 Single-turn Working Memory . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
4.3.2 Multi-turn Working Memory . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

31
32
35
36
37
39
40
41
42
42
43
45

5 Dynamics: How Memory Operates and Evolves?
5.1 Memory Formation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
5.1.1 Semantic Summarization . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
5.1.2 Knowledge Distillation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
5.1.3 Structured Construction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
5.1.4 Latent Representation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
5.1.5 Parametric Internalization . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
5.2 Memory Evolution . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
5.2.1 Consolidation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
5.2.2 Updating . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
5.2.3 Forgetting . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
5.3 Memory Retrieval . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
5.3.1 Retrieval Timing and Intent . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
5.3.2 Query Construction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
5.3.3 Retrieval Strategies . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
5.3.4 Post-Retrieval Processing . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

46
48
48
50
51
53
54
55
55
57
58
59
60
62
62
64

2

6 Resources and Frameworks
6.1 Benchmarks and Datasets . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
6.1.1 Benchmarks for Memory / Lifelong / Self-Evolving Agents . . . . . . . . . . . . . . .
6.1.2 Other Related Benchmarks . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
6.2 Open-Source Frameworks . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

65
65
65
67
68

7 Positions and Frontiers
7.1 Memory Retrieval vs. Memory Generation . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
7.1.1 Look Back: From Memory Retrieval to Memory Generation . . . . . . . . . . . . . . .
7.1.2 Future Perspective . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
7.2 Automated Memory Management . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
7.2.1 Look-Back: From Hand-crafted to Automatically Constructed Memory Systems. . . .
7.2.2 Future Perspective . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
7.3 Reinforcement Learning Meets Agent Memory . . . . . . . . . . . . . . . . . . . . . . . . . . .
7.3.1 Look-Back: RL is Internalizing Memory Management Abilities for Agents. . . . . . . .
7.3.2 Future Perspective . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
7.4 Multimodal Memory . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
7.4.1 Look-Back . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
7.4.2 Future Perspective . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
7.5 Shared Memory in Multi-Agent Systems . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
7.5.1 Look-Back: From Isolated Memories to Shared Cognitive Substrates . . . . . . . . . .
7.5.2 Future Perspective . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
7.6 Memory for World Model . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
7.6.1 Look-Back . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
7.6.2 Future Perspective . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
7.7 Trustworthy Memory . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
7.7.1 Look-Back: From Trustworthy RAG to Trustworthy Memory . . . . . . . . . . . . . .
7.7.2 Future Perspective . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
7.8 Human-Cognitive Connections . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
7.8.1 Look Back . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
7.8.2 Future Perspective . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

69
69
69
69
70
70
70
71
71
72
72
72
73
73
73
73
74
74
74
75
75
75
76
76
76

8 Conclusion

76

3

Figure 1 Overview of agent memory organized by the unified taxonomy of forms (Section 3), functions (Section 4),

and dynamics (Section 5). The diagram positions memory artifacts by their dominant form and primary function. It
further maps representative systems into this taxonomy to provide a consolidated landscape.

1

Introduction

The past two years have witnessed the overwhelming evolution of increasingly capable large language models
(LLMs) into powerful AI agents (Matarazzo and Torlone, 2025; Minaee et al., 2025; Luo et al., 2025a).
These foundation-model-powered agents have demonstrated remarkable progress across diverse domains
such as deep research (Xu and Peng, 2025; Zhang et al., 2025p), software engineering (Wang et al., 2024i),
and scientific discovery (Wei et al., 2025c), continuously advancing the trajectory toward artificial general
interlligence (AGI) (Fang et al., 2025a; Durante et al., 2024). Although early conceptions of “agents” were
highly heterogeneous, a growing consensus has since emerged within the community: beyond a pure LLM
backbone, an agent is typically equipped with capabilities such as reasoning, planning, perception, memory, and
tool-use. Some of these abilities, such as reasoning and tool-use, have been largely internalized within model
parameters through reinforcement learning (Wang et al., 2025m; Qu et al., 2025b), while some still depend
heavily on external agentic scaffolds. Together, these components transform LLMs from static conditional
generators into learnable policies that can interact with diverse external environments and adaptively evolve
over time (Zhang et al., 2025f; Liu et al., 2025a).
Among these agentic faculties, memory stands out as a cornerstone, explicitly enabling the transformation
of static LLMs, whose parameters cannot be rapidly updated, into adaptive agents capable of continual
adaptation through environmental interaction (Zhang et al., 2025s; Wu et al., 2025g). From an application
perspective, numerous domains demand agents with proactive memory management rather than ephemeral,
forgetful behaviors: personalized chatbots (Chhikara et al., 2025; Li et al., 2025b), recommender systems (Liu
et al., 2025c), social simulations (Park et al., 2023; Yang et al., 2025), and financial investigations (Zhang
et al., 2024) all rely on the agent’s ability to process, store, and manage historical information. From a
developmental standpoint, one of the defining aspirations of AGI research is to endow agents with the capacity
for continual evolution through environment interactions (Hendrycks et al., 2025), a capability fundamentally
4

grounded in agent memory.
Agent Memory Needs A New Taxonomy Given the growing significance and community attention
surrounding agent memory systems, it has become both timely and necessary to provide an updated perspective
on contemporary agent memory research. The motivation for a new taxonomy and survey is twofold: ❶
Limitations of Existing Taxonomies: While several recent surveys have provided valuable and comprehensive
overviews of agent memory (Zhang et al., 2025s; Wu et al., 2025g), their taxonomies were developed prior to a
number of rapid methodological advances and therefore do not fully reflect the current breadth and complexity
of the research landscape. For example, emerging directions in 2025, such as memory frameworks that distill
reusable tools from past experiences (Qiu et al., 2025a,c; Zhao et al., 2025c), or memory-augmented test-time
scaling methods (Zhang et al., 2025g; Suzgun et al., 2025), remain underrepresented in earlier classification
schemes. ❷ Conceptual Fragmentation: With the explosive growth of memory-related studies, the concept
itself has become increasingly expansive and fragmented. Researchers often find that papers claiming to study
“agent memory” differ drastically in implementation, objectives, and underlying assumptions. The proliferation
of diverse terminologies (declarative, episodic, semantic, parametric memory, etc.) further obscures conceptual
clarity, highlighting the urgent need for a coherent taxonomy that can unify these emerging concepts.
Therefore, this paper seeks to establish a systematic framework that reconciles existing definitions, bridges
emerging trends, and elucidates the foundational principles of memory in agentic systems. Specifically, this
survey aims to address the following key questions:
Key Questions
❶ How is agent memory defined, and how does it relate to related concepts such as LLM memory,
retrieval-augmented generation (RAG), and context engineering?
❷ Forms: What architectural or representational forms can agent memory take?
❸ Functions: Why is agent memory needed, and what roles or purposes does it serve?
❹ Dynamics: How does agent memory operate, adapt, and evolve over time?
❺ What are the promising frontiers for advancing agent memory research?
To address question ❶, we first provide formal definitions for LLM-based agents and agent memory systems
in Section 2, and present a detailed comparison between agent memory and related concepts such as LLM
memory, RAG, and context engineering. Following the “Forms–Functions–Dynamics” triangle, we offer a
structured overview of agent memory. Question ❷ examines the architectural forms of memory, which we
discuss in Section 3, highlighting three mainstream implementations: token-level, parametric, and latent
memory. Question ❸ concerns the functional roles of memory, addressed in Section 4, where we distinguish
between factual memory, which records knowledge from agents’ interactions with users and the environment;
experiential memory, which incrementally enhances the agent’s problem-solving capabilities through task
execution; and working memory, which manages workspace information during individual task instances.
Question ❹ focuses on the lifecycle and operational dynamics of agent memory, which we present sequentially
in terms of memory formulation, retrieval, and evolution.
After surveying existing research through the lenses of “Forms–Functions–Dynamics,” we further provide our
perspectives and insights on agent memory research. To facilitate knowledge sharing and future development,
we first summarize key benchmarks and framework resources in Section 6. Building upon this foundation, we
then address question ❺ by exploring several emerging yet underdeveloped research frontiers in Section 7,
including automation-oriented memory design, the integration of reinforcement learning (RL), multimodal
memory, shared memory for multi-agent systems, and trustworthy issues.
Contributions The contributions of this survey can be summarized as follows: (1) We present an up-todate and multidimensional taxonomy of agent memory from the perspective of “forms–functions–dynamics,”
offering a structured lens through which to understand current developments in the field. (2) We provide
an in-depth discussion on the suitability and interplay of different memory forms and functional purposes,
5

offering insights into how various memory types can be effectively aligned with distinct agentic objectives.
(3) We investigate emerging and promising research directions in agent memory, thereby outlining future
opportunities and guiding pathways for advancement. (4) We compile a comprehensive collection of resources,
including benchmarks and open-source frameworks, to support both researchers and practitioners in further
exploration of agent memory systems.
Outline of the Survey The remainder of this survey is organized as follows. Section 2 formalizes LLM-based
agents and agent memory systems, and clarifies their relationships with related concepts. Section 3, Section 4,
and Section 5 respectively examine the forms, functions, and dynamics of agent memory. Section 6 summarizes
representative benchmarks and framework resources. Section 7 discusses emerging research frontiers and
future directions. Finally, we conclude the survey with a summary of key insights in Section 8.

2

Preliminaries: Formalizing Agents and Memory

LLM agents increasingly serve as the decision-making core of interactive systems that operate over time,
manipulate external tools, and coordinate with humans or other agents. To study memory in such settings,
we begin by formalizing LLM-based agent systems in a manner that encompasses both single-agent and
multi-agent configurations. We then formalize the memory system coupled to the agent’s decision process
through read/write interactions, enabling a unified treatment of memory phenomena that arise both within a
task (inside-trial / short-term memory) and across tasks (cross-trial / long-term memory).

2.1

LLM-based Agent Systems

Agents and Environment Let I = {1, . . . , N } denote the index set of agents, where N = 1 corresponds
to the single-agent case (e.g., ReAct), and N > 1 represents multi-agent settings such as debate (Li et al.,
2024c) or planner–executor architectures (Wan et al., 2025). The environment is characterized by a state
space S. At each time step t, the environment evolves according to a controlled stochastic transition model
st+1 ∼ Ψ(st+1 | st , at ),
where at denotes the action executed at time t. In multi-agent systems, this abstraction allows for either sequential decision-making (where a single agent acts at each step) or implicit coordination through
environment-mediated effects. Each agent i ∈ I receives an observation
oit = Oi (st , hit , Q),
where hit denotes the portion of the interaction history visible to agent i. This history may include previous
messages, intermediate tool outputs, partial reasoning traces, shared workspace states, or other agents’
contributions, depending on the system design. Q denotes the task specification, such as a user instruction,
goal description, or external constraints, which is treated as fixed within a task unless otherwise specified.
Action Space A distinguishing feature of LLM-based agents is the heterogeneity of their action space.
Rather than restricting actions to plain text generation, agents may operate over a multimodal and semantically
structured action space, including:
• Natural-language generation, such as producing intermediate reasoning, explanations, responses, or instructions (Li et al., 2023b; Wu et al., 2024b; Hong et al., 2024; Qian et al., 2024).
• Tool invocation actions, which call external APIs, search engines, calculators, databases, simulators, or code
execution environments (Qin et al., 2025; Li et al., 2025h; Zhou et al., 2023c, 2024c).
• Planning actions, which explicitly output task decompositions, execution plans, or subgoal specifications to
guide later behavior (CAMEL-AI, 2025; Liu et al., 2025g; Pan et al., 2024).
• Environment-control actions, where the agent directly manipulates the external environment (e.g., navigation
in embodied settings (Shridhar et al., 2021; Wang et al., 2022a), editing a software repository (Jimenez
et al., 2024; Aleithan et al., 2024), or modifying a shared memory buffer).
6

• Communication actions, enabling collaboration or negotiation with other agents through structured
messages (Marro et al., 2024).
These actions, though diverse in semantics, are unified by the fact that they are produced through an
autoregressive LLM backbone conditioned on a contextual input. Formally, each agent i follows a policy
at = πi (oit , mit , Q),
where mit is a memory-derived signal defined in Section 2.2. The policy may internally generate multi-step
reasoning chains, latent deliberation, or scratchpad computations prior to emitting an executable action; such
internal processes are abstracted away and not explicitly modeled.
Interaction Process and Trajectories

A full execution of the system induces a trajectory

τ = (s0 , o0 , a0 , s1 , o1 , a1 , . . . , sT ),
where T is determined by task termination conditions or system-specific stopping criteria. At each step,
the trajectory reflects the interleaving of (i) environment observation, (ii) optional memory retrieval, (iii)
LLM-based computation, and (iv) action execution that drives the next state transition.
This formulation captures a broad class of agentic systems, ranging from a single agent solving reasoning
tasks with tool augmentation to teams of role-specialized agents collaboratively developing software (Qian
et al., 2024; Wang et al., 2025l) or conducting scientific inquiry (Weng et al., 2025). We next formalize the
memory systems that integrate into this agent loop.

2.2

Agent Memory Systems

While an LLM-based agent interacts with an environment, its instantaneous observation oit is often insufficient
for effective decision-making. Agents therefore rely on additional information derived from prior interactions,
both within the current task and across previously completed tasks. We formalize this capability through a
unified agent memory system, represented as an evolving memory state
Mt ∈ M,
where M denotes the space of admissible memory configurations. No specific internal structure is imposed
on Mt ; it may take the form of a text buffer, key–value store, vector database, graph structure, or any
hybrid representation. At the beginning of a task, Mt may already contain information distilled from prior
trajectories (cross-trial memory). During task execution, new information accumulates and functions as
short-term, task-specific memory. Both roles are supported within a single memory container, with temporal
distinctions emerging from usage patterns rather than architectural separation.
Memory Lifecycle: Formation, Evolution, and Retrieval The dynamics of the memory system are
characterized by three conceptual operators.
Memory Formation At time step t, the agent produces informational artifacts ϕt , which may include tool

outputs, reasoning traces, partial plans, self-evaluations, or environmental feedback. A formation operator
Mform
t+1 = F (Mt , ϕt )

selectively transforms these artifacts into memory candidates, extracting information with potential future
utility rather than storing the entire interaction history verbatim.
Memory Evolution Formed memory candidates are integrated into the existing memory base through an

evolution operator

Mt+1 = E(Mform
t+1 ),

which may consolidate redundant entries (Zhao et al., 2024), resolve conflicts (Rasmussen et al., 2025; Li
et al., 2025l), discard low-utility information (Wang et al., 2025r), or restructure memory for efficient retrieval.
The resulting memory state persists across subsequent decision steps and tasks.
7

Memory Retrieval When selecting an action, agent i retrieves a context-dependent memory signal

mit = R(Mt , oit , Q),
where R denotes a retrieval operator that constructs a task-aware query and returns relevant memory content.
The retrieved signal mit is formatted for direct consumption by the LLM policy, for example as a sequence of
textual snippets or a structured summary.
Temporal Roles Within the Agent Loop Although memory is represented as a unified state Mt , the
three lifecycle operators (formation F , evolution E, and retrieval R) need not be invoked at every time step.
Instead, different memory effects arise from distinct temporal invocation patterns. For instance, some systems
perform retrieval only once at task initialization,
(
R(M0 , oi0 , Q), t = 0,
i
mt =
⊥,
t > 0,
where ⊥ denotes null retrieval strategy. Others may retrieve memory intermittently or continuously based on
contextual triggers. Similarly, memory formation may range from minimal accumulation of raw observations,
i
Mform
t+1 = Mt ∪ {ot },

to sophisticated extraction and refinement of reusable patterns or abstractions. Thus, inside a task, short-term
memory effects may arise from lightweight logging just as in Yao et al. (2023b); Chen et al. (2023a) or from
more elaborate iterative refinement (Hu et al., 2025a); across tasks, long-term memory may be updated
episodically at task boundaries or continuously throughout operation. Short-term and long-term memory
phenomena therefore emerge not from discrete architectural modules but from the temporal patterns with
which formation, evolution, and retrieval are engaged.
Memory–Agent Coupling The interaction between memory and the agent’s decision process is similarly
flexible. In general, the agent policy is written as
at = πi (oit , mit , Q),
where the retrieved memory signal mit may be present or absent depending on the retrieval schedule. When
retrieval is disabled at a given step, mit can be treated as a distinguished null input.
Consequently, the overall agent loop consists of observing the environment, optionally retrieving memory,
computing an action, receiving feedback, and optionally updating memory through formation and evolution. Different agent implementations instantiate different subsets of these operations at different temporal
frequencies, giving rise to memory systems that range from passive buffers to actively evolving knowledge
bases.

2.3

Comparing Agent Memory with Other Key Concepts

Despite the growing interest in agentic systems endowed with memory, the community’s understanding of what
constitutes agent memory remains fragmented. In practice, researchers and practitioners often conflate agent
memory with related constructs such as LLM memory (Wu et al., 2025g), retrieval-augmented generation
(RAG) (Gao et al., 2024), and context engineering (Mei et al., 2025). Although these concepts are intrinsically
connected by their involvement in how information is managed and utilized in LLM-driven systems, they
differ in scope, temporal characteristics, and functional roles.
These overlapping yet distinct notions have led to ambiguity in the literature and practice. To clarify these
distinctions and situate agent memory within this broader landscape, we examine how agent memory relates
to, and diverges from, LLM memory, RAG, and context engineering in the subsequent subsubsections. Figure 2
visually illustrates the commonalities and distinctions among these fields through a Venn diagram.

8

- Self-Evolving Memory
- Parametric Memory
e.g., Memento, H2R
e.g., Retroformer, Early experience
- Multimodal Memory
- RL-enabled Memory
e.g., Ella, ViloMem, M3-Agent
e.g., MemAgent, RMM, MemSearcher,
- Latent Memory
e.g., MemoryLLM, M+, MemGen MEM1, Mem-alpha, Memory-R1

Agent
Memory

- Memory graph
e.g., Zep, AriGraph
- Agentic memory
e.g., A-Mem, G-Memory
- Working memory
e.g., HiAgent, ReSum,

- Modular RAG
e.g., FlashRAG, ComposeRAG
- Graph RAG
e.g., LightRAG, HippoRAG
- Agentic RAG
e.g., PlanRAG, Self-RAG

- Few-shot prompting
e.g., CoT, PALM
- Self-Reflection
e.g., Self-refine, CRITIC
- KV compression/reuse
e.g., AutoCompressor, SnapKV

LLM
Memory

RAG

Context
Engineering

- Attention KV management
e.g., Mixture-of-Memory
- Long context processing
e.g., Mamba, Memformer, MoA,
Sparseformer, NSA

- Tool-integrated reasoning
e.g., ReTool, ToolLLM,
Toolformer, VTool-R1, ToRL
- Tool selection
e.g., AutoTool, VisTA
- Communication protocol
e.g., ANP, A2A, MCP, Agora

Figure 2 Conceptual comparison of Agent Memory with LLM Memory, RAG, and Context Engineering. The diagram

illustrates shared technical implementations (e.g., KV reuse, graph retrieval) while highlighting fundamental distinctions:
unlike the architectural optimizations of LLM Memory, the static knowledge access of RAG, or the transient resource
management of Context Engineering, Agent Memory is uniquely characterized by its focus on maintaining a persistent
and self-evolving cognitive state that integrates factual knowledge and experience. The listed categories and examples
are illustrative rather than strictly parallel, serving as representative reference points to clarify conceptual relationships
rather than to define a rigid taxonomy.

2.3.1

Agent Memory vs. LLM Memory

At a high level, agent memory almost fully subsumes what has traditionally been referred to as LLM memory.
Since 2023, many works describing themselves as “LLM memory mechanisms” (Zhong et al., 2024; Packer
et al., 2023a; Wang et al., 2023b) are more appropriately interpreted, under contemporary terminology, as
early instances of agent memory. This reinterpretation arises from the historical ambiguity surrounding the
very notion of an “LLM agent.” During 2023–2024, the community had no stable or coherent definition: in
some cases, prompting an LLM to call a calculator already sufficed to qualify the system as an agent (Wu
et al., 2024c); in other cases, agency required substantially richer capabilities such as explicit planning, tool
use, memory, and reflective reasoning (Ruan et al., 2023). Only recently has a more unified and structured
definition begun to emerge (e.g., LLM-based agent = LLM + reasoning + planning + memory + tool use
+ self-improvement + multi-turn interaction + perception, as discussed by Zhang et al. (2025f)), though
even this formulation is not universally applicable. Against this historical backdrop, early systems such
as MemoryBank (Zhong et al., 2024) and MemGPT (Packer et al., 2023a) framed their contributions as
providing LLM memory. Yet what they fundamentally addressed were classical agentic challenges, for example
enabling an LLM-based conversational agent to track user preferences, maintain dialogue-state information,
and accumulate experience across multi-turn interactions. Under a modern and more mature understanding
of agency, such systems are naturally categorized as instances of agent memory.
That said, the subsumption is not absolute. A distinct line of research genuinely concerns LLM-internal
memory: managing the transformer’s key–value (KV) cache, designing long-context processing mechanisms,
or modifying model architectures (e.g., RWKV (Peng et al., 2023), Mamba (Gu and Dao, 2024; Lieber et al.,
2024), diffusion-based LMs (Nie et al., 2025)) to better retain information as sequence length grows. These
works focus on intrinsic model dynamics and typically address tasks that do not require agentic behavior, and
thus should be considered outside the scope of agent memory.

9

Overlap Within our taxonomy, the majority of what has historically been called “LLM memory” corresponds
to forms of agent memory. Techniques such as few-shot prompting (Prabhumoye et al., 2022; Ma et al., 2023a)
can be viewed as a form of long-term memory, where past exemplars or distilled task summaries serve as
reusable knowledge incorporated through retrieval or context injection. Self-reflection and iterative refinement
methods (Madaan et al., 2023; Mousavi et al., 2023; Han et al., 2025c) naturally align with short-term,
inside-trial memory, as the agent repeatedly leverages intermediate reasoning traces or outcomes from prior
attempts within the same task. Even KV compression and context-window management (Yoon et al., 2024;
Jiang et al., 2023), when used to preserve salient information across the course of a single task, function
as short-term memory mechanisms in an agentic sense. These techniques all support the agent’s ability to
accumulate, transform, and reuse information throughout a task’s execution.
Distinctions In contrast, memory mechanisms that intervene directly in the model’s internal state—such as
architectural modifications for longer effective context, cache rewriting strategies, recurrent-state persistence,
attention-sparsity mechanisms, or externalized KV-store expansions—are more appropriately classified as
LLM memory rather than agent memory. Their goal is to expand or reorganize the representational capacity
of the underlying model, not to furnish a decision-making agent with an evolving external memory base.
They do not typically support cross-task persistence, environment-driven adaptation, or deliberate memory
operations (e.g., formation, evolution, retrieval), and therefore lie outside the operational scope of agent
memory as defined in this survey.
2.3.2

Agent Memory vs. RAG

At a conceptual level, agent memory and retrieval-augmented generation (RAG) exhibit substantial overlap:
both systems construct, organize, and leverage auxiliary information stores to extend the capabilities of
LLM/agents beyond their native parametric knowledge. For instance, structured representations such as
knowledge graphs and indexing strategies appear in both communities’ methods, and recent developments in
agentic RAG demonstrate how autonomous retrieval mechanisms can interact with dynamic databases in ways
reminiscent of agent memory architectures (Singh et al., 2025). Indeed, the engineering stacks underlying
many RAG and agent memory systems share common building blocks, including vector indices, semantic
search, and context expansion modules.
Despite these technological convergences, the two paradigms have historically been distinguished by the
contexts in which they are applied. Classical RAG techniques primarily augment an LLM with access to static
knowledge sources, whether flat document stores, structured knowledge bases, or large corpora externally
indexed to support retrieval on demand (Zhang et al., 2025q; Han et al., 2025b). These systems are designed
to ground generation in up-to-date facts, mitigate hallucinations, and improve accuracy in knowledge-intensive
tasks, but they generally do not maintain an internal, evolving memory of past interactions. In contrast,
agent memory systems are instantiated within an agent’s ongoing interaction with an environment, continuously
incorporating new information generated by the agent’s own actions and environmental feedback into a
persistent memory base (Wang et al., 2024m; Zhao et al., 2024; Sun et al., 2025e).
In early formulations the distinction between RAG and agent memory was relatively clear: RAG retrieved from
externally maintained knowledge for a single task invocation, whereas agent memory evolved over multi-turn,
multi-task interaction. However, this boundary has become increasingly blurred as retrieval systems themselves
become more dynamic. For example, certain retrieval tasks continuously update relevant context during
iterative querying (e.g., multi-hop QA settings where related context is progressively added). Interestingly,
systems such as HippoRAG/HippoRAG2 (Gutierrez et al., 2024; Gutiérrez et al., 2025) have been interpreted
by both RAG and memory communities as addressing long-term memory challenges for LLMs. Consequently,
a more practical (though not perfectly separable) distinction lies in the task domain. RAG is predominantly
applied to augment LLMs with large, externally sourced context for individual inference tasks, exemplified by
classical multi-hop and knowledge-intensive benchmarks such as HotpotQA (Yang et al., 2018), 2WikiMQA (Ho
et al., 2020), and MuSiQue (Trivedi et al., 2022). By contrast, agent memory systems are typically evaluated
in settings requiring sustained multi-turn interaction, temporal dependency, or environment-driven adaptation.
Representative benchmarks include long-context dialogue evaluations such as LoCoMo (Maharana et al.,
2024) and LongMemEval (Wu et al., 2025a), complex problem-solving and deep-research benchmarks such as
GAIA (Mialon et al., 2023), XBench (Chen et al., 2025c), and BrowseComp (Wei et al., 2025b), code-centric
10

