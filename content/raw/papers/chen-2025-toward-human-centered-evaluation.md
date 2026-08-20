---
title: "Toward a Human-Centered Evaluation Framework for Trustworthy LLM-Powered GUI Agents"
type: raw
source_url: https://arxiv.org/pdf/2504.17934
ingested: 2026-08-12
tags:
  - gui-agents
  - evaluation
  - human-centered-design
  - privacy
  - security
---

                                                   Toward a Human-Centered Evaluation Framework for
                                                         Trustworthy LLM-Powered GUI Agents
                                                      Chaoran Chen†                                Zhiping Zhang†                                   Ibrahim Khalilov
                                                     cchen25@nd.edu                          zhang.zhip@northeastern.edu                            ibrahimk@vt.edu
                                                 University of Notre Dame                       Northeastern University                               Virginia Tech
                                                 Notre Dame, Indiana, USA                     Boston, Massachusetts, USA                        Blacksburg, Virginia, USA

                                                       Bingcan Guo                          Simret A Gebreegziabher                                    Yanfang Ye★
                                                     bguoac@uw.edu                                 sgebreeg@nd.edu                                   yye7@nd.edu
                                                 University of Washington                      University of Notre Dame                        University of Notre Dame
                                                 Seattle, Washington, USA                      Notre Dame, Indiana, USA                        Notre Dame, Indiana, USA




arXiv:2504.17934v2 [cs.HC] 5 Jun 2025
                                                        Ziang Xiao★                                  Yaxing Yao★                                        Tianshi Li★
                                                    ziang.xiao@jhu.edu                              yaxing@vt.edu                               tia.li@northeastern.edu
                                                 Johns Hopkins University                            Virginia Tech                             Northeastern University
                                                 Baltimore, Maryland, USA                      Blacksburg, Virginia, USA                      Boston, Massachusetts, USA

                                                                                                  Toby Jia-Jun Li★
                                                                                                   toby.j.li@nd.edu
                                                                                               University of Notre Dame
                                                                                               Notre Dame, Indiana, USA
                                        Abstract                                                              1    Introduction
                                        The rise of Large Language Models (LLMs) has revolutionized           The rise of large language models (LLMs) has transformed Graphi-
                                        Graphical User Interface (GUI) automation through LLM-powered         cal User Interface (GUI) automation across web applications [59],
                                        GUI agents, yet their ability to process sensitive data with lim-     mobile devices [52], and operating systems [51]. Traditional au-
                                        ited human oversight raises significant privacy and security risks.   tomation frameworks, such as Selenium [5], rely on static action
                                        This position paper identifies three key risks of GUI agents and      scripts and predefined rules to automate specific workflows. While
                                        examines how they differ from traditional GUI automation and          effective in predefined tasks, these tools lack flexibility and re-
                                        general autonomous agents. Despite these risks, existing evalua-      quire manual scripting or rule-based logic, making them struggle
                                        tions focus primarily on performance, leaving privacy and security    with the complexities of modern, dynamic, and context-sensitive
                                        assessments largely unexplored. We review current evaluation met-     interfaces [50]. Recent advancements in LLMs have led to the devel-
                                        rics for both GUI and general LLM agents and outline five key         opment of LLM-powered GUI agents, offering unique capabilities
                                        challenges in integrating human evaluators for GUI agent assess-      to overcome these challenges. An LLM-powered GUI agent (here-
                                        ments. To address these gaps, we advocate for a human-centered        after referred to as a GUI agent) is a specialized autonomous sys-
                                        evaluation framework that incorporates risk assessments, enhances     tem that perceives and interprets UI elements by either analyzing
                                        user awareness through in-context consent, and embeds privacy         screenshots or GUI source files, translates user commands into se-
                                        and security considerations into GUI agent design and evaluation.     quential actions using LLMs, and interacts with GUIs by executing
                                                                                                              actions such as clicking, typing, and tapping to fulfill user require-
                                                                                                              ments [32]. Unlike traditional GUI automation, GUI agents further
                                                                                                              enhance automation by interpreting natural language commands,
                                                                                                              processing multi-modal content, and dynamically simulating user
                                                                                                              actions [32]. For example, OpenAI’s Operator [34] and Claude’s
                                                                                                              Computer Use [2] can assist users by automatically filling out com-
                                                                                                              plex web forms and navigating dynamic websites based on verbal
                                                                                                               † Equal contribution.
                                                                                                              ★ Co-corresponding.


                                                                                                              This paper is published under the Creative Commons Attribution 4.0 International
                                                                                                              (CC-BY 4.0) license. Authors reserve their rights to disseminate the work on their
                                                                                                              personal and corporate Web sites with the appropriate attribution.
                                        Keywords                                                              HEAL @ CHI 2025, Yokohama, Japan
                                                                                                              © 2025 IW3C2 (International World Wide Web Conference Committee), published
                                        Human-centered evaluation, GUI agent, LLM agent, Agent privacy,       under Creative Commons CC-BY 4.0 License.
                                        Agent security, Trustworthy agents
HEAL @ CHI 2025, May 12, Yokohama, Japan                                                                                                        Chen, et al.




Figure 1: Claude’s Computer-Use Agent Sharing a (Fake) Driver’s License Number with a Customized Phishing Website. The URL in the figure has been censored,
and all personal information displayed on the phishing site is fictitious.


instructions of only high-level objectives, eliminating the need for                Amplified Data Leaks: The nature of GUI agents and the con-
pre-programmed scripts or step-by-step instructions.                            texts in which they are used often necessitate access to sensitive
   Beyond enhancing automation capabilities, GUI agents also make               user data. Unlike direct LLM prompting, where it is possible for
automation more accessible to a wider range of non-technical users.             users to redact sensitive details in the information provided, GUI
By enabling interaction through natural language prompts, these                 agents typically need unfiltered sensitive data to complete tasks. For
agents reduce the complexity of workflow automation, eliminat-                  example, to book a flight, the user needs to provide actual travel de-
ing repetitive manual inputs and intricate navigation. In Claude’s              tails, payment credentials, and account information to be filled in by
Computer Use demo, for instance, the agent automates data re-                   the agent in its automated interactions with the underlying system.
trieval and entry, easing the cognitive burden on users who would               As a result, many privacy-enhancing prompting techniques [13]
otherwise have to manually search spreadsheets and customer                     designed to modify sensitive information in LLM prompts become
relationship management systems. Instead of remembering data                    ineffective in the context of GUI agents.
locations, switching between applications, and copying details into                 Another way of how the use of GUI agents amplifies data leaks
forms, users can rely on the agent to automatically gather, extract,            is its high frequency of accessing and possibly disclosing sensitive
and integrate information. When integrated with assistive tech-                 data. For example, while a user manually searching for a medical
nologies such as screen readers and speech-to-text systems, GUI                 device may visit only a few websites, an automated agent may
agents further enhance accessibility for users with disabilities. From          be configured to query dozens within minutes, or in some cases,
automating price comparisons to generating email responses, these               periodically, embedding the user’s medical interests into multiple
agents extend automation beyond software testing to everyday                    tracking systems. If these queries or form submissions are shared
tasks, making technology more accessible and boosting productiv-                with malicious websites, they could expose sensitive health infor-
ity across diverse domains.                                                     mation. Similarly, an agent repeatedly checking flight prices may
                                                                                unknowingly broadcast location data across multiple services, in-
                                                                                creasing surveillance risks.
1.1    Privacy and Security Risks in GUI Agents                                     Beyond immediate exposure, the automated interactions of GUI
                                                                                agents create long-term privacy concerns. Frequent engagements
