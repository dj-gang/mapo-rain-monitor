# 마포구 7일 다중모델 강수 모니터링

- 확인 시각: 2026-10-24T10:53:52+09:00 (KST)
- 판정: **기준 충족**
- 위치: 서울 마포구 (37.55, 126.875)
- 기준: 시간당 강수량 20mm 이상 또는 일강수량 20mm 이상

| 날짜 | 모델 | 일강수량(mm) | 강수확률 최대(%) | 최저(°C) | 최고(°C) |
|---|---|---:|---:|---:|---:|
| 2026-10-24 | ecmwf_ifs025 | 0.3 | 22 | 13.7 | 18.5 |
| 2026-10-25 | ecmwf_ifs025 | 0.0 | 8 | 11.4 | 24.4 |
| 2026-10-26 | ecmwf_ifs025 | 0.1 | 4 | 13.6 | 22.4 |
| 2026-10-27 | ecmwf_ifs025 | 0.0 | 0 | 6.7 | 16.6 |
| 2026-10-28 | ecmwf_ifs025 | 0.0 | 0 | 2.7 | 11.7 |
| 2026-10-29 | ecmwf_ifs025 | 0.0 | 36 | 6.4 | 14.4 |
| 2026-10-30 | ecmwf_ifs025 | 21.2 | 73 | 8.5 | 18.6 |
| 2026-10-24 | ncep_gfs_global | 0.0 | 23 | 16.0 | 18.4 |
| 2026-10-25 | ncep_gfs_global | 0.1 | 3 | 14.0 | 24.2 |
| 2026-10-26 | ncep_gfs_global | 0.0 | 6 | 17.1 | 23.6 |
| 2026-10-27 | ncep_gfs_global | 0.0 | 0 | 5.9 | 17.6 |
| 2026-10-28 | ncep_gfs_global | 0.0 | 2 | 4.7 | 11.8 |
| 2026-10-29 | ncep_gfs_global | 0.2 | 44 | 9.8 | 14.7 |
| 2026-10-30 | ncep_gfs_global | 1.3 | 48 | 10.7 | 18.7 |
| 2026-10-24 | icon_global | 0.0 | 5 | 13.7 | 19.6 |
| 2026-10-25 | icon_global | 0.0 | 0 | 13.5 | 23.5 |
| 2026-10-26 | icon_global | 0.0 | 0 | 15.5 | 22.2 |
| 2026-10-27 | icon_global | 0.0 | 0 | 3.9 | 17.0 |
| 2026-10-28 | icon_global | 0.0 | 0 | 1.1 | 10.9 |
| 2026-10-29 | icon_global | 0.6 | 24 | 3.5 | 13.5 |
| 2026-10-30 | icon_global | 3.0 | 55 | 10.2 | 19.1 |
| 2026-10-24 | gem_global | 0.0 | 7 | 11.9 | 20.1 |
| 2026-10-25 | gem_global | 0.0 | 14 | 9.3 | 26.4 |
| 2026-10-26 | gem_global | 0.0 | 5 | 10.7 | 21.8 |
| 2026-10-27 | gem_global | 0.4 | 5 | 5.5 | 17.5 |
| 2026-10-28 | gem_global | 0.0 | 0 | 1.7 | 13.7 |
| 2026-10-29 | gem_global | 6.1 | 33 | 11.2 | 14.0 |
| 2026-10-30 | gem_global | 14.0 | 48 | 10.0 | 17.5 |

## 기준 충족 신호

- ecmwf_ifs025: 2026-10-30 일강수량 21.2mm

## 시공업체 전달 문구

마포구 2026-10-30 일강수량 21.2mm 예보(ecmwf_ifs025), 지하1층 누수 점검 대기 부탁드립니다.

## 모델별 원자료 출처

- ecmwf_ifs025: https://api.open-meteo.com/v1/forecast?latitude=37.55&longitude=126.875&timezone=Asia%2FSeoul&forecast_days=7&models=ecmwf_ifs025&hourly=precipitation%2Cprecipitation_probability%2Ctemperature_2m&daily=precipitation_sum%2Cprecipitation_probability_max%2Ctemperature_2m_min%2Ctemperature_2m_max (수집 2026-10-24T10:53:46+09:00)
- ncep_gfs_global: https://api.open-meteo.com/v1/forecast?latitude=37.55&longitude=126.875&timezone=Asia%2FSeoul&forecast_days=7&models=ncep_gfs_global&hourly=precipitation%2Cprecipitation_probability%2Ctemperature_2m&daily=precipitation_sum%2Cprecipitation_probability_max%2Ctemperature_2m_min%2Ctemperature_2m_max (수집 2026-10-24T10:53:46+09:00)
- icon_global: https://api.open-meteo.com/v1/forecast?latitude=37.55&longitude=126.875&timezone=Asia%2FSeoul&forecast_days=7&models=icon_global&hourly=precipitation%2Cprecipitation_probability%2Ctemperature_2m&daily=precipitation_sum%2Cprecipitation_probability_max%2Ctemperature_2m_min%2Ctemperature_2m_max (수집 2026-10-24T10:53:47+09:00)
- gem_global: https://api.open-meteo.com/v1/forecast?latitude=37.55&longitude=126.875&timezone=Asia%2FSeoul&forecast_days=7&models=gem_global&hourly=precipitation%2Cprecipitation_probability%2Ctemperature_2m&daily=precipitation_sum%2Cprecipitation_probability_max%2Ctemperature_2m_min%2Ctemperature_2m_max (수집 2026-10-24T10:53:52+09:00)

## 응답 실패 모델

- kma_gdps: ValueError: API returned empty or all-null precipitation arrays

## 해석 주의

- 서로 다른 모델의 강수량은 독립적인 예측입니다. 한 모델만 기준을 넘으면 단일 모델 신호로 봅니다.
- API 오류 또는 모델 응답 누락이 있으면 전체 판정은 불완전합니다.
- 이 저장소는 예보표를 기록하며, 별도 알림 채널을 설정하지 않으면 휴대전화 푸시/문자 알림을 보내지 않습니다.
