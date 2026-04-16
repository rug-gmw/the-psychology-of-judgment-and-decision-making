## Overall assessment

This is a strong draft: clear, readable, and mostly faithful to the outline. It explains the core logic of prospect theory well and uses good motivating examples. The main revisions I’d recommend are:

- tighten a few transitions and reduce some repetition,
- add one or two more concrete examples/studies where the discussion becomes general,
- be careful not to overstate some quantitative claims,
- bring the chapter closer to the outline’s specific framing of the Bayesian contrast and the “average of alternatives” reference point,
- check cross-links, since several appear to point to chapter titles that may not correspond to final heading IDs.

Below I organize feedback by the six requested criteria.

---

## 1. Structure

### 1.1 Strong overall flow, but one section break is slightly abrupt

The sequence

> “From Expected Value to Expected Utility”  
> “Prospect Theory”  
> “The Value Function”  
> “Framing Effects”  
> “The Endowment Effect”  
> “The Probability Weighting Function”  
> “Beyond the Weighting Function”  
> “Biases in Risky Choice”  
> “A Bayesian Lens”

is logical and easy to follow.

However, the move from **The Value Function** to **Framing Effects** is somewhat redundant structurally, because framing is already introduced as a consequence of reference dependence. You could improve flow by signaling more explicitly that the next two sections are applications of the value function.

For example, after:

> “There is a second kind of reference dependence that reinforces loss aversion.”

add a bridge such as: *“These properties are not merely theoretical; they produce several characteristic patterns in risky choice, including framing effects and the endowment effect.”*

That would mirror the outline more closely, which presents those as consequences of the value function.

---

### 1.2 “Beyond the Weighting Function” and “Biases in Risky Choice” are somewhat uneven in scope

The section:

> “## Beyond the Weighting Function”

contains three probability-related phenomena: subadditivity, ambiguity aversion, and probability neglect.

Then:

> “## Biases in Risky Choice”

contains omission bias and nature bias.

This division makes sense, but the title “Biases in Risky Choice” is too broad, since all the preceding sections are also about biases in risky choice. Consider renaming it to something narrower, such as:

- **Action, Omission, and the Source of Harm**
- **Additional Evaluative Biases**
- **Action/Inaction and Natural/Artificial Harms**

That would better reflect the content and avoid the feeling that the chapter has started over under a vaguer heading.

---

### 1.3 The “Bayesian Lens” comes a little late and is slightly detached

The final section works, but it feels somewhat appended rather than integrated. The outline frames Bayesian reasoning as the normative standard *throughout the book*, and this chapter would benefit from a lighter earlier signal that expected value/utility are not the same as Bayesian reasoning, even though they are all normative tools.

For instance, in the first section, after introducing expected value and expected utility, you could add one sentence clarifying that these are **decision** benchmarks, while Bayesian reasoning is primarily a benchmark for **belief updating**. That would reduce potential conceptual slippage later when you write:

> “A Bayesian agent updates beliefs by combining prior probabilities with new evidence, using the probabilities directly and evaluating outcomes in terms of their objective values.”

As written, this risks conflating Bayesian belief updating with utility-free choice.

---

## 2. Duplication

### 2.1 Repetition of “prospect theory is descriptive, not normative”

This point appears several times in slightly different forms:

> “Expected utility theory works well as a normative model…”  
> “Prospect theory is a descriptive model…”  
> “Understanding why people make choices like these requires a different kind of theory…”  
> “Prospect theory describes a series of systematic departures from this ideal.”

The distinction is important, but the current draft repeats it more often than necessary. I’d compress the explicit normative/descriptive contrast after the first two mentions, then let the rest of the chapter illustrate it.

---

### 2.2 Repetition of the core claim about framing

You state versions of the same point in multiple places:

> “People evaluate outcomes as gains or losses relative to a reference point.”

> “Because people evaluate outcomes relative to a reference point, the way a problem is described…”

> “The reference point determines what counts as a gain or a loss…”

This is the conceptual core of the chapter, so some repetition is unavoidable. Still, a few sentences could be trimmed, especially in the summary and Bayesian lens, where the point is restated almost verbatim.

---

### 2.3 Repetition around “small probabilities”

