---
source_url: https://arxiv.org/abs/2606.23491
source_pdf: https://arxiv.org/pdf/2606.23491
id: "arXiv:2606.23491v1"
title: "Hallucinations in Organization-backed AI advisors: Evidence about Skepticism, Verification, and Reliance in Goal-Directed Use"
authors: Simon J. Blanchard (Georgetown), Aaron M. Garvey (U. Tennessee), Laura O'Laughlin (Analysis Group)
published: 2026-06-22
primary_category: cs.HC
tags: [hallucinations, ai-advisors, skepticism, verification, reliance, consumer-deception, organization-backed-ai]
sha256:
ingested: 2026-06-23
---

# Hallucinations in Organization-backed AI advisors: Evidence about Skepticism, Verification, and Reliance in Goal-Directed Use

**arXiv:** 2606.23491v1 [cs.HC, cs.CY] — 22 June 2026
**Authors:** Simon J. Blanchard*, Aaron M. Garvey, Laura O'Laughlin
**Affiliations:** Georgetown University; University of Tennessee; Analysis Group, Montreal

## Full Extracted Text

<!-- Raw PDF text below -->

        Hallucinations in Organization-backed AI advisors: Evidence about Skepticism,
                        Verification, and Reliance in Goal-Directed Use

                   Simon J. Blancharda,*, Aaron M. Garveyb, Laura O’Laughlinc

a
    McDonough School of Business, Georgetown University, 37th and O Streets NW, Washington,
                                         DC 20057, USA
    b
      Haslam College of Business, University of Tennessee, 916 Volunteer Boulevard, Knoxville,
                                         TN 37996, USA
                           c
                             Analysis Group, Montreal, Quebec, Canada

                     * Corresponding author. Email: sjb247@georgetown.edu


Abstract
Generative AI systems are increasingly used by organizations to deliver information to
consumers, patients, students, employees, and citizens. These systems can hallucinate, producing
plausible but inaccurate responses. A central question for AI-advised decisions is therefore not
only whether users rely on inaccurate information, but whether they recognize that a response
may require verification. To answer this question, we review emerging empirical evidence
relevant to hallucination detection in goal-directed interactions, with a focus on organization-
backed AI advisors. We distinguish three constructs that existing studies often conflate: whether
users are skeptical of information presented, whether they check it, whether checking succeeds,
and whether the result of user verification affects reliance on the information. Across studies
examining product search, medical decision-making, content generation, and chatbot-assisted
tasks, several patterns emerge. Nearly all studies measure reliance, while variables such as user
skepticism and verification of the information are more often targeted by an intervention than
measured directly. The cues used to prompt scrutiny of the AI response are predominantly
related to the AI output, such as source citations, and the most deployable of these AI output
interventions for organizations – general and specific warnings about the risk of hallucinations –
show the weakest and most mixed effects in the studies reviewed. Although the existing
literature posits that users may be more likely to scrutinize responses related to particular areas
of content, no studies varied the content category, leaving this question open for further research.
In future research, measuring skepticism and verification separately from reliance may clarify
what current evidence shows, what it only implies, and which questions require further
exploration.


Keywords: Generative AI; hallucination; detection; skepticism; verification; reliance; trust;
organization-backed AI advisor; chatbot; disclosure; human-AI interaction


1. Introduction
Organizations increasingly use generative AI systems as tools to assist customers, patients,
students, employees, and citizens in completing ordinary tasks such as obtaining information
about a reservation. Despite their utility, such systems can produce plausible but inaccurate
responses. When incorrect information is provided by an AI tool, do users notice and act on the
problem while pursuing their goals?

Our review examines the existing literature on interactions between individuals and a
conversational AI that involve a risk of hallucination. We use the natural-language-generation
term “hallucinated information” to refer to plausible generated output that is unfaithful to the
relevant source, policy, evidence base, or decision context [2]. We define “organization-backed
AI advisors” as systems offered through an organizational channel or in a context in which users
reasonably treat the system as providing information on the organization’s behalf (e.g., service
chatbots, medical assistants, employer knowledge tools). In these settings, users are typically
engaged in task completion rather than explicit evaluation of the system’s accuracy.

For organization-backed AI advisors, hallucination detection can be usefully separated into three
constructs: skepticism, verification, and reliance. We define skepticism as recognizing that a
response may be inaccurate or require verification; verification as the act of checking the
accuracy of the response against one or more other sources; and reliance as whether the response
affects the user's decision. These constructs are distinct: users may recognize that an answer
requires checking yet still rely on it, or reject an answer without verifying a specific error. The
distinction follows work in trust in automation and appropriate reliance, which separates
attitudes toward systems from behavioral use [3,4,28].

