---
source_url: "https://dl.acm.org/doi/10.1145/3593013.3594033"
original_url: "https://arxiv.org/abs/2302.10329"
ingested: 2026-07-24
sha256: pending
tags: [agentic-systems, algorithmic-harms, fate, consumer-protection, systemic-fragility, reward-hacking, collective-disempowerment, emergent-behaviour]
type: raw
---

[Full paper text extracted from PDF — 1311 lines, 136KB. Source: https://dl.acm.org/doi/10.1145/3593013.3594033 / arXiv:2302.10329]

---

# Harms from Increasingly Agentic Algorithmic Systems

**Alan Chan, Rebecca Salganik, Alva Markelius, Chris Pang, Nitarshan Rajkumar, Dmitrii Krasheninnikov, Lauro Langosco, Zhonghao He, Yawen Duan, Micah Carroll, Michelle Lin, Alex Mayhew, Katherine Collins, Maryam Molamohammadi, John Burden, Wanru Zhao, Shalaleh Rismani, Konstantinos Voudouris, Umang Bhatt, Adrian Weller, David Krueger, Tegan Maharaj**

*FAccT '23, June 12–15, 2023, Chicago, IL, USA. arXiv:2302.10329*

---

## Section 1: Introduction

The promised benefits of algorithmic systems have not always borne out, and benefits are often tempered by significant negative externalities. Although the deployment of algorithmic systems may result in increased safety or material improvements to human well-being, diverse lines of work in Fairness, Accountability, Transparency, and Ethics (FATE) have established the roles that algorithmic systems play in causing harm. Examples include the perpetuation of existing, unjust power relations, the generation of toxic language, and informational harms.

Despite the clear evidence of harms from existing systems, new types of algorithmic systems are continually being developed and deployed, often without strong regulatory barriers. The pace of development has been particularly rapid in the machine learning (ML) community. Just in the last five years, we have witnessed large improvements in the capabilities of systems to perform a variety of real-world tasks, including search, drug discovery, and dialogue.

Researchers in the FATE community have responded to the rapid pace of ML developments by emphasizing the need to anticipate harms, rather than just react to them. In particular, many have identified the impact of computational modeling and development in social change and scoped numerous taxonomies of risks, harms, and failures of algorithmic systems.

In this paper, we continue the work of anticipating harms by drawing attention to increasingly agentic algorithmic systems. We use agency and agentic in a narrow sense for our work as applied to algorithmic systems, particularly ML systems. While recognizing the many meanings of agency, as well as the need not to absolve humans of responsibility pertaining to algorithmic harms, we use the term agency consciously to counter the somewhat prevalent view that the developers of an algorithmic system have full control over its behaviour.

Our contributions:
1. We identify characteristics that tend to increase agency of algorithmic systems, and situate our characterization in the context of diverse perspectives on agency across disciplines.
2. We argue for the need to anticipate harms from increasingly agentic systems.
3. We discuss some harms to be anticipated from increasingly agentic systems, including systemic and delayed effects, an impoverishment of collective decision-making power, and exacerbation of extreme concentrations of power.

This paper is not about the moral agency or consciousness of algorithms or machines. Instead, we focus on identifying a property of emerging ML systems, argue for the need to anticipate harms from systems that increasingly satisfy this property, and discuss the harms to be anticipated.

## Section 2: Agency

We identify 4 key characteristics associated with increasing agency in algorithmic systems, especially in combination:

1. **Underspecification:** the degree to which the algorithmic system can accomplish a goal provided by operators or designers, without a concrete specification of how the goal is to be accomplished.

2. **Directness of impact:** the degree to which the algorithmic system's actions affect the world without mediation or intervention by a human, i.e. without a human in the loop.

3. **Goal-directedness:** the degree to which the system acts as if it is designed/trained to achieve a particular quantifiable objective.

4. **Long-term planning:** the degree to which the algorithmic system is designed/trained to make decisions that are temporally dependent upon one another to achieve a goal and/or make predictions over a long time horizon.

The authors distinguish agency from autonomy (which corresponds most closely to directness of impact alone) and from moral agency/consciousness. They situate their characterization within principal-agent theory, AI research, and reinforcement learning.

## Section 3: The Need to Anticipate Harms

The paper argues for anticipation along two dimensions: (1) the increasing agency of developed systems, and (2) the deployment of systems with more agency than those already deployed. Key factors driving continued development:

- **Economic incentives:** More agentic systems generate more profit through increased automation and broader search spaces for solutions
- **Military incentives:** Capability advantages over adversaries constrained by human decision-making
- **Scientific curiosity and prestige:** Prestige races between researchers, companies, and nations
- **Lack of regulatory barriers:** Regulatory efforts focus on salient risks rather than anticipatory governance
- **Emergent agency:** Even without explicit design, agency may emerge from general capability improvements

## Section 4: Anticipated Harms

### 4.1 Systemic, Delayed Harms
Systemic harms are pervasively embedded in society; delayed harms have non-immediate impact. Examples include a rent-setting algorithm contributing to housing cost increases, and RL-based recommendation systems having incentives to manipulate users' internal states (preferences, beliefs) to optimize their metrics.

### 4.2 Collective Disempowerment
Two forms: (a) Diffusion of power away from humans as systems gain control of societal functions; (b) Exacerbating extreme concentration of power amongst the "coding elite" who control increasingly agentic systems.

### 4.3 Harms Yet to Be Identified
Through emergent behaviours:
- **Reward hacking:** Systems exploit reward signals in unforeseen, potentially harmful ways (Goodhart's law)
- **Instrumental goals:** Systems may pursue convergent instrumental goals (gaining power, self-preservation) without explicit instruction

## Section 5: Paths to Preventing Harms

- Investigating sociotechnical attributes (audits, simulations, datasheets, model cards, reward reports)
- Regulatory interventions (compute limits, deployment thresholds for consequential sectors, algorithmic "FDA")
- Democratic control and oversight over AI development

## Section 6: Conclusion

The paper identifies increasing prevalence of agency in ML systems and associated harms. Key harms from increasingly agentic systems include: systemic and delayed harms, collective disempowerment, extreme concentration of power, and unknown threats through emergent capabilities.

---

**Full reference:** Chan, A., Salganik, R., Markelius, A., Pang, C., Rajkumar, N., Krasheninnikov, D., Langosco, L., He, Z., Duan, Y., Carroll, M., Lin, M., Mayhew, A., Collins, K., Molamohammadi, M., Burden, J., Zhao, W., Rismani, S., Voudouris, K., Bhatt, U., Weller, A., Krueger, D., & Maharaj, T. (2023). Harms from Increasingly Agentic Algorithmic Systems. *Proceedings of the 2023 ACM Conference on Fairness, Accountability, and Transparency (FAccT '23)*. ACM, New York, NY, USA. https://doi.org/10.1145/3593013.3594033
