import subprocess
from pathlib import Path
import re
import pypandoc
import yaml
from pypdf import PdfReader, PdfWriter
from weasyprint import HTML, CSS

# ---- Inputs (adjust as needed) ------------------------------------------------
HTML_TEMPLATE = "styles/template.html"

# With Pandoc -> standalone HTML, --css adds <link> tags to the HTML.
HTML_STYLESHEETS = ["styles/base.css"]

# Optional: add extra CSS at PDF-render time (in addition to <link> tags in HTML)
WEASY_EXTRA_CSS = ["styles/print.css"]
# WEASY_EXTRA_CSS = ["styles/print-a5.css"]

# Optional: pdfs that should be added before and after the main content.
# If an entry is None, a blank page will be inserted at that position.
PREFIX_PDF = [
    "input/pdf/blank.pdf",
    "input/pdf/title-page.pdf",
    "input/pdf/colofon.pdf",
    "input/pdf/blank.pdf",
    "input/pdf/blank.pdf",
]
SUFFIX_PDF: list[str | None] = []

# Bundle descriptor (YAML containing metadata + contents list)
BUNDLE_INFO = "input/yaml/intro-jdm.yaml"

# Output root (all final outputs go here)
OUTPUT_DIR = Path("output")

# Make first letter of each chapter large
DROP_CAPS = False

# Bibtext refs
REFERENCES = Path("references/references.bib")


def preprocess_md(md: str) -> str:
    # Ensure dialogue dashes are separated so they get their own paragraph.
    md = md.replace("\n— ", "\n\n—&thinsp;")

    # Wrap the first letter after a newline in a <span class="big-letter"> tag.
    if DROP_CAPS:
        md = re.sub(r'\n([A-Za-z])', r'\n<span class="big-letter">\1</span>',
                    md, count=1)

    def process_block(match):
        block = match.group(1)
        # Split into lines and strip empty lines from start/end
        lines = block.splitlines()
        # Remove empty lines from start
        while lines and not lines[0].strip():
            lines.pop(0)
        # Remove empty lines from end
        while lines and not lines[-1].strip():
            lines.pop()
        # Rejoin with newlines
        return '\n'.join(['```'] + lines + ['```'])

    # Regex to match fenced code blocks (```content```)
    pattern = re.compile(r'```(.*?)```', re.DOTALL)
    return pattern.sub(process_block, md)


def preprocess_html(html: str) -> str:
    # Replace leading em dash in paragraphs / after <br> with a styled span.
    html = html.replace('<p>—', '<p><span class="quote-dash">&#x2015;</span>')
    html = html.replace("<br />\n—", '<br />\n<span class="quote-dash">&#x2015;</span>')
    return html


# ---- Bundle YAML --------------------------------------------------------------


