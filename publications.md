---
layout: default
title: Publications
permalink: /publications/
---

<div class="pub-list">
{% for pub in site.data.publications %}
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
          {% if pub.pdf %} <a href="{{ pub.pdf }}">PDF</a> {% endif %}
          {% if pub.code %} <a href="{{ pub.code }}">Code</a> {% endif %}
          {% if pub.project %} <a href="{{ pub.project }}">Project</a> {% endif %}
          {% if pub.bibtex %} <a href="{{ pub.bibtex }}">BibTeX</a> {% endif %}
      </div>
    </div>
  </div>
{% endfor %}
</div>