# Master Summary: Human Judgment and Decision-Making

---

## PART I: FOUNDATIONS OF COGNITION AND DECISION-MAKING

---

### 1. Dual-Process Models of Thinking

**Core idea:** Judgments and decisions are carried out via two distinct kinds of mental processing — arguably the most popular organizing framework for the field.

- **System 1 / Type 1 (intuitive):** Fast, effortless, parallel, automatic, emotion-driven, linked to heuristics and biases, does not require working memory. Includes automatic and habitual processing. Not always consciously accessible.
- **System 2 / Type 2 (reflective):** Slow, effortful, serial, deliberate, reason-driven, consciously accessible, necessarily engages working memory. Can be carried out in detachment from reality (abstract, hypothetical, future-oriented thought). Open to introspection.
- **Bounded rationality** (Simon, 1956/1972): Classic models assumed people are fully rational and perfectly informed. In reality, human reasoning is constrained by incomplete knowledge, limited cognitive capacity, and the complexity of the decision at hand. System 2 is often too slow, effortful, or even impossible (because not all information is available) to guide our decisions. This is *why* we rely so heavily on System 1 — not out of laziness, but out of necessity.
- The distinction between System 1 and 2 is convenient but imperfect — many forms of thinking have aspects of both systems.
- **Sloman's (1996) characterization** offers a useful way to understand *what* each system does. His **associative system** (≈ System 1) reasons through similarity and statistical regularities — e.g., recognizing something as a bird because it *looks like* birds you've seen before. Many of the heuristics and biases in this course reflect this associative processing. His **rule-based system** (≈ System 2) reasons through explicit logical, social, or definitional rules — e.g., classifying something as a bird because it meets specific biological criteria. These are not separate theories but complementary descriptions of the same dual-process distinction.
- **Gigerenzer's ecological rationality** offers a contrasting perspective on what System 1 processing achieves. Where Kahneman and Tversky emphasize that heuristics are biased shortcuts in need of System 2 correction, Gigerenzer argues that many heuristics are *ecologically rational* — well-adapted to the structure of real-world environments. Simple rules like **Take the Best** (decide based on the single most valid cue) or the **recognition heuristic** (if you recognize one option but not the other, choose the recognized one) can match or outperform complex deliberation when information is scarce and time is limited. This sets up a central tension in the course: are biases genuine errors, or adaptive strategies judged against an unrealistic normative standard?
- **Categorization as a bridge concept:** The associative vs. rule-based distinction is especially clear in **categorization** — one of the most fundamental cognitive operations. We constantly sort objects, people, and situations into categories to guide our judgments and decisions. System 1 categorizes implicitly by *resemblance*: we match new instances to stored prototypes or previously encountered exemplars (prototype and exemplar models of categorization). System 2 categorizes explicitly by *criteria*: we check whether defining features are present (classical/rule-based categorization). This matters throughout the course: the representativeness heuristic (§9) is essentially categorization-by-resemblance gone awry, base-rate neglect arises when we categorize by similarity while ignoring how common each category is, and stereotyping reflects the application of category-level expectations to individuals.
- **Cognitive Reflection Test (CRT)** (Frederick, 2005): Measures individual differences in the tendency to override System 1 with System 2. Higher CRT scores predict less acceptance of paranormal beliefs and better reasoning.

**🎯 Bayesian lens:** System 1 relies on rough heuristic priors and pattern-matching — fast but prone to ignoring base rates and evidence quality. System 2 enables more deliberate, calibrated belief updating — closer to Bayesian inference. Categorization itself is inherently Bayesian: given observed features (evidence), what is the probability that this instance belongs to category A vs. B (posterior)? Gigerenzer's insight adds a nuance: full Bayesian computation is often impossible given our cognitive constraints (bounded rationality), so heuristics can be understood as *resource-rational approximations* of Bayesian inference (Lieder & Griffiths, 2020). Many biases in this course can be understood as failures to engage System 2 when careful Bayesian updating is needed — but some may also reflect adaptive shortcuts that work well in the environments we evolved in.

**Key references:** Stanovich & West (2000); Evans (2008); Evans & Stanovich (2013); Kahneman (2011); Sloman (1996); Frederick (2005); Simon (1956; 1972); Gigerenzer, Todd, & the ABC Research Group (1999); Lieder & Griffiths (2020)

---

### 2. Bayesian Updating: The Normative Ideal for Belief Revision

**Core idea:** Rational judgment and decision-making can be understood as combining prior beliefs with new evidence to arrive at updated beliefs (posteriors). Bayes' theorem provides the normative standard; the many biases covered in this course represent specific, identifiable departures from this ideal.

- **The Bayesian framework:**
  - **Prior belief (prior):** What you believe before encountering new evidence, expressed as a probability. Shaped by base rates, past experience, cultural knowledge, and schemas.
  - **Evidence (likelihood):** New information — how probable this evidence would be if the hypothesis were true versus false.
  - **Updated belief (posterior):** The revised belief after integrating evidence with the prior. This posterior then becomes the prior for the next piece of evidence.

- **Bayes' theorem (formal):** `P(H|E) = [P(E|H) × P(H)] / P(E)`. Where P(H|E) is the posterior probability of hypothesis H given evidence E, P(E|H) is the likelihood of the evidence given the hypothesis, P(H) is the prior probability, and P(E) is the total probability of the evidence.
- **The mammogram problem — a classic illustration** (Eddy, 1982): A woman has a positive mammogram. The test's sensitivity is 80% (P(positive|cancer) = 0.80) and the false-positive rate is 10% (P(positive|no cancer) = 0.10). The base rate of breast cancer is 1% (P(cancer) = 0.01). What is the probability she has cancer?
- 95 out of 100 physicians estimated 70–80%. The correct answer is ~7.5%.
- People confuse P(positive|cancer) with P(cancer|positive) — ignoring the prior (base rate).
- **Natural frequencies — making Bayesian reasoning intuitive:** Expressing information as concrete counts rather than conditional probabilities dramatically improves accuracy. Out of 1,000 women: 10 have cancer; of those 10, 8 test positive. Of the 990 without cancer, 99 test positive. So of 107 positive results, only 8 (~7.5%) actually have cancer.
- Teaching physicians natural frequencies is more effective than teaching Bayes' theorem, and improvement persists ≥5 weeks (Sedlmeier, 1997). Despite this, few physicians are trained this way.
- **Ideal observer models:** In perception research, ideal observer models specify how a perfectly rational agent would combine prior expectations with noisy sensory evidence. Human perception often approximates this — we perceive what is most probable given our expectations and the sensory data. Perceptual illusions arise when priors (expectations) dominate over ambiguous evidence, just as cognitive biases arise when judgment priors dominate. An example of a perceptual illusion is when someone is on our mind (e.g. a love interest), and then we often mistakenly think that we see this person out on the street. In this case, we have a strong prior expectation (implicit in the fact the we are thinking of this person), and weak evidence (because you only catch glimpses of people), resulting in a perceptual illusion.
- **Signal detection theory (SDT):** A framework for decisions under uncertainty with two key parameters: *sensitivity* (ability to distinguish signal from noise — the quality of evidence) and *criterion/bias* (the threshold for saying "yes" — reflecting the prior and the costs of different errors). A Bayesian agent sets the optimal criterion based on base rates and payoff structure. People often set non-optimal criteria, producing patterns of misses and false alarms.
- **Calibration:** A well-calibrated person's confidence matches their accuracy — events they judge as 70% likely occur ~70% of the time. Perfect calibration is the hallmark of good Bayesian reasoning. Most people are *overconfident* (see §12), meaning their posteriors are too extreme relative to the evidence.
- **Why this matters for the course:** Nearly every bias and heuristic covered in subsequent sections can be understood as a specific departure from Bayesian rationality:

| Phenomenon | Bayesian Departure |
|---|---|
| Base-rate neglect (§9) | Ignoring the prior |
| Anchoring (§10) | Insufficient updating from the prior |
| Availability (§8) | Biased evidence sampling |
| Representativeness (§9) | Likelihood dominates; prior ignored |
| Confirmation bias (§25) | Asymmetric updating |
| Overconfidence (§12) | Posteriors too extreme / poorly calibrated |
| Hindsight bias (§16) | Retroactively revising the prior |
| Belief perseverance (§26) | Failure to update from disconfirming evidence |
| Clinical vs. statistical (§17) | Informal vs. formal evidence integration |

**Key references:** Bayes (1763); Eddy (1982); Hoffrage & Gigerenzer (1998); Sedlmeier (1997); Green & Swets (1966); Griffiths et al. (2008)

---

### 3. Heuristics and Biases (General Definitions)

- **Heuristic:** Answering a hard question by substituting an easier one (Kahneman & Frederick, 2002). Or: a quick-and-easy rule of thumb used under conditions of uncertainty. Classified as Type 1 processing. The world is too complex for full rational analysis, so thinking is often heuristic-based.
- **Bias:** A systematic error in thinking in a specific direction, often resulting from reliance on heuristics. In daily life, "bias" is sometimes used to mean socially undesirable thinking (including stereotypes, such as that professors are male), but this conflates errors in thinking with social desirability.
- **Cognitive illusions:** Systematic errors in subjective judgment, analogous to visual perceptual illusions — they reveal how judgments and decisions are normally made.
- **Affect:** Experienced emotion; people may rely on positive or negative affect as a simple cue when judging and deciding (the *affect heuristic*).

**🎯 Bayesian lens:** Heuristics can be understood as computationally cheap approximations to Bayesian inference. They often work well (when priors and evidence are typical) but produce systematic errors when the shortcut diverges from proper integration of prior and likelihood — i.e., biases are predictable failures of approximate Bayesian computation.

**Key references:** Tversky & Kahneman (1974); Kahneman & Frederick (2002); Pohl (2004); Slovic et al. (2007)

---

### 4. Models of Decision-Making

