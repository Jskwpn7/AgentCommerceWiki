---
title: "Agentic Inequality"
type: raw
source_url: https://arxiv.org/abs/2510.16853
ingested: 2026-08-24
sha256: pending
tags:
  - academic
  - agentic-ai
  - economic-modelling
---

                                                                                 Agentic Inequality
                                                       Matthew Sharp1,2         Omer Bilgin3          Iason Gabriel4          Lewis Hammond3,5
                                                                                         24 April 2026
                                                   1                                                 2                         3
                                                       Oxford Martin AI Governance Initiative            Access Partnership        University of Oxford
                                                                        4                       5
                                                                            Google DeepMind         Cooperative AI Foundation

                                             Abstract
                                             Autonomous AI agents capable of complex planning and action mark a shift beyond today’s genera-
                                             tive tools. As these systems enter political and economic life, who can access them, how capable they
                                             are, and how many can be deployed will shape distributions of power and opportunity. We define this
                                             emerging challenge as “agentic inequality”: disparities in power, opportunity, and outcomes arising
                                             from unequal access to, and capabilities of, AI agents. We show that agents could either deepen




arXiv:2510.16853v3 [cs.CY] 24 Apr 2026
                                             existing divides or, under the right conditions, mitigate them. The paper makes three contributions.
                                             First, it develops a framework for analysing agentic inequality across three dimensions: availability,
                                             quality, and quantity. Second, it argues that agentic inequality differs from earlier technological
                                             divides because agents function as autonomous delegates rather than tools, generating new asymme-
                                             tries through scalable goal delegation and direct agent-to-agent competition. Third, it analyses the
                                             technical and socioeconomic drivers likely to shape the distribution of agentic power, from model
                                             release strategies to market incentives, and concludes with a research agenda for governance.



                                         1. Introduction                                                  economy of AI, but focuses specifically on dispar-
                                                                                                          ities arising from the distinctive features of AI
                                         Generative AI models – typified by systems that                  agents. As these systems are not yet widely de-
                                         convert prompts into prose, code or images –                     ployed, a window of opportunity exists to proac-
                                         now underpin AI agents: systems that pursue                      tively shape their development and ensure their
                                         complex goals with significant autonomy by per-                  benefits are distributed equitably.
                                         ceiving their environment, planning, and execut-                    We build on scholarship on the co-evolution of
                                         ing multi-step tasks across digital environments                 technology and society (Mumford, 1967; Jasanoff,
                                         (Wang et al., 2024; Kasirzadeh and Gabriel,                      2004), and extend research on LLM impacts (Ace-
                                         2025). These systems vary in autonomy, efficacy,                 moglu and Restrepo, 2020; Brynjolfsson et al.,
                                         goal complexity, and generality, ranging from nar-               2025b; Noy and Zhang, 2023) and the “digital di-
                                         row task executors operating within constrained                  vide” (Selwyn, 2004; van Dijk, 2005; Warschauer,
                                         workflows to general-purpose delegates that man-                 2003). On that basis, we develop an analyti-
                                         age cross-domain goals. Although still at an early               cal framework for this emerging challenge, ex-
                                         stage, AI agents are beginning to perform eco-                   ploring both the risks of new forms of inequal-
                                         nomically valuable workflows, and ongoing re-                    ity and the potential for agents to mitigate exist-
                                         search aims to extend their capabilities. This                   ing divides. Agents could amplify the advantages
                                         shift from AI as a command-following tool to AI                  of well-resourced actors, but if capable systems
                                         as an autonomous goal-pursuing actor matters                     are widely accessible, they could also reduce ex-
                                         because it affects human agency: the capacity of                 isting disadvantages by simplifying complex pro-
                                         individuals to pursue goals that they value (Sen,                cesses and performing tasks that previously re-
                                         1999; Prunkl, 2024).                                             quired costly expertise. A critical step involves
                                            This paper introduces and explores “agentic                   shifting our evaluative lens to view AI agents
                                         inequality”: disparities in power and outcomes                   not just as individual products, but as a form
                                         that may arise from unequal access to AI agents.                 of “infrastructure” that is likely to mediate ac-
                                         We argue that agentic inequality differs from ear-               cess to essential goods, services, and opportuni-
                                         lier technological divides for two reasons. First,               ties (Plantin et al., 2018; Rothschild et al., 2025;
                                         agents create new power asymmetries by allowing                  Bergman et al., 2024; Chan et al., 2025; Lazar,
                                         users to delegate complex tasks at scale. Second,                2025). Our focus is primarily on individuals and
                                         they create new competitive dynamics through                     organisations, although the implications extend
                                         direct agent-to-agent competition. Our argument                  to all aspects of society.
                                         sits within broader debates about the political

                                                                                                     1
   The paper proceeds as follows. Section 2 iden-            quality. This refers to what an individual agent
tifies the key dimensions through which agentic              can do and the operational characteristics that
inequality may manifest. Section 3 examines its              determine its behaviour. Agent quality can vary
implications across key societal domains. Sec-               along several axes:
tion 4 analyses the technical and socio-political
drivers that may widen or reduce it. Section 5                • Core intelligence: the combination of an
considers the governance challenge and sets out a               agent’s world knowledge, multimodal capabil-
research agenda.                                                ities across language and other data types,
                                                                and its ability to reason, plan, and solve prob-
2. Dimensions of Agentic Inequality                             lems. This depends largely on the sophistica-
Agentic inequality has three dimensions: avail-                 tion of the underlying foundation model and
ability, quality, and quantity. Each captures a                 its training data (Zhu et al., 2025).
distinct and analytically separable source of dif-
                                                              • Operational speed and throughput: an
ferential advantage; together, they determine the
                                                                agent’s efficiency depends on latency and
