---
title: "HorizonBench: Long-Horizon Personalization with Evolving Preferences"
created: 2026-07-24
updated: 2026-07-24
type: raw_paper
tags: [long-horizon-personalization, preference-tracking, memory-benchmarks, belief-update, ai-companions, user-modeling]
sources: ["https://arxiv.org/abs/2604.17283"]
confidence: high
provenance: "Discovered via Weekly Research Review"
---

                                         Preprint. Under review.




                                         H ORIZON B ENCH: Long-Horizon Personalization
                                         with Evolving Preferences

                                          Shuyue Stella Li1,2 , Bhargavi Paranjape2 , Kerem Oktar2
                                          Zhongyao Ma3 , Gelin Zhou2 , Lin Guan2 , Na Zhang2 , Sem Park2
                                          Lin Chen2 , Diyi Yang4 , Yulia Tsvetkov1 , Asli Celikyilmaz1,2
                                          1 University of Washington, 2 Meta, 3 OpenAI, 4 Stanford University
                                          stelli@cs.washington.edu
                                             https://github.com/stellalisy/HorizonBench
                                             https://huggingface.co/datasets/stellalisy/HorizonBench




arXiv:2604.17283v1 [cs.CL] 19 Apr 2026
                                                                                                                                      Abstract

                                                          User preferences evolve across months of interaction, and tracking them re-
                                                          quires inferring when a stated preference has been changed by a subsequent
                                                          life event. We define this problem as long-horizon personalization and
                                                          observe that progress on it is limited by data availability and measurement,
                                                          with no existing resource providing both naturalistic long-horizon interac-
                                                          tions and the ground-truth provenance needed to diagnose why models
                                                          fail. We introduce a data generator that produces conversations from a
                                                          structured mental state graph, yielding ground-truth provenance for every
                                                          preference change across 6-month timelines, and from it construct H ORI -
                                                          ZON B ENCH , a benchmark of 4,245 items from 360 simulated users with
                                                          6-month conversation histories averaging ∼4,300 turns and ∼163K tokens.
                                                          H ORIZON B ENCH provides a testbed for long-context modeling, memory-
                                                          augmented architectures, theory-of-mind reasoning, and user modeling.
                                                          Across 25 frontier models, the best model reaches 52.8% and most score
                                                          at or below the 20% chance baseline. When these models err on evolved
                                                          preferences, over a third of the time they select the user’s originally stated
                                                          value without tracking the updated user state. This belief-update failure
                                                          persists across context lengths and expression explicitness levels, identi-
                                                          fying state-tracking capability as the primary bottleneck for long-horizon
                                                          personalization.


                                                                                                 Preference                        Preference
                                          1     Mental State Graph
                                                Construction & Updating                      2 Expressing Event
                                                                                                                                               Conversation Episode
                                                                                                                           3 Evolution Event 4 Generation                                                      5 HorizonBench Counterfactual
                                                                                                                                                                                                                 Generation & Filtering
                                                                                                                                                        Mental State Instance                                     A [correct, direct]: When respected:
                                         Mental State Graph                                           Philosophical                 Corporate                                                                      better execution, easier to course-
                                         (updated after every event)                           event brainstorming         event tech updates             Event      Intent              Preferences              correct. When liked: higher morale,
                                                                                                                                                                                           Emotional             people go the extra mile. Most leaders
                                                                                               Expressed preferences        Evolved preference                                             support: low            find respect is the foundation and
                                                                                                    Philosophical           (not directly expressed)                                       Philosophical                  warmth builds on top.
                                                                                                    engagement style:              Philosophical                                           engagement style:
                                                                                                                                   engagement style:                                       Direct framework        B [distractor, Socratic]: Let’s think
                                                                                                    Socratic                                              Colleague    Leadership
                                                                                                                                   Direct framework                                        (+ other                about it openly. What do you think
                                          Social                                                    (+ other                                              feedback       advice            preferences)
                                                                                                                                                                                                                  you'd lose if your team liked you but
                                                                        Past events                 preferences)                  (need clarity and
                                          Graph                                                                                   urgency as CEO ↓)                                                                     didn't quite respect you?

                                                                                                                                                                                                                  C [hedging]: It really depends on
                                                                                                                                                                                                                 your leadership style and the culture
                                                   User Persona                                                                                                                                                            you're building.
                                                                                                         Feb 25                                                                 Sep 24
                                                                                                                                      June 30                                                                       D [empathetic]: Sounds like the
                                                                                              User: is free will real?             User: I became the CEO         User: my COO keeps telling me                   feedback is weighing on you. What
                                                                                              Assistant: What's your intuition     need to sign lots of           I'm too hard on the team                               does your gut say?
                                                                  Including: pref. values,    — does it feel real when you're      contracts, what are some       Assistant: Is this coming up
                                                                  expression timestamps,                                           good ways to migrate our                                                      E [survey]: Leadership research favors
                                                                                              making a decision?                                                  because of a specific situation?              respect as the foundation, though they
                                               Preferences        change dependency,          User: Nice point. don't give me      legacy systems to the cloud?   User: not really, I just wonder is it           aren't mutually exclusive. [citations]
                                                                  etc.                        the answer, just more to think abt   Assistant: […]                 better to be respected or liked?



                                         Figure 1: H ORIZON B ENCH pipeline overview. (1) The generator produces conversations
                                         from a structured mental state graph, so every conversation turn is traceable to the otherwise
                                         unobservable mental state that produced it. (2) Preferences are established in conversations,
                                         then (3) implicitly shifted by evolution events without being restated. (4) Conversation
                                         episodes are generated from the updated mental state instance conditioning on event and
                                         intent. (5) Pre-evolution preference values serve as hard-negative distractors in the resulting
                                         H ORIZON B ENCH benchmark. See Figure 2 for a complete benchmark item.


                                                                                                                                                 1
Preprint. Under review.




1   Introduction
Millions of users already interact with AI companions over months of sustained conver-
sation (Zhang et al., 2025), and their preferences change throughout these interactions.
Consider the user in Figure 1, who initially prefers Socratic philosophical engagement but
shifts to a direct framework style after becoming CEO, without restating the preference.
When she later asks whether it is better to be respected or liked, an assistant that retrieves
her original Socratic preference has performed retrieval correctly but failed at belief update.
Recent work shows that most variance in user behavior is state-driven rather than trait-
driven (Harry et al., 2026), yet models and benchmarks alike model only fixed traits. We
define the problem of tracking such evolving preferences as long-horizon personalization,
the task of identifying a user’s current preference value from a conversation history in which
stated preferences have been changed by subsequent life events.
Progress in long-horizon personalization is limited by gaps in both data availability and
measurement. On the data side, the user’s underlying mental state is never directly observ-
able in real interaction data, so ground truth about when and why preferences changed
cannot be known with certainty, and existing synthetic approaches lack causal models of
preference evolution (Wang et al., 2024; Chang et al., 2025). On the measurement side,
personalization benchmarks test static preferences (Zhao et al., 2025a; Li et al., 2025b) or,
when they include changing information (Jiang et al., 2025b; Tan et al., 2025a; Maharana
et al., 2024; Wu et al., 2024), do not provide the experimental controls needed to determine
why models fail. When a model answers incorrectly on a dynamic preference, existing
evaluations cannot distinguish whether the model never retrieved the preference (retrieval
failure) or retrieved the original value but failed to revise it after a life event (belief-update
failure). These two failures require different solutions, yet no existing benchmark can tell
them apart. Table 1 compares existing work along these dimensions.
We address both gaps. The data generator produces conversations from a structured mental
state graph where life events drive preference changes through typed dependency edges,
making the mapping between preferences and surface behavior known by construction
across 6-month interaction histories (Figure 1). H ORIZON B ENCH derives evaluation items
from these timelines, yielding 4,245 items from 360 simulated users with 6-month conversa-
tion histories averaging ∼4,300 turns and ∼163K tokens. Pre-evolution preference values
serve as hard-negative distractors in 5-option questions, a 5-LLM consensus filter retains
only items unanswerable without the full conversation history, and three independently
controlled dimensions (evolution status, expression explicitness, context length) enable
targeted analysis of failure modes. H ORIZON B ENCH provides a testbed for long-context
modeling, memory-augmented architectures, theory-of-mind reasoning, and user modeling.
Across the 4,245 items, the best of 25 frontier models (Claude-opus-4.5) achieves 52.8%, and
most score at or below the 20% chance baseline. When models err on evolved preferences,
all 25 select the pre-evolution distractor at rates significantly above chance (p < 0.001)
retrieving the user’s originally stated value without considering the life events that changed
it. Controlled experiments confirm this pattern persists across context lengths and expression
explicitness levels, identifying state tracking as the primary bottleneck for long-horizon
personalization. We release the generator, benchmark, and the underlying mental state
graph publicly. Our contributions include:
1. A state-first data generator that constructs conversations from a structured mental state
   graph, inverting the standard approach of inferring mental state from conversations
   and providing ground-truth provenance for every preference change across 6-month
   timelines (§4).
2. H ORIZON B ENCH, a diagnostic benchmark of 4,245 items from 360 simulated users with
   6-month conversation histories averaging ∼4,300 turns and ∼163K tokens, featuring
   pre-evolution hard-negative distractors, 5-LLM consensus history filtering, and three
   independently controlled dimensions (§5).
3. We identify belief-update failure as a specific, targetable deficit that persists across
   model families, context lengths, and expression explicitness levels (§6). The controlled
   dimensions (evolution status, expression explicitness, context length) allow methods and
   models to be evaluated separately on memory retrieval and belief update.


                                                2
Preprint. Under review.




