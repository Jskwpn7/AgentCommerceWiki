---
source_url: https://arxiv.org/abs/2606.19116
source_pdf: https://arxiv.org/pdf/2606.19116
id: "arXiv:2606.19116v1"
title: "Towards an Agent-First Web: Redesigning the Web for AI Agents"
authors: "Eranga Bandara, Ross Gore, Ravi Mukkamala, Asanga Gunaratna, Safdar H. Bouk, Xueping Liang, Peter Foytik, Abdul Rahman, Sachini Rajapakse, Isurunima Kularathna, Pramoda Karunarathna, Chalani Rajapakse, Ng Wee Keong, Kasun De Zoysa, Tharaka Hewa, Amin Hass, Wathsala Herath, Aruna Withanage, Nilaan Loganathan, Atmaram Yarlagadda, Sachin Shetty"
published: 2026-06-17
primary_category: cs.AI
tags: [agent-first-web, web-architecture, ai-agents, web-protocols, machine-readable-content, web-modernization]
sha256:
ingested: 2026-06-23
---

# Towards an Agent-First Web: Redesigning the Web for AI Agents

**arXiv:** 2606.19116v1 [cs.AI, cs.CY] — 17 June 2026
**Authors:** Eranga Bandara, Ross Gore, Ravi Mukkamala, Asanga Gunaratna, Safdar H. Bouk, Xueping Liang, Peter Foytik, Abdul Rahman, Sachini Rajapakse, Isurunima Kularathna, Pramoda Karunarathna, Chalani Rajapakse, Ng Wee Keong, Kasun De Zoysa, Tharaka Hewa, Amin Hass, Wathsala Herath, Aruna Withanage, Nilaan Loganathan, Atmaram Yarlagadda, Sachin Shetty

## Full Extracted Text

<!-- Raw PDF text below -->

                                         Towards an Agent-First Web: Redesigning the Web for
                                                              AI Agents
                                          Eranga Bandaraa , Ross Gorea , Ravi Mukkamalaa , Asanga Gunaratnab ,
                                         Safdar H. Bouka , Xueping Liangd , Peter Foytika , Abdul Rahmanc , Sachini
                                          Rajapaksee , Isurunima Kularathnaf , Pramoda Karunarathnae , Chalani
                                           Rajapaksee , Ng Wee Keongh , Kasun De Zoysai , Tharaka Hewal , Amin




arXiv:2606.19116v1 [cs.AI] 17 Jun 2026
                                             Hassg , Wathsala Herathj , Aruna Withanagek , Nilaan Loganathank ,
                                                           Atmaram Yarlagaddam , Sachin Shettya
                                                             a
                                                                 Old Dominion University, Norfolk, VA, USA
                                                                   b
                                                                     AI Motion Labs, Melbourne, Australia
                                                                         c
                                                                           Deloitte & Touche LLP, USA
                                                                   d
                                                                     Florida International University, USA
                                                                                   e
                                                                                     IcicleLabs.AI
                                                                                f
                                                                                  Linesandloops.art
                                                             g
                                                               Accenture Technology Labs, Arlington, VA, USA
                                                               h
                                                                 Nanyang Technological University, Singapore
                                                                      i
                                                                        University of Colombo, Sri Lanka
                                                                                   j
                                                                                     Agentsway.AI
                                                                                      k
                                                                                        Effectz.AI
                                                   l
                                                     Center for Wireless Communications, University of Oulu, Finland
                                                       m
                                                         McDonald Army Health Center, Newport News, VA, USA




                                             Email addresses: cmedawer@odu.edu (Eranga Bandara), rgore@odu.edu (Ross
                                         Gore), rmukkama@odu.edu (Ravi Mukkamala),
                                         asanga.gunaratna@complianceoslab.app (Asanga Gunaratna), sbouk@odu.edu
                                         (Safdar H. Bouk), xuliang@fiu.edu (Xueping Liang), pfoytik@odu.edu (Peter Foytik),
                                         abdulrahman@deloitte.com (Abdul Rahman), sachini.rajapakse@iciclelabs.ai
                                         (Sachini Rajapakse), nima@linesandloops.art (Isurunima Kularathna),
                                         pramoda.karunarathna@iciclelabs.ai (Pramoda Karunarathna),
                                         chalani.rajapakse@iciclelabs.ai (Chalani Rajapakse), awkng@ntu.edu.sg (Ng Wee
                                         Keong), kasun@ucsc.cmb.ac.lk (Kasun De Zoysa), tharaka.hewa@oulu.fi (Tharaka
                                         Hewa), amin.hassanzadeh@accenture.com (Amin Hass),
                                         wathsala.herath@agentsway.ai (Wathsala Herath), aruna@effectz.ai (Aruna
                                         Withanage), nilaan@effectz.ai (Nilaan Loganathan),
                                         atmaram.yarlagadda.civ@health.mil (Atmaram Yarlagadda), sshetty@odu.edu
                                         (Sachin Shetty)



                                         Preprint submitted to Journal Name                                      June 18, 2026
Abstract
The World Wide Web was architected on a foundational assumption that
has held for three decades: that the primary consumer of web content is a
human being. This assumption permeates every layer of the web — its access
model presumes human visitors, its economic foundations rest on human
attention, and its content architecture targets human perception. The rapid
emergence of AI agents as primary intermediaries between humans and web
content fundamentally invalidates this assumption. Today, AI agents browse,
synthesize, and act on web content on behalf of humans at scale — yet
the web actively resists them through blanket blocking, CAPTCHA-based
exclusion, and economic models that treat agent access as extraction rather
than legitimate interaction.
    This paper proposes a principled redesign of the web across three in-
terdependent layers. At the access layer, we argue that agents acting on
behalf of humans should inherit equivalent access rights to those humans
— governed not by blanket blocking but by rate limiting and standardized
agent identification metadata carried in HTTP requests, analogous to how
browsers currently identify themselves to servers. We propose a dual-layer
web architecture in which human-readable content and agent-optimized con-
tent coexist during a transition period, with a phased migration path to-
ward an agent-first publishing standard. At the economic layer, we reject
universal pay-per-query models in favor of an intent-based tier framework
grounded in the principle that an agent’s economic obligation mirrors that
of the human it represents — the agent-as-human-proxy principle. We pro-
pose a token-based subscription model in which content access is metered
in tokens rather than pageviews, alongside a commissioned content economy
in which human intentionality anchors AI-generated content production and
breaks the self-reinforcing generative loop. At the content layer, we identify
a structural threat we term epistemic recursion — the self-referential loop
in which AI-generated content is consumed by AI agents to produce further
content, progressively detaching web knowledge from human ground truth.
To counter this, we propose the Agent Text Markup Language (ATML) — a
semantic content format optimized for agent consumption — alongside a four-
level human supervision tier model and a cryptographic provenance chain ar-
chitecture that makes the degree of human oversight machine-readable and
verifiable.
    Together, these three layers constitute a framework of ten design princi-


                                      2
ples for an agent-first internet — one in which agents are not threats to be
blocked but first-class citizens whose integration requires renegotiating the
web’s foundational social contract across access, economics, and content.
Keywords: Agentic AI, Agentic Web, LLM, AI Agents, Web Architecture


1. Introduction
    The World Wide Web, since its inception by Berners-Lee in 1989, was de-
signed with a singular assumption: that the primary consumer of web content
is a human being [18]. This assumption permeates every layer of the web’s
architecture. Hypertext Markup Language (HTML) renders content visu-
ally for human perception [47]. Search engines optimize content discovery
around human attention and intent [20]. Economic models monetize human
engagement through advertising impressions and clicks [29]. Security mech-
anisms such as CAPTCHAs are explicitly designed to distinguish humans
from automated agents [1]. For three decades, this human-centric architec-
ture served the web well — enabling an unprecedented global information
ecosystem that transformed commerce, communication, and knowledge.
    This foundational assumption is now breaking down. The rapid advance-
ment of large language models (LLMs) [6, 13] and autonomous AI agents has
introduced a fundamentally new class of web participant [12, 8] — one that
browses, synthesizes, and acts on web content not for itself, but as a proxy for
a human user [54]. Unlike traditional web crawlers, which indexed content
to route human traffic back to publishers, modern AI agents complete tasks
end-to-end — booking flights, answering research questions, drafting docu-
ments — without the human ever visiting the underlying web resource [57].
The web’s human-centric architecture was not designed for this interaction
model, and the friction is now measurable and severe.
    Empirically, this tension manifests across all three layers of the web. At
the access layer, infrastructure providers have begun blocking AI agents by
default. Cloudflare, which routes over 16% of global internet traffic, moved in
July 2025 to block AI crawlers unless explicitly permitted, introducing a pay-
per-crawl model that treats agent access as a commercial transaction rather
than a default right [21]. The crawl-to-referral ratio of AI agents reveals the
economic asymmetry driving this response: by mid-2025, Anthropic’s crawler
exhibited a ratio of 73,000 crawled pages for every single human referral
generated — fundamentally breaking the value exchange that historically

                                       3
justified open crawler access [22]. At the economic layer, zero-click searches
now account for approximately 60% of all Google queries, rising to 93% in AI-
native search modes [50], with click-through rates at position one falling from
27% to 11% [52]. Publishers report organic traffic declines of 70–80%, with
some characterizing the shift as an extinction-level event for web-dependent
media [52]. At the content layer, a deeper structural problem emerges: as AI
agents increasingly consume AI-generated content to produce further content,
the web risks entering a self-referential generative loop that progressively
erodes its epistemic foundations [51] — a phenomenon we term epistemic
recursion.
    The web’s response to these pressures has been reactive and fragmented.
Infrastructure providers block agents by default [21]. Protocol working
groups propose interoperability standards in isolation [5, 33, 44]. Economic
responses treat agent access as a billing problem rather than a design problem
[21, 2]. Content provenance efforts address detection of AI-generated content
without addressing the architectural conditions that produce epistemic recur-
sion [25, 39]. Critically, no existing work addresses all three layers together,
nor frames the challenge as what we argue it fundamentally is: a failure of
the web’s foundational social contract that requires principled redesign, not
reactive patches [16, 10].
    This paper makes the following argument: the web requires simultaneous
redesign across three interdependent layers — access, economics, and content
— grounded in a single philosophical anchor: that AI agents acting on be-
half of humans are first-class web citizens, entitled to the same presumption
of access as the humans they represent, subject to equivalent obligations,
and deserving of an architectural environment designed for their interaction
model rather than one that merely tolerates them.
    Concretely, we propose three mechanism clusters. At the access layer, we
propose agent identification metadata — standardized HTTP request head-
ers that allow agents to declare their identity, the human they represent,
and their intent, analogous to the User-Agent and Accept headers browsers
currently use [31] — alongside agents.txt, a machine-readable access policy
standard that replaces the inadequate robots.txt honor system with grad-
uated, intent-aware access declarations. Together these enable servers to ap-
ply rate limiting rather than blanket blocking, and to serve agent-optimized
content via a dual-layer web architecture that supports gradual migration
rather than disruptive replacement. At the economic layer, we propose a
token-based subscription model in which content access is metered in tokens

                                       4
rather than pageviews — directly compatible with existing AI API pricing
infrastructure — alongside a commissioned content economy in which human
intentionality anchors AI content production, and a free tier governed by rate
limits mirroring the open source / proprietary software distinction [48]. At
the content layer, we propose the Agent Text Markup Language (ATML) —
a semantic content format optimized for agent consumption — alongside a
four-level human supervision tier model and a cryptographic provenance chain
architecture that make the degree of human oversight machine-readable and
verifiable, breaking the epistemic recursion loop at its structural root.
    We make the following specific contributions:

   • We diagnose the web’s human-centric design assumptions across three
     layers and demonstrate empirically that each is incompatible with
     agent-first interaction at scale (Section 3).
   • We propose agent identification metadata and agents.txt as lightweight,
     backward-compatible mechanisms for agent identification, intent dec-
     laration, and access policy over existing HTTP infrastructure, enabling
     rate limiting over blocking and dual-layer content serving (Section 4).
   • We introduce an intent-based economic tier model grounded in the
     agent-as-human-proxy principle, with a token-based subscription mech-
     anism and commissioned content economy directly compatible with ex-
     isting AI API infrastructure (Section 5).
   • We introduce the concept of epistemic recursion — the self-referential
     loop in which AI-generated content is consumed by AI agents to pro-
     duce further content, progressively detaching web knowledge from hu-
     man ground truth — and propose ATML, human supervision tiers,
     and a cryptographic provenance chain as architectural responses (Sec-
     tion 6).
   • We synthesize these contributions into a unified framework of ten de-
     sign principles for an agent-first internet, positioning the challenge as
     a sociotechnical problem requiring renegotiation of the web’s founda-
     tional social contract (Section 7).

    The remainder of this paper is structured as follows. Section 2 reviews
related work across agent protocols, web economics, and content architec-
ture. Section 3 diagnoses the three-layer failure of the human-centric web.

                                      5
Section 4 presents the access layer redesign. Section 5 presents the economic
layer redesign. Section 6 presents the content layer redesign including ATML,
supervision tiers, and epistemic recursion prevention. Section 7 synthesizes
the unified framework and ten principles. Section 8 discusses open challenges.
Section 9 concludes.

2. Related Work
    Research relevant to redesigning the web for AI agents spans four broad
areas: (1) AI agent architectures and web interaction, (2) agent commu-
nication protocols and infrastructure, (3) web economics and the attention
economy, and (4) content provenance and epistemic integrity. While each
area has produced significant contributions, no existing work addresses all
three layers — access, economics, and content — simultaneously, nor frames
the challenge as a renegotiation of the web’s foundational social contract.
Table 1 summarizes how representative works relate to the key dimensions
of our framework.

2.1. AI Agent Architectures and Web Interaction
    Early work on web-based AI agents focused on task completion in con-