extent to which an actor can derive value from
                                                                data-processing capacity, which in turn reflect
agentic AI.
                                                                the computational resources supporting it, in-
2.1. Availability                                               cluding hardware accelerators and cloud in-
Availability is the most basic dimension. It has                frastructure (Sastry et al., 2024).
two layers. The first is structural availability:             • Reliability: the consistency of an agent’s
whether an agent is, in principle, available to a               performance across tasks, including how ro-
given actor, given market presence, regulatory                  bust it is and how often it fails.
permissibility, and the necessary infrastructure.
The second is accessibility: whether that actor               • Tool use: an agent’s ability to access and
can make practical use of the agent, given con-                 effectively use external systems, such as APIs,
straints such as affordability, digital literacy, lan-          proprietary databases, real-time data feeds, or
guage support, and usability. Research on the                   physical actuators (Chan et al., 2025).
digital divide has long emphasised this distinc-              • Disposition: an agent’s behavioural tenden-
tion, showing that formal access does not auto-                 cies, which may affect performance in context-
matically translate into effective use (van Dijk,               specific ways. An aggressive disposition may
2005; Selwyn, 2004; Warschauer, 2003). To-                      help in negotiation, for example, but hin-
gether, these two conditions determine whether                  der performance in a customer service setting
an individual or organisation can use even a sin-               where politeness and helpfulness matter more.
gle AI agent, which is the minimum requirement
for participation in the agentic economy (Toma-                 These sub-components need not move together.
sev et al., 2025).                                           Falling inference costs may commoditise core in-
   A further distinction is important here. Ac-              telligence even as tool use remains gated by in-
cess to a foundation model is not the same as                frastructure controllers. As a result, quality gaps
access to a functional agent. Foundation models              may narrow on one axis while remaining wide on
are becoming more accessible, but, at the time of            another. From an inequality standpoint, core in-
writing, deploying a capable agent remains diffi-            telligence and tool use are likely to matter most.
cult. The infrastructure needed to do so, includ-            The former determines capacity for the complex,
ing high-quality scaffolding, is still new, complex,         high-value tasks where agentic advantage is great-
and often concentrated among a small number                  est; the latter determines whether an agent can
of providers. Effective deployment also typically            act in the world rather than merely advise. Dispo-
requires specialised expertise (Chan et al., 2025;           sition may also become more important as multi-
Liu et al., 2025). Awareness and knowledge gaps              agent interaction expands, since behavioural ten-
therefore remain barriers to entry in their own              dencies in competitive or cooperative settings can
right. Inequalities in availability may also reflect         directly shape outcomes.
choice, where individuals or organisations decide            2.3. Quantity
not to use agents for ethical or practical reasons.
                                                             The final dimension is the quantity of agents
2.2. Quality                                                 an individual or organisation can deploy. This
Availability alone does not settle what an agent             captures a source of advantage that is distinct
enables its user to do. A second dimension is                from the capability of any single agent. Scale

                                                         2
can matter because running more agents allows                not inevitable: agents designed to explain their
a task to be pursued through multiple reasoning              reasoning and build user competence over time
paths in parallel, rather than sequentially. Re-             could reduce reliance rather than deepen it.
cent research finds that performance on complex                 Taken together, these dimensions make con-
tasks can improve as more agents are deployed,               crete two features that distinguish agentic in-
with larger gains on harder tasks (Li et al.,                equality from earlier technological divides. The
2024). Other work shows that running multi-                  first is scalable delegation: deploying many
agent teams in parallel can reduce latency while             agents in parallel may look less like using a better
preserving accuracy, and in some cases improve               tool and more like directing a distributed work-
task completion rates (Zhang et al., 2025). Quan-            force. The second is direct agent-to-agent com-
tity may therefore confer an advantage not just              petition: as agents negotiate, bid, and strategise
by adding effort, but by enabling broader search             on behalf of their users, the contest that previ-
and faster convergence across complex problems.              ously took place between people may now turn
                                                             on differences in algorithmic capability operating
2.4. Interaction Effects, User Dependence,                   at machine speed (Zhu et al., 2025).
     and User-Dependent Value
These dimensions interact rather than operating              3. Implications of Agentic Inequality
independently. In some settings, quantity can                Agentic inequality is not only a theoretical con-
partly offset quality: multiple competent but in-            cern. It may also have substantial economic, so-
dividually limited agents can outperform a single            cial, and political effects. Whether agents mainly
stronger agent operating alone, especially when              concentrate power among already well-resourced
they draw on diverse models, prompts, tools, or              actors or broaden access to opportunity will de-
roles (Li et al., 2024; Żywot et al., 2026). In other       pend on how differences in availability, quality,
settings, however, adding more agents yields lit-            and quantity unfold across domains, and on the
tle, as homogeneous systems produce increasingly             policy choices made in response. The discussion
correlated outputs and returns diminish sharply              below draws on existing evidence where possible,
(Yang et al., 2026; Xu et al., 2026). Where qual-            projects from present trends where the technol-
ity, diversity, and coordination improve together,           ogy is still emerging, and in some places considers
the gains can compound: heterogeneous multi-                 longer-run possibilities. The text indicates which
agent systems can outperform both single-agent               of these modes is being used.
baselines and larger but less differentiated agent
                                                             3.1. Economic Impacts
pools (Yang et al., 2026; Żywot et al., 2026).
   The value users derive from agents is also not            3.1.1 Labour Market Effects
