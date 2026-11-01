import argparse
import math

from app.database import Base, engine, SessionLocal
from app.models import Measurement


def main():
    parser = argparse.ArgumentParser(
        description="Add one simulated PM2.5 measurement"
    )
    parser.add_argument(
        "pm25",
        type=float,
        help="PM2.5 concentration in micrograms/m³",
    )
    args = parser.parse_args()

    if not math.isfinite(args.pm25) or args.pm25 < 0:
        parser.error("PM2.5 must be a finite, non-negative number")

    Base.metadata.create_all(bind=engine)

    with SessionLocal() as db:
        measurement = Measurement(
            pm25=args.pm25,
            source="simulated",
        )

        db.add(measurement)
        db.commit()
        db.refresh(measurement)

        print(
            f"Saved simulated measurement #{measurement.id}: "
            f"PM2.5 = {measurement.pm25}"
        )


if __name__ == "__main__":
    main()