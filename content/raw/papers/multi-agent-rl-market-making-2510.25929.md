---
title: "Multi-Agent Reinforcement Learning for Market Making: Competition without Collusion"
type: raw
source_url: https://arxiv.org/abs/2510.25929
ingested: 2026-08-24
sha256: pending
tags:
  - academic
  - agentic-ai
  - economic-modelling
---

                                                   Multi-Agent Reinforcement Learning for Market Making:
                                                               Competition without Collusion
                                                               Ziyi Wang                                            Carmine Ventre                                Maria Polukarov
                                                       ziyi.1.wang@kcl.ac.uk                                   carmine.ventre@kcl.ac.uk                      maria.polukarov@kcl.ac.uk
                                                       King’s College London                                    King’s College London                          King’s College London
                                                      London, United Kingdom                                   London, United Kingdom                         London, United Kingdom

                                         Abstract                                                                                In 6th ACM International Conference on AI in Finance (ICAIF ’25), Novem-
                                         Algorithmic collusion has emerged as a central question in AI: Will                     ber 15–18, 2025, Singapore, Singapore. ACM, New York, NY, USA, 9 pages.
                                                                                                                                 https://doi.org/10.1145/3768292.3770388
                                         the interaction between different AI agents deployed in markets




arXiv:2510.25929v1 [cs.MA] 29 Oct 2025
                                         lead to collusion? More generally, understanding how emergent
                                         behavior, be it a cartel or market dominance from more advanced                         1   Introduction
                                         bots, affects the market overall is an important research question.                     Modern electronic markets are composed of highly heterogeneous
                                             We propose a hierarchical multi-agent reinforcement learning                        trading agents operating under uncertainty, informational asym-
                                         framework to study algorithmic collusion in market making. The                          metry, and execution competition. The interactions among these
                                         framework includes a self-interested market maker (Agent A), which                      agents not only shape price formation and liquidity, but also deter-
                                         is trained in an uncertain environment shaped by an adversary, and                      mine broader dynamics of stability and market structure. Under-
                                         three bottom-layer competitors: the self-interested Agent B1 (whose                     standing how strategic heterogeneity influences these outcomes is
                                         objective is to maximize its own PnL), the competitive Agent B2                         crucial for modeling intelligent financial systems.
                                         (whose objective is to minimize the PnL of its opponent), and the                          Multi-agent reinforcement learning (MARL) has gained increas-
                                         hybrid Agent B★, which can modulate between the behavior of the                         ing attention in market modeling, offering tools for simulating
                                         other two. To analyze how these agents shape the behavior of each                       strategic interactions under uncertainty. However, how hetero-
                                         other and affect market outcomes, we propose interaction-level                          geneous agents adapt to diverse counterparts and shape market
                                         metrics that quantify behavioral asymmetry and system-level dy-                         outcomes remains insufficiently understood.
                                         namics, while providing signals potentially indicative of emergent
                                         interaction patterns.
                                             Experimental results show that Agent B2 secures dominant per-
                                         formance in a zero-sum setting against B1, aggressively captur-
                                         ing order flow while tightening average spreads, thus improving
                                         market execution efficiency. In contrast, Agent B★ exhibits a self-
                                         interested inclination when co-existing with other profit-seeking
                                         agents, securing dominant market share through adaptive quoting,
                                         yet exerting a milder adverse impact on the rewards of Agents A
                                         and B1 compared to B2. These findings suggest that adaptive in-
                                         centive control supports more sustainable strategic co-existence in
                                         heterogeneous agent environments and offers a structured lens for
                                         evaluating behavioral design in algorithmic trading systems.

                                         CCS Concepts                                                                            Figure 1: Hierarchical multi-agent architecture with a hybrid
                                         • Computing methodologies → Multi-agent systems.                                        agent modulating between self-interested and competitive
                                                                                                                                 roles.
                                         Keywords
                                         Multi-Agent Reinforcement Learning, Agent-Based Modeling, Mar-                             To address this, we propose a hierarchical, behavior-structured
                                         ket Making, Algorithmic Trading, Game Theory                                            multi-agent learning framework for modeling agent-level hetero-
                                                                                                                                 geneity and its impact on market interactions. The system com-
                                         ACM Reference Format:
                                                                                                                                 prises three functional layers: (i) a top-layer adversary, trained via
                                         Ziyi Wang, Carmine Ventre, and Maria Polukarov. 2025. Multi-Agent Re-
                                         inforcement Learning for Market Making: Competition without Collusion.
                                                                                                                                 reinforcement learning, perturbs volatility and order arrival pro-
                                                                                                                                 cesses to simulate external uncertainty; (ii) a mid-layer Agent A,
                                                                                                                                 representing a self-interested market maker trained to maximize
                                                                                                                                 profit under adversarial stress; and (iii) a bottom layer of competi-
                                         This work is licensed under a Creative Commons Attribution 4.0 International License.   tors—Agent B1 is a self-interested market maker optimizing for
                                         ICAIF ’25, Singapore, Singapore                                                         individual profit; Agent B2 is a competitive agent trained in a zero-
                                         © 2025 Copyright held by the owner/author(s).
                                         ACM ISBN 979-8-4007-2220-2/2025/11                                                      sum setting to minimize Agent A’s reward; and the hybrid agent B★
                                         https://doi.org/10.1145/3768292.3770388                                                 introduces a learnable modulation parameter 𝜔 ∈ [0, 1], enabling
ICAIF ’25, November 15–18, 2025, Singapore, Singapore                                                                                           Wang et al.


dynamic interpolation between self-interested and competitive be-         structural risk indicators such as joint drawdowns, behavioral clus-
haviors. This setup supports controlled analysis of behavioral differ-    tering, or correlated inventory shifts [3–5]. Our work contributes
entiation across self-interested, competitive, and hybrid agents. The     to this effort by proposing interpretable, interaction-level metrics
overall agent architecture and strategic interactions are illustrated     for evaluating heterogeneous agent dynamics under asymmetric
in Figure 1.                                                              information and adversarial stress. This supports a behavioral lens
    To measure agent interaction patterns, we introduce a suite of        on systemic risk, moving beyond aggregate PnL toward a more
structural metrics capturing synchronous quoting, price similarity,       structural understanding of multi-agent influence in algorithmic
inventory divergence, joint drawdowns, and fill overlaps. These           markets.
interpretable signals enable the analysis of behavioral convergence,
role differentiation, and potential coordination in competitive envi-     3 Multi-Layered Agent Design
ronments.
    Empirical results show that Agent B2, a competitive market
                                                                          3.1 Market Environment
maker facing the self-interested B1 in a zero-sum setting, achieves       We construct a synthetic high-frequency trading environment to
strong profit through rigid suppression, but at the cost of increased     simulate interactions between market-making agents and a dy-
market share concentration and strategic crowding, potentially lim-       namic order flow. The environment captures key microstructural
iting diversity in liquidity provision. In contrast, Agent B★—despite     elements, including price evolution, stochastic order flow, proba-
exhibiting a self-interested inclination when facing multiple profit-     bilistic execution, and inventory-constrained risk management.
seeking agents—demonstrates adaptive flexibility. It successfully            Asset Price Dynamics. The mid-price 𝑃𝑡 ∈ R evolves via a
captures greater market share while maintaining stable returns and        discrete-time Brownian motion with drift:
imposing milder pressure on overall market dynamics. In hetero-
                                                                                         𝑃𝑡 +1 = 𝑃𝑡 + 𝜇Δ𝑡 + 𝜎𝜖𝑡 ,         𝜖𝑡 ∼ N (0, Δ𝑡)
