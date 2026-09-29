---
layout: page
title: 매니퓰레이션 프로젝트 (Manipulation Stack)
description: GELLO 기반 데이터 수집 인프라 구축 및 Franka FR3 실로봇 안전 배포 파이프라인
img: assets/projects/manipulation/manipulation-cover.jpg
importance: 1
category: research
tags: [VLA, Imitation Learning, Data Collection, GELLO, Franka FR3, Real-robot Deploy, Robot Safety]
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

자체 설계한 경량 VLA 모델을 실제 환경에서 검증·배포하기 위한 엔드투엔드 파이프라인 구축 트랙입니다. 실물 데이터 수집의 병목을 해결하기 위해 비전문가도 운용 가능한 GELLO 기반 수집 환경을 구축하고, Franka FR3의 토크 제어기를 활용한 안전 실시간 배포 시스템을 완성했습니다.

## 1. GELLO 기반 데이터 수집 인프라

비전문가도 직관적으로 작업할 수 있는 환경을 목표로, GELLO 텔레오퍼레이션 하드웨어와 전용 수집 GUI를 구성했습니다.

- **수집 및 검증 파이프라인 단일화**: 데이터 레코딩, 실시간 궤적 저장/검증, 다음 에피소드의 물체 배치 추천 알고리즘을 단일 GUI 화면에 통합
- **하드웨어 및 통신 최적화**: 센서 및 온보드 PC의 안정적인 전원 분배 설계, ZMQ 기반 유무선 저지연 통신 구성
- **성과**: 에피소드 간 준비·정리 간격을 29.6초에서 13.4초로 **54% 단축**, 연구실 동료들과 함께 **3,000개 이상의 조작 에피소드** 확보

<div class="row">
  <div class="col-md mt-3 mt-md-0">
    {% include figure.liquid path="assets/projects/manipulation/gello-teleop.jpg" class="img-fluid rounded z-depth-1" zoomable=true caption="GELLO Master Arm을 활용한 FR3 원격 조종 및 데이터 수집" %}
  </div>
  <div class="col-md mt-3 mt-md-0">
    {% include figure.liquid path="assets/projects/manipulation/collector-gui.jpg" class="img-fluid rounded z-depth-1" zoomable=true caption="데이터 수집 GUI (물체 배치 가이드 및 에피소드 유효성 검증)" %}
  </div>
</div>

## 2. Franka FR3 실로봇 안전 배포

학습된 정책을 HTTP 서버로 모듈화하고, 로봇 클라이언트가 추론 결과를 수신해 제어하는 서버-클라이언트 아키텍처로 배포했습니다.

- **멀티레이트 동기화 & 통신**: 약 80ms의 네트워크 왕복(RTT) 및 추론 지연 환경에서, 20Hz 정책 액션과 로봇의 1kHz 저수준 제어 루프 사이를 실시간 비동기 보간으로 연결하여 부드러운 궤적 생성
- **Torque Mode 기반 안전 계층(Safety Layer)**:
  - 조작 중 마스터 컨트롤러 낙하 등 비정상 입력에 의한 급격한 관절 가속/저크 차단
  - 임계 외력(Torque/Force) 감지 시 즉시 동작을 정지하는 충돌 안전 레이어를 두어 하드웨어 파손 방지

<div class="row">
  <div class="col-md mt-3 mt-md-0">
    {% include video.liquid path="assets/projects/manipulation/fr3-deploy.mp4" class="img-fluid rounded z-depth-1 manip-vid" controls=true autoplay=true loop=true muted=true %}
  </div>
  <div class="col-md mt-3 mt-md-0">
    {% include video.liquid path="assets/projects/manipulation/fr3-demo-cup-box.mp4" class="img-fluid rounded z-depth-1 manip-vid" controls=true autoplay=true loop=true muted=true %}
  </div>
</div>
<div class="caption">Franka FR3 실로봇 조작 구동 (20Hz 정책 추론 - 1kHz 보간 및 Torque 기반 안전 제어)</div>

## 3. Next Step: UMI 기반 확장

- 핸드헬드 그리퍼(UMI) 방식을 도입해 고정형 텔레옵의 공간적 제약을 넘어선 광범위한 데이터 수집 환경 준비
- 배포단 경량화를 위해 Jetson 기반 엣지 디바이스 환경에서의 온로봇 추론 파이프라인 구축 진행

<div class="row">
  <div class="col-md mt-3 mt-md-0">
    {% include figure.liquid path="assets/projects/manipulation/umi-gripper.jpg" class="img-fluid rounded z-depth-1" zoomable=true caption="UMI 프로토타입 그리퍼 및 조작 대상 파츠" %}
  </div>
  <div class="col-md mt-3 mt-md-0">
    {% include figure.liquid path="assets/projects/manipulation/jetson-thor.jpg" class="img-fluid rounded z-depth-1" zoomable=true caption="엣지 배포용 Jetson 보드 세팅" %}
  </div>
</div>
