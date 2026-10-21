# 마포구 7일 다중모델 강수 모니터링

- 확인 시각: 2026-10-21T10:41:16+09:00 (KST)
- 판정: **기준 충족**
- 위치: 서울 마포구 (37.55, 126.875)
- 기준: 시간당 강수량 20mm 이상 또는 일강수량 20mm 이상

| 날짜 | 모델 | 일강수량(mm) | 강수확률 최대(%) | 최저(°C) | 최고(°C) |
|---|---|---:|---:|---:|---:|
| 2026-10-21 | ecmwf_ifs025 | 0.1 | 45 | 7.9 | 15.7 |
| 2026-10-22 | ecmwf_ifs025 | 0.0 | 0 | 5.5 | 13.2 |
| 2026-10-23 | ecmwf_ifs025 | 0.1 | 1 | 7.2 | 18.9 |
| 2026-10-24 | ecmwf_ifs025 | 0.0 | 18 | 12.8 | 18.2 |
| 2026-10-25 | ecmwf_ifs025 | 3.1 | 60 | 13.6 | 19.8 |
| 2026-10-26 | ecmwf_ifs025 | 26.9 | 57 | 13.9 | 18.9 |
| 2026-10-27 | ecmwf_ifs025 | 0.0 | 14 | 5.8 | 15.7 |
| 2026-10-21 | ncep_gfs_global | 0.2 | 77 | 10.2 | 17.9 |
| 2026-10-22 | ncep_gfs_global | 0.0 | 0 | 8.2 | 15.5 |
| 2026-10-23 | ncep_gfs_global | 0.0 | 0 | 11.1 | 19.2 |
| 2026-10-24 | ncep_gfs_global | 0.0 | 6 | 15.1 | 21.4 |
| 2026-10-25 | ncep_gfs_global | 0.0 | 40 | 15.1 | 23.2 |
| 2026-10-26 | ncep_gfs_global | 13.9 | 65 | 14.6 | 18.9 |
| 2026-10-27 | ncep_gfs_global | 0.0 | 0 | 5.9 | 15.4 |
| 2026-10-21 | icon_global | 0.0 | 확인 불가 | 7.5 | 16.0 |
| 2026-10-22 | icon_global | 0.0 | 확인 불가 | 5.1 | 14.3 |
| 2026-10-23 | icon_global | 0.0 | 확인 불가 | 5.9 | 19.6 |
| 2026-10-24 | icon_global | 0.0 | 확인 불가 | 12.2 | 18.8 |
| 2026-10-25 | icon_global | 1.1 | 확인 불가 | 13.0 | 21.3 |
| 2026-10-26 | icon_global | 16.3 | 확인 불가 | 16.3 | 17.4 |
| 2026-10-27 | icon_global | 0.0 | 확인 불가 | 10.2 | 16.5 |
| 2026-10-21 | kma_gdps | 확인 불가 | 확인 불가 | 확인 불가 | 확인 불가 |
| 2026-10-22 | kma_gdps | 확인 불가 | 확인 불가 | 확인 불가 | 확인 불가 |
| 2026-10-23 | kma_gdps | 확인 불가 | 확인 불가 | 확인 불가 | 확인 불가 |
| 2026-10-24 | kma_gdps | 확인 불가 | 확인 불가 | 확인 불가 | 확인 불가 |
| 2026-10-25 | kma_gdps | 확인 불가 | 확인 불가 | 확인 불가 | 확인 불가 |
| 2026-10-26 | kma_gdps | 확인 불가 | 확인 불가 | 확인 불가 | 확인 불가 |
| 2026-10-27 | kma_gdps | 확인 불가 | 확인 불가 | 확인 불가 | 확인 불가 |
| 2026-10-21 | gem_global | 1.2 | 57 | 7.1 | 15.7 |
| 2026-10-22 | gem_global | 0.0 | 0 | 1.9 | 14.6 |
| 2026-10-23 | gem_global | 0.0 | 5 | 1.8 | 21.8 |
| 2026-10-24 | gem_global | 0.0 | 24 | 12.1 | 20.0 |
| 2026-10-25 | gem_global | 0.6 | 24 | 12.5 | 26.8 |
| 2026-10-26 | gem_global | 0.0 | 39 | 11.5 | 21.5 |
| 2026-10-27 | gem_global | 0.0 | 19 | 7.3 | 18.3 |

## 기준 충족 신호

- ecmwf_ifs025: 2026-10-26 일강수량 26.9mm

## 시공업체 전달 문구

마포구 2026-10-26 시간당 최대 26.9mm 예보, 지하1층 누수 점검 대기 부탁드립니다.

※ 일강수량 기준만 충족한 경우에도 위 문구의 시간당 수치는 일강수량을 뜻하지 않으므로, 전달 전 시간당 예보를 확인하세요.

## 모델별 원자료 출처

- ecmwf_ifs025: https://api.open-meteo.com/v1/forecast?latitude=37.55&longitude=126.875&timezone=Asia%2FSeoul&forecast_days=7&models=ecmwf_ifs025&hourly=precipitation%2Cprecipitation_probability%2Ctemperature_2m&daily=precipitation_sum%2Cprecipitation_probability_max%2Ctemperature_2m_min%2Ctemperature_2m_max (수집 2026-10-21T10:41:15+09:00)
- ncep_gfs_global: https://api.open-meteo.com/v1/forecast?latitude=37.55&longitude=126.875&timezone=Asia%2FSeoul&forecast_days=7&models=ncep_gfs_global&hourly=precipitation%2Cprecipitation_probability%2Ctemperature_2m&daily=precipitation_sum%2Cprecipitation_probability_max%2Ctemperature_2m_min%2Ctemperature_2m_max (수집 2026-10-21T10:41:15+09:00)
- icon_global: https://api.open-meteo.com/v1/forecast?latitude=37.55&longitude=126.875&timezone=Asia%2FSeoul&forecast_days=7&models=icon_global&hourly=precipitation%2Cprecipitation_probability%2Ctemperature_2m&daily=precipitation_sum%2Cprecipitation_probability_max%2Ctemperature_2m_min%2Ctemperature_2m_max (수집 2026-10-21T10:41:15+09:00)
- kma_gdps: https://api.open-meteo.com/v1/forecast?latitude=37.55&longitude=126.875&timezone=Asia%2FSeoul&forecast_days=7&models=kma_gdps&hourly=precipitation%2Cprecipitation_probability%2Ctemperature_2m&daily=precipitation_sum%2Cprecipitation_probability_max%2Ctemperature_2m_min%2Ctemperature_2m_max (수집 2026-10-21T10:41:16+09:00)
- gem_global: https://api.open-meteo.com/v1/forecast?latitude=37.55&longitude=126.875&timezone=Asia%2FSeoul&forecast_days=7&models=gem_global&hourly=precipitation%2Cprecipitation_probability%2Ctemperature_2m&daily=precipitation_sum%2Cprecipitation_probability_max%2Ctemperature_2m_min%2Ctemperature_2m_max (수집 2026-10-21T10:41:16+09:00)

## 해석 주의

- 서로 다른 모델의 강수량은 독립적인 예측입니다. 한 모델만 기준을 넘으면 단일 모델 신호로 봅니다.
- API 오류 또는 모델 응답 누락이 있으면 전체 판정은 불완전합니다.
- 이 저장소는 예보표를 기록하며, 별도 알림 채널을 설정하지 않으면 휴대전화 푸시/문자 알림을 보내지 않습니다.
