# The Psychology of Judgment and Decision-Making

Content and build scripts for a University textbook. This textbook is AI-generated based on an outline and summaries of primary sources. The result is intended to a be first draft to be edited by humans.

Copyright 2026 Sebastiaan Mathôt (@smathot)


## Dependencies

The following Python libraries are required.
   
```
pip install sigmund pypdf weasyprint pypandoc bibtexparser
```

You also need to set API keys for Mistral, OpenAI, and Anthropic (all three are required) as environment variables.

```
export OPENAI_API_KEY="key here"
export ANTHROPIC_API_KEY="key here"
export MISTRAL_API_KEY="key here"
```


## Write outline

The outline of the textbook should be in `input/md/outline.md`. This should consist of level-1 headings (`#`), corresponding to parts in the book, and level-2 headings (`##`), corresponding to chapters. Each chapter should have a concise description including references in pandoc citeproc format (e.g. `@ahn_etal1995`).

A condensed outline following roughly the same format should be in `input/md/condensed-outline.md`. (This can be AI-generated from the larger outline.)

The textbook metadata, including the order of the chapters, is defined in `input/yaml/jdm.yaml`. The chapters are also explicitly listed in `input/md/chapters/contents.md` (i.e. the table of contents is not auto-generated).

## Organize references

References should be defined in `references/references.bib`. For each source (e.g. `@ahn_etal1995`), the corresponding pdf should be saved as `references/pdf/anh_etal1995.pdf`.

To easily retrieve pdfs for all references by automatically opening URLs in a browser, run:

```
python manage_refs.py check
python manage_refs.py check --scihub
```

Once all pdfs are available, extract the text using:

```
python manage_refs.py ocr
```

And create summaries using:

```
python manage_refs.py summarize
```


## Write chapters

```
python write.py
```


## Build book


```
python build.py
```


## License

This work is released under a [CC-by 4.0 license](https://creativecommons.org/licenses/by/4.0/). You must give appropriate credit, provide a link to the license, and indicate if changes were made. You may do so in any reasonable manner, but not in any way that suggests the licensor endorses you or your use.
