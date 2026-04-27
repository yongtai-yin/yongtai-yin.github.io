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
    url: "https://scholar.google.com/citations?user=2-HlzyEAAAAJ&hl"
    icon: ai ai-google-scholar
  - name: GitHub
    url: "https://github.com/yongtai-yin"
    icon: fab fa-github
  - name: Linkedin
    url: "https://www.linkedin.com/in/yongtai-yin"
    icon: fab fa-linkedin
---

## About Me

Hello! My name is YIN, Yongtai (殷永泰). I am currently a Ph.D. student at the [DSP & Speech Technology Laboratory](http://dsp.ee.cuhk.edu.hk) in the Department of Electronic Engineering at [The Chinese University of Hong Kong](https://www.cuhk.edu.hk) (CUHK), under the supervision of [Prof. Wing-Kin Ma](https://www.ee.cuhk.edu.hk/~wkma/).

Prior to this, I obtained my B.Eng. and M.Eng. degrees in Communication Engineering from [Northwestern Polytechnical University](https://en.nwpu.edu.cn/) (NWPU) in 2021 and 2024, respectively.

## Research Interests

- Optimization for Signal Processing
- Model-Based Deep Learning
- Generative Models
- Wireless Sensing

## News

{% include news-list.html %}

## Selected Publications

<div class="pub-list">
{% for pub in site.data.publications %}
  {% if pub.selected %}
  {% include publication-item.html pub=pub %}
  {% endif %}
{% endfor %}
</div>
