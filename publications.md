---
layout: default
title: Publications
permalink: /publications/
---

<p class="page-intro">
  A complete list of my publications is organized by year below. Selected works are highlighted on the homepage.
</p>

{% assign publication_years = site.data.publications | map: "year" | uniq %}

{% for year in publication_years %}
<section class="pub-year-section">
  <h2 class="pub-year">{{ year }}</h2>
  <div class="pub-list">
  {% for pub in site.data.publications %}
    {% if pub.year == year %}
    {% include publication-item.html pub=pub %}
    {% endif %}
  {% endfor %}
  </div>
</section>
{% endfor %}
