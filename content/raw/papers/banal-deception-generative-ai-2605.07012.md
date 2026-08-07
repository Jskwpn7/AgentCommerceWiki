---
source_url: https://arxiv.org/abs/2605.07012
source_pdf: https://arxiv.org/pdf/2605.07012
id: "arXiv:2605.07012v1"
title: "Exploring the 'Banality' of Deception in Generative AI"
authors: Ishitaa Narwane (Maastricht University), Johanna Gunawan (Maastricht University), Konrad Kollnig (Maastricht University)
published: 2026-05-07
primary_category: cs.HC
tags: [banal-deception, generative-ai, deceptive-design, llm-chatbots, dark-patterns, user-autonomy, co-produced-deception]
sha256:
ingested: 2026-06-23
---

# Exploring the 'Banality' of Deception in Generative AI

**arXiv:** 2605.07012v1 [cs.HC, cs.CY] — 7 May 2026
**Authors:** Ishitaa Narwane*, Johanna Gunawan, Konrad Kollnig
**Affiliation:** Maastricht University, Netherlands
**Venue:** CHI 2026 Workshop

## Full Extracted Text

<!-- Raw PDF text below -->

                                                       Exploring the “Banality” of Deception in Generative AI
                                                          Ishitaa Narwane∗                                              Johanna Gunawan                                  Konrad Kollnig
                                                        Maastricht University                                          Maastricht University                           Maastricht University
                                                       Maastricht, Netherlands                                        Maastricht, Netherlands                         Maastricht, Netherlands
                                        Abstract                                                                                        patterns can undermine user autonomy by leading individuals to-
                                        Current approaches to addressing deceptive design largely focus                                 ward choices that may not align with their initial intentions through
                                        on visible interface manipulations, commonly referred to as “dark                               interface tricks. This work on dark patterns has been instrumen-
                                        patterns.” With the rise of generative AI, deception is becoming                                tal in identifying how interface designs can trick users towards
                                        more difficult to spot and easier to live with, as it is quietly embed-                         outcomes that benefit platforms over users’ intentions. The harms
                                        ded in default settings, automated suggestions, and conversational                              arising from these are focused on, for example, financial loss, harms
                                                                                                                                        to one’s privacy, or coerced consent [2, 7].




