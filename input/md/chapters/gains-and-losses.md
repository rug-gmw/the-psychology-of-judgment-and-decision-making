# Gains and Losses


Learning goals:


- Explain the difference between expected value theory, expected utility theory, and prospect theory.
- Describe the value function and its key properties: reference dependence, loss aversion, and diminishing sensitivity.
- Explain how reference points determine whether an outcome is experienced as a gain or a loss.
- Describe the probability weighting function and how it differs from using probabilities directly.
- Apply prospect theory to explain framing effects, the endowment effect, and patterns of risk seeking and risk aversion.
- Describe ambiguity aversion, subadditivity, and probability neglect as departures from rational probability use.
- Explain omission bias and nature bias as additional distortions in risky choice.


## The sting of loss


Imagine you find a €20 note on the street. You feel pleased for a moment, perhaps buy yourself a coffee, and move on with your day. Now imagine you reach into your pocket and discover that a €20 note you had earlier is gone. The objective change in wealth is the same in both cases, just with opposite signs. Yet the sting of losing €20 feels considerably worse than the pleasure of finding €20. This asymmetry between gains and losses is one of the most robust findings in the psychology of decision-making, and it sits at the heart of the theory we will explore in this chapter.


## From Expected Value to Expected Utility


To understand how people make decisions involving risk, we first need a benchmark for how they should make such decisions. The simplest normative model is expected value theory. According to this model, you should multiply each possible outcome by its probability and then add up these products. The option with the highest expected value is the one you should choose. As a formula:


$$EV = \sum_{i} x_i \times p_i$$


Here, *x* refers to the monetary outcome and *p* to its probability. If someone offers you a coin flip where heads wins you €200 and tails wins you nothing, the expected value is 0.5 × €200 + 0.5 × €0 = €100. Under a pure expected-value criterion, you should prefer this gamble to any sure amount below €100.


But most people would not behave this way. Offered the choice between €100 for certain and the coin flip described above, many people take the sure €100, even though the two options have the same expected value. People tend to avoid risk when it comes to gains. This observation motivated the development of expected utility theory, which replaces monetary outcomes with subjective utilities. The difference in utility between €0 and €100 is larger than the difference between €100 and €200: each additional euro matters a bit less as you have more. Because of this curvature, the utility of the sure €100 exceeds the expected utility of the gamble, and choosing the sure thing becomes rational. Expected utility theory was formalized by von Neumann and Morgenstern in the 1940s and became the dominant normative framework for risky decision-making [@edwards1954].


Note that expected value and expected utility are benchmarks for *decisions* — for choosing among risky options. The Bayesian framework used throughout this book is primarily a benchmark for *belief updating* — for how to revise probabilities in light of new evidence. These are complementary normative tools: Bayesian reasoning tells you what to believe, and expected utility theory tells you what to do given those beliefs.


Expected utility theory works well as a normative model — a model of how people ideally should decide. But as a descriptive model of how people actually decide, it runs into problems. One of the most famous demonstrations of its failure is the Allais Paradox [@allais1953]. In the original version, people are given two separate choice problems. In the first, they choose between option A, a sure gain of €1,000, and option B, a gamble that gives a 10% chance of €2,500, an 89% chance of €1,000, and a 1% chance of nothing. Most people prefer option A, the sure thing. In the second problem, people choose between option C, an 11% chance of €1,000 and an 89% chance of nothing, and option D, a 10% chance of €2,500 and a 90% chance of nothing. Here, most people prefer option D, the higher payoff. The paradox is that these two preferences are inconsistent under expected utility theory. The shift from the first problem to the second merely removes the same 89% chance of €1,000 from both options, which should not change the preference according to expected utility theory's independence axiom. Yet it does. People are drawn to certainty in the first problem (option A guarantees €1,000), but when certainty is no longer available in the second problem, they shift to the higher expected value. This pattern, known as the certainty effect, reveals that people do not weight outcomes by their probabilities in the way expected utility theory assumes. To explain choices like these, Kahneman and Tversky proposed prospect theory, a descriptive model of risky choice [@kahneman_tversky1979].


## Prospect Theory


