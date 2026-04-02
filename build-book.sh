#!/bin/bash
pandoc --citeproc --bibliography references.bib master-summary.md -o tmp.docx