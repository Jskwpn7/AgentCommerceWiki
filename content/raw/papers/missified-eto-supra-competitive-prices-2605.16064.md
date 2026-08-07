---
source_url: https://arxiv.org/abs/2605.16064
source_pdf: https://arxiv.org/pdf/2605.16064
id: "arXiv:2605.16064v2"
title: "Misspecified Estimate-then-Optimize Leads to Supra-Competitive Prices"
authors: Jackie Baek, Vivek F. Farias, Farrell Wu
published: 2026-05-15
primary_category: cs.GT
tags: [algorithmic-pricing, estimate-then-optimize, supra-competitive-prices, misspecified-demand, algorithmic-collusion, multi-firm-markets, pricing-dynamics]
sha256:
ingested: 2026-06-23
---

# Misspecified Estimate-then-Optimize Leads to Supra-Competitive Prices

**arXiv:** 2605.16064v2 [cs.GT, cs.AI, econ.TH] — 15 May 2026
**Authors:** Jackie Baek, Vivek F. Farias, Farrell Wu

## Full Extracted Text

<!-- Raw PDF text below -->

                                                          Misspecified Estimate-then-Optimize Leads to
                                                                            Supra-Competitive Prices
                                                                Jackie Baek∗              Vivek F. Farias†              Farrell Wu‡




arXiv:2605.16064v2 [cs.GT] 1 Jun 2026
                                                                                             Abstract

                                                    We study whether simple algorithmic pricing systems can systematically produce collusive-
                                                like prices in multi-firm markets. We consider firms that price using a myopic estimate-then-
                                                optimize rule: each repeatedly fits a demand model to its own price and sales history and sets the
                                                price that maximizes estimated profit. This demand model is misspecified, omitting competitors’
                                                prices. We analyze the dynamics of this rule when it is initialized by an exploration phase of
                                                independent random prices. We characterize when this pipeline converges to supra-competitive
                                                prices above the Nash equilibrium, via a fluid-limit ordinary differential equation analysis. We
                                                show that supra-competitive prices arise when firms initially explore within similar price ranges
                                                on the same side of the Nash price. Moreover, prices can be substantially above the Nash
                                                price; we show that prices can reach monopoly levels under symmetric exploration. Simulations
                                                calibrated to a real multifamily rental market confirm that supra-competitive outcomes arise
                                                robustly beyond our theoretical assumptions, including under finite horizons, heterogeneous
                                                products, and nonlinear logit demand.


                                        1       Introduction
                                        Businesses increasingly rely on algorithms to automate pricing decisions (Brown and MacKay, 2023).
                                        This trend has raised a fundamental question: can algorithmic pricing produce collusive-like out-
                                        comes? A growing literature suggests that the answer can be yes for certain learning algorithms.
                                        For example, the seminal work of Calvano et al. (2020) demonstrates that Q-learning agents can
                                        reach and sustain supra-competitive prices through reward-and-punishment dynamics. These re-
                                        sults are highly sensitive to the explicit learning dynamics assumed1 . However, it remains unclear
                                        whether these findings apply to the pricing systems most commonly deployed in practice: classic
                                        reinforcement learning approaches such as Q-learning are complex to implement, require long and
                                        costly training, and they are outperformed by simpler pricing alternatives (den Boer et al., 2024).
                                            ∗
                                             Stern School of Business, New York University, baek@stern.nyu.edu
                                            †
                                             Massachusetts Institute of Technology, vivekf@mit.edu
                                           ‡
                                             Massachusetts Institute of Technology, farrellw@mit.edu
                                           1
                                             For instance, in the case of Calvano et al. (2020), the definition of agent state, discount factor and exploration
                                        probability must all be carefully calibrated to get sustained collusion.




                                                                                                  1
   In practice, many firms use far simpler, model-based approaches to algorithmic pricing: estimate
a demand curve from their historical data of past prices and realized sales, then apply a myopic
“estimate-then-optimize” rule to update prices, often without explicitly modeling competitors’ prices
or strategic responses. This approach has been widely studied in the single-agent learning literature
under various names such as certainty-equivalence in adaptive control (Simon, 1956), and greedy or
exploitation policies in reinforcement learning (Sutton and Barto, 1998). It is also a performant
baseline in the revenue management and inventory control literature (Lariviere and Porteus, 1999;
Aviv and Pazgal, 2002; Farias and Van Roy, 2010).
   It is unclear whether these more realistic dynamics systematically produce supra-competitive
outcomes. To this end, Cooper et al. (2015), building on earlier work by Kirman (1975, 1986,
1995), investigate sellers that use monopoly (i.e., misspecified) demand models under estimate-
then-optimize dynamics. They show that, depending on the initial conditions, the long-run price
can be sub-competitive, Nash, or supra-competitive. This is a statement about what is possible:
they establish it by constructing, for each target price, a short initial history under which prices
freeze at that target within a few periods. Their result thus characterizes which prices can persist,
but does not analyze how prices evolve from natural initial conditions, and so does not identify
which outcome actually arises. Therefore, whether realistic pricing dynamics systematically produce
supra-competitive prices remains an open question.
   We answer this question by analyzing the dynamics directly. We study firms that begin with
an exploration phase, posting independent random prices, before settling into the estimate-then-
optimize dynamic above. We view the exploration phase as a model of uncoordinated initial price
variation that initializes the learning dynamics, rather than a coordinated algorithm firms deliber-
ately adopt. In a fluid scaling where the exploration and exploitation horizons grow large, we prove
that when firms initially explore within a well-defined region of similar prices, the limiting prices
of all firms are supra-competitive. Crucially, the relevant region of exploration covers a nontrivial
fraction of the exploration space and arises naturally when prices are clustered. The mechanism for
supra-competitive prices does not require punishment, communication, or explicit coordination; the
misspecified pricing dynamic suffices. Computational evidence on both synthetic and real-world-
calibrated markets further shows that supra-competitive outcomes persist beyond the conditions of
our analytical results and in realistic rental-market calibrations.

1.1   Summary of model and results
Model setup. We study a competitive market with N symmetric firms over K + T time periods
under a linear demand model. Each firm prices by a myopic estimate-then-optimize rule (“exploita-
tion”) for T periods, initialized by an exploration phase of K periods. In the exploration phase,
firm i’s price is drawn independently over time from a distribution with mean µi . Then, throughout
the exploitation phase, each firm estimates a monopoly-style demand curve in each period using
only its own past prices and realized sales. This demand curve omits competitor prices and is
thus misspecified. This misspecification reflects a common real-world constraint where firms have


                                                   2
limited visibility into competitors’ real-time pricing or choose a simpler model for statistical or
computational efficiency.
   We analyze a “fluid” scaling regime where both the exploration and exploitation horizons grow
large. Under this asymptotic scaling, we show that terminal prices converge to a deterministic limit
described by a price-moments ordinary differential equation (ODE). This ODE keeps track of the
running price means and covariances for all firms, and a careful analysis of this ODE yields the
results we describe below.

Main theoretical result. Our primary result (Theorem 3.2) states that limiting prices are supra-
competitive when firms’ exploration means µi lie on the same side of the Nash price within what we
call the best-response cones (left plot of Figure 1). The upper cone yields supra-competitive prices
immediately, while the lower cone yields supra-competitive prices after a finite waiting period.
Informally, the cone condition is that all firms explore with “similar prices” on the same side of
the Nash price, with the allowable price dispersion across firms increasing as prices move further
from Nash. More formally, these cones are regions where every firm’s best-response price, if it were
computed against the exploration means µ, would move all firms’ prices in the same direction.
   Crucially, under our dynamic, firms do not actually best-respond, nor do they model competitor
prices. Rather, firms simply update their prices to maximize revenue as predicted by a misspecified
demand model fit to their own historical prices and sales. The core innovation in our analysis lies
precisely in analyzing such a dynamic when exploration occurs within a best-response cone.

                 µ2                                     Final price



                                                   Monopoly
                                   θ
           Nash                                        Nash
                             45◦



                                              µ1                                          s
                              Nash                                     Nash Monopoly

Figure 1: Left: the shaded regions depict the best-response cones in the (µ1 , µ2 ) plane, where µi is
firm i’s average exploration price. We show that the terminal prices are supra-competitive whenever
(µ1 , µ2 ) lies in the shaded region. The angle θ depends on the demand parameters but is always at
least 45◦ , so the cones cover more than one quarter of the feasible exploration-mean space. Right:
Final price under symmetric exploration, in the regime of vanishing exploration variance and an
infinite exploitation horizon, where s is the average price during exploration.

   In a duopoly, the best-response cones cover at least one quarter of the feasible price space for
any demand parameters. We also show that in a duopoly, the cone arises endogenously under our
dynamics: under any initial conditions, the limit price falls in the closure of the best-response cones

                                                   3
(Proposition 3.1). This has an iterative implication: even when initial exploration falls outside a
cone, the resulting terminal prices land inside one; so if firms re-explore around those prices, supra-
competitive outcomes are guaranteed in the next round. For general N , we show that naturally
clustered exploration profiles land in a best-response cone with nontrivial probability. In particular,
under a random interval prior in which firms’ exploration means are drawn from a common random
price band, the probability of landing in a best-response cone is at least 1/4, and this probability
increases with N (Proposition 3.2).

Quantifying the price gap. Beyond establishing supra-competitive prices, we quantify the size
of the price gap above Nash under symmetric exploration. We consider a setting where all firms
have the same mean exploration price s, where we prove a sharp analytical characterization of the
final price as exploration noise vanishes and the exploitation horizon grows (right plot of Figure 1,
Theorem 3.3). We show that prices converge to the monopoly price if s is either below the Nash
price or above the monopoly price, and when s is between the Nash and monopoly prices, prices
converge to s. This reveals that limiting prices can be substantially above the Nash price, potentially
reaching the monopoly benchmark. We confirm that the price gap above Nash is substantial beyond
the theorem’s assumptions, using numerical ODE evaluation (Section 4.1) and stochastic simulations
(Section 4.2).

Key mechanism: persistent correlation. The bias channel is omitted-variable bias: when a
firm’s prices are positively correlated with its competitors’ prices, omitting competitors’ prices from
the misspecified OLS regression biases the fitted demand slope, leading the firm to price above its
true best response. Exploration in a best-response cone initializes common-sign price movements
relative to firms’ running means, thereby inducing positive cross-firm price correlation. The central
novelty of our analysis is to show that this correlation does not dissipate: the common-sign movement
is forward invariant, so the correlation persists throughout the exploitation phase. This persistent
upward bias ultimately yields supra-competitive limiting prices.

Simulations calibrated to a real rental market. In assessing the robustness of our theory
there are several issues that merit consideration. In no particular order these include: (1) real-world
time scales vs. the fluid regime; (2) nonlinear demand and firm asymmetry; (3) exploration outside
of the best-response cones; and (4) a richer supply side with product-specific costs. To address these
considerations, we run empirically calibrated simulations to the multifamily rental market in the
Greater Boston area (Section 5). Specifically, using demand estimates and market structure from
Calder-Wang and Kim (2024), we simulate firms deploying the same explore–then–exploit pricing
pipeline in a realistic environment with heterogeneous products, heterogeneous customers, nonlinear
logit demand, and product-specific shadow costs calibrated so that observed rents form the Nash
benchmark.
   This analysis shows that the qualitative predictions of our theory persist: supra-competitive
terminal prices arise across a broad range of exploration parameters, and the effect is strongest

                                                  4
when firms experiment with similar prices on the same side of the Nash benchmark. The finite-
horizon simulations further show that these effects appear quickly, not only in the asymptotic
fluid regime. These results confirm that supra-competitive outcomes arise robustly across a range
of problem parameters and model features that extend beyond the assumptions required for our
analytical results, including parameters calibrated to a real-world rental market.

1.2   Related Work
There is a burgeoning literature studying how pricing algorithms can give rise to algorithmic col-
lusion. One commonly studied class consists of reinforcement-learning algorithms, especially Q-
learning, which has been shown to converge to supra-competitive outcomes in repeated oligopoly
pricing environments (Calvano et al., 2020; Klein, 2021; Hettich, 2021; Abada et al., 2024; Asker
et al., 2022). In many of these models, collusive behavior emerges through reward-and-punishment
dynamics: agents learn to coordinate on cooperative price levels and to implement credible pun-
ishments following deviations. Such mechanisms typically require extensive training, careful state
representation, and the capacity to learn complex, history-dependent strategies. In contrast, we
show that much simpler pricing pipelines can systematically produce supra-competitive prices with-
out any punishment logic or learned threats.
   Closer to our work, a line of research studies firms that fit a misspecified linear demand model
by OLS and post the implied optimal price (Cooper et al., 2015; Lin and Sarıtaç, 2025; Light and
Wang, 2026; Yang et al., 2026). Across these prior works, supra-competitive outcomes arise only
with an explicit source of cross-firm coupling (e.g., correlated exploration). A novel feature of our
analysis is to show that no such explicit coupling is needed: under independent exploration, cross-
firm price correlation emerges endogenously from the estimate-then-optimize dynamics and drives
supra-competitive prices.

Misspecified estimate–then–optimize pricing. The most direct comparison to our work is
Cooper et al. (2015), who study the same estimate-then-optimize rule under misspecification. In
their most comparable case (both intercept and slope unknown), they characterize the range of prices
that can be reached as steady states, by reverse-engineering, for each target price, a short noiseless
three-period history that freezes the system at that target. It is straightforward to formalize this
construction in our framework: a range of target prices below, at, and above Nash can each be made
a steady state of the price-moments ODE by engineering the exploration moments (Proposition B.1
in Appendix B). This type of construction speaks only to which prices can persist; it does not
identify which steady state actually arises from natural initial histories, which is our focus.
   By contrast, we analyze the estimate-then-optimize dynamics to study which steady state is
selected when the system is initialized by an independent exploration history. Notably, the supra-
competitive steady states from Cooper et al. (2015) require positively correlated initial cross-firm
covariance; under our independent exploration, we instead show that the necessary cross-firm price
correlation emerges endogenously during the exploitation dynamics.


                                                  5
   Lin and Sarıtaç (2025) study related OLS dynamics under misspecified linear demand. Their
main result derives a stability condition that guarantees convergence to the competitive equilibrium;
this is in contrast to our paper’s main result, which is to identify conditions that lead to supra-
competitive prices. They also show that supra-competitive prices can be caused by correlation in
exploration across firms, or asymmetry in the response time of algorithmic price updates.
   Two recent papers, Light and Wang (2026) and Yang et al. (2026), also study misspecified
OLS demand dynamics but with ongoing independent price perturbations in each period, rather
than a one-shot exploration phase as in our paper. Both find that supra-competitive prices require
additional cross-firm coupling (correlated experimentation in Light and Wang, 2026, price imitation
in Yang et al., 2026), while independent perturbations alone converge to Nash.

Pricing algorithms without demand estimation. A separate strand studies bandit and
reinforcement-learning algorithms that ignore competitors’ prices, but do so without fitting any
demand model at all (Hansen et al., 2021; Banchio and Mantegazza, 2022; Douglas et al., 2024;
Bichler et al., 2024). Hansen et al. (2021) analyze a UCB bandit policy in a noiseless setting;
because both firms run the same deterministic algorithm, their internal learning states coincide
after exactly two rounds, so their subsequent actions become fully synchronized in the third round.
Douglas et al. (2024) study a similar noiseless setting and generalize this result from UCB to all
symmetric deterministic bandit algorithms. Banchio and Mantegazza (2022) study reinforcement
learners (e.g., ϵ-greedy Q-learning) in a two-action prisoner’s dilemma and show that when learning
is sufficiently slow, payoff estimates can become coupled across firms, sustaining collusive outcomes,
although this coupling can disappear under alternative learning-rate specifications.
   On the other side, Bichler et al. (2024) show that a class of mean-based bandit algorithms (e.g.,
Exp3, MWU) provably converge to Nash equilibrium in repeated price competition. In contrast
to these works, we analyze a natural and widely used estimate–then–optimize rule in a continuous
action space with explicit demand estimation. Our results do not rely on exact synchronization of
algorithms across firms, nor on specific algorithmic parameters.

Other literature on algorithmic collusion. A complementary line of work studies algorithmic
collusion in settings where algorithms are explicitly designed to sustain collusive outcomes. This
literature dates back to the imperfect-monitoring collusion framework of Green and Porter (1984)
and the Edgeworth-cycle model of Maskin and Tirole (1988).
   Recent work in this direction includes Meylahn and den Boer (2022); Loots and den Boer
(2023); Aouad and den Boer (2021). Yang et al. (2023) study how fairness regulations on prices
interact with collusion in a repeated-game setting. Arunachaleswaran et al. (2025) view deploying
an algorithm as a commitment and study the environment as a leader-follower game. They show
that if the leader uses an arbitrary no-regret algorithm, then supra-competitive prices arise if the
follower approximately optimizes within this environment. Recent papers also evaluate whether
large language models can exhibit similar collusive behavior (Fish et al., 2024; Keppo et al., 2025).



                                                  6
    On the empirical side, there is growing evidence that pricing algorithms can lead to elevated
prices in practice (Chen et al., 2016; Abada and Lambin, 2023; Calder-Wang and Kim, 2024; Assad
et al., 2024). We build on the empirical analysis of Calder-Wang and Kim (2024) of the U.S.
multifamily rental market by using their calibrated demand model as a more realistic environment
than our stylized framework, allowing us to assess the robustness of our results.


2     Model
There are N symmetric firms competing over several periods under a linear demand model with id-
iosyncratic shocks. Firms use a myopic estimate-then-optimize pricing rule: each fits a misspecified,
monopoly-style demand curve to its own price and sales history and posts the price that maximizes
predicted profit. Because the fitted curve omits competitors’ prices, each firm treats variation in
demand caused by competitors as unobserved noise.
    We study these dynamics over two phases. During the exploration phase of K periods, firms
post random prices around an initial mean. Thereafter, during the exploitation phase of T periods,
firms apply the estimate-then-optimize rule to their accumulating price-sales history, updating their
fitted demand curves each period. We view the exploration phase as a model of the initial price-sales
history that initializes the exploitation dynamics (e.g., from legacy manual pricing), rather than a
coordinated pricing algorithm that firms deliberately adopt. Any estimate-then-optimize procedure
must begin from some initial data; the exploration phase is a parsimonious way to model it. We
now make this setup precise.

2.1   True demand model
Let Pi,t ∈ R+ denote the price posted by firm i ∈ [N ] in period t ∈ [K + T ]. Firm i realizes quantity
Qi,t ∈ R, which depends on the full vector of current-period prices (Pj,t )j∈[N ] through the linear
demand system
                                               c X
                        Qi,t = a − bPi,t +         Pj,t + εi,t ,          i ∈ [N ].                (1)
                                             N −1
                                                    j̸=i

Here a, b, c > 0. The parameter b captures the own-price effect, while c captures the cross-price
effect from competitors’ prices. We assume b > c, so that own-price effects dominate cross-price
effects. The demand shocks form a martingale difference sequence with respect to the filtration
{Ft }t≥0 generated by the history of prices and quantities:

                                                        E ε2i,t+1 | Ft ≤ σenv
                                                                          2
                                                                     
                             E[εi,t+1 | Ft ] = 0,                             ,

for all i ∈ [N ] and t ∈ {0, . . . , K + T − 1}. Thus the shocks may be history-dependent, but they are
conditionally mean zero and have uniformly bounded conditional second moments.

Constraints on price and quantity. Prices are restricted to the interval [Pmin , Pmax ], where
Pmin > 0. We assume 2b−c
                      a
                         < Pmax ≤ ab . The lower bound ensures that the price cap does not force

                                                    7
firms to remain below the competitive Nash price, which we define in Section 2.3. The upper bound
ensures that conditional expected demand is nonnegative over the feasible price range. Since Qi,t
represents realized sales, we also assume Qi,t > 0 almost surely for all i ∈ [N ] and t ∈ [K + T ].

2.2      Pricing dynamics
We next describe how firms choose prices, recalling that the first K periods correspond to the
exploration phase, and the remaining T periods correspond to the exploitation phase.

Exploration (t ≤ K). During exploration, firms randomize prices according to a fixed distribution
Dexp on RN :
                                                        i.i.d.
                                 (P1,t , . . . , PN,t ) ∼ Dexp ,            t = 1, . . . , K.

       We assume prices across firms are independent. Let µ ∈ [Pmin , Pmax ]N denote the mean of
Dexp , and let Σexp := diag(σ1,exp
                             2                2
                                   , . . . , σN,exp ) denote its covariance matrix, with σi,exp
                                                                                          2     > 0 for all
i ∈ [N ]. We assume Dexp is supported on [Pmin , Pmax ]N . The exploration phase generates the initial
price–quantity histories from which firms begin estimating demand in the exploitation phase.

Exploitation (t > K). During exploitation, each firm follows a myopic estimate–then–optimize
rule. At each time t ≥ K, firm i uses its own history {(Pi,s , Qi,s )}ts=1 to fit the linear demand curve

                                                      q(p) = α + βp.                                            (2)

This model is misspecified because the true demand model (1) also depends on competitors’ prices.
Equivalently, firm i treats the variation in demand caused by competitors’ prices as unobserved
noise. Let (α̂i,t , β̂i,t ) denote the ordinary least squares estimates of (α, β) based on firm i’s history
through period t. The fitted demand curve is

                                                  q̂i,t (p) := α̂i,t + β̂i,t p.

Firm i then chooses the next period’s price by maximizing predicted profit over the feasible price
interval:
                                                                                                                (3)
                                                                   
                    Pi,t+1 :=     arg max         p α̂i,t + β̂i,t p ,        t = K, . . . , K + T − 1.
                                p∈[Pmin ,Pmax ]

       This problem has a unique maximizer.2 To summarize the feedback loop: prices generate data,
the data update the fitted demand curve, and the updated fitted demand curve determines the next
price.

Remark 2.1 (Bayesian reformulation of the exploration phase). The exploration phase can be
replaced by an equivalent Bayesian formulation that encodes the same initial information through a
   2
    More specifically, this problem has a unique maximizer for every fitted demand curve generated by an admissible
history; in the nonnegative-slope case, the realized-demand and price constraints Qi,s > 0 and Pi,s ∈ [Pmin , Pmax ]
make Pmax the unique endpoint maximizer; see Lemma E.1 in Appendix E.1


                                                                 8
prior rather than a random sample. Specifically, each firm runs a Bayesian linear regression for its
misspecified demand curve q(p) = α + βp, starting from a Gaussian prior on the intercept and slope
(α, β) whose sufficient statistics match (µ, Σexp ). Each period, the firm updates this prior into a
posterior using the new price-sales observation, and posts the price that maximizes posterior-mean
predicted profit. The resulting Bayesian price dynamics coincide with the exploitation dynamics
above. Thus (µ, Σexp ) admits two readings: as the moments of an initial random sample, or as the
parameters of an initial Bayesian prior. See Appendix A for the derivation.

2.3   Price benchmarks
Lastly, we define two natural price benchmarks: the competitive Nash price and the monopoly price.

Competitive benchmark. For firm i and price vector p = (p1 , . . . , pN ), let p̄−i := N 1−1
                                                                                               P
                                                                                               j̸=i pj
denote the average price of its competitors. Suppose firms compete under the correct demand model
(1) and observe each other’s posted prices. Then firm i’s profit-maximization problem depends on
its competitors’ prices only through p̄−i . The best-response price for firm i is

                                                        a + c p̄−i
                                        BR(p̄−i ) =                .                               (4)
                                                           2b

The symmetric Nash equilibrium is the fixed point at which every firm charges its best response to
the common price charged by its competitors. Thus the unique Nash price, denoted pNE , is

                                                      a
                                            pNE =          .                                       (5)
                                                    2b − c

We also refer to pNE as the competitive price, thus labelling prices above pNE as supra-competitive.

Monopoly benchmark. The monopoly price, denoted pMNP , is the symmetric price that would
be chosen if firms jointly maximized total industry profits under the same demand system. It is
given by
                                                       a
                                          pMNP =             .                                     (6)
                                                    2(b − c)
    The Nash price pNE and the monopoly price pMNP therefore form natural benchmarks for con-
textualizing the prices generated by the learning dynamics. We assume pNE ≥ Pmin , but do not
necessarily assume pMNP ≤ Pmax . When c ≤ b/2, the monopoly price satisfies pMNP ≤ a/b.


3     Convergence to Supra-Competitive Prices: Analytical Results
We now present the main analytical results. The first step is a convergence result for the stochastic
system: in a fluid scaling where the exploration and exploitation horizons grow proportionally,
terminal prices converge to a deterministic limit characterized by an ODE that tracks running price
means and accumulated covariances (Section 3.1).


                                                    9
   In Section 3.2, we use this ODE to establish two main results. First, we give a sufficient
condition for supra-competitive limiting prices, expressed through best-response cones in the space
of exploration means (Theorem 3.2). Second, under symmetric exploration, we characterize the
limiting price as a function of the exploration mean, quantifying the gap above Nash (Theorem 3.3).
Finally, we discuss the geometry and scope of these cones, showing that they have a simple duopoly
interpretation and arise with nontrivial probability under clustered exploration profiles (Section 3.3).

3.1   Terminal convergence and the price-moments ODE
For each pair (K, T ), the pricing dynamics in Section 2 induce a random terminal price vector
(P1,K+T , . . . , PN,K+T ). We show that when K, T → ∞ with (K + T )/K → τ , this random vector
converges to the solution of a deterministic price-moments ODE, defined as follows.

Definition 3.1 (Price-moments ODE). Fix an exploration-mean vector µ = (µ1 , . . . , µN ) and co-
variance matrix Σexp . The price-moments ODE is the system for (U (τ ), V (τ )) ∈ RN × RN ×N ,
τ ≥ 1, with U (1) = µ, V (1) = Σexp , and

                                        P −U
                                 U̇ =        ,      V̇ = (P − U )(P − U )⊤ ,
                                          τ

where P (τ ) = P (τ ; µ, Σexp ) ∈ RN is the vector of posted prices, defined componentwise. Writing
Ū−i := N 1−1 j̸=i Uj and V̄i,−i := N 1−1 j̸=i Vij ,
             P                           P

                                                        
               (a + c Ū−i )Vii − c Ui V̄i,−i           [Pe ]
                                                            i [Pmin ,Pmax ] ,   if − bVii + cV̄i,−i < 0,
        Pei :=                                ,   Pi :=                                                    (7)
                    2(bVii − cV̄i,−i )                  P ,
                                                             max                otherwise.

   The ODE uses a scaled horizon τ ≥ 1, where τ corresponds to (K + t)/K in the stochastic