strained environments. Yao et al. [57] introduced WebShop, demonstrat-
ing that language model agents could navigate product search and purchase
flows, establishing a benchmark for grounded web interaction. Zhou et al. [59]
extended this with WebArena, a realistic multi-domain environment covering
e-commerce, content management, and developer tools, revealing the signif-
icant gap between agent capability and real-world web complexity. Deng
et al. [26] introduced Mind2Web, the first dataset for generalist web agents
capable of following natural language instructions across diverse websites,
highlighting the challenge of generalizing across the heterogeneous structure
of the human-designed web.
    More recent work has examined agentic behavior at scale. Wang et al. [54]
surveyed LLM-based autonomous agents across planning, memory, and tool
use dimensions, noting that web interaction represents one of the most com-
plex and underspecified deployment environments. Durante et al. [27] exam-
ined multi-agent systems operating in open-ended environments, identifying
trust, coordination, and resource access as primary bottlenecks. Critically,
none of these works examine the web architecture itself as a site of inter-
vention — they treat the existing web as a fixed environment and attempt

                                      6
to improve agent capability within it. Our work takes the complementary
position: that the web architecture must change to accommodate agents, not
only that agents must improve to navigate the existing web.

2.2. Agent Communication Protocols and Infrastructure
    A parallel research and engineering effort has focused on protocol-level
infrastructure for agent interaction. Anthropic [5] introduced the Model Con-
text Protocol (MCP), an open standard enabling AI agents to connect to ex-
ternal tools and data sources through a unified interface, addressing the frag-
mentation of agent-to-tool communication. Google’s Agent-to-Agent (A2A)
protocol [33] extended this to agent-to-agent communication, enabling coor-
dination across heterogeneous agent systems. IBM’s Agent Communication
Protocol (ACP) [49] and the Agent Network Protocol (ANP) [4] addressed
further coordination challenges at network scale. Microsoft [44] proposed
NLWeb, bringing natural language interfaces to websites and positioning ev-
ery NLWeb endpoint as an MCP server — a significant step toward agent-
readable web content.
    Kapoor et al. [37] provided the most comprehensive survey of agent in-
frastructure requirements to date, cataloging use cases, limitations, and open
problems across memory, execution, and communication layers. Li et al.
[41] proposed a conceptual model for the agentic web across intelligence, in-
teraction, and economic dimensions, identifying architectural challenges in
protocol design and agent orchestration. The W3C Agent Web Community
Group [53] identified four core trends in agent-web interaction and three pri-
mary challenges including data silos, human-machine interface friction, and
absence of standard protocols.
    While these works make important protocol-level contributions, they ad-
dress the access and interoperability problem in isolation. They do not ex-
amine the economic model that must accompany open agent access, nor the
epistemic consequences of AI-generated content recursion. Our framework
synthesizes the protocol layer with the economic and content layers to pro-
duce a unified redesign proposal.

2.3. Web Economics and the Attention Economy
    The economic foundations of the web have been studied extensively in
the context of human interaction. Evans [29] characterized the web’s ad-
vertising model as a two-sided market connecting publishers and advertisers


                                      7
through human attention as the mediating resource. Wu [56] traced the his-
torical development of the attention economy, demonstrating how successive
communication technologies — radio, television, the web — converged on
attention capture as the primary economic mechanism.
    The disruption of this model by AI is increasingly documented empir-
ically. Cloudflare [22] reported crawl-to-referral ratios of 73,000:1 for AI
crawlers by mid-2025, demonstrating the complete breakdown of the value
exchange that historically justified open crawler access. Semrush [50] docu-
mented that 93% of searches in AI-native modes end without a click, while
SISTRIX [52] reported click-through rate declines from 27% to 11% at posi-
tion one in AI-augmented search. Cloudflare [21] described the infrastructure
response to these dynamics — default blocking of AI crawlers and introduc-
tion of pay-per-crawl models — as the first large-scale attempt to impose
economic structure on agent access.
    Proposed economic responses have been largely reactive and incomplete.
Perplexity’s publisher revenue sharing [2] and Cloudflare’s pay-per-crawl
model [21] address specific friction points without a principled framework.
Nguyen et al. [45] examined micropayment models for agent content access
but did not address the agent-as-human-proxy principle or the distinction be-
tween personal and commercial agent use. Our work contributes the intent-
based economic tier model — grounded in the philosophical principle that
an agent’s economic obligation mirrors that of the human it represents — as
a principled alternative to universal payment requirements.

2.4. Content Provenance and Epistemic Integrity
    The question of content provenance has gained urgency with the prolif-
eration of AI-generated content. Zellers et al. [58] demonstrated early that
neural text generation could produce indistinguishable fake news, motivat-
ing provenance research. Kirchenbauer et al. [39] proposed watermarking
techniques for LLM outputs, enabling statistical detection of AI-generated
text. The C2PA (Coalition for Content Provenance and Authenticity) stan-
dard [25] established cryptographic provenance for media content, providing
a technical foundation for authorship declaration at the content layer.
    Most directly relevant to our epistemic recursion argument, Shumailov
et al. [51] demonstrated the phenomenon of model collapse — the progressive
degradation of model quality when trained on AI-generated data — providing
empirical grounding for our theoretical framing. Martini et al. [43] examined
provenance requirements for agentic content pipelines, and Bender et al.

                                     8
[17] characterized large language models as stochastic parrots — systems
that recombine existing patterns without grounding in world experience — a
characterization that motivates the human-intentionality anchor we propose.
    Existing provenance work addresses detection and attribution of AI-
generated content but does not address the systemic architectural question
of how the web should be redesigned to preserve epistemic integrity at scale.
Our provenance-anchored content architecture extends this work by propos-
ing a web-level standard for declaring content origin, derivation chain, and
human oversight level — going beyond detection to prevention of epistemic
recursion.

2.5. Summary and Positioning
    Table 1 summarizes the coverage of representative related works across
the six key dimensions of our framework: agent access model, behavioral
contracts, economic framework, intent-based tiers, epistemic recursion, and
provenance architecture. As the table shows, existing works address indi-
vidual dimensions in isolation. Our framework is the first to address all six
dimensions simultaneously, grounded in a unified social contract redesign
philosophy.

3. The Human-Centric Web: A Three-Layer Diagnosis
    The World Wide Web was not designed with a single deliberate choice
to exclude non-human participants — rather, its human-centricity emerged
organically from three decades of architectural decisions, each reasonable
in isolation, that collectively produce a web hostile to agent-first interac-
tion. In this section, we diagnose this incompatibility systematically across
three layers: access, economics, and content. For each layer, we identify the
foundational human-centric assumption, demonstrate empirically how that
assumption fails under agent interaction, and characterize the nature of the
resulting incompatibility. Proposed solutions to each layer are deferred to
Sections 3.1, 3.2, and 3.3 respectively.

3.1. Layer 1: The Access Model
3.1.1. The Human-Centric Assumption
    The web’s access model was designed around the presumption of human
visitors. When a human navigates to a website, the interaction carries a set
of implicit guarantees that the web’s architecture has never needed to make

                                     9
Table 1: Comparison of related work across key dimensions of the agent-first web redesign
framework. ✓ = addressed; ✗ = not addressed; ∼ = partially addressed.

                                    Agent       Behavioral    Economic   Intent-based   Epistemic   Provenance
             Work
                                 access model   contracts    framework       tiers      recursion   architecture

 Yao et al. [57]                     ∼             ✗            ✗             ✗            ✗            ✗
 Zhou et al. [59]                    ∼             ✗            ✗             ✗            ✗            ✗
 Deng et al. [26]                    ∼             ✗            ✗             ✗            ✗            ✗
 Wang et al. [54]                    ∼             ✗            ✗             ✗            ✗            ✗
 Kapoor et al. [37]                  ✓             ✗            ∼             ✗            ✗            ✗
 Li et al. [41]                      ✓             ✗            ∼             ✗            ✗            ✗
 Anthropic MCP [5]                   ✓             ✗            ✗             ✗            ✗            ✗
 Google A2A [33]                     ✓             ✗            ✗             ✗            ✗            ✗
 Microsoft NLWeb [44]                ✓             ✗            ✗             ✗            ✗            ✗
 W3C Agent Web CG [53]               ✓             ∼            ✗             ✗            ✗            ✗
 Cloudflare Pay-per-crawl [21]       ∼             ✗            ∼             ✗            ✗            ✗
 Nguyen et al. [45]                  ✗             ✗            ✓             ✗            ✗            ✗
 Shumailov et al. [51]               ✗             ✗            ✗             ✗            ✓            ✗
 C2PA [25]                           ✗             ✗            ✗             ✗            ✗            ∼
 Kirchenbauer et al. [39]            ✗             ✗            ✗             ✗            ∼            ∼
 Bender et al. [17]                  ✗             ✗            ✗             ✗            ∼            ✗
 Evans [29]                          ✗             ✗            ✓             ✗            ✗            ✗
 Wu [56]                             ✗             ✗            ✓             ✗            ✗            ✗
 This paper (proposed)                ✓             ✓           ✓            ✓             ✓            ✓



explicit: the visitor is a single individual, operating at human speed, consum-
ing content for personal use, and subject to social and legal accountability
for their actions. These implicit guarantees justified the web’s foundational
philosophy of open access — articulated by Berners-Lee as the principle that
any client should be able to retrieve any resource without prior negotiation
[18]. Security mechanisms such as CAPTCHAs operationalize this assump-
tion directly, treating human biological capability as the access credential
[1].
     The only formal mechanism for non-human access management is the
robots.txt standard, introduced in 1994 [40]. Designed for search engine
crawlers operating under an implicit social contract — crawl freely, return
traffic — robots.txt is an honor system with no enforcement mechanism,
no concept of agent identity, no support for graduated access levels, and
no capacity to distinguish between a personal assistant agent acting for one
user and a mass scraper extracting content for commercial training [21]. It
was adequate when the only non-human visitors were well-behaved search
crawlers. It is wholly inadequate for the agent-first web.


                                                    10
3.1.2. Empirical Evidence of Failure
    The incompatibility of the current access model with agent interaction is
now empirically documented at infrastructure scale. Cloudflare, which routes
over 16% of global internet traffic, moved in July 2025 to block AI crawlers
by default — the first time in the web’s history that a major infrastructure
provider has treated non-human access as an opt-in rather than a default
right [21]. Between July 2025 and January 2026, the number of websites
actively blocking AI crawlers was nearly seven times the number blocking
traditional search crawlers such as Googlebot [24, 14]. Raw requests from
GPTBot grew 147% from July 2024 to July 2025, while Meta-ExternalAgent
grew 843% over the same period [23], demonstrating that the scale asymme-
try between human and agent access is not marginal but orders of magnitude.
    The economic asymmetry driving this blocking response is equally stark.
Cloudflare data from mid-2025 reveals that Google’s search crawler — op-
erating under the traditional crawl-for-traffic social contract — crawled ap-
proximately 14 pages per human referral generated. By contrast, OpenAI’s
crawler exhibited a crawl-to-referral ratio of 1,700:1, and Anthropic’s crawler
73,000:1 [22]. From a publisher’s perspective, this ratio represents pure ex-
traction: content consumed at massive scale with essentially zero value re-
turned. The blocking response is rational given this asymmetry — but it is
a symptom of architectural failure, not a solution.

3.1.3. The Nature of the Incompatibility
    The fundamental incompatibility at the access layer is not that agents
access content — humans do that too — but that the web has no mechanism
to distinguish between access types that carry very different implications:

   • A personal agent acting for one user, consuming content on their be-
     half as a proxy for a human visit — analogous to a human reading a
     webpage.

   • A search agent crawling content to build an index that returns traffic to
     publishers — analogous to Googlebot under the original social contract.

   • A training crawler bulk-extracting content to train commercial AI mod-
     els — a use case with no human analog and genuinely novel economic
     implications.



                                      11
   • A malicious bot probing for vulnerabilities, scraping for competitive
     intelligence, or performing denial-of-service — which should be blocked
     regardless of whether the visitor is human or agent.

   Because current infrastructure cannot distinguish these cases, the default
response is to block all non-human access indiscriminately — effectively treat-
ing a personal assistant agent acting for a paying subscriber with the same
hostility as a malicious scraper. This is the access layer’s core failure: the
absence of an agent identification and intent declaration mechanism that
would enable graduated, context-appropriate responses rather than binary
block-or-allow decisions.

3.2. Layer 2: The Economic Model
3.2.1. The Human-Centric Assumption
    The web’s economic model is built on the attention economy — a two-
sided market in which publishers provide content to attract human attention,
and advertisers pay to access that attention [29, 56]. Every economic mecha-
nism the web has developed — advertising impressions, click-through rates,
pageviews, time-on-site, subscription paywalls — is a proxy for human at-
tention. The implicit assumption is that value flows when a human engages
with content: seeing an advertisement, clicking a link, spending time read-
ing. This model sustained a diverse publishing ecosystem for three decades,
funding journalism, research, creative work, and open knowledge resources.
    The attention economy’s dependence on human engagement as its funda-
mental unit of value is not incidental — it is structural. Remove the human
from the content consumption loop and the entire economic architecture col-
lapses, because there is no attention to monetize, no click to count, and no
impression to sell.

3.2.2. Empirical Evidence of Failure
    AI agents are removing humans from the content consumption loop at
measurable and accelerating scale. Zero-click searches — where AI systems
synthesize answers without routing users to source content — now account for
approximately 60% of all Google queries [50]. In AI-native search modes, this
figure rises to 93% [50]. Only 1% of users click links inside an AI Overview
[46]. Click-through rates at position one in search results have fallen from
27% to 11% as AI Overviews have become pervasive [52]. The downstream
impact on publishers is severe and accelerating — HubSpot reported organic

                                      12
traffic declines of 70–80%, Chegg lost 49% of its traffic, and NPR character-
ized the shift as an extinction-level event for online news [52].
    The economic asymmetry driving this blocking response is equally stark.
Cloudflare data from mid-2025 reveals that Google’s search crawler — operat-
ing under the traditional crawl-for-traffic social contract — crawled approxi-
mately 14 pages per human referral generated. By contrast, OpenAI’s crawler
exhibited a crawl-to-referral ratio of 1,700:1, and Anthropic’s crawler 73,000:1
[22]. Zero-click searches now account for approximately 60% of all Google
queries [50], rising to 93% in AI-native search modes, with click-through rates
at position one falling from 27% to 11% [52]. Figure 1 illustrates how the
human web’s working value chain — where content consumption generates
ad revenue that returns to publishers — is structurally broken under agent
interaction, where content is consumed at scale with zero economic return.