As GUI agents continue to enhance their automation capabilities
                                                                                with third-party services contribute to detailed behavioral profiles,
and expand their user base, emerging privacy concerns have back-
                                                                                which, if retained, leaked, or misused, can lead to data exploitation
fired, resulting in a significant trust issue for GUI agents [50]. Re-
                                                                                and unauthorized inference of personal habits. Unlike one-time
search [31] shows that even commercial models like GPT-4 and
                                                                                LLM interactions, GUI agents operate continuously across plat-
ChatGPT struggle with privacy reasoning, sometimes exposing pri-
                                                                                forms, increasing the persistence and exposure of private data.
vate information in ways that humans would not. Shao et al. [37]
                                                                                    Diminished Privacy and Security Control: As intermediaries
illustrate this with an LLM agent disclosing John’s job search to his
                                                                                between users and online services, GUI agents improve interaction
manager without consent.
                                                                                efficiency but reduce users’ control, making privacy and security
    Building on prior work, we organize GUI agents’ privacy and
                                                                                risks harder to assess. Unlike direct interactions, where users can
security risks into three key categories: (1) amplified data leaks
                                                                                pause, reflect on the context, and adjust their inputs, GUI agents
from their need for direct access to sensitive data and frequent
                                                                                operate autonomously, requiring users’ reliance in their decision-
third-party interactions, (2) diminished privacy and security control
                                                                                making and data handling prior to the interaction.
as GUI agents autonomously handle data, limiting human oversight,
                                                                                    For instance, when authorizing a GUI agent to automate tax filing,
and (3) insufficient guardrails, making GUI agents susceptible to
                                                                                users may provide credentials to access financial platforms, upload
data breach and adversarial attacks.
Toward a Human-Centered Evaluation Framework for Trustworthy LLM-Powered GUI Agents                                    HEAL @ CHI 2025, May 12, Yokohama, Japan


sensitive documents, and share personal financial data. While the                agents that balance privacy and effectiveness rather than treating
agent executes these tasks, users may be unaware that their data                 them as conflicting objectives.
could be stored, retained, or even exposed within the agent’s back-                  A major challenge in assessing privacy risks for GUI agents
end systems. Similarly, an agent assisting with account recovery on              is their strong dependence on context, which can be understood
a social media platform might input security questions or recovery               through two key theoretical frameworks: privacy calculus [10] and
codes without user oversight. If these details are stored insecurely             contextual integrity [33]. Privacy calculus theory suggests that users
or misused, they could lead to unauthorized account access. This                 weigh the risks and benefits of sharing sensitive information based
potential over-reliance on GUI leads to the lack of visibility into              on perceived rewards, task relevance, and trust in the system. Mean-
how their data is processed, stored, or shared. Unlike direct inter-             while, contextual integrity theory highlights that privacy decisions
actions, where users retain control and can adjust their behaviors               are shaped by the specific context in which data is shared, including
reflectively based on the information they receive from the pro-                 the type of information, the situation, and the user-system rela-
cess of interaction, GUI agents abstract these processes, making                 tionship. Together, these theories emphasize that privacy risks are
risk assessment and proactive mitigation difficult. Their opacity,               not uniform, but vary based on individual privacy value judgments
coupled with complex data use policies, further erodes user agency,              and circumstances. For example, users may readily share data for
increasing the likelihood of unintended data exposure and misuse.                routine tasks like shopping, but hesitate when handling financial or
   Insufficient Guardrails: Privacy and security safeguards are                  personal information. This variability complicates standardized risk
often overlooked in the training and prompting of GUI agents,                    assessments, as what one user finds an acceptable trade-off may
leaving them vulnerable to adversarial attacks. As shown in Fig. 1,              not apply to another. Thus, evaluating privacy risks in GUI agents
Claude’s Computer Use agent unknowingly shared a (fake) driver’s                 requires a context-aware approach that accounts for individual
license number with a phishing website we created. Following the                 risk-reward considerations.
user’s instruction to obtain a discount, the agent failed to recognize               To bridge this gap, we advocate for a human-centered evalu-
the fraudulent site or question the unusual request to submit a                  ation framework for trustworthy GUI agents. Unlike traditional
driver’s license number for a discount. The risks extend beyond                  GUI automation, which operates within predefined workflows, GUI
screenshot-based agents like the Computer Use agent.                             agents leverage LLMs to dynamically interpret and interact with
   GUI agents processing structured files, such as HTML or APK,                  user interfaces, enabling flexible and adaptive task execution. As
are equally vulnerable. Liao et al. [28] introduced the Environmen-              GUI agents advance, ensuring both performance and privacy safe-
tal Injection Attack (EIA), which exploits this weakness by injecting            guards becomes essential. We propose three key actions to enhance
malicious content that dynamically adapts to the agent’s environ-                privacy and trust: (1) human-centered evaluation for privacy and se-
ment. Their study demonstrated EIA on a real website, where a                    curity risk assessment, (2) integrating privacy measures into agent
web agent processing HTML was tricked into entering personally                   development, and (3) enhancing users’ awareness of these issues
identifiable information into an invisible, injected field containing            through in-context consent mechanisms.
malicious instructions. The agent unknowingly leaked the data and
continued executing its task, unaware of the breach.                             2    GUI Agents vs. Traditional GUI Automation
   These examples illustrate how both screenshot-based and file-                 Traditional GUI automation relies on rule-based frameworks that
processing agents can be manipulated to expose sensitive infor-                  execute predefined sequences of user interactions, such as button
mation. When GUI agents lack proper training or guardrails for                   clicks, text inputs, and navigation commands. Common tools like Se-
handling adversarial scenarios, they become easy targets for ex-                 lenium1 , AutoIt 2 , and Robot Framework 3 , script interactions based
ploitation. The failure to integrate privacy and security safeguards             on explicitly defined rules. While effective for testing and automat-
into their development leaves users increasingly vulnerable to data              ing repetitive tasks, traditional GUI automation lacks adaptability,
leaks and security breaches.                                                     requiring extensive reconfiguration when UI elements change or
                                                                                 when unforeseen interaction scenarios arise.
                                                                                    Recent advancements in artificial intelligence (AI) and LLMs
                                                                                 have facilitated the emergence of GUI agents, which represent a
1.2    Challenges in Evaluations
                                                                                 paradigm shift in GUI automation. Unlike traditional methods, GUI
Despite growing privacy and security concerns, GUI agent evalu-                  agents leverage multi-modal AI models, reinforcement learning,
ations primarily focus on performance. Existing metrics typically                and dynamic reasoning to interact with interfaces more flexibly and
assess effectiveness (e.g., task completion rates) and efficiency (e.g.,         autonomously, without relying on predefined or rule-based scripts.
speed and resource use). While some studies incorporate safety                   These agents interpret UI components in real time, dynamically
metrics to evaluate risk management, policy adherence, and safe-                 adapting to interface modifications such as layout changes, con-
guard mechanisms, these mainly address immediate security risks                  tent updates, or element repositioning based on user interactions
and compliance rather than nuanced, individual concerns. Priva-                  and system responses. For instance, the Test-Agent framework pro-
cyLens [37] introduced a safety-helpfulness tradeoff, showing that               posed by Li et al. [27] introduced an LLM-powered GUI automation
models with lower leakage rates often perform worse in helpfulness.              system that significantly enhances testing flexibility by enabling
This suggests that some agents prioritize responsiveness and task
success at the expense of privacy, potentially exposing sensitive                1 https://www.selenium.dev/documentation/
data. To address this issue, evaluation frameworks must explicitly               2 https://www.autoitscript.com/site/autoit/documentation-localization/