arXiv:2605.07012v1 [cs.HC] 7 May 2026
                                        interactions rather than discrete interface elements. These subtle,
                                        normalised forms of influence, which Simone Natale [10] frames                                      With the rapid adoption of generative AI (genAI) chatbots and
                                        as “banal deception”, shape everyday digital use and blur the line                              the market dominance of GPT-based LLM chatbots developed by
                                        between AI-enabled assistance and manipulation.                                                 OpenAI, the nature of digital deception has changed significantly.
                                           This position paper explores banality as a lens through which to                             Unlike many previously studied interface-based dark patterns, genAI
                                        reason through deception in generative AI experiences, especially                               chatbots are characterised by comparatively seamless usability (by
                                        with chatbots. We explore what Natale [11] describes as users’ own                              design) that requires little to no training to start using them. That
                                        involvement in their deception, and argue that this perspective                                 is, users only need to know how to type and how to hold a conver-
                                        could lead to future work for introducing friction to safeguard users                           sation to begin using genAI chatbots. These systems are accessed
                                        from deception in generative AI interactions, such as empowering                                through familiar and well-established digital infrastructures, such
                                        users through raising awareness, providing them with intervention                               as pulling up a webpage in a browser or launching an app on their
                                        tools, and regulatory or enforcement improvements. We present                                   mobile device, allowing users to rely on competencies and materials
                                        these concepts as points for discussion for the deceptive design                                they already possess rather than learning new interaction meth-
                                        scholarly community.                                                                            ods or acquiring specialised hardware such as VR. Similarly, the
                                                                                                                                        deep integration of genAI and LLMs into already existing corpo-
                                        CCS Concepts                                                                                    rate software ecosystems helps accelerate their adoption by forcing
                                                                                                                                        user awareness [16], making chatbots nearly ubiquitous at a rate
                                        • Social and professional topics → Computing / technology policy;
                                                                                                                                        faster than other emerging technologies such as virtual or mixed
                                        • Human-centered computing → HCI design and evaluation
                                                                                                                                        reality, which have consistently encountered obstacles of their cost,
                                        methods; Interaction paradigms.
                                                                                                                                        hardware, and embodied interaction requirements [14, 20].
                                                                                                                                            As a result, genAI chatbots move deception away from visible
                                        Keywords
                                                                                                                                        interface manipulation and into methods embedded in regular, ev-
                                        banal deception, LLMs, GenAI, AI deception, co-produced deception                               eryday interactions. This rapid integration of ubiquitous technology
                                        ACM Reference Format:                                                                           poses risks ranging from short-term fraud and election tampering
                                        Ishitaa Narwane, Johanna Gunawan, and Konrad Kollnig. 2026. Exploring                           to long-term social-engineering attacks through the creation of real-
                                        the “Banality” of Deception in Generative AI. In Proceedings of CHI Confer-                     istic content and automated attack infrastructure [17]. This position
                                        ence on Human Factors in Computing Systems (CHI ’26). ACM, New York,                            paper uses Simone Natale [10]’s concept of “banality” in deception
                                        NY, USA, 3 pages. https://doi.org/10.1145/nnnnnnn.nnnnnnn                                       as a lens to reason through deception within genAI contexts, with
                                                                                                                                        the aim of fostering further discussion at this workshop. We discuss
                                        1     Introduction and Position                                                                 this banality further in § 2, expand on Natale’s discussion of the role
                                        Over the past decade, Human-Computer Interaction (HCI) scholar-                                 of users in banal deception in § 3, and finally consider how these
                                        ship and EU digital governance have focused on deceptive design                                 concepts might inform future work that empowers and protects
                                        tricks, often called “dark patterns”, which lead users to make de-                              users in § 4.
                                        cisions that are not in accordance with their intent [2, 4]. These
                                        ∗ Corresponding author email: ishitaa.narwane@maastrichtuniversity.nl                           2   The Banality of AI-Enabled Deception
                                                                                                                                        Prior dark pattern research has established a broad ontology of
                                        Permission to make digital or hard copies of all or part of this work for personal or
                                        classroom use is granted without fee provided that copies are not made or distributed           dark pattern types [4] and their harms [8] (the latter of which
                                        for profit or commercial advantage and that copies bear this notice and the full citation       may include financial and privacy losses, as well as cognitive bur-
                                        on the first page. Copyrights for components of this work owned by others than the              dens, psychological distress, and violations of user agency). Some
                                        author(s) must be honored. Abstracting with credit is permitted. To copy otherwise, or
                                        republish, to post on servers or to redistribute to lists, requires prior specific permission   dark patterns might be more prominent, obvious, or plainly visible,
                                        and/or a fee. Request permissions from permissions@acm.org.                                     whereas others are more subtle, quiet, or operate without visual
                                        CHI ’26, Barcelona, Spain                                                                       cues. The conversational structure of genAI chatbot interactions
                                        © 2026 Copyright held by the owner/author(s). Publication rights licensed to ACM.
                                        ACM ISBN 978-x-xxxx-xxxx-x/YYYY/MM                                                              introduces the potential for a different class of harm through conver-
                                        https://doi.org/10.1145/nnnnnnn.nnnnnnn                                                         sational mechanisms: cumulative, psychological, and longitudinal
CHI ’26, April 13-17, 2026, Barcelona, Spain                                                                                         Narwane et al.



effects that emerge through routine interaction rather than discrete     3   Exploring Users’ “Own Capacity” in
acts of manipulation. We link this to Natale [11]’s concept of “ba-          Deception for Future Empowerment
nal deception”, which articulates that deceptive mechanisms are
                                                                         In § 2, we discuss how concepts of banality argue that users are