model (τ = 1 marks the start of exploitation). The vector U (τ ) tracks running price means, and
the matrix V (τ ) accumulates price covariances, where Vii captures the accumulated variance of firm
i’s own prices and Vij the accumulated covariance between firms i and j. Each Pi (τ ) is firm i’s
posted price at time τ ; Eq. (7) is firm i’s misspecified OLS price, expressed in terms of the moments
(U, V ) (see Appendix E.4 for the derivation).
   This formula (7) also makes the source of misspecification bias transparent. When V̄i,−i = 0, the
posted price reduces to the true best-response Pei = BR(Ū−i ) = (a + cŪ−i )/(2b). When V̄i,−i > 0
(representing positive correlation in firm i’s historical prices with its competitors’), this creates an
upward omitted-variable bias, pushing Pei above the true best-response.
   We abbreviate P ODE (τ ; µ, Σexp ) := P (τ ; µ, Σexp ) (or P ODE (τ ) when µ and Σexp are fixed) for the
ODE-implied terminal price at scaled horizon τ . The following theorem states that this deterministic
limit is the fluid limit of the original stochastic pricing process (proof in Appendix E).

Theorem 3.1 (Convergence to the price-moments ODE). Let {(Km , Tm )}m∈N satisfy Km → ∞,



                                                      10
Tm → ∞, and (Km + Tm )/Km → τ ∈ [1, ∞). Then,

                                                  → P ODE (τ ; µ, Σexp )
                                                 P
                 (P1,Km +Tm , . . . , PN,Km +Tm ) −                          as m → ∞.

   We note that a wide range of prices, both below and above Nash, can be made steady states of
the price-moments ODE when exploration is allowed to be correlated across firms; this recovers, in
our framework, the type of multiplicity result shown by Cooper et al. (2015) (Proposition B.1 in
Appendix B).

3.2   Supra-competitive limiting prices
The previous subsection reduces terminal prices to the deterministic limit P ODE (τ ; µ, Σexp ). We now
state two results of this limit. First, we give a sufficient condition on the exploration-mean vector
µ under which the limiting prices are supra-competitive (Theorem 3.2). Second, under symmetric
exploration, we characterize the limiting price as a function of the exploration mean (Theorem 3.3).
   We begin by defining the regions of exploration mean µ that enter the sufficient condition.

Definition 3.2 (Best-response cones). For an exploration-mean vector µ ∈ [Pmin , Pmax ]N , write
µ̄−i := N 1−1 j̸=i µj . The upper and lower best-response cones are
             P


                        C + := µ ∈ [Pmin , Pmax ]N : µi > BR(µ̄−i ) ∀i ∈ [N ] ,                            (8)
                              

                        C − := µ ∈ [Pmin , Pmax ]N : µi < BR(µ̄−i ) ∀i ∈ [N ] .                            (9)
                              


   Membership in C + (resp., C − ) means that every firm explores above (resp., below) its best
response to its competitors’ average exploration mean. The left side of Figure 1 in the introduction
illustrates the cones for N = 2. We defer a detailed discussion and interpretation of these cones to
Section 3.3. We now state our main result, whose proof is in Section 6.

Theorem 3.2 (Supra-competitive limiting prices). Under the same assumptions as Theorem 3.1,

 (a) if µ ∈ C + , then for every τ ∈ [1, ∞), P ODE (τ ; µ, Σexp ) ≻ pNE 1;

 (b) if µ ∈ C − , then there exists τ0 ∈ [1, ∞) such that for all τ > τ0 , P ODE (τ ; µ, Σexp ) ≻ pNE 1.

   Theorem 3.2 identifies simple sufficient conditions on the mean exploration prices µ under which
the long-run outcome is supra-competitive. The two cones have slightly different timing implications.
If µ ∈ C − , then prices begin below the Nash price, so the exploitation dynamics must first push
prices upward; the threshold τ0 is the waiting period required for the deterministic dynamics to
enter the supra-competitive region. In contrast, if µ ∈ C + , the supra-competitive conclusion holds
for every τ ∈ [1, ∞).
   While Theorem 3.2 establishes that limiting prices can exceed the Nash price, it does not specify
by how much. Under symmetric exploration, where µ = s1 and Σexp = σexp
                                                                   2 I , we obtain a sharp
                                                                       N
characterization in a limit where the exploitation horizon grows and the exploration noise vanishes.


                                                     11
Theorem 3.3 (Symmetric exploration). Suppose µ = s1 for some s ∈ [Pmin , Pmax ] and Σexp =
 2 I . Let p̄MNP := min{pMNP , P
σexp N                          max }. Then

                                                           
                                                           s 1,      s ∈ [pNE , p̄MNP ],
                                  ODE
                   lim    lim P         (τ ; µ, Σexp ) =
                 σexp →0 τ →∞                               MNP
                                                            p̄   1,   s < pNE or s > p̄MNP .

      The proof is in Appendix H.2. Theorem 3.3 reveals a stark threshold structure, illustrated in the
right plot of Figure 1. When s ∈ [pNE , p̄MNP ], the limiting price locks in at the exploration mean s
itself. Outside this range, either below Nash or above the capped monopoly price, prices converge
all the way to p̄MNP . Thus the price gap above Nash can be substantial, potentially reaching the
monopoly benchmark when pMNP ≤ Pmax .3

3.3     Coverage of best-response cones
The sets C + and C − consist of exploration profiles where, if each firm were to best-respond to its
competitors’ average exploration price, all firms would adjust their prices in the same direction (a
single round of fictitious play). Concretely, µ ∈ C + means each firm i explores at a price µi exceeding
its best-response to the average exploration mean of its competitors; µ ∈ C − is the analogous region
where every firm explores below that best-response. This is only a characterization of the cones,
not what firms actually do: under the misspecified demand model, firms do not compute best
responses. The actual pricing rule in Definition 3.1 can be decomposed into a best-response term
plus a covariance-driven bias.
      We interpret the cones in two parts. First, in the duopoly case, they admit a simple geometric
description and also arise endogenously from the dynamics. Second, for general N , we introduce a
random interval prior that models clustered exploration profiles and show that the probability of
landing in a cone is at least 1/4 and often much higher, for any N and any demand parameters.

3.3.1     Cone coverage for N = 2

For N = 2, the cones in Definition 3.2 simplify because µ̄−1 = µ2 and µ̄−2 = µ1 :

                   C + = (µ1 , µ2 ) ∈ [Pmin , Pmax ]2 : µ1 > BR(µ2 ) and µ2 > BR(µ1 ) ,
                        

                   C − = (µ1 , µ2 ) ∈ [Pmin , Pmax ]2 : µ1 < BR(µ2 ) and µ2 < BR(µ1 ) .
                        


Figure 2 illustrates these regions in the (µ1 , µ2 ) plane. The two best-response lines µ2 = BR(µ1 ) and
µ1 = BR(µ2 ) intersect at (pNE , pNE ), and C + and C − correspond to the upper-right and lower-left
wedges. Informally, the cones capture settings where both firms explore at similar prices and where
the first best-response adjustment points in the same direction for both firms.
  3
    We show that under symmetric histories, the pairwise price correlation ρ also admits a conduct-parameter in-
terpretation, mapping ρ = 0 to the Nash price and ρ = 1 to the capped monopoly price; see Appendix H.1 for
details.



                                                           12
                                    µ2

                                         µ1 = BR(µ2 )
                                                               C+

                                         pNE , pNE
                                                     
                                                              µ2 = BR(µ1 )


                                         C−
                                                                        µ1

Figure 2: Best-response cones in the duopoly case, shown in the (µ1 , µ2 ) plane for a = b = 1 and
c = 1/2. The two best-response lines intersect at (pNE , pNE ); the upper-right and lower-left wedges
are C + and C − , respectively.


   Beyond this geometric interpretation, the cones also arise endogenously from the dynamic: for
any exploration price vector µ, the duopoly ODE price converges, and the limit must lie in C + ∪ C − ,
where C ± denotes the closure of C ± (allowing equality in the defining inequalities (8)-(9)).

Proposition 3.1 (Duopoly convergence to the closed best-response cones). Take N = 2. Fix
a diagonal covariance matrix Σexp with positive diagonal entries and an exploration-mean vector
µ ∈ [Pmin , Pmax ]2 . Then P ∞ (µ, Σexp ) := lim P ODE (τ ; µ, Σexp ) exists, and P ∞ (µ, Σexp ) ∈ C + ∪ C − .
                                              τ →∞

   The proof is in Appendix I.1. To see why this matters, suppose firms’ exploration prices are
themselves the output of an earlier round of estimate-then-optimize pricing, rather than arbitrary
points in the feasible set; this is natural if real-world prices inherit structure from past pricing rather
than being drawn uniformly. Proposition 3.1 guarantees that such “recycled” exploration prices lie
in C + ∪ C − . Theorem 3.2 then applies after restarting the dynamic from these prices. The cones
are thus not an arbitrary corner of the parameter space but a typical destination of the dynamic.

3.3.2   Cone coverage for general N

We now ask, for general N , how often a randomly drawn exploration profile µ ∈ [Pmin , Pmax ]N lands
in a best-response cone. In practice, exploratory prices tend to cluster within a common local band,
since firms typically tie their experiments to recently observed market prices or industry-typical
price levels. We introduce the following random interval prior to formalize this clustering.

Definition 3.3 (Random interval prior). Fix an outer band [P , P ] containing pNE . Two firms draw
exploration means uniformly from this band,

                          iid
                      x, y ∼ Unif[P , P ],     ℓ := min{x, y},         u := max{x, y},

and we set µ1 = x and µ2 = y. The remaining N − 2 firms draw exploration means uniformly from


                                                         13
the random interval [ℓ, u]:

                                              iid
                                   µi | (ℓ, u) ∼ Unif[ℓ, u],      i = 3, . . . , N.

    Two firms act as anchors by drawing from the full outer band, forming a random subinterval
[ℓ, u]; the remaining N − 2 firms then cluster within that subinterval. The only input to this
construction is the outer band [P , P ]. Letting r := c/b denote the ratio of the cross-price effect to
the own-price effect, the following result gives a universal lower bound on cone membership (proof
in Appendix I.2).

Proposition 3.2 (Cone membership under the random interval prior). Under the random interval
prior, for every N ≥ 2 and r ∈ (0, 1),

                                                           (N − 1)(2 − r)    1
                              Pr µ ∈ C + ∪ C − ≥
                                              
                                                                            ≥ .
                                                        4(N − 1) − r(N − 2)  4

    Under the random interval prior, the probability of landing in a cone is at least 1/4 for any
number of firms N and any demand parameters; Table 1 reports the bound for representative
values, and the bound converges to (2 − r)/(4 − r) as N → ∞.
    Perhaps surprisingly, the bound increases in N for each fixed r. This runs counter to a naive
volume intuition: under a uniform prior on the hypercube [Pmin , Pmax ]N , the best-response cones
shrink exponentially as N grows. Under the random interval prior, however, the inner interval [ℓ, u]
is the same for all firms, so additional firms only reinforce the alignment that places µ inside a cone.

                              N      r = 0.25       r = 0.50   r = 0.75    r → 1.00
                              2       0.4375         0.3750     0.3125      0.2500
                              3       0.4518         0.4006     0.3461      0.2877
                              5       0.4591         0.4143     0.3647      0.3094
                              10      0.4633         0.4222     0.3756      0.3225
                              ∞       0.4667         0.4286     0.3846      0.3333

Table 1: Lower bounds on the probability of landing in C + ∪ C − under the random interval prior,
for representative values of N and r = c/b. The column r → 1.00 is the limiting boundary case.



4    Computational Results via the ODE
The previous section shows that terminal prices are characterized by the deterministic price-moments
ODE and gives sufficient conditions for supra-competitive limits. We now use the ODE to computa-
tionally evaluate prices beyond the analytical cases, where we focus on the duopoly case (N = 2) for
ease of illustration. In this section, we compute the ODE terminal prices over a grid of exploration
means, illustrating how the supra-competitive region changes with µ, τ and σexp (Section 4.1).



                                                          14
Then, we compare these ODE values to the original finite-sample stochastic system from Section 2,
showing how the deterministic heatmaps emerge as the exploration sample size grows (Section 4.2).

4.1      ODE-based duopoly simulations
We numerically evaluate the price-moments ODE for N = 2. We fix a = b = 1 and c = 1/2, so that
pNE = 23 and pMNP = 1. We set the covariance during exploration to be Σexp = σexp
                                                                              2 I
                                                                                  2×2 . Figure 3
plots the ODE-implied terminal price P1ODE (τ ; µ, Σexp ) over a grid of exploration means (µ1 , µ2 ),
varying both the scaled horizon τ and the exploration noise σexp .

                 = 2.0, exp = 0.05                       = 5.0, exp = 0.05                       = 20.0, exp = 0.05
    0.85                                                                                                                          1.0
    0.80
    0.75
                                                                                                                                  0.9
2   0.70
    0.65
    0.60                                                                                                                          0.8
    0.55
    0.500.50 0.55 0.60 0.65 0.70 0.75 0.80 0.85 0.50 0.55 0.60 0.65 0.70 0.75 0.80 0.85 0.50 0.55 0.60 0.65 0.70 0.75 0.80 0.85
                                                                                                                                  0.7
                           1                                       1                                        1                     pNE
                 = 2.0, exp = 0.15                       = 5.0, exp = 0.15                       = 20.0, exp = 0.15
    0.85
                                                                                                                                  0.6
    0.80
    0.75
    0.70                                                                                                                          0.5
2
    0.65
    0.60                                                                                                                          0.4
    0.55
    0.500.50 0.55 0.60 0.65 0.70 0.75 0.80 0.85 0.50 0.55 0.60 0.65 0.70 0.75 0.80 0.85 0.50 0.55 0.60 0.65 0.70 0.75 0.80 0.85
                           1                                       1                                        1

Figure 3: ODE-implied terminal price P1ODE (τ ; µ, σexp
                                                    2 I
                                                        2×2 ) in the duopoly case. Each panel fixes
            2 I
(τ, Σexp = σexp 2×2 ) and varies the exploration means (µ1 , µ2 ). White marks the Nash price p
                                                                                               NE =

2/3, while red and blue indicate terminal prices above and below Nash. Thin lines mark the best-
response boundaries defining the two cones.



Horizons sharpen cone-like regions. As the horizon τ increases (left to right), the heatmaps
show convergence that is qualitatively similar to the best-response cones defined in Definition 3.2,
though the supra-competitive region is in fact larger than the cones. At larger σexp (bottom plots),
this convergence is slower, so the cone-like regions are less sharply separated at the plotted horizons.
The diagonal line (µ1 = µ2 ) corresponds to symmetric exploration, and the heatmap shows values



                                                                 15
consistent with the symmetric exploration result of Theorem 3.3. Specifically, the terminal price is
close to the monopoly price when µ1 < pNE , while terminal prices increase with µ1 when µ1 ≥ pNE .

Exploration noise pulls prices toward Nash. When the exploration noise σexp is higher
(bottom plots), prices are closer to Nash. Because supra-competitive prices arise from correlation in
prices across firms, more exploration noise weakens this effect: it gives each firm more uncorrelated
own-price variation, diluting the cross-firm correlation that drives the bias. Beyond the duopoly
case, Appendix C evaluates the ODE for general N and shows that supra-competitive prices arise
robustly under clustered exploration profiles.

4.2   Comparing the ODE to stochastic simulations
We compare the ODE predictions (assuming an asymptotic scaling) to the original discrete-time
stochastic system from Section 2 for small, finite horizons. We use the same parameters as Section 4.1
for the demand (a = b = 1 and c = 1/2, so that pNE = 32 and pMNP = 1). We evaluate the stochastic
system for (K, T ) ∈ {(10, 50), (100, 500)}, then run the ODE for the corresponding τ = (K+T )/K =
6. We fix σexp = 0.05 and set the standard deviation of the random demand shock to 0.05. For
each exploration-mean pair (µ1 , µ2 ) ∈ [0.5, 0.85]2 , we run 2500 independent simulation pipelines.
Figure 4 compares the mean terminal price of firm 1 to the ODE-implied value P1ODE (τ ; µ, Σexp ).




Figure 4: ODE and stochastic mean terminal-price heatmaps. The left panel is the deterministic
ODE prediction, while the middle and right panels average terminal prices across 2500 stochastic
simulation runs. For small K, finite-sample exploration noise blurs the sharp ODE transition
regions. As K increases from 10 to 100, the stochastic heatmap becomes visibly closer to the
deterministic ODE profile.



Finite samples blur transitions. The stochastic heatmaps are blurred versions of the ODE
heatmap, with the blurring diminishing as K grows. This is consistent with Theorem 3.1, which
predicts convergence to the ODE profile as K → ∞ with τ fixed. When K is small, the exploration
phase provides a noisy estimate of the moments that initialize exploitation, so nearby exploration



                                                 16
profiles can lead to different dynamic regimes. As K increases, these moments concentrate around
their population values and the sharp transitions in the ODE map reappear.

Boundary points create mixtures. As the heatmap only presents the mean price over 2500
runs, we also examine the distribution of prices across runs. In Figure 5, we pick two exploration
means (µ1 , µ2 ) = (0.66, 0.66) and (µ1 , µ2 ) = (0.75, 0.85), and we plot the distribution of terminal
prices across runs. The first point (0.66, 0.66) corresponds to a sharp boundary between Nash-like
and monopoly-like outcomes in the ODE heatmap. Finite-sample noise therefore pushes different
runs to different sides of the boundary, producing a bimodal distribution: roughly one quarter of runs
remain near Nash, while the rest move close to pMNP . By contrast, the second point (0.75, 0.85) lies
in a smoother region of the heatmap, where the stochastic noise does not lead to regime switching.




Figure 5: ODE map and terminal-price histograms from stochastic simulations at τ = 100, σexp =
0.05, and demand-shock standard deviation 0.05 (2500 runs; K = 100, K + T = 10000). The two
marked profiles have similar mean terminal prices, but different distributions: (0.66, 0.66) lies near
a sharp ODE transition and produces a mixture of Nash-like and monopoly-like outcomes, while
(0.75, 0.85) lies in a smoother region and produces a concentrated distribution.



5    Empirically calibrated simulations: Boston multifamily rentals
We complement our analysis with simulations calibrated to a large multifamily rental market, adapt-
ing the heterogeneous-logit demand system in Calder-Wang and Kim (2024). We test whether
an estimate-then-optimize pipeline initialized by exploration can generate systematically elevated
prices, and evaluate whether the patterns from our theory persist in this richer setting. Relative
to our stylized model, this environment features differentiated firms, heterogeneous customers, and
nonlinear logit demand.




                                                  17
5.1    Market setup and calibration
Data. We instantiate a market calibrated to the Boston Core multifamily rentals (PUMAs 08001–
08003) using ACS microdata. We exclude rentals below the within-bedroom-count 5th percentile
of rent and restrict to adult households with income ≥ $30k. After filtering, our sample comprises
N = 801 representative rentals and H = 920 representative households, each weighted by its ACS
survey weight.
    We denote by p0 the vector of observed rents and by s0 the corresponding observed shares
(constructed from normalized survey weights). We model each of the N representative rentals as
an independent firm offering one product, and thus refer to “rentals” and “firms” interchangeably.

Demand-side model. In each period t = 1, . . . , K + T , each household h ∈ {1, . . . , H} chooses
among rentals j ∈ {1, . . . , N } (plus an outside option). Given the price vector Pt = (P1,t , . . . , PN,t ) ∈
RN , the total share (demand) for rental j at time t is
                                                                
                          H
                          X            exp αh Pj,t + x′j βh + ξj                         wh
            sj,t (Pt ; ξ) =     w̃h                                  ,          w̃h := PH          ,
                                    1+ N                     ′
                                      P
                            h=1         k=1 exp αh Pk,t + xk βh + ξk                       ℓ=1 wℓ

where xj are observed rental characteristics, ξj is a rental vertical-differentiation fixed-effect term,
and (αh , βh ) encode renter-specific price sensitivity and characteristic preferences. We adopt the
parameterization of (αh , βh ) from Calder-Wang and Kim (2024) and calibrate {ξj }N
                                                                                  j=1 to match
observed shares s0 at the observed prices p0 (sj (p0 ; ξ) = sj0 ); see Appendix D.1 for details.

Supply-side model. We assume that each rental j has a product-specific shadow cost λj > 0
capturing the intertemporal opportunity cost of renting today, so that its period-t objective is
                                                              
                                     πj,t (Pt , ξ) = Pj,t − λj sj,t (Pt , ξ).

We choose λ = (λj )N
                   j=1 so that the observed rent vector p0 is the Nash equilibrium of the calibrated
static game. This pins down each shadow cost uniquely via the firm’s first-order condition; the
explicit formula is in Appendix D.2. The fitted values are reasonable: the 25th and 75th percentiles
of λj /pj0 are 0.817 and 0.877, respectively.

Nash and monopoly benchmarks. The Nash benchmark is the observed rent vector p0 by
construction, since λ was calibrated to make p0 the Nash equilibrium. The monopoly benchmark
pM is defined by joint profit maximization across all rentals; in our calibration, the monopoly markup
is relatively uniform, with the 25th and 75th percentiles of pM
                                                              j /pj0 at 1.236 and 1.263, respectively.


5.2    Estimate-then-optimize pricing pipeline
We apply an analogous estimate-then-optimize pricing pipeline at the rental level. During explo-
                                                                                                 i.i.d.
ration (t = 1, . . . , K), each rental j posts a perturbed price Pj,t = µj (1 + vj,t ) with vj,t ∼ N (0, σ 2 )

                                                       18
around an exploration mean µj , with price clipped to [0, P̄ ], where P̄ is a large exogenous upper
bound. During exploitation (t ≥ K), each rental fits a naive binary logit on its own price-share
history (treating competitors’ prices as unobserved) and sets its next-period rent by myopically
maximizing predicted profit. Full equations are in Appendix D.3.

Specifying exploration means µ. To mirror the comparative statics in the stylized model, we
vary two features of exploration means: their overall level relative to the Nash benchmark and the
dispersion of prices across rentals. Specifically, for parameters m, σν ≥ 0, we set

                                                    i.i.d.   √     √
                        µj = m pj0 (1 + νj ),     νj ∼ Unif(− 3σν , 3σν ).

Thus m shifts the average exploration price vs. Nash, while σν controls cross-rental dispersion.

5.3     Results and Discussion
We report two experiments. First, we vary the exploration-price parameters m, σν , and σ, which
respectively control the average exploration level relative to Nash, the cross-rental dispersion in
exploration means, and the within-rental exploration noise (Subsection 5.3.1). Second, we vary the
time parameters: the exploitation horizon T and the exploration length K (Subsection 5.3.2).
   For rental j, define the terminal percentage change relative to Nash by
                                                              
                                                      Pj,K+T
                                    ∆j,T := 100              −1 .
                                                        pj0

The figures plot the 10th, 50th, and 90th percentiles of ∆j,T across rentals.

5.3.1    Supra-competitive prices across exploration-price designs

We fix K = 50 and T = 450 (τ = 10), placing the experiment close to the converged regime.
We vary the exploration mean multiplier m ∈ {0.80, 0.82, . . . , 1.30} across four combinations of
within-rental exploration noise σ and cross-rental dispersion σν , each taking values in {0.02, 0.10}.
Figure 6 plots the 10th, 50th, and 90th percentiles of ∆j,T across rentals as a function of m, with
the calibrated average monopoly price as a benchmark.

Main pattern is consistent with theory. The main finding in Figure 6 is that terminal rents
exceed Nash across a wide range of m values and all four panels: supra-competitive outcomes are
the norm, not the exception. The median rent change is positive for most of the plotted range,
and the 10th percentile lies above Nash except near m = 1. The pattern of when prices are most
elevated is consistent with the analytical results. Terminal rents are closest to Nash near m = 1 and
rise when exploration is clustered away from Nash on either side, forming the U-shape predicted by
Theorem 3.3. The low-m side is especially steep, while the high-m side rises more gradually.




                                                  19
                                        = 0.02, v = 0.02                           = 0.10, v = 0.02
                       50
                       45                                                                            90th Percentile
                       40                                                                            50th Percentile




    % change vs Nash
                       35                                                                            10th Percentile
                       30                                                                            Avg Monopoly Price
                       25
                       20
                       15
                       10
                        5
                        0
                        5
                       10
                            0.8   0.9     1.0       1.1    1.2   1.3   0.8   0.9     1.0       1.1         1.2        1.3
                                                m                                          m
                                        = 0.02, v = 0.10                           = 0.10, v = 0.10
                       50
                       45
                       40



    % change vs Nash
                       35
                       30
                       25
                       20
                       15
                       10
                        5
                        0
                        5
                       10
                            0.8   0.9     1.0       1.1    1.2   1.3   0.8   0.9     1.0       1.1         1.2        1.3
                                                m                                          m

Figure 6: Terminal rent changes relative to Nash as the exploration mean multiplier m varies.
Each panel fixes the within-rental exploration noise σ and cross-rental dispersion σν , with K = 50
and T = 450. The percentile curves summarize the cross-section of rentals, while the horizontal
benchmark marks the average monopoly price. The main pattern is the same U-shape predicted by
the stylized model: prices are elevated when exploration is clustered away from Nash.


Variance drives attenuation to Nash. Cross-rental dispersion σν controls how clustered ex-
ploration is across rentals. When σν is small (top panels), exploration means are close together, and
the terminal price profile as a function of m closely matches the characterization in Theorem 3.3:
prices are near Nash when m ≈ 1 and rise toward the monopoly benchmark as m moves away
from Nash in either direction. When σν is larger (bottom panels), this correspondence weakens as
exploration means spread across rentals, though supra-competitive outcomes remain over a broad
range of m. Within-rental noise σ attenuates supra-competitiveness, especially when m > 1. Larger
σ induces more price variation for each rental, reducing the role of endogenous correlation during
exploitation. This attenuation is weaker for m < 1, where prices move more during exploitation
and therefore generate more correlated price variation after exploration.

5.3.2             Effect of time horizon

We now examine how the time horizon affects terminal prices. We fix σ = σν = 0.05 and vary
the exploitation horizon T ∈ [5, 200], comparing two exploration levels (m ∈ {0.80, 1.20}, placing
exploration below and above Nash) and two exploration lengths (K ∈ {10, 50}). Figure 7 plots the


                                                                  20
percentile curves of ∆j,T as a function of T .

                                               K = 10, m = 0.80                      K = 50, m = 0.80
                             40


               % change vs Nash
                             20                                                                      90th Percentile
                                                                                                     50th Percentile
                                                                                                     10th Percentile
                                      5   10     20       50      100 200   5   10     20       50      100 200
                                                       T                                     T
                                               K = 10, m = 1.20                      K = 50, m = 1.20
                             15


               % change vs Nash
                             10

                                  5
                                      5   10     20       50      100 200   5   10     20       50      100 200
                                                      T                                     T