fixed. Even where users have access to the same              The labour market effects of AI remain uncer-
agent, the benefits they obtain may differ sub-              tain. The available evidence is still limited, and
stantially. Outcomes depend not only on access               most of it predates autonomous agents. “Agen-
but also on complementary assets such as work-               tic capital”, autonomous systems capable of man-
flow integration, managerial oversight, domain               aging entire business processes, could acceler-
knowledge, and the capacity to deploy agents                 ate a shift in national income from labour to
strategically (Weidinger et al., 2021; Bommasani             capital, extending a familiar dynamic from ear-
et al., 2022). Some users may get much more out              lier capital-augmenting technologies (Brynjolfs-
of the same agent than others. So even if access is          son and McAfee, 2014; Brynjolfsson et al., 2025b).
equal in formal terms, outcomes may still diverge.           Yet the existing evidence on generative AI’s
   A related issue is user dependence: the extent            labour market impact is mixed. Economy-wide
to which people come to rely on agents for tasks             analyses suggest relative stability (Gimbel et al.,
they previously handled themselves. This depen-              2025), while disaggregated studies of exposed
dence is unlikely to be evenly spread. People with           industries find declining hiring for junior roles
fewer alternative resources may have stronger rea-           alongside stable or growing employment for se-
sons to rely heavily on agents, which can leave              nior workers (Brynjolfsson et al., 2025a; Hos-
them more exposed to quality problems or service             seini Maasoum and Lichtinger, 2025). Some firm-
interruptions (Prunkl, 2024). For that reason, de-           level studies document a “levelling-up” effect, in
pendence is better seen as a factor that intensifies         which technology raises the productivity of less-
the inequalities described above than as a sepa-             experienced staff (Peng et al., 2023; Noy and
rate fourth dimension. That said, dependence is              Zhang, 2023; Cui et al., 2026; Brynjolfsson et al.,

                                                         3
2025b). That effect, however, is a feature of              in ways that secure better outcomes in health-
human-tool augmentation; it is far from clear              care or legal systems (Bovens and Zouridis, 2002).
that it would survive a transition to agentic capi-        That risk may grow if public services are designed
tal built to execute and manage entire workflows           around agentic interaction, leaving citizens with-
with limited human input.                                  out access to comparable tools at a disadvantage.
3.1.2 Industrial Organisation and Market                   But the reverse is also possible. “Public-good”
        Structures                                         agents could widen access by automating form-
                                                           filling and proactively pursuing entitlements on
In industry, the central question is whether agents
                                                           behalf of citizens, reducing administrative bur-
intensify concentration or widen competition.
                                                           dens that fall disproportionately on lower-income
Unequal deployment could accelerate the rise
                                                           groups. Taiwan’s experience with public digi-
of “superstar firms” through two mechanisms.
                                                           tal infrastructure offers an instructive precedent
First, dominant firms may be able to use pro-
                                                           (Weyl et al., 2024).
prietary data to build more capable agents, im-
proving services, attracting more users, and gen-          3.2.2 Political Discourse and Participa-
erating still more data in a feedback loop that                    tion
smaller rivals may find difficult to match (Korinek        In politics, the key tension is between amplify-
and Vipra, 2025). Second, larger firms may be              ing elite influence and enabling broader partic-
able to deploy greater numbers of agents to auto-          ipation (Summerfield et al., 2025). Differences
mate internal processes and accelerate innovation          in agent quantity and quality could allow well-
at a scale beyond the reach of smaller competi-            resourced actors to deploy sophisticated agent
tors. Yet the opposite dynamic is also possible.           swarms to run coordinated, multi-step influence
The declining cost and increasing availability of          campaigns, for example by overwhelming public
powerful agentic platforms could also act as an            consultations or generating personalised propa-
equalising force by lowering barriers to entry, en-        ganda at scale (Gabriel et al., 2024; Persily and
abling startups to run operations that previously          Tucker, 2020). At the same time, broad access to
required substantial human capital.                        agents that can autonomously draft policy pro-
                                                           posals, manage activist campaigns, and engage in
3.1.3 Consumer Welfare and Negotiations
                                                           political processes could strengthen the capacity
Consumer markets may be among the first do-                of citizens and grassroots groups. Recent work
mains in which agentic inequality becomes vis-             has begun to explore how AI might support par-
ible. Corporate agents could amplify manip-                ticipatory deliberation in digital public spaces at
ulative practices already documented in digital            scale (Goldberg et al., 2024). This shift from
markets, including hidden information, scarcity            human persuasion to machine-mediated influence
cues, and deceptive choice architecture, at a scale        also raises a deeper question for democratic le-
and speed no human sales operation could match             gitimacy, since the “public will” may come to be
(Mathur et al., 2019; Kolt, 2025). This asymme-            shaped more heavily by delegated political action.
try may be especially pronounced in negotiations,
where differences in algorithmic capability trans-         3.2.3 Social Stratification
late directly into worse outcomes for the weaker           Agents may also introduce more explicit com-
party (Zhu et al., 2025). At the same time, widely         petition into social life, with effects that could
available consumer agents could pull in the op-            run in either direction. They could deepen the
posite direction by automating comparison shop-            “Matthew Effect”, whereby initial advantages
ping, flagging deceptive pricing, and negotiating          compound over time, or they could widen social
on users’ behalf at a scale no individual could            mobility. Unlike tools that merely augment hu-
manage alone (Van Loo, 2019; Zhu et al., 2025).            man effort, agents could enable the scalable dele-
                                                           gation of complex social strategies, from manag-
3.2. Social and Political Impacts
                                                           ing a professional’s networking to improving ed-
3.2.1 Access to Essential Services                         ucational opportunities for one’s children. More
Agents could reshape the citizen-state relation-           broadly, they could reduce the transaction costs
ship, either producing a more stratified system            that inhibit beneficial coordination, enabling new
or widening access to public services (Ilves et al.,       forms of decentralised social bargaining (Krier,
2025). One risk is that affluent individuals may           2025). Scalable delegation of this kind could cre-
use premium agents to navigate complex bu-                 ate a more persistent divide between those able
reaucratic workflows and optimise applications             to use such autonomous delegates effectively and

                                                       4
