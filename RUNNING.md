# Run the local prototype

Run these commands in PowerShell from the project folder (Python 3.10+):

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m uvicorn app.main:app --reload --host 127.0.0.1
```

Open http://127.0.0.1:8000 in your browser. Press Ctrl+C in the terminal to stop.
Activation of the virtual environment is not required with these commands.

The dashboard renders fixed, labelled test values for PM2.5.
There is no sensor connection, background simulator, database, MQTT integration,
or authentication yet. This initial prototype runs locally only.

- `app/main.py`: FastAPI application and dashboard route.
- `app/templates/dashboard.html`: HTML template and page styling.
- `requirements.txt`: application dependencies.