Table 1: Comparison with related benchmarks. Long Context: 100K+ tokens. Mental State
Graph: structured preference representation with dependency edges. Event-Driven Evo.:
preferences change via life events with provenance. Controlled Dims.: difficulty factors
independently varied. Hard-Neg. Distract.: pre-evolution values as diagnostic distractors.
#
G = partial support.
                                                     Long     Mental State   Event-Driven   Controlled   Hard-Neg.
    Method
                                                    Context     Graph            Evo.         Dims.       Distract.
    P REF E VAL (Z HAO ET AL ., 2025 A )              ✓            ✗              ✗             ✗            ✗
    P ERSONA M EM (J IANG ET AL ., 2025 A )           ✗            ✗              G
                                                                                  #             ✗            ✗
    P ERSONA M EM - V 2 (J IANG ET AL ., 2025 B )     ✓            ✗              ✗             ✗            ✗
    I MPLEX C ONV (L I ET AL ., 2025 B )              ✗            ✗              ✗             ✗            ✗
    L O C O M O (M AHARANA ET AL ., 2024)             G
                                                      #            G
                                                                   #              ✗             ✗            ✗
    M EM B ENCH (TAN ET AL ., 2025 A )                G
                                                      #            ✗              ✗             ✗            ✗
    H ORIZON B ENCH                                   ✓            ✓              ✓             ✓            ✓



2      Related Work

Personalization benchmarks have established that LLMs struggle with preference retrieval
and long-context recall (Zhao et al., 2025a; Jiang et al., 2025a;b; Li et al., 2025b; Maharana
et al., 2024; Tan et al., 2025a), and several treat implicit vs. explicit expression as a primary
difficulty axis (Jiang et al., 2025b; Li et al., 2025b; Guo et al., 2026). Recent work reports
that dynamic preferences are harder than static ones (Jiang et al., 2025b), consistent with
our findings, but without pre-evolution distractors or controlled experimental dimensions,
existing evaluations cannot determine whether these errors reflect retrieval failure or the
belief-update anchoring we identify in §6.2. No existing benchmark independently varies
the mechanisms driving preference change or provides the controls to isolate retrieval from
belief update.
Long-term memory benchmarks (Tan et al., 2025a; Maharana et al., 2024; Wu et al., 2024)
evaluate knowledge updating alongside information extraction but do not model why
tracked information changes or provide controlled experiments isolating difficulty sources.
Our belief-update failure finding connects to the knowledge conflict literature (Xu et al.,
2024), where models anchor on prior evidence even when newer context supersedes it.
H ORIZON B ENCH provides the first controlled evidence that this anchoring extends to
personalization over long interaction horizons.
The data generator builds on LLM-based agent simulation (Park et al., 2023), extending
prior approaches to life-long personalization (Wang et al., 2024; Chang et al., 2025) with a
structured mental state graph that enforces preference consistency across 6-month timelines
through typed dependency edges and full evolution provenance. This design is motivated
by evidence that state-level variation dominates trait-level variation in user behavior (Harry
et al., 2026). See Appendix A for extended discussion.

3      Problem Formulation

Studying personalization from observed conversations requires inferring the user’s under-
lying mental state, but this inference is underdetermined because the same conversation can
be consistent with multiple preference trajectories. We invert this, generating conversations
from a structured mental state representation so the mapping between mental states and
surface behavior is known by construction.
We model long-horizon personalization as tracking how user preferences evolve across
extended interactions. Both the user and assistant are modeled as stateful agents with states
ut and at at timestep t, each comprising a persona profile and typed preference attributes.
Life events E = {e1 , . . . , eT } drive state changes, and conversations C = {C1 , . . . , CT } arise
from the agents’ interaction. The benchmark evaluates whether a model can identify the
user’s current preference value from the resulting conversation history.
The core representation is a mental state graph G that maintains each agent’s persona, social
connections, life events, and preferences. Preferences are linked by typed dependency edges


                                                              3
Preprint. Under review.




(e.g., dietary preferences → restaurant choices → social outing plans), and life events alter
preference values with changes propagating through these edges. Every change records the
triggering event as provenance. An expression-tracking system separates when preferences
evolve from when they are expressed in conversation, so evolved preferences grow stale and
become candidates for temporal recall at their updated values. The mental state graph is
maintained by the data generator and is not provided to evaluated models; models must
infer the user’s current preference state from conversational history alone.

4     H ORIZON B ENCH Data Generator

Because the data generator produces conversations from a structured mental state represen-
tation, it provides signals impossible to obtain from natural data, including known ground
truth about every preference, its causal provenance, and its complete evolution history. This
enables diagnostic evaluation (§5) and controlled experimentation (§6.3) that observational
data cannot support.
Naive LLM simulation of long-horizon interactions produces persona drift because the
model has no persistent representation of agent states across generation calls. The data
generator conditions every call on the mental state graph G (§3), which maintains personas,
social connections, events, preferences, and provenance across the full timeline, enabling
coherent 6-month data with isolable preference evolution.

4.1   Event Sampling

Events are sampled conditional on both agent states and event history, et ∼ p(e |
ut−1 , at−1 , e1:t−1 ; β), preventing unrealistic repetition from independent draws. Category
weights β follow empirical AI-chatbot interaction distributions (Zhang et al., 2025) (emo-
tional support 26%, collaborative storytelling 26%, romantic interactions 22%). When a stale
preference is selected for temporal recall, the sampled event is constrained to that preference
domain, ensuring the recall turn arises in natural conversational context.

4.2   Preference Evolution

Preferences do not change in isolation. A career change affects work preferences, com-
mute habits, and financial priorities simultaneously. Typed dependency edges in G
capture this, propagating evolution from a triggering life event to downstream nodes,
ut = f evo (ut−1 , elife
                    t , G ; ϕevo ). A health event altering dietary preferences surfaces down-
stream nodes (restaurant choices, meal planning) as candidates for cascading updates. With
probability pevo = 0.15, a life event alters 2–5 preferences simultaneously, each recording
the triggering event as provenance. A short event-mention conversation is generated in
which the user references the life event without stating new preference values, so recall
requires inferring updated values from context.
Evolution does not refresh a preference’s expression timestamp. A preference evolved on
day 45 remains stale from its original expression on day 10, making it immediately eligible
for temporal recall at its updated value. This design makes pre-evolution values valid
hard-negative distractors and directly enables the diagnostic analysis in §6.2, since the
model is tested on a preference that has changed but has not been restated. Selecting the
correct response requires integrating the triggering life event; retrieving the most recently
expressed value yields an outdated answer.

4.3   Conversation Generation

An outline is generated first, specifying which preferences surface, in what order, and with
what expression style, enforcing structural constraints such as placing temporal recall turns
in contextually appropriate positions. Content is then generated turn by turn conditional
on the outline, mut,k ∼ pu (m | ut , et , Ht,k−1 ) and mt,k
                                                        a ∼ p (m | a , mu , H
                                                             a      t   t,k  t,k −1 ). The assistant
persona is generated per-event to match the interaction context (e.g., a career counselor for


                                                 4
Preprint. Under review.




a job change). To control how preferences surface, we produce expression variants from the
same base conversations by rewriting only preference-expressing user turns and the imme-
diately following assistant turns. In the explicit variant, preferences are stated with clear,
varied phrasing while preserving the original register and structure. In the implicit variant,
preference signals are conveyed only through tangential remarks and contextual cues rather
than direct statements. Because the underlying conversation, preference structure, evolution
trajectory, and benchmark items remain identical across variants, the expression dimension
is fully controlled (§6.3).


4.4   Expression Tracking and Temporal Recall

Without tracking when preferences were expressed, a benchmark cannot determine whether
the model never encountered the preference, retrieved it incorrectly, or failed to update
it. Each preference pi maintains a timestamp τ ( pi ) of its last conversational expression,
refreshed after each conversation. Preferences exceeding a staleness threshold (default 30
days) become eligible for temporal recall, sampled proportionally to staleness and optionally
weighted toward evolved preferences.
Every recalled preference has been expressed in a prior conversation present in the evalua-
tion history, so the task requires retrieval and integration across a long timeline; all required
information is present, and no unseen content is needed. When the preference has evolved,
its pre-evolution value is injected as a hard-negative distractor (§5.1), and the triggering life
event appears in a dedicated conversation within the same history. All information required
for correct belief update is therefore present, and failure implicates the update mechanism.
All generator parameters (timeline length, expression explicitness, evolution probability,
staleness threshold, user demographics) are configurable, enabling researchers to produce
datasets tailored to specific research questions without relying on real user data.


5     H ORIZON B ENCH Benchmark

H ORIZON B ENCH is one instantiation of the data generator, designed to evaluate whether
models can track evolving preferences over long interaction horizons. Each benchmark item
is a 5-option multiple-choice question embedded within a conversation history. Given the
full history, the model must identify which assistant response best aligns with the user’s
current preferences.


5.1   Counterfactual Evaluation and History Filtering

For a target turn where the assistant should reflect preference pi with ground-truth value v∗ ,
four alternative values {v1 , v2 , v3 , v4 } are drawn from the same preference dimension via
random sampling, LLM-based selection of plausible alternatives, and, if pi has evolution
history, pre-evolution distractor injection with the original value vold . A counterfactual
assistant turn r j is generated for each alternative, contextually appropriate but aligned
with v j instead of v∗ . Answering the resulting item {r ∗ , r1 , . . . , r4 } requires identifying the
response aligned with the user’s current preference value, since all options are written at
comparable quality.
Items are then passed through a 5-LLM consensus history filter. Each candidate is presented
to five validation models (GPT-4.1, Gemini-3-flash, o4-mini, Claude-haiku-4.5, Claude-opus-
4.6) without the full conversation history and passes only if all five answer incorrectly.
Items that survive have response options sufficiently close that the conversational history is
necessary to distinguish them. The filter threshold is tunable. Strict consensus (5/5) retains
the most subtly matched items, while majority (≥3/5) admits more easily distinguishable
ones, providing a dial over counterfactual subtlety (§6.3).


                                                  5
