# WRITE YOUR SOLUTION HERE:
class Employee:
    def __init__(self, name: str):
        self.name = name
        self.subordinates = []

    def add_subordinate(self, employee: 'Employee'):
        self.subordinates.append(employee)


def count_subordinates(employee: Employee):
    c = 0
    for i in range(len(employee.subordinates)):
        c+=count_subordinates(employee.subordinates[i])+1

    return c

