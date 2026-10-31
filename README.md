
# DustLab

### Smart Indoor Air Quality Monitoring & Experiment Analysis

DustLab is an IoT project that monitors indoor air quality and analyses how everyday activities affect airborne particle concentrations.

The project focuses on helping people with household dust allergies and sensitivities better understand their indoor environment and compare methods of reducing airborne particles.

The system uses **Raspberry Pi 5**, environmental sensors, a web application, and an **SQLite database**.

## Key Features

- **Continuous Monitoring** — Collect and store indoor air-quality measurements, even when the dashboard is closed.
- **Web Dashboard** — Display current readings and historical graphs.
- **Air Quality Alerts** — Notify users of sustained increases in PM2.5 concentrations.
- **Manual Action Logging** — Record one action at a time, such as opening a window or turning on an air purifier, and display its timestamp alongside measurements.
- **Database Integration** — Store measurements, user actions, and alert records in SQLite.

## Scope Revision

The original DustLab concept included Monitoring Mode and Experiment Mode.
Following lecturer feedback, this submission will focus on Monitoring Mode.

Experiment Mode, including structured experiment stages, automated summaries,
and comparisons, is deferred as a potential future enhancement.
The original concept is retained in the project documentation.

## Technologies

**Hardware:** Raspberry Pi 5 · SCD41 · PMS7003

**Software:** Python · FastAPI · SQLite · HTML · CSS · JavaScript

## Documentation

| Section | Description |
|---|---|
| [Project Overview](docs/project-overview.md) | Problem statement, target users, aims and objectives |
| [Hardware](docs/hardware.md) | Components, sensors and wiring diagrams |
| [System Architecture](docs/system-architecture.md) | Software structure, data flow and database design |
| [Operating Modes & Use Cases](docs/operating-modes.md) | Monitoring Mode and the deferred Experiment Mode concept |
| [Experiments & Data Analysis](docs/experiments.md) | Original experiment methodology proposed for future development |

## Project Status: Design & Documentation

The project concept, proposed hardware wiring, system architecture, operating modes, and experiment methodology have been documented.

Physical assembly, software implementation, AWS deployment, and testing are planned as the next stages.

## Limitations

DustLab measures airborne particles but does not directly identify specific allergens.

The system is intended for environmental monitoring and educational research, not medical diagnosis or treatment.


