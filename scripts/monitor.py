#!/usr/bin/env python3
"""Fetch 7-day precipitation and temperature forecasts for Mapo-gu, Seoul."""
import json
import os
import sys
import time
from datetime import datetime
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode
from urllib.request import Request, urlopen
from zoneinfo import ZoneInfo

LAT, LON = 37.55, 126.875
TZ = "Asia/Seoul"
MODELS = [
    "ecmwf_ifs025",
    "ncep_gfs_global",
    "icon_global",
    "kma_gdps",
    "gem_global",
]
BASE = "https://api.open-meteo.com/v1/forecast"
HOURLY = "precipitation,precipitation_probability,temperature_2m"
DAILY = "precipitation_sum,precipitation_probability_max,temperature_2m_min,temperature_2m_max"
OUT = Path("reports")
OUT.mkdir(exist_ok=True)

def fetch(model):
    params = {
        "latitude": LAT, "longitude": LON, "timezone": TZ,
        "forecast_days": 7, "models": model,
        "hourly": HOURLY, "daily": DAILY,
    }
    url = BASE + "?" + urlencode(params)
    req = Request(url, headers={"User-Agent": "mapo-rain-monitor/1.0"})
    last = None
    for attempt in range(3):
        try:
            with urlopen(req, timeout=30) as resp:
                payload = json.loads(resp.read().decode("utf-8"))
            daily = payload.get("daily") or {}
            hourly = payload.get("hourly") or {}
            daily_rain = daily.get("precipitation_sum") or []
            hourly_rain = hourly.get("precipitation") or []
            # A 200 response with empty/all-null core arrays is not valid forecast data.
            valid_daily = any(v is not None for v in daily_rain)
            valid_hourly = any(v is not None for v in hourly_rain)
            if not (daily.get("time") and (valid_daily or valid_hourly)):
                raise ValueError("API returned empty or all-null precipitation arrays")
            payload["_source_url"] = url
            payload["_retrieved_at_kst"] = datetime.now(ZoneInfo(TZ)).isoformat(timespec="seconds")
            payload["_requested_model"] = model
            return payload, None
        except (HTTPError, URLError, TimeoutError, json.JSONDecodeError, OSError, ValueError) as exc:
            last = f"{type(exc).__name__}: {exc}"
            if attempt < 2:
                time.sleep(2 ** attempt)
    return None, last

def fmt(value, digits=1):
    return "확인 불가" if value is None else f"{value:.{digits}f}"

def analyze(payload):
    daily = payload.get("daily", {})
    hourly = payload.get("hourly", {})
    daily_dates = daily.get("time", [])
    totals = daily.get("precipitation_sum", [])
    tmins = daily.get("temperature_2m_min", [])
    tmaxs = daily.get("temperature_2m_max", [])
    probs = daily.get("precipitation_probability_max", [])
    hours = hourly.get("time", [])
    rain = hourly.get("precipitation", [])
    prob = hourly.get("precipitation_probability", [])
    t = hourly.get("temperature_2m", [])
    hourly_peaks = []
    for i, val in enumerate(rain):
        if val is not None and val >= 20:
            hourly_peaks.append({"time": hours[i], "mm": val,
                                 "probability": prob[i] if i < len(prob) else None})
    daily_peaks = [{"date": d, "mm": v} for d, v in zip(daily_dates, totals)
                   if v is not None and v >= 20]
    return {
        "daily": [
            {"date": d, "precipitation_mm": totals[i] if i < len(totals) else None,
             "precipitation_probability_max_pct": probs[i] if i < len(probs) else None,
             "temperature_min_c": tmins[i] if i < len(tmins) else None,
             "temperature_max_c": tmaxs[i] if i < len(tmaxs) else None}
            for i, d in enumerate(daily_dates)
        ],
        "hourly_peaks_ge_20mm": hourly_peaks,
        "daily_peaks_ge_20mm": daily_peaks,
    }

results, failures = {}, {}
for model in MODELS:
    payload, error = fetch(model)
    if error:
        failures[model] = error
    else:
        results[model] = {"payload": payload, "analysis": analyze(payload)}

now = datetime.now(ZoneInfo(TZ))
all_peaks = []
for model, result in results.items():
    for item in result["analysis"]["hourly_peaks_ge_20mm"]:
        all_peaks.append({"model": model, "type": "hourly", **item})
    for item in result["analysis"]["daily_peaks_ge_20mm"]:
        all_peaks.append({"model": model, "type": "daily", **item})

