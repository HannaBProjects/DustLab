
import json
import math
import os

import paho.mqtt.client as mqtt

from app.database import Base, SessionLocal, engine
from app.models import Measurement


TOPIC = "dustlab/pm25"


def on_connect(client, userdata, flags, reason_code, properties):
    if reason_code == 0:
        client.subscribe(TOPIC)
        print(f"Subscribed to {TOPIC}", flush=True)
    else:
        print(f"MQTT connection failed: {reason_code}", flush=True)


def on_message(client, userdata, message):
    try:
        data = json.loads(message.payload.decode("utf-8"))
        value = data["pm25"]
        source = data.get("source", "simulated")

        if source not in ("simulated", "sensor"):
            raise ValueError("Invalid measurement source")

        if isinstance(value, bool):
            raise ValueError("PM2.5 must be a number")

        pm25 = float(value)

        if not math.isfinite(pm25) or pm25 < 0:
            raise ValueError("Invalid PM2.5 value")

    except (ValueError, TypeError, KeyError) as error:
        print(f"Ignored message: {error}", flush=True)
        return

    with SessionLocal() as db:
        db.add(Measurement(pm25=pm25, source=source))
        db.commit()

    print(f"Saved MQTT PM2.5: {pm25}", flush=True)


def main():
    Base.metadata.create_all(bind=engine)

    client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
    client.username_pw_set(
        os.environ["MQTT_USERNAME"],
        os.environ["MQTT_PASSWORD"],
    )

    client.on_connect = on_connect
    client.on_message = on_message

    client.connect(os.getenv("MQTT_HOST", "mosquitto"), 1883, 60)
    client.loop_forever()


if __name__ == "__main__":
    main()
