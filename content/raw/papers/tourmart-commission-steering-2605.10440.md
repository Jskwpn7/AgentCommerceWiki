---
source_url: https://arxiv.org/abs/2605.10440
source_pdf: https://arxiv.org/pdf/2605.10440
id: arXiv:2605.10440v1
title: "TourMart: A Parametric Audit Instrument for Commission Steering in LLM Travel Agents"
authors: Yao Liu (Chengdu University of Technology; Universiti Sains Malaysia)
published: 2026-05-11
primary_category: cs.CY
tags: [commission-steering, llm-travel-agents, online-travel-agency, platform-transparency, ai-consumer-harm, consumer-deception]
sha256:
ingested: 2026-06-23
---

# TourMart: A Parametric Audit Instrument for Commission Steering in LLM Travel Agents

**arXiv:** 2605.10440v1 [cs.CY] — 11 May 2026
**Author:** Yao Liu
**Affiliation:** Chengdu University of Technology, Leshan, China; Universiti Sains Malaysia, Penang
**ORCID:** https://orcid.org/0009-0009-3128-7802

## Full Extracted Text

<!-- Raw PDF text below -->

                                                 TourMart: A Parametric Audit Instrument for
                                                  Commission Steering in LLM Travel Agents
                                                                             Yao Liua,b,∗
                                           a
                                             Department of Management and Media, The Engineering and Technology College,




arXiv:2605.10440v1 [cs.CY] 11 May 2026
                                                        Chengdu University of Technology, Leshan, 614000, China
                                           b
                                             School of Computer Sciences, Universiti Sains Malaysia, Penang, 11800, Malaysia




                                         Abstract
                                         Online travel agents—Booking, Trip.com, Expedia—have replaced their ranked-
                                         list interfaces with conversational LLM agents that compress a page of op-
                                         tions into one sentence of prose advice. Each booking earns the OTA com-
                                         mission, and different hotels and airlines pay different rates: the agent has
                                         a structural incentive to favor higher-margin recommendations. Whether
                                         any specific deployed agent does this, and by how much, no one can cur-
                                         rently measure. Existing tools—disclosure banners, conversion A/B testing,
                                         UI dark-pattern taxonomies, generic LLM safety scores—were built for older
                                         interfaces and miss the prose-recommendation surface where the steering
                                         happens.
                                             We propose TourMart, an applied intelligent-system audit instrument
                                         for LLM-OTA commission governance. Two interpretable governance levers—
                                         λ (the weight of message-induced perception in the traveler’s accept/reject
                                         decision) and κ (a budget-normalized cap on how far the message can shift
                                         perceived welfare)—drive a paired counterfactual procedure: holding the
                                         same traveler and the same bundle fixed, the steering delta is read off be-
                                         tween a commission-aware OTA prompt and a minimum-disclosure factual
                                         template. A symmetric six-gate producer audit separates LLM-engineering
                                         failures (template collapse, refusal, internal-ID leakage) from genuine com-
                                         mercial steering.
                                             At deployed governance settings (λ=1, κ=0.05), a Qwen-14B reader shows

                                           ∗
                                               Corresponding author. ORCID: 0009-0009-3128-7802.
                                               Email address: liuyao@student.usm.my (Yao Liu)
                                               URL: https://orcid.org/0009-0009-3128-7802 (Yao Liu)
+7.69pp commission-induced steering (exact McNemar p=0.003); a Llama-
3.1-8B reader shows +3.50pp in the same direction at n=143, with a sup-
plemental extended-n replay (n=270, diagnostic window) confirming signif-
icance (+2.96pp, p=0.008). Across the (λ, κ) governance grid both read-
ers pass family-wise scenario-clustered statistical correction (Qwen p<0.001,
Llama p=0.008). TourMart’s output is a sentence a compliance report can
quote: “at this deployment, 7.7 extra commission-steered recommendations
per 100 paired traveler sessions.”
Keywords: LLM agent governance, commission steering, online travel
agency, multi-agent simulation, audit instrument, platform transparency


1. Introduction
    A VP of Compliance at an online travel aggregator is preparing a board
update six months after her company shipped an LLM-based travel assis-
tant. The dashboard she can show the board is conversion: up 3.1% over
the prior quarter. The disclosure she can point to is a two-line banner at the
bottom of the chat window. The audit committee asks the obvious question:
does our assistant steer travelers toward higher-commission inventory? She
cannot answer. This scene is not hypothetical—Ctrip’s “big-data price dis-
crimination” controversies in the early 2020s placed OTA recommendation
governance on Chinese regulators’ files, and tourism bookings run roughly
RMB 5,000–15,000 for domestic and RMB 20,000–50,000+ for international
packages, are purchased at low frequency, and are information-asymmetric
in ways that e-commerce of everyday goods is not. A mis-steered booking is
not meaningfully returnable. For a given LLM travel-agent deployment at a
given configuration, how much does it steer? That is the question this paper
answers. TourMart, the applied intelligent-system audit instrument we
propose, takes a deployed LLM-OTA configuration as input and outputs a
single deployment-specific number the audit committee can quote.
    Four tools already sit on the compliance officer’s shelf, and none of them
gives her the answer.
    Disclosure banners (“responses generated with AI assistance”) were de-
signed for ranked listings, where a user can scan ten options and discount
whichever is tagged sponsored. When the LLM compresses those ten options
into one sentence, that tag has nowhere to attach [1, 2].
    Conversion A/B testing tells the platform whether a configuration sells,

                                      2
not whether it is honest. A configuration that confidently steers a traveler
toward a higher-margin mismatch produces the same conversion lift as one
that surfaces a genuinely better match [3].
    Dark-pattern taxonomies [4, 5, 6] catalog UI manipulation techniques
(scarcity timers, forced-confirmation dialogs, deceptive button placement)
built for the era when the manipulation lived in buttons. The LLM-OTA
setting moves the manipulation into a single sentence of prose, where these
taxonomies do not reach.
    Generic LLM safety scoring—helpfulness, harmlessness, refusal-to-comply—
audits whether the model would tell a user how to make a bomb. It has no
commission-awareness, no welfare anchor, and no comparison to a counter-
factual message; it cannot tell the audit committee whether the model favors
suppliers who pay the platform more.
    Regulatory frameworks across jurisdictions—EU DSA Article 25 [2], FTC
16 CFR 255 [1], MiFID II Article 27 [7], EU P2B Regulation 2019/1150 [8],
and China’s 2022 Algorithm Recommendation Provisions (CAC Order No. 9) [9]—
each name the harm (“manipulation,” “deception,” “undue interference with
consumer choice”) and prohibit it in algorithmically-mediated commercial
contexts. None of them tells the compliance officer how to measure whether
her own LLM is doing it. There is no fuel-economy label for LLM-OTA
deployments.
    TourMart supplies the missing instrument through a three-step audit de-
sign. (1) Paired counterfactual replay. The same traveler agent evalu-
ates the same bundles twice: once under a commission-aware OTA message
(the commercial context, where the LLM knows it sells for margin), and
once under a minimum-disclosure factual template (no sales language, just
the bundle’s objective specifications). The acceptance gap between these two
runs, with bundle and traveler held fixed, is the steering reading. (2) Two
governance dials swept across a 6×6 grid. A gain λ and a saturation
cap κ act on the message-induced perception term inside a frozen welfare
rule (formal definitions in §3), mapping how steering changes as platform
governance parameters drift away from the deployed point. (3) A sym-
metric six-gate audit on the producer LLM that wrote the messages,
separating generator-side failure modes (template collapse, refusal hedging,
internal-ID leakage) from genuine commercial steering. TourMart’s output
is not a leaderboard score; it is a sentence the audit committee can quote:
“at (λ=1, κ=0.05), this deployment produces +Xpp paired steering under the
hardened welfare rule.”

                                   3
    We instantiate TourMart with a Qwen-7B-Instruct OTA producer and
two traveler-reader backbones (Qwen-14B-AWQ and Llama-3.1-8B) across
143 near-threshold paired stimuli—the regime where the welfare rule is me-
chanically flippable. At the deployed governance point (λ=1, κ=0.05), the
Qwen reader shows +7.69pp commission-induced steering (exact McNemar
p=0.003). The Llama reader shows +3.50pp in the same direction; at n=143
this arm is under-powered for the pre-registered exact test, but a supplemen-
tal extended-n replay (n=270, diagnostic window) confirms significance at
α=0.05 (+2.96pp, b/c=8/0, exact p=0.008; §6.1). Across the 2D governance
grid, peak steering reaches +10.49pp on Qwen and +7.69pp on Llama, with
scenario-clustered grid max-stat permutation p<0.001 on Qwen and p=0.008
on Llama. A symmetric six-gate audit on the producer LLM surfaces two
distinct default-prompt failure modes: Qwen over-hedges (55.9% refusal un-
der a hardened refusal classifier), Llama template-collapses with 80.9–84.6%
internal-ID leakage in its messages. These are governance readings, not ca-
pability claims: TourMart audits a deployed configuration, it does not score
the underlying language model.

Contributions
  1. A parametric audit instrument for commission governance.
     Two interpretable governance dials, λ and κ, act on a frozen welfare-
     rule decision to produce per-configuration behavioral readings rather
     than a leaderboard score.
  2. Scenario-clustered paired inference with channel attribution.
     Grid max-stat permutation correction with scenario as the cluster unit,
     plus coefficient-zero attribution that localizes observed steering to spe-
     cific perception channels under the frozen rule.
  3. Symmetric six-gate producer audit. Identical gates applied to the
     OTA that produced the messages, diagnosing generator-side failures
     (Qwen over-hedging, Llama template-collapse with a repairable style
     fix) that would otherwise confound the behavioral reading.

2. Related Work
    TourMart sits at the intersection of four research lineages whose top-venue
history establishes the legitimacy of its constituent moves; we are explicit
that two of the four are load-bearing (their methods constrain ours) and two


                                      4
are paradigm-level support (their existence licenses the move, but we do not
inherit their architectures).
    (L1, paradigm support) LLM-as-behavioral-subject. Park et al.’s
Generative Agents (UIST 2023) [10], Horton’s Homo Silicus (NBER 2023) [11],
and Argyle et al.’s silicon-sample framework (Political Analysis 2023) [12] es-
tablish that LLMs can be treated as behavioral subjects in social-scientific
simulation. We inherit the legitimacy of LLM agents as traveler-reader and
OTA-producer stand-ins, not their memory, planning, or fidelity-validation
architectures.
    (L2, load-bearing) LLM persuasion measurement. Salvi et al. (Na-
ture Human Behaviour 2025) [13] and the concurrent commercial-steering
line [14, 15] supply the paired-counterfactual measurement frame that Tour-
Mart uses to identify message-induced steering. We extend it from a binary
disclosure manipulation to a continuous (λ, κ) governance grid acting on a
frozen welfare rule.
    (L3, load-bearing) Algorithmic platform audit. Sandvig et al.
(ICA 2014) [16], Hannak et al. (WWW 2013) [17], and Metaxa et al. (Foun-
dations & Trends in HCI 2021) [18] define the external-querying audit in-
strument: probe an opaque platform with controlled inputs, observe out-
puts, infer behavior. TourMart instantiates this paradigm at the LLM-prose-
recommendation surface; (λ, κ) are audit knobs in this tradition.
    (L4, paradigm support) Dark patterns in OTA and LLM con-
