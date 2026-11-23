import math

class AlertLogic:
    def __init__(self, threshold=15.0, delay_seconds=120):
        self.threshold = threshold
        self.delay_seconds = delay_seconds

        self.above_since = None
        self.active = False
        self.last_reading_time = None

    def set_threshold(self, new_threshold):
        if (
            isinstance(new_threshold, bool)
            or not isinstance(new_threshold, (int, float))
            or not math.isfinite(new_threshold)
            or new_threshold < 0
        ):
            raise ValueError("Threshold must be a finite, non-negative number")

        if new_threshold != self.threshold:
            self.threshold = float(new_threshold)
            self.above_since = None
            self.active = False

    def update(self, pm25, current_time):
        self.check_missing(current_time)
        self.last_reading_time = current_time

        if pm25 <= self.threshold:
            self.above_since = None
            self.active = False
            return self.active

        if self.above_since is None:
            self.above_since = current_time

        elapsed = current_time - self.above_since

        if elapsed >= self.delay_seconds:
            self.active = True

        return self.active

    def check_missing(self, current_time):
        if (
            self.last_reading_time is None
            or current_time - self.last_reading_time > 60
        ):
            self.above_since = None
            self.active = False

        return self.active