def load_bundle_info(yaml_path: Path) -> dict:
    """
    Load bundle YAML.

    Expected keys (example):
      title, author, language, identifier, publisher, date, rights, subject,
      description, cover_image, css, contents

    Only 'contents' is required for building; others are used for EPUB metadata.
    """
    data = yaml.safe_load(Path(yaml_path).read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError(f"Bundle YAML must be a mapping/dict: {yaml_path}")
    return data


def bundle_titles(bundle: dict, yaml_path: Path) -> list[str]:
    """
    Get story basenames from bundle YAML.

    Supports:
      contents: [ ... ]   (preferred)
      titles:   [ ... ]
      stories:  [ ... ]
    """
    titles = None
    for key in ("contents", "titles", "stories"):
        if key in bundle:
            titles = bundle[key]
            break

    if not isinstance(titles, list) or not all(isinstance(t, str) and t.strip() for t in titles):
        raise ValueError(
            f"Could not parse story list from {yaml_path}.\n"
            f"Expected a list under one of: contents/titles/stories."
        )
    return [t.strip() for t in titles if Path(f"input/md/{t}.md").exists()]


def _pandoc_metadata_block(bundle: dict, *, fallback_title: str) -> str:
    """
    Create a Pandoc YAML metadata block (--- ... ---) for EPUB.

    Keep keys conservative so they map well to EPUB2 OPF fields.
    """
    meta: dict = {}

    title = bundle.get("title") or fallback_title
    if title:
        meta["title"] = title

    # Pandoc accepts 'author' as string or list
    author = bundle.get("author")
    if author:
        meta["author"] = author

    lang = bundle.get("language") or bundle.get("lang")
    if lang:
        meta["lang"] = lang

    identifier = bundle.get("identifier")
    if identifier:
        meta["identifier"] = identifier

    publisher = bundle.get("publisher")
    if publisher:
        meta["publisher"] = publisher

    date = bundle.get("date")
    if date:
        meta["date"] = date

    rights = bundle.get("rights")
    if rights:
        meta["rights"] = rights

    subject = bundle.get("subject")
    if subject:
        meta["subject"] = subject

    description = bundle.get("description")
    if description:
        meta["description"] = description

    # Dump as YAML and wrap in Pandoc metadata fences
    yaml_text = yaml.safe_dump(meta, sort_keys=False, allow_unicode=True).strip()
    return f"---\n{yaml_text}\n---\n\n"


# ---- HTML/PDF per-title -------------------------------------------------------


def md_to_html(title: str) -> Path:
    """
    Use Pandoc to build a standalone HTML with stylesheet(s) and template.

    Incorporates Markdown and HTML preprocessors.
    """
    src = Path(f"input/md/{title}.md")
    dst = OUTPUT_DIR / f"html/{title}.html"
    dst.parent.mkdir(parents=True, exist_ok=True)

    md_text = preprocess_md(src.read_text(encoding="utf-8"))

    extra_args: list[str] = [
        "--standalone", "--template", HTML_TEMPLATE,
        "--citeproc",
        "--bibliography", str(REFERENCES),
        "--csl", "/home/sebastiaan/snap/zotero-snap/common/Zotero/styles/apa.csl"
    ]
    for css in HTML_STYLESHEETS:
        extra_args += ["--css", css]

    # Convert from in-memory markdown so preprocessing takes effect.
    html = pypandoc.convert_text(
        md_text,
        to="html",
        format="md",
        extra_args=extra_args,
    )

    html = preprocess_html(html)
    dst.write_text(html, encoding="utf-8")

    return dst


def html_to_pdf_weasyprint(html_path: Path, *, out_pdf: Path, base_url: str | None = None) -> Path:
    """
    Render HTML -> PDF using WeasyPrint's Python API (no CLI calls).
    """
    out_pdf.parent.mkdir(parents=True, exist_ok=True)

    if base_url is None:
        base_url = str(Path(".").resolve())

    stylesheets = [CSS(filename=css) for css in WEASY_EXTRA_CSS]
    doc = HTML(filename=str(html_path), base_url=base_url).render(stylesheets=stylesheets)
    doc.write_pdf(str(out_pdf))
    return out_pdf


# ---- TOC generation -----------------------------------------------------------


def _insert_toc(html: str) -> str:
    """
    Parse all <h1 id="...">...</h1> from *html*, build a "Contents" section
    with anchor links, and inject it right after the opening <body> tag.

    Only level-1 headings are included.
    """
    h1_pattern = re.compile(r'<h1[^>]*\bid="([^"]*)"[^>]*>(.*?)</h1>', re.DOTALL)
    headings: list[tuple[str, str]] = []
    for match in h1_pattern.finditer(html):
        heading_id = match.group(1)
        # Strip any inner HTML tags to get plain text
        heading_text = re.sub(r'<[^>]+>', '', match.group(2)).strip()
        headings.append((heading_id, heading_text))

    if not headings:
        return html

    toc_lines = [
        '\n\n<div class=\"bundle-break\"></div>\n\n',
        '<section class="toc">',
        '<h1>Contents</h1>',
        '<ul>',
    ]
    for heading_id, heading_text in headings:
        toc_lines.append(
            f'  <li><a href="#{heading_id}">{heading_text}</a></li>'
        )
    toc_lines += ['</ul>', '</section>']
    toc_html = '\n'.join(toc_lines)

    # Insert right after the opening <body ...> tag
    lower = html.lower()
    body_start = lower.find("<body")
    if body_start == -1:
        return html
    body_tag_end = html.find(">", body_start)
    if body_tag_end == -1:
        return html
    return html[: body_tag_end + 1] + "\n" + toc_html + "\n" + html[body_tag_end + 1 :]


# ---- PDF merge helpers --------------------------------------------------------


def _merge_pdfs(pdf_paths: list[Path], out_path: str | Path) -> Path:
    """
    Merge PDFs in the given order into out_path (pure pypdf).

    Uses PdfReader + PdfWriter for compatibility across pypdf versions.
    """
    out_path = Path(out_path)
    out_path.parent.mkdir(parents=True, exist_ok=True)

    writer = PdfWriter()
    for p in pdf_paths:
        if not p.exists():
            raise FileNotFoundError(p)

        reader = PdfReader(str(p))
        for page in reader.pages:
            writer.add_page(page)

    with out_path.open("wb") as f:
        writer.write(f)

    return out_path


def _apply_prefix_suffix(main_pdf: Path, *, final_pdf: Path) -> Path:
    """
    Merge PREFIX_PDF + main_pdf + SUFFIX_PDF into final_pdf and return final_pdf.

    If PREFIX_PDF/SUFFIX_PDF are empty, this is just a rename/copy into final_pdf.
    If an entry is None, inserts a single blank page at that position.
    """
    blank_pdf = next(
        (Path(p) for p in (PREFIX_PDF + SUFFIX_PDF) if isinstance(p, str) and "blank" in p.lower()),
        None,
    )
    if blank_pdf is None:
        blank_pdf = Path("input/pdf/blank.pdf")

    def normalize(items: list[str | None]) -> list[Path]:
        out: list[Path] = []
        for item in items:
            if item is None:
                out.append(blank_pdf)
            else:
                out.append(Path(item))
        return out

    prefix = normalize(PREFIX_PDF)
    suffix = normalize(SUFFIX_PDF)

    final_pdf.parent.mkdir(parents=True, exist_ok=True)

    if not prefix and not suffix:
        # No merge needed; just move into place if possible.
        if main_pdf.resolve() == final_pdf.resolve():
            return final_pdf
        final_pdf.write_bytes(main_pdf.read_bytes())
        return final_pdf

    merge_list: list[Path] = []
    merge_list.extend(prefix)
    merge_list.append(main_pdf)
    merge_list.extend(suffix)
    return _merge_pdfs(merge_list, final_pdf)


# ---- Bundle PDF ---------------------------------------------------------------


def build_bundle_pdf(yaml_path: Path) -> Path:
    """
    Build a single booklet PDF from the bundle YAML file.

    All chapter markdown is concatenated first, then converted to HTML in a
    single Pandoc call (with --citeproc) so that references appear once at the
    very end.  A table of contents (level-1 headings) is injected into the
    HTML before rendering.

    Final output is: output/<bundle-stem>.pdf
    """
    yaml_path = Path(yaml_path)
    bundle = load_bundle_info(yaml_path)
    titles = bundle_titles(bundle, yaml_path)
    if not titles:
        raise ValueError(f"No titles in {yaml_path}")

    # ---- 1. Concatenate all preprocessed markdown into one document ----------
    combined_parts: list[str] = []
    for title in titles:
        src = Path(f"input/md/{title}.md")
        md_text = preprocess_md(src.read_text(encoding="utf-8")).strip()
        # Ensure every chapter starts with an H1 (needed for TOC & page breaks)
        if not md_text.lstrip().startswith("#"):
            md_text = f"# {title}\n\n{md_text}"
        combined_parts.append(md_text)

    # Append a References section; the ::: {#refs} ::: div tells citeproc to
    # place all collected references at this location.
    combined_parts.append("# References\n\n<section id='references'>\n:::{#refs}\n:::\n</section>")

    # Separate chapters with a page-break div (raw HTML passes through Pandoc)
    combined_md = '\n\n<div class=\"bundle-break\"></div>\n\n' + "\n\n<div class=\"bundle-break\"></div>\n\n".join(combined_parts)

    # ---- 2. Single Pandoc call → one HTML with one reference list -----------
    bundle_html_path = OUTPUT_DIR / f"{yaml_path.stem}.html"
    bundle_html_path.parent.mkdir(parents=True, exist_ok=True)

    extra_args: list[str] = [
        "--standalone", "--template", HTML_TEMPLATE,
        "--citeproc",
        "--bibliography", str(REFERENCES),
        "--csl", "/home/sebastiaan/snap/zotero-snap/common/Zotero/styles/apa.csl"        
    ]
    for css in HTML_STYLESHEETS:
        extra_args += ["--css", css]

    html = pypandoc.convert_text(
        combined_md,
        to="html",
        format="md",
        extra_args=extra_args,
    )
    html = preprocess_html(html)

    # ---- 3. Inject a table of contents (H1 headings only) -------------------
    html = _insert_toc(html)

    bundle_html_path.write_text(html, encoding="utf-8")

    # ---- 4. Render PDF with WeasyPrint & merge prefix/suffix pages ----------
    tmp_main_pdf = OUTPUT_DIR / f"{yaml_path.stem}.unmerged.pdf"
    base_url = str(Path(".").resolve())
    html_to_pdf_weasyprint(bundle_html_path, out_pdf=tmp_main_pdf, base_url=base_url)

    final_pdf = OUTPUT_DIR / f"{yaml_path.stem}.pdf"
    merged_pdf = _apply_prefix_suffix(tmp_main_pdf, final_pdf=final_pdf)

    try:
        tmp_main_pdf.unlink(missing_ok=True)
    except TypeError:
        if tmp_main_pdf.exists():
            tmp_main_pdf.unlink()

    return merged_pdf


# ---- EPUB (bundle) ------------------------------------------------------------


def _run_epubcheck(epub_path: Path) -> None:
    """
    Run epubcheck on the generated epub.

    Requires 'epubcheck' to be available on PATH.
    """
    cmd = ["epubcheck", str(epub_path)]
    proc = subprocess.run(cmd, capture_output=True, text=True)
    if proc.returncode != 0:
        raise RuntimeError(
            "epubcheck failed.\n\n"
            f"Command: {' '.join(cmd)}\n\n"
            f"STDOUT:\n{proc.stdout}\n\n"
            f"STDERR:\n{proc.stderr}\n"
        )


def build_bundle_epub(yaml_path: Path) -> Path:
    """
    Build a single EPUB2 for all stories listed in yaml_path.

    Bundle YAML provides:
    - metadata (title/author/language/identifier/...)
    - cover_image path
    - css list
    - contents list

    Output:
    - EPUB2 because some vendors don't support EPUB3 yet
    - TOC includes only H1 headings: --toc-depth=1
    - Runs epubcheck after generating

    Final output is: output/<bundle-stem>.epub
    """
    yaml_path = Path(yaml_path)
    bundle = load_bundle_info(yaml_path)
    titles = bundle_titles(bundle, yaml_path)
    if not titles:
        raise ValueError(f"No titles in {yaml_path}")

    out_epub = OUTPUT_DIR / f"{yaml_path.stem}.epub"
    out_epub.parent.mkdir(parents=True, exist_ok=True)

    # Build Pandoc metadata block (so epubcheck sees a title, etc.)
    metadata_block = _pandoc_metadata_block(bundle, fallback_title=yaml_path.stem)

    # Concatenate the (preprocessed) markdown sources into one stream.
    combined_parts: list[str] = [metadata_block]
    for title in titles:
        src = Path(f"input/md/{title}.md")
        md_text = preprocess_md(src.read_text(encoding="utf-8")).strip()

        # Ensure each story starts with an H1 (Pandoc will put these in the TOC).
        if not md_text.lstrip().startswith("#"):
            combined_parts.append(f"# {title}\n\n{md_text}\n")
        else:
            combined_parts.append(md_text + "\n")

    combined_md = "\n\n".join(combined_parts).strip() + "\n"

    extra_args: list[str] = [
        "--to=epub2",
        "--toc",
        "--toc-depth=1",
        '--citeproc',
        '--bibliography', str(REFERENCES)
    ]

    # Cover (bundle YAML overrides global)
    cover = bundle.get("cover_image")
    if cover:
        cover_path = Path(cover)
        if not cover_path.exists():
            raise FileNotFoundError(cover_path)
        extra_args += ["--epub-cover-image", str(cover_path)]

    # CSS (bundle YAML overrides global)
    css_list = bundle.get("css")
    if css_list is None:
        css_list = []
    if not isinstance(css_list, list):
        raise ValueError("Bundle YAML 'css' must be a list of paths.")
    for css in css_list:
        css_path = Path(css)
        if not css_path.exists():
            raise FileNotFoundError(css_path)
        extra_args += ["--css", str(css_path)]

    # Convert to EPUB2 from in-memory markdown so preprocessing takes effect.
    pypandoc.convert_text(
        combined_md,
        to="epub",
        format="md",
        outputfile=str(out_epub),
        extra_args=extra_args,
    )

    _run_epubcheck(out_epub)
    return out_epub


# ---- Main (no CLI) ------------------------------------------------------------


def main() -> None:
    bundle_yaml = Path(BUNDLE_INFO)

    pdf_path = build_bundle_pdf(bundle_yaml)
    print(f"Built PDF:  {pdf_path}")

    # epub_path = build_bundle_epub(bundle_yaml)
    # print(f"Built EPUB: {epub_path}")


if __name__ == "__main__":
    main()