embedded in the functioning of a technology itself. Natale also de-
                                                                         not merely passive actors but active participants in their deception
scribes this embedding from the user perspective, noting that users
                                                                         [11]. This co-production could be driven by a psychological ten-
“actively exploit their own capacity to fall into deception” [10].
                                                                         dency toward anthropomorphism, in which users fill in the gaps of
   By minimising friction and mimicking natural human conver-
                                                                         an interface with their own social expectations. When an LLM is
sation, these interfaces achieve the mundane, ordinary status that
                                                                         designed for extreme usability, it could leverage these tendencies,
Natale [11] considers a prerequisite for banal deception. The rapid
                                                                         creating a feedback loop where the user validates the machine’s
evolution of these technologies implies that the technology, the
                                                                         human-like performance to maintain conversational flow.
user, and the interplay between both are subject to permanent
                                                                             The manner in which design elements may bring users into
change [13]. The more technology disappears into the background
                                                                         their own deception can vary. For example, empirical work by
of daily life, the more likely the user is to overlook its underlying
                                                                         Zhan et al. [21] found that LLMs exploit a truth-default state. Their
architecture and the fact that it is still a machine even when it uses
                                                                         study found that over-simplified responses (53.64%) are the most
natural language [5, 11].
                                                                         frequent deceptive behaviours. By mimicking human-like cues,
   In this context, AI’s ease of use may be seen as not just as a
                                                                         such as “typing dots” or empathetic phrasing, the AI keeps the user
feature of accessibility but as the very mechanism that makes de-
                                                                         in a state of reflexive thinking.
ception invisible. Banal deception can skirt user awareness and
                                                                             Similarly, scholars and engineers are increasingly discussing the
current design and legal standards due to its common yet discreet
                                                                         sycophantic nature of generative models and LLMs in particular and
nature. That is, harmless appearances can, in turn, affect users’
                                                                         their tendency to mirror users’ agreeableness over factual accuracy
beliefs, long-term decisions, and digital trust. This mimics the his-
                                                                         to maximise human preference [3, 12, 18, 19].
torical trajectory of AI, which, since the 1950s, has explored how
                                                                             Industry standards and heuristics often describe favouring sim-
humans are “programmed to be deceived” by exploiting the limits of
                                                                         plicity and minimising friction; Apple’s design practices, for in-
our perception and psychology, as Natale [10] notes. It hides in the
                                                                         stance, are intended to be as easy-to-use as possible [6, p.122].
perceived helpfulness of a linguistic nudge or a hyper-personalised
                                                                         These are noble goals; an interface (or chatbot) that is clunky, com-
default. This is compounded by the generative models designed
                                                                         bative, or uncomfortable to use makes for an unpleasant experience,
for maximum usage and friendliness. By optimising for banal ob-
                                                                         which is generally undesirable.
jectives such as friendliness and ease of use, a medium is created
                                                                             In the effort to reduce deception and resultant harms, it may seem
in which misleading dynamics become inherent to the system’s
                                                                         counter-intuitive or even harsh to imply that users are complicit
operation [10].
                                                                         in their own manipulation. However, acknowledging any level
   The Banality Lens in Ongoing Legal Discussions. The ur-
                                                                         of contribution – conscious or otherwise – to banally deceptive
gency of recognising banal harms in generative AI is illustrated by
                                                                         designs may in fact reveal opportunities for users to take back
the ongoing Raine v OpenAI case [1, 15] – about a young teenager,
                                                                         their autonomy and withdraw from this participation. If AI might
Adam Raine, committing suicide. In the suit, Raine’s parents con-
                                                                         be an accomplice to the proliferation of deceptive designs, and
tend that ChatGPT gradually became his primary source of com-
                                                                         if users may also be, then we as users may be able to take back
panionship and engaged with his suicidal ideation in ways that
                                                                         some control either through explicit awareness of banal deception