texts. Kim et al. (Annals of Tourism Research 2021) [19] document UI-
level dark patterns on OTA websites; DarkBench (ICLR 2025 Oral) [20]
extends the dark-pattern taxonomy to LLM outputs. TourMart’s symmet-
ric six-gate producer audit isolates generator-side failures (template collapse,
refusal, internal-ID leakage) from genuine commercial steering—a layer ad-
jacent to, not derived from, these taxonomies.
    We do not claim a new lineage; each is well established. Our contri-
bution is their first instrumented collision in the OTA commission-steering
vertical, where no deployment-specific comparative audit readout currently
exists. We make this scope deliberately narrow: (λ, κ) are decision-time gov-
ernance parameters acting on a frozen welfare rule, not multi-sided exposure-
fairness tradeoffs in the sense of Wu et al. (SIGIR 2022) [21], who jointly
model consumer- and producer-side exposure for ranking. The instrument
is a comparative audit readout, not a calibrated metrology device, and we
treat traveler-reader behavioral fidelity to real bookers as an open validation
question (§9).

                                      5
    We organize the rest of this section by the governance question: what
platforms do today to self-regulate LLM-OTA steering; what regulators have
tried to require; what researchers have built as adjacent tools; and where
each falls short of the readout a compliance officer needs.

2.1. What platforms do today
    Industry practice on LLM-mediated recommendation governance rests on
three legs, none of which yields a per-deployment welfare reading. First, boil-
erplate disclosure: a short banner appended to every assistant message. A
product team’s job is to minimize the banner’s salience; it persists but the
prose it frames steers anyway. Second, internal prompt-engineering policy—
trust-and-safety teams write rules such as “do not mention higher-commission
inventory first”—but these rules are not externally auditable, not version-
controlled against live deployment, and fail silently when the model drifts.
Third, conversion A/B testing, the workhorse of platform measurement: A/B
captures platform benefit (did the traveler book?) but cannot separate con-
version lift from welfare steering. A message that steers a user toward a
higher-commission mismatch produces the same A/B signal as one that sur-
faces a better match [3]. Large-scale industrial deployments report task and
conversion metrics under internal policy; none publishes a welfare-relative
instrument. No per-deployment welfare-relative readout exists in the public
record at the prose-recommendation level.

2.2. What regulators have tried
    Regulatory text names the harm without defining it operationally. The
EU Digital Services Act (Article 25) [2] prohibits interface design that “ma-
terially distorts or impairs the ability of recipients to make free and informed
decisions,” but does not specify a test. The FTC 2022 dark-pattern re-
port [22] and 16 CFR Part 255 Endorsement Guides [1] govern advertising-
style disclosure and predate the prose-recommendation surface. MiFID II
Article 27 [7] articulates a best-execution analogue in financial trading—the
closest prior regulatory instrument with an explicit measurement demand—
but its measurement apparatus does not transfer to commission-driven travel
recommendation. The DSA Observatory [23] tracks the shift from “default
+ opt-out” toward dynamic controls, underscoring that the regulatory target
itself is moving. Adjacent frameworks (EU P2B Regulation 2019/1150 on
platform-to-business transparency [8]; China’s 2022 Algorithm Recommen-
dation Administrative Provisions, CAC Order No. 9 [9]) likewise articulate

                                       6
normative targets without prescribing quantitative tests. Across jurisdic-
tions, the pattern is the same: each instrument names the harm without
operationalizing how to measure it.

2.3. What researchers have offered
    Four strands of research tooling bear on LLM-OTA governance. Each
has produced valuable work; each has a structural gap that prevents it from
producing the reading the compliance officer needs.
Travel-planning benchmarks.. TravelPlanner [24], TripCraft [25], TripScore [26],
TravelBench [27], WideHorizon [28], and TravelAgent [29] measure single-
planner task success against ground-truth itineraries or reward models. They
do not model a commission channel, do not define a welfare rule that gover-
nance parameters can act on, and do not pair a commission message against
a counterfactual.
Multi-agent simulations.. Generative Agents [10] initiated a line of multi-
agent social simulation extended by AutoGen [30], CAMEL [31], MetaGPT [32],
AgentVerse [33], SOTOPIA [34], GovSim [35], and Stakeholders [36]; eco-
nomically grounded variants include EconAgent [37], CompeteAI [38], RecA-
gent [39], Turing Experiments [40], and Homo Silicus [11]. Task-competence
benchmarks AgentBench [41] and AgentBoard [42] measure within-task progress
for a single agent. None of these parametrizes a welfare rule and sweeps gov-
ernance knobs over a paired counterfactual.
Persuasion and sycophancy.. Sycophancy [43], SycEval [44], Durmus et al. [45],
Salvi et al. [13], Hackenburg and Margetts [46], Matz et al. [47], Bai et al. [48],
and Rogiers et al. [49] quantify whether LLMs can shift user attitudes, typi-
cally in debate, advocacy, or marketing. They measure user-side preference
shift, not platform-induced welfare loss under a commission objective.
Commercial steering and LLM-mediated commerce.. A concurrent line of
work has begun to measure LLM commercial steering directly. Salvi et
al. [14], in two preregistered experiments (N =2,012), construct paired coun-
terfactual ebook selection trials in which one-fifth of products are randomly
designated sponsored: an LLM-mediated interface selects sponsored prod-
ucts at 61.2% versus 22.4% under traditional search, with most participants
failing to detect the steering; sponsorship label and concealment instruc-
tions are varied as a binary disclosure axis. Bansal et al. [15] release Ma-
gentic Marketplace, an open-source agentic-market simulator that exposes a

                                       7
generic-marketplace agent to a fixed catalogue of manipulation tactics. These
works establish the phenomenon of LLM commercial steering and a binary-
treatment measurement frame; they do not (i) target the OTA travel verti-
cal, where bookings are high-stakes, low-frequency, and explicitly regulated
by EU DSA Article 25 [2], the FTC Endorsement Guides [1], and China’s
2022 Algorithm Recommendation Provisions; (ii) parametrize commission
intensity and disclosure strictness as continuous orthogonal governance dials
acting on a welfare-rule decision rather than as binary sponsored-versus-
not labels; or (iii) apply a symmetric producer-side audit that distinguishes
generator-failure modes (over-hedging, template collapse, internal-ID leak-
age) from behavioral steering. TourMart positions itself as the instrument
layer that connects the commercial-steering phenomenon to a per-deployment
compliance readout in a regulated commercial vertical, validated under cross-
family replication.

Dark patterns and mechanism design.. UI-level classification—Mathur et al. [6],
Gray et al. [4, 5], Di Geronimo et al. [50], Luguri and Strahilevitz [51]—is
post-hoc and captures UI artefacts, not deployment-time prose under pa-
rameter variation. DarkBench [20] extends the taxonomy to LLM outputs;
Ersoy et al. [52] invert the frame, studying LLMs as victims of UI dark
patterns. Recommender-fairness frameworks (FairRec [53]) regulate ranking
rather than generated prose. Auction-based aggregation (Duetting et al. [54],
Soumalias et al. [55], Dubey et al. [56]) and collusion analysis (Fish et al. [57])
regulate multi-LLM markets through bidding; they do not instrument a sin-
gle deployed LLM’s prose adjustment relative to a welfare rule.
    No strand, alone or in combination, produces the sentence a compliance
officer needs.

2.4. The gap and our contribution
    Taken together, the prior subsections describe a literature that has char-
acterized the harm, named it in regulation, and built adjacent tools for plan-
ning, persuasion analysis, dark-pattern detection, and mechanism design.
What none of them supplies—and what a compliance officer, a board mem-
ber, or a regulator would need in order to act—is a per-configuration,
welfare-rule-anchored, scenario-clustered behavioral readout, with
an external audit on the producer that generated the prose.
Concurrent work has established the phenomenon of LLM commercial steer-
ing in adjacent commercial settings: Salvi et al. [14], in two preregistered

                                       8
ebook-recommendation experiments (N =2,012), demonstrate substantial sponsored-
product preference under binary disclosure manipulation; Bansal et al. [15]
release an open-source agentic-market simulator. We acknowledge these as
the phenomenon-establishing prior art. TourMart’s contribution is not first
measurement of LLM commercial steering—that priority belongs to Salvi et al. [14]—
but the first audit-instrument variant for this phenomenon in a regulated com-
mercial vertical, featuring (i) a continuous (λ, κ) governance grid acting on a
frozen welfare rule (where λ is gain and κ saturation cap on a single message-
induced welfare channel), exposing a three-regime structure (attenuated, live
transmission, saturated) that a binary disclosure axis cannot recover (§6.5);
(ii) a symmetric producer-side six-gate audit that separates generator-failure
modes (template collapse, refusal, internal-ID leakage) from genuine com-
mercial steering—absent in Salvi et al. and required for any deployment-grade
audit; and (iii) scenario-clustered grid max-stat correction with cross-family
verification at the audit-gate level (full Llama-OTA paired replay deferred to
future work; see §9). The differentiation against [14] breaks down along five
axes:

Domain. Salvi et al. study e-book recommendation (consumer retail). We
   study OTA travel, a commercial vertical with explicit regulatory an-
   choring (EU DSA Art. 25, FTC 16 CFR 255, EU P2B 2019/1150,
   China 2022 Algorithm Recommendation Provisions, MiFID II Art. 27
   as best-execution analogue).
Treatment design. Binary disclosure (sponsored-labeled vs. unlabeled) in
     Salvi et al.; continuous (λ, κ) governance grid over 36 cells in TourMart,
     exposing attenuated / live / saturated regimes a binary axis cannot
     recover (§6.5).
Producer-side audit. Absent in Salvi et al. (single-interface measurement).
    TourMart adds a symmetric six-gate audit (JSON validity, bundle cov-
    erage, word-count, refusal, unique-message ratio, ID leakage) that sep-
    arates generator failures from commercial steering.
Cross-family verification. Salvi et al. use one LLM interface. TourMart
    spans two traveler-reader backbones (Qwen-14B-AWQ, Llama-3.1-8B),
    both significant at α=0.05 (Qwen at primary n=143; Llama via extended-
    n supplement at n=270). Producer side attempted Mistral and Llama;
    both surfaced gate failures.


                                      9
           Market M              OTA Θ               Dials (λ, κ)


                            Paired stimuli S


                             msgorig , msgfact         6-gate producer audit


                                ϕorig , ϕfact


                          Welfare rule (Eq. 1)


                          ∆acc , pMcNemar , pperm         gate vector g

Figure 1: TourMart audit instrument. Inputs: market M , deployed OTA Θ, governance
dials (λ, κ). The OTA produces a commission-aware message and a minimum-disclosure
factual template on each paired stimulus; the traveler-reader extracts perception features
that feed the welfare rule. Outputs: paired steering delta ∆acc , significance under exact
McNemar and scenario-clustered permutation, plus a producer-side audit gate vector g.
See Algorithm 2 for the full procedure.


Mechanism analysis. Salvi et al. report effect-size estimates; TourMart
    adds coefficient-zero attribution decomposing steering across four per-
    ception channels (fit, trust, risk, urgency).

3. Problem Formulation
3.1. The TourMart marketplace
    A small market M = (T, H, A, B) with travelers T , hotels H, airlines A,
and bundles B. Each traveler t ∈ T has a budget bt , a vibe/archetype with
acceptance threshold τt , and a utility ut (β) over bundles β ∈ B.
    Each bundle β has a price p(β) decomposed into hotel, airline,
                                                                P and extras
costs. An allocation α : T → B ∪{∅} produces traveler surplus t (ut (α(t))−
p(α(t))) · ⊮[α(t) ̸= ∅] and platform revenue equal to the sum of commission
on matched bundles.
    Oracle welfare ceiling: computed by MILP over feasible allocations
(details in Section 5).

                                                10
