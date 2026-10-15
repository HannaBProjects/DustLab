
# DustLab

### Smart Indoor Air Quality Monitoring & Experiment Analysis

DustLab is an IoT project that monitors indoor air quality and analyses how everyday activities affect airborne particle concentrations.

The project focuses on helping people with household dust allergies and sensitivities better understand their indoor environment and compare methods of reducing airborne particles.

The system uses **Raspberry Pi 5**, environmental sensors, a web application, and an **SQLite database**.

## Key Features

- **Monitoring Mode** — Continuous air quality monitoring, real-time readings, historical graphs, and pollution alerts.
- **Experiment Mode** — Record activities such as cleaning, cooking, opening windows, or using an air purifier.
- **Data Analysis** — Compare experiments, visualise pollution trends, and evaluate particle reduction times.
- **Database Integration** — Store measurements, user actions, alerts, and experiment results.

## Technologies

**Hardware:** Raspberry Pi 5 · SCD41 · PMS7003

**Software:** Python · FastAPI · SQLite · HTML · CSS · JavaScript

## Documentation

| Section | Description |
|---|---|
| [Project Overview](docs/project-overview.md) | Problem statement, target users, aims and objectives |
| [Hardware](docs/hardware.md) | Components, sensors and wiring diagrams |
| [System Architecture](docs/system-architecture.md) | Software structure, data flow and database design |
| [Operating Modes & Use Cases](docs/operating-modes.md) | Monitoring Mode, Experiment Mode and user interactions |
| [Experiments & Data Analysis](docs/experiments.md) | Experiment procedures, graphs and comparison methods |

## Project Status

**Planning & Early Development**

Hardware selection and initial wiring diagrams are in progress. Software implementation and testing will follow.

## Limitations

DustLab measures airborne particles but does not directly identify specific allergens.

The system is intended for environmental monitoring and educational research, not medical diagnosis or treatment.


