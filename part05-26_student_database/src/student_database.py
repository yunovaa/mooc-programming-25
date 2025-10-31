# Write your solution here
def add_student(database, name):
    database[name] = []

def print_student(database, name):
    value = database.get(name, 'no such person in the database')
    if not value:
        print(f'{name}:')
        print(' no completed courses')
    elif value == 'no such person in the database':
        print(f"{name}: {value}")
    else:
        print(f'{name}:')
        print(f' {len(value)} completed courses:')
        grade = 0
        for course in value:
            print(f'  {course[0]} {course[1]}')
            grade+=course[1]
        print(f' average grade {grade/len(value)}')

def add_course(database, name, course_grade):
    dct = {course[0]: course[1] for course in database[name]}
    value = dct.get(course_grade[0])
    if (value and course_grade[1]>value):
        ind = list(dct.keys()).index(course_grade[0])
        database[name][ind] = course_grade
    elif not value and course_grade[1] != 0:
        database[name].append(course_grade)


def summary(database):
    print(f'students {len(database)}')
    mx = 0
    c = 0
    n_c = ''
    n_mx = ''
    for student, value in database.items():
        name = student
        temp1 = max(mx, sum([grade[1] for grade in value])/len(value))
        if mx != temp1:
            n_mx = name
            mx = temp1        
        
        temp2 = max(c, len(value))
        if c != temp2:
            n_c = name
            c = temp2 
    
    print(f'most courses completed {c} {n_c}')
    print(f'best average grade {mx} {n_mx}')



if __name__ == '__main__':
    students = {}
    add_student(students, "Peter")
    add_course(students, "Peter", ("Software Development Methods", 1))
    add_course(students, "Peter", ("Software Development Methods", 5))
    print_student(students, "Peter")