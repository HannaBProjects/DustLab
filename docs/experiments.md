
# Experiments & Data Analysis — Future Enhancement

## Scope Status

This document preserves the original methodology proposed for
Experiment Mode. Following lecturer feedback, this mode has been
deferred and is outside the scope of the current submission.

The workflows and automated calculations described below are
proposed future features, not functionality of the Monitoring Mode MVP.

The current implementation will allow users to record one action
at a time and observe measurements on historical graphs. It will
not manage experiment stages, calculate recovery times, or
automatically compare interventions.

## Experiment Methodology

The proposed Experiment Mode would use a consistent procedure to investigate changes in indoor particulate matter concentrations.

Each experiment will include three stages:Each experiment in the proposed future mode would include three stages:

1. **Baseline:** Record initial air quality measurements for approximately 10–15 minutes.
2. **Activity:** Record measurements while the user performs an activity, such as vacuuming, wet mopping, or opening a window.
3. **Recovery:** Continue recording after the activity to observe how particle concentrations change.

In the proposed Experiment Mode, the user would manually mark the start and end of each activity.

## Analysis Metrics

The proposed Experiment Mode would calculate:

- **Baseline PM2.5:** Average concentration before the activity.
- **Peak PM2.5:** Highest recorded concentration during the experiment.
- **Concentration Change:** Difference between the baseline and subsequent measurements.
- **Recovery Time:** Time required for PM2.5 to return to a defined reference level, if reached.

## Comparing Experiments

In a future version, users could compare different cleaning methods, ventilation, air purification, and natural particle decline without intervention.

For meaningful comparisons, experiments should be repeated under reasonably similar conditions, including room location, experiment duration, and initial air quality.

Results could be presented through graphs and summary statistics, as illustrated in [Operating Modes & Use Cases](operating-modes.md).

## Limitations

Outdoor air quality, ventilation, human activity, and other environmental factors may influence the measurements.

The proposed analysis would identify observed trends and differences between experiments but would not establish direct causation.

All values shown in the proposed dashboard mockups are illustrative rather than actual experimental results.