- **Descriptive models** describe how people *actually* judge and decide, without evaluating quality. The vast majority of models in the field are descriptive (e.g., prospect theory describes how people weigh gains and losses; dual-process models describe the interplay of intuitive and deliberate thinking).
- **Normative models** reflect *optimal* or ideal decision-making — logical, consistent, using all relevant data, getting the person closest to their goals over the long run (e.g., expected utility theory; Bayes' theorem for belief updating).
- **Prescriptive models** recommend how people *ought* to judge and decide in practice; often a practical compromise between normative ideals and descriptive realities (e.g., installing hand sanitizer instead of requiring full handwashing; presenting medical statistics as natural frequencies to improve understanding).
- **Risk vs. uncertainty:** Decision-making under *risk* means you have enough data to estimate probabilities (e.g., the chance of rolling a six). Decision-making under *uncertainty* means you lack the data to assign meaningful probabilities and are essentially guessing (e.g., whether a new technology will succeed). Most real-world decisions fall somewhere on this spectrum.

**🎯 Bayesian lens:** Bayesian updating is the normative standard for how beliefs should change in light of evidence. Descriptive models document how people systematically deviate from this standard. Prescriptive models often aim to nudge people closer to Bayesian rationality (e.g., presenting information as natural frequencies).

**Key references:** Bell, Raiffa, & Tversky (1988); Knight (1921); Simon (1955)

---

### 6. Intelligence and Individual Differences

- **g-factor (General intelligence)** (Spearman): Imagine we organize a mega-Olympics where a hundred random people from the street compete in every event. We'd quickly notice that some people do well across the board — faster runners, better swimmers, higher jumpers — while others consistently struggle. There's a general underlying factor we might call *physical fitness* that largely determines performance across diverse athletic events. Spearman's insight was that intelligence works the same way. There is a general underlying factor — the **g-factor** (for *general intelligence*) — that partly determines how well people perform across all kinds of cognitive tasks. People with a high g-factor tend to have better spatial reasoning, larger vocabularies, higher working-memory capacity, and stronger problem-solving skills. This explains why the specific tasks in an IQ test matter less than you'd think: most cognitive tasks tap into the g-factor to some degree. In applied and organizational psychology, the g-factor is often referred to as **general mental ability (GMA)** — same construct, different label.
- **s-factors (Specific abilities):** Just as a steady hand matters for archery but not for sprinting, some cognitive abilities are task-specific. Language skill matters for vocabulary tests but not for visual puzzles. Spearman called these **s-factors** (for *specific intelligence*). Some abilities are almost purely g-loaded — matrix puzzles are the best example, requiring working memory, flexible recombination of information, and active problem-solving. Others, like musicality, depend mostly on specific factors.
- **Fluid intelligence:** The capacity to flexibly manipulate information in working memory to solve novel problems. Corresponds closely to the g-factor (matrix puzzles are a near-pure measure). Declines with age.
- **Crystallized intelligence:** Accumulated knowledge, skills, and facts in long-term memory (e.g., vocabulary). Increases with age. With experience, tasks that once required fluid intelligence can be solved through crystallized intelligence.
- **Intelligence predicts real-life outcomes:** GMA is one of the strongest single predictors of both academic achievement and job performance across virtually all occupations. Schmidt and Hunter (2004) showed that GMA predicts job performance better than any other single selection method, including work experience, interviews, and personality measures. The predictive power increases with job complexity — for complex jobs (management, engineering), GMA is an even stronger predictor than for simpler jobs. This doesn't mean intelligence is the *only* thing that matters, but it does mean that the g-factor has substantial real-world consequences beyond the lab.
- **Genetic and environmental basis:** Twin studies show roughly half of individual differences are attributable to genetics. The rest is shaped by parental stimulation, socioeconomic status, neighborhood, and cultural background.
- **IQ testing:** Modern tests (e.g., WAIS) define IQ relative to population norms (100 = average; 130 = top ~2%).
- **The Flynn effect and its reversal:** Throughout the 20th century, average IQ scores rose by roughly 3 points per decade — the **Flynn effect**. This is too fast for genetic change, suggesting environmental causes: better nutrition, more education, greater exposure to abstract reasoning. However, recent evidence suggests the Flynn effect has plateaued or even reversed in some countries. Bratsberg and Rogeberg (2018) analyzed Norwegian military conscription data and found IQ scores *declining* among cohorts born after the mid-1970s. The cause of this reversal is debated — possible explanations include changes in education, media consumption, or lifestyle — but it challenges the assumption that each generation is cognitively sharper than the last.

**🎯 Bayesian lens:** Higher fluid intelligence and CRT scores predict better calibration and more Bayesian reasoning — e.g., greater sensitivity to base rates, less anchoring, less susceptibility to framing effects. Individual differences in "Bayesian competence" are real and consequential. The strong predictive power of GMA can itself be understood through a Bayesian lens: people with higher g-factors form more accurate priors, update more appropriately from evidence, and maintain better-calibrated confidence — advantages that compound across academic and professional domains.

**Key references:** Spearman; Wechsler (WAIS); Frederick (2005); Toplak et al. (2011); Schmidt & Hunter (2004); Bratsberg & Rogeberg (2018)

---

### 7. Knowledge Structures: Schemas, Stances, and Framework Theories

**Framework theories:** Distinct sets of commonsense background knowledge in biology, physics, and psychology that develop very early in life and organize understanding of new information. When knowledge from one domain is inappropriately applied to another, errors and superstitions may result.

**Stances / Modes of construal** (Dennett, 1987; Keil, 1995, 2006):
- **Mechanical (physical) stance:** Explaining in purely physical terms.
- **Design (functional) stance:** Explaining in terms of purpose/function.
- **Intentional stance:** Explaining by presuming beliefs and desires.
- The best stance is the one that makes the most sense of the situation. The adopted stance influences the causal narrative one constructs, which in turn shapes moral judgment.

**Schemas and scripts operate within stances.** The stance you adopt determines which schemas are activated and what kind of reasoning follows:

- **Schema:** A set of general knowledge about what to expect in a particular situation or thing. Activated by incoming information to guide comprehension, memory, learning, and performance.
  - *Bransford & Johnson (1972)*: Students who learned a topic before reading disjointed sentences had better comprehension and recall.
  - Not everyone has the same schema content, and the nature of that content profoundly affects behavior.
- **Scripts** (Schank & Abelson, 1977): Schemas for highly routine events (e.g., restaurant visits). Well known within a culture, with agreed-upon temporal sequences. Culture-specific. Violations of scripts are noticed and remembered — especially when they bring the script to a standstill.

**Artifacts vs. natural kinds as a case study in stance activation:**
Even young children distinguish artifacts (human-made items) from natural kinds (e.g., animals, plants) and reason about them differently (Keil, 1989). This reflects that different types of things trigger different default stances:
- **Artifacts → design stance:** We understand artifacts in terms of function and purpose. A broken chair is still a chair because it was *designed* to be sat on.
- **Living things → intentional stance:** We understand animals and people in terms of beliefs, desires, and goals. A dog chases a ball because it *wants* to catch it. This tendency is so strong that children spontaneously attribute intentions even to simple animals and animated shapes.
The key insight is that the type of thing we encounter triggers a default stance, which then activates stance-appropriate schemas. This distinction emerges early in development, suggesting it reflects a deep organizing principle of human cognition.

**🎯 Bayesian lens:** Stances set the broadest level of prior beliefs — which *kind* of explanation is appropriate. Within a stance, schemas encode more specific expectations about what is likely. Scripts represent strong temporal priors within schemas, and script violations are prediction errors. New information is interpreted against these layered priors: stance-inconsistent information may be ignored entirely, while schema-inconsistent information within the right stance is surprising and may trigger updating.

**Key references:** Wellman & Gelman (1992); Keil (1989); Dennett (1987); Bransford & Johnson (1972); Schank & Abelson (1977)

---

## PART II: JUDGMENT UNDER UNCERTAINTY — CORE HEURISTICS

---

### 8. Availability Heuristic

**Definition:** The tendency to estimate frequency or probability based on how easily instances or associations come to mind. The easier recall is, the more likely the event is judged to be. Classified as Type 1 reasoning.

**Key studies:**
- *Famous names* (Tversky & Kahneman, 1973): Lists with very famous women and somewhat famous men led participants to overestimate the number of women — because famous names were more easily recalled.
- *First vs. third letter position* (Tversky & Kahneman, 1973): 69% judged consonants (K, L, N, R, V) as more frequent in the first position of words, but all five actually appear more often in the third position — because it is easier to search by first letter.

**What makes something "available"?** Availability can manifest in different ways: faster recall (a few vivid examples come to mind quickly), more recalled exemplars (many instances are retrieved, even if slowly), or stronger associations (certain pairings are more deeply encoded). These are not competing hypotheses — they are all routes through which the same principle operates. Some researchers use the term *accessibility* (ease of retrieval) to emphasize the speed component, but availability as a concept encompasses all of these manifestations.

**Over the lifespan:** Davies & White (1994) adapted the famous-names paradigm for 7- and 10-year-olds using cartoon characters, finding availability effects as early as age 7 — suggesting this is a fundamental feature of human cognition.

**Negativity bias interaction:** People seek out, attend to, and are more strongly influenced by negative content. Robertson et al. (2023): Click-through rates increased with negative words in headlines and decreased with positive words. This makes negative events disproportionately available, making the world seem grimmer than it is.

**Applied contexts:** The availability heuristic plays a major role in medical decision-making (§31), where recent cases bias diagnosis, and in social media environments (§33), where algorithmic curation makes certain types of information disproportionately available.

**🎯 Bayesian lens:** The availability heuristic biases the *evidence sampling* step of Bayesian reasoning. Instead of drawing a representative sample from memory (which would give accurate base rates), people draw a biased sample — weighted toward recent, vivid, emotional, or easily retrieved instances. The likelihood term is distorted because the evidence itself is not representative. A Bayesian reasoner with unbiased memory access would not show this effect.

**Key references:** Tversky & Kahneman (1973, 1974); MacLeod & Campbell (1992); Davies & White (1994); Robertson et al. (2023)

---

### 9. Representativeness Heuristic

**Definition:** The tendency to judge the probability of an event or category membership based on how similar it is to a prototype or stereotype, rather than on actual statistical information.

**Core mechanism — Base-rate neglect:** The representativeness heuristic is fundamentally driven by base-rate neglect: people attend to how well evidence matches a category (likelihood) while ignoring how common that category actually is (prior/base rate).
- *Tom W. problem* (Kahneman & Tversky, 1973): Likelihood judgments of Tom's graduate field correlated almost perfectly with representativeness ratings but *negatively* with actual base rates of enrollment.
- *Taxicab problem* (Bar-Hillel, 1980): A witness (80% accurate) identifies a hit-and-run cab as Green in a city with 85% Blue cabs. Most people estimate ~80% Green, ignoring base rates. Using natural frequencies: only 12 out of 29 positive identifications (~41%) are truly Green.

**Consequence 1 — Conjunction fallacy:** Because representativeness is driven by similarity rather than probability logic, people judge the conjunction of two events (A and B) as more probable than one event alone (A), violating the conjunction rule P(A∩B) ≤ P(A).
- *Linda problem* (Tversky & Kahneman, 1983): 82% judged "bank teller and feminist" as more probable than "bank teller" alone, because the conjunction better matches Linda's description.
- *Averaging heuristic:* One explanation is that people intuitively average the probabilities of component events rather than multiplying them. "Feminist" has high probability given Linda's description; "bank teller" has low probability; the average feels higher than "bank teller" alone — but proper probability requires multiplication, which would make the conjunction *less* likely.
- *Alternative view* (Hertwig & Gigerenzer, 1999): Participants may interpret "probable" non-mathematically (e.g., as "plausible"), making responses reasonable conversational inferences rather than logical fallacies.

**Consequence 2 — Stereotyping:** Representativeness drives stereotyping: when a person resembles the prototype of a social category, they are judged as more likely to belong to that category regardless of base rates.
- Bodenhausen & Wyer (1985): Predicted future criminal behavior was stereotype-congruent (forgery for "Ashley Chamberlaine," assault for "Carlos Ramirez"), even when alternative explanations were provided.
- This has serious implications for legal decision-making (see §32) and medical diagnosis (see §31).

**Consequence 3 — Distorted perception of randomness:** People have a stereotype of what "random" looks like — roughly alternating, without long runs. Sequences that don't match this stereotype are judged as non-random.
- *Gambler's fallacy:* After a run of five heads, people judge tails as "due" because HHHHHH doesn't look representative of randomness, even though each flip is independent.
- *Hot hand belief:* Streaks in sports performance are perceived as meaningful ("he's on fire!") when they often fall within the range expected by chance.

**🎯 Bayesian lens:** The representativeness heuristic is the most direct violation of Bayesian reasoning, and the hierarchy makes this clear:
- **Core mechanism (base-rate neglect):** People ignore the prior P(H) and base judgments almost entirely on the likelihood P(E|H) — how representative the evidence is of the hypothesis.
- **Conjunction fallacy:** Overweighting likelihood leads to violations of basic probability axioms — the posterior for the conjunction exceeds the posterior for the single event because the conjunction is more representative.
- **Stereotyping:** Stored representativeness judgments (stereotypes) function as inflated likelihood estimates that override low base rates for the stereotyped category.
- **Randomness perception:** People's stereotype of randomness acts as a prior about what random sequences should look like, leading them to reject actually random sequences that don't match this prototype.

**Key references:** Kahneman & Tversky (1972, 1973); Tversky & Kahneman (1971, 1983); Bar-Hillel (1980); Bodenhausen & Wyer (1985); Hertwig & Gigerenzer (1999)

---

### 10. Anchoring and Adjustment

**Definition:** The tendency to make estimates by starting from an initial value (the anchor) and adjusting insufficiently. The anchor may be externally provided or self-generated, and it influences judgments even when clearly irrelevant.

**Classic studies:**
- *Wheel of fortune* (Tversky & Kahneman, 1974): Random numbers (10 vs. 65) influenced estimates of African UN membership (25% vs. 45%).
- *Multiplication sequences* (Tversky & Kahneman, 1973): 1×2×...×8 → median estimate 512; 8×7×...×1 → median estimate 2,250 (correct: 40,320).

**Mechanisms:**
- **Selective Accessibility Model** (Strack & Mussweiler, 1997): The anchor makes consistent information more accessible in memory, biasing the estimate — without explicit adjustment.
- **Numeric priming theory** (Reitsma-van Rooijen & Daamen, 2006): The anchor acts as a prime; under time pressure, its influence is stronger.
- **Self-generated vs. experimenter-provided anchors** (Epley & Gilovich, 2001): Self-generated anchors trigger deliberate adjustment (94%); experimenter-provided anchors less often do (22%).

**Boundary conditions:**
- *Extreme/implausible anchors:* Even wildly implausible anchors (Gandhi age 9 or 140) influence estimates (Strack & Mussweiler, 1997), though extreme anchors have attenuated effects.
- *Subliminal anchors:* Anchors presented subliminally (15 ms, masked) influence estimates — but only under time pressure (Mussweiler & Englich, 2005).
- *Cross-modal anchoring:* Anchors in one domain (line length) influence estimates in another (temperature), suggesting a general magnitude priming effect (Oppenheimer et al., 2008).

**Applied contexts:**
- *Medical diagnosis:* Anchoring influences initial probability estimates, test interpretation, and referral letter processing. Physicians distort neutral cues to support a favored diagnosis (Kostopoulou et al., 2012).
- *Real estate:* Listing prices anchor both laypeople's and experts' home value estimates. Agents show comparable anchoring effects but are less likely to report using the listing price (Northcraft & Neale, 1987).

**Countering anchoring:** Very difficult. Informing people about anchoring does not attenuate it (Chapman & Johnson, 2002). One promising avenue: *positive affect* — physicians who received a small bag of candies showed less anchoring in diagnostic reasoning (Estrada et al., 1997).

**🎯 Bayesian lens:** Anchoring represents the opposite problem from base-rate neglect: here, the prior (anchor) exerts *too much* influence and updating from evidence is *insufficient*. A Bayesian agent would adjust fully to the posterior implied by the evidence; anchored judgments are pulled toward the prior. Self-generated anchors function as genuine (if imperfect) priors; externally provided anchors contaminate the updating process with irrelevant starting points.

**Key references:** Tversky & Kahneman (1973, 1974); Strack & Mussweiler (1997); Epley & Gilovich (2001); Chapman & Johnson (2002); Estrada et al. (1997)

---

### 11. Primacy Effects in Judgment

**Definition:** The disproportionately strong influence of information presented first on overall judgments. Early information sets the context against which later information is interpreted. First impressions are important and difficult to override.

- *Asch (1946)*: Personality traits in opposite orders (*intelligent…envious* vs. *envious…intelligent*) produced markedly different impressions. Positive-first groups inferred additional positive traits (74% "good-looking" vs. 35%).
- *Anderson (1965)*: Clean linear primacy effect; proposed a weighted-average model.
- *Stewart (1965)*: Primacy was reliable with a single final judgment; eliminated or reversed to recency with repeated judgments after each trait.
- Primacy effects are related to **anchoring and adjustment**: first information serves as an anchor, and subsequent information is used for insufficient adjustment.

**Belief-adjustment model** (Hogarth & Einhorn, 1992): Three subprocesses — encoding (interpreting evidence relative to the anchor), processing (piece-by-piece or all at once), and adjustment (degree of contrast between anchor and evidence determines impact).

**🎯 Bayesian lens:** Early information functions as a strong prior. In ideal Bayesian updating, the order of evidence should not matter — the final posterior is the same regardless of presentation order. Primacy effects reveal that people *do not* update symmetrically: early evidence is weighted more heavily, forming a prior that is insufficiently revised by later evidence. This is formally equivalent to anchoring with insufficient adjustment.

**Key references:** Asch (1946); Anderson (1965); Hogarth & Einhorn (1992)

---

### 12. Overconfidence

**Definition:** A family of biases in which people's confidence systematically exceeds their accuracy. One of the most robust and consequential findings in JDM research. Manifests in three distinct forms.

**Overestimation:** Overestimating one's actual performance, knowledge, or control. Related to the *illusion of control* (Langer, 1975): expecting greater personal success than evidence supports, even for chance-determined outcomes. People who chose their own lottery ticket demanded over $8 to sell; randomly assigned tickets were sold for ~$2.

**Overplacement (better-than-average effect):** Judging oneself as better than the average person. Weinstein (1980): Students rated themselves as less likely to contract diseases and more likely to experience positive events than average. Overlaps with *unrealistic optimism* and the *positivity bias*. Korn et al. (2014): Healthy controls showed a positivity bias in updating; patients with major depression did not — suggesting unrealistic optimism is, paradoxically, a sign of good mental health.

**Overprecision (miscalibration):** Confidence intervals are too narrow; people are too certain about their estimates. When asked for 90% confidence intervals, people typically capture the true answer only 40–60% of the time. The most pervasive and least understood form of overconfidence.

**The planning fallacy** (Kahneman & Tversky, 1979): The tendency to underestimate the time, cost, and risk of future actions while overestimating benefits. People focus on the specific plan (inside view) rather than base rates of similar past projects (outside view).
- Buehler et al. (1994): Students predicted finishing assignments far earlier than they did — even when explicitly asked to consider past experience.
- Large infrastructure projects routinely overrun budgets and timelines (Flyvbjerg, 2006).

**Dunning-Kruger effect** (Kruger & Dunning, 1999): The least competent individuals show the greatest overconfidence, because the skills needed to perform well are the same skills needed to recognize poor performance. Highly competent individuals slightly underestimate their ability. Debated: some argue the effect is partly a statistical artifact (regression to the mean), but the core finding — that poor performers are poorly calibrated — is well-replicated.

**Expertise and overconfidence:** Domain expertise improves calibration only when accompanied by clear, frequent feedback (e.g., weather forecasters are well-calibrated; clinical psychologists are not). Without feedback loops, experience increases confidence without increasing accuracy (Einhorn & Hogarth, 1978).

**🎯 Bayesian lens:** Overconfidence means that posterior distributions are too narrow — the agent is more certain than the evidence warrants. A well-calibrated Bayesian would have posteriors that accurately reflect residual uncertainty. The planning fallacy is a failure to use the base rate (outside view) as the prior, instead constructing the estimate from a specific scenario (ignoring the prior). Overprecision represents insufficient probability mass assigned to alternative hypotheses.

**Key references:** Lichtenstein, Fischhoff, & Phillips (1982); Moore & Healy (2008); Langer (1975); Weinstein (1980); Kruger & Dunning (1999); Buehler et al. (1994); Korn et al. (2014)

---

## PART III: CAUSAL REASONING

---

### 13. Covariation and Attribution

**Covariation:** Two things tending to happen together (e.g., petting a cat → purring). Much of the evidence people use for figuring out causes consists of covariation information. People often interpret correlations as causal relationships.

**Covariation principle** (Kelley, 1973): "An effect is attributed to the one of its possible causes with which, over time, it covaries." People search for stable properties of a person or situation that can be expected to cause certain effects (Heider, 1958/2015).

**Personal vs. impersonal causality** (Heider): Personal causality = a person's intention was the force behind an action. Impersonal causality = action occurred without intention. Personal causality is perceived as having strong, pinpointable causal force.

**Kelley's covariation model of attribution:** When inferring causes of others' behavior, people consider:
- **Consensus:** Do other people respond the same way to the same stimulus?
- **Distinctiveness:** Does this person respond this way only to this specific stimulus?
- **Consistency:** Does this person respond similarly over time?
- Different patterns yield different attributions: Low consensus + low distinctiveness + high consistency → person attribution. High consensus + high distinctiveness + high consistency → stimulus attribution.

**Probabilistic contrast model** (Cheng & Novick, 1990): Extends Kelley's model to include interactions (e.g., a specific person's reaction to a specific movie).

