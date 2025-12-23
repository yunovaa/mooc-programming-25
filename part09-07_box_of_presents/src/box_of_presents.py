# WRITE YOUR SOLUTION HERE:
class Present:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def __str__(self):
        return f'{self.name} ({self.weight} kg)'
    
class Box:
    def __init__(self):
        self.box = []

    def add_present(self, present: Present):
        self.box.append(present)

    def total_weight(self):
        w = 0
        for present in self.box:
            w += present.weight
        return w