geneous agent markets, such adaptive behavior suggests a more
sustainable and strategically robust pathway for long-term coexis-        where 𝜇 is the drift and 𝜎 is the volatility. This formulation is consis-
tence.                                                                    tent with classical models for electronic market microstructure [1].
                                                                             Order Flow and Matching. At each step, market orders arrive
                                                                          according to a Poisson process with rate 𝜆. Each order batch of
                                                                          size 𝑁𝑡 ∼ Poisson(𝜆 · Δ𝑡) is deterministically split into buy and sell
2    Related Work
                                                                          orders: 𝐵𝑡 = ⌊𝑁𝑡 /2⌋, 𝑆𝑡 = 𝑁𝑡 − 𝐵𝑡 . This ensures minimal directional
Agent-based modeling (ABM) has long served as a foundation for            imbalance while reflecting volume-based anonymous flow.
simulating financial systems, offering a principled way to capture           Market-making agents submit bid and ask quotes as price offsets:
decentralized interaction, adaptive decision-making, and systemic
risk propagation [9, 11, 12]. Recent applications of ABM highlight its        𝑞 bid = 𝑃𝑡 − 𝑑𝑡bid,   𝑞 ask = 𝑃𝑡 + 𝑑𝑡ask,     𝑑𝑡bid, 𝑑𝑡ask ∈ [0, 𝑑 max ].
value as a computational approach grounded in the institutional and
behavioral structure of financial systems, enabling controlled ex-            Fill Probability and Execution Allocation. Market order ex-
perimentation on market dynamics and agent heterogeneity [2, 13].         ecution is modeled as a probabilistic process governed by quote
This modeling paradigm supports the explicit specification of het-        aggressiveness. For a quote placed at offset 𝑑 from the mid-price
erogeneous agent roles, making it well suited to studying emergent        𝑃𝑡 , the fill probability is given by:
market properties that arise from local agent interactions—such as                                       (
volatility clustering or liquidity fragmentation—rather than from                                          exp(−𝛼𝑑), 0 ≤ 𝑑 ≤ 𝑑 max
                                                                                            𝑝 fill (𝑑) =
global coordination.                                                                                       0,        otherwise
   Alongside these developments, advances in reinforcement learn-
ing (RL) have enabled dynamic adaptation in market-making agents.             where 𝛼 > 0 is a decay coefficient and 𝑑 max sets a maximum
In particular, multi-agent reinforcement learning (MARL) extends          execution range. This reflects empirical findings that more com-
classical RL to settings of strategic interdependence, facilitating the   petitive quotes—closer to the mid-price—receive higher execution
simulation of execution competition and behavioral feedback [10,          priority [7].
14]. To manage complexity, hierarchical RL (HRL) structures decision-         Given 𝐵𝑡 buy and 𝑆𝑡 sell market orders, fills are allocated to
making across abstraction levels [15], and adversarial RL (ARL)           agents via a multinomial mechanism weighted by their normalized
improves robustness by training against perturbed dynamics or             fill probabilities. For ask-side execution:
hostile opponents [16–19]. Our framework builds on these princi-                                                      (       )!
                                                                                                                        𝑝𝑖ask
ples by embedding learning agents within a layered architecture,                         Fillsask ∼ Multinomial 𝐵𝑡 , Í ask
where a non-trading adversary reshapes the market environment,                                                          𝑗 𝑝𝑗            𝑖
and competing market makers face heterogeneous and evolving
                                                                          An analogous procedure applies to bid-side fills. Each agent imposes
strategic pressures.
                                                                          per-side inventory limits:
   Understanding the systemic effects of local adaptation remains
an open challenge in MARL. Prior studies have noted that emergent                           Fill𝑖bid ≤ Maxbid,    Fill𝑖ask ≤ Maxask
market phenomena—such as herding, synchronization, or preda-
tory trading—can amplify fragility even without explicit coordi-            These constraints prevent excessive position accumulation and
nation [2, 8]. To monitor these effects, researchers have explored        enforce realistic market risk bounds.
Multi-Agent Reinforcement Learning for Market Making: Competition without Collusion                                ICAIF ’25, November 15–18, 2025, Singapore, Singapore


  Position Update and PnL. An agent maintains inventory 𝐼𝑡                                      Table 1: Observation and action space of agents
and cash 𝐶𝑡 , which are updated upon execution as:
                                                                                                 Agent                   Observation                   Action
                𝐼𝑡 +1 = 𝐼𝑡 + Fillsbid − Fillsask
                                                                                                Adversary                     (𝑃𝑡 , 𝑡 )               (𝜆𝑡 , 𝜎𝑡 )
               𝐶𝑡 +1 = 𝐶𝑡 − Fillsbid · 𝑞 bid + Fillsask · 𝑞 ask                                  Agent A                 (𝑃𝑡 , 𝑡, 𝐼𝑡𝐴 , 𝐶𝑡𝐴 )       (𝑑𝑡bid , 𝑑𝑡ask )
   The mark-to-market profit is:                                                                Agent B1                (𝑃𝑡 , 𝑡, 𝐼𝑡𝐵1 , 𝐶𝑡𝐵1 )      (𝑑𝑡bid , 𝑑𝑡ask )
                                                                                                Agent B2                (𝑃𝑡 , 𝑡, 𝐼𝑡𝐵2 , 𝐶𝑡𝐵2 )      (𝑑𝑡bid , 𝑑𝑡ask )
                            PnL𝑡 = 𝐶𝑡 + 𝐼𝑡 · 𝑃𝑡                                                 Agent B★
                                                                                                                                    ★
                                                                                                                       (𝑃𝑡 , 𝑡, 𝐼𝑡𝐵 , 𝐶𝑡𝐵 )
                                                                                                                                           ★
                                                                                                                                                  (𝑑𝑡bid , 𝑑𝑡ask , 𝜔𝑡 )
   This environment enables strategic decision-making by exposing
agents to execution competition, price uncertainty, and inventory
risk under realistic market frictions.                                                action space. The adversary’s objective is defined as the negative
                                                                                      of the inventory-regularized profit used above, evaluated on the
3.2     Agent Architecture and Roles                                                  benchmark module:
                                                                                                                                           
We adopt a hierarchical multi-agent framework composed of three                                    𝑟𝑡adv = − ΔPnL𝑡 − 𝜁 𝐼𝑡2 − 𝜂 Iterminal 𝐼𝑡2 ,
functional layers, each designed to capture a distinct strategic role
                                                                                      where ΔPnL𝑡 and 𝐼𝑡 refer to the benchmark module’s mark-to-
in the market simulation. This layered architecture enables the mod-
                                                                                      market change and inventory at time 𝑡. Maximizing 𝑟𝑡adv therefore
eling of exogenous shocks, adaptive policy learning, and emergent
                                                                                      encourages selections of (𝜆𝑡 , 𝜎𝑡 ) that degrade the benchmark’s
agent-agent interactions under shared market dynamics.
                                                                                      performance, assigning the adversary a zero-sum role relative to
    Adversary (Top Layer). The top-layer agent does not trade but
                                                                                      profit-seeking agents.
perturbs the environment by adjusting order flow intensity (𝜆) and
                                                                                         Agent A and B1. These agents receive rewards based on risk-
mid-price volatility (𝜎). It learns to generate adverse conditions
                                                                                      adjusted profitability:
through environment-level actions, representing external market
stress, regulatory interventions, or structural uncertainty.                                                𝑟𝑡 = ΔPnL𝑡 − 𝜁 𝐼𝑡2 − 𝜂 · Iterminal · 𝐼𝑡2
    Agent A (Mid Layer). Positioned as the core learning market                       where ΔPnL𝑡 denotes mark-to-market gain at time 𝑡, and 𝜁 , 𝜂 are
maker, Agent A interacts directly with the adversary-shaped en-                       inventory regularization coefficients. This design encourages exe-
vironment. Its goal is to maintain profitability and stability across                 cution while discouraging large directional positions [1, 17].
volatile regimes. Trained in isolation before interacting with other                      Agent B2. Operates under a zero-sum formulation. Its objective
agents, it serves as a robust policy baseline for strategic evaluation.               is to suppress Agent A’s performance via inverted reward:
    Agents B1, B2, B★ (Bottom Layer). The bottom layer com-
prises agents that interact with a fixed Agent A during multi-agent                                                       𝑟𝑡B2 = −𝑟𝑡A .
evaluation. B1 is a self-interested market maker trained in an envi-                     Hybrid Agent B★. Balances between self-interested and com-
ronment where Agent A follows a pre-trained policy. Its objective                     petitive objectives via a learnable modulation parameter 𝜔𝑡 ∈ [0, 1].
is to optimize its own profitability under execution competition.                     Its reward function is:
B2 represents a zero-sum adversary whose objective is to suppress                           ★
A’s performance. B★ generalizes between these extremes by dy-                           𝑟𝑡𝐵 = 𝜔𝑡 · 𝑟𝑡self − (1 − 𝜔𝑡 ) · 𝑟𝑡𝐴 − penalty_coeff · (𝜔𝑡 − 0.5) 2 .
namically modulating its behavior along the self-interested versus                    Here, 𝑟𝑡self follows the same inventory-penalized objective used by
opponent-suppression axis. This setup supports analysis of compe-                     Agent A. The first two terms define a tunable trade-off between self-
tition, coordination, and behavioral adaptation in heterogeneous                      interested and suppression of A. The final penalty term discourages
agent populations, extending prior work in strategic multi-agent                      extreme values of 𝜔𝑡 , which would otherwise cause the agent to col-
markets.                                                                              lapse into purely self-interested (𝜔𝑡 → 1) or opponent-suppression
                                                                                      (𝜔𝑡 → 0) regimes. Without this regularization, early-stage learning
3.3     Agent Objectives and Incentive Structure                                      may overfit to local reward gradients, reducing strategic flexibility
Each agent interacts with the environment through a structured                        and generalization. The penalty anchors B★ near a neutral stance
observation-action interface, summarized in Table 1. Observation                      and enables deviation only when sufficiently justified by the envi-
vectors encode local private state (inventory and cash) as well as                    ronment.
global market information (price, time). Agents do not observe
any information about other agents’ states or actions, ensuring an                    3.4       Three-Stage Training Process
asymmetric information environment consistent with decentralized                      All learning-based agents are trained using proximal policy op-
market assumptions [7]. Actions represent either quoting behavior                     timization (PPO), implemented via the Stable-Baselines3 library.
or environmental control, depending on the agent type.                                Agents A, B1, and B2 follow standard actor-critic architectures,
   Adversary. The adversary operates at the environment level,                        while Agent B★ employs a custom policy head to support its ex-
selecting the order flow intensity 𝜆𝑡 and the mid-price volatility 𝜎𝑡                 tended action space and strategic modulation.
within prescribed bounds (cf. Section 3.1). The environment also                         The policy of B★ outputs (𝑑 bid, 𝑑 ask, 𝜔), a three-dimensional ac-
includes a benchmark market-making module that generates quotes                       tion tuple where 𝜔 ∈ [0, 1], controls the trade-off between self-
according to a fixed, non-learned linear-utility rule; quoting is thus                interested and suppression. A sigmoid activation ensures bound-
part of the environment dynamics and lies outside the adversary’s                     edness, and the output bias on 𝜔 is initialized to zero, yielding a
ICAIF ’25, November 15–18, 2025, Singapore, Singapore                                                                                                                                Wang et al.


neutral starting point (𝜔 ≈ 0.5). To promote training stability, raw                                           Table 4: Multi-Agent Interaction Metrics
actions are clamped within a bounded range, and the hybrid agent’s
modulation parameter is regularized to prevent early collapse into                             Metric                          Mathematical Definition
extreme strategies.                                                                            Joint Drawdown Ratio            1 Í I(𝑟 𝐴 < 0 ∧ 𝑟 𝐵 < 0)
                                                                                                                               𝑇  𝑡 𝑡          𝑡                                        
   Training is organized into three sequential stages: (i) pretraining                         Herding Ratio                   1 Í I |𝑞 bid,𝐴 − 𝑞 bid,𝐵 | < 𝜀 ∧ |𝑞 ask,𝐴 − 𝑞 ask,𝐵 | < 𝜀
                                                                                                                               𝑇  𝑡     𝑡        𝑡                𝑡         𝑡
                                                                                                                               √︃
the adversary to perturb the environment, (ii) training Agent A as                             Inventory Divergence                 V[𝐼𝑡𝐴 − 𝐼𝑡𝐵 ]
a reinforcement learning-based market maker under adversarial                                  Quote Distance (Bid)            E[ |𝑞𝑡bid,𝐴 − 𝑞𝑡bid,𝐵 | ]
conditions, and (iii) independently training B-type agents against a                           Quote Distance (Ask)            E[ |𝑞𝑡ask,𝐴 − 𝑞𝑡ask,𝐵 | ]
                                                                                               Fill Overlap Ratio              1 Í I[ ( Fillsbid,𝐴 > 0 ∧ Fillsbid,𝐵 > 0) ∨ ( Fillsask,𝐴 >
pre-trained Agent A strategy.                                                                                                  𝑇     𝑡        𝑡               𝑡                   𝑡
                                                                                                                               0 ∧ Fills𝑡ask,𝐵 > 0) ]

4     Evaluation Metrics
To assess the effectiveness and impact of learned policies, we adopt                          5  Strategic Evaluation and Behavioral Analysis
a set of performance metrics spanning agent behavior, market out-                                in Multi-Agent Markets
comes, and systemic risk. These metrics provide a quantitative
basis for comparing agents such as B1, B2, and B★ in heterogeneous                            5.1 Single-Agent Evaluation of Robustness and
competitive settings.                                                                              Generalization
Agent-Level Performance Metrics. This group captures individ-                                 In this section, we aim to evaluate the robustness and generalization
ual agent behavior, including profitability, risk exposure, market                            capacity of learned market-making agents under different training
participation, and quoting style. The metrics listed in Table 2 are                           and evaluation environments. Specifically, we examine whether
computed per agent and aggregated across evaluation episodes.                                 Agent A—adversarially trained through direct interaction with an
                                                                                              adversary—can maintain strong performance when deployed in a
                                                                                              fixed market (𝜆 = 400, 𝜎 = 1.1). We also assess whether Agent B1,
              Table 2: Agent-Level Performance Metrics
                                                                                              which was trained by interacting with a well-trained Agent A but
                                                                                              never exposed to adversarial conditions during training, can adapt
 Metric                   Mathematical Definition
                                                                                              when evaluated in an adversarially-driven market. Furthermore, we
 Mean PnL                         √︁ E[ PnL𝑡 ]
                          PnLmean =
                                                                                              compare the effects of direct versus indirect exposure to adversarial
 PnL Std                  PnLstd = V[ PnL𝑡 ]
 Sharpe Ratio             Sharpe Ratio = √
                                              E[PnL𝑡 ]                                        environments on strategic robustness.
                                            V[PnL𝑡 ]+10   −6
                                  √︁
 Inventory Volatility     Invstd = V[𝐼𝑡 ]
 Quote Aggressiveness     Agg = E[ (𝑑𝑡bid + 𝑑𝑡ask )/2]                                        Table 5: Single-Agent Evaluation for Agent A and B1 under
                                        Total Fills
 Market Share             Share =
                                  Total Arrivals+10 −6                                        Fixed vs. Adversarial Conditions

                                                                                                      Metric               A_Fix           A_Adversarial          B1_Fix         B1_Adversarial
Market-Level Outcomes. These metrics characterize how the                                           PnL_mean           506.490 ± 35.698    626.421 ± 40.250   437.293 ± 32.030   538.535 ± 37.232
quoting behavior of agents shapes the market environment. They                                     Sharpe_ratio         1.749 ± 0.089       1.746 ± 0.080      1.742 ± 0.093      1.741 ± 0.086
                                                                                                Inventory_volatility    28.335 ± 2.383      28.142 ± 2.443     28.335 ± 2.383     28.143 ± 2.443
are designed to reflect overall market quality, including pricing                              Quote_aggressiveness      2.480 ± 0.002       2.480 ± 0.003      2.095 ± 0.004      2.095 ± 0.005
                                                                                                   Market_share         0.997 ± 0.004       0.992 ± 0.005      0.995 ± 0.004      0.990 ± 0.005
efficiency, liquidity access, and trading activity. While the formulas                              Avg_spread           4.959 ± 0.004       4.960 ± 0.005      4.189 ± 0.009      4.190 ± 0.010
in Table 3 use Agents A and B for illustration, the definitions are                               Price_volatility       0.402 ± 0.155       0.531 ± 0.205      0.402 ± 0.155      0.531 ± 0.205
                                                                                                  Zero_fill_steps       27.000 ± 4.273      16.870 ± 3.681     27.000 ± 4.273     16.870 ± 3.681
applicable to any pair of market participants.

                                                                                                 Table 5 summarizes the results of single-agent evaluations for
                        Table 3: Market-Level Metrics                                         two representative agents: Agent A and Agent B1. Each agent is
                                                                                              tested in two market regimes. In the Fix setting, the agent runs alone
 Metric                        Mathematical Definition                                        in a static market with parameters fixed at 𝜆 = 400 and 𝜎 = 1.1. In
                                                                               
                                              ask,𝐴
 Average Spread                𝑇
                                1 Í𝑇
                                     𝑡 =1 𝑞𝑡         − 𝑞𝑡bid,𝐴 + 𝑞𝑡ask,𝐵 − 𝑞𝑡bid,𝐵 /2         the Adversarial setting, the agent also runs alone, but the market
                                                      Í
                                                        𝑡 Fills𝑡
                                                                (𝑖 )                          parameters are dynamically controlled by a trained adversary, with
 Fill Ratio                    Fill Ratio (𝑖 ) = Í                        , for 𝑖 ∈ {𝐴, 𝐵 }
                                                    𝑡 Arrivals 𝑡 +10 −6                       𝜆 varying within [300, 500] and 𝜎 within [0.2, 2.0].
                                                                     (𝑖 )
                               Zero-Fill Count (𝑖 ) = 𝑡 I( Fills𝑡 = 0) , for 𝑖 ∈ {𝐴, 𝐵 }
                                                        Í
 Zero-Fill Steps
                                                                                              5.1.1 Comparison 1: Agent A – Fixed vs Adversarial Market. Agent
                                                                                              A achieves a notable increase of approximately 24% in mean PnL
Multi-Agent Interaction Metrics. This class of metrics captures                               under adversarial conditions, indicating that the policy is capable
structural interaction patterns among learning agents. They quan-                             of exploiting profit opportunities in dynamically changing envi-
tify synchronous quoting activity, quote similarity, inventory diver-                         ronments. The Sharpe ratio remains stable, and inventory volatil-
gence, joint drawdowns, and fill overlaps. These indicators support                           ity shows no significant change, suggesting consistently strong
the analysis of market segmentation, behavioral convergence, and                              risk control. Even as price volatility increases due to adversarial
agent specialization in multi-agent settings.                                                 interventions, quote aggressiveness and average spread remain
   The definitions in Table 4 use Agents A and B for illustration                             stable across both settings, indicating consistent quoting behavior.
but are applicable to any agent pair.                                                         Zero-fill steps are substantially lower under adversarial conditions,
Multi-Agent Reinforcement Learning for Market Making: Competition without Collusion                           ICAIF ’25, November 15–18, 2025, Singapore, Singapore


suggesting either improved agent responsiveness or more abundant                      (e.g., implicit quote separation), or competitive divergence (e.g.,
trading opportunities due to higher order flow.                                       inventory conflict or price overlap). Also, we assess how joint ex-
   Overall, these results suggest that Agent A’s strategy demon-                      ecution influences market outcomes—including liquidity, pricing
strates strong generalization and maintains consistent performance                    efficiency (e.g., Avg_spread), and agent profitability—relative to
across both fixed and adversarial environments.                                       their single-agent baselines (“A_Fix” and “B1_Fix” in Table 5).
5.1.2 Comparison 2: Direct vs Indirect Exposure to Adversarial Con-                       Profitability and Execution Dominance. According to Table 6,
ditions (B1_Fix vs. B1_Adversarial & A_Adversarial vs. B1_Adversarial).               Agent B1 achieves a higher mean PnL (274.555 vs. 192.696) and
We now analyze whether indirect exposure to adversarial environ-                      slightly better Sharpe ratio (1.772 vs. 1.714) than Agent A, despite
ments through co-training with a robust agent can induce adaptive                     A outperforming B1 in both metrics when tested alone (PnL =
behavior, and how it compares to direct adversarial training.                         506.49 vs. 437.293). Their combined PnL in the joint setting (467.250)
   Comparing the B1_Fix and B1_Adversarial columns in Table 5,                        exceeds B1’s solo result but trails A’s, suggesting that B1 not only
we observe that Agent B1, despite never being exposed to adversar-                    dominates A in this setting but also extracts more profit per fill than
ial conditions during training, achieves a significantly higher PnL                   in isolation. B1 also captures significantly more execution share
when evaluated under adversarial market dynamics. Execution effi-                     (0.627 vs. 0.373), implying that Agent A is partially crowded out.
ciency improves substantially, with zero-fill steps dropping from 27                  These results suggest that B1 assumes a dominant execution role
to 16.87, even though Sharpe ratio, inventory volatility, and quote                   in the joint environment and extracts greater profitability.
aggressiveness remain stable. This suggests that B1 maintains a                           Agent Behavior and Market Impact. In the joint environment, both
consistent quoting style and risk posture, yet still achieves better                  Agent A and Agent B1 show reduced inventory volatility compared
execution under volatile market dynamics. The enhanced fill rate,                     to their single-agent baselines (28.335), indicating more conserva-
without changes in quoting parameters, implies that B1 has learned                    tive inventory management. The decline is more pronounced for
to position its quotes more effectively in response to fluctuating                    B1 (down to 9.977 vs. A’s 19.068), suggesting stronger risk control
order flow—likely by indirectly adapting through repeated inter-                      and avoidance of extreme inventory swings. Despite this, their in-
action with the robust Agent A during training. This suggests the                     ventory divergence remains substantial (11.067), and the fill overlap
emergence of indirect robustness propagation through structural                       is low (0.208), pointing to distinct execution paths. A herding ratio
co-learning.                                                                          of 0.000 and quote distances of 0.189 (bid) and 0.558 (ask) further
   Comparing the A_Adversarial and B1_Adversarial columns                             indicate divergent quoting strategies, especially on the ask side.
in Table 5, we find that Agent A achieves a significantly higher                          Overall, although both agents are self-interested profit maxi-
PnL (approximately 16% above B1) despite quoting with larger                          mizers, there is no evidence of collusion. Agent B1 dominates in
average offsets (2.480 vs. 2.095). Since their market shares are nearly               profitability and execution share, while Agent A exhibits distinct
identical, this suggests that A earns more profit per fill—likely by                  quoting and inventory behavior, suggesting that each agent com-
quoting at more favorable prices while still maintaining similar                      petes independently. This contrasts with findings in retail pricing
execution frequency. This indicates that Agent A, having been                         settings [6], where artificial agents have been shown to engage in
explicitly trained under adversarial conditions, adopts bolder and                    collusion—likely because the simulated market price here is driven
more confident quoting strategies compared to B1, which is facing                     by an exogenous stochastic process, preventing price manipulation
such an environment for the first time.                                               by the agents.
   Overall, while Agent B1 was never explicitly trained under ad-
versarial market conditions, its performance demonstrates a degree                    5.3    Strategic Interaction and Market Effects in
of adaptive capability—likely induced through repeated interaction                           A–B2 Evaluation
with the robust Agent A during training. Nonetheless, Agent A                         This section analyzes the joint evaluation of Agent A and Agent B2
consistently achieves superior outcomes, underscoring the limita-                     in a fixed market (𝜆 = 400, 𝜎 = 1.1). Table 6 (“A vs B2” column)
tions of indirectly acquired robustness. These results suggest that                   reports their performance, with metrics shown as “A / B2”. Agent A
although strategic resilience can be partially transferred via struc-                 is adversarially trained for robustness and generalization, while B2
tured multi-agent interaction, such transfer remains incomplete                       is explicitly optimized to suppress A’s profitability in joint execution.
and does not substitute for direct adversarial exposure.                              Unlike general-purpose agents, B2 is not profit-driven, but trained
                                                                                      to exert persistent competitive pressure. This evaluation examines
5.2    Strategic Interaction and Market Effects in                                    (1) how a robust agent like A performs under sustained adversarial
       A–B1 Evaluation                                                                pressure, and (2) how their interaction shapes execution dynamics
This section analyzes the joint evaluation of Agent A and Agent                       and market outcomes.
B1 in a fixed market environment (𝜆 = 400, 𝜎 = 1.1). The “A vs B1”                        Profitability and Execution Dominance. As shown in Table 6,
column in Table 6 shows their respective performance in this setting,                 Agent A achieves a much lower mean PnL than B2 (81.476 vs.
where each metric is presented as “A / B1”. Both agents are trained                   260.953), in sharp contrast to the “A vs. B1” setting, where A outper-
with self-interested objectives, with B1 trained via interaction with                 formed with a PnL of 192.696. The disparity extends to execution
a pre-trained Agent A.                                                                share: A secures only 16.2% of total executions, while B2 captures
   We examine whether strategic interactions between these two                        83.6%, reflecting a consistent and substantial suppression of A’s
trained agents induce emergent behavioral patterns—such as be-                        market presence. A’s Sharpe ratio also drops to 1.639—below both
havioral convergence (e.g., quoting similarity), tacit coordination                   its solo benchmark (1.749 in A_Fix) and B2’s value in the joint
ICAIF ’25, November 15–18, 2025, Singapore, Singapore                                                                                                                 Wang et al.


                            Table 6: Multi-Agent Performance: A vs B1, A vs B2, B1 vs B1, B1 vs B2 (mean ± std)

 Metric                                A vs B1                              A vs B2                              B1 vs B1                              B1 vs B2
 PnL_mean                 192.696 ± 19.703 / 274.555 ± 19.114   81.476 ± 11.535 / 260.953 ± 22.088   218.835 ± 19.353 / 222.811 ± 22.410   104.629 ± 11.040 / 233.721 ± 21.782
 Sharpe_ratio                1.714 ± 0.127 / 1.772 ± 0.088         1.639 ± 0.113 / 1.769 ± 0.108        1.733 ± 0.104 / 1.748 ± 0.126         1.647 ± 0.097 / 1.754 ± 0.122
 Inventory_volatility       19.068 ± 3.313 / 9.977 ± 2.944        6.290 ± 2.699 / 22.628 ± 3.158       14.494 ± 3.238 / 14.451 ± 3.025       4.473 ± 1.821 / 24.794 ± 2.837
 Quote_aggressiveness        2.493 ± 0.011 / 2.126 ± 0.015         2.524 ± 0.028 / 1.482 ± 0.018        2.121 ± 0.011 / 2.119 ± 0.010         2.170 ± 0.030 / 1.476 ± 0.017
 Market_share                0.373 ± 0.017 / 0.627 ± 0.016         0.162 ± 0.016 / 0.836 ± 0.016        0.497 ± 0.030 / 0.500 ± 0.030         0.243 ± 0.014 / 0.756 ± 0.014
 Avg_spread                         4.619 ± 0.013                         4.007 ± 0.025                        4.239 ± 0.013                         3.646 ± 0.034
 Price_volatility                   0.402 ± 0.155                         0.402 ± 0.155                        0.402 ± 0.155                         0.402 ± 0.155
 Fill_ratio                         1.000 ± 0.001                         0.999 ± 0.003                        0.997 ± 0.002                         0.999 ± 0.002
 Zero_fill_steps                    27.000 ± 4.273                       27.000 ± 4.273                        27.000 ± 4.273                        27.000 ± 4.273
 Joint_drawdown_ratio               0.104 ± 0.019                         0.153 ± 0.034                        0.121 ± 0.021                         0.149 ± 0.024
 Herding_ratio                      0.000 ± 0.000                         0.000 ± 0.000                        0.467 ± 0.148                         0.000 ± 0.000
 Inventory_divergence               11.067 ± 4.768                       17.130 ± 5.312                        7.038 ± 2.759                         21.383 ± 4.257
 Quote_distance_bid                 0.189 ± 0.016                         1.002 ± 0.052                        0.012 ± 0.005                         0.759 ± 0.022
 Quote_distance_ask                 0.558 ± 0.029                         1.082 ± 0.029                        0.056 ± 0.017                         0.630 ± 0.072
 Fill_overlap_ratio                 0.208 ± 0.027                         0.124 ± 0.024                        0.219 ± 0.026                         0.162 ± 0.023



setting (1.769)—indicating that B2 imposes a more severe impact                            drawdown and reduced total PnL—suggesting that persistent ad-
on A’s profitability than B1.                                                              versarial pressure can degrade overall value creation. Although
    Agent A also quotes significantly wider spreads (2.524 vs. B2’s                        market liquidity improves, it does so at the cost of A’s robustness,
1.482), even wider than its solo setting (2.480), suggesting a more                        illustrating the tension between individual resilience and systemic
conservative pricing strategy under pressure. In contrast, B2 places                       efficiency in competitive multi-agent settings.
tighter quotes near the mid-price, offering more competitive prices.
By narrowing its spread, B2 sacrifices per-trade margin for higher                         5.4       Strategic Interaction and Market Effects in
fill probability—effectively “paying for priority” to capture order                                  B1–B2 Evaluation
flow. This aggressive execution allows B2 to crowd out A and dom-
                                                                                           This section analyzes the strategic interaction between Agent B1
inate profitability in a zero-sum environment.
                                                                                           and Agent B2 in a fixed market (𝜆 = 400, 𝜎 = 1.1). Agent B1 is
    Agent Behavior and Market Impact. The herding ratio remains                            a self-interested agent trained through interaction with Agent A
zero, and quote distances on both bid and ask sides are higher than                        to maximize its own profitability. In contrast, B2 is an adversarial
in other evaluated pairings, indicating that Agent A and B2 follow                         agent—originally trained to suppress A, but reconfigured here to
distinctly different quoting strategies. Inventory divergence (17.130)                     target B1’s PnL instead.
further reflects divergent risk-taking behavior: B2 holds larger and                          The “B1 vs B2” column in Table 6 reports their performance, with
more volatile inventory positions (inventory volatility = 22.628),                         metrics shown as “B1 / B2”. This setup enables us to assess how a
while A remains conservative (6.290), consistent with its wider                            self-optimizing agent responds to targeted suppression and how
quotes. The low fill overlap ratio (0.124) confirms that the agents                        such interaction shapes execution dynamics and market outcomes.
rarely compete for the same trades and largely operate in disjoint
execution zones.                                                                               Profitability and Execution Dominance. As shown in Table 6,
    The joint drawdown ratio increases to 0.153 (vs. 0.104 in A vs. B1),                   Agent B2 achieves substantially higher profitability than B1 (233.721
indicating more frequent simultaneous losses. This suggests the                            vs. 104.629), indicating dominance in the joint environment. This
emergence of a mutually unprofitable dynamic—likely driven by                              advantage extends to execution share: B2 captures 75.6% of total
structural conflict rather than coordination. Supporting this, the                         fills, while B1 secures only 24.3%, showing that B2 consistently out-
combined PnL of A and B2 (342.429) is substantially lower than A’s                         competes B1 for order flow. Sharpe ratios reinforce this gap, with
solo performance (506.490), implying that adversarial interaction                          B2 achieving 1.754 compared to B1’s 1.647—highlighting superior
fails to generate additional market value.                                                 risk-adjusted performance.
    Nonetheless, the A–B2 pairing results in a narrower average                                In terms of quoting strategy, B2 posts tighter quotes (aggressive-
spread (4.007 vs. 4.959 in A_Fix), suggesting improved market liq-                         ness = 1.476) than B1 (2.170), while B1’s aggressiveness is slightly
uidity. However, this systemic gain comes at the expense of A’s                            higher than in its solo setting (2.095 in B1_Fix). The overall market
individual performance, highlighting a fundamental trade-off be-                           spread narrows in this pairing (3.646 vs. 4.189 in B1_Fix), suggest-
tween market-level efficiency and agent-level robustness under                             ing that B2’s tighter offset contributes to improved market liquidity.
competitive pressure.                                                                      This aggressive pricing enables B2 to quote near the mid-price,
    Overall, the A–B2 evaluation reveals a one-sided competitive                           boosting its fill probability and execution dominance. In contrast,
dynamic: Agent B2 dominates execution and profitability through                            B1’s wider spreads and reactive posture lead to reduced market
aggressive pricing, while Agent A retreats into conservative be-                           participation and lower profitability.
havior with limited market share. Despite the lack of coordination,                           Agent Behavior and Market Impact. The herding ratio remains
their interaction induces mutual inefficiencies—reflected in elevated                      zero, and quote distances on both bid (0.759) and ask (0.630) sides
Multi-Agent Reinforcement Learning for Market Making: Competition without Collusion                                 ICAIF ’25, November 15–18, 2025, Singapore, Singapore


are relatively high, indicating a lack of quoting alignment between                   Table 7: Multi-Agent Performance: A vs B★ and B1 vs B★
the two agents.                                                                       (mean ± std)
   Inventory behavior further highlights strategic divergence. B1’s
inventory volatility drops sharply from 28.335 in solo evaluation                      Metric                              A vs B★                              B1 vs B★

to just 4.473, while B2 maintains a high level (24.794). Inventory                     PnL_mean               172.469 ± 16.464 / 285.461 ± 26.194   215.023 ± 19.933 / 218.830 ± 24.131
                                                                                       Sharpe_ratio              1.775 ± 0.123 / 1.742 ± 0.103         1.860 ± 0.117 / 1.647 ± 0.122
divergence between the two agents is substantial (21.383), reflect-                    Inventory_volatility     10.116 ± 3.555 / 18.983 ± 3.642        6.831 ± 2.015 / 22.244 ± 2.080
ing B2’s aggressive, flow-seeking strategy and B1’s conservative                       Quote_aggressiveness      2.534 ± 0.032 / 2.100 ± 0.020         2.152 ± 0.017 / 2.127 ± 0.021
                                                                                       Market_share              0.329 ± 0.021 / 0.670 ± 0.021         0.471 ± 0.028 / 0.526 ± 0.028
positioning. The fill overlap ratio is moderate (0.162)—lower than                     Mean_omega (B★ )                - / 0.697 ± 0.002                      - / 0.695 ± 0.002
in A–B1 (0.208) but higher than in A–B2 (0.124)—suggesting that                        Avg_spread                       4.634 ± 0.031                          4.280 ± 0.025
B1 and B2 occasionally compete for fills, but generally operate in                     Price_volatility                 0.402 ± 0.155                          0.402 ± 0.155
                                                                                       Fill_ratio                       0.999 ± 0.001                          0.997 ± 0.003
partially disjoint execution zones.                                                    Zero_fill_steps                  27.000 ± 4.273                        27.000 ± 4.273
   Compared to its interaction with Agent A, B1 exhibits less over-                    Joint_drawdown_ratio             0.107 ± 0.026                          0.115 ± 0.023
                                                                                       Herding_ratio                    0.000 ± 0.000                          0.000 ± 0.000
lap in liquidity targeting when facing B2. This likely reflects their di-              Inventory_divergence             11.293 ± 5.570                        16.373 ± 3.319
vergent quoting behaviors: B2 dominates near the mid-price, while                      Quote_distance_bid               0.463 ± 0.049                          0.252 ± 0.010
                                                                                       Quote_distance_ask               0.477 ± 0.025                          0.181 ± 0.033
B1 quotes more defensively at wider spreads. The quote distances                       Fill_overlap_ratio               0.192 ± 0.025                          0.208 ± 0.027
across all three pairings support this interpretation.
   Overall, the B1–B2 evaluation reveals a clear competitive asym-
metry: B2 dominates both execution and profitability, while B1,
                                                                                         Table 7 reports performance metrics for both A–B★ and B1–B★
despite being self-interested and previously robust against A, fails
                                                                                      pairings, with entries formatted as “A / B★” and “B1 / B★”, respec-
to assert itself against a strategically focused and aggressive oppo-
                                                                                      tively. This dual evaluation addresses three core questions:
nent.
                                                                                      (1) Whether the hybrid agent B★ exhibits consistent behavioral
   We attribute B2’s dominance over B1 to two possible factors.
                                                                                          tendencies across distinct market contexts—that is, does it lean
First, B2’s reward shaping promotes inherently suppressive, low-
                                                                                          toward self-interested behavior, competitive behavior, or display
entropy strategies aimed at neutralizing opponents—regardless of
                                                                                          adaptive modulation between the two?
identity. Second, B2 acts as a game-shaper: while B1 optimizes
                                                                                      (2) How does B★ interact with distinct self-interested agents (A
for market-based equilibrium under self-interest, B2 tends to pri-
                                                                                          vs. B1)—through suppression, implicit cooperation, or role dif-
oritize execution control, which may come at the expense of co-
                                                                                          ferentiation?
operative dynamics or market balance. This structural advantage
                                                                                      (3) Compared to single-agent baselines (A_Fix, B1_Fix in Table 5),
becomes particularly evident when comparing B1’s profitability
                                                                                          how does B★ affect market structure and agent-level outcomes?
across matchups. As shown in the “B1 vs B1” column of Table 6,
when two agents with highly similar quoting behavior interact,                           Profitability and Execution Dominance. B★ maintains tighter quot-
both achieve relatively high individual PnLs (218.835 and 222.811),                   ing across both pairings (quote aggressiveness: 2.100 vs. 2.534
yielding a combined total of 441.65. In contrast, in the B1–B2 pair-                  against A; 2.127 vs. 2.152 against B1), allowing it to position closer
ing, although the total PnL drops sharply to 338.35, this decline is                  to the mid-price and enhance execution priority. This assertive
entirely driven by B1’s profit falling to 104.629, while B2’s rises to                quoting behavior is accompanied by significantly higher inventory
233.721. Notably, B2 not only suppresses its opponent but also out-                   volatility (18.983 against A; 22.244 against B1), indicating a more
performs both B1 agents from the symmetric setting. This contrast                     active and risk-tolerant trading posture. Quote distance metrics
underscores that B2’s dominance does not stem from exploiting                         further contextualize this interaction. In the B1 pairing, the average
a weaker counterpart, but from the inherent competitiveness and                       market quote distance (bid/ask = 0.252 / 0.181) is narrower than in
control-oriented nature of its policy.                                                the A pairing (0.463 / 0.477). Since B★ is present in both scenarios,
                                                                                      this difference likely reflects B1’s tighter quoting behavior com-
                                                                                      pared to A, rather than a shift induced by B★. This also suggests
5.5    Strategic Interaction and Market Effects in                                    that B★ and B1 exhibit greater similarity in quoting strategy than
       A–B★ and B1–B★ Evaluation                                                      B★ and A—echoing earlier observations that A and B1 are more
This section analyzes the interaction between baseline agents (A,                     similar to each other than B1 and B2, while B1 and B2 are still more
B1) and the hybrid market-making agent B★ in a fixed market                           aligned than A and B2. These patterns may stem from the three-tier
(𝜆 = 400, 𝜎 = 1.1). Agents A and B1 are trained under self-interested                 agent architecture employed in this work. Consequently, B★ is op-
objectives to maximize individual profitability. In contrast, B★ is                   erating in a more competitive liquidity environment when facing
trained through interaction with Agent A, learning to balance self-                   B1, which may partly explain its heightened inventory volatility in
interested maximization with suppressing its counterpart’s perfor-                    that setting.
mance. Its objective explicitly penalizes A’s profitability, instilling                  Such behavior likely contributes to B★’s ability to dominate exe-
adversarial tendencies into its policy.                                               cution: it captures 67.0% of total market share against A and 52.6%
   In the evaluations presented here, B★ is paired with both A and                    against B1, reflecting consistent control over order flow. The closer
B1, the latter being previously unseen during training. This setup                    balance in the B1 pairing suggests a more symmetric interaction,
is designed to assess whether B★ exhibits generalized suppressive                     whereas the skew toward B★ in the A pairing may reflect either
behavior or adaptively modulates its strategy based on the nature                     A’s limited responsiveness or a strategic asymmetry in favor of
of its opponent.                                                                      B★. In terms of profitability, B★ outperforms both A and B1 in
ICAIF ’25, November 15–18, 2025, Singapore, Singapore                                                                                  Wang et al.


mean PnL (285.461 vs. 172.469 against A; 218.830 vs. 215.023 against       into a consistently adversarial policy. This results in severe perfor-
B1), confirming its execution edge translates into economic gain.          mance degradation for its counterparts (e.g., A’s mean PnL drops
However, its risk-adjusted performance is mixed: against A, its            to 81.476, and B1’s to 104.629), while B2 itself maintains dominant
Sharpe ratio (1.742) is close to A’s (1.775), while against B1, it drops   execution statistics—over 75% market share and highly aggressive
to 1.647—noticeably below B1’s 1.860—suggesting greater return             quoting behavior (e.g., average spread in B1–B2 narrows to 3.646).
volatility despite nominal profit advantage.                               However, such behavior may come at the cost of increased conflict
                                                                           and systemic tension.
   Agent Behavior and Adaptive Strategy. Behavioral indicators sug-           B★, by contrast, is an incentive-adaptive agent trained to bal-
gest that B★ interacts competitively while maintaining indepen-            ance between self-interested and competitive via a tunable weight
dence across both matchups. The fill overlap ratios (0.192 with A,         𝜔. When interacting with non-adversarial agents like A and B1,
0.208 with B1) are notably higher than those observed in B2 pair-          B★ tends to adopt a more self-interested stance (as indicated by
ings, indicating more frequent contention for the same trades. This        𝜔 ≈ 0.696), focusing on maximizing its own return without aggres-
suggests that B★ does not avoid its counterpart’s liquidity zones,         sively targeting counterpart losses. Despite this, B★ consistently
but rather engages in active trade-level interaction. Despite this         outperforms its counterparts in both PnL and market share while
overlap, B★ avoids mimicry. Inventory divergence remains moder-            allowing A and B1 to retain relatively stable Sharpe ratios and risk
ate (11.293 vs. A; 16.373 vs. B1), indicating differentiated risk-taking   profiles. Compared to B2, B★ achieves market dominance through
behavior even under shared execution pressure. Supporting this,            less aggressive means, promoting a healthier interaction dynamic.
the herding ratio is zero, confirming the absence of quote matching           In summary: The competitive agent (B2) achieves gains through
or strategic alignment.                                                    rigid adversarial behavior but induces stress in market dynamics;
   These results suggest that B★ adapts to its counterpart’s behavior      the hybrid agent (B★) leverages flexible modulation between self-
while maintaining distinct execution patterns. It competes actively        interested and competitive objectives to attain modest superiority
for flow without converging structurally, balancing responsiveness         while preserving systemic stability. In heterogeneous agent mar-
with strategic independence.                                               kets, the hybrid agent’s behavioral adaptability suggests a more
   Market-Level Effects. Relative to single-agent benchmarks (A_Fix        sustainable and strategically viable path for long-term coexistence.
and B1_Fix in Table 5), the introduction of B★ produces mixed ef-
fects on both market structure and agent-level outcomes. In A–B★,
the average spread narrows from 4.959 to 4.634, suggesting im-
                                                                           6   Conclusion
proved liquidity; however, in B1–B★, it widens slightly from 4.190
to 4.280, indicating a marginal decline in efficiency. This incon-         This paper presents a hierarchical multi-agent reinforcement learn-
sistency may reflect the fact that B★ is not trained toward a fixed        ing framework designed to study the structural interplay between
market-making goal but instead learns to balance between maxi-             heterogeneous trading agents in competitive markets. By introduc-
mizing its own returns and suppressing those of its counterpart. As        ing explicitly configured agent roles—self-interested, competitive,
a result, its strategic behavior introduces variability into the market    and incentive-modulating—we enable controlled evaluation of be-
environment, producing different structural outcomes depending             havioral asymmetry and adaptive response. A suite of interaction-
on the opponent. Meanwhile, the combined PnL in each pairing               level metrics is proposed to support interpretable analysis of emer-
declines relative to the solo-agent baselines: A and B★ jointly earn       gent structure and strategy impact beyond aggregate performance.
457.93, compared to 506.490 from A alone; B1 and B★ total 433.853,            Our comparative analysis reveals that rigid suppression strate-
slightly below B1’s solo performance of 437.293. This indicates that       gies, as implemented by Agent B2, can outperform self-interested
B★’s presence does not unlock additional market value—rather, it           agents in zero-sum scenarios by monopolizing order flow and tight-
compresses total profitability and imposes systemic pressure on            ening execution spreads. However, such dominance often disrupts
both the counterpart and the overall trading environment.                  competitive balance. In contrast, the hybrid agent B★—despite ex-
   Overall, B★ leverages relatively small quoting advantages to            hibiting self-interested tendencies when interacting with other
consistently capture greater market share, gradually eroding the           profit-seeking agents—demonstrates strategic adaptability by se-
profitability of both A and B1. However, its presence does not un-         curing market share with less severe impact on competitors. This
lock additional market value; instead, total returns decline relative      contrast highlights the potential of behavioral modulation in en-
to single-agent baselines. This suggests that while B★ competes ef-        abling sustainable coexistence among learning agents.
fectively at the agent level, it introduces varying degrees of pressure       While our framework does not induce emergent coordination or
on counterpart strategies and overall market efficiency.                   imitation, it provides a structured basis for identifying interaction-
                                                                           level patterns across heterogeneous agents. One aspect of the cur-
                                                                           rent formulation is that the hybrid agent’s modulation parameter
5.6     Comparative Summary: B2 vs. B★                                     𝜔 is directly optimized as part of the action vector and remains
Both B2 and B★ demonstrate strong competitive capabilities in              tightly coupled to the reward during training. As a future direc-
multi-agent markets, but their behavioral structures and underlying        tion, one could pursue a meta-learning formulation where agents
incentive mechanisms differ fundamentally.                                 learn to adapt their objective preferences based on environmental
   B2 is a zero-sum suppression-oriented agent, whose re-                  conditions or opponent behavior. Such meta-level control could
ward is explicitly defined as the negative PnL of its opponent             support more generalizable incentive adaptation across diverse
(−PnLopponent ). Trained specifically to suppress Agent A, B2 evolves      market regimes.
Multi-Agent Reinforcement Learning for Market Making: Competition without Collusion                                     ICAIF ’25, November 15–18, 2025, Singapore, Singapore


References                                                                                  [10] Sumitra Ganesh, Nelson Vadori, Mengda Xu, Hua Zheng, Prashant Reddy, and
 [1] Marco Avellaneda and Sasha Stoikov. 2008. High-frequency trading in a limit                 Manuela Veloso. 2019. Reinforcement learning for market making in a multi-
     order book. Quantitative Finance 8, 3 (2008), 217–224.                                      agent dealer market. arXiv preprint arXiv:1911.05892 (2019).
 [2] Robert L. Axtell and J. Doyne Farmer. 2025. Agent-Based Modeling in Economics          [11] Blake LeBaron. 2006. Agent-based computational finance. Handbook of Compu-
     and Finance: Past, Present, and Future. Journal of Economic Literature 63, 1 (2025),        tational Economics 2 (2006), 1187–1233.
     197–287. doi:10.1257/jel.20221319                                                      [12] Thomas Lux and Michele Marchesi. 1999. Scaling and criticality in a stochastic
 [3] Stefano Battiston, J Doyne Farmer, Andreas Flache, Diego Garlaschelli, Andrew G             multi-agent model of a financial market. Nature 397 (1999), 498–500.
     Haldane, Hans Heesterbeek, Cars Hommes, Carlo Jaeger, Robert May, and Marten           [13] Bank of England. 2025. Agent-Based Modeling at Central Banks: Recent
     Scheffer. 2016. Complexity theory and financial regulation. Science 351, 6275               Developments and New Challenges. Working Paper Working Paper No. 1045.
     (2016), 818–819.                                                                            Bank of England. https://www.bankofengland.co.uk/-/media/boe/files/working-
 [4] Dimitrios Bisias, Mark Flood, Andrew W Lo, and Stavros Valavanis. 2012. A                   paper/2025/agent-based-modeling-at-central-banks-recent-developments-
     survey of systemic risk analytics. Annu. Rev. Financ. Econ. 4, 1 (2012), 255–296.           and-new-challenges.pdf Accessed: 2025-05-19.
 [5] Richard Bookstaber. 2017. The end of theory: Financial crises, the failure of          [14] Yagna Patel. 2018. Optimizing market making using multi-agent reinforcement
     economics, and the sweep of human interaction. (2017).                                      learning. arXiv preprint arXiv:1812.10252 (2018).
 [6] Emilio Calvano, Giacomo Calzolari, Vincenzo Denicolo, and Sergio Pastorello.           [15] Shrey Pateria, Kaushik Subramanian, Debadeepta Dey, and Devi Parikh. 2021.
     2020. Artificial intelligence, algorithmic pricing, and collusion. American Eco-            Hierarchical reinforcement learning: A comprehensive survey. Comput. Surveys
     nomic Review 110, 10 (2020), 3267–3297.                                                     (2021).
 [7] Álvaro Cartea, Sebastian Jaimungal, and José Penalva. 2015. Algorithmic and            [16] Lerrel Pinto, James Davidson, Rahul Sukthankar, and Abhinav Gupta. 2017. Ro-
     High-Frequency Trading. Cambridge University Press.                                         bust adversarial reinforcement learning. In ICML.
 [8] J Doyne Farmer, Mauro Gallegati, Cars Hommes, Alan Kirman, Paul Ormerod,               [17] Thomas Spooner, Rahul Savani, and Andreas Koukorinis. 2022. Robust market
     Silvano Cincotti, Anxo Sanchez, and Dirk Helbing. 2012. A complex systems                   making via adversarial reinforcement learning. Journal of Machine Learning
     approach to constructing better models for managing financial markets and the               Research 23, 1 (2022), 1–54.
     economy. The European Physical Journal Special Topics 214 (2012), 295–324.             [18] Ziyi Wang, Carmine Ventre, and Maria Polukarov. 2023. Robust market mak-
 [9] Thierry Foucault, Marco Pagano, and Ailsa Röell. 2013. Market Liquidity: Theory,            ing: To quote, or not to quote. In Proceedings of the Fourth ACM International
     Evidence, and Policy. Oxford University Press.                                              Conference on AI in Finance. 664–672.
                                                                                            [19] Ziyi Wang, Carmine Ventre, and Maria Polukarov. 2024. ARL-Based Multi-Action
                                                                                                 Market Making with Hawkes Processes and Variable Volatility. In Proceedings of
                                                                                                 the 5th ACM International Conference on AI in Finance. 437–444.