those who are not, as repeated small advantages             4.1.2 Agent Architecture and Platform
widen gaps in social capital over time. But ac-                   Governance
cessible agents could also improve mobility by of-          The way foundation models are governed,
fering coaching and by opening up opportunities             whether proprietary or open-weight, shapes how
that might otherwise remain out of reach.                   agentic capabilities spread and who retains con-
                                                            trol over them. Proprietary models make adop-
4. Forces Shaping Agentic Inequality                        tion easier by sparing users the costs and burden
                                                            of running the underlying infrastructure them-
The effects of AI agents will not be determined             selves. That convenience can create a form of de-
by the technology alone. They will emerge from              pendence. Users may not be able to tailor model
a mix of technical constraints, market incentives,          weights to private data, may have limited control
institutional arrangements, and political choices.          over updates, and may rely on API access con-
Many of these forces apply to AI more broadly.              trolled by the provider. In practice, those lim-
They bear with particular force on agents, how-             its can affect whether downstream agents per-
ever, because systems that act autonomously on              form complex tasks consistently. Open-weight
behalf of their users convert distributional dispar-        models reduce one barrier by making model pa-
ities more directly into differences in outcomes.           rameters directly available. But they do not re-
This preliminary mapping focuses on proximate               move the practical difficulties of deployment. In-
technical and socioeconomic drivers; it does not            stead, the main constraints shift to compute, en-
attempt a full structural account. Factors such             gineering capacity, and implementation expertise,
as affordability, access to capital, and digital lit-       which means that well-resourced actors still have
eracy are themselves distributed unevenly along             a clear advantage. Neither governance model is
broader lines of race, class, and gender. Those             automatically more equitable. Each comes with
wider patterns deserve further interdisciplinary            its own pattern of access constraints, dependency
attention.                                                  risks, and quality differences (cf. Tiwana 2014).

4.1. Supply-Side and Ecosystem Drivers                      4.1.3 Integration and Deployment
                                                            Much of an agent’s value depends on what it can
4.1.1 Compute Costs and Capital Barriers
                                                            connect to in the wider digital environment, in-
The political economy of AI is shaped in large              cluding APIs, proprietary databases, and soft-
part by the economics of computation. One re-               ware systems. That gives the actors control-
sult is a tension between concentrated capital and          ling this “agent infrastructure”, such as cloud
more distributed application. Two cost struc-               providers, financial institutions, and large soft-
tures matter most. The first is the very large              ware platforms, an important gatekeeping role.
capital investment required to train a foundation           Through API policies, data-sharing terms, and
model, which concentrates that capability within            platform rules, they can widen or narrow the ben-
a small number of major technology firms (Sas-              efits that agents provide to different users and
try et al., 2024; Besiroglu et al., 2024). This af-         developers. This matters directly for agent qual-
fects both the availability of the most powerful            ity, especially when effective tool use is central to
agents and the level of core intelligence they can          performance (Chan et al., 2025; Rothschild et al.,
provide. The second is the ongoing cost of infer-           2025). These chokepoints can create new forms
ence. Although much lower than training costs,              of dependence, although open standards and in-
inference can still become expensive as tasks grow          teroperability requirements may soften them.
more complex. More capable models also tend to
                                                            4.2. Socio-Political        and      Institutional
command higher per-token prices because they
                                                                 Forces
require more compute, which creates a further
pay-for-performance pattern in which premium                4.2.1 Economic Incentives and Market
tiers offer stronger reasoning or faster responses.               Dynamics
At the same time, performance gains may ta-                 Market incentives are likely to pull in both di-
per off for many tasks. If so, falling inference            rections. Firms have strong commercial reasons
costs could still make broadly accessible, “good            to offer basic agentic systems widely and cheaply
enough” agents viable for baseline autonomous               in order to build large user bases. At the same
uses even if frontier systems retain a quality ad-          time, familiar strategies such as product differ-
vantage.                                                    entiation and price discrimination are likely to

                                                        5
create substantial differences in the quality and          4.2.4 Governance, Regulation, and Soci-
quantity of agents. Premium tiers may provide                    etal Adaptation
better planning, broader tool use, or more re-             Any response to agentic inequality is constrained
liable performance. Pricing may also put large             by the “pacing problem”: technological change
agent swarms, which matter for scalable delega-            may advance much faster than institutions can
tion, beyond the reach of individuals and smaller          adapt (Marchant, 2011). That lag creates a win-
organisations. The result may be broad formal              dow in which inequalities in the ability to de-
access alongside continued inequality in the most          ploy autonomous systems can become entrenched
valuable uses.                                             by default, especially where regulatory capture is
4.2.2 Digital Literacy and Human-Agent                     also a risk (Stigler, 1971). Yet this same transi-
         Interaction                                       tion creates an opening for anticipatory gover-
How well people use AI agents will depend in               nance. The challenge is to design institutions
part on existing differences in human capital.             capable of shaping the deployment of systems
In the near term, users may need considerable              that act autonomously in complex social envi-
skill to specify complex goals and manage multi-           ronments before unequal patterns harden into
step delegation, which is likely to favour those           durable structures (Guston, 2014; Floridi et al.,
with higher levels of digital literacy. Over time,         2018).
however, more capable agents may reduce the
need for specialised technical skill by allowing           5. Governing Agentic Inequality: Com-
users to delegate complex tasks through natural               plexity and Future Directions
language and more intuitive interfaces (Gabriel            5.1. The Governance Challenge
et al., 2024). Evidence of relatively high usage of
                                                           Governing agentic inequality is not only about
