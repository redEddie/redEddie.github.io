---
layout: page
title: 석사 학위논문 — Selective SSM 기반 모방학습
description: Selective State Space Model-based Efficient Imitation Learning for Generalizable Robot Manipulation · 2026년 8월
img: assets/projects/thesis/fig-overall.png
importance: 1
category: research
tags: [VLA, Mamba2, Attention, Self-supervised, PyTorch]
related_publications: false
---

<style>
  /* 그림은 가로세로 비율 유지하면서 높이만 제한 */
  .thesis-fig {
    max-height: 340px;
    width: auto !important;
    margin: 0 auto;
    display: block;
  }
  .thesis-fig-tall {
    max-height: 680px;
    width: auto !important;
    margin: 0 auto;
    display: block;
  }
  .thesis-vid {
    max-height: 240px;
    width: auto !important;
    margin: 0 auto;
    display: block;
  }
</style>

진행 중인 석사 학위논문 연구입니다.

> **Selective State Space Model-based Efficient Imitation Learning for Generalizable Robot Manipulation**

**Selective State Space Model(Mamba)이 실제 VLA에서 어디까지 가능한지 체계적으로 검증한 연구입니다.** 어텐션 기반 구조를 선형 복잡도의 Mamba로 재설계하고, 분포 밖(out-of-distribution) 일반화 벤치마크인 LIBERO-PRO에서 기존 공개 VLA와 비교했습니다.

## Key Contributions

- **Transformer 기반 VLA를 Selective SSM(Mamba) 구조로 재설계** — 어텐션의 이차(quadratic) 비용을 선형(linear) 복잡도로 대체
- **Bidirectional Mamba 기반 비전–언어–행동 모델 구성** — 1D 시퀀스 모델로 2D 시각 관측까지 처리
- **LIBERO-PRO Task perturbation에서 기존 공개 VLA 대비 우수한 일반화 성능 확인**
- **Self-supervised Learning의 기여도 분석** — 절제 실험(w/o SSL)으로 정량화

## 동기

Transformer 어텐션은 시퀀스 길이에 대해 이차(quadratic) 비용을 가집니다. 이를 선형(linear) 복잡도의 **Selective SSM(Mamba)** 으로 대체해도 기존 Transformer 기반 VLA에 필적하는 성능을 낼 수 있는지 검증하는 것이 목표입니다. 평가는 학습 분포 내(in-distribution)가 아니라, **분포 밖(out-of-distribution) 일반화**를 측정하는 **LIBERO-PRO**에서 수행합니다.

## 모델 구조

{% include figure.liquid path="assets/projects/thesis/fig-overall.png" class="img-fluid rounded z-depth-1 thesis-fig" zoomable=true caption="전체 아키텍처" %}

<div class="row">
  <div class="col-md mt-3 mt-md-0">
    {% include figure.liquid path="assets/projects/thesis/fig-mamba2.png" class="img-fluid rounded z-depth-1 thesis-fig" zoomable=true caption="Mamba2 블록" %}
  </div>
  <div class="col-md mt-3 mt-md-0">
    {% include figure.liquid path="assets/projects/thesis/fig-mamba-swiglu.png" class="img-fluid rounded z-depth-1 thesis-fig" zoomable=true caption="Mamba + SwiGLU" %}
  </div>
  <div class="col-md mt-3 mt-md-0">
    {% include figure.liquid path="assets/projects/thesis/fig-bimamba.png" class="img-fluid rounded z-depth-1 thesis-fig" zoomable=true caption="양방향 Mamba" %}
  </div>
</div>

## 구성 및 규모

사전학습된 인코더는 동결(frozen)하고, 양방향 비전 인코더 + 멀티모달 Mamba 인코더 + Mamba 정책 헤드를 직접 설계·학습했습니다.

- **비전 인코더**: DINOv3-B (frozen)
- **텍스트 인코더**: EmbeddingGemma (frozen)

경량 설계가 핵심입니다. 추론 시 유효 파라미터 기준:

| 구성 | 파라미터 |
|---|---:|
| 직접 설계·학습 (인코더 + 정책, 추론 유효) | ~188M |
| 비전 인코더 DINOv3-B (frozen) | 86M |
| 텍스트 인코더 EmbeddingGemma (frozen) | 300M |
| **전체 VLA 파이프라인** | **~574M** |