Skepticism may arise through at least two pathways. Output-based skepticism is prompted by
features of the response itself, such as implausibility, inconsistency, or conflict with prior
knowledge. Category-based skepticism is prompted by knowledge that certain content types,
such as numerical claims, policy provisions, medical guidance, and citations, might be more
error-prone or higher-stakes. Once skepticism arises, the user may verify the answer and
verification may or may not change reliance (see Figure 1).




Figure 1. Constructs in the study of AI-advised decisions. Skepticism, verification, and reliance are
conceptually distinct behavioral constructs: Users may be skeptical without verifying, verify without
successfully detecting an error, or rely on a response without verifying it. Post-use reflections (satisfaction
with the interaction, confidence in the answer) are retrospective appraisals. Table 1 classifies each
reviewed study by its primary focus: skepticism, verification, or reliance. Most studies also collect some
measure of post-use reflection; because such measures are near-ubiquitous, we distinguish them
conceptually here but do not track them as a separate focus in Table 1 or in the text.

Our review topic connects to research on misinformation, source evaluation, and correction, but
the interactional setting differs from many standard paradigms in that literature. Users of
organization-backed AI advisors are typically trying to complete a task rather than explicitly
evaluate whether a claim is true. Spontaneous veracity assessments in cooperative
communication are relatively infrequent absent an active trigger [6], and researchers have
posited that consistent use of GenAI for task completion may lead users to delegate
metacognitive oversight to the system, resulting in a state of “cognitive surrender” [32].
However, consumer tendencies to accept unverified outputs from organization-backed AI
advisors, and the factors contributing to such acceptance, remain open questions.

Whether such generalizations extend to organization-backed AI advisors can be assessed by
considering evidence that measures the antecedents of reliance, namely skepticism and
verification, rather than reliance alone. As this review shows, data on organization-backed
advisors are rare, and fewer studies have measured these antecedents directly. Establishing
whether organization-backed AI advisors meaningfully reduce users' scrutiny, therefore, requires
evidence that the field has yet to produce. In the sections that follow, we review evidence on
skepticism, verification, and reliance in goal-directed AI use; consider organizational and policy
responses; and outline open methodological and psychological questions.


2. Skepticism, verification, and reliance in goal-directed use
Direct studies of how consumers are skeptical of, verify and rely upon hallucinations by
organization-backed AI advisors in real settings remain rare. Much of the available evidence,
summarized in Table 1, comes from adjacent goal-directed paradigms, including AI-assisted
search, question answering, simulated AI advice, content generation, and chatbot-assisted tasks.
Two features stand out about these studies. First, nearly every study includes some measure of
reliance, whereas the constructs upstream of reliance – namely, skepticism and verification – are
often left implicit and unmeasured. Second, the studies vary according to 1) the measured
construct and 2) the type of cue manipulated to influence outcomes – that is, whether it
originates in features of the response (output-based) or in the content category (category-based).
We make several observations.

First, most studies that manipulate cues to prompt scrutiny of AI-generated information rely on
output-based cues (i.e., cues present in the responses, such as inconsistencies or cited sources).
Indeed, correct and hallucinated responses can share fluency, confidence, and rhetorical
coherence, and thus output-based skepticism may depend most on content features that make a
possible error visible, such as marking uncertain elements, quantifying confidence, or providing
sources [19,20]. Among these, the more reliable effects arise from response features that lower
verification costs. Source citations and noticeable inconsistencies are associated with reduced
reliance on incorrect responses, whereas explanations alone can increase reliance on both correct
and incorrect responses [11]. Sources lower the marginal cost of verification; explanations may
instead make an answer feel complete without making it easier to evaluate. Other output-based
cues that have been shown to move behavior are less easily translated to deployment, such as
token-level highlighting (e.g., marker-style highlighting of parts of the response for which the
model lacks confidence) or explicit statements that no source data exist, which an organization-
backed AI advisor is unlikely to surface on its own. The output-based cues most feasible for
organizations to implement, such as general and specific warnings, tend to show weaker and
more mixed evidence, a point the disclosure literature in Section 3 develops further.

Second, a smaller set of studies examine user scrutiny in specific category, asking whether users
scrutinize an answer more when its subject matter is recognized as error-prone or high-stakes.
Here, the evidence separates general from targeted information. Generic “ChatGPT can make
mistakes” warnings did not alter diagnostic advice-taking relative to a no-warning control [23],
and source-focused interventions increased general skepticism toward AI without reducing the
influence of specific AI-generated misinformation [24]. More targeted information appears more
promising: Descriptions of the model’s behavior that identify where an AI system tends to fail
improved error verification and appropriate reliance across three domains [25], and aligning
LLM explanations with the model’s actual internal confidence narrowed the gap between user
confidence and model accuracy [26].