**Correspondence bias / Fundamental attribution error** (Gilbert & Malone, 1995; Jones & Davis, 1965): The tendency to make person attributions for behaviors that could be explained by the situation alone — even when told essay writers were assigned positions, people judged they really believed what they wrote. A key mechanism is lack of awareness of how situations powerfully influence behavior.

**🎯 Bayesian lens:** Causal attribution is belief updating about the source of behavior. The prior is one's default assumption about the person or situation; evidence from consensus, distinctiveness, and consistency updates this belief. The fundamental attribution error reflects an overly strong prior toward person-causes (dispositional attribution) that insufficiently updates in light of situational evidence.

**Key references:** Heider (1958/2015); Kelley (1973); Cheng & Novick (1990); Gilbert & Malone (1995)

---

### 14. Cues to Causality

**Cues-to-causality** (Einhorn & Hogarth, 1986): Situational features leading people to judge that a causal relationship is present — covariation, temporal order, contiguity in time and space, causal mechanism, similarity of cause and effect, and counterfactual reasoning.

**Causal field** (Mackie, 1965/1974): The background of existing conditions against which potential causes are evaluated. A **difference-in-a-background** — an event that stands out against the causal field — is inferred to be the cause.

**Temporal order:** When one event regularly precedes another, people infer causation. People use temporal order even when they shouldn't (e.g., judging P(child has blue eyes | parent has blue eyes) as higher than the reverse, though mathematically equal). In legal settings, evidence in temporal order makes jurors more convinced (Pennington & Hastie, 1988).

**Contiguity in time and space:** People are more likely to judge causation when the effect occurs soon after and physically close to the potential cause. Michotte (1946/1963): Two-ball "launching" displays identified precise conditions for perceived causation.

**Temporal binding** (Buehner, 2012): When people believe events are causally related, they infer those events happened closer together in time than they actually did.

**Causal mechanism:** An explanation filling the gap between cause and effect. People explain events in terms of mechanisms 83% of the time, rather than covariation (Ahn et al., 1995).

**Similarity of cause and effect:** (1) Physical resemblance (e.g., doctrine of signatures); (2) Matching magnitude — people expect large effects to have large causes.

