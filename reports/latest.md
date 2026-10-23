# 마포구 7일 다중모델 강수 모니터링

- 확인 시각: 2026-10-23T20:59:15+09:00 (KST)
- 판정: **판정 불가 (일부 모델 응답 실패)**
- 위치: 서울 마포구 (37.55, 126.875)
- 기준: 시간당 강수량 20mm 이상 또는 일강수량 20mm 이상

| 날짜 | 모델 | 일강수량(mm) | 강수확률 최대(%) | 최저(°C) | 최고(°C) |
|---|---|---:|---:|---:|---:|
| 2026-10-23 | ecmwf_ifs025 | 0.0 | 5 | 6.3 | 20.1 |
| 2026-10-24 | ecmwf_ifs025 | 0.6 | 35 | 13.2 | 17.6 |
| 2026-10-25 | ecmwf_ifs025 | 1.0 | 6 | 10.5 | 24.8 |
| 2026-10-26 | ecmwf_ifs025 | 0.0 | 8 | 13.5 | 23.4 |
| 2026-10-27 | ecmwf_ifs025 | -0.2 | 0 | 5.8 | 16.7 |
| 2026-10-28 | ecmwf_ifs025 | 0.0 | 0 | 2.2 | 11.9 |
| 2026-10-29 | ecmwf_ifs025 | 1.1 | 36 | 5.8 | 12.0 |
| 2026-10-23 | ncep_gfs_global | 0.0 | 0 | 10.4 | 20.8 |
| 2026-10-24 | ncep_gfs_global | 0.0 | 49 | 16.1 | 18.7 |
| 2026-10-25 | ncep_gfs_global | 0.0 | 0 | 14.3 | 24.4 |
| 2026-10-26 | ncep_gfs_global | 0.0 | 6 | 15.6 | 22.9 |
| 2026-10-27 | ncep_gfs_global | 0.0 | 3 | 5.1 | 17.6 |
| 2026-10-28 | ncep_gfs_global | 0.0 | 0 | 4.2 | 11.1 |
| 2026-10-29 | ncep_gfs_global | 4.6 | 40 | 9.0 | 14.3 |
| 2026-10-23 | icon_global | 0.0 | 3 | 5.2 | 21.0 |
| 2026-10-24 | icon_global | 0.0 | 5 | 12.9 | 19.3 |
| 2026-10-25 | icon_global | 0.0 | 0 | 11.1 | 25.1 |
| 2026-10-26 | icon_global | 0.0 | 8 | 15.3 | 23.5 |
| 2026-10-27 | icon_global | 0.0 | 3 | 3.6 | 16.8 |
| 2026-10-28 | icon_global | 0.0 | 0 | 0.9 | 9.9 |
| 2026-10-29 | icon_global | 0.9 | 21 | 3.7 | 12.3 |
| 2026-10-23 | gem_global | 0.0 | 0 | 1.7 | 21.9 |
| 2026-10-24 | gem_global | 0.0 | 10 | 11.6 | 19.1 |
| 2026-10-25 | gem_global | 0.0 | 5 | 9.0 | 26.9 |
| 2026-10-26 | gem_global | 0.0 | 14 | 11.0 | 22.6 |
| 2026-10-27 | gem_global | 2.1 | 14 | 6.1 | 16.9 |
| 2026-10-28 | gem_global | 0.0 | 0 | 1.7 | 12.6 |
| 2026-10-29 | gem_global | 19.1 | 29 | 9.2 | 13.3 |

## 기준 충족 신호

- 모델 응답이 불완전해 임계치 미충족으로 단정할 수 없습니다.

## 모델별 원자료 출처

- ecmwf_ifs025: https://api.open-meteo.com/v1/forecast?latitude=37.55&longitude=126.875&timezone=Asia%2FSeoul&forecast_days=7&models=ecmwf_ifs025&hourly=precipitation%2Cprecipitation_probability%2Ctemperature_2m&daily=precipitation_sum%2Cprecipitation_probability_max%2Ctemperature_2m_min%2Ctemperature_2m_max (수집 2026-10-23T20:59:09+09:00)
- ncep_gfs_global: https://api.open-meteo.com/v1/forecast?latitude=37.55&longitude=126.875&timezone=Asia%2FSeoul&forecast_days=7&models=ncep_gfs_global&hourly=precipitation%2Cprecipitation_probability%2Ctemperature_2m&daily=precipitation_sum%2Cprecipitation_probability_max%2Ctemperature_2m_min%2Ctemperature_2m_max (수집 2026-10-23T20:59:09+09:00)
- icon_global: https://api.open-meteo.com/v1/forecast?latitude=37.55&longitude=126.875&timezone=Asia%2FSeoul&forecast_days=7&models=icon_global&hourly=precipitation%2Cprecipitation_probability%2Ctemperature_2m&daily=precipitation_sum%2Cprecipitation_probability_max%2Ctemperature_2m_min%2Ctemperature_2m_max (수집 2026-10-23T20:59:10+09:00)
- gem_global: https://api.open-meteo.com/v1/forecast?latitude=37.55&longitude=126.875&timezone=Asia%2FSeoul&forecast_days=7&models=gem_global&hourly=precipitation%2Cprecipitation_probability%2Ctemperature_2m&daily=precipitation_sum%2Cprecipitation_probability_max%2Ctemperature_2m_min%2Ctemperature_2m_max (수집 2026-10-23T20:59:15+09:00)

## 응답 실패 모델

- kma_gdps: ValueError: API returned empty or all-null precipitation arrays

## 해석 주의

- 서로 다른 모델의 강수량은 독립적인 예측입니다. 한 모델만 기준을 넘으면 단일 모델 신호로 봅니다.
- API 오류 또는 모델 응답 누락이 있으면 전체 판정은 불완전합니다.
- 이 저장소는 예보표를 기록하며, 별도 알림 채널을 설정하지 않으면 휴대전화 푸시/문자 알림을 보내지 않습니다.