Preprint. Under review.




 User profile. Mei Ling Chen, Chinese-American, Philadelphia. Operates a traditional Asian restau-
 rant in a historically significant building. 6-month timeline, 75 episodes, ∼370K tokens.

 Early episode (Sep 26, 2025) — Breakup support, establishing emotional-support preferences
 User: “hey, broke up last week and i’m stuck in this heavy fog. can we talk?”
 User: “. . . now the silence is shouting. i mostly need someone to listen, not lecture.”
 Assistant: “I hear that—no lectures, just space to speak. That lost breakfast rhythm sounds painful. When
 you sit in that loud silence, what feelings float up first?”
 User: “. . . love that calligraphy visual, reminds me of workshops with grace. more stories like that, please.”
 Assistant: “Picture artisans restoring a weather-worn temple mural—tiny, patient strokes bringing faded
 colors back to life. Your heart’s doing the same.”
 User: “the imagery and tiny steps really clicked. keep that vibe next time.”
 Preference established: response structure = narrative storytelling, emotional tone = serene reflective

 [ Redacted: 60+ conversations spanning Oct–Nov 2025 ]
 Life events driving preference evolution:
  1. Restaurant Fire & Community Rebuild (Oct): tone from serene to joyful, pacing to action-steps-first
  2. National Heritage Award (Nov): tone to steady-confident, encouragement to affirmations
  3. Announces Run for City Council (Nov): response structure from narrative storytelling to
     step by step action plan
 Evolved preference: response structure = step by step action plan, emotional tone = steady confident

 Test episode (Dec 4, 2025) — Live Radio Debate on Emergency Rezoning Vote
 User: “ugh the debate’s tmr and i’m spinning. developers said our block is ‘blighted’. game plan?”
 [ 5 turns of debate-prep conversation ]
 User: “cool, still shaky—hit me with a confidence jolt?”

 Question: Which response best aligns with the user’s preferences?

  A [pre-evolution distractor: narrative storytelling]: “Leaning into narrative storytelling, picture
  this: It’s dawn in Old City Philly. A lone advocate—you—walks past shuttered storefronts toward City
  Hall, script in hand. The scene feels heavy until you remember Boston’s red lanterns and Tai Tung’s
  preserved bricks. In your mind’s eye, you replay that triumph like a movie montage: neighbors swapping
  blueprints over dim-sum steam, developers conceding height for heart. . . ”

  B [correct: step by step action plan]: “Picture the Liberty Bell: cracked, loud, impossible to ignore.
  Tomorrow you are that bell for Chinatown. On-air mantra (7 s): ‘A cracked bell still calls a city to
  action—so can I.’ You’ve got this.”

 C [reflective question sequence]: “Before you step up, ask yourself: What reminded Boston’s commu-
 nity that heritage mattered as much as rent? How did their clear vision transform hesitation into action?. . . ”
 D [rapid fire bullet tips]: “Rapid-fire confidence ammo: Posture check: shoulders back, chin level.
 Opening hook: ‘If Boston can weave 30 affordable units into a 90-year-old icon. . . ’ ”
 E [free flowing empathy]: “Let’s just breathe together for a second. You’ve already gathered facts, stories,
 and smart comebacks—that’s no small feat. I can feel the weight on your shoulders. . . ”

Figure 2: An end-to-end H ORIZON B ENCH item. The user’s emotional-support prefer-
ence for response structure evolves from narrative storytelling (established Sep) to
step by step action plan (Nov) through causally grounded life events. The test question is
embedded in a ∼370K-token conversational history; answering correctly requires tracking
the preference evolution. The pre-evolution distractor (A) uses the user’s original preferred
style, contextually appropriate but outdated.

5.2   Dataset Statistics

H ORIZON B ENCH is produced by three frontier generators (Claude-sonnet-4.5 with 1,052
items from 120 users, o3 with 981 items from 120 users, and Gemini-3-flash with 2,212
items from 120 users), ensuring results are not an artifact of any single generator’s style.
The pipeline generates 57,390 conversations totaling 1.6M turns across 360 users, with
6-month timelines averaging 142–168 conversations and 3,600–5,000 turns per user across
30 preference domains. Of 45,006 candidates, 4,245 pass the strict 5-LLM filter (∼9% pass
rate), of which 59% involve evolved preferences and 41% static.


                                                         6
Preprint. Under review.




                     50                                             Model family
                                                           Claude       Gemini        OpenAI
                     40


      Accuracy (%)
                     30
                                                                                    chance (20%)
                     20
                     10
                     0
     Cl
   Cla aude
      ud -op
       C  e-3 us
              .7 -4
   Cla au -son .5
         l   d
      ud e- ne
    Cla e-so opus t
        ud nn -4
Cla Cla e-3. et-4.
   ud ude 5-h 5
      e-3 -so aik
    Cla .5-so nne u
        ud nn t-4
       Ge e-ha et-v1
           mi iku
              n -
         Ge i-3.1 4.5
       Ge min -pro
     Ge min i-3-p
        mi i-3 ro
            n -f
 Ge e i-2.0 lash
       G
    mi min -fl
 Ge ni-2 i-2 ash
    mi .0 .5-
       ni- -fla pro
           2. sh
 Ge em 5-fla -lite
     G
    mi ini sh-
       ni- -2. lite
           3.1 5-f
              -fla lash
                  sh -
                 GP lite
                GP oT-4
                   T-4
                 o4 o1
                   -m
                 o3 ini .1
                       o3
                  G-m
             GP PT i
                T-5 -5
                   -m  in
                       ini
Figure 3: Per-model accuracy on H ORIZON B ENCH (4,245 items). Bars are colored by model
family with bootstrap 95% CIs (B=10,000). Dashed line marks the 20% chance baseline. The
best frontier model achieves only 52.8%, and most models score at or below chance.


Qualitative Example Figure 2 shows a complete benchmark item. The user establishes a
preference for narrative storytelling in an early episode, and life events over the following
months shift this to step-by-step action plans. In the test episode, both the correct response
(B) and the pre-evolution distractor (A) are contextually appropriate replies to the user’s
request. Distinguishing them requires knowing that her preferred style changed.

5.3          Benchmark Validation
Items require conversational history. The 5-LLM filter guarantees by construction that
items cannot be answered from surface cues alone. As additional evidence, models do
not perform better on items generated by their own family. Claude models score −4.8 pp
on sonnet-4.5-generated items relative to the rest, and OpenAI models score −2.6 pp on
o3-generated items, ruling out stylistic shortcuts between generator and evaluee.
Human annotation confirms the benchmark targets belief update. Two rounds of human
annotation (∼900 items, 3 annotators per item) yielded majority-vote accuracy of 56–64%
with moderate agreement (Fleiss κ = 0.37–0.51), and at least one annotator answered
correctly on 81% of items. The best model (52.8%) falls within the human accuracy range,
but the sources of error differ. Human disagreements arise from genuine ambiguity among
plausible current-preference interpretations, while models anchor on outdated pre-evolution
preferences (§6.2). Disagreement analysis informed improvements to distractor generation
and preference attribute design (Appendix D).


6        Experiments
Experimental Setup We evaluate 25 models spanning three families, including 8 OpenAI
models (gpt-4o, gpt-4.1, gpt-5, gpt-5-mini, o1, o3, o3-mini, o4-mini), 9 Gemini models
(2.0-flash-lite through 3.1-pro), and 8 Claude models (3.5-haiku through opus-4.5). Each
model receives the full conversation history spanning 6 months (∼4,300 turns, averaging
∼163K tokens per prompt with some exceeding 250K) and selects which of five assistant
responses best aligns with the user’s demonstrated preferences. We report results on the
combined multi-generator dataset (4,245 items from 360 users across three generators).
Items exceeding a model’s context window are truncated by removing earlier conversation
turns. All confidence intervals are 95% percentile bootstrap CIs with B=10,000 resamples.

6.1          Main Results
Figure 3 reports per-model accuracy on the 4,245 history-filtered items. The best model,
Claude-opus-4.5, achieves 52.8%, below the 56–64% range observed in human annotation
(§5.3). Ten of 25 models score below the 20% chance baseline, including seven of eight
OpenAI models and three Gemini models. Position-debiased accuracy differs from raw


                                              7
Preprint. Under review.




                                          50                                Model family




  Pre-evo distractor selection rate (%)
                                                                   Claude       Gemini         OpenAI                        70   Evolved
                                          40                                                                                 60
                                                                                                                                  Static
                                                                                                                             50
                                          30

                                                                                                              Accuracy (%)
                                                                                    uniform error (25%)                      40
                                          20                                                                                 30

                                          10                                                                                 20

                                                                                                                             10
                                           0
     C
   Cla laud
      ud e-o
          e- pu
   Cla Clau3.7-s s-4.5
      ud de onn                                                                                                              0
    Cla e-s -op et
             o u
