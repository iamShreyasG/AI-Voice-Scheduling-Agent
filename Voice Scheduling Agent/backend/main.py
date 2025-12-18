from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime, timedelta

from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build

# ---------- CONFIG ----------
SCOPES = ["https://www.googleapis.com/auth/calendar"]
SERVICE_ACCOUNT_FILE = "service_account.json"

# ---------- GOOGLE CALENDAR ----------
credentials = Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE,
    scopes=SCOPES
)

service = build("calendar", "v3", credentials=credentials)

# ---------- FASTAPI ----------
app = FastAPI()


# ---------- REQUEST MODEL ----------
class EventRequest(BaseModel):
    name: str
    date: str      # YYYY-MM-DD
    time: str      # HH:MM (24h)
    title: str = "Meeting"


# ---------- CREATE EVENT ----------
@app.post("/create-event")
def create_event(data: EventRequest):
    start_dt = datetime.strptime(
        f"{data.date} {data.time}",
        "%Y-%m-%d %H:%M"
    )

    end_dt = start_dt + timedelta(minutes=30)

    event = {
        "summary": data.title,
        "description": f"Scheduled by {data.name}",
        "start": {
            "dateTime": start_dt.isoformat(),
            "timeZone": "Asia/Kolkata"
        },
        "end": {
            "dateTime": end_dt.isoformat(),
            "timeZone": "Asia/Kolkata"
        }
    }

    service.events().insert(
        calendarId="shreyas.bvg@gmail.com",
        body=event
    ).execute()

    return {"status": "success"}


# ---------- LIST EVENTS ----------
@app.get("/list-events")
def list_events():
    events = service.events().list(
        calendarId="shreyas.bvg@gmail.com",
        maxResults=10,
        singleEvents=True,
        orderBy="startTime"
    ).execute()

    return events

