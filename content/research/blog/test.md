---
title: "Test for Markdown style"
description: "A temporary page for checking how Markdown syntax is rendered by the template."
class: "Blog"
aliases:
  - "/research/test/"
  - "/test/"
hideNav: false
---

## Paragraphs

This page is a temporary Markdown rendering test. It is intended for checking
spacing, text size, link style, list indentation, tables, code blocks, images,
math, and other common Markdown elements in the actual website layout.

This is a second paragraph. It contains a longer sentence so that line wrapping
can be inspected on desktop and mobile screens. The goal is to make sure normal
academic text remains readable when paragraphs become longer than one line.

Line breaks inside Markdown source are normally treated as spaces.
This sentence appears on the next source line, but it should remain in the same
paragraph unless a blank line is inserted.

To force a line break, add two spaces at the end of a line.  
This line should appear directly below the previous line.

## Inline Text

Regular text can include **bold text**, *italic text*, ***bold italic text***,
`inline code`, ~~strikethrough text~~, and escaped Markdown symbols such as
\*literal asterisks\*.

Academic writing often includes abbreviations, numbers, and punctuation: IEEE
TSP, ICASSP 2026, Section 3.2, Fig. 1, Eq. (4), and pp. 100-112.

## Links

Internal link:
[Research page](/research/)

External link:
[Hugo documentation](https://gohugo.io/)

Email link:
[Email example](mailto:name@example.edu)

Anchor link:
[Jump to the table section](#tables)

Local PDF link:
[Example course file](pdf/engg5781/lecture-0-course-info.pdf)

## Headings

# Heading Level 1

This level is included for testing only. Normal content pages should not start
with a level-1 heading because the template already renders the page title.

## Heading Level 2

Level-2 headings are recommended for main body sections.

### Heading Level 3

Level-3 headings are useful for subsections.

#### Heading Level 4

Level-4 headings can be used for smaller subdivisions.

##### Heading Level 5

Level-5 headings should be used sparingly.

###### Heading Level 6

Level-6 headings should be used sparingly.

## Lists

Unordered list:

- First item
- Second item
- Third item with a longer line that wraps on narrow screens and helps test
  indentation alignment

Ordered list:

1. First step
2. Second step
3. Third step

Nested list:

- Research area
  - Signal processing
  - Optimization
  - Machine learning
- Teaching area
  - Course page
  - Project page

Task list:

- [x] Completed item
- [ ] Incomplete item
- [ ] Another incomplete item with longer text

Definition-style list written in plain Markdown:

Term A
: Explanation for term A.

Term B
: Explanation for term B.

## Blockquotes

> This is a simple blockquote. It can be used for short notes, important
> reminders, or quoted material.

> A blockquote can contain multiple paragraphs.
>
> This is the second paragraph inside the same blockquote.

> Nested blockquote:
>
> > This is a nested quote.

## Code

Inline code example: use `hugo server` to preview the website locally.

Indented code block:

    hugo server
    hugo --gc --minify --environment production --destination public

Fenced code block without language:

```
baseURL: "https://example.edu/~username/"
title: "Academic Homepage"
```

Fenced code block with language:

```yaml
menus:
  main:
    - identifier: research
      name: Research
      pageRef: /research
      weight: 20
```

```python
def normalize_title(title):
    return " ".join(title.split())
```

## Tables

Basic table:

| Item | Purpose | Example |
| --- | --- | --- |
| `title` | Page title | `"Research"` |
| `description` | Short page summary | `"Selected research topics."` |
| `class` | Child page group label | `"Software"` |

Aligned table:

| Left aligned | Center aligned | Right aligned |
| :--- | :---: | ---: |
| alpha | beta | 1 |
| longer text | centered | 100 |
| final row | value | 1000 |

## Images

Local image using Markdown:

![photo](img/news/2026-Barcelona.jpg "width=50%")

Linked image:

[![photo linked to Research](img/news/2026-Barcelona.jpg "width=50%")](/research/)

Image with an external link below:

[Image source link example](https://example.com/)

## Math

Inline math example: \( \boldsymbol{x}^{\top}\mathbf{A}\boldsymbol{x} \).

Display math example:

\[
\mathbf{y} = \mathbf{H}\mathbf{x} + \mathbf{n}.
\]

Aligned display math:

\[
\begin{aligned}
f(\mathbf{x}) &= \|\mathbf{A}\mathbf{x} - \mathbf{b}\|_2^2, \\
\nabla f(\mathbf{x}) &= 2\mathbf{A}^{\top}(\mathbf{A}\mathbf{x} - \mathbf{b}).
\end{aligned}
\]

## Horizontal Rule

Text before the rule.

---

Text after the rule.

## Footnotes

This sentence has a footnote.[^note]

This sentence has another footnote with a longer explanation.[^long-note]

[^note]: This is a short footnote.

[^long-note]: This is a longer footnote. It is useful for checking spacing,
    indentation, and line wrapping in generated footnote blocks.

## Special Characters

Markdown can display symbols directly: alpha, beta, gamma, plus/minus, arrows,
and comparison signs can also be written in plain text when no mathematical
typesetting is needed.

Reserved HTML characters should render correctly when written as text:
`<`, `>`, `&`, and `"`.

## Mixed Academic Content Example

### Short Project Summary

This section combines several elements in a style closer to a real academic
project page. The project studies a generic optimization problem with the
following form:

\[
\min_{\mathbf{x} \in \mathcal{X}} \quad g(\mathbf{x}) + h(\mathbf{x}).
\]

Main points:

1. The problem statement is introduced in ordinary prose.
2. Important terms can be emphasized using **bold** or *italic* text.
3. Supporting files can be linked as [PDF files](pdf/engg5781/lecture-0-course-info.pdf).

Related resources:

- [Internal research page](/research/)
- [External documentation](https://gohugo.io/)
- `content/research/software/test.md`

## Long Content Stress Test

This paragraph is intentionally long. It helps test whether the prose width,
line height, and link wrapping remain comfortable when the content resembles a
real academic homepage with dense information. A long link such as
[https://example.com/research/projects/a-very-long-project-name-with-many-path-segments-and-query-parameters](https://example.com/research/projects/a-very-long-project-name-with-many-path-segments-and-query-parameters)
should wrap without breaking the page layout.
