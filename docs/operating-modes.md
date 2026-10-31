
# Operating Modes & Use Cases

## Overview

DustLab helps users monitor indoor air quality and observe changes
in airborne particle concentrations following individual actions.

The original concept included two operating modes:

1. **Monitoring Mode** — Current Scope
2. **Experiment Mode** — Future Enhancement

This section describes the original proposal for Experiment Mode.
These features are outside the scope of the current submission
and are retained for potential future development.

Following lecturer feedback, only Monitoring Mode will be implemented
for this submission. The Experiment Mode description is retained below
to document the original concept.

The current system will use sensors connected to a Raspberry Pi 5.
Measurements will be transmitted to a cloud-hosted application and
displayed through a web dashboard.

## 1. Monitoring Mode

### Purpose

Monitoring Mode will continuously monitor indoor air quality, alert users to elevated particulate matter concentrations, and help them observe changes following their actions.

### Planned Features

- **Data Collection:** The Raspberry Pi 5 will collect PM1.0, PM2.5, PM10, CO₂, temperature, and humidity measurements from the PMS7003 and SCD41 sensors approximately every 30 seconds.
- **Data Transmission and Storage:** Measurements will be transmitted to the cloud application using MQTT and stored in a database, even when the dashboard is closed.
- **Web Dashboard:** Users will be able to view current measurements, historical data, and air quality trends.
- **Air Quality Alerts:** If PM2.5 remains above a configured threshold for a specified period, a buzzer will sound and a warning will appear on the dashboard in red.
- **Action Logging:** Users will be able to record actions such as opening a window, turning on an air purifier, closing a door, or taking no action. The system will store the selected action and its timestamp.

### Example Use Case: Responding to an Air Quality Alert

1. DustLab detects persistently elevated PM2.5 levels and activates the buzzer.
2. The user opens the web dashboard and sees an **Elevated PM2.5** warning, the current concentration, and recent measurements.
3. The dashboard asks **"What did you do?"** and offers four options:
   - **Opened the Window**
   - **Turned On the Air Purifier**
   - **Closed the Door**
   - **Nothing**
4. The user selects the option corresponding to their action. Any physical action is performed manually.
5. DustLab records the event and continues collecting measurements, allowing the user to observe how particulate concentrations change afterwards.

   
The mockup below illustrates how the DustLab dashboard may display an elevated PM2.5 warning and allow users to record their response.

![DustLab Monitoring Mode Alert](images/DustLab%20PM2.5%20Monitoring%20Dashboard.png)

*Figure 1. Proposed Monitoring Mode dashboard showing an elevated PM2.5 alert and user action options.*

### PM2.5 Recovery Comparison

DustLab will compare how quickly PM2.5 concentrations decrease using different methods, including natural decline, opening a window, and using a HEPA air purifier.

The example below compares the time required to reach a PM2.5 concentration of 15 µg/m³.

![PM2.5 Recovery Comparison](images/PM2.5%20Recovery%20Comparison%20Dashboard.png)

*Figure 2. Example comparison of PM2.5 reduction times using different interventions.*

**Note:** The values are illustrative. Actual results will depend on sensor measurements and experimental conditions.



### Limitations

DustLab measures airborne particulate matter concentrations but cannot identify specific allergens or pollution sources. Changes observed after a user action do not establish a direct cause-and-effect relationship.

More structured comparisons of air quality improvement methods will be supported by the separate **Experiment Mode**.


## 2. Experiment Mode

### Purpose

Experiment Mode will allow users to conduct structured experiments to investigate how everyday activities and different interventions affect indoor particulate matter concentrations.

Unlike Monitoring Mode, experiments will follow a defined process with baseline measurements, an activity or intervention, and a recovery period.

### Planned Features

- **Experiment Setup:** Users will select an experiment type, such as cleaning, cooking, opening a window, using an air purifier, or observing natural changes without intervention.
- **Baseline Measurements:** DustLab will record initial air quality conditions for approximately 10–15 minutes before the activity begins.
- **Activity Tracking:** Users will manually mark when an activity or intervention starts and ends.
- **Recovery Monitoring:** The system will continue collecting measurements after the activity to observe how particulate concentrations change.
- **Data Analysis:** DustLab will calculate baseline concentrations, peak PM levels, and changes over time, including recovery time when measurable.
- **Experiment Comparison:** Users will be able to compare results from different experiments using graphs and summary statistics.

### Experiment Workflow

1. The user selects an experiment type and enters any relevant notes.
2. DustLab records baseline air quality measurements.
3. The user starts the activity and marks its beginning in the dashboard.
4. DustLab continuously records sensor measurements during the activity.
5. The user marks the end of the activity.
6. The system continues monitoring the recovery period.
7. The user reviews the graphs and calculated results.

### Example Use Case: Comparing Ventilation Methods

A user wants to investigate whether opening a window or using an air purifier is associated with a faster reduction in PM2.5 concentration.

1. The user conducts an experiment using an open window and records the baseline, intervention, and recovery periods.
2. On another occasion, the user repeats the experiment using an air purifier under reasonably similar conditions.
3. DustLab stores the measurements from both experiments.
4. The user compares PM2.5 trends, initial concentrations, and the time taken for concentrations to decrease.
5. The user may repeat the experiments to identify more consistent patterns.

   The mockup below illustrates how the Experiment Mode dashboard may allow users to select an experiment type, review current PM values, and start a structured experiment.

![DustLab Experiment Mode Dashboard](images/DustLab%20Experiment%20Dashboard1.png)

*Figure 3. Proposed Experiment Mode dashboard showing experiment selection and PM readings.*

The mockup below shows an experiment in progress. DustLab continuously records PM2.5 measurements while the user tracks the experiment phases and marks the end of the cleaning activity.

![DustLab Experiment in Progress](images/DustLab%20Experiment%20Dashboard2.png)

*Figure 4. Proposed Experiment Mode dashboard showing experiment phases and real-time PM2.5 measurements.*

### Experiment Results and Comparison

DustLab will allow users to compare PM2.5 levels after different cleaning methods, including vacuuming, wet mopping, dusting, and no intervention. The graphs will show how particle concentrations change over time and how quickly they decrease.

![Cleaning Methods Comparison](images/Air%20Quality%20Cleaning%20Comparison%20Dashboard.png)

*Figure 5. Proposed dashboard for comparing PM2.5 levels across different cleaning methods.*

**Note:** All values and results shown are illustrative and do not represent actual measurements.


### Limitations

Experiment results may be influenced by outdoor air quality, ventilation conditions, room activities, and other uncontrolled factors.

DustLab will support comparisons of observed measurements but will not establish that a particular intervention directly caused an improvement in air quality.

Detailed experiment methodology and analysis metrics are described in [Experiments & Data Analysis](experiments.md).