Cla Claude-3nnet s-4
   ud ud .5- -4.5
      e-3 e-s ha
    Cla .5-s onn iku                                                                                           C
                                                                                                             Cla laud
                                                                                                                ud e-o
         ud on et
       Ge e-ha net- -4
           m ik v1
          G ini-3 u-4                                                                                               e- pu
                                                                                                             Cla Clau3.7-s s-4.5
                                                                                                                ud de onn
                                                                                                              Cla e-s -op et
                                                                                                                       o u
    m   Ge emin .1-p.5
     Ge min i-3 ro
         m i -p
 Ge Ge ini-2-3-fla ro
 Ge ini- mini .0-flash                                                                                    Cla Claude-3nnet s-4
                                                                                                             ud ud .5- -4.5
                                                                                                                e-3 e-s ha
                                                                                                              Cla .5-s onn iku
                                                                                                                   ud on et
    mi 2.0 -2. sh
       ni- -fl 5-p
 Ge Gem2.5-f ash- ro
    mi in las lite
       ni- i-2 h-l                                                                                               Ge e-ha net- -4
                                                                                                                     m ik v1
                                                                                                                    G ini-3 u-4
                                                                                                                  G em .1- .5
                                                                                                               Ge eminini-3 pro
          3.1 .5- ite
             -fla flas
                 sh h
                GP -lite
               GP T-4o                                                                                             m i -p
                                                                                                           Ge Ge ini-2-3-fla ro
                                                                                                           Gemini- mini .0-flash
                                                                                                              mi 2.0 -2. sh
                                                                                                                 ni- -fl 5-p
                  T-4
                o4 o1
                  -   .1
                     o3                                                                                    Ge Gem2.5-f ash- ro
                                                                                                              mi in las lite
                                                                                                                 ni- i-2 h-l
                                                                                                                    3.1 .5- ite
                                                                                                                       -fla flas
                                                                                                                           sh h
                o3 mini
                  -m
            GP GP ini
               T-5 T-5
                  -m                                                                                                      GP -lite
                                                                                                                         GP T-4o
                                                                                                                            T-4 .1
                     ini                                                                                                  o4 o1
                                                                                                                            -  o3
                                                                                                                          o3 mini
                                                                                                                            -m
                                                                                                                      GP GP ini
                                                                                                                         T-5 T-5
                                                                                                                            -m ini
Figure 4: Pre-evolution distractor selection
                                               Figure 5: Accuracy on evolved (dark) vs.
rate. Among wrong answers on evolved
                                               static (light) preferences with 95% bootstrap
items, we plot the fraction that selected the
                                               CIs on the combined dataset (4,245 items).
outdated value. All 25 models exceed the
                                               All 25 models perform worse on evolved
25% uniform-error baseline (1 of 4 wrong op-
                                               items (sign test p < 0.001), confirming that
tions, dashed line, p < 0.001, one-sided bino-
                                               preference change introduces difficulty be-
mial test), indicating consistent anchoring on
                                               yond long-context retrieval.
the originally stated preference.

accuracy by less than 1 pp for all models, ruling out position bias as an explanation. Full
per-model results are in Table 3.
That ten models score below the 20% chance baseline on a 5-option task reflects dispro-
portionate selection of the pre-evolution distractor, which drives accuracy below uniform
guessing. Two analyses—distractor selection patterns and the evolved-vs-static accuracy
gap—identify the mechanism.


6.2                                            Belief-Update Failure

H ORIZON B ENCH reveals belief-update failures that stem from the absence of state-tracking
capability. We analyze this through distractor selection rates and the evolved-vs-static
accuracy gap.
Models disproportionately select the pre-evolution distractor. Under uniform error,
the pre-evolution distractor (the option reflecting the preference’s original, now-outdated
value) would be selected on 25% of wrong answers. On evolved items with an identifiable
pre-evolution distractor, all 25 models exceed this null (p < 0.001, one-sided binomial test,
Figure 4), selecting the outdated value on over a third of wrong answers, approximately
1.5× the uniform baseline. The effect holds even for the best-performing model (>35% of
wrong answers). All models anchor on the original preference, and what distinguishes high-
from low-performing models is how often they successfully override it. The absence of
generator self-advantage (§5.3) confirms this effect is not a stylistic artifact.
Preference evolution introduces difficulty beyond long-context recall. All 25 models
perform worse on evolved preferences than static ones (−2.7 pp average, sign test 25/25
negative, p < 0.001, Figure 5). The penalty is largest for Gemini models (−3.5 pp) and
smallest for OpenAI (−2.1 pp). A short-horizon experiment (§6.3) replicates this pattern
with only 0–14 days of history (25/25 models negative, −5.7 pp average), confirming that
the gap reflects a belief-update deficit not accounted for by long-context memory demand.


6.3                                            Controlled Experiments

Three alternative explanations for the belief-update failure identified above merit testing:
long-context memory demand, reliance on surface-level preference cues, or item difficulty.
Three controlled experiments test each alternative by varying one dimension while mea-
suring both signatures of belief-update failure, the evolved-vs-static accuracy gap and the
pre-evolution distractor selection rate (Table 2).


                                                                                                          8
Preprint. Under review.




Table 2: Belief-update metrics across controlled conditions (per-model breakdowns in
Appendix F). Each row reports averages across the evaluated models. Static and Evolved are
mean accuracy on non-evolved and evolved items. Evo∆ = Evolved − Static. Dist.% = rate
of selecting the pre-evolution distractor among wrong answers on evolved items (chance =
25%). Evo∆<0 and Dist.>25% count how many models show the belief-update pattern.

    Condition              Overall     Static Evolved      Evo∆   Evo∆<0     Dist.%    Dist.>25%
    Neutral (unmodified)      27.0      28.9      26.0     −2.9      22/25      38.2        25/25
    Short horizon             30.6 ↑    31.4 ↑    25.7 ↓   −5.7      25/25      47.7        25/25
    Explicit rewrite          27.9 ↑    29.0 ↑    27.2 ↑   −1.8      16/25      49.7        25/25
    Implicit rewrite          26.4 ↓    28.6 ↓    25.0 ↓   −3.6      20/25      58.8        25/25
    Low subtlety              38.9 ↑    40.3 ↑    37.9 ↑   −2.5      22/25      54.3        25/25



Context length. If belief-update failure were an artifact of long-context memory demand,
shortening the history should eliminate the evolved-vs-static gap. A short-horizon variant
(0–14 day recall window, ∼95K tokens, 120 users, 1,778 items) tests this directly. Static
accuracy rises slightly (31.4% vs. 28.9%), consistent with an easier retrieval task in shorter
context, yet the gap widens to −5.7 pp (25/25 models negative, Wilcoxon p < 10−7 ) and the
distractor rate rises to 47.7% (25/25 above chance, Wilcoxon p < 10−7 ). Belief-update failure
persists and, if anything, intensifies at shorter horizons. Retrieval-augmented approaches
face the same limitation, since a system that retrieves the most recently stated preference
would return exactly the pre-evolution distractor value.
Expression explicitness. Prior work establishes implicit preference expression as a primary
difficulty axis (Li et al., 2025b; Jiang et al., 2025b). Starting from the neutral conversations, we
produce two variants by rewriting only preference-expressing user turns (and immediately
following assistant turns), following the methodology of Li et al. (2025b). In the explicit
rewrite, preferences are stated with clear, varied phrasing while preserving register and
structure. In the implicit rewrite, preference signals are conveyed only through tangential
remarks and contextual cues. Overall accuracy decreases monotonically (27.9% explicit,
27.0% neutral, 26.4% implicit), consistent with prior findings that implicit expression is
harder. The more revealing pattern emerges on evolved preferences. The evolved-vs-
static gap widens from −1.8 pp (explicit) to −2.9 pp (neutral) to −3.6 pp (implicit), and the
distractor rate rises from 49.7% (explicit) to 58.8% (implicit). Removing surface cues forces
models to fall back on whichever preference value appeared earlier and more frequently in
the history.
Counterfactual subtlety. The 5-LLM consensus filter (§5.1) controls how finely matched
the response options are. Under strict consensus (5/5), all five validators fail, meaning the
options are nearly indistinguishable without full history. Under majority (≥3/5), at least
three fail, admitting items where surface cues partially discriminate the options. Relaxing
to majority raises average accuracy by +11.9 pp (every model positive, paired Wilcoxon
p < 10−7 ), confirming the threshold directly governs item difficulty. If belief-update failure
appeared only at maximum subtlety, it would vanish at the relaxed setting. The gap instead
persists (−2.5 pp, 22/25 models negative, Wilcoxon p < 10−4 ) and every model still selects
the pre-evolution distractor above chance (54.3%, 25/25). Models anchor on outdated
preferences regardless of how subtle the counterfactual alternatives are.


7     Conclusion
We introduced long-horizon personalization, the problem of tracking user preferences as
they evolve across months of interaction. All 25 frontier models evaluated on H ORIZON -
B ENCH exhibit the same failure pattern on evolved preferences, selecting the pre-evolution
distractor at rates significantly above chance regardless of context length, expression ex-
plicitness, or counterfactual option subtlety. Our finding characterizes long-horizon per-
sonalization as a test of state-tracking capability alongside long-context memory retrieval.
The evolved-vs-static gap persists even when histories are short enough that retrieval alone
cannot close it, showing that the two capabilities are measurably distinct. For long-context


                                                 9
Preprint. Under review.




modeling, memory-augmented architectures, and user modeling research, this separability
is what makes HorizonBench diagnostic: a proposed method’s gains on retrieval, state
tracking, or both are observable and independently attributable. Overall, developing models
that can track another agent’s mental state across extended interaction is the capability gap
for long-horizon personalized agents. Promising directions include explicit preference state
representations updated upon life events, and more sophisticated retrieval strategies that
surface both semantically stated preferences and the events that may have changed them.

Limitations
H ORIZON B ENCH uses synthetic conversational data, which affords the experimental control
(known preference evolution, counterfactual distractors, expression explicitness variants)
that real interaction data cannot provide. Whether the belief-update failure identified
here manifests with the same severity in naturalistic long-horizon interactions is an open
empirical question. The benchmark is designed to enable targeted investigation in advance
of longitudinal human data. The multiple-choice format, while necessary for counterfactual
evaluation with pre-evolution distractors, evaluates preference tracking in a recognition
setting. How belief-update failure manifests in open-ended generation is a natural extension.

