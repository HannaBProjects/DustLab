from datetime import UTC, datetime

from sqlalchemy import CheckConstraint, DateTime, Float, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base


class Measurement(Base):
    __tablename__ = "measurements"

    __table_args__ = (
        CheckConstraint("pm25 >= 0", name="check_pm25_non_negative"),
        CheckConstraint(
            "source IN ('simulated', 'sensor')",
            name="check_measurement_source",
        ),
    )

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
    )

    pm25: Mapped[float] = mapped_column(
        Float,
        nullable=False,
    )

    measured_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=lambda: datetime.now(UTC).replace(tzinfo=None),
        nullable=False,
    )

    source: Mapped[str] = mapped_column(
        String(20),
        nullable=False,
    )