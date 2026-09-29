---
layout: about
title: About
permalink: /
subtitle: M.S. in Electronics &amp; Electrical Engineering, KNU · Imitation Learning · VLA · Real-Robot Deployment

profile:
  align: right
  image: prof_pic.jpg
  image_circular: false # crops the image to make it circular
  more_info: >
    <p>M.S., Physical Intelligence Lab</p>
    <p>Kyungpook National University</p>
    <p>Daegu, South Korea</p>

selected_papers: false # includes a list of papers marked as "selected={true}"
social: true # includes social icons at the bottom of the page

announcements:
  enabled: true # includes a list of news items
  scrollable: true # adds a vertical scroll bar if there are more than 3 news items
  limit: 7 # leave blank to include all the news in the `_news` folder

latest_posts:
  enabled: false
  scrollable: true
  limit: 3
---

<style>
/* about 페이지 섹션 제목(News, Selected Publications 등)을 대문자 시작으로 */
.post article h2 > a { text-transform: capitalize; }
/* 증명사진 크기 축소: 데스크톱 30% → 22% */
@media (min-width: 576px) {
  .profile { width: 22%; }
}
/* 모바일: 전체 폭 대신 사진(38%) + 소속 정보를 가로로 배치 */
@media (max-width: 575.98px) {
  .profile {
    display: flex;
    align-items: center;
    gap: 1rem;
    float: none !important;
    margin: 0 0 1.25rem 0 !important;
  }
  .profile figure { flex: 0 0 38%; margin: 0; }
  .profile .more-info { font-size: 0.85rem; margin: 0; }
  .profile .more-info p { display: block; }
}
</style>

경북대학교 **물리지능연구실**(지도교수 이상문)에서 석사 학위를 받았습니다(2026.08).

**모방학습과 VLA(Vision-Language-Action) 모델**을 중심으로, 모델 설계부터 데이터 수집 인프라 구축, 실로봇 배포까지 전 과정을 직접 다룹니다.

- **Model**: Selective State Space Model(Mamba-2) 기반의 경량 VLA 정책을 설계·학습했습니다 (전체 파이프라인 ~574M, 직접 설계·학습 모듈 ~188M).
- **Data**: GELLO 기반 텔레오퍼레이션 수집 환경과 수집 GUI를 구축해, 연구실 동료들과 3,000개 이상의 매니퓰레이션 에피소드를 수집했습니다.
- **Deployment**: Franka FR3에서 HTTP 서버-클라이언트 구조와 토크(Torque) 기반 안전 계층을 갖춘 실시간 배포 파이프라인을 구현했습니다.
- **Background**: 사족·이족보행 로코모션 강화학습(Georgia Tech 인턴, Open Duck Mini)과 VLA 파인튜닝 공동 연구(IROS 2025)에 참여하며 실물 로봇 연구를 시작했습니다.

**Research Interests** — Imitation Learning · VLA · Robot Data Infrastructure · Manipulation · Sim-to-Real · Reinforcement Learning

자세한 이력은 [CV](/cv/), 발표 논문은 [Publications](/publications/), 세부 구현 과정은 [Projects](/projects/)에서 볼 수 있습니다.
