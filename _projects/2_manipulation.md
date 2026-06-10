---
layout: page
title: 매니퓰레이션 프로젝트
description: 시뮬레이션 검증 · 실물 SO-101 데이터 수집 · UMI 기반 데이터셋 확보
importance: 2
category: research
tags: [VLA, Imitation Learning, UMI, Real-robot Deploy]
related_publications: false
---

<style>
  .manip-vid {
    max-height: 300px;
    width: auto !important;
    margin: 0 auto;
    display: block;
  }
</style>

학위논문에서 설계한 VLA 모델을 실환경으로 확장하는 트랙입니다. 시뮬레이션 검증에서 출발해, 실물 로봇 데이터 수집을 거치며 **데이터 확보**가 핵심 병목임을 체감했고, 이를 UMI 방식으로 푸는 방향으로 이어지고 있습니다. (진행 중)

## 시뮬레이션 검증 — lehome

deformable object를 다루는 lehome 작업을 시뮬레이션에서 수행한 정성적 데모입니다.

<div class="row">
  <div class="col-md mt-3 mt-md-0">
    {% include video.liquid path="assets/projects/manipulation/demo-lehome-top-short.mp4" class="img-fluid rounded z-depth-1 manip-vid" controls=true autoplay=true loop=true muted=true %}
  </div>
  <div class="col-md mt-3 mt-md-0">
    {% include video.liquid path="assets/projects/manipulation/demo-lehome-top-long.mp4" class="img-fluid rounded z-depth-1 manip-vid" controls=true autoplay=true loop=true muted=true %}
  </div>
</div>
<div class="row mt-3">
  <div class="col-md mt-3 mt-md-0">
    {% include video.liquid path="assets/projects/manipulation/demo-lehome-pant-short.mp4" class="img-fluid rounded z-depth-1 manip-vid" controls=true autoplay=true loop=true muted=true %}
  </div>
  <div class="col-md mt-3 mt-md-0">
    {% include video.liquid path="assets/projects/manipulation/demo-lehome-pant-long.mp4" class="img-fluid rounded z-depth-1 manip-vid" controls=true autoplay=true loop=true muted=true %}
  </div>
</div>

## 실물 데이터 수집 — SO-101

실물 **SO-101** 팔로 boat **pick-and-place** 작업의 데이터를 수집했습니다. 같은 에피소드를 상단(top)·손목(wrist) 두 시점에서 기록합니다.

<div class="row">
  <div class="col-md mt-3 mt-md-0">
    {% include video.liquid path="assets/projects/manipulation/so101-boat-top.mp4" class="img-fluid rounded z-depth-1 manip-vid" controls=true autoplay=true loop=true muted=true %}
  </div>
  <div class="col-md mt-3 mt-md-0">
    {% include video.liquid path="assets/projects/manipulation/so101-boat-wrist.mp4" class="img-fluid rounded z-depth-1 manip-vid" controls=true autoplay=true loop=true muted=true %}
  </div>
</div>

직접 해보니 실물 데이터 수집은 시간·노동 비용이 매우 크다는 것을 체감했습니다.

## 다음 목표 — UMI 기반 데이터 수집

데이터 수집의 어려움을 풀기 위해, **UMI** 방식으로 데이터셋을 효율적으로 모아 자체 VLA 모델을 구동하는 것이 자연스러운 다음 목표입니다.

**로봇 / 키워드**: UMI · SO-ARM(SO-101) · Franka Research 3
