# AI-Voice-Scheduling-Agent
A real-time voice scheduling assistant that interacts with users conversationally and creates meetings directly in Google Calendar after confirmation.

---

## Overview

This project implements a voice-based AI assistant that:

* Initiates a conversation with the user
* Collects meeting details using natural language
* Confirms details before scheduling
* Creates a real Google Calendar event
* Works through a deployed backend URL

---

## Features

* Voice-driven conversation flow
* Natural language date and time handling
* Automatic conversion to calendar-compatible formats
* Google Calendar event creation
* Secure backend integration

---

## Deployed Backend URL

```
https://miss-resiniferous-bethany.ngrok-free.dev
```

This URL is connected to the voice agent for scheduling meetings.

---

## How to Test the Agent

1. Open the voice agent interface
2. Speak naturally (no specific format required)

   * Example:

     * “My name is Shreyas”
     * “Tomorrow”
     * “10:30 in the morning”
     * “Project discussion”
3. Confirm the details when the assistant repeats them
4. The meeting is automatically added to Google Calendar

---

## Tech Stack

* **Backend:** FastAPI (Python)
* **Voice Agent:** Vapi
* **Calendar:** Google Calendar API
* **Deployment:** ngrok

---

## Calendar Integration Explanation

* Google Calendar API is enabled in Google Cloud Console
* A service account is used for authentication
* The calendar is shared with the service account
* The backend creates events only after user confirmation
* Events are created programmatically using FastAPI endpoints


Open Swagger UI:

```
http://localhost:8000/docs
```

---

## Project Structure

```
Voice-Scheduling-Agent/
├── backend/
│   ├── main.py
│   ├── requirements.txt
│   └── .env.example
├── agent/
│   └── agent_config.txt
├── screenshots/
│   └── calendar_event.png
├── .gitignore
└── README.md
```

---

## Screenshots / Proof

The `screenshots/` folder contains:

* API response screenshots
* Google Calendar event confirmation

These demonstrate successful meeting creation.

---

## Notes for Reviewers

* Dates and times are accepted in natural language
* Internal conversion is handled by the assistant
* Calendar API is only called after user confirmation

---

✅ **Assignment requirements fully met**