Figure 7: Finite-time dynamics of terminal rent changes relative to Nash. We fix σ = σν = 0.05
and vary the exploitation horizon T on a log scale, comparing K ∈ {10, 50} and m ∈ {0.80, 1.20}.



Results show fast convergence. Figure 7 shows that supra-competitive rents emerge quickly
and do not require long exploitation horizons. The percentile curves are already above Nash at T = 5
in all four panels, and the curves flatten by moderate horizons such as T = 50. The strongest case is
K = 10, m = 0.80: even at the smallest plotted horizons, nearly all rentals are already substantially
supra-competitive, with the 10th percentile well above Nash. Across all panels, convergence to a
supra-competitive steady state is rapid: most of the price increase relative to Nash occurs within the
first T = 50 exploitation periods, and further exploitation yields diminishing additional movement.4
        Taken together, these simulations confirm that supra-competitive outcomes arise robustly in a
realistic rental market, persisting across a wide range of exploration parameters, finite time horizons,
heterogeneous products, and nonlinear demand.


6        Proof of Theorem 3.2: Convergence to Supra-competitive Prices
We outline the proof of Theorem 3.2, that limiting prices are strictly supra-competitive, by analyzing
the price-moments ODE from Definition 3.1. Throughout, let (U (τ ), V (τ )) denote the ODE state
    4
    The comparison across K should be interpreted through the normalized clock τ = (K + T )/K. Holding T fixed,
the K = 10 process has a larger τ than the K = 50 process, so it is farther along the ODE trajectory. This is why
the K = 10 curves tend to be closer to their apparent long-run levels at the same value of T , while the K = 50,
m = 0.80 panel starts lower but catches up quickly.




                                                                       21
and P (τ ) = P (U (τ ), V (τ )) the corresponding posted-price vector5 , so that the terminal price in
Theorem 3.2 is P ODE (τ ; µ, Σexp ) = P (τ ; µ, Σexp ).
       The argument has three steps. First, positive historical price correlation creates an omitted-
variable bias that pushes the misspecified OLS price above the true best response. Second, the best-
response cones initialize common-sign movements relative to running means, and this common-sign
pattern is forward invariant, so the induced positive cross-covariances persist through the dynamics.
Third, the persistent correlation bias yields prices greater than Nash. The core of the proof is the
forward-invariance argument in Step 2.

6.1      Step 1: Correlation bias raises OLS prices above best responses
The mechanism here is derived from omitted-variable bias. Firm i fits a one-dimensional demand
curve in its own price, omitting the competitor term cP̄−i from true demand (1). Positive cross-firm
price correlation therefore biases the fitted slope toward less price-sensitivity, so firm i prices above
                                                                                              1 X
the true best response. In the ODE notation, this correlation is captured by V̄i,−i :=                Vij .
                                                                                           N −1
                                                                                                          j̸=i
The following lemma states the bias implication precisely.

Lemma 6.1 (Correlation bias). Fix i ∈ [N ] and hold U and Vii fixed, with bVii − c V̄i,−i > 0. Then:

(1) if V̄i,−i = 0, then Pei (U, V ) = BR(Ū−i );

(2) Pei (U, V ) is strictly increasing in V̄i,−i .

       Thus zero cross-covariance gives exactly the best response to the historical average competitor
price, while positive cross-covariance pushes the price strictly above it (proof in Appendix G.1).
Conversely, without the correlation bias, the running-mean dynamics would reduce to iterated best
responses to historical average competitor prices. Based on the classical fictitious-play convergence
result of Robinson (1951), this leads to convergence to the symmetric Nash fixed point pNE 1.

6.2      Step 2: Best-response cones generate forward-invariant co-movements
We start by recalling the definition of best-response cones: for a set of exploration prices in a best-
response cone, all firms move in the same direction relative to their running means at the start of
exploitation.

Initialization of positive covariance. Independent exploration across firms leads to V̄i,−i (1) =
0, so by Lemma 6.1, Pi (1) = BR(µ̄−i ). Hence, on C + , the cone condition gives Ui (1) = µi >
BR(µ̄−i ) = Pi (1), so Pi (1) − Ui (1) < 0 for every i. Whereas for C − , the inequalities reverse, so
Pi (1) − Ui (1) > 0 for every i. In either case, all firms initially move in the same direction relative
to their exploration means. Since V̇ij = (Pi − Ui )(Pj − Uj ), these common-sign gaps give V̇ij (1) > 0
for every i ̸= j, and hence V̄i,−i (τ ) > 0 for τ slightly above 1.
   5
    To keep the main-text proof focused, we state the intuition in the interior case, where the posted price is not
clipped at Pmin or Pmax ; the appendices prove the corresponding statements for the full capped price map.


                                                        22
Forward invariance. The following lemma presents the key step, which is that the co-movement
relative to running means is self-sustaining. We interpret this as follows: starting from C + , once
all firms price below their running means, no firm can be the first to cross above its running mean;
likewise, for C − , the analogous statement holds.
Lemma 6.2 (Forward invariance of common-sign gap). Fix τ0 ≥ 1. If P − U ⪯ 0 at time τ0 , then
P − U ⪯ 0 for all τ ≥ τ0 . Likewise, if P − U ⪰ 0 at time τ0 , then P − U ⪰ 0 for all τ ≥ τ0 .
   We give the intuition for the C + case; the C − case is the same with signs reversed. Suppose firm
i reaches the boundary Pi = Ui at time τ = τ ⋆ , while every other firm still has Pj − Uj ≤ 0. We
want to show that firm i’s price does not move upward at this moment, so the gap Pi − Ui cannot
rise above zero. At this boundary,

                              U̇i (τ ⋆ ) = 0,        V̇ii (τ ⋆ ) = 0,       V̄˙ i,−i (τ ⋆ ) = 0,        (10)

because each derivative carries the factor Pi − Ui . Thus firm i’s own running mean, own variance,
and average cross-covariance are momentarily frozen.
   Recall that firm i fits the linear demand curve Qi ≈ α
                                                        bi + βbi Pi . In terms of the ODE moments,
the fitted coefficients are

                                                          V̄i,−i                     V̄i,−i
                              bi = a + cŪ−i − cUi
                              α                                  ,      βbi = −b + c        .
                                                           Vii                        Vii

Using (10), we have
                                                                         ˙
                                     b˙ i (τ ⋆ ) = c Ū˙ −i (τ ⋆ ),
                                     α                                  βbi (τ ⋆ ) = 0.

Since βbi (τ ⋆ ) < 0, the price Pei = −b
                                       αi /(2βbi ) moves in the same direction as the fitted intercept α
                                                                                                       bi .
                                                                                              ˙
The other firms have Pj − Uj ≤ 0, so their running means satisfy U̇j ≤ 0 and therefore Ū−i (τ ) ≤ 0.
                                                                                                   ⋆
       ˙
Thus Pei (τ ⋆ ) ≤ 0. Combined with U̇i (τ ⋆ ) = 0, this implies that Pi −Ui cannot cross from nonpositive
to positive at the boundary. In the C − case, the same argument gives Ū˙ (τ ⋆ ) ≥ 0 and prevents  −i
Pi −Ui from crossing from nonnegative to negative. The formal proof is in Appendices G.2 and G.10.

Consequence for correlation. Because the common-sign gap persists for all τ , the covariance
equation V̇ij = (Pi − Ui )(Pj − Uj ) keeps the average cross-covariances V̄i,−i (τ ) nonnegative through-
out; after the strict initial common-sign movement, they are strictly positive for all τ > 1.

6.3    Step 3: Correlation bias gives a Nash lower bound
Combining Steps 1 and 2, we conclude that as the average cross-covariances remain nonnegative,
each firm’s price is at least its best response to the historical average competitor price. The following
lemma then formalizes the dynamics to connect this observation to the limiting price vector.
Lemma 6.3 (Nash lower bound from nonnegative correlation bias). Along any solution of the price-
moments ODE, assume (i) V̄i,−i (τ ) ≥ 0 for all i and τ ≥ 1, and (ii) U is componentwise monotone
in τ . Then the limit U ∞ := limτ →∞ U (τ ) exists and satisfies U ∞ ⪰ pNE 1.

                                                              23
    The argument is by contradiction. If the lowest limiting component were below Nash, then that
firm’s true best response to the limiting historical average of its competitors would exceed its own
limiting mean. The nonnegative correlation bias only strengthens this push, so for all large τ the
firm would have a persistent positive gap Pi (τ ) − Ui (τ ), contradicting convergence of Ui (τ ).
    For µ ∈ C + this completes Theorem 3.2(a): since µ ≻ pNE 1 and the sign-reversed argument
gives P − U ⪯ 0 with positive cross-covariances for all τ > 1, Lemmas 6.1 and 6.3 yield Pi (τ ) > pNE
for every i and every τ ≥ 1 (Appendix G.11), hence

                          P ODE (τ ; µ, Σexp ) ≻ pNE 1   for every τ ∈ [1, ∞).

For µ ∈ C − , Lemma 6.3 gives only the weak bound U ∞ ⪰ pNE 1, and it remains to exclude conver-
gence exactly to Nash. We prove this by contradiction, by showing that convergence to Nash would
leave the cross-covariances at strictly positive limits. The formal argument is in Appendix G.




7    Conclusion
This paper demonstrates that simple estimate-then-optimize pricing algorithms, relying on mis-
specified demand models, can lead to supra-competitive prices. The mechanism does not rely on
punishment, communication, or explicit coordination. Instead, independent exploratory histories
can generate price movements that become positively correlated during exploitation; this correla-
tion creates omitted-variable bias, making firms perceive demand as less price-sensitive and leading
them to choose prices above the competitive benchmark.
    We close with a brief discussion of our modeling assumptions. Our results rest on one core as-
sumption: each firm fits a misspecified demand model that ignores competitors’ prices. Several other
assumptions are for tractability rather than substance: linear demand and symmetric firms simplify
the analysis, and the empirically calibrated simulations of Section 5 show that supra-competitive
outcomes persist under nonlinear (logit) demand, heterogeneous products, and asymmetric costs.
The common exploration length K across firms is a modeling normalization for summarizing ini-
tial histories, not an assumption that firms coordinate on phase timing. The fluid scaling regime
(K, T → ∞ with (K + T )/K → τ ) is what yields the deterministic ODE limit, but the underlying
stochastic dynamics show the same qualitative behavior at moderate finite horizons (Section 4.2).
Finally, we deliberately impose independent exploration across firms, so the supra-competitive out-
comes we establish emerge endogenously and not from any coordinated experimentation, in contrast
to Lin and Sarıtaç (2025).
    Future work could extend the paper in several directions. One direction is a theoretical exten-
sion to nonlinear demand or asymmetric firms (which our simulations already suggest is robust).
Another is to consider dynamics with persistent demand shocks or ongoing experimentation. Lastly,
characterizing when analogous biases arise in other supermodular games would show how broadly
the supra-competitive channel extends beyond multi-firm pricing dynamics.

                                                    24
References
I. Abada and X. Lambin. Artificial intelligence: Can seemingly collusive outcomes be avoided?
  Management Science, 69(9):5042–5065, 2023. doi: 10.1287/mnsc.2022.4623.

I. Abada, X. Lambin, and N. Tchakarov. Collusion by mistake: Does algorithmic sophistication drive
  supra-competitive profits? European Journal of Operational Research, 318(3):927–953, 2024. doi:
  10.1016/j.ejor.2024.06.006.

A. Aouad and A. V. den Boer. Algorithmic collusion in assortment games. Available at SSRN
  3930364, 2021. doi: 10.2139/ssrn.3930364. URL https://ssrn.com/abstract=3930364.

E. R. Arunachaleswaran, N. Collina, S. Kannan, A. Roth, and J. Ziani. Algorithmic collusion
  without threats. In R. Meka, editor, 16th Innovations in Theoretical Computer Science Con-
  ference (ITCS 2025), volume 325 of Leibniz International Proceedings in Informatics (LIPIcs),
  pages 10:1–10:21, Dagstuhl, Germany, 2025. Schloss Dagstuhl – Leibniz-Zentrum für Informatik.
  ISBN 978-3-95977-361-4. doi: 10.4230/LIPIcs.ITCS.2025.10. URL https://drops.dagstuhl.
  de/entities/document/10.4230/LIPIcs.ITCS.2025.10.

J. Asker, C. Fershtman, and A. Pakes. Artificial intelligence, algorithm design, and pricing. AEA
  Papers and Proceedings, 112:452–456, 2022. doi: 10.1257/pandp.20221059.

S. Assad, R. Clark, D. Ershov, and L. Xu. Algorithmic pricing and competition: Empirical evidence
  from the German retail gasoline market. Journal of Political Economy, 132(3):723–771, 2024. doi:
  10.1086/726906.

Y. Aviv and A. Pazgal. Pricing of short life-cycle products through active learning. Working paper,
  Olin School of Business, Washington University in St. Louis, 2002.

M. Banchio and G. Mantegazza. Artificial intelligence and spontaneous collusion. arXiv preprint
  arXiv:2202.05946, 2022. URL https://arxiv.org/abs/2202.05946.

M. Bichler, J. Durmann, and M. Oberlechner. Online optimization algorithms in repeated price
  competition: Equilibrium learning and algorithmic collusion, 2024. URL https://arxiv.org/
  abs/2412.15707.

Z. Y. Brown and A. MacKay. Competition in pricing algorithms. American Economic Journal:
  Microeconomics, 15(2):109–156, 2023. doi: 10.1257/mic.20210158.

S. Calder-Wang and G. H. Kim. Algorithmic pricing in multifamily rentals: Efficiency gains or
  price coordination? Available at SSRN 4403058, 2024. doi: 10.2139/ssrn.4403058. URL https:
  //ssrn.com/abstract=4403058.

E. Calvano, G. Calzolari, V. Denicolò, and S. Pastorello. Artificial intelligence, algorithmic pricing,
  and collusion. American Economic Review, 110(10):3267–3297, 2020. doi: 10.1257/aer.20190623.

                                                  25
L. Chen, A. Mislove, and C. Wilson. An empirical analysis of algorithmic pricing on Amazon
  Marketplace. In Proceedings of the 25th International Conference on World Wide Web, pages
  1339–1349, 2016. doi: 10.1145/2872427.2883089.

W. L. Cooper, T. Homem-de-Mello, and A. J. Kleywegt. Learning and pricing with models that do
  not explicitly incorporate competition. Operations Research, 63(1):86–103, 2015. doi: 10.1287/
  opre.2014.1341.

A. V. den Boer, J. M. Meylahn, and M. P. Schinkel. Artificial collusion: Examining supracom-
  petitive pricing by Q-learning algorithms. Amsterdam Law School Research Paper No. 2022-25;
  Amsterdam Center for Law & Economics Working Paper No. 2022-06; available at SSRN 4213600,
  2024. URL https://ssrn.com/abstract=4213600.

C. Douglas, F. Provost, and A. Sundararajan.           The illusion of collusion.   arXiv preprint
  arXiv:2411.16574, 2024. URL https://arxiv.org/abs/2411.16574.

V. F. Farias and B. Van Roy. Dynamic pricing with a prior on market response. Operations Research,
  58(1):16–29, 2010. doi: 10.1287/opre.1090.0729.

S. Fish, Y. A. Gonczarowski, and R. I. Shorrer. Algorithmic collusion by large language models.
  arXiv preprint arXiv:2404.00806, 2024. URL https://arxiv.org/abs/2404.00806.

E. J. Green and R. H. Porter. Noncooperative collusion under imperfect price information. Econo-
  metrica, 52(1):87–100, 1984. doi: 10.2307/1911462.

K. T. Hansen, K. Misra, and M. M. Pai. Frontiers: Algorithmic collusion: Supra-competitive prices
  via independent algorithms. Marketing Science, 40(1):1–12, 2021. doi: 10.1287/mksc.2020.1276.

M. Hettich. Algorithmic collusion: Insights from deep learning. Available at SSRN 3785966, 2021.
  doi: 10.2139/ssrn.3785966. URL https://ssrn.com/abstract=3785966.

J. Keppo, Y. Li, G. Tsoukalas, and N. Yuan. AI pricing, agent heterogeneity, and collusion. Avail-
  able at SSRN 5386338, 2025. doi: 10.2139/ssrn.5386338. URL https://ssrn.com/abstract=
  5386338.

A. P. Kirman. Learning by firms about demand conditions. In R. H. Day and T. Groves, editors,
  Adaptive Economic Models, pages 137–156. Academic Press, New York, 1975.

A. P. Kirman. On mistaken beliefs and resultant equilibria. In R. Frydman and E. S. Phelps, editors,
  Individual Forecasting and Aggregate Outcomes: “Rational Expectations” Examined, pages 147–
  168. Cambridge University Press, Cambridge, 1986.

A. P. Kirman. Learning in oligopoly: Theory, simulation, and experimental evidence. In A. P.
  Kirman and M. Salmon, editors, Learning and Rationality in Economics, pages 127–178. B.
  Blackwell, Oxford, UK and Cambridge, MA, 1995.


                                                26
T. Klein. Autonomous algorithmic collusion: Q-learning under sequential pricing. The RAND
  Journal of Economics, 52(3):538–558, 2021. doi: 10.1111/1756-2171.12383.

M. A. Lariviere and E. L. Porteus. Stalking information: Bayesian inventory management with
  unobserved lost sales. Management Science, 45(3):346–363, 1999. doi: 10.1287/mnsc.45.3.346.

B. Light and W. Wang. Conjectural variations in competitive dynamic pricing: A learning foun-
  dation via experimentation design and feedback structure, 2026. URL https://arxiv.org/abs/
  2602.12888.

M. Lin and Ö. Sarıtaç. Competition in pricing algorithms: Stability, exploration, and supracompeti-
  tive outcomes. Available at SSRN 5958355, December 2025. URL https://ssrn.com/abstract=
  5958355.

T. Loots and A. V. den Boer. Data-driven collusion and competition in a pricing duopoly with
  multinomial logit demand. Production and Operations Management, 32(4):1169–1186, 2023. doi:
  10.1111/poms.13919.

E. Maskin and J. Tirole. A theory of dynamic oligopoly, II: Price competition, kinked demand
  curves, and edgeworth cycles. Econometrica, 56(3):571–599, 1988. doi: 10.2307/1911701.

J. M. Meylahn and A. V. den Boer. Learning to collude in a pricing duopoly. Manufacturing &
  Service Operations Management, 24(5):2577–2594, 2022. doi: 10.1287/msom.2021.1074.

J. Robinson. An iterative method of solving a game. Annals of Mathematics, 54(2):296–301, 1951.

H. A. Simon. Dynamic programming under uncertainty with a quadratic criterion function. Econo-
  metrica, 24(1):74–81, 1956.

R. S. Sutton and A. G. Barto. Reinforcement Learning: An Introduction. MIT Press, Cambridge,
  MA, 1998.

Z. Yang, X. Lei, and P. Gao. Regulating discriminatory pricing in the presence of tacit collu-
  sion. Available at SSRN 4633784, 2023. doi: 10.2139/ssrn.4633784. URL https://ssrn.com/
  abstract=4633784.

Z. Yang, P. Gao, and Z. Wang. Driven to collusion: Competitive pricing under independent demand
  model and price imitation, 2026. URL https://ssrn.com/abstract=6197578. Available at SSRN
  6197578.




                                                27
Appendix Table of Contents

A Derivation of the Bayesian Interpretation (Section 2.2)                                                       28

B Discussion of multiplicity of steady states in Cooper et al. (2015)                                           32

C Supplemental general-N computational simulations (Section 4.1)                                                33

D Details for the Empirically Calibrated Simulations (Section 5)                                                36

E Proof of Theorem 3.1: convergence to the price-moments ODE (Section 3.1)                                      37

F Omitted Lemmas in Proof of Theorem 3.1 (Section 3.1)                                                          43

G Omitted Steps and Lemmas in Theorem 3.2 (Sections 3.2, 6)                                                     61

H Proofs for the Symmetric-History Results (Section 3.2)                                                        76

I   Proofs for the Best-Response Cone Characterizations (Section 3.3)                                           80




A     Derivation of the Bayesian Interpretation (Section 2.2)
This appendix formalizes the Bayesian interpretation of initialization. It first derives estimate-then-
optimize from Bayesian linear regression, then shows that the exploration-implied prior generates
the price-moments ODE.

A.1     Estimate-then-optimize as Bayesian linear regression
The estimate-then-optimize step can be read as a certainty-equivalent Bayesian rule. Fix firm i,
and write the misspecified own-price demand model as

                                          Qi ≈ αi + βi Pi ,         θi := (αi , βi )⊤ .

For an observation s, define the design vector xi,s := (1, Pi,s )⊤ . We write the Bayesian regression
in normalized information units, suppressing a common observation-noise scale since only posterior
mean coefficients enter the pricing rule.
Proposition A.1 (Bayesian form of estimate-then-optimize). Suppose firm i has Gaussian prior
θi ∼ N (m0i , (Λ0i )−1 ). After observing {(Pi,s , Qi,s )}s≤t , its posterior mean is

                                      !                            −1                                 
                              α
                              bi,t                   X                                    X
                    θbi,t =               = Λ0i +         xi,s x⊤
                                                                 i,s
                                                                        Λ0i m0i +             xi,s Qi,s  .
                              βbi,t                  s≤t                                  s≤t


                                                               28
If firm i posts the posterior-mean optimal price,

                                   Pi,t+1 ∈     arg max p(b
                                                          αi,t + βbi,t p),
                                              p∈[Pmin ,Pmax ]


then the policy is the same estimate-then-optimize rule as in the main model, with the fitted demand
curve interpreted as a posterior mean demand curve.
   Proof. The likelihood under the normalized Gaussian linear model is proportional to
                                                               
                                         1X                    
                                                      ⊤       2
                                     exp −   (Qi,s − xi,s θi ) .
                                         2                     
                                                  s≤t


The Gaussian prior density is proportional to
                                                               
                                       1       0 ⊤ 0         0
                                  exp − (θi − mi ) Λi (θi − mi ) .
                                       2

Multiplying likelihood and prior gives a posterior density proportional to
                                                                           
                  1            X                                 X                
              exp − θi⊤ Λ0i +   xi,s x⊤
                                        i,s
                                             θ i − 2θ ⊤ 0 0
                                                       i  Λ  m
                                                            i i +   x i,s Q i,s    .
                  2                                                               
                                      s≤t                                        s≤t


Thus the posterior precision is
                                                          X
                                         Λi,t = Λ0i +           xi,s x⊤
                                                                      i,s ,
                                                          s≤t

and the posterior information vector is
                                                             X
                                       ri,t = Λ0i m0i +            xi,s Qi,s .
                                                             s≤t


The posterior mean is therefore θbi,t = Λ−1
                                         i,t ri,t , as claimed.
   Given this posterior mean, the posterior-mean predicted demand curve is

                                            qbi,t (p) = α
                                                        bi,t + βbi,t p.

A certainty-equivalent Bayesian firm maximizes posterior-mean predicted profit pb
                                                                                qi,t (p) over the
feasible interval. This is exactly the estimate-then-optimize step in the main model. With the
improper flat prior Λ0i = 0, the posterior mean reduces to the ordinary least-squares estimate based
only on the observed data.

A.2    The exploration-implied prior and the price-moments ODE
We now choose the prior so that its sufficient statistics match the population moments generated
by the exploration phase. This shows that the same price-moments ODE can be obtained without

                                                        29
explicitly referring to a finite exploration sample.
    For each firm i, let σi,exp
                          2     := (Σexp )ii , and set
                                                  !                                          !
                                      a + cµ̄−i                          1         µi
                           m0i :=                     ,        Λ0i :=                            .
                                         −b                             µi µ2i + σi,exp
                                                                                  2



Thus the prior mean curve is qi0 (p) = a − bp + cµ̄−i : firm i’s own-price model treats competitors’
prices as fixed at their prior reference levels. The precision matrix makes µi the price at which the
prior demand curve is most tightly pinned down. Indeed,

                                                                         (p − µi )2
                                     (1, p)(Λ0i )−1 (1, p)⊤ = 1 +           2       .
                                                                           σi,exp

So µi is a prior price center, not a prior optimal price.

Proposition A.2 (Bayesian representation of the price-moments ODE). Suppose each firm i has
prior θi ∼ N (m0i , (Λ0i )−1 ), with m0i and Λ0i defined above. Normalize the prior mass to one, and
let firms update their Bayesian sufficient statistics continuously while posting the posterior-mean
optimal price. Then the induced continuous-time dynamics reduce to the price-moments ODE:

                                                   P (t) − U (t)
  U (1) = µ,        V (1) = Σexp ,      U̇ (t) =                 ,           V̇ (t) = (P (t) − U (t))(P (t) − U (t))⊤ ,
                                                         t

with the same posted-price map as in Definition 3.1.

    Proof. Let
                                M (t) = M P (t), M Q (t), M P P (t), M P Q (t)
                                                                                        


denote the normalized posterior moment state. Here M P and M Q are price and quantity means,
M P P is the raw price second-moment matrix, and M P Q is the vector of own price-quantity moments.
    The prior induces the initial moments

                              MiP (1) = µi ,              MijP P (1) = µi µj + (Σexp )ij .

Since Σexp is diagonal in the main model, the prior also gives

                     MiQ (1) = a − bµi + cµ̄−i ,              MiP Q (1) = µi MiQ (1) − b(Σexp )ii .

These are exactly the population moments of the exploration distribution, now read as prior suffi-
cient statistics.
    Given a posted price vector P (t), write true mean demand as

                                      di (P (t)) := a − bPi (t) + cP̄−i (t).




                                                              30
The continuous-time Bayesian sufficient-statistic updates are the running-average equations

                                           Pi − MiP                    di (P ) − MiQ
                                ṀiP =              ,        ṀiQ =                  ,
                                               t                              t

                                       Pi Pj − MijP P                    Pi di (P ) − MiP Q
                           ṀijP P =                  ,      ṀiP Q =                       .
                                             t                                     t
Define                                                                               
                       U (t) := M P (t),            V (t) := t M P P (t) − U (t)U (t)⊤ .

Then U (1) = µ and V (1) = Σexp . The first running-average equation gives

                                                            P −U
                                                     U̇ =        .
                                                              t

For V , differentiate V = t(M P P − U U ⊤ ). Using

                                               PP⊤ − MPP                      P −U
                                  Ṁ P P =               ,             U̇ =        ,
                                                   t                            t

we obtain
                                               V̇ = (P − U )(P − U )⊤ .

Thus the state dynamics match the price-moments ODE.
   It remains to recover the posted-price map from (U, V ). First,

                                         MiQ (t) = a − bUi (t) + cŪ−i (t).

