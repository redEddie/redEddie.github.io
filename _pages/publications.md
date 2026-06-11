---
layout: page
permalink: /publications/
title: Publications
description: 저널 논문 및 학회 발표.
nav: true
nav_order: 2
---

<!-- _pages/publications.md -->

<style>
  .publications h2.bibliography { color: var(--global-text-color); }
</style>

<!-- Bibsearch Feature -->

{% include bib_search.liquid %}

## Journal · 저널 (1, 투고 / Submitted)

<div class="publications">
{% bibliography --query @article %}
</div>

## Conference Presentations · 학회 발표 (6)

<div class="publications">
{% bibliography --query @inproceedings %}
</div>
