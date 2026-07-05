# Content Maintenance Guide

This guide is for maintainers who know basic Markdown but are not expected to
know HTML, CSS, Hugo internals, or terminal scripting. The normal rule is:
edit source files, preview the site, delete the old `public` folder, then build
a new `public` folder for publishing.

## What To Edit

Most updates happen in these files:

| Task | Edit here |
| --- | --- |
| Name, title, email, office, portrait, CV link, Scholar link | `data/profile.yaml` |
| Homepage content and homepage section switches | `content/_index.md` |
| News | `data/news.yaml` |
| Publications | `bib/refs.bib` |
| Research, Teaching, Group, and other pages | `content/` |
| Images | `static/img/` |
| PDFs, slides, CV, course files | `static/pdf/` |
| Website URL, top navigation order, date format | `hugo.yaml` |

Avoid editing these during normal content work:

| File or folder | Reason |
| --- | --- |
| `public/` | Generated output. Delete and rebuild it instead of editing it. |
| `layouts/` | Page templates. Edit only when the site structure must change. |
| `assets/css/main.css` | Visual design. Edit only when the site style must change; the file is organized by section comments. |
| `assets/js/navigation.js` | Mobile navigation behavior. |
| `data/publications.json` | Generated from `bib/refs.bib`. |

## One Source For Each Type Of Information

To avoid confusion, each kind of information has one main home:

- Personal profile information and the person's SEO summary belong in `data/profile.yaml`.
- Top navigation labels and order belong in `hugo.yaml`.
- Page text belongs in Markdown files under `content/`.
- Publication data belongs in `bib/refs.bib`.
- News data belongs in `data/news.yaml`.

Do not duplicate personal links, portrait paths, or email addresses in
`hugo.yaml`. The homepage, footer, SEO metadata, and web manifest read personal
information from `data/profile.yaml`.

## Basic Workflow

Use this for ordinary changes:

1. Edit the source file.
2. Open PowerShell in the project folder.
3. Start the preview:

```powershell
hugo server
```