This holds because both sides agree at t = 1, and differentiating the right-hand side gives the same
running-average equation as ṀiQ = (di (P ) − MiQ )/t.
   Next,
                                                                 −bVii (t) + cV̄i,−i (t)
                               MiP Q (t) = Ui (t)MiQ (t) +                               .
                                                                           t
To see this, let
                                         Ci (t) := MiP Q (t) − Ui (t)MiQ (t).

Then
                                               (Pi − Ui )(di (P ) − MiQ ) − Ci
                                       Ċi =                                   .
                                                               t
Using di (P ) − MiQ = −b(Pi − Ui ) + c(P̄−i − Ū−i ), this becomes

                                    −b(Pi − Ui )2 + c(Pi − Ui )(P̄−i − Ū−i ) − Ci
                            Ċi =                                                  .
                                                         t

The quantity (−bVii +cV̄i,−i )/t satisfies the same differential equation and has the same initial value,
so the identity follows.


                                                            31
    The posterior mean slope is therefore

                                    M P Q (t) − MiP (t)MiQ (t)          V̄i,−i (t)
                           βbi (t) = i P P           P    2
                                                               = −b + c            .
                                     Mii (t) − (Mi (t))                  Vii (t)

The posterior mean intercept is

                                                                                   V̄i,−i (t)
                      bi (t) = MiQ (t) − βbi (t)Ui (t) = a + cŪ−i (t) − cUi (t)
                      α                                                                       .
                                                                                    Vii (t)

On the interior branch, the posterior-mean optimal price is

                                    αbi (t)   (a + cŪ−i (t))Vii (t) − cUi (t)V̄i,−i (t)
                        Pei (t) = −         =                                            .
                                    2βi (t)
                                      b              2(bVii (t) − cV̄i,−i (t))

Adding the same clipping and nonnegative-slope branch as in Definition 3.1 gives exactly the posted-
price map in the price-moments ODE. This proves the proposition.


B     Discussion of multiplicity of steady states in Cooper et al. (2015)
Cooper et al. (2015) show that estimate-then-optimize dynamics admit a range of steady-state prices,
spanning sub-competitive to supra-competitive, depending on initial conditions. The following
proposition establishes the analog within our framework: for a range of target prices spanning both
below and above Nash, there exist initial conditions (µ, Σexp ) under which the price-moments ODE
is stationary at p∗ (with P (t) = U (t) = p∗ for all t ≥ 1), provided Σexp is allowed to be non-diagonal.

Proposition B.1 (Cooper-style multiplicity). For any target p∗ ∈ [p∗min , min(pMNP , Pmax )], where

                                                      a(N − 1)
                                       p∗min :=                       ,
                                                  (N − 1)(2b − c) + c

the following is a steady-state initialization of the price-moments ODE: µi = p∗ for all i, and
Vii (1) = σ 2 , Vij (1) = ρ∗ σ 2 for i ̸= j, where ρ∗ := (2b − c)(p∗ − pNE )/(c p∗ ) and σ 2 > 0 is arbitrary.
The resulting dynamics satisfy Pi (t) = Ui (t) = p∗ for all i and all t ≥ 1.

    Proof of Proposition B.1.      Substituting into (7) gives Pei = (a + cp∗ (1 − ρ∗ ))/(2(b − cρ∗ )) = p∗
by the definition of ρ∗ . The range p∗ ∈ [p∗min , min(pMNP , Pmax )] corresponds to ρ∗ ∈ [−1/(N − 1), 1],
which makes Σexp positive semi-definite. Hence Pi (1) = p∗ = Ui (1), so U̇ (1) = V̇ (1) = 0 and the
state remains at (p∗ 1, Σexp ) for all t ≥ 1.
    Note that p∗min < pNE : the ratio p∗min /pNE = (N − 1)(2b − c)/[(N − 1)(2b − c) + c] is strictly
less than 1, approaching 1 as N → ∞. Hence the achievable range always contains a strictly sub-
Nash region. Under the independent exploration of our model (Σexp diagonal, so ρ∗ = 0), the only
steady-state initialization is the symmetric Nash profile µ = pNE 1; Proposition B.1 shows that other
steady-state initializations exist only by allowing correlated initial covariance.


                                                       32
C     Supplemental general-N computational simulations (Section 4.1)
The duopoly heatmaps in Section 4.1 are useful because, when N = 2, the exploration-mean space
is two-dimensional and the full terminal-price map can be swept directly. For general N , the
terminal-price map is a function on an N -dimensional hypercube, so an exhaustive visualization
is no longer available. This appendix therefore uses the same price-moments ODE to study two
clustered exploration designs for general N . These designs are not intended to characterize the
full hypercube. Rather, they evaluate the ODE on broad and interpretable families of exploration
profiles in which firms experiment around a common local price band or a common anchor price.
    Throughout, unless otherwise noted, we use the same primitives as in Section 4.1: a = b = 1
and c = 1/2, so that pNE = 2/3 and pMNP = 1. The simulations in this appendix restrict the
exploration covariance to the scalar form

                                                     2
                                             Σexp = σexp IN ,

where σexp is the common exploration standard deviation. For N > 2, when reporting a scalar
terminal price, we use the cross-firm average

                                                            N
                                                       1 X ODE
                            P̄ ODE (τ ; µ, Σexp ) :=      Pi   (τ ; µ, Σexp ).
                                                       N
                                                            i=1

Under the scalar covariance specification above, this is

                                                            N
                                                       1 X ODE          2
                         P̄ ODE (τ ; µ, σexp
                                         2
                                             IN ) =       Pi   (τ ; µ, σexp IN ).
                                                       N
                                                         i=1


C.1    Interval sampling
Motivation. The first design is the general-N analogue of the “similar exploration prices” empha-
sized by the cone analysis. Instead of attempting to sample uniformly from the full N -dimensional
exploration-mean space, we draw firms’ exploration means from a common interval. This focuses
attention on clustered profiles, where firms explore within the same local price band.

Design. For each boundary pair (ℓ, u) with 0.40 ≤ ℓ < u ≤ 1.00, we fix two exploration means at
the endpoints and draw the remaining firms inside the interval:

                                                                iid
                  µ1 = ℓ,       µ2 = u,        µi | (ℓ, u) ∼ Unif[ℓ, u],   i = 3, . . . , N.

This is the computational analogue of the random-interval prior in Definition 3.3: two firms deter-
mine a local price band, and the remaining firms explore within that same band. For each sampled
profile, we solve the price-moments ODE with Σexp = σexp
                                                     2 I
                                                         N and record the mean terminal price
                2 I ). The figure uses N = 10 and σ
