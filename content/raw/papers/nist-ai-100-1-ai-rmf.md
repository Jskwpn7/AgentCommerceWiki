---
source_url: https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-1
ingested: 2026-07-04
sha256: 7576edb531d9848825814ee88e28b1795d3a84b435b4b797d3670eafdc4a89f1
tags: [report, policy-research, cross-sector]
---

# NIST AI 100-1: Artificial Intelligence Risk Management Framework (AI RMF 1.0)

**Publication Date:** January 2023
**Publisher:** National Institute of Standards and Technology (NIST), U.S. Department of Commerce
**DOI:** https://doi.org/10.6028/NIST.AI.100-1
**Pages:** ~42 + appendices
**Version:** 1.0 (living document; minor revisions tracked as ".n"; major review expected no later than 2028)

---

## Full Text

```
NIST AI 100-1

Artificial Intelligence Risk Management Framework (AI RMF 1.0)

This publication is available free of charge from: https://doi.org/10.6028/NIST.AI.100-1
January 2023

U.S. Department of Commerce
Gina M. Raimondo, Secretary
National Institute of Standards and Technology
Laurie E. Locascio, NIST Director and Under Secretary of Commerce for Standards and Technology

--- Executive Summary (full text) ---

Artificial intelligence (AI) technologies have significant potential to transform society and
people's lives — from commerce and health to transportation and cybersecurity to the
environment and our planet. AI technologies can drive inclusive economic growth and support
scientific advancements that improve the conditions of our world. AI technologies, however,
also pose risks that can negatively impact individuals, groups, organizations, communities,
society, the environment, and the planet. Like risks for other types of technology, AI risks
can emerge in a variety of ways and can be characterized as long- or short-term, high- or
low-probability, systemic or localized, and high- or low-impact.

   The AI RMF refers to an AI system as an engineered or machine-based system that
   can, for a given set of objectives, generate outputs such as predictions, recommendations,
   or decisions influencing real or virtual environments. AI systems are designed to operate
   with varying levels of autonomy (Adapted from: OECD Recommendation on AI:2019;
   ISO/IEC 22989:2022).

While there are myriad standards and best practices to help organizations mitigate the risks
of traditional software or information-based systems, the risks posed by AI systems are in
many ways unique. AI systems may be trained on data that can change over time, sometimes
significantly and unexpectedly, affecting system functionality and trustworthiness in ways
that are hard to understand. AI systems and the contexts in which they are deployed are
frequently complex, making it difficult to detect and respond to failures when they occur.

AI systems are inherently socio-technical in nature, meaning they are influenced by societal
dynamics and human behavior. AI risks and benefits can emerge from the interplay of
technical aspects combined with societal factors related to how a system is used, its
interactions with other AI systems, who operates it, and the social context in which it is
deployed.

These risks make AI a uniquely challenging technology to deploy and utilize. Without
proper controls, AI systems can amplify, perpetuate, or exacerbate inequitable or undesirable
outcomes for individuals and communities. With proper controls, AI systems can mitigate
and manage inequitable outcomes.

AI risk management is a key component of responsible development and use of AI systems.
Responsible AI practices can help align decisions about AI system design, development, and
uses with intended aim and values. Core concepts in responsible AI emphasize human
centricity, social responsibility, and sustainability. AI risk management can drive responsible
uses and practices by prompting organizations and their internal teams to think more
critically about context and potential or unexpected negative and positive impacts.

As directed by the National Artificial Intelligence Initiative Act of 2020 (P.L. 116-283), the
goal of the AI RMF is to offer a resource to organizations designing, developing, deploying,
or using AI systems to help manage the many risks of AI and promote trustworthy and
responsible development and use of AI systems. The Framework is intended to be voluntary,
rights-preserving, non-sector-specific, and use-case agnostic, providing flexibility to
organizations of all sizes and in all sectors.

The Framework is designed to equip organizations and individuals — referred to as AI
actors — with approaches that increase the trustworthiness of AI systems, and to help foster
the responsible design, development, deployment, and use of AI systems over time. AI actors
are defined by the OECD as "those who play an active role in the AI system lifecycle,
including organizations and individuals that deploy or operate AI."

The AI RMF is intended to be practical, to adapt to the AI landscape as AI technologies
continue to develop, and to be operationalized by organizations in varying degrees and
capacities so society can benefit from AI while also being protected from its potential harms.

Part 1 discusses how organizations can frame the risks related to AI and describes the
intended audience. Next, AI risks and trustworthiness are analyzed, outlining the
characteristics of trustworthy AI systems, which include: valid and reliable, safe, secure and
resilient, accountable and transparent, explainable and interpretable, privacy enhanced, and
fair with their harmful biases managed.

Part 2 comprises the "Core" of the Framework. It describes four specific functions to help
organizations address the risks of AI systems in practice: GOVERN, MAP, MEASURE, and
MANAGE — broken down further into categories and subcategories.

Additional resources are included in the AI RMF Playbook: https://www.nist.gov/itl/ai-risk-management-framework

--- Part 1: Foundational Information ---

1. Framing Risk

AI risk management offers a path to minimize potential negative impacts of AI systems,
such as threats to civil liberties and rights, while also providing opportunities to maximize
positive impacts.

1.1 Understanding and Addressing Risks, Impacts, and Harms

In the context of the AI RMF, risk refers to the composite measure of an event's probability
of occurring and the magnitude or degree of the consequences of the corresponding event.
The impacts, or consequences, of AI systems can be positive, negative, or both and can
result in opportunities or threats. When considering the negative impact, risk is a function of
1) the negative impact or magnitude of harm that would arise if the circumstance or event
occurs and 2) the likelihood of occurrence.

"Risk management refers to coordinated activities to direct and control an organization with
regard to risk" (Source: ISO 31000:2018).

AI risk management efforts should consider that humans may assume AI systems work —
and work well — in all settings. AI systems are often perceived as being more objective than
humans or as offering greater capabilities than general software.

Examples of potential harms related to AI systems include (from Figure 1):
- Consequential harm: an AI system produces a biased output affecting individuals or groups
- Responsibility gap: difficulty assigning responsibility when AI systems cause harm
- Bias: an AI system generates outputs that reinforce existing inequalities
- Safety: an AI system causes physical harm or endangers human health
- Security: an AI system is vulnerable to adversarial attacks or manipulation
- Privacy: an AI system improperly collects, uses, or shares personal data

1.2 Challenges for AI Risk Management

1.2.1 Risk Measurement
- Risks related to third-party software, hardware, and data can complicate risk measurement
- Tracking emergent risks requires proactive identification
- Lack of consensus on robust and verifiable measurement methods for risk and trustworthiness
- Measurement approaches can be oversimplified, gamed, lack critical nuance, or fail to
  account for differences in affected groups and contexts
- Risk at different stages of the AI lifecycle may yield different results
- Measuring AI risks in controlled environments may differ from real-world risks
- Inscrutable AI systems complicate risk measurement (limited explainability, lack of
  transparency, inherent uncertainties)
- Human baseline comparison is difficult to systematize

1.2.2 Risk Tolerance
- The AI RMF does not prescribe risk tolerance; this is contextual and use-case specific
- Risk tolerance influenced by legal/regulatory requirements, policies, and norms
- Risk tolerances likely to change over time as AI systems, policies, and norms evolve
- Some sectors may have established definitions of harm or documentation requirements

1.2.3 Risk Prioritization
- Attempting to eliminate negative risk entirely can be counterproductive
- Resources should be prioritized based on assessed risk level and potential impact
- AI systems designed to directly interact with humans call for highest initial prioritization
- Systems trained on sensitive/protected data require higher prioritization
- Residual risk (risk remaining after treatment) directly impacts end users

1.2.4 Organizational Integration and Management of Risk
- AI risks should not be considered in isolation; should be integrated into broader enterprise
  risk management strategies
- Overlapping risks include: privacy concerns, energy/environmental implications, security
  concerns, and general software/hardware security
- Effective risk management requires organizational commitment at senior levels
- May require cultural change within an organization or industry

2. Audience

The AI RMF is designed for organizations and individuals involved in the AI lifecycle:
- AI actors (per OECD definition): those who play an active role in the AI system lifecycle
- Includes: designers, developers, deployers, operators, and users of AI systems
- Applicable to organizations of all sizes and sectors

3. AI Risks and Trustworthiness

Characteristics of trustworthy AI systems (Figure 4):
- Valid & Reliable: AI systems perform as intended with appropriate accuracy and robustness
- Safe: AI systems do not cause physical, psychological, or economic harm
- Secure and Resilient: AI systems are protected against adversarial attacks and failures
- Accountable and Transparent: Organizations are accountable for AI system outcomes;
  operations are transparent to affected parties
- Explainable and Interpretable: AI system behavior can be explained to relevant stakeholders
- Privacy-Enhanced: AI systems protect personal data and respect privacy rights
- Fair with Harmful Bias Managed: AI systems do not produce discriminatory or unfair outcomes

4. Effectiveness of the AI RMF

The Framework's effectiveness depends on:
- Voluntary adoption and organizational commitment
- Alignment with existing standards and best practices
- Regular updates based on community feedback (formal review expected by 2028)

--- Part 2: Core and Profiles ---

5. AI RMF Core

The Core consists of four functions organized hierarchically (Figure 5):

5.1 GOVERN (cross-cutting function)
The GOVERN function encompasses organizational activities that manage AI risks across the
entire AI lifecycle. It is designed to be infused throughout the other three functions.

Categories and subcategories (Table 1):
- Map: Introduce policies and procedures for managing AI risks
  - Organizational Coherence: Establish cross-functional AI risk governance
  - Preferences and Stakeholders: Understand organizational preferences, risk tolerance, and
    stakeholder impacts
  - AI Lifecycle Processes: Define AI lifecycle processes and risk management procedures
  - Risk Management Plan: Develop and maintain a risk management plan
  - Documentation: Maintain documentation of risk management activities
- Measure: Implement processes to assess risk performance
  - Assess Risk Performance: Evaluate how well risk management processes work
  - Report AI Risk: Communicate risk findings to relevant stakeholders

5.2 MAP
The MAP function helps organizations understand, document, and communicate details about
their AI systems and risk context.

Categories and subcategories (Table 2):
- Context: Understand the application context and potential impacts
  - Environment: Understand the physical, social, and organizational environment
  - Data: Understand the data used to develop, deploy, or operate the AI system
  - Capabilities: Understand what the AI system can and cannot do
  - Outcomes: Understand the expected and actual outcomes of the AI system
- Plan: Understand the plan for AI system development, deployment, or operation
  - Plan: Understand the organization's plan for developing, deploying, or operating
    the AI system
  - Resources: Understand the resources needed for the AI system
  - Governance: Understand the governance structures for the AI system
  - Metrics: Understand the metrics used to assess the AI system's risk performance

5.3 MEASURE
The MEASURE function involves assessing AI risk performance using metrics and methods.

Categories and subcategories (Table 3):
- Assess: Evaluate risk performance using metrics
  - Metrics: Define and apply metrics to assess risk performance
  - Testing: Conduct testing to evaluate AI system performance
  - Validation: Validate that the AI system meets its intended objectives
  - Verification: Verify that the AI system meets its specifications
- Monitor: Track risk performance over time
  - Monitor: Continuously monitor AI system performance and risk indicators

5.4 MANAGE
The MANAGE function involves making decisions about risk based on the assessment.

Categories and subcategories (Table 4):
- Treat: Implement actions to address identified risks
  - Mitigate: Implement controls to reduce risk
  - Accept: Accept residual risk if it is within tolerance
  - Transfer: Transfer risk to another party (e.g., through insurance)
  - Avoid: Avoid deploying the AI system if risks are unacceptable
- Respond: Respond to emerging risks
  - Respond: Take action when new risks are identified or existing risks change
  - Learn: Learn from risk events and improve risk management processes

6. AI RMF Profiles

Profiles allow organizations to tailor the Framework to their specific context, use case, and
risk tolerance. A profile documents:
- Which parts of the Core are most relevant to the organization
- How the organization implements each function
- Risk tolerance levels for different AI systems
- Mapping to existing standards, regulations, and best practices

--- Appendices ---

Appendix A: Descriptions of AI Actor Tasks
Detailed descriptions of AI actor tasks across the AI lifecycle, including testing, evaluation,
verification, and validation tasks.

Appendix B: How AI Risks Differ from Traditional Software Risks
Explains why AI risks are unique compared to traditional software:
- Data dependency and drift
- Emergent behavior from complex systems
- Socio-technical complexity
- Difficulty in predicting and measuring impacts
- Opaque decision-making processes

Appendix C: AI Risk Management and Human-AI Interaction
Discusses the role of human-AI interaction in risk management and trustworthiness.

Appendix D: Attributes of the AI RMF
1. Be risk-based, resource-efficient, pro-innovation, and voluntary
2. Be consensus-driven and developed through an open, transparent process
3. Use clear and plain language understandable by a broad audience
4. Provide common language and understanding to manage AI risks
5. Be easily usable and fit well with other aspects of risk management
6. Be useful to a wide range of perspectives, sectors, and technology domains
7. Be outcome-focused and non-prescriptive
8. Take advantage of existing standards, guidelines, best practices
9. Be law- and regulation-agnostic
10. Be a living document

--- Notes ---

Relevance to UK Consumer Harms: This is a foundational framework document that provides
a comprehensive taxonomy and structure for understanding AI risks. While US-focused, its
principles are directly applicable to UK consumer protection contexts, particularly for:
- Understanding the spectrum of AI-related harms (bias, safety, security, privacy, fairness)
- Providing a structured approach to AI risk management that UK regulators like the CMA
  and FCA could reference
- Informing the development of UK-specific AI governance frameworks
- Highlighting the gap between current regulatory approaches and AI-specific risks
- The four functions (GOVERN, MAP, MEASURE, MANAGE) provide a template for
  regulatory frameworks and consumer protection strategies