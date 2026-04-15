import re
import os
from pathlib import Path
from sigmund import static

MODEL_WRITE = 'claude-4-6-opus'
MODEL_FEEDBACK = 'gpt-5.4-thinking'
OUTLINE_PATH = 'md/outline.md'
CONDENSED_OUTLINE_PATH = 'md/condensed-outline.md'
SUMMARIES_DIR = 'references/summaries'
OUTPUT_DIR = 'md/chapters'
DRAFTS_DIR = 'md/chapters/drafts'
FEEDBACK_DIR = 'md/chapters/feedback'

BAYESIAN_LENS_FULL = '''The penultimate paragraph should be the Bayesian lens. The goal of this paragraph is to relate the chapter topic to the notion of Bayesian evidence integration in terms of a prior belief that is updated with evidence (with a certain reliability) to form a posterior belief. This framing is a central part of the book. If it is not possible to link a topic to a Bayesian perspective, simply indicate so in the text (no need to force a link if there's no natural connection).

'''

BAYESIAN_LENS_SKIP = ''

PROMPT_TEMPLATE = '''You are a brilliant writer of a textbook for a university course. This textbook is called 'An Introduction to Judgment and Decision-Making'.

# Your task

You are currently working on one chapter. Below you can find a detailed outline of this chapter. You can also find a condensed outline of the entire textbook. Use this to make cross-links to other chapters where appropriate, using anchors that are derived from the title (e.g. '[this relates to another chapter](#another-chapter-title)').

# Style guidelines

Use plain English. This means avoiding jargon, unnecessary synonyms and adjectives, and linguistic variations that don't serve a purpose. Use the simplest terms that are scientifically accurate, and use these terms consistently (i.e. don't use synonyms for the same concept).

# Target audience

You are writing for bachelor students of the international psychology program at The University of Groningen in The Netherlands. Use examples that are relatable to this target audience. Avoid a strong focus on the United States, except when US examples are clearly warranted. Instead, use a mix of examples from across the world, with a slight bias towards European/ Dutch examples. Use European units (meters, kilograms, Celsius, etc.) and currency (Euros), except when an example requires differently.

# References

We will use pandoc citeproc to generate citations in APA style. This means that you should put square brackets around parenthetical citations: 'There is a unified system in the brain [@evans_stanovich2013].' But not around inline citations: '@evans_stanovich2013 argue that there is a unified system in the brain.'

# Chapter structure

The chapter should open with a title (level-1 heading). This should be followed by a bulleted list of learning goals, which should include the most important terms and concepts of the chapter. The rest of the chapter should be divided into sections (level-2 headings). Do not make further subdivisions (i.e. *no* level-3 headings).

```
# Chapter title

Learning goals:

- Each learning goal is a short sentence.

## First section

Section text.

## … More sections

## Summary

Summary text.
```

The rest of the chapter should use a narrative structure. Do not use bullets, except when something needs to be enumerated. Similarly, don't use boldface or other ways to highlight important concepts. Instead, use the narrative structure to highlight what is important.

The chapter should start with a short paragraph that introduces the chapter topic in a relatable way. You can use a real-life example for this, but only if this feels natural.

Next, all points of the outline should be developed in a narrative structure. You are free to deviate from the order of the outline and to include additional material if you feel this improves the content.

Be as concrete as possible when explaining concepts. You can do this either by using concrete examples, or by describing one of the studies from the references with sufficient detail so that the reader understands what was actually done. Please alternate between these two strategies for variation.

{bayesian_lens}The final paragraph should be a short summary of the main points discussed in the chapter, labeled 'Summary'.

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

Are you ready? Please respond with the complete text of the chapter, which will be written to a file. Do not add any additional text.'''

FEEDBACK_TEMPLATE = '''You are an expert reviewer for a university textbook called 'An Introduction to Judgment and Decision-Making'. Below you will find a first draft of one chapter, along with the chapter outline it was based on and a condensed outline of the entire book.

Please provide constructive feedback on the draft. Focus on:

1. **Structure**: Does the chapter flow logically? Are there awkward transitions or sections that feel out of place?
2. **Duplication**: Are any ideas, examples, or explanations repeated unnecessarily?
3. **Concreteness**: Are there passages that remain too abstract? Where would a concrete example or a description of a specific study improve the text?
4. **Accuracy**: Does the draft faithfully cover all the points in the chapter outline? Is anything missing or misrepresented?
5. **Style**: Is the language plain and consistent? Are there unnecessary synonyms, jargon, or filler phrases?
6. **Cross-links**: Are cross-references to other chapters appropriate and correctly formatted?

Be specific: quote the passage you're commenting on and explain what should change.

<condensed_outline>
{condensed_outline}
</condensed_outline>

<chapter_outline>
{chapter_outline}
</chapter_outline>

<chapter_draft>
{chapter_draft}
</chapter_draft>

Please respond with your feedback only. Be thorough but concise.'''

