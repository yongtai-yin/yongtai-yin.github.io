---
layout: default
title: Blog
permalink: /blog/
---

<div class="post-list">
{% for post in site.posts %}
  <div class="post-item" style="margin-bottom: 2rem;">
    <h3 style="margin-bottom: 0.5rem;"><a href="{{ post.url | relative_url }}">{{ post.title }}</a></h3>
    <div style="color: #666; font-size: 0.9rem; margin-bottom: 0.5rem;">{{ post.date | date: "%B %d, %Y" }}</div>
    <div>{{ post.excerpt }}</div>
  </div>
{% endfor %}
</div>