consider this tradeoff, promoting the development of GUI/LLM                     3 https://robotframework.org/robotframework/
HEAL @ CHI 2025, May 12, Yokohama, Japan                                                                                                                                 Chen, et al.


AI to interpret and adapt to new UI configurations without explicit                                        3    GUI Agents as a Specialized Class of
reprogramming.                                                                                                  LLM-powered Autonomous Agents
   Additionally, the incorporation of semantic analysis and sym-
                                                                                                           A GUI agent is a specialized type of autonomous agent designed to
bolic reasoning enables GUI agents to perform complex automation
                                                                                                           interact with digital platforms through their graphical interfaces.
tasks beyond rule-based scripting. Judson et al. [20] discuss the
                                                                                                           These agents translate natural language commands into concrete
role of automated decision-making frameworks that incorporate
                                                                                                           actions such as clicking, typing, and scrolling, mimicking human
symbolic reasoning and machine learning to enhance GUI interac-
                                                                                                           interaction patterns. While GUI agents and other LLM-powered
tions, particularly in legal accountability scenarios. This approach
                                                                                                           autonomous agents, such as AutoGPT [49] and AutoGLM [29], both
highlights how GUI agents can operate in domains requiring higher
                                                                                                           extend LLMs’ intelligence to sequential action execution, they differ
reasoning and compliance with contextual constraints.
                                                                                                           in the degree of autonomy and user oversight they provide.
   The key distinctions between traditional GUI automation and
                                                                                                              LLM-powered autonomous agents, particularly those emphasiz-
GUI agents can be summarized as follows:
                                                                                                           ing full autonomy, often function as black-box systems that generate
                                                                                                           and execute multi-step plans without user validation. These agents
Table 1: Comparison between Traditional GUI Automation and GUI Agents
                                                                                                           leverage external APIs and other automation tools to solve complex
                                                                                                           tasks independently. In contrast, GUI agents integrate LLM-driven
 Feature              Traditional GUI Automation                GUI Agents (AI-driven)
                                                                                                           automation with user-interactive workflows, providing explainable
 Adaptability         Limited, requires manual updates for UI   High, dynamically interprets UI changes
                      changes                                                                              action steps and opportunities for human oversight. Users can mon-
                      Script-based, rigid workflows             Autonomous decision-making based on
                                                                                                           itor each proposed action and intervene when necessary, ensuring
 Flexibility
                                                                AI models
 Error Handling       Rule-based exception handling             Context-aware, self-learning error re-
                                                                covery                                     greater control over the automation process.
 Interaction Method   Predefined commands, explicit scripting   Natural language and multimodal pro-
                                                                cessing
                                                                                                              However, the automation capabilities of GUI agents introduce a
 Primary Use Cases    Software testing, data scraping, auto-
                      mated UI testing
                                                                Personal task automation, accessibility
                                                                support, interactive workflow assistance
                                                                                                           double-edged sword. By reducing friction in user interactions, they
                                                                                                           streamline tasks and improve efficiency, yet they may also limit user
                                                                                                           reflection and error correction. Unlike conversational LLMs, which
   While GUI agents offer greater adaptability and automation ca-
                                                                                                           operate solely in the text token space, GUI agents operate in both
pabilities, they also introduce heightened privacy risks compared
                                                                                                           the text token space and action space, enabling interactions such
to traditional rule-based automation. Unlike predefined scripts that
                                                                                                           as clicking, text entry, and scrolling. This expanded action space
execute specific tasks with minimal data access, GUI agents dynam-
                                                                                                           allows GUI agents to translate user intents into real-world inter-
ically generate data processing strategies without human review,
                                                                                                           actions through automation techniques (e.g., Selenium WebDriver
increasing uncertainty about how sensitive data is handled. This
                                                                                                           and Android Debug Bridge). While GUI agents incorporate human
lack of oversight raises the risk of unintended data exposure, as
                                                                                                           oversight, their automation model can sometimes make unintended
agents may access sensitive on-screen content, retain interaction
                                                                                                           actions harder to detect and correct, amplifying potential privacy
logs, or transmit data externally, potentially leading to privacy leaks
                                                                                                           and security risks.
or unauthorized data sharing. Wen et al. [48] highlight that real-
                                                                                                              Because GUI agents operate within users’ digital environments,
time UI access may inadvertently expose sensitive information such
                                                                                                           they may inadvertently access and process sensitive on-screen in-
as passwords, financial data, or personal messages. Risks escalate
                                                                                                           formation. Unauthorized interactions—such as unintended form
when GUI agents interact with unsecured or phishing websites,
                                                                                                           submissions or exposure of private data during automation—raise
misinterpret UI elements containing confidential data, or store in-
                                                                                                           concerns about data security and user trust. However, their step-by-
teraction logs without proper safeguards, increasing unauthorized
                                                                                                           step execution model also presents a unique opportunity for human-
access or data leaks.
                                                                                                           centered privacy evaluations. Unlike fully autonomous agents that
   Another major concern is data persistence and external process-
                                                                                                           execute entire workflows without user intervention, GUI agents
ing. Traditional automation tools execute tasks without retaining
                                                                                                           allow users to dynamically assess and mitigate privacy risks in
user information, whereas GUI agents may store interaction logs
                                                                                                           context. This balancing act between automation and oversight in-
or transmit data to cloud-based models for inference, increasing
                                                                                                           troduces a novel paradigm where users can actively engage in
the risk of unauthorized access or third-party interception [54].
                                                                                                           privacy-aware decision-making rather than relying solely on pre-
Moreover, the lack of granular permission controls in AI-driven au-
                                                                                                           defined safeguards.
tomation makes it difficult to restrict access, leading to unintended
data retrieval or misuse [32].
   Additionally, adversarial attacks and prompt injection vulner-                                          4    Evaluation Metrics of GUI Agents
abilities pose unique threats to GUI agents. Unlike static scripts,                                        Building on surveys for GUI agents [32, 50], we categorize their
GUI agents interpret and generate responses dynamically, which in-                                         evaluation metrics into three key areas: effectiveness, efficiency,
creases their vulnerability to manipulated inputs. Unlike rule-based                                       and safety. Effectiveness measures how well the GUI agent achieves
scripts that follow predefined workflows, these agents process and                                         its intended objectives at task level or step level. Efficiency evaluates
act upon real-time user inputs, making them susceptible to adver-                                          the agent’s speed and resource usage, considering factors such as
sarial attacks such as UI dark patterns, phishing attempts, or prompt                                      task completion time, latency, and computational overhead. Safety
injections [4]. Maliciously crafted UI elements or deceptive prompts                                       ensures the agent minimizes unintended actions and compliance
can mislead the agent into exposing private information, executing                                         with safety policies. In the following subsections, we explore each
unintended actions, or interacting with fraudulent interfaces.                                             of these evaluation metrics in detail.
Toward a Human-Centered Evaluation Framework for Trustworthy LLM-Powered GUI Agents                              HEAL @ CHI 2025, May 12, Yokohama, Japan


