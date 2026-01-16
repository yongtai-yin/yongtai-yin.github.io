---
layout: default
layout_type: home
title: Yongtai Yin
name: Yongtai Yin
avatar: /assets/img/avatar.jpg
bio_role: Ph.D. Student
bio_school: The Chinese University of Hong Kong
email: ytyin [at] link.cuhk.edu.hk
socials:
  - name: Google Scholar
    url: "#"
    icon: ai ai-google-scholar
  - name: GitHub
    url: "https://github.com/yongtai-yin"
    icon: fab fa-github
  - name: Linkedin
    url: "#"
    icon: fab fa-linkedin
---

## About Me

My name is YIN, Yongtai (殷永泰). I am currently a Ph.D. student at the [DSP & Speech Technology Laboratory](http://dsp.ee.cuhk.edu.hk) in the Department of Electronic Engineering at [The Chinese University of Hong Kong](https://www.cuhk.edu.hk) (CUHK), under the supervision of [Prof. Wing-Kin Ma](https://scholar.google.com/citations?user=zSjjF_UAAAAJ&hl).

Prior to this, I obtained my B.Eng. and M.Eng. degrees in Communication Engineering from [Northwestern Polytechnical University](https://en.nwpu.edu.cn/) (NWPU) in 2021 and 2024, respectively.

## Research Interests

Optimization for Signal Processing, Deep Learning (Generative Models), Wireless Sensing

## News

<table class="news-table">
    <tr>
        <td class="news-date">Oct 2024</td>
        <td class="news-text">My master's thesis was selected as the `Outstanding Master's Thesis` of [NWPU](https://en.nwpu.edu.cn/) 2024.</td>
    </tr>
    <tr>
        <td class="news-date">Aug 2024</td>
        <td class="news-text">I commenced my doctoral studies in the Department of Electronic Engineering at [CUHK](https://www.cuhk.edu.hk) !</td>
    </tr>
</table>

## Selected Publications

<div class="pub-list">
{% for pub in site.data.publications %}
  {% if pub.selected %}
  <div class="pub-item">
      <span class="pub-title">{{ pub.title }}</span>
      <div class="pub-authors">{{ pub.authors }}</div>
      <div class="pub-venue">{{ pub.venue }}</div>
      <div class="pub-links">
          {% if pub.pdf %} <a href="{{ pub.pdf }}">PDF</a> {% endif %}
          {% if pub.code %} <a href="{{ pub.code }}">Code</a> {% endif %}
          {% if pub.project %} <a href="{{ pub.project }}">Project</a> {% endif %}
      </div>
  </div>
  {% endif %}
{% endfor %}
</div>