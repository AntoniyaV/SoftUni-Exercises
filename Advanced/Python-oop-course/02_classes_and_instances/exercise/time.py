class Time:
    max_hours = 23
    max_minutes = 59
    max_seconds = 59

    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def set_time(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def get_time(self):
        return f"{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}"

    def next_second(self):
        new_second = self.seconds + 1
        if new_second > Time.max_seconds:
            new_minute = self.minutes + 1
            if new_minute > Time.max_minutes:
                new_hour = self.hours + 1
                if new_hour > Time.max_hours:
                    self.hours = 0
                    self.minutes = 0
                    self.seconds = 0
                else:
                    self.hours += 1
                    self.minutes = 0
                    self.seconds = 0
            else:
                self.minutes += 1
                self.seconds = 0
        else:
            self.seconds += 1

        return Time.get_time(self)


# Test code
time = Time(9, 30, 59)
print(time.next_second())

time = Time(10, 59, 59)
print(time.next_second())

time = Time(23, 59, 59)
print(time.next_second())