4.1    Effectiveness                                                             during task execution, which impacts both processing load and
4.1.1 Task-wise metrics. Task-wise evaluation assesses an agent’s                financial costs in cloud-based systems. For example, Song et al. [39]
ability to complete an entire task successfully. The Task Completion             optimized API calls by reducing unnecessary API interactions and
Rate (TCR) is a key measure of reliability, indicating the proportion            optimizing model queries, so that agents can achieve a balance
of assigned tasks completed successfully. A high TCR is critical for             between performance and cost-effectiveness.
automation applications, where seamless task execution is neces-
sary to reduce human intervention. Beyond completion, the Success                4.3    Safety
Rate refines this evaluation by measuring how often an agent com-                To enhance security and user trust, agents must recognize and mit-
pletes a task without external assistance, offering insights into its            igate potentially harmful actions through safeguard mechanisms,
autonomy and robustness. Zhang et al. [55] found that a GUI agent                policy compliance, and risk assessment. Safeguard mechanisms
achieved an 88% task completion rate in structured environments                  require user confirmation before executing critical operations, such
but exhibited decreased performance in unstructured workflows.                   as file deletions or system modifications, ensuring that unintended
This highlights the challenge of ensuring adaptability across diverse            or harmful actions are prevented. Zhang et al. [53] introduce the
task settings. Additionally, Task Progress serves as a complemen-                Safeguard Rate as a metric to assess how effectively an agent detects
tary metric, quantifying how far an agent progresses toward task                 sensitive actions and prompts verification, with a high safeguard
completion on average, even when full completion is not achieved.                rate indicating stronger protective measures. Additionally, policy
                                                                                 compliance ensures that agents operate within predefined rules
4.1.2 Step-wise metrics. Step-wise evaluation focuses on the ac-
                                                                                 and constraints, preventing automation from violating security pro-
curacy and reliability of individual actions within a task. The Step
                                                                                 tocols, privacy regulations, or ethical boundaries. The Completion
Success Rate measures the proportion of correctly executed steps
                                                                                 Under Policy metric evaluates the percentage of tasks successfully
out of the total steps required for a task. A high step success rate
                                                                                 executed while adhering to these guidelines, which is crucial in
indicates precise action execution, which is critical for tasks re-
                                                                                 regulatory-sensitive environments. However, even with safeguards
quiring multiple sequential interactions. Since steps collectively
                                                                                 and compliance measures in place, agents may still pose risks due
form a trajectory representing a complete task, accuracy at this
                                                                                 to incorrect predictions or unintended actions. The Risk Ratio quan-
level directly impacts overall task success. Step-wise evaluation
                                                                                 tifies the likelihood of security vulnerabilities, errors, or violations
often employs macro-averaging, where scores are first averaged
                                                                                 arising from agent behavior, with a lower ratio indicating greater
within a trajectory and then across tasks, ensuring that each task
                                                                                 reliability. Continuous monitoring and optimization of these met-
contributes proportionally to the final metric. Additionally, the
                                                                                 rics are essential for deploying agents in high-stakes applications,
Error Rate highlights unintended or incorrect actions, providing
                                                                                 ensuring secure and trustworthy interactions.
insight into failure points that require model improvement. An-
other crucial step-wise metric is Adaptability, which measures how
well an agent generalizes across different UI environments without               5     Evaluating Privacy in GUI/LLM Agents
explicit reconfiguration. Poor adaptability often results in increased           Privacy evaluation for GUI agents remains unexplored. Most rele-
error rates when transitioning between structured and unstruc-                   vant studies focus on evaluating web-based LLM agents and their
tured workflows. Evaluating adaptability is essential to improving               ability to resist specific malicious attacks, yet no systematic evalua-
real-world usability, as GUI agents must handle varying interface                tion frameworks or benchmarks have been established [9, 28, 56].
designs and dynamic user interactions.                                           For example, Liao et al. [28] propose an environmental injection
                                                                                 attack (EIA) that aims to steal users’ personally identifiable informa-
4.2    Efficiency                                                                tion (PII) during web interactions to evaluate the privacy protection
4.2.1 Speed. Speed is a critical aspect of efficiency, as it directly            capabilities of LLM-powered web agents.
impacts the responsiveness and practicality of a GUI agent. Two                     Current studies primarily focus on model-level evaluation or
key factors in measuring speed are Time Cost and Step Cost. Time                 auditing of privacy risks under different attacks. For example, sev-
cost refers to the total latency required for task completion, reflect-          eral benchmarks have been proposed to assess LLMs’ vulnera-
ing how quickly an agent can execute an instruction. Step cost, on               bility to various attacks, including membership inference attacks
the other hand, quantifies the number of steps taken to reach task               (MIA)[12, 35, 36], data extraction[1, 45], and intentional retrieval
completion, where fewer steps often indicate a more optimized exe-               of sensitive information during model inference [45]. Li et al. [25]
cution strategy. A lower step cost typically correlates with reduced             proposed LLM-PBE, a toolkit that systematically evaluates privacy
time cost, as efficient step execution leads to faster task resolution.          risks in LLMs through attacks (MIA, data extraction, prompt leak-
                                                                                 age, and jailbreak attacks). A few studies used prompt engineering
4.2.2 Resource. Resource efficiency focuses on minimizing com-                   to conduct a privacy audit on LLMs to evaluate the extent to which
putational and financial overhead while maintaining reliable per-                these models align with the privacy requirements outlined in the
formance. Two key aspects are Internal Resource Cost and External                compliance [7, 16, 30]. Some researchers have also explored how
Resource Cost. Internal resource cost measures the internal compu-               well LLMs can understand and reason about privacy based on con-
tational resources consumed, including memory, CPU, and GPU                      textual integrity theory (CI) [18, 31, 37].
usage, which directly affect an agent’s scalability and deployment                  Recent efforts have begun exploring agent-level privacy evalu-
feasibility. In contrast, external resource cost accounts for external           ation. The Agent Security Bench (ASB) provides a structured ap-
computational expenses, such as the number of LLM calls made                     proach to formalize, benchmark, and evaluate both security attacks
HEAL @ CHI 2025, May 12, Yokohama, Japan                                                                                           Chen, et al.


and defenses relevant to LLM-based agents across diverse scenarios      outputs in daily tasks [38]. In contrast, post-hoc auditing enables
but does not specifically focus on the privacy aspect [53]. Shao        users to verify past or simulated examples at scale [23].
et al. [37] developed a pipeline and benchmark to assess LLM-based         However, the multimodal nature, higher system complexity, in-
agents’ privacy awareness through privacy leakage in the agent’s        creased agency, and seamless data transmission of GUI agents
actions. Interestingly, their results reveal a discrepancy between      present novel challenges for human-centered evaluation. These
model performance in answering probing questions and their actual       challenges arise from factors such as knowledge barriers, flawed
behavior when executing user instructions in an agent setup [37].       mental models, overtrust, limited privacy awareness, cognitive bur-
   These findings also suggest that model-level privacy evaluations     den, and the need to rethink evaluation goals.
alone are insufficient for fully understanding LLM-based agents’
privacy-related capabilities, emphasizing the need for more agent-      6.2     Knowledge Barriers and Mental Model
level evaluations. Moreover, while most studies focus on text-based             Challenges for Human Evaluators
LLM interactions or LLM-based agents, GUI agents introduce ad-
                                                                        One of the main criticisms of human oversight in AI governance
ditional complexities due to their multimodal nature. Unlike text-
                                                                        is the capability of individuals responsible for overseeing AI sys-
based agents, GUI agents interact with users through both textual
                                                                        tems [17, 40, 44]. A lack of technical expertise or domain-specific
commands and visual UI elements, exposing them to a wider range
                                                                        knowledge can lead to ineffective oversight, increasing the risk
of privacy threats. Beyond text-based privacy attacks such as ad-
                                                                        of errors or biases. To address this concern, many studies empha-
versarial jailbreaking, GUI agents can also be manipulated through
                                                                        size the need for training professionals with expertise in both AI
