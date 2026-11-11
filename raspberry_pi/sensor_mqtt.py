
import getpass
import json
import time
from threading import Event

import paho.mqtt.client as mqtt
import serial

from read_sensor import read_pm25


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
        userdata.set()
    else:
        print(f"MQTT connection failed: {reason_code}")


def main():
    password = getpass.getpass("MQTT password: ")
    connected = Event()

    client = mqtt.Client(
        mqtt.CallbackAPIVersion.VERSION2,
        userdata=connected,
    )
    client.on_connect = on_connect
    client.username_pw_set(MQTT_USERNAME, password)
    client.tls_set()

    client.connect(MQTT_BROKER, MQTT_PORT, 60)
    client.loop_start()

    try:
        if not connected.wait(timeout=10):
            print("Could not connect to MQTT broker")
            return

        with serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=5) as sensor:
            print("Reading PMS7003. Press Ctrl+C to stop.")

            while True:
                pm25 = read_pm25(sensor)

                if pm25 is not None:
                    message = json.dumps({
                        "pm25": pm25,
                        "source": "sensor",
                    })

                    result = client.publish(
                        MQTT_TOPIC,
                        message,
                        qos=1,
                    )
                    result.wait_for_publish(timeout=10)

                    if result.is_published():
                        print(f"Sent PM2.5: {pm25} µg/m³")
                    else:
                        print("Message was not acknowledged")

                    time.sleep(SEND_INTERVAL)

    except KeyboardInterrupt:
        print("\nStopping sensor program")
    finally:
        client.disconnect()
        client.loop_stop()


if __name__ == "__main__":
    main()
