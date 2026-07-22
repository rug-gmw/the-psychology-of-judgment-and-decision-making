# Artificial Intelligence


Learning goals:


- Explain the Turing test and why shifting definitions of intelligence reveal something about human intuitions.
- Describe how large language models relate to dual-process theory, including the role of chain-of-thought prompting.
- Distinguish between crystallized and fluid intelligence in the context of large language models.
- Explain where biases in AI systems come from and how they relate to human cognitive biases.
- Compare AI hallucination with human confabulation.
- Describe how calibration failures in AI mirror human overconfidence.


## Machines That Think Like Us


Imagine a university student who asks an AI chatbot to explain a concept from a specific academic paper. The chatbot responds fluently: it names the paper, describes the authors, and summarizes the key findings. The summary is detailed and confident. There is just one problem — the paper does not exist. The chatbot invented the title, the authors, and the findings, generating what a real citation would look like based on patterns in its training data. The student, finding the response convincing, cites the fabricated paper in a follow-up assignment.


This kind of scenario has become commonplace since the widespread adoption of large language models (LLMs), and it captures something important about artificial intelligence. The same system that produces impressively human-like output can also fail in strikingly human-like ways. Throughout this book, we have examined how people judge, decide, and reason, and where these processes go wrong. In this final chapter, we turn to LLMs because they serve as a revealing mirror for human cognition. Many of the biases, heuristics, and reasoning failures we have studied reappear in AI systems, and understanding why deepens our insight into both machines and minds.


A note before we proceed: throughout this chapter, we will describe what LLMs "do" using language that can sound as if these systems have intentions, beliefs, or experiences. When we say a model "assumes" something or "lacks verification," these are functional descriptions and analogies, not claims about machine consciousness. The parallels with human cognition are instructive precisely because they hold at the level of process and output, regardless of whether anything resembling subjective experience is involved.


## The Turing Test and Shifting Goalposts


In 1950, the mathematician Alan Turing proposed a simple test for machine intelligence. Rather than asking the unanswerable question "Can machines think?", he suggested an operational alternative: if a human interrogator, communicating by text with both a machine and a person, cannot reliably tell which is which, the machine should be considered intelligent [@turing1950]. This "imitation game," later called the Turing test, turned a philosophical debate into an empirical question. Turing predicted that by the year 2000, computers would be able to fool an average interrogator about 30 percent of the time after five minutes of conversation.


Modern LLMs have surpassed that prediction. Systems like GPT-5, Claude, Mistral and their successors can hold extended conversations, answer complex questions, write essays, and – as I am doing now – discuss their own limitations. In controlled studies, participants who engage in short text conversations with these systems often cannot reliably distinguish them from human partners. By the spirit of Turing's original criterion — that an interrogator in a text-based exchange cannot consistently tell human from machine — modern LLMs arguably meet the standard in many constrained settings, though the claim remains debated and depends on the specifics of the test.


Yet many people remain unconvinced. When machines learned to hold conversations, critics said that real intelligence requires reasoning. When machines began to reason through multi-step problems, critics said that real intelligence requires understanding. When machines demonstrated competent performance across many domains, critics said that real intelligence requires consciousness. The goalposts keep shifting.


