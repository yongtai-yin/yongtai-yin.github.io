---
layout: default
layout_type: home
title: Yongtai Yin
header_name: Yongtai Yin
avatar: /assets/img/avatar.png
bio: |
  Ph.D. Student, Electronic Engineering<br>
  The Chinese University of Hong Kong
email: ytyin [at] link.cuhk.edu.hk
socials:
  - name: Google Scholar
    url: "#"
    icon: ai ai-google-scholar
  - name: GitHub
    url: "https://github.com/yongtai-yin"
    icon: fab fa-github
  - name: Linkedin
    url: "https://www.linkedin.com/in/yongtai-yin"
    icon: fab fa-linkedin
---

## About Me

Hello! My name is YIN, Yongtai (殷永泰). I am currently a Ph.D. student at the [DSP & Speech Technology Laboratory](http://dsp.ee.cuhk.edu.hk) in the Department of Electronic Engineering at [The Chinese University of Hong Kong](https://www.cuhk.edu.hk) (CUHK), under the supervision of [Prof. Wing-Kin Ma](https://scholar.google.com/citations?user=zSjjF_UAAAAJ&hl).

Prior to this, I obtained my B.Eng. and M.Eng. degrees in Communication Engineering from [Northwestern Polytechnical University](https://en.nwpu.edu.cn/) (NWPU) in 2021 and 2024, respectively.

## Research Interests

- Optimization for Signal Processing
- Model-Based Deep Learning
- Generative Models
- Wireless Sensing

## News

<table class="news-table">
{% for news in site.data.news %}
    <tr>
        <td class="news-date">{{ news.date }}</td>
        <td class="news-text">{{ news.content | markdownify }}</td>
    </tr>
{% endfor %}
</table>

## Selected Publications

<div class="pub-list">
{% for pub in site.data.publications %}
  {% if pub.selected %}
  <div class="pub-item">
    <div class="pub-img-col">
        {% if pub.short_venue %}
        <span class="pub-abbr">{{ pub.short_venue }}</span>
        {% endif %}
        {% if pub.image %}
        <img src="{{ pub.image }}" class="pub-img" alt="{{ pub.title }}">
        {% endif %}
    </div>
    <div class="pub-content-col">
      <span class="pub-title">{{ pub.title }}</span>
      <div class="pub-authors">{{ pub.authors }}</div>
      <div class="pub-venue">{{ pub.venue }}</div>
      <div class="pub-links">
          {% if pub.pdf %} <a href="{{ pub.pdf }}"><i class="far fa-file-pdf"></i> PDF</a> {% endif %}
          {% if pub.code %} <a href="{{ pub.code }}"><i class="fab fa-github"></i> Code</a> {% endif %}
          {% if pub.project %} <a href="{{ pub.project }}"><i class="fas fa-globe"></i> Project</a> {% endif %}
          {% if pub.bibtex %} <a href="{{ pub.bibtex }}"><i class="fas fa-quote-right"></i> BibTeX</a> {% endif %}
          {% if pub.data %} <a href="{{ pub.data }}"><i class="fas fa-database"></i> Data</a> {% endif %}
      </div>
    </div>
  </div>
  {% endif %}
{% endfor %}
</div>