There are three nearby claims:

> “Small probabilities are overweighted…”

> “Very small probabilities… are often rounded down to zero entirely.”

> “Probability neglect… people may almost entirely ignore probabilities…”

These are not the same phenomenon, but the draft could make the distinctions sharper to avoid sounding repetitive or contradictory. Right now the reader may wonder: *Do people overweight tiny probabilities or ignore them?*

You partly address this, but I’d make it more explicit. For example:

- **overweighting** applies to small, cognitively salient probabilities,
- **rounding to zero** applies when probabilities are too remote to feel real,
- **probability neglect** applies in affect-rich contexts where outcome vividness dominates.

A short comparative sentence would help.

---

## 3. Concreteness

### 3.1 Good use of examples overall

The found/lost €20 opening, Olympic medalists, Asian disease problem, mug experiment, and Ellsberg urn are all effective.

---

### 3.2 “Second kind of reference dependence” is too abstract and may need either an example or trimming

This passage is the most abstract in the chapter:

> “There is a second kind of reference dependence that reinforces loss aversion. People evaluate outcomes not only against a fixed reference point like their current state, but also relative to the alternatives that were available. If you are choosing between two gambles, the average of all possible outcomes serves as an implicit reference. Outcomes below this average produce regret; outcomes above it produce relief or joy.”

This needs either:
1. a concrete worked example, or
2. substantial simplification.

As written, “the average of all possible outcomes serves as an implicit reference” is too technical and underexplained. It also risks sounding like a settled part of prospect theory proper, when it is closer to regret/counterfactual comparison logic than to the standard canonical presentation.

A concrete example would help, e.g., choosing between two job offers and feeling regret because the chosen one pays less than the forgone alternative. Without such an example, this paragraph feels conceptually dense relative to the rest of the chapter.

---

### 3.3 Subadditivity could use a simpler example

This passage is accurate but abstract:

> “When people judge the probability of a combined event (the probability of A or B occurring), they tend to assign it a lower value than the sum of the individual probabilities they would assign to A and B separately…”

Consider adding a simple everyday illustration, such as:
- estimating the probability that a candidate loses due to the economy, scandal, or foreign policy, where separately judged causes sum to more than the judged overall probability of losing;
- or travel delays from weather, traffic, and mechanical problems.

That would make “the parts seem to add up to more than the whole” easier to grasp.

---

### 3.4 Probability neglect would benefit from a named study or more specific paradigm

You write:

> “If someone describes a terrifying but extremely unlikely event, such as a chemical plant explosion, people may react primarily to the horror of the outcome rather than to its probability.”

This is understandable, but it would be stronger with a more concrete experimental setup. For instance, briefly describe participants evaluating willingness to pay to prevent an electric shock, cancer, or a toxic exposure at different probabilities, yet showing weak sensitivity to those probabilities. Right now the example is vivid but generic.

---

### 3.5 Nature bias section needs a clearer example or study detail

This section is the least concrete:

> “People tend to judge harms from artificial causes as worse than equivalent harms from natural causes [@kahneman_ritov1994].”

Then:

> “A chemical additive in food that causes one illness per million consumers may be judged as more dangerous than a naturally occurring toxin with the same risk.”

The example is plausible, but it reads as invented rather than clearly tied to evidence. If there is a specific paradigm in the cited work, describe it briefly. If not, use a more cautious formulation like “for example” and avoid implying that this exact comparison was tested.

---

## 4. Accuracy

### 4.1 Mostly faithful to the chapter outline

The draft covers all major outline items:

- expected value and expected utility,
- Allais paradox and certainty effect,
- value function,
- reference dependence,
- loss aversion,
- diminishing sensitivity,
- Asian disease framing,
- endowment effect,
- probability weighting,
- ambiguity aversion,
- subadditivity,
- probability neglect,
- omission bias,
- nature bias,
- Bayesian contrast.

So in terms of coverage, it is largely complete.

---

### 4.2 Be careful with “Expected value theory says you should prefer this gamble over any sure amount less than €100”

You write:

> “Expected value theory says you should prefer this gamble over any sure amount less than €100.”

