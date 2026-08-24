---
title: "Agentic AI and Hallucinations"
type: raw
source_url: https://arxiv.org/abs/2507.19183
ingested: 2026-08-24
sha256: pending
tags:
  - academic
  - agentic-ai
  - economic-modelling
---

                                                                        Agentic AI and Hallucinations

                                                                           Engin Iyidogan∗,1 and Ali I. Ozkes1,2

                                                         1 SKEMA Business School – Université Côte d’Azur, Paris, France




arXiv:2507.19183v1 [econ.TH] 25 Jul 2025
                                                        2 WU Vienna University of Economics and Business, Vienna, Austria




                                                                                      September 1, 2025




                                                                                            Abstract

                                                    We model a competitive market where AI agents buy answers from upstream generative
                                                 models and resell them to users who differ in how much they value accuracy and in how much
                                                 they fear hallucinations. Agents can privately exert effort for costly verification to lower hal-
                                                 lucination risks. Since interactions halt in the event of a hallucination, the threat of losing
                                                 future rents disciplines effort. A unique reputational equilibrium exists under nontrivial dis-
                                                 counting. The equilibrium effort, and thus the price, increases with the share of users who have
                                                 high accuracy concerns, implying that hallucination-sensitive sectors, such as law and medicine,
                                                 endogenously lead to more serious verification efforts in agentic AI markets.




                                           JEL classification: D82, L14, L15, C73

                                           Keywords: Agentic AI, Artificial Intelligence, Hallucination Risk, Large Language Models


                                             ∗
                                               Corresponding author.
                                           Email addresses: engin.iyidogan@skema.edu (E. Iyidogan), ali.ozkes@skema.edu (Ali I. Ozkes)
1   Introduction

Many industries increasingly rely on AI agents (Brynjolfsson et al., 2025; Colback, 2025). These

software entities intermediate between upstream general-purpose model providers (e.g., large lan-

guage models, LLMs) and end users by converting queries into structured prompts, routing them

to one or several models, and post-processing the returned completions (Rothschild et al., 2025).

Their economic role resembles that of traditional data vendors and consultancy firms, yet two tech-

nological facets distinguish them. First, the upstream supply side offers a discrete menu of models

that differ markedly in both their per-query price and their output quality, measured for instance

by the baseline hallucination rate, the rate at which the model falsely claims to have performed

an action or generated a correct response (Canayaz, 2025; Dahl et al., 2024). Second, downstream

agents can apply various techniques to reduce hallucinations, such as retrieval-augmentation, en-

sembling, or human-in-the-loop verification (Shavit et al., 2023). In other words, AI agents choose

two quality levers: which model to call and how much effort to expend in verification.

    Agents’ quality choices determine the equilibrium mapping from retail price to delivered relia-

bility. When hallucination risk is not perfectly internalized, the standard welfare theorems break

down. In high-stakes domains such as law or medicine, this becomes vitally important (Asgari

et al., 2025). For such users, the disutility from an incorrect answer exceeds by orders of magnitude

the service’s sticker price. Users with lower sensitivity to such failures, such as those who use the

service for entertainment, may rather treat hallucinations as a nuisance. This raises the question:

Can competition and relational contracting alone induce AI agents to verify answers to the stan-

dard demanded by high-criticality users, and how does the equilibrium adjust to the mix of high-

versus low-criticality demand?

    We develop a tractable discrete-time, infinitely-repeated model in which competitive AI agents

pick the wholesale model, verification effort, and retail price. Users differ both in the value they

place on a correct answer and in their aversion to hallucinations. Relational contracts make costly

verification incentive-compatible: the threat of losing future rents disciplines the agent and resolves

the moral-hazard problem. Our model yields testable predictions on how market composition

shapes agentic AI service quality and pricing.

    The verification mechanism we study is akin to relational-incentive contracts (Levin, 2003)


                                                  2
in that costly, non-contractible effort is enforced by the threat of future lost surplus. In our

