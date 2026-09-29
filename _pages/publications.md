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
  /* 국문 핵심 요약(문제·방법·효과) */
  .pub-summary {
    margin: 0.4rem 0 0.2rem;
    padding: 0.5rem 0.75rem;
    border-left: 3px solid var(--global-theme-color);
    background-color: var(--global-code-bg-color);
    font-size: 0.85rem;
    line-height: 1.55;
  }
  /* 라벨 열 + 문장 열: 줄바꿈돼도 문장이 같은 세로선에서 시작 */
  .pub-summary p {
    display: grid;
    grid-template-columns: 2.4rem 1fr;
    column-gap: 0.5rem;
    margin: 0.2rem 0;
  }
  .pub-summary-label {
    font-weight: 600;
    color: var(--global-theme-color);
  }
</style>

<!-- Bibsearch Feature -->

{% include bib_search.liquid %}

## Journal · 저널 (1)

<div class="publications">
{% bibliography --query @article %}
</div>

## Conference Presentations · 학회 발표 (6)

<div class="publications">
{% bibliography --query @inproceedings %}
</div>
