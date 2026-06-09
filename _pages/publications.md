---
layout: page
permalink: /publications/
title: Publications
description: 저널 논문 및 학회 발표.
nav: true
nav_order: 2
---

<!-- _pages/publications.md -->

<!-- Bibsearch Feature -->

{% include bib_search.liquid %}

## Journal · 저널 (1, 투고·심사 중 / under review)

<div class="publications">
{% bibliography --query @article %}
</div>

## Conference Presentations · 학회 발표 (6)

<div class="publications">
{% bibliography --query @inproceedings %}
</div>
