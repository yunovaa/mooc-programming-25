# Write your solution here
import json

def read_json(filename):

    with open(filename) as file:
        data = file.read()
    return json.loads(data)

def print_persons(filename: str):
    people = read_json(filename)
    for person in people:
        print(f'{person['name']} {person['age']} years ({', '.join(person['hobbies'])})')