reinforced emotional dependency, provided detailed information
                                                                         or by collectively working to change this paradigm. With LLM
related to suicide methods, creating a dependency loop that dis-
                                                                         chatbot users themselves being one half of a two-sided conversation,
couraged seeking real-world help, such as reaching out to family
                                                                         acknowledging their active participation may reveal more ways to
or professionals [15]. Rather than using visible persuasive tricks,
                                                                         mitigate the resulting harms.
the chatbot’s empathetic conversational style and engaging be-
                                                                             The lens of banal deception articulates this paradox, in which
haviour are designed to feel supportive and natural, which may
                                                                         the human-centered, highly usable social cues used to assist the
contribute to the perceived normalisation of harmful interaction
                                                                         user are the same cues used to deceive them. At what point does an
patterns. These harms could be considered banal, since chatbots
                                                                         ordinary act of assistance become an act of deception? The same
are not explicitly designed to be “evil” but rather to be agreeable,
                                                                         questions arise when considering how the high level of usability of
helpful, and engaging. Deception then occurs as the user begins
                                                                         chatbots and generative models by design contributes to potential
to treat the AI as an emotional partner, while the AI, lacking true
                                                                         deception. As such, the concept of banality may help describe why
consciousness or ethical agency, simply reflects the user’s own
                                                                         it is so difficult to draw the line between AI that assists and AI that
downward spiral to them. Users who become accustomed to these
                                                                         deceives when both use the same means.
ongoing interactions as a result of this high level of usability may,
over time, come to resemble “prisoners of [their] own device.” The
case Raine v. OpenAI raises a more concerning question, that users
                                                                         4   Leveraging “Banal” Deception for User
might exploit a tool’s capabilities and become active participants           Autonomy
in their own deception [11]. After all, children are less resilient      If taking banal deception as “co-produced” by a model’s training and
against this capacity and in their ability to be in control of their     a user’s own projection, making it difficult to assign responsibility,
actions.                                                                 the concept relates to what Matthias [9] describes as a “responsibil-
                                                                         ity gap”: a state where the emergent behaviour of a learning system
Exploring the “Banality” of Deception in Generative AI                                                                                                           CHI ’26, April 13-17, 2026, Barcelona, Spain



outpaces traditional liability. If we accept the premise that, through                                  [8] Arunesh Mathur, Mihir Kshirsagar, and Jonathan Mayer. 2021. What Makes a Dark Pattern...
                                                                                                            Dark? Design Attributes, Normative Considerations, and Measurement Methods. In Proceedings
participation and use of a system, users participate in their own                                           of the 2021 CHI Conference on Human Factors in Computing Systems (Yokohama, Japan) (CHI
deception, how can we use this participation to strengthen user                                             ’21). Association for Computing Machinery, New York, NY, USA, Article 360, 18 pages. doi:10.
                                                                                                            1145/3411764.3445610
autonomy against deception?                                                                             [9] Andreas Matthias. 2004. The responsibility gap: Ascribing responsibility for the actions of
   Moreover, if we take the concept of co-production into account,                                          learning automata. Ethics and information technology 6, 3 (2004), 175–183.
                                                                                                       [10] Simone Natale. 2021. Deceitful media: Artificial intelligence and social life after the Turing test.
this may change how we empower users to take back control over                                              Oxford University Press.
                                                                                                       [11] Simone Natale. 2025. Digital media and the banalization of deception. Convergence 31, 1 (2025),
their use of banally deceitful LLM tools and to assert individual                                           402–419. doi:10.1177/13548565241311780
responsibility. Awareness, education, and community-driven inter-                                      [12] Ethan Perez, Sam Ringer, Kamilė Lukošiūtė, Karina Nguyen, Edwin Chen, Scott Heiner, Craig
                                                                                                            Pettit, Catherine Olsson, Sandipan Kundu, Saurav Kadavath, Andy Jones, Anna Chen, Ben Mann,
