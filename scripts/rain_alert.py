#!/usr/bin/env python3
"""여러 예보원의 일강수량 예보를 모아 서울에 하루 20mm 이상 비 예보가 있는지 알린다.

표준 라이브러리만 사용한다.

환경 변수
  TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID  텔레그램 전송 (없으면 전송 생략)
  KMA_SERVICE_KEY                       공공데이터포털 기상청 단기예보 키 (없으면 KMA 생략)
  LOCATION_NAME, LATITUDE, LONGITUDE    지점 (기본: 서울시청)
  THRESHOLD_MM                          기준 일강수량 (기본 20)
  ALERT_ONLY=1                          기준 충족 시에만 전송
  DRY_RUN=1                             텔레그램 전송 없이 출력만
"""
import html
import json
import math
import os
import re
import sys
import time
from datetime import datetime, timedelta
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import unquote, urlencode
from urllib.request import Request, urlopen
from zoneinfo import ZoneInfo

KST = ZoneInfo("Asia/Seoul")
LOCATION_NAME = os.environ.get("LOCATION_NAME") or "서울 중구(시청)"
LAT = float(os.environ.get("LATITUDE") or 37.5665)
LON = float(os.environ.get("LONGITUDE") or 126.9780)
THRESHOLD_MM = float(os.environ.get("THRESHOLD_MM") or 20)
FORECAST_DAYS = 7
WEEKDAYS = "월화수목금토일"

OPEN_METEO_URL = "https://api.open-meteo.com/v1/forecast"
# (Open-Meteo 모델 ID, 표시 이름, 표 머리글)
OPEN_METEO_MODELS = [
    ("ecmwf_ifs025", "ECMWF", "ECMW"),
    ("ecmwf_aifs025_single", "ECMWF AIFS", "AIFS"),
    ("ncep_gfs_global", "GFS", "GFS"),
    ("icon_global", "ICON", "ICON"),
    ("gem_global", "GEM", "GEM"),
    ("jma_gsm", "일본기상청", "JMA"),
    ("ukmo_global_deterministic_10km", "영국기상청", "UKMO"),
]
KMA_URL = "https://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getVilageFcst"
KMA_BASE_HOURS = (2, 5, 8, 11, 14, 17, 20, 23)


def log(message):
    print(f"[{datetime.now(KST):%H:%M:%S}] {message}", flush=True)


def http_get_json(url, attempts=3, timeout=30):
    last = None
    for attempt in range(attempts):
        try:
            req = Request(url, headers={"User-Agent": "seoul-rain-alert/2.0"})
            with urlopen(req, timeout=timeout) as resp:
                raw = resp.read().decode("utf-8")
            try:
                return json.loads(raw)
            except json.JSONDecodeError:
                # 기상청 API는 키 오류 등을 JSON 요청에도 XML로 돌려준다.
                raise ValueError(f"JSON 아님: {raw[:200]!r}")
        except HTTPError as exc:
            body = exc.read().decode("utf-8", errors="replace")[:300]
            last = f"HTTP {exc.code}: {body}"
            if 400 <= exc.code < 500 and exc.code != 429:
                break
        except (URLError, TimeoutError, OSError, ValueError) as exc:
            last = f"{type(exc).__name__}: {exc}"
        if attempt < attempts - 1:
            time.sleep(2 ** attempt)
    raise RuntimeError(last)


def fetch_open_meteo(model):
    params = {
        "latitude": LAT, "longitude": LON, "timezone": "Asia/Seoul",
        "forecast_days": FORECAST_DAYS, "daily": "precipitation_sum", "models": model,
    }
    data = http_get_json(OPEN_METEO_URL + "?" + urlencode(params))
    daily = data.get("daily") or {}
    dates = daily.get("time") or []
    values = daily.get("precipitation_sum") or []
    result = {d: (None if v is None else max(0.0, float(v))) for d, v in zip(dates, values)}
    if not any(v is not None for v in result.values()):
        raise RuntimeError("강수량 값이 모두 비어 있음")
    return result


def latlon_to_kma_grid(lat, lon):
    """위경도를 기상청 동네예보 격자(nx, ny)로 변환 (기상청 LCC DFS 공식)."""
    re_, grid = 6371.00877, 5.0
    slat1, slat2, olon, olat = map(math.radians, (30.0, 60.0, 126.0, 38.0))
    xo, yo = 43, 136
    re_ /= grid
    sn = math.log(math.cos(slat1) / math.cos(slat2)) / math.log(
        math.tan(math.pi * 0.25 + slat2 * 0.5) / math.tan(math.pi * 0.25 + slat1 * 0.5))
    sf = math.tan(math.pi * 0.25 + slat1 * 0.5) ** sn * math.cos(slat1) / sn
    ro = re_ * sf / math.tan(math.pi * 0.25 + olat * 0.5) ** sn
    ra = re_ * sf / math.tan(math.pi * 0.25 + math.radians(lat) * 0.5) ** sn
    theta = math.radians(lon) - olon
    if theta > math.pi:
        theta -= 2 * math.pi
    if theta < -math.pi:
        theta += 2 * math.pi
    theta *= sn
    return int(ra * math.sin(theta) + xo + 0.5), int(ro - ra * math.cos(theta) + yo + 0.5)