LLMs in some middle-income countries, includ-
                                                           preventing the harms of disparity; it is also about
ing Nigeria and India (Similarweb, 2026; Sem-
                                                           creating the conditions under which agents can
rush, 2026), suggests that language-based inter-
                                                           function as a powerful equalising tool. This is
faces can broaden adoption in ways that more
                                                           a difficult governance problem because it begins
technical interfaces often do not.
                                                           with a normative question: what distribution of
4.2.3 Geopolitics and Jurisdictional Frag-                 agentic capability should count as fair? (Gabriel,
        mentation                                          2022). Societies already tolerate large dispari-
At the global level, agentic inequality may be             ties in access to expert human services such as
shaped by a tension between techno-national                legal or financial advice. The question, then, is
competition and the need for international coor-           whether inequalities in agentic capability should
dination. National security concerns are already           be judged by the same standards as disparities
driving protectionist policies, such as semicon-           in human capability, or whether their scalability
ductor export controls, which restrict access to           and autonomy require stricter standards of jus-
foundational AI hardware (Leicht, 2025; Larsen,            tice. A full account of agentic equality lies beyond
2022). As agentic systems mature, similar log-             the scope of this paper. Two directions neverthe-
ics could extend from hardware to software, lead-          less seem especially promising: ensuring universal
ing to mercantilist strategies where firms offer de-       structural availability as a threshold condition,
graded export versions of their agents that have           and designing agent infrastructure with public-
weaker planning abilities or tighter limits on au-         interest obligations.
tonomous action. This could produce durable in-               Even if some normative consensus emerges,
ternational asymmetries in agentic power. Juris-           substantial practical obstacles remain. Existing
dictional fragmentation may deepen those asym-             legal frameworks are poorly suited to harms pro-
metries, as divergent regulations on issues such           duced by unequal agentic capability, where dis-
as data privacy create compliance burdens that             advantage may arise through cumulative strate-
large, multinational firms are better positioned to        gic asymmetries rather than a single clearly
absorb than smaller competitors (Mueller, 2021).           cognisable wrong (Kolt, 2025). Attempts to
Against this, an emerging international consen-            level the playing field through direct interven-
sus around AI safety and responsible deployment            tion also face serious coordination problems and
may provide at least a partial basis for more coor-        the Collingridge dilemma: acting early is dif-
dinated and equitable governance (Concordia AI,            ficult because uncertainty is high, while acting
2024; Bengio et al., 2025).                                late risks the technology already being entrenched

                                                       6
(Collingridge, 1980). Caps on agent power, for            5.2.3 Technical and Infrastructural Levers
example, could constrain innovation, while man-                 for Equality
dates to redistribute compute could divert re-            A third programme concerns the design of the
sources away from large-scale projects that may           agentic ecosystem itself. The aim is to build
offer substantial societal benefits. Government           equity-supporting features directly into techni-
efforts to guarantee universal access through a           cal and infrastructural arrangements, reducing
single provider could produce vendor lock-in and          harmful capability gaps and limiting excessive
weaken competition, reinforcing rather than re-           concentration in the deployment of large numbers
ducing inequality (Sastry et al., 2024; Stigler,          of agents. Key questions include: How to govern
1971).                                                    critical resources such as compute in ways that
                                                          balance innovation with equitable access? Which
5.2. A Forward-Looking Research Agenda
                                                          interoperability standards may be needed to pre-
The path forward requires research organised              vent platform lock-in from entrenching disparities
around each of the paper’s three core dimensions.         in agent quality (Chan et al., 2025; Kapoor et al.,
The goal is to build the knowledge needed to gov-         2025)?
ern disparities around each.
                                                          5.2.4 Public Service Models for Agentic
5.2.1 Empirical Foundations: Measuring                          AI
      the Dimensions of Agentic Inequal-
                                                          A fourth line of inquiry concerns non-market
      ity
                                                          models for securing equity. This includes poli-
A first priority is measurement. Before effective         cies intended to guarantee universal access and
interventions can be designed, researchers need           a sufficient baseline of agent quality, while recog-
robust metrics to track disparities in agent avail-       nising that government-led digital provision has a
ability, quality, and quantity in real-world set-         mixed track record (Dunleavy et al., 2006). One
tings. Many of the technologies likely to drive           promising idea is “universal basic agency”: the
this inequality, such as automated negotiation or         view that access to AI agents should be treated
scaled task delegation, remain novel and largely          as a primary good in Rawls’s sense, and thus as
unmeasured. Key questions include: What are               something all citizens are entitled to as a matter
the best methods for empirically tracking the de-         of justice (Rawls, 2001). On this account, agents
ployment of AI agents and their distributional            should function as all-purpose means, enabling
impacts? How can we conduct direct techni-                people to pursue a wide range of ends and concep-
cal comparisons to assess the extent to which             tions of the good life. Justice therefore requires
disparities in agent quality allow more capable           more than formal availability alone. People must
agents to persuade, manipulate, or out-negotiate          be able to access and use agents of sufficient qual-
weaker ones? Possible indicators include: agent           ity for that capability to be genuinely effective
deployment rates by income decile and geogra-             across the population, even where others can de-
phy, benchmark performance gaps between free              ploy more powerful or more numerous systems.
and premium agents on standardised task suites,           Key questions include: Should a government pro-
and performance differentials in controlled nego-         vide a public-option AI agent, or would subsi-
tiation settings across capability tiers.                 dising private services be more effective? What
                                                          level of agent quality would constitute a meaning-
5.2.2 Normative Foundations: Defining
                                                          ful baseline of empowerment? How could public
      Fairness Across the Dimensions
                                                          agents, or public infrastructure for private agents,
