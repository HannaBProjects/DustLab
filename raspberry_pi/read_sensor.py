
import serial


# Configuration
SERIAL_PORT = "/dev/ttyAMA0"
BAUD_RATE = 9600


def read_pm25(sensor):
    # Find the start of a PMS7003 packet
    if sensor.read(1) != b"\x42":
        return None

    if sensor.read(1) != b"\x4d":
        return None

    frame = b"\x42\x4d" + sensor.read(30)

    if len(frame) != 32:
        return None

    frame_length = int.from_bytes(frame[2:4], "big")
    if frame_length != 28:
        return None

    # Check that the packet was received correctly
    expected_checksum = int.from_bytes(frame[30:32], "big")
    if sum(frame[:30]) != expected_checksum:
        return None

    # Read atmospheric PM2.5, in µg/m³
    return int.from_bytes(frame[12:14], "big")


def main():
    with serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=5) as sensor:
        print("Reading PMS7003. Press Ctrl+C to stop.")

        while True:
            pm25 = read_pm25(sensor)

            if pm25 is not None:
                print(f"PM2.5: {pm25} µg/m³")


if __name__ == "__main__":
    main()
