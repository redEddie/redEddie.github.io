---
layout: page
title: PnP 기반 실외 3D 위치 추정
description: 컴퓨터비전특론 과제 — 단일 이미지와 랜드마크 좌표로 지구 좌표계 기준 카메라 포즈 추정 · 2025.06.08
img: assets/projects/pnp/pnp-cover.jpg
importance: 8
category: coursework
tags: [Computer Vision, PnP, RANSAC, Camera Calibration, OpenCV]
related_publications: false
---

스마트폰으로 촬영한 단일 이미지와 캠퍼스 내 5개 지점의 알려진 3차원 좌표(위도·경도·고도)만으로 카메라의 위치와 자세를 추정하는 과제입니다. OpenCV `solvePnPRansac`으로 2D–3D 대응점에서 포즈를 계산하고, 지구 고정 좌표계(WGS84)로 변환해 실측 좌표와 비교했으며, 이동하며 촬영한 사진들로 경로를 복원해 Google Earth에 시각화했습니다.

## 방법

PnP(Perspective-n-Point)는 3차원 점과 그 점들이 이미지에 투영된 2차원 위치의 대응 관계로 카메라의 회전·이동을 추정하는 기법입니다. RANSAC을 결합한 `solvePnPRansac`으로 수동 대응점에 포함된 이상치의 영향을 최소화했습니다.

파이프라인은 다음과 같습니다. 랜드마크의 WGS84 좌표를 `pyproj`로 UTM zone 52N 평면 좌표로 변환하고, 촬영 이미지에서 해당 지점의 픽셀 좌표를 추출해 대응쌍을 구성합니다. `solvePnPRansac`이 반환하는 회전·이동은 월드→카메라 변환이므로, 이를 역변환해 카메라 위치를 지구 좌표로 복원합니다.

$$
\mathbf{X}_c = R\,\mathbf{X}_o + \mathbf{t} \quad\Rightarrow\quad \mathbf{X}_o = R^{\top}(\mathbf{X}_c - \mathbf{t})
$$

## 카메라 캘리브레이션과 검증 — 체스보드

체스보드 패턴으로 카메라(iPhone 16 Plus 광각) 내부 파라미터 $$K$$와 왜곡 계수를 추정했습니다. 평균 재투영 오차 **0.16 픽셀**로 안정적인 캘리브레이션을 확인했습니다. 추정 파이프라인 검증을 위해 `solvePnP`로 체스보드의 자세를 추정하고, 첫 번째 코너 기준 3D 좌표축과 큐브를 이미지에 재투영했습니다.

<div class="row">
  <div class="col-md mt-3 mt-md-0">
    {% include figure.liquid loading="eager" path="assets/projects/pnp/chessboard-axis.jpg" title="3D axis projection" class="img-fluid rounded z-depth-1" zoomable=true %}
  </div>
  <div class="col-md mt-3 mt-md-0">
    {% include figure.liquid loading="eager" path="assets/projects/pnp/chessboard-cube.jpg" title="3D cube projection" class="img-fluid rounded z-depth-1" zoomable=true %}
  </div>
</div>
<div class="caption">추정한 자세로 재투영한 3D 좌표축(좌)과 큐브(우) — 체스보드 평면과 정확히 정합</div>

## 실외 위치 추정 — 지구 좌표계

캠퍼스에서 촬영한 이미지와 건물 모서리 등 5개 랜드마크의 좌표(Google Earth에서 취득)로 카메라 위치를 추정하고, 실측 좌표(GPS)와 비교했습니다.

<div class="row">
  <div class="col-md mt-3 mt-md-0">
    {% include figure.liquid loading="eager" path="assets/projects/pnp/localization-scene.jpg" title="Localization scene" class="img-fluid rounded z-depth-1" zoomable=true %}
  </div>
  <div class="col-md mt-3 mt-md-0 align-self-center">
    {% include figure.liquid loading="eager" path="assets/projects/pnp/landmark-googleearth.jpg" title="Landmark coordinates" class="img-fluid rounded z-depth-1" zoomable=true %}
  </div>
</div>
<div class="caption">좌: 위치 추정에 사용한 촬영 이미지 / 우: Google Earth에서 취득한 랜드마크 3D 좌표</div>

| 구분 | 오차 |
| --- | --- |
| 동–서 (ΔE) | 32.43 m |
| 남–북 (ΔN) | 88.01 m |
| 수직 (Δh) | 4.06 m |
| 전체 3D | 93.88 m |

GPS가 약한 환경에서 단일 이미지와 소수의 랜드마크만으로 위치를 추정할 수 있음을 확인했습니다.

## 이동 경로 추정

일청담에서 본관까지 이동하며 7장의 사진을 촬영하고, 각 프레임의 카메라 위치를 추정해 KML로 변환한 뒤 Google Earth에 경로를 복원했습니다. 한 프레임은 건물 모서리 특징점이 가로등에 가려져 대응점 오차가 수직 오차로 증폭되는 것을 확인하고, 원인 분석 후 분석에서 제외했습니다.

<div class="row justify-content-center">
  <div class="col-md-10 mt-3">
    {% include figure.liquid loading="eager" path="assets/projects/pnp/path-googleearth.png" title="Estimated trajectory" class="img-fluid rounded z-depth-1" zoomable=true %}
  </div>
</div>
<div class="caption">Google Earth에 복원한 이동 경로 — 노란 점: 추정된 카메라 위치, 붉은 선: 실제 이동 경로</div>

## 이 과제로 이해하게 된 것

영상 처리와 특징 추출, 좌표계 변환 과정을 직접 구현하며 컴퓨터 비전 알고리즘이 동작하는 원리를 이해했습니다. 특히 카메라 캘리브레이션은 알고리즘 선택에 따라 결과가 크게 달라져, 재투영 오차를 기준으로 추정 품질을 검증하는 과정이 중요했습니다. 이후 딥러닝 기반 비전 모델을 공부할 때도 이러한 전통적 기하 접근법이 좋은 직관을 제공했습니다.