3.2. The OTA-traveler interaction
    For each market and condition c ∈ {commission, satisfaction, disclosure}:
   1. The OTA LLM receives traveler profiles plus an observable prior (signal
      strength w ∈ [0, 1]) and produces per-traveler recommendations with
      natural-language messages.
   2. Each traveler LLM receives its profile, the OTA’s message, and the
      recommended bundle, and extracts 4 perceived features ϕ(β, msg) ∈
      [−1, 1]4 (perceived fit, trust, risk, urgency).
   3. A deterministic welfare rule maps those features to an acceptance
      decision.

3.3. The decision rule with governance parameters

                  acc(ϕ, ut , pβ , bt , τt ; λ, κ) =
                    h                                                     i    (1)
                  ⊮ (ut (β) − pβ ) + clip(λ⃗c · ϕ · bt , [±κbt ]) ≥ τt bt
      with:

      • λ = coefficient multiplier (Round 20 baseline: λ = 1.0)

      • κ = message adjustment cap as a fraction of budget (Round 20: κ =
        0.05)

      • ⃗c = (0.03, 0.015, −0.025, 0.01) (fit, trust, risk, urgency; signs denote
         direction of effect on welfare)1

      • Hard floor: if ut (β) − pβ < −0.10 · bt , reject regardless.

   λ and κ are the governance parameters we vary in the phase dia-
gram.

  1
    Released evidence files results/phase1c_cap_ablation_v4.md and results/
phase1c_coef_attribution_v4.md print risk=0.025 as a magnitude; the negative sign
is absorbed into the dot product in Eq. 1 above. Both conventions describe the same
welfare rule; higher perceived risk reduces welfare.




                                             11
 Algorithm 1: TourMart Audit Instrument                                        (label 2)
 Input: Market M = (T, H, A, B); deployed OTA backbone Θ; traveler-
 reader Π; governance dials (λ, κ); near-threshold sample S with |S| = n.
 Output: Audit reading R = (∆acc , pMcNemar , pperm , g).

 1.    for each paired stimulus (t, β) ∈ S do
 2.         msgorig ← Θ(t, β; commission-signal)
 3.         msgfact ← factual_template(t, β)
 4.         ϕorig ← Π(t, β, msgorig ); ϕfact ← Π(t, β, msgfact )
 5.         aorig [t, β] ← acc(ϕorig , ut , pβ , bt , τt ; λ, κ) (Eq. 1)
 6.         afact [t, β] ← acc(ϕfact , ut , pβ , bt , τt ; λ, κ)
 7.    end for P
 8.    ∆acc ← n1 (t,β)∈S (aorig [t, β] − afact [t, β])
 9.    (b, c) ← count discordant pairs where aorig ̸= afact
 10.   pMcNemar ← ExactMcNemar(b, c)
 11.   pperm ← ScenarioClusteredPermutation(S, nperm =1000)
 12.   g ← SixGateAudit({msgorig }(t,β)∈S )
 13.   return R = (∆acc , pMcNemar , pperm , g)


Figure 2: TourMart audit procedure: paired counterfactual generation under fixed traveler
and bundle, deterministic welfare-rule scoring, exact and permutation significance, and
producer-side gate audit.


3.4. Estimand
    The paired acceptance delta
                           1     X
                                            acc(ϕorig , ·) − acc(ϕfact , ·)
                                                                          
                  ∆acc =
                           n
                               (m,t,β)∈S


over the sampled near-threshold stimuli S, where ϕorig is extracted from the
OTA’s free-text commission message and ϕfact from a minimum-disclosure
factual template.
    Pre-registered primary endpoint: ∆acc at deployed parameters (λ =
1, κ = 0.05) for each traveler backbone, tested by exact McNemar on discor-
dant pairs.



                                               12
4. The Commission-Messaging Treatment
4.1. OTA prompt
    The OTA agent receives:

   • Market state (bundles, travelers, budgets, capacities).

   • Observable preference prior (signal-weighted).

   • Condition-specific objective block:

        – Commission: “maximize platform commission”
        – Satisfaction: “maximize traveler welfare”
        – Disclosure-compliant: mandatory disclosures block

It outputs a JSON payload with decision_table and recommendations
(bundle_id, message, disclosures).

4.2. Factual template
    Minimum-disclosure floor:

     “Recommend β. Total price: p. Commission rate: r%. Extras:
     E.”

This represents the operational counterfactual—what a regulator could man-
date as a minimum-factual-disclosure floor. It is not a length-matched
persuasion-isolation control; that is a different estimand (future work).

4.3. Traveler hybrid architecture
    Each traveler LLM uses guided JSON to produce {perceived_fit_delta:
float, perceived_risk: float, trust_score: float, urgency_felt:
float, reasoning: str}. A deterministic welfare rule then evaluates ac-
ceptance.




                                     13
5. Experimental Setup
5.1. Models (locked Round 20)
    • OTA backbone: Qwen2.5-7B-Instruct, bf16, vLLM with guided JSON
      and per-market bundle_id enum, max_tokens=2500.
       • Traveler backbones: Qwen2.5-14B-Instruct-AWQ (float16, awq_marlin);
         Llama-3.1-8B-Instruct (bfloat16).
       • Welfare rule: frozen Round 20 coefficients; MSG_ADJ_CAP = 0.05·
         budget; baseline_floor = −0.10 · budget.
5.2. Markets and scenarios
    • Small-market generator generate_small_market(seed, regime) with
      3–5 hotels, 2–3 airlines, 3–6 travelers, 6–10 bundles.
       • Scenario pool: 75 loose regime + 75 tight regime, 3 episode seeds →
         450 per regime, 900 total (v4 scale).
       • Conditions: commission / satisfaction / disclosure_compliant (only
         commission used for Phase 1c replay).
       • Signal weight w ∈ {0.25, 0.5, 0.75} crossed with regime.
5.3. Near-threshold window (diagnostic)

                  baseline_surplus ∈ [τt bt − 0.10bt , τt bt + 0.05bt ]
Stratified sampling per (w, regime), target 100 per stratum, seed = 42.

5.4. Paired sampling
    For each sampled recommendation, the traveler LLM evaluates two vari-
ants:
       • Original: OTA’s full commission-condition message.
       • Factual: minimum-disclosure template.
Paired by the 3-tuple key (scenario, traveler, bundle); the diagnostic-window
filter plus this pairing yields 143 paired stimuli across 88 scenarios (v4).2

   2
     The stratified sampling can produce multiple (signal_wt, episode_seed) realizations
for the same (scenario, traveler, bundle) 3-tuple; under the 3-tuple pair-up, the last real-


                                            14
5.5. Statistical plan (pre-registered)
   1. Primary (per arm): McNemar exact on discordant pairs at deployed
      (λ = 1, κ = 0.05).
   2. 2D phase diagram (secondary-but-predeclared): λ ∈ {1, 2, 3, 5, 10, 20}×
      κ ∈ {1%, 2.5%, 5%, 10%, 20%, 100%}: 36 cells.
   3. Family-wise correction: grid-level max-stat permutation with sce-
      nario as cluster unit (1000 permutations).
   4. Exploratory feature-level: Holm-corrected paired Wilcoxon on the
      4 feature deltas.

5.6. Validity gates
    • Parse success ≥ 95%.

    • Factual acceptance not at ceiling (< 98%).

    • Near-threshold window mechanically flippable.

5.7. OTA-backbone audit (symmetric stimulus)
    Our main results use Qwen-7B-Instruct as the OTA backbone. As a ro-
bustness diagnostic, we audited Llama-3.1-8B-Instruct as a candidate OTA
under the same SYSTEM_PROMPT and vLLM guided-JSON configura-
tion. The audit applies six gates symmetrically to both candidate and com-
parator msgcap: (i) JSON validity ≥ 85%, (ii) bundle-id coverage on suc-
cess recommendations ≥ 80%, (iii) message word-count median ∈ [10, 200],
(iv) refusal/hedging rate ≤ 20% under a regex-based hardened refusal
classifier (regex v2—11 additions over v1: unfortunately, couldn’t find,
could not find, unable to find, cannot find, did not find, no suitable,
not suitable, no bundle matches, does not match your, doesn’t match
your), (v) unique-message ratio on success-only ≥ 30%, (vi) internal-ID leak-
age (regex t\d+ or b\d+ appearing in the message body) ≤ 20%. The classi-
fier is a regex by implementation and a refusal decision rule by function; we

ization per 3-tuple is retained and the earlier ones are collapsed. A strict full-identity
5-tuple (scenario, w, seed, traveler, bundle) re-pairing on the same raw data yields n=409
pairs and shifts the deployed- and peak-point effect sizes (see reproduction artifact
scripts/reproduce_permutation.py and the sibling 5-tuple variant). The headline num-
bers reported in Table 1, the abstract, and the Results section are the 3-tuple analysis; we
release the episode-seed-annotated raw log (results/phase1c_*_diag_v4_report.with_
episode_seed.raw.jsonl) so external verifiers can reproduce either pairing.


                                            15
Table 1: McNemar paired acceptance test at deployed (λ = 1, κ = 0.05).    b/c:
discordant+ /discordant− .
Arm                n   b/c   orig / fact acc   RD             95% CI McNemar p
Qwen-14B-AWQ 143 12/1 56.64 / 48.95% +7.69pp [+2.88, +13.24]             0.0034
Llama-3.1-8B 143 5/0 64.34 / 60.84% +3.50pp [+0.71, +6.58]               0.0625


use “regex-based refusal classifier” consistently throughout. The full protocol,
pre-registration-in-spirit guardrail, and all four audit markdown outputs are
reported in Appendix Appendix C.3 and in refine-logs/PHASE1C_SECTION_5_3_FINDING.md.

6. Results — Cross-family Phase Diagram (Qwen-OTA, n=143)
6.1. Primary endpoint at deployed parameters
    The Qwen-reader arm is significantly steered by commission
messages at deployed parameters. The Llama-reader RD point esti-
mate is positive and its estimation interval excludes zero, but under our
pre-registered two-sided exact McNemar decision rule even the most one-
sided 5/0 split among five discordant pairs yields the minimum achievable
p-value p = 2 · (1/2)5 = 0.0625; we therefore report the deployed Llama effect
as not significant at α = 0.05 despite the positive estimation interval. The
RD estimation CI and the exact McNemar test address different inferential
objects (RD magnitude vs. a discordant-pair sign test), and the two disagree
when the discordant count b+c is small; we treat the pre-registered exact
test as the decision rule and flag this as an inference-method sensitivity in
Section 9.

B.1 supplemental robustness check (Llama extended-n).. The Llama-reader
b+c=5 at deployed parameters places the pre-registered exact McNemar
test at its minimum-achievable p=0.0625, leaving the under-power explana-
tion indistinguishable from a true null. To separate these we ran a post-
submission supplemental replay of the Llama-3.1-8B reader on the same
Qwen-7B-OTA msgcap_v4 source, widening the near-threshold selection from
primary to diagnostic ([τ b − 0.10b, τ b + 0.05b], per-stratum capped at 45)
to lift n from 143 to 270. The extended sample yields +2.96pp paired
RD, b/c=8/0, exact two-sided p=0.0078 (the achievable floor at b+c=8),
95% CI [+0.65, +5.95]pp—cross-family confirmation at α=0.05. The extended-
n point estimate is slightly attenuated relative to the primary-window +3.50pp,

                                       16
         Table 2: Qwen heterogeneity. w = 0.75 shows a strong main effect.
           signal_wt     n           RD      disc+ /disc−   McNemar p
           0.25         46      +6.52pp              3/0         0.25
           0.5          42        0.00pp             1/1         1.00
           0.75         55     +14.55pp              8/0     0.0078 ⋆