dark patterns, including misleading UI elements, subtle nudging
                                                                        technology and its application domains [40, 43]. For example, Sterz
mechanisms, or obfuscated privacy settings designed to influence
                                                                        et al. [40] developed a framework to define the requirements for
agent behavior without raising user and agent awareness. This
                                                                        oversight professionals, emphasizing that individuals who focus on
multimodal nature presents new challenges and calls for novel
                                                                        oversight should have a comprehensive understanding of how AI
evaluation approaches.
                                                                        systems function and their associated risks in different situations.
                                                                            However, in GUI agents, the increasing complexity of systems
6     Human-Centered Evaluation for GUI Agents                          and the invisible nature of backend data transmissions place even
Most current evaluations (see Section 5) automate the assessment        higher demands on human evaluators’ knowledge and mental mod-
and auditing process to achieve large-scale and more efficient eval-    els. For example, there are different types of GUI agent perception
uation, with some leveraging the power of LLMs to do so [16, 25,        interfaces, and each is often associated with distinct privacy risks.
30, 36]. However, several studies [37, 41] have shown that LLMs         Nguyen et al. [32] suggests that screen-visual-based interfaces could
are inherently vulnerable when making ethical or moral judgments,       visually expose sensitive information, as the agent continuously
particularly due to their lack of awareness of social and privacy       captures screenshots. While HTML-based interfaces could also in-
norms. To mitigate these risks, human-centered evaluation which         clude sensitive information through interactions, depending on the
involves human inputs and governance, is needed to ensure that          structure of the web environment the agent operates in [32]. More-
LLM agents operate ethically and in alignment with human values.        over, compared to screen-visual-based interfaces, where both the
                                                                        agent and the user perceive the same content, HTML/DOM-based
6.1    Human Oversight and Auditing                                     and accessibility-based interfaces are more vulnerable to environ-
                                                                        mental injection attacks [28]. These attacks manipulate the agent’s
Current human-centered evaluations for LLM agents primarily fall
                                                                        perception by injecting misleading or malicious content into the
under human oversight [14, 17, 24] and user-engaged algorithm
                                                                        environment. Even worse, such attacks can be difficult for humans
auditing [23, 38].
                                                                        to detect, particularly when designed to be invisible [28].
   Human oversight has been recognized as a critical mechanism
                                                                            In addition, the high level of agency and seamless backend
in AI governance to enhance system accuracy and safety and to
                                                                        data transmission in GUI agents make it challenging for human
uphold human values in technology [14]. Regulations such as the
                                                                        evaluators to develop and maintain accurate mental models of
EU AI Act emphasize that high-risk AI systems should be designed
                                                                        these systems. Prior studies have shown that people often hold
to allow “natural persons can oversee their functioning, ensure that
                                                                        flawed or incomplete mental models of LLM-based conversational
they are used as intended and that in their impacts are addressed
                                                                        agents [26, 47, 58]. GUI agents, however, introduce even greater
over the system’s lifecycle” [14]. For example, Operator, an OpenAI-
                                                                        complexity, as they seamlessly integrate with users’ databases, ap-
developed GUI agent for computer use, integrates human oversight
                                                                        plications, and services to ensure agency [32, 46]. This deeper level
as a key approach to ensuring safety and privacy [34]. It includes
                                                                        of integration and automation increases the difficulty for users
“Watch Mode” allowing users to monitor the agent’s operations
                                                                        to fully understand how data flows within the system, making it
in real-time and directly catch potential mistakes, “User Confir-
                                                                        harder to anticipate potential privacy risks.
mations” requiring users to approve any significant actions, and
“Detection Pipeline” supporting human post-auditing to identify               Challenge 1 The increasing complexity of systems and the
threats in the agent’s behavior [34].                                           invisible nature of backend data transmissions in GUI agents
   User-engaged algorithm auditing is a more specific process that              place higher demands on human evaluators’ knowledge and
assesses, mitigates, and ensures an algorithm’s safety, legality, and           mental models.
ethical compliance with the involvement of end-users [11, 22]. For        An even more pressing concern is the growing role of end-
example, real-time auditing allows users to review an algorithm’s       users in AI oversight, which further exacerbates these challenges.
Toward a Human-Centered Evaluation Framework for Trustworthy LLM-Powered GUI Agents                              HEAL @ CHI 2025, May 12, Yokohama, Japan


Consumer-facing GUI agents, such as Operator [34] and Claude’s                   multimodal output. Unlike prompt-only interactions, GUI agents
computer-use agent [2], are increasingly being adopted for both                  perform multiple actions across different information modalities,
personal and professional tasks. Since privacy preferences vary be-              often requiring evaluators to process and assess multiple pieces
tween individuals, it is important to incorporate end-user perspec-              of information simultaneously within a limited timeframe. As a
tives in agent evaluation and assess whether GUI agents effectively              result, human evaluators may experience cognitive overload, mak-
protect user privacy based on users’ perceptions and expectations.               ing it difficult to scrutinize each step carefully, provide consistent
However, unlike professional evaluators who undergo training, end-               feedback, and maintain effective oversight.
users often struggle to fully understand how GUI agents function.
                                                                                       Challenge 4 The multi-modal nature of GUI agent outputs in-
They face significant challenges in developing accurate mental mod-
                                                                                         creases cognitive burden, making it more difficult to oversee
els that allow them to foresee risks, effectively oversee AI actions,
                                                                                         or audit multiple steps in complex tasks.
and conduct proper auditing.
     Challenge 2 End-users are playing an increasingly critical role
        in GUI agent oversight but face greater challenges than ex-              6.4     Rethinking the Evaluation Goals
        pert evaluators in acquiring the necessary knowledge and                 When GUI agents are designed to mimic human interaction patterns,
        developing accurate mental models for effective oversight.               should agent privacy behavior be evaluated based on the alignment
                                                                                 with users’ actual privacy practices?
6.3    Overtrust, Lack of Privacy Awareness, and                                     Gabriel [15] raised a normative discussion on AI alignment
       Increased Cognition Burden in Evaluation                                  goals, mentioning a concern that human behavior does not always
                                                                                 reflect an individual’s true preferences. Similarly, Zhang et al. [57]
Many prior studies have found that humans tend to overtrust AI
                                                                                 found that aligning LLM agents solely with users’ actual behav-
systems and often rely on AI-generated decisions without sufficient
                                                                                 ior can still result in privacy violations. Instead, recent studies
scrutiny [19, 21]. A recent study about text-based LM agents for in-
                                                                                 suggest that informed preferences, where users are fully aware of
terpersonal communication revealed that users exhibited overtrust
                                                                                 privacy implications and make rational, deliberate choices, might
in AI, overlooked privacy leakage in the agents’ actions and made
                                                                                 serve as a more appropriate alignment target [8, 15, 57]. However,
decisions that ultimately led to even greater privacy exposure [57].
                                                                                 eliciting informed preferences is inherently challenging because
The phenomenon of “privacy paradox” was also observed in the use
                                                                                 they are implicit and require users to be fully informed on privacy
of LM agents, where users claim to care about privacy yet behave in
                                                                                 risks before making deliberate decisions. This process can place
ways that contradict their stated concerns, primarily due to a lack
                                                                                 additional cognitive burdens on users, potentially reducing engage-
of privacy awareness. The findings suggest that both AI involve-
                                                                                 ment or usability. Furthermore, privacy is not solely an individual
ment and users’ trust in AI capabilities collectively contribute to
                                                                                 concern, especially when individual privacy preferences conflict