Prospect theory accounts for the systematic ways in which people deviate from expected utility theory. Kahneman received the 2002 Nobel Prize in Economics largely for this work (Tversky had passed away in 1996 and could not share the prize). The theory was later refined into cumulative prospect theory [@tversky_kahneman1992], but the core ideas remained the same. It does not claim that people *should* decide in a particular way, but rather captures how they actually do. It does this through two main components: a value function and a probability weighting function. Together, these components determine the subjective value of a risky option, which prospect theory calls a *prospect*. The value of a prospect is:


$$V = \sum_{i} v(x_i) \times w(p_i)$$


Here, *v* is the value function, which transforms outcomes into subjective values, and *w* is the probability weighting function, which transforms probabilities into decision weights. The person then chooses the prospect with the highest overall value *V*. This formula looks similar to expected utility theory, but the transformations it applies to both outcomes and probabilities are fundamentally different.


## The Value Function


The value function describes how people evaluate outcomes. It has three key properties that distinguish it from classical utility theory.


Reference dependence – people do not evaluate outcomes in terms of final states of wealth. Instead, they evaluate outcomes as gains or losses relative to a reference point. This reference point is typically the person's current state, but it can also be shaped by expectations, aspirations, or the way a problem is described. A salary of €3,000 per month can feel like a gain if you expected €2,500 or a loss if you expected €3,500. The objective amount is the same, but the psychological experience depends entirely on what you compare it to.


A vivid illustration comes from a study of Olympic medalists. @medvec_etal1995 analyzed video footage from the 1992 Barcelona Olympics and found that bronze medalists appeared happier than silver medalists, both immediately after their event and during the medal ceremony. Independent raters, who did not know which medal each athlete had won, consistently rated bronze medalists as looking more pleased. If reactions depended only on objective rank, silver should always look better than bronze. But silver medalists naturally compare their outcome to gold, which they narrowly missed — and relative to that reference point, silver feels like a loss. Bronze medalists compare their outcome to finishing just outside the medals, the most salient alternative — and relative to no medal, bronze feels like a gain. The same mechanism operates in everyday life. A student who expected to fail an exam and gets a 6 out of 10 may feel elated, while a student who expected a 9 and gets an 8 may feel disappointed, even though the second student performed better.


![](input/svg/value-function.svg)


Loss aversion – losses typically loom about twice as large as equivalent gains. Losing €50 produces more psychological impact than gaining €50. This asymmetry is the formal version of the everyday observation that opened this chapter. Loss aversion explains why people are reluctant to accept fair gambles. A coin flip that wins you €100 or loses you €100 has an expected value of zero, yet most people reject it because the potential loss looms larger than the potential gain. You would typically need to offer something like a coin flip between winning €200 and losing €100 before most people would accept, because only then does the weighted gain begin to match the weighted loss.


Diminishing sensitivity – each additional unit of gain or loss has a smaller psychological impact than the one before. Going from €0 to €100 feels like a big change; going from €1,000 to €1,100 feels like much less. This applies to losses as well: going from a loss of €0 to a loss of €100 is painful, but going from a loss of €1,000 to a loss of €1,100 adds relatively little additional pain. Graphically, the value function is concave (curving downward) for gains and convex (curving upward) for losses, producing an S-shaped curve that is steeper on the loss side.


Comparison with alternatives – a related line of research suggests that people evaluate outcomes not only against a fixed reference point like their current state, but also against the alternatives they could have had. Suppose you are choosing between two job offers. One pays €50,000, the other €60,000. You take the first and later learn the second would have been even better than advertised. The disappointment you feel does not stem from €50,000 being a bad salary in absolute terms — it stems from comparison with the forgone alternative. More generally, outcomes that fall below salient alternatives produce regret, while outcomes that exceed them produce relief. Because negative emotions like regret tend to be psychologically more powerful than positive emotions like relief, this mechanism reinforces the asymmetry captured by loss aversion. This idea extends beyond standard prospect theory into models of regret and counterfactual comparison, but it provides a psychological basis for why losses consistently outweigh gains in people's evaluations. As discussed in [the chapter on the future self](#the-future-self), this kind of affective response plays a role in many judgment contexts.


These properties are not merely theoretical. They produce several characteristic patterns in risky choice, including framing effects and the endowment effect.