consistent with the diagnostic window pulling in pairs that are mechani-
cally less flippable. The producer-side six-gate audit on the same upstream
msgcap reproduces the known Qwen over-hedging failure mode (55.9% re-
fusal) and passes the five other gates. The supplemental replay artifacts
(raw paired JSONL, selection manifest, verdict markdown) are released as
B1_VERDICT_BUNDLE.tar.gz alongside the reproducibility package.

Clip-rate diagnostic.. The clip operation in Eq. 1 binds whenever |λ⃗c · ϕ| >
κ. Across n = 818 paired stimuli (409 original + 409 factual per arm),
empirical |⃗c · ϕ| has mean 0.016 on the Qwen arm and 0.034 on the Llama
arm, with maxima of 0.045 and 0.048 respectively—both below the deployed
κ = 0.05. At deployed (λ=1, κ=0.05) the cap therefore binds on 0/818
(0.0%) stimuli on both arms: κ is prophylactic, not active. The full grid-level
clip-binding map (computed from the released paired-output JSON; analysis
snippet in reproducibility/scripts) shows κ activating as λ scales: at
(λ=1, κ=0.025) the Qwen arm has 7.5% clip-binding while Llama reaches
88.9%, and at (λ=3, κ=0.10) Qwen sits at 7.2% while Llama is already at
68.1%—a qualitative differential bite pattern across (λ, κ) cells that a binary
disclosure axis cannot expose. The deployed point is therefore the least-
saturated end of the grid; the +7.69pp Qwen reading is the unsaturated linear
effect of message-induced perception, and κ becomes a governance lever only
when λ is scaled or when the perception extractor produces near-envelope
|⃗c · ϕ|.

6.2. Heterogeneity by signal strength
    Higher signal-strength (more targeted recommendations) amplifies commission-
steering. This is expected if steering exploits preference-matched framings.

6.3. The 2D phase diagram
    Key features (Figure 3):


                                        17
                                                 Figure 1. Cross-family behavioral steering phase diagram
                                                 (original factual, cell format: RD / discord + /discord )
                                      Qwen-14B-AWQ (n=143)                      Llama-3.1-8B (n=143)
                         ×20   +2.1     +3.5   +5.6   +5.6    +5.6    +5.6                            ×20    +0.0     +0.0   +0.0   ceil   ceil   ceil
                               3/0      5/0    8/0    10/2    10/2    10/2                                   0/0      0/0    0/0
                                                                                                                                                            10
                         ×10   +2.1     +3.5   +5.6   +5.6    +5.6    +5.6                            ×10    +0.0     +0.0   +0.0   ceil   ceil   ceil
                               3/0      5/0    8/0    10/2    10/2    10/2                                   0/0      0/0    0/0




Coefficient multiplier                                                       Coefficient multiplier                                                              Risk difference RD (pp)
                                                                                                                                                            5
                         ×5    +2.1     +3.5   +5.6   +8.4    +8.4    +8.4                            ×5     +0.0     +0.0   +0.0   ceil   ceil   ceil
                               3/0      5/0    8/0    14/2    14/2    14/2                                   0/0      0/0    0/0
                                                                                                                                                            0
                         ×3    +2.1     +3.5   +5.6   +10.5   +10.5   +10.5                           ×3     +0.0     +0.0   +0.0   +4.9   +4.9   +4.9
                               3/0      5/0    8/0    15/0    15/0    15/0                                   0/0      0/0    0/0    7/0    7/0    7/0
                                                                                                                                                            -5
                         ×2    +2.1     +3.5   +7.0   +9.1    +9.1    +9.1                            ×2     +0.0     +0.0   +0.0   +7.7   +7.7   +7.7
                               3/0      5/0    10/0   13/0    13/0    13/0                                   0/0      0/0    0/0    13/2   13/2   13/2
                                                                                                                                                            -10
                         ×1    +2.1     +4.2   +7.7   +7.7    +7.7    +7.7                            ×1     +0.0     +0.7   +3.5   +3.5   +3.5   +3.5
                               3/0      6/0    12/1   12/1    12/1    12/1                                   0/0      1/0    5/0    5/0    5/0    5/0

                               1%       2.5%   5%     10% 20% 100%                                           1%       2.5%   5%     10% 20% 100%
                                      MSG_ADJ_CAP (% of budget)                                                     MSG_ADJ_CAP (% of budget)

Figure 3: Behavioral heatmap: paired RD across the λ × κ grid for both traveler-
reader arms (Qwen-14B-AWQ top, Llama-3.1-8B bottom). Green box marks the deployed
Round 20 cell (λ = 1, κ = 0.05).


                                       Table 3: Grid-level max-stat permutation (primary correction).
                               Arm                             obs max RD                                    Pair p Cluster p (PRIMARY)
                               Qwen-14B +10.49pp @(×3, 10%) < 0.001                                                                               < 0.001
                               Llama-8B  +7.69pp @(×2, 10%)   0.007                                                                                 0.008


                         • Qwen: monotone-ish increasing in (λ, κ) up to (λ = 3, κ = 0.10), peak
                           +10.5pp, 15/0. Above λ = 5, mixed discord (factual begins to ceiling
                           on some pairs).

                         • Llama: non-monotone. Deployed cell marginal (+3.5pp, 5/0). Live-
                           zone peak at (λ = 2, κ = 0.10): +7.7pp, 13/2. Above λ = 3 with
                           κ ≥ 0.10, the factual template itself drives 100% acceptance (ceiling)—
                           this is the disclosure-saturated regime and is validity-excluded.

6.4. Family-wise corrected significance
    Procedure: the unit of exchangeability is the scenario cluster (88 unique
scenarios × up to 3 episode seeds, 143 pairs total). For each of 1000 per-
mutations we randomly flip orig↔fact labels within each scenario cluster

                                                                                                        18
(preserving cluster membership), recompute the 36-cell RD grid, and record
the max RD across cells. The cluster-level p is the fraction of permutations
whose max RD matches or exceeds the observed max RD. This procedure
corrects for (a) the 36 grid-cell multiplicity and (b) within-scenario correla-
tion across episode seeds and grid cells.
    Both arms pass family-wise correction under scenario-clustered
permutation. The live transmission region (λ ∈ [2, 3], κ ∈ [5%, 10%]) is not
a spurious peak; it is a robust parametric neighborhood.

6.5. Three regimes emerge
   1. Attenuated zone at λ ≤ 1, κ ≤ 5% for Llama: the rule admits the de-
      ployed +3.5pp reading but does not cross exact-McNemar significance
      at b+c=5.
   2. Live transmission region at λ ∈ [2, 3], κ ∈ [5%, 10%]: both arms
      produce significant behavioral flips with perceptual shifts of ∆fit ≈
      +0.17.
   3. Saturated zone at λ ≥ 5, κ ≥ 10% for Llama: even the factual
      template triggers 100% acceptance because Llama perceives minimum-
      disclosure prose as substantively positive.

The three-regime structure is what a binary incentive×disclosure ablation
cannot recover: a single low-vs-high κ contrast at fixed λ cannot distinguish
a live transmission region (where governance dials matter) from a saturated
regime (where the disclosure floor itself ceilings) on the Llama arm, and
cannot localize the live-region peak at (λ=2, κ=0.10) versus the deployed
point. The continuous grid is therefore an information-bearing instrument
over a binary design, not a denser re-tabulation.

7. Mechanism: What Drives Transmission?
7.1. Coefficient attribution
    Figure 4 reports a rule-level attribution holding extracted perceptions
fixed; this is not a causal mediation estimate. We do not intervene
on the perception extractor or on the underlying message content—only on
the downstream deterministic rule—so the following should be read as “which
coefficient channel carries the observed RD under the frozen rule,” not “which
perceptual construct causally mediates steering.”


                                      19
                                                         Figure 2. Coefficient attribution fit_delta is the load-bearing channel
                                                           (dotted lines = full-rule baseline; bars show max RD over 2D grid)
                                          14                                                                                                                    Qwen-14B-AWQ




Max observed RD (pp, validity-filtered)
                                                                                                                                                                Llama-3.1-8B
                                          12                                             +11.2        +11.2                                 +11.2
                                                  +10.5                                       +10.5                         +10.5
                                          10                                                                                        +9.1                +9.1

                                           8                  +7.7                                                +7.7
                                                                     +6.3
                                           6                                                                                                                         +5.6

                                           4
                                                                                                                                                                            +2.8
                                                                                +2.1
                                           2

                                           0
                                                       rule               fit               ust            risk               cy                 only                 nly
                                               Ful
                                                   l                 No                No
                                                                                          tr          No               urgen               Fit                    st o
                                                                                                                    No                                         Tru

Figure 4: Coefficient-zero attribution: max RD after setting each of the four rule coeffi-
cients to zero, recomputed over the 2D grid for each traveler-reader arm.


                                          • Removing perceived_fit_delta: Qwen max RD collapses from +10.5
                                            to +6.3pp; Llama max RD collapses from +7.7 to +2.1pp (≈ 3.7× re-
                                            duction).

                                          • Removing trust_score: both arms INCREASE in max RD (Qwen
                                            +11.2, Llama +10.5). This is because Llama reads the factual template
                                            as already high-trust; including trust in the rule raises the factual base-
                                            line’s adjustment and slightly compresses the differential.

                                          • Removing risk: small shift (+0.7pp on Qwen, unchanged on Llama)—
                                            much less than the ∼ 5.6pp fit-channel collapse.

                                          • Removing urgency: small shift (+1.4pp on Llama, unchanged on
                                            Qwen)—also small relative to the fit channel.

7.2. Baseline perception channels differ by traveler-reader backbone
    Llama’s factual-variant baseline perception on the paired n = 143 stimuli
(mean fit_delta = +0.598, mean trust = +0.824) is descriptively much higher
than Qwen’s on the same minimum-disclosure template (fit = +0.010, trust =

                                                                                                       20
                                                 Figure 3. Evidence trajectory across round-21 scale-up stages
                                           (a) Peak behavioral RD                       (b) Discordant pair counts + sample size
                                                                                                                  20.0                                         n=143
                            16                                                                                               Qwen-14B discord +                            140
                                                                                                                  17.5       Llama-8B discord +
                            14                  13.3                                                                       n=122
                                                            12.5                                                                                              15           120




Peak RD over 2D grid (pp)                                                          Discord + count at peak cell
                                                13.3                                                              15.0
                            12                                                                                                                                     13
                                                                        10.5                                                                                               100


                                                                                                                                                                                n paired (bars)
                                                                                        12.5
                                                                               10pp GO threshold
                            10
                                                                                                                                                                           80
                             8                                                                                    10.0
                                                            8.3
                                                                        7.7                                                                                                60
                             6                                                                                     7.5
                                                                                                                                       6           6n=48
                                                                                                                                           5            5                  40
                             4                                                                                     5.0

                             2                                Qwen-14B peak RD                                     2.5                  n=15                               20
                                                              Llama-8B peak RD
                             0                                                                                     0.0                                                     0
                                     v1          v2          v3          v4                                                  v1          v2          v3          v4
                                 (Phase 1b)
                                         (Round 21 scale-up)
                                                         (msgcap_v3) (msgcap_v4)                                         (Phase 1b)
                                                                                                                                 (Round 21 scale-up)
                                                                                                                                                 (msgcap_v3) (msgcap_v4)


Figure 5: Evidence trajectory across v1 (n = 122, feature-only), v2 (n = 15), v3 (n = 48),
v4 (n = 143). The effect size stabilizes at ∼ 10pp Qwen / ∼ 8pp Llama as sample size
grows, with discord counts scaling roughly linearly.


+0.873). This is a descriptive backbone difference, not a causal explanation of
transmission. But it matters for governance: a minimum-disclosure template
is not a perceptual zero-point; its position varies by traveler-reader back-
bone. Consequently, identical regulatory disclosures may produce different
welfare outcomes across user populations served by different LLM interfaces.
Per-variant (orig vs. fact) paired means on the n=143 stimuli are reported
in the shipped Phase 1c calibration files (results/phase1c_qwen14b_awq_
diag_v4_report.md and results/phase1c_llama31_8b_diag_v4_report.
md); pooled per-feature distributions (both variants combined, all 818 calls)
are in Appendix Appendix B.3, and agree with the same cross-reader pattern.

