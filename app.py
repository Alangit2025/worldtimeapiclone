from fastapi import FastAPI
from datetime import datetime
from zoneinfo import ZoneInfo

app = FastAPI()

@app.get("/")
def root():
    return {"mensaje": "API working correctly"}

@app.get("/api/time/{timezone}")
def get_time(timezone: str):
    try:
        tz = ZoneInfo(timezone)
        now = datetime.now(tz)
        return {
            "timezone": timezone,
            "datetime": now.isoformat(),
            "utc_offset_hours": now.utcoffset().total_seconds() / 3600,
            "day_of_week": now.strftime("%A"),
            "day_of_year": now.timetuple().tm_yday,
            "unixtime": int(now.timestamp())
        }
    except Exception:
        return {"detail": "Zona horaria no válida"}
