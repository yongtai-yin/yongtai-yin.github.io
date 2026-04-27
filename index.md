---
layout: default
layout_type: home
title: Yongtai Yin
header_name: Yongtai Yin
avatar: /assets/img/avatar.png
position: Ph.D. Student in Electronic Engineering
affiliation: The Chinese University of Hong Kong
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

I am a Ph.D. student in the Department of Electronic Engineering at [The Chinese University of Hong Kong](https://www.cuhk.edu.hk) (CUHK), advised by [Prof. Wing-Kin Ma](https://www.ee.cuhk.edu.hk/~wkma/). I am a member of the [DSP & Speech Technology Laboratory](http://dsp.ee.cuhk.edu.hk).

Before joining CUHK, I received my B.Eng. and M.Eng. degrees in Communication Engineering from [Northwestern Polytechnical University](https://en.nwpu.edu.cn/) (NWPU) in 2021 and 2024, respectively.

## Research Interests

- Optimization and nonconvex methods for signal processing
- Model-based deep learning and generative modeling
- Wireless sensing, localization, and array signal processing

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

<p class="section-more">
  <a href="{{ '/publications/' | relative_url }}">View all publications</a>
</p>