7.3. Evidence trajectory across scale-up
    Figure 5 reports peak RD and discordant counts across the pilot-to-v4
runs.

8. Discussion
8.1. What TourMart is (and is not)
    Is: an applied intelligent-system audit instrument for governance mech-
anisms over the LLM-OTA → traveler perception → welfare-rule pipeline.


                                                                                                           21
A regulator or platform can use TourMart to answer “how sensitive is this
decision rule to commission-maximizing persuasion?”
   Is not: direct evidence that real Booking.com users would be steered by
+10.5pp. The estimand is transmission through a frozen welfare rule in a
simulator, across multiple traveler backbones.

8.2. Governance implications
    The three-regime structure (attenuated / live / saturated) gives platform
operators and regulators a parametric map. Deployed rules can sit safely
in the attenuated zone (our Round 20 parameters), but the boundaries are
narrow—a single coefficient tightness × cap loosening can move a rule from
safe to steerable. This argues for governance parameter transparency
(e.g., platforms disclosing the effective λ, κ in auditable form).

8.3. Disclosure heterogeneity by user model
    Llama’s “disclosure-saturated zone” (factual text triggers 100% accep-
tance) is a cautionary calibration finding: “neutral disclosure” is not neu-
tral. Its effect on user choice depends on the user-side model/representation.
Benchmarks that evaluate disclosure floors must report paired orig-vs-factual
effects, not absolute factual acceptance. This ‘disclosure-saturated’ pattern—
where mandated transparency saturates rather than informs the recipient—
replicates in the LLM-OTA setting a finding that legal and behavioral-economics
work has documented for over a decade in human-decision settings ([58, 59]);
our contribution here is to show the same failure mode reproduces when dis-
closure is interpreted by an LLM rather than a human reader, and to locate
the threshold (λ ≥ 5, κ ≥ 10% on Llama) at which it activates in our set-
ting. A parallel heterogeneity appears on the producer side (Section 5.7, Ap-
pendix Appendix C.3): the same default SYSTEM_PROMPT under vLLM
guided JSON elicits two qualitatively different failure profiles from Qwen-
7B and Llama-3.1-8B—Qwen over-hedges (55.9% of commission responses
are refusals/hedges under the regex-based hardened refusal classifier), Llama
template-collapses (median 6 words, 80.9–84.6% internal-ID leakage). The
Llama failure is text-surface repairable by an explicit 2-sentence / 15–40-word
style-constraint suffix (Section 5.7 audit gates all pass at seeds 42 and 43,
Appendix Appendix C.3.b–c); a parallel style-suffix repair for Qwen’s hedg-
ing was not evaluated in this submission and is flagged as future work. The
producer-side heterogeneity suggests that OTA-audit regimes must specify


                                     22
which failure modes are monitored rather than assuming a single text-quality
metric suffices.

9. Limitations
  1. Simulator scope: the welfare rule is stylized; real travelers integrate
     information across multiple touches (comparisons, reviews, price his-
     tory) and engage in multi-turn refinement and feedback loops that
     TourMart does not model.
  2. Single OTA family for primary results: our Phase 1c paired replay
     uses Qwen-7B-Instruct as the OTA backbone. We attempted two addi-
     tional families. Mistral-7B-Instruct-v0.3 failed the 85% JSON-validity
     gate under our vLLM structured-output config and was deferred.
     Llama-3.1-8B-Instruct passed JSON validity and bundle-id coverage
     but failed three content gates under the default SYSTEM_PROMPT
     (word-count median = 6, unique-success ratio = 4.0%–12.5%, internal-
     ID leakage = 80.9%–84.6%), a template-collapse pattern that replicated
     across two sampling seeds (42, 43) and was not explained by batch
     size (Section 5.7, Appendix Appendix C.3). The collapse was repaired
     at the audit-gate level by an explicit 2-sentence / 15–40-word style-
     constraint suffix appended to the SYSTEM_PROMPT, but the full
     143-episode paired steering replay under the repaired prompt was not
     run in this submission. We therefore frame the Llama-OTA result as a
     prompt-sensitivity finding for the OTA-language surface, not a
     cross-family robustness claim for TourMart’s main steering estimands.
  3. Two traveler families only: Gemma-2-9B, GPT-4o-mini, and other
     traveler backbones are not evaluated here.
  4. Near-threshold window selection and conditional estimand:
     we test the region where the welfare rule is mechanically flippable.
     Pairs with baseline well above or below τ · bt are deterministically ac-
     cepted/rejected; the phase diagram characterizes the marginal regime.
     More fundamentally, the paired replay identifies message transmission
     conditional on the OTA’s recommended bundle set; it does not
     estimate total platform steering from the joint bundle-selection-plus-
     message policy.
  5. LLM-extracted perception features and “bundle fit” construct
     validity: the traveler’s perception is itself generated by an LLM.
     This is a fundamental constraint of LLM-agent simulators; we do not

                                    23
   claim population-level generalization to humans. It also leaves open
   a construct-validity concern for Section 7: the perceived_fit_delta
   channel may, in part, be the LLM’s default encoding of whatever per-
   suasive signal it received into the coefficient with the largest down-
   stream weight. Human-annotated fit validation on a stratified subset
   of messages and a fit-language-removal counterfactual (planned as fu-
   ture work) are the strongest mitigations.
6. Small-discordance and small-stratum power: headline effects rest
   on small numbers of discordant pairs (Qwen 12/1, Llama 5/0 out of
   143 each) and small per-signal-strength strata (n = 42–55). Exact
   McNemar is conservative at small b+c; in particular the Llama-reader
   deployed p = 0.0625 is the smallest possible two-sided exact p-value
   at b+c=5. The B.1 supplemental extended-n replay (§6.1) directly
   addresses this caveat for the Llama arm: at n=270 in the diagnostic
   window, b+c=8 clears the floor and yields exact p=0.008, ruling out
   under-power as the explanation for the deployed p=0.0625. Grid-level
   max-RD peaks (Qwen 15/0, Llama 13/2) are also small-count effects.
   We treat the 88 unique scenario clusters as the exchangeable unit in
   the permutation test; shared bundle-generator seeds, shared traveler-
   archetype templates, and shared market-generator draws across episode
   seeds may induce residual dependence that 88 clusters underweight,
   which we cannot fully rule out without independently generated sce-
   narios. We report exact tests and estimation intervals separately and
   use the pre-registered exact test as the significance decision; subgroup
   claims (e.g., w=0.75 McNemar p=0.0078) are reported as exploratory
   within the corrected primary test.
7. Audit-gate operational caveats: excluding Mistral-7B and default-
   prompt Llama-3.1-8B from the paired steering replay conditions the
   audit instrument on the OTA passing the six-gate audit. This is the
   correct operational choice for a text-in-the-loop instrument but limits
   claims about OTA models “in the wild” whose deployment pipeline
   may not enforce the same gates. The refusal classifier is regex-based: a
   triage signal, not a semantic quality guarantee, with both false positives
   (a legitimate refusal that uses a non-matching phrase is missed) and
   false negatives (a recommendation that happens to contain a hedging
   substring is flagged). Two of the six audit-gate thresholds were widened
   after the Qwen baseline failure profile was observed—the word-count
   median window from [30, 200] to [10, 200] and the refusal cutoff from

                                   24
     10% to 20% (Appendix D.3); to our knowledge no widely-cited dark-
     pattern or refusal benchmark fixes a 20% refusal cutoff, so the choice
     is a TourMart-internal documentation threshold. The widening did
     not move any arm from fail to pass: Qwen still fails the looser 20%
     refusal gate at 55.9%, and Llama still fails three content gates under
     the default prompt.
  8. Pre-registered decision rule = frozen: the Round 20 coefficients
     were chosen deliberately to sit in the attenuated regime. The phase
     diagram shows what happens if the rule drifts; it does not prove any
     specific (λ, κ) is the “right” choice, and we offer no external calibration
     for the deployed point beyond the validity gates.
  9. λ–⃗c identification: under the deployed coefficient vector ⃗c =
     (0.03, 0.015, −0.025, 0.01), the gain dial λ is identified as a multiplica-
     tive deviation from the baseline rule. Under a free ⃗c the composition
     λ⃗c is only identified up to a positive scalar, so λ alone would be a
     normalization artifact; we therefore treat the deployed ⃗c as part of
     the welfare-rule specification, not a free hyperparameter. Audits of
     platforms with a different welfare rule must restate their ⃗c to make
     λ-readings comparable across deployments.

10. Conclusion
    We introduced TourMart, a parametric audit instrument for measuring
LLM-OTA commission-steering under disclosure governance. With n = 143
paired near-threshold same-bundle replays across two traveler-reader back-
bones, we demonstrated scenario-clustered family-wise-corrected behavioral
steering (+10.49pp Qwen-reader, +7.69pp Llama-reader peak RD), charac-
terized a three-regime transmission phase diagram, and, under coefficient-
zero attribution holding extracted perceptions fixed, found that the perceived-
fit channel carries most of the observed max-RD signal. TourMart’s contri-
bution is operational: it lets regulators and platform operators characterize
the steering susceptibility of a proposed decision rule, and it surfaces the non-
trivial fact that minimum-disclosure templates are not perceptual zero points
across user-side model families. We release the audit instrument, benchmark
scenarios, welfare-rule ablation code, four symmetric OTA-text audit reports,
and all paired raw traveler outputs to support reproduction and extension.



                                       25
Ethics Statement
    Dual-use considerations. TourMart is a governance-audit benchmark:
it measures when commission-maximizing OTA messages transmit into traveler-
agent decisions, and which governance parameters attenuate transmission.
The same instrument could in principle be used to develop a more effective
commission-maximizing OTA by treating the steering RD as a training re-
ward. We mitigate this by (i) publishing the governance-parameter phase
diagram that attenuates steering alongside every positive result, (ii) releas-
ing the symmetric OTA text-audit protocol and hardened refusal classifier
that flag manipulative prose, and (iii) framing release language to platform
operators, regulators, and consumer-protection researchers rather than to
OTA developers seeking optimization targets. The net direction of the re-
lease is therefore audit-enabling rather than manipulation-enabling: an OTA
developer already has better signals (real CTR, booking revenue) than our
simulator provides, whereas a regulator does not currently have a standard-
ized audit instrument.
    Human subjects. No human subjects participated in this study. All
traveler-side perception judgments are LLM-generated through guided-JSON
calls to Qwen-14B-AWQ and Llama-3.1-8B. No user data, browsing traces, or
personally identifiable information from real OTA platforms is used, stored,
or released.
    Synthetic market data. All bundle prices, commission rates, ho-
tel/airline inventories, traveler profiles, and vibe archetypes are generated
by the simulator’s generate_small_market function with fixed seeds; they
do not correspond to, and cannot be reverse-mapped to, any real OTA’s
inventory or pricing.
    Alignment with regulatory instruments. The benchmark is de-
