---
layout: page
title: Projects
permalink: /projects/
description: 진행 중이거나 대표할 만한 연구·개발 프로젝트.
nav: true
nav_order: 3
display_categories: [research]
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
</style>
<div class="projects">
{% if site.enable_project_categories and page.display_categories %}
  <!-- Display categorized projects -->
  {% for category in page.display_categories %}
  <a id="{{ category }}" href=".#{{ category }}">
    <h2 class="category">{{ category }}</h2>
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
  <div class="row row-cols-1 row-cols-md-3">
    {% for project in sorted_projects %}
      {% include projects.liquid %}
    {% endfor %}
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
