# WRITE YOUR SOLUTION HERE:
class LotteryNumbers:
    def __init__(self, weekNumber, list):
        self.weeknumber = weekNumber
        self.list = list

    def number_of_hits(self, numbers: list):
        return len([count for count in numbers if count in self.list])
    
    def hits_in_place(self, numbers):
        return [number if number in self.list else -1 for number in numbers]