signed to produce audit evidence compatible with EU DSA Article 26(3)
(transparency of recommender parameters), FTC 16 CFR Part 255 (en-
dorsement / commercial-relationship disclosure), and MiFID II Article 27
(best-execution-style disclosure). We do not claim regulatory certification;
we provide a reproducible measurement instrument that these frameworks’
compliance-evaluation regimes may adopt or contest.
    Model licensing and provenance. Qwen2.5-7B-Instruct and Qwen2.5-
14B-Instruct-AWQ are used under the Tongyi Qianwen license; Llama-3.1-
8B-Instruct is used under the Meta Llama 3.1 Community License. AWQ
weights are consumed as distributed via vLLM awq_marlin. We report model

                                    26
versions, commit hashes, and inference configurations in the Reproducibility
Statement below.
   Pre-registration and audit integrity. The six-gate thresholds and
the regex v2 hardened refusal classifier were frozen prior to the Llama-OTA
candidate audit (Section 5.7) to avoid selective-threshold criticism. Source
markdown for every audit decision is released with the code.

Reproducibility Statement
    Release. TourMart is released at github.com/usmliuyao/tourmart
and archived at Zenodo (DOI: 10.5281/zenodo.19709369) under MIT (code)
and CC-BY-4.0 (generated data and audit outputs). The release contains
the market generator with all seeds used in this paper, the Qwen-7B OTA
msgcap pipeline (v4 frozen commit), the paired Phase 1c replay for both
traveler-reader arms, the 36-cell phase-diagram sweep, the six-gate symmet-
ric audit and regex v2 refusal classifier, paired raw traveler outputs with
extracted perception features, and the four audit markdown reports refer-
enced in Appendix Appendix C.3.
    Environment and pre-registration. The OTA producer is Qwen2.5-
7B-Instruct (bf16, vLLM with guided JSON over a per-market bundle_id
enum); the traveler-reader backbones are Qwen2.5-14B-Instruct-AWQ and
Llama-3.1-8B-Instruct (bf16), both with guided JSON for the four percep-
tion features. All experiments run on a single RTX 3090 24 GB. Primary
sampling seed is 42, with cross-seed replication at 43 for the OTA-audit. The
Round 20 welfare-rule coefficients, the near-threshold window, the six-gate
thresholds, and the regex v2 refusal classifier were frozen before the Llama-
OTA candidate audit was run; the timestamped pre-registration is included
in Appendix Appendix D.
    One-shot reproduction. A single shell script in the release re-runs the
n = 143 paired replay for both arms and regenerates Table 1, Table 3, and
Figures 3–5 from cached perceptions in well under one GPU-hour; a determin-
istic flag pins vLLM seeds to reproduce reported numbers within rounding.
The statistical pipeline (McNemar exact tests, 95% RD CIs, Holm-corrected
feature-level Wilcoxons, and the 1000-permutation scenario-clustered max-
stat procedure) and the six-gate audit are documented submodules with unit
tests, both rerunnable from the released cached outputs.




                                     27
CRediT Author Statement
    Yao Liu: Conceptualization, Methodology, Software, Validation, Formal
analysis, Investigation, Resources, Data Curation, Writing—Original Draft,
Writing—Review & Editing, Visualization, Supervision, Project administra-
tion, Funding acquisition.

Declaration of Competing Interests
   The authors declare no competing interests.