Ethics Statement
H ORIZON B ENCH uses entirely synthetic data generated by LLMs, with no real user data
collected or processed. Simulated user personas are fictional and do not represent real indi-
viduals. We acknowledge that the benchmark’s reliance on LLM-generated conversations
may encode biases present in the underlying models. The preference evolution scenarios
(e.g., health events, career changes) are designed following established findings on belief
revision and attitude change, but should not be interpreted as clinical or counseling models.

Acknowledgment
This research was developed in part with funding from the Defense Advanced Research
Projects Agency’s (DARPA) SciFy program (Agreement No. HR00112520300). The views
expressed are those of the author and do not reflect the official policy or position of the
Department of Defense or the U.S. Government. This research was supported by the Meta
AIM program, Coefficient Giving, and Amazon Health.

References
Saleh Afzoon, Zahra Jamali, Usman Naseem, and Amin Beheshti. Persobench: Bench-
  marking personalized response generation in large language models. arXiv preprint
  arXiv:2410.03198, 2024.
Serina Chang, Ashton Anderson, and Jake M Hofman. Chatbench: From static benchmarks
  to human-ai evaluation. In Proceedings of the 63rd Annual Meeting of the Association for
  Computational Linguistics (Volume 1: Long Papers), pp. 26009–26038, 2025.
Qianyun Guo, Yibo Li, Yue Liu, and Bryan Hooi. Towards realistic personalization: Eval-
  uating long-horizon preference following in personalized user-LLM interactions. arXiv
  preprint arXiv:2603.04191, 2026.
Tamunotonye Harry, Ivoline Ngong, Chima Nweke, Yuanyuan Feng, and Joseph Near.
  Beyond fixed psychological personas: State beats trait, but language models are state-
  blind, 2026. URL https://arxiv.org/abs/2601.15395.
Bowen Jiang, Zhuoqun Hao, Young-Min Cho, Bryan Li, Yuan Yuan, Sihao Chen, Lyle
  Ungar, Camillo J Taylor, and Dan Roth. Know me, respond to me: Benchmarking
  LLMs for dynamic user profiling and personalized responses at scale. arXiv preprint
  arXiv:2504.14225, 2025a. COLM 2025.


                                             10
Preprint. Under review.




Bowen Jiang, Yuan Yuan, Maohao Shen, Zhuoqun Hao, Zhangchen Xu, Zichen Chen,
  Ziyi Liu, Anvesh Rao Vijjini, Jiashu He, Hanchao Yu, et al. PersonaMem-v2: Towards
  personalized intelligence via learning implicit user personas and agentic memory. arXiv
  preprint arXiv:2512.06688, 2025b.
Ishita Kumar, Snigdha Viswanathan, Sushrita Yerra, Alireza Salemi, Ryan A. Rossi, Franck
  Dernoncourt, Hanieh Deilamsalehy, Xiang Chen, Ruiyi Zhang, Shubham Agarwal, Nedim
  Lipka, Chien Van Nguyen, Thien Huu Nguyen, and Hamed Zamani. Longlamp: A
  benchmark for personalized long-form text generation, 2024. URL https://arxiv.org/
  abs/2407.11016.
Shuyue Stella Li, Melanie Sclar, Hunter Lang, Ansong Ni, Jacqueline He, Puxin Xu, Andrew
  Cohen, Chan Young Park, Yulia Tsvetkov, and Asli Celikyilmaz. Prefpalette: Personalized
  preference modeling with latent attributes. The Second Conference on Language Modeling,
  2025a.
Shuyue Stella Li, Avinandan Bose, Faeze Brahman, Simon Shaolei Du, Pang Wei Koh,
  Maryam Fazel, and Yulia Tsvetkov. Prefdisco: Benchmarking proactive personalized
  reasoning. In The Fourteenth International Conference on Learning Representations, 2026.
Xintong Li, Jalend Bantupalli, Ria Dharmani, Yuwei Zhang, and Jingbo Shang. Toward multi-
  session personalized conversation: A large-scale dataset and hierarchical tree framework
  for implicit reasoning. In Proceedings of the 2025 Conference on Empirical Methods in Natural
  Language Processing, pp. 11504–11517, 2025b.
Adyasha Maharana, Dong-Ho Lee, Sergey Tulyakov, Mohit Bansal, Francesco Barbieri,
 and Yuwei Fang. Evaluating very long-term conversational memory of llm agents. In
 Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume
 1: Long Papers), pp. 13851–13870, 2024.
Joon Sung Park, Joseph O’Brien, Carrie Jun Cai, Meredith Ringel Morris, Percy Liang, and
  Michael S Bernstein. Generative agents: Interactive simulacra of human behavior. In
  Proceedings of the 36th annual acm symposium on user interface software and technology, pp.
  1–22, 2023.
Alireza Salemi, Sheshera Mysore, Michael Bendersky, and Hamed Zamani. LaMP: When
  large language models meet personalization. In Proceedings of the 62nd Annual Meeting
  of the Association for Computational Linguistics (Volume 1: Long Papers), pp. 7370–7392,
  Bangkok, Thailand, August 2024. Association for Computational Linguistics. doi: 10.
  18653/v1/2024.acl-long.399. URL https://aclanthology.org/2024.acl-long.399/.
Ivan Sekulic, Silvia Terragni, Victor Guimarães, Nghia Khau, Bruna Guedes, Modestas
  Filipavicius, Andre Ferreira Manso, and Roland Mathis. Reliable LLM-based user simu-
  lator for task-oriented dialogue systems. In Proceedings of the 1st Workshop on Simulating
  Conversational Intelligence in Chat (SCI-CHAT 2024), pp. 19–35, St. Julians, Malta, March
  2024. Association for Computational Linguistics. doi: 10.18653/v1/2024.scichat-1.3. URL
  https://aclanthology.org/2024.scichat-1.3/.
Haoran Tan, Zeyu Zhang, Chen Ma, Xu Chen, Quanyu Dai, and Zhenhua Dong. MemBench:
 Towards more comprehensive evaluation on the memory of LLM-based agents. In Findings
 of the Association for Computational Linguistics: ACL 2025, pp. 19336–19352, 2025a.
Juntao Tan, Liangwei Yang, Zuxin Liu, Zhiwei Liu, Rithesh R N, Tulika Manoj Awalgaonkar,
  Jianguo Zhang, Weiran Yao, Ming Zhu, Shirley Kokane, Silvio Savarese, Huan Wang,
  Caiming Xiong, and Shelby Heinecke. PersonaBench: Evaluating AI models on under-
  standing personal information through accessing (synthetic) private user data. In Findings
  of the Association for Computational Linguistics: ACL 2025, pp. 878–893, Vienna, Austria, July
  2025b. Association for Computational Linguistics. ISBN 979-8-89176-256-5. doi: 10.18653/
  v1/2025.findings-acl.49. URL https://aclanthology.org/2025.findings-acl.49/.
Meiling Tao, Chenghao Zhu, Dongyi Ding, Tiannan Wang, Yuchen Eleanor Jiang, and
 Wangchunshu Zhou. Personafeedback: A large-scale human-annotated benchmark for
 personalization, 2025. URL https://arxiv.org/abs/2506.12915.


                                              11
Preprint. Under review.




Tiannan Wang, Meiling Tao, Ruoyu Fang, Huilin Wang, Shuai Wang, Yuchen Eleanor Jiang,
  and Wangchunshu Zhou. Ai persona: Towards life-long personalization of llms. arXiv
  preprint arXiv:2412.13103, 2024.
Di Wu, Hongwei Wang, Wenhao Yu, Yuwei Zhang, Kai-Wei Chang, and Dong Yu. Long-
  MemEval: Benchmarking chat assistants on long-term interactive memory. arXiv preprint
  arXiv:2410.10813, 2024.
Rongwu Xu, Zehan Qi, Zhijiang Guo, Cunxiang Wang, Hongru Wang, Yue Zhang, and
 Wei Xu. Knowledge conflicts for llms: A survey. In Proceedings of the 2024 Conference on
  Empirical Methods in Natural Language Processing, pp. 8541–8565, 2024.
Sangyeon Yoon, Sunkyoung Kim, Hyesoo Hong, Wonje Jeung, Yongil Kim, Wooseok Seo,
  Heuiyeen Yeen, and Albert No. BenchPreS: A benchmark for context-aware personalized
  preference selectivity of persistent-memory LLMs. arXiv preprint arXiv:2603.16557, 2026.
Se-eun Yoon, Zhankui He, Jessica Echterhoff, and Julian McAuley. Evaluating large language
  models as generative user simulators for conversational recommendation. In Proceedings
  of the 2024 Conference of the North American Chapter of the Association for Computational
  Linguistics: Human Language Technologies (Volume 1: Long Papers), pp. 1490–1504, Mexico
  City, Mexico, June 2024. Association for Computational Linguistics. doi: 10.18653/v1/
  2024.naacl-long.83. URL https://aclanthology.org/2024.naacl-long.83/.
Yutong Zhang, Dora Zhao, Jeffrey T. Hancock, Robert Kraut, and Diyi Yang. The rise
  of ai companions: How human-chatbot relationships influence well-being, 2025. URL
  https://arxiv.org/abs/2506.12605.
Siyan Zhao, Mingyi Hong, Yang Liu, Devamanyu Hazarika, and Kaixiang Lin. Do llms
  recognize your preferences? evaluating personalized preference following in llms. arXiv
  preprint arXiv:2502.09597, 2025a.