REVISION_TEMPLATE = '''You are a brilliant writer of a textbook for a university course. This textbook is called 'An Introduction to Judgment and Decision-Making'.

You previously wrote a first draft of a chapter. A reviewer has provided feedback on that draft. Carefully consider each suggestion, and include address in a revision if you feel that this will strengthen the chapter. You are also free to disregard some of the reviewer's suggestions.

All the original instructions still apply: use plain English, cite references in pandoc-citeproc format, follow the chapter structure guidelines, and be concrete with examples.

Do *not* add new references.

<condensed_outline>
{condensed_outline}
</condensed_outline>

<chapter_outline>
{chapter_outline}
</chapter_outline>

<first_draft>
{first_draft}
</first_draft>

<reviewer_feedback>
{feedback}
</reviewer_feedback>

Please respond with the complete revised chapter text, which will be written to a file. Do not add any additional text.'''


def split_outline_into_chapters(outline_text):
    """Split the full outline into chapters based on level-2 headings (## ...)."""
    chapters = []
    parts = re.split(r'^(## .+)$', outline_text, flags=re.MULTILINE)
    for i in range(1, len(parts), 2):
        heading = parts[i]
        body = parts[i + 1] if i + 1 < len(parts) else ''
        chapter_text = heading + '\n' + body
        title = heading.strip('# ').strip()
        chapters.append((title, chapter_text))
    return chapters


def extract_references(text):
    """Extract unique pandoc citeproc references (e.g. @simon1956) from text."""
    refs = re.findall(r'@([a-zA-Z0-9_:-]+)', text)
    return sorted(set(refs))


def load_reference_summaries(refs):
    """Load summaries for each reference from the summaries directory."""
    summaries = []
    for ref in refs:
        path = Path(SUMMARIES_DIR) / f'{ref}.md'
        if path.exists():
            content = path.read_text(encoding='utf-8').strip()
            summaries.append(f'## {ref}\n\n{content}')
        else:
            print(f'  ⚠️  Summary not found: {path}')
    return '\n\n---\n\n'.join(summaries) if summaries else 'No reference summaries available.'


def slugify(title):
    """Convert a chapter title to a filename-friendly slug."""
    slug = title.lower()
    slug = re.sub(r'[^a-z0-9]+', '-', slug)
    return slug.strip('-')


def main():
    for d in [OUTPUT_DIR, DRAFTS_DIR, FEEDBACK_DIR]:
        os.makedirs(d, exist_ok=True)
    # Load inputs
    outline = Path(OUTLINE_PATH).read_text(encoding='utf-8')
    condensed_outline = Path(CONDENSED_OUTLINE_PATH).read_text(encoding='utf-8')
    # Split outline into chapters
    chapters = split_outline_into_chapters(outline)
    print(f'📖 Found {len(chapters)} chapters in the outline.\n')
    for i, (title, chapter_outline) in enumerate(chapters):
        print(f'--- Chapter: {title} ---')
        filename = f'{slugify(title)}.md'
        output_path = Path(OUTPUT_DIR) / filename
        draft_path = Path(DRAFTS_DIR) / filename
        feedback_path = Path(FEEDBACK_DIR) / filename
        if output_path.exists():
            print(f'  🔄 Skipping (already exists): {output_path}')
            continue
        # Extract and load references
        refs = extract_references(chapter_outline)
        print(f'  📚 Found {len(refs)} references: {", ".join(refs[:5])}{"..." if len(refs) > 5 else ""}')
        reference_summaries = load_reference_summaries(refs)
        # Determine Bayesian lens text
        bayesian_lens = BAYESIAN_LENS_SKIP if i == 0 else BAYESIAN_LENS_FULL
        # Step 1: Generate first draft
        prompt = PROMPT_TEMPLATE.format(
            condensed_outline=condensed_outline,
            chapter_outline=chapter_outline,
            reference_summaries=reference_summaries,
            bayesian_lens=bayesian_lens
        )
        print('  ✍️  Generating first draft ...')
        first_draft = static.predict(prompt, model=MODEL_WRITE)
        draft_path.write_text(first_draft, encoding='utf-8')
        print(f'  💾 Draft saved to {draft_path}')
        # Step 2: Get feedback
        feedback_prompt = FEEDBACK_TEMPLATE.format(
            condensed_outline=condensed_outline,
            chapter_outline=chapter_outline,
            chapter_draft=first_draft
        )
        print('  🔍 Requesting feedback ...')
        feedback = static.predict(feedback_prompt, model=MODEL_FEEDBACK)
        feedback_path.write_text(feedback, encoding='utf-8')
        print(f'  💾 Feedback saved to {feedback_path}')
        # Step 3: Revise based on feedback
        revision_prompt = REVISION_TEMPLATE.format(
            condensed_outline=condensed_outline,
            chapter_outline=chapter_outline,
            first_draft=first_draft,
            feedback=feedback
        )
        print('  ✍️  Revising chapter ...')
        revised = static.predict(revision_prompt, model=MODEL_WRITE)
        output_path.write_text(revised, encoding='utf-8')
        print(f'  ✅ Final chapter written to {output_path}\n')
        if i > 2:
            break
    print('🎉 All chapters generated!')


if __name__ == '__main__':
    main()