## Framing Effects


Because people evaluate outcomes relative to a reference point, the way a problem is described — its *frame* — can shift the reference point and thereby change decisions. The same objective situation can lead to opposite choices depending on whether outcomes are presented as gains or losses.


The most famous demonstration is the Asian disease problem [@tversky_kahneman1981]. Participants were told that a disease is expected to kill 600 people, and they must choose between two programs. In the gain frame, program A saves 200 people for certain, and program B gives a one-third chance of saving all 600 and a two-thirds chance of saving no one. In this version, 72% chose program A, the sure option. In the loss frame, program C means 400 people will die for certain, and program D gives a one-third chance that no one dies and a two-thirds chance that all 600 die. Here, 78% chose program D, the gamble. The two versions describe identical outcomes: saving 200 of 600 is the same as 400 dying. But the gain frame makes people risk averse (preferring the sure thing), while the loss frame makes people risk seeking (preferring the gamble).


Prospect theory explains this through the shape of the value function. For gains, the function is concave: the sure gain of saving 200 lives has higher subjective value than the expected value of the gamble (which also averages 200 lives saved, but with uncertainty). For losses, the function is convex: the certain loss of 400 lives feels very painful, and people would rather gamble for a chance to avoid any loss at all, even if the gamble could make things worse. This combination — risk aversion for gains and risk seeking for losses — is a direct prediction of the value function's shape and has been confirmed across many contexts, from medical decisions to financial choices.


