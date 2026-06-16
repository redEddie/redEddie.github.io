---
layout: page
title: 조지아공대 인턴 — 사족보행 로코모션 강화학습
description: Sehoon Ha 연구실(Georgia Tech) 인턴 · legged_gym 강화학습 환경 구축과 사람 동작 기반 로코모션 연구 분석 · 2024.08
img: assets/projects/gatech/gatech-cover.jpg
importance: 9
category: research
tags: [Legged Locomotion, Reinforcement Learning, Isaac Gym, Sim-to-Real, Motion Retargeting, Unitree Aliengo]
related_publications: false
---

2024년 8월, Georgia Tech의 Sehoon Ha 교수 연구실에서 사족보행 로코모션을 주제로 인턴을 수행했습니다. 강화학습 시뮬레이션 환경을 직접 구축해 보행 정책을 학습시키고, 연구실 세미나에서 다룬 "사람의 동작을 사족보행 로봇의 제어로 옮기는" 일련의 연구를 분석했습니다. 실로봇 Unitree Aliengo를 처음 다루며 시뮬레이션과 실제 로봇 사이의 간극을 직접 확인한, 이후 로코모션·모방학습 연구의 출발점이 된 경험입니다.

## 강화학습 환경 구축 — legged_gym

Isaac Gym 기반 `legged_gym` 파이프라인을 분석하고, 로봇의 URDF·USD 기술 파일로 시뮬레이션 환경을 구성해 강화학습으로 보행 정책을 학습시켰습니다. 환경을 직접 세우는 과정에서 RL 로코모션이 어떤 요소로 구성되는지를 구조적으로 파악했습니다. 로봇의 관절·링크·충돌 형상을 정의하는 기술 파일, 지형·외란을 다루는 도메인 랜덤화, 그리고 보행의 형태를 결정하는 보상 항이 각각 어디서 작동하는지를 확인했습니다.

이 과정에서 얻은 핵심 관찰은, 같은 환경·같은 알고리즘이라도 **보상 설계가 보행 스타일과 안정성을 사실상 결정한다**는 점이었습니다. 좋은 gait를 얻으려면 보행 주기·발 접촉(contact)·발 높이까지 일일이 보상 항으로 지정하는 reward engineering이 필요한데, 이렇게 설계해도 시뮬레이터 안에서조차 원하는 보행 모션을 얻기 어려웠고, 과하게 맞춰 넣은 보상 항은 오히려 **시뮬레이터와 현실의 갭(sim-to-real gap)을 키우는** 부작용으로 이어졌습니다. 이 부담은 뒤에서 다룬 "사람 동작 데이터를 활용하는" 접근들이 왜 매력적인지를 이해하는 배경이 되었습니다.

## 분석한 연구 — 사람 동작에서 사족보행 제어로

연구실 세미나에서 세 편의 연구를 들었고, 이를 *"사람의 풍부한 동작 데이터를 형태가 다른 로봇의 제어로 어떻게 이식하는가"* 라는 하나의 질문으로 묶어 정리했습니다.

- **ACE — Adversarial Correspondence Embedding** *(Cross-Morphology Motion Retargeting)*: 사람과 형태가 다른(cross-morphology) 캐릭터·로봇 사이의 동작 대응을 수작업 매핑 없이 비지도로 학습하는 모션 리타게팅. <br>↳ Li et al., 2023 · [doi.org/10.48550/arXiv.2305.14792](https://doi.org/10.48550/arXiv.2305.14792)
- **CrossLoco** *(Guided Unsupervised RL)*: 사람 동작을 사전 수집된 로봇 데이터나 수동 대응 없이, guided unsupervised RL로 다리 로봇의 제어 정책으로 직접 변환. <br>↳ Li et al., 2023 · [doi.org/10.48550/arXiv.2309.17046](https://doi.org/10.48550/arXiv.2309.17046)
- **Imitating and Finetuning MPC** *(Robust and Symmetric Quadrupedal Locomotion)*: 모델 예측 제어(MPC)의 동작을 모방학습으로 흡수한 뒤 강화학습으로 미세조정해, 보상 엔지니어링 없이도 견고하고 대칭적인 사족보행을 얻는 연구. <br>↳ Youm et al., RA-L 2023 · [doi.org/10.1109/LRA.2023.3320827](https://doi.org/10.1109/LRA.2023.3320827)

세 연구는 같은 질문에 서로 다른 층위의 답을 내놓는다는 점을 이해했습니다. ACE는 **표현 학습**으로 동작 대응을, CrossLoco는 **강화학습 변환**으로 정책을, MPC imitation은 **모델 기반 제어와의 결합**으로 안정성을 확보합니다. 앞서 직접 겪은 "보상 설계가 전부"라는 한계를, 이들 연구가 각각 데이터·표현·모델로 우회한다는 흐름으로 읽혔습니다.

## 실로봇 — Unitree Aliengo 로코모션

Unitree Aliengo에 전진(forward) 커맨드를 주어 로코모션을 구동하며, 시뮬레이션에서 다루던 보행을 실제 하드웨어에서 처음 확인했습니다. 접지 마찰·미끄러짐·구동기 응답처럼 시뮬레이터가 완전히 담지 못하는 요소들이 거동에 어떻게 드러나는지(sim-to-real gap)를 직접 관찰했습니다.

<div class="row justify-content-center">
  <div class="col-md-6 mt-3">
    {% include video.liquid path="assets/projects/gatech/aliengo-locomotion.mp4" class="img-fluid rounded z-depth-1" controls=true autoplay=true loop=true muted=true %}
  </div>
</div>
<div class="caption">전진(forward) 커맨드로 구동한 Unitree Aliengo의 로코모션 — 실로봇의 거동을 직접 관찰</div>

## 이해하게 된 것 · 이후 연구로 이어진 것

강화학습 로코모션은 보상 설계와 도메인 랜덤화로 "원하는 보행"을 빚어내는 과정이며, 데이터·모델·제어가 만나는 지점이 성능을 좌우한다는 것을 환경 구축과 세미나 분석을 통해 이해했습니다. 동시에, 사람 동작을 로봇으로 옮기는 모방·리타게팅 관점이 강화학습 단독 접근의 보상 설계 부담을 줄이는 실질적 대안이 된다는 점을 확인했습니다.

이 경험은 사족보행 로코모션이라는 출발점에서, 단순한 보행 제어를 넘어 **"동작 데이터를 어떻게 일반화 가능한 행동지능으로 만드는가"** 라는 질문으로 관심이 확장되는 계기가 되었습니다. 이후 모방학습과 VLA(Vision-Language-Action) 모델을 직접 설계·구현하는 석사 연구로 이어졌습니다.
