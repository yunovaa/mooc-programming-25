import string

class ClimbingRoute:
    def __init__(self, name: str, length: int, grade: str):
        self.name = name
        self.length = length
        self.grade = grade

    def __str__(self):
        return f"{self.name}, length {self.length} metres, grade {self.grade}"

# Write your solution herer:
def sort_by_length(routes: list):
    def order_by_length(route:ClimbingRoute):
        return route.length
    return sorted(routes, key=order_by_length, reverse=True)

def sort_by_difficulty(routes: list):

    def order_by_difficulty(route:ClimbingRoute):
        grade = route.grade
        plus = 1 if '+' in grade else 0
        letter = grade[1] if len(grade)>1 and grade[1] in string.ascii_uppercase else 'Z'
        number = int(grade[0])
        return (number, letter, plus, route.length)
    
    return sorted(routes, key=order_by_difficulty, reverse=True)