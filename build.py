import subprocess
from pathlib import Path
import re
import pypandoc
import yaml
from pypdf import PdfReader, PdfWriter
from weasyprint import HTML, CSS

# ---- Inputs (adjust as needed) ------------------------------------------------
HTML_TEMPLATE = "styles/template.html"
HTML_STYLESHEETS = ["styles/base.css"]
WEASY_EXTRA_CSS = ["styles/print.css"]
CITATION_STYLE = "styles/apa.csl"

# Math rendering method for Pandoc → HTML/PDF conversion.
# Options:
#   "--mathml"                                        : MathML (WeasyPrint support is limited)
#   "--webtex=https://latex.codecogs.com/svg.image?"  : SVG images via CodeCogs (internet required)
#   "--webtex=https://latex.codecogs.com/png.image?"  : PNG images via CodeCogs (internet required)
MATH_RENDERING = "--webtex=https://latex.codecogs.com/svg.image?"

# Math rendering for EPUB. Uses PNG instead of SVG because SVG support is
# inconsistent across e-readers (Kindle, Kobo, Apple Books, etc.).
# Pandoc fetches and embeds the images directly into the EPUB archive.
EPUB_MATH_RENDERING = "--webtex=https://latex.codecogs.com/png.image?"

# Optional: pdfs that should be added before and after the main content.
# If an entry is None, a blank page will be inserted at that position.
PREFIX_PDF = [
    "input/pdf/blank.pdf",
    "input/pdf/title-page.pdf",
    "input/pdf/colofon.pdf"
]
SUFFIX_PDF: list[str | None] = []

# Bundle descriptor (YAML containing metadata + contents list)
BUNDLE_INFO = "input/yaml/jdm.yaml"

# Output root (all final outputs go here)
OUTPUT_DIR = Path("output")

# Chapter markdown files directory
CHAPTERS_DIR = Path("input/md/chapters")

# BibTeX references
REFERENCES = Path("references/references.bib")


def preprocess_md(md: str) -> str:
    # Ensure dialogue dashes are separated so they get their own paragraph.
    md = md.replace("\n— ", "\n\n—&thinsp;")

    def process_block(match):
        block = match.group(1)
        lines = block.splitlines()
        while lines and not lines[0].strip():
            lines.pop(0)
        while lines and not lines[-1].strip():
            lines.pop()
        return '\n'.join(['```'] + lines + ['```'])

    pattern = re.compile(r'```(.*?)```', re.DOTALL)
    return pattern.sub(process_block, md)


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
    Get chapter basenames from bundle YAML.

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
            f"Could not parse chapter list from {yaml_path}.\n"
            f"Expected a list under one of: contents/titles/stories."
        )
    return [t.strip() for t in titles if (CHAPTERS_DIR / f"{t}.md").exists()]


def _pandoc_metadata_block(bundle: dict, *, fallback_title: str) -> str:
    """
    Create a Pandoc YAML metadata block (--- ... ---) for EPUB.

    Keep keys conservative so they map well to EPUB2 OPF fields.
    """
    meta: dict = {}

    title = bundle.get("title") or fallback_title
    if title:
        meta["title"] = title

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

    yaml_text = yaml.safe_dump(meta, sort_keys=False, allow_unicode=True).strip()
    return f"---\n{yaml_text}\n---\n\n"


# ---- WeasyPrint PDF render ----------------------------------------------------


def html_to_pdf_weasyprint(html_path: Path, *, out_pdf: Path, base_url: str | None = None) -> Path:
    """
    Render HTML -> PDF using WeasyPrint's Python API.

    Images and other relative paths in the HTML are resolved relative to
    base_url, which defaults to the project root (i.e. where you run the
    script from). So 'input/figures/fig1.png' in your markdown resolves to
    '{project_root}/input/figures/fig1.png'.
    """
    out_pdf.parent.mkdir(parents=True, exist_ok=True)

    if base_url is None:
        base_url = str(Path(".").resolve())

    stylesheets = [CSS(filename=css) for css in WEASY_EXTRA_CSS]
    doc = HTML(filename=str(html_path), base_url=base_url).render(stylesheets=stylesheets)
    doc.write_pdf(str(out_pdf))
    return out_pdf


# ---- PDF merge helpers --------------------------------------------------------