## Mamba는 2D 이미지를 이해하는가

1D 시퀀스 모델임에도, Mamba 백본이 2D 이미지의 공간 구조를 의미 있게 포착하는지 시각화로 확인합니다.

<!-- TODO(redEddie): vision-attention 그림은 최신 버전이 아님 — 최신 학습 결과로 교체 예정 (assets/projects/thesis/fig-vision-attention.png) -->
{% include figure.liquid path="assets/projects/thesis/fig-vision-attention.png" class="img-fluid rounded z-depth-1 thesis-fig" zoomable=true caption="Mamba 백본이 이미지에서 포착한 공간 구조 시각화" %}

## 결과

평가는 LIBERO 표준 프로토콜에 따라 작업당 **50 에피소드**로 측정해 편향을 줄이고 신뢰할 수 있는 성능을 얻었습니다. (SSL = self-supervised learning, 자기지도 학습을 뗀 것이 *w/o SSL* 절제 실험)

LIBERO에서 다른 VLA 모델과 비교했을 때 평균 성공률에서 경쟁력 있는 수준을 보입니다.

**LIBERO success rate (%) — task suite별**

| Method | Object | Spatial | Goal | LIBERO-10 | Average |
|---|---:|---:|---:|---:|---:|
| UniVLA | 96 | 97 | 95 | 93 | 95.25 |
| GLaD | 97 | 97 | 98 | 94 | 96.50 |
| OpenVLA | 99 | 98 | 98 | 93 | 97.00 |
| π₀ | 98 | 97 | 92 | 82 | 92.25 |
| **Ours (Full)** | **100** | 95 | 96 | **98** | **97.25** |
| Ours (w/o SSL) | 99 | 93 | 91 | 95 | 94.50 |

본 연구의 초점은 **out-of-distribution 일반화(LIBERO-PRO)** 입니다. LIBERO-PRO는 학습 때 보지 못한 4가지 교란을 **평가 시점에만** 적용합니다.

{% include figure.liquid path="assets/projects/thesis/fig-libero-pro.png" class="img-fluid rounded z-depth-1 thesis-fig-tall" zoomable=true caption="LIBERO-PRO의 4가지 교란 유형" %}

- **Obj**: 객체 외형 변경
- **Pos**: 초기 공간 배치 변경
- **Sem**: 지시문 패러프레이즈 (의미는 유지, 표현만 변경)
- **Task**: 목표 객체·요구 행동 자체 변경

특히 가장 까다로운 **Task 교란**에서 기존 모델 대비 뚜렷한 강점을 보입니다.

**LIBERO-PRO — Object**

| Method | Obj | Pos | Sem | Task |
|---|---:|---:|---:|---:|
| UniVLA | 82 | 4 | 97 | 0 |
| GLaD | 86 | 3 | 97 | 0 |
| OpenVLA | 98 | 0 | 98 | 0 |
| π₀ | 94 | 0 | 90 | 0 |
| **Ours (Full)** | 92 | 0 | **100** | **10** |
| Ours (w/o SSL) | 91 | 0 | 99 | 10 |

**LIBERO-PRO — Spatial** (— : 미보고)

| Method | Obj | Pos | Sem | Task |
|---|---:|---:|---:|---:|
| UniVLA | 98 | 0 | 97 | — |
| GLaD | 98 | **12** | 97 | — |
| OpenVLA | 97 | 0 | 97 | 0 |
| π₀ | 95 | 0 | 97 | 0 |
| **Ours (Full)** | 90 | 8 | 75 | **53** |
| Ours (w/o SSL) | 74 | 3 | 83 | 49 |

#### Spatial swap — 정성 비교

LIBERO-Spatial에서 객체의 공간 배치를 바꾼 **swap** 조건과 **원본**을 비교한 정성 결과입니다. 학습 때 보지 못한 배치에서도 지시한 그릇을 집어, 위치 암기가 아니라 일반화로 동작함을 보여줍니다.

**접시와 라미킨 사이의 그릇**