This is acceptable as a simplified statement, but as a normative claim it is only true under an expected-value criterion and risk neutrality. Since the next paragraph introduces expected utility, readers may incorrectly infer that EV is the general normative standard for risky choice. Consider softening:

- “Under a pure expected-value criterion, you should prefer…”
- or “If only expected monetary value mattered…”

That would preserve the pedagogical point while avoiding overstatement.

---

### 4.3 “Losses feel roughly 2.25 times as painful” is too precise as a general fact

You write:

> “Losses feel roughly 2.25 times as painful as equivalent gains feel pleasant.”

The outline gives “~2.25×,” but in textbook prose this level of precision can sound stronger than the evidence warrants. The exact coefficient varies by study, domain, elicitation method, and has been debated. Better:

- “Losses often loom about twice as large as gains”
- or “A common estimate is around two-to-one”

This would be more cautious and more in line with current teaching practice.

---

### 4.4 The treatment of “second kind of reference dependence” may blur prospect theory with regret-based models

The outline includes:

> “People evaluate outcomes not only against a fixed reference point, but also relative to the alternatives: the average of all possible outcomes serves as an implicit reference.”

Your draft renders this as:

> “If you are choosing between two gambles, the average of all possible outcomes serves as an implicit reference.”

This is faithful to the outline, but conceptually it is not standard textbook prospect theory. Because of that, the reader may wrongly think this is part of the canonical Kahneman-Tversky formulation. You should either:
- flag it as a related extension, or
- integrate it more carefully as “a related idea in later work on regret and counterfactual comparison.”

As written, it sounds more established and central than it is.

---

### 4.5 “A Bayesian agent… evaluates outcomes in terms of their objective values” is too strong

You write:

> “A Bayesian agent updates beliefs by combining prior probabilities with new evidence, using the probabilities directly and evaluating outcomes in terms of their objective values.”

Bayesian reasoning governs belief updating; decision-making under a Bayesian framework typically also requires a utility or loss function. So “objective values” is misleading. A Bayesian decision-maker can have subjective utilities. The key contrast here is not objective values versus subjective values, but:
- coherent probability use,
- invariance under equivalent descriptions,
- and explicit utility/loss tradeoffs.

I would revise this passage substantially.

---

### 4.6 “Direct violation of Bayesian invariance” is somewhat imprecise

You write:

> “Framing effects mean the same evidence produces different decisions depending on presentation — a direct violation of Bayesian invariance.”

This is a useful teaching contrast, but “Bayesian invariance” is not the clearest label for the principle at stake. The issue is more broadly **description invariance** or **extensionality**: equivalent representations should not change rational judgment/choice. If you want to keep the Bayesian framing, define the principle more carefully.

---

### 4.7 Missing explicit mention of ambiguity aversion in relation to expected value

The outline says:

> “Known risks are preferred over equivalent unknown risks, even at identical expected values.”

Your draft explains ambiguity aversion well, but it would help to state more explicitly that the preference persists even when the person can make no consistent expected-value or expected-utility account of their choices. Right now that implication is present, but only indirectly:

> “This preference cannot be explained by any consistent assignment of probabilities…”

A clearer sentence tying it back to normative benchmarks would help.

---

## 5. Style

### 5.1 Overall style is plain and consistent

The prose is generally strong: direct, accessible, and appropriate for a textbook.

---

### 5.2 A few sentences are too padded

Example:

> “Understanding why people make choices like these requires a different kind of theory, one that describes how people actually evaluate risky options rather than how they should. That theory is prospect theory.”

This is not wrong, but it is a bit theatrical and could be tighter:

- “To explain this pattern, Kahneman and Tversky proposed prospect theory, a descriptive model of risky choice.”

Similarly:

> “This pattern makes no sense if happiness depends on the objective outcome: silver is objectively better than bronze.”

Could be tighter:

- “If reactions depended only on objective rank, silver should look better than bronze.”

---

### 5.3 Watch mixed terminology around “value,” “utility,” and “objective value”

The chapter uses:
- “value” in expected value,
- “subjective utilities” in expected utility,
- “value function” in prospect theory,
- “objective values” in the Bayesian section.

This can be confusing for students. I would recommend tightening terms:

- **monetary outcome** for EV,
- **utility** for EU,
- **subjective value** for prospect theory’s value function.

Avoid “objective value” unless you define it carefully.

---

### 5.4 A few places use unnecessary fillers

Examples:
- “The idea is that…”
- “This happens because…”
- “One such departure is…”
- “A second departure is…”
- “A third departure is…”

These are functional, but repeated often. Varying sentence openings slightly would make the chapter smoother.

---

### 5.5 “smallish probabilities” from the outline has wisely been replaced

Good choice not to use the outline’s “smallish probabilities,” which would sound informal and imprecise in a textbook.

---

## 6. Cross-links

### 6.1 Cross-links are conceptually appropriate, but formatting/targets may be unreliable

You use links such as:

> “[the chapter on the future self](#the-future-self)”  
> “[the chapter on medical decision-making](#medical-decision-making)”  
> “[the chapter on steering other people's choices](#steering-other-peoples-choices)”  
> “[the chapter on risk perception](#risk-perception)”  
> “[the chapter on heuristics and biases](#heuristics-and-biases)”  
> “[the chapter on morality](#morality)”  
> “[the chapter on mental models](#mental-models)”

Conceptually these are good. The concern is technical consistency:

- If each chapter is a separate file, `#the-future-self` will not work unless this is a single-page book build.
- Apostrophes in heading IDs are handled differently across markdown systems.  
  `#steering-other-peoples-choices` may or may not be the actual generated anchor.
- “the chapter on heuristics and biases” may not match the actual chapter title if that title is in a different part/section hierarchy.

If this project uses Quarto/Pandoc, I’d recommend explicit identifiers in source headings and cross-links using those identifiers rather than auto-generated anchors.

---

### 6.2 One cross-link feels slightly weak conceptually

This sentence:

> “The bias may stem from the application of an intentional stance to artificial products, as if someone intended the harm, whereas natural harms are attributed to impersonal forces. This connects to ideas about the intentional stance discussed in [the chapter on mental models](#mental-models).”

This is interesting, but speculative. If you keep it, I’d soften the wording:

- “One possible explanation is…”
- “This may connect to…”

Otherwise it reads as more established than the preceding discussion supports.

---

## Specific revision priorities

If you want a short list of the highest-value edits, I’d prioritize these:

1. **Revise the “second kind of reference dependence” paragraph**  
   Add a concrete example and clarify whether this is part of standard prospect theory or a related extension.

2. **Tighten the Bayesian section**  
   Avoid saying Bayesian agents use “objective values”; distinguish belief updating from decision utility more clearly.

3. **Soften precise quantitative and normative claims**  
   Especially:
   - “2.25 times”
   - EV as “should” without qualification
   - “direct violation of Bayesian invariance”

4. **Clarify the distinction among overweighting, rounding-to-zero, and probability neglect**  
   So readers do not perceive an inconsistency.

5. **Check cross-link implementation**  
   The references are sensible, but the anchor formatting may break depending on the publishing system.

---

## Sample line edits

A few concrete rewrites:

### Current
> “Losses feel roughly 2.25 times as painful as equivalent gains feel pleasant.”

### Suggested
> “Losses typically loom about twice as large as equivalent gains.”

---

### Current
> “Expected value theory says you should prefer this gamble over any sure amount less than €100.”

### Suggested
> “Under a pure expected-value criterion, you should prefer this gamble to any sure amount below €100.”

---

### Current
> “A Bayesian agent updates beliefs by combining prior probabilities with new evidence, using the probabilities directly and evaluating outcomes in terms of their objective values.”

### Suggested
> “From a Bayesian perspective, probabilities should be used coherently and updated consistently. In decision contexts, equivalent descriptions should not reverse preferences, and choices should reflect explicit tradeoffs among outcomes rather than shifts in framing.”

---

### Current
> “If you are choosing between two gambles, the average of all possible outcomes serves as an implicit reference.”

### Suggested
> “People also compare outcomes to salient alternatives they could have had. For example, a job offer can feel disappointing not because it is bad in itself, but because a forgone alternative paid more.”

---

In sum: this is a solid draft with a clear pedagogical arc. The main work now is refinement rather than reconstruction.