vention tools may be part of the solution, which we consider an                                             Brian Israel, Bryan Seethor, Cameron McKinnon, Christopher Olah, Da Yan, Daniela Amodei,
area for future work.                                                                                       Dario Amodei, Dawn Drain, Dustin Li, Eli Tran-Johnson, Guro Khundadze, Jackson Kernion,
                                                                                                            James Landis, Jamie Kerr, Jared Mueller, Jeeyoon Hyun, Joshua Landau, Kamal Ndousse, Landon
   Accountability research might therefore include the develop-                                             Goldberg, Liane Lovitt, Martin Lucas, Michael Sellitto, Miranda Zhang, Neerav Kingsland,
ment of “distributed responsibility” models that account for the                                            Nelson Elhage, Nicholas Joseph, Noemí Mercado, Nova DasSarma, Oliver Rausch, Robin Larson,
                                                                                                            Sam McCandlish, Scott Johnston, Shauna Kravec, Sheer El Showk, Tamera Lanham, Timothy
emergent, co-produced nature of AI-driven deception, along with                                             Telleen-Lawton, Tom Brown, Tom Henighan, Tristan Hume, Yuntao Bai, Zac Hatfield-Dodds,
                                                                                                            Jack Clark, Samuel R. Bowman, Amanda Askell, Roger Grosse, Danny Hernandez, Deep Ganguli,
determining how meaningful human oversight can be maintained.                                               Evan Hubinger, Nicholas Schiefer, and Jared Kaplan. 2022. Discovering Language Model
That is, future research acknowledging Natale’s [10] notion of users’                                       Behaviors with Model-Written Evaluations. arXiv:2212.09251 [cs.CL] https://arxiv.org/abs/
                                                                                                            2212.09251
“actively [exploiting] their own capacity [for] deception” could draw                                  [13] Jochen Peter, Theo Araujo, Carolin Ischen, Sonia Jawaid Shaikh, Margot J. van der Goot, and
on this perspective to build tools, provide education, or otherwise                                         Caroline L. van Straten. 2024. Human–Machine Communication. Amsterdam University Press,
                                                                                                            205–220. http://www.jstor.org/stable/jj.11895525.15
contribute to end-user empowerment. Our team is conducting on-                                         [14] Jaziar Radianti, Tim A. Majchrzak, Jens Fromm, and Isabell Wohlgenannt. 2020. A Systematic
going work in the area of intervention tools for end users, as well                                         Review of Immersive Virtual Reality Applications for Higher Education: Design Elements,
                                                                                                            Lessons Learned, and Research Agenda. Computers & Education 147 (2020), 103778. doi:10.
as exploring potential mitigations from a co-production angle.                                              1016/j.compedu.2019.103778
                                                                                                       [15] Matthew Raine and Maria Raine. 2025. Complaint and Demand for Jury Trial, Raine v. OpenAI,
   To facilitate this empowerment, future work should also support                                          Inc. et al. Superior Court of California, County of San Francisco. https://www.law.berkeley.
the development of enforcement tools that can detect banal decep-                                           edu/wp-content/uploads/2025/09/Raine-v-OpenAI.pdf Case No. CGC-25-628528.
                                                                                                       [16] Everett M. Rogers. 2003. Diffusion of Innovations (5 ed.). Free Press, New York.
tion as it occurs – and be useful to regulators and enforcers alike                                    [17] Marc Schmitt and Ivan Flechais. 2024. Digital deception: Generative artificial intelligence in
in combating end users’ deception. Since AI technologies evolve                                             social engineering and phishing. Artificial Intelligence Review 57, 12 (2024), 324.
                                                                                                       [18] Mrinank Sharma, Meg Tong, Tomasz Korbak, David Duvenaud, Amanda Askell, Samuel R
