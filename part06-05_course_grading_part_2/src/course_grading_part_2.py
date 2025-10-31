# write your solution here
if True:
    # this is never executed
    student_info = input("Student information: ")
    exercise_data = input("Exercises completed: ")
    exam_points = input("Exam points: ")
else:
    # hard-coded input
    student_info = "students1.csv"
    exercise_data = "exercises1.csv"
    exam_points = "exam_points1.csv"

with open(student_info) as student_file:
    db = {line.split(';')[0]: 
          {'full name': f'{line.split(';')[1]} {line.split(';')[2]}'}  
          for line in student_file.readlines()[1:] if line}
    
with open(exercise_data) as exercise_file:
    for line in exercise_file.readlines()[1:]:
        if line:
            id, exercises = line.split(';')[0], line.split(';')[1:]
            db[id]['ex'] = sum(list(map(lambda x: int(x), exercises)))

with open(exam_points) as exam_file:
    for line in exam_file.readlines()[1:]:
        if line:
            id, exams = line.split(';')[0], line.split(';')[1:]
            exe_point = int((100*db[id]['ex']/40)//10)
            point_sum = sum(list(map(lambda x: int(x), exams))) + exe_point
            grade = 0
            if point_sum <= 14:
                grade = 0
            elif point_sum <=17:
                grade = 1
            elif point_sum <=20:
                grade = 2
            elif point_sum <=23:
                grade = 3
            elif point_sum <=27:
                grade = 4
            else:
                grade = 5


            db[id]['grade'] = grade


            

for person in db:
    print(f'{db[person]['full name'].split('\n')[0]} {db[person]['grade']}')