Figure 1: The broken economic loop. In the human web (top), content consumption
generates advertising revenue that returns to publishers, sustaining the content ecosystem.
In the agent web (bottom), agents retrieve and synthesize content on behalf of users
without generating pageviews, clicks, or impressions — delivering value to users while
returning zero economic signal to publishers. This structural asymmetry is the primary
driver of blanket agent blocking.


3.2.3. The Nature of the Incompatibility
    The economic incompatibility has three distinct components that must
be addressed separately:


                                            13
    The consumption problem. When an agent retrieves and synthesizes
content on behalf of a user, the publisher receives no economic signal — no
impression, no click, no pageview. The value delivered to the user is real;
the value returned to the publisher is zero. This is not a problem of agent
malice but of architectural mismatch: the web has no mechanism for value
exchange at the point of agent consumption.
    The attribution problem. When an agent synthesizes an answer from
multiple sources, there is no mechanism for fractional attribution — no way
to record that source A contributed 40% of the answer’s informational content
and source B contributed 60%, and to distribute economic value accordingly.
Human-web economics were never required to solve this problem because
humans visit one page at a time.
    The production problem. As AI generates increasing proportions of
web content, the human creative labor that justified content economics —
the journalist’s investigation, the researcher’s analysis, the expert’s judg-
ment — is displaced. An economic model that does not distinguish between
human-authored and AI-generated content provides no incentive for the hu-
man contribution that grounds content quality and epistemic integrity.

3.3. Layer 3: The Content Model
3.3.1. The Human-Centric Assumption
    The web’s content architecture was designed for human perception.
HTML encodes visual layout, typography, color, and interactive behavior
— all properties relevant to human reading experience and irrelevant to ma-
chine comprehension [47]. Search engine optimization, link structures, and
content discovery mechanisms were designed around human attention pat-
terns and search intent [20]. Even the semantic web effort — intended to
make content machine-readable — was designed to augment human-targeted
HTML rather than replace it [19].
    The result is a content layer that is simultaneously over-specified for hu-
man rendering — carrying vast amounts of visual layout information irrel-
evant to agents — and under-specified for machine comprehension, lacking
the semantic structure, provenance information, and intent metadata that
agents need to evaluate and use content reliably.

3.3.2. Empirical Evidence of Failure
    The inefficiency of current web content formats for agent consumption
is quantifiable. [55, 15] demonstrated that agent-optimized content delivery

                                      14
— stripping visual rendering overhead and providing structured semantic
content — achieves a 67.6% reduction in token usage compared to standard
HTML delivery. Since token consumption is directly proportional to com-
putational cost in LLM-based agents, this represents a massive structural
inefficiency imposed on every agent interaction with the current web.
    Beyond format inefficiency, the content layer faces a structural integrity
problem with no precedent in the human web. [51] demonstrated the phe-
nomenon of model collapse — the progressive degradation of AI model qual-
ity when trained iteratively on AI-generated data. Each generation of AI
content introduces statistical artifacts, amplifies existing biases, and loses
the diversity that characterizes human-origin content. When this content
re-enters the training pipeline, these artifacts compound. The web, as the
primary reservoir of training data for large language models, is thus at risk
of becoming a source of progressively degraded knowledge — not through
any deliberate action but through the structural dynamics of AI content
generation at scale. We term this phenomenon epistemic recursion: the self-
referential loop in which AI-generated content becomes the input for future
AI content generation, progressively detaching web knowledge from human
ground truth. Figure 2 illustrates this loop and its compounding degradation
across generations.




                                     15
Figure 2: The epistemic recursion loop. Human-origin knowledge enters the web through
AI-generated content. AI agents retrieve and synthesize this content to produce further
content, which re-enters the web for subsequent retrieval. Each cycle amplifies statistical
artifacts and biases while reducing diversity, progressively detaching web knowledge from
human ground truth. The dashed arrow represents the feedback path that sustains the
loop across generations. Unlike model collapse [51], which describes degradation within a
single training pipeline, epistemic recursion describes a web-scale phenomenon operating
across the entire AI content ecosystem.

3.3.3. The Nature of the Incompatibility
    We identify three distinct content-layer incompatibilities:
    The format incompatibility. Current web content formats — HTML,
JavaScript-rendered pages, PDF documents — carry significant visual ren-
dering overhead that is meaningless to agents and computationally expensive
to process. Agents require structured semantic content: clean text, explicit
metadata, machine-readable relationships between concepts. The web cur-
rently has no standard format serving this requirement, though recent pro-
posals such as llms.txt [36] represent early steps toward agent-readable
content declarations.
    The provenance incompatibility. Current web content carries no
standard mechanism for declaring its origin, derivation chain, or the degree
of human oversight involved in its production. An agent retrieving a web
page cannot determine whether it is reading a human expert’s peer-reviewed
analysis, an AI-generated content farm article, or a human-AI collaborative
piece. This absence of provenance metadata prevents agents from making

                                            16
quality-aware content decisions and enables the epistemic recursion problem
described above.
    The discoverability incompatibility. Search engine optimization was
built to attract human attention through search rankings optimized for hu-
man query patterns. There is no equivalent agent discoverability standard —
no mechanism by which an agent can determine which site holds authorita-
tive data on a topic, what content formats a site supports, what access terms
apply, or what semantic capabilities a site exposes. Agents currently nav-
igate content discovery through human-facing search interfaces, producing
significant inefficiency and unreliability.

3.4. Summary: Three Layers, One Failure
    The three failures diagnosed in this section are not independent — they
are deeply coupled in a self-reinforcing cycle. The access layer’s inability
to identify agent intent drives blanket blocking, which prevents the develop-
ment of economic models for legitimate agent access. The absence of eco-
nomic models eliminates the incentive for publishers to invest in high-quality,
human-supervised content production. The collapse of human-supervised
content production accelerates epistemic recursion, further degrading the
web’s knowledge quality and reinforcing the perception that agent access
is extractive rather than valuable — which in turn strengthens the case for
blanket blocking. Figure 3 illustrates this interdependency. Addressing any
single layer in isolation — as existing work has largely done — produces
solutions that are undermined by the failures of the other two. A coherent
redesign must address all three layers simultaneously, grounded in a unified
philosophical foundation, which we develop in the following sections.




                                      17
Figure 3: Three-layer failure coupling. The access, economic, and content layer failures of
the human-centric web are deeply interdependent. Blanket blocking (access) prevents the
development of economic models; absent economic models eliminate incentives for quality
content production; degraded content quality reinforces the case for blocking. The dashed
arc represents the feedback path completing the cycle. Fixing any single layer in isolation
creates new contradictions — all three must be redesigned simultaneously.

    Table 2 summarizes the three-layer diagnosis across the key dimensions
of assumption, empirical evidence, and nature of incompatibility.
  Table 2: Three-layer diagnosis of human-centric web failure under agent interaction.

                   Human-centric                            Empirical                                     Nature of
  Layer
                    assumption                              evidence                                   incompatibility

             Visitors are single humans               7× more sites                            No mechanism to distinguish
Access                                                                            [24]
                  at human speed                blocking AI vs Googlebot                          agent types or intent
             Value flows through human     73,000:1 crawl-to-referral ratio [22];           No value exchange at point of agent
Economic                                                                          [50]
                attention and clicks           93% zero-click in AI search                  consumption; attribution impossible
           Content is human-authored and    67.6% token overhead in HTML [55];           Format overhead; no provenance standard;
Content
           rendered for human perception    model collapse under AI training [51]                epistemic recursion risk




4. The Access Layer Redesign
    Having diagnosed the three-layer failure of the human-centric web in Sec-
tion 3, we now turn to proposed solutions. This section addresses the access

                                                            18
layer, proposing a principled redesign grounded in a single philosophical an-
chor: that AI agents acting on behalf of humans are first-class web citizens
entitled to the same presumption of access as the humans they represent.

4.1. The Agent-as-Human-Proxy Principle
    The web’s founding access philosophy — articulated by Berners-Lee as
the principle that any client should be able to retrieve any resource without
prior negotiation [18] — was grounded in a presumption of human visitors.
We propose extending this presumption to AI agents through what we term
the agent-as-human-proxy principle:

      An AI agent acting on behalf of a human user should inherit the
      same presumption of access as that human — no more, no less.
      The agent’s access rights, obligations, and economic responsibili-
      ties are determined by the human it represents, not by its nature
      as an automated system.

     This principle has several important implications. First, it establishes
that the relevant unit of access is the human-agent pair, not the agent in
isolation. An anonymous human can browse freely — their agent should too.
A subscribed human has paid for access — their agent should inherit it. A
human cannot legally bulk-scrape a million pages for commercial resale —
neither can their agent. Second, it implies that blanket blocking of agents is
philosophically unjustifiable when those agents represent humans who would
otherwise be welcome. Third, it identifies the two genuinely novel cases that
fall outside the human-proxy principle — commercial training use and multi-
user content aggregation — as the only cases requiring new access rules rather
than extensions of existing human-web norms.
     The agent-as-human-proxy principle does not eliminate the need for agent
identification — it defines what that identification must accomplish. Rather
than requiring agents to prove full identity (which raises privacy concerns
and creates friction), agents need only declare the behavioral context that
makes the proxy relationship legible: who they represent, at what scale, and
for what purpose.

4.2. Agent Identification Metadata
    The central technical contribution of this section is the proposal for agent
identification metadata — a set of standardized HTTP request headers that

                                      19
allow agents to declare their identity, represented user, and intent to web
servers. This proposal is grounded in a direct analogy to existing browser
identification mechanisms.
    When a browser makes an HTTP request, it sends a set of headers that
identify its capabilities and context [31]:

User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X)
Accept: text/html,application/xhtml+xml
Accept-Language: en-US,en;q=0.9

    Servers read these headers to serve appropriate content — mobile vs desk-
top layouts, supported media types, preferred language versions. No new
protocol is required; the mechanism is embedded in the existing HTTP in-
frastructure that every web server already supports.
    We propose an analogous mechanism for agents:

Agent-Identity: claude/sonnet-4
Agent-Represents: user/anonymous
Agent-Intent: personal-use
Agent-Auth: Bearer <delegation-token>
Agent-Rate-Class: free

     The semantics of each header are as follows. Agent-Identity de-
clares the agent system and version — analogous to User-Agent for
browsers. Agent-Represents declares the relationship between the agent
and the human it serves — anonymous, authenticated, or subscribed.
Agent-Intent declares the purpose of the request from a controlled vo-
cabulary: personal-use, search, training, commercial, or research.
Agent-Auth carries a delegation token linking the agent to a human user’s ex-
isting credentials — enabling subscription inheritance without exposing per-
sonal identity. Agent-Rate-Class declares the agent’s expected consump-
tion tier, enabling servers to pre-authorize appropriate rate limits.
     Figure 4 illustrates the full request-response flow enabled by agent iden-
tification metadata, showing how servers can distinguish agent types and
respond with graduated access rather than binary blocking.




                                      20
Figure 4: Agent identification metadata flow. An AI agent sends standardized metadata
headers alongside its HTTP request, declaring identity, represented user, and intent. The
web server reads these headers to identify the agent type, verify authorization, apply
appropriate rate limits, and select the correct content format (ATML for agents, HTML
for humans). All communication occurs over existing HTTP/TCP infrastructure — no
new transport protocol is required. The metadata mechanism directly extends the browser
User-Agent identification pattern already ubiquitous in web infrastructure.


    This proposal requires no new transport protocol — everything operates
over existing HTTP infrastructure that every web server already supports. It
is backward compatible: servers that do not recognize agent metadata head-
ers simply ignore them, serving their existing content as before. Adoption
can be incremental, with agent-aware servers gaining the ability to serve op-
timized content and apply graduated access controls while non-aware servers
continue to function normally.
    A critical security consideration is metadata verification. Unlike browser
User-Agent headers, which carry no cryptographic guarantee, agent metadata
headers should be cryptographically signed to prevent impersonation — the
Perplexity case demonstrated that bad actors will modify agent identifiers
to circumvent restrictions [2]. We propose that the Agent-Identity header
be accompanied by a cryptographic signature verifiable against a public key
registry maintained by registered agent operators, analogous to DKIM sig-
natures for email [3]. This does not prevent all impersonation but raises the
cost significantly above simple header modification.


                                           21
4.3. Rate Limiting as the New Default
    The agent-as-human-proxy principle implies that blanket blocking of
agents is not a legitimate long-term access policy — it is a reactive mea-
sure taken in the absence of better tools. Agent identification metadata pro-
vides those tools. Once servers can distinguish agent types and intents, the
appropriate response is graduated rate limiting rather than binary blocking.
    We propose that the default access control posture for agent requests shift
from block unless permitted to rate limit unless escalated, mirroring the web’s
existing posture toward anonymous human visitors. Figure 5 illustrates the
proposed tier model.




Figure 5: Graduated rate limiting model replacing blanket blocking. Agent access is tiered
by declared intent and authentication level rather than binary blocked or allowed. Anony-
mous personal agents receive rate-limited free access, equivalent to anonymous human
browsing. Authenticated agents inherit their represented user’s subscription. Training
crawlers access a licensed tier with negotiated terms. Only malicious behavior — not
agent identity — triggers blocking. This model preserves the web’s open access philoso-
phy while providing servers with meaningful differentiation between agent types.


    The specific rate limits for each tier are not mandated by this framework
— they are determined by individual publishers based on their content eco-
nomics and infrastructure capacity. The framework mandates only the struc-
ture: that tiers exist, that they are determined by intent and authentication
level rather than by agent identity alone, and that blocking is reserved for
behaviorally malicious access rather than applied to all non-human requests
indiscriminately.

                                           22
4.4. Subscription Inheritance Protocol
    Perhaps the most immediately actionable proposal in this paper is sub-