Across these studies, one useful distinction is whether an intervention directs users’ scrutiny
toward specific higher-risk content rather than merely reminding them that errors are possible. A
limitation runs through this group, however: Where content category is treated as the source of
scrutiny, it is typically held fixed, with medical stimuli throughout, for example, rather than
contrasted against a lower-risk category in the same design. Because the category is not varied,
heightened scrutiny cannot be attributed to it, and the category-based pathway is assumed to
operate rather than shown to do so.

Third, what the literature less often establishes is the process between cue and reliance. The
manipulations are largely aimed at skepticism and verification, yet the outcomes recorded are
most often reliance, so the intervening steps are often assumed from a downstream shift rather
than observed directly. Few studies measure skepticism itself, whether in the moment or
retrospectively, so whether skepticism moved is often inferred from a change in reliance. A
related substitution occurs when self-report stands in for behavior. Participants in an LLM-search
experiment reported a more satisfying experience with the LLM search tool even when the
participants’ decisions were less accurate [7]. AI advisor responses with explanations increased
perceived response quality, reduced follow-up questions, and increased reliance on incorrect
responses [11]. In organizational AI contexts, a branded interface may further complicate users’
calibration, though this is understudied. The implication is that satisfaction with the interaction
and self-reported confidence in the response are not sufficient proxies for appropriate reliance,
and final decision accuracy is only an indirect proxy for skepticism and verification. Behavioral
traces, including source consultation, answer revision, and repeated model reference, may offer a
more direct window into these processes [17].


                Setting and user         How AI error was                                 Behavioral outcome       Primary
 Study                                                                Cue type
                goal                     introduced                                       measured                 focus
                                                                      Output-based
                                         Incorrect AI suggestions                         Disagreement with the
 Buçinca et     Nutrition decisions                                   (uncertainty,                                Skepticism;
                                         paired with cognitive                            AI; downstream
 al. [15]       with AI suggestions                                   suggestion                                   reliance
                                         forcing functions                                decision accuracy
                                                                      framing)
                LLM-based vs.
                                         LLM occasionally                                 Final purchase-
 Spatharioti    traditional search;                                   Output-based                                 Skepticism;
                                         provides incorrect                               decision accuracy;
 et al. [7]     consumer product                                      (highlight)                                  reliance
                                         product information                              search depth
                choice (cars)
                                         Incorrect answers paired
                LLM-infused search
 Kim et al.                              with first-person or         Output-based        Self-reported reliance   Verification;
                engine; medical
 [12]                                    impersonal uncertainty       (uncertainty)       and answer accuracy      reliance
                information seeking
                                         language
                                                                                          Reliance on incorrect
                LLM-infused              Incorrect answers with                           answers; follow-up
 Kim et al.                                                           Output-based                                 Verification;
                application; objective   or without explanations                          questioning on
 [11]                                                                 (sources)                                    reliance
                question answering       and sources                                      confidence and
                                                                                          verification
                AI-assisted tasks                                     Category-based
                                         AI errors with/without                           Error detection rate
 Cabrera et     across three domains                                  (Describing AI’s                             Verification;
                                         high-level failure-pattern                       and appropriate
 al. [25]       with behavior                                         accuracy for the                             reliance
                                         descriptions                                     reliance
                descriptions                                          context)



                                         Confident incorrect
                                                                      Output-based        Choosing the model
 Zhou et al.    Trivia answering with    model output, with and                                                    Verification;
                                                                      (confidence         answer over
 [10]           deployed LLMs            without epistemic                                                         reliance
                                                                      markers)            independent lookup
                                         markers



                Content-grounded data    Hallucinated source          Output-based        Whether users copy,
 Ashktorab                                                                                                         Verification;
                generation with an       content embedded in the      (formulate, read-   append, edit, or
 et al. [16]                                                                                                       reliance
                LLM assistant            workflow                     first, highlight)   correct AI text
                LLM-assisted tasks:                                                       Behavioral patterns:
                                         Plausible misinformation     Output-based
 Liu et al.     quiz solving, article                                                     copy-paste,              Verification;
                                         injected into LLM            (screen shows
 [17]           summarization, and                                                        comprehension depth,     reliance
                                         responses                    open search page)
                trip planning                                                             repeated reference
                Medical students using   Standard “ChatGPT can
 Kıyak et al.                                                         Output-based        Diagnostic advice-
                ChatGPT for              make mistakes” warning                                                    Reliance
 [23]                                                                 (general warning)   taking behavior
                diagnostic reasoning     vs. no warning
                  Setting and user          How AI error was                               Behavioral outcome       Primary
 Study                                                                 Cue type
                  goal                      introduced                                     measured                 focus
                                            AI-generated
                  Misinformation                                       Output-based
 Spearing et                                misinformation                                 Belief accuracy and
                  evaluation with AI-                                  (sources; general                            Reliance
 al. [24]                                   with/without                                   sharing intentions
                  generated content                                    disclaimer)
                                            countermeasures
                  Knowledge-intensive                                                      Reliance on incorrect
                                                                       Output-based
 He et al. [27]   tasks with AI             AI outputs                                     AI outputs conditional   Reliance
                                                                       (explanation)
                  assistance                                                               on perceived expertise
                  Debate interactions                                  Category-based      Change in stated
 Salvi et al.
                  with GPT-4 on             None                       (personalized       opinion pre- to post-    Reliance
 [22]
                  political topics                                     description)        interaction
                                            Incorrect predictions                          Acceptance of the
 Vasconcelos      Maze-solving with                                    Output-based
                                            accompanied by                                 incorrect AI             Reliance
 et al. [5]       simulated AI advice                                  (explanations)
                                            explanations                                   prediction
                                                                       Output-based        Overreliance and
                  LLM advice on LSAT        Erroneous LLM outputs
                                                                       (disclaimer,        appropriate reliance,
 Bo et al. [14]   and numerical-            paired with reliance                                                    Reliance
                                                                       highlighting,       with confidence
                  estimation problems       interventions
                                                                       implicit answer)    calibration
                  LLM as medical
                  assistant for the         Naturalistic LLM errors                        Condition
 Bean et al.
                  general public;           across ten clinical        None                identification and       Reliance
 [8]
                  identify condition and    scenarios                                      disposition accuracy
                  disposition
                  AI-generated user         Persona fabricates a       Output-based        Whether the user
 Kaate et al.
                  persona for product       response to an             (mentions of no     adopts the fabricated    Reliance
 [9]
                  research                  unanswerable question      data)               response
                  Management                                           Category-based      Quality of output;
 Dell’Acqua       consulting tasks (field   Tasks inside vs. outside   (prompt             reliance on AI for
                                                                                                                    Reliance
 et al. [31]      experiment with BCG       AI capability frontier     engineering         tasks beyond its
                  consultants)                                         training)           frontier
                                            Hallucinated answers                           Signal-detection
 Pak et al.       Difficult quiz with                                  Output-based
                                            interleaved with correct                       sensitivity and          Reliance
 [13]             chatbot assistant                                    (politeness)
                                            ones                                           response bias