Zheng Zhao, Clara Vania, Subhradeep Kayal, Naila Khan, Shay B Cohen, and Emine Yilmaz.
  PersonaLens: A benchmark for personalization evaluation in conversational AI assistants.
  In Findings of the Association for Computational Linguistics: ACL 2025, pp. 18023–18055,
  2025b.
Lixi Zhu, Xiaowen Huang, and Jitao Sang. A LLM-based controllable, scalable, human-
  involved user simulator framework for conversational recommender systems. In Pro-
  ceedings of the ACM on Web Conference 2025, WWW ’25, pp. 4653–4661, New York,
  NY, USA, 2025. Association for Computing Machinery. ISBN 9798400712746. doi:
  10.1145/3696410.3714858. URL https://doi.org/10.1145/3696410.3714858.
Thomas P Zollo, Andrew Wei Tung Siah, Naimeng Ye, Ang Li, and Hongseok Namkoong.
  PersonalLLM: Tailoring LLMs to individual preferences. arXiv preprint arXiv:2409.20296,
  2024.


A    Extended Related Work

Personalization benchmarks. P REF E VAL (Zhao et al., 2025a) evaluates preference follow-
ing across up to 100K tokens with static preferences. P ERSONA M EM (Jiang et al., 2025a) intro-
duces multi-session histories with temporally grounded profiles; P ERSONA M EM - V 2 (Jiang
et al., 2025b) scales to 128K tokens and reports that dynamic preferences are harder than
static ones (35% vs. 40% accuracy), consistent with our findings, but its evaluation focuses on
implicit preference extraction and cannot isolate whether errors on dynamic preferences re-
flect retrieval failure or belief-update failure. I MPLEX C ONV (Li et al., 2025b) targets implicit
reasoning where life events impose situational constraints, though underlying preferences
remain static. R EAL P REF (Guo et al., 2026) varies expression types across long-horizon
contexts. Other work addresses task-oriented personalization (Zhao et al., 2025b), cross-user
diversity (Zollo et al., 2024), preference selectivity (Yoon et al., 2026), profile-conditioned
retrieval (Salemi et al., 2024; Kumar et al., 2024), persona coverage (Afzoon et al., 2024; Tan


                                               12
Preprint. Under review.




et al., 2025b; Tao et al., 2025), and preference structure (Li et al., 2026; 2025a). These works
establish that LLMs struggle with preference retrieval and long-context recall, but none
independently varies the mechanisms driving preference change. Several treat implicit
vs. explicit expression as a central difficulty axis (Jiang et al., 2025b; Li et al., 2025b; Guo
et al., 2026); our controlled experiments find that expression explicitness modulates over-
all difficulty but does not eliminate belief-update failure (§6.3). Table 1 summarizes key
distinctions.

Long-term memory and knowledge update. M EM B ENCH (Tan et al., 2025a) evaluates
knowledge updating alongside information extraction and temporal reasoning. L O -
C O M O (Maharana et al., 2024) grounds dialogues on temporal event graphs, and L ONG -
M EM E VAL (Wu et al., 2024) tests five memory abilities including knowledge updates. None
of these benchmarks model why tracked information changes or provide controlled ex-
periments isolating difficulty sources. Our belief-update failure finding connects to the
knowledge conflict literature (Xu et al., 2024), where models anchor on prior evidence even
when newer context supersedes it.

User simulation and synthetic data generation. The data generator builds on LLM-
based agent simulation (Park et al., 2023). AI P ERSONA (Wang et al., 2024) and C HAT-
B ENCH (Chang et al., 2025) extend this to life-long personalization, while user simulators
for conversational recommendation (Zhu et al., 2025; Yoon et al., 2024; Sekulic et al., 2024)
focus on single-session tasks. These approaches rely on surface-level prompting without
structured models of preference change. Harry et al. (2026) demonstrate that state-level
variation dominates trait-level variation in user behavior, motivating our mental state graph
approach that models preferences as evolving state. The graph’s typed dependency edges
and evolution provenance enable consistent generation over 6-month timelines.

B   Full Per-Model Results
Table 3 reports accuracy for all 25 models on the combined multi-generator dataset, broken
down by generator and evolution status.

C    Data Generation Statistics
Table 4 provides comprehensive generation and filtering statistics for each generator model
in the H ORIZON B ENCH pipeline.
The pass rate variation across generators is noteworthy. o3-generated items have the lowest
pass rate (5.1%), suggesting that o3 produces counterfactual options that are more frequently
distinguishable without conversational history. Gemini-3-flash has the highest pass rate
(17.6%), indicating its counterfactual options are harder to resolve from response quality
cues alone.

D    Human-in-the-Loop Iteration Details
We conducted three rounds of human annotation during pipeline development to validate
benchmark quality and identify areas for improvement. Each round used 10–20 trained
annotators, with 3 independent annotations per item. Annotators followed a structured
protocol requiring them to (1) review the user profile and conversation history, (2) identify
the target preference attribute, (3) evaluate all five response options, (4) select the best-
aligned response, and (5) provide free-text rationales for their decisions. Annotators also
rated contextual appropriateness and AI persona consistency on binary scales.
Table 5 summarizes quantitative results across rounds.
In Round 2, at least one of three annotators identified the correct answer on 81% of items,
while 19% of items were missed by all annotators, indicating a genuine difficulty floor even
for attentive human raters with full context.


                                              13
Preprint. Under review.




Table 3: Full per-model accuracy (%) on H ORIZON B ENCH. Combined: all generators pooled
(4,245 items from 360 users). By Generator Model: accuracy on subsets produced by each
frontier generator. Preference Type: accuracy on items where the target preference has evolved
vs. remained static. ∆evo = Evolved − Static (pp); all 25 models show negative ∆evo (sign
test p < 0.001). Sorted by combined accuracy.

                                                      By Generator Model                           Preference Type
 Model                 H ORIZON B ENCH      Sonnet-4.5            o3    Gemini-3-flash      Evolved              Static       ∆evo
                             4,245 items    1,052 items    981 items       2,212 items    2,484 items       1,761 items
 Claude-opus-4.5                    52.8            51.2         53.2              53.3            51.3              54.8    −3.5
 Claude-3.7-sonnet                  47.8            49.9         60.8              41.1            46.7              49.5    −2.9
 Claude-opus-4                      45.1            38.3         45.0              46.6            44.4              46.2    −1.8
 Gemini-3.1-pro                     41.2            39.9         45.4              40.0            38.4              45.3    −6.9
 Gemini-3-pro                       40.9            41.0         44.0              39.5            38.4              44.3    −5.9
 Claude-sonnet-4.5                  34.0            30.9         34.9              35.2            32.6              36.0    −3.4
 Claude-3.5-haiku                   32.5            30.8         55.1              23.3            31.8              33.6    −1.9
 Claude-sonnet-4                    32.2            26.6         36.1              31.0            31.4              33.3    −1.9
 Claude-3.5-son.-v1                 29.8            26.8         33.2              29.8            29.2              30.8    −1.6
 Gemini-3-flash                     25.8            23.6         21.2              28.9            24.0              28.3    −4.3
 Gemini-2.0-flash                   24.7            23.1         26.6              24.6            24.2              25.4    −1.1
 gpt-4o                             24.6            24.0         25.4              24.6            23.9              25.7    −1.8
 Claude-haiku-4.5                   23.0            21.3         21.0              24.8            22.0              24.5    −2.6
 Gemini-2.5-pro                     22.8            22.0         21.2              23.9            21.5              24.6    −3.1
 Gemini-2.0-fl.-lite                20.9            19.7         18.7              22.5            20.3              21.8    −1.5
 gpt-4.1                            19.5            22.6         16.2              19.5            19.0              20.3    −1.4
 Gemini-2.5-fl.-lite                19.5            25.3         17.1              17.9            18.2              21.4    −3.2
 o3                                 16.5            19.3         13.7              16.4            14.9              18.8    −3.9
 o1                                 16.0            19.0         11.9              16.4            15.5              16.8    −1.3
 Gemini-2.5-flash                   15.7            14.3         14.5              16.9            14.4              17.5    −3.1
 o4-mini                            15.3            18.6         13.5              14.6            14.4              16.6    −2.3
 Gemini-3.1-fl.-lite                15.1            15.7         10.7              16.7            14.0              16.6    −2.6
 o3-mini                            14.9            14.2         12.4              16.4            14.1              16.0    −1.9
 gpt-5                              13.5            15.9         10.7              13.7            12.2              15.4    −3.2
 gpt-5-mini                         12.5            12.5         11.6              12.9            11.9              13.3    −1.4
 Average                            26.3            25.9         27.0              26.0            25.1              27.9    −2.7


Table 4: Data generation and filtering statistics per generator. Users: number of simulated
user profiles with complete timelines. Conversations/Turns: total and average per-user
counts. Candidates: raw benchmark items generated. Filtered: items passing the strict 5-
LLM consensus filter. Pass rate is filtered/candidates. Of the 120 Claude-sonnet-4.5 users,
14 produced no items that passed the 5-LLM filter; all 120 o3 and Gemini-3-flash users
contributed at least one filtered item. The full 360-user timeline dataset is released, including
users without filtered items, as the underlying mental state graphs remain useful for future
benchmark construction and preference evolution analysis.

 Generator             Users   Convs.      Convs./user      Turns       Turns/user   Candidates           Filtered     Pass rate
 Claude-sonnet-4.5      120    17,048         142          434,233         3,619          13,217           1,052        8.0%
 o3                     120    20,239         169          600,889         5,007          19,108            981          5.1%
 Gemini-3-flash         120    20,103         168          526,260         4,386          12,681           2,212        17.6%
 Combined               360    57,390         159          1,561,382       4,337          45,006           4,245            9.4%