scription inheritance — the principle that a human user’s existing paid sub-
scriptions should extend to their AI agents without requiring separate agent
subscriptions. This is a direct application of the agent-as-human-proxy prin-
ciple: if a human has paid for access, their agent proxy should have it too.
    Technically, this requires a lightweight extension to existing OAuth 2.0
delegation mechanisms [34]. A user authenticates with a content provider
as normal, obtaining an access token. When authorizing their AI agent, the
user generates a delegation token — a derived credential that encodes:

   • The human user’s subscription level and scope

   • The agent system authorized to use it

   • The permitted use cases (personal-use only, no training, no redistribu-
     tion)

   • An expiry and revocation mechanism

    The delegation token is passed as the Agent-Auth header in agent re-
quests. The server verifies the token, confirms it maps to a valid subscription,
and grants the agent the same content access the human subscriber would
receive. The human user’s subscription is not consumed or duplicated — it
is extended to their proxy.
    This mechanism has several advantages over alternative approaches. It
requires no changes to existing subscription billing infrastructure. It pre-
serves publisher revenue — the human still pays for subscription, the agent
merely inherits it. It gives users meaningful control over what their agents
can access on their behalf. And it is directly compatible with existing OAuth
infrastructure deployed by virtually every major content platform.

4.5. Dual-Layer Web Architecture
    The access layer redesign requires not only new identification and autho-
rization mechanisms but a new approach to content delivery. We propose a
dual-layer web architecture in which the same domain serves both human-
readable HTML and agent-optimized content — with the server selecting the
appropriate format based on request metadata.


                                      23
    This is not a new concept in web architecture — content negotiation
has been part of HTTP since its earliest versions [31], enabling servers to
serve different content types to different clients. The Accept header allows
browsers to declare their preferred media types; servers respond with the
best available match. We propose extending this mechanism to include an
agent-optimized content type — which we call ATML (Agent Text Markup
Language, developed in Section 6) — as a first-class content type alongside
HTML.
    A browser request declares:

Accept: text/html, application/xhtml+xml

   An agent request declares:

Accept: application/atml+xml, text/markdown
Agent-Identity: claude/sonnet-4
Agent-Intent: personal-use

    The server responds with HTML to the browser and ATML to the agent
— the same content, differently structured. No separate domain, no separate
publishing workflow. Publishers maintain one content repository; the server
layer handles format negotiation.
    Figure 6 illustrates this architecture and the three-phase migration path
from the current human-only web to an agent-first web.




                                     24
Figure 6: Dual-layer web architecture and migration path. The same domain serves HTML
responses to browser requests and ATML responses to agent requests, with format selection
driven by request metadata. Phase 1 represents the current state (HTML only). Phase
2 introduces parallel ATML alongside HTML. Phase 3 establishes ATML as the primary
format with HTML maintained for legacy compatibility — analogous to how HTTPS was
added alongside HTTP before becoming the mandatory standard.


    The migration path is deliberately gradual. Phase 1 represents the cur-
rent state — human HTML only, with agent metadata headers added as a
forward compatibility measure. Phase 2 introduces ATML as a parallel de-
livery format, with publishers adopting it incrementally. Phase 3 establishes
ATML as the primary delivery format, with HTML maintained for legacy
browser compatibility. This mirrors the HTTPS migration: years of coexis-
tence, then a tipping point driven by security requirements, then universal
adoption [30].

4.6. A New agents.txt Standard
    The final component of the access layer redesign is a replacement for
robots.txt — a richer, machine-readable standard that declares a site’s
agent access policy in a way that the existing honor-system standard cannot.
We propose agents.txt, a structured declaration file served at a well-known
URL (/.well-known/agents.txt) that encodes:

                                           25
# agents.txt example
[personal-agent]
allow: true
rate-limit: 100000 tokens/day
content-format: atml, markdown
auth-required: false

[subscribed-agent]
allow: true
rate-limit: unlimited
content-format: atml, markdown
auth-required: true
auth-type: delegation-token

[training-crawler]
allow: conditional
license-required: true
contact: licensing@publisher.com

[malicious-bot]
allow: false

    Unlike robots.txt, agents.txt is not an honor system — its declara-
tions are enforced by the agent identification metadata mechanism. A server
receiving a request with Agent-Intent: training can automatically ap-
ply the [training-crawler] policy declared in agents.txt, without manual
configuration per crawler. Publishers gain granular control over agent access
without resorting to blanket blocking. Agents gain clear, machine-readable
signals about what access is available and under what terms — eliminating
the current situation where agents must attempt access and interpret failures
heuristically.

4.7. Summary
    Table 3 summarizes the access layer redesign proposals and their rela-
tionship to the failures diagnosed in Section 3.1.




                                     26
      Table 3: Access layer redesign: diagnosed failures and proposed solutions.

                       Diagnosed failure         Proposed solution

                      No agent iden- Agent    identification
                      tity standard  metadata headers over
                                     HTTP
                      Blanket blocking     Graduated rate limiting
                      default              by intent and auth level
                      No subscription OAuth delegation token
                      extension       for subscription inheri-
                                      tance
                      HTML-only de- Dual-layer architecture
                      livery        with ATML content
                                    negotiation
                      robots.txt inade- agents.txt   —     rich
                      quacy             machine-readable access
                                        policy


     Together these five proposals constitute a complete access layer redesign
that preserves the web’s founding philosophy of open access while provid-
ing the identification, authorization, and policy infrastructure necessary for
servers to respond to agents appropriately rather than defensively. Crit-
ically, all proposals operate over existing HTTP/TCP infrastructure — no
new transport protocol is required. The agent-first web is not a new internet;
it is the existing internet with the missing metadata layer added.

5. The Economic Layer Redesign
    The access layer redesign proposed in Section 4 establishes how agents
reach content. This section addresses what happens when they do — propos-
ing an economic framework that replaces the broken attention economy with
a principled value-exchange model. We argue that the economic redesign
must be grounded in the same philosophical anchor as the access redesign:
the agent-as-human-proxy principle. An agent’s economic obligation mirrors
that of the human it represents — no more, no less.

5.1. The Attention Economy Cannot Be Patched
    The web’s attention economy was not designed — it emerged organi-
cally as advertising became the dominant funding mechanism for online con-
tent [29, 56]. Its core mechanism — human attention proxied by clicks and

                                            27
pageviews, monetized through advertising impressions — worked because it
created a closed value loop: publishers produced content, humans consumed
it, advertisers paid for access to that attention, and revenue returned to pub-
lishers who produced more content. Every layer of the web’s architecture
evolved to serve this loop: SEO to attract human attention, analytics to
measure it, advertising networks to monetize it.
     AI agents do not fit this loop. They do not see advertisements. They
do not generate pageviews. They do not click. The value they deliver to
users is real — task completion, information synthesis, decision support —
but that value is entirely decoupled from the economic signals the attention
economy was built to capture. This is not a marginal disruption. Zero-click
searches now account for 93% of queries in AI-native search modes [50], and
click-through rates at position one have fallen from 27% to 11% [52]. The
attention economy is not being disrupted at the edges — it is collapsing at
its foundation.
     Reactive patches — Cloudflare’s pay-per-crawl model, Perplexity’s rev-
enue sharing program [2, 21] — address specific friction points without a
principled framework. They treat agent access as a billing problem rather
than a design problem. The result is an incoherent patchwork: some content
is paywalled per crawl, some is blocked outright, some is freely scraped, and
publishers have no consistent basis on which to make access decisions. A
principled framework is needed.

5.2. The Agent-as-Human-Proxy Economic Principle
    We propose that the economic redesign be grounded in a single principle
that resolves the majority of agent content access cases without requiring
new economic models:
     An agent’s economic obligation to a content publisher is equiva-
     lent to the economic obligation of the human it represents. If the
     content is free for anonymous humans, it is free for their agents.
     If the content requires a subscription, the agent inherits that sub-
     scription. The economic relationship is between the human and
     the publisher; the agent is a proxy, not a new economic entity.
   This principle is powerful because it resolves most agent content access
cases by reference to existing human-web economics — no new models re-
quired. It also identifies precisely where new models are needed: the gen-
uinely novel cases for which no human analog exists. These are commercial

                                      28
training use — where an agent bulk-extracts content to train AI models, a
use case no human performs — and multi-user aggregation — where a single
agent serves content to millions of users simultaneously, a scale no human
achieves. For these two cases, the human-proxy principle does not apply, and
new economic models must be designed from first principles.

5.3. The Intent-Based Economic Tier Model
    Applying the agent-as-human-proxy principle produces a natural taxon-
omy of agent content access behaviors, each with an appropriate economic
model. We term this the intent-based economic tier model. Figure 7 presents
the full model.




Figure 7: Intent-based economic tier model. Agent content access behaviors are classified
by declared intent and authentication level. The top three tiers — personal use, subscribed
access, and search/discovery — are resolved by the agent-as-human-proxy principle, map-
ping directly to existing human-web economic models. The bottom three tiers — com-
mercial training, multi-user aggregation, and bulk extraction — represent genuinely novel
cases with no human analog, requiring new economic models. The dividing line between
these groups is the boundary of the human-proxy principle.


   For the human-proxy tiers, the economic model is straightforward. A
personal agent accessing free content on behalf of an anonymous user pays
nothing — exactly as the user would. A subscribed agent accessing paywalled

                                            29
content inherits the user’s subscription via the delegation token mechanism
described in Section 4.4. A search agent crawling content for indexing op-
erates under the traditional crawl-for-traffic social contract, with a machine-
readable attribution requirement replacing the implicit honor system that
robots.txt currently relies on.
    For the novel tiers, new models are required. Commercial training ac-
cess requires a licensing framework analogous to stock photo or music sync
licensing — negotiated terms declared in agents.txt, with fees proportional
to the commercial value derived. Multi-user aggregation — where a single
AI system serves millions of users using content from many publishers —
requires a collective model analogous to music streaming royalties, discussed
in Section 5.

5.4. The Open/Closed Source Analogy
    The intent-based tier model preserves a critical property of the current
web: economic diversity. The web’s strength has never derived from a single
economic model — it derives from the coexistence of free and paid content,
open and proprietary knowledge, advertising-supported and subscription-
supported publishing. This diversity must be preserved in the agent-first
web.
    We propose framing the content economics decision for publishers through
an analogy that has already proven robust in the adjacent domain of software:
the open source / closed source distinction [48]. Just as a software developer
chooses whether to release code under an open license (freely available, po-
tentially with attribution requirements) or a proprietary license (paid access,
restricted use), a publisher chooses whether to make content available to
agents under an open model or a paid model. The choice is entirely the
publisher’s — the framework mandates no universal model.
    Under this framing:
    Open content is freely accessible to agents under the same terms as
humans. Rate limits apply as the boundary of free access — analogous
to open source licenses that permit free use but not unlimited commercial
exploitation. Wikipedia, government data, open research, personal blogs —
all of these continue to operate as they do today, with agents welcome on the
same terms as humans.
    Paid content requires economic exchange for agent access. Publishers
declare their pricing terms in agents.txt and content headers. The eco-
nomic model — subscription, per-token, outcome-based — is chosen by the

                                      30
publisher. The agent checks declared terms before accessing and pays accord-
ingly. The New York Times, academic journals, professional data services —
all of these can operate paid agent access tiers independently of their human
subscription models.
    This framing is politically important as well as technically clean. It does
not mandate that all content be paid — which would kill open knowledge and
information access. It does not mandate that content be free — which would
destroy publisher economics. It gives publishers the same choice software
developers have had for decades and lets the market produce diversity.

5.5. Token-Based Subscription Model
    For paid content, we propose the token-based subscription model as the
primary economic mechanism for agent content access. Rather than metering
access by pageviews, article counts, or time periods — all human-centric units
— content access is metered in tokens consumed, directly mirroring how AI
API access is priced today [5].
    Under this model, a publisher declares a price per million tokens for their
content. An agent consuming that content is billed based on tokens actu-
ally consumed from the response. Publishers can declare different prices for
different content tiers — breaking news vs archived content, premium analy-
sis vs commodity information — using the agents.txt pricing declarations
introduced in Section 4.6.
    Figure 8 illustrates the token-based subscription model and its relation-
ship to existing AI infrastructure.




                                      31
Figure 8: Token-based subscription model. Content access is metered in tokens consumed
rather than pageviews or article counts. Publishers declare price per million tokens; agents
pay on consumption. Free tier access is rate-limited by token budget rather than blocked.
The model is directly compatible with existing AI API billing infrastructure — the same
token metering used by major AI providers requires no new payment rails for adoption.

    The token-based model has several properties that make it well-suited
to agent content economics. First, it is directly compatible with existing
AI billing infrastructure. AI providers already meter token consumption for
API access — the same infrastructure can be extended to meter content
consumption, requiring no new payment rails. Second, it is proportional to
actual consumption. A short agent query that retrieves a single paragraph
costs less than a deep research task that retrieves thousands of articles —
unlike subscription models that charge fixed fees regardless of actual use.
Third, it is format-agnostic. ATML content, Markdown content, structured
data — all can be metered in tokens regardless of their format, providing a
unified pricing mechanism across the heterogeneous content landscape of the
web.
    For free-tier access, the token budget functions as a rate limit rather than
a paywall — an agent consuming 100,000 tokens per day of a publisher’s
content at no charge is welcome; an agent consuming 10 million tokens per
day for commercial purposes is directed to the paid tier. The boundary
is declared in agents.txt, enforced by the agent identification metadata
mechanism, and transparent to both agents and publishers.

                                            32
5.6. The Commissioned Content Economy
    The economic models described above address the demand side of agent
content economics — how agents pay for content they consume. We now
address the supply side: how content production in the agent-first web can
be economically sustainable and epistemically grounded.
    The epistemic recursion problem identified in Section 3.3 — the self-
referential loop in which AI generates content that AI consumes — arises
precisely because AI-generated content currently carries no economic cost and
no provenance requirement. Content farms flood the web with AI-generated
articles at negligible marginal cost; there is no economic signal distinguishing
this content from human-authored journalism, and no provenance mechanism
flagging it as AI-derived. The loop is sustained by the absence of economic
friction at the production stage.
    We propose the commissioned content economy as a structural solution
