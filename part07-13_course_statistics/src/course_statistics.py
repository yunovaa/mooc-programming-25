# Write your solution here
import urllib.request
import json
import math
def retrieve_all():
    address = "https://studies.cs.helsinki.fi/stats-mock/api/courses"
    my_request = urllib.request.urlopen(address)
    json_format = json.load(my_request)
    l = []
    for course in json_format:
        if course['enabled'] == True:
            l.append((course['fullName'], course['name'], course['year'], 
                      sum(course['exercises'])))
    return l

def retrieve_course(course_name: str):
    address = f'https://studies.cs.helsinki.fi/stats-mock/api/courses/{course_name}/stats'
    my_request = urllib.request.urlopen(address)
    json_format = json.load(my_request)
    d = {}
    weeks = 0 
    student = 0
    hours = 0
    exercises = 0
    for number in json_format:
        week = json_format[number]
        weeks+=1
        student = max(student, week['students'])
        hours += week['hour_total']
        exercises += week['exercise_total']

    d['weeks'] = weeks
    d['students'] = student
    d['hours'] = hours
    d['hours_average'] = math.floor(hours/student)
    d['exercises'] = exercises
    d['exercises_average'] = math.floor(exercises/student)

    return d

