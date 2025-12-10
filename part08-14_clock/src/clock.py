# Write your solution here:
class Clock:
    def __init__(self, hour, min, sec):
        self.seconds = sec
        self.minutes = min
        self.hours = hour

    def tick(self):
        if self.seconds != 59:
            self.seconds += 1
        else:
            self.seconds = 0
            if self.minutes != 59:
                self.minutes += 1
            else:
                self.minutes = 0
                if self.hours != 23:
                    self.hours += 1
                else:
                    self.hours = 0
        
    def set(self, hour, min):
        self.hours = hour
        self.minutes = min
        self.seconds = 0

    def __str__(self):
        return f'{self.hours:0>2}:{self.minutes:0>2}:{self.seconds:0>2}'

