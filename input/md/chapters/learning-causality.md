# Learning Causality

Learning goals:

- Explain how a 2 × 2 contingency table summarizes the co-occurrence of two factors, and describe the cell A bias.
- Describe how classical and operant conditioning serve as forms of causal learning.
- Explain prediction error as the mechanism that drives learning, and describe how dopamine neurons encode prediction errors.
- Define blocking and explain why it occurs in predictive but not diagnostic learning.
- Distinguish between illusory correlation and illusory causation, and explain how both arise from biased evidence use.
- Explain regression toward the mean and why people tend to misinterpret it as a causal effect.
- Describe how the plausibility of a cause functions as a prior belief that shapes how people evaluate new evidence.
- Explain why only experimental designs allow causal conclusions.

## Learning from Co-Occurrence

Imagine you start taking a new herbal supplement because a friend told you it helps with concentration. Over the next few weeks, you notice that on several days when you take the supplement, you do seem to focus well during lectures. After a while, you become convinced: the supplement works. But did you ever pay attention to the days when you took it and still could not focus? Or the days when you skipped it but concentrated just fine? Probably not. This chapter is about how people learn causal relationships from experience, and about the systematic errors that creep in along the way. These errors help explain why people believe in ineffective treatments and see patterns in randomness. But the story is not all negative. The basic mechanism that drives causal learning — prediction error — is remarkably efficient, and in some ways it mirrors the kind of rational updating described in [Bayesian Reasoning](#bayesian-reasoning).

To understand how people learn about causes and effects, we first need a simple framework for organizing evidence. When you want to know whether one thing causes another — say, whether a supplement improves concentration — there are four possible combinations of events. The supplement is present or absent, and good concentration is present or absent. These four combinations can be arranged in a 2 × 2 contingency table:

|                          | **Effect present** | **Effect absent** |
|--------------------------|--------------------|-------------------|
| **Cause present**        | Cell A             | Cell B            |
| **Cause absent**         | Cell C             | Cell D            |

Cell A contains cases where you took the supplement and concentrated well. Cell B contains cases where you took the supplement but could not focus. Cell C contains cases where you skipped the supplement and concentrated well. Cell D contains cases where you skipped the supplement and could not focus.

A rational agent who wants to determine whether the supplement actually causes better concentration would need to consider all four cells. The standard measure of contingency, ΔP, captures this:

> ΔP = P(effect | cause) − P(effect | no cause) = A/(A+B) − C/(C+D)

If ΔP is zero, the supplement does nothing: you concentrate well at the same rate whether you take it or not. If ΔP is positive, the supplement is associated with better concentration. Importantly, even a positive ΔP from observational data does not prove causation, because other factors might explain the link. Only experimental manipulation — randomly assigning people to take the supplement or a placebo while holding everything else constant — can justify a causal conclusion. We return to this point in detail later in the chapter.

But people do not treat all four cells equally. Research consistently shows that people give the most weight to cell A, followed by cell B, then cell C, and finally cell D [@lipe1990]. This ordering matters. Underweighting cell C is especially damaging, because cell C contains cases where the effect occurs *without* the cause. If you never notice the days when you concentrate well without the supplement, you will overestimate the supplement's importance. When the task becomes difficult or people simplify, they sometimes attend only to cell A — the cases where both the cause and the effect are present. At its extreme, this becomes a purely confirmatory approach: you look only at cases consistent with the idea that the cause produces the effect, and you ignore everything else. As we discuss in [Confirmation](#confirmation), this tendency to focus on confirming evidence appears throughout human reasoning, not just in causal learning.

Notice that the cell A bias operates not only at the stage of judgment but also at the stage of evidence gathering. If someone only asks users of the supplement whether their concentration improved, they collect mostly cell A and cell B cases, and never observe cells C and D at all. A journalist who interviews only people who took a remedy and felt better is sampling exclusively from cell A.

@lipe1990 conducted a meta-analysis of published studies on covariation judgment, using a lens model framework to examine how people weight the four cells. Across 34 data points drawn from six studies, she found that all four cells did influence people's judgments to some degree. A linear model of these judgments explained 74% of the variance, and when judgments were aggregated across participants, they correlated reasonably well with the actual statistical relationship between the two factors. At the individual level, however, judgments were considerably noisier and matched normative statistics less well. The overall picture is that people can use all four cells when the data are clearly presented, but they give disproportionate weight to confirming co-occurrences.

## Conditioning and Causal Learning

Where does our ability to learn about causes come from? At the most basic level, causal learning rests on association. When two events repeatedly occur together, we come to expect one when we observe the other. This process is called classical conditioning. The classic example is from Pavlov's experiments: a dog hears a bell just before receiving food. After many pairings, the bell alone triggers salivation. The dog has learned that the bell predicts food.

In operant conditioning, the association is between an action and its outcome. A rat presses a lever and receives a food pellet. Over time, the rat learns that pressing the lever causes food to appear.

Both classical and operant conditioning provide a foundation for causal learning, but human causal reasoning goes beyond simple association. People also draw on background knowledge, causal models, and plausibility judgments — topics we return to later in this chapter. Still, the core associative machinery is shared across species and remains central to how humans learn from experience. When you notice that eating a particular food is followed by feeling unwell, you develop an aversion to that food. When you notice that studying in a particular café seems to lead to productive sessions, you start going there more often. These are causal beliefs built from repeated experience, and they follow many of the same principles that govern conditioning in the laboratory.

## Prediction Error

What makes conditioning work? Early theories assumed that simple repetition was enough: the more often two events co-occur, the stronger the association. But this turns out to be wrong. What really drives learning is surprise — or more precisely, prediction error, the difference between what you expected and what actually happened.

@schultz_etal1997 provided some of the most striking evidence for this idea by recording the activity of dopamine neurons in monkey brains. When a monkey received an unexpected reward, such as a squirt of juice, dopamine neurons fired vigorously. But after the monkey learned that a particular cue (say, a light) predicted the juice, the pattern changed. The dopamine response shifted from the reward itself to the cue that predicted it. The light now triggered the dopamine burst, while the juice itself — now fully expected — no longer did. If the cue appeared but the expected reward was omitted, dopamine activity dropped below its baseline level. The neurons were not simply responding to good things happening; they were signaling the difference between what was expected and what occurred.

In computational terms, the dopamine signal acts like a prediction error: positive when outcomes are better than expected, zero when outcomes match expectations, and negative when outcomes are worse than expected. Learning occurs when outcomes are surprising. Once a cue perfectly predicts an outcome, the prediction error signal falls silent and learning stops. This is why you stop noticing the hum of your refrigerator: it is perfectly predictable and carries no new information.

## Blocking

Prediction error has a powerful consequence for how we assign credit to potential causes. Suppose you already know that cue A perfectly predicts an outcome. Now cue A and a new cue B are presented together, and the outcome occurs. Do you learn anything about cue B? Because cue A already fully accounts for the outcome, there is no surprise when it occurs — and therefore no prediction error to drive learning about cue B. Cue A "blocks" learning about cue B.

Blocking was first demonstrated in animal conditioning experiments and has since been replicated in human learning tasks. It shows that people assign causal credit selectively, based on what is informative, rather than associating everything present with the outcome. In idealized predictive settings, blocking is rational: once a cue explains the outcome, a redundant cue provides no additional evidence and should receive no weight.

Blocking is also where simple associative theories and causal-model theories diverge, because it turns out that blocking depends on the direction of the causal relationship.

## Predictive versus Diagnostic Learning

If causal learning were simply a matter of forming associations between events that co-occur, the direction of the association should not matter. Learning that a cause predicts an effect should be the same as learning that an effect indicates a cause, as long as the data are the same. @waldmann_holyoak1992 showed that this is not the case.

In their experiments, participants learned about relationships between cues and outcomes. In the predictive condition, cues were described as causes that produced effects. For example, participants learned that certain features of chemical compounds caused particular emotional responses in workers. In the diagnostic condition, the same data were presented in reverse: symptoms were described as effects of a disease, and participants had to learn which symptoms indicated which disease. The critical finding was that blocking occurred only in the predictive condition. When cues were causes, a previously established cause blocked learning about a new, redundant one. But when cues were effects of a common cause, no blocking occurred. Multiple symptoms of the same disease did not compete with each other.

The logic is straightforward. If you already know that substance A causes a headache, then learning that substance A plus substance B also causes a headache gives you no reason to think substance B does anything. Causes compete for credit. But if you know that a disease causes symptom A, learning that it also causes symptom B does not reduce the diagnostic value of symptom A. Effects of a common cause can coexist without competing.

The key lesson is that causal learning depends on more than simple co-occurrence. People build mental models of the causal structure of a situation, and these models determine how evidence is processed. The same data lead to different learning outcomes depending on whether the learner interprets them as going from causes to effects or from effects to causes. This is consistent with the broader role of background knowledge in shaping interpretation, discussed in [Mental Models](#mental-models).

## Illusory Correlations

The cell A bias has a predictable downstream consequence: people sometimes perceive correlations that do not actually exist. When you selectively attend to cases where two things occur together (cell A) and ignore the other cells, you can come to believe that two unrelated things are associated. This is called illusory correlation.

Consider a common example. Many people believe there is a strong link between the political party in power and the state of the economy. When your preferred party is in power and the economy does well, you notice it and remember it (cell A). When your preferred party is in power and the economy does poorly, you are more likely to explain it away or forget it (cell B). When the other party is in power and the economy does well, you may not pay much attention (cell C). And when the other party is in power and the economy struggles, you notice it, but mainly as confirmation that the other party is bad — not as relevant evidence for the full contingency table. The result is an inflated perception of the relationship between party and economic performance.

Illusory correlations also play a role in stereotyping. When a minority group is small (making encounters less frequent) and a behavior is rare (making instances memorable), the co-occurrence of the two becomes especially salient. This can create the impression of an association between the group and the behavior, even when none exists — a point we revisit in [Representativeness](#representativeness).

## Illusory Causation and Quackery

Illusory correlation concerns perceived association. Illusory causation adds a further inference: that the association reflects a genuine causal effect. While illusory correlation means seeing a link that is not there, illusory causation means interpreting a real but non-causal correlation as evidence that one thing produces another. This additional step — from "these things go together" to "this thing causes that thing" — is the cognitive mechanism behind much of quackery and pseudoscience.

@matute_etal2011 demonstrated this in an elegant experiment. Participants were shown records of 100 fictional patients suffering from a made-up disease. Eighty percent of these patients recovered, regardless of whether they took a particular fictional medicine. The medicine had no causal effect whatsoever; the recovery rate was the same with or without it. Despite this, participants judged the medicine to be effective.

The key manipulation was the proportion of patients who took the medicine. In the high-exposure condition, 80 out of 100 patients took it. In the low-exposure condition, only 20 out of 100 took it. When 80 patients took the medicine, about 64 of them recovered (80% of 80) — a lot of cases in cell A. In the low-exposure condition, only about 16 patients fell in cell A (80% of 20). Even though the recovery rate was identical regardless of treatment, participants in the high-exposure condition rated the medicine as more effective. The sheer number of confirming cases in cell A drove their causal judgment.

This finding explains why so many ineffective treatments are perceived as working. Most illnesses resolve on their own. If you take a remedy and get better (cell A), you credit the remedy. But you rarely think about what would have happened without it (cells C and D). And when many people take a remedy — as happens when something is popular or heavily marketed — cell A fills up with apparent successes, even if the remedy does nothing. Without considering how many people recover without the treatment, you cannot know whether the treatment added anything. In Bayesian terms, this is base-rate neglect: ignoring the prior probability of recovery, P(recovery), which equals the recovery rate regardless of treatment. The same type of error appears in other contexts, as discussed in [Bayesian Reasoning](#bayesian-reasoning) and [Representativeness](#representativeness).

@matute_etal2011 also found that the wording of the question mattered. Participants who were asked whether the medicine *caused* the recovery gave lower ratings than those asked whether the medicine was *effective*. Simply framing the question in causal terms prompted more careful evaluation of the evidence.

## Regression toward the Mean

Another common source of illusory causal beliefs is regression toward the mean. Any single measurement reflects both a true underlying value and random variation — noise. When random variation pushes a measurement to an extreme, it is unlikely that the next measurement will be pushed to the same extreme by chance. The result is that extreme measurements tend to be followed by less extreme ones.

Consider blood pressure. A patient visits the doctor on a particularly stressful day and records an unusually high reading of 155/95. The doctor prescribes a new medication. At the follow-up visit two weeks later, the reading is 138/88. The doctor concludes the medication is working. But some of that drop was inevitable: the first reading was extreme partly because of random factors (stress that day, rushing to the appointment, the "white coat" effect), and those factors were unlikely to all align again. The blood pressure would have decreased somewhat even without the medication.

Or consider the "commentator's curse" in sports. A television commentator praises a footballer for an extraordinary run of five goals in three matches. The next two matches, the player scores nothing. Fans joke that the commentator jinxed the player, but regression toward the mean predicts exactly this: an extreme streak is partly due to luck — favorable matchups, defenders' mistakes, shots that happened to find the corner — and luck is unlikely to repeat.

A classic example involves training. An instructor notices that trainees who perform exceptionally well on one trial tend to perform worse on the next, while trainees who perform poorly tend to improve. The instructor concludes that praise is harmful and criticism is helpful. But regression toward the mean predicts this pattern regardless of whether the instructor says anything. Extreme performances on one trial are partly due to chance, and chance is unlikely to repeat.

This kind of causal misinterpretation is pervasive. It affects how people evaluate medical treatments (symptoms at their worst tend to improve), educational interventions (students who score at the bottom tend to score higher next time), and personnel decisions (employees who have a great first year may have a more ordinary second year). In each case, the natural tendency is to construct a causal story for what is fundamentally a statistical regularity.

## Plausibility Shapes Learning

Not all potential causes are treated equally. When you already believe that a cause is plausible, you give more weight to evidence that supports the link. When you believe a cause is implausible, you are more skeptical of the same evidence. A vitamin causing improved concentration seems more plausible than a sticker on a laptop causing improved concentration. That difference in plausibility changes how you process exactly the same data.

@fugelsang_thompson2003 tested this by having participants evaluate unfamiliar causal candidates — for example, whether a fictional substance caused a particular outcome. Before seeing any data, participants received information designed to make the cause seem either plausible or implausible. Some received information about a plausible causal mechanism (how the substance could produce the effect), while others received information about past statistical co-occurrence (how often the substance and effect had been observed together). Participants then saw new data — a set of contingency tables — and rated how strongly they believed the cause produced the effect.

In these experiments, when participants believed the cause was plausible based on mechanism knowledge, they weighted the new evidence more heavily. The same data had a bigger effect on their judgments when they already found the cause mechanistically plausible. This interaction was specific to mechanism-based beliefs; when plausibility was based on past co-occurrence, it did not modulate how new evidence was weighted. The researchers also found that participants were relatively unaware of the influence their prior beliefs had on their judgments. They could report how much they used the new data, but they underestimated the role of their existing beliefs.

@goedert_etal2014 extended this line of research by examining how plausibility affects which evidence people seek out. In their experiments, participants chose whether to observe cases where the potential cause was present or absent. When the cause was plausible, participants showed a strong preference for observing cause-present cases: they wanted to see whether the cause was followed by the effect. This is the positive test strategy discussed in [Confirmation](#confirmation). But when the cause was implausible, this preference weakened. Participants were more willing to look at cause-absent cases, effectively checking whether the effect occurred even without the supposed cause. Implausibility nudged people toward a more balanced evidence search.

These findings illustrate that plausibility functions as a prior belief. A plausible cause starts with a higher prior, and confirming evidence reinforces it. An implausible cause starts with a lower prior, and the same evidence has less impact. When prior beliefs are well calibrated, giving more weight to evidence for plausible causes and less weight to evidence for implausible causes is a sensible strategy. The danger arises when prior beliefs are poorly calibrated — because then plausibility can prevent you from learning about genuine causal relationships that happen to seem unlikely, or cause you to accept false causal claims that happen to seem plausible.

## The Need for Experiments

Given all the ways in which observational evidence can mislead, how can we ever be confident that one thing causes another? As noted at the start of this chapter, the answer is experimental design. In a true experiment, the researcher manipulates the potential cause (the independent variable) while holding everything else constant. Participants are randomly assigned to conditions, which makes the groups comparable on average and reduces confounding, so that any systematic differences in outcomes can be attributed to the manipulation.

Consider the supplement example from the opening. In everyday life, you take the supplement on days when you feel motivated enough to remember it, skip it on lazy days, and judge your concentration based on your subjective impression. There are countless confounds: maybe you take the supplement on days when you slept better, or when you have more interesting lectures. A proper experiment would randomly assign people to take the supplement or a placebo on different days, measure their concentration with a standardized task, and compare the two conditions.

This is the fundamental distinction between correlational and experimental evidence. Observational covariation — the kind of evidence that fills up the contingency table in everyday life — is exactly what fuels illusory correlations and illusory causation. You observe that two things tend to go together, but without intervention you cannot discriminate between a direct causal effect, a reverse causal relationship, or a common cause driving both. Experimental manipulation breaks this ambiguity. It is the reason why medical treatments should be evaluated in randomized controlled trials rather than through testimonials, and why educational interventions need proper control groups.

This principle is easy to state but surprisingly difficult to internalize. As this chapter has shown, observation-based associative learning can produce causal beliefs even when causation is absent. The human mind is naturally inclined to draw causal conclusions from correlational patterns. Recognizing this limitation is the first step toward better causal reasoning.

## A Bayesian Lens

Each of the errors discussed in this chapter can be understood as a specific departure from Bayesian updating. The cell A bias is a form of overweighting confirming evidence: instead of using all four cells to compute ΔP, people disproportionately attend to cases where both cause and effect are present. Illusory causation, as demonstrated by @matute_etal2011, reflects base-rate neglect: people judge a treatment as effective without considering the probability of recovery in the absence of treatment. Misinterpreting regression toward the mean is a failure to account for noise: people treat random fluctuations as meaningful signals that demand causal explanations.

But several features of causal learning are strikingly Bayesian. Prediction error drives learning precisely when outcomes are surprising — corresponding to updating beliefs in proportion to the likelihood ratio of new evidence. When an outcome is fully expected, the likelihood ratio is close to one, and there is nothing to update. Blocking follows the same logic: once a cue explains the outcome, a redundant cue provides no additional evidence and correctly receives no credit. And plausibility mirrors the role of priors in Bayesian reasoning — a plausible cause starts with a higher prior and is updated more readily, while an implausible cause starts with a lower prior and requires stronger evidence to shift beliefs. As long as priors are well calibrated, this is exactly what a rational agent should do. The challenge, as always, is that human priors are not always well calibrated, and the evidence people attend to is not always complete.

## Summary

**How causal learning works.** People learn about causal relationships through association, building on the same mechanisms that underlie classical and operant conditioning. The driving force is prediction error: the brain updates its causal models when outcomes are surprising and stops learning when outcomes are fully expected. Blocking demonstrates this — a well-established cause prevents learning about a redundant new cause. Causal learning also depends on the direction of the causal model: blocking occurs when cues are interpreted as causes but not when they are interpreted as effects, showing that people build structured causal models rather than forming simple associations.

**Where causal learning goes wrong.** The cell A bias leads people to overweight cases where a cause and effect co-occur, producing illusory correlations and illusory causal beliefs. This is especially dangerous in the context of ineffective treatments, where high exposure creates many apparent successes in cell A while the base rate of recovery is ignored. Regression toward the mean is another source of false causal beliefs, as people construct causal stories for what is really a statistical regularity.

**How prior beliefs shape learning.** Plausibility functions as a prior: plausible causes receive more weight from new evidence, while implausible causes receive less. When priors are well calibrated, this is rational; when they are not, it can entrench false beliefs or block genuine discoveries.

**Why experiments matter.** Only experimental designs that manipulate the potential cause while holding everything else constant can distinguish genuine causal relationships from mere correlations. Observational evidence fills the contingency table but cannot rule out reverse causation or common causes.