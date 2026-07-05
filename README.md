# Academic Homepage Hugo Template

This repository is a reusable Hugo static-site template for an academic
homepage. The sample content under `content/`, `data/`, `bib/`, and `static/`
can be used as a reference when adapting the site for a different person.

## Requirements

- [Hugo Extended](https://gohugo.io/). The site has been verified with Hugo `v0.163.3`.
- [Python 3](https://www.python.org/) for regenerating publication data from BibTeX. The site has been verified with `Python 3.13.5`.
- [PowerShell](https://learn.microsoft.com/en-us/powershell/) for the Windows commands shown below. I recommend using `PowerShell 7`.

## Repository Map

- `hugo.yaml`: site configuration, including `baseURL`, top navigation, and SEO defaults.
- `content/`: Markdown pages and section pages.
- `data/profile.yaml`: profile, contact details, portrait, and homepage links.
- `data/news.yaml`: news items rendered on the News page and optionally on the homepage.
- `bib/refs.bib`: source of truth for publication entries.
- `data/publications.json`: generated publication data for Hugo.
- `static/img/`: images copied directly into the built site.
- `static/pdf/`: PDF files copied directly into the built site.
- `layouts/`: Hugo templates and partials.
- `layouts/index.webmanifest`: generated web manifest template.
- `assets/css/main.css`: single site stylesheet, organized by section comments.
- `assets/js/navigation.js`: mobile navigation behavior.
- `scripts/build_publications.py`: converts `bib/refs.bib` into `data/publications.json`.
- `public/`: generated output only; do not edit it by hand.

See [docs/content-maintenance.md](docs/content-maintenance.md) before changing
profile data, news, publications, pages, images, or PDFs.

## Layout Model

The template intentionally keeps only a few page layouts:

- Home page: `layouts/index.html`; page content and homepage section switches
  live in `content/_index.md`.
- Ordinary top-level pages, such as Research, Teaching, and Group:
  `layouts/_default/list.html`.
- Ordinary child pages, such as project, software, and course pages:
  `layouts/_default/single.html`.
- Publications page: `layouts/publications/list.html`.
- News page: `layouts/news/list.html`.
- Shared page title block: `layouts/partials/page-header.html`.
- Shared Markdown content block: `layouts/partials/page-content.html`.
- Shared resource link resolver: `layouts/partials/resource-href.html`.
- Shared anchor renderer for static and external resources:
  `layouts/partials/resource-link.html`.
- SEO metadata entry point: `layouts/partials/seo.html`; structured data lives in
  `layouts/partials/structured-data.html`.

This means most new pages should be added only under `content/`; they do not
need new HTML templates. Tags and categories are disabled by default to keep the
template simple and avoid unused taxonomy pages.

## First-Time Setup

1. Install Hugo Extended and confirm it is available:

```powershell
hugo version
```

If this command fails even though Hugo is installed, add the Hugo executable to
`PATH`, or replace `hugo` in the commands below with the full path to
`hugo.exe`.

2. Install Python 3 and confirm it is available:

```powershell
python --version
```

3. Update personal profile information in `data/profile.yaml`. This is the
   single source for the homepage owner's name, contact details, portrait, and
   homepage links.

4. Update the site configuration in `hugo.yaml`:

```yaml
baseURL: "https://example.edu/~username/"
title: "Academic Homepage"
params:
  dateFormat: "Jan 2006"
```

`title` is only a generic fallback title. The homepage owner's name and summary
belong in `data/profile.yaml`.

5. Update news, publications, and Markdown pages as needed:

- `data/news.yaml`
- `bib/refs.bib`
- Markdown pages under `content/`

## Update Publications

After editing `bib/refs.bib`, regenerate the Hugo data file:

```powershell
python .\scripts\build_publications.py
```

Review `data/publications.json` only to confirm the output; do not maintain it
by hand during normal editing.

## Manage Pages And Navigation

Top-level navigation is controlled by `menus.main` in `hugo.yaml`. To add a new
top-level page:

1. Add a section file such as `content/service/_index.md` or
   `content/projects/_index.md`.
2. Add a matching menu item in `hugo.yaml` with `identifier`, `name`, `pageRef`,
   and menu `weight`.
3. Run `hugo server` and confirm the navigation order.

To remove a top-level page, remove or archive its content file or folder, then
remove the matching `menus.main` item.

For ordinary nested pages, add Markdown files under an existing section, such as
`content/research/project-name.md` or `content/teaching/courses/course-name.md`.
Use front matter `title`, `description`, `class`, and `aliases` to control page
metadata. Do not add `weight` to Markdown pages; top navigation order is
maintained only in `hugo.yaml`. Do not add a top-level Markdown `#` heading at
the start of the body; the template renders the page title from front matter so
all pages align consistently.

`description` supports Markdown links, for example:

```yaml
description: "A short note with a [link](/research/)."
```

## Homepage Content

The homepage always renders the profile hero from `data/profile.yaml`. The
editable homepage body comes from `content/_index.md`, so it can contain normal
Markdown sections such as Biography, About Me, Research Interests, or Service.

Use `showNews` and `showPublications` in `content/_index.md` to control whether
the homepage shows the Recent News and Selected Publications blocks:

```yaml
---
title: "Home"
showNews: true
showPublications: true
---
```

Both values default to `true` when omitted. Set either value to `false` to hide
that block from the homepage.

## Local Preview

For ordinary local preview, run:

```powershell
hugo server
```

If the final site will be deployed under a subpath, preview with the same URL
shape:

```powershell
hugo server --baseURL "http://localhost:1313/~username/" --appendPort=false
```

Use the preview server only for development. Do not deploy files generated by
`hugo server`.

## Production Build

1. Regenerate publication data if `bib/refs.bib` changed:

```powershell
python .\scripts\build_publications.py
```

2. Delete the existing `public` folder manually in File Explorer if it exists.

3. Build the deployable site using the `baseURL` in `hugo.yaml`:

```powershell
hugo --gc --minify --environment production --destination public
```

4. Deploy only the final `public` folder.

## Pre-Publish Checklist

- Profile, news, pages, and publication data are edited in source files.
- `data/publications.json` has been regenerated if `bib/refs.bib` changed.
- Local image and PDF paths resolve under `static/`.
- `hugo --gc --minify --environment production --destination public` completes successfully.
- Only the final `public/` output is deployed.