to this problem. Under this model, AI-generated content that enters the web
as a publishable resource — rather than as an ephemeral agent response —
is produced under a commissioning relationship: a human entity pays for the
content to be produced, establishing a human intentionality anchor at the
production stage. The commissioned content is published with a machine-
readable provenance tag declaring the commissioner, the producing agent,
and the human oversight level. Other agents and humans can access the
content under declared terms, with revenue flowing back to the commissioner.
    Figure 9 illustrates the commissioned content economy as a two-sided
marketplace.




                                      33
Figure 9: The commissioned content economy. On the supply side, a human entity com-
missions an AI agent to produce content under a paid agreement. The content is published
with a provenance tag declaring commissioner, producing agent, and human supervision
level. On the demand side, other agents and human readers access the content under
declared terms, paying where required. Revenue flows back to the commissioner. The
critical contribution of this model is the human commissioning decision at the production
stage — which introduces human intentionality as a ground truth anchor, breaking the
epistemic recursion loop even when the content itself is AI-generated.


    The commissioned content model does not require that all web content
be commissioned — the open web continues to exist for informal, personal,
and community-generated content. It provides an economic structure for the
subset of web content where quality, provenance, and trustworthiness matter
most: journalism, research, professional analysis, educational content. For
this subset, the commissioning relationship reintroduces the human judgment
that the epistemic recursion loop erodes — not by requiring humans to write
every word, but by requiring a human to decide that this content is worth
producing and to take responsibility for it.



                                           34
5.7. The Agent Advertising Model
    The attention economy’s primary mechanism — advertising — does not
disappear in the agent-first web. It transforms. When an agent retrieves
content on behalf of a human user and presents a synthesized response, there
remains a human attention moment: the user reading the agent’s output.
This moment is potentially monetizable, though the mechanism differs fun-
damentally from traditional web advertising.
    We sketch a preliminary model for agent-targeted advertising, acknowl-
edging that full development of this model constitutes a separate research
contribution beyond the scope of this paper. Under the proposed model,
publishers embed structured advertisement metadata in their ATML con-
tent alongside substantive content. When an agent retrieves and synthesizes
this content, it carries the advertisement metadata as part of its response
payload. The agent frontend — Claude, ChatGPT, Gemini, or other inter-
face — surfaces the advertisement to the human user at an appropriate point
in the interaction. An impression is recorded when the advertisement reaches
the human; revenue flows to the publisher whose content carried it.
    This model faces a significant open challenge: agent frontends have lim-
ited incentive to surface publisher advertisements, particularly when doing
so competes with their own monetization interests. Resolving this tension
requires either a protocol-level standard mandating advertisement carriage
— analogous to the must-carry rules in broadcast television regulation — or
a revenue-sharing agreement between publishers and agent frontend opera-
tors. Both approaches involve stakeholder coordination that extends beyond
technical standardization. We identify this as a priority open challenge in
Section 8 and flag it as a direction for future work.

5.8. Summary
    Table 4 summarizes the economic layer redesign proposals and their re-
lationship to the failures diagnosed in Section 3.2.




                                    35
     Table 4: Economic layer redesign: diagnosed failures and proposed solutions.

                       Diagnosed failure        Proposed solution

                      Attention econ- Intent-based tier model
                      omy     collapses grounded in agent-as-
                      under       agent human-proxy principle
                      interaction
                      No value ex- Token-based     subscrip-
                      change at point tion model — metered
                      of agent con- on consumption
                      sumption
                      Universal pay- Open/closed source anal-
                      ment mandates ogy — publisher chooses
                      kill open knowl- model
                      edge
                      No     economic Commissioned content
                      model for AI economy with human
                      content produc- intentionality anchor
                      tion
                      Attribution im- Collective pool model
                      possible at scale for multi-user aggrega-
                                        tion tiers
                      Ad model breaks Agent advertising model
                      without human (open challenge — future
                      attention       work)


   The economic layer redesign is the most complex of the three layers be-
cause it must accommodate the full diversity of the existing web — free
and paid, open and proprietary, advertising-supported and subscription-
supported — while introducing new mechanisms for the genuinely novel cases
that agent interaction creates. The intent-based tier model, grounded in the
agent-as-human-proxy principle, provides the organizing framework. The
token-based subscription model provides the primary mechanism for paid
access. The commissioned content economy addresses the supply side. To-
gether they constitute a coherent replacement for the attention economy —
one designed from first principles for a web in which agents are primary
consumers of content.




                                           36
6. The Content Layer Redesign
    The access layer redesign (Section 4) establishes how agents reach content
and identify themselves. The economic layer redesign (Section 5) establishes
how value flows when they do. This section addresses what the content
itself looks like in an agent-first web — proposing a new content format, a
human supervision standard, a provenance chain architecture, and an agent-
native discoverability mechanism. Together these proposals address the three
content-layer incompatibilities diagnosed in Section 3.3: format inefficiency,
provenance absence, and epistemic recursion.

6.1. Design Principles for Agent-First Content
    Before proposing specific mechanisms, we establish the design principles
that agent-first content must satisfy. These principles are derived from the
requirements of LLM-based agents as content consumers — requirements
that are fundamentally different from those of human readers.
    Semantic richness over visual presentation. Agents process mean-
ing, not appearance. HTML’s investment in visual layout — typography,
color, responsive grid systems, animation — is not merely neutral overhead
for agents; it is active noise that consumes token budget without contribut-
ing to comprehension. Agent-first content must prioritize semantic structure:
what is being said, who said it, what it is derived from, and how confident
the source is. Visual presentation is a secondary concern addressed by the
rendering layer of the agent frontend, not the content layer.
    Explicit provenance as a first-class property. An agent retrieving
content must be able to determine its origin, derivation chain, and human
oversight level without inferring it from context. Provenance is not metadata
appended to content — it is a structural property of the content itself, as
fundamental as the content body.
    Machine-readable access and license terms. An agent must be able
to determine, before consuming content, what terms govern that consump-
tion — free or paid, personal or commercial, redistributable or restricted.
These terms must be embedded in the content itself or in a well-known dec-
laration file, not buried in a human-readable terms-of-service page that no
agent can reliably parse.
    Token efficiency. Every token an agent consumes processing layout
noise rather than semantic content is a token wasted. webMCP Authors
[55], Bandara et al. [7] demonstrated that current HTML carries 67.6% to-

                                     37
ken overhead relative to semantic content alone. Agent-first content must
minimize this overhead — not merely for economic reasons but because to-
ken efficiency directly determines the quality and depth of agent reasoning
over content at scale.
    Dual-layer compatibility. The human web does not disappear. Agent-
first content must coexist with human-readable content through the dual-
layer architecture proposed in Section 4.5 — served from the same domain,
produced from the same content repository, differentiated only at the delivery
layer.

6.2. ATML: Agent Text Markup Language
    We propose the Agent Text Markup Language (ATML) as the content for-
mat for agent-first web delivery. ATML is not an entirely new language — it
is a structured semantic profile designed for machine consumption, composed
of three explicit layers: provenance, access terms, and semantic content. We
engage first with the question of whether a new format is necessary at all.

6.2.1. The HTML Debate
    Karpathy [38] has argued that HTML is already sufficiently structured for
agent consumption — that modern LLMs can parse HTML effectively and
that a new format is unnecessary overhead. This position has merit: HTML
does encode semantic structure through heading tags, paragraph tags, list
tags, and semantic HTML5 elements such as <article>, <section>, and
<main>. Many agents do navigate HTML-rendered web content successfully
today.
    We argue, however, that HTML is inadequate for three reasons beyond
parsing difficulty. First, the token overhead problem is structural, not in-
cidental: even well-structured semantic HTML carries layout, styling, and
scripting overhead that is irrelevant to agent consumption. The 67.6% token
reduction demonstrated by webMCP Authors [55], Bandara et al. [11] was
achieved not by better HTML parsing but by delivering a semantically equiv-
alent content representation without layout noise — a task HTML cannot
accomplish without effectively becoming a different format. Second, HTML
has no native provenance layer. The information an agent most needs —
who authored this, what was it derived from, what supervision level applies
— has no standardized HTML representation. Third, HTML has no native
machine-readable access terms layer. An agent cannot read a content license


                                     38
from HTML structure; it must parse a separate legal document written for
human readers.
   ATML addresses all three gaps while remaining grounded in familiar XML
syntax that existing tooling can process without new parsers.

6.2.2. ATML Structure
    ATML is organized into three layers, as illustrated in Figure 10.




Figure 10: ATML structure compared to current HTML. HTML carries significant visual
rendering overhead — layout tags, CSS, JavaScript, navigation, advertisement slots —
that is irrelevant to agent consumption and imposes a 67.6% token overhead [55]. ATML
replaces this with three explicit semantic layers: provenance (declaring origin, commis-
sioner, derivation chain, and human supervision level), access and economics (declaring
tier, rate limits, and pricing), and semantic content (clean text, summary, and structured
entities). The result is a format optimized for agent comprehension while carrying all the
metadata agents need to evaluate, cite, and pay for content appropriately.


    A minimal ATML document has the following structure:

<atml version="1.0">
  <provenance>
    <authored-by>human</authored-by>

                                           39
    <commissioned-by>NYT</commissioned-by>
    <derived-from>
      <source url="https://..."
              retrieved="2025-11-01"/>
    </derived-from>
    <supervised>true</supervised>
    <supervision-level>2</supervision-level>
  </provenance>
  <access>
    <tier>paid</tier>
    <rate-limit unit="tokens"
                period="day">100000</rate-limit>
    <price unit="per-million-tokens">
      2.50
    </price>
    <license>personal-use</license>
    <license>no-training</license>
  </access>
  <content>
    <title>Article title here</title>
    <summary>Agent-optimized abstract
             in 2-3 sentences.</summary>
    <body>Clean semantic text without
          layout or styling markup.
    </body>
    <entities>
      <entity type="person">Name</entity>
      <entity type="org">Organisation
      </entity>
    </entities>
  </content>
</atml>

    The <provenance> layer is the ATML element with no HTML equiva-
lent. It declares the authorship type (human, agent, or collaborative), the
commissioning entity, the sources the content was derived from with retrieval
dates, and the human supervision level from the tier model proposed in Sec-
tion 6.3. This layer directly enables agents to make quality-aware content

                                     40
decisions and breaks the epistemic recursion loop by making AI-origin con-
tent explicitly visible.
    The <access> layer declares economic terms in machine-readable form,
directly compatible with the token-based subscription model proposed in
Section 5.5. Agents read these terms before consuming content — no separate
legal document required.
    The <content> layer carries the semantic text without layout noise. The
<summary> field enables agents to make relevance decisions before consuming
the full body — a significant token efficiency gain for research tasks involving
many sources. The <entities> field provides structured key concepts that
enable downstream reasoning without full-body parsing.

6.3. Human Supervision Requirements
    The epistemic recursion problem identified in Section 3.3 cannot
be solved by format alone.        A provenance tag that always declares
<supervised>false</supervised> for AI-generated content is honest but
does not break the recursion loop — it merely labels it. Breaking the loop re-
quires reintroducing human intentionality into the content production chain
at a structural level.
    We propose a four-level human supervision tier model that classifies con-
tent by the degree of human involvement in its production. Each level maps
to a declared provenance value in ATML and carries implications for how
agents should weight the content in their reasoning. Figure 11 illustrates the
model.




                                      41
Figure 11: Human supervision tier model. Content is classified into four levels based
on degree of human involvement in production, from Level 0 (fully AI generated, no
human review) to Level 3 (fully human authored). Each level maps to a declared ATML
provenance value and carries implications for epistemic trust — the weight agents and
search engines assign to the content in reasoning and ranking. The model does not prohibit
AI-generated content; it makes the degree of human oversight transparent, enabling agents
to make quality-aware consumption decisions.


    Level 0 — No human oversight. Content is fully AI generated with
no human review before publication. Declared as supervised: false in
ATML provenance. Agents should assign lowest epistemic weight to Level
0 content and avoid using it as a primary source for factual claims. Search
engines and agent content indices should rank Level 0 content below human-
supervised content for informational queries.
    Level 1 — Human edited. Content is AI generated but reviewed and
edited by a human before publication. The human editor takes responsibil-
ity for factual accuracy and quality. Declared as supervised: partial.
Represents the minimum acceptable supervision level for content that will
be cited by agents as a source.
    Level 2 — AI assisted. Content is human authored with AI tools
used for assistance — drafting, research, editing — but with a human as
the primary author and decision-maker. Declared as supervised: true,
authored-by: human. This level encompasses most professional content
production in the near-term future and should be treated as equivalent to

                                           42
traditional human-authored content.
    Level 3 — Fully human authored. Content is produced without
AI involvement. Declared as supervised: full, authored-by: human.
This level provides the strongest epistemic ground truth signal and should
receive highest weight in agent reasoning for factual claims.
    The supervision tier model does not prohibit any level of AI involvement
in content production. It makes the degree of human oversight transparent
and machine-readable, enabling agents to make quality-aware content deci-
sions rather than treating all web content as equally trustworthy regardless
of origin. This is the structural mechanism by which the web can sustain
a diverse content ecosystem — including AI-generated content — without
collapsing into the epistemic recursion loop.

6.4. Provenance Chain Architecture
    The supervision tier model establishes what level of human oversight ap-
plies to a piece of content. The provenance chain architecture establishes how
that claim is verified. A provenance declaration is only as useful as the trust
placed in it — an AI content farm could declare supervised: true and
break the epistemic intent of the model entirely. Cryptographic verification
is required.
    We propose building ATML provenance on the Coalition for Content
Provenance and Authenticity (C2PA) standard [25], extending it with agent-
specific fields. Under this architecture, each ATML document carries a cryp-
tographic provenance certificate that encodes:

   • The identity of the publishing entity, verified against a public key in-
     frastructure

   • The supervision level declared, signed by the publishing entity

   • A hash of the content body at time of publication, enabling verification
     that content has not been modified post-publication

   • A chain of derived-from references, each with its own provenance cer-
     tificate, enabling agents to trace the epistemic lineage of a claim back
     to primary sources

   This architecture does not guarantee that supervision declarations are
