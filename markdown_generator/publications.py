#! /usr/bin/python3
# coding: utf-8
# Generate a markdown file from Bibtex entries for "academicpages"
import os
import bibtexparser as bp
from bibtexparser.bwriter import BibTexWriter
from bibtexparser.bibdatabase import BibDatabase

bibfile = open("/home/cwatson/texmf/bib/bib/personal.bib")
bibdb = bp.load(bibfile)

## Escape special characters
# YAML is very picky about how it takes a valid string, so we are replacing single and double quotes
# (and ampersands) with their HTML encoded equivalents.
# This makes them look not so readable in raw format, but they are parsed and rendered nicely.
html_escape_table = {
    "&": "&amp;",
    '"': "&quot;",
    "'": "&apos;"
    }

def html_escape(text):
    """Produce entities within text."""
    return "".join(html_escape_table.get(c,c) for c in text)

# Loop through all entries in the bibtex file and concatenate a string containing
# the markdown for each type. YAML metadata is first, then the description for each pub.
for entries in bibdb.entries_dict:
    entry = bibdb.entries_dict.get(entries)

    ## YAML variables
    ID = entry.get('ID')
    year = entry.get('year')
    date = entry.get('date')
    journal = html_escape(entry.get('journal'))
    title = entry.get('title').replace('{', '')
    title = title.replace('}', '')
    if 'url' in entry:
        url = entry.get('url')
    else:
        if 'doi' in entry:
            doi = entry.get('doi')
            if doi[0] == '1':
                url = "https://doi.org/" + doi
            else:
                url = doi
        else:
            url = "https://cwatson.github.io/"

    md = "---\ntitle: \""   + title + "\""
    md += """\ncollection: publications"""
    md += """\npermalink: /publication/""" + ID
    md += "\ndate: " + date
    md += "\nvenue: '" +  journal + "'"
    md += "\npaperurl: '" + url + "'"

    citation = entry.get('author') + " (" + year + "). <u>" + title + "</u>."
    citation += " <i>" + journal + "</i>. " + entry.get('volume')
    if 'number' in entry:
        citation += "(" + entry.get('number') + ")"

    pages = entry.get('pages').replace(' ', '')
    pages = pages.replace('--', '-')
    citation += ":" + pages + "."

    md += "\ncitation: '" + html_escape(citation) + "'\n---"

    # Markdown description for individual page
    md += "\n\n<a href='" + url + "'>Download paper here</a>\n"

    md_filename = ID + ".md"
    md_filename = os.path.basename(md_filename)

    with open("../_publications/" + md_filename, 'w') as f:
        f.write(md)
