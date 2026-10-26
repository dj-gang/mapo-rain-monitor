# 서울 강수 알림

매일 오전 9시(KST) 여러 예보원의 7일 일강수량 예보를 모아, 하루 20mm 이상 예보가 있는 날을 텔레그램으로 알립니다.

## 예보원

| 예보원 | 출처 | 키 |
|---|---|---|
| ECMWF, ECMWF AIFS, GFS, ICON, GEM, 일본기상청(JMA), 영국기상청(UKMO), 한국기상청 GDPS | [Open-Meteo](https://open-meteo.com/en/docs) `models=` | 불필요 |
| 한국기상청 단기예보 (약 3일) | [공공데이터포털 VilageFcstInfoService_2.0](https://www.data.go.kr/data/15084084/openapi.do) | `KMA_SERVICE_KEY` |

- 판정: 예보원별 일강수량 ≥ 기준값이면 "N곳 중 M곳" 으로 집계합니다.
- 한 예보원이 실패해도 나머지로 판정하고, 실패한 예보원은 메시지에 표시합니다.
- 기상청 PCP의 범위 표기(`30.0~50.0mm`, `50.0mm 이상`)는 하한값, `1mm 미만`은 0.5mm로 합산합니다.
- 애플날씨·아큐웨더는 유료 API라 포함하지 않았습니다.

## 설정 (Settings → Secrets and variables → Actions)

Secrets
- `TELEGRAM_BOT_TOKEN`, `TELEGRAM_CHAT_ID` (필수)
- `KMA_SERVICE_KEY` (선택, 포털의 Decoding/Encoding 키 모두 가능)

Variables (선택)
- `LOCATION_NAME`, `LATITUDE`, `LONGITUDE` — 기본 서울시청(37.5665, 126.9780)
- `THRESHOLD_MM` — 기본 20
- `ALERT_ONLY` — `1`이면 기준 충족일 때만 전송

## 실행 시각

GitHub Actions `schedule`은 부하 시 지연·누락될 수 있습니다([문서](https://docs.github.com/en/actions/writing-workflows/choosing-when-your-workflow-runs/events-that-trigger-workflows#schedule)).
그래서 09:00 정시 실행은 외부 크론이 `workflow_dispatch`를 호출하고, `schedule`(09:13 / 09:47 / 10:27)은 그날 성공 실행이 없을 때만 동작하는 백업입니다.

외부 크론 설정 (예: [cron-job.org](https://cron-job.org), 시간대 Asia/Seoul, 매일 09:00):
- URL: `https://api.github.com/repos/<owner>/<repo>/actions/workflows/monitor.yml/dispatches`
- Method: `POST`
- Headers: `Authorization: Bearer <fine-grained PAT, 이 저장소 Actions: Read and write>`, `Accept: application/vnd.github+json`
- Body: `{"ref":"main"}`

## 로컬 실행

```sh
DRY_RUN=1 python scripts/rain_alert.py
python -m unittest discover -s tests
```