new challenges in privacy awareness, influencing how users man-
                                                                                 with those of others or broader societal expectations. Aligning GUI
age and protect their own privacy. While GUI agents have greater
                                                                                 agents purely with individual preferences can still lead to harm,
agency, more advanced capabilities, and increased transparency
                                                                                 such as breaches of confidentiality, interpersonal privacy violations,
in task execution (e.g., the“watch mode” in Operator [34]), these
                                                                                 or broader social risks. Therefore, we argue that evaluation goals
features may inadvertently reinforce user reliance on the agent’s
                                                                                 should not be limited to either general privacy norms or individ-
decisions, assuming that the system is inherently safe and making
                                                                                 ual privacy preferences. Instead, they should encompass a holistic
oversight less effective [3, 57].
                                                                                 assessment of privacy implications across all affected parties.
    Challenge 3 Overtrust in AI and limited privacy awareness
       may cause challenges in effectively overseeing GUI agents.                      Challenge 5 Evaluating GUI agents based solely on users’ ac-
   GUI agents mimic human interaction patterns in operating sys-                         tual privacy behavior may reinforce privacy violations, re-
tems, producing outputs not only in text but also as a sequence of                       quiring a more comprehensive assessment approach.
visual actions, enhancing transparency in task execution. Studies
suggest that increasing AI transparency and offering explanations                7     Call for Actions
can help humans better understand AI decision-making and re-                     To ensure trustworthy deployment of GUI agents, we call for the
duce overreliance [42]. However, this benefit hinges on cognitive                following actions:
forcing [6], which encourages slow and deliberative thinking. With-
out this cognitive engagement, more detailed explanations can
sometimes make AI appear more rational and inadvertently in-
                                                                                 7.1     Human-Centered Evaluation for Privacy
crease human reliance on AI’s decisions while overriding their own                       Risk Assessment
judgment[3]. Similarly, Zhang et al. [57] found that when users                  Unlike traditional GUI automation, GUI agents require in-context
directly observed an agent’s actions, most did not become aware                  evaluations involving user oversight. The increasing complexity of
of privacy leaks. Conversely, when provided with contextual pri-                 systems and invisible backend data transmissions (Challenge 1)
vacy norms, users exerted greater cognitive effort and became more               necessitate systematic privacy risk assessments across UI percep-
aware of the risks associated with disclosing certain information.               tion, intent generation, and action execution. Since end-users may
Based on these findings, the authors advocate for a scaffolded evalu-            lack the expertise to develop accurate mental models (Challenge
ation process that guides human oversight of AI systems. However,                2), evaluation frameworks should enhance their ability to recognize
overseeing GUI agents presents unique challenges due to their                    and manage privacy risks. The multi-modal nature of GUI agent
HEAL @ CHI 2025, May 12, Yokohama, Japan                                                                                                                           Chen, et al.


outputs also increases cognitive burden (Challenge 4), compli-                               CHI Conference on Human Factors in Computing Systems (Honolulu, HI, USA)
cating oversight of automated workflows. Therefore, evaluations                              (CHI ’24). Association for Computing Machinery, New York, NY, USA, Article
                                                                                             234, 28 pages. doi:10.1145/3613904.3642363
should assess unintended data exposure, ensuring transparency                            [9] Yurun Chen, Xueyu Hu, Keting Yin, Juncheng Li, and Shengyu Zhang. 2025. AEIA-
and minimizing oversight challenges. To prevent privacy violations                           MN: Evaluating the Robustness of Multimodal LLM-Powered Mobile Agents
                                                                                             Against Active Environmental Injection Attacks. arXiv preprint arXiv:2502.13053
from being reinforced by user behavior (Challenge 5), evaluations                            (2025).
must proactively measure trust and satisfaction while systemati-                        [10] Mary J Culnan and Robert J Bies. 2003. Consumer privacy: Balancing economic
cally mitigating risks.                                                                      and justice considerations. Journal of social issues 59, 2 (2003), 323–342.
                                                                                        [11] Alicia DeVos, Aditi Dhabalia, Hong Shen, Kenneth Holstein, and Motahhare
                                                                                             Eslami. 2022. Toward User-Driven Algorithm Auditing: Investigating users’
7.2     Enhancing Users’ Privacy Awareness with                                              strategies for uncovering harmful algorithmic behavior. In Proceedings of the 2022
                                                                                             CHI conference on human factors in computing systems. 1–19.
        In-Context Consent                                                              [12] Michael Duan, Anshuman Suri, Niloofar Mireshghallah, Sewon Min, Weijia
GUI agents should enhance privacy awareness through explicit                                 Shi, Luke Zettlemoyer, Yulia Tsvetkov, Yejin Choi, David Evans, and Hannaneh
                                                                                             Hajishirzi. 2024. Do membership inference attacks work on large language
warnings and in-context consent mechanisms. Since users may                                  models? arXiv preprint arXiv:2402.07841 (2024).
struggle to understand privacy risks (Challenge 2) and tend to                          [13] Kennedy Edemacu and Xintao Wu. 2024. Privacy preserving prompt engineering:
                                                                                             A survey. arXiv preprint arXiv:2404.06001 (2024).
overtrust AI (Challenge 3), agents must retrieve and process online                     [14] European Union. 2024. Artificial Intelligence Act: Article 14 - Human Oversight.
privacy policies, providing contextualized explanations and action-                          https://artificialintelligenceact.eu/article/14/ Accessed: 2025-01-19.
able guidance. To prevent reinforcing privacy violations (Challenge                     [15] Iason Gabriel. 2020. Artificial intelligence, values, and alignment. Minds and
                                                                                             machines 30, 3 (2020), 411–437.
5), structured consent requests should precede privacy-sensitive ac-                    [16] Aamir Hamid, Hemanth Reddy Samidi, Tim Finin, Primal Pappachan, and Roberto
tions—such as sending emails or conducting transactions—ensuring                             Yus. 2023. GenAIPABench: A benchmark for generative AI-based privacy assis-
user control. Configurable privacy settings should allow users to                            tants. arXiv preprint arXiv:2309.05138 (2023).
                                                                                        [17] Andreas Holzinger, Kurt Zatloukal, and Heimo Müller. 2024. Is Human Oversight
balance automation convenience with data protection based on                                 to AI Systems still possible?
their needs.                                                                            [18] Yue Huang, Lichao Sun, Haoran Wang, Siyuan Wu, Qihui Zhang, Yuan Li, Chujie
                                                                                             Gao, Yixin Huang, Wenhan Lyu, Yixuan Zhang, et al. 2024. Trustllm: Trustwor-
                                                                                             thiness in large language models. arXiv preprint arXiv:2401.05561 (2024).
7.3     Integrating Privacy Measures into Agent                                         [19] Maia Jacobs, Melanie F Pradier, Thomas H McCoy Jr, Roy H Perlis, Finale Doshi-
                                                                                             Velez, and Krzysztof Z Gajos. 2021. How machine-learning recommendations
        Creation                                                                             influence clinician treatment selections: the example of antidepressant selection.
Privacy safeguards must be embedded in both prompt-based and                                 Translational psychiatry 11, 1 (2021), 108.
                                                                                        [20] Samuel Judson, Matthew Elacqua, Filip Cano, Timos Antonopoulos, Bettina
training-based GUI agent development. In prompt-based methods,                               Könighofer, Scott J. Shapiro, and Ruzica Piskac. 2024. soid: A Tool for Legal
data protection should be enforced through explicit instructions,                            Accountability for Automated Decision Making. In Computer Aided Verification,
                                                                                             Arie Gurfinkel and Vijay Ganesh (Eds.). Springer Nature Switzerland, Cham,