Table 1. “Cue type” indicates whether the manipulated cue originates in features of the response (output-based) or
in the content category (category-based). “Primary focus” indicates which constructs the study focuses on, which
may be more than one. Studies are grouped by primary focus: skepticism, then verification, then reliance.

3. Organizational and policy responses

We have examined how users are skeptical of, verify, and rely upon AI advisors in adjacent
settings. We now ask how organizations handle hallucination risks. Organizations often mitigate
hallucination risks through at least two kinds of responses, a system-side response and a user-
side response, and the two act at different points.

The system-side response aims to reduce the frequency of hallucinations. For example, retrieval-
augmented generation (RAG) architectures can, when properly designed, ground responses in
verified knowledge bases, and human-in-the-loop review can provide a mechanism for
independent verification before some outputs reach users [30,36]. Both can improve the
information itself and operate before the user encounters it [18,21].

The user-side response does not primarily improve the underlying accuracy of the information
output but shapes how the user responds to it. Disclaimers, interface labels, source citations, and
uncertainty cues attempt to make users recognize that a response may require checking, verifying
it, and relying on it appropriately. Article 50 of the EU AI Act partly reflects this transparency
logic, requiring that users be informed and that AI-generated content be identifiable [33].

We focus on user-side response for two reasons. First, its levers are the output-based and
category-based cues we reviewed in Section 2, so asking whether they shift skepticism,
verification, and reliance is the same question the reviewed evidence addresses. Second,
reducing hallucinations does not remove the need to understand user-side responses. Even when
models perform well on their own, assisted users often do not. For example, in the medical
domain, lay users supported by frontier models identified relevant conditions and chose
appropriate dispositions less often than the models scored in isolation, and no better than users
relying on their ordinary resources, suggesting that the gap can arise from the interaction, not
only from model-level error [8].