honest — a bad actor who controls their own signing key can still declare

                                      43
false supervision levels. However, it makes false declarations attributable: if
a publisher is found to have systematically declared false supervision levels,
their signing key can be revoked from the public key infrastructure, removing
trust from all their content. The reputational and legal consequences of
provenance fraud create a deterrent analogous to the consequences of false
advertising in existing legal frameworks.
    The derived-from chain is particularly important for breaking epistemic
recursion. When an agent traces the provenance chain of a piece of content
and finds that it derives from another AI-generated piece, which derives
from another AI-generated piece, without a human-authored primary source
anywhere in the chain, it has detected epistemic recursion in action. Agents
can be designed to flag such chains and reduce the weight assigned to content
with deep AI-only derivation chains — a practical circuit breaker for the
recursion loop that requires no centralised authority to operate.

6.5. Agent Content Discoverability
    The human web’s discovery mechanism — search engines optimizing for
human attention and click-through — does not serve agent needs. An agent
does not want the most popular result; it wants the most authoritative,
most accurately provenance-tagged, most appropriately-priced result for its
specific task. These are different optimization targets requiring different
infrastructure.
    We propose an agent content discoverability architecture built on a capa-
bility declaration standard and an agent-optimized search index. Figure 12
illustrates the full discoverability flow.




                                      44
Figure 12: Agent content discoverability architecture. An agent queries an agent search
index optimized for semantic relevance, provenance quality, and access terms rather than
human attention signals. The index returns ATML endpoints from publishers who have
declared agent capabilities in a structured agents.json file. The agent fetches the ca-
pability declaration to understand available content types, supervision levels, and pricing
before making content requests. This eliminates blind scraping — agents always know
what they are accessing and under what terms before they access it.

   The capability declaration — served at /.well-known/agents.json —
extends the agents.txt access policy file proposed in Section 4.6 with richer
content metadata:
{
    "atml-endpoint": "/atml",
    "content-types": ["news", "analysis",
                      "data"],
    "languages": ["en", "fr"],
    "supervision-level": 2,
    "auth": "delegation-token",

                                            45
    "pricing": "/.well-known/agents.txt",
    "search-topics": ["finance",
                      "technology"],
    "update-frequency": "real-time"
}

    Agent search engines index these capability declarations rather than raw
content — they know which sites publish which content types at which su-
pervision levels and under what economic terms, without having to scrape
and parse the full content of every page. This is a fundamentally more effi-
cient discovery architecture than human-web search, which must index full
page content to infer topical relevance.
    The agent search index optimizes for different signals than human search:
semantic relevance to agent task, provenance quality of the source, supervi-
sion level of available content, and access terms compatibility with the agent’s
authorization level. These signals produce rankings appropriate for agent in-
formation retrieval tasks — prioritizing trustworthy, well-provenance-tagged
sources over high-traffic, SEO-optimized pages.

6.6. Dual Publishing Strategy
    The transition from a human-centric to an agent-first content layer cannot
be abrupt. Publishers cannot abandon HTML overnight; human users con-
tinue to browse the web directly; legacy systems depend on existing content
formats. The dual-layer web architecture proposed in Section 4.5 requires a
corresponding dual publishing strategy at the content layer.
    We propose that publishers adopt ATML as a parallel delivery format
alongside HTML, generated from the same content source. In most publish-
ing systems, content is stored in a structured internal format — a content
management system database — and rendered into HTML at delivery time.
ATML is an alternative rendering target for the same source content, not
a separate authoring workflow. A publisher who stores articles as struc-
tured database records can generate both an HTML rendering (for browsers)
and an ATML rendering (for agents) from the same record, adding only the
provenance and access layers that ATML requires and HTML does not.
    The migration path mirrors the access layer migration described in Sec-
tion 4.5: Phase 1 establishes ATML as an optional parallel format; Phase 2
normalizes dual publishing as standard practice; Phase 3 establishes ATML
as the primary format for agent consumption with HTML maintained for

                                      46
browser compatibility. The human web does not disappear — it becomes
a rendering target for a content layer that is fundamentally structured for
agent consumption.

6.7. Summary
    Table 5 summarizes the content layer redesign proposals and their rela-
tionship to the failures diagnosed in Section 3.3.

      Table 5: Content layer redesign: diagnosed failures and proposed solutions.

                        Diagnosed failure         Proposed solution

                       HTML format ATML — semantic con-
                       overhead    — tent format without lay-
                       67.6%    token out noise
                       waste
                       No provenance        ATML provenance layer
                       standard             + C2PA cryptographic
                                            chain
                       No human su-         Four-level human super-
                       pervision signal     vision tier model
                       Epistemic recur- Provenance chain circuit
                       sion — AI feed- breaker + supervision
                       ing AI           declaration
                       No agent dis- agents.json  capability
                       coverability  declaration + agent
                       standard      search index
                       Human-only       Dual publishing strategy
                       publishing work- — HTML and ATML
                       flow             from same source


    The content layer redesign closes the loop opened by the access and eco-
nomic layer redesigns. An agent that can identify itself (Section 4), operate
under an appropriate economic model (Section 5), and retrieve semantically
rich, provenance-tagged content in an efficient format (this section) has ev-
erything it needs to operate as a first-class web citizen. The three layers are
deeply interdependent — ATML content is only useful if agents can reach it
(access layer) and publishers have an incentive to produce it (economic layer)
— which is why all three must be redesigned simultaneously rather than in
isolation.


                                             47
7. The Agent-First Web: A Unified Framework
   The preceding three sections proposed solutions to each layer of the
human-centric web’s failure under agent interaction: an access layer redesign
(Section 4), an economic layer redesign (Section 5), and a content layer re-
design (Section 6). This section synthesizes these proposals into a unified
framework — establishing the design principles, social contract restatement,
and migration roadmap that constitute the paper’s headline contribution.

7.1. The Social Contract Restatement
    The web’s original social contract — articulated implicitly through the
architectural choices of its first decade — rested on three foundational com-
mitments [18, 60]. First, open access: any client should be able to retrieve
any resource without prior negotiation or identity disclosure. Second, the
attention economy: publishers provide content freely in exchange for human
attention monetized through advertising. Third, human authorship: the web
is a record of human knowledge, experience, and expression, authored by hu-
mans for human readers.
    Each of these commitments is now under structural pressure. Open access
is being dismantled by blanket agent blocking. The attention economy is col-
lapsing under zero-click AI synthesis. Human authorship is being displaced
by AI-generated content at scale. The web’s social contract is not merely
being stressed — it is being violated simultaneously at all three layers by
forces its architects did not anticipate.
    We propose a restatement of the web’s social contract for the agent-first
era, preserving its founding values while extending them to accommodate
the new realities of agent-mediated interaction. Figure 13 illustrates the
comparison between the original and proposed contracts.




                                     48
Figure 13: The web’s social contract: original versus agent-first. The original contract
(1991) rested on open access for human clients, an attention economy, HTML for human
perception, and anonymous identity. The agent-first contract preserves open access but
extends it to agents through behavioral contracts; replaces the attention economy with a
value-exchange economy based on tokens and outcomes; replaces HTML with provenance-
anchored ATML; and replaces CAPTCHA-based human filtering with intent-based be-
havioral declaration. The web has renegotiated its social contract before — HTTP to
HTTPS, desktop to mobile — this is the next renegotiation.


   The new social contract can be stated concisely:

      The agent-first web is open to any client — human or agent —
      that declares its behavioral context and respects the terms declared
      by content providers. Value flows at the point of consumption, not
      the point of attention. Content carries its own provenance and
      human oversight level, enabling quality-aware consumption. The
      human web continues to exist; the agent web is built alongside it,
      not in replacement of it.

   This restatement preserves the web’s founding commitment to openness
— no client is excluded by identity — while introducing the behavioral ac-
countability and economic transparency that agent-scale interaction requires.

7.2. The Ten Principles of an Agent-First Internet
    We synthesize the proposals of Sections 4–6 into ten design principles for
the agent-first internet. These principles are intended to serve the same func-

                                          49
tion that REST principles served for API design [32] or mobile-first princi-
ples served for responsive web design [42]: a concise, quotable framework that
practitioners can apply when making architectural decisions about agent-web
interaction.
  1. Presumption of agent access. Agents acting on behalf of humans
     are presumed welcome on any web resource that is open to anonymous
     human visitors. Blocking is reserved for malicious behavior, not agent
     identity. The default posture is access, not exclusion.
  2. Behavioral contract over identity mandate. Agents declare their
     behavioral context — who they represent, at what scale, for what pur-
     pose — rather than proving their identity. Anonymous is acceptable;
     unaccountable is not. Intent declaration enables graduated responses
     without requiring privacy-invasive identification.
  3. Rate limiting as the universal access control. The binary block-
     /allow decision is replaced by graduated rate limiting determined by
     declared intent and authentication level. No legitimate agent use case
     is categorically blocked; all are accommodated at appropriate scale and
     under appropriate terms.
  4. Economic equivalence to the represented human. An agent’s
     economic obligation mirrors that of the human it represents. Free con-
     tent for anonymous humans is free for their agents. Paid subscriptions
     extend to agents through delegation tokens. New economic models
     are required only for genuinely novel agent behaviors with no human
     analog.
  5. Token as the unit of value exchange. The pageview and the adver-
     tising impression are replaced by the token as the fundamental unit of
     value exchange between agents and content providers. Token consump-
     tion is proportional to actual value derived, compatible with existing
     AI billing infrastructure, and format-agnostic.
  6. Publisher economic sovereignty. No universal economic model is
     mandated. Publishers choose between open and paid content — mir-
     roring the open source / proprietary software distinction — and declare
     their terms in machine-readable form. Economic diversity is preserved
     as a web property.
  7. Provenance as a first-class web property. Every piece of web con-
     tent carries a machine-readable provenance declaration: who authored
     it, what it was derived from, and what degree of human oversight was

                                     50
     applied. Provenance is not optional metadata — it is a structural prop-
     erty of agent-first content, as fundamental as the content body itself.
  8. Human supervision declared, not assumed. The degree of human
     involvement in content production is declared explicitly through the
     supervision tier model rather than inferred or assumed. Agents weight
     content in their reasoning according to declared supervision level. AI-
     generated content is not prohibited; it is labelled.
  9. Dual-layer coexistence. The human web and the agent web coexist
     on the same infrastructure. HTML for human browsers and ATML for
     agent clients are served from the same domain, generated from the same
     content source, differentiated only at the delivery layer. Migration is
     gradual and additive, not disruptive.
 10. Simultaneous three-layer redesign. Access, economics, and con-
     tent are redesigned together. Fixing any single layer in isolation pro-
     duces solutions that are undermined by the failures of the other two.
     The three layers are deeply coupled — they must be addressed as a
     system, not as independent problems.

   These ten principles constitute the agent-first internet framework. Fig-
ure 14 illustrates how the principles map to the three layers and their inter-
dependencies.




                                     51
Figure 14: The unified agent-first web framework. The agent-as-human-proxy principle
provides the philosophical foundation. Three redesign layers — access, economic, and
content — each contribute specific mechanisms. Together they produce an agent-first
internet in which agents are first-class citizens with open access, value-exchange economics,
and provenance-anchored content. The migration path is phased and additive, preserving
the human web throughout the transition.


7.3. Migration Roadmap
    The agent-first web is not built overnight. The proposals in this paper
span a range of implementation complexity — from the immediately deploy-
able (agent metadata headers, agents.txt) to the medium-term (ATML
adoption, OAuth delegation tokens) to the longer-term (full provenance chain
infrastructure, agent search indices). We propose a three-phase migration
roadmap that sequences these proposals by implementation complexity and
stakeholder readiness.
    Phase 1 — Identification and Declaration (near-term). The im-
mediate priority is establishing the identification and declaration infrastruc-

                                             52
ture that enables all subsequent proposals. This includes: deployment of
agent metadata HTTP headers by major AI agent providers; adoption of
agents.txt by publishers as a machine-readable access policy standard; and
expansion of llms.txt [36] from a content permission declaration into a
richer capability declaration incorporating access terms and supervision lev-
els. These measures require no new standards bodies and no new infras-
tructure — they are extensions of existing HTTP and web conventions that
individual actors can adopt unilaterally.
    Phase 2 — Economic and Format Infrastructure (medium-
term). Once identification and declaration are in place, the economic and
content format infrastructure can be built. This includes: ATML as a par-
allel content delivery format alongside HTML; OAuth delegation tokens for
subscription inheritance; token-based billing APIs for content publishers; and
pilot implementations of the commissioned content economy model. These
measures require coordination between AI providers, content publishers, and
payment infrastructure operators — achievable through industry working
groups without formal standards bodies.
    Phase 3 — Full Agent-First Infrastructure (longer-term). The
final phase establishes ATML as the primary agent-facing content format; de-
ploys full cryptographic provenance chain infrastructure built on C2PA [25];
launches agent-optimized search indices; and establishes the agent advertis-
ing protocol. These measures require formal standardization through bodies
such as the W3C and IETF, analogous to the standardization processes that
established HTTPS [30] and OAuth [34].
    Table 6 summarizes the migration roadmap.




                                     53
                   Table 6: Agent-first web migration roadmap.

                     Phase      Focus        Key proposals
                                                             Coordination
                                                               required

                     1       Identification Agent            Unilateral
                             and decla- metadata             — indi-
                             ration         headers,         vidual
                                            agents.txt,      actors
                                            llms.txt
                                            expansion
                     2       Economic        ATML,       Industry
                             and format      OAuth       working
                             infrastruc-     delega-     groups
                             ture            tion, token
                                             billing
                     3       Full agent-     Provenance Formal
                             first infras-   chain, agent standards
                             tructure        search, ad bodies
                                             protocol


7.4. Backward Compatibility
     A recurring concern with proposals to redesign web infrastructure is dis-