study, that bilateral logic is embedded in a competitive market whose users differ in their tolerance

for hallucinations, so the agent’s informational rent is passed through to prices. Our paper also

complements the allocation-of-authority framework by Athey et al. (2020). While they study

whether a principal should delegate decision rights to an AI or retain them in-house, we take AI

authority as given and analyze the verification effort exerted by a profit-maximizing operator.


2   The Model

We develop a dynamic economy that features (i) a unit mass of users with heterogeneous valuation

and hallucination aversion, (ii) a perfectly competitive continuum of (AI) agents who assemble

information services, and (iii) a finite set of upstream providers of models (e.g., LLMs). We

model the interaction as an infinitely repeated game where uncertainty arises from the stochastic

occurrence of hallucinations.

    More precisely, users and agents interact in a competitive market, choosing from a menu of

services offered by model providers. Time is discrete, and all parties share a common discount

factor δ ∈ [0, 1). Each user is endowed with a privately observed type θ ∈ {H(igh), L(ow)}, which

governs the utility v(θ) > 0 from a correct answer and the disutility α(θ) > 0 from a hallucinated

answer. We impose v(H) > v(L) and, crucially, α(H) > α(L) to capture the heightened stakes of

the segment with high-type users. The population share of H is µ ∈ (0, 1).

    Each agent is a long-lived firm that chooses a model m ∈ M, where M is publicly known to

be finite, to query and a retail price p to post. Although m and p stay the same throughout, the

agent chooses its verification effort level in each period, e ∈ R≥0 . Model m carries a wholesale fee

km > 0 per call and a baseline hallucination probability h0 (m) ∈ (0, 1). We assume m ≠ m′ implies

km ≠ km′ and h0 (m) ≠ h0 (m′ ).

    Verification effort, chosen by the agent when interacting with a user, lowers the hallucination

probability exponentially:

                                         h(m, e) = h0 (m) exp(−βe),                             (2.1)

where β > 0 denotes verification efficacy. Effort induces a convex cost c(e) satisfying c(0) = 0,

c′ (e) > 0, and c′′ (e) > 0 for all e > 0.


                                                     3
    In any interaction, agents first post long-term relational contracts, specified by a model m

and a price per-period p. Users observe the available contracts and choose one to enter a long-

term relationship. Then, in each subsequent period, the user pays p and the agent chooses an

unobservable effort e. After the service is delivered, a hallucination may occur with probability

h(m, e). If a hallucination occurs, the user observes this poor outcome, the relationship terminates,

and the user exits the market. If no hallucination occurs, the relationship continues to the next

period. In each period, a mass of new, uninformed users enters the market, equal to the mass of

users who exited in the previous period, keeping the total population constant.

    A user of type θ receives expected per-period utility


                          Uθ (p, m, e) = (1 − h(m, e))v(θ) − h(m, e)α(θ) − p.


The total lifetime value to the user from entering the relationship is the expected discounted sum

of these per-period utilities:
                                                           Uθ (p, m, e)
                                      Vθ (p, m, e) =                      .                      (2.2)
                                                       1 − δ(1 − h(m, e))

The user commits to the relationship if and only if their expected lifetime value is non-negative,

Vθ (p, m, e) ≥ 0.

    We analyze equilibria where agents offer a single, unified contract. In equilibrium, this contract

must be self-sustaining for the agent and acceptable to all participating user types. An agent’s

commitment to effort e is sustained by the value of the ongoing relationship. The incentive com-

patibility constraint is then

                                      c(e) ≤ δ[h(m, 0) − h(m, e)]VC ,                            (2.3)

where VC is the agent’s present value of relational rents, such that

                                                    p − km − c(e)
                                          VC =                      .
                                                 1 − δ(1 − h(m, e))

Competition leads agents to lower the price p until this constraint binds, which yields the minimum