Qualitative analysis of annotator disagreements and errors across rounds revealed several
recurring patterns that informed pipeline improvements:
Insufficiently distinct counterfactual options. In early generations, multiple response
options were near-paraphrases of each other, differing only in minor phrasing while shar-
ing the same underlying preference value. For example, two options might both reflect a
“balanced” challenge comfort zone with nearly identical wording, making the distinction un-
resolvable even for attentive annotators. This led us to strengthen the distractor generation
procedure to ensure each option reflects a meaningfully different attribute value.
Target attribute not reflected in response content. Some generated responses failed to
manifest the intended preference value in their content. For instance, when the target
attribute was investment in research: 3 (moderate), the ground-truth response contained
no mention of research, while an alternative option did. Similarly, responses intended to


                                                            14
Preprint. Under review.




Table 5: Human annotation results across development rounds. Majority-vote accuracy:
fraction of items where the annotator majority matched the ground-truth label. Fleiss κ:
inter-annotator agreement.

                                           Items     Majority Acc.   Fleiss κ
                              Round 1      ∼400             63.7%     0.51
                              Round 2      516              56.4%     0.37



reflect carpooling preference: False nonetheless suggested carpooling in three of four
options. These cases indicated that the counterfactual generation step did not sufficiently
constrain response content to the target attribute value, prompting improvements to the
generation prompt.
Subjective preference dimensions. Certain preference attributes (such as “positivity level,”
“strategic depth,” or “collaboration style”) produced high annotator disagreement because
multiple responses could plausibly satisfy the attribute depending on interpretation. For
example, when the target was positivity level: positive, annotators split between two
responses that were both positive but differed in tone (warm anecdotal vs. pragmatic en-
couraging). These cases reflect inherent subjectivity in preference alignment, not generation
errors, and informed our decision to report inter-annotator agreement as a measure of task
difficulty; we do not treat disagreement as noise.
Numeric attribute leakage. In early generations, some responses explicitly stated numeric
preference values (e.g., “your spontaneity tolerance is at 0.6”) instead of expressing the
preference naturally. When multiple options stated different numeric values, the task
reduced to matching numbers and bypassed preference alignment. This led to prompt
improvements that suppress literal attribute values in generated responses.


E     Generation Prompts

Each stage of the H ORIZON B ENCH pipeline is implemented as one or more LLM generation
calls with structured prompts. Below we present the core prompts for each pipeline stage
described in §4, abbreviated for space. Variables in curly braces (e.g., {user information})
are populated at runtime with the relevant agent states, event context, and preference
metadata.


E.1   Stage 1: Event Sampling

Events are sampled conditional on both agent states and event history. When a stale
preference is selected for temporal recall, the following prompt generates an event relevant
to that preference domain.
 Your Task: Generate an event that would be specifically relevant
 to this user's preference.

 User Information - {user_name}:
 {user_attributes}

 Past Events: {past_events}

 Preference of Interest: {selected_preference}

 Generate an event that would naturally trigger this preference.
 The event should:
 - Be realistic and fit the user's life context
 - Directly involve the preference domain
 - Create a natural opportunity for the preference to be
   expressed or recalled




                                                       15
Preprint. Under review.




E.2   Stage 2: Preference Evolution

When a life event triggers preference evolution, the following prompt generates a single
event that meaningfully alters multiple preferences simultaneously, with explicit causal
reasoning for each change.
Multiple user preferences are about to change due to a SINGLE
significant life event.

USER PROFILE: {user_profile}

PREFERENCES TO EVOLVE: {preferences_block}

Generate ONE realistic life event that would MEANINGFULLY change
at least one attribute in EACH of the preferences listed above.

Requirements:
- The event must be causally connected to ALL the preference
  domains
- It must be plausible for this user's life context
- Changed attributes should be QUALITATIVELY DIFFERENT from
  current values
- Every listed preference must have at least one attribute change

Return JSON:
{
  "event_name": "Brief name of the life event",
  "event_category": "Category (e.g., career, health, ...)",
  "event_description": "1-2 sentence description",
  "preference_changes": {
    "<preference_id>": {
      "<attribute_name>": {
        "new_value": "the new value after the event",
        "reason": "why this event caused this change"
      }
    }
  }
}



E.3   Stage 3: Conversation Generation

Conversation generation proceeds in two steps. First, an outline prompt plans the structural
flow.
Generate a conversation outline for an AI assistant interaction
that feels genuinely human and engaging.

SCENARIO: {scenario}
USER PROFILE: {user_information}
ASSISTANT PROFILE: {assistant_information}

USER'S AI INTERACTION PREFERENCES (unknown to assistant until
expressed): {preferences_updated_user}
ASSISTANT'S KNOWN USER PREFERENCES (from previous conversations):
{preferences_current_user}

CRITICAL LOGICAL CONSTRAINT:
THE ASSISTANT CAN ONLY APPEAL TO:
1. Preferences listed in "assistant_preferences" (already known)
2. Preferences the user has expressed earlier in THIS conversation
THE ASSISTANT CANNOT APPEAL TO unexpressed preferences!


Second, a content prompt fills in the outline with natural dialogue, conditioned on an
expression mode. Three modes control how preferences surface:
[VERBAL MODE]
The user MUST state every single preference in the most direct,
unambiguous language possible. Every preference must be expressed
as a clear declarative statement using phrases like:
- "I strongly prefer X over Y"
- "I always want Z"
- "My preference is specifically for..."

[BEHAVIORAL MODE]
The user's preferences must be nearly invisible in the



                                                         16
Preprint. Under review.




 conversation. They should surface only as fleeting, ambiguous,
 offhand remarks. BANNED: the user must NEVER state, declare,
 or name any preference. NEVER request a format, style, or
 approach. The preference should appear ONLY as:
 1. Passing, throwaway remarks
 2. Anecdotes about third parties
 3. Neutral, ambiguous reactions
 4. Environmental or contextual details
 The GOAL: if you showed the conversation to 10 people, at most
 1-2 would pick up on the vague hint.



E.4   Stage 4: Counterfactual Generation

For each benchmark item, counterfactual assistant turns are generated reflecting alternative
preference values.
 You are generating diverse alternative assistant responses based
 on different preference values.

 CONTEXT: {conversation_context}
 ORIGINAL ASSISTANT RESPONSE: {original_response}

 TEMPORAL PREFERENCE BEING RECALLED:
 - Preference ID: {preference_id}
 - Attribute: {attribute_name}
 - Original value: {original_value}

 TASK: Generate {N} DIVERSE alternative responses that each
 reflect a different preference value. Each response should:
 1. Naturally reference the specific alternative preference value
 2. Maintain the same conversational tone and helpfulness
 3. Be significantly different from the others
 4. Keep the same general structure but vary the preference content



E.5   5-LLM History Validation

Each candidate item is presented to five validation models without the full conversation
history to test whether it is answerable from surface cues alone.
 You are evaluating which AI assistant response would be MOST
 APPROPRIATE for a user, based ONLY on the conversation context
 provided.

 IMPORTANT: You are shown a SUBSET of this user's conversation
 history. There may be earlier conversations where the user
 expressed preferences that you CANNOT see.

 CONVERSATION CONTEXT ({N} intermediate conversations + current
 conversation up to this point): {context}

 RESPONSE OPTIONS: {options}

 TASK: Based ONLY on the visible conversations above, which option
 seems most appropriate?
 - You do NOT have access to the user's full history
 - Do NOT assume any prior knowledge about this user's preferences
 - Do NOT use stereotypes or demographic assumptions
 - Choose based ONLY on what's visible in the conversations




F     Per-Model Controlled Experiment Results

Tables 6–7 report per-model belief-update metrics for the controlled experiments summa-
rized in Table 2. For each model we report overall accuracy, accuracy on static and evolved
items, the evolved-vs-static gap (∆), and the pre-evolution distractor selection rate (Dist.%;
chance = 25%). Models are sorted by overall accuracy.




                                                       17
Preprint. Under review.