In the user-side response, disclosure dominates, and it seems to mostly address skepticism.
Disclaimers and labels aim to make users aware that any response may require checking, without
specifying which responses or content categories warrant it. Yet the evidence that such warnings
change behavior is weak and mixed: a general warning did not significantly increase advice-
taking compared with a no-warning control, and a source-focused intervention increased general
skepticism toward AI but did not significantly reduce the influence of specific AI-generated
misinformation [23,24].
While disclosure may serve to limit the organization's liability, that protection appears limited. In
Moffatt v. Air Canada [1], the tribunal rejected the airline’s argument that its chatbot was a
separate entity and held the organization responsible for misleading information delivered
through its website, despite the availability of correct information elsewhere on the website.
Courts in several jurisdictions have sanctioned attorneys for submitting AI-generated filings
containing fabricated citations or other false authorities [34,37,38], framing those false
authorities as failures of professional verification rather than as excusable tool errors [39].
Across these examples, responsibility appears to attach to how organizations and professionals
verify AI-assisted outputs, not merely to whether the possibility of error was disclosed.

The broader record points the same way. Public databases of legal hallucination cases show that
hallucinated materials continue to reach formal proceedings, suggesting that awareness, policies
or general warnings may be insufficient when verification remains optional, burdensome, or easy
to bypass [41]. Similarly, AI hallucination-related risk disclosures in corporate governance
materials indicate that AI error risk is increasingly being treated as an organizational issue rather
than merely a user-interface design issue [35]. Organizations should be cautious about assuming
that users will be skeptical or that verification will occur simply because users have been warned.

The same organization that posts a disclaimer also markets its system, and marketing can
suppress the skepticism the disclaimer is meant to raise. Promoting an AI tool as reliable or
already vetted invites users to treat its output as checked rather than as something to verify. In
2024, the U.S. Federal Trade Commission launched Operation AI Comply, targeting allegedly
deceptive AI capability-related claims across legal, security, and content-generation tools
[42,43,44], reflecting broader concerns about AI-washing and unsubstantiated capability claims.
Whether an AI label raises or lowers skepticism is therefore an empirical question, and the
answer is unlikely to be uniform.

The evidence reviewed here suggests that warnings and labels are unlikely, on their own, to
make users skeptical of, or appropriately reliant on, the answers organization-backed AI advisors
provide. The legal examples point in a similar direction: tribunals and courts have treated AI
errors as matters of organizational or professional responsibility, not as problems solved by
generic disclosure alone. Reducing reliance on hallucinations is therefore likely to depend less on
warnings that errors are possible than on whether the interaction makes higher-risk content
visible and verification feasible.

4. Open psychological, methodological, and organizational questions

Field studies of organization-backed AI advisors and how users respond to their hallucinations
are rare, and the framework points to what such studies should measure. Reliance, the outcome
these studies most often record, can follow from skepticism, attempted verification, or successful
verification, and these should not be conflated. Work that aims to generalize to organization-
backed AI advisors should measure skepticism, verification, and reliance separately.

One noteworthy avenue for future research is that category-based skepticism (scrutinizing
plausible output because the content type is recognized as higher risk) remains understudied.
Users’ ability and proclivity to scrutinize output from LLMs may depend on users’ individual
understanding of the competence boundaries of AI systems [29], although evidence from
knowledge-work settings suggests that even domain experts may struggle to identify where AI
systems are likely to perform poorly [31]. Future work should examine what forms of training,
interface support, or task-specific feedback help improve recognition of higher-risk content
categories over repeated interaction.

Additionally, empirical work on stable individual differences remains limited in this literature.
Potentially relevant factors include prior experience, metacognitive self-monitoring, and
confidence in both the AI system and one’s task knowledge [15, 40]. Existing findings suggest
that confidence profiles may matter: Confidence in GenAI was associated with less critical
thinking, while task-specific self-confidence was associated with more [40]. This suggests that
skepticism and verification may depend not only on system design, but also on how users
calibrate confidence in the tool and in their own task knowledge.


References and recommended reading
Papers of particular interest, published within the period of review, have been highlighted as:

* of special interest
** of outstanding interest

[1] Moffatt v Air Canada, 2024 BCCRT 149.
[2] Ji Z, Lee N, Frieske R, et al. Survey of hallucination in natural language generation. ACM Comput Surv
        2023;55:Article 248. https://doi.org/10.1145/3571730.
[3] Lee JD, See KA. Trust in automation: designing for appropriate reliance. Hum Factors 2004;46:50-80.
       https://doi.org/10.1518/hfes.46.1.50_30392.
[4] Schemmer M, Kuehl N, Benz C, Bartos A, Satzger G. Appropriate reliance on AI advice: conceptualization and
       the effect of explanations. In: Proceedings of the 28th International Conference on Intelligent User Interfaces.
       ACM; 2023, p. 410-22. https://doi.org/10.1145/3581641.3584066.