A second programme is normative. Once em-                 be designed to serve public rather than commer-
pirical patterns are clearer, the next task is de-        cial interests? Early proposals for public AI in-
termining which disparities in agent availability,        frastructure suggest that this is a live policy ques-
quality, and quantity are socially or ethically un-       tion in several jurisdictions (Jackson et al., 2024;
acceptable. Key questions here include: Which             Sitaraman and Parek, 2025).
participatory methods, such as citizen assem-
blies, are best suited to eliciting public prefer-        5.2.5 Regulatory Frameworks for Agentic
ences about unacceptable capability gaps? How                   Interactions
can these preferences be translated into concrete         A final programme concerns the regulation of
design principles or regulatory guardrails govern-        asymmetries in agent quality and quantity. These
ing disparities in agent quality?                         new asymmetries strain existing legal doctrines,

                                                      7
and without clearer rules, the advantages con-                Advanced AI Assistants, pages 146–156. 2024.
ferred by superior agents may become entrenched.              Preprint at arXiv:2404.16244.
Key questions include: How can legal frame-
works be adapted to provide recourse for indi-              Besiroglu, Tamay, Bergerson, Sage A., Michael,
viduals harmed by disparities in agent quality                Amelia, Heim, Lennart, Luo, Xueyun, and
(Calvo et al., 2020)? What agile or outcome-                  Thompson, Neil. The compute divide in ma-
based regulatory models can keep pace with tech-              chine learning: A threat to academic con-
nical change while protecting people from ex-                 tribution and scrutiny?, 2024. Preprint at
ploitation by actors deploying vast numbers of                arXiv:2401.02452.
agents (Marchant, 2011)?
                                                            Bommasani, Rishi, Hudson, Drew A., Adeli,
5.3. Conclusion                                               Ehsan, Altman, Russ, Arora, Simran, et al. On
Agentic inequality is a new societal challenge pro-           the opportunities and risks of foundation mod-
duced by the interaction of technical, economic,              els, 2022. Preprint at arXiv:2108.07258.
and political forces. The framework developed
here – availability, quality, and quantity – marks          Bovens, Mark and Zouridis, Stavros. From
out the territory. Scalable delegation represents             street-level to system-level bureaucracies: How
a genuinely novel source of inequality, as does the           information and communication technology
shift from contests between people to contests be-            is transforming administrative discretion and
tween their agents. However, many of the drivers              constitutional control. Public Administration
of inequality are also the potential levers for shap-         Review, 62(2):174–184, 2002.
ing more equitable outcomes, from model archi-
                                                            Brynjolfsson, Erik and McAfee, Andrew. The
tecture to market design. That window will not
                                                              Second Machine Age: Work, Progress, and
remain open indefinitely. Once patterns of agen-
                                                              Prosperity in a Time of Brilliant Technologies.
tic deployment become entrenched, they will be
                                                              W. W. Norton & Company, New York, NY,
far harder to reshape. The research agenda pro-
                                                              2014.
posed above is an attempt to identify what needs
to be understood before that point.                         Brynjolfsson, Erik, Chandar, Bhargav, and Chen,
                                                              Rui. Canaries in the coal mine? Six facts about
Acknowledgements
                                                              the recent employment effects of artificial in-
We thank Alan Chan, Noam Kolt, Seth Lazar,
                                                              telligence. Technical report, Stanford Digital
and Sam Manning for helpful feedback. This
                                                              Economy Lab, Stanford Institute for Human-
work was supported by the Future Impact Group
                                                              Centered Artificial Intelligence, 2025a.
and the Cooperative AI Foundation.
Competing interests                                         Brynjolfsson, Erik, Li, Danielle, and Raymond,
M.S. is employed by Access Partnership, a tech-               Lindsey. Generative AI at work. The Quarterly
nology policy consultancy whose clients include               Journal of Economics, 140(2):889–942, 2025b.
companies operating in the AI industry. I.G. is
                                                            Calvo, Rafael A., Peters, Dorian, Vold, Karina,
employed by Google DeepMind. O.B. and L.H.
                                                              and Ryan, Richard M. Supporting human au-
declare no competing interests.
                                                              tonomy in AI systems: A framework for ethi-
References                                                    cal enquiry. In Burr, Christopher and Floridi,
Acemoglu, Daron and Restrepo, Pascual. Robots                 Luciano, editors, Ethics of Digital Well-Being,
  and jobs: Evidence from US labor markets.                   volume 140, pages 31–54. Springer Interna-
  Journal of Political Economy, 128(6):2188–                  tional Publishing, Cham, 2020.
  2244, 2020.
                                                            Chan, Alan, Wei, Kevin, Huang, Sihao, Rajku-
Bengio,  Yoshua et al.        International                  mar, Nitarshan, Perrier, Elija, Lazar, Seth,
  AI safety report 2025, 2025.      https:                   Hadfield, Gillian K., and Anderljung, Markus.
  //internationalaisafetyreport.                             Infrastructure for AI agents. Transactions on
  org/publication/                                           Machine Learning Research, 2025. https://
  international-ai-safety-report-2025.                       openreview.net/forum?id=Ckh17xN2R2.

Bergman, A. S., Shelby, Renee, and Gabriel, Ia-             Collingridge, David. The Social Control of Tech-
  son. Access and opportunity. In The Ethics of               nology. Frances Pinter, 1980.

                                                        8
Concordia AI.      The state of China-                   Ilves, Luukas, Kilian, Martin, Parazzoli, Ste-
  Western track 1.5 and 2 dialogues                         fano Maria, Peixoto, Tiago C., and Velsberg,
  on AI.      AI Safety in China, 2024.                     Ott. The agentic state: Rethinking govern-
  https://aisafetychina.substack.com/                       ment for the era of agentic AI. Technical report,
  p/the-state-of-china-western-track.                       Global Government Technology Centre Berlin
                                                            & The World Bank, 2025.
