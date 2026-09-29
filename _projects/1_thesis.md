---
layout: page
title: 석사 학위논문 — Selective SSM 기반 모방학습
description: Selective State Space Model-based Efficient Imitation Learning for Generalizable Robot Manipulation · 2026년 8월
img: assets/projects/thesis/fig-overall.png
importance: 2
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

경북대학교 석사 학위논문(2026.08)입니다. [dCollection](https://www.dcollection.net/handler/knu/000000113705)

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

### 추론 효율

같은 조건에서 액션 청크 1회를 추론하는 데 걸리는 시간을 π₀와 비교했습니다. π₀ 대비 약 **6배 빠르게** 추론합니다.

| 모델 | 파라미터 | 추론 시간 (액션 청크 1회) | GPU 메모리 |
|---|---:|---:|---:|
| **Ours** | ~574M | **~20 ms** | ~3 GB |
| π₀ | ~3.3B | ~120 ms | — |

<div class="caption">측정 조건: RTX PRO 6000 · 배치 1 · 카메라 2대(224×224) · 액션 청크 10 · Flow Matching 10 스텝. GPU 메모리는 PyTorch 측정값, π₀ 파라미터는 π₀ 논문 기준.</div>

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

## 기술적 난제와 해결

### 1. RoPE 없는 Mamba-2에서 위치 신호와 이미지 신호의 균형

- **현상·원인**: Transformer와 달리 Mamba-2에는 RoPE 같은 위치 인코딩 장치가 없어, 위치 임베딩을 이미지 임베딩에 더해야 했습니다. 위치 신호가 이미지 신호에 묻히지도, 이미지를 압도하지도 않도록 크기를 맞추는 것이 관건이었습니다.
- **시도**: 위치 임베딩에 학습 가능한 게이트를 두었으나, 게이트가 초기값에 머물거나 위치 임베딩의 크기를 키워 이미지 신호를 압도하는 방향으로 학습됐습니다.
- **해결**: 게이트를 학습시키는 대신 스케일을 실험적으로 탐색해 가장 성능이 높았던 값으로 고정했습니다. 여기에 양방향 Mamba와 자기지도 학습(SSL)을 결합해 적은 데이터로도 공간 구조를 학습하도록 설계했습니다.

### 2. 행동 헤드의 기울기에 의한 멀티모달 표현 훼손

- **현상·원인**: 학습 loss는 충분히 낮아졌지만 성공률이 기대만큼 오르지 않았습니다. Flow Matching 행동 헤드의 큰 역전파 기울기가 멀티모달 Mamba 인코더로 전달되면서, 사전학습 표현이 가진 일반화 능력이 훼손된 것으로 판단했습니다. 행동 학습이 VLM의 일반화 능력을 잊게 만든다는 [*Knowledge Insulating VLA*](https://arxiv.org/abs/2505.23705) (Driess et al., 2025)의 지적과 같은 맥락입니다.
- **해결**: 학습을 두 단계로 분리했습니다. Stage 1에서 SSL loss로 멀티모달 표현을 학습하고, Stage 2에서 행동 헤드를 학습해 앞 단계의 표현을 보존했습니다.
- **검증**: 같은 장면에 다른 지시문을 주는 LIBERO-PRO Task 교란에서, 다른 공개 VLA(0–10%) 대비 **10–53%**의 성공률을 기록해 지시문 이해 능력이 향상됐음을 확인했습니다.

### 3. 손목 카메라 편향과 행동 암기

- **현상·원인**: 정책이 3인칭(agent) 카메라를 무시하고 손목(wrist) 카메라에만 의존하면서, 장면을 파악하기보다 행동을 외우는 경향이 나타났습니다.
- **해결**: 이미지를 복원하는 SSL loss를 추가해 agent 카메라 정보를 참조하도록 강제했습니다.
- **검증**: SSL을 뺀 절제 실험 대비 LIBERO 평균 성공률이 **94.50% → 97.25%**로 향상됐고, Task 교란 성능도 함께 개선됐습니다(LIBERO-10 기준 7% → 14%).

## Discussion

**확인한 점**

- 양방향 구조와 멀티모달 융합 설계를 통해 Mamba 기반 구조로도 기존 Transformer 기반 VLA에 필적하는 성능을 낼 수 있음을 확인했습니다.
- 비전·언어·로봇 상태를 하나의 Selective SSM 시퀀스로 안정적으로 처리할 수 있었습니다.

**한계**

- SSL은 멀티모달 표현 학습에는 효과가 있었으나, 행동 생성 단계에 직접 적용하기는 구조적으로 어려웠습니다.
- Mamba-2는 채널이 깊거나 비전 토큰 수가 많아지면 이미지 이해 성능이 떨어지는 경향이 있어, 비교적 작은 비전 인코더(DINOv3-B)를 선택해야 했습니다.

**후속 연구 방향**

- **실로봇 적용**: Franka FR3 배포 파이프라인([매니퓰레이션 프로젝트](/projects/2_manipulation/))에서 학위논문 모델의 실로봇 구동을 확인했으며, 정량적 성공률 평가는 진행 중입니다.
- **행동 학습에 의한 일반화 망각**: 난제 2에서 확인한 현상, 즉 Flow Matching 행동 학습이 사전학습 표현의 일반화 능력을 훼손하는 문제를 후속 연구로 이어가고 있습니다.

**사용 기술**: PyTorch · Selective SSM(Mamba) · Imitation Learning · 대규모 학습 인프라
