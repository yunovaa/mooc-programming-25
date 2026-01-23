from functools import reduce

class CourseAttempt:
    def __init__(self, course_name: str, grade: int, credits: int):
        self.course_name = course_name
        self.grade = grade
        self.credits = credits

    def __str__(self):
        return f"{self.course_name} ({self.credits} cr) grade {self.grade}"

# Write your solution
def sum_of_all_credits(attempts: list):
    return reduce(lambda sum, item: sum+item.credits, attempts, 0)

def sum_of_passed_credits(att: list):
    return reduce(lambda sum, item: sum+item.credits, filter(lambda t: t.grade>=1, att), 0)

def average(att: list):
    l = list(filter(lambda t: t.grade>=1, att))
    return reduce(lambda sum, item: sum+item.grade/len(l), l, 0)


