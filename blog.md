---
layout: default
title: Blog
permalink: /blog/
blog_filter: true
---

<div class="blog-tags">
  <button class="filter-tag active" data-tag="all">All</button>
  {% assign sorted_tags = site.tags | sort %}
  {% for tag in sorted_tags %}
    <button class="filter-tag" data-tag="{{ tag[0] }}">{{ tag[0] }}</button>
  {% endfor %}
</div>

<div class="post-list">
{% for post in site.posts %}
  <article class="post-item" data-tags="{{ post.tags | join: ',' }}">
    <h3 class="post-title"><a href="{{ post.url | relative_url }}">{{ post.title }}</a></h3>
    <div class="post-meta">
        {{ post.date | date: "%B %d, %Y" }}
        {% if post.tags.size > 0 %}
        <span class="post-tags">
            <i class="fas fa-tag"></i>
            {{ post.tags | join: ', ' }}
        </span>
        {% endif %}
    </div>
    <div>{{ post.excerpt }}</div>
  </article>
{% endfor %}
</div>
