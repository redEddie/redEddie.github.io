---
layout: page
title: 자기부상(MagLev) 비선형 제어
description: 비선형시스템제어 수업 프로젝트 — Feedback Linearization 설계·실장비 실시간 실험 · 2025.06.23
img: assets/projects/maglev/maglev-cover.jpg
importance: 7
category: coursework
tags: [Nonlinear Control, Feedback Linearization, MATLAB/Simulink, Real-Time Experiment]
related_publications: false
---

<style>
  .maglev-vid {
    max-height: 360px;
    width: auto !important;
    margin: 0 auto;
    display: block;
  }
</style>

전자석 코일 전류로 자기장을 조절해 쇠구슬의 부상 높이를 제어하는 프로젝트입니다. 수업에서 배운 비선형 제어기를 직접 설계하고, 시뮬레이션을 거쳐 실제 장비(Feedback 33-210)에서 사인파·구형파 등 다양한 기준 신호를 추종하는지 실시간 실험으로 검증했습니다.

## 시스템 — Magnetic Levitation

자기부상 시스템은 전자석의 인력과 중력이 균형을 이루는 대표적인 비선형·개루프 불안정 시스템입니다.

$$
\ddot{x} = g - \hat{h}\,\frac{i^2}{x^2}, \qquad \hat{h} = \frac{k}{m}
$$

쇠구슬의 수직 위치 $$x$$가 제어 변수, 코일 전류 $$i$$가 제어 입력입니다. 제어 입력이 제곱으로, 위치가 분모의 제곱으로 들어가는 강한 비선형성이 핵심 난점입니다.

## 제어기 설계 — Feedback Linearization

수업에서 여러 비선형 제어기(Nonlinear PID, SMC 등)를 배웠지만, **모델을 정확히 안다면 제어기가 비선형성을 그대로 상쇄할 수 있다**는 가장 단순한 접근을 직접 확인해보고 싶어 Feedback Linearization을 선택했습니다. 비선형 항을 상쇄하고 나면 남는 시스템은 선형이므로, 바깥 루프는 익숙한 PID로 다룰 수 있습니다.

<div class="row justify-content-center">
  <div class="col-md-10 mt-3">
    {% include figure.liquid loading="eager" path="assets/projects/maglev/fl-controller-block.png" title="Feedback Linearization controller" class="img-fluid rounded z-depth-1" zoomable=true %}
  </div>
</div>
<div class="caption">제어기 외부 구조 — 위치 측정값과 오차를 받아 PID 출력을 Feedback Linearization 블록에 전달</div>

<div class="row justify-content-center">
  <div class="col-md-10 mt-3">
    {% include figure.liquid loading="eager" path="assets/projects/maglev/fl-internal-block.png" title="Feedback Linearization internal" class="img-fluid rounded z-depth-1" zoomable=true %}
  </div>
</div>
<div class="caption">Feedback Linearization 블록 내부 — $$i = \sqrt{(g - \ddot{x}_{des})\,x^2 / \hat{k}}$$ 역모델 연산으로 전류 명령을 만들고 전압 명령으로 변환. $$x_{min}$$ 클램핑으로 0 나눗셈을 방지</div>

시뮬레이션에서는 GA·PSO로 튜닝한 Linear/Nonlinear PID와 비교했고, 설계한 제어기가 사인파 기준 신호를 잘 추종하는 것을 확인했습니다.

<div class="row justify-content-center">
  <div class="col-md-8 mt-3">
    {% include figure.liquid loading="eager" path="assets/projects/maglev/fl-sim-response.png" title="Simulation response" class="img-fluid rounded z-depth-1" zoomable=true %}
  </div>
</div>
<div class="caption">사인파 기준(파랑) 대비 시뮬레이션 응답(노랑)</div>

## 실시간 실험

PCI1711 I/O 보드로 Simulink 모델을 실장비에 연결해 실시간 실험을 수행했습니다. 진폭이 변하는 사인파·구형파 기준 신호를 안정적으로 추종하며 쇠구슬의 높이가 조절되는 것을 확인했습니다.

<div class="row">
  <div class="col-md mt-3 mt-md-0">
    {% include video.liquid path="assets/projects/maglev/maglev-experiment.mp4" class="img-fluid rounded z-depth-1 maglev-vid" controls=true autoplay=true loop=true muted=true %}
  </div>
  <div class="col-md mt-3 mt-md-0 align-self-center">
    {% include video.liquid path="assets/projects/maglev/maglev-scope.mp4" class="img-fluid rounded z-depth-1" controls=true autoplay=true loop=true muted=true %}
  </div>
</div>
<div class="caption">좌: 사인파 기준 신호에 따라 쇠구슬의 높이가 진동하는 실험 장비(Feedback 33-210) / 우: 기준 신호(노랑)와 쇠구슬 위치(파랑), 제어 신호 스코프</div>

<div class="row justify-content-center">
  <div class="col-md-9 mt-3">
    {% include figure.liquid loading="eager" path="assets/projects/maglev/experiment-simulink.png" title="Real-time experiment model" class="img-fluid rounded z-depth-1" zoomable=true %}
  </div>
</div>
<div class="caption">실시간 실험용 Simulink 모델 — ADC Ch1로 쇠구슬 위치를 읽고 제어기 출력을 DAC Ch1로 코일 드라이버에 인가(PCI1711). 좌측 Sinus·Square 신호 발생기를 스위치로 선택해 오프셋(−1.5 V)을 더한 기준 신호로 사용하고, 전압–위치 Converter를 거쳐 기준·실제 위치와 제어 신호를 Signal scope로 기록</div>

## 어려웠던 점 → 배운 점

처음 설계해보는 비선형 제어기였고, 구현 과정에서 나눗셈 처리 오류로 **오차가 참값보다 작게 계산되는 버그**가 숨어 있었습니다.

"비선형성이 상쇄되었다면 남은 시스템은 선형이니, 계산값에서 벗어나더라도 선형 PID처럼 튜닝하면 동작해야 한다"는 설계 원리에 근거해 수동 튜닝을 진행했습니다. 응답 특성을 관찰한 결과 제어 입력이 부족하다고 판단했고, 이를 바탕으로 게인을 조정해 정상 동작을 확보했습니다. 이후 **동작 게인이 계산값과 크게 다르다는 점을 단서로** 구현 오류를 역추적해 수정했습니다.

이 경험으로 두 가지를 배웠습니다. 첫째, 모델 기반 제어는 **모델을 정확히 아는 것**이 전부라는 것. 둘째, 실제 하드웨어를 다룰 때는 **시스템 관점의 직관**이 중요하다는 것입니다. 설계 원리에 대한 이해가 버그를 추적하고 실험을 성공시키는 결정적 단서가 되었습니다.
