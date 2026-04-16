import re
import os
from pathlib import Path
from sigmund import static

MODEL_WRITE = 'claude-4-6-opus'
MODEL_FEEDBACK = 'gpt-5.4-thinking'
OUTLINE_PATH = 'input/md/outline.md'
CONDENSED_OUTLINE_PATH = 'input/md/condensed-outline.md'
SUMMARIES_DIR = 'references/summaries'
OUTPUT_DIR = 'input/md/chapters'
DRAFTS_DIR = 'input/md/chapters/drafts'
FEEDBACK_DIR = 'input/md/chapters/feedback'
PROMPT_TEMPLATE = Path('prompts/write.md').read_text()
FEEDBACK_TEMPLATE = Path('prompts/feedback.md').read_text()
REVISION_TEMPLATE = Path('prompts/revise.md').read_text()


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
        # Step 1: Generate first draft
        prompt = PROMPT_TEMPLATE.format(
            condensed_outline=condensed_outline,
            chapter_outline=chapter_outline,
            reference_summaries=reference_summaries
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
    print('🎉 All chapters generated!')


if __name__ == '__main__':
    main()