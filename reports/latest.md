# 마포구 7일 다중모델 강수 모니터링

- 확인 시각: 2026-10-21T20:15:29+09:00 (KST)
- 판정: **기준 충족**
- 위치: 서울 마포구 (37.55, 126.875)
- 기준: 시간당 강수량 20mm 이상 또는 일강수량 20mm 이상

| 날짜 | 모델 | 일강수량(mm) | 강수확률 최대(%) | 최저(°C) | 최고(°C) |
|---|---|---:|---:|---:|---:|
| 2026-10-21 | ecmwf_ifs025 | 0.8 | 92 | 7.7 | 15.9 |
| 2026-10-22 | ecmwf_ifs025 | 0.1 | 0 | 5.5 | 13.3 |
| 2026-10-23 | ecmwf_ifs025 | -0.1 | 2 | 7.2 | 20.3 |
| 2026-10-24 | ecmwf_ifs025 | 0.0 | 16 | 12.5 | 18.6 |
| 2026-10-25 | ecmwf_ifs025 | 0.2 | 49 | 11.9 | 23.8 |
| 2026-10-26 | ecmwf_ifs025 | 1.2 | 61 | 15.6 | 22.0 |
| 2026-10-27 | ecmwf_ifs025 | 0.0 | 9 | 4.3 | 16.9 |
| 2026-10-21 | ncep_gfs_global | 0.2 | 77 | 10.1 | 17.9 |
| 2026-10-22 | ncep_gfs_global | 0.0 | 0 | 8.3 | 15.5 |
| 2026-10-23 | ncep_gfs_global | 0.0 | 0 | 10.9 | 19.6 |
| 2026-10-24 | ncep_gfs_global | 0.0 | 3 | 14.7 | 21.3 |
| 2026-10-25 | ncep_gfs_global | 0.0 | 33 | 15.0 | 24.6 |
| 2026-10-26 | ncep_gfs_global | 22.3 | 65 | 15.3 | 20.2 |
| 2026-10-27 | ncep_gfs_global | 0.0 | 10 | 5.2 | 15.3 |
| 2026-10-21 | icon_global | 0.0 | 23 | 7.6 | 16.0 |
| 2026-10-22 | icon_global | 0.0 | 0 | 5.6 | 14.7 |
| 2026-10-23 | icon_global | 0.0 | 3 | 6.2 | 18.7 |
| 2026-10-24 | icon_global | 0.0 | 0 | 12.2 | 19.1 |
| 2026-10-25 | icon_global | 0.3 | 12 | 13.5 | 24.2 |
| 2026-10-26 | icon_global | 36.9 | 44 | 16.0 | 19.6 |
| 2026-10-27 | icon_global | 0.0 | 33 | 5.8 | 16.0 |
| 2026-10-21 | gem_global | 1.1 | 57 | 6.6 | 16.3 |
| 2026-10-22 | gem_global | 0.0 | 0 | 2.3 | 15.1 |
| 2026-10-23 | gem_global | 0.0 | 10 | 1.8 | 21.6 |
| 2026-10-24 | gem_global | 0.1 | 17 | 12.6 | 19.6 |
| 2026-10-25 | gem_global | 0.0 | 20 | 12.1 | 26.9 |
| 2026-10-26 | gem_global | 0.0 | 29 | 10.3 | 21.5 |
| 2026-10-27 | gem_global | 5.7 | 15 | 2.7 | 15.2 |

## 기준 충족 신호

- ncep_gfs_global: 2026-10-26 일강수량 22.3mm
- icon_global: 2026-10-26 일강수량 36.9mm

## 시공업체 전달 문구

마포구 2026-10-26 일강수량 22.3mm 예보(ncep_gfs_global), 지하1층 누수 점검 대기 부탁드립니다.

## 모델별 원자료 출처

- ecmwf_ifs025: https://api.open-meteo.com/v1/forecast?latitude=37.55&longitude=126.875&timezone=Asia%2FSeoul&forecast_days=7&models=ecmwf_ifs025&hourly=precipitation%2Cprecipitation_probability%2Ctemperature_2m&daily=precipitation_sum%2Cprecipitation_probability_max%2Ctemperature_2m_min%2Ctemperature_2m_max (수집 2026-10-21T20:14:51+09:00)
- ncep_gfs_global: https://api.open-meteo.com/v1/forecast?latitude=37.55&longitude=126.875&timezone=Asia%2FSeoul&forecast_days=7&models=ncep_gfs_global&hourly=precipitation%2Cprecipitation_probability%2Ctemperature_2m&daily=precipitation_sum%2Cprecipitation_probability_max%2Ctemperature_2m_min%2Ctemperature_2m_max (수집 2026-10-21T20:14:52+09:00)
- icon_global: https://api.open-meteo.com/v1/forecast?latitude=37.55&longitude=126.875&timezone=Asia%2FSeoul&forecast_days=7&models=icon_global&hourly=precipitation%2Cprecipitation_probability%2Ctemperature_2m&daily=precipitation_sum%2Cprecipitation_probability_max%2Ctemperature_2m_min%2Ctemperature_2m_max (수집 2026-10-21T20:14:53+09:00)
- gem_global: https://api.open-meteo.com/v1/forecast?latitude=37.55&longitude=126.875&timezone=Asia%2FSeoul&forecast_days=7&models=gem_global&hourly=precipitation%2Cprecipitation_probability%2Ctemperature_2m&daily=precipitation_sum%2Cprecipitation_probability_max%2Ctemperature_2m_min%2Ctemperature_2m_max (수집 2026-10-21T20:15:29+09:00)

## 응답 실패 모델

- kma_gdps: URLError: <urlopen error _ssl.c:993: The handshake operation timed out>

## 해석 주의

- 서로 다른 모델의 강수량은 독립적인 예측입니다. 한 모델만 기준을 넘으면 단일 모델 신호로 봅니다.
- API 오류 또는 모델 응답 누락이 있으면 전체 판정은 불완전합니다.
- 이 저장소는 예보표를 기록하며, 별도 알림 채널을 설정하지 않으면 휴대전화 푸시/문자 알림을 보내지 않습니다.
