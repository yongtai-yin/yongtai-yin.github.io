---
layout: default
layout_type: home
title: Yongtai Yin - Home
name: Yongtai Yin
avatar: /assets/img/avatar.jpg
bio_role: Ph.D. Student
bio_school: University of XXX
email: san.zhang [at] university.edu
socials:
  - name: Google Scholar
    url: "#"
  - name: GitHub
    url: "#"
  - name: Twitter
    url: "#"
---

## About Me

I am a first-year Ph.D. student at the University of XXX, advised by Prof. YYY. My research interests include **Computer Vision**, **Machine Learning**, and **AI for Sustainability**.

## News

<table class="news-table">
    <tr>
        <td class="news-date">Jan 2026</td>
        <td class="news-text">One paper accepted to <strong>CVPR 2026</strong>!</td>
    </tr>
    <tr>
        <td class="news-date">Sep 2025</td>
        <td class="news-text">Joined University of XXX.</td>
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