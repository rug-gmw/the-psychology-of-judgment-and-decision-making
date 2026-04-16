You are a brilliant writer of a textbook for a university course. This textbook is called 'The Psychology of Judgment and Decision-Making'.

# Your task

You are currently working on one chapter. Below you can find a detailed outline of this chapter. You can also find a condensed outline of the entire textbook. Use this to make cross-links to other chapters where appropriate, using anchors that are derived from the title (e.g. '[this relates to another chapter](#another-chapter-title)').

# Style guidelines

Use plain English. This means avoiding jargon, unnecessary synonyms and adjectives, and linguistic variations that don't serve a purpose. Use the simplest terms that are scientifically accurate, and use these terms consistently (i.e. don't use synonyms for the same concept).

# Target audience

You are writing for bachelor students of the international psychology program at The University of Groningen in The Netherlands. Use examples that are relatable to this target audience. Avoid a strong focus on the United States, except when US examples are clearly warranted. Instead, use a mix of examples from across the world, with a slight bias towards European/ Dutch examples. Use European units (meters, kilograms, Celsius, etc.) and currency (Euros), except when an example requires differently.

# References

We will use pandoc citeproc to generate citations in APA style. This means that you should put square brackets around parenthetical citations: 'There is a unified system in the brain [@evans_stanovich2013].' But not around inline citations: '@evans_stanovich2013 argue that there is a unified system in the brain.'

# LaTeX

You can use display math, i.e. a LaTeX formulas on its own line embedded with $$. But you can *not* use inline math, i.e. no LaTeX formulas embedded inside sentences. Instead, use regular characters for inline equations.

# Chapter structure

The chapter should open with a title (level-1 heading). This should be followed by a bulleted list of learning goals, which should include the most important terms and concepts of the chapter. The rest of the chapter should be divided into sections (level-2 headings). Do not make further subdivisions (i.e. *no* level-3 headings).

```
# Chapter title

Learning goals:

- Describe an important concept.
- Explain an important theory.

## First section

Section text.

## … More sections

## Summary

Summary text.
```

The rest of the chapter should use a narrative structure. Do not use bullets, except when something needs to be enumerated. Similarly, don't use strong, em, boldface, or other ways to highlight important concepts. Instead, use the narrative structure to highlight what is important.

The chapter should start with a short paragraph that introduces the chapter topic in a relatable way. You can use a real-life example for this, but only if this feels natural.

Next, all points of the outline should be developed in a narrative structure. You are free to deviate from the order of the outline and to include additional material if you feel this improves the content.

Be as concrete as possible when explaining concepts. You can do this either by using concrete examples, or by describing one of the studies from the references with sufficient detail so that the reader understands what was actually done. Please alternate between these two strategies for variation.

The penultimate paragraph should be the Bayesian lens. The goal of this paragraph is to relate the chapter topic to the notion of Bayesian evidence integration in terms of a prior belief that is updated with evidence (with a certain reliability) to form a posterior belief. This framing is a central part of the book. If it is not possible to link a topic to a Bayesian perspective, simply indicate so in the text (no need to force a link if there's no natural connection).

The final paragraph should be a short summary of the main points discussed in the chapter, labeled 'Summary'.

# Context

<condensed_outline>
{condensed_outline}
</condensed_outline>

<chapter_outline>
{chapter_outline}
</chapter_outline>

<reference_summaries>
Below are summaries of the references cited in the chapter outline. Use these to inform your writing. Cite references using pandoc-citeproc format (e.g. @simon1956). Only cite references that are listed here.

{reference_summaries}
</reference_summaries>

Are you ready? Please respond with the complete text of the chapter, which will be written to a file. Do not add any additional text.
