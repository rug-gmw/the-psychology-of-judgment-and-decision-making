# Foundations

---

## Reason and Intuition

**Core idea:** Judgments and decisions are carried out via two distinct kinds of mental processing — arguably the most popular organizing framework for the field.

- **System 1 / Type 1 (intuitive):** Fast, effortless, parallel, automatic, emotion-driven, linked to heuristics and biases, does not require working memory. Includes automatic and habitual processing. Not always consciously accessible.
- **System 2 / Type 2 (reflective):** Slow, effortful, serial, deliberate, reason-driven, consciously accessible, necessarily engages working memory. Can be carried out in detachment from reality (abstract, hypothetical, future-oriented thought). Open to introspection.
- **Bounded rationality** [@simon1956; @simon1972]: Classic models assumed people are fully rational and perfectly informed. In reality, human reasoning is constrained by incomplete knowledge, limited cognitive capacity, and the complexity of the decision at hand. System 2 is often too slow, effortful, or even impossible (because not all information is available) to guide our decisions. This is *why* we rely so heavily on System 1 — not out of laziness, but out of necessity.
- The distinction between System 1 and 2 is convenient but imperfect — many forms of thinking have aspects of both systems.
- **@sloman1996's characterization** offers a useful way to understand *what* each system does. His **associative system** (≈ System 1) reasons through similarity and statistical regularities — e.g., recognizing something as a bird because it *looks like* birds you've seen before. Many of the heuristics and biases in this course reflect this associative processing. His **rule-based system** (≈ System 2) reasons through explicit logical, social, or definitional rules — e.g., classifying something as a bird because it meets specific biological criteria. These are not separate theories but complementary descriptions of the same dual-process distinction.
- **Gigerenzer's ecological rationality** offers a contrasting perspective on what System 1 processing achieves. Where Kahneman and Tversky emphasize that heuristics are biased shortcuts in need of System 2 correction, Gigerenzer argues that many heuristics are *ecologically rational* — well-adapted to the structure of real-world environments [@gigerenzer_todd1999]. Simple rules like **Take the Best** (decide based on the single most valid cue) or the **recognition heuristic** (if you recognize one option but not the other, choose the recognized one) can match or outperform complex deliberation when information is scarce and time is limited. This sets up a central tension in the course: are biases genuine errors, or adaptive strategies judged against an unrealistic normative standard?
- **Categorization as a bridge concept:** The associative vs. rule-based distinction is especially clear in **categorization** — one of the most fundamental cognitive operations. We constantly sort objects, people, and situations into categories to guide our judgments and decisions. System 1 categorizes implicitly by *resemblance*: we match new instances to stored prototypes or previously encountered exemplars (prototype and exemplar models of categorization). System 2 categorizes explicitly by *criteria*: we check whether defining features are present (classical/rule-based categorization). This matters throughout the course: the representativeness heuristic (see [Representativeness](#representativeness)) is essentially categorization-by-resemblance gone awry, base-rate neglect arises when we categorize by similarity while ignoring how common each category is, and stereotyping reflects the application of category-level expectations to individuals.
- **Cognitive Reflection Test (CRT)** [@frederick2005]: Measures individual differences in the tendency to override System 1 with System 2. Higher CRT scores predict less acceptance of paranormal beliefs and better reasoning.

**🎯 Bayesian lens:** System 1 relies on rough heuristic priors and pattern-matching — fast but prone to ignoring base rates and evidence quality. System 2 enables more deliberate, calibrated belief updating — closer to Bayesian inference. Categorization itself is inherently Bayesian: given observed features (evidence), what is the probability that this instance belongs to category A vs. B (posterior)? Gigerenzer's insight adds a nuance: full Bayesian computation is often impossible given our cognitive constraints (bounded rationality), so heuristics can be understood as *resource-rational approximations* of Bayesian inference [@lieder_griffiths2020]. Many biases in this course can be understood as failures to engage System 2 when careful Bayesian updating is needed — but some may also reflect adaptive shortcuts that work well in the environments we evolved in.

**Key references:** @stanovich_west2000; @evans2008; @evans_stanovich2013; @kahneman2011; @sloman1996; @frederick2005; @simon1956; @simon1972; @gigerenzer_todd1999; @lieder_griffiths2020

---

## Bayesian Reasoning

**Core idea:** Rational judgment and decision-making can be understood as combining prior beliefs with new evidence to arrive at updated beliefs (posteriors). Bayes' theorem provides the normative standard; the many biases covered in this course represent specific, identifiable departures from this ideal.

- **The Bayesian framework:**
  - **Prior belief (prior):** What you believe before encountering new evidence, expressed as a probability. Shaped by base rates, past experience, cultural knowledge, and schemas.
  - **Evidence (likelihood):** New information — how probable this evidence would be if the hypothesis were true versus false.
  - **Updated belief (posterior):** The revised belief after integrating evidence with the prior. This posterior then becomes the prior for the next piece of evidence.

- **Bayes' theorem (formal):** `P(H|E) = [P(E|H) × P(H)] / P(E)`. Where P(H|E) is the posterior probability of hypothesis H given evidence E, P(E|H) is the likelihood of the evidence given the hypothesis, P(H) is the prior probability, and P(E) is the total probability of the evidence.
- **The mammogram problem — a classic illustration**: A woman has a positive mammogram. The test's sensitivity is 80% (P(positive|cancer) = 0.80) and the false-positive rate is 10% (P(positive|no cancer) = 0.10). The base rate of breast cancer is 1% (P(cancer) = 0.01). What is the probability she has cancer?
- 95 out of 100 physicians estimated 70–80%. The correct answer is ~7.5%.
- People confuse P(positive|cancer) with P(cancer|positive) — ignoring the prior (base rate).
- **Natural frequencies — making Bayesian reasoning intuitive:** Expressing information as concrete counts rather than conditional probabilities dramatically improves accuracy. Out of 1,000 women: 10 have cancer; of those 10, 8 test positive. Of the 990 without cancer, 99 test positive. So of 107 positive results, only 8 (~7.5%) actually have cancer.
- Teaching physicians natural frequencies is more effective than teaching Bayes' theorem, and improvement persists ≥5 weeks [@sedlmeier1997]. Despite this, few physicians are trained this way.
- **Ideal observer models:** In perception research, ideal observer models specify how a perfectly rational agent would combine prior expectations with noisy sensory evidence. Human perception often approximates this — we perceive what is most probable given our expectations and the sensory data. Perceptual illusions arise when priors (expectations) dominate over ambiguous evidence, just as cognitive biases arise when judgment priors dominate. An example of a perceptual illusion is when someone is on our mind (e.g. a love interest), and then we often mistakenly think that we see this person out on the street. In this case, we have a strong prior expectation (implicit in the fact the we are thinking of this person), and weak evidence (because you only catch glimpses of people), resulting in a perceptual illusion.
- **Signal detection theory (SDT):** A framework for decisions under uncertainty with two key parameters: *sensitivity* (ability to distinguish signal from noise — the quality of evidence) and *criterion/bias* (the threshold for saying "yes" — reflecting the prior and the costs of different errors). A Bayesian agent sets the optimal criterion based on base rates and payoff structure. People often set non-optimal criteria, producing patterns of misses and false alarms.
- **Calibration:** A well-calibrated person's confidence matches their accuracy — events they judge as 70% likely occur ~70% of the time. Perfect calibration is the hallmark of good Bayesian reasoning. Most people are *overconfident* (see [Overconfidence](#overconfidence)), meaning their posteriors are too extreme relative to the evidence.
- **Why this matters for the course:** Nearly every bias and heuristic covered in subsequent sections can be understood as a specific departure from Bayesian rationality:

| Phenomenon | Bayesian Departure |
|---|---|
| Base-rate neglect ([Representativeness](#representativeness)) | Ignoring the prior |
| Anchoring ([Anchoring and Primacy](#anchoring-and-primacy)) | Insufficient updating from the prior |
| Availability ([Availability](#availability)) | Biased evidence sampling |
| Representativeness ([Representativeness](#representativeness)) | Likelihood dominates; prior ignored |
| Confirmation bias ([Confirmation](#confirmation)) | Asymmetric updating |
| Overconfidence ([Overconfidence](#overconfidence)) | Posteriors too extreme / poorly calibrated |
| Hindsight bias ([Hindsight](#hindsight)) | Retroactively revising the prior |
| Belief perseverance ([Belief Formation and Perseverance](#belief-formation-and-perseverance)) | Failure to update from disconfirming evidence |
| Clinical vs. statistical ([Statistical vs. Intuitive Prediction](#statistical-vs-intuitive-prediction)) | Informal vs. formal evidence integration |

**Key references:** @bayes1763; @swarna2017; @hoffrage_gigerenzer1998; @sedlmeier1997;  @griffiths_etal2008

---

## Heuristics and Biases

- **Heuristic:** Answering a hard question by substituting an easier one [@kahneman_frederick2002]. Or: a quick-and-easy rule of thumb used under conditions of uncertainty. The term heuristic appears to have been popularized by George Pólya in his 1945 book *How to Solve It*, although he used it mainly in the context of mathematical problem solving. Classified as Type 1 processing. The world is too complex for full rational analysis, so thinking is often heuristic-based (i.e. bounded rationality).
- **Bias:** A systematic error in thinking in a specific direction, often resulting from reliance on heuristics. In daily life, "bias" is sometimes used to mean socially undesirable thinking (including stereotypes, such as that professors are male), but this conflates errors in thinking with social desirability.
- **Cognitive illusions:** Systematic errors in subjective judgment, analogous to visual perceptual illusions — they reveal how judgments and decisions are normally made.
- **Affect:** Experienced emotion; people may rely on positive or negative affect as a simple cue when judging and deciding (the *affect heuristic*).
- **Bias blind spot** [@pronin_etal2002]: People readily recognize biases in others but believe themselves to be largely immune. This is itself a bias — and a particularly stubborn one, because it persists even after people learn about biases. The implication: studying heuristics and biases is not just about understanding *other people's* errors. Every bias discussed in this book applies to the reader too.
- **Debiasing:** If biases are so pervasive, can they be corrected? Sometimes — but it is difficult. The most promising approaches shift thinking from Type 1 to Type 2: explicitly generating alternative viewpoints, delaying decisions, and using structured procedures (see [Steering Other People's Choices](#steering-other-peoples-choices)). However, debiasing is limited by the bias blind spot (people who don't believe they are biased see no reason to correct), by the effortful nature of Type 2 processing, and by deeply entrenched beliefs. Awareness of biases is necessary but rarely sufficient.

**🎯 Bayesian lens:** Heuristics can be understood as computationally cheap approximations to Bayesian inference. They often work well (when priors and evidence are typical) but produce systematic errors when the shortcut diverges from proper integration of prior and likelihood — i.e., biases are predictable failures of approximate Bayesian computation.

**Key references:** @tversky_kahneman1974; @kahneman_frederick2002; @slovic_etal2007; @pronin_etal2002;

---

## How It Is vs. How It Should Be

- **Descriptive models** describe how people *actually* judge and decide, without evaluating quality. The vast majority of models in the field are descriptive (e.g., prospect theory describes how people weigh gains and losses; dual-process models describe the interplay of intuitive and deliberate thinking).
- **Normative models** reflect *optimal* or ideal decision-making — logical, consistent, using all relevant data, getting the person closest to their goals over the long run (e.g., expected utility theory; Bayes' theorem for belief updating).
- **Prescriptive models** recommend how people *ought* to judge and decide in practice; often a practical compromise between normative ideals and descriptive realities (e.g., installing hand sanitizer instead of requiring full handwashing; presenting medical statistics as natural frequencies to improve understanding).

**🎯 Bayesian lens:** Bayesian updating is the normative standard for how beliefs should change in light of evidence. Descriptive models document how people systematically deviate from this standard. Prescriptive models often aim to nudge people closer to Bayesian rationality (e.g., presenting information as natural frequencies).

**Key references:** @simon1955

---

## Mental Models

**Framework theories:** Distinct sets of commonsense background knowledge in biology, physics, and psychology that develop very early in life and organize understanding of new information. When knowledge from one domain is inappropriately applied to another, errors and superstitions may result.

**Stances / Modes of construal** [@dennett1987; @keil2006]:
- **Mechanical (physical) stance:** Explaining in purely physical terms.
- **Design (functional) stance:** Explaining in terms of purpose/function.
- **Intentional stance:** Explaining by presuming beliefs and desires.
- The best stance is the one that makes the most sense of the situation. The adopted stance influences the causal narrative one constructs, which in turn shapes moral judgment.

**Schemas and scripts operate within stances.** The stance you adopt determines which schemas are activated and what kind of reasoning follows:

- **Schema:** A set of general knowledge about what to expect in a particular situation or thing. Activated by incoming information to guide comprehension, memory, learning, and performance.
  - @bransford_johnson1972: Students who learned a topic before reading disjointed sentences had better comprehension and recall.
  - Not everyone has the same schema content, and the nature of that content profoundly affects behavior.
- **Scripts**: Schemas for highly routine events (e.g., restaurant visits). Well known within a culture, with agreed-upon temporal sequences. Culture-specific. Violations of scripts are noticed and remembered — especially when they bring the script to a standstill.

**Artifacts vs. natural kinds as a case study in stance activation:**
Even young children distinguish artifacts (human-made items) from natural kinds (e.g., animals, plants) and reason about them differently. This reflects that different types of things trigger different default stances:
- **Artifacts → design stance:** We understand artifacts in terms of function and purpose. A broken chair is still a chair because it was *designed* to be sat on.
- **Living things → intentional stance:** We understand animals and people in terms of beliefs, desires, and goals. A dog chases a ball because it *wants* to catch it. This tendency is so strong that children spontaneously attribute intentions even to simple animals and animated shapes.
The key insight is that the type of thing we encounter triggers a default stance, which then activates stance-appropriate schemas. This distinction emerges early in development, suggesting it reflects a deep organizing principle of human cognition.

**🎯 Bayesian lens:** Stances set the broadest level of prior beliefs — which *kind* of explanation is appropriate. Within a stance, schemas encode more specific expectations about what is likely. Scripts represent strong temporal priors within schemas, and script violations are prediction errors. New information is interpreted against these layered priors: stance-inconsistent information may be ignored entirely, while schema-inconsistent information within the right stance is surprising and may trigger updating.

**Key references:** @wellman_gelman1992; @dennett1987; @bransford_johnson1972;

---

# Intelligence

---

## What is intelligence?

- **Intelligence resists verbal definition — but that's okay.** Ask ten psychologists to define intelligence and you'll get ten different answers. Some emphasize problem-solving, others learning speed, others adaptation to new environments. This ambiguity sometimes leads people to a relativist position: if we can't even define intelligence, maybe the concept is meaningless. But this confuses *verbal* definition with *statistical* definition. We don't need a crisp sentence to make intelligence scientifically useful — we need it to behave consistently in data. And it does. The g-factor (below) is one of the most robust and replicable findings in all of psychology. Intelligence may be hard to put into words, but it is easy to measure, and it predicts real-world outcomes with striking consistency.
- **g-factor (General intelligence)** [@spearman1904]: Imagine we organize a mega-Olympics where a hundred random people from the street compete in every event. We'd quickly notice that some people do well across the board — faster runners, better swimmers, higher jumpers — while others consistently struggle. There's a general underlying factor we might call *physical fitness* that largely determines performance across diverse athletic events. Spearman's insight was that intelligence works the same way. There is a general underlying factor — the **g-factor** (for *general intelligence*) — that partly determines how well people perform across all kinds of cognitive tasks. People with a high g-factor tend to have better spatial reasoning, larger vocabularies, higher working-memory capacity, and stronger problem-solving skills. This explains why the specific tasks in an IQ test matter less than you'd think: most cognitive tasks tap into the g-factor to some degree. In applied and organizational psychology, the g-factor is often referred to as **general mental ability (GMA)** — same construct, different label.
- **s-factors (Specific abilities):** Just as a steady hand matters for archery but not for sprinting, some cognitive abilities are task-specific. Language skill matters for vocabulary tests but not for visual puzzles. Spearman called these **s-factors** (for *specific intelligence*). Some abilities are almost purely g-loaded — matrix puzzles are the best example, requiring working memory, flexible recombination of information, and active problem-solving. Others, like musicality, depend mostly on specific factors.
- **Fluid intelligence** [@cattell1963]: The capacity to flexibly manipulate information in working memory to solve novel problems. Corresponds closely to the g-factor (matrix puzzles are a near-pure measure). Declines with age.
- **Crystallized intelligence** [@cattell1963]: Accumulated knowledge, skills, and facts in long-term memory (e.g., vocabulary). Increases with age. With experience, tasks that once required fluid intelligence can be solved through crystallized intelligence.

**🎯 Bayesian lens:** The fluid–crystallized distinction maps neatly onto Bayesian inference. Crystallized intelligence is your stock of **priors** — the rich body of knowledge and patterns accumulated over a lifetime. Fluid intelligence is the engine that processes **evidence** and computes the **posterior** — flexibly integrating new information with what you already know. A person with strong priors (crystallized) but a weakening engine (declining fluid intelligence) can still perform well in familiar domains, but will struggle when the environment changes and priors alone aren't enough. This is exactly what we see with aging: experienced professionals compensate for slower updating with richer priors.

**Key references:** @spearman1904; @cattell1963

---

## Intelligence vs. Rationality

- **Dysrationalia** [@stanovich1993]: Stanovich argues that standard IQ tests measure *algorithmic-level* processing — raw computational power — but miss *reflective-level* thinking dispositions: the tendency to actually engage that power when it matters. He coined the term **dysrationalia** to describe the condition of having adequate intelligence yet thinking poorly. A high-IQ person can still fall prey to biases if they lack the disposition to override intuitive responses.
- **The Cognitive Reflection Test (CRT)** [@frederick2005]: A brief test that measures the tendency to override an intuitive but incorrect response (System 1) with a deliberate, correct one (System 2). CRT scores predict susceptibility to biases — anchoring, framing, base-rate neglect — above and beyond IQ. Where IQ asks *can you solve this?*, the CRT asks *will you bother to check your gut feeling?*
- **Actively Open-Minded Thinking (AOT)** [@stanovich_toplak2023]: A thinking disposition characterized by willingness to consider alternative viewpoints, seek disconfirming evidence, and revise beliefs. AOT predicts resistance to belief bias and myside bias independently of intelligence. It captures something IQ misses: intellectual humility and epistemic flexibility.

**🎯 Bayesian lens:** Intelligence gives you the computational machinery to perform a Bayesian update; rationality is the *disposition to actually perform it*. A dysrational thinker has the processing power to integrate base rates, weigh evidence, and revise beliefs — but defaults to System 1 shortcuts instead. The CRT captures exactly this: the willingness to notice that your intuitive posterior feels wrong and recalculate. AOT goes further — it reflects the habit of actively seeking out evidence that could *change* your posterior, rather than selectively gathering evidence that confirms it. In Bayesian terms, intelligence is the capacity to compute; rationality is the willingness to compute honestly.

**Key references:** @stanovich1993; @frederick2005; @stanovich_etal2013;

---

## Intelligence in the Real World

- **Intelligence predicts real-life outcomes:** GMA is one of the strongest single predictors of both academic achievement and job performance across virtually all occupations. @schmidt_hunter2004 showed that GMA predicts job performance better than any other single selection method, including work experience, interviews, and personality measures. The predictive power increases with job complexity — for complex jobs (management, engineering), GMA is an even stronger predictor than for simpler jobs. This doesn't mean intelligence is the *only* thing that matters, but it does mean that the g-factor has substantial real-world consequences beyond the lab.
- **Genetic and environmental basis:** Twin studies show roughly half of individual differences are attributable to genetics. The rest is shaped by parental stimulation, socioeconomic status, neighborhood, and cultural background.
- **IQ testing:** Modern tests (e.g., WAIS) define IQ relative to population norms (100 = average; 130 = top ~2%).
- **The Flynn effect and its reversal:** Throughout the 20th century, average IQ scores rose by roughly 3 points per decade — the **Flynn effect**. This is too fast for genetic change, suggesting environmental causes: better nutrition, more education, greater exposure to abstract reasoning. However, recent evidence suggests the Flynn effect has plateaued or even reversed in some countries. @bratsberg_rogeberg2018 analyzed Norwegian military conscription data and found IQ scores *declining* among cohorts born after the mid-1970s. The cause of this reversal is debated — possible explanations include changes in education, media consumption, or lifestyle — but it challenges the assumption that each generation is cognitively sharper than the last.

**🎯 Bayesian lens:** The strong predictive power of GMA can itself be understood through a Bayesian lens: people with higher g-factors form more accurate priors, update more appropriately from evidence, and maintain better-calibrated confidence — advantages that compound across academic and professional domains. Higher fluid intelligence and CRT scores predict more Bayesian reasoning — greater sensitivity to base rates, less anchoring, less susceptibility to framing effects [@frederick2005; @toplak_etal2011]. The Flynn effect raises an intriguing question: if populations are (or were) getting better at abstract reasoning, are they also becoming more Bayesian? And if the trend is reversing, what does that mean for the quality of collective judgment?

**Key references:** @frederick2005; @toplak_etal2011; @schmidt_hunter2004; @bratsberg_rogeberg2018

---

# Uncertainty

---

## Availability

**Definition:** The tendency to estimate frequency or probability based on how easily instances or associations come to mind. The easier recall is, the more likely the event is judged to be. Classified as Type 1 reasoning.

**Key studies:**
- *Famous names* [@tversky_kahneman1973]: Lists with very famous women and somewhat famous men led participants to overestimate the number of women — because famous names were more easily recalled.
- *First vs. third letter position* [@tversky_kahneman1973]: 69% judged consonants (K, L, N, R, V) as more frequent in the first position of words, but all five actually appear more often in the third position — because it is easier to search by first letter.

**What makes something "available"?** Availability can manifest in different ways: faster recall (a few vivid examples come to mind quickly), more recalled exemplars (many instances are retrieved, even if slowly), or stronger associations (certain pairings are more deeply encoded). These are not competing hypotheses — they are all routes through which the same principle operates. Some researchers use the term *accessibility* (ease of retrieval) to emphasize the speed component, but availability as a concept encompasses all of these manifestations.

**Negativity bias interaction:** People seek out, attend to, and are more strongly influenced by negative content. @robertson_etal2023: Click-through rates increased with negative words in headlines and decreased with positive words. This makes negative events disproportionately available, making the world seem grimmer than it is.

**Applied contexts:** The availability heuristic plays a major role in [Medical Decision-Making](#medical-decision-making), where recent cases bias diagnosis, and in social media environments (see [Populism and Social Media](#populism-and-social-media)), where algorithmic curation makes certain types of information disproportionately available.

**🎯 Bayesian lens:** The availability heuristic biases the *evidence sampling* step of Bayesian reasoning. Instead of drawing a representative sample from memory (which would give accurate base rates), people draw a biased sample — weighted toward recent, vivid, emotional, or easily retrieved instances. The likelihood term is distorted because the evidence itself is not representative. A Bayesian reasoner with unbiased memory access would not show this effect.

**Key references:** @tversky_kahneman1973; @tversky_kahneman1974; @macleod_campbell1992; @robertson_etal2023

---

## Representativeness

**Definition:** The tendency to judge the probability of an event or category membership based on how similar it is to a prototype or stereotype, rather than on actual statistical information.

**Core mechanism — Base-rate neglect:** The representativeness heuristic is fundamentally driven by base-rate neglect: people attend to how well evidence matches a category (likelihood) while ignoring how common that category actually is (prior/base rate).
- *Tom W. problem* [@kahneman_tversky1973]: Likelihood judgments of Tom's graduate field correlated almost perfectly with representativeness ratings but *negatively* with actual base rates of enrollment.
- *Taxicab problem* [@barhillel1980]: A witness (80% accurate) identifies a hit-and-run cab as Green in a city with 85% Blue cabs. Most people estimate ~80% Green, ignoring base rates. Using natural frequencies: only 12 out of 29 positive identifications (~41%) are truly Green.

**Consequence 1 — Conjunction fallacy:** Because representativeness is driven by similarity rather than probability logic, people judge the conjunction of two events (A and B) as more probable than one event alone (A), violating the conjunction rule P(A∩B) ≤ P(A).
- *Linda problem* [@tversky_kahneman1983]: 82% judged "bank teller and feminist" as more probable than "bank teller" alone, because the conjunction better matches Linda's description.
- *Averaging heuristic:* One explanation is that people intuitively average the probabilities of component events rather than multiplying them. "Feminist" has high probability given Linda's description; "bank teller" has low probability; the average feels higher than "bank teller" alone — but proper probability requires multiplication, which would make the conjunction *less* likely.
- *Alternative view* [@hertwig_gigerenzer1999]: Participants may interpret "probable" non-mathematically (e.g., as "plausible"), making responses reasonable conversational inferences rather than logical fallacies.

**Consequence 2 — Stereotyping:** Representativeness drives stereotyping: when a person resembles the prototype of a social category, they are judged as more likely to belong to that category regardless of base rates.
- @bodenhausen_wyer1985: Predicted future criminal behavior was stereotype-congruent (forgery for "Ashley Chamberlaine," assault for "Carlos Ramirez"), even when alternative explanations were provided.
- This has serious implications for [Legal Decision-Making](#legal-decision-making) and [Medical Decision-Making](#medical-decision-making).

**Consequence 3 — Distorted perception of randomness:** People have a stereotype of what "random" looks like — roughly alternating, without long runs. Sequences that don't match this stereotype are judged as non-random.
- *Gambler's fallacy:* After a run of five heads, people judge tails as "due" because HHHHHH doesn't look representative of randomness, even though each flip is independent.
- *Hot hand belief:* Streaks in sports performance are perceived as meaningful ("he's on fire!") when they often fall within the range expected by chance.

**🎯 Bayesian lens:** The representativeness heuristic is the most direct violation of Bayesian reasoning, and the hierarchy makes this clear:
- **Core mechanism (base-rate neglect):** People ignore the prior P(H) and base judgments almost entirely on the likelihood P(E|H) — how representative the evidence is of the hypothesis.
- **Conjunction fallacy:** Overweighting likelihood leads to violations of basic probability axioms — the posterior for the conjunction exceeds the posterior for the single event because the conjunction is more representative.
- **Stereotyping:** Stored representativeness judgments (stereotypes) function as inflated likelihood estimates that override low base rates for the stereotyped category.
- **Randomness perception:** People's stereotype of randomness acts as a prior about what random sequences should look like, leading them to reject actually random sequences that don't match this prototype.

**Key references:** @kahneman_tversky1972; @kahneman_tversky1973; @tversky_kahneman1971; @tversky_kahneman1983; @barhillel1980; @bodenhausen_wyer1985; @hertwig_gigerenzer1999

---

## Anchoring and Primacy

**Definition:** The tendency to make judgments by starting from an initial value or first impression and adjusting insufficiently. The anchor is highly *available* (see [Availability](#availability)), making anchor-consistent information more accessible in memory and biasing the estimate — even when the anchor is clearly irrelevant.

**Classic studies:**
- *Wheel of fortune* [@tversky_kahneman1974]: Random numbers (10 vs. 65) influenced estimates of African UN membership (25% vs. 45%).
- *Multiplication sequences* [@tversky_kahneman1973]: 1×2×...×8 → median estimate 512; 8×7×...×1 → median estimate 2,250 (correct: 40,320).

**Mechanism:**
- The anchor makes anchor-consistent information more accessible in memory, biasing the estimate without the person being aware of it. This is essentially the availability heuristic (see [Availability](#availability)) applied to numerical estimation: the anchor is the most available number, and information consistent with it comes to mind most easily. Adjustment away from the anchor is typically insufficient.

**Boundary conditions:**
- *Extreme/implausible anchors:* Even wildly implausible anchors (Gandhi age 9 or 140) influence estimates [@strack_mussweiler1997], though extreme anchors have attenuated effects.
- *Cross-modal anchoring:* Anchors in one domain (e.g., line length) influence estimates in another (e.g., temperature) [@oppenheimer_etal2008]. This may reflect the brain's shared representation of magnitude: numbers, space, time, brightness, and weight are all represented in partly overlapping ways, so that anchoring in one dimension can spill over into another.

**From numbers to impressions — primacy effects:**
- Anchoring is primarily about *numerical* estimation, but the same principle applies to *qualitative* judgments. When forming impressions of people, situations, or ideas, the first information we encounter functions as an anchor, shaping how we interpret everything that follows.
- @asch1946: Personality traits in opposite orders (*intelligent…envious* vs. *envious…intelligent*) produced markedly different impressions. Positive-first groups inferred additional positive traits (74% "good-looking" vs. 35%).

**Applied contexts:**
- *Real estate:* Listing prices anchor both laypeople's and experts' home value estimates. Agents show comparable anchoring effects but are less likely to report using the listing price [@northcraft_neale1987].
- *Advertising:* Price anchoring ("was €99, now €49") exploits the original price as an anchor, making the discounted price seem like a better deal.
- *Medical diagnosis:* See [Medical Decision-Making](#medical-decision-making).

**Countering anchoring:** Very difficult. Informing people about anchoring does not attenuate it [@chapman_johnson2002]. One promising avenue: *positive affect* — physicians who received a small bag of candies showed less anchoring in diagnostic reasoning [@estrada_etal1997].

**🎯 Bayesian lens:** Anchoring and primacy both represent *over-weighting of the prior*. In ideal Bayesian updating, the order of evidence should not matter — the final posterior is the same regardless of presentation order. In reality, the first piece of information (whether a number or a personality trait) forms a strong prior that is insufficiently revised by later evidence. This is the opposite problem from base-rate neglect: here the prior exerts *too much* influence.

**Key references:** @tversky_kahneman1973; @tversky_kahneman1974; @asch1946; @anderson1965; @strack_mussweiler1997; @hogarth_einhorn1992; @chapman_johnson2002; @oppenheimer_etal2008; @northcraft_neale1987; @estrada_etal1997

---

## Overconfidence

**Definition:** Overconfidence manifests in two fundamentally different ways, corresponding to two different distortions of belief. Understanding these two dimensions clarifies an otherwise confusing family of biases.

**Self-favorable bias:** A systematic tendency to hold beliefs about oneself that are more favorable than warranted. This manifests in several overlapping ways:
- *Overestimation:* Overestimating one's actual performance, knowledge, or control. Related to the *illusion of control* [@langer1975]: people who chose their own lottery ticket demanded over $8 to sell; randomly assigned tickets were sold for ~$2.
- *Overplacement (better-than-average effect):* Judging oneself as better than the average person. @weinstein1980: Students rated themselves as less likely to contract diseases and more likely to experience positive events than average.
- *Positivity bias / unrealistic optimism:* Selectively updating beliefs in a self-favorable direction. 
- These are all expressions of the same underlying tendency: the posterior is *shifted* in a self-favorable direction.

**Overprecision (narrowed posterior):** Underestimating the uncertainty in one's own judgments. When asked for 90% confidence intervals, people typically capture the true answer only 40–60% of the time. The most pervasive and least understood form of overconfidence. Here, the posterior is not shifted but *too narrow* — the agent assigns too little probability mass to alternative outcomes.

**Overconfidence and mental health:** A self-favorable bias appears to be a marker of mental health.
- @korn_etal2014 found that healthy controls showed a positivity bias in belief updating, while patients with major depression did not.
- This connects to @seligman_maier1967's work on learned helplessness: dogs exposed to inescapable shocks initially kept trying to escape — an "unrealistically optimistic" response, but also a healthy one. After repeated failure, they stopped trying, even when escape became possible. This learned helplessness parallels depression.
- Similarly, @alloy_abramson1979 found that depressed individuals are actually *more accurate* in judging their control over outcomes ("depressive realism").
- The paradox: a degree of overconfidence — a shifted posterior — appears to be psychologically adaptive, while a more realistic (unshifted) posterior is associated with depression and helplessness.

**The planning fallacy** [@kahneman_tversky1979]: The tendency to underestimate the time, cost, and risk of future actions while overestimating benefits. Both distortions operate simultaneously: the estimate is too optimistic (shifted posterior) *and* fails to account for the full range of things that could go wrong (narrowed posterior). People focus on the specific plan (inside view) rather than base rates of similar past projects (outside view).
- @buehler_etal1994: Students predicted finishing assignments far earlier than they did — even when explicitly asked to consider past experience.
- Large infrastructure projects routinely overrun budgets and timelines [@flyvbjerg2006].

**Dunning-Kruger effect** [@kruger_dunning1999]: The least competent individuals show the greatest overconfidence, because the skills needed to perform well are the same skills needed to recognize poor performance. This combines both distortions: a large self-favorable shift (they think they're doing well) and poor calibration (they have no awareness of their uncertainty). Highly competent individuals slightly underestimate their ability. Debated: some argue the effect is partly a statistical artifact (regression to the mean), but the core finding — that poor performers are poorly calibrated — is well-replicated.

**Expertise and overconfidence:** Domain expertise improves calibration only when accompanied by clear, frequent feedback (e.g., weather forecasters are well-calibrated; clinical psychologists are not). Without feedback loops, experience increases confidence without increasing accuracy [@einhorn_hogarth1978]. This is one reason people tend to prefer clinical intuition over statistical models, even when models outperform (see [Statistical vs. Intuitive Prediction](#statistical-vs-intuitive-prediction)).

**🎯 Bayesian lens:** Two distinct Bayesian failures: (1) *Shifted posterior* — the self-favorable bias pushes beliefs in a direction that flatters the self, as if applying a biased prior that says "I am exceptional." (2) *Narrowed posterior* — overprecision assigns too little probability mass to alternative outcomes, as if discounting evidence that would widen the distribution. The planning fallacy illustrates both: the estimate is shifted toward optimism *and* the uncertainty band is too narrow. A well-calibrated Bayesian would maintain posteriors that are both unbiased and appropriately wide.

**Key references:** @lichtenstein_etal1982; @moore_healy2008; @langer1975; @weinstein1980; @kruger_dunning1999; @buehler_etal1994; @korn_etal2014; @flyvbjerg2006; @einhorn_hogarth1978

---

# Causality

---

## Cues to Causality

**Cues-to-causality** [@einhorn_hogarth1986]: Situational features leading people to judge that a causal relationship is present. These are the basic toolkit people use to infer causation in everyday life.

**Causal field** [@mackie1965]: The background of existing conditions against which potential causes are evaluated. A **difference-in-a-background** — an event that stands out against the causal field — is inferred to be the cause.

**Temporal order:** When one event regularly precedes another, people infer causation. People use temporal order even when they shouldn't (e.g., judging P(child has blue eyes | parent has blue eyes) as higher than the reverse, though mathematically equal). In legal settings, evidence in temporal order makes decision-makers more convinced [@pennington_hastie1988; see also [Legal Decision-Making](#legal-decision-making)].

**Contiguity and covariation:** People are more likely to infer causation when events co-occur — both at the level of single instances (contiguity: the cause and effect happen close together in time and space) and across repeated instances (covariation: the cause and effect tend to happen together). @michotte1963: Two-ball "launching" displays demonstrate contiguity-based causation — precise spatiotemporal proximity triggers an immediate causal percept. Covariation extends this to the aggregate: when petting a cat reliably co-occurs with purring, we infer causation across instances. People often interpret correlations as causal relationships.

**Causal mechanism:** An explanation filling the gap between cause and effect. People explain events in terms of mechanisms 83% of the time, rather than covariation [@ahn_etal1995].

**Similarity of cause and effect:** (1) Physical resemblance (e.g., doctrine of signatures); (2) Matching magnitude — people expect large effects to have large causes.

**Simulation heuristic and counterfactual reasoning** [@kahneman_tversky1982]: People mentally simulate what might have happened differently. A factor is a **but-for cause** if the event would not have occurred without it.

**🎯 Bayesian lens:** Cues to causality function as features that strengthen or weaken the likelihood of a causal hypothesis. Each cue updates the probability of causality: temporal order, contiguity/covariation, and mechanism all increase P(E|causal link), while their absence decreases it.

**Key references:** @einhorn_hogarth1986; @mackie1965; @michotte1963; @ahn_etal1995; @kahneman_tversky1982; @pennington_hastie1988

---

## Blame, Praise, and Responsibility

**From cues to people:** The cues to causality from [Cues to Causality](#cues-to-causality) apply to all causal reasoning. But when the potential cause is a *person*, a special set of attributional processes kicks in. This connects directly to the distinction between stances in [Mental Models](#mental-models): when we reason about people, we adopt the **intentional stance** — attributing behavior to beliefs, desires, and goals. When we reason about impersonal causes, we use the **mechanical or design stance**. Attributing causality to people is closely tied to moral judgment (see [Morality](#morality)): deciding who caused an outcome is often the first step toward deciding who deserves blame or praise.

**Personal vs. impersonal causality**:
- Personal causality = a person's intention was the force behind an action. We assign **blame or praise** only when we perceive personal causality — someone *meant* to do it [@young1995]. A doctor who prescribes the wrong medication *on purpose* deserves blame; one who does so because of a confusing label does not — even though the outcome is identical.
- Impersonal causality = the action occurred without intention. There is **no one to blame** — the outcome is attributed to circumstances, chance, or mechanical forces. This maps directly onto the intentional stance (personal) vs. the mechanical stance (impersonal) from [Mental Models](#mental-models).

**Covariation principle** [@kelley1973]: "An effect is attributed to the one of its possible causes with which, over time, it covaries." Applied to person perception, covariation (introduced in [Cues to Causality](#cues-to-causality)) is broken down into three specific dimensions:
- **Consensus:** Do other people respond the same way to the same stimulus?
- **Distinctiveness:** Does this person respond this way only to this specific stimulus?
- **Consistency:** Does this person respond similarly over time?
- Different patterns yield different attributions: Low consensus + low distinctiveness + high consistency → person attribution ("it's something about *them*" → blame or praise the person). High consensus + high distinctiveness + high consistency → stimulus attribution ("it's something about the *situation*" → no personal blame or praise).

**Correspondence bias / Fundamental attribution error** [@gilbert_malone1995]: We systematically **over-blame people and under-blame situations**. Even when told essay writers were assigned their position, people judged they really believed what they wrote. In everyday terms: a student fails an exam? "They're lazy" (blame the person), not "the exam was unfair" (blame the situation). This is an over-application of the intentional stance when the mechanical stance (situational forces) would be more appropriate.

**🎯 Bayesian lens:** Causal attribution is belief updating about the source of behavior. The prior is one's default assumption about the person or situation; evidence from consensus, distinctiveness, and consistency updates this belief. The fundamental attribution error reflects an overly strong prior toward the intentional stance — defaulting to "who is to blame?" and insufficiently updating in light of situational evidence that no one deserves blame (or praise) at all.

**Key references:** @kelley1973; @cheng_novick1990; @gilbert_malone1995; @young1995;

---

## Learning Causality

**2 × 2 contingency table:** Summarizes co-occurrence of two factors (cells A, B, C, D). A Bayesian agent would use all four cells to compute the contingency. But people give cell A (both present) the most weight, followed by B, then C, and D the least. When simplifying, people sometimes attend only to cell A — a purely confirmatory approach.

**Conditioning as the basis of causal learning:** We learn causal relationships through association. In *classical conditioning*, two events that tend to co-occur become linked (the bell predicts food). In *operant conditioning*, we learn that actions lead to outcomes (pressing a lever causes a reward). Both are forms of learning about the causal structure of the world.

**Prediction error as the driving mechanism:** What makes conditioning work is *prediction error* — the brain signals deviations from what was expected. @schultz_etal1997: dopamine neurons respond to unexpected rewards and go silent when expected rewards are omitted. After conditioning, the dopamine response shifts from the reward itself to the cue that predicts it. Learning occurs when outcomes are surprising; once a cue fully predicts an outcome, learning stops.

**Blocking**: This is prediction error in action. When a first cue already perfectly predicts an outcome, pairing it with a second cue produces no prediction error — so nothing is learned about the second cue. The first cue "blocks" the second. This is actually Bayesian: once a cue fully explains the outcome, a redundant cue provides no additional evidence and should receive no credit.

**Predictive vs. diagnostic learning** [@waldmann_holyoak1992]: Blocking depends on causal direction.
- *Predictive task:* Cause presented first → learner determines the effect. Cues compete; blocking occurs.
- *Diagnostic task:* Effect presented first → learner determines the cause. Blocking does *not* occur.
- Same data, different learning outcomes — demonstrating that causal learning depends on more than simple associations.

**Illusory correlations:** Perceiving correlations that do not actually exist (e.g., perceived link between political parties and economic performance). This is a downstream consequence of the cell A bias: selectively attending to confirming co-occurrences while ignoring disconfirming cases.

**Illusory causation / Quackery:** Interpreting real but non-causal correlations as causal. When many cases appear in cell A (treatment present, recovery present), people perceive a causal link even when recovery rates are identical regardless of treatment.
- @matute_etal2011: 80% of patients recovered regardless of treatment, yet participants judged the medicine effective — especially when many patients took it (64 vs. 16 in cell A).
- This is a failure to account for the base rate of recovery (cell A + C), i.e., P(recovery) regardless of treatment.

**Regression toward the mean:** An initial extreme value is followed by a value closer to the mean. People create spurious causal explanations for this statistical phenomenon rather than recognizing natural variability.

**Plausibility:** Pre-existing beliefs about which causal relationships are plausible strongly influence processing of covariation data. Plausible causes receive more weight from covariation evidence [@fugelsang_thompson2003]. People seek out cause-present information more when the cause is plausible [@goedert_etal2014]. In Bayesian terms, plausibility functions as a prior that modulates how evidence is weighted — a form of prior-driven evidence evaluation.

**Experimental designs:** Only experimental manipulation (controlling an independent variable while holding everything else constant) allows causal conclusions — as opposed to the correlational evidence that drives illusory causation.

**🎯 Bayesian lens:** Each failure of causal reasoning maps onto a specific departure from Bayesian updating. Cell A bias = overweighting confirming evidence. Illusory causation = neglecting base rates. Regression misinterpretation = failing to account for noise. Yet some aspects of causal learning *are* Bayesian: prediction error drives learning exactly when outcomes are surprising (high likelihood ratio), blocking correctly assigns zero weight to redundant predictors, and plausibility shows that priors (appropriately) shape learning.

**Key references:** @lipe1990; @schultz_etal1997; @waldmann_holyoak1992; @matute_etal2011; @fugelsang_thompson2003; @goedert_etal2014

---

# Past and future

---

## Hindsight

**Definition:** The tendency to believe, after learning an outcome, that one "knew it all along" [@fischhoff1975]. People's recalled predictions shift toward the actual outcome, the outcome feels inevitable in retrospect (**creeping determinism**), and people are unaware their judgments have changed.

**Example — visual hindsight bias:** People who know what a degraded image depicts believe a naïve observer would recognize it at a much earlier (more degraded) stage — the "I saw it all along" effect [@bernstein_etal2004]. This illustrates how knowing the answer makes it feel obvious.

**Paradigms:**
- *Memory paradigm:* People make predictions, then recall them after learning the outcome. Recalled judgments shift toward the actual outcome.
- *Hypothetical paradigm:* A foresight group (no outcome knowledge) is compared to a hindsight group (knows the outcome, but is asked to judge "as if" they don't). Hindsight judgments are closer to the actual outcome [@fischhoff1975].

**Contributing factors:**
- **Availability (see [Availability](#availability)):** What actually happened comes to mind easily and vividly; what *could have* happened does not. The actual outcome dominates recall.
- **Causal narrative construction:** People construct a coherent causal story explaining why the outcome occurred. Once built, this narrative is difficult to disregard — it makes the outcome feel logical and inevitable (cf. [Cues to Causality](#cues-to-causality)).
- **Curse of knowledge:** Learning changes you, and it is difficult to put yourself back in the mindset of your previous, less-informed self. This is closely related to **theory of mind** — the ability to represent others' (or your past self's) mental states as different from your current state. Epistemic egocentrism: people underestimate how likely another person is to hold a false belief [@birch_bloom2007].
- **Self-serving bias:** People take credit for positive outcomes ("I knew it would work") more than negative ones, further inflating hindsight.

**Outcome bias:** A related phenomenon: judging the *quality of a decision* by its outcome, even when the outcome was unforeseeable. @baron_hershey1988: a physician's decision was rated as poorer when the patient died, despite identical reasoning. This conflates outcome quality with decision quality.

**When hindsight bias is weak or reversed:**
- **No plausible causal antecedents:** When people cannot construct a causal narrative for the outcome, hindsight bias does not occur [@yopchick_kim2012]. This confirms that causal narrative construction is a key driver.
- **Self-serving motivation counteracts it:** @mark_mellor1991: laid-off workers showed the *least* hindsight bias — admitting "I knew I'd be fired" would threaten self-esteem.
- **Reverse hindsight bias:** Under extreme surprise, people believe they "never would have seen it coming." @ofir_mazursky1997: hindsight participants rated a fatal heart bypass as *more likely to succeed* than foresight participants. The surprise blocks causal narrative construction and triggers an opposite effect.

**🎯 Bayesian lens:** Hindsight bias is retroactive revision of the prior to match the posterior. After learning the outcome, the prior is "overwritten" — people can no longer access what they believed before the evidence arrived. A true Bayesian retains awareness of prior vs. posterior; the hindsight-biased thinker confuses them. The curse of knowledge is the core mechanism: legitimate Bayesian updating changes your beliefs, but you lose access to the pre-update state.

**Key references:** @fischhoff1975; @baron_hershey1988; @birch_bloom2007; @bernstein_etal2004; @yopchick_kim2012

---

## Statistical vs. Intuitive Prediction

**Clinical intuition:** Domain experts consider available information and make intuitive predictions, drawing on experience and holistic assessment. People tend to overestimate its value.

**Statistical prediction:** Predictions based solely on empirical evidence and statistical comparison. A meta-analysis of 136 studies [@grove_etal2000]: 46% favored statistical prediction, 48% showed no difference, *only 6%* favored clinical intuition. Publication date, training, experience, and domain had no effect.

**Why clinical intuition is overvalued:**
- *Cognitive fluency:* With experience, assessment *feels* easy and confident — even when accuracy hasn't improved (see [Overconfidence](#overconfidence)).
- Especially problematic in areas with little concrete feedback (clinical psychology, law, university admissions).
- Corrective feedback is critical for learning; weather forecasters exemplify accurate expert prediction because they receive frequent, consistent feedback.

**Case study 1 — Selecting judges in the Netherlands [@dehoog2026a]:**
Researchers evaluated the multi-round selection procedure for the Dutch judiciary training program [@neumann_etal2026]. Key findings:
- The procedure was lengthy (five rounds) yet violated basic best practices at nearly every stage: unclear criteria, inconsistent questions across candidates, and no predefined decision rules for pass/fail.
- Decisions were largely intuition-based — a scoring rubric existed but was rarely used; "fit" and "gut feeling" drove choices, especially in local interviews.
- A simple intelligence test (round two) predicted training performance *better* than an elaborate expert-led assessment involving psychologist interviews and actor role-plays.
- The best-rated part of the procedure (final interviews) used structured questions, predefined scoring anchors for good/bad answers, and independent numerical ratings — precisely the features statistical prediction advocates.
- Even in this strong final round, post-interview deliberation among evaluators introduced bias. Simply summing independent scores would have produced equally good — and more consistent — selections.
- Illustrates a core tension: professionals value intuition ("my gut should have a voice") and resist structured methods, even when evidence shows structure improves outcomes. One evaluator compared intuition to a physician's "gut instinct" — yet in medicine too, intuitive diagnosis rarely improves on structured checklists.
- Broader lesson: *less information, applied consistently, beats more information applied intuitively.* The researchers' advice: "Do as little as necessary — and do it well."

**Case study 2 — Data-driven football recruitment at Heart of Midlothian [@dehoog2026b]:**
Heart of Midlothian, a Scottish football club co-owned by entrepreneur and poker player Tony Bloom, illustrates what happens when statistical prediction *leads* rather than merely supports decisions.
- Traditional football scouting is clinical intuition: scouts travel to matches, watch players, and form holistic impressions. Most clubs treat data as "supporting, never leading."
- Bloom's approach inverts this. His fortune was built on a statistical insight, and he also applies this logic to player recruitment: a team's quality is better predicted by chances created than by goals scored — because creating chances reflects skill, while scoring reflects luck.
- Hearts uses data models to evaluate what individual players contribute to the chances their team creates. This allows the club to screen players across *all* leagues simultaneously — including obscure ones where talent is undervalued and therefore cheap.
- The club has no traditional scouts. Recent signings came from Kazakhstan, North Macedonia, Norway's second division, and the Dutch Keuken Kampioen Divisie. Video review serves only to verify what the data already suggest.
- Players know the system: "You play well if the data say you play well." If your data decline, a replacement with better data will be found.
- Results: at the time of writing, Hearts sit above both Celtic and Rangers — clubs with vastly larger budgets — atop the Scottish Premiership. Players who were unknown and unwanted elsewhere have become stars.
- The football world has known about data-driven methods since at least FC Midtjylland's success in 2015. Yet most clubs still rely on traditional scouting. The resistance mirrors the judiciary case: professionals prefer intuition even when statistical methods demonstrably outperform it.

**Two cases, one lesson:** The judiciary case shows what goes wrong when clinical intuition dominates — inconsistent decisions, wasted information, poor prediction. The Hearts case shows what goes right when statistical methods lead — hidden talent is found, resources are used efficiently, and results exceed expectations. In both domains, the same pattern holds: structured, data-driven prediction outperforms expert intuition.

**🎯 Bayesian lens:** Clinical intuition represents informal, heuristic Bayesian reasoning — integrating evidence with experience-based priors, but doing so imprecisely and inconsistently. Statistical methods are formal Bayesian (or frequentist) inference — applying the same evidence-weighting rules uniformly across cases. The superiority of statistical methods shows that human intuitive "Bayesian" processing is noisy and biased, especially without calibrating feedback. Expertise without feedback increases confidence (strengthens the prior) without improving the quality of evidence integration.

**Key references:** @grove_etal2000; @dawes_etal1989; @garb2005; @einhorn_hogarth1978; @neumann_etal2026; @dehoog2026a; @dehoog2026b

---

## The Future Self

**Core theme:** People struggle to relate to their future selves. This manifests in two distinct but related ways: mispredicting how future events will make you feel (*affective forecasting*), and undervaluing outcomes that happen to your future self (*temporal discounting*). Both stem from a common root: psychological distance from the future self, who is experienced almost as a stranger. This connects to theory of mind and the curse of knowledge (see [Hindsight](#hindsight)): it is hard to inhabit another mind, whether that mind belongs to another person, your past self, or your future self.

**Affective forecasting:** Predictions about how future events would make you feel. People are generally good at predicting *valence* (positive vs. negative) but poor at predicting *intensity* and *duration*. This is a cognitive failure: you try to simulate your future self's feelings but get it wrong.

**Impact bias (intensity):** Overestimating how intensely and how long a future event will affect feelings. Can lead to disproportionate effort to facilitate positive or prevent negative events.
- @eastwick_etal2008: Students predicted higher distress from a romantic breakup than they actually experienced.

**Emotional evanescence (duration):** Emotions fade more quickly than anticipated.

**Focalism:** A major cause of impact bias — overestimating how much a specific event would affect feelings and underestimating the influence of other concurrent events.

**Projection bias** [@loewenstein2005]: Projecting current mental/emotional state into the future. You use present-you as a model for future-you, but present-you is a poor model.

**Hot-cold empathy gap** [@loewenstein2005]: A specific form of projection bias — people in a "cold" (calm, rational) state cannot accurately predict how they would feel or act in a "hot" (emotional, visceral) state, and vice versa. Leads to underestimating the influence of hunger, pain, craving, or sexual arousal on future decisions. Implications for addiction, dieting, and advance decision-making.

**Disability paradox and living wills:** Healthy people predict they would prefer death over severe disability, but when actually sick, people often feel differently. @slevin_etal1990: Only 10% of healthy participants but 42% of cancer patients would accept chemotherapy for 3 extra months. This is projection bias in action — the healthy person's "cold" state cannot access the adaptive coping that emerges during actual illness. Living wills (advance directives) are a practical consequence of this problem: they increase concordance with patient wishes and reduce unwanted interventions [@brinkmanstoppelenburg_etal2014], but they are inherently limited by the affective forecasting errors of the healthy person who writes them.

**Peak-end rule:** Past experiences are evaluated based on the average of peak intensity and end-point, rather than total duration. @kahneman_etal1993: Participants preferred a longer pain episode that tapered off over a shorter one with the same peak. This matters for affective forecasting because people don't know in advance how they will *remember* an experience — they predict based on imagined total experience, but evaluate based on peak and end. This mismatch between anticipated and remembered experience is one reason forecasts go wrong.

**Temporal discounting:** While affective forecasting is about mispredicting future feelings (a cognitive failure), temporal discounting is about undervaluing future outcomes (a motivational failure). People place less value on future gains the farther away they are — choosing smaller-sooner rewards over larger-later ones. This is not about getting the prediction wrong, but about not caring enough about the person who will receive the outcome: your future self.

**The future self as a stranger:** @hershfield_etal2011 demonstrated the link directly: participants who viewed digitally aged avatars of themselves — making their future self feel less like a stranger — allocated significantly more to retirement savings. Temporal discounting decreases with age, possibly because the gap between present and future self narrows. This suggests that both forecasting errors and discounting errors share a common root: the psychological distance between you and the person you will become.

**🎯 Bayesian lens:** Both affective forecasting and temporal discounting are failures of prediction about the future self. The impact bias reflects poorly calibrated posteriors — too extreme relative to what the evidence (actual future experience) will support. Projection bias means using the wrong prior (current emotional state) instead of the appropriate one (the likely future state). Temporal discounting can be understood as implicitly assigning low prior probability to the future self's preferences mattering — a prior that Hershfield's intervention corrects by making the future self more vivid and real.

**Key references:** @wilson_gilbert2005; @kahneman_snell1992; @eastwick_etal2008; @kahneman_etal1993; @loewenstein2005; @brinkmanstoppelenburg_etal2014; @hershfield_etal2011

---

## Risk Perception

**Definition:** How people judge risks — often misaligned with evidence due to heuristic processing.

**Voluntary vs. involuntary risk** [@starr1969; @fischhoff_etal1978]: People accept roughly 1,000 times more risk for *voluntary* activities (e.g., skiing) than for *involuntary* ones (e.g., living near a chemical plant). This asymmetry reveals that risk perception is not about probabilities — it is about *how the risk feels*.

**Neglect of rare risks:** Extremely low probabilities are typically treated as zero — people simply ignore them. This means that many small but real risks (e.g., food contamination, household accidents) receive far less attention than their actual probability warrants.

**Dread risk as the exception:** The neglect of rare risks breaks down when a risk triggers *dread* — the feeling that a hazard is catastrophic, uncontrollable, and unfairly distributed [@slovic1987]. Dread flips a rare risk from invisible to massively overweighted. Characteristics that increase dread: newness, poor understanding, unobservability, involuntariness, catastrophic potential.
- Experts judge risk primarily by mortality rates; laypeople are driven by dread and perceived lack of knowledge. The higher the dread, the more risky people perceive an activity and the more they demand strict regulation.
- *Post-9/11 driving fatalities* [@gigerenzer2004]: A plane crash is objectively rare, but because it is a dread risk, the 9/11 attacks made flying feel impossibly dangerous. Americans avoided planes and drove instead → approximately 350 additional road deaths in the following months. Driving the same distance as the average U.S. flight is 65 times more dangerous, even including 9/11.
- *Madrid train bombings* [@lopezrousseau2005]: After the 2004 attacks, Spaniards reduced train *and* car travel → fewer car fatalities. A cultural contrast with the American response: dread led to avoidance of all travel rather than substitution to a more dangerous mode.

**Scope insensitivity** [@hsee_rottenstreich2004]: People's valuations are insensitive to the magnitude of a problem. Willingness to pay is nearly identical for saving 2,000 vs. 20,000 vs. 200,000 migratory birds. Driven by the affect heuristic — an emotional response is generated for the *category* (endangered birds) rather than scaled to the *quantity*. This has enormous implications for charitable giving and public policy: the difference between a small disaster and a massive one barely registers emotionally.

**Identifiable victim effect** [@small_loewenstein2003]: A single identified victim (with a name, face, story) generates more empathy and charitable giving than statistical information about thousands of victims. Combining statistical information with an identified victim can actually *reduce* giving — statistics trigger analytical thinking that dampens the emotional response [@small_etal2007]. This is scope insensitivity in action: one vivid case outweighs thousands of faceless cases.

**Risk communication — relative vs. absolute risk:**
- *Relative risk* (ratio or percentage change) sounds alarming: "twofold increase in blood clots."
- *Absolute risk* gives actual probabilities: "2 in 7,000 vs. 1 in 7,000."
- *Contraceptive pill scare* (mid-1990s UK): A "twofold increase" in blood clots led to widespread discontinuation of the pill and approximately 13,000 additional abortions — even though pregnancy carries a higher clot risk than the pill itself.
- Communicating risk as natural frequencies makes the underlying probabilities transparent and reduces misunderstanding (see [Bayesian Reasoning](#bayesian-reasoning)).

**Climate change and affect** [@weber2006]: Abstract statistics about global warming influence Type 2 reasoning but fail to trigger the Type 1 emotional response needed to motivate action. @akerlof_etal2013: People who believed they had *personally experienced* global warming showed elevated risk estimates — direct experience generates the affect that statistics cannot.

**🎯 Bayesian lens:** Risk perception errors involve distortions in either the prior (ignoring base rates of rare risks) or the evidence-weighting function (overweighting vivid/dread evidence, underweighting statistical evidence). Dread acts as an inflated likelihood ratio — a single catastrophic event updates the posterior far more than its base rate warrants. Scope insensitivity means the posterior does not scale with the magnitude of evidence. The identifiable victim effect shows that narrative evidence (a single case) updates beliefs more powerfully than statistical evidence (base rates) — the opposite of what Bayesian weighting would prescribe.

**Key references:** @slovic1987; @gigerenzer2004; @lopezrousseau2005; @hsee_rottenstreich2004; @small_loewenstein2003; @small_etal2007; @weber2006; @akerlof_etal2013; @starr1969; @fischhoff_etal1978

---

# Choice

---

## Gains and Losses

**From rational choice to prospect theory:** Expected value theory (EV = Σ(value × probability)) is the normative baseline for risky decisions. Expected utility theory (EU) extends this by replacing objective values with subjective utilities, and captures **risk aversion** — the tendency to prefer a sure outcome over a gamble with equal or higher expected value (demonstrated by refusal to play fair gambles where EV = 0). EU is generally normative, not descriptive.
- **The Allais Paradox** [@allais1953] exposes EU's descriptive failure: People prefer a sure €1,000 over a higher-EV gamble (the **certainty effect**), but when the same utilities appear at lower probabilities — removing certainty — they reverse preferences. This is logically inconsistent under EU, but predicted by prospect theory.

**Definition:** An influential descriptive model of risky choice [@kahneman_tversky1979] accounting for systematic departures from expected utility theory. Kahneman won the 2002 Nobel Prize in Economics for this work.

**Core assumptions:**
1. **Reference dependence:** People evaluate outcomes as gains or losses relative to a reference point (often current state or expectations), not as final wealth.
   - Olympic silver medalists appeared *less happy* than bronze medalists — silver compared to gold (loss), bronze compared to nothing (gain) [@medvec_etal1995].
2. **Biases in utility estimation (subjective value function, v):**
   - *Loss aversion:* Losses loom ~2.25× larger than equivalent gains.
   - *Diminishing sensitivity:* Concave for gains, convex for losses — small changes near the reference point have disproportionate impact.
   - Formally: v(x) = x^0.88 for gains; v(x) = −2.25(−x)^0.88 for losses.
3. **Biases in probability estimation (decision weight function, w):**
   - Overweight low probabilities (why people buy lottery tickets).
   - Underweight moderate-to-high probabilities.
   - Formally: w(P) = P^0.65 / (P^0.65 + (1−P)^0.65)^(1/0.65).

**Two stages of choice:**
- **Framing phase:** Simplify prospects — recode as gains/losses relative to reference point, separate certain from risky components, cancel identical pairs.
- **Valuation phase:** Compute overall value V = Σ(v(outcome) × w(probability)). Choose the prospect with highest V.

**Principle of invariance:** Preferences should not change when equivalent options are described differently. People systematically violate this:
- **Framing effects:** Gain frames → risk aversion; loss frames → risk seeking. @tversky_kahneman1981: "Save 200 of 600" → 72% chose sure option; "400 will die" → 78% chose gamble.
- **Procedure invariance:** Preferences change depending on whether asked to choose or reject. @shafir1993: A parent with extreme traits was both *chosen* (64%) and *rejected* (55%) for custody.

**Endowment effect:** People value items they own more than they would value acquiring the same items. @kahneman_etal1990: Sellers' median price > 2× buyers' price. Explained by loss aversion.

**🎯 Bayesian lens:** Prospect theory describes systematic distortions in how people weight probabilities — the decision weight function w(P) is a biased transformation of true probabilities. A Bayesian agent would use P directly; prospect-theory agents overweight small P and underweight large P. Framing effects show that the *same evidence* produces different posteriors depending on how it is presented — a direct violation of Bayesian invariance. The reference point functions as a prior: what counts as a "gain" or "loss" depends entirely on where one starts.

**Key references:** @edwards1954; @kahneman_tversky1979; @tversky_kahneman1981; @tversky_kahneman1992; @allais1953; @barberis2013

---

## Satisficing vs. Maximizing

**Core idea:** When faced with a set of options, people differ in how extensively they consider each option. This has important consequences for decision quality, effort, and well-being.

- **Satisficing** [@simon1956]: Selecting an option that is "good enough" — one that meets a minimum threshold of acceptability. The decision-maker stops searching as soon as a satisfactory option is found.
- **Maximizing:** Striving for the best possible option by exhaustively comparing all available alternatives. This sounds rational in theory, but in practice it is costly: it requires evaluating more options, making more comparisons, and often leads to greater regret (because the decision-maker is more aware of what they might have missed).
- **The maximizing paradox**: Maximizers tend to achieve objectively *better* outcomes than satisficers, but feel *worse* about them — experiencing more regret, less satisfaction, and more counterfactual thinking ("what if I had chosen differently?"). More choice can make maximizers worse off.
- **Choice overload** [@iyengar_lepper2000]: The maximizing paradox plays out dramatically when the number of options increases. In a famous demonstration, shoppers who encountered 24 jam samples were far less likely to buy (3%) than those who saw only 6 (30%). More choice should help maximizers find the best option, but instead it paralyzes them — the cost of exhaustive comparison becomes overwhelming. Satisficers, who stop at "good enough," are relatively immune.
- **Maximization Scale** [@schwartz_etal2002]: Individual differences in the tendency to maximize can be measured. Higher scores correlate with regret, depression, perfectionism, and neuroticism; lower scores with happiness, satisfaction, and optimism. Importantly, maximizing is *not* the same as having high standards — a person can have high standards while still satisficing (they simply set a high threshold for "good enough").
- Satisficing is a direct consequence of bounded rationality (→ [How It Is vs. How It Should Be](#how-it-is-vs-how-it-should-be)): because we lack the time, information, and cognitive capacity to evaluate all options, "good enough" is often the best we can do — and often leads to better subjective outcomes than relentless optimization.

**🎯 Bayesian lens:** Maximizing assumes you can compute the expected value of every option and select the highest — essentially a full Bayesian decision analysis. Satisficing acknowledges that this computation is often infeasible and replaces it with a simpler threshold rule: is the posterior probability that this option is "good enough" sufficiently high? This is a resource-rational strategy — trading a small expected loss in quality for a large saving in cognitive effort.

**Key references:** @simon1956; @schwartz_etal2002; @iyengar_lepper2000; @vargova_etal2020

---

## Steering Other People's Choices

**The tension — libertarian paternalism:** Every choice environment is designed by someone. No arrangement of options is truly neutral — the order, the default, the framing all influence what people choose. This creates a tension: people should be free to choose, but the environment inevitably steers them. **Libertarian paternalism** embraces this tension: institutions can and should design choice environments that steer people toward beneficial outcomes, while preserving the freedom to opt out. The question is not *whether* to influence, but *how*.

**Defaults and the status quo bias:** The most powerful nudge is simply pre-selecting the desired option. People tend to stick with whatever is already chosen — the **status quo bias** (preference for inaction over action). @johnson_goldstein2004: Austria's opt-out organ donation system → ~100% consent vs. Germany's opt-in system → 12%. Same choice, radically different outcome, driven entirely by the default.

**Other nudge types**:
- **Increasing ease and visibility** of the desired choice (e.g., placing healthy food at eye level in cafeterias).
- **Social pressure:** Making behavior visible or communicating social norms (e.g., "most of your neighbors have already paid their taxes").
- **Educational nudges:** Providing vivid information to shift preferences (e.g., graphic health warnings on tobacco packaging; meta-analyses suggest they increase willingness to quit, though effectiveness can wear off over time) [@pang_etal2021].

**Framing spending categories — mental accounting as a tool:** People do not treat all money as equivalent. They mentally categorize resources into separate accounts — salary, bonuses, savings, windfalls — and spend from each category differently, violating the **principle of fungibility** [@thaler1999]. A bonus feels like "free money" and gets spent more freely than the same amount received as salary. Choice architects can exploit this:
- **Earmarked subsidies and vouchers** are spent on their intended purpose precisely because people respect the category label.
- **Commitment devices** steer future behavior by moving resources into harder-to-access accounts (e.g., automatic pension deductions), exploiting the reluctance to spend savings [@shefrin_thaler1988].

**Mandates, bans, and economic incentives:** At the other end of the spectrum, interventions can remove options entirely (bans) or attach monetary consequences to choices (taxes, subsidies). These are effective but sacrifice the "libertarian" part of libertarian paternalism — they constrain rather than steer.

**🎯 Bayesian lens:** Choice architecture manipulates the prior. Defaults set a strong prior that most people never override — equivalent to starting with a heavily weighted anchor. The status quo bias reflects an asymmetry in updating: maintaining the current state requires no evidence, while switching requires overcoming an evidentiary threshold. Nudges work precisely because people are not fully Bayesian — a rational agent would choose identically regardless of default framing. Mental accounting violates Bayesian rationality because the *label* on a resource should carry no informational value, yet it shifts spending behavior as if it were new evidence.

**Key references:** @johnson_goldstein2004; @thaler1999; @shefrin_thaler1988; @pang_etal2021; @lin_etal2017;

---

## Group Decisions

**Core idea:** Many consequential decisions are made by groups (committees, juries, teams, boards). Group processes can improve or degrade decision quality compared to individuals.

**Wisdom of crowds** [@galton1907]: Aggregating many independent judgments often produces remarkably accurate estimates — sometimes outperforming individual experts. The mechanism is essentially the law of large numbers: each individual judgment can be thought of as a true value plus measurement noise; when many such judgments are averaged, the noise cancels out and the aggregate converges on the true value. Students familiar with statistics will recognize this: individual judgments are like individual observations in a sample, and the group average is like the sample mean. Key conditions for this to work: diversity of opinion, independence (judgments not influenced by each other), and a mechanism for aggregation. The wisdom of crowds breaks down when independence is violated — just as in statistics, correlated observations do not reduce noise. Social influence, shared information sources, or groupthink can all destroy independence.

**Group polarization** [@moscovici_zavalloni1969]: After group discussion, individual members tend to hold more extreme positions than they held before the discussion — and they do so privately, not just publicly. This is not merely about the group reaching an extreme collective decision; each person individually shifts. If most members initially lean toward risk, each member becomes personally more risk-seeking after discussion; if most initially lean toward caution, each becomes more cautious. Two mechanisms drive this: persuasive arguments (during discussion, members encounter novel arguments supporting the dominant view, which genuinely change their minds) and social comparison (members compete to embody the group's valued position, pushing each other further).

**Groupthink**: Highly cohesive groups with strong leaders may prioritize consensus over critical evaluation, leading to poor decisions. Where group polarization changes members' minds through persuasion, groupthink silences dissent through conformity pressure. Members may privately have doubts, but suppress them to maintain harmony. Symptoms include: illusion of invulnerability, collective rationalization, stereotyping of outgroups, self-censorship, and illusion of unanimity. Classic cases: Bay of Pigs, Challenger disaster. The relationship between polarization and groupthink is important: both can produce a uniform, extreme group position, but through different mechanisms — polarization *convinces* you, groupthink *silences* you. In practice, they often co-occur: polarization pushes the group in one direction, and groupthink prevents anyone from pushing back. Preventive measures: assign a devil's advocate, encourage dissent, consult external experts. Janis's book "Victims of Groupthink" (discussed in @hart1991) was highly influential in putting these phenomena on the map.

**Shared information bias** [@stasser_titus1985]: Groups spend disproportionate time discussing information already known to all members and neglect unique information held by individual members — even when the unique information would change the decision. This is a failure of information pooling: the group functions as if it has one shared mind rather than multiple independent perspectives. Structured information-sharing protocols can mitigate this.

**🎯 Bayesian lens:** The wisdom of crowds works because aggregation approximates Bayesian integration — each person's independent estimate is a noisy signal, and averaging reduces noise, converging on the true posterior. Groupthink and group polarization represent failures of independent evidence sampling: when group members share the same prior and the same biased evidence, the group's "posterior" becomes more extreme without genuinely new evidence — a form of collective overconfidence. Shared information bias means the group updates from redundant evidence (shared information) while ignoring unique diagnostic evidence — like a Bayesian agent who counts the same datum multiple times.

**Key references:** @galton1907; @moscovici_zavalloni1969; @stasser_titus1985
---

# Belief

---

## Confirmation

**Definition:** A pervasive tendency to seek, interpret, and favor information that confirms existing beliefs or hypotheses. Proposed as the single cognitive bias most relevant to ideological extremism.

**Confirmatory evidence and the positive test strategy:** Confirmatory evidence is consistent with a hypothesis but cannot definitively prove it. Yet people naturally gravitate toward it — the *positive test strategy* involves examining instances where the hypothesized property is expected to occur. This is confirmation bias at work: we default to looking for evidence that fits. *Example:* A manager believes that older employees resist new technology. She notices every time a senior colleague struggles with a software update — each case *confirms* her hypothesis. But she never checks whether younger employees struggle just as often (which would be disconfirmatory). The confirmatory evidence accumulates, and the hypothesis feels increasingly certain — even though it was never properly tested.

**Disconfirmatory evidence and the negative test strategy:** Disconfirmatory evidence refutes a hypothesis. A single piece can topple a hypothesis — making it uniquely powerful. The *negative test strategy* involves deliberately seeking cases that *disconfirm* the hypothesis. This goes against our natural confirmation tendency and requires effortful, System 2 thinking. It connects to **falsifiability**, a term connected to the philosopher of science Karl Popper: science should center on attempting to disconfirm hypotheses. In practice, people rarely do this spontaneously. *Example:* The manager above could actively look for older employees who *do* adopt new technology easily, or younger employees who *don't*. Finding even a few such cases would seriously weaken her hypothesis — far more informative than adding another confirmatory case to the pile.

**2-4-6 task** [@wason1960]: Demonstrates both strategies. Participants are told that the sequence 2-4-6 fits a rule, and must discover the rule by proposing new sequences. The actual rule is simply *any three ascending numbers* — but most participants hypothesize a more specific rule, such as "even numbers ascending by 2." They then test confirming sequences (e.g., 8-10-12, 20-22-24) — all of which fit the true rule, reinforcing the wrong hypothesis. Only 21% found the actual rule. Those who succeeded employed the negative test strategy: testing sequences that *violated* their hypothesis, such as 1-3-5 (odd numbers — still ascending, so "yes") or 1-2-3 (ascending by 1 — still "yes") or 6-4-2 (descending — finally "no"). By discovering what *doesn't* work, they narrowed down the real rule.

**Consistency fallacy**: Confirmation bias is not only about favoring beliefs we are personally invested in — it reflects a more general cognitive pull toward confirmatory patterns. Data that merely *confirm* a hypothesis are misinterpreted as proving it, even for neutral hypotheses. A striking example: people are more convinced by psychological explanations accompanied by neuroscience descriptions, even irrelevant ones [@weisberg_etal2008]. The colorful fMRI brain scan *looks* like confirmatory evidence, making the explanation feel more scientific — even though it adds no actual support.

**🎯 Bayesian lens:** A Bayesian agent should weight evidence symmetrically — updating equally from confirming and disconfirming evidence (proportional to their diagnosticity). Confirmation bias produces *asymmetric updating*: confirming evidence strengthens beliefs while disconfirming evidence is discounted or ignored. This creates a self-reinforcing cycle where the posterior drifts ever further from what balanced evidence would warrant. A single disconfirming observation can be enormously informative (high likelihood ratio), yet people treat it as if it has low diagnosticity.

**Key references:** @klayman_ha1987; @nickerson1998; @wason1960; @weisberg_etal2008

---

## Belief Formation and Perseverance

**How beliefs form and persist** All points in this section flow from the foundational insight of automatic acceptance.

**Spinozan belief (automatic acceptance)** [@gilbert1991]: Following Spinoza, people automatically accept information in the process of understanding it. Rejecting false information requires a subsequent deliberate evaluation. When this process is disrupted (interruption, time pressure, cognitive load), people fail to reject falsehoods.
- @gilbert_etal1990: Interruption during true/false identification had no effect on recognizing true statements, but severely impaired identifying false statements — strong tendency to say "true."

**Executive control as override:** Higher CRT scores predict less acceptance of paranormal and irrational beliefs. Consistent with the Spinozan hypothesis: people are natural believers who can become skeptics with effort. Paranormal beliefs (astrology, telekinesis, superstitions) are incredibly common among ordinary adults — a testament to how rarely System 2 overrides the default acceptance.

**Belief perseverance:** Once automatically accepted, beliefs are incredibly resistant to contradictory evidence — the belief is *explicitly maintained* in the face of counterevidence. People who show belief perseverance also tend to presume intentionality and prefer simple causal explanations.

**Continued influence effect:** Distinct from perseverance: the erroneous belief is *explicitly abandoned* and the correction is understood and accepted — yet the original misinformation still exerts influence on subsequent judgments. Retraction never fully erases misinformation influence.
- *Warehouse fire studies:* Even with retraction, judgments continued to reflect misinformation. Adding "clarifying" negated statements can produce a **rebound effect**, making misinformation *more* influential.

**Myth-versus-fact effect:** A specific case of continued influence driven by familiarity. Repeated exposure to a statement — even in a context that labels it false — increases its perceived truth.
- @schwarz_etal2007: 30 minutes after reading a myth-vs-fact handout, people were *more likely* to misidentify myths as facts and *less likely* to intend vaccination.

**When beliefs are challenged** the following phenomena come into play:

**Reactance** [@rosenberg_siegel2018]: A strong physiological response when freedom to think or act is threatened, intensifying the intent to do the opposite of what is asked. This is a gut-feeling response — not a deliberate choice to resist. Reactance theory was first introduced by Jack Brehm.

**Cognitive dissonance:** Distinct from reactance. Mental discomfort from internal conflict (e.g., existing beliefs vs. new evidence). To reduce the discomfort, people either update their beliefs or reject/question the threatening evidence. The latter path leads to belief perseverance; the former is genuine learning.

**Mechanisms that protect beliefs** are the following:

**Biases and heuristics that protect beliefs (System 1 mechanisms):** Mere exposure (familiar = true), availability heuristic (easy-to-recall = true), confirmation bias (seek confirming information), source amnesia (forget where we learned something). Together, these make it hard to be aware of something without believing it.

**Sunk cost as behavioral perseverance:** Continuing to invest in a losing course because of what has already been spent, even though sunk costs should be irrelevant. This is perseverance extended to behavior: the prior commitment, rather than a prior belief, resists updating.
- @arkes_blumer1985: 54% chose a more expensive but less enjoyable ski trip; 85% continued funding a near-complete project vs. 17% when no prior investment existed.
- Develops with age and socialization (the "don't waste" heuristic) [@arkes_ayton1999].

**🎯 Bayesian lens:** Spinozan acceptance means all incoming information is initially assigned a high prior (P(true) is the default), requiring effortful System 2 processing to revise downward. Belief perseverance represents a failure to update — the prior is treated as virtually certain (P ≈ 1), making any single piece of counter-evidence insufficient to shift the posterior. The continued influence effect shows that even after a "retraction update," the original information retains residual influence on the posterior — the update is incomplete. Reactance and cognitive dissonance are emotional responses that block the update process altogether.

**Key references:** @gilbert1991; @lewandowsky_etal2012; @schwarz_etal2007; @rosenberg_siegel2018; @arkes_blumer1985; @arkes_ayton1999

---

## Conspiracy Theories

**Conspiracy theories:** Explanations invoking secret plots by powerful people. Can be false, partially true, or completely true. A key characteristic: contradictory evidence is absorbed into the theory by claiming it is part of the cover-up. People may endorse mutually contradictory conspiracies simultaneously [@wood_etal2012: believing both that Diana faked her death *and* was murdered].

**Cognitive and personality factors** that positively correlate with conspiracy thinking: seeing patterns in randomness (apophenia), paranormal beliefs, attributing agency where it doesn't exist, preferring simple explanations, narcissism, and being male. Negatively correlated with intelligence and analytical thinking [@swami_etal2014]. Apophenia and agency detection suggest that conspiracy thinking is partly a byproduct of pattern-recognition systems that are tuned for sensitivity over accuracy — the same System 1 mechanisms that produce superstitious and paranormal beliefs (see [Belief Formation and Perseverance](#belief-formation-and-perseverance)). [ref needed for personality factors; @douglas_etal2017 reviews many of these]

**Existential factors:** Conspiracy theories may help deal with existential threats by regaining a sense of control through explaining the unexplainable.

**Social factors:** Often have ingroup–outgroup structure ("we" the noble oppressed vs. "they" the conspiring elite). Related to populism. More common in disadvantaged groups.

**Echo chambers and groupthink:** Conspiracy beliefs are rarely formed in isolation. They thrive in communities where group polarization ([Group Decisions](#group-decisions)) pushes members toward increasingly extreme positions, groupthink ([Group Decisions](#group-decisions)) suppresses dissent (questioning the conspiracy risks being labeled a shill or part of the cover-up), and shared information bias ([Group Decisions](#group-decisions)) ensures only confirming evidence is discussed. Social media algorithms ([Populism and Social Media](#populism-and-social-media)) function as modern echo chambers, creating filter bubbles that accelerate this process. The self-sealing nature of conspiracy theories makes these groups particularly resistant to correction from outside.

**Rejection of science:** A form of conspiracy thinking, built on beliefs that scientists have hidden agendas.
- @lewandowsky_etal2013: Free-market ideology strongly predicted rejecting climate science and the smoking–cancer link but not HIV–AIDS. Conspiracy thinking predicted rejection of all science findings.

**🎯 Bayesian lens:** Conspiracy theories are self-sealing belief systems: the prior P(conspiracy) is set so high that *all evidence* — supporting or contradicting — is reinterpreted to increase the posterior. Disconfirming evidence is recoded as confirming ("that's exactly what they'd want you to think"). This makes the belief unfalsifiable and immune to Bayesian updating. Endorsing mutually contradictory conspiracies reveals that the updating is not about specific evidence at all, but about a meta-prior: "powerful people are conspiring." Rejection of science involves discounting the credibility of evidence sources, effectively setting the likelihood of scientific evidence to near zero.

**Key references:** @douglas_sutton2008; @wood_etal2012; @lewandowsky_etal2013; @douglas_etal2017; @douglas_etal2019; @swami_etal2014
---

# Morality and Cooperation

---

## Morality

**Moral judgment as belief formation:** Moral judgments are beliefs about whether something is right or wrong. They follow many of the same principles as other beliefs — formed quickly, resistant to updating, shaped by System 1 and System 2 — but carry special weight: people consider morality an essential component of identity, more so than memories, personality, or mental abilities [@strohminger_nichols2014]. The central theoretical question is whether moral judgments arise primarily from rational deliberation (System 2) or gut feeling (System 1).

**Rationalist models (System 2):** These models hold that people first consciously reason through a moral problem, then arrive at a judgment.
- **Kohlberg's stages of moral development** [@kohlberg1971]: Children develop moral reasoning over six stages in three levels: pre-conventional (seeking rewards, avoiding punishment), conventional (upholding social conventions and rules), post-conventional (universal moral principles; may protest unjust laws). Responses classified by *reasons given*, not the answer itself.
- **Social interactionist model**: Classified as rationalist because it assumes children arrive at moral judgments through *deliberate reasoning* about consequences — evaluating whether an action causes harm, violates fairness, or merely breaks a social convention. Proposes three domains: personal, moral (inherently harmful), and social (violating local rules). Children as young as 5–6 distinguish social conventions from moral principles. @haidt_etal1993: High-SES people classified offensive-but-harmless actions as social conventions; low-SES classified them as moral — suggesting the boundary between domains is culturally shaped.

**Intuitionist models (System 1):** These models hold that moral judgments are primarily driven by gut feelings, with reasoning coming *after* as post-hoc justification.
- **Social intuitionist model** [@haidt2001]: Moral judgments arise from fast, automatic intuitions. Reasoning serves to justify rather than generate them.
- *Moral dumbfounding:* People hold definite moral opinions but cannot produce clear reasons — suggesting the judgment came first, the reasoning second.
- **Wag-the-dog illusion:** The mistaken belief that our moral judgment is driven by our reasoning.
- **Wag-the-other-dog's-tail illusion:** The mistaken belief that rebutting someone's reasoning will change their moral position. Instead, change their emotional response.
- **Moral Foundations Theory** [@graham_etal2009]: Describes the *content* of moral intuitions across five dimensions: Harm, Fairness, Ingroup, Authority, Purity. US liberals emphasize harm and fairness; US conservatives place relatively more weight on ingroup, authority, and purity.

**Emotion as self-perception and evolutionary roots:** If moral judgments are driven by bodily gut feelings, where do those feelings come from? @james1884 proposed that emotion derives *first* from a bodily response, which is then shaped by cognitive appraisal. Bodily states such as hunger can intensify emotional responses to neutral stimuli [@maccormack_lindquist2018]. From an evolutionary perspective, these bodily moral responses are adaptive: Darwin argued that any sufficiently social and intelligent animal would develop a moral sense. Many species show empathy, retribution, and fairness — capuchin monkeys become visibly upset when a partner receives a better reward for the same task [@dewaal2003]. Morality, understood as cooperation, exists at all levels of biological organization.

**Affect as information and somatic markers:** These two frameworks describe the same core insight — that feelings serve as informational input to judgment — but from different perspectives.
- **Affect-as-information heuristic** [@schwarz_clore1983]: The psychological principle. People consult their current feeling state as a cue for judgment: "How do I feel about this?" If the feeling is positive, the judgment is favorable. This is a general heuristic that applies broadly (including moral judgments), and it explains why incidental mood (e.g., sunny weather) can influence unrelated evaluations.
- **Somatic marker hypothesis** [@bechara_etal2000]: The neurobiological implementation. The affective signals used as information are specifically *bodily* states — gut feelings, skin conductance, heart rate changes — that mark options as good or bad. Without these somatic markers (due to ventromedial prefrontal cortex damage), people cannot learn from emotional feedback: on the Iowa Gambling Task, they continue choosing from disadvantageous decks despite repeated losses, even while their reasoning remains intact. This demonstrates that rational analysis alone is insufficient — the emotional body plays a necessary role.
- **Trolley vs. footbridge — somatic markers in action:** The trolley dilemma (flip a switch to divert a trolley from five people to one) and the footbridge dilemma (push a stranger off a bridge to stop the trolley) have identical utilitarian structure but trigger very different judgments. Most people flip the switch but refuse to push. The difference is somatic: pushing someone activates a visceral bodily response that flipping a switch does not. Brain imaging confirms heightened emotional-area activation in personal dilemmas [@greene_etal2001]. Crucially, manipulating bodily states directly changes moral judgment — positive mood increases willingness to push [@valdesolo_desteno2006], while induced disgust (fart spray: @schnall_etal2008) and bitter tastes [@eskine_etal2011] decrease moral leniency.
- **Omission bias:** The tendency to judge harmful *actions* as worse than equally harmful *omissions*. Doing nothing *feels* less bad than actively causing harm — the somatic signal from acting is stronger, even when outcomes are identical or worse. Relevant to vaccination (perceived risk of acting > not acting) and end-of-life decisions (withdrawing treatment vs. not starting it). Connects to status quo bias ([Steering Other People's Choices](#steering-other-peoples-choices)).

**🎯 Bayesian lens:** Moral intuitions function as strong priors: formed early, felt with certainty, and resistant to updating. The social intuitionist model implies that moral reasoning is not Bayesian belief-updating from evidence but post-hoc rationalization of a pre-set prior. Changing moral positions requires changing the prior (emotional intuition), not presenting disconfirming evidence (rational argument). Moral Foundations Theory describes the *content* of these priors, which vary systematically across individuals and cultures. The somatic marker hypothesis suggests these priors are literally embodied — encoded in bodily sensations, not just cognitive representations. In trolley vs. footbridge, the emotional prior (do not harm directly) overwhelms utilitarian calculation in personal dilemmas but not impersonal ones. Omission bias reflects a prior that inaction is morally neutral — evidence about equivalent outcomes is insufficient to overcome it.

**Key references:** @james1884; @kohlberg1971; @haidt2001; @graham_etal2009; @schwarz_clore1983; @bechara_etal2000; @greene_etal2001; @valdesolo_desteno2006; @strohminger_nichols2014; @dewaal2003; @maccormack_lindquist2018
---

## Cooperation

Decisions to cooperate (or not) pit personal interest against the greater good. These decisions draw on moral judgments ([Morality](#morality)), framing ([Gains and Losses](#gains-and-losses)), System 1 intuitions vs. System 2 calculation ([Reason and Intuition](#reason-and-intuition)), and social norms. Game theory provides the formal framework for studying how these factors interact.

**The core tension:** In many social situations, individual rationality leads to collective irrationality. Each person maximizing their own payoff produces outcomes that are worse for everyone — a theme that unites all paradigms below.

**Tragedy of the commons** [@hardin1968]: Multiple individuals sharing a common resource each try to increase personal wealth, leading to destruction of the resource for everyone. Real-world examples: overfishing, climate change. The tragedy arises because the personal benefit of exploiting the resource is immediate and concrete (System 1), while the collective cost is distant and abstract (requires System 2 reasoning to appreciate).

**Prisoner's dilemma** [@flood1958; @tucker1983]: Two players choose to cooperate or defect. The **Nash equilibrium** predicts mutual defection (the rational choice for each individual), yet behavioral studies show substantial cooperation (~55% among German prisoners; @khadjavi_lange2013). This gap between prediction and behavior suggests that moral intuitions — fairness, reciprocity — override pure self-interest.

**Ultimatum game** [@guth_etal1982]: A proposer offers a split of money; the responder can accept or reject (both get nothing if rejected). Rational prediction: the proposer offers the minimum, the responder accepts anything > 0. Reality: offers below ~30% are typically rejected. Responders *pay* to punish unfairness — sacrificing personal gain to enforce a moral norm. This connects directly to somatic markers ([Morality](#morality)): unfairness triggers a visceral "that's not right" response that overrides rational calculation.

**Dictator game:** Like the ultimatum game, but the responder has no power to reject — the proposer simply decides. Even here, proposers typically give away ~20–30%. With no strategic incentive to be fair, this suggests genuine moral motivation (altruism or internalized norms), not just fear of punishment.

**Trust game** [@berg_etal1995]: Player 1 sends money to Player 2 (the amount is tripled), and Player 2 decides how much to return. Tests trust (Player 1's willingness to be vulnerable) and reciprocity (Player 2's willingness to return fairly). Cooperation requires a leap of faith — a prior belief that others will reciprocate — which connects to Bayesian updating about others' intentions.

**Public goods game:** Players contribute (or not) to a shared pool that is multiplied and redistributed. Classic rationality predicts free riding (benefiting without contributing), yet cooperation rates start around 40–60%. Key twist: **altruistic punishment** [@fehr_gachter2002] — when players can pay to punish free riders, cooperation increases dramatically. People sacrifice personal resources to enforce norms, which is irrational from a self-interest perspective but essential for maintaining group cooperation. Like the ultimatum game, this suggests a moral enforcement mechanism rooted in affect.

**Framing effects on cooperation** [@liberman_etal2004]: The same prisoner's dilemma game was presented as either the "Wall Street Game" or the "Community Game." Cooperation roughly doubled under the community frame. The strategic structure was identical — only the label changed. This demonstrates that cooperative decisions are shaped by the same framing effects that influence other judgments throughout this book ([Gains and Losses](#gains-and-losses), [Steering Other People's Choices](#steering-other-peoples-choices)), activating different moral identities and social norms.

**Intuitive cooperation** [@rand_etal2012]: When forced to decide quickly (under time pressure), people cooperate *more*. When given time to deliberate, they cooperate *less*. This suggests that cooperation is a System 1 default — an automatic, intuitive response — while defection requires System 2 deliberation to override the cooperative impulse. This finding bridges game theory back to the dual-process framework ([Reason and Intuition](#reason-and-intuition)) and the intuitionist model of moral judgment ([Morality](#morality)).

**🎯 Bayesian lens:** Strategic interaction requires maintaining and updating beliefs about others' likely behavior. Each round provides evidence about the other's type (cooperative vs. selfish). The trust game makes this explicit: Player 1's decision to send money reflects their prior about reciprocity, which is updated based on experience. At the group level, the tragedy of the commons illustrates that locally rational Bayesian agents — each optimizing their own expected payoff — can collectively produce irrational outcomes.

**Key references:** @hardin1968; @nash1950; @guth_etal1982; @berg_etal1995; @fehr_gachter2002; @liberman_etal2004; @rand_etal2012; @parks_etal2013
---

# Real Life

---

## Medical Decision-Making

**Doctors are human too:** All the heuristics, biases, and decision-making patterns covered throughout this book apply to medical professionals. Doctors deal with imperfect information under time pressure — conditions that favor System 1 reasoning and its associated biases (see [Reason and Intuition](#reason-and-intuition)). Understanding these biases is critical because medical decisions have life-or-death consequences.

The following **Heuristics and biases** play a role in medical decision-making:
- **Availability in diagnosis:** Recently seen cases influence diagnosis of new cases (see [Availability](#availability)). A doctor who has just treated several patients with a rare disease is more likely to diagnose it in the next ambiguous case. Counterintuitively, this effect may *increase* with expertise, because experienced clinicians have richer memories to draw on.
- **Anchoring in diagnosis:** Clinicians anchor on initial hypotheses and distort subsequent cues to fit (see [Anchoring and Primacy](#anchoring-and-primacy)). This is related to availability: the first hypothesis that comes to mind — often the most *available* one — becomes the anchor. Experience reduces but does not eliminate susceptibility.
- **Confirmation bias in diagnosis:** Once an initial hypothesis is anchored, clinicians tend to seek confirmatory evidence (see [Confirmation](#confirmation)). @mendel_etal2011 found that both psychiatrists (13%) and students (25%) using confirmatory strategies were much more likely to make wrong diagnoses. However, a confirmatory strategy is efficient *when the initial hypothesis is correct* — the problem arises specifically when anchored on the wrong diagnosis.

These biases can be reduced in two main ways:
- **Decision support systems:** Structured tools can counteract heuristic-driven errors. They are most effective when computerized, built into clinical workflow, and providing both diagnoses and treatment recommendations — essentially replacing intuitive judgment with systematic evidence evaluation.
- **Natural frequencies and Bayes' theorem:** Physicians reason far more accurately about diagnostic probabilities when given natural frequencies rather than conditional probabilities (see [Bayesian Reasoning](#bayesian-reasoning)). For example, understanding that "10 out of 1,000 patients have this disease, and 8 of those 10 will test positive" is far easier than processing sensitivity and specificity as percentages. Training clinicians to think in natural frequencies is a simple but powerful debiasing intervention.

**Causal reasoning** is also important in clinical judgment: Clinicians hold causal models of mental disorders that function as schemas (see [Mental Models](#mental-models), [Cues to Causality](#cues-to-causality), [Blame, Praise, and Responsibility](#blame-praise-and-responsibility), and [Learning Causality](#learning-causality)). They show significant agreement on causal structure, weight causally central symptoms more heavily — even though the DSM gives equal weight to all symptoms — and their treatment recommendations can be predicted from their causal models.
- @kim_ahn2002a; @kim_ahn2002b: Clinicians agreed on causal models and diagnosed based on causal centrality.
- @flores_etal2014: Causally inconsistent temporal order of symptoms slowed reading and reduced diagnostic agreement.
- @delosreyes_marsh2011: Non-symptom contextual information strongly influenced conduct disorder judgments.

**🎯 Bayesian lens:** Medical diagnosis is Bayesian updating in action: the physician starts with a prior (base rate of the disease, patient demographics), gathers evidence (symptoms, tests), and arrives at a posterior (diagnostic probability). Every bias in clinical reasoning maps onto a specific Bayesian failure: anchoring = sticky prior, availability = biased evidence sampling, confirmation bias = asymmetric updating. Decision support systems and natural-frequency training improve decisions precisely because they formalize the Bayesian computation that clinicians perform intuitively and imperfectly.

**Key references:** @kim_ahn2002a; @kim_ahn2002b; @flores_etal2014; @mendel_etal2011; @delosreyes_marsh2011; @hoffrage_gigerenzer1998

---

## Legal Decision-Making

**Opening framing:** Police officers, forensic experts, and judges are human decision-makers subject to the same cognitive biases discussed throughout this book. Legal contexts are particularly high-stakes — errors can mean wrongful convictions or guilty parties going free.

**Heuristics and biases in legal contexts:**

- **Availability heuristic** (→ [Availability](#availability)): Recent or vivid cases influence legal decision-making. A judge who has recently handled a violent crime may perceive subsequent defendants as more dangerous, shifting sentencing upward — not because the evidence warrants it, but because similar cases come to mind easily.
- **Forensic confirmation bias** (→ [Confirmation](#confirmation)): Prior expectations influence evidence collection and interpretation in criminal cases. Once an investigator or expert forms a hypothesis about a suspect, they tend to seek and interpret evidence in line with that hypothesis.
  - *Madrid bombings fingerprint* [@oig2006]: Three FBI experts matched a print to an innocent man; they began "finding" additional features suggested by the suspect's prints.
  - @dror_charlton2006: Practicing fingerprint experts' identifications were influenced by background case information.
- **Anchoring in sentencing** (→ [Anchoring and Primacy](#anchoring-and-primacy)): Sentencing decisions are influenced by the prosecution's demand, even when it is arbitrary. @englich_mussweiler2001 [ref to verify]: Even randomly generated numbers influenced sentencing recommendations by experienced judges.
- **Representativeness and racial bias** (→ [Representativeness](#representativeness)): Defendants who more closely match the stereotypical prototype of a "criminal" receive harsher sentences. @blair_etal2004: More Afrocentric facial features predicted longer sentences, *even controlling for the defendant's race*. This is the representativeness heuristic applied to people — judgment driven by similarity to a category prototype rather than by case-specific evidence.
- **Bodily states and sentencing** (→ [Morality](#morality), somatic markers / affect-as-information): Judges' bodily states influence their decisions. @danziger_etal2011: Israeli parole board judges were far more likely to grant parole right after food breaks, with approval rates dropping to nearly zero just before breaks — suggesting that hunger and fatigue shift decision-making toward harsher defaults. [Note: this finding has been contested due to possible scheduling confounds; present with caveat.]

**Counteracting biases — and how this can backfire:**

- **Linear processing** as a debiasing strategy: Analyze each piece of evidence fully before comparing to suspect information, preventing prior expectations from contaminating evidence evaluation (→ [Heuristics and Biases](#heuristics-and-biases), debiasing).
- **But instructions to disregard can backfire** (→ [Belief Formation and Perseverance](#belief-formation-and-perseverance), reactance): Telling legal decision-makers to disregard inadmissible evidence can paradoxically increase its influence, because the instruction draws attention to the evidence and triggers reactance.

**Causal reasoning and narrative construction:**

- **Story model** [@pennington_hastie1986; @pennington_hastie1988; @pennington_hastie1992]: Legal decision-makers do not weigh evidence piece by piece. Instead, they construct a coherent, temporally ordered narrative using an **episode schema** (→ [Mental Models](#mental-models)), then seek a match between their story and verdict categories. ~45% of story elements are inferences about mental states and goals rather than direct testimony. Decision-makers watching the same trial can reach opposite verdicts because they constructed different stories.
- **Temporal order** (→ [Cues to Causality](#cues-to-causality)): Evidence presented in temporal (causal) order is more persuasive. @pennington_hastie1988: Guilty verdicts were most likely when the prosecution's evidence followed temporal order and the defense's was scrambled. This connects back to cues to causality — temporal order creates a sense of causal coherence that strengthens the narrative.
- **Information integration theory** [@kaplan_kemmerick1974]: An alternative, more normative model. Each piece of evidence has a guilt/innocence value, weighted by importance, and combined with the decision-maker's prior — essentially a weighted averaging process. In practice, the story model better describes how people actually reason, while information integration theory describes how they *should*.

**🎯 Bayesian lens:** The legal process is formally structured as sequential Bayesian updating: decision-makers start with a prior (presumption of innocence), receive evidence sequentially, and arrive at a posterior (guilt beyond reasonable doubt). Information integration theory captures this structure explicitly. But the story model reveals the descriptive reality: decision-makers construct holistic narratives rather than updating incrementally — their prior shapes how they *interpret* evidence, rather than evidence updating their prior. Forensic confirmation bias is this Bayesian failure in its most consequential form.

**Key references:** @pennington_hastie1986; @pennington_hastie1988; @pennington_hastie1992; @kassin_etal2013; @dror_charlton2006; @englich_mussweiler2001 [ref to verify]; @blair_etal2004; @danziger_etal2011 [contested]; @kaplan_kemmerick1974; @oig2006

---

## Populism and Social Media

**A new and powerful force:** Social media is a relatively new phenomenon that has become immensely important in shaping society. Digital platforms for user-generated content now reach ~5 billion users worldwide (~2.5 hours/day). The effects of social media on individuals and societies are not fully understood yet. However, there is strong reason to believe that social media, populism, and misinformation form self-reinforcing loops: social media amplifies populist messages → populist leaders exploit social media → misinformation fuels both → algorithms accelerate everything. Understanding these loops draws on many concepts from throughout this book.

**Populism:** A political approach appealing to "ordinary people" who don't consider themselves part of the ruling class. Features: mistrust of the ruling class, nationalism, moral outrage, strong leader, promise of change, traditional values. Exists across the political spectrum. Populism existed long before social media — but social media has given it a powerful new vehicle.

**Loss framing and populist rhetoric:** Populist messages are often framed in terms of loss — "we're losing our country," "they're taking your jobs," "our traditions are disappearing." As prospect theory predicts (see [Gains and Losses](#gains-and-losses)), loss framing triggers risk-seeking behavior: when people feel they are losing, they become receptive to extreme political options they would normally reject. This is a deviation from the usual tendency toward risk aversion, and populist leaders exploit it systematically.

**Social media as a catalyst:** Social media is not the root cause of populism, but it amplifies populist messages disproportionately. @guriev_etal2020: 3G mobile internet rollout predicted decreased government approval and more populist votes worldwide. @lorenzspreen_etal2023: Digital media increased political participation but also hate, polarization, and populism.

**Moral outrage as engagement fuel:** Morally outraged content strongly attracts attention — consistent with the negativity bias and the affect-as-information heuristic (see [Morality](#morality)): content that triggers strong bodily responses (anger, disgust) captures attention and feels important. Very few users create morally outraged content (associated with dark-triad personality traits), but it is widely shared. @rathje_etal2021: Out-group language substantially increased engagement. @humprecht_etal2024: Populist politicians' posts generated disproportionately more "angry" reactions.

**Algorithms and echo chambers:** Algorithms boost popular content, creating a semi-random winner-takes-all process. Typical winners: extreme views and moral outrage. This creates echo chambers at scale — connecting back to group polarization and groupthink (see [Group Decisions](#group-decisions)): within these algorithmically curated groups, members polarize toward more extreme views while dissent is suppressed. @larooij_tornberg2025: Six algorithmic changes produced only modest effects — attention inequality and polarization appear partly inherent to user-generated content platforms. See also [Conspiracy Theories](#conspiracy-theories) (conspiracy theories thrive in these same echo chambers).

**Misinformation and Spinozan acceptance:** Lies and half-truths spread organically on social media. The sheer volume and speed of information overwhelms System 2's capacity to evaluate (see [Belief Formation and Perseverance](#belief-formation-and-perseverance)): Spinozan acceptance means information is believed by default, and correction requires effortful processing that the endless scroll of social media actively undermines. @schaffner_luks2018: Highly educated Trump voters incorrectly chose Trump's inauguration photo as more attended — possibly participatory propaganda rather than genuine belief, suggesting the relationship between misinformation and belief is complex.

**Social media as a strategic tool:** Populist leaders may strategically use social media to divert attention from damaging coverage — exploiting the availability heuristic (see [Availability](#availability)) by flooding the information environment with alternative narratives. @lewandowsky_etal2020: Trump systematically tweeted about immigration/economy in response to damaging articles.

**🎯 Bayesian lens:** Social media systematically distorts the evidence available for belief updating. Algorithms create biased evidence samples (echo chambers) — users receive a non-representative stream of information that confirms existing priors. Negativity bias in engagement means outrage-inducing content is overrepresented, distorting posteriors about the state of the world. Loss framing (see [Gains and Losses](#gains-and-losses)) shifts risk preferences, making extreme options appear acceptable. Spinozan acceptance (see [Belief Formation and Perseverance](#belief-formation-and-perseverance)) means the volume of misinformation overwhelms correction. The result is polarization — two groups updating from entirely different evidence samples arrive at radically different posteriors about the same world.

**Key references:** @guriev_etal2020; @guriev_papaioannou2020; @lorenzspreen_etal2023; @rathje_etal2021; @humprecht_etal2024; @lewandowsky_etal2020; @larooij_tornberg2025; @schaffner_luks2018

---

## Artificial Intelligence

**Core idea:** Artificial intelligence — particularly large language models (LLMs) — provides a revealing mirror for human judgment and decision-making. Many of the biases, heuristics, and dual-process phenomena studied in human cognition have direct parallels in AI systems, and understanding these parallels deepens insight into both.

**The Turing test and shifting goalposts:**
- @turing1950 proposed the gold standard for machine intelligence: if an interrogator cannot distinguish a machine from a human in text-based conversation, the machine exhibits intelligent behavior. For decades, this was considered the definitive test.
- Modern LLMs now pass the Turing test convincingly — yet many people remain unconvinced that this constitutes "real" intelligence. The goalposts keep shifting: first it was conversation, then reasoning, then understanding, then consciousness.
- This reveals something about our intuitions about intelligence: we keep redefining it to exclude whatever machines can currently do. This connects to the bias blind spot (see [Heuristics and Biases](#heuristics-and-biases)) — a reluctance to accept that our own cognition might not be as special as we believe.

**System 1 / System 2 and LLMs:**
- Standard LLM output resembles System 1: fast, pattern-based, associative, drawing on statistical regularities in training data. The model generates plausible-sounding responses without explicit step-by-step reasoning.
- **Chain-of-thought (CoT) prompting** and **reasoning models** resemble System 2: the model is prompted or trained to produce intermediate reasoning steps before arriving at an answer. This improves performance on logical, mathematical, and multi-step problems — paralleling how System 2 overrides System 1 errors in humans.
- The analogy is imperfect but pedagogically powerful: CoT reasoning, like human System 2, is slower and more resource-intensive, but reduces errors on problems that require deliberation.

**Crystallized vs. fluid intelligence in LLMs:**
- LLMs are essentially *massive crystallized intelligence* (see [Intelligence](#intelligence)): vast knowledge retrieval from training data — facts, definitions, procedures, cultural associations. This is what they excel at.
- They struggle more with *fluid intelligence*: novel reasoning, abstract pattern detection in unfamiliar domains, problems that cannot be solved by retrieving or recombining prior knowledge.
- Chain-of-thought and reasoning models can be understood as attempts to add fluid intelligence on top of a crystallized knowledge base — mirroring the human relationship where crystallized intelligence depends on fluid intelligence having operated first (see [Intelligence](#intelligence)).
- Both humans and LLMs use both forms of intelligence, but the emphasis differs: humans lead with fluid intelligence and accumulate crystallized knowledge over time; LLMs begin with crystallized knowledge and are gradually acquiring fluid capabilities.

**Where do AI biases come from?**
- LLMs are trained on vast corpora of human-generated text that embed human biases — stereotypes, framing effects, cultural assumptions. AI biases are, to a significant degree, inherited human biases.
- LLMs replicate many classic biases: anchoring (influenced by numbers in the prompt), framing effects (different responses to gain vs. loss frames), sycophancy (a form of confirmation bias — telling users what they want to hear), and representativeness-like pattern matching.
- This replication is itself evidence about the nature of these biases: if they emerge from statistical patterns in language, they may be deeply embedded in how knowledge is structured and communicated — not just quirks of neural hardware.

**AI hallucination and human confabulation:**
- LLMs sometimes generate confident, plausible-sounding but factually incorrect outputs ("hallucinations"). This parallels human confabulation (see [Mental Models](#mental-models)): both involve pattern completion without verification — producing what *fits* the context rather than what is *true*.
- In both cases, the system generates the most probable completion given the context, without checking against ground truth. Humans confabulate when schemas dominate verification (System 1 without System 2 correction); LLMs hallucinate because they lack a ground-truth verification mechanism entirely.
- Crucially, both humans and LLMs are *more convincing when wrong*: confident, fluent, and detailed — because the same pattern-completion mechanism that produces good answers also produces compelling-sounding bad ones. There is no reliable internal "uncertainty signal" in either case.

**Calibration in AI:**
- LLMs are often poorly calibrated — expressing high confidence in incorrect answers, mirroring human overconfidence (see [Overconfidence](#overconfidence)). When asked to estimate their own certainty, models' stated confidence frequently does not match their actual accuracy.
- Improving AI calibration is an active research area, just as improving human calibration is a goal of debiasing interventions.

**🎯 Bayesian lens:** LLMs can be understood as approximate Bayesian reasoners: training data constitutes the prior, the prompt is the evidence, and the output is the posterior (most likely completion given prior + evidence). Biases in LLMs arise from biased priors (training data), just as human biases arise from biased experiential priors. Chain-of-thought reasoning improves performance by making the evidence-integration process more explicit — analogous to how deliberate Bayesian computation outperforms intuitive shortcuts. AI hallucination occurs when the prior (training patterns) dominates over evidence (factual constraints) — the same mechanism behind human confirmation bias and belief perseverance. Calibration failures in AI mirror the human overconfidence that arises from insufficiently wide posterior distributions.

**Key references:** @turing1950; @wei_etal2022; @bommasani_etal2021; @weidinger_etal2021