4. Open the preview address shown by Hugo, usually `http://localhost:1313/`.
5. Check the page in the browser.
6. Stop preview by pressing `Ctrl+C` in PowerShell.
7. When ready to publish, build the final site using the steps in
   [Production Build](#production-build).

## Markdown Basics

Markdown is used by files under `content/`.

```markdown
## Section Heading

This is a paragraph.

- Bullet item
- Another bullet item

[Link text](/research/)

![Image description](img/example.jpg)
```

Important heading rule:

- Put the page title in front matter.
- Do not start the page body with `# Page Title`.
- Start body sections with `##`.

This keeps title placement consistent across pages.

## YAML Basics

Files such as `hugo.yaml`, `data/profile.yaml`, and `data/news.yaml` use YAML.
YAML is sensitive to indentation.

```yaml
displayName: "Homepage Owner"
photo: "img/profile.jpg"
links:
  - label: "[CV]"
    url: "pdf/cv.pdf"
```

Rules:

- Keep the existing indentation style.
- Use spaces, not tabs.
- Use quotes around text that contains punctuation or special characters.
- Keep list items aligned with `-`.

## Site Configuration

Site-level settings live in `hugo.yaml`.

Common fields:

- `baseURL`: final website URL.
- `title`: generic fallback title. The person's name comes from `data/profile.yaml`.
- `menus.main`: top navigation labels and order.
- `params.dateFormat`: footer date format.

Example:

```yaml
baseURL: "https://example.edu/~username/"
title: "Academic Homepage"
params:
  dateFormat: "Jan 2006"
```

`params.description` and `params.keywords` are intentionally not used. The
person-specific search description is `summary` in `data/profile.yaml`, and the
HTML `keywords` meta tag is not useful enough to justify another field for
non-technical maintainers.

Top navigation order is controlled only by `menus.main` in `hugo.yaml`:

```yaml
menus:
  main:
    - identifier: research
      name: Research
      pageRef: /research
      weight: 20
```

Smaller menu `weight` values appear earlier. Do not add `weight` to Markdown
page front matter.

Tags and categories are disabled by default to avoid extra taxonomy pages.

## Layout Model

The site uses a small number of reusable layouts:

| Page type | Layout file | Normal action |
| --- | --- | --- |
| Home | `layouts/index.html` | Edit `content/_index.md` and `data/profile.yaml`. |
| Research, Teaching, Group, and similar section pages | `layouts/_default/list.html` | Edit the section `_index.md`. |
| Project, software, course, and similar child pages | `layouts/_default/single.html` | Add or edit Markdown files under `content/`. |
| Publications | `layouts/publications/list.html` | Edit `bib/refs.bib`, then regenerate JSON. |
| News | `layouts/news/list.html` | Edit `data/news.yaml`. |

Software pages, project pages, and course pages share one child-page layout, so
their title position and spacing stay consistent.

Shared template parts keep repeated logic in one place:

- `layouts/partials/page-content.html` renders normal Markdown body content.
- `layouts/partials/page-header.html` renders page titles and descriptions.
- `layouts/partials/resource-href.html` resolves internal files and external links.
- `layouts/partials/resource-link.html` renders repeated resource links consistently.
- `layouts/partials/seo.html` renders standard SEO tags.
- `layouts/partials/structured-data.html` renders JSON-LD structured data.

Most maintainers do not need to edit these files. They are listed here to make
the site structure easier to understand if the template is customized later.

## Profile

Profile data lives in `data/profile.yaml`.

Common fields:

- `name`: normal name used by the footer, metadata, and generated manifest.
- `displayName`: name shown only in the homepage hero.
- `summary`: default search-engine description for the person.
- `title`: role or position.
- `department`, `university`: institution information shown on the homepage.
- `emailDisplay`: email text shown on the page.
- `office`: office location.
- `photo`: portrait path under `static/`.
- `publicationAuthorNames`: name variants highlighted in publications.
- `links`: homepage links such as CV, Google Scholar, lab site, or GitHub.

Example:

```yaml
name: "Homepage Owner"
displayName: "Homepage Owner"
summary: "Academic homepage of Homepage Owner."
title: "Professor"
department: "Department Name"
university: "University Name"
emailDisplay: "name [at] example.edu"
photo: "img/profile.jpg"
links:
  - label: "[CV]"
    url: "pdf/cv.pdf"
  - label: "[Google Scholar]"
    url: "https://scholar.google.com/"
```

If the file is `static/img/profile.jpg`, write the path as `img/profile.jpg`.

## Homepage Content

The homepage always starts with the profile hero, which reads from
`data/profile.yaml`. Everything below the hero is controlled by
`content/_index.md`.

Use normal Markdown headings and paragraphs in `content/_index.md`:

```markdown
---
title: "Home"
showNews: true
showPublications: true
---

## Biography

Short biography text.

## Research Interests

- Signal processing
- Optimization
```

Homepage-only fields:

- `showNews`: set to `false` to hide the Recent News block from the homepage.
- `showPublications`: set to `false` to hide the Selected Publications block
  from the homepage.

If these fields are omitted, both blocks are shown by default.

## News

News items live in `data/news.yaml`. The News page always reads this file; the
homepage Recent News block is shown only when `showNews` in `content/_index.md`
is not `false`.

```yaml
items:
  - time: "Jun 2026"
    text: "A new paper was accepted."
    images:
      - "paper-award.jpg"
    pdf: "pdf/papers/example.pdf"
```

Common fields:

- `time`: date shown on the site, such as `Jun 2026` or `2026-05`.
- `text`: Markdown text.
- `image`: one image under `static/img/news/`.
- `images`: several images under `static/img/news/`.
- `pdf`, `slides`, `file`: local files, usually under `static/pdf/`.
- `arxiv`, `code`: external links.

Simple image names, such as `paper-award.jpg`, are read from
`static/img/news/`.

## Publications

Publication source data lives in `bib/refs.bib`.

After editing `bib/refs.bib`, run:

```powershell
python .\scripts\build_publications.py
```

This updates `data/publications.json`. Do not edit `data/publications.json`
by hand during normal maintenance.

Useful website-specific BibTeX fields:

```bibtex
selected={true},
order={1},
status={preprint},
pdf={pdf/papers/example-paper.pdf},
slides={pdf/papers/example-slides.pdf},
code={https://github.com/example/project},
doi={10.0000/example},
award={Best Paper Award}
```

`selected={true}` shows a paper in the homepage Selected Publications block
when `showPublications` is not `false`. Local file paths should not include the
deployed website subpath.

## Pages

Markdown pages live under `content/`.

Common files:

- `content/_index.md`: homepage content and homepage section switches.
- `content/research/_index.md`: Research page.
- `content/publications/_index.md`: Publications intro text.
- `content/teaching/_index.md`: Teaching page.
- `content/group/_index.md`: Group page.
- `content/news/_index.md`: News intro text.
- Nested files such as `content/research/software/example.md` or
  `content/teaching/courses/example.md`: child pages.

A page starts with front matter:

```yaml
---
title: "Page Title"
description: "Optional short description with a [link](/research/)."
showChildren: false
class: "Software"
aliases:
  - "/old-path/"
hideNav: false
---
```

Common fields:

- `title`: page title shown at the top.
- `description`: short text shown under the title. It supports Markdown links.
- `showChildren`: set to `true` on section pages to list child pages.
- `showNews`: set to `false` on the homepage to hide Recent News.
- `showPublications`: set to `false` on the homepage to hide Selected Publications.
- `class`: group label used when a parent page lists child pages.
- `aliases`: old URLs that should redirect to this page.
- `hideNav`: hide the top navigation for special pages.

The visible `description` is styled in a lighter color than the body text. If
you want to add a link, write:

```yaml
description: "See the [research page](/research/) for details."
```

The same description is also used for metadata. For metadata, Markdown
formatting is automatically converted to plain text.

## Add A Top-Level Page

Example: add a Projects page.

1. Create `content/projects/_index.md`.
2. Add front matter and content:

```markdown
---
title: "Projects"
description: "Selected projects."
showChildren: true
---

Introductory text for the Projects page.
```

3. Add a menu item in `hugo.yaml`:

```yaml
menus:
  main:
    - identifier: projects
      name: Projects
      pageRef: /projects
      weight: 70
```

4. Run `hugo server` and check the top navigation.

Only `hugo.yaml` controls top navigation order.

## Remove A Top-Level Page

1. Delete or archive the related folder under `content/`.
2. Remove the matching item from `menus.main` in `hugo.yaml`.
3. Run `hugo server`.
4. Check that the menu item is gone.

## Add A Child Page

Child pages do not need a new layout file.

Example paths:

```text
content/research/project-name.md
content/research/software/tool-name.md
content/teaching/courses/course-name.md
```

Example child page:

```markdown
---
title: "Project Name"
description: "Short project description."
class: "Projects"
---

## Overview

Project description starts here.
```

## Automatically List Child Pages

Set `showChildren: true` in a section page such as
`content/teaching/_index.md`:

```yaml
---
title: "Teaching"
showChildren: true
---
```

The template searches child Markdown files under that section and groups them.
When `showChildren` is enabled, avoid manually repeating those same child-page
links in the section body.

If a child page has `class`, that value becomes the group heading:

```yaml
---
title: "ENGG 5781 Matrix Analysis and Computations"
class: "Current Teaching"
---
```

Rendered result:

```markdown
## Current Teaching

- [ENGG 5781 Matrix Analysis and Computations](/teaching/courses/engg5781/)
```

If `class` is not set, the first subfolder name is used. For example,
`content/teaching/projects/example.md` appears under `Projects`.

Within each group, child pages are sorted alphabetically by title.

## Links And Static Files

Recommended folders:

- Portrait and general images: `static/img/`.
- News images: `static/img/news/`.
- Project or software images: `static/img/projects/` or `static/img/software/`.
- Papers and slides: `static/pdf/papers/`.
- Course files: `static/pdf/courses/`.
- CV: `static/pdf/cv.pdf`.

Examples:

```markdown
[Research](/research/)
[CV](pdf/cv.pdf)
![Profile photo](img/profile.jpg)
![Smaller profile photo](img/profile.jpg "width=360")
![Half-width profile photo](img/profile.jpg "width=50%")
```

Images are centered automatically. If an image is too large, add `width=...`
inside the optional image title. Use a pixel value such as `width=360` or a
percentage such as `width=50%`.

Do not include the deployment subpath. Write `/research/`, not
`/~username/research/`.

The same link rules are used by Markdown pages, news items, publications, and
SEO image paths, so paths can be maintained consistently across the site.

## Production Build

Use this when preparing files for publication.

1. If publications changed, run:

```powershell
python .\scripts\build_publications.py
```

2. In File Explorer, delete the existing `public` folder if it exists.
3. In PowerShell, run:

```powershell
hugo --gc --minify --environment production --destination public
```

4. Publish the newly generated `public` folder.

Do not publish files generated while `hugo server` is running. Use the
production build above for the final website.

## Common Problems

Page title appears twice:

- Remove the first `# Page Title` from the Markdown body.
- Keep the title only in front matter.

New top-level page does not appear in the menu:

- Confirm the page has a file such as `content/projects/_index.md`.
- Confirm `hugo.yaml` has a matching `menus.main` item.
- Confirm `pageRef` matches the page path, such as `/projects`.

Navigation order looks wrong:

- Edit only the menu `weight` values in `hugo.yaml`.
- Do not add `weight` to Markdown pages.

Child pages do not appear on a section page:

- Set `showChildren: true` in that section's `_index.md`.
- Confirm the child page is under the same section folder.
- Confirm the child page is a Markdown file, not only a folder.

Child page appears under the wrong heading:

- Add or edit `class` in the child page front matter.
- If `class` is missing, the first subfolder name is used.

Image does not appear:

- Confirm the image file is under `static/img/` or another `static/` folder.
- Do not write `static/` in the page path.
- Example: file location `static/img/profile.jpg`, page path `img/profile.jpg`.

PDF link does not work:

- Confirm the file is under `static/pdf/`.
- Use a path such as `pdf/cv.pdf` or `pdf/papers/example.pdf`.

Publication does not appear:

- Confirm the entry is in `bib/refs.bib`.
- Run `python .\scripts\build_publications.py`.
- Refresh the preview page.

Generated site still shows preview-only content:

- Delete the `public` folder manually.
- Run the production build again.
- Publish only the newly generated `public` folder.

## Pre-Publish Checklist

Before publishing:

- `hugo.yaml` has the correct `baseURL`, menu, and date format.
- Personal profile data is updated in `data/profile.yaml`.
- News, pages, and publications were edited in their source files.
- `data/publications.json` was regenerated if `bib/refs.bib` changed.
- Content links do not hard-code the deployed subpath.
- Image and PDF paths point to files under `static/`.
- The local preview looks correct on desktop and mobile widths.
- The production build completes successfully.
- Only the newly generated `public` folder is deployed.
