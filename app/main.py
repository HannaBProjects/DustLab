from pathlib import Path
from typing import Annotated

from fastapi import Depends, FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.database import Base, engine, get_db
from app.models import Measurement
from app.schemas import MeasurementResponse


Base.metadata.create_all(bind=engine)

app = FastAPI(title="DustLab")

templates = Jinja2Templates(
    directory=str(Path(__file__).parent / "templates")
)


def get_latest_measurement(db: Session):
    statement = (
        select(Measurement)
        .order_by(
            Measurement.measured_at.desc(),
            Measurement.id.desc(),
        )
        .limit(1)
    )
    return db.scalar(statement)


@app.get(
    "/api/measurements/latest",
    response_model=MeasurementResponse,
)
def latest_measurement(
    db: Annotated[Session, Depends(get_db)],
):
    measurement = get_latest_measurement(db)

    if measurement is None:
        raise HTTPException(
            status_code=404,
            detail="No measurements available",
        )

    return measurement


@app.get("/", response_class=HTMLResponse)
def dashboard(
    request: Request,
    db: Annotated[Session, Depends(get_db)],
):
    measurement = get_latest_measurement(db)

    return templates.TemplateResponse(
        request=request,
        name="dashboard.html",
        context={"measurement": measurement},
    )