price required to sustain effort e:


                                  p(m, e) = km + c(e) [1 + R(m, e)] ,                            (2.4)

                                                         4
where
                                                1 − δ(1 − h(m, e))
                                   R(m, e) =                        ,
                                               δ(h(m, 0) − h(m, e))

such that c(e)R(m, e) denotes the agent’s per-period markup (or rent). An equilibrium contract

is one that maximizes average user lifetime value, subject to the enforcement price (2.4) and the

participation constraint, Vθ ≥ 0, for θ ∈ {H, L}.


3     Results

We analyze the market outcomes under relational contracting, focusing on how the value of repu-

tation enables verification effort in a market with heterogeneous users.


3.1     Benchmark: The Spot Market Outcome

We first consider the benchmark where future interactions have no value, i.e., δ = 0. For brevity,

we let UH (m, p, e) ≡ Uθ=H (p, m, e) (and UL (m, p, e) analogously).

Proposition 1. If δ = 0, the only sustainable effort level is e∗ = 0. Competitive agents offer

the contract (m∗ , p∗ ) where p∗ = km∗ and the model m∗ is the one that maximizes the µ-weighted

average of user utilities:


                        m∗ = arg max {µUH (m, km , 0) + (1 − µ)UL (m, km , 0)}
                                 m∈M



The market is active only if this contract is acceptable to both user types.

Proof. When δ = 0, the IC constraint (2.3) implies e∗ = 0. An agent’s cost thus equals km , and

competition forces the price p∗ = km . To attract users, agents must offer a contract that provides the

highest possible average utility to the market, thus solving for m∗ as defined in the proposition.

      This benchmark highlights that without the shadow of the future, agents have no incentive to

exert costly verification effort, and the quality of service provision regresses to its minimum possible

level, e = 0. Competition can only occur over the observable dimensions of baseline model quality

h0 (m) and its associated cost km , demonstrating that a mechanism like reputation is essential to

solving the underlying moral hazard problem.


                                                    5
3.2     The Reputational Equilibrium

When δ > 0, agents can exert positive effort. An equilibrium contract must maximize the average

user’s lifetime value, subject to the enforcement price (2.4). This is equivalent to solving a planner’s

problem that maximizes the total surplus allocated to users, net of the incentive rents required by

the agent (c(e)R(m, e) discounted). Let vavg (µ) = µv(H) + (1 − µ)v(L) and αavg (µ) = µα(H) + (1 −

µ)α(L). The participation constraint becomes Vθ (m, e) ≥ 0, where

                                        (1 − h(m, e))v(θ) − h(m, e)α(θ) − p(m, e)
                          Vθ (m, e) =                                             ,
                                                    1 − δ(1 − h(m, e))

for θ ∈ {H, L}. The objective is:

                        (1 − h(m, e))vavg (µ) − h(m, e)αavg (µ) − km − c(e)
           W (m, e) =
                                                                                 c(e)R(m, e)
  max                                                                       −                    ,   (3.1)
  m,e≥0                                 1 − δ(1 − h(m, e))                    1 − δ(1 − h(m, e))

subject to participation constraints. To solve this, we first identify which constraint is binding in

relation to the equilibrium hallucination probability h∗ (m, e).

                        α(H)−α(L)
Lemma 1. Let κ = v(H)−v(L) be the sensitivity ratio.

  (i) h∗ (m, e) > 1/(1 + κ) Ô⇒ VH (p, m, e) < VL (p, m, e), thus, VH ≥ 0 is binding.

 (ii) h∗ (m, e) < 1/(1 + κ) Ô⇒ VH (p, m, e) > VL (p, m, e), thus, VL ≥ 0 is binding.

Proof. The ordering of VH and VL is determined by the ordering of the per-period utilities UH and

UL . We have UL ≥ UH if and only if


                          h(m, e)[α(H) − α(L)] ≥ (1 − h(m, e))[v(H) − v(L)],