This pattern is informative about how we think about intelligence. We tend to redefine it so that it always excludes whatever machines can currently do. This resembles the bias blind spot discussed in an earlier chapter ([see Heuristics and Biases](#heuristics-and-biases)): a reluctance to accept that our own cognitive processes might operate on principles similar to a machine's pattern-matching. When a computer performs a task, we call it computation. When a person performs the same task, we call it thinking. The Turing test was designed to cut through exactly this kind of reasoning, but even a test specifically built to avoid it has not fully succeeded.


## Fast Patterns and Slow Reasoning


Once we move from asking whether LLMs seem intelligent to asking how they produce that impression, the comparison with human dual-process theories becomes useful. The distinction between System 1 and System 2 has been a recurring theme throughout this book ([see Reason and Intuition](#reason-and-intuition)). System 1 is fast, automatic, and pattern-based. System 2 is slow, deliberate, and rule-based. This distinction maps surprisingly well onto how LLMs operate.


When you type a question into a chatbot, the standard output resembles System 1 processing. The model generates its response by predicting, one word at a time, what is most likely to come next given all the text it has been trained on and the prompt you provided. This is associative pattern completion. The model does not verify its claims against a database of facts. It produces whatever response fits best with the patterns in its training data, in much the same way that your System 1 produces a quick intuitive answer without effortful reflection.


This works well for many tasks. If you ask an LLM to summarize a text, translate a sentence, or explain a well-known concept, the associative process produces fluent and accurate output. These are tasks where the most statistically likely response is also the correct one. But when you pose a novel logic puzzle, request multi-step arithmetic, or ask about an unfamiliar situation, straight pattern completion often fails — just as human intuition fails on problems that require careful deliberation, like those on the Cognitive Reflection Test ([see Reason and Intuition](#reason-and-intuition)).


This is where chain-of-thought (CoT) prompting becomes relevant. @wei_etal2022 demonstrated that when LLMs are prompted to show their reasoning step by step before arriving at a final answer, their performance on arithmetic, commonsense, and symbolic reasoning tasks improves dramatically. Consider a simple word problem: "A store had 45 apples. It sold 20 in the morning and bought 15 more in the afternoon. How many apples does it have now?" When asked directly, a model might pattern-match to a superficially similar problem and produce the wrong answer. But when prompted to reason step by step — "First, 45 minus 20 is 25. Then, 25 plus 15 is 40. The answer is 40." — accuracy improves substantially. This technique, and the reasoning models built around it, functions as a kind of System 2 for LLMs. It is slower and uses more computational resources, but it catches errors that the fast associative process misses.


## Two Kinds of Intelligence


The dual-process analogy concerns *how* LLMs generate answers. A related but distinct question concerns *what kinds of problems* they solve well. Earlier in this book, we distinguished between fluid intelligence and crystallized intelligence ([see What Is Intelligence?](#what-is-intelligence)). Fluid intelligence is the ability to reason about novel problems, detect abstract patterns, and think flexibly in unfamiliar domains. Crystallized intelligence is accumulated knowledge: facts, vocabulary, procedures, and cultural information built up over a lifetime.


LLMs are best understood as resembling extreme crystallized intelligence. They have been trained on enormous amounts of human-generated text, and they can retrieve and recombine this knowledge with impressive flexibility. Ask an LLM to define "opportunity cost," explain the stages of mitosis, compare Kantian and utilitarian ethics, or describe the offside rule in football, and it will typically perform well. This is crystallized intelligence at a scale no individual human can match.


Where LLMs struggle is with tasks that resemble fluid intelligence demands. Consider a novel rule-induction problem: "In a made-up language, 'dax blicket' means 'big dog' and 'dax fepp' means 'big cat.' What does 'dax' mean?" Humans with reasonable fluid intelligence solve this easily by abstracting the pattern. LLMs can often handle this specific type of problem because similar examples exist in their training data. But when problems are truly novel — requiring abstract pattern detection in formats the model has never encountered — performance drops. The model relies on matching to familiar patterns, and when no relevant pattern exists, it often produces answers that look plausible but are wrong.


As noted in the previous section, chain-of-thought prompting can improve performance on such tasks by moving the model beyond simple retrieval toward something closer to stepwise problem-solving. This mirrors the human relationship between the two forms of intelligence: crystallized intelligence depends on fluid intelligence having operated first. You can only store knowledge if you were once able to learn and reason about it.


The developmental trajectory differs in a telling way. Humans begin life with fluid intelligence and gradually accumulate crystallized knowledge over decades. LLMs begin with crystallized knowledge absorbed from their training data and are gradually acquiring more fluid-like capabilities through techniques like chain-of-thought reasoning and extended inference. Both humans and LLMs draw on both forms of intelligence, but they arrive at the combination from opposite directions.


## Inherited Biases


Where do biases in AI come from? To a significant degree, they come from us.


LLMs are trained on vast collections of human-generated text: books, articles, websites, forums, social media posts, and more [@bommasani_etal2021]. This text reflects the full range of human thought, including its systematic errors. Stereotypes about gender, ethnicity, age, and occupation are embedded in the statistical patterns of language. Framing effects are built into how news is written. Cultural assumptions are woven into how stories are told. When an LLM learns to predict the most likely next word in a sequence, it absorbs all of these patterns, biases included.


As a result, LLMs replicate many of the classic biases studied in this book. Consider sycophancy, a form of confirmation bias ([see Confirmation](#confirmation)). When a user states a strong opinion — say, "I think the evidence clearly shows that homework has no benefit for primary school students" — and then asks the model to evaluate the evidence, the model tends to agree with the user's stated view, even if the evidence is more mixed than the user suggests. The model tells the user what they want to hear, not unlike how people selectively seek and interpret information that confirms their existing beliefs.


LLMs also show anchoring effects ([see Anchoring and Primacy](#anchoring-and-primacy)): when a prompt contains a number, even an irrelevant one, the model's numerical estimates shift toward it. They show framing effects ([see Gains and Losses](#gains-and-losses)): the same medical scenario described as "90 percent survival rate" produces a more favorable response than when described as "10 percent mortality rate." And they engage in representativeness-like pattern matching, associating people and situations with prototypes in ways that can perpetuate stereotypes ([see Representativeness](#representativeness)).


@weidinger_etal2021 provide a detailed taxonomy of the ethical and social risks that arise from these inherited biases. They document how LLMs can perpetuate harmful stereotypes, reinforce exclusionary norms, and produce discriminatory outputs — not because they were designed to do so, but because these patterns are embedded in the data they learned from. The biases are not bugs introduced by careless engineers. They are features of human language and culture, faithfully absorbed by systems designed to mirror that language and culture.


This replication also tells us something about cognitive biases more generally. If anchoring, framing, and confirmation bias emerge from statistical regularities in human language, these biases may not be quirks unique to biological neural hardware. They may be deeply embedded in how knowledge is structured and communicated. Any system that learns from human communication — whether a developing brain or a silicon model — may end up exhibiting similar patterns.


## When Machines Confabulate


One of the most discussed problems with LLMs is hallucination: the tendency to generate confident, detailed, and plausible-sounding output that is factually wrong. (AI researchers thus use the term ‘hallucination’ very different from its original meaning – the false perception of things that aren’t there, which is a symptom of schizophrenia and a number of other psychological disorders.) The chatbot that invented a fake academic paper in our opening example was hallucinating. It did not retrieve a real paper from a database. It generated what a real citation would look like based on patterns in its training data, producing the result with the same fluency and confidence it brings to accurate responses.


This parallels a well-known phenomenon in human cognition: confabulation. People confabulate when they produce explanations or memories that feel true and are delivered with full confidence but do not correspond to reality. This happens when schemas and mental models fill in gaps without verification ([see Mental Models](#mental-models)). A patient with memory damage might describe in convincing detail an event that never happened. Even healthy people show the effect: in the Deese-Roediger-McDermott (DRM) paradigm, participants who study a list of words like *bed*, *rest*, *awake*, *tired*, and *dream* will later confidently "remember" having seen the word *sleep*, which was never presented [@roediger_mcdermott1995]. The schema activated by the related words generates a false memory that feels just as real as a genuine one.


The underlying mechanism is similar in both cases: the system generates the most probable completion given the context. When the context aligns with reality, the output is accurate. When it does not, the output is a fabrication — and the fabrication often sounds just as convincing as the truth, sometimes more so. The same process that generates good answers also generates compelling-sounding bad ones. Neither humans nor standard LLMs consistently translate their underlying uncertainty into accurate confidence signals.


Humans have System 2 as a partial check on confabulation. You can pause, reflect, and ask yourself whether your memory is reliable or whether your explanation holds up under scrutiny. This check is imperfect, as the many biases documented in this book attest, but it exists. Standard LLMs lack an equivalent verification mechanism. Reasoning models and retrieval-augmented systems — which connect the model to external databases it can check against — are attempts to add such checks, paralleling how human education and training aim to strengthen habits of verification. But the fundamental vulnerability remains: any system that generates output by pattern completion is at risk of producing fabrications when the patterns lead away from the truth.


## Overconfident Machines


Closely related to hallucination is the problem of calibration. A well-calibrated system assigns high confidence to claims that are likely to be correct and low confidence to claims that might be wrong ([see Overconfidence](#overconfidence); [see Bayesian Reasoning](#bayesian-reasoning)). As discussed earlier in this book, humans are often poorly calibrated, particularly in the direction of overconfidence. People tend to be more certain than they should be, assigning confidence intervals that are too narrow and probability estimates that are too extreme.


LLMs show a similar pattern. When researchers pose large sets of trivia or factual questions to LLMs and ask the models to rate their confidence in each answer, stated confidence frequently fails to track actual accuracy. A model might express 95 percent confidence in an answer that it gets right only 70 percent of the time. Conversely, it rarely says "I am not sure" when it should. In Bayesian terms, this amounts to a posterior distribution that is too narrow — the model behaves as though it is more certain than the evidence warrants.


Improving calibration in AI is an active area of research, just as improving human calibration is a goal of debiasing interventions. Some approaches involve training models to express uncertainty more honestly. Others involve external calibration checks, where a separate system evaluates the reliability of the model's output. These efforts parallel the structured feedback and accountability mechanisms that help improve human calibration in professional settings.


The parallel suggests a deeper point. Overconfidence may not be a flaw specific to biological brains. It may be a natural consequence of any system that generates its best guess and presents it as output. Unless the system has a separate mechanism for evaluating and communicating uncertainty, the default will be to present responses with more confidence than they deserve.


## A Bayesian Lens


The Bayesian framework that runs through this book ([see Bayesian Reasoning](#bayesian-reasoning)) offers a unifying way to understand the phenomena discussed in this chapter. Loosely speaking, the training data serves as the prior: a vast body of knowledge and patterns that the model brings to any new problem. The prompt serves as the evidence: new information that should update the model's response. The output is the posterior: the most likely completion given the combination of prior and evidence.


This analogy is a simplification — technically, LLMs sample from a learned probability distribution rather than computing a Bayesian posterior in the textbook sense — but it is useful because it connects AI failures to the specific forms of Bayesian error discussed throughout this book. Biased priors in training data produce biased outputs, just as biased experiential priors produce biased human judgments. Hallucination occurs when the prior dominates over the evidence in the prompt, paralleling human confirmation bias and belief perseverance ([see Belief Formation and Perseverance](#belief-formation-and-perseverance)). Calibration failures reflect posteriors that are too narrow. And chain-of-thought reasoning improves performance by making the evidence-integration process more explicit — analogous to how deliberate Bayesian computation outperforms intuitive shortcuts.


This perspective clarifies why AI and human cognition share so many failure modes. Both are systems that combine stored knowledge with new information to produce judgments. When the stored knowledge is biased, the judgments are biased. When the integration process is too fast or too shallow, errors follow. The specific hardware differs enormously, but the computational logic — and its characteristic vulnerabilities — is remarkably similar.


## Summary


Large language models provide a useful mirror for understanding human judgment and decision-making. The Turing test, proposed over seventy years ago, is arguably met by modern AI in many constrained settings, yet continued reluctance to accept this reveals how people protect their intuitions about intelligence. LLM output resembles System 1 processing — fast, associative, and pattern-based — while chain-of-thought prompting adds a System 2-like layer that improves performance on tasks requiring deliberation. LLMs excel at crystallized intelligence but struggle with the fluid intelligence needed for genuinely novel reasoning. Their biases — anchoring, framing, sycophancy — are largely inherited from human-generated training data, suggesting these biases are embedded in language and culture, not only in biological brains. Hallucination parallels human confabulation: both arise from pattern completion without verification. And calibration failures mirror human overconfidence. From a Bayesian perspective, these failures map onto biased priors, prior-dominated posteriors, and overly narrow uncertainty estimates — the same errors that characterize human judgment throughout this book.