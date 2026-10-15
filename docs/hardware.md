
# Hardware

## Hardware Overview

DustLab uses a Raspberry Pi 5 and environmental sensors to collect real-time indoor air quality measurements.

The hardware is designed to monitor airborne particulate matter, CO₂ concentration, temperature, and humidity.

## Hardware Components

| Component | Purpose | Interface | Status |
|---|---|---|---|
| Raspberry Pi 5 | Main processing unit | GPIO | Available |
| Adafruit SCD41 | CO₂, temperature, humidity | I²C | Available |
| Plantower PMS7003 | PM1.0, PM2.5, PM10 | UART | Planned |
| RGB LED | Visual air quality indication | GPIO | Optional |
| Buzzer | Audible notifications | GPIO | Available |

## Sensor Connections

### SCD41 — CO₂, Temperature and Humidity

The SCD41 communicates with the Raspberry Pi using the I²C protocol.

| SCD41 | Raspberry Pi 5 |
|---|---|
| VIN | Pin 1 — 3.3V |
| GND | Pin 6 — GND |
| SDA | Pin 3 — GPIO2 |
| SCL | Pin 5 — GPIO3 |
| 3Vo | Not connected |

### PMS7003 — Particulate Matter Sensor

The PMS7003 uses UART communication to transmit particulate matter measurements.

Planned connections using a compatible adapter:

| PMS7003 | Raspberry Pi 5 |
|---|---|
| VCC | Pin 4 — 5V |
| GND | Pin 9 — GND |
| TX | Pin 10 — GPIO15 (RX) |
| RX | Pin 8 — GPIO14 (TX) |

The final wiring will be verified against the purchased sensor and adapter documentation before physical connection.

## Wiring Diagram

The wiring diagram is being developed using Fritzing.

A Raspberry Pi 4B model is temporarily used to represent the Raspberry Pi 5 because the required 40-pin GPIO connections are compatible.

The final verified wiring diagram will be added here.

## Hardware Safety

- Raspberry Pi GPIO pins use 3.3V logic.
- Sensor power requirements must be verified.
- GPIO pins must not receive 5V signals.
- All physical connections must be checked before powering the system.