def kma_base_time(now):
    """API 제공 시각(발표 후 약 10분)을 지난 가장 최근 발표 시각."""
    ready = now - timedelta(minutes=15)
    for day_offset in (0, 1):
        day = ready - timedelta(days=day_offset)
        for hour in reversed(KMA_BASE_HOURS):
            base = day.replace(hour=hour, minute=0, second=0, microsecond=0)
            if base <= ready:
                return base
    raise AssertionError("unreachable")


def parse_kma_pcp(value):
    """기상청 1시간 강수량(PCP) 문자열을 mm로. 범위 표기는 하한값을 쓴다.

    "강수없음" -> 0, "1mm 미만"/"1.0mm 미만" -> 0.5, "6.0mm" -> 6.0,
    "30.0~50.0mm" -> 30.0, "50.0mm 이상" -> 50.0
    """
    text = str(value).strip()
    if text in ("", "강수없음", "0", "-"):
        return 0.0
    if "미만" in text:
        return 0.5
    match = re.search(r"\d+(?:\.\d+)?", text)
    if not match:
        raise ValueError(f"알 수 없는 PCP 값: {text!r}")
    return float(match.group())


def fetch_kma(service_key, now):
    nx, ny = latlon_to_kma_grid(LAT, LON)
    base = kma_base_time(now)
    # 포털의 Encoding 키를 넣어도 이중 인코딩되지 않도록 한 번 풀어 둔다.
    key = unquote(service_key.strip()) if "%" in service_key else service_key.strip()
    items, page = [], 1
    while True:
        params = {
            "serviceKey": key, "dataType": "JSON", "numOfRows": 1000, "pageNo": page,
            "base_date": f"{base:%Y%m%d}", "base_time": f"{base:%H%M}", "nx": nx, "ny": ny,
        }
        data = http_get_json(KMA_URL + "?" + urlencode(params))
        header = data.get("response", {}).get("header", {})
        if header.get("resultCode") != "00":
            raise RuntimeError(f"KMA {header.get('resultCode')}: {header.get('resultMsg')}")
        body = data["response"]["body"]
        items += body["items"]["item"]
        if len(items) >= int(body.get("totalCount", 0)):
            break
        page += 1
    daily = {}
    for item in items:
        if item.get("category") != "PCP":
            continue
        date = f"{item['fcstDate'][:4]}-{item['fcstDate'][4:6]}-{item['fcstDate'][6:]}"
        daily[date] = daily.get(date, 0.0) + parse_kma_pcp(item["fcstValue"])
    if not daily:
        raise RuntimeError("PCP 항목 없음")
    log(f"KMA base={base:%Y-%m-%d %H:%M} nx={nx} ny={ny} days={sorted(daily)}")
    return daily, base


def collect(now):
    sources = []
    for model, name, short in OPEN_METEO_MODELS:
        entry = {"name": name, "short": short, "id": f"open-meteo:{model}", "daily": {}, "error": None}
        try:
            entry["daily"] = fetch_open_meteo(model)
            log(f"OK   {name}")
        except RuntimeError as exc:
            entry["error"] = str(exc)[:200]
            log(f"FAIL {name}: {entry['error']}")
        sources.append(entry)
    key = os.environ.get("KMA_SERVICE_KEY", "")
    if key:
        entry = {"name": "한국기상청 단기예보", "short": "KMA", "id": "kma:vilage", "daily": {}, "error": None}
        try:
            entry["daily"], base = fetch_kma(key, now)
            entry["note"] = f"{base:%m/%d %H}시 발표, 당일은 발표 이후 시간만 합산"
            log(f"OK   {entry['name']}")
        except RuntimeError as exc:
            entry["error"] = str(exc)[:200]
            log(f"FAIL {entry['name']}: {entry['error']}")
        sources.insert(0, entry)
    return sources


def evaluate(sources, today, threshold=THRESHOLD_MM):
    days = []
    for offset in range(FORECAST_DAYS):
        date = (today + timedelta(days=offset)).isoformat()
        values = {s["name"]: s["daily"].get(date) for s in sources}
        known = {k: v for k, v in values.items() if v is not None}
        hits = {k: v for k, v in known.items() if v >= threshold}
        days.append({
            "date": date, "values": values, "available": len(known),
            "hits": dict(sorted(hits.items(), key=lambda kv: -kv[1])),
            "max": max(known.values()) if known else None,
        })
    return days