Cui, Kevin Zhiqi et al. The effects of genera-
 tive AI on high-skilled work: Evidence from             Jackson, Ben et al. Public AI: Infrastructure
 three field experiments with software devel-              for the common good. Public AI Network,
 opers. Management Science, 2026. https:                   2024.    https://doi.org/10.5281/zenodo.
 //doi.org/10.1287/mnsc.2025.00535.                        13914560.
                                                         Jasanoff, Sheila. States of Knowledge: The Co-
Dunleavy, Patrick, Margetts, Helen, Bastow, Si-            Production of Science and the Social Order.
 mon, and Tinkler, Jane. Digital Era Gov-                  Routledge, London, 2004.
 ernance: IT Corporations, the State, and e-
 Government. Oxford University Press, 2006.              Kapoor, Sayash, Kolt, Noam, and Lazar, Seth.
                                                          Position: Build agent advocates, not platform
Floridi, Luciano, Cowls, Josh, Beltrametti,               agents. In Proceedings of Machine Learning Re-
  Monica, Chatila, Raja, Chazerand, Patrice,              search, volume 267, pages 81617–81633, 2025.
  Dignum, Virginia, Luetge, Christoph, Madelin,
  Robert, Pagallo, Ugo, Rossi, Francesca,                Kasirzadeh, Atoosa and Gabriel, Iason. Char-
  Schafer, Burkhard, Valcke, Peggy, and Vayena,           acterizing AI agents for alignment and gover-
  Effy. AI4People — an ethical framework for              nance, 2025. Preprint at arXiv:2504.21848.
  a good AI society: Opportunities, risks, prin-         Kolt, Noam. Governing AI agents, 2025. Preprint
  ciples, and recommendations. Minds and Ma-              at arXiv:2501.07913.
  chines, 28(4):689–707, 2018.
                                                         Korinek, Anton and Vipra, Jai. Concentrating
Gabriel, Iason. Toward a theory of justice for ar-        intelligence: Scaling and market structure in
 tificial intelligence. Daedalus, 151(2):218–231,         artificial intelligence. Economic Policy, 40:225–
 2022.                                                    256, 2025.

Gabriel, Iason, Manzini, Arianna, Keeling, Geoff,        Krier, Samuel.     Coasean bargaining at
 et al. The ethics of advanced AI assistants,              scale.    AI Policy Perspectives, 2025.
 2024. Preprint at arXiv:2404.16244.                       https://www.aipolicyperspectives.com/
                                                           p/coasean-bargaining-at-scale.
Gimbel, Martha, Kinder, Molly, Kendall, Jake,            Larsen, Bjørn Conrad. Geopolitics of AI and the
  and Lee, Michael. Evaluating the impact of AI            rise of digital sovereignty. Technical report,
  on the labor market: Current state of affairs.           Brookings Institution, 2022.
  Technical report, The Budget Lab at Yale Uni-
  versity, 2025.                                         Lazar, Seth. Governing the algorithmic city. Phi-
                                                           losophy & Public Affairs, 53(2):102–168, 2025.
Goldberg, Ben et al. AI and the future of
 digital public squares, 2024. Preprint at               Leicht, Anton. Mercantilist AI policy: Re-
 arXiv:2412.09988.                                         constructing the doctrine behind US
                                                           AI foreign policy.   Online essay, 2025.
Guston, David H. Understanding anticipatory                https://writing.antonleicht.me/p/
 governance. Social Studies of Science, 44(2):             mercantilist-ai-policy.
 218–242, 2014.                                          Li, Junyou, Zhang, Qin, Yu, Yangbin, Fu, Qiang,
                                                           and Ye, Deheng. More agents is all you need.
Hosseini Maasoum, Seyed Mohamad and
                                                           Transactions on Machine Learning Research,
 Lichtinger, Gal.         Generative AI as
                                                           2024.
 seniority-biased technological change: Ev-
 idence from U.S. résumé and job posting               Liu, Chang, Wang, Chonghua, Cao, Jiaxuan,
 data.      SSRN Electronic Journal, 2025.                 et al. A vision for auto research with LLM
 https://doi.org/10.2139/ssrn.5425555.                     agents, 2025. Preprint at arXiv:2504.18765.

                                                     9
Marchant, Gary E.       The growing gap be-                Sastry, Girish, Heim, Lennart, Belfield, Haydn,
 tween emerging technologies and the law.                    Anderljung, Markus, Brundage, Miles, Hazell,
 In Marchant, Gary E., Allenby, Braden R.,                   Julian, O’Keefe, Cullen, Hadfield, Gillian K.,
 and Herkert, Joseph R., editors, The Grow-                  Ngo, Richard, Pilz, Konstantin, Gor, George,
 ing Gap Between Emerging Technologies and                   Bluemke, Emma, Shoker, Sarah, Egan, Janet,
 Legal-Ethical Oversight, volume 7, pages 19–33.             Trager, Robert F., Avin, Shahar, Weller,
 Springer Netherlands, Dordrecht, 2011.                      Adrian, Bengio, Yoshua, and Coyle, Di-
                                                             ane. Computing power and the governance
Mathur, Arunesh et al. Dark patterns at scale:               of artificial intelligence, 2024. Preprint at
 Findings from a crawl of 11K shopping web-                  arXiv:2402.08797.
 sites. Proceedings of the ACM on Human-
 Computer Interaction, 3(CSCW):81, 2019.                   Selwyn, Neil. Reconsidering political and popu-
                                                             lar understandings of the digital divide. New
Mueller, Benjamin. How much will the artificial              Media & Society, 6(3):341–362, 2004.
 intelligence act cost Europe? Technical report,
 Centre for Data Innovation, 2021.                         Semrush. Top websites in Nigeria. https://www.
                                                             semrush.com/trending-websites/ng/all,
