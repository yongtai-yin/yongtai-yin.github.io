# Yongtai Yin Personal Homepage

This repository contains the source files for Yongtai Yin's personal academic homepage, built with Jekyll and hosted on GitHub Pages.

The site is intentionally lightweight: most content is maintained through Markdown files and YAML data files, while reusable page fragments live in `_includes/`.

## Project Structure

```text
.
├── _config.yml                  # Site title, description, navigation, URL
├── index.md                     # Homepage content and profile metadata
├── publications.md              # Publications page
├── blog.md                      # Blog index page
├── cv.md                        # CV page, embeds assets/pdf/cv.pdf
├── _data/
│   ├── news.yml                 # Homepage news items
│   └── publications.yml         # Publication records
├── _includes/
│   ├── news-list.html           # Renders homepage news
│   ├── publication-item.html    # Renders one publication item
│   └── social-links.html        # Renders profile social links
├── _layouts/
│   ├── default.html             # Main site layout
│   └── post.html                # Blog post layout
├── _posts/                      # Blog posts
├── assets/
│   ├── css/style.css            # Global visual style
│   ├── js/theme-toggle.js       # Light/dark mode toggle
│   ├── js/blog-filter.js        # Blog tag filtering
│   ├── img/                     # Avatar and publication images
│   └── pdf/cv.pdf               # CV PDF
└── Gemfile                      # GitHub Pages/Jekyll dependency entry
```

## Common Content Updates

### Update Homepage Profile

Edit the front matter at the top of `index.md`.

```yaml
header_name: Yongtai Yin
avatar: /assets/img/avatar.png
position: Ph.D. Student in Electronic Engineering
affiliation: The Chinese University of Hong Kong
email: ytyin [at] link.cuhk.edu.hk
socials:
  - name: Google Scholar
    url: "https://scholar.google.com/citations?user=..."
    icon: ai ai-google-scholar
```

Use `position` and `affiliation` for the homepage profile header. Social icons are rendered by `_includes/social-links.html`.

### Update About Me or Research Interests

Edit the Markdown body of `index.md`.

```markdown
## About Me

...

## Research Interests

- Optimization and nonconvex methods for signal processing
- Model-based deep learning and generative modeling
- Wireless sensing, localization, and array signal processing
```

Keep the text short and formal. The homepage is meant to be a concise academic profile.

### Add or Edit News

Edit `_data/news.yml`.

```yaml
- date: Jan 2026
  content: "One paper accepted to [ICASSP 2026](https://2026.ieeeicassp.org/) (Barcelona, Spain)."
```

Add newer items at the top. The `content` field supports Markdown links and emphasis.

### Add a Publication

Edit `_data/publications.yml`. Add newer publications near the top so that the homepage and Publications page stay in reverse chronological order.

Template:

```yaml
- title: "Paper Title"
  authors:
    - name: "Yongtai Yin"
      self: true
    - name: "Coauthor Name"
  venue: "Conference or Journal Name, Year"
  short_venue: "Venue"
  year: 2026
  type: conference
  status: accepted
  image: "/assets/img/example.png"
  selected: true
  links:
    pdf: "/assets/pdf/example.pdf"
    code: "https://github.com/example/repo"
    project: "https://example.com/project"
    doi: "10.xxxx/example"
    arxiv: "2401.00000"
    bibtex: "#"
    data: "https://example.com/data"
```

Required fields:

- `title`
- `authors`
- `venue`
- `short_venue`
- `year`
- `type`
- `status`
- `selected`
- `links`

Author highlighting:

- Mark Yongtai's author entry with `self: true`.
- Each publication should have exactly one `self: true`.

Publication type:

- Use values such as `conference`, `journal`, or `preprint`.

Publication status:

- `published` is treated as the default final state and is not displayed as a label.
- `accepted`, `preprint`, `under_review`, and `in_press` are displayed as lightweight status labels.

Links:

- `doi` can be either a bare DOI such as `10.xxxx/example` or a full `https://doi.org/...` URL.
- `arxiv` can be either an arXiv ID such as `2401.00000` or a full `https://arxiv.org/abs/...` URL.
- Leave unavailable links out of `links`, or keep `links: {}` when there are no links.

Homepage selection:

- Set `selected: true` to show a publication on the homepage.
- Set `selected: false` to show it only on the Publications page.

Publication images:

- Put images in `assets/img/`.
- Reference them with absolute site paths, for example `/assets/img/2024-IOTJ.png`.
- If `image` is omitted, the publication still renders correctly; the image column will simply be empty on desktop and hidden on mobile.

### Update the CV

Replace:

```text
assets/pdf/cv.pdf
```

The CV page `cv.md` embeds this PDF directly. Keep the same filename if you want the existing page to work without further edits.

### Add a Blog Post

Create a Markdown file in `_posts/` using this filename format:

```text
YYYY-MM-DD-title.md
```

Example:

```markdown
---
layout: post
title: "Post Title"
date: 2026-01-27
tags: [reinforcement learning]
katex: true
---

Post content goes here.
```

Notes:

- `tags` are used by the Blog page filter.
- Set `katex: true` if the post contains math.
- Posts are listed automatically on `blog.md`.

### Update Navigation

Edit `_config.yml`.

```yaml
navigation:
  - title: Home
    url: /
  - title: CV
    url: /cv/
  - title: Publications
    url: /publications/
  - title: Blog
    url: /blog/
```

Navigation active states are handled in `_layouts/default.html`.

## When to Edit Templates

Most routine updates should not require editing templates.

Edit these files only when changing layout or rendering behavior:

- `_includes/publication-item.html`: publication item markup and link rendering
- `_includes/news-list.html`: news list rendering
- `_includes/social-links.html`: social link rendering
- `_layouts/default.html`: site-wide layout, navigation, metadata, footer
- `assets/css/style.css`: visual design
- `assets/js/theme-toggle.js`: dark mode behavior
- `assets/js/blog-filter.js`: blog tag filtering

## Local Preview

This site uses GitHub Pages/Jekyll.

Typical local preview command:

```bash
bundle exec jekyll serve
```

Then open:

```text
http://localhost:4000
```

If Bundler is missing or version-mismatched, install the Bundler version required by `Gemfile.lock` or update the local Ruby/Bundler environment. GitHub Pages will build the site using its supported Jekyll environment after pushing to the repository.

## Maintenance Checklist

Before pushing updates:

- Check YAML syntax in `_data/news.yml` and `_data/publications.yml`.
- Confirm each publication has exactly one `self: true` author.
- Confirm new images or PDFs are placed under `assets/`.
- Preview the homepage, Publications page, Blog page, and CV page.
- Check both light and dark modes after visual changes.
