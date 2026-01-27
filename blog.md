---
layout: default
title: Blog
permalink: /blog/
---

<!-- Tag Filter Section -->
<div class="blog-tags">
  <button class="filter-tag active" data-tag="all">All</button>
  {% assign sorted_tags = site.tags | sort %}
  {% for tag in sorted_tags %}
    <button class="filter-tag" data-tag="{{ tag[0] }}">{{ tag[0] }}</button>
  {% endfor %}
</div>

<div class="post-list">
{% for post in site.posts %}
  <div class="post-item" data-tags="{{ post.tags | join: ',' }}" style="margin-bottom: 2rem;">
    <h3 style="margin-bottom: 0.5rem;"><a href="{{ post.url | relative_url }}">{{ post.title }}</a></h3>
    <div style="color: #666; font-size: 0.9rem; margin-bottom: 0.5rem;">
        {{ post.date | date: "%B %d, %Y" }}
        {% if post.tags.size > 0 %}
        <span style="margin-left: 10px; font-size: 0.85em; opacity: 0.8;">
            <i class="fas fa-tag" style="margin-right: 4px;"></i>
            {{ post.tags | join: ', ' }}
        </span>
        {% endif %}
    </div>
    <div>{{ post.excerpt }}</div>
  </div>
{% endfor %}
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
    const filterButtons = document.querySelectorAll('.filter-tag');
    const posts = document.querySelectorAll('.post-item');

    filterButtons.forEach(button => {
        button.addEventListener('click', () => {
            // Remove active class from all buttons
            filterButtons.forEach(btn => btn.classList.remove('active'));
            // Add active class to clicked button
            button.classList.add('active');

            const selectedTag = button.getAttribute('data-tag');

            posts.forEach(post => {
                const postTags = post.getAttribute('data-tags').split(',');
                if (selectedTag === 'all' || postTags.includes(selectedTag)) {
                    post.classList.remove('hidden');
                } else {
                    post.classList.add('hidden');
                }
            });
        });
    });
});
</script>