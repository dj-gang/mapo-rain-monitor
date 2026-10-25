# 마포구 7일 다중모델 강수 모니터링

- 확인 시각: 2026-10-25T22:40:51+09:00 (KST)
- 판정: **판정 불가 (일부 모델 응답 실패)**
- 위치: 서울 마포구 (37.55, 126.875)
- 기준: 시간당 강수량 20mm 이상 또는 일강수량 20mm 이상

| 날짜 | 모델 | 일강수량(mm) | 강수확률 최대(%) | 최저(°C) | 최고(°C) |
|---|---|---:|---:|---:|---:|
| 2026-10-25 | ecmwf_ifs025 | 0.1 | 10 | 12.6 | 22.4 |
| 2026-10-26 | ecmwf_ifs025 | 1.5 | 4 | 12.8 | 18.0 |
| 2026-10-27 | ecmwf_ifs025 | 0.0 | 0 | 5.8 | 15.0 |
| 2026-10-28 | ecmwf_ifs025 | 0.0 | 0 | 2.5 | 11.0 |
| 2026-10-29 | ecmwf_ifs025 | 1.9 | 76 | 4.8 | 12.0 |
| 2026-10-30 | ecmwf_ifs025 | 2.4 | 71 | 8.5 | 18.2 |
| 2026-10-31 | ecmwf_ifs025 | 0.2 | 9 | 6.3 | 15.8 |
| 2026-10-25 | ncep_gfs_global | 0.0 | 3 | 14.3 | 24.0 |
| 2026-10-26 | ncep_gfs_global | 0.0 | 0 | 15.2 | 18.6 |
| 2026-10-27 | ncep_gfs_global | 0.0 | 0 | 7.0 | 15.9 |
| 2026-10-28 | ncep_gfs_global | 0.0 | 0 | 5.9 | 13.0 |
| 2026-10-29 | ncep_gfs_global | 1.6 | 43 | 9.3 | 12.9 |
| 2026-10-30 | ncep_gfs_global | 10.8 | 58 | 9.9 | 18.3 |
| 2026-10-31 | ncep_gfs_global | 0.0 | 3 | 4.6 | 11.8 |
| 2026-10-25 | icon_global | 0.0 | 0 | 12.0 | 22.9 |
| 2026-10-26 | icon_global | 0.0 | 0 | 15.5 | 21.2 |
| 2026-10-27 | icon_global | 0.0 | 0 | 6.9 | 16.3 |
| 2026-10-28 | icon_global | 0.0 | 0 | 2.8 | 12.3 |
| 2026-10-29 | icon_global | 0.6 | 46 | 4.4 | 12.5 |
| 2026-10-30 | icon_global | 0.0 | 60 | 9.5 | 19.6 |
| 2026-10-31 | icon_global | 0.0 | 12 | 3.1 | 13.0 |
| 2026-10-25 | gem_global | 0.0 | 5 | 8.5 | 25.0 |
| 2026-10-26 | gem_global | 0.0 | 5 | 12.5 | 22.7 |
| 2026-10-27 | gem_global | 0.0 | 5 | 5.6 | 17.1 |
| 2026-10-28 | gem_global | 0.0 | 0 | 1.3 | 12.2 |
| 2026-10-29 | gem_global | 2.8 | 57 | 0.6 | 14.5 |
| 2026-10-30 | gem_global | 4.4 | 57 | 10.9 | 18.0 |
| 2026-10-31 | gem_global | 0.0 | 8 | 0.6 | 11.7 |

## 기준 충족 신호

- 모델 응답이 불완전해 임계치 미충족으로 단정할 수 없습니다.

## 모델별 원자료 출처

- ecmwf_ifs025: https://api.open-meteo.com/v1/forecast?latitude=37.55&longitude=126.875&timezone=Asia%2FSeoul&forecast_days=7&models=ecmwf_ifs025&hourly=precipitation%2Cprecipitation_probability%2Ctemperature_2m&daily=precipitation_sum%2Cprecipitation_probability_max%2Ctemperature_2m_min%2Ctemperature_2m_max (수집 2026-10-25T22:40:46+09:00)
- ncep_gfs_global: https://api.open-meteo.com/v1/forecast?latitude=37.55&longitude=126.875&timezone=Asia%2FSeoul&forecast_days=7&models=ncep_gfs_global&hourly=precipitation%2Cprecipitation_probability%2Ctemperature_2m&daily=precipitation_sum%2Cprecipitation_probability_max%2Ctemperature_2m_min%2Ctemperature_2m_max (수집 2026-10-25T22:40:47+09:00)
- icon_global: https://api.open-meteo.com/v1/forecast?latitude=37.55&longitude=126.875&timezone=Asia%2FSeoul&forecast_days=7&models=icon_global&hourly=precipitation%2Cprecipitation_probability%2Ctemperature_2m&daily=precipitation_sum%2Cprecipitation_probability_max%2Ctemperature_2m_min%2Ctemperature_2m_max (수집 2026-10-25T22:40:47+09:00)
- gem_global: https://api.open-meteo.com/v1/forecast?latitude=37.55&longitude=126.875&timezone=Asia%2FSeoul&forecast_days=7&models=gem_global&hourly=precipitation%2Cprecipitation_probability%2Ctemperature_2m&daily=precipitation_sum%2Cprecipitation_probability_max%2Ctemperature_2m_min%2Ctemperature_2m_max (수집 2026-10-25T22:40:51+09:00)

## 응답 실패 모델

- kma_gdps: ValueError: API returned empty or all-null precipitation arrays

## 해석 주의

- 서로 다른 모델의 강수량은 독립적인 예측입니다. 한 모델만 기준을 넘으면 단일 모델 신호로 봅니다.
- API 오류 또는 모델 응답 누락이 있으면 전체 판정은 불완전합니다.
- 이 저장소는 예보표를 기록하며, 별도 알림 채널을 설정하지 않으면 휴대전화 푸시/문자 알림을 보내지 않습니다.
