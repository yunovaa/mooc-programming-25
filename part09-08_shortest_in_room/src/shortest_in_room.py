# WRITE YOUR SOLUTION HERE:
class Person:
    def __init__(self, name: str, height: int):
        self.name = name
        self.height = height

    def __str__(self):
        return self.name


class Room:
    def __init__(self):
        self.persons = []

    def add(self, person: Person):
        self.persons.append(person)

    def is_empty(self):
        return False if len(self.persons)>0 else True
    
    def print_contents(self):
        print(f'There are {len(self.persons)} persons in the room, and their combined height is {sum([w.height for w in self.persons])} cm')
        for person in self.persons:
            print(f'{person.name} ({person.height} cm)')

    def shortest(self):
        if self.is_empty():
            return None
        else:
            sh = 1000
            sh_person = ''
            for person in self.persons:
                if person.height<sh:
                    sh = person.height
                    sh_person = person

            return sh_person
        
    def remove_shortest(self):
        shortest = self.shortest()
        if not self.is_empty():
            self.persons.remove(shortest)
        return shortest


