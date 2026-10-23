# 마포구 7일 다중모델 강수 모니터링

- 확인 시각: 2026-10-23T10:28:45+09:00 (KST)
- 판정: **기준 충족**
- 위치: 서울 마포구 (37.55, 126.875)
- 기준: 시간당 강수량 20mm 이상 또는 일강수량 20mm 이상

| 날짜 | 모델 | 일강수량(mm) | 강수확률 최대(%) | 최저(°C) | 최고(°C) |
|---|---|---:|---:|---:|---:|
| 2026-10-23 | ecmwf_ifs025 | 0.0 | 3 | 6.8 | 20.4 |
| 2026-10-24 | ecmwf_ifs025 | 0.0 | 13 | 13.3 | 19.9 |
| 2026-10-25 | ecmwf_ifs025 | 0.0 | 10 | 11.3 | 24.4 |
| 2026-10-26 | ecmwf_ifs025 | 0.5 | 25 | 15.6 | 20.3 |
| 2026-10-27 | ecmwf_ifs025 | 0.0 | 4 | 5.4 | 17.0 |
| 2026-10-28 | ecmwf_ifs025 | 0.0 | 0 | 2.7 | 12.7 |
| 2026-10-29 | ecmwf_ifs025 | 1.6 | 35 | 7.0 | 15.7 |
| 2026-10-23 | ncep_gfs_global | 0.0 | 0 | 10.4 | 20.4 |
| 2026-10-24 | ncep_gfs_global | 0.0 | 20 | 16.3 | 19.4 |
| 2026-10-25 | ncep_gfs_global | 0.0 | 3 | 14.3 | 24.0 |
| 2026-10-26 | ncep_gfs_global | 0.0 | 14 | 16.3 | 19.8 |
| 2026-10-27 | ncep_gfs_global | 0.0 | 6 | 5.4 | 16.8 |
| 2026-10-28 | ncep_gfs_global | 0.0 | 2 | 5.1 | 13.0 |
| 2026-10-29 | ncep_gfs_global | 6.6 | 56 | 9.8 | 14.8 |
| 2026-10-23 | icon_global | 0.0 | 0 | 5.2 | 19.6 |
| 2026-10-24 | icon_global | 0.0 | 5 | 12.5 | 19.8 |
| 2026-10-25 | icon_global | 0.0 | 5 | 13.9 | 25.0 |
| 2026-10-26 | icon_global | 0.0 | 15 | 16.4 | 23.8 |
| 2026-10-27 | icon_global | 0.0 | 3 | 4.7 | 17.9 |
| 2026-10-28 | icon_global | 0.0 | 0 | 0.2 | 9.8 |
| 2026-10-29 | icon_global | 2.4 | 18 | 3.3 | 14.0 |
| 2026-10-23 | gem_global | 0.0 | 0 | 1.7 | 21.9 |
| 2026-10-24 | gem_global | 0.0 | 14 | 11.4 | 20.2 |
| 2026-10-25 | gem_global | 0.0 | 11 | 7.9 | 27.1 |
| 2026-10-26 | gem_global | 0.0 | 14 | 13.6 | 23.0 |
| 2026-10-27 | gem_global | 0.0 | 10 | 5.8 | 17.2 |
| 2026-10-28 | gem_global | 0.6 | 5 | 2.4 | 12.1 |
| 2026-10-29 | gem_global | 20.7 | 43 | 11.4 | 18.2 |

## 기준 충족 신호

- gem_global: 2026-10-29 일강수량 20.7mm

## 시공업체 전달 문구

마포구 2026-10-29 일강수량 20.7mm 예보(gem_global), 지하1층 누수 점검 대기 부탁드립니다.

## 모델별 원자료 출처

- ecmwf_ifs025: https://api.open-meteo.com/v1/forecast?latitude=37.55&longitude=126.875&timezone=Asia%2FSeoul&forecast_days=7&models=ecmwf_ifs025&hourly=precipitation%2Cprecipitation_probability%2Ctemperature_2m&daily=precipitation_sum%2Cprecipitation_probability_max%2Ctemperature_2m_min%2Ctemperature_2m_max (수집 2026-10-23T10:28:39+09:00)
- ncep_gfs_global: https://api.open-meteo.com/v1/forecast?latitude=37.55&longitude=126.875&timezone=Asia%2FSeoul&forecast_days=7&models=ncep_gfs_global&hourly=precipitation%2Cprecipitation_probability%2Ctemperature_2m&daily=precipitation_sum%2Cprecipitation_probability_max%2Ctemperature_2m_min%2Ctemperature_2m_max (수집 2026-10-23T10:28:40+09:00)
- icon_global: https://api.open-meteo.com/v1/forecast?latitude=37.55&longitude=126.875&timezone=Asia%2FSeoul&forecast_days=7&models=icon_global&hourly=precipitation%2Cprecipitation_probability%2Ctemperature_2m&daily=precipitation_sum%2Cprecipitation_probability_max%2Ctemperature_2m_min%2Ctemperature_2m_max (수집 2026-10-23T10:28:40+09:00)
- gem_global: https://api.open-meteo.com/v1/forecast?latitude=37.55&longitude=126.875&timezone=Asia%2FSeoul&forecast_days=7&models=gem_global&hourly=precipitation%2Cprecipitation_probability%2Ctemperature_2m&daily=precipitation_sum%2Cprecipitation_probability_max%2Ctemperature_2m_min%2Ctemperature_2m_max (수집 2026-10-23T10:28:45+09:00)

## 응답 실패 모델

- kma_gdps: ValueError: API returned empty or all-null precipitation arrays

## 해석 주의

- 서로 다른 모델의 강수량은 독립적인 예측입니다. 한 모델만 기준을 넘으면 단일 모델 신호로 봅니다.
- API 오류 또는 모델 응답 누락이 있으면 전체 판정은 불완전합니다.
- 이 저장소는 예보표를 기록하며, 별도 알림 채널을 설정하지 않으면 휴대전화 푸시/문자 알림을 보내지 않습니다.
