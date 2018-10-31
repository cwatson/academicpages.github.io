#! /usr/bin/python3
# coding: utf-8
# Generate a markdown file from Bibtex entries for "academicpages"
import os
import bibtexparser as bp
from bibtexparser.bwriter import BibTexWriter
from bibtexparser.bibdatabase import BibDatabase

#    The .md file will be `YYYY-MM-DD-[url_slug].md` and the permalink will be `https://[yourdomain]/publications/YYYY-MM-DD-[url_slug]`
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

## Creating the markdown files
# This is where the heavy lifting is done. This loops through all the rows in the TSV dataframe,
# then starts to concatentate a big string (```md```) that contains the markdown for each type.
# It does the YAML metadata first, then does the description for the individual page.
# If you don't want something to appear (like the "Recommended citation")
for entries in bibdb.entries_dict:
    entry = bibdb.entries_dict.get(entries)

    md_filename = str(entry.get('ID')) + ".md"
#    html_filename = str(item.pub_date) + "-" + item.url_slug
#    year = item.pub_date[:4]

    ## YAML variables
    md = "---\ntitle: \""   + entry.get('title')
    md += """\ncollection: publications"""
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

    md += """\npermalink: /publication/""" + entry.get('ID')

#    if len(str(item.excerpt)) > 5:
#        md += "\nexcerpt: '" + html_escape(item.excerpt) + "'"

    md += "\ndate: " + str(entry.get('year'))
    md += "\nvenue: '" + html_escape(entry.get('journal')) + "'"
    md += "\npaperurl: '" + url + "'"

    citation = entry.get('author') + " (" + entry.get('year') + "). <u>" + entry.get('title') + "</u>."
    citation += " <i>" + entry.get('journal') + "</i>. " + entry.get('volume')
    if 'number' in entry:
        citation += "(" + entry.get('number') + ")"

    pages = entry.get('pages').replace(' ', '')
    pages = pages.replace('--', '-')
    citation += ":" + pages + "."

    md += "\ncitation: '" + html_escape(citation) + "'"
    md += "\n---"

    ## Markdown description for individual page
#    if len(str(item.paper_url)) > 5:
    if 'url' in entry:
        md += "\n\n<a href='" + entry.get('url') + "'>Download paper here</a>\n"

#    if len(str(item.excerpt)) > 5:
#        md += "\n" + html_escape(item.excerpt) + "\n"

    md += "\nRecommended citation: " + citation
    md_filename = os.path.basename(md_filename)

    with open("../_publications/" + md_filename, 'w') as f:
        f.write(md)
