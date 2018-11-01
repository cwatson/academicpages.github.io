---
layout: archive
title: "CV"
permalink: /cv/
author_profile: true
redirect_from:
  - /resume
---

{% include base_path %}

<h2>Table of Contents</h2>
* TOC
{:toc}

## Education

| Year  | Institution                                           |
| ----- | ------------------------------------                  |
| 2016  | Boston University, Boston, MA                         |
|       | Ph.D in Computational Neuroscience                    |
|       | Dissertation title: [*Brain structural connectivity and neurodevelopment in post-Fontan adolescents*](https://hdl.handle.net/2144/19163) |
| 2007  | Massachusetts Institute of Technology, Cambridge, MA  |
|       | B.S. in Brain & Cognitive Sciences                    |

## Work experience
* September 2016 -- present
  * Postdoctoral Research Fellow
  * Children's Learning Institute; Dept. of Pediatrics, University of Texas Health Science Center at Houston
  * Supervisor: Linda Ewing-Cobbs, Ph.D

* October 2007 -- August 2016
  * Research Assistant
  * Dept. of Neurology, Boston Children's Hospital
  * Supervisor: Michael Rivkin, M.D.

## Skills

| Category                          |                                                                   |
| ----------                        | ---------------------------------------------------------------   |
| *Operating systems*               | Linux/Unix, Windows                                               |
| *Software*                        | R, Freesurfer, FSL, Matlab, SPM, \LaTeX, Microsoft Office Suite   |
| *Programming languages*           | R, Matlab, Bash (shell), Python                                   |
| *Neuropsychological assessments*  | WASI, WISC, D-KEFS, CTOPP, CELF, Grooved pegboard                 |

## Publications
  <ul>{% for post in site.publications %}
    {% include archive-single-cv.html %}
  {% endfor %}</ul>

## Talks
  <ul>{% for post in site.talks %}
    {% include archive-single-talk-cv.html %}
  {% endfor %}</ul>

{% comment %}
## Teaching
  <ul>{% for post in site.teaching %}
    {% include archive-single-cv.html %}
  {% endfor %}</ul>

## Service and leadership
* Currently signed in to 43 different slack teams
{% endcomment %}