which yields the threshold 1/(1 + κ). The two constraints coincide when h∗ (m, e) = 1/(1 + κ).

      This leads to our main result stated in Theorem 1, which characterizes the equilibrium for

nontrivial discount factors. We first note that an active equilibrium requires that the participation

constraint for the binding users, i.e., the L types, is met. This requires that the per-period utility

is sufficient to cover the agent’s rent, i.e., (1 − h)vL − hαL − km − c(e) ≥ c(e)R(m, e). Substituting



                                                       6
the expression for the rent term R(m, e) and solving for δ yields the condition δ ≥ δ(m, e), where

                                                     (1 − h)vL − hαL − km − c(e)
                                                                                  −1
                    δ(m, e) ∶= ((1 − h) + (h0 − h)                               )     .
                                                                 c(e)

Thus, an active market is only sustainable if players are sufficiently patient.

Theorem 1. An active relational equilibrium contract exists if and only if δ ≥ δ(m∗ , e∗ ), where the

equilibrium is characterized by the unique pair (m∗ , e∗ ). The equilibrium verification effort e∗ is

strictly increasing in the share of high-type users, µ.

Proof. The equilibrium (m∗ , e∗ ) solves 3.1 whenever δ ≥ δ(m∗ , e∗ ). For given m, the first-order

condition defines an interior solution e∗ (m) and precisely formulates the trade-off between generated

surplus and agent’s markup such that

                   d (1 − h)vavg (µ) − hαavg (µ) − km − c(e)
                      (                                      )=   (          ),
                                                                d    c(e)
                                                                                                  (3.2)
                   de              1 − δ(1 − h)                 de δ(h0 − h)

where h = h(m, e) and h0 = h0 (m). Uniqueness is guaranteed if ∂ 2 W /∂e2 < 0, which holds if c′′ (e)

is sufficiently large. Differentiating the first-order condition with respect to µ, we have

                                          de∗   ∂ 2 W /∂e∂µ
                                                 ∂ W /∂e2
                                              =− 2          .
                                          dµ

The denominator is negative by the second-order condition. The cross-partial derivative becomes:

                              ∂ 2 W βh ((vH − vL ) + (1 − δ)(αH − αL ))
                                   =                                    ,
                                             (1 − δ(1 − h))
                              ∂e∂µ                           2



which is positive as vH > vL , αH > αL , β, h > 0, and δ ∈ (0, 1). It follows that de∗ /dµ > 0.

Our main contributions are twofold. First, the model highlights the trade-off between a model’s

baseline hallucination risk, h0 (m), and an agent’s verification effort, e, made visible in both the

pricing and equilibrium conditions. Second, the comparative static finding de∗ /dµ > 0 delivers a

sharp exposition: market composition itself acts as a disciplinary device, in that sectors with higher

composition of high-criticality users, such as law and medicine, endogenously generate more heavily

verified and consequently more expensive AI services.


                                                     7
3.3         Numerical Example

We conclude our analysis with a numerical example. Low-type users gain v(L) = 1 from a correct

answer and incur α(L) = 1.5 if the answer is hallucinated; high-type users gain v(H) = 3 and lose

α(H) = 10. Verification lowers hallucination risk according to (2.1) with efficacy β = 0.70 and incurs
                                         2
quadratic cost c(e) = e8 . The discount factor is set to δ = 0.95. The baseline upstream model (A)

features a hallucination probability hA
                                      0 = 0.20 and wholesale fee kA = 0.05. A second model, Model

B, is such that hB
                 0 = 0.13 and kB = 0.30.

       Figure 1a shows that greater patience relaxes the incentive-compatibility constraint, shifting the

whole e∗ (µ) schedule upward, while effort is strictly increasing in µ as established in Theorem 1.

Verification plateaus once e∗ ≈ 1.97, where the hallucination rate falls below 0.02.

     2.00         δ = 0.75                                                  2.00         β = 0.5
                  δ = 0.85                                                               β = 0.6
     1.75         δ = 0.95                                                  1.75         β = 0.7

     1.50
                                                                            1.50
     1.25
                                                                            1.25
