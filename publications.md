---
layout: default
title: Publications
permalink: /publications/
---

<div class="pub-list">
{% for pub in site.data.publications %}
  <div class="pub-item">
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
{% endfor %}
</div>