**Simulation heuristic and counterfactual reasoning** (Kahneman & Tversky, 1982): People mentally simulate what might have happened differently. A factor is a **but-for cause** if the event would not have occurred without it.

**Prediction error:** The brain signals deviations from expected events. Schultz et al. (1997): Dopamine neurons respond to unexpected rewards and show negative responses when expected rewards are omitted. After conditioning, the dopamine response shifts from the reward to the predictor.

**Conditioning:** Learning associations through covariation.
- *Classical conditioning:* When two things tend to happen together, we learn to associate them.
- *Operant conditioning:* Learning that actions cause rewards or punishments.

**🎯 Bayesian lens:** Cues to causality function as features that strengthen or weaken the likelihood of a causal hypothesis. Each cue updates the probability of causality: temporal order, contiguity, and mechanism all increase P(E|causal link), while their absence decreases it. Prediction error is fundamentally Bayesian — it is the discrepancy between expected (prior) and observed (evidence) outcomes, which drives learning (updating).

**Key references:** Einhorn & Hogarth (1986); Mackie (1965, 1974); Michotte (1946/1963); Ahn et al. (1995); Buehner (2012); Schultz et al. (1997)

---

### 15. Causal Learning, Illusory Correlation, and Plausibility

**2 × 2 contingency table:** Summarizes co-occurrence of two factors (cells A, B, C, D). People give cell A (both present) the most weight, followed by B, then C, and D the least. When simplifying, people sometimes attend only to cell A — a purely confirmatory approach.

**Blocking** (Rescorla & Wagner, 1972): When a first cue perfectly predicts an outcome, pairing it with a second cue does not lead to learning about the second cue. The first cue "blocks" learning about the second.

**Predictive vs. diagnostic learning** (Waldmann & Holyoak, 1992):
- *Predictive task:* Cause presented first → learner determines the effect. Cues compete; blocking occurs.
- *Diagnostic task:* Effect presented first → learner determines the cause. Blocking does *not* occur.
- Same data produced different learning outcomes depending on causal structure, demonstrating that causal learning depends on more than associations.

**Illusory correlations:** Perceiving correlations that do not actually exist (e.g., perceived link between political parties and economic performance).

**Illusory causation / Quackery:** Interpreting real but non-causal correlations as causal. When many cases appear in cell A (treatment present, recovery present), people perceive a causal link even when recovery rates are identical regardless of treatment.
- Matute et al. (2011): 80% of patients recovered regardless of treatment, yet participants judged the medicine effective — especially when many patients took it (64 vs. 16 in cell A).

**Regression toward the mean:** An initial extreme value is followed by a value closer to the mean. People create spurious causal explanations for this statistical phenomenon rather than recognizing natural variability.

**Role of plausibility:** Pre-existing beliefs about which causal relationships are plausible strongly influence processing of covariation data. Plausible causes receive more weight from covariation evidence (Fugelsang & Thompson, 2003). People seek out cause-present information more when the cause is plausible (Goedert et al., 2014).

**Experimental designs:** Only experimental manipulation (controlling an independent variable while holding everything else constant) allows causal conclusions — as opposed to the correlational evidence that drives illusory causation.

**🎯 Bayesian lens:** Cell A bias means people overweight confirming evidence (hypothesis present, outcome present) and underweight the other cells — especially cell D (both absent). A Bayesian agent would use all four cells to compute the contingency. Blocking is Bayesian: once a cue fully explains the outcome, a second redundant cue provides no additional evidence and should receive no credit. Plausibility effects show that prior beliefs about causal structure modulate how evidence is weighted — a form of prior-driven evidence evaluation. Illusory causation is a failure to properly account for the base rate of recovery (cell A + C), i.e., P(recovery) regardless of treatment.

**Key references:** Lipe (1990); Rescorla & Wagner (1972); Waldmann & Holyoak (1992); Matute et al. (2011); Fugelsang & Thompson (2003)

---

## PART IV: JUDGING THE PAST AND FUTURE

---

### 16. Hindsight Bias

**Definition:** The erroneous judgment that one "knew all along" that a particular outcome would occur. Three components (Fischhoff, 1975): (1) retroactive probability judgments shift toward the actual outcome, (2) the outcome is judged as relatively inevitable (**creeping determinism**), (3) people are unaware their judgments have changed.