[5] Vasconcelos H, Jörke M, Grunde-McLaughlin M, Gerstenberg T, Bernstein MS, Krishna R. Explanations can
      reduce overreliance on AI systems during decision-making. Proc ACM Hum-Comput Interact
      2023;7(CSCW1):Article 129. https://doi.org/10.1145/3579605.
[6] Clare DD, Levine TR. Documenting the truth-default: the low frequency of spontaneous unprompted veracity
       assessments in deception detection. Hum Commun Res 2019;45:286-308. https://doi.org/10.1093/hcr/hqz001.
[7] Spatharioti SE, Rothschild DM, Goldstein DG, Hofman JM. Effects of LLM-based search on decision making:
      speed, accuracy, and overreliance. In: Proceedings of the 2025 CHI Conference on Human Factors in
      Computing Systems. ACM; 2025. https://doi.org/10.1145/3706598.3714082.
[8]* Bean AM, Payne RE, Parsons G, et al. Reliability of LLMs as medical assistants for the general public: a
      randomized preregistered study. Nat Med 2026;32:609-15. 10.1038/s41591-025-04074-y.
      In a randomized study with 1,298 participants across ten clinical scenarios, lay users assisted by GPT-4o,
      Llama 3, or Command R+ identified relevant conditions in fewer than 34.5% of cases and selected
      appropriate dispositions in fewer than 44.2%, despite the same models scoring 94.9% and 56.3% respectively
      when tested alone, and despite assisted participants performing no better than a control group using their
      usual resources. The study documents that strong model-alone performance is insufficient to translate into
      appropriate consumer use, and that interactional breakdown rather than model failure alone accounts for the
      gap.

[9] Kaate I, Salminen J, Jung SG, Xuan TTT, Häyhänen E, Azem JY, Jansen BJ. “You always get an answer”:
      analyzing users’ interaction with AI-generated personas given unanswerable questions and risk of
      hallucination. In: Proceedings of the 30th International Conference on Intelligent User Interfaces. ACM;
      2025. https://doi.org/10.1145/3708359.3712160.
[10] Zhou K, Hwang JD, Ren X, Sap M. Relying on the unreliable: the impact of language models’ reluctance to
      express uncertainty. In: Proceedings of the 62nd Annual Meeting of the Association for Computational
      Linguistics (Volume 1: Long Papers). Association for Computational Linguistics; 2024, p. 3623-43.
      https://doi.org/10.18653/v1/2024.acl-long.198.
[11]** Kim SSY, Wortman Vaughan J, Liao QV, Lombrozo T, Russakovsky O. Fostering appropriate reliance on
      large language models: the role of explanations, sources, and inconsistencies. In: Proceedings of the 2025
      CHI Conference on Human Factors in Computing Systems. ACM; 2025.
      https://doi.org/10.1145/3706598.3714020.
      Across a think-aloud study and a large preregistered controlled experiment, this paper isolates three features
      of LLM responses and measures their distinct effects on reliance behavior: explanations alone increased
      reliance on both correct and incorrect answers, while source citations and inconsistencies present in
      incorrect explanations were associated with reduced overreliance. The study provides the cleanest evidence
      to date that interface transparency is not a unitary construct, and that cues lowering the cost of verification
      are functionally distinct from cues that raise the apparent authority or completeness of the answer.

[12] Kim SSY, Liao QV, Vorvoreanu M, Ballard S, Wortman Vaughan J. “I’m not sure, but …”: examining the
      impact of large language models’ uncertainty expression on user reliance and trust. In: Proceedings of the
      2024 ACM Conference on Fairness, Accountability, and Transparency. ACM; 2024, p. 822-35.
      https://doi.org/10.1145/3630106.3658941.
[13] Pak R, Rovira E, McLaughlin AC. Polite AI mitigates user susceptibility to AI hallucinations. Ergonomics
      2025;68:1735-45. https://doi.org/10.1080/00140139.2024.2434604.
[14]** Bo JY, Wan S, Anderson A. To rely or not to rely? Evaluating interventions for appropriate reliance on large
      language models. In: Proceedings of the 2025 CHI Conference on Human Factors in Computing Systems.
      ACM; 2025. 10.1145/3706598.3714097.
      This study directly benchmarks three reliance interventions, a persistent reliance disclaimer, token-level
      uncertainty highlighting, and an implicit-answer presentation requiring users to come up with their own
      conclusion, in a randomized online experiment with 400 participants on LSAT logical reasoning and image-
      based numerical estimation. All three interventions reduced overreliance in at least some configurations, but
      generally failed to improve appropriate reliance, and participants in some conditions became more confident
      after making poor reliance decisions. The paper provides the most direct empirical evidence to date that
      warnings change awareness more readily than behavior, and that friction-based interventions can shift
      reliance broadly without improving the discrimination of good from bad advice.

