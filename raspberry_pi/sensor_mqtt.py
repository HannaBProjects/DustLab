
import getpass
import json
import asyncio
from time import monotonic

import paho.mqtt.client as mqtt
import serial

from read_sensor import read_pm25
from alert_logic import AlertLogic


# Configuration
SERIAL_PORT = "/dev/ttyAMA0"
BAUD_RATE = 9600

MQTT_BROKER = "dustlab.online"
MQTT_PORT = 8883
MQTT_TOPIC = "dustlab/pm25"
MQTT_USERNAME = "dustlab_pi"

SEND_INTERVAL = 30


def on_connect(client, userdata, flags, reason_code, properties):
    if reason_code == 0:
        print("Connected to MQTT broker")
    else:
        print(f"MQTT connection failed: {reason_code}")

async def buzzer_worker(buzzer, alert_event):
    try:
        while True:
            # Wait until the alert becomes active
            await alert_event.wait()

            while alert_event.is_set():
                buzzer.on()
                await asyncio.sleep(0.2)

                buzzer.off()
                await asyncio.sleep(0.8)

    finally:
        buzzer.off()

async def monitor_sensor_timeout(alert, alert_event):
    while True:
        alert_active = alert.check_missing(monotonic())

        if not alert_active:
            alert_event.clear()

        await asyncio.sleep(1)

async def publish_pm25(client, pm25):
    if not client.is_connected():
        print("MQTT is disconnected; reading was not sent")
        return

    message = json.dumps({
        "pm25": pm25,
        "source": "sensor",
    })

    result = client.publish(
        MQTT_TOPIC,
        message,
        qos=1,
    )

    if result.rc != mqtt.MQTT_ERR_SUCCESS:
        print("Could not publish measurement")
        return

    try:
        await asyncio.to_thread(
            result.wait_for_publish, timeout=10
        )
    except (RuntimeError, ValueError) as error:
        print(f"MQTT publish error: {error}")
        return

    if result.is_published():
        print(f"Sent PM2.5: {pm25} µg/m³")
    else:
        print("Message was not acknowledged")

async def main():
    password = getpass.getpass("MQTT password: ")
    alert = AlertLogic()
    alert_event = asyncio.Event()

    client = mqtt.Client(
        mqtt.CallbackAPIVersion.VERSION2
    )

    client.on_connect = on_connect
    client.username_pw_set(MQTT_USERNAME, password)
    client.tls_set()

    client.connect_async(MQTT_BROKER, MQTT_PORT, 60)
    client.loop_start()

    timeout_task = None

    try:

        timeout_task = asyncio.create_task(
            monitor_sensor_timeout(alert, alert_event)
        )

        with serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=5) as sensor:
            print("Reading PMS7003. Press Ctrl+C to stop.")

            while True:
                pm25 = await asyncio.to_thread(read_pm25, sensor)

                if pm25 is not None:
                    alert_active = alert.update(pm25, monotonic())
                    print(f"Alert active: {alert_active}")

                    if alert_active:
                        alert_event.set()
                    else:
                        alert_event.clear()

                    await publish_pm25(client, pm25)

                    await asyncio.sleep(SEND_INTERVAL)

    except KeyboardInterrupt:
        print("\nStopping sensor program")
    finally:
        if timeout_task is not None:
            timeout_task.cancel()

            try:
                await timeout_task
            except asyncio.CancelledError:
                pass

        client.disconnect()
        client.loop_stop()


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nStopping sensor program")