ruption to the existing ecosystem. We emphasize that every proposal in this
framework is additive rather than disruptive. No existing web standard is
deprecated. No existing content format is invalidated. No existing economic
model is prohibited.
     Agent metadata headers are additional HTTP headers — servers that do
not recognize them ignore them. agents.txt is an additional well-known
file — sites that do not provide it simply have no declared agent policy, and
agents fall back to default behaviors. ATML is an additional content type
— browsers that do not request it receive HTML as before. Token billing is
an additional payment option — publishers who do not adopt it continue to
operate under existing models.
     The human web does not disappear in the agent-first future — it be-
comes one layer of a richer, dual-layer web that serves both human and
agent clients from the same infrastructure. This is not a replacement; it is
an extension. The web has extended itself before — adding HTTPS along-
side HTTP, adding mobile layouts alongside desktop, adding APIs alongside
HTML pages — and has been strengthened by each extension. The agent-
first layer is the next extension in this lineage.


                                             54
7.5. Relationship to Existing Protocol Work
    The agent-first internet framework proposed in this paper is complemen-
tary to, not competitive with, the protocol-level work surveyed in Section 2.
MCP [5], A2A [33], NLWeb [44], and related protocols address agent-to-tool
and agent-to-agent communication — the plumbing of the agentic web. The
agent-first internet framework addresses the social contract, economic model,
and content architecture of the web that these agents operate within — the
foundations those protocols build on.
    The relationship is analogous to the relationship between TCP/IP and
the web’s application layer: TCP/IP provides the communication substrate;
HTTP, HTML, and the web’s economic conventions constitute the applica-
tion layer built on top. MCP and A2A are the emerging TCP/IP of the
agentic web; the agent-first internet framework is the application layer —
the conventions, economic models, and content standards that determine
what agents actually do with the communication capabilities those protocols
provide.

7.6. Summary
    The agent-first internet framework synthesizes fifteen specific proposals
across three layers into a coherent redesign grounded in a single philosoph-
ical anchor — the agent-as-human-proxy principle — and expressed as ten
design principles that practitioners can apply when making architectural de-
cisions about agent-web interaction. The framework is additive, backward-
compatible, and phased — preserving the human web throughout the transi-
tion to an agent-first architecture. It positions the challenge not as a technical
problem of protocol design but as a sociotechnical problem requiring renego-
tiation of the web’s foundational social contract — a renegotiation that the
web has successfully accomplished before and must accomplish again.

8. Open Challenges
    The agent-first internet framework proposed in this paper is principled
and internally coherent, but it does not resolve all problems. Honest account-
ing of what the framework does not solve is as important as what it proposes
— it defines the research agenda that follows from this work and prevents
overreach in the claims made. This section identifies six open challenges that
remain unresolved, each constituting a direction for future work. Figure 15
provides an overview.

                                       55
Figure 15: Open challenges in the agent-first web. Six challenge areas remain unresolved
by the proposed framework: governance and standardization, adversarial agents, the agent
advertising model, regulatory alignment, small publisher equity, and multi-agent coordina-
tion. These challenges do not invalidate the framework — they define the research agenda
that follows from it.


8.1. Governance and Standardization
    The proposals in this paper — agent metadata headers, agents.txt,
ATML, the supervision tier model, the provenance chain architecture —
require standardization to achieve the universal adoption that makes them
effective. A metadata header that only some agent providers implement
provides partial identification at best. A content format that only some
publishers adopt creates a two-tier web rather than a unified agent-first layer.
Standards achieve their value through universality, and universality requires
a governance process [9].
    The web’s history of standardization is instructive but not entirely encour-
aging. HTML was standardized through the W3C, a process that produced
robust but slow-moving standards vulnerable to browser-vendor fragmenta-


                                           56
tion during the browser wars of the late 1990s [47]. HTTP was standardized
through the IETF, a more technically rigorous but equally slow process.
OAuth emerged from industry collaboration before IETF formalization [34].
Each pathway involved years of negotiation between parties with conflicting
commercial interests.
    The agent-first web faces a governance challenge of comparable complex-
ity, with the additional complication that the primary stakeholders — AI
companies, content publishers, infrastructure providers, and regulators —
have interests that are not merely competitive but structurally opposed. AI
companies benefit from open agent access; publishers benefit from controlled,
economically compensated access; infrastructure providers benefit from be-
ing the chokepoint of any access control mechanism; regulators benefit from
accountability that none of the other parties are inclined to provide volun-
tarily.
    We do not propose a governance solution here — the political economy of
web standards governance is a research domain in its own right. We note that
the Phase 1 proposals in our migration roadmap (Section 7.3) are deliberately
designed to be adoptable unilaterally by individual actors without standards
body coordination, precisely to create momentum and demonstrated value
before formal standardization is required.

8.2. The Adversarial Agent Problem
    The agent identification metadata mechanism proposed in Section 4.2
assumes that agent metadata declarations are honest. The Perplexity case
demonstrated that this assumption does not hold under adversarial condi-
tions: bad actors will modify agent identifiers, rotate IP addresses, and falsify
intent declarations to circumvent access controls [2]. Cryptographic signing
of agent metadata raises the cost of impersonation significantly but does not
eliminate it — a bad actor who controls their own signing key can still de-
clare false intent, and a compromised legitimate signing key can be used for
impersonation until revocation.
    The adversarial agent problem is structurally similar to the email spam
problem. Email authentication standards — SPF, DKIM, DMARC — sig-
nificantly reduced certain classes of email abuse by making sender identity
verifiable, but did not eliminate spam or phishing; they shifted the attack
surface rather than eliminating it [3]. Agent metadata authentication is likely
to follow a similar trajectory: reducing casual circumvention while displacing
sophisticated attackers toward more costly evasion strategies.

                                       57
    A more robust long-term defense is behavioral rather than declarative:
monitoring agent consumption patterns over time to detect statistical anoma-
lies — consumption rates inconsistent with declared personal use, content
extraction patterns consistent with training rather than query-answering,
access patterns consistent with competitive intelligence rather than user as-
sistance. Behavioral detection is harder to evade than declaration forgery,
but requires infrastructure that does not currently exist at web scale and
raises privacy concerns about agent activity monitoring that must be care-
fully managed.

8.3. The Agent Advertising Model
    The agent advertising model sketched in Section 5.7 faces a fundamen-
tal principal-agent conflict that the framework does not resolve. Publish-
ers want their advertisements surfaced to human users by agent frontends.
Agent frontends — Claude, ChatGPT, Gemini — have competing monetiza-
tion interests and limited incentive to surface publisher advertisements that
generate no revenue for the frontend operator. Users want clean, uninter-
rupted agent responses and are likely to prefer frontends that do not surface
advertisements.
    This three-way conflict cannot be resolved by technical standards alone.
Two resolution pathways exist, both of which involve stakeholder coordina-
tion beyond what any single actor can achieve. The first is a revenue-sharing
model in which publisher advertisement revenue is split between the publisher
and the agent frontend operator that surfaces it — giving frontend opera-
tors a financial incentive to carry publisher advertisements. The second is
a regulatory mandate analogous to must-carry rules in broadcast television
regulation, requiring agent frontends to surface publisher advertisements as
a condition of accessing publisher content.
    Neither pathway is politically straightforward. Revenue sharing requires
bilateral agreements between every publisher and every agent frontend oper-
ator — a combinatorially complex negotiation landscape. Regulatory man-
dates require jurisdictional agreement across regulators who currently lack
frameworks for agent content intermediation. We identify this as a priority
open challenge and flag it as a direction for future work in both the technical
and policy research communities.




                                      58
8.4. Regulatory Alignment
    The existing regulatory landscape for web content and data was designed
for human-web interaction and applies imperfectly or ambiguously to agent-
mediated interaction across multiple dimensions.
    Copyright. When an AI agent retrieves and synthesizes content from
multiple sources, the copyright status of the synthesized output is legally un-
settled in most jurisdictions. The training data copyright disputes currently
before courts in the United States and European Union [35] address a related
but distinct question — whether training on copyrighted data constitutes in-
fringement — and their resolution will not definitively answer the question
of whether agent synthesis of copyrighted content for a user constitutes fair
use or requires licensing. The token-based licensing model proposed in Sec-
tion 5.5 is designed to be compatible with whatever copyright resolution
emerges, but cannot itself produce that resolution.
    Data protection. GDPR and equivalent regulations govern the pro-
cessing of personal data by automated systems, with requirements around
consent, purpose limitation, and data subject rights [28]. When an AI agent
processes content containing personal data on behalf of a user, it is unclear
which entity — the user, the agent provider, the content publisher — bears
data controller responsibility. The delegation token mechanism proposed
in Section 4.4 partially addresses this by establishing a clear authorization
chain, but does not resolve the underlying regulatory ambiguity.
    Platform liability. Section 230 of the US Communications Decency
Act and equivalent provisions in other jurisdictions limit platform liability
for user-generated content. It is unclear whether AI agents that synthesize
and present content to users are acting as platforms (potentially eligible for
liability protection) or as publishers (potentially liable for the content they
synthesize). This ambiguity has significant implications for the design of
agent content systems and requires legislative rather than technical resolu-
tion.

8.5. The Small Publisher Equity Problem
    The proposals in this paper — ATML publishing infrastructure, prove-
nance chain certification, token billing APIs, agents.json capability decla-
rations — carry implementation costs that large publishers can absorb and
small publishers cannot. The New York Times has engineering teams ca-
pable of implementing dual-layer publishing infrastructure. An independent
journalist with a WordPress blog does not.

                                      59
    If the agent-first web is accessible only to publishers with the resources
to implement its infrastructure, it creates a two-tier web in which large pub-
lishers dominate agent-accessible content and small, independent, and com-
munity publishers are effectively excluded. This replicates and potentially
amplifies existing web inequality — large platforms already dominate search
rankings and social distribution; agent-first infrastructure could extend this
dominance to agent-mediated information access.
    The mitigation is platform-level adoption: if WordPress, Substack, Ghost,
and similar publishing platforms implement ATML generation, agents.json
capability declarations, and provenance tagging as platform features, their
users gain agent-first capabilities without individual implementation effort.
This mirrors how SSL adoption was democratized through hosting platform
support rather than individual webmaster implementation. We recommend
that the standards proposed in this paper be designed with platform-level im-
plementation as the primary deployment pathway — simplicity for platform
integration is more important than feature richness for individual deploy-
ment.

8.6. Multi-Agent Coordination
    The framework proposed in this paper addresses the interaction between
a single agent and web content. Increasingly, however, agent tasks involve
multiple agents collaborating — an orchestrator agent directing specialist
agents to retrieve, analyze, and synthesize content from many sources simul-
taneously [27]. This multi-agent scenario introduces attribution and billing
complexities that the framework does not resolve.
    When five specialist agents each retrieve content from ten sources to com-
plete a single user task, who pays for the content access? The user, through
their orchestrating agent? Each specialist agent independently? The orches-
trator on behalf of all specialists? The token-based billing model proposed
in Section 5.5 provides a unit of account but not a billing architecture for
multi-agent scenarios.
    Attribution is equally complex. When a multi-agent pipeline produces
a synthesized output that incorporates content from fifty sources retrieved
by multiple agents, the provenance chain described in Section 6.4 must span
agent boundaries — tracking not just which sources were consulted but which
agents consulted them and how their outputs were combined. This requires
a cross-agent provenance standard that does not currently exist and whose
design involves significant technical and privacy tradeoffs.

                                     60
   The A2A protocol [33] and related multi-agent communication standards
provide communication infrastructure for multi-agent systems but do not
address content attribution or billing coordination. We identify multi-agent
content economics as a priority area for future work, noting that its resolution
requires coordination between the agent communication protocol community
and the web content economics community — two communities that have not
yet engaged substantively with each other’s work.

8.7. Summary
    Table 7 summarizes the six open challenges and their relationship to the
framework proposals.

   Table 7: Open challenges and their relationship to the agent-first web framework.

                                      Framework       Resolution
                         Challenge
                                       limitation      pathway

                       Governance Proposals         W3C, IETF,
                       and    stan- require         industry
                       dardization universal        working
                                    adoption        groups
                       Adversarial   Declarations Behavioral
                       agents        can be falsi- detection
                                     fied          +       cryp-
                                                   tographic
                                                   signing
                       Agent ad- Frontend in- Revenue
                       vertising centive con- sharing    or
                                 flict        regulatory
                                              mandate
                       Regulatory    Legal          Legislative
                       alignment     frameworks     and judicial
                                     predate        resolution
                                     agents
                       Small pub- Implementation  Platform-
                       lisher equity costs create level adop-
                                     barriers     tion pathway
                       Multi-agent   Single-agent   Cross-agent
                       coordina-     billing and    provenance
                       tion          attribution    standard
                                     model



                                          61
    These six challenges are significant but do not invalidate the framework.
Each represents a known limitation with an identifiable resolution pathway
— they are open problems, not fatal flaws. The web has faced compara-
ble challenges at every major architectural transition: HTTPS deployment
faced governance fragmentation and small-site adoption barriers before Let’s
Encrypt democratized certificate issuance; OAuth faced competing imple-
mentations before RFC 6749 standardized the protocol; mobile web faced
regulatory uncertainty before jurisdictions developed mobile-specific frame-
works. The agent-first web transition will follow a similar pattern — early
adoption by large actors, gradual standardization, eventual universal deploy-
ment — provided the foundational framework is principled enough to survive
the transition intact. We believe the framework proposed in this paper meets
that standard.

9. Conclusion
    The World Wide Web was built for human eyes. For three decades, this
assumption was so fundamental that it required no articulation — it was
simply the water in which the web swam. The emergence of AI agents as
primary intermediaries between humans and web content has made this as-
sumption visible by breaking it. Blanket agent blocking, collapsing publisher
revenues, and the epistemic recursion loop are not isolated problems — they
are symptoms of a single underlying condition: a web whose architecture was
designed for a world that no longer exists.
    This paper has argued that the response to this condition cannot be re-
