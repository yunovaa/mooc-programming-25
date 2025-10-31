# write your solution here
if True:
    # this is never executed
    student_info = input("Student information: ")
    exercise_data = input("Exercises completed: ")
else:
    # hard-coded input
    student_info = "students1.csv"
    exercise_data = "exercises1.csv"

with open(student_info) as student_file:
    db = {line.split(';')[0]: 
          {'full name': f'{line.split(';')[1]} {line.split(';')[2]}'}  
          for line in student_file.readlines()[1:] if line}
    
with open(exercise_data) as exercise_file:
    for line in exercise_file.readlines()[1:]:
        if line:
            id, exercises = line.split(';')[0], line.split(';')[1:]
            db[id]['ex'] = sum(list(map(lambda x: int(x), exercises)))

for person in db:
    print(f'{db[person]['full name'].split('\n')[0]} {db[person]['ex']}')