Mumford, Lewis. The Myth of the Machine.                     2026. Accessed April 2026.
 Vol. 1: Technics and Human Development.
 Harcourt, Brace, Jovanovich, New York, NY,                Sen, Amartya. Development as Freedom. Oxford
 1967.                                                       University Press, 1999.

                                                           Similarweb.   Top websites ranking for In-
Noy, Shakked and Zhang, Whitney. Experimental
                                                             dia.        https://www.similarweb.com/
  evidence on the productivity effects of genera-
                                                             top-websites/india/, 2026.      Accessed
  tive artificial intelligence. Science, 381(6654):
                                                             April 2026.
  187–192, 2023.
                                                           Sitaraman, Ganesh and Parek, Ketan. The global
Peng, Sida, Kalliamvakou, Eirini, Cihon, Peter,              rise of public AI. Technical report, Vanderbilt
  and Demirer, Mert. The impact of AI on de-                 Policy Accelerator, 2025.
  veloper productivity: Evidence from GitHub
  Copilot, 2023. Preprint at arXiv:2302.06590.             Stigler, George J. The theory of economic reg-
                                                             ulation. The Bell Journal of Economics and
Persily, Nathaniel and Tucker, Joshua A. Social              Management Science, 2(1):3–21, 1971.
  Media and Democracy: The State of the Field,
  Prospects for Reform. Cambridge University               Summerfield, Christopher et al. The impact of
  Press, 2020.                                               advanced AI systems on democracy. Nature
                                                             Human Behaviour, 9:2420–2430, 2025.
Plantin, Jean-Christophe, Lagoze, Carl, Ed-
  wards, Paul N., and Sandvig, Christian. In-              Tiwana, Amrit. Platform Ecosystems: Aligning
  frastructure studies meet platform studies in              Architecture, Governance, and Strategy. Else-
  the age of Google and Facebook. New Media                  vier, 2014.
  & Society, 20(1):293–310, 2018.                          Tomasev, Nenad et al. Virtual agent economies,
Prunkl, Carina. Human autonomy at risk? An                   2025. Preprint at arXiv:2509.10147.
  analysis of the challenges from AI. Minds and            van Dijk, Jan A. G. M. The Deepening Divide:
  Machines, 34:26, 2024.                                     Inequality in the Information Society. SAGE,
                                                             2005.
Rawls, John. Justice as Fairness: A Restatement.
  Harvard University Press, 2001.                          Van Loo, Rory. Digital market perfection. Michi-
                                                             gan Law Review, 117(5):815–884, 2019.
Rothschild, David M., Mobius, Markus, Hof-
  man, Jake M., Dillon, Eleanor W., Goldstein,             Wang, Lei, Ma, Chen, Feng, Xueyang, Zhang,
  Daniel G., Immorlica, Nicole, Jaffe, Sonia,               Zeyu, Yang, Hao, Zhang, Jingsen, Chen,
  Lucier, Brendan, Slivkins, Aleksandrs, and Vo-            Zhiyuan, Tang, Jiakai, Chen, Xu, Lin, Yankai,
  gel, Matt. The agentic economy, 2025. Preprint            Zhao, Wayne Xin, Wei, Zhewei, and Wen,
  at arXiv:2505.15799.                                      Ji-Rong. A survey on large language model

                                                      10
  based autonomous agents. Frontiers of Com-
  puter Science, 18(6):186345, 2024. URL http:
  //arxiv.org/abs/2308.11432.

Warschauer, Mark. Technology and Social Inclu-
 sion: Rethinking the Digital Divide. MIT Press,
 2003.

Weidinger, Laura, Mellor, John, Rauh, Maribeth,
 Griffin, Conor, Uesato, Jonathan, Huang, Po-
 Sen, Cheng, Myra, Glaese, Mia, Balle, Borja,
 Kasirzadeh, Atoosa, Kenton, Zac, Brown,
 Sasha, Hawkins, William, Stepleton, Tom,
 Biles, Courtney, Birhane, Abeba, Haas, Ju-
 lia, Rimell, Laura, Hendricks, Lisa Anne, Isaac,
 William, Legassick, Sean, Irving, Geoffrey, and
 Gabriel, Iason. Ethical and social risks of
 harm from language models, 2021. Preprint
 at arXiv:2112.04359.

Weyl, E. Glen, Tang, Audrey, and the Plurality
 Community. Plurality: The Future of Collab-
 orative Technology and Democracy. Radicalx-
 Change, 2024.

Xu, Jiawei et al. Rethinking the value of multi-
 agent workflow: A strong single agent baseline,
 2026. Preprint at arXiv:2601.12307.

Yang, Yifan et al. Understanding agent scaling in
  LLM-based multi-agent systems via diversity,
  2026. Preprint at arXiv:2602.03794.

Zhang, Eric, Zhu, Eric E., Bansal, Gagan, Four-
  ney, Adam, Mozannar, Hussein, and Gerrits,
  Jacob. Optimizing sequential multi-step tasks
  with parallel LLM agents, 2025. Preprint at
  arXiv:2507.08944.

Zhu, Shijia, Sun, Jingbo, Nian, Yi, South, To-
  bin, Pentland, Alex, and Pei, Jian. The au-
  tomated but risky game: Modeling and bench-
  marking agent-to-agent negotiations and trans-
  actions in consumer markets, 2025. Preprint at
  arXiv:2506.00073.

Żywot, Aleksander, Chen, Xiang, and de Ri-
   jke, Maarten. Can small agent collaboration
   beat a single big LLM?, 2026. Preprint at
   arXiv:2601.11327.




                                                    11