active or piecemeal. Patching the access layer without the economic layer
produces agents that can reach content but publishers who cannot sustain
producing it. Patching the economic layer without the content layer produces
billing infrastructure for content that degrades in quality through epistemic
recursion. The three layers — access, economics, and content — are deeply
coupled, and must be redesigned simultaneously, grounded in a single philo-
sophical anchor: that AI agents acting on behalf of humans are first-class
web citizens entitled to the same presumption of access, subject to equiva-
lent obligations, and deserving of an architectural environment designed for
their interaction model.
    The agent-first internet framework proposed in this paper offers that re-
design. At the access layer, agent identification metadata headers and a grad-
uated rate-limiting model replace blanket blocking with context-appropriate

                                     62
access control. At the economic layer, the intent-based tier model and token-
based subscription mechanism replace the broken attention economy with
a value-exchange model grounded in the agent-as-human-proxy principle.
At the content layer, ATML, the human supervision tier model, and the
provenance chain architecture replace opaque HTML with semantically rich,
provenance-anchored content that breaks the epistemic recursion loop. To-
gether these proposals constitute ten design principles for the agent-first in-
ternet — a framework intended to serve practitioners making architectural
decisions about agent-web interaction in the same way that REST princi-
ples served API designers and mobile-first principles served responsive web
designers.
    The web has renegotiated its social contract before. The transition from
HTTP to HTTPS reframed security from an optional feature to a default
expectation. The transition from desktop to mobile reframed layout from a
fixed assumption to a responsive variable. Each transition required years
of friction, partial adoption, and eventual standardization before becom-
ing universal. The transition to an agent-first web is the next renegotia-
tion in this lineage — and by the evidence of collapsing publisher revenues,
infrastructure-scale agent blocking, and accelerating epistemic recursion, it
is already overdue.
    The cost of inaction is not merely economic. A web that successfully
excludes AI agents excludes the humans those agents represent — making
the web less useful to the people it was built to serve. A web whose content
is generated by AI for consumption by AI, without human intentionality at
any point in the chain, is no longer a record of human knowledge — it is a
hall of mirrors, reflecting increasingly distorted versions of what humans once
knew. Redesigning the web for AI agents is not a concession to technological
change. It is an act of stewardship for the knowledge ecosystem that both
humans and AI depend upon.

References
 [1] von Ahn, L., Blum, M., Hopper, N.J., Langford, J., 2003. CAPTCHA:
     Using hard AI problems for security, in: Advances in Cryptology – EU-
     ROCRYPT 2003, pp. 294–311.

 [2] AI, P., 2024. Publisher revenue sharing program.          https://www.
     perplexity.ai.


                                      63
 [3] Allman, E., Callas, J., Delany, M., Libbey, M., Fenton, J., Thomas,
     M., 2007. DomainKeys identified mail (DKIM) signatures – RFC 4871.
     https://tools.ietf.org/html/rfc4871.

 [4] ANP Working Group, 2025. Agent network protocol (ANP). https:
     //agent-network-protocol.com.

 [5] Anthropic, 2024.   Model context protocol (MCP).             https://
     modelcontextprotocol.io.

 [6] Arora, S., Yang, B., Eyuboglu, S., Narayan, A., Hojel, A., Trummer,
     I., Ré, C., 2023. Language models enable simple systems for gen-
     erating structured views of heterogeneous data lakes. arXiv preprint
     arXiv:2304.09433 .

 [7] Bandara, E., Bouk, S.H., Mukkamala, R., Rahman, A., Liang, X., Gore,
     R., Shetty, S., 2025a. Slice-mcp — fine-tuned llama-4 llm and mcp
     enabled 5g network slice orchestration platform, in: MILCOM 2025 -
     2025 IEEE Military Communications Conference (MILCOM), pp. 1506–
     1511. doi:10.1109/MILCOM64451.2025.11310417.

 [8] Bandara, E., Gore, R., Foytik, P., Shetty, S., Mukkamala, R., Rah-
     man, A., Liang, X., Bouk, S.H., Hass, A., Rajapakse, S., et al., 2025b.
     A practical guide for designing, developing, and deploying production-
     grade agentic ai workflows. arXiv preprint arXiv:2512.08769 .

 [9] Bandara, E., Gore, R., Gunaratna, A., Rajapakse, S., Kularathna,
     I., Mukkamala, R., Shetty, S., Liang, X., Hass, A., Hewa, T., et al.,
     2026a. Think before you act–a neurocognitive governance model for
     autonomous ai agents. arXiv preprint arXiv:2604.25684 .

[10] Bandara, E., Gore, R., Liang, X., Rajapakse, S., Kularathne, I.,
     Karunarathna, P., Foytik, P., Shetty, S., Mukkamala, R., Rahman,
     A., et al., 2025c. Agentsway–software development methodology for
     ai agents-based teams. arXiv preprint arXiv:2510.23664 .

[11] Bandara, E., Gore, R., Shetty, S., Mukkamala, R., Rhea, C., Yarla-
     gadda, A., Kaushik, S., De Silva, L., Maznychenko, A., Sokolowska,




                                    64
    I., et al., 2025d. Standardization of neuromuscular reflex analysis–
    role of fine-tuned vision-language model consortium and openai gpt-
    oss reasoning llm enabled decision support system. arXiv preprint
    arXiv:2508.12473 .
[12] Bandara, E., Gore, R., Shetty, S., Rajapakse, S., Kularathna, I.,
     Karunarathna, P., Mukkamala, R., Foytik, P., Bouk, S.H., Rahman, A.,
     et al., 2026b. A practical guide to agentic ai transition in organizations.
     arXiv preprint arXiv:2602.10122 .
[13] Bandara, E., Gunaratna, A., Gore, R., Rahman, A., Mukkamala, R.,
     Shetty, S., Rajapakse, S., Kularathna, I., Foytik, P., Bouk, S.H., et al.,
     2026c. Ai trust os–a continuous governance framework for autonomous
     ai observability and zero-trust compliance in enterprise environments.
     arXiv preprint arXiv:2604.04749 .
[14] Bandara, E., Hass, A., Gore, R., Shetty, S., Mukkamala, R., Bouk, S.H.,
     Liang, X., Keong, N.W., De Zoysa, K., Withanage, A., et al., 2025e.
     Astride: A security threat modeling platform for agentic-ai applications.
     arXiv preprint arXiv:2512.04785 .
[15] Bandara, E., Hewa, T., Gore, R., Shetty, S., Mukkamala, R., Foytik,
     P., Rahman, A., Bouk, S.H., Liang, X., Hass, A., et al., 2025f. Towards
     responsible and explainable ai agents with consensus-driven reasoning.
     arXiv preprint arXiv:2512.21699 .
[16] Bandara, E., Shetty, S., Mukkamala, R., Gore, R., Foytik, P., Bouk,
     S.H., Rahman, A., Liang, X., Keong, N.W., De Zoysa, K., et al., 2025g.
     Model context contracts-mcp-enabled framework to integrate llms with
     blockchain smart contracts. arXiv preprint arXiv:2510.19856 .
[17] Bender, E.M., Gebru, T., McMillan-Major, A., Shmitchell, S., 2021. On
     the dangers of stochastic parrots: Can language models be too big?, in:
     Proceedings of the ACM Conference on Fairness, Accountability, and
     Transparency (FAccT), pp. 610–623.
[18] Berners-Lee, T., 1989. Information Management: A Proposal. Technical
     Report. CERN.
[19] Berners-Lee, T., Hendler, J., Lassila, O., 2001. The semantic web. Sci-
     entific American 284, 34–43.

                                      65
[20] Brin, S., Page, L., 1998. The anatomy of a large-scale hypertextual web
     search engine, in: Proceedings of the 7th International Conference on
     World Wide Web (WWW), pp. 107–117.

[21] Cloudflare, 2025a. Cloudflare blocks AI crawlers by default. https:
     //blog.cloudflare.com.

[22] Cloudflare, 2025b. The crawl-to-click gap: Cloudflare data on AI bots,
     training, and referrals. https://blog.cloudflare.com.

[23] Cloudflare, 2025c. From Googlebot to GPTBot: Who’s crawling your
     site in 2025. https://blog.cloudflare.com.

[24] Cloudflare, 2026. Google’s AI crawler policy and competitive implica-
     tions. https://blog.cloudflare.com.

[25] Coalition for Content Provenance and Authenticity, 2024. C2PA tech-
     nical specification. https://c2pa.org/specifications.

[26] Deng, X., Gu, Y., Zheng, B., Chen, S., Stevens, S., Wang, B., Sun, H.,
     Su, Y., 2023. Mind2web: Towards a generalist agent for the web, in:
     Advances in Neural Information Processing Systems (NeurIPS).

[27] Durante, Z., Sarkar, B., Gong, R., Taori, R., Noda, Y., Tang, P., Adeli,
     E., Lakshmikanth, S.K., Schulman, K., Milstein, A., et al., 2024. Agent
     AI: Surveying the horizons of multimodal interaction, in: arXiv preprint
     arXiv:2401.03568.

[28] European Parliament, 2016. General data protection regulation (GDPR)
     – regulation (eu) 2016/679. https://gdpr-info.eu.

[29] Evans, D.S., 2008. The economics of the online advertising industry.
     Review of Network Economics 7, 359–391.

[30] Felt, A.P., Barnes, R., King, A., Palmer, C., Bentzel, C., Tabriz, P.,
     2017. Measuring HTTPS adoption on the web, in: 26th USENIX Secu-
     rity Symposium, pp. 1323–1338.

[31] Fielding, R., Gettys, J., Mogul, J., Nielsen, H., Masinter, L., Leach, P.,
     Berners-Lee, T., 1999. HTTP/1.1 – RFC 2616. Technical Report. IETF.



                                      66
[32] Fielding, R.T., 2000. Architectural Styles and the Design of Network-
     based Software Architectures. Ph.D. thesis. University of California,
     Irvine.

[33] Google, 2025. Agent-to-agent protocol (A2A). https://developers.
     google.com/agent-to-agent.

[34] Hardt, D., 2012. The OAuth 2.0 Authorization Framework – RFC 6749.
     Technical Report. IETF.

[35] Henderson, P., Li, X., Jurafsky, D., Hashimoto, T., Lemley, M.A.,
     Liang, P., 2023. Foundation models and fair use, in: arXiv preprint
     arXiv:2303.15715.

[36] Howard, J., 2024. A proposed standard for LLMs: llms.txt. https:
     //llmstxt.org.

[37] Kapoor, S., et al., 2025. Infrastructure for AI Agents. Technical Report
     2501.10114. arXiv.

[38] Karpathy, A., 2025. Html is the language of the agentic web. https:
     //twitter.com/karpathy.

[39] Kirchenbauer, J., Geiping, J., Wen, Y., Katz, J., Miers, I., Goldstein,
     T., 2023. A watermark for large language models, in: International
     Conference on Machine Learning (ICML).

[40] Koster, M., 1994. A standard for robot exclusion.        https://www.
     robotstxt.org/orig.html.

[41] Li, Y., et al., 2025. Agentic Web: Weaving the Next Web with AI
     Agents. Technical Report 2507.21206. arXiv.

[42] Marcotte, E., 2011. Responsive Web Design. A Book Apart.

[43] Martini, M., et al., 2024. Provenance requirements for agentic content
     pipelines. arXiv preprint.

[44] Microsoft, 2025. NLWeb: Natural language interface for the web. https:
     //github.com/microsoft/NLWeb.



                                     67
[45] Nguyen, T., et al., 2025. Economic models for AI agent content access.
     arXiv preprint.

[46] Pew Research Center, 2025. User behavior with AI overviews in search.
     https://www.pewresearch.org.

[47] Raggett, D., Le Hors, A., Jacobs, I., 1999. HTML 4.01 specification.
     W3C Recommendation .

[48] Raymond, E.S., 1999. The Cathedral and the Bazaar: Musings on Linux
     and Open Source by an Accidental Revolutionary. O’Reilly Media.

[49] Research, I., 2025. Agent Communication Protocol (ACP). Technical
     Report. IBM.

[50] Semrush, 2025. Zero-click searches in AI mode. https://www.semrush.
     com.

[51] Shumailov, I., Shumaylov, Z., Zhao, Y., Gal, Y., Papernot, N., Ander-
     son, R., 2023. The curse of recursion: Training on generated data makes
     models forget, in: Advances in Neural Information Processing Systems
     (NeurIPS).

[52] SISTRIX, 2026. Click-through rate analysis: AI overviews impact.
     https://www.sistrix.com.

[53] W3C Agent Web Community Group, 2025. Agent web: Architecture
     and challenges. https://www.w3.org/community/agent-web.

[54] Wang, L., Ma, C., Feng, X., Zhang, Z., Yang, H., Zhang, J., Chen, Z.,
     Tang, J., Chen, X., Lin, Y., Zhao, W.X., Wei, Z., Wen, J.R., 2024. A
     survey on large language model based autonomous agents. Frontiers of
     Computer Science 18.

[55] webMCP Authors, 2025. webMCP: A Client-Side Standard for Agent-
     Ready Web Design. Technical Report 2508.09171. arXiv.

[56] Wu, T., 2016. The Attention Merchants: The Epic Scramble to Get
     Inside Our Heads. Knopf.




                                    68
[57] Yao, S., Chen, H., Yang, J., Narasimhan, K., 2022. Webshop: Towards
     scalable real-world web interaction with grounded language agents, in:
     Advances in Neural Information Processing Systems (NeurIPS).

[58] Zellers, R., Holtzman, A., Rashkin, H., Bisk, Y., Farhadi, A., Roesner,
     F., Choi, Y., 2019. Defending against neural fake news, in: Advances in
     Neural Information Processing Systems (NeurIPS).

[59] Zhou, S., Xu, F.F., Zhu, H., Zhou, X., Lo, R., Sridhar, A., Cheng, X.,
     Bisk, Y., Fried, D., Alon, U., Neubig, G., 2024. WebArena: A realis-
     tic web environment for building autonomous agents, in: International
     Conference on Learning Representations (ICLR).

[60] Zittrain, J., 2008. The Future of the Internet – And How to Stop It.
     Yale University Press.




                                    69