Framing effects have real consequences. @tversky_kahneman1981 showed that even physicians displayed the same pattern of preference reversal. As discussed in [the chapter on medical decision-making](#medical-decision-making), framing plays a significant role in how health-related options are communicated and perceived. And as discussed in [the chapter on steering other people's choices](#steering-other-peoples-choices), the deliberate use of frames is a central tool in nudging people toward particular decisions.


## The Endowment Effect


Loss aversion also manifests in how people value things they already own. The endowment effect is the tendency to demand more to give up an object than one would pay to acquire it. In a classic experiment, @kahneman_etal1990 randomly gave coffee mugs to half the participants in a university class. Those who received a mug (sellers) were asked for the minimum price at which they would sell it, and those without a mug (buyers) were asked for the maximum price they would pay. If ownership did not affect valuation, sellers and buyers should have agreed on roughly the same price, and about half the mugs should have changed hands. Instead, the median selling price was more than twice the median buying price, and far fewer mugs were traded than predicted by standard economic theory.


Giving up something you own is coded as a loss, while acquiring something new is coded as a gain. Since losses loom larger than gains, sellers require more compensation to part with their mug than buyers are willing to pay to get one. The endowment effect is closely related to the status quo bias, the preference for the current state of affairs over change. Both phenomena arise because moving away from the status quo involves a loss of what you currently have. You can read more about the role of the status quo in [the chapter on steering other people's choices](#steering-other-peoples-choices), where defaults and status quo bias are discussed as tools for influencing behavior.


## The Probability Weighting Function


The second component of prospect theory is the probability weighting function, which describes how people transform stated probabilities into decision weights. In expected utility theory, a 10% chance is simply weighted by 0.10. In prospect theory, people do not use probabilities directly. Instead, they transform them through the weighting function *w(p)*, which systematically distorts the impact of probabilities on decisions.


![](input/svg/probability-function.svg)


The weighting function has a characteristic inverse S-shape. Small probabilities are overweighted: a 5% chance receives more decision weight than 0.05, meaning it has more influence on the decision than it should. This explains why people buy lottery tickets. A one-in-ten-million chance of winning is objectively negligible, but people treat it as if it were much more likely. At the same time, moderate to high probabilities are underweighted: a 90% chance receives less decision weight than 0.90, meaning people treat near-certain outcomes as less certain than they really are. This explains the certainty effect that appeared in the Allais Paradox: the difference between 100% and 99% feels much larger than the difference between 50% and 49%, even though both are one-percentage-point differences.


A distinct phenomenon occurs at the extremes. Very small probabilities — such as the chance of being hit by a meteorite — are often rounded down to zero entirely. And very high probabilities are sometimes treated as certainties. This collapsing is different from the overweighting just described. The overweighting of small probabilities applies when a probability is small but still cognitively salient — noticeable enough to register as a real possibility. When a probability is so remote that it barely registers at all, people may ignore it completely, which can lead them to forego insurance or dismiss genuine risks because a small probability feels like no probability at all. As we will see shortly, there is yet a third pattern — probability neglect — where emotionally vivid outcomes cause people to disregard probability information regardless of its size. These three phenomena (overweighting, rounding to zero, and neglect) are distinct mechanisms, but all reflect failures to use probabilities as stated. As discussed in [the chapter on risk perception](#risk-perception), these distortions have practical implications for how people respond to low-probability, high-consequence events.


The combination of the value function and the probability weighting function produces what @tversky_kahneman1992 called the fourfold pattern of risk attitudes. For high-probability gains, people are risk averse (they prefer a sure gain over a gamble with slightly higher expected value). For low-probability gains, people are risk seeking (they prefer the gamble, as in buying lottery tickets). For high-probability losses, people are risk seeking (they gamble to avoid a sure loss). And for low-probability losses, people are risk averse (they pay to eliminate a small risk, as in buying insurance). This fourfold pattern emerges naturally from the interaction of the S-shaped value function with the inverse-S-shaped weighting function, and it captures a wide range of real-world behavior that expected utility theory cannot explain.


## Beyond the Weighting Function


Subsequent research identified additional ways in which people depart from rational use of probability, extending beyond the original weighting function.


**Subadditivity.** When people judge the probability of a combined event (the probability of A or B occurring), they tend to assign it a lower value than the sum of the individual probabilities they would assign to A and B separately [@tversky_fox1995]. The parts seem to add up to more than the whole. Consider estimating why a flight might be delayed. If you separately judge the probability of delay due to weather, due to a mechanical problem, and due to air traffic congestion, each individual estimate receives focused attention, and the three probabilities might sum to, say, 65%. But if you simply judge the overall probability of "any delay," you might estimate only 40%. Considering each cause on its own gives it more psychological weight than when it is lumped together with other causes. @tversky_fox1995 demonstrated this pattern in experiments where people assessed uncertain events in domains they knew well, such as the outcome of a football match or future temperatures. When people evaluated the probability of each possible outcome one at a time, the probabilities summed to more than 100%. This subadditivity was stronger for uncertain events (where probabilities were unknown) than for risky events (where probabilities were stated explicitly), suggesting that vagueness amplifies the distortion.


**Ambiguity aversion.** People prefer known risks over unknown risks, even when the expected values are identical. @ellsberg1961 demonstrated this with a thought experiment involving two urns. One urn contains 50 red balls and 50 black balls (a known risk). The other contains 100 balls, but the proportion of red to black is unknown (an ambiguous risk). When asked which urn they would rather bet on, most people prefer the urn with the known distribution, regardless of which color they are betting on. This preference cannot be explained by any consistent assignment of probabilities to the unknown urn: if you thought the unknown urn favored red, you should bet on it for red, and if you thought it favored black, you should bet on it for black. Yet people avoid the unknown urn for both bets, which means no coherent probability estimate is driving their choice. Under expected utility theory, a decision-maker who assigns *any* probability distribution to the unknown urn should not systematically avoid it. The preference reflects discomfort with not knowing the probabilities — a feeling of uncertainty about uncertainty. Ambiguity aversion helps explain real-world behavior such as the preference for familiar investments over foreign ones, or the tendency to buy insurance against well-defined risks while ignoring vaguely understood threats.


**Probability neglect.** In emotionally charged situations, people may almost entirely ignore probabilities and respond instead to the vividness or severity of the outcome. @baron_etal1993 studied this in experiments where participants evaluated risks such as exposure to a toxic chemical. Participants were told the probability of harm varied — from very small to moderate — but their judgments of how much they would pay to avoid the exposure were barely affected by these differences in probability. What drove their responses was the nature of the outcome itself: how frightening or aversive the harm sounded. When the outcome is vivid enough, probability fades into the background. This is related to the affect heuristic discussed in [the chapter on heuristics and biases](#heuristics-and-biases): when emotions run high, the emotional intensity of an outcome dominates the judgment, and the actual likelihood becomes almost irrelevant.


## Action, Omission, and the Source of Harm


Beyond the mechanisms captured by prospect theory and the distortions of probability just described, several additional biases shape how people evaluate risky outcomes based on the nature of the risk and whether harm results from action or inaction.


**Omission bias.** People tend to judge harmful consequences of inaction as less bad than equivalent harmful consequences of action. @baron_ritov2004 studied this extensively in the context of vaccination decisions. When a vaccine carries a small risk of serious side effects, some parents refuse to vaccinate their child, even when the disease itself poses a larger risk. The harm caused by vaccinating (an action) feels worse than the equal or greater harm caused by not vaccinating (an omission), because action is perceived as a more direct cause. This bias persists even when participants are explicitly told that the risks of inaction are greater than the risks of action. Omission bias is related to themes discussed in [the chapter on morality](#morality), where the distinction between action and inaction plays a central role in moral judgment, as in the trolley problem.


**Nature bias.** People tend to judge harms from artificial causes as worse than equivalent harms from natural causes [@kahneman_ritov1994]. For example, a synthetic chemical additive in food may be judged as more dangerous than a naturally occurring toxin at the same level of objective risk. This bias influences consumer behavior (preferences for "natural" products), environmental policy (stricter regulation of synthetic chemicals than naturally occurring ones), and medical decisions (skepticism toward synthetic medications compared to herbal remedies). One possible explanation is that people apply something like an intentional stance to artificial products — as if someone chose to introduce the harm — whereas natural harms are attributed to impersonal forces. This may connect to ideas about the intentional stance discussed in [the chapter on mental models](#mental-models), though the link remains speculative.


## A Bayesian Lens


Throughout this book, we use the framework of Bayesian reasoning as a benchmark for rational belief updating. In decision contexts, the complementary benchmark is expected utility theory: use probabilities coherently, combine them with explicit tradeoffs among outcomes, and remain consistent regardless of how a problem is described. Prospect theory documents a series of systematic departures from both of these ideals.


The probability weighting function means that people do not use probabilities as stated. Small probabilities are inflated and moderate probabilities are deflated, producing a distorted version of the likelihood information that a Bayesian agent would use faithfully. Subadditivity compounds this by making individual event assessments add up to more than the whole. Ambiguity aversion means that the confidence in one's probability estimates affects choices in ways that neither Bayesian updating nor expected utility theory would predict, since a rational agent should simply work with whatever probability distribution is available. And probability neglect means that in emotional situations, probability information may be discarded entirely — the opposite of what any normative framework requires.


On the outcome side, framing effects mean that logically equivalent descriptions can produce different decisions. A rational decision-maker should be indifferent to whether a medical treatment is described as having a 90% survival rate or a 10% mortality rate, because these carry the same information. But as we have seen, people are not indifferent to such reframings. The reference point determines what counts as a gain or a loss, and shifts in this reference point — whether caused by the wording of a question, recent experiences, or the set of available alternatives — reshape the entire evaluation. This is a direct violation of description invariance, the principle that equivalent representations of the same problem should lead to the same choice.


## Summary


This chapter traced the development from expected value theory through expected utility theory to prospect theory, showing why each step was necessary to explain how people actually make decisions under risk. Prospect theory, developed by Kahneman and Tversky, describes decisions through two components. The value function captures how people evaluate outcomes as gains or losses relative to a reference point, with losses looming about twice as large as equivalent gains, and with diminishing sensitivity to larger amounts. The probability weighting function captures how people transform probabilities into decision weights, overweighting small probabilities and underweighting moderate-to-high ones. Together, these components explain a wide range of phenomena: the certainty effect, framing effects, the endowment effect, and the fourfold pattern of risk attitudes. Beyond prospect theory, people also show subadditivity in probability judgments, aversion to ambiguous risks, and neglect of probabilities when emotions are strong. Additional biases favor inaction over action and natural over artificial causes when evaluating harm. From a Bayesian and expected-utility perspective, these patterns represent systematic distortions in both how probabilities are used and how outcomes are evaluated — departures that have real consequences for decisions in medicine, policy, and everyday life.