**Paradigms:**
- *Memory paradigm:* People make predictions, then recall them after learning the outcome. Recalled judgments shift toward the actual outcome (Fischhoff & Beyth, 1975).
- *Hypothetical paradigm:* Foresight group (no outcome knowledge) vs. hindsight group (knows outcome, judges "as if" they don't). Hindsight judgments are closer to the actual outcome (Fischhoff, 1975).

**Cognitive models:**
- **SARA model** (Pohl et al., 2003): Correct answer activates outcome-consistent information; reconstruction is disproportionately influenced by this information.
- **RAFT model** (Hoffrage et al., 2000): After learning the correct answer, cue values are updated to match the outcome; reconstruction using updated cues produces hindsight bias. Treats the bias as a side effect of adaptive learning.
- **Causal model theory** (Wasserman et al., 1991): Learning the outcome makes people highlight causally relevant antecedents. If no plausible antecedents are available, hindsight bias does not occur (Yopchick & Kim, 2012).

**Additional contributing factors:** Availability heuristic (what happened comes to mind easily); curse of knowledge (new information is automatically incorporated); causal narratives (coherent stories for actual outcomes); self-serving bias (taking credit for positive outcomes); desire to look smart.

**Motivational influences:** Mark & Mellor (1991): Laid-off workers showed the *least* hindsight bias (self-serving bias counteracted it).

**Reverse hindsight bias:** Under extreme surprise, people believe they "never would have seen it coming." Ofir & Mazursky (1997): Hindsight participants rated a fatal heart bypass as *more likely to succeed* than foresight participants.

**Outcome bias:** Judging decision quality by the outcome, even when the outcome is irrelevant to the reasoning process. Baron & Hershey (1988): A physician's decision was rated poorer when the patient died, despite identical reasoning.

**Epistemic egocentrism / Curse of knowledge effect:** Underestimating how likely another person is to hold a false belief. Related to theory of mind and hindsight bias (Birch & Bloom, 2007).

**Visual hindsight bias:** People who know an image's identity believe a naïve peer would recognize it at a more degraded stage — the "I saw it all along" effect (Bernstein et al., 2004).

**Lifespan:** U-shaped pattern — strongest in young children (3–4), decreases through young adulthood, increases again in older adults.

**Cross-cultural:** Nearly universal, but collectivist cultures may show stronger bias for surprising outcomes (Choi & Nisbett, 2000).

**🎯 Bayesian lens:** Hindsight bias is retroactive revision of the prior to match the posterior. After learning the outcome, the prior is "overwritten" — people can no longer access what they believed before the evidence arrived. The RAFT model is explicitly Bayesian: learning the outcome updates cue-outcome associations (legitimate updating), but the inability to recall the pre-update prior produces the illusion of having "always known." A true Bayesian retains awareness of prior vs. posterior; the hindsight-biased thinker confuses them.

**Key references:** Fischhoff (1975); Fischhoff & Beyth (1975); Pohl et al. (2003); Hoffrage et al. (2000); Baron & Hershey (1988); Bernstein et al. (2011)

---

### 17. Prediction: Clinical Intuition vs. Statistical Methods

**Clinical intuition:** Domain experts consider available information and make intuitive predictions, drawing on experience and holistic assessment. People tend to overestimate its value.

**Statistical prediction:** Predictions based solely on empirical evidence and statistical comparison. A meta-analysis of 136 studies (Grove et al., 2000): 46% favored statistical prediction, 48% showed no difference, *only 6%* favored clinical intuition. Publication date, training, experience, and domain had no effect.

**Why clinical intuition is overvalued:**
- *Cognitive fluency:* With experience, assessment *feels* easy and confident — even when accuracy hasn't improved.
- Especially problematic in areas with little concrete feedback (clinical psychology, law, university admissions).
- Corrective feedback is critical for learning; weather forecasters exemplify accurate expert prediction because they receive frequent, consistent feedback.

**Tools for statistical prediction:**
- **MMPI/MMPI-2:** Large standardized questionnaire (567 true/false) for clinical diagnosis. Items included via **blind empiricism** — based on statistical predictive power regardless of **face validity**.
- **Decision support systems:** Computer-based tools comparing patient characteristics against databases. Most effective when computerized, built into workflow, and providing diagnoses *and* recommendations (Kawamoto et al., 2005).
- **Sabermetrics** (Lewis, 2004): Statistical analysis of baseball data to predict player performance, replacing scouts' intuitive impressions.

**🎯 Bayesian lens:** Clinical intuition represents informal, heuristic Bayesian reasoning — integrating evidence with experience-based priors, but doing so imprecisely and inconsistently. Statistical methods are formal Bayesian (or frequentist) inference — applying the same evidence-weighting rules uniformly across cases. The superiority of statistical methods shows that human intuitive "Bayesian" processing is noisy and biased, especially without calibrating feedback. Expertise without feedback increases confidence (strengthens the prior) without improving the quality of evidence integration.

**Key references:** Meehl (1954/1996); Grove et al. (2000); Dawes, Faust, & Meehl (1989); Garb (1998); Einhorn & Hogarth (1978)

---

### 18. Affective Forecasting

**Definition:** Predictions about how future events would make you feel. People are generally good at predicting *valence* (positive vs. negative) but poor at predicting *intensity* and *duration*.

**Impact bias:** Overestimating how intensely and how long a future event will affect feelings. Can lead to disproportionate effort to facilitate positive or prevent negative events.
- Eastwick et al. (2008): Students predicted higher distress from a romantic breakup than they actually experienced.
- Kahneman & Snell (1992): Predicted increasing dislike of yogurt over 8 days, but actual liking dropped on day 2 then steadily rose.

**Emotional evanescence:** Emotions fade more quickly than anticipated.

**Focalism:** A major cause of impact bias — overestimating how much a specific event would affect feelings and underestimating the influence of other concurrent events.

**Disability paradox:** Healthy people predict they would prefer death over severe disability, but when actually sick, people often feel differently. This raises ethical dilemmas for end-of-life decisions.

**Projection bias** (Loewenstein, 2005): Projecting current mental/emotional state into the future. Slevin et al. (1990): Only 10% of healthy participants but 42% of cancer patients would accept chemotherapy for 3 extra months.

**Hot-cold empathy gap** (Loewenstein, 2005): A specific form of projection bias — people in a "cold" (calm, rational) state cannot accurately predict how they would feel or act in a "hot" (emotional, visceral) state, and vice versa. Leads to underestimating the influence of hunger, pain, craving, or sexual arousal on future decisions. Implications for addiction, dieting, and advance decision-making.

**Peak-end rule:** Evaluating past episodes based on the average of peak intensity and end-point, rather than total duration. Kahneman et al. (1993): Participants preferred a longer pain episode that tapered off over a shorter one with the same peak.

**Living wills / advance directives:** Legal documents expressing end-of-life care preferences. Increase concordance with patient wishes and reduce unwanted interventions (Brinkman-Stoppelenburg et al., 2014). Complicated by affective forecasting errors and the hot-cold empathy gap.

**Intertemporal choice and temporal discounting:** Choosing between immediate and future outcomes. People place less value on future gains the farther away they are. Temporal discounting decreases with age and can be reduced by feeling connected to one's future self — Hershfield et al. (2011): Viewing digitally aged avatars increased retirement savings allocation.

**🎯 Bayesian lens:** Affective forecasting is a prediction task: using current emotional priors and imagined evidence to estimate future emotional posteriors. The impact bias reflects poorly calibrated posteriors — too extreme relative to what the evidence (actual future experience) will support. Projection bias means using the wrong prior (current emotional state) instead of the appropriate one (the likely future state). The hot-cold empathy gap is a failure to update one's model of oneself across different states.

**Key references:** Wilson & Gilbert (2005); Kahneman & Snell (1992); Eastwick et al. (2008); Kahneman et al. (1993); Loewenstein (2005); Hershfield et al. (2011)

---

### 19. Risk Perception and Communication

**Risk perception:** How people judge risks — often misaligned with evidence due to heuristic processing.

**Risk-benefit analyses:** Weighing harms against benefits. Key findings (Starr, 1969; Fischhoff et al., 1978):
- People accept ~1,000 times more risk for *voluntary* vs. *involuntary* activities.
- Experts are influenced more purely by mortality rates; laypeople are swayed by dread and perceived lack of knowledge.

**Unknown risks vs. known risks** (Slovic, 1987): Unknown = new, poorly understood, unobservable. Known = older, well-researched, observable.

**Dread risks:** Catastrophic potential, uncontrollable, unfair distribution. The higher the dread, the more risky people perceive an activity and the more they want strict regulation.
- *Post-9/11 driving fatalities* (Gigerenzer, 2004): Americans avoided flying (dread risk) and drove instead → ~350 additional road deaths. Driving the same distance as the average U.S. flight is 65 times more dangerous even including 9/11.
- *Madrid train bombings* (López-Rousseau, 2005): Reduced train *and* car travel → fewer car fatalities (cultural difference).

**Neglect of low-probability risks:** Extremely low (or high) probabilities are often treated as impossibilities (or certainties).

**Scope insensitivity / scope neglect** (Kahneman, 1986): People's valuations are insensitive to the magnitude of the problem. Willingness to pay is nearly identical for saving 2,000 vs. 20,000 vs. 200,000 migratory birds. Driven by the affect heuristic — an emotional response is generated for the *category* (endangered birds) rather than scaled to the *quantity*. Has enormous implications for charitable giving and public policy.

**Identifiable victim effect** (Small & Loewenstein, 2003): A single identified victim (with a name, face, story) generates more empathy and charitable giving than statistical information about thousands of victims. Combining statistical information with an identified victim can actually *reduce* giving — statistics trigger analytical thinking that dampens emotional response (Small, Loewenstein, & Slovic, 2007).

**Relative risk vs. absolute risk:**
- *Relative risk* (ratio/percentage change) sounds alarming: "twofold increase in blood clots."
- *Absolute risk* gives actual probabilities: "2 in 7,000 vs. 1 in 7,000."
- *Contraceptive pill scare* (mid-1990s UK): "Twofold increase" in clots led to discontinued use and ~13,000 additional abortions — though pregnancy carries higher clot risk than the pill.

**Ambiguity aversion** (Ellsberg, 1961): People prefer known risks over unknown risks, even when the unknown option may be objectively equivalent or better. In the Ellsberg paradox, people prefer drawing from a bag with a known 50/50 red/black split over one with an unknown ratio — despite identical expected value. Connects to the distinction between risk (known probabilities) and uncertainty (unknown probabilities) (§4).

**High-stakes decisions** (Kunreuther et al., 2002): Six deviations from normative reasoning: treating rare events as impossible, shortsightedness, affect heuristic, stress effects, reliance on social cues, and status quo bias.

**Climate change and affect:** Weber (2006): Abstract statistics about global warming influence Type 2 reasoning but fail to trigger the Type 1 emotional reasoning needed to motivate action. Akerlof et al. (2013): People who believed they personally experienced global warming had elevated risk estimates.

**🎯 Bayesian lens:** Risk perception errors often involve distortions in either the prior (ignoring base rates of risk) or the evidence-weighting function (overweighting vivid/dread evidence, underweighting statistical evidence). Scope insensitivity means the posterior does not scale with the magnitude of evidence. Ambiguity aversion reflects discomfort with vague priors — people prefer well-specified priors even when the evidence is identical. The identifiable victim effect shows that narrative evidence (a single case) updates beliefs more powerfully than statistical evidence (base rates) — the exact opposite of what Bayesian weighting would prescribe. Communicating risk as natural frequencies helps because it makes the Bayesian computation transparent (see §2).

**Key references:** Slovic (1987); Gigerenzer (2004); Eddy (1982); Kunreuther et al. (2002); Weber (2006); Kahneman (1986); Ellsberg (1961); Small & Loewenstein (2003)

---

## PART V: CHOICE AND DECISION-MAKING

---

### 20. Models of Rational Choice

**Expected value theory:** Normative model — the most rational option maximizes monetary value over the long run. EV = Σ(value × probability). Limitations: assumes known probabilities, repeated play, and does not capture risk.

**Utility:** Subjective desirability of an outcome (can be non-monetary). Utilities from one person cannot be compared with another's.

**Expected utility theory (EU):** Extends EV by replacing objective values with subjective utilities. Three features (Kahneman & Tversky, 1979): (1) expectation principle (EU = Σ(utility × probability)), (2) accept when EU exceeds current holdings, (3) fundamental risk aversion. Generally normative, not descriptive.
- *Amniocentesis example* (Fan & Levine, 2007): Normative choice depends on how the parent rates possible outcomes.

**Fair gamble:** EV = 0. Risk aversion is demonstrated by refusal to play fair gambles.

**Allais Paradox** (Allais, 1953): People prefer a sure €1,000 over a higher-EV gamble (certainty effect), but when the same utilities appear at lower probabilities (removing certainty), they reverse preferences — logically inconsistent under EU theory, but predicted by prospect theory.

**Multi-attribute utility theory (MAUT) / MCDM:** For decisions with multiple attributes. List attributes → assign importance weights → rate options → calculate weighted sums. Poor as a description but useful as a decision-support tool.
- *Real-life decisions* (Galotti, 2007): People consider 3–9 attributes, 2–5 options; decisions correlate moderately-to-strongly with MAUT predictions.

**One-reason decision-making and Take the Best** (Gigerenzer, 2007): Rank-order attributes by importance; choose the first option that is superior on the most important discriminating attribute. Surprisingly accurate under uncertainty, sometimes outperforming multi-attribute formulas.

**Robust satisficing** (Schwartz, Ben-Haim, & Dacso, 2010): Maximize confidence that the chosen option will be "good enough" across the widest range of scenarios.

**🎯 Bayesian lens:** EU theory is Bayesian-adjacent: it weights outcomes by their probabilities, just as Bayesian inference weights hypotheses by their evidence. MAUT extends this to multi-dimensional updating. Take the Best is a fast-and-frugal approximation that works well when one cue is highly diagnostic — analogous to Bayesian inference dominated by a single strong piece of evidence. Rational choice theory assumes accurate probability estimation; the biases in this course show why this assumption often fails.

**Key references:** Edwards (1954); von Neumann & Morgenstern (1944/2007); Kahneman & Tversky (1979); Allais (1953); Gigerenzer (2007); Galotti (2007)

---

### 21. Prospect Theory

**Definition:** An influential descriptive model of risky choice (Kahneman & Tversky, 1979) accounting for systematic departures from expected utility theory. Kahneman won the 2002 Nobel Prize in Economics for this work.

**Core assumptions:**
1. **Reference dependence:** People evaluate outcomes as gains or losses relative to a reference point (often current state or expectations), not as final wealth.
   - Olympic silver medalists appeared *less happy* than bronze medalists — silver compared to gold (loss), bronze compared to nothing (gain) (Medvec et al., 1995).
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
- **Framing effects:** Gain frames → risk aversion; loss frames → risk seeking. Tversky & Kahneman (1981): "Save 200 of 600" → 72% chose sure option; "400 will die" → 78% chose gamble.
- **Procedure invariance:** Preferences change depending on whether asked to choose or reject. Shafir (1993): A parent with extreme traits was both *chosen* (64%) and *rejected* (55%) for custody.

**Health messaging:** Rothman & Salovey (1997): Gain framing more effective for *prevention* behaviors; loss framing more effective for *detection* behaviors.

**Certainty effect:** Disproportionate preference for certain outcomes over merely probable ones, even when the probable option has higher EV.

**Endowment effect:** People value items they own more than they would value acquiring the same items. Kahneman et al. (1990): Sellers' median price > 2× buyers' price. Explained by loss aversion.

**Source dependence** (Heath & Tversky, 1991): People prefer to bet on outcomes in domains where they feel competent, even when they judge probabilities as equal.

**Risk seeking and politics:** When people feel secure (gain frame) → risk aversion → moderate views. When afraid for their future (loss frame) → risk seeking → extreme views. Populist politicians exploit this with fear-based discourse.

**🎯 Bayesian lens:** Prospect theory describes systematic distortions in how people weight probabilities — the decision weight function w(P) is a biased transformation of true probabilities. A Bayesian agent would use P directly; prospect-theory agents overweight small P and underweight large P. Framing effects show that the *same evidence* produces different posteriors depending on how it is presented — a direct violation of Bayesian invariance. The reference point functions as a prior: what counts as a "gain" or "loss" depends entirely on where one starts.

**Key references:** Kahneman & Tversky (1979); Tversky & Kahneman (1981, 1992); Barberis (2013); Heath & Tversky (1991)

---

### NEW. Satisficing vs. Maximizing

**Core idea:** When faced with a set of options, people differ in how they search — and when they stop. This has important consequences for decision quality, effort, and well-being.

- **Satisficing** (Simon, 1956): Selecting an option that is "good enough" — one that meets a minimum threshold of acceptability. The decision-maker stops searching as soon as a satisfactory option is found.
- **Maximizing:** Striving for the best possible option by exhaustively comparing all available alternatives. This sounds rational in theory, but in practice it is costly: it requires evaluating more options, making more comparisons, and often leads to greater regret (because the decision-maker is more aware of what they might have missed).
- **The maximizing paradox** (Schwartz, 2004): Maximizers tend to achieve objectively *better* outcomes than satisficers, but feel *worse* about them — experiencing more regret, less satisfaction, and more counterfactual thinking ("what if I had chosen differently?"). More choice can make maximizers worse off.
- As a personality trait, maximizing is associated with regret, depression, perfectionism, and neuroticism. Importantly, maximizing is *not* the same as having high standards — a person can have high standards while still satisficing (they simply set a high threshold for "good enough").
- Satisficing is a direct consequence of bounded rationality: because we lack the time, information, and cognitive capacity to evaluate all options, "good enough" is often the best we can do — and often leads to better subjective outcomes than relentless optimization.
- Connects to choice architecture (§23): the number and presentation of options interacts with a person's tendency to satisfice vs. maximize. Choice overload is particularly harmful for maximizers.

**🎯 Bayesian lens:** Maximizing assumes you can compute the expected value of every option and select the highest — essentially a full Bayesian decision analysis. Satisficing acknowledges that this computation is often infeasible and replaces it with a simpler threshold rule: is the posterior probability that this option is "good enough" sufficiently high? This is a resource-rational strategy — trading a small expected loss in quality for a large saving in cognitive effort.

**Key references:** Simon (1956); Schwartz (2004); Schwartz et al. (2002); Vargová et al. (2020)

---

### 22. Mental Accounting, Sunk Costs, and Spending Behavior

**Mental accounting** (Thaler, 1999): Informal rules by which people track and categorize resources, treating categories differently despite objective equivalence — violating the **principle of fungibility** (one dollar is equivalent to any other dollar).

**Behavioral life-cycle (BLC) hypothesis** (Shefrin & Thaler, 1988): People divide wealth into three mental accounts:
- *Current income* (paychecks, small bonuses) — readily spent.
- *Current assets* (non-retirement savings, windfalls) — reluctantly spent.
- *Future wealth* (retirement, future income) — largely disregarded.
- **Self-control** and **commitment devices** (e.g., automatic deductions) reduce the need for effortful restraint.
- **Elderly spending puzzle:** Normatively, elderly people should spend down assets, but they resist.

**Sunk cost effect:** Continuing to invest in a losing course because of what has already been spent, even though sunk costs should be irrelevant.
- Arkes & Blumer (1985): 54% chose a more expensive but less enjoyable ski trip; 85% continued funding a near-complete project vs. 17% when no prior investment existed.
- Develops with age and socialization (the "don't waste" heuristic) (Arkes & Ayton, 1999).

**Time vs. money:** Time-based sunk costs do *not* produce the same sunk cost effect. Soman (2001): 95% chose the more enjoyable event when tickets were earned through time, but only 38% when money was at stake.

**Price primacy vs. product primacy:** Seeing the product first activates reward areas (nucleus accumbens); seeing the price first may trigger analytical evaluation (Knutson et al., 2007; Karmarkar et al., 2015).

**🎯 Bayesian lens:** Mental accounting violates Bayesian principles because evidence (money) is not treated as fungible — the same dollar is weighted differently depending on its "account." The sunk cost fallacy means that past evidence (already spent resources) inappropriately biases the posterior about whether to continue, when only future costs and benefits should matter. A Bayesian agent would update beliefs about a project's value based on current evidence, not past investments.

**Key references:** Thaler (1980, 1999); Shefrin & Thaler (1988); Arkes & Blumer (1985); Soman (2001)

---

### 23. Choice Architecture: Nudges, Defaults, and Libertarian Paternalism

**Mandates and bans:** The most restrictive interventions — removing options entirely. **Economic incentives/disincentives:** Linking monetary gains/losses to specific choices.

**Nudges** (Thaler & Sunstein, 2008): Liberty-preserving interventions steering people toward particular choices while allowing opting out. Types include:
- **Default rules:** Pre-selecting the desired option, exploiting the **status quo bias** (preference for inaction). Johnson & Goldstein (2004): Austria's opt-out organ donation → ~100% consent vs. Germany's opt-in → 12%.
- **Increasing ease/visibility** of desired choices.
- **Social pressure:** Making behavior visible.
- **Educational nudges** (e.g., graphic health warnings on tobacco; meta-analyses suggest they increase willingness to quit, but effectiveness wears off) (Pang et al., 2021).

**Libertarian paternalism:** The philosophy that institutions can influence behavior for people's benefit while preserving liberty. Because no choice environment is truly neutral, nudges are unavoidable and should be designed for beneficial outcomes.

**Choice overload effect:** More options can lead to worse outcomes — lower purchase likelihood, lower quality decisions.
- Iyengar & Lepper (2000): 24 jam samples → 3% bought; 6 samples → 30% bought.

**Maximization Scale** (Schwartz et al., 2002): Higher scores correlate with regret, depression, perfectionism; lower scores with happiness, satisfaction, optimism.

**🎯 Bayesian lens:** Choice architecture manipulates the prior. Defaults set a strong prior that most people do not override — equivalent to starting with a highly weighted anchor. The status quo bias reflects an asymmetry in updating: maintaining the current state requires no evidence, while switching requires overcoming an evidentiary threshold. Nudges work precisely because people are not fully Bayesian — a rational agent would choose identically regardless of default framing.

**Key references:** Thaler & Sunstein (2008); Sunstein (2014); Johnson & Goldstein (2004); Iyengar & Lepper (2000); Schwartz et al. (2002)

---

### 24. Group Decision-Making

**Core idea:** Many consequential decisions are made by groups (committees, juries, teams, boards). Group processes can improve or degrade decision quality compared to individuals.

**Wisdom of crowds** (Galton, 1907; Surowiecki, 2004): Aggregating many independent judgments often produces remarkably accurate estimates — sometimes outperforming individual experts. Conditions for success: diversity of opinion, independence (not influenced by others), decentralization, and a mechanism for aggregation. Breaks down when judgments are not independent (e.g., social influence, shared information).

**Group polarization** (Moscovici & Zavalloni, 1969): Group discussion tends to shift members toward a more extreme version of their initial inclinations. Risky individuals become riskier; cautious individuals become more cautious. Mechanisms: persuasive arguments (exposure to novel arguments supporting the dominant view) and social comparison (competing to be more extreme than the group norm).

**Groupthink** (Janis, 1972): Highly cohesive groups with strong leaders may prioritize consensus over critical evaluation, leading to poor decisions. Symptoms: illusion of invulnerability, collective rationalization, stereotyping of outgroups, self-censorship, illusion of unanimity. Classic cases: Bay of Pigs, Challenger disaster. Preventive measures: assign a devil's advocate, encourage dissent, consult external experts.

**Shared information bias** (Stasser & Titus, 1985): Groups spend disproportionate time discussing information already known to all members and neglect unique information held by individual members — even when the unique information would change the decision. Structured information-sharing protocols can mitigate this.

**🎯 Bayesian lens:** The wisdom of crowds works because aggregation approximates Bayesian integration — each person's independent estimate is a noisy signal, and averaging reduces noise, converging on the true posterior. Groupthink and group polarization represent failures of independent evidence sampling: when group members share the same prior and the same biased evidence, the group's "posterior" becomes more extreme without more evidence — a form of collective overconfidence. Shared information bias means the group updates from redundant evidence (shared information) while ignoring unique diagnostic evidence.

**Key references:** Galton (1907); Surowiecki (2004); Janis (1972); Moscovici & Zavalloni (1969); Stasser & Titus (1985)

---

## PART VI: CONFIRMATION, BELIEF, AND RESISTANCE TO CHANGE

---

### 25. Confirmation Bias

**Definition:** A pervasive tendency to seek, interpret, and favor information that confirms existing beliefs or hypotheses, manifesting in both selective search and reinterpretation of evidence. Proposed as the single cognitive bias most relevant to ideological extremism.

**Logical foundation — confirmatory vs. disconfirmatory evidence:**
- *Confirmatory evidence:* Consistent with a hypothesis but cannot definitively prove it.
- *Disconfirmatory evidence:* Refutes a hypothesis. Uniquely powerful — a single piece can topple a hypothesis.
- **Falsifiability** (Popper, 1959/1968): Science should center on attempting to disconfirm hypotheses. In practice, people treat abundant confirmatory evidence as proof.

**Positive test strategy:** Examining instances where the hypothesized property is expected to occur. Not always ineffective — when the hypothesis is more *general* than the true rule, positive testing can elicit useful disconfirmatory feedback.

**Negative test strategy:** Trying to find cases that *disconfirm* the hypothesis. Most valuable when the hypothesis is more *specific* than the true rule.

**2-4-6 task** (Wason, 1960): Only 21% found the rule — most used positive test strategies, testing only confirming sequences.

**Consistency fallacy** (Mole & Klein, 2010): Data that merely *confirm* a hypothesis are misinterpreted as proving it. People are more convinced by psychological explanations accompanied by neuroscience descriptions, even irrelevant ones (Weisberg et al., 2008).

**Forensic confirmation bias:** Prior expectations influence evidence collection and interpretation in criminal cases.
- *Madrid bombings fingerprint* (OIG, 2006): Three FBI experts matched a print to an innocent man; they began "finding" additional features suggested by the suspect's prints.
- Dror & Charlton (2006): Practicing fingerprint experts' identifications were influenced by background case information.
- Advocated solution: **linear processing** — analyze each piece of evidence fully before comparing to suspect information.

**Confirmation bias in medical diagnosis:** Mendel et al. (2011): Both psychiatrists (13%) and students (25%) using confirmatory strategies were much more likely to make wrong diagnoses. However, a confirmatory strategy is efficient when the initial hypothesis is correct.

**Bias blind spot** (Pronin et al., 2002): People believe *others* are more prone to biases than they themselves are. Persists across diverse populations. Makes debiasing especially challenging.

**Debiasing:** Most promising approaches shift people from Type 1 to Type 2 thinking: generating alternative viewpoints, delaying decisions. Challenges: bias blind spot, deeply entrenched beliefs.

**🎯 Bayesian lens:** Confirmation bias is a fundamental violation of Bayesian updating. A Bayesian agent should weight evidence symmetrically — updating equally from confirming and disconfirming evidence (proportional to their diagnosticity). Confirmation bias produces *asymmetric updating*: confirming evidence strengthens beliefs while disconfirming evidence is discounted or ignored. This creates a self-reinforcing cycle where the posterior drifts ever further from what balanced evidence would warrant. In Bayesian terms, people treat the likelihood ratio as if disconfirming evidence has low diagnosticity, when in fact a single disconfirming observation can be enormously informative.

**Key references:** Klayman & Ha (1987); Nickerson (1998); Wason (1960); Kassin, Dror, & Kukucka (2013); Pronin et al. (2002)

---

### 26. Belief Formation, Perseverance, and Irrational Beliefs

**Spinozan belief (automatic acceptance)** (Gilbert, 1991): Following Spinoza, people automatically accept information in the process of understanding it. Rejecting false information requires a subsequent deliberate evaluation. When this process is disrupted (interruption, time pressure, cognitive load), people fail to reject falsehoods.
- Gilbert et al. (1990): Interruption during true/false identification had no effect on recognizing true statements, but severely impaired identifying false statements — strong tendency to say "true."

**Executive control and belief:** Higher CRT scores predict less acceptance of paranormal and irrational beliefs. Consistent with the Spinozan hypothesis: people are natural believers who can become skeptics with effort.

**Belief perseverance:** Once accepted, beliefs are incredibly resistant to contradictory evidence. People who show belief perseverance also tend to presume intentionality and prefer simple causal explanations.

**Continued influence effect:** Erroneous ideas continue to influence judgments even after retraction and even when the correction is understood and accepted. Retraction never fully erases misinformation influence.
- *Warehouse fire studies:* Even with retraction, judgments continued to reflect misinformation. Adding "clarifying" negated statements can produce a **rebound effect**, making misinformation *more* influential.

**Myth-versus-fact backfire:** Repeated exposure to a statement (even retracted) increases familiarity.
- Schwarz et al. (2007): 30 minutes after reading a myth-vs-fact handout, people were *more likely* to misidentify myths as facts and *less likely* to intend vaccination.

**Reactance** (Brehm & Brehm, 1981): Strong physiological response when freedom to think/act is threatened, intensifying intent to do the opposite. When judges ask jurors to disregard evidence, jurors cling more strongly to it.

**Backfire effect:** Instructions to disregard information cause people to rely on it *more heavily*. Cox & Tanford (1989): Jurors told to disregard damaging evidence recommended *harsher* punishments.

**Cognitive dissonance:** Mental discomfort from internal conflict (e.g., beliefs vs. new evidence). To reduce it, people either update beliefs or reject/question the evidence.

**Biases and heuristics that protect beliefs (System 1 mechanisms):** Mere exposure (familiar = true), availability heuristic (easy-to-recall = true), confirmation bias (seek confirming information), source amnesia (forget where we learned something). Together, these make it hard to be aware of something without believing it.

**Paranormal beliefs and superstitions:** Scientifically unaccepted beliefs (astrology, telekinesis, magical contamination). Incredibly common among ordinary adults. Driven by illusory causality, hindsight bias, confirmation bias, and domain overextension.
- **Law of contagion** (Rozin et al., 1989): An undesirable person contacting an object transmits undesirable properties that persist even after cleaning.
- **Law of similarity** (Rozin et al., 1986): An object perceptually similar to a disgusting object is felt to acquire its undesirable properties.
- **Core knowledge confusions** (Lindeman & Aarnio, 2007): Magical thinking emerges when domain-specific core knowledge is inappropriately overextended (e.g., biological contamination logic applied to social judgments). The confusions scale predicts paranormal beliefs and remains undiminished across undergraduate education.
- **Evolutionary account** (Bering, 2006): Predisposition to believe in the supernatural may carry evolutionary advantage — refraining from dishonest behavior (fear of being observed by non-physical beings) increases survival.

**🎯 Bayesian lens:** Belief perseverance represents a failure to update the prior from disconfirming evidence — the prior is treated as virtually certain (P ≈ 1), making any single piece of counter-evidence insufficient to shift the posterior. Spinozan acceptance means that all incoming information is initially treated as having a high prior (P(true) is the default), requiring effortful System 2 processing to revise downward. The continued influence effect shows that even after a "retraction update," the original information retains residual influence on the posterior — the update is incomplete. Irrational beliefs like superstitions reflect over-application of priors from one domain (biological contamination) to another where they do not apply.

**Key references:** Gilbert (1991); Lewandowsky et al. (2012); Schwarz et al. (2007); Brehm & Brehm (1981); Rozin et al. (1986, 1989); Lindeman & Aarnio (2007); Bering (2006)

---

### 27. Conspiracy Theories and Rejection of Science

**Conspiracy theories:** Explanations invoking secret plots by powerful people. Can be false, partially true, or completely true. A key characteristic: contradictory evidence is absorbed into the theory by claiming it is part of the cover-up. People may endorse mutually contradictory conspiracies simultaneously (Wood et al., 2012: believing both that Diana faked her death *and* was murdered).

**Cognitive and personality factors** that positively correlate with conspiracy thinking: seeing patterns in randomness, paranormal beliefs, attributing agency where it doesn't exist, preferring simple explanations, narcissism, and being male. Negatively correlated with intelligence and analytical thinking.

**Existential factors:** Conspiracy theories may help deal with existential threats by regaining a sense of control through explaining the unexplainable.

**Social factors:** Often have ingroup–outgroup structure ("we" the noble oppressed vs. "they" the conspiring elite). Related to populism. More common in disadvantaged groups.

**Rejection of science:** A form of conspiracy thinking, built on beliefs that scientists have hidden agendas.
- Lewandowsky et al. (2013): Free-market ideology strongly predicted rejecting climate science and the smoking–cancer link but not HIV–AIDS. Conspiracy thinking predicted rejection of all science findings.

**🎯 Bayesian lens:** Conspiracy theories are self-sealing belief systems: the prior P(conspiracy) is set so high that *all evidence* — supporting or contradicting — is reinterpreted to increase the posterior. Disconfirming evidence is recoded as confirming ("that's exactly what they'd want you to think"). This makes the belief unfalsifiable and immune to Bayesian updating. Endorsing mutually contradictory conspiracies reveals that the updating is not about specific evidence at all, but about a meta-prior: "powerful people are conspiring." Rejection of science involves discounting the credibility of evidence sources, effectively setting the likelihood of scientific evidence to near zero.

**Key references:** Douglas & Sutton (2008); Wood et al. (2012); Lewandowsky et al. (2013); Douglas et al. (2019)

---

## PART VII: MORAL JUDGMENT AND COOPERATION

---

### 28. Models of Moral Judgment

**Morality and personal identity:** People consider morality an essential component of identity — more so than memories, personality, mental abilities, or preferences. Strohminger & Nichols (2014): Brain transplant recipients who lost morality were rated as having retained identity *less* than those who lost all long-term memories.

**Emotion as self-perception** (William James, 1884): Emotion derives *first* from a bodily response (arousal), which is then shaped by cognitive appraisal. Bodily states (e.g., hunger) can affect emotional responses to neutral stimuli (MacCormack & Lindquist, 2018).

**Rationalist view:** People first consciously reason through a moral problem, then arrive at a judgment.

**Kohlberg's stages of moral development** (1971): Children develop moral reasoning over six stages in three levels:
- *Pre-conventional (Stages 1–2):* Seeking rewards, avoiding punishment.
- *Conventional (Stages 3–4):* Upholding social conventions. Stage 3: interpersonal concerns (caring). Stage 4: following rules and laws.
- *Post-conventional (Stages 5–6):* Universal moral principles. May protest unjust laws.
- Responses classified by *reasons given*, not the answer itself. Gilligan (1982) critiqued male-only samples; meta-analysis (Jaffee & Hyde, 2000) found weak gender effects.

**Social interactionist model** (Turiel, 2002): Rationalist model proposing three domains — personal, moral (inherently harmful), social (violating local rules). Children as young as 5–6 distinguish social conventions from moral principles. Haidt et al. (1993): High-SES people classified offensive-but-harmless actions as social conventions; low-SES classified them as moral.

**Social intuitionist model** (Haidt, 2001, 2012): Moral judgments are primarily driven by intuitive gut feelings (System 1). Reasoning comes *after* as post-hoc justification.
- *Moral dumbfounding:* People have definite moral opinions but cannot produce clear reasons.
- **Wag-the-dog illusion:** The mistaken belief that our moral judgment is driven by our reasoning.
- **Wag-the-other-dog's-tail illusion:** The mistaken belief that rebutting someone's reasoning will change their moral position. Instead, change their emotional response.

**Moral Foundations Theory** (Graham, Haidt, & Nosek, 2009): Five dimensions of moral intuition: Harm, Fairness, Ingroup, Authority, Purity. US liberals emphasize harm and fairness; US conservatives place relatively more weight on ingroup, authority, and purity.

**Evolutionary roots of morality:** Darwin argued any sufficiently social and intelligent animal would develop a moral sense. Many species show empathy, retribution, and fairness. Capuchin monkeys visibly upset when a partner receives a better reward for the same task (De Waal, 2003). Morality can be understood as cooperation, existing at all levels of biological organization.

**Somatic marker hypothesis** (Bechara, Damasio, & Damasio, 2000): Emotional bodily experience strongly influences decisions. Without emotional gut feelings (due to brain damage), decision-making is severely impaired.
- *Phineas Gage* (1848): Ventromedial prefrontal cortex damage → profound personality and decision-making changes, intact reasoning.

**🎯 Bayesian lens:** Moral intuitions function as strong priors: they are formed early, feel certain, and resist updating from evidence or argument. The social intuitionist model implies that moral reasoning is not Bayesian belief-updating from evidence but rather post-hoc rationalization of a pre-set prior. Changing moral positions requires changing the prior (emotional intuition), not presenting disconfirming evidence to the posterior (rational argument). Moral Foundations Theory describes the *content* of moral priors, which vary systematically across individuals and cultures. The somatic marker hypothesis suggests that these priors are literally embodied — encoded in bodily sensations, not just cognitive representations.

**Key references:** Kohlberg (1971); Haidt (2001, 2012); Graham et al. (2009); Turiel (2002); Bechara et al. (2000); Strohminger & Nichols (2014); De Waal (2003)

---

### 29. Moral Dilemmas and Neuroscience

**Trolley dilemma:** Flip a switch to divert a trolley from five people to one. Most choose the utilitarian option (save five). Brain areas associated with working memory more active during such impersonal dilemmas (Greene et al., 2001).

**Footbridge dilemma:** Push a large stranger off a bridge to stop a trolley from killing five. Despite identical utilitarian structure, people generally refuse. Pushing is more personal → stronger affective response. Emotional brain areas showed heightened activity (Greene et al., 2001), supporting a dual-process account.
- Valdesolo & DeSteno (2006): Positive mood significantly increased willingness to push.
- Schnall et al. (2008): Induced disgust ("fart spray") made people less morally lenient.
- Eskine et al. (2011): Bitter-tasting liquid reduced moral leniency, especially for political conservatives.

**Omission bias:** The tendency to judge harmful *actions* as worse than equally harmful *omissions* (inaction). In trolley dilemmas, actively pushing someone feels worse than passively allowing deaths — even when the outcome is identical or worse. Connects to status quo bias (§23): doing nothing is the default. Relevant to vaccination (perceived risk of acting > perceived risk of not acting) and end-of-life decisions (withdrawing treatment vs. not starting it).

**Transfer effects** (Wiegmann et al., 2012): Responses to one dilemma influence the next, but asymmetrically — footbridge before trolley reduces utilitarian responses in trolley, but not vice versa.

**Causal model theory of transfer effects** (Wiegmann & Waldmann, 2014): Transfer is based on analogy to causal structure, not emotional carry-over. Intuitions about unambiguous scenarios transfer to ambiguous ones, not vice versa.

**🎯 Bayesian lens:** Moral dilemmas pit two inference systems against each other: an emotional prior (do not harm directly) and a deliberative likelihood calculation (five lives > one life). In impersonal dilemmas, the emotional prior is weak, so deliberative updating drives the decision. In personal dilemmas, the emotional prior is so strong that utilitarian evidence barely shifts the posterior. Mood and disgust manipulations alter the strength of the emotional prior. Omission bias reflects a prior that inaction is morally neutral — updating from evidence about equivalent outcomes is insufficient to overcome it.

**Key references:** Greene et al. (2001); Valdesolo & DeSteno (2006); Wiegmann & Waldmann (2014); Ritov & Baron (1990)

---

### 30. Game Theory and Cooperation

**Zero-sum game:** Gains and losses among players sum to zero.

**Tragedy of the commons** (Hardin, 1968): Multiple individuals sharing a common resource each try to increase personal wealth, leading to destruction of the resource for everyone.

**Game theory:** Studies how people's choices interact to affect outcomes. Key contribution: people must consider not only their own preferences but expectations about others' preferences.

**Prisoner's dilemma** (Flood, 1958; Tucker, 1983): Two players choose to cooperate or defect. Despite the **Nash equilibrium** predicting mutual defection, behavioral studies show substantial cooperation (~55% among German prisoners; Khadjavi & Lange, 2013).

**Tit for Tat** (Axelrod, 1984): Won two successive iterated prisoner's dilemma competitions. Always cooperates first, then copies opponent's previous move. Key properties: never defects first; retaliates immediately; forgives immediately.

**Public goods:** Benefits available to everyone through collective contributions. Classic rationality predicts they should never exist (everyone would free ride), yet they emerge in virtually every society.
- **Free riding:** Benefiting without contributing. Cooperation increases when: goals seem achievable, systems encourage cooperation and punish non-cooperation, and people identify with the group.

**🎯 Bayesian lens:** Strategic decision-making requires maintaining and updating beliefs about others' likely behavior. Each round of interaction provides evidence that updates the prior about the opponent's type (cooperative vs. selfish). Tit for Tat is implicitly Bayesian: it starts with a cooperative prior and updates immediately from the opponent's last action. The tragedy of the commons represents a situation where individually rational Bayesian agents (each updating on their own payoffs) collectively produce an irrational outcome — illustrating that local Bayesian optimality does not guarantee global optimality.

**Key references:** Hardin (1968); Nash (1950); Axelrod (1984); Parks, Joireman, & Van Lange (2013)

---

## PART VIII: APPLIED CONTEXTS

---

### 31. Medical and Clinical Decision-Making

**Schemas in clinical judgment:** Clinicians hold causal models of mental disorders that function as schemas. They show significant agreement on causal structure, weight causally central symptoms more (even though DSM gives equal weight), and their treatment recommendations can be predicted from their causal models.
- Kim & Ahn (2002a, 2002b): Clinicians agreed on causal models and diagnosed based on causal centrality.
- Flores et al. (2014): Causally inconsistent temporal order of symptoms slowed reading and reduced diagnostic agreement.
- De Los Reyes & Marsh (2011): Non-symptom contextual information strongly influenced conduct disorder judgments.

**Anchoring in diagnosis:** Clinicians may anchor on initial hypotheses and distort cues to fit (see §10). Experience reduces but does not eliminate susceptibility.

**Availability in diagnosis:** Recently seen cases influence diagnosis of new cases (see §8). Effect may increase with expertise.

**Confirmation bias in diagnosis:** Confirmatory search is harmful when paired with anchoring; efficient when the initial hypothesis is correct (see §25).

**Decision support systems:** Most effective when computerized, built into workflow, and providing diagnoses plus recommendations.

**Natural frequencies and Bayes' Theorem:** Physicians reason far more accurately when given natural frequencies rather than conditional probabilities (see §2, §19).

**🎯 Bayesian lens:** Medical diagnosis is Bayesian updating in action: the physician starts with a prior (base rate of the disease, patient demographics), gathers evidence (symptoms, tests), and arrives at a posterior (diagnostic probability). Every bias in clinical reasoning maps onto a specific Bayesian failure: anchoring = sticky prior, availability = biased evidence sampling, confirmation bias = asymmetric updating. Decision support systems improve decisions precisely because they formalize the Bayesian computation that clinicians perform intuitively and imperfectly.

**Key references:** Kim & Ahn (2002); Flores et al. (2014); Mendel et al. (2011); Eddy (1982); Hoffrage & Gigerenzer (1998)

---

### 32. Legal Decision-Making

**Information integration theory** (Kaplan & Kemmerick, 1974): Each piece of evidence has a guilt/innocence value, weighted by importance, and combined with the juror's prior.

**Story model** (Pennington & Hastie, 1986, 1988, 1992): Jurors reason in three steps:
1. Construct a coherent, temporally ordered story using an **episode schema**.
2. Learn verdict categories and qualifications.
3. Seek a match between story and verdicts.
- ~45% of story elements are inferences about mental states/goals rather than direct testimony. Equal numbers of jurors watching the same trial chose different verdicts based on different stories.

**Forensic confirmation bias:** Prior expectations influence evidence collection and interpretation (see §25). Advocated solution: linear (non-circular) processing.

**Temporal order in trials:** Evidence presented in temporal order makes jurors more convinced (see §14). Pennington & Hastie (1988): Guilty verdicts most likely when prosecution's evidence was temporal and defense's was scrambled.

**Reactance/backfire in jury instructions:** Instructions to disregard evidence can backfire (see §26).

**🎯 Bayesian lens:** The legal process is formally structured as sequential Bayesian updating: jurors start with a prior (presumption of innocence), receive evidence piece by piece, and arrive at a posterior (guilt beyond reasonable doubt). The story model shows that jurors do not update incrementally but construct holistic narratives — prior-driven interpretation of evidence rather than evidence-driven updating of the prior. Information integration theory is explicitly Bayesian in structure (weighted combination of prior and evidence). Forensic confirmation bias shows that practitioners' strong priors contaminate evidence evaluation.

**Key references:** Pennington & Hastie (1986, 1988, 1992); Kassin et al. (2013); Dror (2009)

---

### 33. Social Media, Populism, and Misinformation

**Populism:** A political approach appealing to "ordinary people" who don't consider themselves part of the ruling class. Features: mistrust of ruling class, nationalism, moral outrage, strong leader, promise of change, traditional values. Exists across the political spectrum. Existed long before social media.

**Social media:** Digital platforms for user-generated content (~5 billion users worldwide, ~2.5 hours/day). Believed to negatively affect mental health and societal functioning, though much remains unclear.

**Social media as a catalyst for populism:** Not the root cause, but an amplifier. Guriev et al. (2020): 3G mobile internet rollout predicted decreased government approval and more populist votes worldwide. Lorenz-Spreen et al. (2023): Digital media increased political participation but also hate, polarization, and populism.

**Moral outrage on social media:** Strongly attracts attention (consistent with negativity bias). Very few create morally outraged content (associated with dark-triad traits), but it is widely shared.
- Rathje et al. (2021): Out-group language substantially increased engagement.
- Humprecht et al. (2024): Populist politicians' posts generated disproportionately more "angry" reactions.

**Misinformation:** Lies and half-truths spread organically. Schaffner & Luks (2018): Highly educated Trump voters incorrectly chose Trump's inauguration photo as more attended — possibly as participatory propaganda rather than genuine belief.

**Social media as a decoy:** Populist leaders may strategically tweet to divert attention from damaging coverage. Lewandowsky et al. (2020): Trump systematically tweeted about immigration/economy in response to damaging articles.

**Social-media dynamics and algorithms:** Algorithms boost popular content, creating a semi-random winner-takes-all process. Typical winners: extreme views and moral outrage. Larooij & Törnberg (2025): Six algorithmic changes produced modest effects — attention inequality and polarization appear inherent to user-generated content platforms.

**🎯 Bayesian lens:** Social media systematically distorts the evidence available for belief updating. Algorithms create biased evidence samples (echo chambers) — users receive a non-representative stream of information that confirms their existing priors. Negativity bias in engagement means negative and outrage-inducing content is overrepresented in the evidence stream, distorting posteriors about the state of the world. Misinformation exploits Spinozan acceptance (§26): information is believed by default, and the volume/speed of social media overwhelms the System 2 processing needed for correction. The result is polarization — two groups updating from entirely different evidence samples arrive at radically different posteriors about the same world.

**Key references:** Guriev et al. (2020); Lorenz-Spreen et al. (2023); Rathje et al. (2021); Lewandowsky et al. (2020); Larooij & Törnberg (2025)

---

### 34. AI and Decision-Making

**Core idea:** Artificial intelligence — particularly large language models (LLMs) — provides a revealing mirror for human judgment and decision-making. Many of the biases, heuristics, and dual-process phenomena studied in human cognition have direct parallels in AI systems, and understanding these parallels deepens insight into both.

**System 1 / System 2 and LLMs:**
- Standard LLM output resembles System 1: fast, pattern-based, associative, drawing on statistical regularities in training data. The model generates plausible-sounding responses without explicit step-by-step reasoning.
- **Chain-of-thought (CoT) prompting** and **reasoning models** (e.g., OpenAI's o-series) resemble System 2: the model is prompted or trained to produce intermediate reasoning steps before arriving at an answer. This improves performance on logical, mathematical, and multi-step problems — paralleling how System 2 overrides System 1 errors in humans.
- The analogy is imperfect but pedagogically powerful: CoT reasoning, like human System 2, is slower and more resource-intensive, but reduces errors on problems that require deliberation.

**Where do AI biases come from?**
- LLMs are trained on vast corpora of human-generated text that embed human biases — stereotypes, framing effects, cultural assumptions. AI biases are, to a significant degree, inherited human biases.
- LLMs replicate many classic biases: anchoring (influenced by numbers in the prompt), framing effects (different responses to gain vs. loss frames), sycophancy (a form of confirmation bias — telling users what they want to hear), and representativeness-like pattern matching.
- This replication is itself evidence about the nature of these biases: if they emerge from statistical patterns in language, they may be deeply embedded in how knowledge is structured and communicated — not just quirks of neural hardware.

**AI hallucination and human confabulation:**
- LLMs sometimes generate confident, plausible-sounding but factually incorrect outputs ("hallucinations"). This parallels human confabulation (§7): both involve pattern completion without verification — producing what *fits* the context rather than what is *true*.
- In both cases, the system generates the most probable completion given the context (a kind of "maximum likelihood" response), without checking against ground truth. Humans confabulate when schemas dominate verification (System 1 without System 2 correction); LLMs hallucinate because they lack a ground-truth verification mechanism entirely.

**Calibration in AI:**
- LLMs are often poorly calibrated — expressing high confidence in incorrect answers, mirroring human overconfidence (§12). When asked to estimate their own certainty, models' stated confidence frequently does not match their actual accuracy.
- Improving AI calibration is an active research area, just as improving human calibration is a goal of debiasing interventions.

**AI as decision support:**
- AI systems are increasingly used as clinical decision support (§31), legal risk assessment, and financial forecasting tools.
- The evidence on human decision support systems (§17) applies: AI-assisted decisions are most effective when recommendations are specific, integrated into workflow, and when the human retains the ability to override.
- Risk: automation bias — over-relying on AI recommendations, analogous to anchoring on an initial hypothesis. Users may accept AI suggestions uncritically, especially when the AI expresses high confidence.

**Algorithmic bias in high-stakes contexts:**
- AI systems used in criminal sentencing (e.g., COMPAS), hiring, and medical triage can encode and amplify societal biases present in training data.
- This connects to the base-rate and representativeness problems (§9): if historical data reflects discriminatory patterns, a model trained on this data will reproduce those patterns as "base rates" — making biased predictions appear statistically justified.
- Fairness in AI requires deliberate choices about which base rates to use and which to correct for — a prescriptive challenge (§4).

**The Turing test revisited** (Turing, 1950): A machine exhibits human-like intelligence if an interrogator cannot distinguish it from a human in text-based conversation. Modern LLMs pass convincingly, but debate continues about whether this reflects genuine understanding or sophisticated pattern completion. The debate parallels the distinction between System 1 mimicry (producing human-like outputs) and System 2 reasoning (genuinely understanding the problem).

**🎯 Bayesian lens:** LLMs can be understood as approximate Bayesian reasoners: training data constitutes the prior, the prompt is the evidence, and the output is the posterior (most likely completion given prior + evidence). Biases in LLMs arise from biased priors (training data), just as human biases arise from biased experiential priors. Chain-of-thought reasoning improves performance by making the evidence-integration process more explicit — analogous to how deliberate Bayesian computation outperforms intuitive shortcuts. AI hallucination occurs when the prior (training patterns) dominates over evidence (factual constraints) — the same mechanism behind human confirmation bias and belief perseverance. Calibration failures in AI mirror the human overconfidence that arises from insufficiently wide posterior distributions.

**Key references:** Turing (1950); Wei et al. (2022); Bommasani et al. (2021); Weidinger et al. (2021); Angwin et al. (2016)