def _merge_pdfs(pdf_paths: list[Path], out_path: str | Path) -> Path:
    """Merge PDFs in the given order into out_path."""
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

    If PREFIX_PDF/SUFFIX_PDF are empty, this is just a copy into final_pdf.
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
    very end. A table of contents (level-1 headings) is injected into the
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
        src = CHAPTERS_DIR / f"{title}.md"
        md_text = preprocess_md(src.read_text(encoding="utf-8")).strip()
        if not md_text.lstrip().startswith("#"):
            md_text = f"# {title}\n\n{md_text}"
        combined_parts.append(md_text)

    # Append a References section; the ::: {#refs} ::: div tells citeproc to
    # place all collected references at this location.
    combined_parts.append("# References\n\n<section id='references'>\n:::{#refs}\n:::\n</section>")

    combined_md = '\n\n<div class=\"bundle-break\"></div>\n\n' + "\n\n<div class=\"bundle-break\"></div>\n\n".join(combined_parts)

    # ---- 2. Single Pandoc call → one HTML with one reference list -----------
    bundle_html_path = OUTPUT_DIR / f"{yaml_path.stem}.html"
    bundle_html_path.parent.mkdir(parents=True, exist_ok=True)

    extra_args: list[str] = [
        "--standalone", "--template", HTML_TEMPLATE,
        "--citeproc",
        "--bibliography", str(REFERENCES),
        "--csl", CITATION_STYLE,
        MATH_RENDERING,
    ]
    for css in HTML_STYLESHEETS:
        extra_args += ["--css", css]

    html = pypandoc.convert_text(
        combined_md,
        to="html",
        format="md",
        extra_args=extra_args,
    )

    bundle_html_path.write_text(html, encoding="utf-8")

    # ---- 4. Render PDF with WeasyPrint & merge prefix/suffix pages ----------
    tmp_main_pdf = OUTPUT_DIR / f"{yaml_path.stem}.unmerged.pdf"
    html_to_pdf_weasyprint(bundle_html_path, out_pdf=tmp_main_pdf)

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
    Build a single EPUB2 for all chapters listed in yaml_path.

    Bundle YAML provides:
    - metadata (title/author/language/identifier/...)
    - cover_image path
    - css list
    - contents list

    Math is rendered as embedded PNG images (fetched from CodeCogs by Pandoc
    and bundled into the EPUB archive), ensuring offline compatibility across
    all e-readers.

    Final output is: output/<bundle-stem>.epub
    """
    yaml_path = Path(yaml_path)
    bundle = load_bundle_info(yaml_path)
    titles = bundle_titles(bundle, yaml_path)
    if not titles:
        raise ValueError(f"No titles in {yaml_path}")

    out_epub = OUTPUT_DIR / f"{yaml_path.stem}.epub"
    out_epub.parent.mkdir(parents=True, exist_ok=True)

    metadata_block = _pandoc_metadata_block(bundle, fallback_title=yaml_path.stem)

    combined_parts: list[str] = [metadata_block]
    for title in titles:
        src = CHAPTERS_DIR / f"{title}.md"
        md_text = preprocess_md(src.read_text(encoding="utf-8")).strip()
        if not md_text.lstrip().startswith("#"):
            combined_parts.append(f"# {title}\n\n{md_text}\n")
        else:
            combined_parts.append(md_text + "\n")

    combined_md = "\n\n".join(combined_parts).strip() + "\n"

    extra_args: list[str] = [
        "--to=epub2",
        "--citeproc",
        "--bibliography", str(REFERENCES),
        EPUB_MATH_RENDERING,
    ]

    cover = bundle.get("cover_image")
    if cover:
        cover_path = Path(cover)
        if not cover_path.exists():
            raise FileNotFoundError(cover_path)
        extra_args += ["--epub-cover-image", str(cover_path)]

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

    pypandoc.convert_text(
        combined_md,
        to="epub",
        format="md",
        outputfile=str(out_epub),
        extra_args=extra_args,
    )

    _run_epubcheck(out_epub)
    return out_epub


# ---- Main --------------------------------------------------------------------


def main() -> None:
    bundle_yaml = Path(BUNDLE_INFO)

    pdf_path = build_bundle_pdf(bundle_yaml)
    print(f"Built PDF:  {pdf_path}")

    epub_path = build_bundle_epub(bundle_yaml)
    print(f"Built EPUB: {epub_path}")


if __name__ == "__main__":
    main()