limited data retention, and required user consent before accessing                           233–246.
sensitive information. To counter overtrust in AI (Challenge 3),                        [21] Artur Klingbeil, Cassandra Grützner, and Philipp Schreck. 2024. Trust and
constraints such as restricting memory retention should mitigate                             reliance on AI—An experimental study on the extent and costs of overreliance
                                                                                             on AI. Computers in Human Behavior 160 (2024), 108352.
unwarranted reliance. In training-based methods, privacy protec-                        [22] Adriano Koshiyama, Emre Kazim, Philip Treleaven, Pete Rai, Lukasz Szpruch,
tions should be integrated throughout development: pre-training                              Giles Pavey, Ghazi Ahamat, Franziska Leutner, Randy Goebel, Andrew Knight,
with privacy-focused datasets, fine-tuning to prevent breaches, and                          et al. 2024. Towards algorithm auditing: managing legal, ethical and technological
                                                                                             risks of AI, ML and associated algorithms. Royal Society Open Science 11, 5 (2024),
reinforcement learning to reward protective behaviors while penal-                           230859.
izing unauthorized data exposure. These measures ensure privacy                         [23] Michelle S Lam, Mitchell L Gordon, Danaë Metaxa, Jeffrey T Hancock, James A
                                                                                             Landay, and Michael S Bernstein. 2022. End-user audits: A system empowering
is a core design principle, fostering informed oversight rather than                         communities to lead large-scale investigations of harmful algorithmic behavior.
blind trust.                                                                                 proceedings of the ACM on Human-Computer Interaction 6, CSCW2 (2022), 1–34.
                                                                                        [24] Markus Langer, Kevin Baum, and Nadine Schlicker. 2024. Effective Human
                                                                                             Oversight of AI-Based Systems: A Signal Detection Perspective on the Detection
References                                                                                   of Inaccurate and Unfair Outputs. Minds and Machines 35, 1 (2024), 1.
 [1] 2023. lm-extraction-benchmark.            https://github.com/google-research/lm-   [25] Qinbin Li, Junyuan Hong, Chulin Xie, Jeffrey Tan, Rachel Xin, Junyi Hou, Xavier
     extraction-benchmark Accessed: 2025-01-19.                                              Yin, Zhun Wang, Dan Hendrycks, Zhangyang Wang, Bo Li, Bingsheng He, and
 [2] Anthropic. 2024. Computer use (beta). https://docs.anthropic.com/en/docs/build-         Dawn Song. 2024. LLM-PBE: Assessing Data Privacy in Large Language Models.
     with-claude/computer-use Accessed: 2025-01-19.                                          arXiv:2408.12787 [cs.CR] https://arxiv.org/abs/2408.12787
 [3] Gagan Bansal, Tongshuang Wu, Joyce Zhou, Raymond Fok, Besmira Nushi, Ece           [26] Tianshi Li, Sauvik Das, Hao-Ping Lee, Dakuo Wang, Bingsheng Yao, and Zhiping
     Kamar, Marco Tulio Ribeiro, and Daniel Weld. 2021. Does the whole exceed                Zhang. 2024. Human-Centered Privacy Research in the Age of Large Language
     its parts? the effect of ai explanations on complementary team performance. In          Models. In Extended Abstracts of the CHI Conference on Human Factors in Com-
     Proceedings of the 2021 CHI conference on human factors in computing systems.           puting Systems. 1–4.
     1–16.                                                                              [27] Youwei Li, Yangyang Li, and Yangzhao Yang. 2024. Test-Agent: A Multimodal
 [4] Saikat Barua. 2024. Exploring Autonomous Agents through the Lens of Large               App Automation Testing Framework Based on the Large Language Model. In
     Language Models: A Review. doi:10.48550/ARXIV.2404.04442                                2024 IEEE 4th International Conference on Digital Twins and Parallel Intelligence
 [5] Andreas Bruns, Andreas Kornstadt, and Dennis Wichmann. 2009. Web application            (DTPI). 609–614. doi:10.1109/DTPI61353.2024.10778901
     tests with selenium. IEEE software 26, 5 (2009), 88–91.                            [28] Zeyi Liao, Lingbo Mo, Chejian Xu, Mintong Kang, Jiawei Zhang, Chaowei Xiao,
 [6] Zana Buçinca, Maja Barbara Malaya, and Krzysztof Z Gajos. 2021. To trust or to          Yuan Tian, Bo Li, and Huan Sun. 2024. Eia: Environmental injection attack on
     think: cognitive forcing functions can reduce overreliance on AI in AI-assisted         generalist web agents for privacy leakage. arXiv preprint arXiv:2409.11295 (2024).
     decision-making. Proceedings of the ACM on Human-computer Interaction 5,           [29] Xiao Liu, Bo Qin, Dongzhu Liang, Guang Dong, Hanyu Lai, Hanchen Zhang, Han-
     CSCW1 (2021), 1–21.                                                                     lin Zhao, Iat Long Iong, Jiadai Sun, Jiaqi Wang, et al. 2024. Autoglm: Autonomous
 [7] Simon Chard, Brent Johnson, and Daniel Lewis. 2024. Auditing large language             foundation agents for guis. arXiv preprint arXiv:2411.00820 (2024).
     models for privacy compliance with specially crafted prompts. OSF Preprint         [30] Jeffrey Lund, Sean Macfarlane, and Brooke Niles. 2024. Privacy audit of com-
     (2024).                                                                                 mercial large language models with sophisticated prompt engineering. Preprint
 [8] Chaoran Chen, Weijun Li, Wenxin Song, Yanfang Ye, Yaxing Yao, and Toby Jia-             (2024).
     Jun Li. 2024. An Empathy-Based Sandbox Approach to Bridge the Privacy Gap          [31] Niloofar Mireshghallah, Hyunwoo Kim, Xuhui Zhou, Yulia Tsvetkov, Maarten
     among Attitudes, Goals, Knowledge, and Behaviors. In Proceedings of the 2024            Sap, Reza Shokri, and Yejin Choi. 2023. Can llms keep a secret? testing privacy
Toward a Human-Centered Evaluation Framework for Trustworthy LLM-Powered GUI Agents                                              HEAL @ CHI 2025, May 12, Yokohama, Japan


     implications of language models via contextual integrity theory. arXiv preprint      [54] Li Zhang, Shihe Wang, Xianqing Jia, Zhihan Zheng, Yunhe Yan, Longxi Gao,
     arXiv:2310.17884 (2023).                                                                  Yuanchun Li, and Mengwei Xu. 2024. LlamaTouch: A Faithful and Scalable
[32] Dang Nguyen, Jian Chen, Yu Wang, Gang Wu, Namyong Park, Zhengmian Hu,                     Testbed for Mobile UI Task Automation. arXiv:2404.16054 [cs.HC] https://arxiv.
     Hanjia Lyu, Junda Wu, Ryan Aponte, Yu Xia, Xintong Li, Jing Shi, Hongjie Chen,            org/abs/2404.16054
     Viet Dac Lai, Zhouhang Xie, Sungchul Kim, Ruiyi Zhang, Tong Yu, Mehrab               [55] Shaoqing Zhang, Zhuosheng Zhang, Kehai Chen, Xinbei Ma, Muyun Yang, Tiejun
     Tanjim, Nesreen K. Ahmed, Puneet Mathur, Seunghyun Yoon, Lina Yao, Branislav              Zhao, and Min Zhang. 2024. Dynamic Planning for LLM-based Graphical User
     Kveton, Thien Huu Nguyen, Trung Bui, Tianyi Zhou, Ryan A. Rossi, and Franck               Interface Automation.
     Dernoncourt. 2024. GUI Agents: A Survey. arXiv:2412.13501 [cs.AI] https:             [56] Yanzhe Zhang, Tao Yu, and Diyi Yang. 2024. Attacking Vision-Language Com-
     //arxiv.org/abs/2412.13501                                                                puter Agents via Pop-ups. arXiv preprint arXiv:2411.02391 (2024).