if all_peaks:
    status = "기준 충족"
elif results and not failures:
    status = "기준 미충족"
else:
    status = "판정 불가" if not results else "판정 불가 (일부 모델 응답 실패)"

report = {
    "generated_at_kst": now.isoformat(timespec="seconds"),
    "location": {"name": "서울 마포구", "latitude": LAT, "longitude": LON},
    "thresholds": {"hourly_precipitation_mm_gte": 20, "daily_precipitation_mm_gte": 20},
    "status": status,
    "successful_models": list(results.keys()),
    "failed_models": failures,
    "models": {m: {"analysis": r["analysis"], "source_url": r["payload"]["_source_url"],
                   "retrieved_at_kst": r["payload"]["_retrieved_at_kst"],
                   "api_model": r["payload"].get("model"),
                   "hourly_units": r["payload"].get("hourly_units"),
                   "daily_units": r["payload"].get("daily_units")}
               for m, r in results.items()},
    "threshold_events": all_peaks,
}
(OUT / "latest.json").write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")

lines = [
    "# 마포구 7일 다중모델 강수 모니터링",
    "",
    f"- 확인 시각: {report['generated_at_kst']} (KST)",
    f"- 판정: **{status}**",
    "- 위치: 서울 마포구 (37.55, 126.875)",
    "- 기준: 시간당 강수량 20mm 이상 또는 일강수량 20mm 이상",
    "",
    "| 날짜 | 모델 | 일강수량(mm) | 강수확률 최대(%) | 최저(°C) | 최고(°C) |",
    "|---|---|---:|---:|---:|---:|",
]
for model, result in results.items():
    for row in result["analysis"]["daily"]:
        lines.append("| {date} | {model} | {rain} | {prob} | {low} | {high} |".format(
            date=row["date"], model=model,
            rain=fmt(row["precipitation_mm"]),
            prob="확인 불가" if row["precipitation_probability_max_pct"] is None else str(row["precipitation_probability_max_pct"]),
            low=fmt(row["temperature_min_c"]), high=fmt(row["temperature_max_c"])))
lines += ["", "## 기준 충족 신호", ""]
if all_peaks:
    for event in all_peaks:
        if event["type"] == "hourly":
            lines.append(f"- {event['model']}: {event['time']} 시간당 {event['mm']}mm (강수확률 {event.get('probability') if event.get('probability') is not None else '확인 불가'}%)")
        else:
            lines.append(f"- {event['model']}: {event['date']} 일강수량 {event['mm']}mm")
    first = all_peaks[0]
    when = first.get("time", first.get("date", "일시 확인 필요"))
    amount = first.get("mm", "확인 불가")
    if first["type"] == "hourly":
        contractor = f"마포구 {when} 시간당 최대 {amount}mm 예보({first['model']}), 지하1층 누수 점검 대기 부탁드립니다."
    else:
        contractor = f"마포구 {when} 일강수량 {amount}mm 예보({first['model']}), 지하1층 누수 점검 대기 부탁드립니다."
    lines += ["", "## 시공업체 전달 문구", "", contractor]
else:
    lines.append("- 확인된 임계치 초과 없음." if results and not failures else "- 모델 응답이 불완전해 임계치 미충족으로 단정할 수 없습니다.")
lines += ["", "## 모델별 원자료 출처", ""]
for model, result in results.items():
    lines.append(f"- {model}: {result['payload']['_source_url']} (수집 {result['payload']['_retrieved_at_kst']})")
if failures:
    lines += ["", "## 응답 실패 모델", ""]
    for model, err in failures.items():
        lines.append(f"- {model}: {err}")
lines += ["", "## 해석 주의", "",
          "- 서로 다른 모델의 강수량은 독립적인 예측입니다. 한 모델만 기준을 넘으면 단일 모델 신호로 봅니다.",
          "- API 오류 또는 모델 응답 누락이 있으면 전체 판정은 불완전합니다.",
          "- 이 저장소는 예보표를 기록하며, 별도 알림 채널을 설정하지 않으면 휴대전화 푸시/문자 알림을 보내지 않습니다."]
(OUT / "latest.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
print(f"Status: {status}; successful={len(results)}; failed={len(failures)}")
# Keep exit status successful after writing a "판정 불가" report so the workflow
# can still save and notify the user about API outages.
