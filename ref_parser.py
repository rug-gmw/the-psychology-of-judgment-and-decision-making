#!/usr/bin/env python3
"""
ref_manager.py – Manage references for a book project.

Usage
-----
  python ref_manager.py check               # open doi.org for missing PDFs
  python ref_manager.py check --scihub      # open Sci-Hub instead
  python ref_manager.py ocr                 # convert PDFs → Markdown
  python ref_manager.py ocr --force         # re-run OCR even if Markdown exists
  python ref_manager.py summarize           # summarize Markdown files
  python ref_manager.py summarize --force   # re-summarize even if summary exists

Global options
--------------
  --bib PATH   Path to the .bib file (default: references.bib)
"""
import os
import argparse
import base64
import time
import webbrowser
from pathlib import Path
import bibtexparser
from mistralai.client import Mistral
from sigmund import static

# ── Configuration ─────────────────────────────────────────────────────────────

BIB_PATH      = 'references/references.bib'
PDF_DIR       = Path('references/pdf')
MD_DIR        = Path('references/md')
SUMM_DIR      = Path('references/summaries')
MISTRAL_MODEL = 'mistral-large-latest'
MISTRAL_API_KEY = os.environ.get('MISTRAL_API_KEY')

SUMMARIZE_PROMPT = '''\
Can you summarize the article for me? Please use the following format:

<summary_template>
# Article Title

Author1, F., Author2, F.

__A very brief summary of at most three sentences. Should convey the article\'s core message.__

A comprehensive summary. Use a narrative structure, not bulleted lists. Cover all important \
aspects of the introduction, methods, results, and discussion (for empirical articles); \
or the theory (for theoretical articles).
</summary_template>

Here is the article:

<article>
{content}
</article>

Please reply only with your summary following the summary_template above \
(do not include the <summary_template> tags themselves).'''


# ── Shared helpers ─────────────────────────────────────────────────────────────

def load_bib(bib_path):
    with open(bib_path) as f:
        return bibtexparser.load(f)


def ocr_pdf(pdf_bytes):
    """Run Mistral OCR on raw PDF bytes and return Markdown text."""
    b64 = base64.b64encode(pdf_bytes).decode('utf-8')
    client = Mistral(api_key=MISTRAL_API_KEY)
    response = client.ocr.process(
        model='mistral-ocr-latest',
        document={
            'type': 'document_url',
            'document_url': f'data:application/pdf;base64,{b64}',
        },
        include_image_base64=False,
    )
    return '\n\n'.join(page.markdown for page in response.pages)


# ── check ──────────────────────────────────────────────────────────────────────

def cmd_check(args):
    """Check for missing PDFs and open their DOIs in the browser."""
    bib_db = load_bib(args.bib)
    has_pdf, no_pdf, no_doi = [], [], []

    for entry in bib_db.entries:
        key = entry['ID']
        if (PDF_DIR / f'{key}.pdf').exists():
            has_pdf.append(key)
            continue

        doi = entry.get('doi', '').strip()
        if not doi:
            print(f'⚠️  No DOI: {key}')
            no_doi.append(key)
            continue

        url = doi if doi.startswith('http') else f'https://doi.org/{doi}'
        if args.scihub:
            url = url.replace('https://doi.org/', 'https://sci-hub.st/')
        print(f'🌐 Opening: {key} → {url}')
        webbrowser.open(url)
        time.sleep(0.3)
        no_pdf.append(key)
        input('   Press Enter to continue...')

    print(f'\n✅ Already have PDF : {len(has_pdf)}')
    print(f'🌐 Opened in browser: {len(no_pdf)}')
    print(f'⚠️  No DOI found     : {len(no_doi)}')
    if no_doi:
        print('\nEntries without a DOI:')
        for k in no_doi:
            print(f'  - {k}')


# ── ocr ────────────────────────────────────────────────────────────────────────

def cmd_ocr(args):
    """Convert PDFs to Markdown using Mistral OCR."""
    MD_DIR.mkdir(parents=True, exist_ok=True)
    bib_db = load_bib(args.bib)

    for entry in bib_db.entries:
        key = entry['ID']
        pdf_path = PDF_DIR / f'{key}.pdf'
        md_path  = MD_DIR  / f'{key}.md'

        if not pdf_path.exists():
            print(f'[{key}] No PDF — skipping')
            continue
        if md_path.exists() and not args.force:
            print(f'[{key}] Markdown already exists — skipping (use --force to redo)')
            continue

        print(f'[{key}] Running OCR...')
        try:
            md_path.write_text(ocr_pdf(pdf_path.read_bytes()))
            print(f'  ✓ Saved → {md_path}')
        except Exception as e:
            print(f'  ✗ OCR failed: {e}')


# ── summarize ──────────────────────────────────────────────────────────────────

def cmd_summarize(args):
    """Summarize Markdown files using Mistral."""
    SUMM_DIR.mkdir(parents=True, exist_ok=True)

    for md_path in sorted(MD_DIR.glob('*.md')):
        summ_path = SUMM_DIR / md_path.name
        if summ_path.exists() and not args.force:
            print(f'[{md_path.stem}] Summary already exists — skipping (use --force to redo)')
            continue

        print(f'[{md_path.stem}] Summarizing...')
        try:
            summary = static.predict(
                SUMMARIZE_PROMPT.format(content=md_path.read_text()),
                MISTRAL_MODEL,
            )
            summ_path.write_text(summary)
            print(f'  ✓ Saved → {summ_path}')
        except Exception as e:
            print(f'  ✗ Failed: {e}')


# ── Entry point ────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(
        prog='ref_manager.py',
        description='Manage references for a book project.',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    parser.add_argument('--bib', default=BIB_PATH, metavar='PATH',
                        help=f'Path to the .bib file (default: {BIB_PATH})')

    sub = parser.add_subparsers(dest='command', required=True)

    # check
    p_check = sub.add_parser('check', help='Check for missing PDFs and open their DOIs')
    p_check.add_argument('--scihub', action='store_true',
                         help='Open Sci-Hub instead of doi.org')
    p_check.set_defaults(func=cmd_check)

    # ocr
    p_ocr = sub.add_parser('ocr', help='Convert PDFs to Markdown via Mistral OCR')
    p_ocr.add_argument('--force', action='store_true',
                       help='Re-run OCR even if Markdown already exists')
    p_ocr.set_defaults(func=cmd_ocr)

    # summarize
    p_summ = sub.add_parser('summarize', help='Summarize Markdown files via Mistral')
    p_summ.add_argument('--force', action='store_true',
                        help='Re-summarize even if a summary already exists')
    p_summ.set_defaults(func=cmd_summarize)

    args = parser.parse_args()
    args.func(args)


if __name__ == '__main__':
    main()