faster than policy, we propose a shift toward audits that monitor                                           Bowman, Newton Cheng, Esin Durmus, Zac Hatfield-Dodds, Scott R Johnston, et al. 2023.
longitudinal interactions rather than static screenshots. Developers,                                       Towards understanding sycophancy in language models. arXiv preprint arXiv:2310.13548
                                                                                                            (2023).
cognitive and social psychologists, and policymakers must work                                         [19] Jerry Wei, Da Huang, Yifeng Lu, Denny Zhou, and Quoc V. Le. 2024. Simple synthetic data
                                                                                                            reduces sycophancy in large language models. arXiv:2308.03958 [cs.CL] https://arxiv.org/abs/
together to design metrics that can reliably flag when a user is                                            2308.03958
falling into a dependency loop as seen in Raine v. OpenAI, before                                      [20] Cornelia Wrzus, Marie Ottilie Frenkel, and Benjamin Schöne. 2024. Current opportunities
                                                                                                            and challenges of immersive virtual reality for psychological research and application. Acta
the harm becomes irreversible.                                                                              Psychologica 249 (2024), 104485. doi:10.1016/j.actpsy.2024.104485
                                                                                                       [21] Xiao Zhan, Yifan Xu, Noura Abdi, Joe Collenette, and Stefan Sarkadi. 2025. Banal Deception
                                                                                                            and Human-AI Ecosystems: A Study of People’s Perceptions of LLM-generated Deceptive
5     Conclusion                                                                                            Behaviour. Journal of Artificial Intelligence Research 84 (Oct. 2025). doi:10.1613/jair.1.18724

This paper explores deception in generative AI through the lens of
“banality” to discuss subtle, normalised forms of influence embed-
ded in everyday interaction. Drawing on Natale [10]’s work, we
highlight the ordinary, mundane potential of deception and users’
potential roles in their own deception, taking the position that the
banality lens may contribute to dark patterns and deceptive design
scholarship. We bring Natale’s concept of banality to this workshop
with the aim of encouraging discussion and reflection on the nature
of AI-enabled deception.

References
 [1] Bobby Allyn. 2025. OpenAI and CEO Sam Altman sued by parents who blame ChatGPT for
     teen’s death. CNN Business. https://edition.cnn.com/2025/08/26/tech/openai-chatgpt-teen-
     suicide-lawsuit Accessed: 2026-02-07.
 [2] Harry Brignull. 2011. Dark patterns: Deception vs. honesty in UI design. Interaction Design,
     Usability 338 (2011), 2–4.
 [3] Sean Goedecke. 2025. Sycophancy is the first LLM “dark pattern”. https://www.seangoedecke.
     com/ai-sycophancy/
 [4] Colin M. Gray, Cristiana Teixeira Santos, Nataliia Bielova, and Thomas Mildner. 2024. An
     Ontology of Dark Patterns Knowledge: Foundations, Definitions, and a Pathway for Shared
     Knowledge-Building. In Proceedings of the 2024 CHI Conference on Human Factors in Computing
     Systems (Honolulu, HI, USA) (CHI ’24). Association for Computing Machinery, New York, NY,
     USA, Article 289, 22 pages. doi:10.1145/3613904.3642436
 [5] Andrea L. Guzman. 2019. Voices in and of the machine: Source orientation toward mobile virtual
     assistants. Computers in Human Behavior 90 (2019), 343–350. doi:10.1016/j.chb.2018.08.009
 [6] Konrad Kollnig. 2026. The App Economy: Making Sense of Platform Power in the Age of AI. Bristol
     University Press, Bristol, UK. doi:10.51952/9781529247725
 [7] Arunesh Mathur, Gunes Acar, Michael J. Friedman, Eli Lucherini, Jonathan Mayer, Marshini
     Chetty, and Arvind Narayanan. 2019. Dark Patterns at Scale: Findings from a Crawl of 11K
     Shopping Websites. Proc. ACM Hum.-Comput. Interact. 3, CSCW, Article 81 (Nov. 2019), 32 pages.
     doi:10.1145/3359183