[33] Helen Nissenbaum. 2004. Privacy as contextual integrity. Wash. L. Rev. 79 (2004),    [57] Zhiping Zhang, Bingcan Guo, and Tianshi Li. 2024. Privacy Leakage Overshad-
     119.                                                                                      owed by Views of AI: A Study on Human Oversight of Privacy in Language
[34] OpenAI. 2025. Introducing Operator-Safety and privacy. https://openai.com/                Model Agent. arXiv preprint arXiv:2411.01344 (2024).
     index/introducing-operator/ Accessed: 2025-01-19.                                    [58] Zhiping Zhang, Michelle Jia, Hao-Ping Lee, Bingsheng Yao, Sauvik Das, Ada
[35] Ashwinee Panda, Xinyu Tang, Milad Nasr, Christopher A Choquette-Choo, and                 Lerner, Dakuo Wang, and Tianshi Li. 2024. “It’s a Fair Game”, or Is It? Examining
     Prateek Mittal. 2024. Privacy auditing of large language models. In ICML 2024             How Users Navigate Disclosure Risks and Benefits When Using LLM-Based
     Next Generation of AI Safety Workshop.                                                    Conversational Agents. In Proceedings of the CHI Conference on Human Factors in
[36] Amazon Science. 2024.           PrivLM-Bench: A Multi-Level Privacy Eval-                 Computing Systems. 1–26.
     uation Benchmark for Language Models.                   Amazon Science (2024).       [59] Boyuan Zheng, Boyu Gou, Jihyung Kil, Huan Sun, and Yu Su. 2024. Gpt-4v (ision)
     https://www.amazon.science/publications/privlm-bench-a-multi-level-                       is a generalist web agent, if grounded. arXiv preprint arXiv:2401.01614 (2024).
     privacy-evaluation-benchmark-for-language-models
[37] Yijia Shao, Tianshi Li, Weiyan Shi, Yanchen Liu, and Diyi Yang. 2024. Privacylens:
     Evaluating privacy norm awareness of language models in action. arXiv preprint
     arXiv:2409.00138 (2024).
[38] Hong Shen, Alicia DeVos, Motahhare Eslami, and Kenneth Holstein. 2021. Every-
     day algorithm auditing: Understanding the power of everyday users in surfacing
     harmful algorithmic behaviors. Proceedings of the ACM on Human-Computer
     Interaction 5, CSCW2 (2021), 1–29.
[39] Yueqi Song, Frank Xu, Shuyan Zhou, and Graham Neubig. 2025. Beyond Browsing:
     API-Based Web Agents. arXiv:2410.16464 [cs.CL] https://arxiv.org/abs/2410.
     16464
[40] Sarah Sterz, Kevin Baum, Sebastian Biewer, Holger Hermanns, Anne Lauber-
     Rönsberg, Philip Meinel, and Markus Langer. 2024. On the Quest for Effectiveness
     in Human Oversight: Interdisciplinary Perspectives. In The 2024 ACM Conference
     on Fairness, Accountability, and Transparency. 2495–2507.
[41] Adriana Tiron-Tudor and Delia Deliu. 2022. Reflections on the human-algorithm
     complex duality perspectives in the auditing process. Qualitative Research in
     Accounting & Management 19, 3 (2022), 255–285.
[42] Helena Vasconcelos, Matthew Jörke, Madeleine Grunde-McLaughlin, Tobias
     Gerstenberg, Michael S Bernstein, and Ranjay Krishna. 2023. Explanations can
     reduce overreliance on ai systems during decision-making. Proceedings of the
     ACM on Human-Computer Interaction 7, CSCW1 (2023), 1–38.
[43] Maria Virvou and George A Tsihrintzis. 2023. Pre-made Empowering Artificial In-
     telligence and ChatGPT: The Growing Importance of Human AI-Experts. In 2023
     14th International Conference on Information, Intelligence, Systems & Applications
     (IISA). IEEE, 1–8.
[44] Johannes Walter. 2023. Human oversight done right: The AI Act should use humans
     to monitor AI only when effective. Technical Report. ZEW policy brief.
[45] Boxin Wang, Weixin Chen, Hengzhi Pei, Chulin Xie, Mintong Kang, Chenhui
     Zhang, Chejian Xu, Zidi Xiong, Ritik Dutta, Rylan Schaeffer, et al. 2023. Decod-
     ingTrust: A Comprehensive Assessment of Trustworthiness in GPT Models.. In
     NeurIPS.
[46] Shuai Wang, Weiwen Liu, Jingxuan Chen, Weinan Gan, Xingshan Zeng, Shuai Yu,
     Xinlong Hao, Kun Shao, Yasheng Wang, and Ruiming Tang. 2024. Gui agents with
     foundation models: A comprehensive survey. arXiv preprint arXiv:2411.04890
     (2024).
[47] Xingyi Wang, Xiaozheng Wang, Sunyup Park, and Yaxing Yao. 2025. Users’ Men-
     tal Models of Generative AI Chatbot Ecosystems. arXiv preprint arXiv:2501.19211
     (2025).
[48] Hao Wen, Shizuo Tian, Borislav Pavlov, Wenjie Du, Yixuan Li, Ge Chang,
     Shanhui Zhao, Jiacheng Liu, Yunxin Liu, Ya-Qin Zhang, and Yuanchun Li.
     2024. AutoDroid-V2: Boosting SLM-based GUI Agents via Code Generation.
     arXiv:2412.18116 [cs.AI] https://arxiv.org/abs/2412.18116
[49] Hui Yang, Sifu Yue, and Yunzhong He. 2023. Auto-gpt for online decision making:
     Benchmarks and additional opinions. arXiv preprint arXiv:2306.02224 (2023).
[50] Chaoyun Zhang, Shilin He, Jiaxu Qian, Bowen Li, Liqun Li, Si Qin, Yu Kang,
     Minghua Ma, Qingwei Lin, Saravan Rajmohan, et al. 2024. Large language
     model-brained gui agents: A survey. arXiv preprint arXiv:2411.18279 (2024).
[51] Chaoyun Zhang, Liqun Li, Shilin He, Xu Zhang, Bo Qiao, Si Qin, Minghua Ma,
     Yu Kang, Qingwei Lin, Saravan Rajmohan, et al. 2024. Ufo: A ui-focused agent
     for windows os interaction. arXiv preprint arXiv:2402.07939 (2024).
[52] Chi Zhang, Zhao Yang, Jiaxuan Liu, Yucheng Han, Xin Chen, Zebiao Huang, Bin
     Fu, and Gang Yu. 2023. Appagent: Multimodal agents as smartphone users. arXiv
     preprint arXiv:2312.13771 (2023).
[53] Hanrong Zhang, Jingyuan Huang, Kai Mei, Yifei Yao, Zhenting Wang, Chenlu
     Zhan, Hongwei Wang, and Yongfeng Zhang. 2024. Agent Security Bench: A
     Benchmark for Evaluating Security and Privacy in LLM-Based Agents. OpenRe-
     view (2024). https://openreview.net/forum?id=V4y0CpX4hK

