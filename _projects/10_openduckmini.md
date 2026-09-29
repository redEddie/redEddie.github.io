---
layout: page
title: Open Duck Mini — 저비용 이족보행 로봇
description: 오픈소스 이족보행 로봇 재현 — AMP 스타일 로코모션 학습과 실물 구현, 저가 모터의 한계 분석 · 2026.06
img: assets/projects/openduckmini/cover.jpg
importance: 4
category: research
tags: [Bipedal Locomotion, Reinforcement Learning, AMP, Sim-to-Real, IMU, Feetech]
related_publications: false
---

<style>
  .duck-vid {
    max-height: 360px;
    width: auto !important;
    margin: 0 auto;
    display: block;
  }
  .duck-vid-lg {
    max-height: 470px;
    width: auto !important;
    margin: 0 auto;
    display: block;
  }
  .duck-pair-img {
    max-height: 300px;
    width: auto !important;
    margin: 0 auto;
    display: block;
  }
</style>

3D 프린팅 부품과 Feetech 저가 서보모터만으로 집에서도 만들 수 있는 오픈소스 이족보행 로봇 [Open Duck Mini](https://github.com/apirrone/Open_Duck_Mini)를 직접 조립하고 걷게 해본 개인 프로젝트입니다. 강화학습으로 학습한 로코모션을 실물 로봇으로 옮기는 전 과정을 경험하는 것이 목표였습니다. 이 프로젝트를 크게 두 부분으로 나누어 분석했습니다 — **(1)** `placo`로 레퍼런스 모션을 생성해 AMP 스타일로 로코모션을 학습시키는 부분, **(2)** 학습된 정책을 실제 로봇에 올려 센서–연산–구동을 잇는 부분입니다.

## 만든 로봇

상용 연구용 플랫폼과 달리 부품 대부분을 직접 출력하고 저가 모터로 구동하는 구조라, 적은 비용으로 이족보행 로봇의 전 과정을 다뤄볼 수 있었습니다.

<div class="row justify-content-center align-items-center">
  <div class="col-md-5 mt-3 mt-md-0">
    {% include figure.liquid loading="eager" path="assets/projects/openduckmini/build-hardware.jpg" title="Assembled Open Duck Mini" class="img-fluid rounded z-depth-1 duck-pair-img" zoomable=true %}
  </div>
  <div class="col-md-6 mt-3 mt-md-0">
    {% include figure.liquid loading="eager" path="assets/projects/openduckmini/duck-render.png" title="Simulation model" class="img-fluid rounded z-depth-1 duck-pair-img" zoomable=true %}
  </div>
</div>
<div class="caption">좌: 직접 조립한 실물 로봇 — 주황색 3D 프린팅 섀시, Feetech 서보모터와 배선 / 우: 학습·검증에 사용한 시뮬레이션 모델</div>

## AMP 스타일 로코모션 학습 — 레퍼런스 모션을 보상으로

보행 동작을 보상 함수로 일일이 설계(reward engineering)하는 대신, **참고할 만한 움직임(reference motion)을 미리 만들어 강화학습의 추가 보상 항으로 제공하는** AMP 스타일 접근을 따랐습니다. 레퍼런스 모션은 `placo`로 이차계획(QP) 문제를 풀어 생성합니다 — 보행 주기에 맞춰 다리 관절 궤적과 발 접촉(contact)이 주기적으로 반복되는 기준 동작을 어렵지 않게 얻을 수 있었습니다.

<div class="row justify-content-center">
  <div class="col-md-9 mt-3">
    {% include figure.liquid loading="eager" path="assets/projects/openduckmini/ref-motion-periodic.png" title="Generated reference motion" class="img-fluid rounded z-depth-1" zoomable=true %}
  </div>
</div>
<div class="caption">`placo`로 생성한 보행 레퍼런스 — 위: 다리 관절 궤적, 아래: 좌·우 발 접촉이 주기적으로 번갈아 나타나는 걸음새</div>

복잡한 보상 설계 없이도, 이렇게 만든 레퍼런스에 스타일을 맞추도록 학습시키는 것만으로 자연스러운 걸음을 얻을 수 있다는 점이 인상적이었습니다. 아래는 프로젝트에서 제공하는 학습 체크포인트를 시뮬레이터에서 재생한 모습입니다.

<div class="row justify-content-center">
  <div class="col-md mt-3 mt-md-0">
    {% include video.liquid path="assets/projects/openduckmini/checkpoint-walk.mp4" class="img-fluid rounded z-depth-1 duck-vid" controls=true autoplay=true loop=true muted=true %}
  </div>
</div>
<div class="caption">프로젝트 제공 체크포인트의 시뮬레이터 보행 — 학습된 정책이 레퍼런스 걸음새를 따라간다</div>

## 모터를 더 사실적으로 — 백래시·입력 전압 모델링

이 로봇의 원본인 디즈니 BDX 논문은, 저가 모터의 미세한 **백래시(backlash)**를 모사하기 위해 모터마다 가상 모터를 덧붙여 ±0.5°의 유격을 모델링하고 그 모터 모델 위에서 정책을 학습합니다. 직접 비교해 봤지만, 백래시의 영향은 시뮬레이터에서도 실제 로봇에서도 뚜렷하게 확인하기 어려웠습니다.

<div class="row justify-content-center">
  <div class="col-md-10 mt-3">
    {% include video.liquid path="assets/projects/openduckmini/backlash-compare.mp4" class="img-fluid rounded z-depth-1" controls=true autoplay=true loop=true muted=true %}
  </div>
</div>
<div class="caption">±0.5° 백래시 모터 모델 유무 비교 — 시뮬레이터·실물 모두에서 영향을 뚜렷이 확인하긴 어려웠다</div>

반면 **입력 전압에 따른 최대 토크 차이**는 시뮬레이터와 실제 로봇 양쪽에서 분명하게 관측되었습니다. 5V와 7.4V를 비교하면 모터가 낼 수 있는 토크가 달라지고, 그 차이가 보행 거동으로 이어졌습니다. BAM 액추에이터 모델 덕분에 **전압과 토크의 상관관계를 직접 확인**할 수 있었던 점이 이 부분의 수확입니다.

<div class="row justify-content-center">
  <div class="col-md-10 mt-3">
    {% include video.liquid path="assets/projects/openduckmini/motor-voltage-compare.mp4" class="img-fluid rounded z-depth-1" controls=true autoplay=true loop=true muted=true %}
  </div>
</div>
<div class="caption">입력 전압에 따른 모터 거동 시뮬레이션 — 5V(좌) vs 7.4V(우), 전압이 높을수록 낼 수 있는 최대 토크가 커진다</div>

## 나만의 변주 — 점프하는 레퍼런스

기본 보행을 넘어, 직접 변주를 시도했습니다. 두 발이 동시에 지면을 떠나는 **비행 구간(flight phase)**을 갖는 점프 레퍼런스를 만들어, QP 기반 레퍼런스 생성이 어디까지 가능한지 확인해 보았습니다.

<div class="row justify-content-center">
  <div class="col-md-9 mt-3">
    {% include figure.liquid loading="eager" path="assets/projects/openduckmini/ref-motion-hop.png" title="Hop reference motion" class="img-fluid rounded z-depth-1" zoomable=true %}
  </div>
</div>
<div class="caption">직접 생성한 점프 레퍼런스 — 좌·우 발 접촉이 동시에 0이 되는 비행 구간(분홍 음영)과 이륙(vz>0)·착지(vz<0) 수직 속도가 나타난다</div>

<div class="row">
  <div class="col-md mt-3 mt-md-0">
    {% include video.liquid path="assets/projects/openduckmini/hop-fwd-reference.mp4" class="img-fluid rounded z-depth-1 duck-vid" controls=true autoplay=true loop=true muted=true %}
  </div>
  <div class="col-md mt-3 mt-md-0">
    {% include video.liquid path="assets/projects/openduckmini/hop-fwd-trained.mp4" class="img-fluid rounded z-depth-1 duck-vid" controls=true autoplay=true loop=true muted=true %}
  </div>
</div>
<div class="caption">좌: 직접 만든 전진 점프 레퍼런스 / 우: 이를 학습한 정책</div>

다만 직접 만든 점프 레퍼런스가 물리 법칙을 온전히 만족하는 모션으로 생성된 것은 아니었습니다. 그 문제를 차치하더라도, 모터 출력의 한계 탓에 **시뮬레이터에서조차 유의미한 점프를 학습하지는 못했습니다.** 그럼에도 간단한 이차계획 문제를 푸는 것만으로 원하는 레퍼런스 모션을 만들고, 그 스타일을 강화학습에 입힐 수 있다는 점을 직접 확인한 것은 좋은 공부였습니다.

## 실물 로봇 구현과 한계

학습한 정책을 실제 로봇에 올렸습니다. IMU와 모터 회전 위치를 읽어 관측을 구성하고, 정책 연산을 거쳐 **50Hz로 모터에 목표 명령**을 보내는 흐름까지는 이해하고 동작시킬 수 있었습니다. 그러나 로봇은 제대로 걷지 못하고 넘어졌습니다.

<div class="row justify-content-center">
  <div class="col-md-8 mt-3">
    {% include video.liquid path="assets/projects/openduckmini/real-walk-attempt.mp4" class="img-fluid rounded z-depth-1 duck-vid-lg" controls=true autoplay=true loop=true muted=true %}
  </div>
</div>
<div class="caption">실물 로봇의 보행 시도 — 연산된 명령만큼 움직이지 못하고 균형을 잃는다</div>

원인을 살펴본 결과, **모터가 연산된 명령보다 덜 움직여** 발생한 현상으로 추론했습니다. 흥미롭게도, 같은 BOM과 전압을 쓰더라도 사용자마다 결과가 천차만별이었고, 저처럼 실패한 사례도 충분히 찾아볼 수 있었습니다. 저는 이를 잠정적으로 **저가 모터의 한계**로 결론지었습니다. Dynamixel처럼 연구용으로 안정적으로 검증된 모터와 달리, 저렴함을 앞세워 빠르게 보급된 저가 모터는 기능 자체의 한계뿐 아니라 개체 편차도 있는 것이 아닌가 의심하고 있습니다. 실제로 같은 문제를 겪는 다른 사용자가 있는지 [프로젝트 이슈로 남겨](https://github.com/apirrone/Open_Duck_Mini/issues/48) 일부 사용자도 공유하는 문제임을 확인했습니다. 제 경우에는 다른 사용자보다도 모터가 더 좁은 범위로만 움직이고, 의도된 속도보다 현저히 느렸습니다.

## IMU의 역할 — 보행과 균형

이 프로젝트를 따라 하며 가장 분명하게 배운 것은 **IMU가 보행·균형에 미치는 영향**입니다. 관측에서 IMU 입력(가속도·각속도)을 제거하자, 시뮬레이터에서조차 제대로 걷지 못하고 제자리걸음에 그치는 식으로만 학습되었습니다.

<div class="row justify-content-center">
  <div class="col-md-6 mt-3">
    {% include video.liquid path="assets/projects/openduckmini/noimu-march.mp4" class="img-fluid rounded z-depth-1 duck-vid" controls=true autoplay=true loop=true muted=true %}
  </div>
</div>
<div class="caption">IMU 입력(가속도·각속도)을 제거한 경우 — 시뮬레이터에서도 전진하지 못하고 제자리걸음에 머문다</div>

## 배운 점과 앞으로의 연구

비용 부담 없이 이족보행 로봇의 전 과정 — 레퍼런스 생성, 강화학습, 실물 이식 — 을 직접 다뤄볼 수 있는 매우 흥미로운 프로젝트였습니다. AMP 스타일 학습으로 보상 설계 부담을 줄이는 법, IMU가 보행·균형에 갖는 비중을 몸으로 이해할 수 있었습니다.

동시에 한계도 분명했습니다. ±0.5° 백래시 모델링의 효과는 시뮬레이터·실물 모두에서 뚜렷하지 않았던 반면, BAM으로 입력 전압과 최대 토크의 상관관계는 분명히 확인할 수 있었습니다. 그럼에도 무엇보다 저가 모터는 의도된 가동 범위·속도를 내지 못한다는 근본적 제약이 있었습니다.

이 경험을 토대로, 앞으로는 **Feetech 저가 모터의 한정된 성능이 보행에 어떤 영향을 미치는지**를 모터 모델 관점에서 파고들어 보려 합니다. 토크·속도가 왜 부족했는지, 균형을 잡기 위해 필요한 새로운 자세를 모터가 충분히 만들어내지 못한 것인지 — 모터 모델을 제대로 공부하면 이번에 잠정적으로 내린 결론을 정량적으로 확인할 수 있을 것으로 기대합니다.
