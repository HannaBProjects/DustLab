"""Local DustLab prototype using fixed demonstration readings."""

from pathlib import Path

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI(title="DustLab")
templates = Jinja2Templates(directory=str(Path(__file__).parent / "templates"))


@app.get("/", response_class=HTMLResponse)
def dashboard(request: Request):
    readings = [
        {"name": "PM2.5", "value": 12.0},
    ]
    return templates.TemplateResponse(
        request=request,
        name="dashboard.html",
        context={"readings": readings},
    )