<div class="row">
  <div class="col-md mt-3 mt-md-0">
    {% include video.liquid path="assets/projects/thesis/spatial-between-orig.mp4" class="img-fluid rounded z-depth-1 thesis-vid" controls=true autoplay=true loop=true muted=true caption="원본" %}
  </div>
  <div class="col-md mt-3 mt-md-0">
    {% include video.liquid path="assets/projects/thesis/spatial-between-swap.mp4" class="img-fluid rounded z-depth-1 thesis-vid" controls=true autoplay=true loop=true muted=true caption="swap" %}
  </div>
</div>

**테이블 중앙의 그릇**

<div class="row">
  <div class="col-md mt-3 mt-md-0">
    {% include video.liquid path="assets/projects/thesis/spatial-center-orig.mp4" class="img-fluid rounded z-depth-1 thesis-vid" controls=true autoplay=true loop=true muted=true caption="원본" %}
  </div>
  <div class="col-md mt-3 mt-md-0">
    {% include video.liquid path="assets/projects/thesis/spatial-center-swap.mp4" class="img-fluid rounded z-depth-1 thesis-vid" controls=true autoplay=true loop=true muted=true caption="swap" %}
  </div>
</div>

**나무 캐비닛 위 서랍 안의 그릇**

<div class="row">
  <div class="col-md mt-3 mt-md-0">
    {% include video.liquid path="assets/projects/thesis/spatial-drawer-orig.mp4" class="img-fluid rounded z-depth-1 thesis-vid" controls=true autoplay=true loop=true muted=true caption="원본" %}
  </div>
  <div class="col-md mt-3 mt-md-0">
    {% include video.liquid path="assets/projects/thesis/spatial-drawer-swap.mp4" class="img-fluid rounded z-depth-1 thesis-vid" controls=true autoplay=true loop=true muted=true caption="swap" %}
  </div>
</div>

**접시 옆의 그릇**

<div class="row">
  <div class="col-md mt-3 mt-md-0">
    {% include video.liquid path="assets/projects/thesis/spatial-next-orig.mp4" class="img-fluid rounded z-depth-1 thesis-vid" controls=true autoplay=true loop=true muted=true caption="원본" %}
  </div>
  <div class="col-md mt-3 mt-md-0">
    {% include video.liquid path="assets/projects/thesis/spatial-next-swap.mp4" class="img-fluid rounded z-depth-1 thesis-vid" controls=true autoplay=true loop=true muted=true caption="swap" %}
  </div>
</div>

**LIBERO-PRO — Goal**

| Method | Obj | Pos | Sem | Task |
|---|---:|---:|---:|---:|
| UniVLA | 62 | 4 | 97 | 9 |
| GLaD | 81 | 4 | **98** | 10 |
| OpenVLA | **96** | 0 | **98** | 0 |
| π₀ | 94 | 0 | 93 | 0 |
| **Ours (Full)** | 67 | 4 | 87 | **12** |
| Ours (w/o SSL) | 49 | 2 | 83 | 10 |

**LIBERO-PRO — LIBERO-10**

| Method | Obj | Pos | Sem | Task |
|---|---:|---:|---:|---:|
| UniVLA | 47 | 1 | 91 | 9 |
| GLaD | 54 | **2** | 93 | 9 |
| OpenVLA | **81** | 0 | **96** | 0 |
| π₀ | 79 | 0 | 82 | 0 |
| **Ours (Full)** | 55 | 0 | 84 | **14** |
| Ours (w/o SSL) | 45 | 0 | 75 | 7 |

## Discussion

**확인한 점**

- Mamba 기반 구조로도 VLA를 충분히 구성할 수 있으며, 설계와 학습을 적절히 가져가면 기존 Transformer 기반 모델에 필적하는 성능을 보입니다.
- Mamba는 멀티모달 처리에서도 안정적으로 동작합니다.

**한계**

- 자기지도 학습(SSL)을 도입했으나, action 생성 단계에는 효과적으로 적용하기 어려웠습니다.

**후속 연구 방향**

- 멀티모달 처리 단계에 SSL을 결합하는 방향이 유망합니다.
- 추론 시 action 생성을 end-to-end로 묶기보다 분리해 설계하는 편이 낫다고 판단했으며, 이는 **월드 모델(world model)** 이 주목받는 이유와 맞닿아 있습니다.

**사용 기술**: PyTorch · Selective SSM(Mamba) · Imitation Learning · 대규모 학습 인프라