[15] Buçinca Z, Malaya MB, Gajos KZ. To trust or to think: cognitive forcing functions can reduce overreliance on
      AI in AI-assisted decision-making. Proc ACM Hum-Comput Interact 2021;5(CSCW1):Article 188.
      https://doi.org/10.1145/3449287.
[16] Ashktorab Z, Desmond M, Pan Q, Johnson JM, Brachman M, Dugan C, et al. Emerging reliance behaviors in
      human-AI content grounded data generation: the role of cognitive forcing functions and hallucinations. In:
      Proceedings of the 4th Annual Symposium on Human-Computer Interaction for Work. ACM; 2025.
      10.1145/3729176.3729179.
[17]* Liu C, Zhou Q, Shen X, Liu XB, Wu T, Chen XA. Behavioral indicators of overreliance during interaction
      with conversational language models. In: Proceedings of the 2026 CHI Conference on Human Factors in
      Computing Systems. ACM; 2026. 10.1145/3772318.3790332.
      Drawing on interaction logs from 77 participants working with an LLM injected with plausible
      misinformation across three real-world tasks (quiz solving, article summarization, and trip planning), this
      study identifies five behavioral patterns that distinguish low- from high-overreliance users: low-overreliance
      users show careful task comprehension and fine-grained navigation, while high-overreliance users show
      frequent copy-paste of whole paragraphs, skipping initial comprehension, repeated LLM references, coarse
      locating, and accepting misinformation despite hesitation. The methodological contribution is to show that
      overreliance is observable in behavioral traces that post-hoc task outcomes cannot capture, motivating a
      process-level rather than outcome-level approach to studying reliance.

[18] Blanchard SJ, Duani N, Garvey AM, Netzer O, Oh TT. New Tools, New Rules: A Practical Guide to Effective
      and Responsible Generative AI Use for Surveys and Experiments in Research. Journal of Marketing 2025;
      89(6):119-39.
[19] Reber R, Schwarz N. Effects of perceptual fluency on judgments of truth. Consciousness and Cognition
      1999;8:338–42. https://doi.org/10.1006/ccog.1999.0386.
[20] Fazio LK, Brashier NM, Payne BK, Marsh EJ. Knowledge does not protect against illusory truth. Journal of
      Experimental Psychology: General 2015;144:993–1002. https://doi.org/10.1037/xge0000098.
[21] Arora N, Chakraborty I, Nishimura Y. AI–human hybrids for marketing research: Leveraging large language
      models (LLMs) as collaborators. Journal of Marketing 2025; 89(2):43-70.
[22]** Salvi F, Horta Ribeiro M, Gallotti R, West R. On the conversational persuasiveness of GPT-4. Nature
Human Behaviour 2025;9:1645–53. https://doi.org/10.1038/s41562-025-02194-6.

      In a preregistered experiment with 900 participants across 600 debates, GPT-4 with access to personal
      information was more persuasive than human debaters on political topics, demonstrating that LLM
      conversational fluency translates into measurable opinion change and providing direct evidence for the
      persuasive-fluency mechanism that suppresses reactive skepticism.


[23] Kıyak YS, Coşkun Ö, Budakoğlu Iİ. “ChatGPT can make mistakes” warnings fail: a randomized controlled
trial. Medical Education 2026;60:138–42. https://doi.org/10.1111/medu.70056.
[24]* Spearing ER, Gile CI, Fogwill AL, Prike T, Swire-Thompson B, Lewandowsky S, Ecker UKH. Countering
AI-generated misinformation with pre-emptive source discreditation and debunking. Royal Society Open Science
2025;12:242148. https://doi.org/10.1098/rsos.242148.

      This study demonstrates that a source-focused inoculation intervention successfully reduced general trust in
      AI as an information source but failed to reduce the specific influence of AI-generated misinformation on
      reasoning, providing a clear dissociation between awareness of AI limitations and behavioral resistance to
      specific hallucinated content.


[25] Cabrera AA, Perer A, Hong JI. Improving human-AI collaboration with descriptions of AI behavior.
Proceedings of the ACM on Human-Computer Interaction 2023;7(CSCW1):Article 136.
https://doi.org/10.1145/3579612.

[26]** Steyvers M, Tejeda H, Kumar A, et al. What large language models know and what people think they know.
Nature Machine Intelligence 2025;7:221–31. https://doi.org/10.1038/s42256-024-00976-7.

      Across multiple experiments, this work demonstrates a systematic gap between what LLMs actually know (as
      measured by calibrated confidence) and what users believe they know, and shows that aligning expressed
      confidence with actual accuracy improves users' ability to distinguish correct from incorrect outputs.