def day_label(date):
    d = datetime.strptime(date, "%Y-%m-%d")
    return f"{d:%m/%d}({WEEKDAYS[d.weekday()]})"


def build_message(sources, days, now):
    ok = [s for s in sources if not s["error"]]
    alert_days = [d for d in days if d["hits"]]
    thr = f"{THRESHOLD_MM:g}mm"
    if alert_days:
        lines = [f"🚨 <b>서울 일강수량 {thr} 이상 예보</b>"]
    else:
        lines = [f"✅ <b>7일간 일강수량 {thr} 이상 예보 없음</b>"]
    lines += [
        f"{html.escape(LOCATION_NAME)} · {now:%Y-%m-%d %H:%M} KST · 예보원 {len(ok)}/{len(sources)} 응답",
        "",
    ]
    for d in alert_days:
        hit_text = ", ".join(f"{html.escape(k)} {v:.1f}" for k, v in d["hits"].items())
        lines.append(f"• <b>{day_label(d['date'])}</b> {d['available']}곳 중 <b>{len(d['hits'])}곳</b> ≥{thr}")
        lines.append(f"  {hit_text}")
    if alert_days:
        lines.append("")

    # 휴대폰 폭에 맞춰 행=예보원, 열=날짜. 단위 mm, '-'는 값 없음.
    header = "      " + "".join(f"{d['date'][8:]:>5}" for d in days)
    table = [header]
    for s in ok:
        cells = []
        for d in days:
            v = s["daily"].get(d["date"])
            cells.append("    -" if v is None else f"{v:5.0f}" if v >= 10 else f"{v:5.1f}")
        mark = "*" if any((s["daily"].get(d["date"]) or 0) >= THRESHOLD_MM for d in days) else " "
        table.append(f"{s['short'][:4]:<4}{mark} " + "".join(cells))
    lines.append(f"<b>일강수량(mm)</b> · {day_label(days[0]['date'])}~{day_label(days[-1]['date'])}")
    lines.append("<pre>" + html.escape("\n".join(table)) + "</pre>")
    notes = [f"{s['short']}: {s['note']}" for s in ok if s.get("note")]
    if notes:
        lines += [html.escape(n) for n in notes]
    failed = [s for s in sources if s["error"]]
    if failed:
        lines.append("⚠️ 응답 실패: " + ", ".join(html.escape(f"{s['name']}({s['error'][:60]})") for s in failed))
    return "\n".join(lines)


def send_telegram(text):
    token = os.environ["TELEGRAM_BOT_TOKEN"]
    body = json.dumps({
        "chat_id": os.environ["TELEGRAM_CHAT_ID"], "text": text,
        "parse_mode": "HTML", "disable_web_page_preview": True,
    }).encode()
    req = Request(f"https://api.telegram.org/bot{token}/sendMessage", data=body,
                  headers={"Content-Type": "application/json"}, method="POST")
    try:
        with urlopen(req, timeout=20) as resp:
            result = json.loads(resp.read().decode())
    except HTTPError as exc:
        raise RuntimeError(f"Telegram HTTP {exc.code}: {exc.read().decode(errors='replace')[:300]}")
    if not result.get("ok"):
        raise RuntimeError(f"Telegram ok=false: {result.get('description')}")


def main():
    now = datetime.now(KST)
    log(f"START {LOCATION_NAME} ({LAT}, {LON}) threshold={THRESHOLD_MM:g}mm")
    sources = collect(now)
    days = evaluate(sources, now.date())
    ok_count = sum(1 for s in sources if not s["error"])
    message = build_message(sources, days, now)
    if ok_count == 0:
        message = "❌ <b>서울 강수 알림: 모든 예보원 응답 실패</b>\n" + message

    out = Path("out")
    out.mkdir(exist_ok=True)
    (out / "report.json").write_text(json.dumps({
        "generated_at_kst": now.isoformat(timespec="seconds"),
        "location": {"name": LOCATION_NAME, "lat": LAT, "lon": LON},
        "threshold_mm": THRESHOLD_MM, "sources": sources, "days": days,
    }, ensure_ascii=False, indent=2), encoding="utf-8")
    print(message)

    has_alert = any(d["hits"] for d in days)
    dry = os.environ.get("DRY_RUN") == "1"
    alert_only = os.environ.get("ALERT_ONLY") == "1"
    if dry:
        log("DRY_RUN: 텔레그램 전송 생략")
    elif not (os.environ.get("TELEGRAM_BOT_TOKEN") and os.environ.get("TELEGRAM_CHAT_ID")):
        log("텔레그램 secrets 없음: 전송 생략")
        return 1
    elif alert_only and not has_alert and ok_count:
        log("ALERT_ONLY: 기준 충족 없음, 전송 생략")
    else:
        send_telegram(message)
        log("텔레그램 전송 완료")
    return 0 if ok_count else 1


if __name__ == "__main__":
    sys.exit(main())
