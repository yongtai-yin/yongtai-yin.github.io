---
layout: default
title: Publications
permalink: /publications/
---

<div class="pub-list">
{% for pub in site.data.publications %}
  {% include publication-item.html pub=pub %}
{% endfor %}
</div>