Data Availability
    The TourMart benchmark, all synthetic market scenarios (generated by
generate_small_market with fixed seeds), the 818 raw traveler-LLM call
rows per arm (which collapse via the 3-tuple (scenario_id, traveler_id,
bundle_id) key to 143 paired traveler-LLM outputs with extracted per-
ception features, the four OTA audit markdown reports, and all statistical
analysis code are available at https://github.com/usmliuyao/tourmart
and archived at Zenodo (DOI: 10.5281/zenodo.19709369) under MIT (code)
and CC-BY-4.0 (generated data and audit outputs). A self-contained repro-
ducibility package under reproducibility/ ships pre-computed permuta-
tion null distributions and a reproduce_all.sh master runner that regener-
ates all headline numbers (Table 1, Table 2, Figs. 1–3) from the paired raw
outputs on a standard CPU in under 10 minutes, with no GPU required.
SHA-256 checksums for all input data files are embedded in verify.py. No
proprietary data, human-subject data, or real OTA inventory data are used
in this study.

Appendix A. Extended reproducibility notes
   • Code: github.com/usmliuyao/tourmart (Zenodo DOI 10.5281/zen-
     odo.19709369).
   • Commit hash: [frozen v4].
   • GPU: 1× RTX 3090 24 GB (Server B); Llama-OTA seed-43 chain also
     on Server B.
   • Additional runtimes: seed-43 msgcap + audit ≈ 51 min; batch-size
     confound check (b32 + b128) ≈ 8 min.

                                    28
                     Table B.4: Symmetric audit gates and rationale.
      Gate                              Threshold      Rationale
      JSON validity                       ≥ 85%        structured-output survival
      Bundle_id coverage                  ≥ 80%        bundle identifier in schema slot
      Msg word-count median              [10, 200]     excludes refusals and schema-blob
                                                       overflow
      Refusal rate                       ≤ 20%         OTA must produce commission
                                                       prose
      Unique-msg ratio (success)         ≥ 30%         template-collapse detection
      Internal-ID leakage                ≤ 20%         bid/bundle tokens in user-facing
                                                       text


Table B.5: Audit gate outcomes per arm (bolded cells are sub-threshold). Verdict abbre-
viations: ref =refusal, wc=word-count, uq=uniqueness, lk =ID-leak.
  Arm                          JSON     Bundle    wc   Refusal     Uniq   ID-leak   Verdict
  Qwen msgcap v4 (s42)         100.0%   91.3%   23     55.9% 74.1%          0.0%    FAIL: ref
  Llama v6 default (s42)       100.0%   91.7%    6       8.0%  4.0%       84.6%     FAIL: wc/uq/lk
  Llama default (s43)           99.3%   91.3%    6       8.5% 12.5%       80.9%     FAIL: wc/uq/lk
  Llama probe (s43, verbose)   100.0%   87.0%   21      13.0% 97.9%         3.7%    PASS
  Llama probe (s42, b=32)      100.0%   88.9% 22.5      13.0% 97.9%         3.7%    PASS
  Llama probe (s42, b=128)     100.0%   88.9%   23      13.0% 97.9%         0.0%    PASS



Appendix B. Validity-gate detail
B.1 Stimulus-audit gates (locked symmetric audit protocol)
   The six audit gates applied symmetrically to each OTA-candidate msgcap
under the regex-based hardened refusal classifier v2:
   Gate outcomes by arm:
   Source markdowns: results/msgcap_v7_v6_vs_qwen_regex_v2.md, results/
msgcap_v7_seed43_default_vs_v6.md, results/msgcap_v7_seed43_probe_
vs_seed43_default.md, results/msgcap_v7_batch128_vs_batch32.md.

B.2 Phase 1c calibration diagnostics (per traveler-reader arm, v4)
    Under the deployed governance point (λ = 1, κ = 0.05) and the diagnostic
near-threshold window [τ · b − 10% · b, τ · b + 5% · b], with 818 traveler calls per
arm yielding 143 paired near-threshold episodes (identical scenario sampling
across arms):
    No MSG_ADJ cap-hit is observed at the deployed cap κ = 0.05 under
either reader. Cap-hit rates at larger κ multipliers are recovered from the 2D


                                                 29
Table B.6: Phase 1c calibration diagnostics per traveler-reader arm. Parse and cap-hit are
0/818 missing for both arms; 818 calls per arm.
            Arm               Parse Fact acc Cap-hit      n         orig / fact
            Qwen-14B-AWQ 100%         48.95%       0% 143 56.64% / 48.95%
            Llama-3.1-8B 100%         60.84%       0% 143 64.34% / 60.84%


         Table B.7: Per-feature distributions (mean, std, saturation |v| ≥ 0.99).
       Feature                 Qwen-14B reader                Llama-3.1-8B reader
       perceived_fit_delta     +0.070 (0.242, 3.5%)           +0.710 (0.147, 0.5%)
       perceived_risk          +0.013 (0.079, 0.5%)           +0.201 (0.025, 0.0%)
       trust_score             +0.938 (0.229, 89.9%)          +0.857 (0.058, 0.0%)
       urgency_felt            +0.021 (0.105, 0.2%)           +0.497 (0.087, 0.0%)


sensitivity grid (Appendix Appendix C.1): hits emerge only in the saturated
regime (κ ∈ {20%, 100%}) where the transmission effect plateaus.

B.3 Per-feature distributions at the deployed point
    Welfare-rule input features (all 818 calls per arm, both message variants
pooled):
    Saturation warning (Qwen trust_score, 89.9% at the upper ceil-
ing) is flagged as a construct-validity limitation (Section 9 item 5 and Sec-
tion 7.2): the Qwen-reader trust channel is near-degenerate at the deployed
point, which is one reason the dominant attributable channel in Figure 4
is perceived fit rather than trust. The Llama reader shows no ceiling satu-
ration; its distributions are tighter and off-center. These cross-reader base-
line shifts—not interventions on any backbone—are the quantitative form of
Section 7.2’s statement that “baseline perception channels differ by traveler-
reader backbone.”

B.4 What the gates do NOT guarantee
    The audit gates certify benchmark eligibility—that the OTA-candidate’s
msgcap is informative enough to drive a transmission analysis. They do not
certify:

    • ecological realism of message style (deferred to marketing-team user
      study, future work);

                                           30
   • absence of steganographic or subtle-persuasion channels the regex does
     not recognize (Section 9 item 6);
   • that the deployed point (λ = 1, κ = 0.05) is optimal for any stake-
     holder; this is the governance default, swept by the phase diagram in
     Section 6.1.

Appendix C. Offline sensitivity analyses
C.1 2D cap × coef_multiplier grid (Fig 1)
   See Figure 3.

C.2 Coefficient attribution (Fig 2)
    See Figure 4. Holm-corrected exploratory feature-level deltas are reported
in the released supplementary material.

C.3 Llama-OTA cross-seed and batch-size checks
    Four symmetric-stimulus audits under the Llama-3.1-8B-Instruct OTA
candidate:
    (a) Failure-replication across sampling seeds. Llama default at
seed 43 vs. Llama default at seed 42 (v6): the template-collapse pattern
replicates (both FAIL wc-median, success-only uniqueness, and internal-ID
leakage with near-identical numbers; the top success message is identical
across seeds).
    (b) Seed-43 style-suffix repair. Llama default vs. Llama probe (VER-
BOSE_PROBE_SUFFIX) at seed 43: the three failing gates are restored
(wc median 6 → 21, unique-success 12.5% → 97.9%, internal-ID leakage
80.9% → 3.7%); the three originally-passing gates (JSON validity, bundle-id
coverage, refusal rate) remain above threshold (100%, 87.0%, 13.0% respec-
tively).
    (c) Seed-42 style-suffix repair + batch-size confound check. Llama
probe at batch=32 vs. Llama probe at batch=128, both at seed 42: all
six gates PASS in both batch conditions (wc median 22/23, unique-success
97.9%/97.9%, internal-ID leakage 3.7%/0.0%; the three originally-passing
gates also pass), establishing simultaneously that the suffix repair replicates
at seed 42 AND that batch size does not confound the prompt effect.
    (d) Producer-side cross-backbone failure-profile comparison. Qwen-
7B default (Qwen v4) vs. Llama-3.1-8B default (Llama v6) under the regex-
based hardened refusal classifier: two distinct failure profiles—Qwen refusal

                                     31
rate 55.9% (fails the ≤ 20% refusal gate), Llama internal-ID leakage 84.6%
(fails the ≤ 20% leakage gate).
    Source markdowns: msgcap_v7_seed43_default_vs_v6.md, msgcap_v7_
seed43_probe_vs_seed43_default.md, msgcap_v7_batch128_vs_batch32.
md, msgcap_v7_v6_vs_qwen_regex_v2.md. Full analysis in refine-logs/
PHASE1C_SECTION_5_3_FINDING.md.

Appendix D. Full pre-registration document (v6 Llama-OTA au-
            dit)
    Reproduced below, unedited except for formatting, from refine-logs/
PHASE1C_V6_LLAMA_OTA_PREREG.md, frozen 2026-04-20 before the Llama-
OTA chain launched on Server B. This is the pre-registration for the
Section 5.7 / Appendix Appendix C.3 Llama-OTA candidate au-
dit only; the Round 20 v4 welfare-rule coefficients, near-threshold window,
primary paired-endpoint estimand, and 2D phase-diagram sweep plan (Sec-
tion 3.4, Section 5.3, Section 5.5) were frozen in a separate earlier pre-
registration at Round 20 and are reproduced in refine-logs/ROUND_21_
FINAL.md and the locked-config file configs/round20_v4.yaml.

D.1 Hypothesis
    The v4 transmission phase diagram (three regimes—attenuated / live /
saturated; peak +10.49pp under Qwen-14B reader, +7.69pp under Llama-
3.1-8B reader) is hypothesized to be a property of commission-maximizing
LLM-OTA prose in general, not an artifact of Qwen-7B as OTA backbone;
the Llama-OTA replay specified in D.2–D.5 is the pre-registered test of this
hypothesis.

D.2 Estimands
   • Primary (off-diagonal, cross-family): Llama-OTA → Qwen-14B-
     AWQ reader at deployed (λ = 1, κ = 0.05): paired risk difference of
     accept rate between commission prose and factual template.

   • Secondary (diagonal): Llama-OTA → Llama-3.1-8B reader at the
     same point, same estimand. Pre-registered as lower-weight evidence
     because of the same-family instruction-following prior.




                                    32
D.3 Audit gates (frozen before generation)
    See Appendix Appendix B.1 for the six gates. Each gate is identical to
v5 (the deleted Mistral attempt) except for two deliberate loosenings post-
v5: the wc median threshold was widened from [30, 200] to [10, 200] after
inspection confirmed 10–30-word single-sentence replies are informative; the
refusal gate was raised from 10% to 20% after the Qwen baseline itself landed
at 55.9% under the hardened regex v2 (documenting template collapse vs.
over-hedging as two distinct failure profiles). All gate changes were applied
symmetrically to every arm and re-audited from raw msgcap output; no arm
was tuned retroactively to pass. We are not aware of a widely-cited dark-
pattern or refusal benchmark that fixes a 20% refusal cutoff, so the widened
thresholds are TourMart-internal documentation choices, not community-
standard cutoffs; we discuss the audit-integrity implications in §9 (item 13).

D.4 Decision rules (frozen, applied verbatim)
   • Off-diagonal RD same sign and within 50% of v4 → “cross-family gen-
     eralization confirmed.”

   • Off-diagonal null or wrong-sign at both deployed and peak → “cross-
     family dependence; report as model-pair-specific.”

   • Primary passes, secondary fails → report 2 × 2 mixed; avoid factorial-
     confirmation language.

   • Both pass → factorial confirmation (not the realized outcome; the
     Llama-reader deployed cell has five discordant pairs with an exact Mc-
     Nemar minimum two-sided p = 0.0625).

D.5 Failure protocol (frozen)
   • JSON validity < 85% → chain stops before traveler replay. No post-hoc
     tuning, no fallback to a third OTA model in this submission.

   • Pre-reg-violating configurations (timeout, OOM, sampler drift) → abort,
     mark .chain_v6_failed_*, re-pre-register before re-attempting.




                                     33
D.6 Prior-attempt disclosure
    v5 attempted Mistral-7B-Instruct-v0.3 as the OTA candidate. msgcap
produced ∼25% JSON validity under identical vLLM guided-JSON config
(vs. Qwen v4 100%, Llama v6 100%). The pre-registered validity gate (D.3
item 1, < 85% JSON validity → abort) killed the chain before traveler replay.
No v5 traveler data exists; no v5 figure was drawn; no v5 number entered the
paper. Scripts are retained for reproducibility (chain_runner_phase1c_v5_
mistral.sh, run_stimulus_audit_v5.py). Raw artifacts (∼30 MB jsonl
+ model weights) were deleted per the frozen failure protocol (D.5 item 2,
“abort and mark .chain_v6_failed_*”) to reclaim disk; the failure-decision
record is preserved in git history and in this appendix.

D.7 Out of scope for this submission
   • Additional (λ, κ) cells beyond the deployed point and the v4 sweep
     grid under the Llama-OTA condition (secondary analyses only, not
     pre-registered).

   • OTA families beyond Qwen and Llama (no Gemma, no GPT-4o-mini).

   • Changes to traveler-reader parameters between v4 and v6.

   • Human-subject evaluation of message ecological validity (deferred to
     marketing-team post-submission user study).

   • A parallel style-suffix repair for Qwen’s over-hedging failure profile
     (flagged as future work; Claim 2 is stated only for Llama’s template-
     collapse profile).

References
 [1] Federal Trade Commission, Guides concerning the use of endorsements
     and testimonials in advertising, 16 CFR part 255, https://www.ecfr.
     gov/current/title-16/chapter-I/subchapter-B/part-255, final
     rule effective July 26, 2023; 88 FR 48092 (July 2023).

 [2] European Parliament and Council, Regulation (EU) 2022/2065 on a
     single market for digital services (digital services act), Official Journal
     of the European Union L 277/1 (October 2022).



                                      34
 [3] G. Aridor, D. Gonçalves, Recommenders’ originals: The welfare effects
     of the dual role of platforms as producers and recommender systems,
     International Journal of Industrial Organization 83 (2022) 102845. doi:
     10.1016/j.ijindorg.2022.102845.

 [4] C. M. Gray, Y. Kou, B. Battles, J. Hoggatt, A. L. Toombs, The
     dark (patterns) side of UX design, in: Proceedings of the 2018 CHI
     Conference on Human Factors in Computing Systems (CHI), 2018.
     doi:10.1145/3173574.3174108.

 [5] C. M. Gray, C. T. Santos, N. Bielova, T. Mildner, An ontology of
     dark patterns knowledge: Foundations, definitions, and a pathway for
     shared knowledge-building, in: Proceedings of the 2024 CHI Confer-
     ence on Human Factors in Computing Systems (CHI), 2024. doi:
     10.1145/3613904.3642436.

 [6] A. Mathur, G. Acar, M. J. Friedman, E. Lucherini, J. Mayer, M. Chetty,
     A. Narayanan, Dark patterns at scale: Findings from a crawl of 11k
     shopping websites, Proceedings of the ACM on Human-Computer In-
     teraction 3 (CSCW) (2019). doi:10.1145/3359183.

 [7] European Parliament and Council, Directive 2014/65/EU (mifid ii), ar-
     ticle 27: Obligation to execute orders on terms most favourable to the
     client, Official Journal of the European Union L 173/349 (2014).

 [8] European Parliament and Council, Regulation (EU) 2019/1150 of the
     european parliament and of the council of 20 june 2019 on promoting
     fairness and transparency for business users of online intermediation
     services, Official Journal of the European Union L 186/57 (July 2019).

 [9] Cyberspace Administration of China and Ministry of Industry and In-
     formation Technology and Ministry of Public Security and State Admin-
     istration for Market Regulation, Provisions on the administration of al-
     gorithmic recommendations of internet information services (CAC order
     no. 9), http://www.cac.gov.cn/2022-01/04/c_1642894606364259.
     htm, effective 2022-03-01; in force when this paper was prepared (March
     2022).

[10] J. S. Park, J. O’Brien, C. J. Cai, M. R. Morris, P. Liang, M. S. Bern-
     stein, Generative agents: Interactive simulacra of human behavior, in:

                                     35
    Proceedings of the 36th Annual ACM Symposium on User Interface
    Software and Technology (UIST), 2023.

[11] J. J. Horton, A. Filippas, B. S. Manning, Large language models as
     simulated economic agents: What can we learn from Homo Silicus?,
     NBER Working Paper 31122, National Bureau of Economic Research
     (2023). doi:10.3386/w31122.

[12] L. P. Argyle, E. C. Busby, N. Fulda, J. R. Gubler, C. Rytting,
     D. Wingate, Out of one, many: Using language models to simu-
     late human samples, Political Analysis 31 (3) (2023) 337–351. doi:
     10.1017/pan.2023.2.

[13] F. Salvi, M. Horta Ribeiro, R. Gallotti, R. West, On the conversational
     persuasiveness of GPT-4, Nature Human Behaviour 9 (2025) 1645–1653.
     doi:10.1038/s41562-025-02194-6.

[14] F. Salvi, A. Cuevas, M. Horta Ribeiro, Commercial persuasion in
     AI-mediated conversations, arXiv preprint arXiv:2604.04263 (2026).
     arXiv:2604.04263.

[15] G. Bansal, W. Hua, Z. Huang, A. Fourney, A. Swearngin, W. Epperson,
     T. Payne, J. M. Hofman, B. Lucier, C. Singh, M. Mobius, A. Nambi,
     A. Yadav, K. Gao, D. M. Rothschild, A. Slivkins, D. G. Goldstein,
     H. Mozannar, N. Immorlica, M. Murad, M. Vogel, S. Kambhampati,
     E. Horvitz, S. Amershi, Magentic marketplace: An open-source envi-
     ronment for studying agentic markets, arXiv preprint arXiv:2510.25779
     (2025). arXiv:2510.25779.

[16] C. Sandvig, K. Hamilton, K. Karahalios, C. Langbort, Auditing algo-
     rithms: Research methods for detecting discrimination on internet plat-
     forms, in: 64th Annual Meeting of the International Communication
     Association (ICA), Data and Discrimination Preconference, 2014.

[17] A. Hannak, P. Sapiezynski, A. Molavi Kakhki, B. Krishnamurthy,
     D. Lazer, A. Mislove, C. Wilson, Measuring personalization of web
     search, in: Proceedings of the 22nd International Conference on World
     Wide Web (WWW), ACM, 2013, pp. 527–538. doi:10.1145/2488388.
     2488435.


                                    36
[18] D. Metaxa, J. S. Park, R. E. Robertson, K. Karahalios, C. Wil-
     son, J. Hancock, C. Sandvig, Auditing algorithms: Understanding al-
     gorithmic systems from the outside in, Foundations and Trends in
     Human-Computer Interaction 14 (4) (2021) 272–344. doi:10.1561/
     1100000083.

[19] W. G. Kim, S. Pillai, K. Haldorai, W. Ahmad, Dark patterns used by
     online travel agency websites, Annals of Tourism Research 88 (2021)
     103055. doi:10.1016/j.annals.2020.103055.

[20] E. Kran, H. M. Nguyen, A. Kundu, S. Jawhar, J. Park, M. M. Ju-
     rewicz, DarkBench: Benchmarking dark patterns in large language mod-
     els, in: International Conference on Learning Representations (ICLR),
     Oral, 2025. arXiv:2503.10728.

[21] H. Wu, B. Mitra, C. Ma, F. Diaz, X. Liu, Joint multisided exposure
     fairness for recommendation, in: Proceedings of the 45th International
     ACM SIGIR Conference on Research and Development in Information
     Retrieval (SIGIR), ACM, 2022, pp. 703–714. doi:10.1145/3477495.
     3532007.

[22] Federal  Trade   Commission,   Bringing    dark   patterns to
     light:   FTC staff report,      https://www.ftc.gov/reports/
     bringing-dark-patterns-light, p214800 (September 2022).

[23] U. Reviglio, M. Fabbri, The regulation of recommender systems under
     the DSA: A transition from default to multiple and dynamic controls?,
     DSA Observatory Policy Analysis (November 2024).

[24] J. Xie, K. Zhang, J. Chen, T. Zhu, R. Lou, Y. Tian, Y. Xiao, Y. Su, Trav-
     elPlanner: A benchmark for real-world planning with language agents,
     in: Proceedings of the 41st International Conference on Machine Learn-
     ing (ICML), Spotlight, 2024. arXiv:2402.01622.

[25] S. Chaudhuri, P. Purkar, R. Raghav, S. Mallick, M. Gupta, A. Jana,
     S. Ghosh, TripCraft: A benchmark for spatio-temporally fine grained
     travel planning, arXiv preprint arXiv:2502.20508 (2025). arXiv:2502.
     20508.




                                     37
[26] Y. Qu, H. Xiao, F. Li, G. Li, H. Zhou, X. Dai, X. Dai, TripScore: Bench-
     marking and rewarding real-world travel planning with fine-grained eval-
     uation, arXiv preprint arXiv:2510.09011 (2025). arXiv:2510.09011.

[27] X. Cheng, Y. Hu, X. Zhang, L. Xu, L. Tan, Z. Pan, X. Li, Y. Liu,
     Beyond itinerary planning—a real-world benchmark for multi-turn and
     tool-using travel tasks, arXiv preprint arXiv:2512.22673 (2025). arXiv:
     2512.22673.

[28] D. Yang, et al., Wide-horizon thinking and simulation-based evaluation
     for real-world LLM planning with multifaceted constraints, in: Advances
     in Neural Information Processing Systems (NeurIPS), 2025. arXiv:
     2506.12421.

[29] A. Chen, X. Ge, Z. Fu, Y. Xiao, J. Chen, TravelAgent: An AI assis-
     tant for personalized travel planning, arXiv preprint arXiv:2409.08069
     (2024).

[30] Q. Wu, G. Bansal, J. Zhang, Y. Wu, B. Li, E. Zhu, L. Jiang, X. Zhang,
     S. Zhang, J. Liu, A. H. Awadallah, R. W. White, D. Burger, C. Wang,
     AutoGen: Enabling next-gen LLM applications via multi-agent conver-
     sations, in: Conference on Language Modeling (COLM), 2024. arXiv:
     2308.08155.

[31] G. Li, H. A. A. K. Hammoud, H. Itani, D. Khizbullin, B. Ghanem,
     CAMEL: Communicative agents for “mind” exploration of large language
     model society, in: Advances in Neural Information Processing Systems
     (NeurIPS), 2023.

[32] S. Hong, M. Zhuge, J. Chen, X. Zheng, Y. Cheng, C. Zhang, J. Wang,
     Z. Wang, S. K. S. Yau, Z. Lin, L. Zhou, C. Ran, L. Xiao, C. Wu,
     J. Schmidhuber, MetaGPT: Meta programming for a multi-agent col-
     laborative framework, in: International Conference on Learning Repre-
     sentations (ICLR), Oral, 2024. arXiv:2308.00352.

[33] W. Chen, Y. Su, J. Zuo, C. Yang, C. Yuan, C.-M. Chan, H. Yu, Y. Lu,
     Y.-H. Hung, C. Qian, et al., AgentVerse: Facilitating multi-agent collab-
     oration and exploring emergent behaviors, in: International Conference
     on Learning Representations (ICLR), 2024.


                                     38
[34] X. Zhou, H. Zhu, L. Mathur, R. Zhang, H. Yu, Z. Qi, L.-P. Morency,
     Y. Bisk, D. Fried, G. Neubig, M. Sap, SOTOPIA: Interactive evaluation
     for social intelligence in language agents, in: International Conference
     on Learning Representations (ICLR), Spotlight, 2024.

[35] G. Piatti, Z. Jin, M. Kleiman-Weiner, B. Schölkopf, M. Sachan, R. Mi-
     halcea, Cooperate or collapse: Emergence of sustainable cooperation in
     a society of LLM agents, in: Advances in Neural Information Processing
     Systems (NeurIPS), 2024.

[36] S. Abdelnabi, A. Gomaa, S. Sivaprasad, L. Schönherr, M. Fritz, Coop-
     eration, competition, and maliciousness: LLM-stakeholders interactive
     negotiation, in: Advances in Neural Information Processing Systems
     (NeurIPS) Datasets and Benchmarks Track, 2024.

[37] N. Li, C. Gao, M. Li, Y. Li, Q. Liao, EconAgent: Large language model-
     empowered agents for simulating macroeconomic activities, in: Proceed-
     ings of the 62nd Annual Meeting of the Association for Computational
     Linguistics (ACL), 2024.

[38] Q. Zhao, J. Wang, Y. Zhang, Y. Jin, K. Zhu, H. Chen, X. Xie, Com-
     peteAI: Understanding the competition dynamics of large language
     model-based agents, in: Proceedings of the 41st International Confer-
     ence on Machine Learning (ICML), Oral, 2024.

[39] L. Wang, J. Zhang, H. Yang, Z. Chen, J. Tang, Z. Zhang, X. Chen,
     Y. Lin, R. Song, W. X. Zhao, J. Xu, Z. Dou, J. Wang, J.-R. Wen, User
     behavior simulation with large language model-based agents for recom-
     mender systems, ACM Transactions on Information Systems (TOIS)
     (2025).

[40] G. V. Aher, R. I. Arriaga, A. T. Kalai, Using large language models
     to simulate multiple humans and replicate human subject studies, in:
     Proceedings of the 40th International Conference on Machine Learning
     (ICML), 2023.

[41] X. Liu, H. Yu, H. Zhang, Y. Xu, X. Lei, H. Lai, Y. Gu, H. Ding, K. Men,
     K. Yang, et al., AgentBench: Evaluating LLMs as agents, in: Interna-
     tional Conference on Learning Representations (ICLR), 2024.


                                     39
[42] C. Ma, J. Zhang, Z. Zhu, C. Yang, Y. Yang, Y. Jin, Z. Lan, L. Kong,
     J. He, AgentBoard: An analytical evaluation board of multi-turn
     LLM agents, in: Advances in Neural Information Processing Systems
     (NeurIPS) Datasets and Benchmarks Track, 2024.
[43] M. Sharma, M. Tong, T. Korbak, D. Duvenaud, A. Askell, S. R.
     Bowman, N. Cheng, E. Durmus, Z. Hatfield-Dodds, S. R. John-
     ston, S. Kravec, T. Maxwell, S. McCandlish, K. Ndousse, O. Rausch,
     N. Schiefer, D. Yan, M. Zhang, E. Perez, Towards understanding syco-
     phancy in language models, in: International Conference on Learning
     Representations (ICLR), 2024. arXiv:2310.13548.
[44] A. Fanous, J. Goldberg, A. Agarwal, J. Lin, A. Zhou, S. Xu, V. Bikia,
     R. Daneshjou, S. Koyejo, SycEval: Evaluating LLM sycophancy, in:
     Proceedings of the AAAI/ACM Conference on AI, Ethics, and Society
     (AIES), Vol. 8, 2025, pp. 893–900. arXiv:2502.08177, doi:10.1609/
     aies.v8i1.36598.
[45] E. Durmus, L. Lovitt, A. Tamkin, S. Ritchie, J. Clark, D. Gan-
     guli, Measuring the persuasiveness of language models, https://
     www.anthropic.com/news/measuring-model-persuasiveness (April
     2024).
[46] K. Hackenburg, H. Margetts, Evaluating the persuasive influence of po-
     litical microtargeting with large language models, Proceedings of the
     National Academy of Sciences (PNAS) 121 (24) (2024) e2403116121.
     doi:10.1073/pnas.2403116121.
[47] S. C. Matz, J. D. Teeny, S. S. Vaid, H. Peters, G. M. Harari, M. Cerf, The
     potential of generative AI for personalized persuasion at scale, Scientific
     Reports 14 (2024) 4692. doi:10.1038/s41598-024-53755-0.
[48] H. Bai, J. G. Voelkel, S. Muldowney, J. C. Eichstaedt, R. Willer, LLM-
     generated messages can persuade humans on policy issues, Nature Com-
     munications 16 (2025) 6037. doi:10.1038/s41467-025-61345-5.
[49] A. Rogiers, S. Noels, M. Buyl, T. De Bie, Persuasion with large language
     models: A survey, arXiv preprint arXiv:2411.06837 (2024).
[50] L. Di Geronimo, L. Braz, E. Fregnan, F. Palomba, A. Bacchelli, UI dark
     patterns and where to find them: A study on mobile applications and

                                      40
    user perception, in: Proceedings of the 2020 CHI Conference on Human
    Factors in Computing Systems (CHI), 2020. doi:10.1145/3313831.
    3376600.

[51] J. Luguri, L. J. Strahilevitz, Shining a light on dark patterns, Journal
     of Legal Analysis 13 (1) (2021) 43–109. doi:10.1093/jla/laaa006.

[52] D. Ersoy, B. Lee, A. Shreekumar, A. Arunasalam, M. Ibrahim,
     A. Bianchi, Z. B. Celik, Investigating the impact of dark patterns on
     LLM-based web agents, in: Proceedings of the 47th IEEE Symposium
     on Security and Privacy (S&P), 2026, to appear. arXiv:2510.18113.

[53] G. K. Patro, A. Biswas, N. Ganguly, K. P. Gummadi, A. Chakraborty,
     FairRec: Two-sided fairness for personalized recommendations in two-
     sided platforms, in: Proceedings of The Web Conference 2020 (WWW),
     2020. doi:10.1145/3366423.3380196.

[54] P. Duetting, V. Mirrokni, R. Paes Leme, H. Xu, S. Zuo, Mechanism
     design for large language models, in: Proceedings of the ACM Web
     Conference 2024 (WWW), Best Paper, 2024. doi:10.1145/3589334.
     3645511.

[55] E. Soumalias, M. J. Curry, S. Seuken, Truthful aggregation of LLMs
     with an application to online advertising, in: International Conference
     on Learning Representations (ICLR), 2025. arXiv:2405.05905.

[56] K. A. Dubey, Z. Feng, R. Kidambi, A. Mehta, D. Wang, Auctions with
     LLM summaries, in: Proceedings of the 30th ACM SIGKDD Conference
     on Knowledge Discovery and Data Mining (KDD), ACM, 2024, pp. 713–
     722. doi:10.1145/3637528.3672022.

[57] S. Fish, Y. A. Gonczarowski, R. I. Shorrer, Algorithmic collusion by
     large language models, arXiv preprint arXiv:2404.00806 (2024).

[58] O. Ben-Shahar, C. E. Schneider, More Than You Wanted to Know: The
     Failure of Mandated Disclosure, Princeton University Press, 2014.

[59] G. Loewenstein, C. R. Sunstein, R. Golman, Disclosure: Psychology
     changes everything, Annual Review of Economics 6 (2014) 391–419.
     doi:10.1146/annurev-economics-080213-041341.


                                     41