eμ   1.00                                                              eμ
                                                                            1.00
     0.75


     0.50                                                                   0.75


     0.25
                                                                            0.50

     0.00
                                                                            0.25
            0.0              0.2   0.4           0.6   0.8   1.0                   0.0             0.2   0.4       0.6   0.8   1.0
                                             μ                                                                 μ



(a) Patience and verification effort.                                  (b) Verification-technology comparative static.
Equilibrium effort e∗ as a function of the share of                    Equilibrium effort e∗ as a function of µ for three
high-type users µ for three discount factors                           verification efficacies (β = 0.50, 0.60, 0.70).
(δ = 0.75, 0.85, 0.95).

Fig. 1. Equilibrium verification effort under varying discount factors and verification efficacies.


       Figure 1b shows that more effective screening technology lifts the e∗ (µ) schedule, allowing

agents to reach the quality ceiling at lower µ. The result follows from the effort efficacy as in (2.1).

       Figure 2 illustrates the upstream model choice. For µ < 0.26 agents rely on the cheaper but

riskier model and compensate with higher verification effort. When the high-type composition

exceeds roughly one-fourth of the market, paying the higher wholesale fee for the cleaner model

maximizes surplus, and quality provision shifts from the retail to the upstream layer.




                                                                   8
                               16         ModelμAμ(h0 = 0.20,μk = 0.05)
                                          ModelμBμ(h0 = 0.13,μk = 0.30)
                               14

                               12

                               10
                           W
                                8

                                6

                                4

                                2
                                    0.0               0.2                 0.4           0.6    0.8   1.0
                                                                                    μ




Fig. 2. Upstream model choice. Notes: Total welfare W under Model A (hA
                                                                      0 = 0.20, kA = 0.05, solid) and Model B
(hB
  0 = 0.13, kB = 0.30, dashed).




References

Asgari, E., N. Montaña-Brown, M. Dubois, S. Khalil, J. Balloch, J. A. Yeung, and D. Pimenta

  (2025). A Framework to Assess Clinical Safety and Hallucination Rates of LLMs for Medical

  Text Summarisation. npj Digital Medicine 8(1), 274.

Athey, S. C., K. A. Bryan, and J. S. Gans (2020). The allocation of decision authority to human

  and artificial intelligence. AEA Papers and Proceedings 110, 80–84.

Brynjolfsson, E., D. Li, and L. Raymond (2025). Generative AI at Work. The Quarterly Journal

  of Economics 140(2), 889–942.

Canayaz, M. (2025). AI Agency. Available at SSRN 5109326.

Colback,       L.     (2025).                         AI            Agents:                   From   Co-pilot   to   Autopilot.

  https://www.ft.com/content/3e862e23-6e2c-4670-a68c-e204379fe01f.                                               [Accessed 22-

  07-2025].

Dahl, M., V. Magesh, M. Suzgun, and D. E. Ho (2024). Large Legal Fictions: Profiling Legal

  Hallucinations in Large Language Models. Journal of Legal Analysis 16(1), 64–93.

Levin, J. (2003). Relational incentive contracts. American Economic Review 93(3), 835–857.

Rothschild, D. M., M. Mobius, J. M. Hofman, E. W. Dillon, D. G. Goldstein, N. Immorlica,

  S. Jaffe, B. Lucier, A. Slivkins, and M. Vogel (2025). The Agentic Economy. arXiv preprint

  arXiv:2505.15799.

Shavit, Y., S. Agarwal, M. Brundage, S. Adler, C. O’Keefe, R. Campbell, T. Lee, P. Mishkin,



                                                                                9
T. Eloundou, A. Hickey, et al. (2023). Practices for Governing Agentic AI Systems. Research

Paper, OpenAI.




                                           10