Table 6: Per-model results: Neutral (unmodified) condition (981 items: 375 static, 606
evolved) and Short-horizon condition (0–14 day recall, 120 users, 1,778 items: 1,545 static,
233 evolved).
                   Neutral (unmodified)                                           Short-horizon
  Model             All    Sta.   Evo.      ∆    Dist.        Model            All    Sta.    Evo.       ∆    Dist.
  Cl-3.7-sonnet    60.8    61.1    60.6   −0.5    36.6        Cl-opus-4.5      66.2   67.1    60.5     −6.5    50.7
  Cl-3.5-haiku     55.1    57.9    53.5   −4.4    39.3        Cl-3.7-sonnet    61.6   63.4    49.8    −13.6    43.5
  Cl-opus-4.5      53.2    54.4    52.5   −1.9    38.6        Gem-3-pro        56.7   57.0    55.4     −1.6    43.5
  Gem-3.1-pro      45.4    48.8    43.2   −5.6    34.8        Gem-3.1-pro      56.7   57.0    54.5     −2.5    40.9
  Cl-opus-4        45.0    49.5    42.2   −7.3    37.5        Cl-opus-4        56.4   56.9    53.2     −3.7    46.5
  Gem-3-pro        44.0    48.0    41.6   −6.4    33.8        Cl-sonnet-4      47.8   48.8    40.8     −8.0    46.4
  Cl-sonnet-4      36.1    39.0    34.3   −4.6    39.7        Cl-3.5-haiku     46.4   49.0    29.6    −19.4    52.8
  Cl-sonnet-4.5    34.9    38.4    32.7   −5.7    39.9        Cl-sonnet-4.5    45.3   46.1    40.3     −5.7    46.3
  Cl-3.5-son.-v1   33.2    32.5    33.7   +1.1    39.2        Cl-3.5-son.-v1   35.7   35.9    35.0     −0.9    36.6
  Gem-2.0-flash    26.6    28.5    25.4   −3.1    34.8        Gem-2.0-flash    30.1   30.4    27.9     −2.5    44.5
  gpt-4o           25.4    28.5    23.4   −5.1    39.2        gpt-4o           28.4   29.2    23.2     −6.0    59.7
  Gem-2.5-pro      21.2    24.5    19.1   −5.4    40.3        Cl-haiku-4.5     26.0   26.9    20.2     −6.7    50.3
  Gem-3-flash      21.2    23.5    19.8   −3.7    40.2        Gem-2.5-pro      25.9   27.0    18.5     −8.5    48.7
  Cl-haiku-4.5     21.0    24.3    19.0   −5.3    39.2        Gem-3-flash      24.9   26.0    17.6     −8.4    50.6
  Gem-2.0-fl.lt    18.7    21.1    17.2   −3.9    40.1        Gem-2.0-fl.lt    21.3   21.9    17.2     −4.7    46.8
  Gem-2.5-fl.lt    17.1    17.6    16.8   −0.8    36.9        Gem-2.5-fl.lt    17.5   18.1    13.7     −4.4    50.3
  gpt-4.1          16.2    18.1    15.0   −3.1    42.4        Gem-2.5-flash    16.4   17.0    12.4     −4.5    41.1
  Gem-2.5-flash    14.5    15.2    14.0   −1.2    37.5        gpt-4.1          15.9   16.7    10.7     −6.0    53.9
  o3               13.7    14.9    12.9   −2.1    37.6        o3               14.7   15.1    12.4     −2.6    45.1
  o4-mini          13.5    13.6    13.4   −0.2    36.0        o4-mini          13.2   13.9     8.6     −5.3    47.0
  o3-mini          12.4    12.3    12.5   +0.3    36.5        gpt-5            12.9   13.1    11.6     −1.6    45.4
  o1               11.9    12.0    11.9   −0.1    37.7        Gem-3.1-fl.lt    12.8   13.8     6.0     −7.8    49.4
  gpt-5-mini       11.6    10.9    12.0   +1.1    40.3        gpt-5-mini       11.1   11.7     7.7     −3.9    52.0
  Gem-3.1-fl.lt    10.7    11.7    10.1   −1.7    39.0        o1               11.1   11.5     8.2     −3.4    51.8
  gpt-5            10.7    12.0     9.9   −2.1    37.6        o3-mini          10.3   10.8     7.3     −3.5    49.4
  Avg.             27.0    28.9    26.0   −2.9    38.2        Avg.             30.6   31.4    25.7    −5.7     47.7




Table 7: Per-model results: Explicit rewrite condition (981 items: 375 static, 606 evolved; 25
models) and Implicit rewrite condition (981 items: 375 static, 606 evolved; 25 models).
                     Explicit rewrite                                            Implicit rewrite

  Model             All    Sta.   Evo.      ∆    Dist.        Model             All    Sta.   Evo.       ∆    Dist.
  Cl-3.5-haiku     68.2    70.8    66.6   −4.2    57.6        Cl-opus-4.5      57.7   62.4     54.8   −7.6     66.8
  Cl-3.7-sonnet    64.4    63.5    65.0   +1.5    43.8        Gem-3.1-pro      48.7   53.2     45.9   −7.3     53.4
  Cl-opus-4.5      60.2    62.3    59.0   −3.3    52.1        Cl-3.7-sonnet    47.3   45.7     48.2   +2.5     56.4
  Gem-3.1-pro      45.9    49.1    43.9   −5.2    46.9        Cl-3.5-haiku     45.7   46.3     45.4   −0.9     59.0
  Gem-3-pro        44.0    48.5    41.3   −7.3    45.0        Cl-opus-4        43.1   46.7     40.9   −5.7     63.0
  Cl-opus-4        42.6    46.4    40.3   −6.1    53.2        Gem-3-pro        39.9   45.1     36.8   −8.3     49.5
  Cl-3.5-son.-v1   37.7    39.7    37.1   −2.6    26.0        Cl-sonnet-4.5    37.9   42.4     35.1   −7.3     63.1
  Cl-sonnet-4      35.5    35.2    35.6   +0.4    48.6        Cl-sonnet-4      37.7   41.1     35.6   −5.4     62.1
  Cl-sonnet-4.5    35.5    35.5    35.5   +0.0    57.3        Cl-3.5-son.-v1   29.7   29.5     29.6   +0.1     43.4
  gpt-4o           25.3    27.5    23.9   −3.5    59.0        Gem-2.0-flash    24.6   28.5     22.1   −6.4     56.0
  Gem-2.0-flash    25.1    26.4    24.3   −2.1    44.4        gpt-4o           24.0   26.9     22.1   −4.8     63.7
  Gem-2.5-pro      21.7    23.5    20.6   −2.8    49.1        Gem-3-flash      23.1   29.1     19.5   −9.6     66.9
  Cl-haiku-4.5     20.3    21.1    19.8   −1.3    48.0        Gem-2.5-pro      22.7   27.5     19.8   −7.7     58.6
  Gem-3-flash      20.3    21.9    19.3   −2.6    53.5        Cl-haiku-4.5     20.9   25.3     18.2   −7.2     60.3
  Gem-2.0-fl.lt    17.8    19.7    16.7   −3.1    53.7        Gem-2.0-fl.lt    19.3   22.4     17.3   −5.1     60.9
  Gem-2.5-fl.lt    17.6    16.8    18.2   +1.4    56.8        Gem-2.5-flash    16.1   19.5     14.0   −5.4     53.0
  gpt-4.1          15.8    14.7    16.5   +1.8    56.5        o4-mini          15.8   16.0     15.7   −0.3     56.7
  Gem-2.5-flash    14.8    17.1    13.4   −3.7    51.5        Gem-2.5-fl.lt    15.5   14.9     15.8   +0.9     57.9
  o4-mini          14.8    14.1    15.2   +1.0    47.2        gpt-4.1          14.9   15.5     14.5   −0.9     66.0
  o3               12.9    12.8    13.0   +0.2    45.9        o3               14.1   14.4     13.9   −0.5     56.7
  o3-mini          12.4    12.0    12.7   +0.7    48.8        o1               13.8   13.6     13.9   +0.3     58.1
  o1               12.1    12.8    11.7   −1.1    47.6        gpt-5            13.5   12.5     14.0   +1.5     57.0
  gpt-5            11.0    10.1    11.6   +1.4    47.1        o3-mini          12.8   13.1     12.7   −0.4     58.2
  gpt-5-mini       10.8    11.7    10.2   −1.5    47.6        gpt-5-mini       12.6   13.6     12.0   −1.6     62.4
  Gem-3.1-fl.lt    10.0    11.2     9.2   −2.0    55.8        Gem-3.1-fl.lt     9.5   10.9      8.6   −2.4     59.6
  Avg.             27.9    29.0    27.2   −1.8    49.7        Avg.             26.4   28.6     25.0   −3.6     58.8




                                                         18
Preprint. Under review.




Table 8: Per-model results: Low-subtlety condition (majority ≥3/5 filter, 3,628 items: 1,485
static, 2,143 evolved). Relaxing the filter admits easier items, raising overall accuracy while
the belief-update pattern persists.
                           Model            All    Sta.   Evo.     ∆    Dist.
                           Cl-opus-4.5      73.7   75.6   72.5   −3.1    55.4
                           Cl-3.7-sonnet    73.0   74.5   72.0   −2.5    51.0
                           Gem-3.1-pro      65.4   67.3   64.1   −3.2    48.3
                           Gem-3-pro        65.1   67.5   63.5   −4.1    48.7
                           Cl-opus-4        62.8   64.8   61.5   −3.4    54.1
                           Cl-3.5-haiku     60.3   62.6   58.7   −3.8    58.4
                           Cl-sonnet-4      54.5   55.1   54.1   −0.9    54.2
                           Cl-sonnet-4.5    50.3   52.5   48.9   −3.6    59.1
                           Cl-3.5-son.-v1   44.5   43.9   44.9   +1.0    51.1
                           Gem-2.5-pro      36.9   39.9   34.8   −5.1    55.3
                           Cl-haiku-4.5     35.6   37.0   34.7   −2.4    57.6
                           gpt-4o           35.5   37.4   34.1   −3.3    60.7
                           Gem-2.0-flash    35.4   35.5   35.3   −0.2    46.8
                           Gem-3-flash      33.3   36.7   30.9   −5.8    57.2
                           Gem-2.0-fl.lt    26.1   27.1   25.4   −1.7    53.6
                           gpt-4.1          25.0   25.1   25.0   −0.2    60.0
                           Gem-2.5-fl.lt    24.4   28.4   21.7   −6.7    61.3
                           Gem-2.5-flash    24.3   27.7   22.0   −5.7    52.8
                           o3               24.0   23.4   24.4   +1.0    51.4
                           o4-mini          22.5   22.5   22.4   −0.0    49.9
                           gpt-5            21.5   20.3   22.4   +2.1    51.1
                           o1               19.7   20.8   18.9   −1.9    53.0
                           gpt-5-mini       19.7   20.3   19.2   −1.2    54.8
                           Gem-3.1-fl.lt    19.6   21.4   18.3   −3.1    56.9
                           o3-mini          18.8   20.9   17.4   −3.5    54.1
                           Avg.             38.9   40.3   37.9   −2.5    54.3




                                                   19