P̄ ODE (τ ; µ, σexp N                              exp = 0.10. Each boundary pair averages over 100



                                                       33
independent draws of the interior N − 2 exploration means. For visualization, we symmetrize the
heatmap: cells with µ2 < µ1 are filled using the value from the corresponding flipped pair (µ2 , µ1 ).


                        1.00
                                     N = 10,    exp = 0.10                1.00

                        0.90
                                                                          0.83
                        0.80


                                                                            Mean price
                    1   0.70                                              0.67


                        0.60
                                                                          0.50
                        0.50

                        0.40                                              0.33
                           0.40 0.50 0.60 0.70 0.80 0.90 1.00
                                                 2
Figure 8: ODE-implied mean terminal price under interval sampling. For each boundary pair
0.40 ≤ ℓ < u ≤ 1.00 on a grid with increments of 0.01, two exploration means are fixed at ℓ and u,
and the remaining N − 2 means are drawn uniformly from [ℓ, u]. Each boundary pair averages over
100 draws, with N = 10 and scalar exploration covariance Σexp = 0.102 IN . White is centered at the
Nash price; red and blue indicate supra-competitive and sub-competitive mean prices, respectively.
The heatmap is then symmetrized by assigning cells with µ2 < µ1 the value from the flipped pair.



Results. Figure 8 shows that the cone calculation is conservative. Across boundary pairs, 78.6%
have mean terminal price above Nash. At the simulation level, 74.2% of draws have total profit
above the Nash total-profit benchmark, and 70.2% of boundary pairs have average total profit
above that benchmark. The overall mean terminal price is 0.758, compared with pNE = 0.667, and
the range of mean terminal prices is [0.652, 1.000]. Thus, within this family of clustered general-
N exploration profiles, sub-competitive outcomes remain close to Nash, while supra-competitive
outcomes can reach the monopoly benchmark.

C.2    Center–dispersion sampling
Motivation. The second design parameterizes clustered exploration profiles by a common anchor
price and a dispersion level. This separates the location of the exploration cluster from the amount
of cross-firm heterogeneity. Small dispersion approximates symmetric exploration, while larger
dispersion tests how robust the qualitative pattern is when firms’ exploration means are no longer
nearly identical.



                                                 34
 Design. For an anchor price s and dispersion parameter ν, draw

                                                iid           √             √
                                             µi ∼ Unif[s −        3ν, s +       3ν],         i = 1, . . . , N.

 Thus s controls the location of the exploration cluster and ν controls cross-firm heterogeneity. The
       √
 factor 3 normalizes ν as the standard deviation of the cross-firm exploration means. We solve the
 price-moments ODE with N = 10 and compare ν ∈ {0.02, 0.10} and scalar exploration covariances
         2 I with σ
 Σexp = σexp N      exp ∈ {0.02, 0.10}.


                                        N = 10, = 0.02                                              N = 10, = 0.10
                          Monopoly price                                           Monopoly price
                   1.00
                   0.95



Mean final price
                   0.90
                   0.85
                   0.80
                                                                   exp = 0.02                                             exp = 0.02
                   0.75                                            exp = 0.10                                             exp = 0.10

                   0.70
                          Nash price                                               Nash price
                   0.65
                           0.4         0.6      0.8     1.0         1.2                0.4         0.6      0.8     1.0   1.2
                                             Anchor price                                                Anchor price
 Figure 9: Mean terminal price under center–dispersion sampling.
                                                              √        For
                                                                        √ each anchor price s, ex-
 ploration means are drawn independently from Unif[s − 3ν, s + 3ν]. The panels compare
 cross-firm dispersion levels ν ∈ {0.02, 0.10}, and the lines compare scalar exploration covariances
               N with σexp ∈ {0.02, 0.10}, using N = 10. Dashed horizontal and vertical lines mark
           2 I
 Σexp = σexp
 the Nash and monopoly benchmarks.


 Results. The pattern in Figure 9 mirrors the symmetric-exploration benchmark. Prices are closest
 to Nash when the anchor is near pNE , and they rise substantially when the anchor is below Nash
 or above the monopoly benchmark. Increasing either the cross-firm dispersion ν or the common
 exploration standard deviation σexp attenuates the supra-competitive effect, but the qualitative
 shape remains stable.
                   Taken together, these general-N simulations are not an exhaustive statement about the full
 exploration-mean space. They instead evaluate the ODE on broad families of clustered profiles.
 Within these families, supra-competitive outcomes arise more broadly than the analytical cone
 certificate alone would imply.




                                                                          35
D     Details for the Empirically Calibrated Simulations (Section 5)
This appendix collects deferred details for the empirically calibrated simulation design described in
Section 5. The demand and observed rents are calibrated from data, while the pricing dynamics are
simulated counterfactually on top of that calibrated environment.

D.1       Demand-side parameterization
Recall the random-coefficients logit demand system from Section 5:
                                                                            
                                    H
                                    X              exp αh Pj,t + x′j βh + ξj
                       sj,t (Pt ; ξ) =     w̃h     PN                             .
                                               1 +      exp α   P     + x ′β +ξ
                                       h=1          k=1       h   k,t     k h   k


This demand system converts any rent vector into predicted market shares by aggregating hetero-
geneous household choice probabilities. The covariates xj are observed rental characteristics (e.g.,
bedrooms, new-building indicators, and quality proxies). The renter-specific coefficients (αh , βh )
are set as in Calder-Wang and Kim (2024): αh < 0 is a decreasing linear function of log income,
and βh uses their estimated interaction structure (Table 13 of Calder-Wang and Kim, 2024).
    The vertical-differentiation fixed effects {ξj }N
                                                    j=1 are calibrated so that at observed rents p0 , the
model matches the observed shares s0 :

                                sj (p0 ; ξ) = sj0    for each j = 1, . . . , N.

These fixed effects absorb product-specific vertical quality not captured by observed characteristics,
so the calibrated model exactly matches baseline shares.

D.2       Calibration of the shadow costs
We calibrate λ = (λj )N
                      j=1 so that the observed rent vector p0 is the Nash equilibrium of the calibrated
static game. These shadow costs are not observed accounting costs; they are supply-side primitives
chosen to rationalize observed rents as Nash. Formally, firm j solves
                                                                     
                                    max(pj − λj ) sj (pj , p−j,0 ); ξ ,
                                      pj


taking rivals’ rents as fixed at p−j,0 . We set λj so that the first-order condition holds at pj0 :

                                                      ∂sj
                        0 = sj (p0 ; ξ) + pj0 − λj         (p0 ; ξ),        j = 1, . . . , N.
                                                       ∂pj

Because the demand side is calibrated so that sj (p0 ; ξ) = sj0 , this pins down a unique λj for each
rental:
                                                            sj0
                                       λj = pj0 +                       .
                                                      ∂sj /∂pj (p0 ; ξ)



                                                       36
D.3    Explore-then-exploit pipeline: full equations
We provide the full equations for the explore-then-exploit dynamics.

Exploration. Fix an exploration mean µj for each rental j. During t = 1, . . . , K, rental j posts
a perturbed price
                                                                  i.i.d.
                                Pj,t = µj (1 + vj,t ),        vj,t ∼ N (0, σ 2 ),

clipped to [0, P̄ ], where P̄ is a large exogenous upper bound.

Exploitation. For t ≥ K, each rental j estimates a naive binary logit using only its own price-
share history {(Pj,r , sj,r )}r≤t , treating competitors’ prices as unobserved:
                                           s       
                                              j,r
                            yj,r := log               ≈ ηj,t + θj,t Pj,r ,     r ≤ t.
                                           1 − sj,r

Here “naive” means that the fitted logit is one-product and own-price only, even though true shares
depend on all rents. This yields (η̂j,t , θ̂j,t ) and a predicted share ŝj,t (p) = Λ(η̂j,t + θ̂j,t p), where
Λ(z) = (1 + e−z )−1 is the logistic function. The next-period rent is set by myopically maximizing
predicted profit:

                     Pj,t+1 ∈ arg max (p − λj )ŝj,t (p),           t = K, . . . , K + T − 1.
                                  p∈[0,P̄ ]


E     Proof of Theorem 3.1: convergence to the price-moments ODE
      (Section 3.1)
This appendix proves Theorem 3.1. The proof is organized in three steps. First, we write the
empirical price–quantity moments as a stochastic approximation recursion. Second, we show that
this recursion tracks a deterministic mean-field ODE on the fluid time scale. Third, we identify the
posted-price coordinate of that ODE with the price-moments ODE in Definition 3.1.
    The argument is written for the diagonal exploration covariance matrix Σexp from the model
section, with positive diagonal entries. Proofs of the auxiliary lemmas stated below are collected in
Appendix F.
    The main point is that the stochastic process and the ODE are written in two different coor-
dinate systems. We first prove convergence in a raw empirical-moment state, where the stochastic
approximation is transparent, and only afterward change variables to the centered price moments
used in the main text.

E.1    Empirical moments and the OLS price map
We begin by defining a state that contains exactly the information used by each firm’s own-price
OLS regression and by the conditional mean of the next observation.


                                                         37
    For each period t, let

                            Pt = (P1,t , . . . , PN,t )⊤ ,        Qt = (Q1,t , . . . , QN,t )⊤ ,

and define the one-period moment vector

                        Xt := Pt , Qt , Pt Pt⊤ , Pt ⊙ Qt ∈ RN × RN × RN ×N × RN ,
                                                        


where ⊙ denotes componentwise multiplication. Let

                                                 t
                                             1X                              
                                    X̄t :=      Xs = P̄t , Q̄t , P P t , P Qt .
                                             t
                                                s=1


Thus P̄t and Q̄t are running price and quantity means, P P t is the raw price second-moment matrix,
and P Qt is the vector of own price–quantity moments.
    We keep raw second moments in this state because they update linearly as running averages. The
centered variances and covariances needed for OLS can then be recovered by subtracting products
of first moments.
    For a generic state

                           x = (xP , xQ , xP P , xP Q ) ∈ RN × RN × RN ×N × RN ,

define the local own-price variance and own price–quantity covariance terms

                             Ri (x) := xPii P − (xPi )2 ,         Si (x) := xPi Q − xPi xQ
                                                                                         i .


On states with Ri (x) > 0, the OLS slope and intercept in firm i’s own-price regression are

                                             Si (x)
                                 β̂i (x) =          ,        α̂i (x) = xQ           P
                                                                        i − β̂i (x)xi .
                                             Ri (x)

Substituting these coefficients into the myopic one-dimensional pricing problem gives a deterministic
price as a function of the empirical moments. This is the key Markovian reduction: the full past
history enters future prices only through X̄t .
    The induced OLS pricing map is
                                   "                     #
                                      xP xP Q − xP P xQ
                                    i Pi Q       ii
                                                       i                 , if Si (x) < 0,
                                   
                                   
                                      2  x    − x P xQ
                         πi (x) :=         i      i i       [Pmin ,Pmax ]
                                   
                                                                            if Si (x) ≥ 0.
                                   
                                    Pmax ,
                                   


Let π(x) := (π1 (x), . . . , πN (x))⊤ .

Lemma E.1 (OLS price from empirical moments). For every exploitation period t ≥ K, Pt+1 =


                                                             38
π(X̄t ). Moreover, on the finite-horizon neighborhoods used in the ODE-tracking argument below, the
map π is continuous and Lipschitz.

   After this lemma, proving terminal convergence is reduced to proving convergence of the empir-
ical moment vector X̄t and then applying the continuous price map π.

E.2    Stochastic approximation recursion
We next compute the conditional drift of the moment state during exploitation. Conditional on
the current history, the next posted price is already fixed by Lemma E.1; only the demand shocks
remain random.
   For a posted-price vector p ∈ RN , define expected demand by

                                           c X
                   di (p) := a − bpi +         pj ,          d(p) := (d1 (p), . . . , dN (p))⊤ .
                                         N −1
                                                j̸=i


Given the empirical moment state x, the conditional mean of the next observation is

                          f (x) := π(x), d(π(x)), π(x)π(x)⊤ , π(x) ⊙ d(π(x)) .
                                                                            


Define the drift
                                              h(x) := f (x) − x.                                   (11)

Thus f (x) is the population one-period moment vector induced by the price chosen from state x,
and h(x) is the gap between this new target observation and the current running average.

Lemma E.2 (Conditional mean update). For every exploitation period t ≥ K,

                                            E[Xt+1 | Ft ] = f (X̄t ).

   The running-average identity then gives the stochastic approximation recursion.
   The factor 1/(t + 1) below is the usual running-average step size. It is this slowly vanishing step
size that produces the multiplicative, or fluid, time scale used in the limiting ODE.

Lemma E.3 (SA recursion and start condition). Let

                                           ξt+1 := Xt+1 − f (X̄t ).

Then, for all t ≥ K,

                                          1                
                       X̄t+1 = X̄t +         h(X̄t ) + ξt+1 ,           E[ξt+1 | Ft ] = 0.
                                         t+1

Moreover, there is a constant σξ < ∞ such that

                                            E ∥ξt+1 ∥22 | Ft ≤ σξ2 .
                                                           


                                                       39
Under exploration, letting µX := E[X1 ] and ΣX := Var(X1 ),

                                                                 tr(ΣX )
                                                 E ∥X̄K − µX ∥22 =
                                                  
                           E[X̄K ] = µX ,                                 .
                                                                     K

   This lemma gives the two ingredients needed for the fluid limit: the noise is a controlled mar-
tingale difference, and the exploration phase initializes the recursion near the deterministic point
µX .
   The exploration mean µX has the following explicit coordinates. Define

                                 1 X                                     1 X
                     µ̄−i :=         µj ,              Σ̄exp,i,−i :=         (Σexp )ij .
                               N −1                                    N −1
                                       j̸=i                                  j̸=i


Writing
                                        µX = µP , µQ , µP P , µP Q ,
                                                                  


we have
                                 µPi = µi ,           µQ
                                                       i = a − bµi + cµ̄−i ,

                   µP P = µµ⊤ + Σexp ,          µPi Q = µi µQ
                                                            i − b(Σexp )ii + cΣ̄exp,i,−i .

These formulas make explicit how the exploration distribution enters the limiting initial condition.
In particular, the covariance matrix Σexp affects the initial price–quantity moments and therefore
the initial OLS slopes.

E.3     Mean-field ODE and ODE tracking
Dropping the martingale term from the stochastic approximation recursion gives the deterministic
mean-field dynamics. The time variable is normalized so that τ = 1 corresponds to the end of
exploration.
   The deterministic ODE associated with the recursion in Lemma E.3 is

                                      1
                          Ṁ (τ ) =     h(M (τ )),        M (1) = µX ,         τ ≥ 1.          (12)
                                      τ

Write
                           M (τ ) = M P (τ ), M Q (τ ), M P P (τ ), M P Q (τ ) ,
                                                                              


where M P P (τ ) is an N × N matrix. If

                               P (τ ) := π(M (τ )),          q(τ ) := d(P (τ )),

then (12) has the coordinate form

                                                      Pi (τ ) − MiP (τ )
                                        ṀiP (τ ) =                      ,
                                                               τ


                                                        40
                                                        qi (τ ) − MiQ (τ )
                                          ṀiQ (τ ) =                      ,
                                                                 τ
                                          Pi (τ )Pj (τ ) − MijP P (τ )
                         ṀijP P (τ ) =                                ,        i, j ∈ [N ],
                                                        τ
                                                    Pi (τ )qi (τ ) − MiP Q (τ )
                                  ṀiP Q (τ ) =                                 .
                                                                  τ
Each coordinate has the same running-average interpretation: the current mean-field moment is
pulled toward the population moment generated by the current deterministic price P (τ ).
   The next lemma is the fluid-limit step.

Lemma E.4 (Mean-field ODE convergence). Let M (·) solve (12). Let {Km }m≥1 satisfy Km → ∞,
and let {nm }m≥1 satisfy nm ≥ Km and nm /Km → τ ∈ [1, ∞). Then

                                                         P
                                                 X̄nm −
                                                      → M (τ ).

   The proof of Lemma E.4 uses a localized Lipschitz argument. Although the OLS pricing rule
contains ratios of empirical moments and is not globally Lipschitz, the mean-field path stays in a
region where expected demand is bounded away from zero and own-price variance is bounded below.
This gives a fixed tube around the path on which the drift is regular.
   Thus the possible singularities in the OLS ratios are avoided on every fixed fluid-time window,
and the martingale error in Lemma E.3 vanishes in the limit.

E.4    Identification with the price-moments ODE
The convergence lemma is stated in the raw moment coordinates M . The ODE in Definition 3.1,
however, is written only in terms of running price means and centered price co-movements, so we
now translate between the two descriptions.
   It remains to rewrite the mean-field ODE in centered price-moment coordinates. Define

                     U (τ ) := M P (τ ),         V (τ ) := τ M P P (τ ) − U (τ )U (τ )⊤ .
                                                                                       


Thus U (τ ) is the running price mean and V (τ ) is the scaled centered price second-moment matrix.
   The scaling by τ records accumulated price variation rather than the centered second moment
itself. This normalization is what gives V the simple evolution V̇ = (P − U )(P − U )⊤ .

Lemma E.5 (Mean-field ODE in price-moments coordinates). Let M (·) solve (12), and define
(U, V ) as above. Then (U, V ) solves

                                                             P −U
            U (1) = µ,      V (1) = Σexp ,           U̇ =         ,            V̇ = (P − U )(P − U )⊤ ,
                                                               τ




                                                         41
where P (τ ) = π(M (τ )) is given componentwise as follows. For each i ∈ [N ], let

                                     1 X                                           1 X
                         Ū−i :=         Uj ,                        V̄i,−i :=         Vij .
                                   N −1                                          N −1
                                              j̸=i                                      j̸=i


Then                               
                                   [Pe ]
                                       i [P   min ,Pmax ]
                                                            ,    if − bVii + cV̄i,−i < 0,
                           Pi =
                                   P ,                          otherwise,
                                     max

with
                                           (a + cŪ−i )Vii − cUi V̄i,−i
                                     Pei =                              .
                                               2(bVii − cV̄i,−i )
   Equivalently, the mean-field coordinates are recovered from (U, V ) by

                       MiP (τ ) = Ui (τ ),           MiQ (τ ) = a − bUi (τ ) + cŪ−i (τ ),

                                                                1
                                    M P P (τ ) = U (τ )U (τ )⊤ + V (τ ),
                                                                τ
and
                                                                     1
                        MiP Q (τ ) = Ui (τ )MiQ (τ ) +
                                                                                                
                                                                       −bVii (τ ) + cV̄i,−i (τ ) .
                                                                     τ
   The recovery formulas show that no information relevant for the posted-price coordinate is lost:
once (U, V ) is known, the quantity moments appearing in the raw OLS state are pinned down by
the linear demand model. These dynamics and the posted-price coordinate P (τ ) coincide with the
price-moments ODE in Definition 3.1.
   This completes the deterministic identification step: the stochastic approximation is tracked in
the full moment state, but its limiting posted prices can be read from the price-moments coordinates
of Definition 3.1.

E.5    Terminal convergence
Proof of Theorem 3.1 We now combine the preceding pieces. The empirical moment state converges
to the mean-field state, the terminal price is a continuous function of that state, and the resulting
deterministic price is the posted-price coordinate of the price-moments ODE.
   Let {(Km , Tm )}m≥1 satisfy

                                                                      Km + Tm
                       Km → ∞,           Tm → ∞,                              → τ ∈ [1, ∞).
                                                                        Km

Set nm := Km + Tm − 1. Since

                                      nm   Km + Tm    1
                                         =         −    → τ,
                                      Km     Km      Km




                                                                42
Lemma E.4 gives
                                                         P
                                                  X̄nm −
                                                       → M (τ ).

This is convergence of the full empirical state through the last period whose data are used to
compute the terminal exploitation price.
    The terminal exploitation price is computed from the empirical moments through period Km +
Tm − 1. Therefore, by Lemma E.1,

                                                PKm +Tm = π(X̄nm ).

Because π is continuous in a neighborhood of the limiting path, the continuous mapping theorem
implies
                                                                 P
                                        PKm +Tm = π(X̄nm ) −
                                                           → π(M (τ )).

The remaining task is only notational: the limit π(M (τ )) is still expressed in the raw moment
coordinates, while the theorem states the limit in the price-moments notation.
    By Lemma E.5, the vector π(M (τ )) is exactly P (τ ), the posted-price coordinate of the price-
moments ODE initialized at
                                           (U (1), V (1)) = (µ, Σexp ).

In the notation of Definition 3.1, this gives

                                         π(M (τ )) = P ODE (τ ; µ, Σexp ).

Therefore
                                                              → P ODE (τ ; µ, Σexp ),
                                                                 P
                             (P1,Km +Tm , . . . , PN,Km +Tm ) −

as claimed.
    This proves the desired terminal convergence and completes the reduction from the finite-sample
explore–then–exploit process to the deterministic price-moments ODE.


F      Omitted Lemmas in Proof of Theorem 3.1 (Section 3.1)
F.1      Proof of Lemma E.1
Proof. For each firm i, the OLS regression uses only the four own-firm empirical moments

                   t                       t                              t                      t
                 1X                     1X                             1X 2                   1X
      P̄i,t :=      Pi,s ,   Q̄i,t :=      Qi,s ,         P 2 i,t :=     Pi,s ,   P Qi,t :=      Pi,s Qi,s .
                 t                      t                              t                      t
                  s=1                     s=1                            s=1                   s=1

In the full moment state
                                           X̄t = (P̄t , Q̄t , P P t , P Qt ),




                                                          43
these are the local coordinates

                         loc
                                                                                                   
                       X̄i,t := P̄i,t , Q̄i,t , P P ii,t , P Qi,t = P̄i,t , Q̄i,t , P 2 i,t , P Qi,t .

   Define the clipping operator

                                 [x][Pmin ,Pmax ] := min{max{x, Pmin }, Pmax }.

We first show that, for every exploitation period t ≥ K,

                                                                 loc
                                                  Pi,t+1 = fP (X̄i,t ),

where                      "                             #
                              P̄     P Q    − P 2 Q̄
                                 i,t    i,t      i,t  i,t
                                                                          , if P Qi,t − P̄i,t Q̄i,t < 0,
                           
                           
                                                     
                   loc
             fP (X̄i,t ) =     2 P Qi,t − P̄i,t Q̄i,t
                                                            [Pmin ,Pmax ]
                           
                                                                            otherwise.
                           
                            Pmax ,
                           

Equivalently, in the notation of Appendix E,

                                                      loc
                                    πi (X̄t ) = fP (X̄i,t ),         Pt+1 = π(X̄t ).

   Fix a firm i ∈ [N ] and a time t ≥ K. Define
                                                                                         2
                            Si,t := P Qi,t − P̄i,t Q̄i,t ,        Ri,t := P 2 i,t − P̄i,t .

By nondegenerate exploration, Ri,t > 0 a.s. for all t ≥ K, so the OLS slope is well-defined. Since
Qi,s > 0 a.s. for all s ≤ t, we also have Q̄i,t > 0 a.s.
   The OLS normal equations, with an intercept, for regressing Qi,s on (1, Pi,s ) over s ≤ t are

                          α̂i,t + β̂i,t P̄i,t = Q̄i,t ,      α̂i,t P̄i,t + β̂i,t P 2 i,t = P Qi,t .

Subtracting P̄i,t times the first equation from the second gives β̂i,t Ri,t = Si,t , i.e.

                                               Si,t
                                     β̂i,t =        ,      α̂i,t = Q̄i,t − β̂i,t P̄i,t .
                                               Ri,t

   Let π̂i,t (p) := p(α̂i,t + β̂i,t p) for p ∈ [Pmin , Pmax ]. By the exploitation rule,

                                         Pi,t+1 = arg          max          π̂i,t (p).
                                                          p∈[Pmin ,Pmax ]


Case 1: Si,t < 0 (equivalently β̂i,t < 0). Then π̂i,t is strictly concave, so its unique unconstrained
maximizer is p⋆ = −α̂i,t /(2β̂i,t ), and the constrained maximizer is Pi,t+1 = [p⋆ ][Pmin ,Pmax ] . Using



                                                             44
α̂i,t = Q̄i,t − β̂i,t P̄i,t and β̂i,t Ri,t = Si,t ,

                               Q̄i,t − β̂i,t P̄i,t       P̄i,t Si,t − Q̄i,t Ri,t   P̄i,t P Qi,t − P 2 i,t Q̄i,t
                      p⋆ = −                         =                           =                           .
                                     2β̂i,t                       2Si,t             2 P Qi,t − P̄i,t Q̄i,t

This is the first branch of the claimed formula.

Case 2: Si,t ≥ 0 (equivalently β̂i,t ≥ 0). Then π̂i,t is convex, or linear, on [Pmin , Pmax ], so
maximizers lie at the endpoints. Moreover,
                                                                                        
             π̂i,t (Pmax ) − π̂i,t (Pmin ) = (Pmax − Pmin ) α̂i,t + β̂i,t (Pmax + Pmin )
                                                                                               
                                           = (Pmax − Pmin ) Q̄i,t + β̂i,t (Pmax + Pmin − P̄i,t ) > 0,

since Pmax > Pmin , Q̄i,t > 0, β̂i,t ≥ 0, and P̄i,t ≤ Pmax implies Pmax + Pmin − P̄i,t ≥ Pmin > 0. Hence
the unique maximizer is Pmax , giving the second branch.
      Combining the two cases proves the stated deterministic mapping from the local empirical
moments to Pi,t+1 , and hence proves Pt+1 = π(X̄t ).
      The continuity and Lipschitz statement used in the finite-horizon ODE-tracking argument follows
from Lemmas F.3 and F.4 below. Those lemmas show that, on the fixed tube around the mean-field
trajectory, each local block
                                                         (xPi , xQ    PP    PQ
                                                                 i , xii , xi )

lies in a domain where the OLS denominator is bounded away from zero and the pricing map is
Lipschitz. Therefore π is continuous and Lipschitz on the finite-horizon neighborhoods used in
Lemma E.4.

F.2      Proof of Lemma E.2
Proof. Recall that
                                                                                               t
                                                                                             1X
                                 Xt = (Pt , Qt , Pt Pt⊤ , Pt ⊙ Qt ),              X̄t =         Xs .
                                                                                             t
                                                                                              s=1

Let
                                                                                         
                                              Ft := σ (Pj,s , Qj,s )j∈[N ], 1≤s≤t

be the history filtration.
      Fix t ≥ K. By Lemma E.1,
                                                           Pt+1 = π(X̄t ),

so Pt+1 is Ft -measurable. Write p := π(X̄t ). Then, by the demand model and E[εi,t+1 | Ft ] = 0,

                                                                          c X
                                  E[Qi,t+1 | Ft ] = a − bpi +                 pj = di (p).
                                                                        N −1
                                                                                  j̸=i




                                                                   45
Since Pt+1 is Ft -measurable, we also have

                                                                  ⊤
                                E[Pt+1 | Ft ] = p,        E[Pt+1 Pt+1 | Ft ] = pp⊤ ,

and, for each i,
                              E[Pi,t+1 Qi,t+1 | Ft ] = pi E[Qi,t+1 | Ft ] = pi di (p).

Therefore

            E[Xt+1 | Ft ] = π(X̄t ), d(π(X̄t )), π(X̄t )π(X̄t )⊤ , π(X̄t ) ⊙ d(π(X̄t )) = f (X̄t ),
                                                                                       


which proves the claim.

F.3    Proof of Lemma E.3 (SA recursion and start condition)
Proof. Recall
                                                                                    t
                                                                              1X
                             Xt := (Pt , Qt , Pt Pt⊤ , Pt ⊙ Qt ),      X̄t :=    Xs .
                                                                              t
                                                                                   s=1

Let
                                                                              
                                        Ft := σ (Pj,s , Qj,s )j∈[N ], 1≤s≤t

be the history filtration.

Step 1: Running-mean identity and SA decomposition. For every t ≥ 1,

                           t+1
                        1 X          t         1                1            
               X̄t+1 =         Xs =     X̄t +     Xt+1 = X̄t +     Xt+1 − X̄t .
                       t+1          t+1       t+1              t+1
                                 s=1

For t ≥ K, define
                              ξt+1 := Xt+1 − f (X̄t ),         h(X̄t ) := f (X̄t ) − X̄t .

Then
                                                 1                
                               X̄t+1 = X̄t +        h(X̄t ) + ξt+1 ,              t ≥ K.
                                                t+1
By Lemma E.2,
                                   E[ξt+1 | Ft ] = E[Xt+1 | Ft ] − f (X̄t ) = 0.

Step 2: Componentwise form of the noise. Fix t ≥ K. By Lemma E.1,

                                                  Pt+1 = π(X̄t ),




                                                          46
hence Pt+1 is Ft -measurable and satisfies Pmin ≤ Pi,t+1 ≤ Pmax for every i. By the demand model
and E[εi,t+1 | Ft ] = 0,

                                                                        c X
                             E[Qi,t+1 | Ft ] = a − bPi,t+1 +                Pj,t+1 .
                                                                      N −1
                                                                                  j̸=i


Moreover, since Pt+1 is Ft -measurable,

                                                  ⊤                  ⊤
                                          E[Pt+1 Pt+1 | Ft ] = Pt+1 Pt+1 ,

and
                                  E[Pi,t+1 Qi,t+1 | Ft ] = Pi,t+1 E[Qi,t+1 | Ft ].

Thus the noise coordinates satisfy

                                           P                    PP
                                          ξt+1 = 0,            ξt+1 = 0N ×N ,

and, for each i,

                     Qi                                                          P Qi
                    ξt+1 = Qi,t+1 − E[Qi,t+1 | Ft ] = εi,t+1 ,                  ξt+1  = Pi,t+1 εi,t+1 .

Step 3: Uniform conditional second-moment bound. Using the preceding identities,

                                 N 
                                 X                                                           N
                                                                                              X
                                                                                      2
                   ∥ξt+1 ∥22 =                 2
                                       (εi,t+1 ) + (Pi,t+1 εi,t+1 )   2
                                                                              ≤ (1 + Pmax )         ε2i,t+1 .
                                 i=1                                                          i=1


Taking conditional expectation and using E[ε2i,t+1 | Ft ] ≤ σenv
                                                             2   yields

                                                         N
                                                         X
                   E[∥ξt+1 ∥22 | Ft ] ≤ (1 + Pmax
                                              2
                                                  )            E[ε2i,t+1 | Ft ] ≤ N (1 + Pmax
                                                                                          2     2
                                                                                              )σenv .
                                                         i=1

Thus we may take
                                             σξ2 := N (1 + Pmax
                                                            2     2
                                                                )σenv .

Step 4: Exploration start condition. Under the exploration law, (X1 , . . . , XK ) are i.i.d. with
mean µX := E[X1 ] and covariance ΣX := Var(X1 ). Hence

                                                       K
                                                    h1 X   i
                                         E[X̄K ] = E     Xs = µX ,
                                                     K
                                                               s=1

and
                                               K
                                            1 X                K
                                                             1 X           1
                       Var(X̄K ) = Var                   Xs = 2   Var(Xs ) = ΣX .
                                              K              K              K
                                                   s=1                 s=1




                                                           47
Finally,
                                                                   tr(ΣX )
                                    E ∥X̄K − µX ∥22 = tr Var(X̄K ) =
                                                  
                                                                            .
                                                                       K



F.4     Proof of Lemma E.4 (Mean-field ODE convergence)
Proof. Fix τ̄ ∈ [1, ∞) and a sequence {Km }m≥1 with Km → ∞ and {nm }m≥1 satisfying nm ≥ Km
and nm /Km → τ̄ . Fix τ+ > τ̄ . For all sufficiently large m, nm /Km ≤ τ+ ; throughout we work on
the finite window [1, τ+ ].
    Let M : [1, ∞) → RN × RN × RN ×N × RN solve the mean ODE

                                                      1
                                          Ṁ (τ ) =     h(M (τ )),       M (1) = µX .                                  (13)
                                                      τ

We will show X̄nm −
                  → M (τ̄ ) by comparing the SA recursion to an Euler scheme and then to M ,
                           P

using a fixed Lipschitz tube around the ODE trajectory on [1, τ+ ].

Lemma F.1 (Mean-field bounds on M (τ ) on [1, τ+ ]). Define

                        Qmin := a − bPmax + cPmin > 0,                 Qmax := a − bPmin + cPmax .

Then for all τ ∈ [1, τ+ ] and all i, j ∈ [N ],

                                Pmin ≤ MiP (τ ) ≤ Pmax ,             Qmin ≤ MiQ (τ ) ≤ Qmax ,

                         2
                        Pmin ≤ MijP P (τ ) ≤ Pmax
                                              2
                                                  ,          Pmin Qmin ≤ MiP Q (τ ) ≤ Pmax Qmax .

    Proof of Lemma F.1 For any state x, the induced next-period price vector is π(x) ∈ [Pmin , Pmax ]N ,
and the induced expected-demand vector is d(π(x)) ∈ RN . Since πi (x) ∈ [Pmin , Pmax ] for all i, we
have di (π(x)) ∈ [Qmin , Qmax ] for all i.
    Writing the mean ODE (13) coordinatewise, for each i, j ∈ [N ],

                               1                                               1
                 ṀiP (τ ) =     πi (M (τ )) − MiP (τ ) ,        ṀiQ (τ ) =     di (π(M (τ ))) − MiQ (τ ) ,
                                                                                                         
                               τ                                               τ
                 1                                                                 1
ṀijP P (τ ) =     πi (M (τ ))πj (M (τ ))−MijP P (τ ) ,          ṀiP Q (τ ) =       πi (M (τ )) di (π(M (τ )))−MiP Q (τ ) .
                                                                                                                         
                 τ                                                                 τ
Multiplying by τ and integrating from 1 to τ gives the identities
                                Z τ                                                       Z τ                 
               1                                                            1
    MiP (τ ) =           P
                        Mi (1) +     πi (M (s)) ds ,             MiQ (τ ) =          Q
                                                                                    Mi (1) +     di (π(M (s))) ds ,
                   τ                  1                                        τ                 1
                                                           Z τ                        
                                             1
                               MijP P (τ ) =       PP
                                                  Mij (1) +     πi (M (s))πj (M (s)) ds ,
                                             τ                   1




                                                               48
                                                          Z τ                           
                                          1
                           MiP Q (τ ) =        MiP Q (1) +     πi (M (s))di (π(M (s))) ds .
                                          τ                 1

Now use the bounds πi (M (s)) ∈ [Pmin , Pmax ] and di (π(M (s))) ∈ [Qmin , Qmax ] for all s, so that

                                2      2
       πi (M (s))πj (M (s)) ∈ [Pmin , Pmax ],            πi (M (s))di (π(M (s))) ∈ [Pmin Qmin , Pmax Qmax ].

The initial condition M (1) = µX satisfies the same bounds, because it is the corresponding explo-
ration moment vector. Each display above therefore implies that the corresponding coordinate of
M (τ ) remains within the stated interval for all τ ≥ 1, and in particular for all τ ∈ [1, τ+ ].

Lemma F.2 (Own-price variance floor along the mean ODE). For each i, define
                                                                            2
                                          RiM (τ ) := MiiP P (τ ) − MiP (τ ) .

Then τ RiM (τ ) is nondecreasing and

                                                RiM (1)   (Σexp )ii
                                 RiM (τ ) ≥             =                   for all τ ≥ 1.
                                                   τ         τ

In particular, for all τ ∈ [1, τ+ ], RiM (τ ) ≥ (Σexp )ii /τ+ .

    Proof of Lemma F.2          From the ODE coordinates,

                           1                                                     1
             ṀiP (τ ) =     πi (M (τ )) − MiP (τ ) ,           ṀiiP P (τ ) =     πi (M (τ ))2 − MiiP P (τ ) .
                                                                                                            
                           τ                                                     τ

Differentiate RiM (τ ) = MiiP P (τ ) − (MiP (τ ))2 :

                       ṘiM (τ ) = ṀiiP P (τ ) − 2MiP (τ )ṀiP (τ )
                                   1                                                    
                                 =      πi (M (τ ))2 − MiiP P − 2MiP (πi (M (τ )) − MiP )
                                   τ
                                   1                     P 2        PP       P 2
                                                                                   
                                 =      (πi (M (τ )) − Mi ) − (Mii − (Mi ) )
                                   τ
                                   1                                   
                                 =      (πi (M (τ )) − MiP )2 − RiM (τ ) .
                                   τ

Therefore
                     d
                       τ RiM (τ ) = τ ṘiM (τ ) + RiM (τ ) = (πi (M (τ )) − MiP (τ ))2 ≥ 0,
                                 
                    dτ
so τ RiM (τ ) is nondecreasing and τ RiM (τ ) ≥ RiM (1). Finally,

                           RiM (1) = MiiP P (1) − (MiP (1))2 = Varexp (Pi,1 ) = (Σexp )ii .




Lemma F.3 (Lipschitz pricing map under (Q, Var(P )) floors). Fix constants ηQ > 0 and ηV > 0,


                                                            49
and define the block-domain
                 
S(ηQ , ηV ) :=       x = (xP , xQ , xP P , xP Q ) ∈ R4 : 0 ≤ xP ≤ Pmax + 1, ηQ ≤ xQ ≤ Qmax + 1,

                                                        0 ≤ xP P ≤ (Pmax + 1)2 , 0 ≤ xP Q ≤ (Pmax + 1)(Qmax + 1),
                                                                         
                                                         PP      P 2
                                                        x − (x ) ≥ ηV .


Then fP : S(ηQ , ηV ) → [Pmin , Pmax ] is globally Lipschitz: there exists LP = LP (Pmin , Pmax , Qmax , ηQ , ηV ) <
∞ such that for all x, y ∈ S(ηQ , ηV ),

                                         |fP (x) − fP (y)| ≤ LP ∥x − y∥2 .

   Proof of Lemma F.3           Fix x ∈ S(ηQ , ηV ) and define

                           v(x) := xP P − (xP )2 (≥ ηV ),         s(x) := xP Q − xP xQ ,

                                              s(x)
                                    β(x) :=        ,      α(x) := xQ − β(x)xP .
                                              v(x)
Set the shorthand P+ := Pmax + 1 and Q+ := Qmax + 1.

Step 1: explicit bounds and Lipschitz constants for (α, β). On S(ηQ , ηV ) we have 0 ≤ xP ≤
P+ , ηQ ≤ xQ ≤ Q+ , and 0 ≤ xP Q ≤ P+ Q+ , hence

                                    |s(x)| ≤ |xP Q | + |xP xQ | ≤ 2P+ Q+ =: Bs .

Moreover, ∇v = (−2xP , 0, 1, 0) and ∇s = (−xQ , −xP , 0, 1), so
                                   q                                  q
                       ∥∇v∥2 ≤      4P+2 + 1 =: Lv ,       ∥∇s∥2 ≤        Q2+ + P+2 + 1 =: Ls .

By the mean value theorem, for all x, y ∈ S(ηQ , ηV ),

                         |v(x) − v(y)| ≤ Lv ∥x − y∥2 ,         |s(x) − s(y)| ≤ Ls ∥x − y∥2 .

Using v(·) ≥ ηV and |s(·)| ≤ Bs , we obtain
                                              
                                   Ls  Bs Lv                                                   Bs
           |β(x) − β(y)| ≤            + 2          ∥x − y∥2 =: Lβ ∥x − y∥2 ,       |β(x)| ≤       =: Bβ .
                                   ηV   ηV                                                     ηV

Finally,
                               |α(x)| ≤ |xQ | + |β(x)| |xP | ≤ Q+ + Bβ P+ =: Bα ,




                                                          50
and

   |α(x) − α(y)| ≤ |xQ − y Q | + |β(x)xP − β(y)y P | ≤ 1 + Bβ + P+ Lβ ∥x − y∥2 =: Lα ∥x − y∥2 .
                                                                     


Step 2: Lipschitzness of fP . Let [u][Pmin ,Pmax ] := min{max{u, Pmin }, Pmax }. With g(α, β) :=
−α/(2β), the pricing map can be written as
                                   
                                   Pmax ,                                   β(x) ≥ 0,
                           fP (x) = 
                                    g(α(x), β(x))                        , β(x) < 0.
                                                    [P       min ,Pmax ]


If β(x) < 0, then
                                      α(x) = xQ − β(x)xP ≥ xQ ≥ ηQ ,

since xP ≥ 0. Define
                                                       ηQ
                                             δ :=           > 0.
                                                      2Pmax
If β(x) ∈ [−δ, 0), then
                                                       α(x)     ηQ
                                  g(α(x), β(x)) =             ≥    = Pmax ,
                                                      2|β(x)|   2δ
hence fP (x) = Pmax whenever β(x) ≥ −δ.
   On the region {β ≤ −δ}, g is smooth and

                                         ∂g  1               ∂g  Bα
                                            ≤ ,                 ≤ 2.
                                         ∂α  2δ              ∂β  2δ

Thus, by the mean value theorem, for β(x), β(y) ≤ −δ,

                                                        1                 Bα
               |g(α(x), β(x)) − g(α(y), β(y))| ≤           |α(x) − α(y)| + 2 |β(x) − β(y)|.
                                                        2δ                2δ

Since u 7→ [u][Pmin ,Pmax ] is 1-Lipschitz, the same bound holds for |fP (x) − fP (y)|, giving
                                                 
                                      Lα Bα Lβ
            |fP (x) − fP (y)| ≤          +            ∥x − y∥2 ,       whenever β(x), β(y) ≤ −δ.
                                      2δ   2δ 2

Step 3: mixed-region pairs and conclusion. If β(x) ≥ −δ and β(y) ≤ −δ, then fP (x) = Pmax
and

                                                      Bα               Bα                 Bα Lβ
Pmax − fP (y) ≤ g(α(y), −δ) − g(α(y), β(y)) ≤              |β(y)| − δ  ≤ 2 |β(x) − β(y)| ≤       ∥x − y∥2 .
                                                      2δ 2              2δ                  2δ 2

The symmetric case is identical. Combining all cases, we may take

                                                      Lα Bα Lβ
                                           LP :=         +      ,
                                                      2δ   2δ 2



                                                        51
which proves global Lipschitzness of fP on S(ηQ , ηV ).

Lemma F.4 (Fixed Lipschitz tube for h). Let Σexp,min := mini∈[N ] (Σexp )ii and set

                                            Σexp,min                   Qmin
                                    ηV :=            ,         ηQ :=        .
                                              2τ+                       2

Let
                                         Γ := {M (τ ) : τ ∈ [1, τ+ ]}.

Then there exists R ∈ (0, 1] and constants Lh , Hh < ∞ such that on the tube

                         ΓR := x ∈ RN × RN × RN ×N × RN : dist(x, Γ) ≤ R ,
                              


the following hold:

  (i) For every x ∈ ΓR and every i, the local block

                                                         Q PP       PQ
                                            xloc    P
                                             i := (xi , xi , xii , xi )


       lies in S(ηQ , ηV ).

 (ii) h is Lh -Lipschitz and bounded by Hh on ΓR :

                      ∥h(x) − h(y)∥2 ≤ Lh ∥x − y∥2       ∀x, y ∈ ΓR ,           sup ∥h(x)∥2 ≤ Hh .
                                                                                x∈ΓR


      Proof of Lemma F.4      Step 1: margins on the path. By Lemma F.1, for all τ ∈ [1, τ+ ],

                                          MiQ (τ ) ≥ Qmin = 2ηQ .

By Lemma F.2, for all τ ∈ [1, τ+ ],

                                                               (Σexp )ii
                                 MiiP P (τ ) − (MiP (τ ))2 ≥             ≥ 2ηV .
                                                                 τ+

Also Lemma F.1 gives the remaining coordinate bounds on Γ.
      Step 2: choose R so margins persist. Define the blockwise maps

                                          Q
                               q(xloc
                                  i ) := xi ,        v(xloc     PP     P 2
                                                        i ) := xii − (xi ) .


On the bounded set 0 ≤ xPi ≤ Pmax + 1 we have
                                                               p
                     ∥∇v(xloc          P
                          i )∥2 = ∥(−2xi , 0, 1, 0)∥2 ≤         4(Pmax + 1)2 + 1 =: L(1)
                                                                                     v ,




                                                      52
         (1)
so v is Lv -Lipschitz there, while q is 1-Lipschitz. Choose
                                         (                                      )
                                                    ηV
                             R := min 1, ηQ ,        (1)
                                                           , Pmin , Pmin Qmin       .
                                                   Lv

If x ∈ ΓR , pick τ ∈ [1, τ+ ] with ∥x − M (τ )∥2 ≤ R. Then for each i,

                                          ∥xloc  loc
                                            i − Mi (τ )∥2 ≤ R,


hence
                         xQ    Q          loc  loc
                          i ≥ Mi (τ ) − ∥xi − Mi (τ )∥2 ≥ 2ηQ − R ≥ ηQ ,

and

        xPii P − (xPi )2 ≥ MiiP P (τ ) − (MiP (τ ))2 − L(1) loc  loc               (1)
                                                    
                                                        v ∥xi − Mi (τ )∥2 ≥ 2ηV − Lv R ≥ ηV .


Moreover,
                         xPi ≥ MiP (τ ) − ∥xloc  loc
                                            i − Mi (τ )∥2 ≥ Pmin − R ≥ 0,

and
                                       xPi ≤ Pmax + R ≤ Pmax + 1.

The same coordinatewise comparison gives

                   0 ≤ xPii P ≤ (Pmax + 1)2 ,       0 ≤ xPi Q ≤ (Pmax + 1)(Qmax + 1),

after shrinking by the above choice of R, because Γ satisfies the bounds in Lemma F.1 and each
coordinate is 1-Lipschitz in Euclidean distance. This proves (i).
     Step 3: Lipschitzness of h on the tube. By (i) and Lemma F.3, each local block map
 i 7→ fP (xi ) is LP -Lipschitz on ΓR . Therefore the vector price map π satisfies
xloc       loc


                             N
                             X                                    N
                                                                  X
         ∥π(x) − π(y)∥22 =         |fP (xloc        loc 2   2
                                         i ) − fP (yi )| ≤ LP           ∥xloc  loc 2   2        2
                                                                          i − yi ∥2 ≤ LP ∥x − y∥2 ,
                             i=1                                  i=1

so
                                      ∥π(x) − π(y)∥2 ≤ LP ∥x − y∥2 .

     Define the linear expected-demand map d : [Pmin , Pmax ]N → RN by

                                                              c X
                                      di (p) := a − bpi +         pj .
                                                            N −1
                                                                   j̸=i


Its matrix has diagonal entries −b and off-diagonal entries c/(N − 1), hence its induced 1- and
∞-norms are both b + c, so
                                    ∥d(p) − d(p′ )∥2 ≤ (b + c)∥p − p′ ∥2 .

                                                     53
     Now define
                                   Φ : RN → RN × RN × RN ×N × RN

by
                                    Φ(p) := p, d(p), pp⊤ , p ⊙ d(p) .
                                                                   


Using the bounds 0 ≤ pi ≤ Pmax and Qmin ≤ di (p) ≤ Qmax , one checks that for all p, p′ ∈
[Pmin , Pmax ]N ,
                                     ∥Φ(p) − Φ(p′ )∥2 ≤ LΦ ∥p − p′ ∥2 ,

where one may take
                          q                 √                               2
                     LΦ := 1 + (b + c)2 + (2 N Pmax )2 + Pmax (b + c) + Qmax .

Indeed,
                                                                         √
               ∥pp⊤ − p′ p′⊤ ∥F ≤ ∥(p − p′ )p⊤ ∥F + ∥p′ (p − p′ )⊤ ∥F ≤ 2 N Pmax ∥p − p′ ∥2 ,

and
                    ∥p ⊙ d(p) − p′ ⊙ d(p′ )∥2 ≤ Qmax ∥p − p′ ∥2 + Pmax ∥d(p) − d(p′ )∥2 .

Since f (x) = Φ(π(x)), it follows that

                         ∥f (x) − f (y)∥2 ≤ LΦ ∥π(x) − π(y)∥2 ≤ LΦ LP ∥x − y∥2 .

Finally,

∥h(x) − h(y)∥2 = ∥(f (x) − x) − (f (y) − y)∥2 ≤ ∥f (x) − f (y)∥2 + ∥x − y∥2 ≤ (LΦ LP + 1)∥x − y∥2 .

Thus (ii) holds with
                                             Lh := LΦ LP + 1.

Boundedness supx∈ΓR ∥h(x)∥2 < ∞ follows from continuity of h and compactness of ΓR , and we
denote this bound by Hh .

Step 1: log-time reparametrization and a deterministic Euler scheme. Define the log-
time variable ℓ := log τ , so τ = eℓ , and the reparametrized mean-field trajectory

                                       M ℓ (ℓ) := M (eℓ ),     ℓ ≥ 0.

Since M (·) solves Ṁ (τ ) = τ1 h(M (τ )), the chain rule gives

                            d ℓ
                               M (ℓ) = h(M ℓ (ℓ)),        M ℓ (0) = M (1) = µX .
                            dℓ




                                                     54
Thus M ℓ solves the autonomous ODE

                                     d ℓ
                                        M (ℓ) = h(M ℓ (ℓ)),           M ℓ (0) = µX .                    (14)
                                     dℓ

    Fix m and abbreviate K := Km and n := nm . For calendar times s ≥ K, define the accumulated
step size
                                                 s
                                                 X 1
                                         SK,s :=     ,               SK,K = 0.
                                                   r
                                                   r=K+1

For all s ∈ {K, . . . , n},
                                         Z s
                                            dx       s       n
                                SK,s ≤         = log     ≤ log     ≤ log τ+ ,
                                          K x         K         K

for all sufficiently large m. Hence SK,s ∈ [0, log τ+ ] and

                    M ℓ (SK,s ) ∈ Γ := {M (τ ) : τ ∈ [1, τ+ ]}            for all s ∈ {K, . . . , n}.

    Define the deterministic Euler scheme for (14) on the grid {SK,s }:

                                                                     1
                       YK,K := µX ,            YK,s+1 := YK,s +         h(YK,s ),         s ≥ K.
                                                                    s+1

Define the Euler error
                                       es := YK,s − M ℓ (SK,s ),           s ≥ K,

so eK = 0.
    We now prove the uniform bound (16). The argument uses only that on the tube ΓR from
Lemma F.4, h is Lh -Lipschitz and bounded by Hh .

Step 1a (local truncation error for the exact flow). For each s ≥ K,
                                                                  Z SK,s+1
                                 ℓ                  ℓ
                               M (SK,s+1 ) − M (SK,s ) =                     h(M ℓ (u)) du.
                                                                   SK,s


Write
                                                                           1
                                         ∆s := SK,s+1 − SK,s =                .
                                                                          s+1
Add and subtract ∆s h(M ℓ (SK,s )) to obtain

                              M ℓ (SK,s+1 ) = M ℓ (SK,s ) + ∆s h(M ℓ (SK,s )) + ρs+1 ,

where                                    Z SK,s+1                                 
                               ρs+1 :=                  h(M ℓ (u)) − h(M ℓ (SK,s )) du.
                                          SK,s




                                                             55
Since M ℓ (u) ∈ Γ ⊆ ΓR and ∥h(·)∥ ≤ Hh on ΓR , for u ∈ [SK,s , SK,s+1 ],

           ∥h(M ℓ (u)) − h(M ℓ (SK,s ))∥2 ≤ Lh ∥M ℓ (u) − M ℓ (SK,s )∥2 ≤ Lh Hh (u − SK,s ),

and therefore
                             Z SK,s+1
                                                                    Lh Hh 2 Lh Hh  1
                ∥ρs+1 ∥2 ≤              Lh Hh (u − SK,s ) du =           ∆s =            .
                              SK,s                                    2       2 (s + 1)2


Step 1b (error recursion, localized to the tube). Define the deterministic exit time from the
tube
                 sE := inf{s ∈ {K, K + 1, . . . , n} : YK,s ∈
                                                            / ΓR },             (inf ∅ := n + 1).

For s < sE we have YK,s ∈ ΓR and M ℓ (SK,s ) ∈ Γ ⊆ ΓR , so

                es+1 = YK,s+1 − M ℓ (SK,s+1 )
                                                                                
                     = YK,s + ∆s h(YK,s ) − M ℓ (SK,s ) + ∆s h(M ℓ (SK,s )) + ρs+1
                                                       
                     = es + ∆s h(YK,s ) − h(M ℓ (SK,s )) − ρs+1 .

Taking norms and using Lipschitzness of h on ΓR gives, for all s < sE ,
                                            Lh           Lh Hh  1
                             ∥es+1 ∥2 ≤ 1 +       ∥es ∥2 +              .                           (15)
                                            s+1              2 (s + 1)2

Step 1c (solve the recursion). Let as := ∥es ∥2 and c := Lh Hh /2. From (15), for all s < sE ,
                                         Lh           c
                              as+1 ≤ 1 +       as +          ,                aK = 0.
                                         s+1        (s + 1)2

Unrolling yields, for K ≤ s ≤ sE ∧ n,
                                                  s         s
                                                  X      1 Y      Lh 
                                        as ≤ c                 1 +      .
                                                         r2         j
                                                 r=K+1     j=r+1


Moreover, log(1 + Lh /j) ≤ Lh /j implies
                                                
                    s                       s
                    Y          Lh         X L h
                                                      s Lh  n Lh
                             1+      ≤ exp        ≤        ≤        ≤ τ+Lh ,
                                 j             j       r      K
                   j=r+1                          j=r+1


for all sufficiently large m. Hence, for s ≤ sE ∧ n,
                                                                n
                                                                X      1
                                            ∥es ∥2 ≤ c τ+Lh               .
                                                                       r2
                                                               r=K+1




                                                          56
Define
                                                       Lh Hh Lh
                                               CE :=        τ+ .
                                                         2
                                                                      Pn                   R∞
Step 1d (the Euler iterates stay in the tube). Since                      r=K+1 r
                                                                                    −2 ≤
                                                                                           K    x−2 dx = 1/K, we
have
                                                                   CE
                                               max      ∥es ∥2 ≤      .
                                            K≤s≤sE ∧n              K
Because Km → ∞, for all sufficiently large m we have CE /K ≤ R/2. Fix such an m. Then for all
s ≤ sE ∧ n,
                                     ∥YK,s − M ℓ (SK,s )∥2 = ∥es ∥2 ≤ R/2,

and since M ℓ (SK,s ) ∈ Γ, this implies YK,s ∈ ΓR/2 ⊆ ΓR for all s ≤ sE ∧ n. Thus sE = n + 1, i.e.,
YK,s ∈ ΓR for all s ∈ {K, . . . , n}, and

                                                                                CE
                             max ∥YK,s − M ℓ (SK,s )∥2 = max ∥es ∥2 ≤              .                        (16)
                            K≤s≤n                             K≤s≤n             K

Step 2: SA vs. Euler (martingale perturbation) via localization. Let

                                               ds := X̄s − YK,s .

Define the stopping time

                  sSA := inf{s ∈ {K, K + 1, . . . , n} : ∥ds ∥2 > R/2},         (inf ∅ := ∞),

and the stopped process
                                                 d˜s := ds∧sSA .

On {s < sSA } we have X̄s , YK,s ∈ ΓR , hence

                                       ∥h(X̄s ) − h(YK,s )∥2 ≤ Lh ∥ds ∥2 .

   Using Lemma E.3 and the Euler recursion for YK,s , for s ≥ K we have

                                             1                       1
                           ds+1 = ds +          h(X̄s ) − h(YK,s ) +     ξs+1 .
                                            s+1                      s+1

Taking conditional expectation of ∥d˜s+1 ∥22 given Fs and using E[ξs+1 | Fs ] = 0 yields

                                                 L2h
                                                      
                                         2Lh                          1
              E ∥d˜s+1 ∥22 | Fs ≤                          ˜s ∥2 +                    2
                                                                                          
                                     1+      +           ∥ d   2            E  ∥ξs+1 ∥2 | Fs   .
                                        s + 1 (s + 1)2             (s + 1)2




                                                        57
Using E[∥ξs+1 ∥22 | Fs ] ≤ σξ2 and (s + 1)−2 ≤ (s + 1)−1 , there is a constant C1 such that

                                                                    σξ2
                                                    
                                                  C1     ˜
                             E∥d˜s+1 ∥22 ≤    1+             2
                                                       E∥ds ∥2 +          .
                                                 s+1             (s + 1)2

Iterating and using
                                  n                                 n
                                  X     1                           X     1    1
                                          ≤ log τ+ ,                        2
                                                                              ≤ ,
                                        r                                 r    K
                                r=K+1                           r=K+1

gives                                                       
                                      ˜                    1
                                          2            2
                                    E∥dn ∥2 ≤ C2 E∥dK ∥2 +     ,                                 (17)
                                                           K
where C2 < ∞ depends only on C1 , σξ2 , τ+ . Since dK = X̄K − µX , Lemma E.3 gives

                                             E∥dK ∥22 = O(1/K),

hence
                                             E∥d˜n ∥22 = O(1/K).

Therefore                                                       
                                                     R                   4
                          Pr(sSA ≤ n) ≤ Pr ∥d˜n ∥2 ≥                 ≤      E∥d˜n ∥22 −→ 0.
                                                     2                   R2

On {sSA > n} we have dn = d˜n , so
                                                            P
                                                    dn −
                                                       → 0.

Step 3: conclude X̄nm → M (τ̄ ). By (16) and dn −
                                                                P
                                                → 0,

                      X̄n − M ℓ (SK,n ) = (X̄n − YK,n ) + (YK,n − M ℓ (SK,n )) −
                                                                                         P
                                                                               → 0.
                                          |    {z    } |          {z         }
                                                   dn                        en


It remains to identify the limit of M ℓ (SK,n ). Using the integral test for harmonic sums,
                                  Z n      n     Z n
                                      dx   X 1       dx  1
                                         ≤     ≤        + ,
                                    K x      r    K x
                                                 r=K+1
                                                         K

so                        n                                                   
                                   1                                     n         1
             SK,n = log         +O           ,    hence e       SK,n
                                                                       =   · exp O     −→ τ̄ .
                            K      K                                     K         K
By continuity of M (·),
                                   M ℓ (SK,n ) = M (eSK,n ) → M (τ̄ ).

Therefore
                                                        P
                                                 X̄nm −
                                                      → M (τ̄ ),

proving Lemma E.4.


                                                        58
F.5    Proof of Lemma E.5
Proof. Let M (·) be the mean-field ODE solution from Lemma E.4, and write

                              M (τ ) = M P (τ ), M Q (τ ), M P P (τ ), M P Q (τ ) .
                                                                                 


By definition of the mean-field moment coordinates, for τ ≥ 1 the price mean M P (τ ) ∈ RN and
raw price second-moment matrix M P P (τ ) ∈ RN ×N satisfy

                                        P − MP                          PP⊤ − MPP
                              Ṁ P =           ,            Ṁ P P =              ,
                                           τ                                τ

where P (τ ) = π(M (τ )). Define

            U (τ ) := M P (τ ),       ΣP (τ ) := M P P (τ ) − U (τ )U (τ )⊤ ,            V (τ ) := τ ΣP (τ ).

Deriving the (U, V ) dynamics. From U = M P we immediately have

                                                            P −U
                                                     U̇ =        .
                                                              τ

For V = τ ΣP , the product rule gives

                                                V̇ = ΣP + τ Σ̇P .

Also
                                        Σ̇P = Ṁ P P − U̇ U ⊤ − U U̇ ⊤ .

Substituting the ODEs for Ṁ P P and U̇ and using M P P = ΣP + U U ⊤ yields

                       τ Σ̇P = P P ⊤ − (ΣP + U U ⊤ ) − (P − U )U ⊤ − U (P − U )⊤
                             = (P − U )(P − U )⊤ − ΣP .

Therefore
                      V̇ = ΣP + (P − U )(P − U )⊤ − ΣP = (P − U )(P − U )⊤ .
                                                      


Expressing P (τ ) as a function of (U, V ). Fix i ∈ [N ] and write

                                        1 X                                    1 X
                            Ū−i :=         Uj ,                 V̄i,−i :=         Vij .
                                      N −1                                   N −1
                                              j̸=i                                j̸=i


The mean-field moment coordinates inherit the linear moment identities from the demand model:

                                            MiQ = a − b Ui + c Ū−i ,




                                                            59
and
                                                                                        1 X PP
                    MiP Q = a Ui − b MiiP P + c M P P i,−i ,         M P P i,−i :=         Mij .
                                                                                      N −1
                                                                                           j̸=i

Since
                                                               1
                                                M P P = U U ⊤ + V,
                                                               τ
we have
                                            1                                     1
                              MiiP P = Ui2 + Vii ,          M P P i,−i = Ui Ū−i + V̄i,−i .
                                            τ                                     τ
Substituting into MiP Q gives

                                                             1
                                     MiP Q = Ui MiQ +
                                                                                
                                                               − bVii + c V̄i,−i ,
                                                             τ

so
                                                                 −bVii + c V̄i,−i
                                       MiP Q − MiP MiQ =                          .
                                                                       τ
Also
                                                                       Vii
                                               MiiP P − (MiP )2 =          .
                                                                        τ
Hence the OLS slope estimate in moment form satisfies

                                            MiP Q − MiP MiQ   −bVii + c V̄i,−i
                                    β̂i =      P P      P 2
                                                            =                  .
                                            Mii − (Mi )             Vii

     Thus:

     • If −bVii + c V̄i,−i ≥ 0, equivalently β̂i ≥ 0, then predicted profit pi (α̂i + β̂i pi ) is nondecreasing
        at the relevant upper endpoint in the sense established in Lemma E.1, and the selected price
        is Pmax .

     • If −bVii + c V̄i,−i < 0, equivalently β̂i < 0, the unconstrained maximizer is −α̂i /(2β̂i ). Using

                                     α̂i = MiQ − β̂i Ui ,        MiQ = a − bUi + cŪ−i ,

        and the moment identities above, a direct substitution gives

                                                       (a + c Ū−i )Vii − c Ui V̄i,−i
                                         Pei (U, V ) =                               .
                                                           2 bVii − c V̄i,−i

        Enforcing feasibility gives
                                                 Pi = [Pei (U, V )][Pmin ,Pmax ] .

This is exactly the pricing map stated in Lemma E.5, so P (τ ) = π(M (τ )) is the posted-price
coordinate of the price-moments ODE.



                                                            60
Initial conditions. Because U = M P , we have

                                                U (1) = M P (1) = µ.

Also,
                V (1) = 1 · M P P (1) − U (1)U (1)⊤ = (µµ⊤ + Σexp ) − µµ⊤ = Σexp .
                                                   


Therefore (U, V ) solves

                                                               P −U
             U (1) = µ,        V (1) = Σexp ,           U̇ =        ,         V̇ = (P − U )(P − U )⊤ ,
                                                                 τ

with the stated price map.
    Finally, the recovery formulas follow from the same identities:

                          MiP (τ ) = Ui (τ ),          MiQ (τ ) = a − bUi (τ ) + cŪ−i (τ ),

                                                                  1
                                      M P P (τ ) = U (τ )U (τ )⊤ + V (τ ),
                                                                  τ
and
                                                               1                          
                           MiP Q (τ ) = Ui (τ )MiQ (τ ) +         −bVii (τ ) + cV̄i,−i (τ ) .
                                                               τ
These dynamics and the posted-price coordinate P (τ ) coincide with Definition 3.1.


G       Omitted Steps and Lemmas in Theorem 3.2 (Sections 3.2, 6)
This appendix completes the proof of Theorem 3.2 which was outlined in Section 6. Throughout,
(U (τ ), V (τ )) denotes the solution to the price-moments ODE from Definition 3.1, P (τ ) denotes the
corresponding posted-price vector, and

                                            e(τ ) := P (τ ) − U (τ ).

We also write
                                        1 X                                   1 X
                            Ū−i :=         Uj ,                V̄i,−i :=         Vij .
                                      N −1                                  N −1
                                                j̸=i                              j̸=i

The proof below strings together the main-text lemmas and states the remaining auxiliary lemmas
at the points where they are used. The proofs of all lemmas follow in the subsequent subsections:
first the lemmas stated in the main text, then the auxiliary lemmas stated in this appendix.
    Proof.   We first consider the lower cone, µ ∈ C − . At τ = 1, V (1) = Σexp is diagonal, so
V̄i,−i (1) = 0. By Lemma 6.1, the initial OLS price is the correct best response:

                                                 Pi (1) = BR(µ̄−i ).




                                                           61
The cap is inactive because µi < BR(µ̄−i ) implies BR(µ̄−i ) > Pmin , while

                                       BR(µ̄−i ) ≤ BR(Pmax ) < Pmax

under the standing price-bound assumptions. Since µ ∈ C − , we therefore have

                        ei (1) = Pi (1) − Ui (1) = BR(µ̄−i ) − µi > 0          for all i.

Lemma 6.2 then implies
                                         e(τ ) ⪰ 0        for all τ ≥ 1.

Thus U is componentwise nondecreasing, since U̇ = e/τ ⪰ 0.
   The same-sign gap generates the cross-firm covariance needed for the correlation-bias argument.
Because the covariance state evolves as V̇ = ee⊤ , common-sign price movements imply nonnegative
off-diagonal covariances; strict common-sign movement at the start makes these cross-covariances
strictly positive immediately afterward.

Lemma G.1 (Common-sign gaps generate positive cross-covariances). Assume Vij (1) = 0 for all
i ̸= j. If e(τ ) ⪰ 0 for all τ ≥ 1 or e(τ ) ⪯ 0 for all τ ≥ 1, then Vij (τ ) ≥ 0 for all i ̸= j and all τ ≥ 1.
If, moreover, e(τ0 ) ≻ 0 or e(τ0 ) ≺ 0 for some τ0 ≥ 1, then

                             V̄i,−i (τ ) > 0       for all i ∈ [N ] and all τ > τ0 .

   Applying Lemma G.1 with τ0 = 1 gives

                                 V̄i,−i (τ ) ≥ 0       for all i and all τ ≥ 1,

with strict positivity for every τ > 1. The hypotheses of Lemma 6.3 are therefore satisfied: U is
componentwise monotone and the average cross-covariances are nonnegative. Hence the limit

                                               U ∞ := lim U (τ )
                                                        τ →∞

exists and satisfies the Nash lower bound

                                                   U ∞ ⪰ pNE 1.

   It remains to show that the inequality is strict. The first reduction shows that, once the Nash
lower bound is known, any equality in a single coordinate forces the entire limiting vector to be
exactly Nash.

Lemma G.2 (Reduction to the Nash boundary). Suppose U ∞ := limτ →∞ U (τ ) exists, V̄i,−i (τ ) ≥ 0
for all i and all τ ≥ 1, and
                                                   U ∞ ⪰ pNE 1.


                                                        62
If Uj∞ = pNE for some j, then U ∞ = pNE 1.
   Suppose, toward a contradiction, that U ∞ is not componentwise strictly above Nash. Then
some coordinate satisfies Uj∞ = pNE , and Lemma G.2 implies

                                              U ∞ = pNE 1.

We now rule out this boundary case.
   The boundary argument uses one additional monotonicity property. The forward-invariance
lemma gives P − U ⪰ 0; the next two lemmas show that, on the lower cone, the posted prices
themselves are componentwise nondecreasing. First, once Ṗ ⪰ 0, this sign is forward invariant.
Lemma G.3 (Forward invariance of price monotonicity on C − ). Assume P (τ ) − U (τ ) ⪰ 0 for all
τ ≥ τ0 . If Ṗ (τ0 ) ⪰ 0 at some τ0 ≥ 1, then P is componentwise nondecreasing on [τ0 , ∞).
   The hypothesis of Lemma G.3 is initialized at the start of exploitation.
Lemma G.4 (Initialization of price monotonicity on C − ). Suppose µ ∈ C − and U (1) = µ, V (1) =
Σexp , where Σexp is positive diagonal. Then P is right-differentiable at τ = 1 and

                                               Ṗ (1+ ) ≻ 0.

   By Lemmas G.4 and G.3, P is componentwise nondecreasing. If U (τ ) → pNE 1, this monotonicity
forces P (τ ) to converge to the same Nash vector and eventually lie below it. The next lemma then
shows that the covariance matrix stabilizes, while the accumulated cross-covariances remain strictly
positive.
Lemma G.5 (Covariance convergence on the Nash boundary). Suppose that U (τ ) → pNE 1, P (τ )−
U (τ ) ⪰ 0 for all τ ≥ 1, P is componentwise nondecreasing, and V̄i,−i (τ ) ≥ 0 for all i and all τ ≥ 1.
Assume also that e(τ0 ) ≻ 0 for some τ0 ≥ 1. Then:
(1) P (τ ) → pNE 1 and P (τ ) ⪯ pNE 1 for all sufficiently large τ ;

(2) each Vii (τ ) converges to a finite limit Vii∞ , and each average cross term

                                                          1 X
                                        V̄i,−i (τ ) =         Vij (τ )
                                                        N −1
                                                               j̸=i

                                              ∞ > 0.
    converges to a strictly positive limit V̄i,−i
   Applying Lemma G.5 with τ0 = 1 gives

                     P (τ ) → pNE 1,      Vii (τ ) → Vii∞ ,                        ∞
                                                                  V̄i,−i (τ ) → V̄i,−i > 0.

But this is incompatible with the OLS price map. A strictly positive limiting cross-covariance
creates a persistent upward omitted-variable bias at the Nash vector, so the posted price cannot
converge to Nash.

                                                        63
Lemma G.6 (Limiting bias excludes the Nash boundary). Suppose µ ∈ C − . There is no lower-cone
trajectory such that

    U (τ ) → pNE 1,       P (τ ) → pNE 1,       Vii (τ ) → Vii∞ ,                     ∞
                                                                     V̄i,−i (τ ) → V̄i,−i >0   for every i.

    This contradicts Lemma G.6. Therefore the limiting running mean must satisfy

                                                U ∞ ≻ pNE 1.

Since e(τ ) = P (τ ) − U (τ ) ⪰ 0 on C − , there exists τ0 < ∞ such that, for all τ > τ0 ,

                                P ODE (τ ; µ, Σexp ) = P (τ ) ⪰ U (τ ) ≻ pNE 1.

This proves Theorem 3.2(b).
    It remains to handle the upper cone, µ ∈ C + . The proof is the same in spirit, but the invariant
orthant is reversed. At τ = 1, V (1) is diagonal, so Pi (1) = BR(µ̄−i ). Since µ ∈ C + , we have

                             Pi (1) − Ui (1) = BR(µ̄−i ) − µi < 0       for all i.

Thus prices initially move downward relative to trailing means. The required sign-reversed forward-
invariance statement is the following.

Lemma G.7 (Negative-orthant forward invariance). Fix τ0 ≥ 1. If P (τ0 ) − U (τ0 ) ⪯ 0, then
P (τ ) − U (τ ) ⪯ 0 for all τ ≥ τ0 .

    By Lemma G.7, e(τ ) ⪯ 0 for all τ ≥ 1 on C + . Since covariance accumulation depends on
products ei ej , not on the sign of ei alone, Lemma G.1 again gives positive cross-covariances for all
τ > 1. The upper-cone case is therefore simpler than the lower-cone case: because µ ∈ C + already
implies µ ≻ pNE 1, and the induced correlation bias gives pointwise prices above Nash, no separate
exclusion of the Nash boundary is needed. We record this as the final auxiliary lemma.

Lemma G.8 (Upper-cone strictness). If µ ∈ C + , then

                           P ODE (τ ; µ, Σexp ) ≻ pNE 1       for every τ ∈ [1, ∞).

    Lemma G.8 proves Theorem 3.2(a). Together with the lower-cone argument above, this com-
pletes the proof of Theorem 3.2.

G.1      Proof of Lemma 6.1
Proof.    Fix i ∈ [N ] and hold U and Vii fixed. Write x := V̄i,−i and A := a + c Ū−i . Using the
algebraic OLS price from Definition 3.1, write

                                  A Vii − c Ui x
                       Pei (x) :=                ,     on the domain bVii − cx > 0.
                                  2(bVii − cx)

                                                       64
    Part (1). If x = 0, then
                                                  A Vii   A
                                        Pei (0) =       =    = BR(Ū−i ).
                                                  2bVii   2b
    Part (2). Differentiate Pei with respect to x using the quotient rule. Let N (x) := AVii − cUi x
and D(x) := 2(bVii − cx). Then N ′ (x) = −cUi and D′ (x) = −2c, so
                                                                                   
             ′      N ′ (x)D(x) − N (x)D′ (x)   (−cUi ) 2(bVii − cx) − AVii − cUi x (−2c)
           Pi (x) =
           e                                  =                                           .
                             D(x)2                             4(bVii − cx)2

Expanding the numerator and canceling the x-terms gives

                         (−2cUi bVii + 2cUi cx) + (2cAVii − 2c2 Ui x) = 2cVii (A − bUi ).

Therefore,
                                                       2cVii (A − bUi )
                                            Pei′ (x) =                  .
                                                        4(bVii − cx)2
On the domain bVii − cx > 0, the denominator is strictly positive. Also Vii > 0 because Vii (1) =
(Σexp )ii > 0 and V̇ii = (Pi − Ui )2 ≥ 0. Finally,

                             A − bUi = a + cŪ−i − bUi ≥ a − bPmax + cPmin > 0,

because Ui , Ū−i ∈ [Pmin , Pmax ], Pmin > 0, and Pmax ≤ a/b. Hence Pei′ (x) > 0 and Pei is strictly
increasing in V̄i,−i .

G.2     Proof of the nonnegative-orthant part of Lemma 6.2
Proof. Let e(τ ) := P (τ ) − U (τ ). The claim is that if e(τ0 ) ⪰ 0 for some τ0 ≥ 1, then e(τ ) ⪰ 0 for
all τ ≥ τ0 .
    Assume for contradiction that the trajectory leaves RN
                                                         + after τ0 , and define the first exit time


                                     τ ⋆ := inf{τ ≥ τ0 : ∃i with ei (τ ) < 0}.

By continuity of e(·), we have e(τ ⋆ ) ⪰ 0 and there exists at least one index i with ei (τ ⋆ ) = 0. Fix
such an i.
    We rule out each possible way in which the ith coordinate could be the first one to cross into
the negative orthant.

Clipped and non-OLS branches. First consider the branches on which the posted price is
locally fixed at a cap. If Pi (τ ⋆ ) = Pmin and ei (τ ⋆ ) = 0, then Ui (τ ⋆ ) = Pmin . As long as the lower
clip remains active, Ui solves
                                                          Pmin − Ui (τ )
                                             U̇i (τ ) =                  ,
                                                               τ



                                                           65
with initial value Ui (τ ⋆ ) = Pmin , and hence Ui (τ ) = Pmin on that right-neighborhood. Thus the
lower clip cannot by itself make ei negative. If the lower clip ceases to bind, the posted price moves
weakly upward from Pmin = Ui (τ ⋆ ), which is also not a first exit from RN
                                                                          +.
    If Pi (τ ⋆ ) = Pmax and ei (τ ⋆ ) = 0, then Ui (τ ⋆ ) = Pmax . While the upper clip, or the non-OLS
branch Pi ≡ Pmax , remains active, feasibility gives Ui (τ ) ≤ Pmax and hence ei (τ ) = Pmax −Ui (τ ) ≥ 0.
Therefore this branch cannot itself generate a negative gap. The only remaining possibility is that
the trajectory leaves the upper clipped branch and crosses through the algebraic OLS boundary
Pei = Ui . That crossing is covered by the energy calculation below.

OLS boundary. It remains to rule out a crossing through an OLS boundary point with

                                    Bi := bVii − cV̄i,−i > 0,             Pei (τ ⋆ ) − Ui (τ ⋆ ) = 0.

This includes the interior OLS case and the instant at which a clip ceases to bind. Define
                                                                     
                                           Ei := 2bVii Ui − BR(Ū−i ) − cUi V̄i,−i .

A direct rearrangement of the formula for Pei gives the exact identity

                                                                      −Ei
                                                           Pei − Ui =     .
                                                                      2Bi

Since Bi > 0, crossing from Pei − Ui ≥ 0 to Pei − Ui < 0 is equivalent to crossing from Ei ≤ 0 to
Ei > 0. At time τ ⋆ we have Ei (τ ⋆ ) = 0.
   We now compute Ėi (τ ⋆ ) under the information e(τ ⋆ ) ⪰ 0 and ei (τ ⋆ ) = 0. First, e(τ ⋆ ) ⪰ 0
implies U̇ (τ ⋆ ) = e (τ ⋆ )/τ ⋆ ≥ 0 for all j, so Ū˙ (τ ⋆ ) = 1   U̇ (τ ⋆ ) ≥ 0. Also e (τ ⋆ ) = 0
                                                                  P
             j              j                                      −i             N −1     j̸=i   j                    i
implies U̇i (τ ⋆ ) = 0, and from V̇ = (P − U )(P − U )⊤ we get V̇ii (τ ⋆ ) = ei (τ ⋆ )2 = 0 and V̄˙ i,−i (τ ⋆ ) =
ei (τ ⋆ )ē−i (τ ⋆ ) = 0.
    Differentiating Ei along the ODE gives
                                                                             
                 Ėi = 2b V̇ii Ui − BR(Ū−i ) + 2bVii U̇i − BR′ (Ū−i ) Ū˙ −i − c U̇i V̄i,−i − cUi V̄˙ i,−i .
                                             


Evaluating at τ ⋆ and using V̇ii (τ ⋆ ) = U̇i (τ ⋆ ) = V̄˙ i,−i (τ ⋆ ) = 0 gives

                       Ėi (τ ⋆ ) = −2bVii (τ ⋆ ) BR′ (Ū−i (τ ⋆ )) Ū˙ −i (τ ⋆ ) = −c Vii (τ ⋆ ) Ū˙ −i (τ ⋆ ) ≤ 0.

Therefore, at a boundary point where Ei (τ ⋆ ) = 0, the derivative points toward {Ei ≤ 0} and cannot
cross into {Ei > 0}. Equivalently, Pei − Ui cannot become negative immediately after τ ⋆ , hence ei
cannot become negative immediately after τ ⋆ .

Conclusion. In all cases, ei cannot be the first coordinate to turn negative, contradicting the
definition of τ ⋆ . Hence e(τ ) ⪰ 0 for all τ ≥ τ0 .


                                                                   66
G.3     Proof of Lemma 6.3
Proof. Assume (i) V̄i,−i (τ ) ≥ 0 for all i and τ ≥ 1, and (ii) each coordinate Ui (τ ) is monotone in τ .
Since Ui (τ ) ∈ [Pmin , Pmax ] for all τ (because U is a running average of prices in [Pmin , Pmax ]), every
monotone Ui has a finite limit; write Ui∞ := limτ →∞ Ui (τ ) and U ∞ := (Ui∞ )N
                                                                              i=1 .


Step 1: show Pi (τ ) ≥ BR(Ū−i (τ )) for all i, τ . Fix i and τ . If the non-OLS branch is active,
then Pi (τ ) = Pmax . Under the standing feasibility condition pNE ≤ Pmax and monotonicity of
BR, we have BR(Ū−i (τ )) ≤ BR(Pmax ) ≤ Pmax = Pi (τ ). If instead the OLS branch is active,
then bVii − cV̄i,−i > 0 and Lemma 6.1 gives Pei (U, V ) ≥ BR(Ū−i ) because V̄i,−i ≥ 0 and equality
holds at V̄i,−i = 0. Clipping cannot reduce the value below BR(Ū−i ) since BR(Ū−i ) ≤ Pmax and
Pi = [Pei ][P ,P ] (if BR(Ū−i ) < Pmin then Pi ≥ Pmin > BR(Ū−i )). Hence Pi (τ ) ≥ BR(Ū−i (τ )) in
             min   max

all cases.

Step 2: rule out mini Ui∞ < pNE . Let m∞ := mini Ui∞ and choose an index k with Uk∞ = m∞ .
Suppose for contradiction that m∞ < pNE . Define the continuous function ψ(u, v) := BR(u)−v. We
have ψ(m∞ , m∞ ) = BR(m∞ ) − m∞ > 0 because BR(u) − u is affine with unique zero at u = pNE .
Therefore we can pick ε > 0 small enough that

                                   η := BR(m∞ − ε) − (m∞ + ε) > 0.

                                     ∞ ≥ m∞ , there exists τ such that for all τ ≥ τ , U (τ ) ≤
Since Uk (τ ) → m∞ and Ū−k (τ ) → Ū−k                     1                       1   k
m∞ + ε and Ū−k (τ ) ≥ m∞ − ε. Using Step 1 and monotonicity of BR,

  ek (τ ) := Pk (τ ) − Uk (τ ) ≥ BR(Ū−k (τ )) − Uk (τ ) ≥ BR(m∞ − ε) − (m∞ + ε) = η,                τ ≥ τ1 .

Then U̇k (τ ) = ek (τ )/τ ≥ η/τ for all τ ≥ τ1 , so integrating gives Uk (τ ) ≥ Uk (τ1 ) + η log(τ /τ1 ), which
diverges as τ → ∞, contradicting convergence of Uk (τ ). Hence m∞ ≥ pNE , i.e. U ∞ ⪰ pNE 1.

G.4     Proof of Lemma G.1
Proof. Write e(τ ) := P (τ ) − U (τ ). For i ̸= j, the ODE gives

                                            V̇ij (τ ) = ei (τ )ej (τ ).

If e(τ ) ⪰ 0 for all τ ≥ 1 or e(τ ) ⪯ 0 for all τ ≥ 1, then ei (τ )ej (τ ) ≥ 0 for all i ̸= j and all τ ≥ 1.
Thus Vij is nondecreasing and Vij (τ ) ≥ Vij (1) = 0.
    Now assume e(τ0 ) ≻ 0; the case e(τ0 ) ≺ 0 is identical after reversing signs. Fix any τ > τ0 .
The map (U, V ) 7→ P (U, V ) is continuous (it is a rational map on the OLS region, composed
with coordinatewise clipping, and equals the constant Pmax on the non-OLS region), and (U, V )
is continuous in time because it solves an ODE with locally bounded right-hand side. Hence e(·)
is continuous. Since e(τ0 ) ≻ 0, there exist δτ ∈ (0, τ − τ0 ] and ετ > 0 such that ei (s) ≥ ετ and


                                                       67
ej (s) ≥ ετ for all s ∈ [τ0 , τ0 + δτ ]. Therefore
                                         Z τ                            Z τ0 +δτ
                  Vij (τ ) = Vij (1) +         ei (s)ej (s) ds ≥                   ε2τ ds = ε2τ δτ > 0.
                                           1                             τ0

Since τ > τ0 was arbitrary, Vij (τ ) > 0 for every i ̸= j and every τ > τ0 . Averaging over j ̸= i gives

                                                           1 X
                                         V̄i,−i (τ ) =         Vij (τ ) > 0
                                                         N −1
                                                                 j̸=i


for all i and all τ > τ0 .

G.5      Proof of Lemma G.2
Proof. Assume U ∞ ⪰ pNE 1 and Uj∞ = pNE for some j. Suppose for contradiction that U ∞ ̸= pNE 1.
Then there exists k ̸= j with Uk∞ > pNE , so Ū−j
                                               ∞ > pNE . Because BR is strictly increasing and

BR(pNE ) = pNE , we have BR(Ū−j
                              ∞ ) > pNE . Define


                                                 1      ∞
                                                           ) − pNE > 0.
                                                                  
                                          η :=     BR(Ū−j
                                                 2

By convergence, for all sufficiently large τ we have

                             BR(Ū−j (τ )) ≥ pNE + η,               Uj (τ ) ≤ pNE + η/2.

Also V̄j,−j (τ ) ≥ 0 implies Pj (τ ) ≥ BR(Ū−j (τ )), by the same argument as in the proof of Lemma 6.3.
Hence, for all sufficiently large τ ,

                       ej (τ ) := Pj (τ ) − Uj (τ ) ≥ (pNE + η) − (pNE + η/2) = η/2.

Therefore U̇j (τ ) = ej (τ )/τ ≥ (η/2)/τ for all large τ , which implies Uj (τ ) cannot converge to pNE .
This contradiction shows that no such k exists, hence U ∞ = pNE 1.

G.6      Proof of Lemma G.3
Proof.    Assume e(τ ) := P (τ ) − U (τ ) ⪰ 0 for all τ ≥ τ0 , as in the nonnegative-orthant part of
Lemma 6.2. Fix τ0 ≥ 1 and assume Ṗ (τ0 ) ⪰ 0.
    Because P is defined by a piecewise-smooth map of (U, V ) (rational on the OLS region, constant
on the non-OLS region, and coordinatewise clipped), it suffices to prove that on any open time
interval on which (i) every firm is on the OLS branch (Bi > 0) and (ii) clipping is inactive (Pi =
Pei ∈ (Pmin , Pmax )), the condition Ṗ ⪰ 0 is forward invariant. Once proved, crossing into the clipped
or non-OLS regimes cannot create a negative Ṗi (in those regimes Pi is locally constant), so the
result extends to all τ ≥ τ0 .




                                                            68
Step 1: compute Ṗi and isolate its sign. Work on an interval where Pi = Pei ∈ (Pmin , Pmax )
and Bi := bVii − c V̄i,−i > 0 for every i. Write Ai := a + c Ū−i and recall

                                                           Ai Vii − cUi V̄i,−i
                                                Pi = Pei =                     .
                                                                  2Bi

Define also the (strictly positive) conditional expected demand at (Ui , Ū−i ):

                                        Di := Ai − bUi = a + c Ū−i − bUi > 0,

which holds because Ui , Ū−i ∈ [Pmin , Pmax ] and a − bPmax + cPmin > 0.
     Differentiate Pi along the ODE. First, the reduced ODE gives U̇i = ei /τ and Ū˙ −i = ē−i /τ , where
ē−i := N 1−1 j̸=i ej . Also V̇ii = e2i and V̄˙ i,−i = ei ē−i because V̇ = ee⊤ .
             P

                                                                        i −Ni Ḃi
    Let Ni := Ai Vii − cUi V̄i,−i , so Pi = Ni /(2Bi ). Then Ṗi = Ṅi B2B 2      . Compute
                                                                                               i


                               c
               Ȧi = c Ū˙ −i = ē−i ,           Ḃi = b V̇ii − c V̄˙ i,−i = be2i − cei ē−i = ei (bei − cē−i ),
                               τ

and
                                                                  c                   c
           Ṅi = Ȧi Vii + Ai V̇ii − c U̇i V̄i,−i − cUi V̄˙ i,−i = Vii ē−i + Ai e2i − V̄i,−i ei − cUi ei ē−i .
                                                                  τ                   τ
Substituting into Ṗi and grouping terms yields the factorization

                                c
                      Ṗi =          ℓi k i ,       ℓi := Bi + τ ei Di ,               ki := Vii ē−i − V̄i,−i ei .
                              2τ Bi2

(One can verify this by expanding Ṅi Bi −Ni Ḃi , then using Bi = bVii −cV̄i,−i to rewrite the bracketed
expression as cDi ki ; the remaining (c/τ )Bi ki term comes from the Ȧi contribution.) Under ei ≥ 0,
Bi > 0, and Di > 0, we have ℓi > 0. Hence, on this interior OLS interval,

                                            sign(Ṗi ) = sign(ki )            for each i.

Step 2: derive the dynamics of k and show k ⪰ 0 is forward invariant. Differentiate
ki = Vii ē−i − V̄i,−i ei :
                                        k̇i = V̇ii ē−i + Vii ē˙ −i − V̄˙ i,−i ei − V̄i,−i ėi .

Using V̇ii = e2i and V̄˙ i,−i = ei ē−i , the first and third terms cancel:

                                         V̇ii ē−i − V̄˙ i,−i ei = e2i ē−i − ei ē−i ei = 0.

Thus
                                                     k̇i = Vii ē˙ −i − V̄i,−i ėi .




                                                                  69
Now ėi = Ṗi − U̇i = Ṗi − ei /τ and ē˙ −i = P̄˙−i − Ū˙ −i = P̄˙−i − ē−i /τ , where

                                                           1 X
                                              P̄˙−i :=         Ṗj .
                                                         N −1
                                                                j̸=i


Therefore
                                               1                                               1
                 k̇i = Vii P̄˙−i − V̄i,−i Ṗi − Vii ē−i − V̄i,−i ei = Vii P̄˙−i − V̄i,−i Ṗi − ki .
                                                                    
                                               τ                                               τ
Substituting
                                                           c
                                                 Ṗj =          ℓj kj
                                                         2τ Bj2

gives a linear system k̇ = A(τ )k with Metzler off-diagonal structure: for j ̸= i, the coefficient
multiplying kj in k̇i is
                                                Vii    c
                                                            ℓj ≥ 0.
                                               N − 1 2τ Bj2

Hence the cone {k ⪰ 0} is forward invariant on this interval: if ki hits 0 while all kj ≥ 0, then
k̇i ≥ 0.

Step 3: conclude Ṗ ⪰ 0 persists. At time τ0 we assume Ṗ (τ0 ) ⪰ 0. On the interior OLS
interval, ℓi (τ0 ) > 0, so Ṗi (τ0 ) ≥ 0 implies ki (τ0 ) ≥ 0 for each i. By forward invariance, k(τ ) ⪰ 0 for
later times on the interval, and then Step 1 gives Ṗ (τ ) ⪰ 0.
    Finally, if at some later time the trajectory enters a regime where firm i is clipped (so Pi is
locally constant) or enters the non-OLS branch (Pi ≡ Pmax ), then Ṗi ≥ 0 holds trivially there. Thus
P is componentwise nondecreasing on [τ0 , ∞).

G.7        Proof of Lemma G.4
            Let ei := Pi − Ui and ē−i := (N − 1)−1               j̸=i ej .   Use the notation from the proof of
                                                               P
Proof.
Lemma G.3:

   Bi := bVii − cV̄i,−i ,      Di := a + cŪ−i − bUi ,          ℓi := Bi + τ ei Di ,      ki := Vii ē−i − V̄i,−i ei .

At τ = 1, U (1) = µ, V (1) = Σexp , and Σexp is diagonal, so

                                      Vii (1) = (Σexp )ii ,      V̄i,−i (1) = 0.

Hence Bi (1) = b(Σexp )ii > 0 and the OLS branch is active. Also Pei (1) = BR(µ̄−i ). The clipping is
inactive: the lower clip is inactive because BR(µ̄−i ) > µi ≥ Pmin , while the upper clip is inactive
because
                                        BR(µ̄−i ) ≤ BR(Pmax ) < Pmax .

Hence
                              Pi (1) = BR(µ̄−i ),         ei (1) = BR(µ̄−i ) − µi > 0

                                                          70
for every i, since µ ∈ C − .
    Thus ē−i (1) > 0 and
                                         ki (1) = (Σexp )ii ē−i (1) > 0.

The factorization in Lemma G.3 gives

                                                               c
                                                     Ṗi =          ℓi ki
                                                             2τ Bi2

on the smooth OLS interior branch. At τ = 1, we have Bi (1) > 0, ki (1) > 0, and

                                       ℓi (1) = Bi (1) + ei (1)Di (1) > 0,

since
                               Di (1) = a + cµ̄−i − bµi ≥ a + cPmin − bPmax > 0

by the standing price-bound assumptions. Therefore Ṗi (1+ ) > 0 for every i, so Ṗ (1+ ) ≻ 0.

G.8       Proof of Lemma G.5
Proof.     Assume U (τ ) → pNE 1, e(τ ) := P (τ ) − U (τ ) ⪰ 0 for all τ ≥ 1, P is componentwise
nondecreasing, V̄i,−i (τ ) ≥ 0 for all i, τ , and e(τ0 ) ≻ 0 for some τ0 .

Part (1): P → pNE 1 and eventually P ⪯ pNE 1. Fix i. Since Pi is nondecreasing and Pi (τ ) ∈
[Pmin , Pmax ], the limit
                                                 Pi∞ := lim Pi (τ )
                                                             τ →∞

exists. The ODE U̇i = (Pi − Ui )/τ implies the running-average identity
                                                              Z τ          
                                                 1
                                     Ui (τ ) =        Ui (1) +     Pi (s) ds .
                                                 τ                   1

If Pi (s) → Pi∞ , then the Cesàro mean converges to the same limit:
                                                 Z τ
                                            1
                                                         Pi (s) ds → Pi∞ .
                                            τ        1

Hence Ui (τ ) → Pi∞ as well. Since we also assume Ui (τ ) → pNE , it follows that Pi∞ = pNE for every
i, i.e.
                                                     P (τ ) → pNE 1.

Because Pi is nondecreasing and converges to pNE , we must have Pi (τ ) ≤ pNE for all sufficiently
large τ . Thus P (τ ) ⪯ pNE 1 eventually.




                                                             71
Part (2): convergence of V and strict positivity of limiting cross terms. For large τ ,
Part (1) gives P (τ ) ⪯ pNE 1. Since e(τ ) ⪰ 0, we also have U (τ ) ⪯ P (τ ) ⪯ pNE 1 for large τ . Define

                        gi (τ ) := pNE − Ui (τ ) ≥ 0,              δi (τ ) := pNE − Pi (τ ) ≥ 0

for all sufficiently large τ . Then

                               ei (τ ) = Pi (τ ) − Ui (τ ) = gi (τ ) − δi (τ ) ≤ gi (τ ).

     Because V̄i,−i (τ ) ≥ 0, the same argument as in the proof of Lemma 6.3 gives

                                      Pi (τ ) ≥ BR(Ū−i (τ ))              for all i, τ.

Therefore, for large τ ,

                                                                          c NE              c
             δi (τ ) = pNE − Pi (τ ) ≤ pNE − BR(Ū−i (τ )) =
                                                                                          
                                                                             p − Ū−i (τ ) = ḡ−i (τ ),
                                                                          2b                2b
                                                         PN
where ḡ−i := (N − 1)−1      j̸=i gj . Let G(τ ) :=           i=1 gi (τ ). Using U̇i = ei /τ gives
                           P


                                                             gi (τ ) − δi (τ )
                                              ġi (τ ) = −                     ,
                                                                     τ

so                                                                                              !
                                1X                        1                        c X
                     Ġ(τ ) = −   (gi (τ ) − δi (τ )) ≤ −                  G(τ ) −     ḡ−i (τ ) .
                                τ                         τ                        2b
                                     i                                                     i

But     i ḡ−i = G, since each gj appears in exactly N − 1 averages and the factor 1/(N − 1) cancels.
      P

Hence
                                                         1    c
                                            Ġ(τ ) ≤ −      1−    G(τ ).
                                                         τ     2b
Integrating yields
                                                G(τ ) ≤ Cτ −(1−c/(2b))

for some C > 0. Since c < b implies 1 − 2b
                                        c
                                           > 21 , we have G ∈ L2 ([1, ∞)). In particular, ei (τ ) ≤
gi (τ ) ≤ G(τ ) implies ei ∈ L2 ([1, ∞)).
     Now                                                           Z τ
                                           Vii (τ ) = Vii (1) +           ei (s)2 ds
                                                                      1

converges to a finite limit Vii∞ because e2i is integrable. Similarly, for i ̸= j,
                                                                Z τ
                                         Vij (τ ) = Vij (1) +         ei (s)ej (s) ds
                                                                  1

converges because ei ej is integrable by Cauchy–Schwarz. Finally, since e(τ0 ) ≻ 0, continuity implies




                                                             72
that ei (s)ej (s) > 0 on some interval of positive length for every i ̸= j. Thus
                                                Z ∞
                                                      ei (s)ej (s) ds > 0,
                                                  1

and, because Vij (1) = 0 for i ̸= j, we get Vij∞ > 0 for all i ̸= j. Averaging gives V̄i,−i
                                                                                        ∞ > 0 for all i.




G.9    Proof of Lemma G.6
Proof. Suppose, toward a contradiction, that along a lower-cone trajectory,

           U (τ ) → pNE 1,            P (τ ) → pNE 1,        Vii (τ ) → Vii∞ ,                        ∞
                                                                                     V̄i,−i (τ ) → V̄i,−i >0

for every i. Fix i.
   For large τ , the non-OLS branch is impossible: if −bVii (τ ) + cV̄i,−i (τ ) ≥ 0, then by definition
Pi (τ ) = Pmax , contradicting Pi (τ ) → pNE < Pmax . Thus for all sufficiently large τ we are on the
OLS branch, so
                                          Bi (τ ) := bVii (τ ) − cV̄i,−i (τ ) > 0.

   We first note that Bi∞ := limτ →∞ Bi (τ ) must be strictly positive. If Bi∞ = 0, then since
Vii∞ ≥ Vii (1) > 0 and V̄i,−i
                          ∞ > 0, the numerator of the algebraic OLS price satisfies

                                                                       
              lim         (a + cŪ−i (τ ))Vii (τ ) − cUi (τ )V̄i,−i (τ ) = (a + cpNE )Vii∞ − cpNE V̄i,−i
                                                                                                     ∞
             τ →∞

                                                                       = 2bpNE Vii∞ − cpNE V̄i,−i
                                                                                              ∞


                                                                       = pNE 2bVii∞ − cV̄i,−i
                                                                                          ∞
                                                                                              

                                                                       = pNE bVii∞ > 0,

where the last equality uses bVii∞ = cV̄i,−i
                                         ∞ . Since the denominator 2B (τ ) would converge to 0 from
                                                                     i
above, the algebraic OLS price would diverge to +∞, and hence the clipped posted price would
converge to Pmax , not to pNE . This contradiction shows Bi∞ > 0.
   Therefore we may pass to the limit in the algebraic OLS price. At U = pNE 1 and V̄i,−i
                                                                                      ∞ > 0,

Lemma 6.1 gives
                                         Pei (pNE 1, V ∞ ) > BR(pNE ) = pNE .

Thus there exists η > 0 such that, for all sufficiently large τ ,

                                              Pei (U (τ ), V (τ )) ≥ pNE + η.

Clipping cannot turn this into a price converging to pNE : if Pei (U (τ ), V (τ )) ≤ Pmax , then

                                         Pi (τ ) = Pei (U (τ ), V (τ )) ≥ pNE + η,



                                                            73
while if Pei (U (τ ), V (τ )) > Pmax , then Pi (τ ) = Pmax > pNE . In either case, Pi (τ ) ̸→ pNE , contradict-
ing the assumption. Therefore no such trajectory exists.

G.10      Proof of Lemma G.7
Proof. Let e(τ ) := P (τ ) − U (τ ). Suppose e(τ0 ) ⪯ 0 and assume, toward a contradiction, that the
trajectory leaves RN
                   − after τ0 . Define


                                    τ ⋆ := inf{τ ≥ τ0 : ∃i with ei (τ ) > 0}.

At τ = τ ⋆ , we have e(τ ⋆ ) ⪯ 0 and at least one coordinate satisfies ei (τ ⋆ ) = 0. Fix such an i.
     The upper-cap and non-OLS cases are analogous to the lower-cone argument. If Pi (τ ⋆ ) = Pmax
and ei (τ ⋆ ) = 0, then Ui (τ ⋆ ) = Pmax . As long as the upper clip, or the non-OLS branch Pi ≡ Pmax ,
remains active, Ui solves
                                                           Pmax − Ui (τ )
                                              U̇i (τ ) =
                                                                τ
with initial value Ui (τ ⋆ ) = Pmax , so Ui (τ ) = Pmax and ei (τ ) = 0 on that right-neighborhood. If
the upper cap ceases to bind, the posted price moves weakly downward from Pmax = Ui (τ ⋆ ), which
points into RN
             − , not out of it.
     If Pi (τ ⋆ ) = Pmin and ei (τ ⋆ ) = 0, then Ui (τ ⋆ ) = Pmin . While the lower clip remains active, the
same scalar argument gives Ui (τ ) = Pmin and ei (τ ) = 0. If the lower clip ceases to bind upward,
any possible exit must pass through the algebraic OLS boundary Pei = Ui . Thus it remains only to
rule out an OLS-boundary crossing with

                              Bi := bVii − cV̄i,−i > 0,            Pei (τ ⋆ ) − Ui (τ ⋆ ) = 0.

     Use the same energy as in the proof of the nonnegative-orthant part of Lemma 6.2,
                                                              
                                    Ei := 2bVii Ui − BR(Ū−i ) − cUi V̄i,−i ,

for which
                                                              −Ei
                                                   Pei − Ui =     .
                                                              2Bi
Because Bi > 0, crossing from Pei − Ui ≤ 0 to Pei − Ui > 0 is equivalent to crossing from Ei ≥ 0 to
Ei < 0. At the boundary time, Ei (τ ⋆ ) = 0.
    Now e(τ ⋆ ) ⪯ 0 implies U̇j (τ ⋆ ) = ej (τ ⋆ )/τ ⋆ ≤ 0 for all j, so Ū˙ −i (τ ⋆ ) ≤ 0. Also ei (τ ⋆ ) = 0 implies
U̇ (τ ⋆ ) = 0, V̇ (τ ⋆ ) = 0, and V̄˙ (τ ⋆ ) = 0. The same derivative computation as in the proof of
 i              ii                   i,−i
Lemma 6.2 gives
                                        Ėi (τ ⋆ ) = −cVii (τ ⋆ ) Ū˙ −i (τ ⋆ ) ≥ 0.

Thus Ei cannot cross from Ei ≥ 0 to Ei < 0, equivalently Pei − Ui cannot cross from Pei − Ui ≤ 0 to
Pei − Ui > 0. This contradicts the definition of τ ⋆ . Therefore P (τ ) − U (τ ) ⪯ 0 for all τ ≥ τ0 .


                                                            74
G.11         Proof of Lemma G.8
Proof. We prove the result in four short steps.

Step 1: C + implies exploration means exceed Nash. If µ ∈ C + , then µ ≻ pNE 1. To see this,
let m := mini µi and choose k with µk = m. Since µ̄−k ≥ m and BR is increasing,

                                     m = µk > BR(µ̄−k ) ≥ BR(m).

But BR(u) − u is affine with unique zero at u = pNE , hence m > pNE , and therefore µi ≥ m > pNE
for all i.
    At τ = 1, V (1) = Σexp is diagonal, so V̄i,−i (1) = 0. The zero-cross-covariance case of the pricing
rule gives Pi (1) = BR(µ̄−i ), with the cap inactive under the standing price bounds. Since µ̄−i > pNE
and BR is increasing with BR(pNE ) = pNE , we have

                                        Pi (1) = BR(µ̄−i ) > pNE .

Also, since µ ∈ C + ,
                           Pi (1) − Ui (1) = BR(µ̄−i ) − µi < 0      for all i.

Step 2: the negative orthant is forward invariant. By Lemma G.7,

                                  P (τ ) − U (τ ) ⪯ 0    for all τ ≥ 1.

Thus U is componentwise nonincreasing, since U̇ = (P − U )/τ ⪯ 0. Also, because e(1) ≺ 0,
Lemma G.1 gives
                                V̄i,−i (τ ) > 0   for all i and all τ > 1.

Step 3: the running mean remains weakly above Nash. The hypotheses of Lemma 6.3 are
satisfied on C + : U is componentwise monotone, and V̄i,−i (τ ) ≥ 0 for all i, τ . Hence

                        U ∞ := lim U (τ ) exists and satisfies U ∞ ⪰ pNE 1.
                                τ →∞

Since U is componentwise nonincreasing, this implies

                                U (τ ) ⪰ U ∞ ⪰ pNE 1       for all τ ≥ 1.

Therefore Ū−i (τ ) ≥ pNE for every i and τ .

Step 4: posted prices are strictly above Nash. Fix τ > 1 and i ∈ [N ]. If the non-OLS
branch is active, then Pi (τ ) = Pmax > pNE . If the OLS branch is active, then bVii − cV̄i,−i > 0 and,




                                                    75
since V̄i,−i (τ ) > 0, Lemma 6.1 gives

                                           Pei (τ ) > BR(Ū−i (τ )).

By Step 3, Ū−i (τ ) ≥ pNE , so
                                     BR(Ū−i (τ )) ≥ BR(pNE ) = pNE .

Thus Pei (τ ) > pNE . Clipping cannot reduce the posted price below pNE : if Pei (τ ) ≤ Pmax then
Pi (τ ) = Pei (τ ) > pNE , while if Pei (τ ) > Pmax then Pi (τ ) = Pmax > pNE . Hence

                                  Pi (τ ) > pNE      for all i and all τ > 1.

Together with Step 1, which gives Pi (1) > pNE , we conclude

                      P ODE (τ ; µ, Σexp ) = P (τ ) ≻ pNE 1       for every τ ∈ [1, ∞).




H      Proofs for the Symmetric-History Results (Section 3.2)
This appendix contains two symmetric-history calculations. First, we formalize the historical-
correlation interpretation from Section 3.2: in a symmetric history, the common pairwise price
correlation ρ generates the same symmetric price as an auxiliary conduct game in which each firm
internalizes rivals’ profits with weight ρ. Second, we prove the symmetric-exploration limit in The-
orem 3.3. Throughout, BR(x) = (a + cx)/(2b) and p̄MNP := min{pMNP , Pmax }.

H.1    Historical correlation as an implied conduct parameter
Consider a symmetric price history in the price-moments state. The OLS demand regression is
misspecified because each firm regresses demand on its own price while omitting rivals’ prices, even
though rivals’ prices affect demand. The relevant moments are (U, V ): Ui is firm i’s historical
average price, Vii is its accumulated own-price variance, and Vij is the accumulated covariance
between firms i and j.
    A symmetric equicorrelated history has Ui = u, Vii = v > 0, and Vij = ρv for every pair i ̸= j.
Then
                                                    Vij
                                                  p        = ρ,
                                                   Vii Vjj
so ρ is the common pairwise correlation of firms’ historical price paths. We show that this same ρ
also has a conduct interpretation: the self-consistent OLS price is the same as the symmetric price
in an auxiliary game where each firm acts as if it internalizes a fraction ρ of rivals’ profits. Thus
ρ = 0 corresponds to Nash pricing, while ρ = 1 corresponds to full joint-profit internalization.



                                                       76
   For the calculation, recall the OLS pricing rule
                                         
             (a + cŪ−i )Vii − cUi V̄i,−i                                        1 X                                 1 X
  Pi =                                                   ,        Ū−i :=            Uj ,              V̄i,−i :=         Vij ,
                 2(bVii − cV̄i,−i )        [Pmin ,Pmax ]                       N −1                                N −1
                                                                                         j̸=i                           j̸=i


on the branch where bVii − cV̄i,−i > 0. In the symmetric equicorrelated state below, this condition
holds because bVii − cV̄i,−i = (b − cρ)v > 0.
   Now let
                                                                                        1 X
                                πi (p) = pi (a − bpi + cp̄−i ),             p̄−i :=         pj .
                                                                                      N −1
                                                                                                j̸=i

The auxiliary ρ-conduct game is the static game in which firm i chooses pi ∈ [Pmin , Pmax ] to
maximize
                                                                X
                                                   πi (p) + ρ          πj (p).
                                                                j̸=i

The equivalence below is an outcome equivalence: the OLS rule and this auxiliary conduct game
have the same symmetric fixed-point price, although they need not have the same off-equilibrium
best-response map.

Lemma H.1 (Historical correlation as an implied conduct parameter). Fix N ≥ 2 and ρ ∈ [0, 1].
At any symmetric equicorrelated price-moments state with Ui = u, Vii = v > 0, and Vij = ρv for all
i ̸= j, the misspecified OLS rule reduces to
                                                                
                                                   a + c(1 − ρ)u
                                          Bρ (u) =                               .
                                                     2(b − cρ)     [Pmin ,Pmax ]

Its symmetric self-consistent price is
                                                                                     
                                                                        a
                                           pρ = min Pmax ,                                .
                                                                  2b − c(1 + ρ)

This same pρ is the symmetric Nash price of the auxiliary ρ-conduct game.

   Proof. At the stated symmetric equicorrelated state, Ū−i = u, V̄i,−i = ρv, and bVii − cV̄i,−i =
(b − cρ)v > 0. Substituting into the OLS pricing rule gives
                                                                            
                            (a + cu)v − cuρv                     a + c(1 − ρ)u
                 Pi =                                        =                                 =: Bρ (u).
                               2(bv − cρv)     [Pmin ,Pmax ]       2(b − cρ)     [Pmin ,Pmax ]


   A symmetric self-consistent OLS price solves p = Bρ (p). Ignoring the price caps,

                                                                                               a
                             2(b − cρ)p = a + c(1 − ρ)p,               so        p∗ρ =                 .
                                                                                         2b − c(1 + ρ)

As ρ increases from 0 to 1, this price moves from the Nash price a/(2b − c) to the monopoly price
a/[2(b − c)]. Thus, under the maintained assumption that the lower cap does not bind at Nash,


                                                             77
only the upper cap can bind, giving
                                                                                        
                                                                           a
                                           Pmax , p∗ρ
                                       
                            pρ = min                    = min Pmax ,                          .
                                                                     2b − c(1 + ρ)

    It remains to check that the auxiliary conduct game has the same symmetric price. Differenti-
ating firm i’s auxiliary objective with respect to pi gives
                                  
            ∂             X
                πi (p) + ρ   πj (p) = a − 2bpi + cp̄−i + ρcp̄−i = a − 2bpi + c(1 + ρ)p̄−i .
           ∂pi
                              j̸=i


Therefore the unconstrained best response in the auxiliary game is

                                                        a + c(1 + ρ)p̄−i
                                                pi =                     .
                                                               2b

At a symmetric Nash equilibrium, pi = p̄−i = p, so

                                                (2b − c(1 + ρ))p = a,

which gives the same un-capped price p∗ρ . Applying the same upper price cap yields pρ .
    Thus ρ gives a simple calibration of the implied degree of collusion: ρ = 0 rationalizes the
Nash price, ρ = 1 rationalizes the capped monopoly benchmark, and intermediate values rationalize
intermediate symmetric prices.

H.2      Proof of Theorem 3.3: symmetric-exploration price limit
Proof.    The proof reduces the symmetric price-moments ODE to one scalar trajectory. We then
use the fixed sign of the price-minus-mean gap to get convergence, relate terminal displacement to
accumulated co-movement, and pass to the vanishing-exploration-noise limit.
    Fix σexp > 0 and set Σexp = σexp
                                 2 I . By permutation equivariance of the price-moments ODE
                                     N
in Definition 3.1 and of the posted-price map (7), the symmetric initial condition U (1) = s1 and
             N remains symmetric. Thus there are scalar functions u, v, C, p such that Ui (τ ) =
         2 I
V (1) = σexp                                                     6

u(τ ), Vii (τ ) = v(τ ), Vij (τ ) = C(τ ) for i ̸= j, and Pi (τ ) = p(τ ). They satisfy

                    p−u
             u̇ =       ,        v̇ = Ċ = (p − u)2 ,            u(1) = s,            2
                                                                              v(1) = σexp ,       C(1) = 0,
                     τ

so v − C ≡ σexp
            2 . Since −bv + cC = −(b − c)C − bσ 2 < 0, the non-OLS branch never occurs. The
                                               exp
common unclipped price is
                                       2 ) + cσ 2 u
                              a(C + σexp       exp                                            
            peσexp (u, C) =                         ,             p(τ ) = peσexp (u(τ ), C(τ )) [P                 .
                                               2 )
                               2((b − c)C + bσexp                                                    min ,Pmax ]


   6
     The lowercase notation is local to the symmetric reduction. The full ODE variables remain the vector/matrix
objects U (τ ), V (τ ), and P (τ ).


                                                            78
    Let e(τ ) := p(τ ) − u(τ ). At τ = 1, the unclipped price is BR(s), and clipping preserves the
sign of BR(s) − s. Since BR(s) − s = (a − (2b − c)s)/(2b), this sign is − sign(s − pNE ). By the
sign-invariance lemma, e(τ ) ≥ 0 if s < pNE , e(τ ) ≤ 0 if s > pNE , and e(τ ) ≡ 0 if s = pNE . Hence
u(τ ) is monotone and bounded, so u∞ (σexp ) := limτ →∞ u(τ ) exists; also C(τ ) increases to some
C∞ (σexp ) ∈ [0, ∞].
    We first record the terminal relation between u∞ and C∞ . If C∞ = ∞, then peσexp (u(τ ), C(τ )) →
p MNP , so p(τ ) → p̄MNP ; since u converges and du/d log τ = e has fixed sign, e(τ ) → 0 and therefore
u∞ = p̄MNP . If instead u∞ < p̄MNP , then C∞ < ∞, the upper clip is eventually inactive, and
u∞ = peσexp (u∞ , C∞ ). Solving this identity and using Ċ = e2 = τ 2 u̇2 gives
                                                                      Z ∞                      2
                            2b − c u∞ − pNE
                   2
             C∞ = σexp                        ,                  2
                                                         |u∞ − s| =          r−1 (ru̇(r)) dr       ≤ C∞ .
                           2(b − c) pMNP − u∞                          1


Consequently, whenever u∞ < p̄MNP ,
                                                                             1/2
                                                         2b − c u∞ − pNE
                                                    
                                 |u∞ − s| ≤ σexp                                    .
                                                        2(b − c) pMNP − u∞

The same relation also shows u∞ ≥ pNE ; otherwise the displayed formula for C∞ would be negative.
    We also need an upper bound. If pMNP ≥ Pmax , then u∞ ≤ Pmax = p̄MNP . If pMNP < Pmax ,
then
                                            2(b − c)(pMNP − u)C + (2b − c)(pNE − u)σexp
                                                                                    2
                      peσexp (u, C) − u =                              2 )
                                                                                        .
                                                        2((b − c)C + bσexp

Thus u(τ ) ≥ pMNP +δ eventually would imply p(τ )−u(τ ) ≤ −η eventually, uniformly over C(τ ) ≥ 0,
contradicting convergence of u(τ ). Hence pNE ≤ u∞ (σexp ) ≤ p̄MNP for every σexp > 0.
    Now let σexp ↓ 0. If s = pNE , then e ≡ 0 and u∞ (σexp ) = s. If s ∈ (pNE , p̄MNP ), monotonicity
gives u∞ (σexp ) ≤ s, and the factor in the width bound is uniformly bounded, so u∞ (σexp ) → s. If
s = p̄MNP , the same conclusion follows by contradiction: any subsequence with u∞ (σk ) ≤ s − ε has
a uniformly bounded width factor and is forced to converge to s. Therefore u∞ (σexp ) → s for all
s ∈ [pNE , p̄MNP ].
    If s < pNE , then u∞ (σexp ) ≥ pNE > s. A subsequence satisfying u∞ (σk ) ≤ p̄MNP − ε would
again have a uniformly bounded width factor and would be forced to converge to s, a contradiction.
Hence u∞ (σexp ) → p̄MNP . Finally, if s > p̄MNP , then necessarily p̄MNP = pMNP < Pmax ; the upper
bound gives u∞ (σexp ) ≤ pMNP , and any subsequence bounded below pMNP by a fixed ε is ruled out
by the same width-bound argument. Thus u∞ (σexp ) → pMNP = p̄MNP .
    For each fixed σexp > 0, the preceding terminal argument gives p(τ ) − u(τ ) → 0. Since the
symmetric trajectory satisfies P ODE (τ ; s1, σexp
                                               2 I ) = p(τ )1, we have
                                                   N


                                    lim P ODE (τ ; s1, σexp
                                                        2
                                                            IN ) = u∞ (σexp )1.
                                   τ →∞

Combining this identity with the scalar limits above gives exactly the two cases in Theorem 3.3.


                                                          79
I      Proofs for the Best-Response Cone Characterizations (Section 3.3)
This appendix proves the two auxiliary propositions stated in Section 3.3. Throughout, BR(x) =
(a + cx)/(2b) and C + , C − are the best-response cones defined in (8)–(9). We write P (τ ) for the
posted-price coordinate of the price-moments ODE and U (τ ) for the running price mean.

I.1      Proof of Proposition 3.1
Proof.     Consider the duopoly case N = 2. Let Π(U, V ) denote the posted-price map in the price-
moments ODE. Write (U (τ ), V (τ )) for the ODE solution, P (τ ) := Π(U (τ ), V (τ )), and e(τ ) :=
P (τ ) − U (τ ). We first show that P (τ ) converges.
      For log time s ≥ 0, define

                 U ℓ (s) := U (es ),     Z ℓ (s) := e−s V (es ),         P ℓ (s) := Π(U ℓ (s), Z ℓ (s)),

and set eℓ (s) := P ℓ (s) − U ℓ (s). Since Π is homogeneous of degree zero in its second argument,
P ℓ (s) = P (es ). The log-time dynamics are

                                       U̇ ℓ = eℓ ,       Ż ℓ = eℓ (eℓ )⊤ − Z ℓ ,

where dots denote derivatives in s. The trajectory (U ℓ , Z ℓ ) is bounded: U ℓ (s) ∈ [Pmin , Pmax ]2 , and
                                                         Z s
                                           −s
                                  ℓ
                                Z (s) = e       Σexp +         e−(s−r) eℓ (r)eℓ (r)⊤ dr.
                                                          0

      We use the following elementary consequence of this autonomous log-time system. If U ℓ (s) has
a componentwise limit, then eℓ (s) → 0. Indeed, every point in the ω-limit set has the same U ℓ -
coordinate, equal to that limit. Since the ω-limit set is invariant, the U ℓ -coordinate must remain
fixed along the vector field on this set. But U̇ ℓ = eℓ , so every ω-limit point has eℓ = 0. Hence, by
continuity along the trajectory, eℓ (s) → 0.
      We now consider the sign pattern of eℓ . By Lemma 6.2, if eℓ (s0 ) ⪰ 0 for some s0 , then eℓ (s) ⪰ 0
for all s ≥ s0 . By the sign-reversed argument in Appendix G.10, if eℓ (s0 ) ⪯ 0, then eℓ (s) ⪯ 0 for
all s ≥ s0 . Thus, if the trajectory ever enters one of the two closed same-sign orthants, then U ℓ
is componentwise monotone and bounded on the tail. Hence U ℓ (s) has a componentwise limit, so
eℓ (s) → 0, and P ℓ (s) = U ℓ (s) + eℓ (s) converges.
      It remains to consider the case where the trajectory never enters either closed same-sign orthant.
Then eℓ1 (s)eℓ2 (s) < 0 for every s ≥ 0. Moreover, the mixed-sign orientation cannot change without
first entering one of the two closed same-sign orthants. Hence either eℓ1 (s) > 0 > eℓ2 (s) for all s ≥ 0,
or eℓ2 (s) > 0 > eℓ1 (s) for all s ≥ 0. In the first case U1ℓ is increasing and bounded while U2ℓ is



                                                           80
decreasing and bounded; in the second case the roles of the two coordinates are reversed. Thus
U ℓ (s) again has a componentwise limit, so eℓ (s) → 0, and P ℓ (s) = U ℓ (s) + eℓ (s) converges.
   Therefore P (τ ) converges as τ → ∞, equivalently

                                P ∞ (µ, Σexp ) := lim P ODE (τ ; µ, Σexp )
                                                  τ →∞

exists. The preceding argument also gives U (τ ) → P ∞ (µ, Σexp ).
   It remains to identify the limit. Define

                  ∆1 (τ ) := P1 (τ ) − BR(U2 (τ )),        ∆2 (τ ) := P2 (τ ) − BR(U1 (τ )).

We show that ∆1 (τ ) and ∆2 (τ ) always have the same weak sign. On the OLS branch, a direct
rearrangement of the price-moments pricing formula gives

                          cV12 (a + cU2 − bU1 )                            cV12 (a + cU1 − bU2 )
          Pe1 − BR(U2 ) =                       ,          Pe2 − BR(U1 ) =                       .
                            2b(bV11 − cV12 )                                 2b(bV22 − cV12 )

The terms a + cU2 − bU1 and a + cU1 − bU2 are strictly positive because Ui ∈ [Pmin , Pmax ] and
a − bPmax + cPmin > 0. Hence, on the OLS branch, both unclipped deviations have the sign of V12 .
   Clipping preserves this weak sign. Since BR is increasing with fixed point pNE ∈ [Pmin , Pmax ],
we have BR(x) ∈ [Pmin , Pmax ] for every x ∈ [Pmin , Pmax ]. Therefore projecting Pei onto [Pmin , Pmax ]
cannot change the weak sign of Pei − BR(U−i ). Finally, on the non-OLS branch, the pricing rule sets
Pi = Pmax ; this branch can occur only when the corresponding cross-covariance term is nonnegative,
and then Pi − BR(U−i ) ≥ 0. Therefore, for every τ ,

                                            ∆1 (τ )∆2 (τ ) ≥ 0.

   Passing to the limit and using U (τ ) → P ∞ and continuity of BR, we obtain

                                P1∞ − BR(P2∞ ) P2∞ − BR(P1∞ ) ≥ 0.
                                                            


Thus either both deviations are weakly positive, in which case P ∞ (µ, Σexp ) ∈ C + , or both deviations
are weakly negative, in which case P ∞ (µ, Σexp ) ∈ C − . Hence

                                        P ∞ (µ, Σexp ) ∈ C + ∪ C − .

   If both best-response equalities bind, then

                                P1∞ = BR(P2∞ ),            P2∞ = BR(P1∞ ).

Since BR(x) = (a + cx)/(2b) is affine with slope c/(2b) < 1, this fixed-point system has the unique
solution P1∞ = P2∞ = a/(2b − c) = pNE . Thus the only point at which both best-response equalities
bind is pNE 1. Consequently, if the limiting point is not on a one-sided best-response boundary, then

                                                      81
it lies in C + or C − .

I.2     Proof of Proposition 3.2
Proof. It is convenient to recenter prices around Nash. Let

                                                                         c   r
                                       zi := µi − pNE ,          λ :=       = .
                                                                         2b  2

Since BR(pNE + z) − pNE = λz, the cone conditions become
                                                                                             
                        1  X                                                1  X             
          C + = zi > λ        zj for all i ,                    C − = zi < λ        zj for all i .
                      N −1                                                N −1               
                                j̸=i                                                     j̸=i


      Write the outer band in the random interval prior as [P , P ] = [pNE −L, pNE +H], with L, H > 0.
Let x, y be the two outer-band draws, and let ℓ := min{x, y} and u := max{x, y} as in the main-
body definition of the prior. Conditional on both recentered anchors being positive, equivalently
ℓ > pNE , write
                                       zℓ := ℓ − pNE ,         zu := u − pNE ,

so 0 < zℓ < zu . The remaining N − 2 firms draw independently from [ℓ, u], so after recentering we
may write
                                zk = zℓ + (zu − zℓ )Yk ,             k = 3, . . . , N,

where the Yk are i.i.d. Unif[0, 1]. Let

                                                                    N
                                               zℓ                   X
                                           q := ,          Y :=           Yk .
                                               zu
                                                                    k=3

Conditional on both recentered anchors being positive, the ratio q is uniform on [0, 1] and indepen-
dent of Y .
      When all zi are positive, membership in C + is determined by the smallest coordinate zℓ : since
the inequality                                            P
                                                               j̸=i zj
                                                 zi > λ
                                                           N −1
is most stringent for the smallest zi , it is necessary and sufficient to check it at zi = zℓ . Thus µ ∈ C +
whenever
                                                    zu + N
                                                         P
                                                           k=3 zk
                                             zℓ > λ               .
                                                        N −1
Dividing by zu and substituting zk /zu = q + (1 − q)Yk , this condition is equivalent to

                                                                 λ(1 + Y )
                           q > θ(Y ),         θ(Y ) :=                            .
                                                          (N − 1) − λ(N − 2 − Y )



                                                          82
Since q ∼ Unif[0, 1] independently of Y ,

                   Pr(µ ∈ C + | both recentered anchors positive) = E[1 − θ(Y )].

The function y 7→ θ(y) is concave on [0, N − 2], because

                                             2 (N − 1) − λ(N − 1)
                                                                  
                                          2λ
                              θ′′ (y) = −                        3 < 0.
                                          (N − 1) − λ(N − 2 − y)

Therefore Jensen’s inequality gives
                                                         
                                            N −2                          Nλ
                      E[θ(Y )] ≤ θ(EY ) = θ                   =                       .
                                              2                   2(N − 1) − λ(N − 2)

Hence

                                                                      Nλ              2(N − 1)(1 − λ)
Pr(µ ∈ C + | both recentered anchors positive) ≥ 1−                               =                     .
                                                              2(N − 1) − λ(N − 2)   2(N − 1) − λ(N − 2)

   The same argument applies conditional on both recentered anchors being negative, equivalently
u < pNE , after replacing zi by −zi , and gives the identical lower bound for C − . If

                                           H                         L
                                  π+ :=       ,           π− :=         ,
                                          L+H                       L+H

then the probability that both recentered anchors are positive is π+
                                                                   2 and the probability that both

recentered anchors are negative is π−
                                    2 . Therefore


                                                                 2(N − 1)(1 − λ)
                        Pr(µ ∈ C + ∪ C − ) ≥ (π+
                                               2    2
                                                 + π− )                            .
                                                               2(N − 1) − λ(N − 2)

                            2 + π 2 ≥ 1/2. Thus
Since π+ + π− = 1, we have π+    −

                                                        (N − 1)(1 − λ)
                              Pr(µ ∈ C + ∪ C − ) ≥                       .
                                                     2(N − 1) − λ(N − 2)

Substituting λ = r/2 yields

                                                        (N − 1)(2 − r)
                              Pr(µ ∈ C + ∪ C − ) ≥                       .
                                                     4(N − 1) − r(N − 2)

   It remains to show that this lower bound is at least 1/4. Using λ = r/2 < 1/2,

                                         (N − 1)(1 − λ)     1
                                                          ≥
                                      2(N − 1) − λ(N − 2)   4

is equivalent to
                               4(N − 1)(1 − λ) ≥ 2(N − 1) − λ(N − 2),


                                                     83
or
                                    2(N − 1) ≥ λ(3N − 2).

This holds for every N ≥ 2 because λ < 1/2 implies

                                             3N − 2
                               λ(3N − 2) <          ≤ 2(N − 1).
                                               2

Therefore
                                                (N − 1)(2 − r)    1
                        Pr µ ∈ C + ∪ C − ≥
                                        
                                                                 ≥ ,
                                             4(N − 1) − r(N − 2)  4
as claimed.




                                              84
