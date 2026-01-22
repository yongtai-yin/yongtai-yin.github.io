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
          {% if pub.pdf %} <a href="{{ pub.pdf }}"><i class="far fa-file-pdf"></i> PDF</a> {% endif %}
          {% if pub.code %} <a href="{{ pub.code }}"><i class="fab fa-github"></i> Code</a> {% endif %}
          {% if pub.project %} <a href="{{ pub.project }}"><i class="fas fa-globe"></i> Project</a> {% endif %}
          {% if pub.bibtex %} <a href="{{ pub.bibtex }}"><i class="fas fa-quote-right"></i> BibTeX</a> {% endif %}
          {% if pub.data %} <a href="{{ pub.data }}"><i class="fas fa-database"></i> Data</a> {% endif %}
      </div>
    </div>
  </div>
{% endfor %}
</div>