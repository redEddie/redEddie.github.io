---
layout: page
title: Projects
permalink: /projects/
description: 진행 중이거나 대표할 만한 연구·개발 프로젝트와 수업 프로젝트.
nav: true
nav_order: 3
display_categories: [research, coursework]
horizontal: false
---

<!-- pages/projects.md -->
<style>
  .project-tags { margin-top: 0.5rem; display: flex; flex-wrap: wrap; gap: 0.35rem; }
  .project-tag {
    display: inline-block;
    font-size: 0.7rem;
    line-height: 1;
    padding: 0.3rem 0.5rem;
    border-radius: 1rem;
    color: var(--global-theme-color);
    border: 1px solid var(--global-theme-color);
    background-color: transparent;
    white-space: nowrap;
  }
  .card:hover .project-tag { background-color: var(--global-theme-color); color: var(--global-card-bg-color); }
  .projects h2.category { color: var(--global-text-color); }
  /* 카드 썸네일: 16:9 고정, 이미지 없으면 빈 영역 */
  .project-thumb {
    aspect-ratio: 16 / 9;
    overflow: hidden;
    background-color: var(--global-divider-color);
    border-top-left-radius: inherit;
    border-top-right-radius: inherit;
  }
  .project-thumb figure, .project-thumb picture { margin: 0; width: 100%; height: 100%; display: block; }
  .project-thumb img { width: 100%; height: 100%; object-fit: cover; }
  /* 더보기: 접힌 카드는 순서를 유지한 채 숨김 */
  .project-group .project-more { display: none; }
  .project-group.show-all .project-more { display: block; }
  .project-more-toggle {
    display: block;
    margin: 0.75rem auto 2rem;
    padding: 0.4rem 1.2rem;
    font-size: 0.85rem;
    color: var(--global-theme-color);
    background: transparent;
    border: 1px solid var(--global-theme-color);
    border-radius: 1rem;
    cursor: pointer;
  }
  .project-more-toggle:hover { background-color: var(--global-theme-color); color: var(--global-card-bg-color); }
</style>
<div class="projects">
{% if site.enable_project_categories and page.display_categories %}
  <!-- Display categorized projects -->
  {% for category in page.display_categories %}
  <a id="{{ category }}" href=".#{{ category }}">
    <h2 class="category">{{ category | capitalize }}</h2>
  </a>
  {% assign categorized_projects = site.projects | where: "category", category %}
  {% assign sorted_projects = categorized_projects | sort: "importance" %}
  <!-- Generate cards for each project -->
  {% if page.horizontal %}
  <div class="container">
    <div class="row row-cols-1 row-cols-md-2">
    {% for project in sorted_projects %}
      {% include projects_horizontal.liquid %}
    {% endfor %}
    </div>
  </div>
  {% else %}
  <div class="project-group">
  <div class="row row-cols-1 row-cols-md-3">
    {% for project in sorted_projects %}
      {% include projects.liquid %}
    {% endfor %}
  </div>
  {% assign collapsed_projects = categorized_projects | where: "collapsed", true %}
  {% if collapsed_projects.size > 0 %}
  <button type="button" class="btn btn-sm btn-outline-secondary project-more-toggle"
    onclick="var g=this.closest('.project-group');g.classList.toggle('show-all');this.textContent=g.classList.contains('show-all')?'접기':'더보기 ({{ collapsed_projects.size }})';">더보기 ({{ collapsed_projects.size }})</button>
  {% endif %}
  </div>
  {% endif %}
  {% endfor %}

{% else %}

<!-- Display projects without categories -->

{% assign sorted_projects = site.projects | sort: "importance" %}

  <!-- Generate cards for each project -->

{% if page.horizontal %}

  <div class="container">
    <div class="row row-cols-1 row-cols-md-2">
    {% for project in sorted_projects %}
      {% include projects_horizontal.liquid %}
    {% endfor %}
    </div>
  </div>
  {% else %}
  <div class="row row-cols-1 row-cols-md-3">
    {% for project in sorted_projects %}
      {% include projects.liquid %}
    {% endfor %}
  </div>
  {% endif %}
{% endif %}
</div>