[27] He G, Kuiper L, Gadiraju U. Knowing about knowing: an illusion of human competence can hinder appropriate
reliance on AI systems. In: Proceedings of the 2023 CHI Conference on Human Factors in Computing Systems.
ACM; 2023. https://doi.org/10.1145/3544548.3581025.

[28] Guo Z, Wu Y, Hartline JD, Hullman J. A decision theoretic framework for measuring AI reliance. In:
Proceedings of the 2024 ACM Conference on Fairness, Accountability, and Transparency. ACM; 2024.
https://doi.org/10.1145/3630106.3658901.

[29] Steyvers M, Kumar A. Three challenges for AI-assisted decision-making. Perspectives on Psychological
Science 2024;19:722–34. https://doi.org/10.1177/17456916231181102.

[30]** Farquhar S, Kossen J, Kuhn L, Gal Y. Detecting hallucinations in large language models using semantic
entropy. Nature 2024;630:625–30. https://doi.org/10.1038/s41586-024-07421-0.

      This paper introduces semantic entropy as a method for detecting hallucinations in LLMs without external
      knowledge bases, demonstrating that hallucinations cluster predictably at model knowledge boundaries
      rather than occurring uniformly, a finding that provides the empirical basis for anticipatory skepticism
      directed at specific content categories.

[31] Dell’Acqua F, McFowland E III, Mollick ER, et al. Navigating the jagged technological frontier: field
experimental evidence of the effects of artificial intelligence on knowledge worker productivity and quality.
Organization Science 2026. (forthcoming) https://doi.org/10.1287/orsc.2025.21838.

[32]* Kim TW, Usman U, Garvey A, Duhachek A. From algorithm aversion to AI dependence: deskilling,
upskilling, and emerging addictions in the GenAI age. Consumer Psychology Review 2026;9:142–64.
https://doi.org/10.1002/arcp.70008.

      Drawing on extant literature, this paper provides a framework theorizing the trajectory from initial algorithm
      aversion through calibrated use to dependence, introducing the concept of cognitive surrender to describe the
      end state in which users delegate metacognitive oversight of offloaded cognitive tasks to the AI system.
[33] Regulation (EU) 2024/1689 of the European Parliament and of the Council of 13 June 2024 laying down
harmonised rules on artificial intelligence (Artificial Intelligence Act). OJ L, 2024/1689.

[34] Mata v Avianca, Inc., No. 1:22-cv-01461 (S.D.N.Y. June 22, 2023) (order imposing sanctions for AI-generated
fabricated citations).

[35] EY analysis of Fortune 100 10-K filings, cited in: How boards can lead in a world remade by AI. Harvard Law
School Forum on Corporate Governance, February 19, 2026. https://corpgov.law.harvard.edu/2026/02/19/how-
boards-can-lead-in-a-world-remade-by-ai/.

[36] McKinsey & Company. What are AI guardrails? November 2024. https://www.mckinsey.com/featured-
insights/mckinsey-explainers/what-are-ai-guardrails.

[37] Zhang v Chen, 2024 BCSC 285 (lawyer ordered to pay costs and audit all files after submitting ChatGPT-
fabricated citations in child custody dispute).

[38] Ko v Li, 2025 ONSC 2766 (Ontario judge ordered counsel to show cause for contempt after AI-generated false
citations identified).

[39]* Couvrette v Wisnovsky, 2025 WL 4109655 (D. Or. Dec. 12, 2025).

[40] Lee, H. P., Sarkar, A., Tankelevitch, L., Drosos, I., Rintel, S., Banks, R., & Wilson, N. The impact of
generative AI on critical thinking: Self-reported reductions in cognitive effort and confidence effects from a survey
of knowledge workers. In Proceedings of the 2025 CHI conference on human factors in computing systems 2025; 1-
22. DOI 10.1145/3706598.3713778.

[41] Charlotin D. AI hallucination cases database. https://www.damiencharlotin.com/hallucinations/ (last updated
May 14, 2026; 1,434 cases catalogued globally).

[42] Federal Trade Commission. FTC announces crackdown on deceptive AI claims and schemes (Operation AI
Comply). September 25, 2024. https://www.ftc.gov/news-events/news/press-releases/2024/09/ftc-announces-
crackdown-deceptive-ai-claims-schemes.

[43] In re DoNotPay, Inc., FTC File No. 2323042 (final order issued Jan. 10, 2025) ($193,000 penalty for marketing
AI chatbot as equivalent to human lawyer without substantiation).

[44] In re Evolv Technologies Holdings, Inc., FTC File No. 2423132 (settlement approved Dec. 2024) (AI security
scanner marketed as weapons detection system failed to detect handguns; company removed negative findings from
commissioned report).
