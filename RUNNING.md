# Run the local prototype

Run these commands in PowerShell from the project folder (Python 3.10+):

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m uvicorn app.main:app --reload --host 127.0.0.1
```

Open http://127.0.0.1:8000 in your browser. Press Ctrl+C in the terminal to stop.
Activation of the virtual environment is not required with these commands.

The dashboard reads the latest PM2.5 measurement from SQLite. Initially it
shows "No measurements available". In another terminal, insert a test reading:

```powershell
.\.venv\Scripts\python.exe -m app.add_sample 12.0
```

Refresh the page to see the saved value, its UTC timestamp, and its simulated
source. Each command inserts one new record; page visits never create records.
Data persists in `data/dustlab_orm.sqlite3`, which is excluded from Git.

`GET /api/measurements/latest` returns the latest measurement as JSON, or HTTP
404 when the database is empty. Interactive API documentation is at `/docs`.

There is no MQTT integration or authentication yet. This prototype runs locally only.

- `app/main.py`: FastAPI application and dashboard route.
- `app/database.py`: SQLite storage.
- `app/add_sample.py`: command for adding a simulated measurement.
- `app/templates/dashboard.html`: HTML template and page styling.
- `requirements.txt`: application dependencies.
